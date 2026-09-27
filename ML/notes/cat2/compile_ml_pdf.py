import os
import re
import sys
import markdown_it
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\ankit\Fall2627\ML\notes\cat2"
PDF_OUT_DIR = os.path.join(BASE_DIR, "pdf")
os.makedirs(PDF_OUT_DIR, exist_ok=True)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CSE4005 Machine Learning: CAT-II Calculations Master Booklet</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<style>
  @page {
    size: A4;
    margin: 11mm 11mm 11mm 11mm;
  }
  
  *, *::before, *::after {
    box-sizing: border-box;
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 8.0pt;
    line-height: 1.30;
    color: #0f172a;
    background: #ffffff;
    margin: 0;
    padding: 0;
  }

  h1 {
    font-size: 11.5pt;
    color: #1e3a8a;
    border-bottom: 2px solid #1e3a8a;
    padding-bottom: 2px;
    margin-top: 8pt;
    margin-bottom: 3pt;
    page-break-after: avoid;
    break-after: avoid;
  }

  h2 {
    font-size: 10.0pt;
    color: #0369a1;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 1.5px;
    margin-top: 6pt;
    margin-bottom: 2pt;
    page-break-after: avoid;
    break-after: avoid;
  }

  h3 {
    font-size: 8.8pt;
    color: #0f766e;
    margin-top: 5pt;
    margin-bottom: 1.5pt;
    page-break-after: avoid;
    break-after: avoid;
  }

  h4 {
    font-size: 8.2pt;
    color: #334155;
    margin-top: 4pt;
    margin-bottom: 1pt;
    page-break-after: avoid;
    break-after: avoid;
  }

  p {
    margin-top: 1.5pt;
    margin-bottom: 2.5pt;
  }

  ul, ol {
    margin-top: 1pt;
    margin-bottom: 2.5pt;
    padding-left: 14pt;
  }

  li {
    margin-bottom: 1pt;
  }

  strong {
    color: #090d16;
  }

  code {
    font-family: "Fira Code", Consolas, Monaco, "Courier New", monospace;
    font-size: 7.2pt;
    background: #f1f5f9;
    color: #0f172a;
    padding: 0.5pt 2.5pt;
    border-radius: 2px;
    border: 1px solid #e2e8f0;
  }

  pre {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 3px;
    padding: 4pt 6pt;
    margin: 2.5pt 0;
    overflow-x: auto;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  pre code {
    background: transparent;
    padding: 0;
    border: none;
    font-size: 7.0pt;
    line-height: 1.25;
    color: #0f172a;
  }

  blockquote {
    margin: 3pt 0;
    padding: 3pt 7pt;
    background: #f0fdf4;
    border-left: 3.5px solid #16a34a;
    border-radius: 0 3px 3px 0;
    color: #166534;
    font-size: 7.6pt;
  }

  blockquote p {
    margin: 0.5pt 0;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin: 3pt 0;
    font-size: 7.2pt;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  th, td {
    border: 1px solid #cbd5e1;
    padding: 2.5pt 4pt;
    text-align: left;
    vertical-align: middle;
  }

  th {
    background-color: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
  }

  tr:nth-child(even) td {
    background-color: #f8fafc;
  }

  .math-display {
    margin: 3pt 0;
    text-align: center;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  .math-inline {
    font-size: 8.0pt;
  }

  .diagram-box {
    margin: 4pt 0;
    padding: 4pt 6pt;
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    page-break-inside: avoid;
    break-inside: avoid;
    text-align: center;
  }

  .diagram-grid {
    display: flex;
    gap: 6pt;
    justify-content: space-between;
    margin: 3pt 0;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  .diagram-card {
    flex: 1;
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 3px;
    padding: 4pt;
    text-align: center;
    font-size: 6.8pt;
  }

  .diagram-card svg {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto 2pt;
  }

  .diagram-caption {
    font-size: 6.8pt;
    font-weight: bold;
    color: #1e3a8a;
    margin-top: 2pt;
  }

  .exam-banner {
    background: linear-gradient(135deg, #1e3a8a 0%, #0369a1 100%);
    color: #ffffff;
    padding: 6pt 9pt;
    border-radius: 4px;
    margin-bottom: 5pt;
  }

  .exam-banner h1 {
    color: #ffffff;
    border-bottom: 1px solid rgba(255, 255, 255, 0.3);
    margin: 0;
    padding-bottom: 2pt;
    font-size: 11pt;
  }

  .exam-banner p {
    margin: 1.5pt 0;
    font-size: 7.6pt;
    color: #e2e8f0;
  }
</style>
</head>
<body>
{banner_html}

{content_html}

<script>
document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
        delimiters: [
            {left: "$$", right: "$$", display: true},
            {left: "$", right: "$", display: false}
        ],
        throwOnError: false
    });
});
</script>
</body>
</html>
"""

def markdown_to_print_html(md_text, banner_html):
    clean_text = md_text.replace(r"\$", "@@@ESCDOLLAR@@@")

    math_blocks = []

    def save_display(m):
        idx = len(math_blocks)
        math_blocks.append(('display', m.group(1)))
        return f"XQDMATH{idx}MQX"

    def save_inline(m):
        idx = len(math_blocks)
        math_blocks.append(('inline', m.group(1)))
        return f"XQIMATH{idx}MQX"

    # Protect display math ($$ ... $$)
    protected = re.sub(r'\$\$(.*?)\$\$', save_display, clean_text, flags=re.DOTALL)

    # Protect inline math ($ ... $)
    protected = re.sub(r'\$([^\$\n]+?)\$', save_inline, protected)

    # Restore escaped dollar inside plain text before markdown parsing
    protected = protected.replace("@@@ESCDOLLAR@@@", "&#36;")

    # Sanitize SVGs: strip empty lines and leading spaces inside <svg> tags to prevent markdown-it code-block triggers
    def clean_svg(match):
        svg_content = match.group(0)
        cleaned_lines = []
        for line in svg_content.splitlines():
            line_str = line.strip()
            if line_str:
                cleaned_lines.append(line_str)
        return '\n'.join(cleaned_lines)

    protected = re.sub(r'<svg[\s\S]*?</svg>', clean_svg, protected)

    # Parse markdown to HTML
    md_parser = markdown_it.MarkdownIt('default', options_update={'html': True}).enable('table')
    html = md_parser.render(protected)

    # Re-inject math with KaTeX delimiters
    import html as html_lib
    for idx, (mtype, raw) in enumerate(math_blocks):
        restored_math = raw.replace("@@@ESCDOLLAR@@@", r"\$")
        escaped_math = html_lib.escape(restored_math)
        if mtype == 'display':
            html = html.replace(f"XQDMATH{idx}MQX", f'<div class="math-display">$${escaped_math}$$</div>')
        else:
            html = html.replace(f"XQIMATH{idx}MQX", f'<span class="math-inline">${escaped_math}$</span>')

    full_html = HTML_TEMPLATE.replace("{banner_html}", banner_html)
    full_html = full_html.replace("{content_html}", html)
    return full_html

def compile_ml_pdf():
    md_file = os.path.join(BASE_DIR, "ML_CAT2_CALCULATIONS_MASTER_BOOKLET.md")
    out_pdf = os.path.join(PDF_OUT_DIR, "ML_CAT2_CALCULATIONS_MASTER_BOOKLET.pdf")

    if not os.path.exists(md_file):
        print(f"Error: {md_file} not found!")
        return

    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    banner_html = """
    <div class="exam-banner">
        <h1>CSE4005: MACHINE LEARNING — CAT-II CALCULATIONS MASTER BOOKLET</h1>
        <p><strong>Course:</strong> CSE4005 — Machine Learning | <strong>Exam Mode:</strong> Open Book / Open Notes (50 Marks, 90 Mins)</p>
        <p><strong>Faculty Pattern:</strong> Dr. Nilamadhab Mishra | <strong>Scope:</strong> Unit 3 (3 Questions - 30M) & Unit 4 (2 Questions - 20M) — 100% Calculations</p>
    </div>
    """

    html_content = markdown_to_print_html(md_text, banner_html)

    # Save debug HTML
    debug_html_path = os.path.join(BASE_DIR, "debug_ml_print.html")
    with open(debug_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.set_content(html_content, wait_until="networkidle")
        page.wait_for_timeout(3000)

        header_template = """
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 6.8pt; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 11mm;">
            <span><strong>CSE4005: Machine Learning</strong> — CAT-II Calculations Master Booklet</span>
            <span>VIT Bhopal University — Fall 2026-27</span>
        </div>
        """

        footer_template = """
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 7.0pt; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 11mm;">
            <span>Dr. Nilamadhab Mishra (Units 3 & 4: Ensembles, Clustering, Bayes, Association Rules)</span>
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
                "top": "12mm",
                "bottom": "12mm",
                "left": "11mm",
                "right": "11mm"
            }
        )
        browser.close()

    print(f"Successfully generated PDF: {out_pdf}")

if __name__ == "__main__":
    compile_ml_pdf()
