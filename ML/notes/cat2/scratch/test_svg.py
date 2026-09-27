from markdown_it import MarkdownIt

md = MarkdownIt('default', options_update={'html': True}).enable('table')

broken = """<div class="diagram-box">
  <svg>
    <rect x="10"/>

    <rect x="20"/>
  </svg>
</div>"""

clean = """<div class="diagram-box">
<svg>
<rect x="10"/>
<rect x="20"/>
</svg>
</div>"""

print("--- BROKEN ---")
print(md.render(broken))
print("--- CLEAN ---")
print(md.render(clean))
