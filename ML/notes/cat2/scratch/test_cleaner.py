import re
from markdown_it import MarkdownIt

def sanitize_svgs(text):
    def clean_svg(match):
        svg_content = match.group(0)
        cleaned_lines = []
        for line in svg_content.splitlines():
            line_str = line.strip()
            if line_str:  # remove empty/whitespace-only lines
                cleaned_lines.append(line_str)
        return '\n'.join(cleaned_lines)
    
    return re.sub(r'<svg[\s\S]*?</svg>', clean_svg, text)

md = MarkdownIt('default', options_update={'html': True}).enable('table')
broken = """<div class="diagram-box">
  <svg>
    <rect x="10"/>

    <rect x="20"/>
  </svg>
</div>"""

cleaned = sanitize_svgs(broken)
out = md.render(cleaned)
print("HAS PRE CODE:", "<pre>" in out or "<code>" in out)
print("OUT:\n", out)
