import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\ankit\Fall2627\TOC\notes\cat2"
md_file = os.path.join(BASE_DIR, "TOC_CAT2_FOOLPROOF_SOLVE_BOOKLET.md")

with open(md_file, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()
for idx, line in enumerate(lines):
    # Check for raw $ followed by space, or space followed by $, or unescaped standalone $
    matches = list(re.finditer(r'(?<!\\)\$', line))
    # If odd number of $, definitely an issue
    if len(matches) % 2 != 0:
        print(f"Line {idx+1} [ODD $ count ({len(matches)})]: {line}")
    # Also check if line has " $ " or " ($ " or " $)"
    elif any(pattern in line for pattern in [" $ ", " ($", " $)"]):
        print(f"Line {idx+1} [RAW $ in text]: {line}")
