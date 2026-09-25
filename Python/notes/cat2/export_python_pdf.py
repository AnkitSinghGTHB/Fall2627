import os
import re
import sys
import markdown_it
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\ankit\Fall2627\Python\notes\cat2"
PDF_OUT_DIR = os.path.join(BASE_DIR, "pdf")
os.makedirs(PDF_OUT_DIR, exist_ok=True)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CSE3011 Python Programming: CAT-II Master Reference</title>
<style>
  @page {
    size: A4;
    margin: 8mm 9mm 8mm 9mm;
  }
  
  *, *::before, *::after {
    box-sizing: border-box;
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 7.0pt;
    line-height: 1.15;
    color: #0f172a;
    background: #ffffff;
    margin: 0;
    padding: 0;
  }

  h1 {
    font-size: 10.0pt;
    color: #0f766e;
    border-bottom: 1.5px solid #0f766e;
    padding-bottom: 1px;
    margin-top: 4pt;
    margin-bottom: 1.5pt;
    break-after: avoid;
    page-break-after: avoid;
  }

  h2 {
    font-size: 8.4pt;
    color: #134e4a;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 1px;
    margin-top: 3pt;
    margin-bottom: 1pt;
    break-after: avoid;
    page-break-after: avoid;
  }

  h3 {
    font-size: 7.6pt;
    color: #0f766e;
    margin-top: 2.5pt;
    margin-bottom: 1pt;
    break-after: avoid;
    page-break-after: avoid;
  }

  h4 {
    font-size: 7.0pt;
    color: #334155;
    margin-top: 2pt;
    margin-bottom: 0.5pt;
    font-weight: 700;
    break-after: avoid;
    page-break-after: avoid;
  }

  p {
    margin: 1pt 0 1.5pt 0;
  }

  ul, ol {
    margin: 1pt 0 1.5pt 10pt;
    padding: 0;
  }

  li {
    margin-bottom: 0.5pt;
  }

  hr {
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 2pt 0;
  }

  /* Tables: Ultra-compact display with repeated headers */
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 6.5pt;
    line-height: 1.12;
    margin: 1.5pt 0 2.5pt 0;
    break-inside: auto;
    page-break-inside: auto;
  }

  thead {
    display: table-header-group;
  }

  tr {
    break-inside: avoid;
    page-break-inside: avoid;
  }

  th, td {
    border: 1px solid #cbd5e1;
    padding: 1.5pt 2.5pt;
    text-align: left;
    vertical-align: middle;
  }

  th {
    background-color: #f0fdfa;
    color: #134e4a;
    font-weight: 600;
  }

  tr:nth-child(even) {
    background-color: #f8fafc;
  }

  /* Code Blocks: Compact print, right-side comments, zero wasted vertical lines */
  pre {
    background: #ffffff;
    color: #0f172a;
    padding: 2.5pt 4pt;
    border-radius: 3px;
    font-family: "Consolas", "Courier New", monospace;
    font-size: 6.4pt;
    line-height: 1.14;
    overflow-x: auto;
    margin: 1pt 0 2pt 0;
    border: 1px solid #cbd5e1;
    border-left: 2.5px solid #0f766e;
    break-inside: auto;
    page-break-inside: auto;
    orphans: 3;
    widows: 3;
  }

  /* Output Blocks - Distinct Clean Terminal Box */
  pre:has(code.language-text),
  pre:has(code.language-output) {
    background-color: #f8fafc;
    border: 1px dashed #94a3b8;
    border-left: 2.5px solid #2563eb;
    color: #1e293b;
    font-size: 6.2pt;
    line-height: 1.12;
    padding: 2pt 3.5pt;
    break-inside: avoid;
    page-break-inside: avoid;
  }

  code {
    font-family: "Consolas", "Courier New", monospace;
    font-size: 6.6pt;
    background-color: #f1f5f9;
    color: #0f766e;
    padding: 0 1.5px;
    border-radius: 2px;
  }

  pre code {
    background-color: transparent;
    color: inherit;
    padding: 0;
  }

  /* Exam Banner */
  .exam-banner {
    background-color: #f0fdfa;
    border: 1.5px solid #0f766e;
    border-left: 3.5px solid #0f766e;
    color: #042f2e;
    padding: 3pt 6pt;
    border-radius: 3px;
    margin-bottom: 3pt;
    break-inside: avoid;
  }

  .exam-banner h1 {
    color: #0f766e;
    border: none;
    margin: 0 0 1pt 0;
    font-size: 10.0pt;
    letter-spacing: -0.2px;
  }

  .exam-banner p {
    margin: 0.5pt 0;
    font-size: 6.6pt;
    color: #134e4a;
  }

  /* Target Question Box - Compact Callout */
  blockquote {
    border: 1px solid #cbd5e1;
    border-left: 3px solid #0f766e;
    border-radius: 0 2px 2px 0;
    margin: 1.5pt 0 2pt 0;
    padding: 1.5pt 5pt;
    background-color: #f8fafc;
    color: #0f172a;
    font-size: 6.8pt;
    line-height: 1.15;
    break-inside: avoid;
    page-break-inside: avoid;
    break-after: avoid;
    page-break-after: avoid;
  }

  blockquote p {
    margin: 0.5pt 0;
  }

  blockquote h3 {
    margin-top: 0.5pt;
    margin-bottom: 0.5pt;
    font-size: 7.2pt;
    color: #0f766e;
  }
