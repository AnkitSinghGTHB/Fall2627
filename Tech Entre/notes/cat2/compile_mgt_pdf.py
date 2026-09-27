import os
import re
import sys
import markdown_it
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\ankit\Fall2627\Tech Entre\notes\cat2"
PDF_OUT_DIR = os.path.join(BASE_DIR, "pdf")
os.makedirs(PDF_OUT_DIR, exist_ok=True)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>MGT2003: Technology Entrepreneurship — CAT-II Master Handwritten Copy Booklet</title>
<style>
  @page {
    size: A4;
    margin: 10mm 11mm 10mm 11mm;
  }
  
  *, *::before, *::after {
    box-sizing: border-box;
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 8.2pt;
    line-height: 1.34;
    color: #0f172a;
    background: #ffffff;
    margin: 0;
    padding: 0;
  }

  /* Exam Main Banner */
  .exam-banner {
    background: linear-gradient(135deg, #1e3a8a 0%, #1e1b4b 100%);
    color: #ffffff;
    padding: 8pt 12pt;
    border-radius: 5px;
    margin-bottom: 8pt;
    border-bottom: 3px solid #3b82f6;
  }

  .exam-banner h1 {
    color: #ffffff !important;
    background: transparent !important;
    border: none !important;
    border-left: none !important;
    margin: 0 0 3pt 0;
    padding: 0;
    font-size: 12.5pt;
    font-weight: 800;
    letter-spacing: -0.2px;
  }

  .exam-banner p {
    margin: 2pt 0;
    font-size: 7.8pt;
    color: #cbd5e1;
    line-height: 1.3;
  }

  .exam-banner strong {
    color: #ffffff;
  }

  .banner-badge {
    display: inline-block;
    background: #3b82f6;
    color: #ffffff;
    padding: 1pt 5pt;
    border-radius: 3px;
    font-size: 7.2pt;
    font-weight: 700;
    text-transform: uppercase;
    margin-right: 4pt;
  }

  /* Notebook Page Section - Each starts on a fresh page */
  .notebook-page-section {
    page-break-before: always;
    break-before: page;
  }
  
  .notebook-page-section:first-child {
    page-break-before: avoid;
    break-before: avoid;
  }

  /* Section Headings */
  h1 {
    font-size: 10.5pt;
    color: #1e3a8a;
    background: #f1f5f9;
    border-left: 4.5px solid #2563eb;
    padding: 3pt 6pt;
    margin-top: 2pt;
    margin-bottom: 3.5pt;
    border-radius: 0 4px 4px 0;
    page-break-after: avoid;
    break-after: avoid;
  }

  h2 {
    font-size: 9.2pt;
    color: #0369a1;
    border-bottom: 1.5px solid #e2e8f0;
    padding-bottom: 1pt;
    margin-top: 5pt;
    margin-bottom: 2pt;
    page-break-after: avoid;
    break-after: avoid;
  }

  h3 {
    font-size: 8.4pt;
    color: #0f766e;
    margin-top: 4pt;
    margin-bottom: 1.5pt;
    page-break-after: avoid;
    break-after: avoid;
    font-weight: 700;
  }

  h4 {
    font-size: 8.0pt;
    color: #334155;
    margin-top: 3pt;
    margin-bottom: 1pt;
    page-break-after: avoid;
    break-after: avoid;
  }

  p {
    margin-top: 1pt;
    margin-bottom: 2pt;
  }

  ul, ol {
    margin-top: 1pt;
    margin-bottom: 2.5pt;
    padding-left: 13pt;
  }

  li {
    margin-bottom: 1pt;
  }

  strong {
    color: #090d16;
    font-weight: 700;
  }

  /* Inline Code */
  code {
    font-family: "Cascadia Code", "Fira Code", Consolas, Monaco, monospace;
    font-size: 7.2pt;
    background: #f1f5f9;
    color: #0f172a;
    padding: 0.5pt 2.5pt;
    border-radius: 2px;
    border: 1px solid #e2e8f0;
  }

  /* ASCII Diagram & Code Blocks */
  pre {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 3.5px solid #3b82f6;
    border-radius: 3px;
    padding: 3.5pt 6pt;
    margin: 2.5pt 0 3.5pt 0;
    overflow-x: auto;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  pre code {
    background: transparent;
    padding: 0;
    border: none;
    font-size: 6.8pt;
    line-height: 1.20;
    color: #0f172a;
    font-family: "Cascadia Code", "Fira Code", Consolas, Monaco, monospace;
    white-space: pre;
  }

  /* Callouts & Blockquotes */
  blockquote {
    margin: 2.5pt 0;
    padding: 2.5pt 7pt;
    background: #eff6ff;
    border-left: 3.5px solid #3b82f6;
    border-radius: 0 3px 3px 0;
    color: #1e40af;
    font-size: 7.6pt;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  blockquote p {
    margin: 0.5pt 0;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 2.5pt 0 3.5pt 0;
    font-size: 7.2pt;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  th, td {
    border: 1px solid #cbd5e1;
    padding: 2.2pt 4pt;
    text-align: left;
    vertical-align: top;
    line-height: 1.25;
  }

  th {
    background-color: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
    border-bottom: 2px solid #94a3b8;
  }

  tr:nth-child(even) td {
    background-color: #f8fafc;
  }

  hr {
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 4pt 0;
  }

  .highlight-badge {
    background: #fef08a;
    color: #854d0e;
    padding: 0.5pt 3pt;
    border-radius: 2px;
    font-weight: 700;
    font-size: 7.2pt;
  }
</style>
</head>
<body>

{content_html}

</body>
</html>
"""

def compile_mgt_pdf():
    md_file = os.path.join(BASE_DIR, "MGT2003_CAT2_HANDWRITTEN_COPY_MASTER.md")
    out_pdf = os.path.join(PDF_OUT_DIR, "MGT2003_CAT2_MASTER_NOTES.pdf")

    if not os.path.exists(md_file):
        print(f"Error: {md_file} not found!")
        return

    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    md_text = md_text.replace(r"($1\times$ participating)", "(1x participating)")
    md_text = md_text.replace(r"$1\times$", "1x")

    # Parse markdown to HTML
    md_parser = markdown_it.MarkdownIt('default', options_update={'html': True}).enable('table')
    html = md_parser.render(md_text)

    # Style the first banner blockquote specially
    # Replace top title and first blockquote with an exam banner
    def create_banner(m):
        title = m.group(1).strip()
        body = m.group(2).strip()
        # convert body lines to p tags
        lines = [line.strip('> ').strip() for line in body.split('\n') if line.strip()]
        body_p = "".join([f"<p>{l}</p>" for l in lines])
        return f"""
        <div class="exam-banner">
            <h1>{title}</h1>
            {body_p}
        </div>
        """

    # Match H1 at start followed by blockquote
    banner_regex = r"<h1>(.*?)</h1>\s*<blockquote>(.*?)</blockquote>"
    html = re.sub(banner_regex, create_banner, html, count=1, flags=re.DOTALL)

    # Split HTML by Notebook Pages so each Notebook Page gets its own clean A4 page
    parts = re.split(r"(?:<hr\s*/?>\s*)?<h1>📑\s*NOTEBOOK PAGE", html)
    if len(parts) > 1:
        sections = []
        # First section combines banner + Page 1
        sec1 = parts[0] + "<h1>📑 NOTEBOOK PAGE" + parts[1]
        sections.append(f'<div class="notebook-page-section">\n{sec1}\n</div>')
        for p in parts[2:]:
            sec = "<h1>📑 NOTEBOOK PAGE" + p
            sections.append(f'<div class="notebook-page-section">\n{sec}\n</div>')
        html = "\n".join(sections)

    full_html = HTML_TEMPLATE.replace("{content_html}", html)

    # Save debug HTML
    debug_html_path = os.path.join(BASE_DIR, "debug_mgt_print.html")
    with open(debug_html_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.set_content(full_html, wait_until="networkidle")
        page.wait_for_timeout(2000)

        header_template = """
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 6.8pt; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 11mm;">
            <span><strong>MGT2003: Technology Entrepreneurship</strong> — CAT-II Master Handwritten Copy Booklet</span>
            <span>VIT Bhopal University — Fall 2026-27</span>
        </div>
        """

        footer_template = """
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 6.8pt; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 11mm;">
            <span>Prof. Brahmadev Panda (Modules 3 & 4: IPR, Tech Transfer, Incubators, Funding)</span>
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
                "top": "11mm",
                "bottom": "11mm",
                "left": "11mm",
                "right": "11mm"
            }
        )
        browser.close()

    print(f"Successfully generated PDF: {out_pdf}")

if __name__ == "__main__":
    compile_mgt_pdf()
