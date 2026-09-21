"""
High-Precision Academic PDF Exporter for DLD CAT-2 Notes Suite
Converts Markdown to vector-crisp, printable A4 PDFs with:
- KaTeX Math formulas (equations, arrays, truth/state tables)
- Embedded ANSI/IEEE logic gate schematics and waveforms (Base64)
- Academic typography, zebra-striped tables, and callout boxes
- Dynamic page numbering ('Page X of Y') and subject header banners
- Individual PDFs + All-in-One Master Exam Booklet
"""

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

# ----------------- HTML & PRINT STYLING TEMPLATE -----------------

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{doc_title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
  mermaid.initialize({{
    startOnLoad: true,
    theme: 'base',
    themeVariables: {{
      primaryColor: '#eff6ff',
      primaryBorderColor: '#2563eb',
      primaryTextColor: '#0f172a',
      lineColor: '#1e293b',
      edgeLabelBackground: '#ffffff',
      fontSize: '13px'
    }}
  }});
</script>
<style>
  @page {{
    size: A4;
    margin: 14mm 14mm 14mm 14mm;
  }}
  
  *, *::before, *::after {{
    box-sizing: border-box;
  }}

  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 9.5pt;
    line-height: 1.48;
    color: #0f172a;
    background: #ffffff;
    margin: 0;
    padding: 0;
  }}

  h1 {{
    font-size: 16pt;
    color: #1e3a8a;
    border-bottom: 2.5px solid #1e3a8a;
    padding-bottom: 5px;
    margin-top: 16pt;
    margin-bottom: 8pt;
    page-break-after: avoid;
  }}

  h2 {{
    font-size: 13pt;
    color: #1e293b;
    border-bottom: 1.5px solid #cbd5e1;
    padding-bottom: 3px;
    margin-top: 14pt;
    margin-bottom: 6pt;
    page-break-after: avoid;
  }}

  h3 {{
    font-size: 11pt;
    color: #334155;
    margin-top: 11pt;
    margin-bottom: 4pt;
    page-break-after: avoid;
  }}

  h4 {{
    font-size: 10pt;
    color: #475569;
    margin-top: 9pt;
    margin-bottom: 3pt;
    page-break-after: avoid;
  }}

  p {{
    margin: 4pt 0 6pt 0;
  }}

  ul, ol {{
    margin: 4pt 0 6pt 0;
    padding-left: 20px;
  }}

  li {{
    margin-bottom: 2.5pt;
  }}

  hr {{
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 12pt 0;
  }}

  /* Table styling - Essential for Truth/State/Excitation tables */
  table {{
    border-collapse: collapse;
    width: 100%;
    margin: 8pt 0;
    font-size: 8.8pt;
    page-break-inside: avoid;
  }}

  th {{
    background-color: #1e293b;
    color: #ffffff;
    font-weight: 600;
    padding: 5px 8px;
    border: 1px solid #94a3b8;
    text-align: center;
  }}

  td {{
    padding: 4px 7px;
    border: 1px solid #cbd5e1;
    text-align: center;
  }}

  tr:nth-child(even) td {{
    background-color: #f8fafc;
  }}

  /* Schematics & Images */
  .img-container {{
    text-align: center;
    margin: 10pt 0 6pt 0;
    page-break-inside: avoid;
  }}

  img {{
    max-width: 95%;
    max-height: 380px;
    height: auto;
    object-fit: contain;
    border: 1px solid #cbd5e1;
    border-radius: 5px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
  }}

  .caption {{
    font-size: 8pt;
    color: #475569;
    font-style: italic;
    margin-top: 3pt;
    margin-bottom: 8pt;
    text-align: center;
    page-break-after: avoid;
  }}

  /* Mermaid State Diagrams */
  .mermaid-container {{
    text-align: center;
    margin: 10pt 0 8pt 0;
    page-break-inside: avoid;
  }}

  .mermaid {{
    display: inline-block;
  }}

  .mermaid svg {{
    max-width: 85%;
    max-height: 340px;
    height: auto;
  }}

  /* Math rendering */
  .katex {{
    font-size: 1.05em;
  }}

  .math-display {{
    text-align: center;
    margin: 6pt 0;
    page-break-inside: avoid;
    overflow-x: auto;
  }}

  /* Code & Preformatted */
  code {{
    font-family: "Consolas", "Courier New", monospace;
    background: #f1f5f9;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 8.5pt;
    border: 1px solid #e2e8f0;
  }}

  pre {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 5px;
    padding: 8pt;
    font-size: 8pt;
    page-break-inside: avoid;
    overflow-x: auto;
  }}

  pre code {{
    background: none;
    border: none;
    padding: 0;
  }}

  /* Blockquotes & Callouts */
  blockquote {{
    border-left: 3.5px solid #3b82f6;
    background: #eff6ff;
    padding: 6pt 10pt;
    margin: 6pt 0;
    border-radius: 0 4px 4px 0;
    page-break-inside: avoid;
  }}

  .exam-banner {{
    background: linear-gradient(135deg, #1e3a8a 0%, #1e293b 100%);
    color: #ffffff;
    padding: 12pt 16pt;
    border-radius: 6px;
    margin-bottom: 14pt;
  }}

  .exam-banner h1 {{
    color: #ffffff;
    border-bottom: 1px solid rgba(255, 255, 255, 0.25);
    margin-top: 0;
    padding-bottom: 4pt;
  }}

  .exam-banner p {{
    margin: 2pt 0;
    font-size: 9pt;
    color: #e2e8f0;
  }}

  .page-break {{
    page-break-after: always;
  }}
</style>
</head>
<body>
{content_html}

<script>
document.addEventListener("DOMContentLoaded", function() {{
    renderMathInElement(document.body, {{
        delimiters: [
            {{left: "$$", right: "$$", display: true}},
            {{left: "$", right: "$", display: false}}
        ],
        throwOnError: false
    }});
}});
</script>
</body>
</html>
"""

# ----------------- MARKDOWN PROCESSOR -----------------

def markdown_to_print_html(md_text, base_dir, doc_title="DLD Notes", cover_html=""):
    """
    Transforms markdown into print-ready HTML:
    - Protects LaTeX math from CommonMark asterisks/underscores
    - Embeds local images as Base64 data URIs
    - Wraps captions and math blocks nicely
    """
    math_blocks = []

    def save_display(m):
        idx = len(math_blocks)
        math_blocks.append(('display', m.group(1)))
        return f"XQDMATH{idx}MQX"

    def save_inline(m):
        idx = len(math_blocks)
        math_blocks.append(('inline', m.group(1)))
        return f"XQIMATH{idx}MQX"

    # 1. Protect display and inline math
    protected = re.sub(r'\$\$(.*?)\$\$', save_display, md_text, flags=re.DOTALL)
    protected = re.sub(r'\$([^\$\n]+?)\$', save_inline, protected)

    # 2. Render markdown to HTML
    md_parser = markdown_it.MarkdownIt('commonmark').enable('table')
    html = md_parser.render(protected)

    # 3. Restore LaTeX math
    for idx, (mtype, raw) in enumerate(math_blocks):
        if mtype == 'display':
            html = html.replace(f"XQDMATH{idx}MQX", f'<div class="math-display">$${raw}$$</div>')
        else:
            html = html.replace(f"XQIMATH{idx}MQX", f'<span class="math-inline">${raw}$</span>')

    # 4. Embed Images as Base64 data URIs
    def replace_img_tag(match):
        src = match.group(1)
        alt = match.group(2)
        if not os.path.isabs(src):
            img_path = os.path.normpath(os.path.join(base_dir, src))
        else:
            img_path = src

        if os.path.exists(img_path):
            ext = os.path.splitext(img_path)[1].lower()
            mime = "image/png" if ext == ".png" else "image/svg+xml" if ext == ".svg" else "image/jpeg"
            with open(img_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode('utf-8')
            return f'<div class="img-container"><img src="data:{mime};base64,{b64}" alt="{alt}"></div>'
        else:
            print(f"Warning: Image not found at {img_path}")
            return match.group(0)

    html = re.sub(r'<img src="([^"]+)" alt="([^"]*)"\s*/?>', replace_img_tag, html)

    # Also style figure captions: *(Figure X.Y: ...)*
    html = re.sub(r'<p>\s*\*\((Figure [^\)]+)\)\*\s*</p>', r'<div class="caption">(\1)</div>', html)

    # Convert code-fenced mermaid into <div class="mermaid">
    html = re.sub(r'<pre><code class="language-mermaid">([\s\S]*?)</code></pre>', r'<div class="mermaid-container"><div class="mermaid">\1</div></div>', html)

    full_content = cover_html + html if cover_html else html
    return HTML_TEMPLATE.format(doc_title=doc_title, content_html=full_content)


# ----------------- PLAYWRIGHT PDF GENERATION -----------------

def render_html_to_pdf(playwright, html_content, output_pdf_path, header_title="ECE2002: Digital Logic Design"):
    """Renders HTML string to PDF using Playwright Chromium with dynamic headers and footers"""
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # Load HTML with wait until network idle (so KaTeX scripts load completely)
    page.set_content(html_content, wait_until="networkidle")

    # Give KaTeX and Mermaid auto-render time to format all formulas and SVGs in the DOM
    page.wait_for_timeout(3500)

    # Standard academic header & footer template
    header_tmpl = f"""
    <div style="font-family: -apple-system, sans-serif; font-size: 7.5pt; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 14mm;">
        <span style="font-weight: bold; color: #1e3a8a;">{header_title}</span>
        <span>CAT-2 Open-Book Handwritten/Printed Master Reference</span>
    </div>
    """

    footer_tmpl = """
    <div style="font-family: -apple-system, sans-serif; font-size: 7.5pt; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 14mm;">
        <span>VIT School of Electronics Engineering (SENSE)</span>
        <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
    </div>
    """

    page.pdf(
        path=output_pdf_path,
        format="A4",
        print_background=True,
        display_header_footer=True,
        header_template=header_tmpl,
        footer_template=footer_tmpl,
        margin={
            "top": "16mm",
            "bottom": "16mm",
            "left": "12mm",
            "right": "12mm"
        }
    )
    browser.close()
    print(f"✅ Generated: {output_pdf_path}")


# ----------------- MAIN PIPELINE -----------------

def main():
    print("🚀 Starting High-Precision DLD CAT-2 PDF Export...")

    files_to_export = [
        {
            "src": os.path.join(BASE_DIR, "cat2-hots-module3-sequential-circuits.md"),
            "pdf": os.path.join(PDF_OUT_DIR, "DLD_CAT2_Module3_Sequential_Circuits.pdf"),
            "title": "DLD Module 3: Sequential Circuits & Latches",
            "header": "DLD CAT-2 | Module 3: Sequential Circuits, Flip-Flops & Registers"
        },
        {
            "src": os.path.join(BASE_DIR, "cat2-hots-module4-registers-counters-fsm.md"),
            "pdf": os.path.join(PDF_OUT_DIR, "DLD_CAT2_Module4_Counters_and_FSM.pdf"),
            "title": "DLD Module 4: Counters, Registers & FSM",
            "header": "DLD CAT-2 | Module 4: Asynchronous/Synchronous Counters & FSM"
        },
        {
            "src": os.path.join(BASE_DIR, "cat2-dld-assignment-4-and-class-cases-solved.md"),
            "pdf": os.path.join(PDF_OUT_DIR, "DLD_CAT2_Assignment4_Solved.pdf"),
            "title": "DLD Assignment 4 Solved (With IEEE Gate Schematics)",
            "header": "DLD CAT-2 | Assignment 4 Solved Archetypes"
        },
        {
            "src": os.path.join(BASE_DIR, "cat2-dld-assignment-5-solved.md"),
            "pdf": os.path.join(PDF_OUT_DIR, "DLD_CAT2_Assignment5_Solved.pdf"),
            "title": "DLD Assignment 5 Solved (With IEEE Gate Schematics)",
            "header": "DLD CAT-2 | Assignment 5 Solved Archetypes"
        }
    ]

    with sync_playwright() as p:
        # 1. Export 4 Individual PDFs
        all_md_sections = []
        for item in files_to_export:
            print(f"\nProcessing: {os.path.basename(item['src'])}...")
            with open(item["src"], "r", encoding="utf-8") as f:
                md_content = f.read()

            all_md_sections.append(md_content)
            html_out = markdown_to_print_html(md_content, BASE_DIR, doc_title=item["title"])
            render_html_to_pdf(p, html_out, item["pdf"], header_title=item["header"])

        # 2. Export All-in-One Master Exam Booklet
        print("\n📚 Generating Comprehensive All-in-One Master Exam Booklet...")
        booklet_cover = """
<div class="exam-banner" style="text-align: center; padding: 25pt 15pt; margin-top: 20pt; margin-bottom: 25pt;">
    <h1 style="font-size: 22pt; margin-bottom: 6pt;">⚡ ECE2002 — DIGITAL LOGIC DESIGN (CAT-2)</h1>
    <h2 style="color: #93c5fd; font-size: 14pt; font-weight: normal; margin-top: 0; border: none;">COMPLETE OPEN-BOOK PRINTABLE MASTER EXAM SUITE</h2>
    <p style="font-size: 10pt; color: #e2e8f0; margin-top: 10pt;">
        <b>Coverage</b>: Module 3 (Sequential Circuits & Flip-Flops) • Module 4 (Counters, Registers & FSM) • Assignment 4 Solved • Assignment 5 Solved
    </p>
    <p style="font-size: 9pt; color: #cbd5e1;">
        Format: Self-Contained Step-by-Step Derivations • Full Truth/Excitation Tables • K-Maps • Exact IEEE Logic Schematics
    </p>
</div>

<div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 6px; padding: 12pt 16pt; margin-bottom: 20pt;">
    <h3 style="margin-top: 0; color: #1e3a8a;">📖 Booklet Table of Contents</h3>
    <ol style="margin-bottom: 0; line-height: 1.7; font-size: 9.5pt;">
        <li><b>Part 1: Module 3 Sequential Circuits & Flip-Flops HOTS Master</b> — <i>SR, JK, D, T Flip-Flops, Master-Slave Race-Around Solution, Universal FF Conversions, 4-Bit Registers (SISO/SIPO/PISO/PIPO), Ring & Johnson Counters, 74LS194 USR, State Reduction.</i></li>
        <li><b>Part 2: Module 4 Counters & Finite State Machines HOTS Master</b> — <i>Asynchronous Ripple Up/Down Rules, Mod-6 Truncated Counter with NAND Reset, 3-Bit Synchronous Binary Up Counter, Mealy vs. Moore Models, Up/Down Mode Steering, BCD Mod-10 Synchronous Counter, Gray Code Counter, Arbitrary Sequence Counter & Lockout Proof.</i></li>
        <li><b>Part 3: Assignment 4 Fully Solved Problem Set</b> — <i>Q1 SR Latch Metastability, Q2 Positive Edge-Triggered T Flip-Flop NAND & 6-Clock Waveform, Q3 Sequential Analysis, Q4 Arbitrary Synchronous Counter with D FFs, Q5 Decade Asynchronous Ripple Counter.</i></li>
        <li><b>Part 4: Assignment 5 Fully Solved Problem Set</b> — <i>Q1 Mod-5 Prime Number Counter (2,3,5,7,11) with JK FFs, Q2 Autonomous Toy Robot FSM, Q3 4-Bit SISO Serial Shift Register Trace, Q4 4-Bit Ring Counter Lockout Self-Correction, Q5 1010 Overlapping Mealy Sequence Detector.</i></li>
    </ol>
</div>
<div class="page-break"></div>
"""
        # Combine all markdown texts with page breaks
        combined_md = "\n\n<div class=\"page-break\"></div>\n\n".join(all_md_sections)
        combined_html_body = markdown_to_print_html(combined_md, BASE_DIR, doc_title="DLD CAT-2 Master Exam Booklet", cover_html=booklet_cover)
        master_booklet_pdf = os.path.join(PDF_OUT_DIR, "DLD_CAT2_COMPLETE_MASTER_EXAM_BOOKLET.pdf")
        render_html_to_pdf(p, combined_html_body, master_booklet_pdf, header_title="ECE2002 DLD | CAT-2 COMPLETE MASTER EXAM BOOKLET")

    print("\n🎉 ALL PDFs SUCCESSFULLY GENERATED IN:")
    print(PDF_OUT_DIR)

if __name__ == "__main__":
    main()
