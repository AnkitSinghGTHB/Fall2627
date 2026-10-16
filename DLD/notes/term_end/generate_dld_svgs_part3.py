"""
generate_dld_svgs_part3.py
Generates the remaining vital DLD circuit diagrams:
1. binary_to_gray_circuit.svg
2. universal_gates_realization.svg
3. sequence_detector_circuit.svg
4. mux_4to1_circuit.svg
"""

import os

OUT_DIR = r"c:\Users\ankit\Fall2627\DLD\notes\term_end\images"
os.makedirs(OUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. Binary to Gray and Gray to Binary Converters
# -------------------------------------------------------------
def gen_binary_gray_converters():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 480" width="950" height="480">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .box { fill: #1e293b; stroke: #334155; stroke-width: 2; rx: 8; }
      .subbox { fill: #0f172a; stroke: #475569; stroke-width: 1.5; rx: 6; }
      .wire { stroke: #38bdf8; stroke-width: 2; fill: none; stroke-linecap: round; }
      .wire-gray { stroke: #fbbf24; stroke-width: 2; fill: none; stroke-linecap: round; }
      .wire-fb { stroke: #ec4899; stroke-width: 2; fill: none; stroke-linecap: round; stroke-dasharray: 4,2; }
      .gate { fill: #3b82f6; stroke: #93c5fd; stroke-width: 2; }
      .gate-lbl { fill: #ffffff; font-family: 'Consolas', monospace; font-size: 11px; text-anchor: middle; font-weight: bold; }
      .title { fill: #38bdf8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; font-weight: bold; }
      .subtitle { fill: #94a3b8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; }
      .lbl { fill: #e2e8f0; font-family: 'Consolas', monospace; font-size: 13px; font-weight: bold; }
      .eqn { fill: #34d399; font-family: 'Consolas', monospace; font-size: 12px; }
      .dot { fill: #38bdf8; }
      .dot-gray { fill: #fbbf24; }
    </style>
  </defs>

  <rect width="100%" height="100%" class="bg" />

  <!-- LEFT: 4-Bit Binary to Gray -->
  <g transform="translate(20, 20)">
    <rect width="430" height="440" class="box" />
    <text x="215" y="30" text-anchor="middle" class="title">4-BIT BINARY TO GRAY CONVERTER</text>
    <text x="215" y="48" text-anchor="middle" class="subtitle">G3 = B3, G2 = B3 ⊕ B2, G1 = B2 ⊕ B1, G0 = B1 ⊕ B0</text>

    <!-- Inputs B3, B2, B1, B0 -->
    <!-- B3 line (straight to G3 and branching to XOR2) -->
    <text x="30" y="95" class="lbl">B3 (MSB)</text>
    <path d="M 95 90 L 330 90" class="wire" />
    <circle cx="160" cy="90" r="4" class="dot" />
    <path d="M 160 90 L 160 160 L 220 160" class="wire" />
    <text x="340" y="95" class="lbl" fill="#fbbf24">G3 = B3</text>

    <!-- B2 line -->
    <text x="30" y="185" class="lbl">B2</text>
    <path d="M 95 180 L 180 180" class="wire" />
    <circle cx="180" cy="180" r="4" class="dot" />
    <path d="M 180 180 L 220 180" class="wire" />
    <path d="M 180 180 L 180 250 L 220 250" class="wire" />

    <!-- XOR for G2 -->
    <rect x="220" y="150" width="50" height="40" rx="4" class="gate" />
    <text x="245" y="174" class="gate-lbl">XOR</text>
    <path d="M 270 170 L 330 170" class="wire-gray" />
    <text x="340" y="175" class="lbl" fill="#fbbf24">G2 = B3⊕B2</text>

    <!-- B1 line -->
    <text x="30" y="275" class="lbl">B1</text>
    <path d="M 95 270 L 200 270" class="wire" />
    <circle cx="200" cy="270" r="4" class="dot" />
    <path d="M 200 270 L 220 270" class="wire" />
    <path d="M 200 270 L 200 340 L 220 340" class="wire" />

    <!-- XOR for G1 -->
    <rect x="220" y="240" width="50" height="40" rx="4" class="gate" />
    <text x="245" y="264" class="gate-lbl">XOR</text>
    <path d="M 270 260 L 330 260" class="wire-gray" />
    <text x="340" y="265" class="lbl" fill="#fbbf24">G1 = B2⊕B1</text>

    <!-- B0 line -->
    <text x="30" y="365" class="lbl">B0 (LSB)</text>
    <path d="M 95 360 L 220 360" class="wire" />

    <!-- XOR for G0 -->
    <rect x="220" y="330" width="50" height="40" rx="4" class="gate" />
    <text x="245" y="354" class="gate-lbl">XOR</text>
    <path d="M 270 350 L 330 350" class="wire-gray" />
    <text x="340" y="355" class="lbl" fill="#fbbf24">G0 = B1⊕B0</text>

    <text x="30" y="420" class="eqn">Exam Tip: 3 XOR gates required for n=4 bits</text>
  </g>

  <!-- RIGHT: 4-Bit Gray to Binary -->
  <g transform="translate(480, 20)">
    <rect width="440" height="440" class="box" />
    <text x="220" y="30" text-anchor="middle" class="title">4-BIT GRAY TO BINARY CONVERTER</text>
    <text x="220" y="48" text-anchor="middle" class="subtitle">B3 = G3, B2 = B3 ⊕ G2, B1 = B2 ⊕ G1, B0 = B1 ⊕ G0</text>

    <!-- Inputs G3, G2, G1, G0 -->
    <!-- G3 line (straight to B3 and feedback to XOR2) -->
    <text x="30" y="95" class="lbl" fill="#fbbf24">G3 (MSB)</text>
    <path d="M 95 90 L 330 90" class="wire-gray" />
    <circle cx="160" cy="90" r="4" class="dot-gray" />
    <!-- feedback to XOR2 -->
    <path d="M 160 90 L 160 155 L 220 155" class="wire-fb" />
    <text x="340" y="95" class="lbl">B3 = G3</text>

    <!-- G2 line -->
    <text x="30" y="185" class="lbl" fill="#fbbf24">G2</text>
    <path d="M 95 180 L 220 180" class="wire-gray" />

    <!-- XOR for B2 -->
    <rect x="220" y="145" width="50" height="40" rx="4" class="gate" />
    <text x="245" y="169" class="gate-lbl">XOR</text>
    <path d="M 270 165 L 330 165" class="wire" />
    <circle cx="295" cy="165" r="4" class="dot" />
    <!-- feedback from B2 to XOR1 -->
    <path d="M 295 165 L 295 210 L 180 210 L 180 245 L 220 245" class="wire-fb" />
    <text x="340" y="170" class="lbl">B2 = B3⊕G2</text>

    <!-- G1 line -->
    <text x="30" y="275" class="lbl" fill="#fbbf24">G1</text>
    <path d="M 95 270 L 220 270" class="wire-gray" />

    <!-- XOR for B1 -->
    <rect x="220" y="235" width="50" height="40" rx="4" class="gate" />
    <text x="245" y="259" class="gate-lbl">XOR</text>
    <path d="M 270 255 L 330 255" class="wire" />
    <circle cx="295" cy="255" r="4" class="dot" />
    <!-- feedback from B1 to XOR0 -->
    <path d="M 295 255 L 295 300 L 180 300 L 180 335 L 220 335" class="wire-fb" />
    <text x="340" y="260" class="lbl">B1 = B2⊕G1</text>

    <!-- G0 line -->
    <text x="30" y="365" class="lbl" fill="#fbbf24">G0 (LSB)</text>
    <path d="M 95 360 L 220 360" class="wire-gray" />

    <!-- XOR for B0 -->
    <rect x="220" y="325" width="50" height="40" rx="4" class="gate" />
    <text x="245" y="349" class="gate-lbl">XOR</text>
    <path d="M 270 345 L 330 345" class="wire" />
    <text x="340" y="350" class="lbl">B0 = B1⊕G0</text>

    <text x="30" y="420" class="eqn">Feedback Path: Binary output feeds into next stage XOR!</text>
  </g>
</svg>'''
    with open(os.path.join(OUT_DIR, "binary_to_gray_circuit.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# 2. Universal Gate Realizations (NAND and NOR)
# -------------------------------------------------------------
def gen_universal_gates():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 560" width="950" height="560">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .box { fill: #1e293b; stroke: #334155; stroke-width: 2; rx: 8; }
      .wire { stroke: #38bdf8; stroke-width: 2; fill: none; }
      .wire-out { stroke: #34d399; stroke-width: 2.5; fill: none; }
      .gate { fill: #1e1b4b; stroke: #818cf8; stroke-width: 2; }
      .gate-lbl { fill: #c7d2fe; font-family: 'Consolas', monospace; font-size: 11px; text-anchor: middle; font-weight: bold; }
      .bubble { fill: #0f172a; stroke: #818cf8; stroke-width: 2; }
      .title { fill: #38bdf8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; font-weight: bold; }
      .subhead { fill: #f59e0b; font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; font-weight: bold; }
      .lbl { fill: #e2e8f0; font-family: 'Consolas', monospace; font-size: 12px; }
      .res { fill: #34d399; font-family: 'Consolas', monospace; font-size: 12px; font-weight: bold; }
      .dot { fill: #38bdf8; }
    </style>
  </defs>

  <rect width="100%" height="100%" class="bg" />

  <!-- SECTION 1: NAND REALIZATIONS -->
  <g transform="translate(20, 20)">
    <rect width="440" height="520" class="box" />
    <text x="220" y="28" text-anchor="middle" class="title">NAND AS UNIVERSAL GATE</text>

    <!-- NOT using NAND -->
    <text x="25" y="60" class="subhead">1. NOT Gate (Inverter) - 1 Gate</text>
    <path d="M 30 90 L 70 90 M 50 90 L 50 78 L 70 78 M 50 90 L 50 102 L 70 102" class="wire" />
    <circle cx="50" cy="90" r="3" class="dot" />
    <text x="15" y="94" class="lbl">A</text>
    <rect x="70" y="70" width="45" height="40" rx="4" class="gate" />
    <circle cx="120" cy="90" r="5" class="bubble" />
    <text x="92" y="94" class="gate-lbl">NAND</text>
    <path d="M 125 90 L 170 90" class="wire-out" />
    <text x="175" y="94" class="res">Y = A'</text>

    <!-- AND using NAND -->
    <text x="25" y="145" class="subhead">2. AND Gate - 2 Gates</text>
    <text x="15" y="172" class="lbl">A</text>
    <text x="15" y="198" class="lbl">B</text>
    <path d="M 30 168 L 70 168 M 30 192 L 70 192" class="wire" />
    <rect x="70" y="155" width="45" height="48" rx="4" class="gate" />
    <circle cx="120" cy="179" r="5" class="bubble" />
    <text x="92" y="183" class="gate-lbl">NAND</text>
    <!-- Out of 1st into 2nd -->
    <path d="M 125 179 L 160 179 M 145 179 L 145 168 L 160 168 M 145 179 L 145 190 L 160 190" class="wire" />
    <circle cx="145" cy="179" r="3" class="dot" />
    <rect x="160" y="158" width="45" height="42" rx="4" class="gate" />
    <circle cx="210" cy="179" r="5" class="bubble" />
    <text x="182" y="183" class="gate-lbl">NAND</text>
    <path d="M 215 179 L 260 179" class="wire-out" />
    <text x="265" y="183" class="res">Y = (AB)'' = AB</text>

    <!-- OR using NAND -->
    <text x="25" y="240" class="subhead">3. OR Gate (DeMorgan's) - 3 Gates</text>
    <!-- Gate 1: A' -->
    <text x="15" y="272" class="lbl">A</text>
    <path d="M 30 268 L 70 268 M 50 268 L 50 258 L 70 258 M 50 268 L 50 278 L 70 278" class="wire" />
    <circle cx="50" cy="268" r="3" class="dot" />
    <rect x="70" y="250" width="40" height="36" rx="4" class="gate" />
    <circle cx="115" cy="268" r="5" class="bubble" />
    <text x="90" y="272" class="gate-lbl">NAND</text>

    <!-- Gate 2: B' -->
    <text x="15" y="325" class="lbl">B</text>
    <path d="M 30 322 L 70 322 M 50 322 L 50 312 L 70 312 M 50 322 L 50 332 L 70 332" class="wire" />
    <circle cx="50" cy="322" r="3" class="dot" />
    <rect x="70" y="304" width="40" height="36" rx="4" class="gate" />
    <circle cx="115" cy="322" r="5" class="bubble" />
    <text x="90" y="326" class="gate-lbl">NAND</text>

    <!-- Gate 3: combined -->
    <path d="M 120 268 L 155 268 L 155 285 L 175 285" class="wire" />
    <path d="M 120 322 L 155 322 L 155 305 L 175 305" class="wire" />
    <rect x="175" y="275" width="45" height="40" rx="4" class="gate" />
    <circle cx="225" cy="295" r="5" class="bubble" />
    <text x="197" y="299" class="gate-lbl">NAND</text>
    <path d="M 230 295 L 270 295" class="wire-out" />
    <text x="275" y="299" class="res">Y = (A'·B')' = A+B</text>

    <!-- XOR using NAND -->
    <text x="25" y="375" class="subhead">4. XOR Gate (Minimum 4 NAND Gates)</text>
    <text x="15" y="420" class="lbl">A</text>
    <text x="15" y="460" class="lbl">B</text>
    <path d="M 30 420 L 70 420 M 30 460 L 70 460" class="wire" />
    <!-- Gate 1: central NAND(A, B) -->
    <rect x="70" y="420" width="45" height="40" rx="4" class="gate" />
    <circle cx="120" cy="440" r="5" class="bubble" />
    <text x="92" y="444" class="gate-lbl">N1</text>
    <circle cx="45" cy="420" r="3" class="dot" />
    <circle cx="45" cy="460" r="3" class="dot" />

    <!-- Route to Top NAND N2 -->
    <path d="M 45 420 L 45 395 L 150 395" class="wire" />
    <path d="M 125 440 L 138 440 L 138 408 L 150 408" class="wire" />
    <rect x="150" y="388" width="40" height="30" rx="4" class="gate" />
    <circle cx="195" cy="403" r="5" class="bubble" />
    <text x="170" y="407" class="gate-lbl">N2</text>

    <!-- Route to Bottom NAND N3 -->
    <path d="M 45 460 L 45 485 L 150 485" class="wire" />
    <path d="M 138 440 L 138 472 L 150 472" class="wire" />
    <circle cx="138" cy="440" r="3" class="dot" />
    <rect x="150" y="462" width="40" height="30" rx="4" class="gate" />
    <circle cx="195" cy="477" r="5" class="bubble" />
    <text x="170" y="481" class="gate-lbl">N3</text>

    <!-- Output Gate N4 -->
    <path d="M 200 403 L 230 403 L 230 432 L 250 432" class="wire" />
    <path d="M 200 477 L 230 477 L 230 448 L 250 448" class="wire" />
    <rect x="250" y="422" width="45" height="38" rx="4" class="gate" />
    <circle cx="300" cy="441" r="5" class="bubble" />
    <text x="272" y="445" class="gate-lbl">N4</text>
    <path d="M 305 441 L 340 441" class="wire-out" />
    <text x="345" y="445" class="res">Y = A⊕B</text>
  </g>

  <!-- SECTION 2: NOR REALIZATIONS -->
  <g transform="translate(480, 20)">
    <rect width="450" height="520" class="box" />
    <text x="225" y="28" text-anchor="middle" class="title" fill="#f43f5e">NOR AS UNIVERSAL GATE</text>

    <!-- NOT using NOR -->
    <text x="25" y="60" class="subhead" fill="#fb7185">1. NOT Gate (Inverter) - 1 Gate</text>
    <path d="M 30 90 L 70 90 M 50 90 L 50 78 L 70 78 M 50 90 L 50 102 L 70 102" class="wire" />
    <circle cx="50" cy="90" r="3" class="dot" />
    <text x="15" y="94" class="lbl">A</text>
    <rect x="70" y="70" width="45" height="40" rx="4" class="gate" style="stroke:#fb7185; fill:#3f1422" />
    <circle cx="120" cy="90" r="5" class="bubble" style="stroke:#fb7185" />
    <text x="92" y="94" class="gate-lbl">NOR</text>
    <path d="M 125 90 L 170 90" class="wire-out" />
    <text x="175" y="94" class="res">Y = A'</text>

    <!-- OR using NOR -->
    <text x="25" y="145" class="subhead" fill="#fb7185">2. OR Gate - 2 Gates</text>
    <text x="15" y="172" class="lbl">A</text>
    <text x="15" y="198" class="lbl">B</text>
    <path d="M 30 168 L 70 168 M 30 192 L 70 192" class="wire" />
    <rect x="70" y="155" width="45" height="48" rx="4" class="gate" style="stroke:#fb7185; fill:#3f1422" />
    <circle cx="120" cy="179" r="5" class="bubble" style="stroke:#fb7185" />
    <text x="92" y="183" class="gate-lbl">NOR</text>
    <!-- Out of 1st into 2nd -->
    <path d="M 125 179 L 160 179 M 145 179 L 145 168 L 160 168 M 145 179 L 145 190 L 160 190" class="wire" />
    <circle cx="145" cy="179" r="3" class="dot" />
    <rect x="160" y="158" width="45" height="42" rx="4" class="gate" style="stroke:#fb7185; fill:#3f1422" />
    <circle cx="210" cy="179" r="5" class="bubble" style="stroke:#fb7185" />
    <text x="182" y="183" class="gate-lbl">NOR</text>
    <path d="M 215 179 L 260 179" class="wire-out" />
    <text x="265" y="183" class="res">Y = (A+B)'' = A+B</text>

    <!-- AND using NOR -->
    <text x="25" y="240" class="subhead" fill="#fb7185">3. AND Gate (DeMorgan's) - 3 Gates</text>
    <!-- Gate 1: A' -->
    <text x="15" y="272" class="lbl">A</text>
    <path d="M 30 268 L 70 268 M 50 268 L 50 258 L 70 258 M 50 268 L 50 278 L 70 278" class="wire" />
    <circle cx="50" cy="268" r="3" class="dot" />
    <rect x="70" y="250" width="40" height="36" rx="4" class="gate" style="stroke:#fb7185; fill:#3f1422" />
    <circle cx="115" cy="268" r="5" class="bubble" style="stroke:#fb7185" />
    <text x="90" y="272" class="gate-lbl">NOR</text>

    <!-- Gate 2: B' -->
    <text x="15" y="325" class="lbl">B</text>
    <path d="M 30 322 L 70 322 M 50 322 L 50 312 L 70 312 M 50 322 L 50 332 L 70 332" class="wire" />
    <circle cx="50" cy="322" r="3" class="dot" />
    <rect x="70" y="304" width="40" height="36" rx="4" class="gate" style="stroke:#fb7185; fill:#3f1422" />
    <circle cx="115" cy="322" r="5" class="bubble" style="stroke:#fb7185" />
    <text x="90" y="326" class="gate-lbl">NOR</text>

    <!-- Gate 3: combined -->
    <path d="M 120 268 L 155 268 L 155 285 L 175 285" class="wire" />
    <path d="M 120 322 L 155 322 L 155 305 L 175 305" class="wire" />
    <rect x="175" y="275" width="45" height="40" rx="4" class="gate" style="stroke:#fb7185; fill:#3f1422" />
    <circle cx="225" cy="295" r="5" class="bubble" style="stroke:#fb7185" />
    <text x="197" y="299" class="gate-lbl">NOR</text>
    <path d="M 230 295 L 270 295" class="wire-out" />
    <text x="275" y="299" class="res">Y = (A'+B')' = A·B</text>

    <!-- Gate summary table inside NOR section -->
    <text x="25" y="375" class="subhead" fill="#fb7185">4. Gate Requirement Comparison Summary</text>
    <rect x="25" y="390" width="400" height="110" rx="6" style="fill:#111827; stroke:#374151; stroke-width:1.5" />
    <text x="40" y="415" class="lbl" fill="#93c5fd">Gate Function</text>
    <text x="180" y="415" class="lbl" fill="#93c5fd">Using NAND</text>
    <text x="310" y="415" class="lbl" fill="#fb7185">Using NOR</text>
    <line x1="35" y1="423" x2="415" y2="423" stroke="#374151" stroke-width="1" />
    <text x="40" y="442" class="lbl">NOT</text> <text x="210" y="442" class="lbl">1</text> <text x="340" y="442" class="lbl">1</text>
    <text x="40" y="460" class="lbl">AND</text> <text x="210" y="460" class="lbl">2</text> <text x="340" y="460" class="lbl">3</text>
    <text x="40" y="478" class="lbl">OR</text>  <text x="210" y="478" class="lbl">3</text> <text x="340" y="478" class="lbl">2</text>
    <text x="40" y="496" class="lbl">XOR / XNOR</text> <text x="200" y="496" class="lbl">4 / 5</text> <text x="330" y="496" class="lbl">5 / 4</text>
  </g>
</svg>'''
    with open(os.path.join(OUT_DIR, "universal_gates_realization.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# 3. Sequence Detector 1011 (Mealy Overlapping) with D Flip-Flops
# -------------------------------------------------------------
def gen_sequence_detector_circuit():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 520" width="980" height="520">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .box { fill: #1e293b; stroke: #334155; stroke-width: 2; rx: 8; }
      .ff-box { fill: #1e1b4b; stroke: #818cf8; stroke-width: 2; rx: 6; }
      .gate { fill: #064e3b; stroke: #34d399; stroke-width: 2; }
      .gate-lbl { fill: #a7f3d0; font-family: 'Consolas', monospace; font-size: 11px; text-anchor: middle; font-weight: bold; }
      .wire { stroke: #38bdf8; stroke-width: 2; fill: none; stroke-linecap: round; }
      .wire-clk { stroke: #ec4899; stroke-width: 2; fill: none; }
      .wire-fb { stroke: #fbbf24; stroke-width: 2; fill: none; }
      .wire-out { stroke: #34d399; stroke-width: 2.5; fill: none; }
      .title { fill: #38bdf8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; font-weight: bold; }
      .subtitle { fill: #94a3b8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; }
      .lbl { fill: #e2e8f0; font-family: 'Consolas', monospace; font-size: 12px; font-weight: bold; }
      .ff-title { fill: #c7d2fe; font-family: 'Consolas', monospace; font-size: 13px; font-weight: bold; text-anchor: middle; }
      .pin { fill: #93c5fd; font-family: 'Consolas', monospace; font-size: 11px; }
      .dot { fill: #38bdf8; }
      .dot-clk { fill: #ec4899; }
      .dot-fb { fill: #fbbf24; }
    </style>
  </defs>

  <rect width="100%" height="100%" class="bg" />

  <rect x="20" y="15" width="940" height="490" class="box" />
  <text x="490" y="38" text-anchor="middle" class="title">HARDWARE IMPLEMENTATION: 1011 OVERLAPPING SEQUENCE DETECTOR (MEALY FSM)</text>
  <text x="490" y="56" text-anchor="middle" class="subtitle">Using Faculty Recommended D Flip-Flops: D1 = Q1'Q0·X + Q1·Q0'·X | D0 = Q1'Q0'·X + Q1·Q0·X | Output Z = Q1·Q0·X</text>

  <!-- Input X -->
  <text x="40" y="110" class="lbl" fill="#38bdf8">X (Serial Input)</text>
  <path d="M 150 105 L 240 105" class="wire" />
  <circle cx="200" cy="105" r="4" class="dot" />

  <!-- Inverter for X' if needed, or distribute X -->
  <path d="M 200 105 L 200 450" class="wire" />

  <!-- COMBINATIONAL CLOUD: Logic Gates for D1, D0, Z -->
  <!-- AND Gate 1 for D1: Q1'·Q0·X -->
  <rect x="250" y="120" width="55" height="36" rx="4" class="gate" />
  <text x="277" y="142" class="gate-lbl">AND</text>
  <text x="210" y="132" class="pin">Q1'·Q0·X</text>

  <!-- AND Gate 2 for D1: Q1·Q0'·X -->
  <rect x="250" y="170" width="55" height="36" rx="4" class="gate" />
  <text x="277" y="192" class="gate-lbl">AND</text>
  <text x="210" y="182" class="pin">Q1·Q0'·X</text>

  <!-- OR Gate for D1 -->
  <path d="M 305 138 L 330 138 L 330 160 L 350 160" class="wire" />
  <path d="M 305 188 L 330 188 L 330 172 L 350 172" class="wire" />
  <rect x="350" y="150" width="50" height="35" rx="4" class="gate" style="fill:#047857" />
  <text x="375" y="172" class="gate-lbl">OR</text>
  <!-- D1 output into FF1 -->
  <path d="M 400 167 L 460 167" class="wire" />
  <text x="425" y="160" class="lbl">D1</text>

  <!-- AND Gate 3 for D0: Q1'·Q0'·X -->
  <rect x="250" y="270" width="55" height="36" rx="4" class="gate" />
  <text x="277" y="292" class="gate-lbl">AND</text>
  <text x="205" y="282" class="pin">Q1'·Q0'·X</text>

  <!-- AND Gate 4 for D0: Q1·Q0·X -->
  <rect x="250" y="320" width="55" height="36" rx="4" class="gate" />
  <text x="277" y="342" class="gate-lbl">AND</text>
  <text x="215" y="332" class="pin">Q1·Q0·X</text>

  <!-- OR Gate for D0 -->
  <path d="M 305 288 L 330 288 L 330 308 L 350 308" class="wire" />
  <path d="M 305 338 L 330 338 L 330 322 L 350 322" class="wire" />
  <rect x="350" y="300" width="50" height="35" rx="4" class="gate" style="fill:#047857" />
  <text x="375" y="322" class="gate-lbl">OR</text>
  <!-- D0 output into FF0 -->
  <path d="M 400 317 L 460 317" class="wire" />
  <text x="425" y="310" class="lbl">D0</text>

  <!-- Output Detector AND Gate for Z = Q1 · Q0 · X -->
  <rect x="250" y="420" width="60" height="40" rx="4" class="gate" style="stroke:#fbbf24; fill:#78350f" />
  <text x="280" y="444" class="gate-lbl" fill="#fef08a">AND</text>
  <path d="M 310 440 L 890 440" class="wire-out" />
  <text x="900" y="445" class="lbl" fill="#34d399">Z = 1 (DETECT!)</text>

  <!-- D FLIP-FLOP 1 (MSB: Q1) -->
  <g transform="translate(460, 130)">
    <rect width="110" height="110" class="ff-box" />
    <text x="55" y="24" class="ff-title">D-FF 1 (Q1)</text>
    <text x="12" y="42" class="pin">D</text>
    <text x="12" y="88" class="pin">CLK</text>
    <path d="M 0 83 L 12 88 L 0 93" fill="none" stroke="#818cf8" stroke-width="1.5" />
    <text x="90" y="42" class="pin">Q1</text>
    <text x="85" y="88" class="pin">Q1'</text>
    <!-- Outputs -->
    <path d="M 110 38 L 150 38" class="wire-fb" />
    <path d="M 110 84 L 140 84" class="wire-fb" />
  </g>

  <!-- D FLIP-FLOP 0 (LSB: Q0) -->
  <g transform="translate(460, 280)">
    <rect width="110" height="110" class="ff-box" />
    <text x="55" y="24" class="ff-title">D-FF 0 (Q0)</text>
    <text x="12" y="42" class="pin">D</text>
    <text x="12" y="88" class="pin">CLK</text>
    <path d="M 0 83 L 12 88 L 0 93" fill="none" stroke="#818cf8" stroke-width="1.5" />
    <text x="90" y="42" class="pin">Q0</text>
    <text x="85" y="88" class="pin">Q0'</text>
    <!-- Outputs -->
    <path d="M 110 38 L 150 38" class="wire-fb" />
    <path d="M 110 84 L 140 84" class="wire-fb" />
  </g>

  <!-- COMMON CLOCK LINE -->
  <text x="40" y="245" class="lbl" fill="#ec4899">CLK</text>
  <path d="M 75 240 L 430 240" class="wire-clk" />
  <circle cx="430" cy="240" r="4" class="dot-clk" />
  <path d="M 430 240 L 430 218 L 460 218" class="wire-clk" />
  <path d="M 430 240 L 430 368 L 460 368" class="wire-clk" />

  <!-- STATE BUS FEEDBACK ROUTING (Q1, Q1', Q0, Q0' return to combinational input) -->
  <rect x="630" y="125" width="230" height="270" rx="8" style="fill:#0f172a; stroke:#fbbf24; stroke-width:1.5; stroke-dasharray: 4,3" />
  <text x="745" y="150" text-anchor="middle" class="lbl" fill="#fbbf24">State Feedback Bus</text>

  <text x="645" y="180" class="lbl" fill="#fbbf24">Q1  ➔ to AND gates &amp; Z</text>
  <text x="645" y="215" class="lbl" fill="#fbbf24">Q1' ➔ to AND gates</text>
  <text x="645" y="250" class="lbl" fill="#fbbf24">Q0  ➔ to AND gates &amp; Z</text>
  <text x="645" y="285" class="lbl" fill="#fbbf24">Q0' ➔ to AND gates</text>

  <!-- Routing back from FF to Bus -->
  <path d="M 610 168 L 630 168" class="wire-fb" />
  <path d="M 600 214 L 615 214 L 615 205 L 630 205" class="wire-fb" />
  <path d="M 610 318 L 618 318 L 618 245 L 630 245" class="wire-fb" />
  <path d="M 600 364 L 624 364 L 624 280 L 630 280" class="wire-fb" />

  <!-- Bus returning line to inputs -->
  <path d="M 745 395 L 745 480 L 170 480 L 170 140" class="wire-fb" style="stroke-dasharray: 5,3" />

  <!-- Summary Box -->
  <rect x="40" y="470" width="900" height="25" rx="4" style="fill:#042f2e" />
  <text x="490" y="487" text-anchor="middle" class="lbl" fill="#34d399">Faculty Shortcut: D-FF requires ZERO excitation algebra! D = Q(next). 100% full marks in minimum exam time.</text>
</svg>'''
    with open(os.path.join(OUT_DIR, "sequence_detector_circuit.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# 4. 4:1 Multiplexer Internal Architecture & Logic Implementation
# -------------------------------------------------------------
def gen_mux_circuit():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 500" width="950" height="500">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .box { fill: #1e293b; stroke: #334155; stroke-width: 2; rx: 8; }
      .wire { stroke: #38bdf8; stroke-width: 2; fill: none; stroke-linecap: round; }
      .wire-sel { stroke: #ec4899; stroke-width: 2; fill: none; stroke-linecap: round; }
      .wire-not { stroke: #a855f7; stroke-width: 2; fill: none; stroke-linecap: round; }
      .wire-out { stroke: #34d399; stroke-width: 2.5; fill: none; stroke-linecap: round; }
      .gate-and { fill: #1e3a8a; stroke: #60a5fa; stroke-width: 2; }
      .gate-or { fill: #064e3b; stroke: #34d399; stroke-width: 2; }
      .gate-not { fill: #581c87; stroke: #c084fc; stroke-width: 1.5; }
      .bubble { fill: #0f172a; stroke: #c084fc; stroke-width: 1.5; }
      .gate-lbl { fill: #ffffff; font-family: 'Consolas', monospace; font-size: 11px; text-anchor: middle; font-weight: bold; }
      .title { fill: #38bdf8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; font-weight: bold; }
      .subtitle { fill: #94a3b8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; }
      .lbl { fill: #e2e8f0; font-family: 'Consolas', monospace; font-size: 12px; font-weight: bold; }
      .eqn { fill: #34d399; font-family: 'Consolas', monospace; font-size: 12px; }
      .dot { fill: #38bdf8; }
      .dot-sel { fill: #ec4899; }
      .dot-not { fill: #a855f7; }
    </style>
  </defs>

  <rect width="100%" height="100%" class="bg" />

  <!-- LEFT: 4:1 MUX Gate Level Architecture -->
  <g transform="translate(20, 20)">
    <rect width="520" height="460" class="box" />
    <text x="260" y="30" text-anchor="middle" class="title">4:1 MULTIPLEXER INTERNAL GATE ARCHITECTURE</text>
    <text x="260" y="48" text-anchor="middle" class="subtitle">Y = I0·S1'S0' + I1·S1'S0 + I2·S1S0' + I3·S1S0</text>

    <!-- Inputs I0, I1, I2, I3 -->
    <text x="20" y="105" class="lbl">I0</text>
    <path d="M 45 100 L 250 100" class="wire" />

    <text x="20" y="185" class="lbl">I1</text>
    <path d="M 45 180 L 250 180" class="wire" />

    <text x="20" y="265" class="lbl">I2</text>
    <path d="M 45 260 L 250 260" class="wire" />

    <text x="20" y="345" class="lbl">I3</text>
    <path d="M 45 340 L 250 340" class="wire" />

    <!-- Select Lines S1, S0 at bottom -->
    <text x="90" y="435" class="lbl" fill="#ec4899">S1</text>
    <text x="160" y="435" class="lbl" fill="#ec4899">S0</text>

    <!-- Vertical Lines for S1, S1', S0, S0' -->
    <!-- S1 line -->
    <path d="M 100 420 L 100 70" class="wire-sel" />
    <circle cx="100" cy="385" r="3" class="dot-sel" />
    <!-- S1 inverter -->
    <path d="M 100 385 L 115 385" class="wire-sel" />
    <polygon points="115,377 115,393 127,385" class="gate-not" />
    <circle cx="131" cy="385" r="3" class="bubble" />
    <path d="M 134 385 L 140 385 L 140 70" class="wire-not" />

    <!-- S0 line -->
    <path d="M 170 420 L 170 70" class="wire-sel" />
    <circle cx="170" cy="385" r="3" class="dot-sel" />
    <!-- S0 inverter -->
    <path d="M 170 385 L 185 385" class="wire-sel" />
    <polygon points="185,377 185,393 197,385" class="gate-not" />
    <circle cx="201" cy="385" r="3" class="bubble" />
    <path d="M 204 385 L 210 385 L 210 70" class="wire-not" />

    <!-- Connections to 4 AND Gates -->
    <!-- AND 0: I0, S1', S0' -->
    <circle cx="140" cy="112" r="3" class="dot-not" />
    <path d="M 140 112 L 250 112" class="wire-not" />
    <circle cx="210" cy="122" r="3" class="dot-not" />
    <path d="M 210 122 L 250 122" class="wire-not" />
    <rect x="250" y="90" width="55" height="42" rx="4" class="gate-and" />
    <text x="277" y="115" class="gate-lbl">AND</text>

    <!-- AND 1: I1, S1', S0 -->
    <circle cx="140" cy="192" r="3" class="dot-not" />
    <path d="M 140 192 L 250 192" class="wire-not" />
    <circle cx="170" cy="202" r="3" class="dot-sel" />
    <path d="M 170 202 L 250 202" class="wire-sel" />
    <rect x="250" y="170" width="55" height="42" rx="4" class="gate-and" />
    <text x="277" y="195" class="gate-lbl">AND</text>

    <!-- AND 2: I2, S1, S0' -->
    <circle cx="100" cy="272" r="3" class="dot-sel" />
    <path d="M 100 272 L 250 272" class="wire-sel" />
    <circle cx="210" cy="282" r="3" class="dot-not" />
    <path d="M 210 282 L 250 282" class="wire-not" />
    <rect x="250" y="250" width="55" height="42" rx="4" class="gate-and" />
    <text x="277" y="275" class="gate-lbl">AND</text>

    <!-- AND 3: I3, S1, S0 -->
    <circle cx="100" cy="352" r="3" class="dot-sel" />
    <path d="M 100 352 L 250 352" class="wire-sel" />
    <circle cx="170" cy="362" r="3" class="dot-sel" />
    <path d="M 170 362 L 250 362" class="wire-sel" />
    <rect x="250" y="330" width="55" height="42" rx="4" class="gate-and" />
    <text x="277" y="355" class="gate-lbl">AND</text>

    <!-- 4-Input OR Gate -->
    <path d="M 305 111 L 350 111 L 350 210 L 370 210" class="wire" />
    <path d="M 305 191 L 340 191 L 340 220 L 370 220" class="wire" />
    <path d="M 305 271 L 340 271 L 340 230 L 370 230" class="wire" />
    <path d="M 305 351 L 350 351 L 350 240 L 370 240" class="wire" />
    <rect x="370" y="195" width="60" height="60" rx="4" class="gate-or" />
    <text x="400" y="230" class="gate-lbl">OR</text>
    <path d="M 430 225 L 480 225" class="wire-out" />
    <text x="485" y="230" class="lbl" fill="#34d399">Y (Out)</text>
  </g>

  <!-- RIGHT: Logic Function Realization Using 4:1 MUX Block -->
  <g transform="translate(560, 20)">
    <rect width="370" height="460" class="box" />
    <text x="185" y="30" text-anchor="middle" class="title">FUNCTION IMPLEMENTATION</text>
    <text x="185" y="48" text-anchor="middle" class="subtitle">F(A,B,C) = Σm(1, 3, 5, 6) using 4:1 MUX</text>

    <!-- Block Diagram of 4:1 MUX -->
    <rect x="110" y="110" width="150" height="220" rx="6" style="fill:#1e1b4b; stroke:#818cf8; stroke-width:2;" />
    <text x="185" y="135" text-anchor="middle" class="title" fill="#c7d2fe">4:1 MUX</text>

    <!-- Inputs -->
    <text x="30" y="170" class="lbl">I0 = C</text>
    <path d="M 75 165 L 110 165" class="wire" />
    <text x="120" y="170" class="pin">I0</text>

    <text x="30" y="210" class="lbl">I1 = C</text>
    <path d="M 75 205 L 110 205" class="wire" />
    <text x="120" y="210" class="pin">I1</text>

    <text x="30" y="250" class="lbl">I2 = C</text>
    <path d="M 75 245 L 110 245" class="wire" />
    <text x="120" y="250" class="pin">I2</text>

    <text x="25" y="290" class="lbl">I3 = C'</text>
    <path d="M 75 285 L 110 285" class="wire" />
    <text x="120" y="290" class="pin">I3</text>

    <!-- Output Y -->
    <path d="M 260 220 L 315 220" class="wire-out" />
    <text x="235" y="224" class="pin">Y</text>
    <text x="325" y="224" class="lbl" fill="#34d399">F(A,B,C)</text>

    <!-- Select Lines S1=A, S0=B -->
    <path d="M 150 330 L 150 380" class="wire-sel" />
    <text x="145" y="322" class="pin">S1</text>
    <text x="140" y="400" class="lbl" fill="#ec4899">S1 = A</text>

    <path d="M 210 330 L 210 380" class="wire-sel" />
    <text x="205" y="322" class="pin">S0</text>
    <text x="200" y="400" class="lbl" fill="#ec4899">S0 = B</text>

    <!-- Implementation Table -->
    <rect x="25" y="420" width="320" height="25" rx="4" style="fill:#042f2e" />
    <text x="185" y="437" text-anchor="middle" class="lbl" fill="#34d399">Faculty Rule: Connect A,B to select lines S1,S0</text>
  </g>
</svg>'''
    with open(os.path.join(OUT_DIR, "mux_4to1_circuit.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    gen_binary_gray_converters()
    gen_universal_gates()
    gen_sequence_detector_circuit()
    gen_mux_circuit()
    print("Part 3 SVGs successfully generated!")
