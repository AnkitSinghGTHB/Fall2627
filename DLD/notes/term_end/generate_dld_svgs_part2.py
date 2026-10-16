# -*- coding: utf-8 -*-
"""
Generate remaining publication-quality SVG circuit diagrams for ECE2002 DLD
"""
import os

images_dir = r"c:\Users\ankit\Fall2627\DLD\notes\term_end\images"
os.makedirs(images_dir, exist_ok=True)

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
# 7. SR LATCHES (NOR & NAND) SCHEMATIC
# -------------------------------------------------------------
sr_latches = '''
  <g transform="translate(30, 40)" font-family="Consolas, monospace" font-size="12">
    <!-- 1. NOR Latch (Left) -->
    <text x="20" y="20" font-weight="bold" fill="#1e3a8a" font-size="13">1. SR Latch using NOR Gates (Active-High)</text>
    
    <!-- Top NOR Gate (R Input) -->
    <line x1="20" y1="55" x2="60" y2="55" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/><text x="5" y="60">R</text>
    <line x1="20" y1="75" x2="60" y2="75" stroke="#1e3a8a" stroke-width="1.8"/>
    <path d="M 55 45 Q 70 65 55 85 Q 90 85 105 65 Q 90 45 55 45 Z" fill="#f8fafc" stroke="#1e3a8a" stroke-width="2"/>
    <circle cx="109" cy="65" r="3.5" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="113" y1="65" x2="230" y2="65" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <circle cx="180" cy="65" r="3" fill="#1e3a8a"/>
    <text x="235" y="70" font-weight="bold" fill="#15803d" font-size="14">Q</text>

    <!-- Bottom NOR Gate (S Input) -->
    <line x1="20" y1="145" x2="60" y2="145" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="20" y1="165" x2="60" y2="165" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/><text x="5" y="170">S</text>
    <path d="M 55 135 Q 70 155 55 175 Q 90 175 105 155 Q 90 135 55 135 Z" fill="#f8fafc" stroke="#1e3a8a" stroke-width="2"/>
    <circle cx="109" cy="155" r="3.5" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="113" y1="155" x2="230" y2="155" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <circle cx="170" cy="155" r="3" fill="#1e3a8a"/>
    <text x="235" y="160" font-weight="bold" fill="#15803d" font-size="14">Q'</text>

    <!-- Cross-Coupled Feedback Lines -->
    <line x1="180" y1="65" x2="180" y2="100" stroke="#dc2626" stroke-width="1.5"/>
    <line x1="180" y1="100" x2="40" y2="120" stroke="#dc2626" stroke-width="1.5"/>
    <line x1="40" y1="120" x2="40" y2="145" stroke="#dc2626" stroke-width="1.5"/>
    <line x1="40" y1="145" x2="60" y2="145" stroke="#dc2626" stroke-width="1.5"/>

    <line x1="170" y1="155" x2="170" y2="120" stroke="#16a34a" stroke-width="1.5"/>
    <line x1="170" y1="120" x2="40" y2="100" stroke="#16a34a" stroke-width="1.5"/>
    <line x1="40" y1="100" x2="40" y2="75" stroke="#16a34a" stroke-width="1.5"/>
    <line x1="40" y1="75" x2="60" y2="75" stroke="#16a34a" stroke-width="1.5"/>

    <!-- 2. NAND Latch (Right) -->
    <g transform="translate(340, 0)">
      <text x="20" y="20" font-weight="bold" fill="#1e3a8a" font-size="13">2. SR Latch using NAND Gates (Active-Low)</text>
      <!-- Top NAND Gate (S' Input) -->
      <line x1="20" y1="55" x2="60" y2="55" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/><text x="2" y="60">S'</text>
      <line x1="20" y1="75" x2="60" y2="75" stroke="#1e3a8a" stroke-width="1.8"/>
      <path d="M 60 45 L 80 45 A 20 20 0 0 1 80 85 L 60 85 Z" fill="#f8fafc" stroke="#1e3a8a" stroke-width="2"/>
      <circle cx="104" cy="65" r="3.5" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.8"/>
      <line x1="108" y1="65" x2="230" y2="65" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
      <circle cx="180" cy="65" r="3" fill="#1e3a8a"/>
      <text x="235" y="70" font-weight="bold" fill="#15803d" font-size="14">Q</text>

      <!-- Bottom NAND Gate (R' Input) -->
      <line x1="20" y1="145" x2="60" y2="145" stroke="#1e3a8a" stroke-width="1.8"/>
      <line x1="20" y1="165" x2="60" y2="165" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/><text x="2" y="170">R'</text>
      <path d="M 60 135 L 80 135 A 20 20 0 0 1 80 175 L 60 175 Z" fill="#f8fafc" stroke="#1e3a8a" stroke-width="2"/>
      <circle cx="104" cy="155" r="3.5" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.8"/>
      <line x1="108" y1="155" x2="230" y2="155" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
      <circle cx="170" cy="155" r="3" fill="#1e3a8a"/>
      <text x="235" y="160" font-weight="bold" fill="#15803d" font-size="14">Q'</text>

      <!-- Cross Feedback -->
      <line x1="180" y1="65" x2="180" y2="100" stroke="#dc2626" stroke-width="1.5"/>
      <line x1="180" y1="100" x2="40" y2="120" stroke="#dc2626" stroke-width="1.5"/>
      <line x1="40" y1="120" x2="40" y2="145" stroke="#dc2626" stroke-width="1.5"/>
      <line x1="40" y1="145" x2="60" y2="145" stroke="#dc2626" stroke-width="1.5"/>

      <line x1="170" y1="155" x2="170" y2="120" stroke="#16a34a" stroke-width="1.5"/>
      <line x1="170" y1="120" x2="40" y2="100" stroke="#16a34a" stroke-width="1.5"/>
      <line x1="40" y1="100" x2="40" y2="75" stroke="#16a34a" stroke-width="1.5"/>
      <line x1="40" y1="75" x2="60" y2="75" stroke="#16a34a" stroke-width="1.5"/>
    </g>
  </g>
'''
with open(os.path.join(images_dir, "sr_latches.svg"), "w", encoding="utf-8") as f:
    f.write(svg_wrap(700, 270, sr_latches, "Cross-Coupled SR Latches: NOR Gate vs NAND Gate Configurations"))

