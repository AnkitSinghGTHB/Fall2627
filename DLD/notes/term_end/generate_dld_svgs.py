# -*- coding: utf-8 -*-
"""
Generate publication-quality SVG circuit diagrams for ECE2002 DLD
All diagrams use crisp vector styling, standard gate symbols, labels, and color coding.
"""
import os

images_dir = r"c:\Users\ankit\Fall2627\DLD\notes\term_end\images"
os.makedirs(images_dir, exist_ok=True)

# Common SVG styles and marker defs
def svg_wrap(width, height, content, title=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <marker id="arr" markerWidth="7" markerHeight="7" refX="5" refY="2.5" orient="auto">
      <path d="M0,0 L0,5 L5,2.5 z" fill="#1e3a8a" />
    </marker>
    <marker id="redarr" markerWidth="7" markerHeight="7" refX="5" refY="2.5" orient="auto">
      <path d="M0,0 L0,5 L5,2.5 z" fill="#dc2626" />
    </marker>
  </defs>
  <rect width="100%" height="100%" fill="#ffffff" rx="8"/>
  <rect width="100%" height="100%" fill="none" stroke="#e2e8f0" stroke-width="2" rx="8"/>
  <text x="20" y="25" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a">{title}</text>
  {content}
</svg>'''

# -------------------------------------------------------------
# 1. RTL NOR GATE SCHEMATIC
# -------------------------------------------------------------
rtl_content = '''
  <g transform="translate(60, 40)" font-family="Consolas, monospace" font-size="12">
    <!-- Vcc Rail -->
    <line x1="200" y1="20" x2="200" y2="60" stroke="#0f172a" stroke-width="2.5"/>
    <circle cx="200" cy="20" r="4" fill="#0f172a"/>
    <text x="210" y="24" font-weight="bold" fill="#b91c1c">+Vcc (+3.6V)</text>
    
    <!-- Collector Resistor Rc -->
    <rect x="190" y="60" width="20" height="40" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>
    <text x="220" y="85" fill="#0f172a">Rc (640 Ω)</text>
    <line x1="200" y1="100" x2="200" y2="130" stroke="#0f172a" stroke-width="2.5"/>
    
    <!-- Output Node Y -->
    <circle cx="200" cy="130" r="4" fill="#1e3a8a"/>
    <line x1="200" y1="130" x2="350" y2="130" stroke="#1e3a8a" stroke-width="2.5" marker-end="url(#arr)"/>
    <text x="360" y="135" font-weight="bold" fill="#1e3a8a" font-size="14">Output Y = (A + B)' [NOR]</text>
    
    <!-- Transistor Bus -->
    <line x1="120" y1="130" x2="280" y2="130" stroke="#0f172a" stroke-width="2"/>
    <line x1="120" y1="130" x2="120" y2="160" stroke="#0f172a" stroke-width="2"/>
    <line x1="280" y1="130" x2="280" y2="160" stroke="#0f172a" stroke-width="2"/>
    
    <!-- Transistor Q1 (Left) -->
    <!-- Collector line -->
    <line x1="120" y1="160" x2="120" y2="185" stroke="#0f172a" stroke-width="2"/>
    <!-- Base Bar & Slanted lines -->
    <line x1="105" y1="180" x2="105" y2="210" stroke="#0f172a" stroke-width="3"/>
    <line x1="105" y1="185" x2="120" y2="175" stroke="#0f172a" stroke-width="2"/>
    <line x1="105" y1="205" x2="120" y2="215" stroke="#0f172a" stroke-width="2"/>
    <!-- Emitter arrow -->
    <polygon points="116,211 122,217 114,217" fill="#0f172a"/>
    <line x1="120" y1="215" x2="120" y2="250" stroke="#0f172a" stroke-width="2"/>
    <text x="75" y="195" font-weight="bold" fill="#0f172a">Q1</text>
    
    <!-- Input A with RB -->
    <line x1="10" y1="195" x2="40" y2="195" stroke="#0f172a" stroke-width="2"/>
    <text x="-5" y="200" font-weight="bold" fill="#1e3a8a">Input A</text>
    <rect x="40" y="185" width="40" height="20" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>
    <text x="45" y="200" font-size="10">RB (450Ω)</text>
    <line x1="80" y1="195" x2="105" y2="195" stroke="#0f172a" stroke-width="2"/>

    <!-- Transistor Q2 (Right) -->
    <!-- Collector line -->
    <line x1="280" y1="160" x2="280" y2="185" stroke="#0f172a" stroke-width="2"/>
    <!-- Base Bar & Slanted lines -->
    <line x1="265" y1="180" x2="265" y2="210" stroke="#0f172a" stroke-width="3"/>
    <line x1="265" y1="185" x2="280" y2="175" stroke="#0f172a" stroke-width="2"/>
    <line x1="265" y1="205" x2="280" y2="215" stroke="#0f172a" stroke-width="2"/>
    <!-- Emitter arrow -->
    <polygon points="276,211 282,217 274,217" fill="#0f172a"/>
    <line x1="280" y1="215" x2="280" y2="250" stroke="#0f172a" stroke-width="2"/>
    <text x="235" y="195" font-weight="bold" fill="#0f172a">Q2</text>
    
    <!-- Input B with RB -->
    <line x1="170" y1="195" x2="200" y2="195" stroke="#0f172a" stroke-width="2"/>
    <text x="125" y="200" font-weight="bold" fill="#1e3a8a">Input B</text>
    <rect x="200" y="185" width="40" height="20" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>
    <text x="205" y="200" font-size="10">RB (450Ω)</text>
    <line x1="240" y1="195" x2="265" y2="195" stroke="#0f172a" stroke-width="2"/>

    <!-- Common Emitter Ground Bus -->
    <line x1="120" y1="250" x2="280" y2="250" stroke="#0f172a" stroke-width="2.5"/>
    <line x1="200" y1="250" x2="200" y2="270" stroke="#0f172a" stroke-width="2.5"/>
    <line x1="185" y1="270" x2="215" y2="270" stroke="#0f172a" stroke-width="3"/>
    <line x1="190" y1="275" x2="210" y2="275" stroke="#0f172a" stroke-width="2"/>
    <line x1="195" y1="280" x2="205" y2="280" stroke="#0f172a" stroke-width="1.5"/>
    <text x="225" y="275" font-size="11" fill="#64748b">GND (0V)</text>
  </g>
'''
with open(os.path.join(images_dir, "rtl_nor_gate.svg"), "w", encoding="utf-8") as f:
    f.write(svg_wrap(620, 350, rtl_content, "RTL (Resistor-Transistor Logic) 2-Input NOR Gate Schematic"))

# -------------------------------------------------------------
# 2. BCD TO EXCESS-3 LOGIC CIRCUIT DIAGRAM
# -------------------------------------------------------------
bcd_circuit = '''
  <g transform="translate(40, 40)" font-family="Consolas, monospace" font-size="12">
    <!-- Input Rails -->
    <text x="10" y="40" font-weight="bold" fill="#1e3a8a">A</text>
    <line x1="30" y1="35" x2="520" y2="35" stroke="#cbd5e1" stroke-width="2"/>
    <text x="10" y="80" font-weight="bold" fill="#1e3a8a">B</text>
    <line x1="30" y1="75" x2="520" y2="75" stroke="#cbd5e1" stroke-width="2"/>
    <text x="10" y="120" font-weight="bold" fill="#1e3a8a">C</text>
    <line x1="30" y1="115" x2="520" y2="115" stroke="#cbd5e1" stroke-width="2"/>
    <text x="10" y="160" font-weight="bold" fill="#1e3a8a">D</text>
    <line x1="30" y1="155" x2="520" y2="155" stroke="#cbd5e1" stroke-width="2"/>

    <!-- Output Z: Inverter on D -->
    <circle cx="80" cy="155" r="3" fill="#1e3a8a"/>
    <line x1="80" y1="155" x2="80" y2="200" stroke="#1e3a8a" stroke-width="2"/>
    <line x1="80" y1="200" x2="120" y2="200" stroke="#1e3a8a" stroke-width="2"/>
    <!-- Inverter Triangle -->
    <polygon points="120,190 145,200 120,210" fill="#f8fafc" stroke="#1e3a8a" stroke-width="2"/>
    <circle cx="149" cy="200" r="3.5" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="153" y1="200" x2="520" y2="200" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <text x="530" y="205" font-weight="bold" fill="#16a34a" font-size="14">Z = D'</text>

    <!-- Sub-expression (C + D) OR Gate -->
    <circle cx="160" cy="115" r="3" fill="#1e3a8a"/>
    <circle cx="170" cy="155" r="3" fill="#1e3a8a"/>
    <line x1="160" y1="115" x2="160" y2="245" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="160" y1="245" x2="200" y2="245" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="170" y1="155" x2="170" y2="265" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="170" y1="265" x2="200" y2="265" stroke="#1e3a8a" stroke-width="1.8"/>
    <!-- OR gate symbol -->
    <path d="M 195 240 Q 210 255 195 270 Q 225 270 240 255 Q 225 240 195 240 Z" fill="#f8fafc" stroke="#1e3a8a" stroke-width="2"/>
    <line x1="240" y1="255" x2="270" y2="255" stroke="#1e3a8a" stroke-width="2"/>
    <text x="245" y="250" font-size="11" fill="#64748b">(C+D)</text>

    <!-- Output Y: XNOR of C and D -->
    <circle cx="110" cy="115" r="3" fill="#1e3a8a"/>
    <circle cx="120" cy="155" r="3" fill="#1e3a8a"/>
    <line x1="110" y1="115" x2="110" y2="305" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="110" y1="305" x2="200" y2="305" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="120" y1="155" x2="120" y2="325" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="120" y1="325" x2="200" y2="325" stroke="#1e3a8a" stroke-width="1.8"/>
    <!-- XNOR gate symbol -->
    <path d="M 190 300 Q 200 315 190 330" fill="none" stroke="#1e3a8a" stroke-width="2"/>
    <path d="M 196 300 Q 211 315 196 330 Q 226 330 241 315 Q 226 300 196 300 Z" fill="#f8fafc" stroke="#1e3a8a" stroke-width="2"/>
    <circle cx="245" cy="315" r="3.5" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="249" y1="315" x2="520" y2="315" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <text x="530" y="320" font-weight="bold" fill="#16a34a" font-size="14">Y = (C ⊕ D)'</text>

    <!-- Output X: XOR of B and (C + D) -->
    <circle cx="260" cy="75" r="3" fill="#1e3a8a"/>
    <line x1="260" y1="75" x2="260" y2="365" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="260" y1="365" x2="310" y2="365" stroke="#1e3a8a" stroke-width="1.8"/>
    <circle cx="270" cy="255" r="3" fill="#1e3a8a"/>
    <line x1="270" y1="255" x2="270" y2="385" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="270" y1="385" x2="310" y2="385" stroke="#1e3a8a" stroke-width="1.8"/>
    <!-- XOR symbol -->
    <path d="M 304 360 Q 314 375 304 390" fill="none" stroke="#1e3a8a" stroke-width="2"/>
    <path d="M 310 360 Q 325 375 310 390 Q 340 390 355 375 Q 340 360 310 360 Z" fill="#f8fafc" stroke="#1e3a8a" stroke-width="2"/>
    <line x1="355" y1="375" x2="520" y2="375" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <text x="530" y="380" font-weight="bold" fill="#16a34a" font-size="14">X = B ⊕ (C + D)</text>

    <!-- Output W: A + B(C + D) -->
    <!-- AND gate for B(C + D) -->
    <circle cx="280" cy="75" r="3" fill="#1e3a8a"/>
    <line x1="280" y1="75" x2="280" y2="425" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="280" y1="425" x2="310" y2="425" stroke="#1e3a8a" stroke-width="1.8"/>
    <circle cx="270" cy="385" r="3" fill="#1e3a8a"/>
    <line x1="270" y1="385" x2="270" y2="445" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="270" y1="445" x2="310" y2="445" stroke="#1e3a8a" stroke-width="1.8"/>
    <path d="M 310 415 L 330 415 A 15 15 0 0 1 330 455 L 310 455 Z" fill="#f8fafc" stroke="#1e3a8a" stroke-width="2"/>
    <line x1="345" y1="435" x2="390" y2="435" stroke="#1e3a8a" stroke-width="1.8"/>
    <!-- OR gate with A -->
    <circle cx="370" cy="35" r="3" fill="#1e3a8a"/>
    <line x1="370" y1="35" x2="370" y2="465" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="370" y1="465" x2="390" y2="465" stroke="#1e3a8a" stroke-width="1.8"/>
    <path d="M 385 430 Q 400 450 385 470 Q 420 470 435 450 Q 420 430 385 430 Z" fill="#f8fafc" stroke="#1e3a8a" stroke-width="2"/>
    <line x1="435" y1="450" x2="520" y2="450" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <text x="530" y="455" font-weight="bold" fill="#16a34a" font-size="14">W = A + B(C + D)</text>
  </g>
'''
with open(os.path.join(images_dir, "bcd_to_excess3_circuit.svg"), "w", encoding="utf-8") as f:
    f.write(svg_wrap(740, 540, bcd_circuit, "BCD to Excess-3 Code Converter Minimal Logic Schematic"))

# -------------------------------------------------------------
# 3. MASTER-SLAVE JK FLIP-FLOP SCHEMATIC
# -------------------------------------------------------------
ms_circuit = '''
  <g transform="translate(30, 40)" font-family="Consolas, monospace" font-size="12">
    <!-- Master Block Box -->
    <rect x="50" y="40" width="220" height="240" fill="#f0f9ff" stroke="#0284c7" stroke-width="2" rx="6"/>
    <text x="160" y="65" text-anchor="middle" font-weight="bold" fill="#0369a1" font-size="14">MASTER (JK Flip-Flop)</text>
    
    <!-- Slave Block Box -->
    <rect x="350" y="40" width="220" height="240" fill="#fdf4ff" stroke="#c026d3" stroke-width="2" rx="6"/>
    <text x="460" y="65" text-anchor="middle" font-weight="bold" fill="#a21caf" font-size="14">SLAVE (SR Flip-Flop)</text>
    
    <!-- Clock line with Inverter -->
    <line x1="10" y1="160" x2="50" y2="160" stroke="#0f172a" stroke-width="2.5" marker-end="url(#arr)"/>
    <text x="10" y="150" font-weight="bold" fill="#0f172a">CLK</text>
    <circle cx="30" cy="160" r="3" fill="#0f172a"/>
    
    <!-- Clock Inverter to Slave -->
    <line x1="30" y1="160" x2="30" y2="25" stroke="#0f172a" stroke-width="2"/>
    <line x1="30" y1="25" x2="300" y2="25" stroke="#0f172a" stroke-width="2"/>
    <!-- Inverter Symbol -->
    <polygon points="300,15 320,25 300,35" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>
    <circle cx="324" cy="25" r="3.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/>
    <line x1="328" y1="25" x2="460" y2="25" stroke="#0f172a" stroke-width="2"/>
    <line x1="460" y1="25" x2="460" y2="40" stroke="#0f172a" stroke-width="2" marker-end="url(#arr)"/>
    <text x="340" y="20" font-weight="bold" fill="#dc2626">CLK' (Active Low)</text>

    <!-- Inputs J and K -->
    <line x1="10" y1="100" x2="50" y2="100" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <text x="10" y="95" font-weight="bold" fill="#1e3a8a">J</text>
    <line x1="10" y1="220" x2="50" y2="220" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <text x="10" y="215" font-weight="bold" fill="#1e3a8a">K</text>
    
    <!-- Master Outputs Y and Y' -->
    <line x1="270" y1="110" x2="350" y2="110" stroke="#0369a1" stroke-width="2.5" marker-end="url(#arr)"/>
    <text x="310" y="100" font-weight="bold" fill="#0369a1">Y (Set)</text>
    <line x1="270" y1="210" x2="350" y2="210" stroke="#0369a1" stroke-width="2.5" marker-end="url(#arr)"/>
    <text x="310" y="200" font-weight="bold" fill="#0369a1">Y' (Reset)</text>

    <!-- Final Outputs Q and Q' -->
    <line x1="570" y1="110" x2="650" y2="110" stroke="#15803d" stroke-width="2.5" marker-end="url(#arr)"/>
    <circle cx="600" cy="110" r="3" fill="#15803d"/>
    <text x="655" y="115" font-weight="bold" fill="#15803d" font-size="14">Q</text>
    
    <line x1="570" y1="210" x2="650" y2="210" stroke="#15803d" stroke-width="2.5" marker-end="url(#arr)"/>
    <circle cx="610" cy="210" r="3" fill="#15803d"/>
    <text x="655" y="215" font-weight="bold" fill="#15803d" font-size="14">Q'</text>

    <!-- Feedback Paths from Q' to J and Q to K -->
    <line x1="600" y1="110" x2="600" y2="300" stroke="#dc2626" stroke-width="1.8"/>
    <line x1="600" y1="300" x2="20" y2="300" stroke="#dc2626" stroke-width="1.8"/>
    <line x1="20" y1="300" x2="20" y2="230" stroke="#dc2626" stroke-width="1.8"/>
    <line x1="20" y1="230" x2="50" y2="230" stroke="#dc2626" stroke-width="1.8" marker-end="url(#redarr)"/>
    <text x="320" y="295" font-weight="bold" fill="#dc2626">Feedback Q to K Input</text>

    <line x1="610" y1="210" x2="610" y2="320" stroke="#16a34a" stroke-width="1.8"/>
    <line x1="610" y1="320" x2="10" y2="320" stroke="#16a34a" stroke-width="1.8"/>
    <line x1="10" y1="320" x2="10" y2="90" stroke="#16a34a" stroke-width="1.8"/>
    <line x1="10" y1="90" x2="50" y2="90" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arr)"/>
    <text x="320" y="335" font-weight="bold" fill="#16a34a">Feedback Q' to J Input</text>
  </g>
