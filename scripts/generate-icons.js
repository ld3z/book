const fs = require('fs');
const path = require('path');
const { locate } = require('@iconify/json');

// Configuration
const CONTENT_DIR = path.join(__dirname, '../content');
const OUTPUT_FILE = path.join(__dirname, '../sass/_iconify-icons.scss');

// Regex to find icon shortcodes: {{ icon(name="prefix:icon-name") }} or {{ icon(name='prefix:icon-name') }}
const ICON_REGEX = /\{\{\s*icon\s*\(\s*name\s*=\s*["']([^"']+)["']\s*\)\s*\}\}/g;

function getAllFiles(dirPath, arrayOfFiles) {
    const files = fs.readdirSync(dirPath);

    arrayOfFiles = arrayOfFiles || [];

    files.forEach(function (file) {
        if (fs.statSync(dirPath + "/" + file).isDirectory()) {
            arrayOfFiles = getAllFiles(dirPath + "/" + file, arrayOfFiles);
        } else {
            if (file.endsWith('.md')) {
                arrayOfFiles.push(path.join(dirPath, "/", file));
            }
        }
    });

    return arrayOfFiles;
}

function getIconData(iconName) {
    const [prefix, name] = iconName.split(':');
    if (!prefix || !name) {
        console.warn(`Invalid icon format: ${iconName}. Expected format: prefix:name`);
        return null;
    }

    try {
        const filename = locate(prefix);
        if (!filename) {
            console.warn(`Icon set not found for prefix: ${prefix}`);
            return null;
        }
        const iconSet = JSON.parse(fs.readFileSync(filename, 'utf8'));

        // Check for the icon in the set
        if (!iconSet.icons[name]) {
            // Try aliase
            if (iconSet.aliases && iconSet.aliases[name]) {
                const alias = iconSet.aliases[name];
                if (iconSet.icons[alias.parent]) {
                    return { ...iconSet.icons[alias.parent], ...alias };
                }
            }
            console.warn(`Icon not found: ${iconName}`);
            return null;
        }

        const iconData = iconSet.icons[name];

        // Merge with set defaults
        const result = {
            body: iconData.body,
            width: iconData.width || iconSet.width || 16,
            height: iconData.height || iconSet.height || 16
        };

        return result;
    } catch (err) {
        console.error(`Error loading icon set for ${prefix}:`, err.message);
        return null;
    }
}

function svgToDataUri(body, width, height) {
    // Basic SVG construction
    const svg = `<svg xmlns='http://www.w3.org/2000/svg' width='${width || 16}' height='${height || 16}' viewBox='0 0 ${width || 16} ${height || 16}'>${body}</svg>`;

    // Simple URI encoding
    // We can use a simpler encoder than encodeURIComponent for SVG data URIs to keep them smaller
    // but encodeURIComponent is safer and standard node env doesn't have a mini-svg-data-uri equivalent.

    // Using a minimal replace similar to what zola/sass might expect if we want to be safe with quotes
    // But since we are putting it in a url("..."), we need to escape " and % and others.

    // Let's use standard URI encoding but decode some common chars to keep it readable if desired,
    // though purely standard encoding is safest.
    const encoded = encodeURIComponent(svg)
        .replace(/'/g, '%27')
        .replace(/"/g, '%22');

    return `url("data:image/svg+xml;charset=utf-8,${encoded}")`;
}

function main() {
    console.log('Scanning for icons...');

    if (!fs.existsSync(CONTENT_DIR)) {
        console.error(`Content directory not found: ${CONTENT_DIR}`);
        return;
    }

    const files = getAllFiles(CONTENT_DIR);
    const foundIcons = new Set();

    files.forEach(file => {
        const content = fs.readFileSync(file, 'utf8');
        let match;
        while ((match = ICON_REGEX.exec(content)) !== null) {
            foundIcons.add(match[1]);
        }
    });

    console.log(`Found ${foundIcons.size} unique icons.`);

    let scssContent = ':root {\n';

    // Sort for deterministic output
    const sortedIcons = Array.from(foundIcons).sort();

    for (const iconName of sortedIcons) {
        const data = getIconData(iconName);
        if (data) {
            const cssVarName = `--icon-${iconName.replace(/:/g, '-')}`;
            const width = data.width || 16; // Default standard sizing if missing, though usually packed in viewbox or body
            const height = data.height || 16;
            const body = data.body;

            scssContent += `\t${cssVarName}: ${svgToDataUri(body, width, height)};\n`;
        }
    }

    scssContent += '}\n';

    // Ensure directory exists
    const outputDir = path.dirname(OUTPUT_FILE);
    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }

    fs.writeFileSync(OUTPUT_FILE, scssContent);
    console.log(`Generated SCSS to ${OUTPUT_FILE}`);
}

main();
