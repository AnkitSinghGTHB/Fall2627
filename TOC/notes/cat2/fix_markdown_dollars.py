import os
import re

BASE_DIR = r"c:\Users\ankit\Fall2627\TOC\notes\cat2"
md_path = os.path.join(BASE_DIR, "TOC_CAT2_FOOLPROOF_SOLVE_BOOKLET.md")

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace any `$ inside backticks` with `&#36;`
def replace_code_dollars(match):
    content = match.group(1)
    if '$' in content:
        content = content.replace('$', '&#36;')
        return f"<code>{content}</code>"
    return match.group(0)

text = re.sub(r'`([^`\n]*?\$(?:[^`\n]*?))`', replace_code_dollars, text)
text = text.replace("<code>&#36; +$</code>", "<code>+</code>")

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

dd = chr(36) + chr(36)
print("Double dollar count:", text.count(dd), "(Must be even)")

lines = text.splitlines()
odd_lines = []
for i, line in enumerate(lines):
    line_no_dd = line.replace(dd, '')
    if line_no_dd.count('$') % 2 != 0:
        odd_lines.append((i+1, line))

print(f"Total lines with odd single $: {len(odd_lines)}")
for ln, l in odd_lines:
    print(f"  Line {ln}: {l}")
