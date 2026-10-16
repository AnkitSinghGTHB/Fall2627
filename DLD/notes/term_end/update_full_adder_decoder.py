"""
update_full_adder_decoder.py
Regenerates full_adder_decoder.svg with beautiful, 100% valid XML, high-contrast dark-mode styling,
active-low bubbles, explicit De Morgan's equations, and Enable pin connections.
"""

import os
import xml.etree.ElementTree as ET

SVG_CONTENT = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 480" width="920" height="480">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .box { fill: #1e293b; stroke: #334155; stroke-width: 2; rx: 8; }
      .decoder-box { fill: #1e1b4b; stroke: #818cf8; stroke-width: 2.5; rx: 8; }
      .gate-nand { fill: #064e3b; stroke: #34d399; stroke-width: 2; }
      .gate-nand-carry { fill: #451a03; stroke: #f59e0b; stroke-width: 2; }
      .bubble { fill: #0f172a; stroke: #818cf8; stroke-width: 2; }
      .bubble-sum { fill: #0f172a; stroke: #34d399; stroke-width: 2; }
      .bubble-carry { fill: #0f172a; stroke: #f59e0b; stroke-width: 2; }
      .wire { stroke: #38bdf8; stroke-width: 2; fill: none; stroke-linecap: round; }
      .wire-sum { stroke: #34d399; stroke-width: 2; fill: none; stroke-linecap: round; }
      .wire-carry { stroke: #fb7185; stroke-width: 2; fill: none; stroke-linecap: round; }
      .wire-out { stroke: #38bdf8; stroke-width: 2.5; fill: none; stroke-linecap: round; }
      .title { fill: #38bdf8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; font-weight: bold; }
      .subtitle { fill: #94a3b8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; }
      .lbl { fill: #e2e8f0; font-family: 'Consolas', monospace; font-size: 13px; font-weight: bold; }
      .pin { fill: #c7d2fe; font-family: 'Consolas', monospace; font-size: 12px; }
      .pin-out { fill: #cbd5e1; font-family: 'Consolas', monospace; font-size: 12px; }
      .gate-lbl { fill: #a7f3d0; font-family: 'Consolas', monospace; font-size: 11px; text-anchor: middle; font-weight: bold; }
      .gate-lbl-carry { fill: #fed7aa; font-family: 'Consolas', monospace; font-size: 11px; text-anchor: middle; font-weight: bold; }
      .note { fill: #34d399; font-family: 'Consolas', monospace; font-size: 12px; }
      .dot-sum { fill: #34d399; }
      .dot-carry { fill: #fb7185; }
    </style>
  </defs>

  <rect width="100%" height="100%" class="bg" />

  <rect x="20" y="15" width="880" height="450" class="box" />
  <text x="460" y="38" text-anchor="middle" class="title">FULL ADDER IMPLEMENTATION USING 3:8 ACTIVE-LOW DECODER &amp; NAND GATES</text>
  <text x="460" y="56" text-anchor="middle" class="subtitle">De Morgan&apos;s Equivalence: S = (Y1&apos;·Y2&apos;·Y4&apos;·Y7&apos;)&apos; = m1+m2+m4+m7 | Cout = (Y3&apos;·Y5&apos;·Y6&apos;·Y7&apos;)&apos; = m3+m5+m6+m7</text>

  <!-- 3 INPUTS (A, B, Cin) -->
  <text x="35" y="145" class="lbl">A (S2)</text>
  <path d="M 95 140 L 160 140" class="wire" />

  <text x="35" y="205" class="lbl">B (S1)</text>
  <path d="M 95 200 L 160 200" class="wire" />

  <text x="35" y="265" class="lbl">Cin(S0)</text>
  <path d="M 95 260 L 160 260" class="wire" />

  <!-- ENABLE LINES -->
  <path d="M 100 320 L 160 320" class="wire" style="stroke:#64748b" />
  <text x="40" y="324" class="lbl" fill="#94a3b8">E (VCC)</text>

  <!-- 3:8 DECODER IC BLOCK -->
  <g transform="translate(160, 90)">
    <rect width="180" height="270" class="decoder-box" />
    <text x="90" y="32" text-anchor="middle" class="title" fill="#a5b4fc">3:8 DECODER</text>
    <text x="90" y="50" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#818cf8">(74LS138 Active-Low)</text>

    <!-- Input Pins Inside -->
    <text x="12" y="54" class="pin">A (MSB)</text>
    <text x="12" y="114" class="pin">B</text>
    <text x="12" y="174" class="pin">Cin (LSB)</text>
    <text x="12" y="234" class="pin" fill="#94a3b8">Enable G1</text>

    <!-- Output Pins (Y0' to Y7' with Inversion Bubbles) -->
    <!-- Y0' -->
    <circle cx="186" cy="30" r="4" class="bubble" />
    <text x="145" y="34" class="pin-out">Y0&apos;</text>
    <path d="M 190 30 L 210 30" class="wire" style="stroke:#475569" />

    <!-- Y1' (Sum) -->
    <circle cx="186" cy="60" r="4" class="bubble" />
    <text x="145" y="64" class="pin-out" fill="#34d399">Y1&apos;</text>

    <!-- Y2' (Sum) -->
    <circle cx="186" cy="90" r="4" class="bubble" />
    <text x="145" y="94" class="pin-out" fill="#34d399">Y2&apos;</text>

    <!-- Y3' (Carry) -->
    <circle cx="186" cy="120" r="4" class="bubble" />
    <text x="145" y="124" class="pin-out" fill="#fb7185">Y3&apos;</text>

    <!-- Y4' (Sum) -->
    <circle cx="186" cy="150" r="4" class="bubble" />
    <text x="145" y="154" class="pin-out" fill="#34d399">Y4&apos;</text>

    <!-- Y5' (Carry) -->
    <circle cx="186" cy="180" r="4" class="bubble" />
    <text x="145" y="184" class="pin-out" fill="#fb7185">Y5&apos;</text>

    <!-- Y6' (Carry) -->
    <circle cx="186" cy="210" r="4" class="bubble" />
    <text x="145" y="214" class="pin-out" fill="#fb7185">Y6&apos;</text>

    <!-- Y7' (Both Sum & Carry) -->
    <circle cx="186" cy="240" r="4" class="bubble" />
    <text x="145" y="244" class="pin-out" fill="#fbbf24">Y7&apos;</text>
  </g>

  <!-- INTERCONNECT WIRES TO 4-INPUT NAND GATES -->
  <!-- Y1' into SUM NAND -->
  <path d="M 350 150 L 530 150 L 530 135 L 560 135" class="wire-sum" />

  <!-- Y2' into SUM NAND -->
  <path d="M 350 180 L 515 180 L 515 145 L 560 145" class="wire-sum" />

  <!-- Y4' into SUM NAND -->
  <path d="M 350 240 L 490 240 L 490 155 L 560 155" class="wire-sum" />

  <!-- Y3' into CARRY NAND -->
  <path d="M 350 210 L 460 210 L 460 275 L 560 275" class="wire-carry" />

  <!-- Y5' into CARRY NAND -->
  <path d="M 350 270 L 515 270 L 515 285 L 560 285" class="wire-carry" />

  <!-- Y6' into CARRY NAND -->
  <path d="M 350 300 L 530 300 L 530 295 L 560 295" class="wire-carry" />

  <!-- Y7' feeds BOTH Sum and Carry -->
  <path d="M 350 330 L 440 330" class="wire" style="stroke:#fbbf24" />
  <circle cx="440" cy="330" r="4" class="dot-sum" style="fill:#fbbf24" />
  <!-- To Sum NAND -->
  <path d="M 440 330 L 440 165 L 560 165" class="wire-sum" style="stroke:#fbbf24" />
  <!-- To Carry NAND -->
  <path d="M 440 330 L 440 305 L 560 305" class="wire-carry" style="stroke:#fbbf24" />

  <!-- 4-INPUT NAND GATE FOR SUM -->
  <g transform="translate(560, 120)">
    <!-- NAND shape: flat back, curved front -->
    <path d="M 0 0 L 30 0 A 30 30 0 0 1 30 60 L 0 60 Z" class="gate-nand" />
    <circle cx="65" cy="30" r="5" class="bubble-sum" />
    <text x="24" y="34" class="gate-lbl">NAND</text>
    <!-- Output wire -->
    <path d="M 70 30 L 150 30" class="wire-out" style="stroke:#34d399" />
    <text x="158" y="34" class="lbl" fill="#34d399">SUM = Σm(1, 2, 4, 7)</text>
  </g>

  <!-- 4-INPUT NAND GATE FOR CARRY -->
  <g transform="translate(560, 260)">
    <path d="M 0 0 L 30 0 A 30 30 0 0 1 30 60 L 0 60 Z" class="gate-nand-carry" />
    <circle cx="65" cy="30" r="5" class="bubble-carry" />
    <text x="24" y="34" class="gate-lbl-carry">NAND</text>
    <!-- Output wire -->
    <path d="M 70 30 L 150 30" class="wire-out" style="stroke:#f59e0b" />
    <text x="158" y="34" class="lbl" fill="#f59e0b">Cout = Σm(3, 5, 6, 7)</text>
  </g>

  <!-- SUMMARY CALLOUT BOX -->
  <rect x="40" y="420" width="840" height="30" rx="6" style="fill:#111827; stroke:#334155; stroke-width:1.5" />
  <text x="460" y="440" text-anchor="middle" class="note">Faculty Golden Rule: Active-Low outputs require NAND gates (NOT OR gates) to implement SOP minterms directly!</text>
</svg>'''

TARGET_PATH = r"c:\Users\ankit\Fall2627\DLD\notes\term_end\images\full_adder_decoder.svg"

with open(TARGET_PATH, "w", encoding="utf-8") as f:
    f.write(SVG_CONTENT)

# Validate XML parse
ET.fromstring(SVG_CONTENT)
print("Updated full_adder_decoder.svg successfully and verified 100% XML validity!")
