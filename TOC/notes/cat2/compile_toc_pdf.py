import os
import sys
import re
import base64
import subprocess
import markdown_it
import pypdf

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\ankit\Fall2627\TOC\notes\cat2"
PDF_OUT_DIR = os.path.join(BASE_DIR, "pdf")
os.makedirs(PDF_OUT_DIR, exist_ok=True)

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CSE2004 Theory of Computation: CAT-II Master Reference</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        document.querySelectorAll('.math-inline').forEach(function(el) {
            try {
                katex.render(el.textContent, el, { throwOnError: false, displayMode: false });
            } catch(e) {}
        });
        document.querySelectorAll('.math-display').forEach(function(el) {
            try {
                katex.render(el.textContent, el, { throwOnError: false, displayMode: true });
            } catch(e) {}
        });
    });
</script>
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
    margin-top: 10pt;
    margin-bottom: 4pt;
    page-break-after: avoid;
  }

  h2 {
    font-size: 10.8pt;
    color: #1e293b;
    border-bottom: 1.2px solid #cbd5e1;
    padding-bottom: 2px;
    margin-top: 9pt;
    margin-bottom: 3pt;
    page-break-after: avoid;
  }

  h3 {
    font-size: 9.6pt;
    color: #1e3a8a;
    margin-top: 7pt;
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
    margin: 2.5pt 0 3.5pt 0;
  }

  ul, ol {
    margin: 2pt 0 3.5pt 14pt;
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
    font-size: 8.0pt;
    margin: 5pt 0 7pt 0;
    page-break-inside: avoid;
  }

  th, td {
    border: 1px solid #cbd5e1;
    padding: 3.2pt 4.8pt;
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
    margin: 5pt 0 4pt 0;
    page-break-inside: avoid;
  }

  img {
    max-width: 95%;
    max-height: 180px;
    height: auto;
    object-fit: contain;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  }

  /* Code Blocks - Pure White Background, Black/Navy Text */
  pre {
    background: #ffffff;
    color: #0f172a;
    padding: 6pt 8pt;
    border-radius: 4px;
    font-family: "Consolas", "Courier New", monospace;
    font-size: 7.7pt;
    line-height: 1.34;
    overflow-x: auto;
    margin: 4pt 0 6pt 0;
    page-break-inside: avoid;
    border: 1px solid #cbd5e1;
    border-left: 3.5px solid #2563eb;
  }

  code {
    font-family: "Consolas", "Courier New", monospace;
    font-size: 8.1pt;
    background-color: #f1f5f9;
    color: #1e3a8a;
    padding: 1px 3px;
    border-radius: 3px;
  }

  pre code {
    background-color: transparent;
    color: inherit;
    padding: 0;
  }

  .math-display {
    text-align: center;
    margin: 4pt 0;
    page-break-inside: avoid;
  }

  /* Exam Banner - Clean Light Theme, Zero Black Background */
  .exam-banner {
    background-color: #eff6ff;
    border: 1.5px solid #1e3a8a;
    border-left: 5px solid #1e3a8a;
    color: #1e3a8a;
    padding: 9pt 13pt;
    border-radius: 5px;
    margin-bottom: 9pt;
    page-break-inside: avoid;
  }

  .exam-banner h1 {
    color: #1e3a8a;
    border: none;
    margin: 0 0 3pt 0;
    font-size: 13.5pt;
    letter-spacing: -0.2px;
  }

  .exam-banner p {
    margin: 1.5pt 0;
    font-size: 8.2pt;
    color: #1e40af;
  }

  blockquote {
    border-left: 3px solid #1e3a8a;
    margin: 4pt 0;
    padding: 3pt 9pt;
    background-color: #eff6ff;
    color: #1e3a8a;
    font-size: 8.1pt;
  }
