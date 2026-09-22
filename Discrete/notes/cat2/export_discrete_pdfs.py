"""
High-Precision Academic PDF Exporter for Discrete Mathematics & Graph Theory (MAT2002) CAT-2 Suite
Strict Syllabus Scope: Module 3 (Lattices & Boolean Algebra) and Module 4 (Graphs & Matrix Representations)

Features:
- KaTeX Math formulas (equations, matrices, sets, logic propositions, Havel-Hakimi)
- Embedded Graph Figures and Schematics (Base64 encoded for zero-latency local rendering)
- Academic typography, zebra-striped tables, and callout boxes
- Dynamic page numbering ('Page X of Y') and subject header banners
- Generates 5 standalone topic PDFs + 1 All-in-One Master Exam Booklet
"""

import os
import re
import sys
import base64
import markdown_it
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\ankit\Fall2627\Discrete\notes\cat2"
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
    font-size: 9.2pt;
    line-height: 1.45;
    color: #0f172a;
    background: #ffffff;
    margin: 0;
    padding: 0;
  }}

  h1 {{
    font-size: 15pt;
    color: #1e3a8a;
    border-bottom: 2px solid #1e3a8a;
    padding-bottom: 4px;
    margin-top: 14pt;
    margin-bottom: 6pt;
    page-break-after: avoid;
  }}

  h2 {{
    font-size: 12.5pt;
    color: #1e293b;
    border-bottom: 1.2px solid #cbd5e1;
    padding-bottom: 3px;
    margin-top: 12pt;
    margin-bottom: 5pt;
    page-break-after: avoid;
  }}

  h3 {{
    font-size: 10.5pt;
    color: #334155;
    margin-top: 10pt;
    margin-bottom: 3pt;
    page-break-after: avoid;
  }}

  h4 {{
    font-size: 9.5pt;
    color: #475569;
    margin-top: 8pt;
    margin-bottom: 2pt;
    page-break-after: avoid;
  }}

  p {{
    margin: 4pt 0 6pt 0;
  }}

  ul, ol {{
    margin: 4pt 0 6pt 16pt;
    padding: 0;
  }}

  li {{
    margin-bottom: 2.5pt;
  }}

  hr {{
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 10pt 0;
  }}

  /* Tables */
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 8.5pt;
    margin: 8pt 0 10pt 0;
    page-break-inside: avoid;
  }}

  th, td {{
    border: 1px solid #cbd5e1;
    padding: 4pt 6pt;
    text-align: left;
    vertical-align: top;
  }}

  th {{
    background-color: #f1f5f9;
    color: #1e293b;
    font-weight: 600;
  }}

  tr:nth-child(even) {{
    background-color: #f8fafc;
  }}

  /* Images */
  .img-container {{
    text-align: center;
    margin: 10pt 0 6pt 0;
    page-break-inside: avoid;
  }}

  img {{
    max-width: 90%;
    max-height: 320px;
    height: auto;
    object-fit: contain;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  }}

  .caption {{
    font-size: 8pt;
    color: #475569;
    font-style: italic;
    margin-top: 3pt;
    margin-bottom: 6pt;
    text-align: center;
    page-break-after: avoid;
  }}

  /* Math rendering */
  .katex {{
    font-size: 1.05em;
  }}

  .math-display {{
    text-align: center;
    margin: 5pt 0;
    page-break-inside: avoid;
    overflow-x: auto;
  }}

  /* Code & Preformatted */
  code {{
    font-family: "Consolas", "Courier New", monospace;
    background: #f1f5f9;
    padding: 1px 3px;
    border-radius: 3px;
    font-size: 8.2pt;
    border: 1px solid #e2e8f0;
  }}

  pre {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 6pt;
    font-size: 7.8pt;
    line-height: 1.35;
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
    border-left: 3.5px solid #2563eb;
    background: #eff6ff;
    padding: 5pt 8pt;
    margin: 5pt 0;
    border-radius: 0 4px 4px 0;
    page-break-inside: avoid;
  }}

  .exam-banner {{
    background: linear-gradient(135deg, #1e3a8a 0%, #1e293b 100%);
    color: #ffffff;
    padding: 10pt 14pt;
    border-radius: 5px;
    margin-bottom: 12pt;
  }}

  .exam-banner h1 {{
    color: #ffffff;
    border-bottom: 1px solid rgba(255, 255, 255, 0.25);
    margin-top: 0;
    padding-bottom: 3pt;
  }}

  .exam-banner p {{
    margin: 2pt 0;
    font-size: 8.8pt;
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

def markdown_to_print_html(md_text, base_dir, doc_title="Discrete Math Notes", cover_html=""):
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

    # 0. Pre-process Markdown image tags ![alt](src) into Base64 HTML blocks
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

    # Combine cover and content
    full_body = cover_html + html
    return HTML_TEMPLATE.format(doc_title=doc_title, content_html=full_body)

# ----------------- PLAYWRIGHT PDF EXPORT ENGINE -----------------

def export_html_to_pdf(page, html_content, output_pdf_path, header_title="MAT2002: Discrete Mathematics"):
    """
    Renders HTML in Chromium and prints to vector A4 PDF with KaTeX and page numbering.
    """
    page.set_content(html_content, wait_until="networkidle")

    # Give KaTeX and browser fonts time to render
    page.wait_for_timeout(1500)

    # Header and Footer Template for open-book college exam format
    header_template = f"""
    <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 7pt; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 14mm;">
        <span><strong>MAT2002: Discrete Mathematics & Graph Theory</strong> — {header_title}</span>
        <span>CAT-2 Open-Book Exam Suite</span>
    </div>
    """

    footer_template = """
    <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 7.5pt; color: #64748b; width: 100%; display: flex; justify-content: space-between; padding: 0 14mm;">
        <span>Modules 3 & 4 (Lattices, Boolean Algebra, Graph Theory & Matrix Representations)</span>
        <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
    </div>
    """

    page.pdf(
        path=output_pdf_path,
        format="A4",
        print_background=True,
        display_header_footer=True,
        header_template=header_template,
        footer_template=footer_template,
        margin={
            "top": "16mm",
            "bottom": "16mm",
            "left": "14mm",
            "right": "14mm"
        }
    )
    print(f"Generated PDF: {os.path.basename(output_pdf_path)}")

# ----------------- MAIN PIPELINE -----------------

DOCUMENTS = [
    {
        "id": "decoder",
        "file": "cat2-exam-questionnaire-decoder.md",
        "pdf_name": "Discrete_CAT2_Questionnaire_Exam_Decoder.pdf",
        "title": "EXAM QUESTION-LANGUAGE DECODER & QUESTIONNAIRE BANK",
        "banner_sub": "Instant Keyword Trigger Matrix + 18 Exam Problem Archetypes with Plug-and-Play Solution Templates & Common Traps"
    },
    {
        "id": "actual_paper",
        "file": "cat2-actual-paper-sep2026-solved.md",
        "pdf_name": "Discrete_CAT2_Actual_Paper_Sep2026_Solved.pdf",
        "title": "VIT BHOPAL CAT-II OFFICIAL PAPER (SEP 2026) — COMPLETE SOLUTIONS",
        "banner_sub": "All 5 Compulsory Questions Solved: Distributive Median Proof, Boolean Tuple PDNF/PCNF, D12, Handshaking Partition, C6 Isomorphism & Floyd-Warshall"
    },
    {
        "id": "quiz2",
        "file": "cat2-discrete-quiz-2-solved.md",
        "pdf_name": "Discrete_CAT2_Quiz2_Solved.pdf",
        "title": "QUIZ-2 Master Solutions (Module 4 Graphs)",
        "banner_sub": "Faculty: Dr. Suresh Dara | 8 Solved Problems on Complements, Havel-Hakimi, Isomorphism & Degree Proofs"
    },
    {
        "id": "tut4",
        "file": "cat2-discrete-tutorial-4-dijkstra-solved.md",
        "pdf_name": "Discrete_CAT2_Tutorial4_Dijkstra_Solved.pdf",
        "title": "TUTORIAL-4 Master Solutions (Dijkstra Shortest Path)",
        "banner_sub": "Faculty: Dr. Suresh Dara | Full Iteration Tables, Predecessor Updates, Pre-drawn Digraphs & Shortest Path Trees"
    },
    {
        "id": "tut2",
        "file": "cat2-discrete-tutorial-2-solved.md",
        "pdf_name": "Discrete_CAT2_Tutorial2_Solved.pdf",
        "title": "TUTORIAL-2 Master Solutions (Posets, Relations & Lattices)",
        "banner_sub": "Lexicographical Order on R^2, Relation Compositions & Inverses, D12 Divisor Lattice & Complementation"
    },
    {
        "id": "mod3",
        "file": "cat2-hots-module3-lattices-boolean.md",
        "pdf_name": "Discrete_CAT2_Module3_Lattices_Boolean.pdf",
        "title": "MODULE 3: Lattices & Boolean Algebra Master Notes",
        "banner_sub": "Posets, Hasse Diagrams, Distributive/Modular/Bounded/Complemented Lattices, PDNF/PCNF & Switching Circuits"
    },
    {
        "id": "mod4",
        "file": "cat2-hots-module4-graphs-matrices.md",
        "pdf_name": "Discrete_CAT2_Module4_Graphs_and_Matrices.pdf",
        "title": "MODULE 4: Graphs & Matrix Representations Master Notes",
        "banner_sub": "Handshaking Lemma, Havel-Hakimi, Bipartite & Kőnig, Isomorphism Theorem 3, Self-Complementary Graphs & Matrices"
    }
]

def make_banner(title, subtitle):
    return f"""
    <div class="exam-banner">
        <h1>{title}</h1>
        <p><strong>Course:</strong> MAT2002 — Discrete Mathematics & Graph Theory | <strong>Target Exam:</strong> CAT-2 (Open Book Format)</p>
        <p><strong>Coverage:</strong> {subtitle}</p>
    </div>
    """

def run_export():
    print("=" * 60)
    print("Starting Discrete Mathematics & Graph Theory CAT-2 PDF Export")
    print(f"Output Directory: {PDF_OUT_DIR}")
    print("=" * 60)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # 1. Export 7 Standalone PDFs
        for doc in DOCUMENTS:
            md_path = os.path.join(BASE_DIR, doc["file"])
            if not os.path.exists(md_path):
                print(f"Skipping {doc['file']} (Not found)")
                continue

            with open(md_path, "r", encoding="utf-8") as f:
                md_text = f.read()

            banner = make_banner(doc["title"], doc["banner_sub"])
            html_content = markdown_to_print_html(md_text, BASE_DIR, doc_title=doc["title"], cover_html=banner)
            out_pdf = os.path.join(PDF_OUT_DIR, doc["pdf_name"])
            export_html_to_pdf(page, html_content, out_pdf, header_title=doc["title"])

        # 2. Export All-in-One Master Exam Booklet
        print("-" * 60)
        print("Compiling All-in-One Master Exam Booklet...")
        master_cover = """
        <div style="text-align: center; padding: 40pt 20pt 30pt 20pt; border-bottom: 3px double #1e3a8a; margin-bottom: 25pt;">
            <div style="font-size: 13pt; font-weight: bold; color: #64748b; letter-spacing: 2px; text-transform: uppercase;">Vellore Institute of Technology — VIT Bhopal</div>
            <div style="font-size: 24pt; font-weight: 800; color: #1e3a8a; margin: 12pt 0 6pt 0;">MAT2002: Discrete Mathematics & Graph Theory</div>
            <div style="font-size: 16pt; font-weight: 600; color: #0f172a; margin-bottom: 12pt;">CAT-2 Complete Master Exam Booklet (Modules 3 & 4)</div>
            <div style="display: inline-block; background: #eff6ff; border: 1.5px solid #2563eb; padding: 6pt 16pt; border-radius: 20pt; font-size: 10pt; color: #1e40af; font-weight: 600;">
                Strict CAT-2 Syllabus Scope: Module 3 (Lattices & Boolean Algebra) + Module 4 (Graphs & Matrices)
            </div>
            <div style="margin-top: 20pt; font-size: 9.5pt; color: #475569; line-height: 1.6;">
                <strong>Included Papers:</strong> Official CAT-II Paper (Sept 2026) Solved + Dr. Suresh Dara's Quiz 2, Tutorial 4, Tutorial 2 + HOTS Notes<br>
                <strong>Exam Usage:</strong> Approved for Open-Book Hall Direct Copying, Quick Matching & Step-by-Step Template Lookup
            </div>
        </div>

        <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 14pt 18pt; margin-bottom: 25pt;">
            <h3 style="margin-top: 0; color: #1e3a8a;">Table of Contents & Quick Topic Index</h3>
            <table style="margin-top: 8pt;">
                <tr><th style="width: 28%;">Section</th><th style="width: 44%;">Core Content</th><th style="width: 28%;">Exam Importance</th></tr>
                <tr><td><strong>Section 1: Question-Language Decoder</strong></td><td>Instant Keyword Trigger Matrix + 18 Exam Problem Archetypes with Plug-and-Play Solution Templates & Traps</td><td><strong>Primary Hall Index: Match question phrasing in 5 seconds</strong></td></tr>
                <tr><td><strong>Section 2: Official CAT-II Paper (Sep 2026)</strong></td><td>All 5 Questions Solved: Median Identity, Tuple PDNF/PCNF, $D_{12}$ Complements, Handshaking Partition, $C_6$ Isomorphism & Floyd-Warshall</td><td><strong>Exact 2026 Exam Paper Full Marks Solution</strong></td></tr>
                <tr><td><strong>Section 3: Quiz-2 Solved</strong></td><td>8 Problems: Graph Complements, Havel-Hakimi, Non-Isomorphism, 3-Regular Graphs, Degree Formula</td><td>Direct Class Quiz Problems (Exact exam repeats)</td></tr>
                <tr><td><strong>Section 4: Tutorial-4 Solved</strong></td><td>Dijkstra Algorithm: 6-Vertex Graph ($S \to A,B,C,D,E$) & 5-Vertex Graph ($1 \to 2,3,4,5$, Unreachable Vertex 5)</td><td>Shortest Path Direct Exam Traces</td></tr>
                <tr><td><strong>Section 5: Tutorial-2 Solved</strong></td><td>Lexicographical Poset on $\\mathbb{R}^2$, Relations $S \\circ R$, $R^{-1}$, and $D_{12}$ Lattice Properties</td><td>Posets, Relations & Hasse Diagram Questions</td></tr>
                <tr><td><strong>Section 6: Module 3 HOTS</strong></td><td>Posets, Distributive ($N_5, M_3$), Complements, Boolean Algebra, PDNF/PCNF Algorithms & Circuits</td><td>CO3 Complete Theoretical Mastery</td></tr>
                <tr><td><strong>Section 7: Module 4 HOTS</strong></td><td>Handshaking, Bipartite & Kőnig, Isomorphism Theorem 3, Self-Complementary $p \\equiv 0,1 \\pmod 4$, Adjacency/Incidence Matrices</td><td>CO4 Complete Theoretical Mastery</td></tr>
            </table>
        </div>
        <div class="page-break"></div>
        """

        combined_html_parts = [master_cover]
        for idx, doc in enumerate(DOCUMENTS):
            md_path = os.path.join(BASE_DIR, doc["file"])
            if not os.path.exists(md_path):
                continue

            with open(md_path, "r", encoding="utf-8") as f:
                md_text = f.read()

            sec_banner = f"""
            <div class="exam-banner" style="margin-top: 15pt;">
                <div style="font-size: 8.5pt; text-transform: uppercase; letter-spacing: 1px; color: #93c5fd; font-weight: bold;">Booklet Section {idx + 1}</div>
                <h1 style="margin-top: 2pt;">{doc['title']}</h1>
                <p><strong>Focus:</strong> {doc['banner_sub']}</p>
            </div>
            """
            section_html = markdown_to_print_html(md_text, BASE_DIR, doc_title=doc["title"], cover_html=sec_banner)
            # Extract body content from HTML
            body_match = re.search(r'<body>([\s\S]*?)<script>', section_html)
            if body_match:
                combined_html_parts.append(body_match.group(1))
            else:
                combined_html_parts.append(section_html)

            combined_html_parts.append('<div class="page-break"></div>')

        master_html = HTML_TEMPLATE.format(
            doc_title="Discrete Mathematics CAT-2 Master Exam Booklet",
            content_html="\n".join(combined_html_parts)
        )
        master_pdf = os.path.join(PDF_OUT_DIR, "Discrete_CAT2_COMPLETE_MASTER_EXAM_BOOKLET.pdf")
        export_html_to_pdf(page, master_html, master_pdf, header_title="Complete Master Exam Booklet")

        browser.close()

    print("=" * 60)
    print("ALL PDFs SUCCESSFULLY EXPORTED TO:")
    print(PDF_OUT_DIR)
    print("=" * 60)

if __name__ == "__main__":
    run_export()