'''
with open(os.path.join(images_dir, "master_slave_jk_ff.svg"), "w", encoding="utf-8") as f:
    f.write(svg_wrap(720, 420, ms_circuit, "Master-Slave JK Flip-Flop Architecture (Eliminates Race-Around)"))

# -------------------------------------------------------------
# 4. SYNCHRONOUS DECADE COUNTER SCHEMATIC
# -------------------------------------------------------------
sync_counter = '''
  <g transform="translate(20, 35)" font-family="Consolas, monospace" font-size="11">
    <!-- FF A (LSB) -->
    <rect x="40" y="60" width="90" height="130" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2" rx="4"/>
    <text x="85" y="80" text-anchor="middle" font-weight="bold" fill="#1e3a8a">FF A (LSB)</text>
    <text x="50" y="105">J</text><text x="50" y="155">K</text>
    <text x="110" y="105">QA</text><text x="110" y="155">QA'</text>
    <polygon points="40,125 50,130 40,135" fill="none" stroke="#1e3a8a" stroke-width="1.5"/>

    <!-- FF B -->
    <rect x="200" y="60" width="90" height="130" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2" rx="4"/>
    <text x="245" y="80" text-anchor="middle" font-weight="bold" fill="#1e3a8a">FF B</text>
    <text x="210" y="105">J</text><text x="210" y="155">K</text>
    <text x="270" y="105">QB</text><text x="270" y="155">QB'</text>
    <polygon points="200,125 210,130 200,135" fill="none" stroke="#1e3a8a" stroke-width="1.5"/>

    <!-- FF C -->
    <rect x="360" y="60" width="90" height="130" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2" rx="4"/>
    <text x="405" y="80" text-anchor="middle" font-weight="bold" fill="#1e3a8a">FF C</text>
    <text x="370" y="105">J</text><text x="370" y="155">K</text>
    <text x="430" y="105">QC</text><text x="430" y="155">QC'</text>
    <polygon points="360,125 370,130 360,135" fill="none" stroke="#1e3a8a" stroke-width="1.5"/>

    <!-- FF D (MSB) -->
    <rect x="530" y="60" width="90" height="130" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2" rx="4"/>
    <text x="575" y="80" text-anchor="middle" font-weight="bold" fill="#1e3a8a">FF D (MSB)</text>
    <text x="540" y="105">J</text><text x="540" y="155">K</text>
    <text x="600" y="105">QD</text><text x="600" y="155">QD'</text>
    <polygon points="530,125 540,130 530,135" fill="none" stroke="#1e3a8a" stroke-width="1.5"/>

    <!-- Shared Synchronous Clock Line -->
    <line x1="10" y1="220" x2="530" y2="220" stroke="#dc2626" stroke-width="2"/>
    <text x="10" y="240" font-weight="bold" fill="#dc2626">Common Clock CLK</text>
    <line x1="40" y1="220" x2="40" y2="130" stroke="#dc2626" stroke-width="2"/>
    <line x1="200" y1="220" x2="200" y2="130" stroke="#dc2626" stroke-width="2"/>
    <line x1="360" y1="220" x2="360" y2="130" stroke="#dc2626" stroke-width="2"/>
    <line x1="530" y1="220" x2="530" y2="130" stroke="#dc2626" stroke-width="2"/>

    <!-- Logic 1 to FF A -->
    <line x1="10" y1="100" x2="40" y2="100" stroke="#15803d" stroke-width="2" marker-end="url(#arr)"/>
    <line x1="10" y1="150" x2="40" y2="150" stroke="#15803d" stroke-width="2" marker-end="url(#arr)"/>
    <text x="5" y="90" font-weight="bold" fill="#15803d">Logic 1</text>

    <!-- FF B inputs: JB = QA · QD', KB = QA -->
    <line x1="130" y1="100" x2="160" y2="100" stroke="#1e3a8a" stroke-width="2"/>
    <circle cx="150" cy="100" r="3" fill="#1e3a8a"/>
    <!-- AND gate for JB -->
    <path d="M 160 90 L 175 90 A 10 10 0 0 1 175 110 L 160 110 Z" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.5"/>
    <line x1="185" y1="100" x2="200" y2="100" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <!-- QD' feedback to AND gate -->
    <line x1="620" y1="150" x2="640" y2="150" stroke="#64748b" stroke-width="1.5"/>
    <line x1="640" y1="150" x2="640" y2="25" stroke="#64748b" stroke-width="1.5"/>
    <line x1="640" y1="25" x2="160" y2="25" stroke="#64748b" stroke-width="1.5"/>
    <line x1="160" y1="25" x2="160" y2="95" stroke="#64748b" stroke-width="1.5"/>
    <!-- KB = QA -->
    <line x1="150" y1="100" x2="150" y2="150" stroke="#1e3a8a" stroke-width="1.5"/>
    <line x1="150" y1="150" x2="200" y2="150" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>

    <!-- FF C inputs: JC = KC = QA · QB -->
    <line x1="290" y1="100" x2="310" y2="100" stroke="#1e3a8a" stroke-width="1.8"/>
    <!-- QA feedforward to C -->
    <line x1="150" y1="150" x2="150" y2="180" stroke="#1e3a8a" stroke-width="1.5"/>
    <line x1="150" y1="180" x2="310" y2="180" stroke="#1e3a8a" stroke-width="1.5"/>
    <line x1="310" y1="180" x2="310" y2="115" stroke="#1e3a8a" stroke-width="1.5"/>
    <!-- AND gate for JC, KC -->
    <path d="M 315 95 L 330 95 A 10 10 0 0 1 330 115 L 315 115 Z" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.5"/>
    <line x1="340" y1="105" x2="360" y2="105" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <circle cx="350" cy="105" r="3" fill="#1e3a8a"/>
    <line x1="350" y1="105" x2="350" y2="150" stroke="#1e3a8a" stroke-width="1.5"/>
    <line x1="350" y1="150" x2="360" y2="150" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>

    <!-- FF D inputs: JD = QA · QB · QC, KD = QA -->
    <circle cx="340" cy="105" r="3" fill="#1e3a8a"/>
    <line x1="340" y1="105" x2="340" y2="45" stroke="#1e3a8a" stroke-width="1.5"/>
    <line x1="340" y1="45" x2="480" y2="45" stroke="#1e3a8a" stroke-width="1.5"/>
    <line x1="450" y1="100" x2="480" y2="100" stroke="#1e3a8a" stroke-width="1.5"/>
    <!-- 2nd AND gate for JD -->
    <path d="M 480 60 L 495 60 A 10 10 0 0 1 495 80 L 480 80 Z" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.5"/>
    <line x1="505" y1="70" x2="530" y2="100" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <!-- KD = QA -->
    <line x1="150" y1="180" x2="510" y2="180" stroke="#1e3a8a" stroke-width="1.5"/>
    <line x1="510" y1="180" x2="510" y2="150" stroke="#1e3a8a" stroke-width="1.5"/>
    <line x1="510" y1="150" x2="530" y2="150" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
  </g>
