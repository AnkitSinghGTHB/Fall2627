import os
import re
import sys
import base64
import markdown_it
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\ankit\Fall2627\DLD\notes\cat2"
PDF_OUT_DIR = os.path.join(BASE_DIR, "pdf")
os.makedirs(PDF_OUT_DIR, exist_ok=True)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ECE2002 DLD: CAT-II Foolproof Exam Solve Booklet</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<style>
  @page {
    size: A4;
    margin: 11mm 12mm 11mm 12mm;
  }
  
  *, *::before, *::after {
    box-sizing: border-box;
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 8.5pt;
    line-height: 1.38;
    color: #0f172a;
    background: #ffffff;
    margin: 0;
    padding: 0;
  }

  h1 {
    font-size: 13pt;
    color: #1e3a8a;
    border-bottom: 2px solid #1e3a8a;
    padding-bottom: 2px;
    margin-top: 8pt;
    margin-bottom: 3.5pt;
    page-break-after: avoid;
  }

  h2 {
    font-size: 10.8pt;
    color: #1e293b;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 2px;
    margin-top: 7pt;
    margin-bottom: 3pt;
    page-break-after: avoid;
  }

  h3 {
    font-size: 9.5pt;
    color: #1e3a8a;
    margin-top: 6pt;
    margin-bottom: 2.5pt;
    page-break-after: avoid;
  }

  h4 {
    font-size: 8.8pt;
    color: #334155;
    margin-top: 5pt;
    margin-bottom: 2pt;
    font-weight: 700;
    page-break-after: avoid;
  }

  p {
    margin: 2.2pt 0 3.2pt 0;
  }

  ul, ol {
    margin: 2pt 0 3.2pt 14pt;
    padding: 0;
  }

  li {
    margin-bottom: 1.5pt;
  }

  hr {
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 5pt 0;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.8pt;
    margin: 4pt 0 5pt 0;
    page-break-inside: avoid;
  }

  th, td {
    border: 1px solid #cbd5e1;
    padding: 2.6pt 4pt;
    text-align: left;
    vertical-align: middle;
  }

  th {
    background-color: #f1f5f9;
    color: #1e293b;
    font-weight: 600;
  }

  tr:nth-child(even) {
    background-color: #f8fafc;
  }

  /* Images & Schematics */
  .img-container {
    text-align: center;
    margin: 5pt 0 3pt 0;
    page-break-inside: avoid;
  }

  img {
    max-width: 92%;
    max-height: 200px;
    height: auto;
    object-fit: contain;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  }

  .caption {
    font-size: 7.4pt;
    color: #475569;
    font-style: italic;
    margin-top: 1.5pt;
    margin-bottom: 3pt;
    text-align: center;
    page-break-after: avoid;
  }

  /* Math rendering */
  .katex {
    font-size: 1.02em;
  }

  .math-display {
    text-align: center;
    margin: 2.2pt 0;
    page-break-inside: avoid;
    overflow-x: auto;
  }

  code {
    font-family: "Consolas", "Courier New", monospace;
    background: #f1f5f9;
    padding: 1px 3pt;
    border-radius: 3px;
    font-size: 7.6pt;
    border: 1px solid #e2e8f0;
  }

  blockquote {
    border-left: 3.5px solid #2563eb;
    background: #eff6ff;
    padding: 3.5pt 6.5pt;
    margin: 3.5pt 0;
    border-radius: 0 3px 3px 0;
    page-break-inside: avoid;
  }

  .exam-banner {
    background: linear-gradient(135deg, #1e3a8a 0%, #1e293b 100%);
    color: #ffffff;
    padding: 8pt 12pt;
    border-radius: 4px;
    margin-bottom: 7pt;
  }

  .exam-banner h1 {
    color: #ffffff;
    border-bottom: 1px solid rgba(255, 255, 255, 0.25);
    margin-top: 0;
    padding-bottom: 2pt;
    font-size: 12pt;
  }

  .exam-banner p {
    margin: 1.2pt 0;
    font-size: 8.2pt;
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

def markdown_to_print_html(md_text, base_dir, banner_html):
    # Step 1: Protect escaped dollars so they don't break math delimiters
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

    def replace_md_img(match):
        alt = match.group(1)
        src = match.group(2)
        if src.startswith("file:///"):
            clean_path = src[8:].replace('/', '\\')
        elif not os.path.isabs(src):
            clean_path = os.path.normpath(os.path.join(base_dir, src))
        else:
            clean_path = src

        if os.path.exists(clean_path):
            ext = os.path.splitext(clean_path)[1].lower()
            mime = "image/png" if ext == ".png" else "image/svg+xml" if ext == ".svg" else "image/jpeg"
            with open(clean_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode('utf-8')
            return f'\n\n<div class="img-container"><img src="data:{mime};base64,{b64}" alt="{alt}"><div class="caption">{alt}</div></div>\n\n'
        else:
            print(f"Warning: Image not found at {clean_path}")
            return match.group(0)

    # Replace local image references with base64 data URIs
    protected = re.sub(r'!\[(.*?)\]\((.*?)\)', replace_md_img, clean_text)

    # Protect display math ($$ ... $$)
    protected = re.sub(r'\$\$(.*?)\$\$', save_display, protected, flags=re.DOTALL)

    # Protect inline math ($ ... $)
    protected = re.sub(r'\$([^\$\n]+?)\$', save_inline, protected)

    # Restore escaped dollar inside plain text before markdown parsing
    protected = protected.replace("@@@ESCDOLLAR@@@", "&#36;")

    # Parse markdown to HTML
    md_parser = markdown_it.MarkdownIt('commonmark').enable('table')
    html = md_parser.render(protected)

    # Re-inject math with KaTeX delimiters, restoring escaped dollar signs inside LaTeX
    for idx, (mtype, raw) in enumerate(math_blocks):
        restored_math = raw.replace("@@@ESCDOLLAR@@@", r"\$")
        if mtype == 'display':
            html = html.replace(f"XQDMATH{idx}MQX", f'<div class="math-display">$${restored_math}$$</div>')
        else:
            html = html.replace(f"XQIMATH{idx}MQX", f'<span class="math-inline">${restored_math}$</span>')

    full_html = HTML_TEMPLATE.replace("{banner_html}", banner_html)
    full_html = full_html.replace("{content_html}", html)
    return full_html

def export_dld_booklet():
    src_file = os.path.join(BASE_DIR, "DLD_CAT2_FOOLPROOF_SOLVE_BOOKLET.md")
    out_pdf = os.path.join(PDF_OUT_DIR, "DLD_CAT2_FOOLPROOF_SOLVE_BOOKLET.pdf")

    if not os.path.exists(src_file):
        print(f"Error: Source file {src_file} does not exist!")
        return

    with open(src_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    banner_html = """
    <div class="exam-banner">
        <h1>⚡ ECE2002: DIGITAL LOGIC DESIGN — CAT-II FOOLPROOF SOLVE BOOKLET</h1>
        <p><strong>Course:</strong> ECE2002 — Digital Logic Design | <strong>Exam:</strong> CAT-2 (Open Book Master Reference)</p>
        <p><strong>Coverage:</strong> Modules 3 & 4 (Sequential Circuits, FF Conversions, Registers, Counters & FSMs)</p>
    </div>
    """

    print("Rendering HTML and preparing KaTeX math...")
    html_content = markdown_to_print_html(md_text, BASE_DIR, banner_html)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        print("Loading content in headless Chromium...")
        page.set_content(html_content, wait_until="networkidle")
        page.wait_for_timeout(2500)

        header_template = """
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 6.8pt; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 12mm;">
            <span><strong>ECE2002: Digital Logic Design</strong> — CAT-II Foolproof Exam Solve Booklet</span>
            <span>CAT-2 Open-Book Master Reference</span>
        </div>
        """

        footer_template = """
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 7.0pt; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 12mm;">
            <span>Modules 3 & 4 (Sequential Circuits, Registers, Counters & FSMs)</span>
            <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
        </div>
        """

        print("Exporting PDF...")
        page.pdf(
            path=out_pdf,
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template=header_template,
            footer_template=footer_template,
            margin={
                "top": "13mm",
                "bottom": "13mm",
                "left": "12mm",
                "right": "12mm"
            }
        )
        browser.close()
        print("Successfully Generated PDF:", out_pdf)

if __name__ == "__main__":
    export_dld_booklet()
