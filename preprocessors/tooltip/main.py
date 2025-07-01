import sys
import json
import re
import html

def escape_attr(s):
    """Escape string for use in an HTML attribute."""
    return html.escape(s, quote=True)

def replace_tooltips(content):
    # This regex finds [tooltip-(content here)] patterns
    tooltip_pattern = re.compile(r'\[tooltip-\(([^)]+)\]')

    def process_tooltip(match):
        tooltip_content = match.group(1)
        # Create a span with the info icon and tooltip content
        return (
            '<span class="tooltip-trigger" data-tippy-content="' + 
            escape_attr(tooltip_content) + 
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