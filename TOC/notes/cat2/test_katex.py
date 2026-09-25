import subprocess
import os

html = """<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
            delimiters: [
                {left: "$$", right: "$$", display: true},
                {left: "$", right: "$", display: false}
            ],
            ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"],
            throwOnError: false
        });
    });
</script>
</head>
<body>
<p id="t1">Test 1: Put &#36; in $\\text{FOLLOW}(S)$, where $S$ is the start symbol (&#36; is the input endmarker).</p>
<p id="t2">Test 2: $\\text{FOLLOW}(S) = \\{\\text{\\$}\\}$</p>
<p id="t3">Test 3: $\\text{FOLLOW}(S) = \\{\\$\\}$</p>
<p id="t4">Test 4: $\\text{FOLLOW}(S) = \\{ \\$ \\}$</p>
<p id="t5">Test 5: Table cell: | &#36; |</p>
</body>
</html>"""

html_path = r"c:\Users\ankit\Fall2627\TOC\notes\cat2\test_katex_render.html"
pdf_path = r"c:\Users\ankit\Fall2627\TOC\notes\cat2\test_katex.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [chrome, "--headless=new", "--disable-gpu", f"--print-to-pdf={pdf_path}", html_path]
res = subprocess.run(cmd, capture_output=True, text=True)
print("PDF printed, code:", res.returncode)

import pypdf
reader = pypdf.PdfReader(pdf_path)
text = reader.pages[0].extract_text()
print("Extracted text from PDF:")
for line in text.splitlines():
    print("  ", line)