</style>
</head>
<body>
{{CONTENT}}
</body>
</html>
"""

def markdown_to_print_html(md_text, banner_html):
    md = markdown_it.MarkdownIt("commonmark", {"html": True, "breaks": True})
    md.enable(["table", "strikethrough"])
    
    # Strip redundant top title lines so Page 1 contains Banner + Navigation Matrix
    lines = md_text.splitlines()
    body_lines = []
    skip = True
    for l in lines:
        if skip:
            if l.strip() == "---":
                skip = False
            continue
        # Ensure Section 1 starts cleanly at top of Page 2
        if l.startswith("# SECTION 1:"):
            body_lines.append('<div style="page-break-before: always;"></div>')
        body_lines.append(l)

    rendered_body = md.render("\n".join(body_lines))
    full_body = banner_html + "\n" + rendered_body
    return HTML_TEMPLATE.replace("{{CONTENT}}", full_body)

def export_python_pdf():
    md_file = os.path.join(BASE_DIR, "PYTHON_CAT2_FOOLPROOF_SOLVE_BOOKLET.md")
    out_pdf = os.path.join(PDF_OUT_DIR, "PYTHON_CAT2_FOOLPROOF_SOLVE_BOOKLET.pdf")

    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    banner_html = """
    <div class="exam-banner">
        <h1>CSE3011: PYTHON PROGRAMMING — CAT-II FOOLPROOF SPEEDRUN BOOKLET</h1>
        <p><strong>Course:</strong> CSE3011 — Python | <strong>Exam:</strong> CAT-2 Open Book Master Reference | <strong>Marks:</strong> 50 Marks</p>
        <p><strong>Coverage:</strong> Modules 3 & 4 (Advanced OOP, Dunder Methods, Persistence, Streams, OS & DB-API) + September 2026 Solved Papers</p>
    </div>
    """

    html_content = markdown_to_print_html(md_text, banner_html)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html_content, wait_until="networkidle")
        page.wait_for_timeout(1000)

        header_template = """
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 5.8pt; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 9mm;">
            <span><strong>CSE3011: Python Programming</strong> — CAT-II Master Reference</span>
            <span>CAT-2 Open-Book Solved Reference</span>
        </div>
        """

        footer_template = """
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 6.0pt; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 9mm;">
            <span>Modules 3 & 4 + Solved September 2026 Examination Papers</span>
            <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
        </div>
        """

        page.pdf(
            path=out_pdf,
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template=header_template,
            footer_template=footer_template,
            margin={
                "top": "9mm",
                "bottom": "9mm",
                "left": "9mm",
                "right": "9mm"
            }
        )
        print("Successfully Generated Python PDF:", out_pdf)
        browser.close()

if __name__ == "__main__":
    export_python_pdf()
