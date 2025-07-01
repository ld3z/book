const fs = require('fs');
const path = require('path');

// Create theme directory if it doesn't exist
const themeDir = path.join(__dirname, 'theme');
if (!fs.existsSync(themeDir)) {
  fs.mkdirSync(themeDir, { recursive: true });
}

// Copy Tippy.js files
const tippySource = path.join(__dirname, 'node_modules', 'tippy.js');
const tippyDest = path.join(themeDir, 'tippy');

if (!fs.existsSync(tippyDest)) {
  fs.mkdirSync(tippyDest, { recursive: true });
}

fs.copyFileSync(
  path.join(tippySource, 'dist', 'tippy-bundle.umd.min.js'),
  path.join(tippyDest, 'tippy-bundle.umd.min.js')
);

fs.copyFileSync(
  path.join(tippySource, 'dist', 'tippy.css'),
  path.join(tippyDest, 'tippy.css')
);

// Copy Popper.js files
const popperSource = path.join(__dirname, 'node_modules', '@popperjs', 'core', 'dist', 'umd');
const popperDest = path.join(themeDir, 'popper');

if (!fs.existsSync(popperDest)) {
  fs.mkdirSync(popperDest, { recursive: true });
}

fs.copyFileSync(
  path.join(popperSource, 'popper.min.js'),
  path.join(popperDest, 'popper.min.js')
);

console.log('Dependencies copied to theme directory');
