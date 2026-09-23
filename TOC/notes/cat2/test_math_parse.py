import os
import re
import base64
import markdown_it
from playwright.sync_api import sync_playwright

BASE_DIR = r"c:\Users\ankit\Fall2627\TOC\notes\cat2"

def test_parse(filename):
    p = os.path.join(BASE_DIR, filename)
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()

    # Step 1: protect escaped dollars
    clean_text = text.replace(r"\$", "@@@ESCDOLLAR@@@")

    math_blocks = []
    def save_display(m):
        idx = len(math_blocks)
        math_blocks.append(('display', m.group(1)))
        return f"XQDMATH{idx}MQX"

    def save_inline(m):
        idx = len(math_blocks)
        math_blocks.append(('inline', m.group(1)))
        return f"XQIMATH{idx}MQX"

    # Step 2: Display math
    protected = re.sub(r'\$\$(.*?)\$\$', save_display, clean_text, flags=re.DOTALL)
    
    # Step 3: Inline math
    protected = re.sub(r'\$([^\$\n]+?)\$', save_inline, protected)

    # Check if there are any stray $ remaining in protected!
    remaining_dollars = [line for line in protected.splitlines() if '$' in line]
    print(f"=== {filename} ===")
    print(f"Total display math blocks: {len([b for b in math_blocks if b[0]=='display'])}")
    print(f"Total inline math blocks: {len([b for b in math_blocks if b[0]=='inline'])}")
    print(f"Remaining stray dollar lines in text: {len(remaining_dollars)}")
    for line in remaining_dollars[:5]:
        print("  Stray dollar line:", repr(line[:70]))

test_parse("cat2-actual-paper-sep2026-solved.md")
test_parse("TOC_CAT2_FOOLPROOF_SOLVE_BOOKLET.md")
