"""
Production-grade IEEE standard logic gate schematic renderer for DLD CAT-2:
Module 3 (Sequential Circuits, Latches, Flip-Flops, Master-Slave, Conversions, Registers)
Module 4 (Asynchronous Ripple Counters, Synchronous Counters, Mod-N Reset, FSM Mealy/Moore)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import sys

# Add directory to path to import helpers from render_circuits
CURRENT_DIR = r"c:\Users\ankit\Fall2627\DLD\notes\cat2\circuits"
sys.path.append(CURRENT_DIR)

from render_circuits import (
    draw_ortho, draw_path, draw_dot,
    draw_and, draw_nand, draw_or, draw_nor, draw_xor, draw_not, draw_flip_flop,
    OUT_DIR
)

# ----------------- EXTENDED PRIMITIVES -----------------

def draw_box(ax, x, y, w, h, title="", subtitle="", color="#f8fafc", border="#1e293b", lw=2.0, title_color="#0f172a"):
    """Draws a generic block/module box with centered title and optional subtitle"""
    rect = patches.FancyBboxPatch((x, y - h/2), w, h, boxstyle="square,pad=0",
                                  facecolor=color, edgecolor=border, lw=lw, zorder=3)
    ax.add_patch(rect)
    if subtitle:
        ax.text(x + w/2, y + 0.22*h, title, ha='center', va='center', fontsize=9.0, fontweight='bold', color=title_color, zorder=4)
        ax.text(x + w/2, y - 0.18*h, subtitle, ha='center', va='center', fontsize=7.5, color="#64748b", zorder=4)
    else:
        ax.text(x + w/2, y, title, ha='center', va='center', fontsize=9.0, fontweight='bold', color=title_color, zorder=4)
    return {
        'left': (x, y),
        'right': (x + w, y),
        'top': (x + w/2, y + h/2),
        'bottom': (x + w/2, y - h/2),
        'in1': (x, y + 0.28*h),
        'in2': (x, y - 0.28*h),
        'out1': (x + w, y + 0.28*h),
        'out2': (x + w, y - 0.28*h)
    }

def draw_mux_2to1(ax, x, y, w=1.5, h=2.4, label="2:1 MUX", color="#f0fdf4", border="#15803d"):
    """Draws standard IEEE trapezoidal 2-to-1 Multiplexer"""
    pts = np.array([
        [x, y - h/2],
        [x + w, y - h*0.35],
        [x + w, y + h*0.35],
        [x, y + h/2]
    ])
    poly = patches.Polygon(pts, closed=True, facecolor=color, edgecolor=border, lw=2.0, zorder=3)
    ax.add_patch(poly)
    ax.text(x + w*0.48, y, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color=border, zorder=4)
    ax.text(x + 0.22, y + h*0.28, "0", ha='left', va='center', fontsize=7.5, fontweight='bold', color="#475569", zorder=4)
    ax.text(x + 0.22, y - h*0.28, "1", ha='left', va='center', fontsize=7.5, fontweight='bold', color="#475569", zorder=4)
    ax.text(x + w*0.48, y - h*0.38, "S", ha='center', va='top', fontsize=7.5, fontweight='bold', color="#475569", zorder=4)
    return {
        'in0': (x, y + h*0.28),
        'in1': (x, y - h*0.28),
        'sel': (x + w*0.48, y - h*0.42),
        'out': (x + w, y)
    }

def draw_mux_4to1(ax, x, y, w=1.8, h=3.4, label="4:1 MUX", color="#f0fdf4", border="#15803d"):
    """Draws standard IEEE trapezoidal 4-to-1 Multiplexer"""
    pts = np.array([
        [x, y - h/2],
        [x + w, y - h*0.36],
        [x + w, y + h*0.36],
        [x, y + h/2]
    ])
    poly = patches.Polygon(pts, closed=True, facecolor=color, edgecolor=border, lw=2.0, zorder=3)
    ax.add_patch(poly)
    ax.text(x + w*0.5, y, label, ha='center', va='center', fontsize=8.0, fontweight='bold', color=border, zorder=4)
    for idx, frac in enumerate([0.33, 0.11, -0.11, -0.33]):
        ax.text(x + 0.22, y + h*frac, str(idx), ha='left', va='center', fontsize=7.5, fontweight='bold', color="#475569", zorder=4)
    return {
        'in0': (x, y + h*0.33),
        'in1': (x, y + h*0.11),
        'in2': (x, y - h*0.11),
        'in3': (x, y - h*0.33),
        'sel0': (x + w*0.35, y - h*0.42),
        'sel1': (x + w*0.65, y - h*0.42),
        'out': (x + w, y)
    }


# =====================================================================
# MODULE 3 CIRCUITS
# =====================================================================

def gen_m3_jk_ff():
    """Module 3 - Section 2B: Clocked JK Flip-Flop with Cross-Coupled Feedback"""
    fig, ax = plt.subplots(figsize=(12, 7.0), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10.5)
    ax.axis('off')

    ax.text(8.0, 9.9, "Clocked JK Flip-Flop with Cross-Coupled Feedback", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(8.0, 9.4, "Module 3 - Section 2B | Solves SR Invalid State via Output Feedback (Toggle Mode)", ha='center', fontsize=9.5, color="#64748b")

    # Input Steering NAND Gates (3-input)
    nand1 = draw_nand(ax, 3.2, 7.0, w=1.8, h=1.5, label="NAND 1\nSteering")
    nand2 = draw_nand(ax, 3.2, 3.0, w=1.8, h=1.5, label="NAND 2\nSteering")

    # Latch NAND Gates (2-input)
    nand3 = draw_nand(ax, 9.2, 7.0, w=1.8, h=1.5, label="NAND 3\nLatch")
    nand4 = draw_nand(ax, 9.2, 3.0, w=1.8, h=1.5, label="NAND 4\nLatch")

    # External Inputs J and K
    draw_ortho(ax, (1.0, nand1['in_3_top'][1]), nand1['in_3_top'], label="J (Set)", label_pos=(1.4, nand1['in_3_top'][1] + 0.35))
    draw_ortho(ax, (1.0, nand2['in_3_bot'][1]), nand2['in_3_bot'], label="K (Reset)", label_pos=(1.4, nand2['in_3_bot'][1] - 0.35))

    # Common Clock Pulse
    draw_path(ax, [(1.0, 5.0), (2.2, 5.0), (2.2, nand1['in_3_mid'][1]), nand1['in_3_mid']], label="CLK", label_pos=(1.3, 5.35))
    draw_path(ax, [(2.2, 5.0), (2.2, nand2['in_3_mid'][1]), nand2['in_3_mid']])
    draw_dot(ax, 2.2, 5.0)

    # Inter-stage Steering to Latch Wires
    draw_ortho(ax, nand1['out'], nand3['in1'], x_break=6.8, label=r"$\overline{S}$", label_pos=(6.5, nand1['out'][1] + 0.35))
    draw_ortho(ax, nand2['out'], nand4['in2'], x_break=6.8, label=r"$\overline{R}$", label_pos=(6.5, nand2['out'][1] - 0.35))

    # Internal Latch Cross-Coupling
    draw_dot(ax, 11.8, nand3['out'][1])
    draw_path(ax, [(11.8, nand3['out'][1]), (11.8, 5.4), (8.2, 5.4), (8.2, nand4['in1'][1]), nand4['in1']])

    draw_dot(ax, 12.1, nand4['out'][1])
    draw_path(ax, [(12.1, nand4['out'][1]), (12.1, 4.6), (7.9, 4.6), (7.9, nand3['in2'][1]), nand3['in2']])

    # External Outputs Q and Q'
    draw_ortho(ax, nand3['out'], (15.0, nand3['out'][1]), label="Q (Output)", label_pos=(14.2, nand3['out'][1] + 0.35))
    draw_ortho(ax, nand4['out'], (15.0, nand4['out'][1]), label=r"$\overline{Q}$ (Output)", label_pos=(14.2, nand4['out'][1] - 0.35))

    # Long Feedback Lines:
    # Q' output feeds back to NAND 1 in_3_bot
    draw_dot(ax, 13.5, nand4['out'][1])
    draw_path(ax, [(13.5, nand4['out'][1]), (13.5, 1.8), (2.5, 1.8), (2.5, nand1['in_3_bot'][1]), nand1['in_3_bot']],
              color="#0284c7", lw=1.6, label=r"$\overline{Q} \text{ Feedback}$", label_pos=(8.0, 1.5), label_color="#0284c7")

    # Q output feeds back to NAND 2 in_3_top
    draw_dot(ax, 13.0, nand3['out'][1])
    draw_path(ax, [(13.0, nand3['out'][1]), (13.0, 8.5), (2.8, 8.5), (2.8, nand2['in_3_top'][1]), nand2['in_3_top']],
              color="#059669", lw=1.6, label=r"$Q \text{ Feedback}$", label_pos=(8.0, 8.8), label_color="#059669")

    # Explanatory Box
    note_txt = (
        "WHY TOGGLE OCCURS AT J=1, K=1:\n"
        "• If current state Q=0 (Q'=1): Q' enables top NAND 1, forcing next state to SET (Q -> 1).\n"
        "• If current state Q=1 (Q'=0): Q enables bottom NAND 2, forcing next state to RESET (Q -> 0).\n"
        "• Hence, when J=K=1, the circuit deterministically inverts its state on every clock pulse: Q+ = Q'"
    )
    ax.text(8.0, 0.7, note_txt, ha='center', va='center', fontsize=8.0, color="#1e3a8a",
            bbox=dict(boxstyle='round,pad=0.35', fc='#eff6ff', ec='#93c5fd', lw=1.2))

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_jk_ff.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_jk_ff.svg"))
    plt.close()
    print("Generated circuit_m3_jk_ff")

def gen_m3_d_and_t_ff():
    """Module 3 - Section 2C & 2D: D Flip-Flop and T Flip-Flop Derivation from JK"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6.5), dpi=300)
    for ax in (ax1, ax2):
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 9)
        ax.axis('off')

    # Subplot 1: D Flip-Flop
    ax1.text(6.0, 8.5, "D (Data / Delay) Flip-Flop", ha='center', fontsize=12, fontweight='bold', color="#0f172a")
    ax1.text(6.0, 8.0, r"Derived from JK using Inverter: $J = D, \quad K = \overline{D}$", ha='center', fontsize=8.5, color="#64748b")

    ff_d = draw_flip_flop(ax1, 6.5, 4.5, ff_type="JK", name="JK Core", clk_edge="pos")
    not_d = draw_not(ax1, 3.2, 3.2, w=1.2, h=0.8, label="NOT")

    # D Input
    draw_ortho(ax1, (0.8, 5.8), (2.0, 5.8), label="Data In (D)", label_pos=(1.2, 6.2))
    draw_dot(ax1, 2.0, 5.8)
    draw_ortho(ax1, (2.0, 5.8), ff_d['J'], label="J = D", label_pos=(4.5, 6.1))
    draw_path(ax1, [(2.0, 5.8), (2.0, not_d['in'][1]), not_d['in']])
    draw_ortho(ax1, not_d['out'], ff_d['K'], label=r"$K = \overline{D}$", label_pos=(5.3, 3.5))

    # Clock
    draw_ortho(ax1, (0.8, ff_d['CLK'][1]), ff_d['CLK'], label="CLK", label_pos=(3.5, ff_d['CLK'][1] + 0.35))

    # Outputs
    draw_ortho(ax1, ff_d['Q'], (11.2, ff_d['Q'][1]), label="Q (Output: Q+ = D)", label_pos=(10.0, ff_d['Q'][1] + 0.35))
    draw_ortho(ax1, ff_d['Q_bar'], (11.2, ff_d['Q_bar'][1]), label=r"$\overline{Q}$", label_pos=(10.0, ff_d['Q_bar'][1] - 0.35))

    note_d = "OPERATION:\n• D = 0 -> J=0, K=1 -> RESET (Q+ = 0)\n• D = 1 -> J=1, K=0 -> SET (Q+ = 1)\nEquation: Q+ = D (Zero invalid states!)"
    ax1.text(6.0, 1.2, note_d, ha='center', va='center', fontsize=7.5, color="#1e3a8a",
             bbox=dict(boxstyle='round,pad=0.3', fc='#f0f9ff', ec='#bae6fd'))

    # Subplot 2: T Flip-Flop
    ax2.text(6.0, 8.5, "T (Toggle) Flip-Flop", ha='center', fontsize=12, fontweight='bold', color="#0f172a")
    ax2.text(6.0, 8.0, r"Derived from JK by Tying Inputs: $J = K = T$", ha='center', fontsize=8.5, color="#64748b")

    ff_t = draw_flip_flop(ax2, 6.5, 4.5, ff_type="JK", name="JK Core", clk_edge="pos")

    # T Input tied together
    draw_ortho(ax2, (0.8, 4.5), (2.5, 4.5), label="Toggle In (T)", label_pos=(1.4, 4.9))
    draw_dot(ax2, 2.5, 4.5)
    draw_path(ax2, [(2.5, 4.5), (2.5, ff_t['J'][1]), ff_t['J']], label="J = T", label_pos=(4.5, ff_t['J'][1] + 0.35))
    draw_path(ax2, [(2.5, 4.5), (2.5, ff_t['K'][1]), ff_t['K']], label="K = T", label_pos=(4.5, ff_t['K'][1] - 0.35))

    # Clock
    draw_ortho(ax2, (0.8, ff_t['CLK'][1]), ff_t['CLK'], label="CLK", label_pos=(4.5, ff_t['CLK'][1] + 0.35))

    # Outputs
    draw_ortho(ax2, ff_t['Q'], (11.2, ff_t['Q'][1]), label=r"Q (Output: $Q^+ = T \oplus Q$)", label_pos=(9.8, ff_t['Q'][1] + 0.35))
    draw_ortho(ax2, ff_t['Q_bar'], (11.2, ff_t['Q_bar'][1]), label=r"$\overline{Q}$", label_pos=(10.0, ff_t['Q_bar'][1] - 0.35))

    note_t = "OPERATION:\n• T = 0 -> J=0, K=0 -> HOLD (Q+ = Q)\n• T = 1 -> J=1, K=1 -> TOGGLE (Q+ = Q')\nIdeal for Frequency Dividers & Binary Counters!"
    ax2.text(6.0, 1.2, note_t, ha='center', va='center', fontsize=7.5, color="#581c87",
             bbox=dict(boxstyle='round,pad=0.3', fc='#faf5ff', ec='#e9d5ff'))

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_d_and_t_ff.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_d_and_t_ff.svg"))
    plt.close()
    print("Generated circuit_m3_d_and_t_ff")

