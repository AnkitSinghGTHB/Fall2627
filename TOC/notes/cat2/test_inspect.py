with open(r"c:\Users\ankit\Fall2627\TOC\notes\cat2\test_repl.py", "r") as f:
    pass

import re, markdown_it

with open(r"c:\Users\ankit\Fall2627\TOC\notes\cat2\TOC_CAT2_FOOLPROOF_SOLVE_BOOKLET.md", "r", encoding="utf-8") as f:
    md_text = f.read()

display_blocks = []
def save_display(m):
    idx = len(display_blocks)
    raw = m.group(1).strip()
    display_blocks.append(raw)
    return f"XQDMATH{idx}MQX"

text = re.sub(r'\$\$(.*?)\$\$', save_display, md_text, flags=re.DOTALL)

md = markdown_it.MarkdownIt("commonmark", {"html": True, "breaks": True})
html = md.render(text)

pos = html.find("XQDMATH")
print("First XQDMATH found in html at:", pos)
print("Snippet around pos:")
print(html[pos:pos+100])