# -------------------------------------------------------------
# 8. FULL ADDER USING 3:8 DECODER SCHEMATIC
# -------------------------------------------------------------
fa_decoder = '''
  <g transform="translate(40, 40)" font-family="Consolas, monospace" font-size="12">
    <!-- 3:8 Decoder Block -->
    <rect x="50" y="30" width="160" height="260" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2" rx="6"/>
    <text x="130" y="60" text-anchor="middle" font-weight="bold" fill="#1e3a8a" font-size="14">3:8 Decoder</text>
    <text x="130" y="78" text-anchor="middle" font-size="10" fill="#64748b">(74LS138 Active-Low)</text>
    
    <!-- Inputs A, B, Cin -->
    <line x1="0" y1="110" x2="50" y2="110" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/><text x="10" y="105">A (S2)</text>
    <line x1="0" y1="160" x2="50" y2="160" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/><text x="10" y="155">B (S1)</text>
    <line x1="0" y1="210" x2="50" y2="210" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/><text x="10" y="205">Cin(S0)</text>

    <!-- Outputs Y0 to Y7 -->
    <text x="180" y="100">Y0'</text><line x1="210" y1="95" x2="230" y2="95" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="180" y="120">Y1'</text><line x1="210" y1="115" x2="330" y2="115" stroke="#1e3a8a" stroke-width="1.8"/>
    <text x="180" y="140">Y2'</text><line x1="210" y1="135" x2="330" y2="135" stroke="#1e3a8a" stroke-width="1.8"/>
    <text x="180" y="160">Y3'</text><line x1="210" y1="155" x2="330" y2="155" stroke="#dc2626" stroke-width="1.8"/>
    <text x="180" y="180">Y4'</text><line x1="210" y1="175" x2="330" y2="175" stroke="#1e3a8a" stroke-width="1.8"/>
    <text x="180" y="200">Y5'</text><line x1="210" y1="195" x2="330" y2="195" stroke="#dc2626" stroke-width="1.8"/>
    <text x="180" y="220">Y6'</text><line x1="210" y1="215" x2="330" y2="215" stroke="#dc2626" stroke-width="1.8"/>
    <text x="180" y="240">Y7'</text><line x1="210" y1="235" x2="310" y2="235" stroke="#1e3a8a" stroke-width="1.8"/>

    <!-- Tap off Y7 for both NAND gates -->
    <circle cx="300" cy="235" r="3" fill="#1e3a8a"/>
    <line x1="300" y1="235" x2="330" y2="235" stroke="#dc2626" stroke-width="1.8"/>
    <line x1="300" y1="235" x2="300" y2="105" stroke="#1e3a8a" stroke-width="1.8"/>
    <line x1="300" y1="105" x2="330" y2="105" stroke="#1e3a8a" stroke-width="1.8"/>

    <!-- Sum 4-input NAND Gate (Y1, Y2, Y4, Y7) -->
    <path d="M 330 85 L 355 85 A 25 25 0 0 1 355 135 L 330 135 Z" fill="#f8fafc" stroke="#1e3a8a" stroke-width="2"/>
    <circle cx="384" cy="110" r="4" fill="#ffffff" stroke="#1e3a8a" stroke-width="2"/>
    <line x1="388" y1="110" x2="480" y2="110" stroke="#1e3a8a" stroke-width="2.5" marker-end="url(#arr)"/>
    <text x="490" y="115" font-weight="bold" fill="#1e3a8a" font-size="14">Sum S = Σm(1,2,4,7)</text>

    <!-- Carry 4-input NAND Gate (Y3, Y5, Y6, Y7) -->
    <path d="M 330 180 L 355 180 A 25 25 0 0 1 355 230 L 330 230 Z" fill="#f8fafc" stroke="#dc2626" stroke-width="2"/>
    <circle cx="384" cy="205" r="4" fill="#ffffff" stroke="#dc2626" stroke-width="2"/>
    <line x1="388" y1="205" x2="480" y2="205" stroke="#dc2626" stroke-width="2.5" marker-end="url(#redarr)"/>
    <text x="490" y="210" font-weight="bold" fill="#dc2626" font-size="14">Cout = Σm(3,5,6,7)</text>
  </g>
'''
with open(os.path.join(images_dir, "full_adder_decoder.svg"), "w", encoding="utf-8") as f:
    f.write(svg_wrap(740, 360, fa_decoder, "Full Adder Implementation using 3:8 Active-Low Decoder & NAND Gates"))

