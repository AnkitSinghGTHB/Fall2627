import subprocess

html = """<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        // Target ONLY elements explicitly marked as math containers!
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
</head>
<body>
<p>Line 96: Put $ in <span class="math-inline">\\text{FOLLOW}(S)</span>, where <span class="math-inline">S</span> is the start symbol ($ is the input endmarker).</p>
<p>Line 105: Table cell with math: <span class="math-inline">\\text{FOLLOW}(S) = \\{ \\$ \\}</span> and raw dollar: $</p>
<div class="math-display">E \\Rightarrow_{lm} E + E \\Rightarrow_{lm} id + id</div>
</body>
</html>"""

html_path = r"c:\Users\ankit\Fall2627\TOC\notes\cat2\test_targeted_katex.html"
pdf_path = r"c:\Users\ankit\Fall2627\TOC\notes\cat2\test_targeted_katex.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [chrome, "--headless=new", "--disable-gpu", f"--print-to-pdf={pdf_path}", html_path]
res = subprocess.run(cmd, capture_output=True, text=True)

import pypdf
reader = pypdf.PdfReader(pdf_path)
text = reader.pages[0].extract_text()
print("Targeted KaTeX extracted text:")
for line in text.splitlines():
    print("  ", line)