</style>
</head>
<body>
{{CONTENT}}
</body>
</html>
"""

def render_markdown_with_protected_math(md_text, base_dir):
    display_blocks = []
    inline_blocks = []

    def save_display(m):
        idx = len(display_blocks)
        display_blocks.append(m.group(1).strip())
        return f"XQDMATH{idx}MQX"

    def save_inline(m):
        idx = len(inline_blocks)
        inline_blocks.append(m.group(1).strip())
        return f"XQIMATH{idx}MQX"

    def replace_img(match):
        alt = match.group(1)
        src = match.group(2)
        full_path = os.path.normpath(os.path.join(base_dir, src))
        if os.path.exists(full_path):
            ext = os.path.splitext(full_path)[1].lower().replace('.', '')
            mime = 'jpeg' if ext in ['jpg', 'jpeg'] else 'png'
            with open(full_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode('utf-8')
            return f'<div class="img-container"><img src="data:image/{mime};base64,{b64}" alt="{alt}"/></div>'
        return match.group(0)

    # 1. Protect images
    text = re.sub(r'!\[(.*?)\]\((.*?)\)', replace_img, md_text)

    # 2. Protect display math $$ ... $$
    text = re.sub(r'\$\$(.*?)\$\$', save_display, text, flags=re.DOTALL)

    # 3. Protect inline math $ ... $
    inline_pattern = r'(?<!\\)\$((?:\\\$|[^$\n])+?)(?<!\\)\$'
    text = re.sub(inline_pattern, save_inline, text)

    # 4. Render markdown
    md = markdown_it.MarkdownIt("commonmark", {"html": True, "breaks": True})
    md.enable(["table", "strikethrough"])
    html = md.render(text)

    # 5. Restore math into dedicated targeted elements
    for idx, raw in enumerate(display_blocks):
        html = html.replace(f"XQDMATH{idx}MQX", f'<div class="math-display">{raw}</div>')

    for idx, raw in enumerate(inline_blocks):
        html = html.replace(f"XQIMATH{idx}MQX", f'<span class="math-inline">{raw}</span>')

    return html

def compile_toc_pdf():
    md_file = os.path.join(BASE_DIR, "TOC_CAT2_FOOLPROOF_SOLVE_BOOKLET.md")
    temp_html = os.path.join(BASE_DIR, "temp_toc_booklet.html")
    out_pdf = os.path.join(PDF_OUT_DIR, "TOC_CAT2_FOOLPROOF_SOLVE_BOOKLET.pdf")

    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    banner_html = """
    <div class="exam-banner">
        <h1>CSE2004: THEORY OF COMPUTATION & COMPILER DESIGN — CAT-II FOOLPROOF SPEEDRUN</h1>
        <p><strong>Course:</strong> CSE2004 — Theory of Computation & Compiler Design | <strong>Exam:</strong> CAT-2 (Open Book Master Reference)</p>
        <p><strong>Coverage:</strong> 100% Official Syllabus Blueprint: Top-Down/Bottom-Up Parsing (SLR, CLR, LALR) & 5 Master Turing Machines</p>
    </div>
    """

    rendered_body = render_markdown_with_protected_math(md_text, BASE_DIR)
    full_html = HTML_TEMPLATE.replace("{{CONTENT}}", banner_html + "\n" + rendered_body)

    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(full_html)

    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--virtual-time-budget=5000",
        "--run-all-compositor-stages-before-draw",
        "--no-pdf-header-footer",
        f"--print-to-pdf={out_pdf}",
        temp_html
    ]
    
    print("Compiling TOC PDF via Chrome Headless...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Chrome error:", res.stderr)
        return

    if os.path.exists(temp_html):
        os.remove(temp_html)

    reader = pypdf.PdfReader(out_pdf)
    num_pages = len(reader.pages)
    file_size_kb = os.path.getsize(out_pdf) / 1024
    print(f"SUCCESS! Generated {out_pdf}")
    print(f"Total Pages: {num_pages} pages | File Size: {file_size_kb:.1f} KB")

if __name__ == "__main__":
    compile_toc_pdf()