def gen_m3_master_slave_jk():
    """Module 3 - Section 3: Master-Slave JK Flip-Flop Architecture"""
    fig, ax = plt.subplots(figsize=(15, 8.0), dpi=300)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 11)
    ax.axis('off')

    ax.text(10.0, 10.4, "Master-Slave JK Flip-Flop Architecture", ha='center', fontsize=14, fontweight='bold', color="#0f172a")
    ax.text(10.0, 9.9, "Eliminates Race-Around Condition via Dual-Stage Clock Phase Isolation", ha='center', fontsize=10, color="#64748b")

    # Master Flip-Flop Block
    master = draw_box(ax, 5.0, 6.2, w=3.4, h=4.2, title="MASTER FLIP-FLOP", subtitle="Active when CLK = 1\n(Slave is Disabled)",
                      color="#eff6ff", border="#1d4ed8")
    # Slave Flip-Flop Block
    slave = draw_box(ax, 11.8, 6.2, w=3.4, h=4.2, title="SLAVE FLIP-FLOP", subtitle="Active when CLK = 0\n(Master is Disabled)",
                     color="#fefce8", border="#b45309")

    # Master Clock and Inverter
    inv = draw_not(ax, 9.4, 3.6, w=1.2, h=0.8, label="NOT")

    draw_ortho(ax, (0.8, 3.6), (4.0, 3.6), label="Clock Pulse (CLK)", label_pos=(2.2, 4.0))
    draw_dot(ax, 4.0, 3.6)
    draw_path(ax, [(4.0, 3.6), (4.0, master['bottom'][1] + 0.6), (5.0, master['bottom'][1] + 0.6)], label="CLK", label_pos=(4.5, master['bottom'][1] + 0.9))
    draw_ortho(ax, (4.0, 3.6), inv['in'])
    draw_path(ax, [inv['out'], (11.8, inv['out'][1]), (11.8, slave['bottom'][1] + 0.6)], label=r"$\overline{CLK}$", label_pos=(11.0, 3.9))

    # External Inputs J and K
    draw_ortho(ax, (0.8, master['in1'][1]), master['in1'], label="J (Input)", label_pos=(2.5, master['in1'][1] + 0.35))
    draw_ortho(ax, (0.8, master['in2'][1]), master['in2'], label="K (Input)", label_pos=(2.5, master['in2'][1] - 0.35))

    # Inter-stage Master to Slave Connections
    draw_ortho(ax, master['out1'], slave['in1'], label=r"$Q_M$", label_pos=(10.1, master['out1'][1] + 0.35))
    draw_ortho(ax, master['out2'], slave['in2'], label=r"$\overline{Q_M}$", label_pos=(10.1, master['out2'][1] - 0.35))

    # Final Outputs Q and Q'
    draw_ortho(ax, slave['out1'], (18.5, slave['out1'][1]), label="Q (Final Output)", label_pos=(17.2, slave['out1'][1] + 0.35))
    draw_ortho(ax, slave['out2'], (18.5, slave['out2'][1]), label=r"$\overline{Q}$ (Final Output)", label_pos=(17.2, slave['out2'][1] - 0.35))

    # Isolated Feedback loops from Slave outputs to Master inputs
    draw_dot(ax, 16.5, slave['out1'][1])
    draw_path(ax, [(16.5, slave['out1'][1]), (16.5, 9.4), (2.0, 9.4), (2.0, master['in2'][1] + 0.4), (5.0, master['in2'][1] + 0.4)],
              color="#059669", lw=1.6, label="Q Feedback into K steering", label_pos=(10.0, 9.7), label_color="#059669")

    draw_dot(ax, 17.0, slave['out2'][1])
    draw_path(ax, [(17.0, slave['out2'][1]), (17.0, 2.2), (2.3, 2.2), (2.3, master['in1'][1] - 0.4), (5.0, master['in1'][1] - 0.4)],
              color="#dc2626", lw=1.6, label=r"$\overline{Q} \text{ Feedback into J steering}$", label_pos=(10.0, 1.9), label_color="#dc2626")

    # Race-around elimination proof box
    proof_txt = (
        "HOW RACE-AROUND IS PHYSICALLY IMPOSSIBLE:\n"
        "1. Clock HIGH (CLK = 1): Master accepts J, K and updates QM. Meanwhile, inverter forces CLK_Slave = 0, so Slave is disabled and isolates Q.\n"
        "2. Clock Transition to LOW (1 -> 0): Master is instantly disabled. Slave turns ON and transfers QM to Q.\n"
        "3. Since Master and Slave are NEVER simultaneously active, outputs cannot race back to input during the same clock cycle!"
    )
    ax.text(10.0, 0.7, proof_txt, ha='center', va='center', fontsize=8.0, color="#1e293b",
            bbox=dict(boxstyle='round,pad=0.4', fc='#f8fafc', ec='#cbd5e1', lw=1.2))

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_master_slave_jk.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_master_slave_jk.svg"))
    plt.close()
    print("Generated circuit_m3_master_slave_jk")

