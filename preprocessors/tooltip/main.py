import sys
import json
import re
import os
import html
from pathlib import Path

def escape_attr(s):
    """Escape string for use in an HTML attribute."""
    return html.escape(s, quote=True)

def load_tooltip_content(tooltip_ref):
    # Check if the reference is a file path (starts with @)
    if tooltip_ref.startswith('@'):
        # Remove @ and any whitespace
        file_path = tooltip_ref[1:].strip()
        # Look for the file in the content/tooltips directory
        tooltip_file = Path('content/tooltips') / f"{file_path}.md"
        
        if tooltip_file.exists():
            with open(tooltip_file, 'r', encoding='utf-8') as f:
                return f.read().strip()
        return f"[Tooltip not found: {file_path}]"
    return tooltip_ref

def replace_tooltips(content, file_path=None):
    # This regex finds [^tooltip:content] patterns
    tooltip_pattern = re.compile(r'\[\^tooltip:([^\]]+)\]')

    def process_tooltip(match):
        tooltip_ref = match.group(1).strip()
        # Load the tooltip content (either direct content or from file)
        tooltip_content = load_tooltip_content(tooltip_ref)
        
        # Escape HTML entities for the data attribute
        escaped_content = escape_attr(tooltip_content)
        
        # Create a span with the info icon and tooltip content
        return (
            '<span class="tooltip-trigger" data-tippy-content="' + 
            escaped_content + 
            '"><i class="fa fa-info-circle" aria-hidden="true"></i></span>'
        )

    return tooltip_pattern.sub(process_tooltip, content)

def process_chapter(chapter):
    if 'content' in chapter:
        chapter['content'] = replace_tooltips(chapter['content'])
    if 'sub_items' in chapter:
        for sub_item in chapter['sub_items']:
            if 'Chapter' in sub_item:
                process_chapter(sub_item['Chapter'])

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "supports":
        sys.exit(0)

    context, book = json.load(sys.stdin)

    for section in book['sections']:
        if 'Chapter' in section:
            process_chapter(section['Chapter'])

    print(json.dumps(book))