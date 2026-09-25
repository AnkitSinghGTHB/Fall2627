import re

with open(r"c:\Users\ankit\Fall2627\TOC\notes\cat2\TOC_CAT2_FOOLPROOF_SOLVE_BOOKLET.md", "r", encoding="utf-8") as f:
    text = f.read()

# Pattern for dollar sign immediately adjacent to another dollar sign (even with backslash)
bad_patterns = [r'\$\\\$', r'\\\$\$', r'\$\s*\\\$']
for p in bad_patterns:
    matches = list(re.finditer(p, text))
    print(f"Pattern {p}: {len(matches)} matches")
    for m in matches:
        start = max(0, m.start() - 25)
        end = min(len(text), m.end() + 25)
        print("  Context:", repr(text[start:end]))