def gen_m3_ff_conversion():
    """Module 3 - Section 4: Universal Flip-Flop Conversion Blueprint Schematic"""
    fig, ax = plt.subplots(figsize=(13, 6.5), dpi=300)
    ax.set_xlim(0, 17)
    ax.set_ylim(0, 9.5)
    ax.axis('off')

    ax.text(8.5, 9.0, "Universal Flip-Flop Conversion Blueprint", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(8.5, 8.5, "Converting Available Flip-Flop (e.g. JK) to Target Flip-Flop (e.g. D or T)", ha='center', fontsize=9.5, color="#64748b")

    # Outer dashed boundary for the New Composite Flip-Flop
    boundary = patches.FancyBboxPatch((4.2, 1.5), 10.2, 6.2, boxstyle="round,pad=0.2",
                                     facecolor='#f8fafc', edgecolor='#6366f1', lw=2.0, ls='--', zorder=1)
    ax.add_patch(boundary)
    ax.text(9.3, 7.4, "TARGET FLIP-FLOP BOUNDARY (Composite)", ha='center', fontsize=9.0, fontweight='bold', color="#4f46e5", zorder=2)

    # Combinational Logic Block (Derived from K-Maps)
    comb = draw_box(ax, 4.8, 4.5, w=3.6, h=3.6, title="COMBINATIONAL\nLOGIC", subtitle="Synthesized from\nK-Map Minimization",
                    color="#fdf4ff", border="#9333ea")

    # Available Flip-Flop Block (e.g. JK FF)
    avail_ff = draw_flip_flop(ax, 10.8, 4.5, w=2.4, h=3.4, ff_type="JK", name="Available FF", clk_edge="pos")

    # Target Inputs entering Combinational Logic
    draw_ortho(ax, (0.8, comb['in1'][1]), comb['in1'], label="Target Inputs (e.g., D or T)", label_pos=(2.5, comb['in1'][1] + 0.35))

    # Excitations from Combinational Logic to Available Flip-Flop
    draw_ortho(ax, comb['out1'], avail_ff['J'], label="Excitation J = f(Inputs, Q)", label_pos=(9.6, comb['out1'][1] + 0.35))
    draw_ortho(ax, comb['out2'], avail_ff['K'], label="Excitation K = f(Inputs, Q)", label_pos=(9.6, comb['out2'][1] - 0.35))

    # External Clock
    draw_ortho(ax, (0.8, avail_ff['CLK'][1]), avail_ff['CLK'], label="Clock Pulse (CLK)", label_pos=(3.0, avail_ff['CLK'][1] + 0.35))

    # Outputs Q and Q'
    draw_ortho(ax, avail_ff['Q'], (16.2, avail_ff['Q'][1]), label="Output Q", label_pos=(15.0, avail_ff['Q'][1] + 0.35))
    draw_ortho(ax, avail_ff['Q_bar'], (16.2, avail_ff['Q_bar'][1]), label=r"Output $\overline{Q}$", label_pos=(15.0, avail_ff['Q_bar'][1] - 0.35))

    # Feedback from Present State Q into Combinational Logic
    draw_dot(ax, 14.2, avail_ff['Q'][1])
    draw_path(ax, [(14.2, avail_ff['Q'][1]), (14.2, 2.5), (4.0, 2.5), (4.0, comb['in2'][1]), comb['in2']],
              color="#0891b2", lw=1.6, label="Present State Q Feedback", label_pos=(9.0, 2.2), label_color="#0891b2")

    # 4-step conversion recipe box
    recipe_txt = (
        "UNIVERSAL 4-STEP PROCEDURE:\n"
        "1. Write Target Truth Table (Target Inputs + Present State Q -> Next State Q+).\n"
        "2. Append Excitation Columns for Available Flip-Flop (e.g. J, K required to achieve Q -> Q+ transition).\n"
        "3. Derive minimal Boolean equations for J and K using K-Maps.\n"
        "4. Implement the combinational steering gates driving the available flip-flop!"
    )
    ax.text(8.5, 0.7, recipe_txt, ha='center', va='center', fontsize=7.5, color="#1e293b",
            bbox=dict(boxstyle='round,pad=0.3', fc='#f1f5f9', ec='#94a3b8'))

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_ff_conversion.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_ff_conversion.svg"))
    plt.close()
    print("Generated circuit_m3_ff_conversion")

def gen_m3_registers_comparison():
    """Module 3 - Section 5: Comparison of SIPO, PISO, PIPO and Johnson Counters"""
    # 1. SIPO Register
    fig, ax = plt.subplots(figsize=(15, 6.0), dpi=300)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    ax.text(9.0, 7.9, "4-Bit Serial-In Parallel-Out (SIPO) Shift Register", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(9.0, 7.4, "Serial loading (N=4 pulses) | All outputs available simultaneously in parallel", ha='center', fontsize=9.0, color="#64748b")

    ff3 = draw_flip_flop(ax, 2.5, 4.0, ff_type="D", name="FF 3 (MSB)")
    ff2 = draw_flip_flop(ax, 6.5, 4.0, ff_type="D", name="FF 2")
    ff1 = draw_flip_flop(ax, 10.5, 4.0, ff_type="D", name="FF 1")
    ff0 = draw_flip_flop(ax, 14.5, 4.0, ff_type="D", name="FF 0 (LSB)")

    # Serial In
    draw_ortho(ax, (0.5, ff3['D'][1]), ff3['D'], label="Serial In (Data)", label_pos=(1.4, ff3['D'][1] + 0.35))

    # Shift Connections
    draw_ortho(ax, ff3['Q'], ff2['D'])
    draw_dot(ax, 5.5, ff3['Q'][1])
    draw_ortho(ax, ff2['Q'], ff1['D'])
    draw_dot(ax, 9.5, ff2['Q'][1])
    draw_ortho(ax, ff1['Q'], ff0['D'])
    draw_dot(ax, 13.5, ff1['Q'][1])

    # Parallel Outputs tapped from each Q
    draw_path(ax, [(5.5, ff3['Q'][1]), (5.5, 6.5)], label=r"$Q_3 \text{ (MSB)}$", label_pos=(5.5, 6.8), label_color="#2563eb")
    draw_path(ax, [(9.5, ff2['Q'][1]), (9.5, 6.5)], label=r"$Q_2$", label_pos=(9.5, 6.8), label_color="#2563eb")
    draw_path(ax, [(13.5, ff1['Q'][1]), (13.5, 6.5)], label=r"$Q_1$", label_pos=(13.5, 6.8), label_color="#2563eb")
    draw_path(ax, [(ff0['Q'][0] + 0.6, ff0['Q'][1]), (ff0['Q'][0] + 0.6, 6.5)], label=r"$Q_0 \text{ (LSB)}$", label_pos=(ff0['Q'][0] + 0.6, 6.8), label_color="#2563eb")
    draw_ortho(ax, ff0['Q'], (ff0['Q'][0] + 0.6, ff0['Q'][1]))
    draw_dot(ax, ff0['Q'][0] + 0.6, ff0['Q'][1])

    # Common Clock Bus
    draw_path(ax, [(0.5, 1.6), (15.5, 1.6)], label="Common Clock Pulse (CLK)", label_pos=(1.8, 1.25))
    for f in [ff3, ff2, ff1, ff0]:
        draw_dot(ax, f['CLK'][0] - 0.5, 1.6)
        draw_path(ax, [(f['CLK'][0] - 0.5, 1.6), (f['CLK'][0] - 0.5, f['CLK'][1]), f['CLK']])

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_sipo_register.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_sipo_register.svg"))
    plt.close()
    print("Generated circuit_m3_sipo_register")

    # 2. PISO Register
    fig, ax = plt.subplots(figsize=(15, 6.5), dpi=300)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 9.0)
    ax.axis('off')

    ax.text(9.0, 8.4, r"4-Bit Parallel-In Serial-Out (PISO) Shift Register with 2:1 Steering MUX", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(9.0, 7.9, r"Shift / $\overline{\text{Load}}$ Control selects between Parallel Loading and Serial Shifting", ha='center', fontsize=9.0, color="#64748b")

    # Shift/Load Control Line at y=2.0
    draw_path(ax, [(0.5, 2.0), (16.5, 2.0)], label=r"Shift / $\overline{\text{Load}}$ Control Line", label_pos=(2.2, 1.65), label_color="#b45309")

    # Stages 3, 2, 1, 0
    # Stage 3 takes Parallel In X3 directly or through MUX
    ff3 = draw_flip_flop(ax, 2.8, 4.8, ff_type="D", name="FF 3")
    mux2 = draw_mux_2to1(ax, 5.8, 4.8, label="MUX 2")
    ff2 = draw_flip_flop(ax, 8.0, 4.8, ff_type="D", name="FF 2")
    mux1 = draw_mux_2to1(ax, 11.0, 4.8, label="MUX 1")
    ff1 = draw_flip_flop(ax, 13.2, 4.8, ff_type="D", name="FF 1")

    # Stage 3 Parallel In X3
    draw_ortho(ax, (1.0, ff3['D'][1]), ff3['D'], label=r"$X_3 \text{ (Parallel In)}$", label_pos=(1.6, ff3['D'][1] + 0.35))

    # MUX connections:
    # MUX 2: in0 = X2, in1 = Q3
    draw_ortho(ax, (4.8, mux2['in0'][1]), mux2['in0'], label=r"$X_2$", label_pos=(4.6, mux2['in0'][1] + 0.3))
    draw_ortho(ax, ff3['Q'], mux2['in1'], label=r"$Q_3$", label_pos=(5.3, mux2['in1'][1] - 0.3))
    draw_ortho(ax, mux2['out'], ff2['D'])

    # MUX 1: in0 = X1, in1 = Q2
    draw_ortho(ax, (10.0, mux1['in0'][1]), mux1['in0'], label=r"$X_1$", label_pos=(9.8, mux1['in0'][1] + 0.3))
    draw_ortho(ax, ff2['Q'], mux1['in1'], label=r"$Q_2$", label_pos=(10.5, mux1['in1'][1] - 0.3))
    draw_ortho(ax, mux1['out'], ff1['D'])

    # Serial Output from Stage 0
    draw_ortho(ax, ff1['Q'], (17.0, ff1['Q'][1]), label=r"Serial Out ($Q_0$ via cascade)", label_pos=(15.8, ff1['Q'][1] + 0.35), label_color="#dc2626")

    # Connect Shift/Load line to MUX select lines
    for m in [mux2, mux1]:
        draw_dot(ax, m['sel'][0], 2.0)
        draw_ortho(ax, (m['sel'][0], 2.0), m['sel'])

    # Common Clock Bus at y=0.8
    draw_path(ax, [(0.5, 0.8), (16.5, 0.8)], label="Common Clock Pulse (CLK)", label_pos=(2.0, 0.45))
    for f in [ff3, ff2, ff1]:
        draw_dot(ax, f['CLK'][0] - 0.4, 0.8)
        draw_path(ax, [(f['CLK'][0] - 0.4, 0.8), (f['CLK'][0] - 0.4, f['CLK'][1]), f['CLK']])

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_piso_register.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_piso_register.svg"))
    plt.close()
    print("Generated circuit_m3_piso_register")

    # 3. PIPO Register
    fig, ax = plt.subplots(figsize=(15, 6.0), dpi=300)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    ax.text(9.0, 7.9, "4-Bit Parallel-In Parallel-Out (PIPO) Register", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(9.0, 7.4, "Instant 1-clock load (N=1) and instant 0-clock read | Maximum Bandwidth", ha='center', fontsize=9.0, color="#64748b")

    ffs = []
    x_positions = [2.2, 6.2, 10.2, 14.2]
    for i, x in enumerate(x_positions):
        f = draw_flip_flop(ax, x, 4.0, ff_type="D", name=f"FF {3-i}")
        ffs.append(f)
        # Parallel In
        draw_ortho(ax, (x - 1.2, f['D'][1]), f['D'], label=f"$X_{3-i}$", label_pos=(x - 0.7, f['D'][1] + 0.35))
        # Parallel Out
        draw_ortho(ax, f['Q'], (x + 3.2, f['Q'][1]), label=f"$Q_{3-i}$", label_pos=(x + 2.8, f['Q'][1] + 0.35), label_color="#2563eb")

    # Common Clock Bus
    draw_path(ax, [(0.5, 1.6), (16.5, 1.6)], label="Common Clock Pulse (CLK)", label_pos=(1.8, 1.25))
    for f in ffs:
        draw_dot(ax, f['CLK'][0] - 0.4, 1.6)
        draw_path(ax, [(f['CLK'][0] - 0.4, 1.6), (f['CLK'][0] - 0.4, f['CLK'][1]), f['CLK']])

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_pipo_register.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_pipo_register.svg"))
    plt.close()
    print("Generated circuit_m3_pipo_register")

    # 4. Ring vs Johnson Counter Feedback
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5.5), dpi=300)
    for ax in (ax1, ax2):
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8.0)
        ax.axis('off')

    # Ring Counter
    ax1.text(7.0, 7.4, "4-Bit Ring Counter (MOD = N = 4)", ha='center', fontsize=12, fontweight='bold', color="#0f172a")
    ax1.text(7.0, 6.9, "Direct Normal Feedback: Q0 -> D3 | States: 1000 -> 0100 -> 0010 -> 0001", ha='center', fontsize=8.0, color="#64748b")
    r3 = draw_flip_flop(ax1, 1.2, 3.8, w=1.8, h=2.6, ff_type="D", name="FF 3")
    r2 = draw_flip_flop(ax1, 4.2, 3.8, w=1.8, h=2.6, ff_type="D", name="FF 2")
    r1 = draw_flip_flop(ax1, 7.2, 3.8, w=1.8, h=2.6, ff_type="D", name="FF 1")
    r0 = draw_flip_flop(ax1, 10.2, 3.8, w=1.8, h=2.6, ff_type="D", name="FF 0")
    draw_ortho(ax1, r3['Q'], r2['D']); draw_ortho(ax1, r2['Q'], r1['D']); draw_ortho(ax1, r1['Q'], r0['D'])
    # Feedback Q0 -> D3
    draw_dot(ax1, 12.4, r0['Q'][1])
    draw_path(ax1, [(12.4, r0['Q'][1]), (12.4, 6.2), (0.6, 6.2), (0.6, r3['D'][1]), r3['D']],
              color="#059669", lw=1.8, label=r"$\text{Direct Feedback } Q_0 \to D_3$", label_pos=(6.5, 6.5), label_color="#059669")

    # Johnson Counter
    ax2.text(7.0, 7.4, "4-Bit Johnson Counter (MOD = 2N = 8)", ha='center', fontsize=12, fontweight='bold', color="#0f172a")
    ax2.text(7.0, 6.9, r"Inverted Feedback: $\overline{Q_0} \to D_3$ | Self-starting, 8 decoded states", ha='center', fontsize=8.0, color="#64748b")
    j3 = draw_flip_flop(ax2, 1.2, 3.8, w=1.8, h=2.6, ff_type="D", name="FF 3")
    j2 = draw_flip_flop(ax2, 4.2, 3.8, w=1.8, h=2.6, ff_type="D", name="FF 2")
    j1 = draw_flip_flop(ax2, 7.2, 3.8, w=1.8, h=2.6, ff_type="D", name="FF 1")
    j0 = draw_flip_flop(ax2, 10.2, 3.8, w=1.8, h=2.6, ff_type="D", name="FF 0")
    draw_ortho(ax2, j3['Q'], j2['D']); draw_ortho(ax2, j2['Q'], j1['D']); draw_ortho(ax2, j1['Q'], j0['D'])
    # Feedback Q0_bar -> D3
    draw_dot(ax2, 12.4, j0['Q_bar'][1])
    draw_path(ax2, [(12.4, j0['Q_bar'][1]), (12.4, 6.2), (0.6, 6.2), (0.6, j3['D'][1]), j3['D']],
              color="#dc2626", lw=1.8, label=r"$\text{Inverted Feedback } \overline{Q_0} \to D_3$", label_pos=(6.5, 6.5), label_color="#dc2626")

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_ring_johnson_counters.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_ring_johnson_counters.svg"))
    plt.close()
    print("Generated circuit_m3_ring_johnson_counters")

