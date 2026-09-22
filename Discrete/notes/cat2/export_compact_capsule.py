import os
import re
import sys
import base64
import markdown_it
import pypdf
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\ankit\Fall2627\Discrete\notes\cat2"
PDF_OUT_DIR = os.path.join(BASE_DIR, "pdf")
os.makedirs(PDF_OUT_DIR, exist_ok=True)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>MAT2002 Discrete Mathematics CAT-2 Ultimate Exam Capsule</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<style>
  @page {
    size: A4;
    margin: 10mm 11mm 10mm 11mm;
  }
  
  *, *::before, *::after {
    box-sizing: border-box;
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 8.4pt;
    line-height: 1.35;
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
    margin-top: 10pt;
    margin-bottom: 4pt;
    page-break-after: avoid;
  }

  h2 {
    font-size: 11pt;
    color: #1e293b;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 2px;
    margin-top: 8pt;
    margin-bottom: 3pt;
    page-break-after: avoid;
  }

  h3 {
    font-size: 9.5pt;
    color: #334155;
    margin-top: 7pt;
    margin-bottom: 2pt;
    page-break-after: avoid;
  }

  h4 {
    font-size: 8.8pt;
    color: #475569;
    margin-top: 5pt;
    margin-bottom: 2pt;
    page-break-after: avoid;
  }

  p {
    margin: 3pt 0 4pt 0;
  }

  ul, ol {
    margin: 2pt 0 4pt 14pt;
    padding: 0;
  }

  li {
    margin-bottom: 1.5pt;
  }

  hr {
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 6pt 0;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.8pt;
    margin: 4pt 0 6pt 0;
    page-break-inside: avoid;
  }

  th, td {
    border: 1px solid #cbd5e1;
    padding: 2.5pt 4pt;
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

  /* Images */
  .img-container {
    text-align: center;
    margin: 6pt 0 4pt 0;
    page-break-inside: avoid;
  }

  img {
    max-width: 82%;
    max-height: 180px;
    height: auto;
    object-fit: contain;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  }

  .caption {
    font-size: 7.2pt;
    color: #475569;
    font-style: italic;
    margin-top: 2pt;
    margin-bottom: 4pt;
    text-align: center;
    page-break-after: avoid;
  }

  /* Math rendering */
  .katex {
    font-size: 1.02em;
  }

  .math-display {
    text-align: center;
    margin: 3pt 0;
    page-break-inside: avoid;
    overflow-x: auto;
  }

  code {
    font-family: "Consolas", "Courier New", monospace;
    background: #f1f5f9;
    padding: 1px 2.5pt;
    border-radius: 2px;
    font-size: 7.6pt;
    border: 1px solid #e2e8f0;
  }

  blockquote {
    border-left: 3px solid #2563eb;
    background: #eff6ff;
    padding: 4pt 6pt;
    margin: 4pt 0;
    border-radius: 0 3px 3px 0;
    page-break-inside: avoid;
  }

  .exam-banner {
    background: linear-gradient(135deg, #1e3a8a 0%, #1e293b 100%);
    color: #ffffff;
    padding: 8pt 12pt;
    border-radius: 4px;
    margin-bottom: 8pt;
  }

  .exam-banner h1 {
    color: #ffffff;
    border-bottom: 1px solid rgba(255, 255, 255, 0.25);
    margin-top: 0;
    padding-bottom: 2pt;
    font-size: 12pt;
  }

  .exam-banner p {
    margin: 1.5pt 0;
    font-size: 8pt;
    color: #e2e8f0;
  }
</style>
</head>
<body>
<div class="exam-banner">
    <h1>MAT2002: Discrete Mathematics & Graph Theory — CAT-2 Ultimate Exam Capsule</h1>
    <p><strong>Strict Page Budget:</strong> Maximum 16 Pages | <strong>Format:</strong> High-Yield Open-Book Exam-Hall Master Reference</p>
    <p><strong>Contents:</strong> 30-Sec Instant Topic Matcher + Official Papers 1 & 2 (Sep 2026) Solved + Universal Algorithmic Blueprints</p>
</div>

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

def markdown_to_print_html(md_text, base_dir):
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

    md_text = re.sub(r'!\[(.*?)\]\((.*?)\)', replace_md_img, md_text)
    protected = re.sub(r'\$\$(.*?)\$\$', save_display, md_text, flags=re.DOTALL)
    protected = re.sub(r'\$([^\$\n]+?)\$', save_inline, protected)

    md_parser = markdown_it.MarkdownIt('commonmark').enable('table')
    html = md_parser.render(protected)

    for idx, (mtype, raw) in enumerate(math_blocks):
        if mtype == 'display':
            html = html.replace(f"XQDMATH{idx}MQX", f'<div class="math-display">$${raw}$$</div>')
        else:
            html = html.replace(f"XQIMATH{idx}MQX", f'<span class="math-inline">${raw}$</span>')

    return HTML_TEMPLATE.replace("{content_html}", html)

def generate_capsule_pdf():
    md_file = os.path.join(BASE_DIR, "cat2-compact-exam-capsule-max16p.md")
    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    html_content = markdown_to_print_html(md_text, BASE_DIR)
    out_pdf = os.path.join(PDF_OUT_DIR, "Discrete_CAT2_ULTIMATE_EXAM_CAPSULE_MAX16P.pdf")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html_content, wait_until="networkidle")
        page.wait_for_timeout(1500)

        header_template = """
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 6.8pt; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 11mm;">
            <span><strong>MAT2002: Discrete Mathematics & Graph Theory</strong> — CAT-2 Ultimate Exam Capsule</span>
            <span>Open-Book Master Reference</span>
        </div>
        """

        footer_template = """
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 7pt; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 11mm;">
            <span>Modules 3 & 4 (Lattices, Boolean Algebra, Graph Theory & Matrix Representations)</span>
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

    reader = pypdf.PdfReader(out_pdf)
    num_pages = len(reader.pages)
    print(f"============================================================")
    print(f"Generated PDF: {os.path.basename(out_pdf)}")
    print(f"Total Page Count: {num_pages} pages")
    print(f"Target Budget Status: {'PASS (<= 16 pages)' if num_pages <= 16 else 'EXCEEDED (> 16 pages)'}")
    print(f"============================================================")

if __name__ == "__main__":
    generate_capsule_pdf()
