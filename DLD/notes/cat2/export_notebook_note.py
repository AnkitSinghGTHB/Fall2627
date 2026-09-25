import os
import sys
from export_dld_booklet import markdown_to_print_html, sync_playwright

BASE_DIR = r"c:\Users\ankit\Fall2627\DLD\notes\cat2"
md_file = os.path.join(BASE_DIR, "FINAL_EXAM_HANDWRITTEN_NOTEBOOK_NOTE.md")
out_pdf = os.path.join(BASE_DIR, "pdf", "FINAL_EXAM_HANDWRITTEN_NOTEBOOK_NOTE.pdf")

with open(md_file, "r", encoding="utf-8") as f:
    md_text = f.read()

banner_html = """
<div class="exam-banner">
    <h1>⚡ DLD CAT-II: LAST-MINUTE HANDWRITTEN COPY CHEAT SHEET</h1>
    <p>5 Golden Teacher Instructions | Vending Machine FSM | Sequence Generator | 80% Core Checklist</p>
</div>
"""

html_content = markdown_to_print_html(md_text, BASE_DIR, banner_html)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_content(html_content, wait_until="networkidle")
    page.wait_for_timeout(2000)
    page.pdf(
        path=out_pdf,
        format="A4",
        print_background=True,
        margin={"top": "12mm", "bottom": "12mm", "left": "12mm", "right": "12mm"}
    )
    browser.close()
    print("Successfully generated:", out_pdf)