'''
with open(os.path.join(images_dir, "sync_decade_counter_circuit.svg"), "w", encoding="utf-8") as f:
    f.write(svg_wrap(720, 320, sync_counter, "Synchronous Decade (Mod-10) Counter Hardware Circuit Schematic"))

# -------------------------------------------------------------
# 5. ASYNCHRONOUS (RIPPLE) DECADE COUNTER SCHEMATIC
# -------------------------------------------------------------
async_counter = '''
  <g transform="translate(30, 40)" font-family="Consolas, monospace" font-size="11">
    <!-- FF 0 -->
    <rect x="30" y="50" width="85" height="120" fill="#f8fafc" stroke="#0f172a" stroke-width="2" rx="4"/>
    <text x="72" y="70" text-anchor="middle" font-weight="bold">FF 0 (T=1)</text>
    <text x="95" y="95">Q0</text><text x="95" y="145">Q0'</text>
    <polygon points="30,105 40,110 30,115" fill="none" stroke="#0f172a" stroke-width="1.5"/>
    <circle cx="27" cy="110" r="3" fill="#ffffff" stroke="#0f172a"/>
    <text x="72" y="160" font-size="9" text-anchor="middle" fill="#dc2626">CLR'</text>

    <!-- FF 1 -->
    <rect x="180" y="50" width="85" height="120" fill="#f8fafc" stroke="#0f172a" stroke-width="2" rx="4"/>
    <text x="222" y="70" text-anchor="middle" font-weight="bold">FF 1 (T=1)</text>
    <text x="245" y="95">Q1</text><text x="245" y="145">Q1'</text>
    <polygon points="180,105 190,110 180,115" fill="none" stroke="#0f172a" stroke-width="1.5"/>
    <circle cx="177" cy="110" r="3" fill="#ffffff" stroke="#0f172a"/>
    <text x="222" y="160" font-size="9" text-anchor="middle" fill="#dc2626">CLR'</text>

    <!-- FF 2 -->
    <rect x="330" y="50" width="85" height="120" fill="#f8fafc" stroke="#0f172a" stroke-width="2" rx="4"/>
    <text x="372" y="70" text-anchor="middle" font-weight="bold">FF 2 (T=1)</text>
    <text x="395" y="95">Q2</text><text x="395" y="145">Q2'</text>
    <polygon points="330,105 340,110 330,115" fill="none" stroke="#0f172a" stroke-width="1.5"/>
    <circle cx="327" cy="110" r="3" fill="#ffffff" stroke="#0f172a"/>
    <text x="372" y="160" font-size="9" text-anchor="middle" fill="#dc2626">CLR'</text>

    <!-- FF 3 -->
    <rect x="480" y="50" width="85" height="120" fill="#f8fafc" stroke="#0f172a" stroke-width="2" rx="4"/>
    <text x="522" y="70" text-anchor="middle" font-weight="bold">FF 3 (T=1)</text>
    <text x="545" y="95">Q3</text><text x="545" y="145">Q3'</text>
    <polygon points="480,105 490,110 480,115" fill="none" stroke="#0f172a" stroke-width="1.5"/>
    <circle cx="477" cy="110" r="3" fill="#ffffff" stroke="#0f172a"/>
    <text x="522" y="160" font-size="9" text-anchor="middle" fill="#dc2626">CLR'</text>

    <!-- Ripple Clock Cascade (Negative-Edge Triggered) -->
    <line x1="-10" y1="110" x2="24" y2="110" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <text x="-25" y="105" font-weight="bold" fill="#1e3a8a">CLK</text>
    <!-- Q0 drives FF 1 -->
    <line x1="115" y1="90" x2="140" y2="90" stroke="#0f172a" stroke-width="1.8"/>
    <line x1="140" y1="90" x2="140" y2="110" stroke="#0f172a" stroke-width="1.8"/>
    <line x1="140" y1="110" x2="174" y2="110" stroke="#0f172a" stroke-width="1.8" marker-end="url(#arr)"/>
    <!-- Q1 drives FF 2 -->
    <line x1="265" y1="90" x2="290" y2="90" stroke="#0f172a" stroke-width="1.8"/>
    <circle cx="280" cy="90" r="3" fill="#0f172a"/>
    <line x1="290" y1="90" x2="290" y2="110" stroke="#0f172a" stroke-width="1.8"/>
    <line x1="290" y1="110" x2="324" y2="110" stroke="#0f172a" stroke-width="1.8" marker-end="url(#arr)"/>
    <!-- Q2 drives FF 3 -->
    <line x1="415" y1="90" x2="440" y2="90" stroke="#0f172a" stroke-width="1.8"/>
    <line x1="440" y1="90" x2="440" y2="110" stroke="#0f172a" stroke-width="1.8"/>
    <line x1="440" y1="110" x2="474" y2="110" stroke="#0f172a" stroke-width="1.8" marker-end="url(#arr)"/>
    <circle cx="580" cy="90" r="3" fill="#0f172a"/>

    <!-- Asynchronous NAND Clear Circuit (Detects Q3 · Q1 = 1010_2) -->
    <!-- Line from Q1 -->
    <line x1="280" y1="90" x2="280" y2="210" stroke="#dc2626" stroke-width="1.8"/>
    <line x1="280" y1="210" x2="370" y2="210" stroke="#dc2626" stroke-width="1.8"/>
    <!-- Line from Q3 -->
    <line x1="565" y1="90" x2="580" y2="90" stroke="#dc2626" stroke-width="1.8"/>
    <line x1="580" y1="90" x2="580" y2="230" stroke="#dc2626" stroke-width="1.8"/>
    <line x1="580" y1="230" x2="370" y2="230" stroke="#dc2626" stroke-width="1.8"/>
    <!-- NAND Gate -->
    <path d="M 370 200 L 390 200 A 20 20 0 0 1 390 240 L 370 240 Z" fill="#f8fafc" stroke="#dc2626" stroke-width="2"/>
    <circle cx="414" cy="220" r="4" fill="#ffffff" stroke="#dc2626" stroke-width="2"/>
    <text x="360" y="255" font-weight="bold" fill="#dc2626">2-Input NAND Gate</text>

    <!-- Clear Bus to all FFs -->
    <line x1="418" y1="220" x2="440" y2="220" stroke="#dc2626" stroke-width="2"/>
    <line x1="440" y1="220" x2="440" y2="270" stroke="#dc2626" stroke-width="2"/>
    <line x1="440" y1="270" x2="72" y2="270" stroke="#dc2626" stroke-width="2"/>
    <!-- Vertical lines to CLR pins -->
    <line x1="72" y1="270" x2="72" y2="170" stroke="#dc2626" stroke-width="2" marker-end="url(#redarr)"/>
    <line x1="222" y1="270" x2="222" y2="170" stroke="#dc2626" stroke-width="2" marker-end="url(#redarr)"/>
    <line x1="372" y1="270" x2="372" y2="170" stroke="#dc2626" stroke-width="2" marker-end="url(#redarr)"/>
    <line x1="522" y1="270" x2="522" y2="170" stroke="#dc2626" stroke-width="2" marker-end="url(#redarr)"/>
    <text x="230" y="290" font-weight="bold" fill="#dc2626">Active-Low Clear Bus (Resets at 1010_2 = 10)</text>
  </g>
