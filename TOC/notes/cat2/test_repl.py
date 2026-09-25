import re
import markdown_it

with open(r"c:\Users\ankit\Fall2627\TOC\notes\cat2\TOC_CAT2_FOOLPROOF_SOLVE_BOOKLET.md", "r", encoding="utf-8") as f:
    md_text = f.read()

display_blocks = []
inline_blocks = []

def save_display(m):
    idx = len(display_blocks)
    display_blocks.append(m.group(1).strip())
    return f"XQDMATH{idx}MQX"

def save_inline(m):
    idx = len(inline_blocks)
    inline_blocks.append(m.group(1).strip())
    return f"XQIMATH{idx}MQX"

# Step 1: protect display math
text = re.sub(r'\$\$(.*?)\$\$', save_display, md_text, flags=re.DOTALL)

# Step 2: protect inline math
inline_pattern = r'(?<!\\)\$((?:\\\$|[^$\n])+?)(?<!\\)\$'
text = re.sub(inline_pattern, save_inline, text)

print("Total display blocks:", len(display_blocks))
print("Total inline blocks:", len(inline_blocks))

# Step 3: markdown render
md = markdown_it.MarkdownIt("commonmark", {"html": True, "breaks": True})
md.enable(["table", "strikethrough"])
html = md.render(text)

# Step 4: restore
for idx, raw in enumerate(display_blocks):
    tok = f"XQDMATH{idx}MQX"
    if tok not in html:
        print(f"Missing display token: {tok}")
    html = html.replace(tok, f'<div class="math-display">{raw}</div>')

for idx, raw in enumerate(inline_blocks):
    tok = f"XQIMATH{idx}MQX"
    if tok not in html:
        print(f"Missing inline token: {tok}")
    html = html.replace(tok, f'<span class="math-inline">{raw}</span>')

print("Remaining XQ tokens in html:", html.count("XQDMATH"), html.count("XQIMATH"))
