import sys
import json
import re
import os
import html
import markdown
from pathlib import Path

def escape_attr(s):
    """Escape string for use in an HTML attribute."""
    return html.escape(s, quote=True)

def convert_markdown_to_html(md_content):
    """Convert markdown content to HTML."""
    # First, convert markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['extra', 'nl2br'])
    
    # Process links to add target and rel attributes
    import re
    link_pattern = re.compile(r'<a\s+(?:[^>]*?\s+)?href=["\'](.*?)["\'](?:[^>]*)>(.*?)</a>', re.DOTALL)
    
    def process_link(match):
        url = match.group(1)
        text = match.group(2)
        # Ensure URL is properly quoted
        url = html.escape(url, quote=True)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{text}</a>'
    
    # Process all links in the content
    return link_pattern.sub(process_link, html_content)

def load_tooltip_content(tooltip_ref):
    # Check if the reference is a file path (starts with @)
    if tooltip_ref.startswith('@'):
        # Remove @ and any whitespace
        file_path = tooltip_ref[1:].strip()
        # Look for the file in the content/tooltips directory
        tooltip_file = Path('content/tooltips') / f"{file_path}.md"
        
        if tooltip_file.exists():
            with open(tooltip_file, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                return convert_markdown_to_html(content)
        return f"[Tooltip not found: {file_path}]"
    # If it's direct content, convert markdown to HTML
    return convert_markdown_to_html(tooltip_ref)

def replace_tooltips(content, file_path=None):
    # This regex finds [^tooltip:content] patterns
    tooltip_pattern = re.compile(r'\[\^tooltip:([^\]]+)\]')

    def process_tooltip(match):
        tooltip_ref = match.group(1).strip()
        # Load the tooltip content (either direct content or from file)
        tooltip_content = load_tooltip_content(tooltip_ref)
        
        # Create a span with the info icon and tooltip content
        # Note: We're not escaping the content here as it's already HTML
        return (
            '<span class="tooltip-trigger" data-tippy-content="' + 
            tooltip_content.replace('"', '&quot;') + 
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