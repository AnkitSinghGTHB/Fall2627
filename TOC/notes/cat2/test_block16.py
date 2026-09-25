import re

with open(r"c:\Users\ankit\Fall2627\TOC\notes\cat2\TOC_CAT2_FOOLPROOF_SOLVE_BOOKLET.md", "r", encoding="utf-8") as f:
    md_text = f.read()

display_blocks = []
def save_display(m):
    idx = len(display_blocks)
    raw = m.group(1).strip()
    display_blocks.append((idx, raw))
    return f"XQDMATH{idx}MQX"

text = re.sub(r'\$\$(.*?)\$\$', save_display, md_text, flags=re.DOTALL)
print("Block 16 raw:", repr(display_blocks[16]))

pos = text.find("XQDMATH16MQX")
print("Position in text of XQDMATH16MQX:", pos)
if pos != -1:
    print(repr(text[pos-50:pos+50]))
else:
    print("NOT FOUND in text! Why?")
