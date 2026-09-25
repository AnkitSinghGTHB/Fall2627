import re

with open(r"c:\Users\ankit\Fall2627\TOC\notes\cat2\TOC_CAT2_FOOLPROOF_SOLVE_BOOKLET.md", "r", encoding="utf-8") as f:
    text = f.read()

math_inlines = re.findall(r'\$([^\$\n]+?)\$', text)
suspicious = []
for m in math_inlines:
    if "'='" in m:
        suspicious.append(m)

print("Suspicious inline math containing '=':", len(suspicious))
for s in suspicious:
    print("  ", s)
