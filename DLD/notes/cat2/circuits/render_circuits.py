"""
Production-grade IEEE standard logic gate schematic renderer for DLD CAT-2.
Renders razor-sharp ANSI/IEEE gates, orthogonal wire routing, pin-accurate connections,
and full truth/timing summaries for Assignment 4 and Assignment 5.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

OUT_DIR = r"c:\Users\ankit\Fall2627\DLD\notes\cat2\circuits"
os.makedirs(OUT_DIR, exist_ok=True)

# ----------------- ROUTING & WIRE HELPERS -----------------

def draw_ortho(ax, p1, p2, x_break=None, y_break=None, color="#1e293b", lw=2.0, label=None, label_pos=None, label_color="#0f172a", fontsize=8.5):
    """Draws strictly orthogonal (horizontal & vertical) wires between p1 and p2"""
    x1, y1 = p1
    x2, y2 = p2
    if abs(y1 - y2) < 1e-4:
        pts = [(x1, y1), (x2, y2)]
    elif abs(x1 - x2) < 1e-4:
        pts = [(x1, y1), (x2, y2)]
    elif x_break is not None:
        pts = [(x1, y1), (x_break, y1), (x_break, y2), (x2, y2)]
    elif y_break is not None:
        pts = [(x1, y1), (x1, y_break), (x2, y_break), (x2, y2)]
    else:
        xm = (x1 + x2) / 2.0
        pts = [(x1, y1), (xm, y1), (xm, y2), (x2, y2)]

    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    ax.plot(xs, ys, color=color, lw=lw, solid_capstyle='round', zorder=2)

    if label and label_pos:
        ax.text(label_pos[0], label_pos[1], label, color=label_color, fontsize=fontsize, fontweight='bold',
                ha='center', va='center', bbox=dict(boxstyle='square,pad=0.15', fc='white', ec='none', alpha=0.9), zorder=6)

def draw_path(ax, pts, color="#1e293b", lw=2.0, label=None, label_pos=None, label_color="#0f172a", fontsize=8.5):
    """Draws multi-segment orthogonal wire path"""
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    ax.plot(xs, ys, color=color, lw=lw, solid_capstyle='round', zorder=2)
    if label and label_pos:
        ax.text(label_pos[0], label_pos[1], label, color=label_color, fontsize=fontsize, fontweight='bold',
                ha='center', va='center', bbox=dict(boxstyle='square,pad=0.15', fc='white', ec='none', alpha=0.9), zorder=6)

def draw_dot(ax, x, y, color="#1e293b", r=0.09):
    circle = patches.Circle((x, y), r, facecolor=color, edgecolor=color, zorder=5)
    ax.add_patch(circle)

# ----------------- ANSI/IEEE GATE PRIMITIVES -----------------

def draw_and(ax, x, y, w=1.8, h=1.4, label="", color="#dbeafe", border="#1e40af"):
    theta = np.linspace(-np.pi/2, np.pi/2, 50)
    arc_x = x + w/2 + (w/2) * np.cos(theta)
    arc_y = y + (h/2) * np.sin(theta)
    pts = np.vstack([
        [x, y - h/2],
        [x, y + h/2],
        [x + w/2, y + h/2],
        np.column_stack([arc_x[::-1], arc_y[::-1]]),
        [x + w/2, y - h/2]
    ])
    poly = patches.Polygon(pts, closed=True, facecolor=color, edgecolor=border, lw=2, zorder=3)
    ax.add_patch(poly)
    if label:
        ax.text(x + w*0.35, y, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color=border, zorder=4)
    return {
        'in1': (x, y + h*0.28),
        'in2': (x, y - h*0.28),
        'in_mid': (x, y),
        'in_3_top': (x, y + h*0.33),
        'in_3_mid': (x, y),
        'in_3_bot': (x, y - h*0.33),
        'out': (x + w, y)
    }

def draw_nand(ax, x, y, w=1.8, h=1.4, label="", color="#fef3c7", border="#b45309"):
    r_b = 0.11
    pins = draw_and(ax, x, y, w=w, h=h, label=label, color=color, border=border)
    bubble = patches.Circle((x + w + r_b, y), r_b, facecolor='white', edgecolor=border, lw=2, zorder=4)
    ax.add_patch(bubble)
    pins['out'] = (x + w + 2*r_b, y)
    return pins

def draw_or(ax, x, y, w=1.8, h=1.4, label="", color="#e0e7ff", border="#3730a3"):
    t = np.linspace(-1, 1, 50)
    y_back = y + (h/2) * t
    x_back = x + 0.3 * w * (1 - t**2)
    x_top = np.linspace(x, x + w, 50)
    y_top = y + (h/2) * (1 - (np.linspace(0, 1, 50))**1.6)
    x_bot = np.linspace(x + w, x, 50)
    y_bot = y - (h/2) * (1 - (np.linspace(1, 0, 50))**1.6)
    pts = np.vstack([
        np.column_stack([x_back, y_back]),
        np.column_stack([x_top, y_top]),
        np.column_stack([x_bot, y_bot])
    ])
    poly = patches.Polygon(pts, closed=True, facecolor=color, edgecolor=border, lw=2, zorder=3)
    ax.add_patch(poly)
    if label:
        ax.text(x + w*0.42, y, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color=border, zorder=4)
    return {
        'in1': (x + 0.15*w, y + h*0.28),
        'in2': (x + 0.15*w, y - h*0.28),
        'in_3_top': (x + 0.18*w, y + h*0.33),
        'in_3_mid': (x + 0.28*w, y),
        'in_3_bot': (x + 0.18*w, y - h*0.33),
        'out': (x + w, y)
    }

def draw_nor(ax, x, y, w=1.8, h=1.4, label="", color="#fef2f2", border="#dc2626"):
    r_b = 0.11
    pins = draw_or(ax, x, y, w=w, h=h, label=label, color=color, border=border)
    bubble = patches.Circle((x + w + r_b, y), r_b, facecolor='white', edgecolor=border, lw=2, zorder=4)
    ax.add_patch(bubble)
    pins['out'] = (x + w + 2*r_b, y)
    return pins

def draw_xor(ax, x, y, w=1.8, h=1.4, label="", color="#f3e8ff", border="#6b21a8"):
    pins = draw_or(ax, x, y, w=w, h=h, label=label, color=color, border=border)
    t = np.linspace(-1, 1, 50)
    y_arc = y + (h/2) * t
    x_arc = (x - 0.22) + 0.3 * w * (1 - t**2)
    ax.plot(x_arc, y_arc, color=border, lw=2, zorder=3)
    pins['in1'] = (x - 0.22 + 0.15*w, y + h*0.28)
    pins['in2'] = (x - 0.22 + 0.15*w, y - h*0.28)
    return pins

def draw_not(ax, x, y, w=1.2, h=0.8, label="", color="#fee2e2", border="#b91c1c"):
    r_b = 0.10
    pts = [[x, y - h/2], [x + w, y], [x, y + h/2]]
    poly = patches.Polygon(pts, closed=True, facecolor=color, edgecolor=border, lw=2, zorder=3)
    ax.add_patch(poly)
    bubble = patches.Circle((x + w + r_b, y), r_b, facecolor='white', edgecolor=border, lw=2, zorder=4)
    ax.add_patch(bubble)
    if label:
        ax.text(x + w*0.35, y, label, ha='center', va='center', fontsize=7, fontweight='bold', color=border, zorder=4)
    return {
        'in': (x, y),
        'out': (x + w + 2*r_b, y)
    }

def draw_flip_flop(ax, x, y, w=2.2, h=2.8, ff_type="D", name="FF 0", clk_edge="pos", has_clr=False,
                    color="#f8fafc", border="#0f172a"):
    rect = patches.FancyBboxPatch((x, y - h/2), w, h, boxstyle="square,pad=0",
                                  facecolor=color, edgecolor=border, lw=2.0, zorder=3)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2 - 0.35, name, ha='center', va='center', fontsize=9.5, fontweight='bold', color=border, zorder=4)
    ax.text(x + w/2, y + h/2 - 0.65, f"({ff_type} FF)", ha='center', va='center', fontsize=7.5, color="#64748b", zorder=4)

    pins = {}
    ax.text(x + w - 0.3, y + h/4, "Q", ha='right', va='center', fontsize=9.5, fontweight='bold', color=border, zorder=4)
    ax.text(x + w - 0.3, y - h/4, r"$\overline{Q}$", ha='right', va='center', fontsize=9.5, fontweight='bold', color=border, zorder=4)
    pins['Q'] = (x + w, y + h/4)
    pins['Q_bar'] = (x + w, y - h/4)

    if ff_type == "D":
        ax.text(x + 0.3, y + h/4, "D", ha='left', va='center', fontsize=9.5, fontweight='bold', color=border, zorder=4)
        pins['D'] = (x, y + h/4)
    elif ff_type == "T":
        ax.text(x + 0.3, y + h/4, "T", ha='left', va='center', fontsize=9.5, fontweight='bold', color=border, zorder=4)
        pins['T'] = (x, y + h/4)
    elif ff_type == "JK":
        ax.text(x + 0.3, y + h/3, "J", ha='left', va='center', fontsize=9.5, fontweight='bold', color=border, zorder=4)
        ax.text(x + 0.3, y - h/3, "K", ha='left', va='center', fontsize=9.5, fontweight='bold', color=border, zorder=4)
        pins['J'] = (x, y + h/3)
        pins['K'] = (x, y - h/3)

    clk_y = y if ff_type in ["JK", "SR"] else y - h/4
    chv_w = 0.22
    chv_h = 0.22
    if clk_edge == "neg":
        r_b = 0.09
        bubble = patches.Circle((x - r_b, clk_y), r_b, facecolor='white', edgecolor=border, lw=1.5, zorder=4)
        ax.add_patch(bubble)
        pins['CLK'] = (x - 2*r_b, clk_y)
    else:
        pins['CLK'] = (x, clk_y)

    ax.plot([x, x + chv_w, x], [clk_y + chv_h/2, clk_y, clk_y - chv_h/2], color=border, lw=1.8, zorder=4)
    ax.text(x + 0.3, clk_y, "CLK", ha='left', va='center', fontsize=7.5, color="#475569", zorder=4)

    if has_clr:
        clr_x = x + w/2
        r_b = 0.09
        bubble = patches.Circle((clr_x, y - h/2 - r_b), r_b, facecolor='white', edgecolor=border, lw=1.5, zorder=4)
        ax.add_patch(bubble)
        ax.text(clr_x, y - h/2 + 0.3, r"$\overline{CLR}$", ha='center', va='center', fontsize=7.5, fontweight='bold', color="#dc2626", zorder=4)
        pins['CLR'] = (clr_x, y - h/2 - 2*r_b)

    return pins

# ----------------- ALL 10 CIRCUITS -----------------

def gen_a4_q1():
    """Assignment 4 - Q1: Clocked SR Flip-Flop (NAND implementation)"""
    fig, ax = plt.subplots(figsize=(11, 6.5), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(8.0, 9.4, "Clocked SR Flip-Flop (NAND-Gate Implementation)", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(8.0, 8.9, "Assignment 4 - Question 1 | Metastability & Invalid State Analysis (S=1, R=1)", ha='center', fontsize=9.5, color="#64748b")

    # Gates
    g1 = draw_nand(ax, 3.0, 6.5, label="NAND 1\nSteering")
    g2 = draw_nand(ax, 3.0, 3.0, label="NAND 2\nSteering")
    g3 = draw_nand(ax, 9.0, 6.5, label="NAND 3\nLatch")
    g4 = draw_nand(ax, 9.0, 3.0, label="NAND 4\nLatch")

    # Inputs S & R
    draw_ortho(ax, (1.0, g1['in1'][1]), g1['in1'], label="S", label_pos=(1.3, g1['in1'][1] + 0.35))
    draw_ortho(ax, (1.0, g2['in2'][1]), g2['in2'], label="R", label_pos=(1.3, g2['in2'][1] - 0.35))

    # CLK
    draw_path(ax, [(1.0, 4.75), (2.0, 4.75), (2.0, g1['in2'][1]), g1['in2']], label="CLK", label_pos=(1.3, 5.05))
    draw_path(ax, [(2.0, 4.75), (2.0, g2['in1'][1]), g2['in1']])
    draw_dot(ax, 2.0, 4.75)

    # Inter-stage wires (strictly rectilinear)
    draw_ortho(ax, g1['out'], g3['in1'], x_break=6.5, label=r"$\overline{S'}$", label_pos=(6.2, g1['out'][1] + 0.35))
    draw_ortho(ax, g2['out'], g4['in2'], x_break=6.5, label=r"$\overline{R'}$", label_pos=(6.2, g2['out'][1] - 0.35))

    # Outputs
    q_out = (14.5, g3['out'][1])
    q_bar_out = (14.5, g4['out'][1])
    draw_ortho(ax, g3['out'], q_out, label="Q (Output)", label_pos=(14.0, g3['out'][1] + 0.35))
    draw_ortho(ax, g4['out'], q_bar_out, label=r"$\overline{Q}$ (Output)", label_pos=(14.0, g4['out'][1] - 0.35))

    # Cross feedback loops (strictly orthogonal)
    draw_dot(ax, 12.0, g3['out'][1])
    draw_path(ax, [(12.0, g3['out'][1]), (12.0, 5.2), (7.8, 5.2), (7.8, g4['in1'][1]), g4['in1']])

    draw_dot(ax, 12.3, g4['out'][1])
    draw_path(ax, [(12.3, g4['out'][1]), (12.3, 4.3), (7.5, 4.3), (7.5, g3['in2'][1]), g3['in2']])

    # Analysis Box
    note_txt = (
        "METASTABILITY EXPLANATION (Edge 4 to Edge 5 Transition):\n"
        "• At S=1, R=1: Both NAND 3 and NAND 4 outputs are driven to logic HIGH (Q = Q_bar = 1, complement broken!).\n"
        "• When inputs transition to S=0, R=0 (HOLD): Both latches simultaneously attempt to maintain 1, causing a race\n"
        "  condition. Transistor propagation delay mismatch forces the latch into an unpredictable state (Metastable oscillation)."
    )
    ax.text(8.0, 1.0, note_txt, ha='center', va='center', fontsize=8, color="#7f1d1d",
            bbox=dict(boxstyle='round,pad=0.4', fc='#fef2f2', ec='#f87171', lw=1.2))

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_a4_q1_sr_latch.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_a4_q1_sr_latch.svg"))
    plt.close()
    print("Gen a4_q1")

def gen_a4_q2():
    """Assignment 4 - Q2: Positive Edge-Triggered T Flip-Flop (All-NAND Master-Slave)"""
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    ax.set_xlim(0, 19)
    ax.set_ylim(0, 12)
    ax.axis('off')

    ax.text(9.5, 11.4, "Positive Edge-Triggered T Flip-Flop (All-NAND Master-Slave Architecture)", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(9.5, 10.9, "Assignment 4 - Question 2 | 9 NAND Gates with Rectilinear Anti-Race Feedback", ha='center', fontsize=9.5, color="#64748b")

    # Master Stage
    g1 = draw_nand(ax, 2.5, 8.2, label="G1\nMaster In")
    g2 = draw_nand(ax, 2.5, 3.8, label="G2\nMaster In")
    g3 = draw_nand(ax, 6.2, 8.2, label="G3\nMaster Latch")
    g4 = draw_nand(ax, 6.2, 3.8, label="G4\nMaster Latch")

    # Clock Inverter
    g5 = draw_nand(ax, 6.2, 6.0, w=1.3, h=1.0, label="G5\nCLK Invert")

    # Slave Stage
    g6 = draw_nand(ax, 10.0, 8.2, label="G6\nSlave In")
    g7 = draw_nand(ax, 10.0, 3.8, label="G7\nSlave In")
    g8 = draw_nand(ax, 13.8, 8.2, label="G8\nSlave Latch")
    g9 = draw_nand(ax, 13.8, 3.8, label="G9\nSlave Latch")

    # T Input
    draw_path(ax, [(0.6, 7.0), (1.5, 7.0), (1.5, g1['in_3_top'][1]), g1['in_3_top']], label="T", label_pos=(0.8, 7.3))
    draw_path(ax, [(1.5, 7.0), (1.5, g2['in_3_bot'][1]), g2['in_3_bot']])
    draw_dot(ax, 1.5, 7.0)

    # CLK
    draw_path(ax, [(0.6, 6.0), (2.0, 6.0), (2.0, g1['in_3_mid'][1]), g1['in_3_mid']], label="CLK", label_pos=(0.8, 6.3))
    draw_path(ax, [(2.0, 6.0), (2.0, g2['in_3_mid'][1]), g2['in_3_mid']])
    draw_dot(ax, 2.0, 6.0)
    # CLK to G5 inverter
    draw_path(ax, [(2.0, 6.0), (5.5, 6.0), (5.5, g5['in1'][1]), g5['in1']])
    draw_path(ax, [(5.5, 6.0), (5.5, g5['in2'][1]), g5['in2']])
    draw_dot(ax, 5.5, 6.0)

    # Inverted Clock to Slave
    draw_path(ax, [g5['out'], (9.0, 6.0), (9.0, g6['in2'][1]), g6['in2']], label=r"$\overline{CLK}$", label_pos=(8.7, 6.3))
    draw_path(ax, [(9.0, 6.0), (9.0, g7['in1'][1]), g7['in1']])
    draw_dot(ax, 9.0, 6.0)

    # Master Latch Wires
    draw_ortho(ax, g1['out'], g3['in1'], x_break=5.4)
    draw_ortho(ax, g2['out'], g4['in2'], x_break=5.4)
    # Master cross feedback
    draw_dot(ax, 8.5, g3['out'][1])
    draw_path(ax, [(8.5, g3['out'][1]), (8.5, 7.1), (5.7, 7.1), (5.7, g4['in1'][1]), g4['in1']])
    draw_dot(ax, 8.7, g4['out'][1])
    draw_path(ax, [(8.7, g4['out'][1]), (8.7, 4.9), (5.5, 4.9), (5.5, g3['in2'][1]), g3['in2']])

    # Master to Slave
    draw_ortho(ax, (8.5, g3['out'][1]), g6['in1'], x_break=9.2)
    draw_ortho(ax, (8.7, g4['out'][1]), g7['in2'], x_break=9.2)

    # Slave Latch Wires
    draw_ortho(ax, g6['out'], g8['in1'], x_break=12.9)
    draw_ortho(ax, g7['out'], g9['in2'], x_break=12.9)
    # Slave cross feedback
    draw_dot(ax, 16.2, g8['out'][1])
    draw_path(ax, [(16.2, g8['out'][1]), (16.2, 7.1), (13.2, 7.1), (13.2, g9['in1'][1]), g9['in1']])
    draw_dot(ax, 16.4, g9['out'][1])
    draw_path(ax, [(16.4, g9['out'][1]), (16.4, 4.9), (13.0, 4.9), (13.0, g8['in2'][1]), g8['in2']])

    # Outputs
    draw_ortho(ax, (16.2, g8['out'][1]), (18.2, g8['out'][1]), label="Q", label_pos=(17.8, g8['out'][1] + 0.35))
    draw_ortho(ax, (16.4, g9['out'][1]), (18.2, g9['out'][1]), label=r"$\overline{Q}$", label_pos=(17.8, g9['out'][1] - 0.35))

    # Long Feedback Loops (Rectilinear)
    # Q to G2 (K steering)
    draw_dot(ax, 17.2, g8['out'][1])
    draw_path(ax, [(17.2, g8['out'][1]), (17.2, 10.2), (1.0, 10.2), (1.0, g2['in_3_top'][1]), g2['in_3_top']], color="#dc2626", lw=1.6)
    ax.text(9.5, 10.45, "Feedback Q to G2 (K-input steering)", color="#dc2626", fontsize=8, fontweight='bold', ha='center')

    # Q_bar to G1 (J steering)
    draw_dot(ax, 17.5, g9['out'][1])
    draw_path(ax, [(17.5, g9['out'][1]), (17.5, 1.8), (0.7, 1.8), (0.7, g1['in_3_bot'][1]), g1['in_3_bot']], color="#0284c7", lw=1.6)
    ax.text(9.5, 1.55, r"Feedback $\overline{Q}$ to G1 (J-input steering)", color="#0284c7", fontsize=8, fontweight='bold', ha='center')

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_a4_q2_nand_t_ff.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_a4_q2_nand_t_ff.svg"))
    plt.close()
    print("Gen a4_q2")

def gen_a4_q2_waveform():
    """Assignment 4 - Q2: Output Waveform Q(t) for 6 Positive Clock Edges"""
    fig, ax = plt.subplots(figsize=(13, 7), dpi=300)
    ax.set_xlim(-0.5, 7.5)
    ax.set_ylim(-0.5, 9.5)
    ax.axis('off')

    ax.text(3.5, 9.0, "Positive Edge-Triggered T Flip-Flop: 6-Clock-Edge Waveform Analysis", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(3.5, 8.5, "Assignment 4 - Question 2 | Initial Q = 1 | T toggles Q when T = 1 at positive clock edge", ha='center', fontsize=9.5, color="#64748b")

    # Grid vertical lines for clock edges
    for i in range(1, 7):
        ax.axvline(i, color="#cbd5e1", ls="--", lw=1.2, zorder=1)
        ax.text(i, 7.9, f"Edge {i}\n(↑)", ha='center', va='center', fontsize=8, fontweight='bold', color="#475569",
                bbox=dict(boxstyle='round,pad=0.2', fc='#f1f5f9', ec='#cbd5e1'))

    # 1. Clock Waveform
    clk_x = [0.0]
    clk_y = [5.5]
    for i in range(1, 7):
        clk_x.extend([i - 0.5, i, i, i + 0.5, i + 0.5])
        clk_y.extend([5.5, 5.5, 6.7, 6.7, 5.5])
    clk_x.append(7.0)
    clk_y.append(5.5)
    ax.plot(clk_x, clk_y, color="#1e293b", lw=2.2, zorder=3)
    ax.text(-0.3, 6.1, "CLK", fontsize=10, fontweight='bold', ha='right', va='center', color="#1e293b")

    for i in range(1, 7):
        ax.annotate('', xy=(i, 6.75), xytext=(i, 5.45),
                    arrowprops=dict(arrowstyle="->", color="#ef4444", lw=2))

    # 2. Input T Waveform
    t_pts = [
        (0.0, 3.0), (1.6, 3.0), (1.6, 4.2), (2.4, 4.2), (2.4, 3.0),
        (4.4, 3.0), (4.4, 4.2), (7.0, 4.2)
    ]
    tx = [p[0] for p in t_pts]
    ty = [p[1] for p in t_pts]
    ax.step(tx, ty, where='post', color="#2563eb", lw=2.2, zorder=3)
    ax.text(-0.3, 3.6, "Input T", fontsize=10, fontweight='bold', ha='right', va='center', color="#2563eb")

    t_levels = [("T=0", 0), ("T=1", 1), ("T=0", 0), ("T=0", 0), ("T=1", 1), ("T=1", 1)]
    for idx, (lbl, val) in enumerate(t_levels, start=1):
        y_pos = 4.4 if val == 1 else 3.3
        c_bg = "#dbeafe" if val == 1 else "#f1f5f9"
        ax.text(idx, y_pos, lbl, ha='center', va='bottom', fontsize=8, fontweight='bold', color="#1d4ed8",
                bbox=dict(boxstyle='square,pad=0.15', fc=c_bg, ec='none', alpha=0.9))

    # 3. Output Q(t) Waveform
    q_pts = [
        (0.0, 1.7), (2.0, 1.7), (2.0, 0.5), (5.0, 0.5),
        (5.0, 1.7), (6.0, 1.7), (6.0, 0.5), (7.0, 0.5)
    ]
    qx = [p[0] for p in q_pts]
    qy = [p[1] for p in q_pts]
    ax.step(qx, qy, where='post', color="#059669", lw=2.5, zorder=3)
    ax.text(-0.3, 1.1, "Output Q(t)", fontsize=10, fontweight='bold', ha='right', va='center', color="#059669")

    states = [
        (0.5, "Q = 1\n(Initial)", "#10b981", "#ecfdf5"),
        (1.5, "Q = 1\n(HOLD)", "#10b981", "#ecfdf5"),
        (2.5, "Q = 0\n(TOGGLE)", "#ef4444", "#fef2f2"),
        (3.5, "Q = 0\n(HOLD)", "#64748b", "#f8fafc"),
        (4.5, "Q = 0\n(HOLD)", "#64748b", "#f8fafc"),
        (5.5, "Q = 1\n(TOGGLE)", "#10b981", "#ecfdf5"),
        (6.5, "Q = 0\n(TOGGLE)", "#ef4444", "#fef2f2"),
    ]
    for x_pos, text, b_col, f_col in states:
        ax.text(x_pos, -0.2, text, ha='center', va='center', fontsize=7.5, fontweight='bold', color=b_col,
                bbox=dict(boxstyle='round,pad=0.25', fc=f_col, ec=b_col, lw=1.2))

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_a4_q2_waveform.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_a4_q2_waveform.svg"))
    plt.close()
    print("Gen a4_q2_waveform")

def gen_a4_q3():
    """Assignment 4 - Q3: Sequential Circuit Analysis (Fig 3.3.4 a)"""
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 11)
    ax.axis('off')

    ax.text(8.0, 10.4, "Analysis of Sequential Circuit (Fig. 3.3.4 a)", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(8.0, 9.9, "Assignment 4 - Question 3 | Exact Gate Topology & Moore Output F = A XOR B", ha='center', fontsize=9.5, color="#64748b")

    # Flip-Flops
    ffa = draw_flip_flop(ax, 7.0, 7.2, ff_type="JK", name="Flip-Flop A")
    ffb = draw_flip_flop(ax, 7.0, 2.6, ff_type="JK", name="Flip-Flop B")

    # Combinational Gates
    inv_x  = draw_not(ax, 1.8, 7.8, label="NOT")
    and_ka = draw_and(ax, 4.0, 6.4, label="AND")
    xor_kb = draw_xor(ax, 4.0, 1.8, label="XOR")
    xor_f  = draw_xor(ax, 12.0, 8.0, label="XOR")

    # Input X
    draw_ortho(ax, (0.5, inv_x['in'][1]), inv_x['in'], label="Input X", label_pos=(1.0, inv_x['in'][1] + 0.35))
    draw_dot(ax, 1.1, inv_x['in'][1])
    draw_path(ax, [(1.1, inv_x['in'][1]), (1.1, xor_kb['in2'][1]), xor_kb['in2']])

    # Inverter Output X_bar
    draw_ortho(ax, inv_x['out'], and_ka['in1'], x_break=3.5, label=r"$\overline{X}$", label_pos=(3.3, inv_x['out'][1] + 0.35))
    draw_dot(ax, 3.5, inv_x['out'][1])
    draw_path(ax, [(3.5, inv_x['out'][1]), (3.5, ffb['J'][1]), ffb['J']], label=r"$J_B = \overline{X}$", label_pos=(5.3, ffb['J'][1] + 0.35))

    # Line B from FF B
    draw_ortho(ax, ffb['Q'], (10.2, ffb['Q'][1]))
    draw_dot(ax, 10.2, ffb['Q'][1])
    ax.text(10.5, ffb['Q'][1] + 0.35, "Line B", fontsize=8.5, fontweight='bold', color="#0f172a")

    # Line B to J_A
    draw_path(ax, [(10.2, ffb['Q'][1]), (10.2, 4.8), (3.0, 4.8), (3.0, ffa['J'][1]), ffa['J']], label=r"$J_A = B$", label_pos=(5.2, ffa['J'][1] + 0.35))
    draw_dot(ax, 3.0, 4.8)
    draw_path(ax, [(3.0, 4.8), (3.0, and_ka['in2'][1]), and_ka['in2']])

    # AND_KA output to K_A
    draw_ortho(ax, and_ka['out'], ffa['K'], label=r"$K_A = B \cdot \overline{X}$", label_pos=(5.8, ffa['K'][1] + 0.35))

    # Line A from FF A
    draw_ortho(ax, ffa['Q'], (10.8, ffa['Q'][1]))
    draw_dot(ax, 10.8, ffa['Q'][1])
    ax.text(10.5, ffa['Q'][1] + 0.35, "Line A", fontsize=8.5, fontweight='bold', color="#0f172a")

    # Line A to XOR_KB
    draw_path(ax, [(10.8, ffa['Q'][1]), (10.8, 0.8), (3.5, 0.8), (3.5, xor_kb['in1'][1]), xor_kb['in1']])

    # XOR_KB output to K_B
    draw_ortho(ax, xor_kb['out'], ffb['K'], label=r"$K_B = A \oplus X$", label_pos=(5.8, ffb['K'][1] - 0.35))

    # Line A and Line B to Output XOR_F
    draw_path(ax, [(10.8, ffa['Q'][1]), (10.8, xor_f['in1'][1]), xor_f['in1']])
    draw_path(ax, [(10.2, ffb['Q'][1]), (11.4, ffb['Q'][1]), (11.4, xor_f['in2'][1]), xor_f['in2']])

    # Output F
    draw_ortho(ax, xor_f['out'], (15.0, xor_f['out'][1]), label=r"Output $F = A \oplus B$", label_pos=(14.2, xor_f['out'][1] + 0.4), label_color="#6b21a8")

    # Common Clock Bus
    draw_path(ax, [(5.5, 0.3), (5.5, ffa['CLK'][1]), ffa['CLK']], label="Clock", label_pos=(5.5, 0.1))
    draw_dot(ax, 5.5, ffb['CLK'][1])
    draw_ortho(ax, (5.5, ffb['CLK'][1]), ffb['CLK'])

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_a4_q3_sequential_circuit.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_a4_q3_sequential_circuit.svg"))
    plt.close()
    print("Gen a4_q3")

def gen_a4_q4():
    """Assignment 4 - Q4: 3-Bit Synchronous Counter (D Flip-Flops)"""
    fig, ax = plt.subplots(figsize=(14, 8.5), dpi=300)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 13)
    ax.axis('off')

    ax.text(10.0, 12.4, "3-Bit Arbitrary Synchronous Counter (D Flip-Flops)", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(10.0, 11.9, "Sequence: 0 -> 4 -> 6 -> 1 -> 3 -> 7 -> 2 -> 5 -> 0 | Assignment 4 - Question 4", ha='center', fontsize=9.5, color="#64748b")

    # 3 D Flip-Flops
    ff2 = draw_flip_flop(ax, 14.5, 9.2, ff_type="D", name="FF 2 (MSB)")
    ff1 = draw_flip_flop(ax, 14.5, 5.5, ff_type="D", name="FF 1")
    ff0 = draw_flip_flop(ax, 14.5, 1.8, ff_type="D", name="FF 0 (LSB)")

    # Outputs
    draw_ortho(ax, ff2['Q'], (18.5, ff2['Q'][1]), label="Q2", label_pos=(18.0, ff2['Q'][1] + 0.35))
    draw_ortho(ax, ff2['Q_bar'], (18.5, ff2['Q_bar'][1]), label=r"$\overline{Q_2}$", label_pos=(18.0, ff2['Q_bar'][1] - 0.35))

    draw_ortho(ax, ff1['Q'], (18.5, ff1['Q'][1]), label="Q1", label_pos=(18.0, ff1['Q'][1] + 0.35))
    draw_ortho(ax, ff1['Q_bar'], (18.5, ff1['Q_bar'][1]), label=r"$\overline{Q_1}$", label_pos=(18.0, ff1['Q_bar'][1] - 0.35))

    draw_ortho(ax, ff0['Q'], (18.5, ff0['Q'][1]), label="Q0", label_pos=(18.0, ff0['Q'][1] + 0.35))
    draw_ortho(ax, ff0['Q_bar'], (18.5, ff0['Q_bar'][1]), label=r"$\overline{Q_0}$", label_pos=(18.0, ff0['Q_bar'][1] - 0.35))

    # Combinational Logic Gates
    # D2 = Q1'*Q0' + Q2'*Q1
    and_2a = draw_and(ax, 7.0, 10.2, label="AND\nQ1'*Q0'")
    and_2b = draw_and(ax, 7.0, 8.4, label="AND\nQ2'*Q1")
    or_2   = draw_or(ax, 10.5, 9.3, label="OR\nD2")
    draw_ortho(ax, and_2a['out'], or_2['in1'], x_break=9.6)
    draw_ortho(ax, and_2b['out'], or_2['in2'], x_break=9.6)
    draw_ortho(ax, or_2['out'], ff2['D'], label=r"$D_2$", label_pos=(13.2, ff2['D'][1] + 0.35))

    # D1 = Q2'*Q0 + Q1*Q0 + Q2*Q1'*Q0'
    and_1a = draw_and(ax, 6.8, 6.7, label="AND\nQ2'*Q0")
    and_1b = draw_and(ax, 6.8, 5.5, label="AND\nQ1*Q0")
    and_1c = draw_and(ax, 6.8, 4.3, label="AND\nQ2*Q1'*Q0'")
    or_1   = draw_or(ax, 10.5, 5.5, label="OR\nD1")
    draw_ortho(ax, and_1a['out'], or_1['in_3_top'], x_break=9.5)
    draw_ortho(ax, and_1b['out'], or_1['in_3_mid'], x_break=9.5)
    draw_ortho(ax, and_1c['out'], or_1['in_3_bot'], x_break=9.5)
    draw_ortho(ax, or_1['out'], ff1['D'], label=r"$D_1$", label_pos=(13.2, ff1['D'][1] + 0.35))

    # D0 = Q1*Q0' + Q2'*Q0
    and_0a = draw_and(ax, 7.0, 2.7, label="AND\nQ1*Q0'")
    and_0b = draw_and(ax, 7.0, 1.1, label="AND\nQ2'*Q0")
    or_0   = draw_or(ax, 10.5, 1.9, label="OR\nD0")
    draw_ortho(ax, and_0a['out'], or_0['in1'], x_break=9.6)
    draw_ortho(ax, and_0b['out'], or_0['in2'], x_break=9.6)
    draw_ortho(ax, or_0['out'], ff0['D'], label=r"$D_0$", label_pos=(13.2, ff0['D'][1] + 0.35))

    # Feedback Bus lines
    ax.text(3.0, 11.6, "State Feedback Bus", ha='center', fontsize=9.5, fontweight='bold', color="#475569")
    signals = [
        (1.0, r"$Q_2$"), (1.8, r"$\overline{Q_2}$"),
        (2.6, r"$Q_1$"), (3.4, r"$\overline{Q_1}$"),
        (4.2, r"$Q_0$"), (5.0, r"$\overline{Q_0}$")
    ]
    for x_bus, name in signals:
        draw_ortho(ax, (x_bus, 0.5), (x_bus, 10.8), color="#94a3b8", lw=1.2)
        ax.text(x_bus, 11.05, name, ha='center', fontsize=8.5, fontweight='bold', color="#1e293b")

    # Connect buses to gates
    # and_2a: Q1_bar (3.4), Q0_bar (5.0)
    draw_ortho(ax, (3.4, and_2a['in1'][1]), and_2a['in1']); draw_dot(ax, 3.4, and_2a['in1'][1])
    draw_ortho(ax, (5.0, and_2a['in2'][1]), and_2a['in2']); draw_dot(ax, 5.0, and_2a['in2'][1])

    # and_2b: Q2_bar (1.8), Q1 (2.6)
    draw_ortho(ax, (1.8, and_2b['in1'][1]), and_2b['in1']); draw_dot(ax, 1.8, and_2b['in1'][1])
    draw_ortho(ax, (2.6, and_2b['in2'][1]), and_2b['in2']); draw_dot(ax, 2.6, and_2b['in2'][1])

    # and_1a: Q2_bar (1.8), Q0 (4.2)
    draw_ortho(ax, (1.8, and_1a['in1'][1]), and_1a['in1']); draw_dot(ax, 1.8, and_1a['in1'][1])
    draw_ortho(ax, (4.2, and_1a['in2'][1]), and_1a['in2']); draw_dot(ax, 4.2, and_1a['in2'][1])

    # and_1b: Q1 (2.6), Q0 (4.2)
    draw_ortho(ax, (2.6, and_1b['in1'][1]), and_1b['in1']); draw_dot(ax, 2.6, and_1b['in1'][1])
    draw_ortho(ax, (4.2, and_1b['in2'][1]), and_1b['in2']); draw_dot(ax, 4.2, and_1b['in2'][1])

    # and_0a: Q1 (2.6), Q0_bar (5.0)
    draw_ortho(ax, (2.6, and_0a['in1'][1]), and_0a['in1']); draw_dot(ax, 2.6, and_0a['in1'][1])
    draw_ortho(ax, (5.0, and_0a['in2'][1]), and_0a['in2']); draw_dot(ax, 5.0, and_0a['in2'][1])

    # and_0b: Q2_bar (1.8), Q0 (4.2)
    draw_ortho(ax, (1.8, and_0b['in1'][1]), and_0b['in1']); draw_dot(ax, 1.8, and_0b['in1'][1])
    draw_ortho(ax, (4.2, and_0b['in2'][1]), and_0b['in2']); draw_dot(ax, 4.2, and_0b['in2'][1])

    # Clock line
    draw_path(ax, [(13.8, 0.4), (13.8, ff2['CLK'][1]), ff2['CLK']], label="Clock", label_pos=(13.8, 0.1))
    draw_dot(ax, 13.8, ff1['CLK'][1]); draw_ortho(ax, (13.8, ff1['CLK'][1]), ff1['CLK'])
    draw_dot(ax, 13.8, ff0['CLK'][1]); draw_ortho(ax, (13.8, ff0['CLK'][1]), ff0['CLK'])

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_a4_q4_3bit_counter.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_a4_q4_3bit_counter.svg"))
    plt.close()
    print("Gen a4_q4")

def gen_a4_q5():
    """Assignment 4 - Q5: Decade (Mod-10) Asynchronous Counter (T Flip-Flops)"""
    fig, ax = plt.subplots(figsize=(14, 7), dpi=300)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(9.0, 9.4, "Decade (Mod-10) Asynchronous Ripple Counter (T Flip-Flops)", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(9.0, 8.9, "Assignment 4 - Question 5 | Mod-10 Active-Low Truncation Gate (NAND: Q3 * Q1)", ha='center', fontsize=9.5, color="#64748b")

    # 4 T Flip-Flops (Cascaded Ripple)
    ff0 = draw_flip_flop(ax, 2.5, 5.0, ff_type="T", name="FF 0 (LSB)", clk_edge="neg", has_clr=True)
    ff1 = draw_flip_flop(ax, 6.2, 5.0, ff_type="T", name="FF 1", clk_edge="neg", has_clr=True)
    ff2 = draw_flip_flop(ax, 9.9, 5.0, ff_type="T", name="FF 2", clk_edge="neg", has_clr=True)
    ff3 = draw_flip_flop(ax, 13.6, 5.0, ff_type="T", name="FF 3 (MSB)", clk_edge="neg", has_clr=True)

    # VCC to all T inputs
    draw_ortho(ax, (1.0, 7.8), (15.0, 7.8), color="#16a34a", lw=2)
    ax.text(0.9, 7.8, r"Logic 1 ($V_{CC}$)", ha='right', va='center', fontsize=9.5, fontweight='bold', color="#16a34a")
    for ff in [ff0, ff1, ff2, ff3]:
        draw_path(ax, [(ff['T'][0] - 0.4, 7.8), (ff['T'][0] - 0.4, ff['T'][1]), ff['T']], color="#16a34a")
        draw_dot(ax, ff['T'][0] - 0.4, 7.8, color="#16a34a")

    # External Clock to FF 0
    draw_ortho(ax, (1.0, ff0['CLK'][1]), ff0['CLK'], label="CLK In", label_pos=(1.5, ff0['CLK'][1] + 0.35))

    # Ripple clocks: Q_k to CLK_{k+1}
    draw_path(ax, [ff0['Q'], (5.2, ff0['Q'][1]), (5.2, ff1['CLK'][1]), ff1['CLK']])
    draw_dot(ax, 5.2, ff0['Q'][1])
    draw_ortho(ax, (5.2, ff0['Q'][1]), (5.2, 7.2), label="Q0", label_pos=(5.2, 7.45))

    draw_path(ax, [ff1['Q'], (8.9, ff1['Q'][1]), (8.9, ff2['CLK'][1]), ff2['CLK']])
    draw_dot(ax, 8.9, ff1['Q'][1])
    draw_ortho(ax, (8.9, ff1['Q'][1]), (8.9, 7.2), label="Q1", label_pos=(8.9, 7.45))

    draw_path(ax, [ff2['Q'], (12.6, ff2['Q'][1]), (12.6, ff3['CLK'][1]), ff3['CLK']])
    draw_dot(ax, 12.6, ff2['Q'][1])
    draw_ortho(ax, (12.6, ff2['Q'][1]), (12.6, 7.2), label="Q2", label_pos=(12.6, 7.45))

    draw_ortho(ax, ff3['Q'], (16.8, ff3['Q'][1]), label="Q3 (MSB)", label_pos=(16.5, ff3['Q'][1] + 0.35))

    # Reset NAND Gate for count 10 (1010_2 -> Q3=1, Q1=1)
    nand_rst = draw_nand(ax, 8.5, 1.8, label="NAND\nReset")
    draw_path(ax, [(8.9, 7.2), (8.9, nand_rst['in1'][1]), nand_rst['in1']], color="#dc2626")
    draw_dot(ax, 8.9, 7.2, color="#dc2626")

    draw_path(ax, [(16.2, ff3['Q'][1]), (16.2, nand_rst['in2'][1]), nand_rst['in2']], color="#dc2626")
    draw_dot(ax, 16.2, ff3['Q'][1], color="#dc2626")

    # Connect NAND output to all CLR pins
    draw_path(ax, [nand_rst['out'], (11.0, 1.8), (11.0, 3.2), (3.6, 3.2)], color="#dc2626", lw=1.8)
    draw_dot(ax, 11.0, 3.2, color="#dc2626")
    draw_path(ax, [(11.0, 3.2), (14.7, 3.2), (14.7, ff3['CLR'][1]), ff3['CLR']], color="#dc2626")
    draw_ortho(ax, (11.0, 3.2), ff2['CLR'], color="#dc2626")
    draw_path(ax, [(7.3, 3.2), (7.3, ff1['CLR'][1]), ff1['CLR']], color="#dc2626"); draw_dot(ax, 7.3, 3.2, color="#dc2626")
    draw_path(ax, [(3.6, 3.2), (3.6, ff0['CLR'][1]), ff0['CLR']], color="#dc2626"); draw_dot(ax, 3.6, 3.2, color="#dc2626")

    ax.text(10.5, 2.7, r"Active-Low Clear Bus: $\overline{CLR} = \overline{Q_3 \cdot Q_1}$", color="#dc2626", fontsize=8.5, fontweight='bold')

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_a4_q5_decade_ripple.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_a4_q5_decade_ripple.svg"))
    plt.close()
    print("Gen a4_q5")

def gen_a5_q1():
    """Assignment 5 - Q1: Prime Counter (2 -> 3 -> 5 -> 7 -> 2) Using T Flip-Flops"""
    fig, ax = plt.subplots(figsize=(13, 8), dpi=300)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 12)
    ax.axis('off')

    ax.text(9.0, 11.4, "Synchronous Prime Number Up-Counter (2 -> 3 -> 5 -> 7 -> 2)", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(9.0, 10.9, "Assignment 5 - Question 1 | T Flip-Flop Design with Combinational Excitation", ha='center', fontsize=9.5, color="#64748b")

    # 3 T Flip-Flops
    ff2 = draw_flip_flop(ax, 12.5, 8.5, ff_type="T", name="FF 2 (MSB)")
    ff1 = draw_flip_flop(ax, 12.5, 5.0, ff_type="T", name="FF 1")
    ff0 = draw_flip_flop(ax, 12.5, 1.5, ff_type="T", name="FF 0 (LSB)")

    # Outputs
    draw_ortho(ax, ff2['Q'], (16.5, ff2['Q'][1]), label="Q2", label_pos=(16.0, ff2['Q'][1] + 0.35))
    draw_ortho(ax, ff2['Q_bar'], (16.5, ff2['Q_bar'][1]), label=r"$\overline{Q_2}$", label_pos=(16.0, ff2['Q_bar'][1] - 0.35))

    draw_ortho(ax, ff1['Q'], (16.5, ff1['Q'][1]), label="Q1", label_pos=(16.0, ff1['Q'][1] + 0.35))
    draw_ortho(ax, ff1['Q_bar'], (16.5, ff1['Q_bar'][1]), label=r"$\overline{Q_1}$", label_pos=(16.0, ff1['Q_bar'][1] - 0.35))

    draw_ortho(ax, ff0['Q'], (16.5, ff0['Q'][1]), label="Q0", label_pos=(16.0, ff0['Q'][1] + 0.35))
    draw_ortho(ax, ff0['Q_bar'], (16.5, ff0['Q_bar'][1]), label=r"$\overline{Q_0}$", label_pos=(16.0, ff0['Q_bar'][1] - 0.35))

    # Excitation Gates
    # T2 = Q1 * Q0
    and_t2 = draw_and(ax, 8.0, 9.2, label="AND\nQ1*Q0")
    draw_ortho(ax, and_t2['out'], ff2['T'], label=r"$T_2$", label_pos=(11.0, ff2['T'][1] + 0.35))

    # T1 = (Q2*Q1)' * Q0
    nand_t1 = draw_nand(ax, 5.5, 6.1, label="NAND\n(Q2*Q1)'")
    and_t1  = draw_and(ax, 8.5, 5.7, label="AND\nT1")
    draw_ortho(ax, nand_t1['out'], and_t1['in1'], x_break=7.8)
    draw_ortho(ax, and_t1['out'], ff1['T'], label=r"$T_1$", label_pos=(11.0, ff1['T'][1] + 0.35))

    # T0 = Q1 * (Q0' + Q2)
    or_t0  = draw_or(ax, 5.5, 1.8, label="OR\nQ0'+Q2")
    and_t0 = draw_and(ax, 8.5, 2.2, label="AND\nT0")
    draw_ortho(ax, or_t0['out'], and_t0['in2'], x_break=7.8)
    draw_ortho(ax, and_t0['out'], ff0['T'], label=r"$T_0$", label_pos=(11.0, ff0['T'][1] + 0.35))

    # Bus lines
    signals = [(1.5, r"$Q_2$"), (2.3, r"$Q_1$"), (3.1, r"$Q_0$"), (3.9, r"$\overline{Q_0}$")]
    for x_bus, name in signals:
        draw_ortho(ax, (x_bus, 0.5), (x_bus, 10.0), color="#94a3b8", lw=1.2)
        ax.text(x_bus, 10.2, name, ha='center', fontsize=8.5, fontweight='bold', color="#1e293b")

    # Connect to gates
    # and_t2: Q1 (2.3), Q0 (3.1)
    draw_ortho(ax, (2.3, and_t2['in1'][1]), and_t2['in1']); draw_dot(ax, 2.3, and_t2['in1'][1])
    draw_ortho(ax, (3.1, and_t2['in2'][1]), and_t2['in2']); draw_dot(ax, 3.1, and_t2['in2'][1])

    # nand_t1: Q2 (1.5), Q1 (2.3)
    draw_ortho(ax, (1.5, nand_t1['in1'][1]), nand_t1['in1']); draw_dot(ax, 1.5, nand_t1['in1'][1])
    draw_ortho(ax, (2.3, nand_t1['in2'][1]), nand_t1['in2']); draw_dot(ax, 2.3, nand_t1['in2'][1])
    # and_t1: Q0 (3.1)
    draw_ortho(ax, (3.1, and_t1['in2'][1]), and_t1['in2']); draw_dot(ax, 3.1, and_t1['in2'][1])

    # or_t0: Q2 (1.5), Q0_bar (3.9)
    draw_ortho(ax, (1.5, or_t0['in1'][1]), or_t0['in1']); draw_dot(ax, 1.5, or_t0['in1'][1])
    draw_ortho(ax, (3.9, or_t0['in2'][1]), or_t0['in2']); draw_dot(ax, 3.9, or_t0['in2'][1])
    # and_t0: Q1 (2.3)
    draw_ortho(ax, (2.3, and_t0['in1'][1]), and_t0['in1']); draw_dot(ax, 2.3, and_t0['in1'][1])

    # Clock Line
    draw_path(ax, [(11.8, 0.4), (11.8, ff2['CLK'][1]), ff2['CLK']], label="Clock", label_pos=(11.8, 0.1))
    draw_dot(ax, 11.8, ff1['CLK'][1]); draw_ortho(ax, (11.8, ff1['CLK'][1]), ff1['CLK'])
    draw_dot(ax, 11.8, ff0['CLK'][1]); draw_ortho(ax, (11.8, ff0['CLK'][1]), ff0['CLK'])

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_a5_q1_prime_counter.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_a5_q1_prime_counter.svg"))
    plt.close()
    print("Gen a5_q1")

def gen_a5_q2():
    """Assignment 5 - Q2: Toy Robot 4-State Machine (D Flip-Flops)"""
    fig, ax = plt.subplots(figsize=(11, 7), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(8.0, 9.4, "Toy Robot State Machine (D Flip-Flop Implementation)", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(8.0, 8.9, "Stand -> Walk -> Tumble -> Clap | Assignment 5 - Question 2", ha='center', fontsize=9.5, color="#64748b")

    # 2 D Flip-Flops
    ff1 = draw_flip_flop(ax, 10.5, 6.2, ff_type="D", name="FF 1 (MSB)")
    ff0 = draw_flip_flop(ax, 10.5, 2.2, ff_type="D", name="FF 0 (LSB)")

    # Input Button Switch X
    draw_ortho(ax, (1.0, 5.0), (3.0, 5.0), label="Switch X", label_pos=(1.8, 5.35))

    # Gates
    xor_0 = draw_xor(ax, 5.5, 2.9, label="XOR 0")
    draw_ortho(ax, xor_0['out'], ff0['D'], label=r"$D_0 = Q_0 \oplus X$", label_pos=(8.8, ff0['D'][1] + 0.35))

    and_en = draw_and(ax, 4.5, 6.9, label="AND\nQ0*X")
    xor_1  = draw_xor(ax, 7.5, 6.9, label="XOR 1")
    draw_ortho(ax, and_en['out'], xor_1['in2'])
    draw_ortho(ax, xor_1['out'], ff1['D'], label=r"$D_1 = Q_1 \oplus (Q_0 \cdot X)$", label_pos=(9.2, ff1['D'][1] + 0.45), fontsize=8)

    # Feedbacks
    draw_dot(ax, 3.0, 5.0)
    draw_path(ax, [(3.0, 5.0), (3.0, xor_0['in2'][1]), xor_0['in2']])
    draw_path(ax, [(3.0, 5.0), (3.0, and_en['in2'][1]), and_en['in2']])

    # Q0 feedback
    draw_ortho(ax, ff0['Q'], (13.5, ff0['Q'][1]))
    draw_dot(ax, 13.5, ff0['Q'][1])
    draw_path(ax, [(13.5, ff0['Q'][1]), (13.5, 1.0), (3.8, 1.0), (3.8, xor_0['in1'][1]), xor_0['in1']])
    draw_dot(ax, 3.8, 1.0)
    draw_path(ax, [(3.8, 1.0), (3.8, and_en['in1'][1]), and_en['in1']])
    draw_ortho(ax, (13.5, ff0['Q'][1]), (15.0, ff0['Q'][1]), label="Q0", label_pos=(14.5, ff0['Q'][1] + 0.35))

    # Q1 feedback
    draw_ortho(ax, ff1['Q'], (13.8, ff1['Q'][1]))
    draw_dot(ax, 13.8, ff1['Q'][1])
    draw_path(ax, [(13.8, ff1['Q'][1]), (13.8, 8.2), (7.0, 8.2), (7.0, xor_1['in1'][1]), xor_1['in1']])
    draw_ortho(ax, (13.8, ff1['Q'][1]), (15.0, ff1['Q'][1]), label="Q1", label_pos=(14.5, ff1['Q'][1] + 0.35))

    # Clock Bus
    draw_path(ax, [(9.5, 0.4), (9.5, ff1['CLK'][1]), ff1['CLK']], label="Clock", label_pos=(9.5, 0.1))
    draw_dot(ax, 9.5, ff0['CLK'][1]); draw_ortho(ax, (9.5, ff0['CLK'][1]), ff0['CLK'])

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_a5_q2_toy_robot_fsm.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_a5_q2_toy_robot_fsm.svg"))
    plt.close()
    print("Gen a5_q2")

def gen_a5_q3():
    """Assignment 5 - Q3: 4-Bit Serial-In Serial-Out (SISO) Shift Register"""
    fig, ax = plt.subplots(figsize=(14, 6.5), dpi=300)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 9)
    ax.axis('off')

    ax.text(9.0, 8.4, "4-Bit Serial-In Serial-Out (SISO) Shift Register", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(9.0, 7.9, "Assignment 5 - Question 3 | Shifts Right (Q3 -> Q2 -> Q1 -> Q0) on Each Clock Edge", ha='center', fontsize=9.5, color="#64748b")

    # 4 D Flip-Flops in Series
    ff3 = draw_flip_flop(ax, 2.5, 4.5, ff_type="D", name="FF 3 (MSB)")
    ff2 = draw_flip_flop(ax, 6.2, 4.5, ff_type="D", name="FF 2")
    ff1 = draw_flip_flop(ax, 9.9, 4.5, ff_type="D", name="FF 1")
    ff0 = draw_flip_flop(ax, 13.6, 4.5, ff_type="D", name="FF 0 (LSB)")

    # Serial In
    draw_ortho(ax, (0.8, ff3['D'][1]), ff3['D'], label="Serial Data In", label_pos=(1.5, ff3['D'][1] + 0.4), label_color="#1d4ed8")

    # Cascading Data Lines
    draw_ortho(ax, ff3['Q'], ff2['D'], label="Q3", label_pos=(5.3, ff3['Q'][1] + 0.35))
    draw_ortho(ax, ff2['Q'], ff1['D'], label="Q2", label_pos=(9.0, ff2['Q'][1] + 0.35))
    draw_ortho(ax, ff1['Q'], ff0['D'], label="Q1", label_pos=(12.7, ff1['Q'][1] + 0.35))
    draw_ortho(ax, ff0['Q'], (17.0, ff0['Q'][1]), label="Serial Out (Q0)", label_pos=(16.5, ff0['Q'][1] + 0.4), label_color="#15803d")

    # Common Shift Clock Line
    draw_ortho(ax, (1.0, 2.0), (14.0, 2.0))
    ax.text(0.9, 2.0, "Shift Clock", ha='right', va='center', fontsize=9.5, fontweight='bold', color="#0f172a")
    for ff in [ff3, ff2, ff1, ff0]:
        draw_path(ax, [(ff['CLK'][0] - 0.4, 2.0), (ff['CLK'][0] - 0.4, ff['CLK'][1]), ff['CLK']])
        draw_dot(ax, ff['CLK'][0] - 0.4, 2.0)

    # Execution Table Summary
    table_txt = "Trace starting at '1100' with serial inputs (1, 1, 0, 0, 1, 1) -> 6th pulse returns register to '1100' (12_10)"
    ax.text(9.0, 0.8, table_txt, ha='center', fontsize=9.5, fontweight='bold', color="#1e3a8a",
            bbox=dict(boxstyle='round,pad=0.4', fc='#eff6ff', ec='#93c5fd'))

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_a5_q3_siso_shift_register.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_a5_q3_siso_shift_register.svg"))
    plt.close()
    print("Gen a5_q3")

def gen_a5_q4():
    """Assignment 5 - Q4: 4-Bit Ring Counter with Frequency Division"""
    fig, ax = plt.subplots(figsize=(14, 7), dpi=300)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(9.0, 9.4, "4-Bit Ring Counter & Frequency Division Analysis", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(9.0, 8.9, "Assignment 5 - Question 4 | Circulating '1' Sequence: 1000 -> 0100 -> 0010 -> 0001 -> 1000", ha='center', fontsize=9.5, color="#64748b")

    # 4 D Flip-Flops in Ring
    ff3 = draw_flip_flop(ax, 2.5, 5.0, ff_type="D", name="FF 3 (Bit 3)")
    ff2 = draw_flip_flop(ax, 6.2, 5.0, ff_type="D", name="FF 2 (Bit 2)")
    ff1 = draw_flip_flop(ax, 9.9, 5.0, ff_type="D", name="FF 1 (Bit 1)")
    ff0 = draw_flip_flop(ax, 13.6, 5.0, ff_type="D", name="FF 0 (Bit 0)")

    # Forward Shift connections
    draw_ortho(ax, ff3['Q'], ff2['D'], label="Q3", label_pos=(5.3, ff3['Q'][1] + 0.35))
    draw_ortho(ax, ff2['Q'], ff1['D'], label="Q2", label_pos=(9.0, ff2['Q'][1] + 0.35))
    draw_ortho(ax, ff1['Q'], ff0['D'], label="Q1", label_pos=(12.7, ff1['Q'][1] + 0.35))

    # Ring Feedback: Q0 to D3 (Rectilinear)
    draw_path(ax, [ff0['Q'], (16.5, ff0['Q'][1]), (16.5, 7.8), (1.5, 7.8), (1.5, ff3['D'][1]), ff3['D']], color="#2563eb", lw=2)
    draw_dot(ax, 16.5, ff0['Q'][1], color="#2563eb")
    ax.text(9.0, 8.1, "Ring Feedback Path: Q0 connected to D3", color="#2563eb", fontsize=8.5, fontweight='bold', ha='center')

    # Common Clock
    draw_ortho(ax, (1.0, 2.5), (14.0, 2.5))
    ax.text(0.9, 2.5, "Clock (CLK)", ha='right', va='center', fontsize=9.5, fontweight='bold', color="#0f172a")
    for ff in [ff3, ff2, ff1, ff0]:
        draw_path(ax, [(ff['CLK'][0] - 0.4, 2.5), (ff['CLK'][0] - 0.4, ff['CLK'][1]), ff['CLK']])
        draw_dot(ax, ff['CLK'][0] - 0.4, 2.5)

    # Frequency Division Notes
    div_box = (
        "FREQUENCY DIVISION FORMULA: f_out = f_clk / N  (where N = 4 flip-flops)\n"
        "• At f_clk = 12 kHz:  f_out = 12 kHz / 4 = 3 kHz\n"
        "• At f_clk = 20 kHz:  f_out = 20 kHz / 4 = 5 kHz\n"
        "Duty Cycle = 1/N = 25% (HIGH for 1 clock cycle, LOW for 3 clock cycles)"
    )
    ax.text(9.0, 1.0, div_box, ha='center', fontsize=9, color="#1e3a8a",
            bbox=dict(boxstyle='round,pad=0.4', fc='#eff6ff', ec='#3b82f6', lw=1.2))

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_a5_q4_ring_counter.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_a5_q4_ring_counter.svg"))
    plt.close()
    print("Gen a5_q4")

def gen_a5_q5():
    """Assignment 5 - Q5: 1010 Mealy Sequence Detector Using T Flip-Flops"""
    fig, ax = plt.subplots(figsize=(15, 9.5), dpi=300)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 14)
    ax.axis('off')

    ax.text(10.0, 13.3, "1010 Overlapping Mealy Sequence Detector (T Flip-Flops)", ha='center', fontsize=13, fontweight='bold', color="#0f172a")
    ax.text(10.0, 12.8, "Assignment 5 - Question 5 | Complete IEEE Logic Gate Schematic with Synchronous Clock", ha='center', fontsize=9.5, color="#64748b")

    # 2 T Flip-Flops
    ffa = draw_flip_flop(ax, 13.5, 7.8, ff_type="T", name="FF A (MSB)")
    ffb = draw_flip_flop(ax, 13.5, 2.8, ff_type="T", name="FF B (LSB)")

    # Outputs
    draw_ortho(ax, ffa['Q'], (16.5, ffa['Q'][1]), label="State A", label_pos=(16.0, ffa['Q'][1] + 0.35))
    draw_ortho(ax, ffb['Q'], (16.5, ffb['Q'][1]), label="State B", label_pos=(16.0, ffb['Q'][1] + 0.35))

    # Signal Bus & Inverter
    # X input enters at (0.5, 10.4)
    draw_ortho(ax, (0.5, 10.4), (1.5, 10.4), label="Input X", label_pos=(1.0, 10.75))
    draw_dot(ax, 1.5, 10.4)
    # Bus line for X at x=1.5
    draw_ortho(ax, (1.5, 1.0), (1.5, 10.4), color="#94a3b8", lw=1.2)
    ax.text(1.5, 10.6, r"$X$", ha='center', fontsize=8.5, fontweight='bold', color="#1e293b")

    # Inverter for X'
    inv_x = draw_not(ax, 2.2, 10.4, label="NOT")
    draw_ortho(ax, (1.5, 10.4), inv_x['in'])
    # Bus line for X_bar at x=3.8
    draw_ortho(ax, inv_x['out'], (3.8, 10.4))
    draw_dot(ax, 3.8, 10.4)
    draw_ortho(ax, (3.8, 1.0), (3.8, 10.4), color="#94a3b8", lw=1.2)
    ax.text(3.8, 10.6, r"$\overline{X}$", ha='center', fontsize=8.5, fontweight='bold', color="#1e293b")

    # State A feedback bus at x=4.8
    # From ffa['Q'] tap at 15.6 up to 12.2, over to 4.8, down to 1.0
    draw_dot(ax, 15.6, ffa['Q'][1])
    draw_path(ax, [(15.6, ffa['Q'][1]), (15.6, 12.2), (4.8, 12.2), (4.8, 1.0)], color="#94a3b8", lw=1.2)
    ax.text(4.8, 10.6, r"$A$", ha='center', fontsize=8.5, fontweight='bold', color="#1e293b")

    # State B feedback bus at x=5.8
    # From ffb['Q'] tap at 16.0 up to 11.8, over to 5.8, down to 1.0
    draw_dot(ax, 16.0, ffb['Q'][1])
    draw_path(ax, [(16.0, ffb['Q'][1]), (16.0, 11.8), (5.8, 11.8), (5.8, 1.0)], color="#94a3b8", lw=1.2)
    ax.text(5.8, 10.6, r"$B$", ha='center', fontsize=8.5, fontweight='bold', color="#1e293b")

    ax.text(3.8, 11.2, "Signal Distribution Bus", ha='center', fontsize=9.5, fontweight='bold', color="#475569")

    # Combinational Logic for TB = B XOR X
    xor_tb = draw_xor(ax, 8.5, 3.0, label="XOR\nB (+) X")
    # Connect B (x=5.8) to in1, X (x=1.5) to in2
    draw_ortho(ax, (5.8, xor_tb['in1'][1]), xor_tb['in1']); draw_dot(ax, 5.8, xor_tb['in1'][1])
    draw_ortho(ax, (1.5, xor_tb['in2'][1]), xor_tb['in2']); draw_dot(ax, 1.5, xor_tb['in2'][1])
    draw_ortho(ax, xor_tb['out'], ffb['T'], label=r"$T_B$", label_pos=(11.5, ffb['T'][1] + 0.35))

    # Combinational Logic for TA = (A (+) B)*X' + A*B*X
    xor_ab  = draw_xor(ax, 7.2, 9.2, label="XOR\nA (+) B")
    # Connect A (x=4.8) to in1, B (x=5.8) to in2
    draw_ortho(ax, (4.8, xor_ab['in1'][1]), xor_ab['in1']); draw_dot(ax, 4.8, xor_ab['in1'][1])
    draw_ortho(ax, (5.8, xor_ab['in2'][1]), xor_ab['in2']); draw_dot(ax, 5.8, xor_ab['in2'][1])

    and_ta1 = draw_and(ax, 9.8, 9.0, label="AND\n(A(+)B)*X'")
    draw_ortho(ax, xor_ab['out'], and_ta1['in1'])
    # Connect X_bar (x=3.8) to in2
    draw_ortho(ax, (3.8, and_ta1['in2'][1]), and_ta1['in2']); draw_dot(ax, 3.8, and_ta1['in2'][1])

    and_ta2 = draw_and(ax, 9.8, 6.8, label="AND\nA*B*X")
    # Connect A (x=4.8), B (x=5.8), X (x=1.5)
    draw_ortho(ax, (4.8, and_ta2['in_3_top'][1]), and_ta2['in_3_top']); draw_dot(ax, 4.8, and_ta2['in_3_top'][1])
    draw_ortho(ax, (5.8, and_ta2['in_3_mid'][1]), and_ta2['in_3_mid']); draw_dot(ax, 5.8, and_ta2['in_3_mid'][1])
    draw_ortho(ax, (1.5, and_ta2['in_3_bot'][1]), and_ta2['in_3_bot']); draw_dot(ax, 1.5, and_ta2['in_3_bot'][1])

    or_ta   = draw_or(ax, 11.8, 7.8, label="OR\nTA")
    draw_ortho(ax, and_ta1['out'], or_ta['in1'], x_break=11.3)
    draw_ortho(ax, and_ta2['out'], or_ta['in2'], x_break=11.3)
    draw_ortho(ax, or_ta['out'], ffa['T'], label=r"$T_A$", label_pos=(13.0, ffa['T'][1] + 0.35))

    # Output Gate Z = A * B * X'
    and_z = draw_and(ax, 15.5, 5.5, label="AND\nA*B*X'")
    # in_3_top from State A (tap from QA line at x=15.0)
    draw_dot(ax, 15.0, ffa['Q'][1])
    draw_path(ax, [(15.0, ffa['Q'][1]), (15.0, and_z['in_3_top'][1]), and_z['in_3_top']])
    # in_3_mid from State B (tap from QB line at x=15.0)
    draw_dot(ax, 15.0, ffb['Q'][1])
    draw_path(ax, [(15.0, ffb['Q'][1]), (15.0, and_z['in_3_mid'][1]), and_z['in_3_mid']])
    # in_3_bot from X_bar (x=3.8)
    draw_dot(ax, 3.8, and_z['in_3_bot'][1])
    draw_ortho(ax, (3.8, and_z['in_3_bot'][1]), and_z['in_3_bot'])

    draw_ortho(ax, and_z['out'], (19.0, and_z['out'][1]), label="Output Z (MATCH!)", label_pos=(18.2, and_z['out'][1] + 0.4), label_color="#dc2626")

    # Common Clock Bus
    draw_path(ax, [(12.5, 0.4), (12.5, ffa['CLK'][1]), ffa['CLK']], label="Clock (CLK)", label_pos=(12.5, 0.1))
    draw_dot(ax, 12.5, ffb['CLK'][1]); draw_ortho(ax, (12.5, ffb['CLK'][1]), ffb['CLK'])

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_a5_q5_mealy_sequence_detector.png"), dpi=300)
    plt.savefig(os.path.join(OUT_DIR, "circuit_a5_q5_mealy_sequence_detector.svg"))
    plt.close()
    print("Gen a5_q5")

if __name__ == "__main__":
    gen_a4_q1()
    gen_a4_q2()
    gen_a4_q2_waveform()
    gen_a4_q3()
    gen_a4_q4()
    gen_a4_q5()
    gen_a5_q1()
    gen_a5_q2()
    gen_a5_q3()
    gen_a5_q4()
    gen_a5_q5()
    print("ALL CIRCUITS AND WAVEFORMS SUCCESSFULLY RE-RENDERED WITH PERFECT QUALITY!")
