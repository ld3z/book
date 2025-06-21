import sys
import json
import re
import os
import base64

# Path to the local iconify json files
# Assumes the script is run from the book's root directory
ICON_ROOT = "node_modules/@iconify/json/json"

def get_available_collections():
    """Get a set of available icon collections from the json files."""
    if not os.path.exists(ICON_ROOT):
        return set()
    return {f[:-5] for f in os.listdir(ICON_ROOT) if f.endswith('.json')}

def replace_icons(content):
    # Get available collections once for better performance
    available_collections = get_available_collections()
    
    # Create a mapping of collection names to their preferred format
    collection_map = {}
    for col in available_collections:
        # Map both the full name and any common variations
        collection_map[col] = col
        if col.endswith('-icons'):
            collection_map[col.replace('-icons', '')] = col
        if col.endswith('-icon'):
            collection_map[col.replace('-icon', '')] = col
    
    # Regex to find icon patterns
    icon_pattern = re.compile(r':([a-z0-9-]+-[a-z0-9-]+):')
    
    def process_icon(match):
        full_ref = match.group(1)
        parts = full_ref.split('-')
        collection = None
        icon_name = None
        
        # Try to find the best matching collection
        for i in range(min(4, len(parts)-1), 0, -1):
            potential_collection = '-'.join(parts[:i])
            
            # Check if we have a direct match or a mapped version
            if potential_collection in collection_map:
                collection = collection_map[potential_collection]
                icon_name = '-'.join(parts[i:])
                break
        
        # If no match found, try common variations
        if not collection:
            for i in range(1, min(4, len(parts))):
                potential = '-'.join(parts[:i])
                for suffix in ['', 's', '-icon', '-icons']:
                    if f"{potential}{suffix}" in collection_map:
                        collection = collection_map[f"{potential}{suffix}"]
                        icon_name = '-'.join(parts[i:])
                        break
                if collection:
                    break
        
        if not collection:
            sys.stderr.write(f"Warning: Could not resolve icon reference: {full_ref}\n")
            return match.group(0)
            
        # Now process the icon
        json_path = os.path.join(ICON_ROOT, f"{collection}.json")

        if not os.path.exists(json_path):
            sys.stderr.write(f"Warning: Icon collection '{collection}' not found.\n")
            return match.group(0)


        with open(json_path, 'r', encoding='utf-8') as f:
            icon_data = json.load(f)
        
        if icon_name not in icon_data.get('icons', {}):
            sys.stderr.write(f"Warning: Icon '{icon_name}' not found in collection '{collection}'.\n")
            return match.group(0)

        svg_body = icon_data['icons'][icon_name]['body']
        width = icon_data.get("width", 24)
        height = icon_data.get("height", 24)
        
        # Check if the icon has a palette (i.e., it's colored)
        has_palette = icon_data.get('info', {}).get('palette', False)

        # Construct the full SVG tag
        full_svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="1em" height="1em" '
            f'preserveAspectRatio="xMidYMid meet" '
            f'viewBox="0 0 {width} {height}">{svg_body}</svg>'
        )
        
        encoded_svg = base64.b64encode(full_svg.encode('utf-8')).decode('utf-8')
        icon_url = f"data:image/svg+xml;base64,{encoded_svg}"

        # Use a different class for colored icons
        if has_palette:
            return f'<span class="icon-colored" style="--icon-url: url(\'{icon_url}\');"></span>'
        else:
            return f'<span class="icon" style="--icon-url: url(\'{icon_url}\');"></span>'
    
    # Process all icon references in the content
    return icon_pattern.sub(process_icon, content)

    # Process the normalized content with the replace_match function
    # Match patterns like :collection-icon: or :collection-icon-name:
    return re.sub(r':([a-z0-9-]+-[a-z0-9-]+):', replace_match, normalized_content)

def process_chapter(chapter):
    if 'content' in chapter:
        chapter['content'] = replace_icons(chapter['content'])
    if 'sub_items' in chapter:
        for sub_item in chapter['sub_items']:
            # In mdbook JSON, sub_items are Chapters
            if 'Chapter' in sub_item:
                process_chapter(sub_item['Chapter'])

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "supports":
        # mdbook checks if the preprocessor supports the renderer
        # We support html, so we don't need to do anything special
        sys.exit(0)

    # Load the book from stdin
    context, book = json.load(sys.stdin)

    # Process each chapter
    for section in book['sections']:
        if 'Chapter' in section:
            process_chapter(section['Chapter'])

    # Output the modified book to stdout
    print(json.dumps(book))