def gen_m3_usr_stage():
    """Module 3 - Section 5F: Single Stage of Universal Shift Register (IC 74LS194)"""
    fig, ax = plt.subplots(figsize=(13, 7.5), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 11)
    ax.axis('off')

    ax.text(8.0, 10.4, "Single Stage i of Universal Shift Register (IC 74LS194)", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(8.0, 9.9, "Controlled by 4:1 Multiplexer with Mode Select Lines S1, S0", ha='center', fontsize=9.5, color="#64748b")

    # 4:1 MUX
    mux = draw_mux_4to1(ax, 4.5, 5.5, w=2.2, h=4.8, label="4:1 MUX\nStage i")

    # Flip Flop Stage i
    ff = draw_flip_flop(ax, 10.0, 5.5, w=2.4, h=3.6, ff_type="D", name=r"FF Stage $i$", clk_edge="pos")

    # Connect MUX out to D input of FF
    draw_ortho(ax, mux['out'], ff['D'], label=r"$D_i$", label_pos=(8.5, ff['D'][1] + 0.35))

    # MUX Inputs
    # 0: Hold (Qi)
    draw_ortho(ax, (1.0, mux['in0'][1]), mux['in0'], label=r"Input 0: $Q_i$ (Hold / No Change)", label_pos=(2.5, mux['in0'][1] + 0.35))
    # 1: Shift Right (Q_(i+1))
    draw_ortho(ax, (1.0, mux['in1'][1]), mux['in1'], label=r"Input 1: $Q_{i+1}$ (Shift Right)", label_pos=(2.5, mux['in1'][1] + 0.35))
    # 2: Shift Left (Q_(i-1))
    draw_ortho(ax, (1.0, mux['in2'][1]), mux['in2'], label=r"Input 2: $Q_{i-1}$ (Shift Left)", label_pos=(2.5, mux['in2'][1] - 0.35))
    # 3: Parallel Load (I_i)
    draw_ortho(ax, (1.0, mux['in3'][1]), mux['in3'], label=r"Input 3: $I_i$ (Parallel Load)", label_pos=(2.5, mux['in3'][1] - 0.35))

    # Mode Select Lines S1 and S0
    draw_path(ax, [(mux['sel0'][0], 1.8), mux['sel0']], label=r"$S_1$", label_pos=(mux['sel0'][0] - 0.3, 2.3))
    draw_path(ax, [(mux['sel1'][0], 1.8), mux['sel1']], label=r"$S_0$", label_pos=(mux['sel1'][0] + 0.3, 2.3))
    ax.text((mux['sel0'][0] + mux['sel1'][0])/2, 1.4, "Mode Select Lines", ha='center', fontsize=8.5, fontweight='bold', color="#15803d")

    # Output Q_i
    draw_ortho(ax, ff['Q'], (14.5, ff['Q'][1]), label=r"$Q_i \text{ (Stage Output)}$", label_pos=(13.8, ff['Q'][1] + 0.35))

    # Hold Feedback from Qi to Input 0
    draw_dot(ax, 13.0, ff['Q'][1])
    draw_path(ax, [(13.0, ff['Q'][1]), (13.0, 8.8), (3.8, 8.8), (3.8, mux['in0'][1]), mux['in0']],
              color="#0284c7", lw=1.5, label="Hold Feedback", label_pos=(8.5, 9.1), label_color="#0284c7")

    # Clock line
    draw_ortho(ax, (7.5, ff['CLK'][1]), ff['CLK'], label="Common CLK", label_pos=(8.5, ff['CLK'][1] + 0.35))

    # Truth Table Summary Box
    tbl_txt = (
        "74LS194 MODE FUNCTION TABLE:\n"
        "• S1=0, S0=0 -> Hold: Di = Qi (retains current bit)\n"
        "• S1=0, S0=1 -> Shift Right: Di = Q(i+1) (takes left bit; Stage 3 takes Serial In SR)\n"
        "• S1=1, S0=0 -> Shift Left: Di = Q(i-1) (takes right bit; Stage 0 takes Serial In SL)\n"
        "• S1=1, S0=1 -> Parallel Load: Di = Ii (loads external 4-bit data parallel in 1 clock pulse)"
    )
    ax.text(8.0, 0.6, tbl_txt, ha='center', va='center', fontsize=7.5, color="#1e293b",
            bbox=dict(boxstyle='round,pad=0.35', fc='#f8fafc', ec='#cbd5e1'))

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_usr_stage.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_m3_usr_stage.svg"))
    plt.close()
    print("Generated circuit_m3_usr_stage")


# =====================================================================
# MODULE 4 CIRCUITS
# =====================================================================

def gen_m4_asynch_vs_synch():
    """Module 4 - Section 1: Asynchronous (Ripple) vs Synchronous Counter Architecture"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8.0), dpi=300)
    for ax in (ax1, ax2):
        ax.set_xlim(0, 16)
        ax.set_ylim(0, 6.5)
        ax.axis('off')

    # Top: Asynchronous Ripple Counter
    ax1.text(8.0, 5.8, "Asynchronous (Ripple) Counter: Domino Clocking Architecture", ha='center', fontsize=12, fontweight='bold', color="#b45309")
    ax1.text(8.0, 5.3, r"Clock cascades from stage to stage | Propagation delay accumulates: $T_{total} = n \times t_{pd}$ (Slow)", ha='center', fontsize=8.5, color="#64748b")

    a0 = draw_flip_flop(ax1, 2.8, 3.0, w=2.0, h=2.5, ff_type="T", name="FF 0 (LSB)", clk_edge="neg")
    a1 = draw_flip_flop(ax1, 7.2, 3.0, w=2.0, h=2.5, ff_type="T", name="FF 1", clk_edge="neg")
    a2 = draw_flip_flop(ax1, 11.6, 3.0, w=2.0, h=2.5, ff_type="T", name="FF 2 (MSB)", clk_edge="neg")

    # External Clock to FF0 only
    draw_ortho(ax1, (0.8, a0['CLK'][1]), a0['CLK'], label="Ext CLK", label_pos=(1.6, a0['CLK'][1] + 0.35))

    # Domino Ripple: Q0 clocks FF1, Q1 clocks FF2
    draw_ortho(ax1, a0['Q'], a1['CLK'], label=r"$Q_0 \to \text{CLK}_1$", label_pos=(5.8, a0['Q'][1] + 0.35), label_color="#b45309")
    draw_ortho(ax1, a1['Q'], a2['CLK'], label=r"$Q_1 \to \text{CLK}_2$", label_pos=(10.2, a1['Q'][1] + 0.35), label_color="#b45309")
    draw_ortho(ax1, a2['Q'], (14.8, a2['Q'][1]), label=r"$Q_2 \text{ (MSB)}$", label_pos=(14.2, a2['Q'][1] + 0.35))

    # All T tied to 1
    for f in [a0, a1, a2]:
        draw_ortho(ax1, (f['T'][0] - 0.6, f['T'][1]), f['T'], label="1", label_pos=(f['T'][0] - 0.3, f['T'][1] + 0.25))

    # Bottom: Synchronous Counter
    ax2.text(8.0, 5.8, "Synchronous Counter: Unified Master Clock Architecture", ha='center', fontsize=12, fontweight='bold', color="#15803d")
    ax2.text(8.0, 5.3, r"All flip-flops trigger simultaneously on common clock | Delay is only 1 stage: $T_{total} = t_{pd}$ (Blazing Fast)", ha='center', fontsize=8.5, color="#64748b")

    s0 = draw_flip_flop(ax2, 2.8, 3.0, w=2.0, h=2.5, ff_type="T", name="FF 0 (LSB)", clk_edge="pos")
    s1 = draw_flip_flop(ax2, 7.2, 3.0, w=2.0, h=2.5, ff_type="T", name="FF 1", clk_edge="pos")
    s2 = draw_flip_flop(ax2, 11.6, 3.0, w=2.0, h=2.5, ff_type="T", name="FF 2 (MSB)", clk_edge="pos")

    # Common Clock Bus
    draw_path(ax2, [(0.8, 0.8), (12.0, 0.8)], label="Unified Master Clock (CLK)", label_pos=(2.0, 0.45), label_color="#15803d")
    for f in [s0, s1, s2]:
        draw_dot(ax2, f['CLK'][0] - 0.4, 0.8)
        draw_path(ax2, [(f['CLK'][0] - 0.4, 0.8), (f['CLK'][0] - 0.4, f['CLK'][1]), f['CLK']])

    # Outputs
    draw_ortho(ax2, s0['Q'], (s0['Q'][0] + 0.8, s0['Q'][1]), label=r"$Q_0$", label_pos=(s0['Q'][0] + 0.6, s0['Q'][1] + 0.35))
    draw_ortho(ax2, s1['Q'], (s1['Q'][0] + 0.8, s1['Q'][1]), label=r"$Q_1$", label_pos=(s1['Q'][0] + 0.6, s1['Q'][1] + 0.35))
    draw_ortho(ax2, s2['Q'], (14.8, s2['Q'][1]), label=r"$Q_2 \text{ (MSB)}$", label_pos=(14.2, s2['Q'][1] + 0.35))

    # T logic: T0=1, T1=Q0, T2=Q0*Q1
    draw_ortho(ax2, (s0['T'][0] - 0.6, s0['T'][1]), s0['T'], label="1", label_pos=(s0['T'][0] - 0.3, s0['T'][1] + 0.25))
    draw_ortho(ax2, (s1['T'][0] - 0.6, s1['T'][1]), s1['T'], label=r"$Q_0$", label_pos=(s1['T'][0] - 0.4, s1['T'][1] + 0.25))
    and_s2 = draw_and(ax2, 10.0, 3.8, w=1.2, h=1.0, label="AND")
    draw_ortho(ax2, and_s2['out'], s2['T'], label=r"$Q_0 Q_1$", label_pos=(11.1, s2['T'][1] + 0.3))

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_m4_asynch_vs_synch.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_m4_asynch_vs_synch.svg"))
    plt.close()
    print("Generated circuit_m4_asynch_vs_synch")

def gen_m4_ripple_up_down():
    """Module 4 - Section 2A & 2B: 3-Bit Asynchronous UP and DOWN Ripple Counters"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8.5), dpi=300)
    for ax in (ax1, ax2):
        ax.set_xlim(0, 16)
        ax.set_ylim(0, 7.0)
        ax.axis('off')

    # Part A: UP Counter (Q clocks next stage with negative-edge FFs)
    ax1.text(8.0, 6.4, "3-Bit Asynchronous UP Counter (Negative-Edge Triggered T FFs)", ha='center', fontsize=12, fontweight='bold', color="#0f172a")
    ax1.text(8.0, 5.9, r"Rule: Neg-edge + Normal Output $Q \rightarrow$ UP Counter ($0 \to 1 \to 2 \dots \to 7 \to 0$)", ha='center', fontsize=8.5, color="#64748b")

    u0 = draw_flip_flop(ax1, 2.8, 3.4, w=2.0, h=2.5, ff_type="T", name="FF 0 (LSB)", clk_edge="neg")
    u1 = draw_flip_flop(ax1, 7.2, 3.4, w=2.0, h=2.5, ff_type="T", name="FF 1", clk_edge="neg")
    u2 = draw_flip_flop(ax1, 11.6, 3.4, w=2.0, h=2.5, ff_type="T", name="FF 2 (MSB)", clk_edge="neg")

    draw_ortho(ax1, (0.8, u0['CLK'][1]), u0['CLK'], label="Clock In", label_pos=(1.6, u0['CLK'][1] + 0.35))
    draw_ortho(ax1, u0['Q'], u1['CLK'], label=r"$Q_0$", label_pos=(5.8, u0['Q'][1] + 0.35))
    draw_dot(ax1, 5.8, u0['Q'][1]); draw_path(ax1, [(5.8, u0['Q'][1]), (5.8, 5.2)], label=r"$Q_0 \text{ Out}$", label_pos=(5.8, 5.4), label_color="#2563eb")

    draw_ortho(ax1, u1['Q'], u2['CLK'], label=r"$Q_1$", label_pos=(10.2, u1['Q'][1] + 0.35))
    draw_dot(ax1, 10.2, u1['Q'][1]); draw_path(ax1, [(10.2, u1['Q'][1]), (10.2, 5.2)], label=r"$Q_1 \text{ Out}$", label_pos=(10.2, 5.4), label_color="#2563eb")

    draw_ortho(ax1, u2['Q'], (14.5, u2['Q'][1]), label=r"$Q_2 \text{ Out}$", label_pos=(14.0, u2['Q'][1] + 0.35), label_color="#2563eb")

    # VCC to all T inputs
    draw_path(ax1, [(1.5, 1.2), (12.0, 1.2)], label="Logic 1 (VCC)", label_pos=(1.8, 0.85), label_color="#15803d")
    for f in [u0, u1, u2]:
        draw_dot(ax1, f['T'][0] - 0.4, 1.2)
        draw_path(ax1, [(f['T'][0] - 0.4, 1.2), (f['T'][0] - 0.4, f['T'][1]), f['T']])

    # Part B: DOWN Counter (Q' clocks next stage with negative-edge FFs)
    ax2.text(8.0, 6.4, "3-Bit Asynchronous DOWN Counter (Negative-Edge Triggered T FFs)", ha='center', fontsize=12, fontweight='bold', color="#0f172a")
    ax2.text(8.0, 5.9, r"Rule: Neg-edge + Inverted Output $\overline{Q} \rightarrow$ DOWN Counter ($7 \to 6 \to 5 \dots \to 0 \to 7$)", ha='center', fontsize=8.5, color="#64748b")

    d0 = draw_flip_flop(ax2, 2.8, 3.4, w=2.0, h=2.5, ff_type="T", name="FF 0 (LSB)", clk_edge="neg")
    d1 = draw_flip_flop(ax2, 7.2, 3.4, w=2.0, h=2.5, ff_type="T", name="FF 1", clk_edge="neg")
    d2 = draw_flip_flop(ax2, 11.6, 3.4, w=2.0, h=2.5, ff_type="T", name="FF 2 (MSB)", clk_edge="neg")

    draw_ortho(ax2, (0.8, d0['CLK'][1]), d0['CLK'], label="Clock In", label_pos=(1.6, d0['CLK'][1] + 0.35))
    draw_ortho(ax2, d0['Q_bar'], d1['CLK'], label=r"$\overline{Q_0}$", label_pos=(5.8, d0['Q_bar'][1] - 0.35))
    draw_ortho(ax2, d0['Q'], (5.8, d0['Q'][1]), label=r"$Q_0 \text{ Out}$", label_pos=(5.8, d0['Q'][1] + 0.35), label_color="#2563eb")

    draw_ortho(ax2, d1['Q_bar'], d2['CLK'], label=r"$\overline{Q_1}$", label_pos=(10.2, d1['Q_bar'][1] - 0.35))
    draw_ortho(ax2, d1['Q'], (10.2, d1['Q'][1]), label=r"$Q_1 \text{ Out}$", label_pos=(10.2, d1['Q'][1] + 0.35), label_color="#2563eb")

    draw_ortho(ax2, d2['Q'], (14.5, d2['Q'][1]), label=r"$Q_2 \text{ Out}$", label_pos=(14.0, d2['Q'][1] + 0.35), label_color="#2563eb")

    # VCC to all T inputs
    draw_path(ax2, [(1.5, 1.2), (12.0, 1.2)], label="Logic 1 (VCC)", label_pos=(1.8, 0.85), label_color="#15803d")
    for f in [d0, d1, d2]:
        draw_dot(ax2, f['T'][0] - 0.4, 1.2)
        draw_path(ax2, [(f['T'][0] - 0.4, 1.2), (f['T'][0] - 0.4, f['T'][1]), f['T']])

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_m4_ripple_up_down.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_m4_ripple_up_down.svg"))
    plt.close()
    print("Generated circuit_m4_ripple_up_down")

def gen_m4_mod6_ripple():
    """Module 4 - Section 2C: Mod-6 Truncated Asynchronous Counter with Active-Low NAND Reset"""
    fig, ax = plt.subplots(figsize=(14, 7.0), dpi=300)
    ax.set_xlim(0, 17)
    ax.set_ylim(0, 9.5)
    ax.axis('off')

    ax.text(8.5, 9.0, "Mod-6 Truncated Asynchronous Ripple Counter with NAND Reset", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(8.5, 8.5, r"Counts $0 \to 1 \to 2 \to 3 \to 4 \to 5$ | Resets on state $6$ ($110_2 \rightarrow \overline{\text{CLR}} = \overline{Q_2 \cdot Q_1}$)", ha='center', fontsize=9.0, color="#64748b")

    # 3 Flip-Flops with CLEAR inputs
    ff0 = draw_flip_flop(ax, 3.0, 4.2, w=2.2, h=2.8, ff_type="T", name="FF 0 (LSB)", clk_edge="neg", has_clr=True)
    ff1 = draw_flip_flop(ax, 7.5, 4.2, w=2.2, h=2.8, ff_type="T", name="FF 1", clk_edge="neg", has_clr=True)
    ff2 = draw_flip_flop(ax, 12.0, 4.2, w=2.2, h=2.8, ff_type="T", name="FF 2 (MSB)", clk_edge="neg", has_clr=True)

    # External Clock
    draw_ortho(ax, (1.0, ff0['CLK'][1]), ff0['CLK'], label="Clock In", label_pos=(1.8, ff0['CLK'][1] + 0.35))

    # Ripple clocking (Q0 -> CLK1, Q1 -> CLK2)
    draw_ortho(ax, ff0['Q'], ff1['CLK'])
    draw_dot(ax, 6.0, ff0['Q'][1])
    draw_path(ax, [(6.0, ff0['Q'][1]), (6.0, 6.5)], label=r"$Q_0$", label_pos=(6.0, 6.8), label_color="#2563eb")

    draw_ortho(ax, ff1['Q'], ff2['CLK'])
    draw_dot(ax, 10.5, ff1['Q'][1])
    draw_path(ax, [(10.5, ff1['Q'][1]), (10.5, 6.5)], label=r"$Q_1$", label_pos=(10.5, 6.8), label_color="#2563eb")

    draw_ortho(ax, ff2['Q'], (15.5, ff2['Q'][1]), label=r"$Q_2$", label_pos=(15.0, ff2['Q'][1] + 0.35), label_color="#2563eb")

    # Reset NAND Gate detecting Q2=1 and Q1=1
    nand_rst = draw_nand(ax, 7.8, 7.5, w=1.6, h=1.3, label="NAND\nReset")

    # Connect Q1 to NAND in1
    draw_dot(ax, 10.5, 6.5)
    draw_path(ax, [(10.5, 6.5), (10.5, nand_rst['in2'][1]), nand_rst['in2']])

    # Connect Q2 to NAND in2
    draw_dot(ax, 14.5, ff2['Q'][1])
    draw_path(ax, [(14.5, ff2['Q'][1]), (14.5, nand_rst['in1'][1]), nand_rst['in1']])

    # NAND Output connects to active-low CLR pins of all flip-flops
    rst_out = nand_rst['out']
    draw_path(ax, [rst_out, (16.2, rst_out[1]), (16.2, 1.8), (4.1, 1.8)],
              color="#dc2626", lw=2.0, label=r"$\text{Active-Low Reset Pulse } \overline{\text{CLR}} = \overline{Q_2 \cdot Q_1}$",
              label_pos=(9.5, 1.5), label_color="#dc2626")

    for f in [ff0, ff1, ff2]:
        draw_dot(ax, f['CLR'][0], 1.8)
        draw_ortho(ax, (f['CLR'][0], 1.8), f['CLR'], color="#dc2626")

    # T inputs tied to VCC
    for f in [ff0, ff1, ff2]:
        draw_ortho(ax, (f['T'][0] - 0.6, f['T'][1]), f['T'], label="1", label_pos=(f['T'][0] - 0.3, f['T'][1] + 0.25))

    # Explanation of Transient Glitch
    glitch_txt = (
        "RESET TIMING & TRANSIENT GLITCH ANALYSIS:\n"
        "• State 6 (110_2) is an UNSTABLE TRANSIENT STATE. It exists for only ~15 ns (gate propagation delay).\n"
        "• The instant Q2=1 and Q1=1 become HIGH, the NAND gate output drops to 0, asserting CLR and forcing all FFs to 000_2.\n"
        "• Modulus = 6 (Traverses 6 stable states: 0, 1, 2, 3, 4, 5)."
    )
    ax.text(8.5, 0.6, glitch_txt, ha='center', va='center', fontsize=7.5, color="#991b1b",
            bbox=dict(boxstyle='round,pad=0.3', fc='#fef2f2', ec='#fca5a5'))

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_m4_mod6_ripple.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_m4_mod6_ripple.svg"))
    plt.close()
    print("Generated circuit_m4_mod6_ripple")

def gen_m4_sync_up_counter():
    """Module 4 - Section 3: 3-Bit Synchronous Binary UP Counter Schematic"""
    fig, ax = plt.subplots(figsize=(14, 7.0), dpi=300)
    ax.set_xlim(0, 17)
    ax.set_ylim(0, 9.5)
    ax.axis('off')

    ax.text(8.5, 9.0, "3-Bit Synchronous Binary UP Counter Schematic", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(8.5, 8.5, r"Common Clock Pulse | $T_0 = 1, \quad T_1 = Q_0, \quad T_2 = Q_0 \cdot Q_1$ (Carry Lookahead)", ha='center', fontsize=9.0, color="#64748b")

    ff0 = draw_flip_flop(ax, 3.0, 4.5, w=2.2, h=2.8, ff_type="T", name="FF 0 (LSB)", clk_edge="pos")
    ff1 = draw_flip_flop(ax, 7.5, 4.5, w=2.2, h=2.8, ff_type="T", name="FF 1", clk_edge="pos")
    ff2 = draw_flip_flop(ax, 12.0, 4.5, w=2.2, h=2.8, ff_type="T", name="FF 2 (MSB)", clk_edge="pos")

    # Common Clock Bus at y=1.2
    draw_path(ax, [(1.0, 1.2), (13.0, 1.2)], label="Unified Master Clock (CLK)", label_pos=(2.2, 0.85), label_color="#15803d")
    for f in [ff0, ff1, ff2]:
        draw_dot(ax, f['CLK'][0] - 0.4, 1.2)
        draw_path(ax, [(f['CLK'][0] - 0.4, 1.2), (f['CLK'][0] - 0.4, f['CLK'][1]), f['CLK']])

    # Output lines Q0, Q1, Q2
    draw_ortho(ax, ff0['Q'], (6.5, ff0['Q'][1]), label=r"$Q_0$", label_pos=(6.0, ff0['Q'][1] + 0.35), label_color="#2563eb")
    draw_ortho(ax, ff1['Q'], (11.0, ff1['Q'][1]), label=r"$Q_1$", label_pos=(10.5, ff1['Q'][1] + 0.35), label_color="#2563eb")
    draw_ortho(ax, ff2['Q'], (15.5, ff2['Q'][1]), label=r"$Q_2 \text{ (MSB)}$", label_pos=(14.8, ff2['Q'][1] + 0.35), label_color="#2563eb")

    # T0 tied to Logic 1
    draw_ortho(ax, (1.2, ff0['T'][1]), ff0['T'], label="Logic 1 (Always Toggles)", label_pos=(2.0, ff0['T'][1] + 0.35))

    # T1 = Q0
    draw_dot(ax, 5.8, ff0['Q'][1])
    draw_path(ax, [(5.8, ff0['Q'][1]), (5.8, ff1['T'][1]), ff1['T']], label=r"$T_1 = Q_0$", label_pos=(6.6, ff1['T'][1] + 0.35))

    # T2 = Q0 * Q1 via 2-input AND gate
    and1 = draw_and(ax, 9.8, 5.8, w=1.4, h=1.2, label="AND 1")
    # Connect Q0 into AND 1 in1
    draw_dot(ax, 5.8, 7.5)
    draw_path(ax, [(5.8, ff0['Q'][1]), (5.8, 7.5), (9.2, 7.5), (9.2, and1['in1'][1]), and1['in1']])
    # Connect Q1 into AND 1 in2
    draw_dot(ax, 10.2, ff1['Q'][1])
    draw_path(ax, [(10.2, ff1['Q'][1]), (10.2, and1['in2'][1]), and1['in2']])
    # Connect AND 1 out to T2
    draw_ortho(ax, and1['out'], ff2['T'], label=r"$T_2 = Q_0 \cdot Q_1$", label_pos=(11.5, ff2['T'][1] + 0.35))

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_m4_sync_up_counter.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_m4_sync_up_counter.svg"))
    plt.close()
    print("Generated circuit_m4_sync_up_counter")

def gen_m4_up_down_steering():
    """Module 4 - Section 5: Synchronous UP/DOWN Counter Mode Steering Logic"""
    fig, ax = plt.subplots(figsize=(13, 7.0), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9.5)
    ax.axis('off')

    ax.text(8.0, 9.0, "Synchronous UP / DOWN Counter Mode Steering Logic", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(8.0, 8.5, r"Steering equation for stage $i$: $T_i = M \cdot Q_{i-1} + \overline{M} \cdot \overline{Q_{i-1}}$ (Mode $M=1 \rightarrow \text{UP}, M=0 \rightarrow \text{DOWN}$)", ha='center', fontsize=9.0, color="#64748b")

    # Mode Inverter
    inv_m = draw_not(ax, 3.5, 4.0, w=1.2, h=0.8, label="NOT")

    # Mode Control Input M at y=6.5
    draw_ortho(ax, (0.8, 6.5), (2.5, 6.5), label="Mode Control (M)", label_pos=(1.6, 6.85), label_color="#15803d")
    draw_dot(ax, 2.5, 6.5)
    draw_path(ax, [(2.5, 6.5), (2.5, inv_m['in'][1]), inv_m['in']])

    # AND Gate 1: M * Q_(i-1) (for UP counting)
    and_up = draw_and(ax, 6.5, 6.8, w=1.8, h=1.4, label="AND 1\n(UP Mode)")
    # M to in1
    draw_ortho(ax, (2.5, 6.5), (2.5, and_up['in1'][1]))
    draw_ortho(ax, (2.5, and_up['in1'][1]), and_up['in1'], label="M", label_pos=(4.5, and_up['in1'][1] + 0.3))
    # Q_(i-1) to in2
    draw_ortho(ax, (0.8, and_up['in2'][1]), and_up['in2'], label=r"$Q_{i-1} \text{ (Normal)}$", label_pos=(1.8, and_up['in2'][1] + 0.3))

    # AND Gate 2: M' * Q'_(i-1) (for DOWN counting)
    and_dn = draw_and(ax, 6.5, 3.2, w=1.8, h=1.4, label="AND 2\n(DOWN Mode)")
    # M' from inverter to in1
    draw_ortho(ax, inv_m['out'], and_dn['in1'], label=r"$\overline{M}$", label_pos=(5.5, and_dn['in1'][1] + 0.3))
    # Q'_(i-1) to in2
    draw_ortho(ax, (0.8, and_dn['in2'][1]), and_dn['in2'], label=r"$\overline{Q_{i-1}} \text{ (Inverted)}$", label_pos=(1.8, and_dn['in2'][1] - 0.3))

    # OR Gate combining UP and DOWN steering
    or_comb = draw_or(ax, 10.5, 5.0, w=1.8, h=1.5, label="OR\nCombine")
    draw_ortho(ax, and_up['out'], or_comb['in1'], x_break=9.8)
    draw_ortho(ax, and_dn['out'], or_comb['in2'], x_break=9.8)

    # Output to Stage i T input
    draw_ortho(ax, or_comb['out'], (14.5, or_comb['out'][1]),
               label=r"$T_i = M \cdot Q_{i-1} + \overline{M} \cdot \overline{Q_{i-1}}$",
               label_pos=(13.2, or_comb['out'][1] + 0.4), label_color="#dc2626")

    # Mode description box
    mode_desc = (
        "OPERATING PRINCIPLE:\n"
        "• UP Counting (M = 1): AND 1 is enabled, passing Q_(i-1). AND 2 is disabled (output 0). Counter counts UP.\n"
        "• DOWN Counting (M = 0): Inverter enables AND 2, passing Q'_(i-1). AND 1 is disabled. Counter counts DOWN."
    )
    ax.text(8.0, 1.0, mode_desc, ha='center', va='center', fontsize=8.0, color="#1e293b",
            bbox=dict(boxstyle='round,pad=0.35', fc='#f8fafc', ec='#cbd5e1'))

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_m4_up_down_steering.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_m4_up_down_steering.svg"))
    plt.close()
    print("Generated circuit_m4_up_down_steering")

def gen_m4_fsm_mealy_moore():
    """Module 4 - Section 4: Architectural Comparison of Mealy vs Moore Sequential Machines"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8.5), dpi=300)
    for ax in (ax1, ax2):
        ax.set_xlim(0, 17)
        ax.set_ylim(0, 7.0)
        ax.axis('off')

    # Top: Moore Machine Architecture
    ax1.text(8.5, 6.4, "Moore Machine Architecture: Output Depends ONLY on Present State", ha='center', fontsize=12, fontweight='bold', color="#1d4ed8")
    ax1.text(8.5, 5.9, r"Output equation: $Y = g(Q)$ | Glitch-free, safe outputs, updated synchronously with clock", ha='center', fontsize=8.5, color="#64748b")

    moore_ns = draw_box(ax1, 2.0, 3.5, w=3.0, h=2.5, title="NEXT STATE\nLOGIC", subtitle="Combinational\nGates", color="#eff6ff", border="#3b82f6")
    moore_mem = draw_box(ax1, 6.8, 3.5, w=3.0, h=2.5, title="STATE MEMORY", subtitle="Clocked Flip-Flops\n(Present State Q)", color="#f8fafc", border="#1e293b")
    moore_out = draw_box(ax1, 11.6, 3.5, w=3.0, h=2.5, title="OUTPUT\nLOGIC", subtitle="Combinational\nY = g(Q)", color="#fdf4ff", border="#a855f7")

    # Inputs to Next State
    draw_ortho(ax1, (0.5, moore_ns['in1'][1]), moore_ns['in1'], label="Input x", label_pos=(1.2, moore_ns['in1'][1] + 0.35))
    # Next State to Memory
    draw_ortho(ax1, moore_ns['out1'], moore_mem['in1'], label=r"$Q^+ \text{ (Next State)}$", label_pos=(5.3, moore_ns['out1'][1] + 0.35))
    # Memory to Output Logic
    draw_ortho(ax1, moore_mem['out1'], moore_out['in1'], label=r"$Q \text{ (State)}$", label_pos=(10.2, moore_mem['out1'][1] + 0.35))
    # Output Logic to Y
    draw_ortho(ax1, moore_out['out1'], (16.0, moore_out['out1'][1]), label=r"Output $Y = g(Q)$", label_pos=(15.0, moore_out['out1'][1] + 0.35), label_color="#7e22ce")
    # State Feedback
    draw_dot(ax1, 10.2, moore_mem['out1'][1])
    draw_path(ax1, [(10.2, moore_mem['out1'][1]), (10.2, 1.2), (1.2, 1.2), (1.2, moore_ns['in2'][1]), moore_ns['in2']],
              color="#0284c7", lw=1.5, label="Present State Feedback (Q)", label_pos=(5.5, 0.9), label_color="#0284c7")

    # Bottom: Mealy Machine Architecture
    ax2.text(8.5, 6.4, "Mealy Machine Architecture: Output Depends on BOTH State AND Input", ha='center', fontsize=12, fontweight='bold', color="#b45309")
    ax2.text(8.5, 5.9, r"Output equation: $Y = g(Q, x)$ | Reacts immediately in same cycle, but prone to input glitches", ha='center', fontsize=8.5, color="#64748b")

    mealy_ns = draw_box(ax2, 2.0, 3.5, w=3.0, h=2.5, title="NEXT STATE\nLOGIC", subtitle="Combinational\nGates", color="#fefce8", border="#eab308")
    mealy_mem = draw_box(ax2, 6.8, 3.5, w=3.0, h=2.5, title="STATE MEMORY", subtitle="Clocked Flip-Flops\n(Present State Q)", color="#f8fafc", border="#1e293b")
    mealy_out = draw_box(ax2, 11.6, 3.5, w=3.0, h=2.5, title="OUTPUT\nLOGIC", subtitle="Combinational\nY = g(Q, x)", color="#fef2f2", border="#ef4444")

    # Inputs x enters BOTH Next State and Output Logic!
    draw_ortho(ax2, (0.5, mealy_ns['in1'][1]), mealy_ns['in1'], label="Input x", label_pos=(1.2, mealy_ns['in1'][1] + 0.35))
    draw_dot(ax2, 1.2, mealy_ns['in1'][1])
    # Direct feedthrough of x to Output Logic (Key Mealy trait!)
    draw_path(ax2, [(1.2, mealy_ns['in1'][1]), (1.2, 5.4), (11.0, 5.4), (11.0, mealy_out['in1'][1]), mealy_out['in1']],
              color="#b45309", lw=1.8, label="Direct Input Feedthrough (x)", label_pos=(6.5, 5.7), label_color="#b45309")

    # Next State to Memory
    draw_ortho(ax2, mealy_ns['out1'], mealy_mem['in1'], label=r"$Q^+ \text{ (Next State)}$", label_pos=(5.3, mealy_ns['out1'][1] + 0.35))
    # Memory to Output Logic
    draw_ortho(ax2, mealy_mem['out2'], mealy_out['in2'], label=r"$Q \text{ (State)}$", label_pos=(10.2, mealy_mem['out2'][1] + 0.35))
    # Output Logic to Y
    draw_ortho(ax2, mealy_out['right'], (16.0, mealy_out['right'][1]), label=r"Output $Y = g(Q, x)$", label_pos=(14.8, mealy_out['right'][1] + 0.35), label_color="#b91c1c")
    # State Feedback
    draw_dot(ax2, 10.2, mealy_mem['out2'][1])
    draw_path(ax2, [(10.2, mealy_mem['out2'][1]), (10.2, 1.2), (1.5, 1.2), (1.5, mealy_ns['in2'][1]), mealy_ns['in2']],
              color="#0284c7", lw=1.5, label="Present State Feedback (Q)", label_pos=(5.5, 0.9), label_color="#0284c7")

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_m4_fsm_mealy_moore.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_m4_fsm_mealy_moore.svg"))
    plt.close()
    print("Generated circuit_m4_fsm_mealy_moore")

if __name__ == "__main__":
    print("RENDERING ALL MODULE 3 & MODULE 4 SCHEMATICS...")
    # Module 3
    gen_m3_jk_ff()
    gen_m3_d_and_t_ff()
    gen_m3_master_slave_jk()
    gen_m3_ff_conversion()
    gen_m3_registers_comparison()
    gen_m3_usr_stage()

    # Module 4
    gen_m4_asynch_vs_synch()
    gen_m4_ripple_up_down()
    gen_m4_mod6_ripple()
    gen_m4_sync_up_counter()
    gen_m4_up_down_steering()
    gen_m4_fsm_mealy_moore()
    print("ALL MODULE CIRCUITS RENDERED SUCCESSFULLY WITH 300 DPI AND VECTOR SVG!")
