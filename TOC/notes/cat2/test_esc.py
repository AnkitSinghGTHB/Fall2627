import os
import re
import base64
import markdown_it
from playwright.sync_api import sync_playwright

BASE_DIR = r"c:\Users\ankit\Fall2627\TOC\notes\cat2"
md_file = os.path.join(BASE_DIR, "cat2-actual-paper-sep2026-solved.md")

with open(md_file, "r", encoding="utf-8") as f:
    raw_md = f.read()

print("File length:", len(raw_md))

# Check for stray unescaped dollars or patterns
# Let's inspect escaped dollar instances
found_esc = re.findall(r'\\\$', raw_md)
print("Count of \\$ in file:", len(found_esc))

# Let's see some contexts of \$
for m in re.finditer(r'\\\$', raw_md):
    start = max(0, m.start() - 25)
    end = min(len(raw_md), m.end() + 25)
    print(f"Context: {repr(raw_md[start:end])}")
    break