# -------------------------------------------------------------
# 9. RING COUNTER VS JOHNSON COUNTER
# -------------------------------------------------------------
ring_johnson = '''
  <g transform="translate(30, 40)" font-family="Consolas, monospace" font-size="11">
    <!-- 1. Ring Counter (Top) -->
    <text x="10" y="20" font-weight="bold" fill="#1e3a8a" font-size="13">1. 4-Bit Ring Counter [States = 4, f_out = f_clk / 4, Preset = 1000]</text>
    <rect x="40" y="40" width="70" height="60" fill="#eff6ff" stroke="#1e3a8a" stroke-width="1.8" rx="4"/><text x="75" y="75" text-anchor="middle">FF3</text>
    <line x1="110" y1="70" x2="160" y2="70" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <rect x="160" y="40" width="70" height="60" fill="#eff6ff" stroke="#1e3a8a" stroke-width="1.8" rx="4"/><text x="195" y="75" text-anchor="middle">FF2</text>
    <line x1="230" y1="70" x2="280" y2="70" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <rect x="280" y="40" width="70" height="60" fill="#eff6ff" stroke="#1e3a8a" stroke-width="1.8" rx="4"/><text x="315" y="75" text-anchor="middle">FF1</text>
    <line x1="350" y1="70" x2="400" y2="70" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
    <rect x="400" y="40" width="70" height="60" fill="#eff6ff" stroke="#1e3a8a" stroke-width="1.8" rx="4"/><text x="435" y="75" text-anchor="middle">FF0</text>
    <!-- Straight Feedback Q0 to D3 -->
    <line x1="470" y1="70" x2="510" y2="70" stroke="#15803d" stroke-width="2"/>
    <line x1="510" y1="70" x2="510" y2="120" stroke="#15803d" stroke-width="2"/>
    <line x1="510" y1="120" x2="20" y2="120" stroke="#15803d" stroke-width="2"/>
    <line x1="20" y1="120" x2="20" y2="70" stroke="#15803d" stroke-width="2"/>
    <line x1="20" y1="70" x2="40" y2="70" stroke="#15803d" stroke-width="2" marker-end="url(#arr)"/>
    <text x="210" y="115" font-weight="bold" fill="#15803d">Straight Feedback: Q0 to D3</text>

    <!-- 2. Johnson Counter (Bottom) -->
    <g transform="translate(0, 160)">
      <text x="10" y="20" font-weight="bold" fill="#1e3a8a" font-size="13">2. 4-Bit Johnson (Twisted-Ring) Counter [States = 8, f_out = f_clk / 8, Clear = 0000]</text>
      <rect x="40" y="40" width="70" height="60" fill="#fdf4ff" stroke="#c026d3" stroke-width="1.8" rx="4"/><text x="75" y="75" text-anchor="middle">FF3</text>
      <line x1="110" y1="70" x2="160" y2="70" stroke="#c026d3" stroke-width="2" marker-end="url(#arr)"/>
      <rect x="160" y="40" width="70" height="60" fill="#fdf4ff" stroke="#c026d3" stroke-width="1.8" rx="4"/><text x="195" y="75" text-anchor="middle">FF2</text>
      <line x1="230" y1="70" x2="280" y2="70" stroke="#c026d3" stroke-width="2" marker-end="url(#arr)"/>
      <rect x="280" y="40" width="70" height="60" fill="#fdf4ff" stroke="#c026d3" stroke-width="1.8" rx="4"/><text x="315" y="75" text-anchor="middle">FF1</text>
      <line x1="350" y1="70" x2="400" y2="70" stroke="#c026d3" stroke-width="2" marker-end="url(#arr)"/>
      <rect x="400" y="40" width="70" height="60" fill="#fdf4ff" stroke="#c026d3" stroke-width="1.8" rx="4"/><text x="435" y="75" text-anchor="middle">FF0</text>
      <!-- Inverted Feedback Q0' to D3 -->
      <line x1="470" y1="85" x2="510" y2="85" stroke="#dc2626" stroke-width="2"/>
      <line x1="510" y1="85" x2="510" y2="120" stroke="#dc2626" stroke-width="2"/>
      <line x1="510" y1="120" x2="20" y2="120" stroke="#dc2626" stroke-width="2"/>
      <line x1="20" y1="120" x2="20" y2="70" stroke="#dc2626" stroke-width="2"/>
      <line x1="20" y1="70" x2="40" y2="70" stroke="#dc2626" stroke-width="2" marker-end="url(#redarr)"/>
      <text x="190" y="115" font-weight="bold" fill="#dc2626">Inverted Feedback: Q0' (Complement) to D3</text>
    </g>
  </g>
'''
with open(os.path.join(images_dir, "ring_and_johnson_counters.svg"), "w", encoding="utf-8") as f:
    f.write(svg_wrap(680, 360, ring_johnson, "Ring Counter vs Johnson Counter Architecture & Feedback Wiring"))

print("All remaining SVGs successfully generated!")