'''
with open(os.path.join(images_dir, "async_decade_counter_circuit.svg"), "w", encoding="utf-8") as f:
    f.write(svg_wrap(680, 360, async_counter, "Asynchronous (Ripple) Mod-10 Decade Counter with Active-Low NAND Reset"))

# -------------------------------------------------------------
# 6. ALL 4 SHIFT REGISTERS SCHEMATIC
# -------------------------------------------------------------
shift_reg = '''
  <g transform="translate(20, 35)" font-family="Consolas, monospace" font-size="11">
    <!-- 1. SISO -->
    <text x="10" y="20" font-weight="bold" fill="#1e3a8a" font-size="13">1. Serial-In Serial-Out (SISO) [Takes 2n - 1 pulses: 4-bit = 7 pulses]</text>
    <line x1="20" y1="45" x2="50" y2="45" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <text x="5" y="40">Din</text>
    <rect x="50" y="30" width="45" height="30" fill="#f1f5f9" stroke="#1e3a8a" stroke-width="1.5"/><text x="65" y="50">FF3</text>
    <line x1="95" y1="45" x2="115" y2="45" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <rect x="115" y="30" width="45" height="30" fill="#f1f5f9" stroke="#1e3a8a" stroke-width="1.5"/><text x="130" y="50">FF2</text>
    <line x1="160" y1="45" x2="180" y2="45" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <rect x="180" y="30" width="45" height="30" fill="#f1f5f9" stroke="#1e3a8a" stroke-width="1.5"/><text x="195" y="50">FF1</text>
    <line x1="225" y1="45" x2="245" y2="45" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <rect x="245" y="30" width="45" height="30" fill="#f1f5f9" stroke="#1e3a8a" stroke-width="1.5"/><text x="260" y="50">FF0</text>
    <line x1="290" y1="45" x2="320" y2="45" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <text x="325" y="50" font-weight="bold" fill="#15803d">Dout (Serial)</text>

    <!-- 2. SIPO -->
    <text x="10" y="100" font-weight="bold" fill="#1e3a8a" font-size="13">2. Serial-In Parallel-Out (SIPO) [Takes n pulses: 4-bit = 4 pulses]</text>
    <line x1="20" y1="125" x2="50" y2="125" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <text x="5" y="120">Din</text>
    <rect x="50" y="110" width="45" height="30" fill="#f1f5f9" stroke="#1e3a8a" stroke-width="1.5"/><text x="65" y="130">FF3</text>
    <line x1="95" y1="125" x2="115" y2="125" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <rect x="115" y="110" width="45" height="30" fill="#f1f5f9" stroke="#1e3a8a" stroke-width="1.5"/><text x="130" y="130">FF2</text>
    <line x1="160" y1="125" x2="180" y2="125" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <rect x="180" y="110" width="45" height="30" fill="#f1f5f9" stroke="#1e3a8a" stroke-width="1.5"/><text x="195" y="130">FF1</text>
    <line x1="225" y1="125" x2="245" y2="125" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <rect x="245" y="110" width="45" height="30" fill="#f1f5f9" stroke="#1e3a8a" stroke-width="1.5"/><text x="260" y="130">FF0</text>
    <!-- Parallel Outputs -->
    <line x1="72" y1="140" x2="72" y2="160" stroke="#15803d" stroke-width="2" marker-end="url(#arr)"/><text x="68" y="172">Q3</text>
    <line x1="137" y1="140" x2="137" y2="160" stroke="#15803d" stroke-width="2" marker-end="url(#arr)"/><text x="133" y="172">Q2</text>
    <line x1="202" y1="140" x2="202" y2="160" stroke="#15803d" stroke-width="2" marker-end="url(#arr)"/><text x="198" y="172">Q1</text>
    <line x1="267" y1="140" x2="267" y2="160" stroke="#15803d" stroke-width="2" marker-end="url(#arr)"/><text x="263" y="172">Q0</text>

    <!-- 3. PISO -->
    <text x="380" y="20" font-weight="bold" fill="#1e3a8a" font-size="13">3. Parallel-In Serial-Out (PISO) [1 load + (n-1) shift = n pulses]</text>
    <line x1="400" y1="40" x2="400" y2="55" stroke="#b91c1c" stroke-width="1.8" marker-end="url(#arr)"/><text x="395" y="35">D3</text>
    <rect x="380" y="55" width="40" height="25" fill="#f1f5f9" stroke="#1e3a8a" stroke-width="1.5"/><text x="390" y="72">FF3</text>
    <line x1="420" y1="67" x2="445" y2="67" stroke="#1e3a8a" stroke-width="1.5" marker-end="url(#arr)"/>
    <line x1="465" y1="40" x2="465" y2="55" stroke="#b91c1c" stroke-width="1.8" marker-end="url(#arr)"/><text x="460" y="35">D2</text>
    <rect x="445" y="55" width="40" height="25" fill="#f1f5f9" stroke="#1e3a8a" stroke-width="1.5"/><text x="455" y="72">FF2</text>
    <line x1="485" y1="67" x2="510" y2="67" stroke="#1e3a8a" stroke-width="1.5" marker-end="url(#arr)"/>
    <line x1="530" y1="40" x2="530" y2="55" stroke="#b91c1c" stroke-width="1.8" marker-end="url(#arr)"/><text x="525" y="35">D1</text>
    <rect x="510" y="55" width="40" height="25" fill="#f1f5f9" stroke="#1e3a8a" stroke-width="1.5"/><text x="520" y="72">FF1</text>
    <line x1="550" y1="67" x2="575" y2="67" stroke="#1e3a8a" stroke-width="1.5" marker-end="url(#arr)"/>
    <line x1="595" y1="40" x2="595" y2="55" stroke="#b91c1c" stroke-width="1.8" marker-end="url(#arr)"/><text x="590" y="35">D0</text>
    <rect x="575" y="55" width="40" height="25" fill="#f1f5f9" stroke="#1e3a8a" stroke-width="1.5"/><text x="585" y="72">FF0</text>
    <line x1="615" y1="67" x2="640" y2="67" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <text x="645" y="72" font-weight="bold" fill="#15803d">Serial Out</text>

    <!-- 4. PIPO -->
    <text x="380" y="115" font-weight="bold" fill="#1e3a8a" font-size="13">4. Parallel-In Parallel-Out (PIPO) [Takes 1 pulse only]</text>
    <line x1="400" y1="130" x2="400" y2="145" stroke="#b91c1c" stroke-width="1.8" marker-end="url(#arr)"/><text x="395" y="127">D3</text>
    <rect x="380" y="145" width="40" height="25" fill="#f1f5f9" stroke="#1e3a8a" stroke-width="1.5"/><text x="390" y="162">FF3</text>
    <line x1="400" y1="170" x2="400" y2="185" stroke="#15803d" stroke-width="1.8" marker-end="url(#arr)"/><text x="395" y="198">Q3</text>
    
    <line x1="465" y1="130" x2="465" y2="145" stroke="#b91c1c" stroke-width="1.8" marker-end="url(#arr)"/><text x="460" y="127">D2</text>
    <rect x="445" y="145" width="40" height="25" fill="#f1f5f9" stroke="#1e3a8a" stroke-width="1.5"/><text x="455" y="162">FF2</text>
    <line x1="465" y1="170" x2="465" y2="185" stroke="#15803d" stroke-width="1.8" marker-end="url(#arr)"/><text x="460" y="198">Q2</text>

    <line x1="530" y1="130" x2="530" y2="145" stroke="#b91c1c" stroke-width="1.8" marker-end="url(#arr)"/><text x="525" y="127">D1</text>
    <rect x="510" y="145" width="40" height="25" fill="#f1f5f9" stroke="#1e3a8a" stroke-width="1.5"/><text x="520" y="162">FF1</text>
    <line x1="530" y1="170" x2="530" y2="185" stroke="#15803d" stroke-width="1.8" marker-end="url(#arr)"/><text x="525" y="198">Q1</text>

    <line x1="595" y1="130" x2="595" y2="145" stroke="#b91c1c" stroke-width="1.8" marker-end="url(#arr)"/><text x="590" y="127">D0</text>
    <rect x="575" y="145" width="40" height="25" fill="#f1f5f9" stroke="#1e3a8a" stroke-width="1.5"/><text x="585" y="162">FF0</text>
    <line x1="595" y1="170" x2="595" y2="185" stroke="#15803d" stroke-width="1.8" marker-end="url(#arr)"/><text x="590" y="198">Q0</text>
  </g>
'''
with open(os.path.join(images_dir, "shift_registers_all4.svg"), "w", encoding="utf-8") as f:
    f.write(svg_wrap(750, 260, shift_reg, "All 4 Shift Registers (SISO, SIPO, PISO, PIPO) Architectures & Timing"))

print("All 6 primary SVGs generated successfully in:", images_dir)
