"""
Render specialized exam paper schematics and diagrams for DLD CAT-2 Foolproof Booklet:
1. Paper 1 Q1: Reverse D-to-JK Flip-Flop Conversion Schematic
2. Paper 1 Q1: JK Flip-Flop State Transition Diagram
3. Paper 1 Q2: Medical Monitoring Device State Diagram (Standby -> Monitoring -> Warning -> Shutdown)
4. Paper 1 Q3: Digital Locker 4-Bit Shift Register (SIPO) Schematic with Pulse Trace
5. Paper 1 Q4: MOD-10 Synchronous BCD Counter State Diagram with Lockout Recovery
6. Paper 1 Q4: MOD-10 Synchronous Counter Schematic (T Flip-Flops)
7. Paper 1 Q5: 101 Overlapping Mealy Sequence Detector State Diagram
8. Paper 2 Q1: 8-State Diagram (Original states a through h)
9. Paper 2 Q1: 5-State Reduced Diagram (States A through E)
10. Paper 2 Q2: T Flip-Flop Sequential Circuit Schematic
11. Paper 2 Q3: Asynchronous Decade Counter Multi-Channel Timing Diagram (Waveforms)
12. Paper 2 Q4: MOD-8 Johnson Counter State Diagram & Logic Schematic
13. Paper 2 Q5: 1001 Overlapping Mealy Sequence Detector State Diagram & D FF Schematic
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
import numpy as np
import os

OUT_DIR = r"c:\Users\ankit\Fall2627\DLD\notes\cat2\circuits"
os.makedirs(OUT_DIR, exist_ok=True)

BG_COLOR = "#ffffff"

def draw_state_node(ax, xy, r, title, subtitle="", fc="#eff6ff", ec="#2563eb", title_color="#0f172a", sub_color="#475569"):
    circle = patches.Circle(xy, r, facecolor=fc, edgecolor=ec, linewidth=2.2, zorder=4)
    ax.add_patch(circle)
    if subtitle:
        ax.text(xy[0], xy[1] + 0.12, title, fontsize=11, fontweight="bold", color=title_color, ha="center", va="center", zorder=5)
        ax.text(xy[0], xy[1] - 0.22, subtitle, fontsize=8.5, fontweight="bold", color=sub_color, ha="center", va="center", zorder=5)
    else:
        ax.text(xy[0], xy[1], title, fontsize=11.5, fontweight="bold", color=title_color, ha="center", va="center", zorder=5)

def draw_curved_arrow(ax, p1, p2, rad=0.2, color="#2563eb", lw=1.8, label="", label_pos=None, label_color="#0f172a", fontsize=9.2, is_dashed=False):
    ls = "-" if not is_dashed else "--"
    arrow = FancyArrowPatch(p1, p2, connectionstyle=f"arc3,rad={rad}", arrowstyle="-|>", mutation_scale=13, color=color, linewidth=lw, linestyle=ls, zorder=3)
    ax.add_patch(arrow)
    if label:
        if label_pos is not None:
            lx, ly = label_pos
        else:
            x1, y1 = p1
            x2, y2 = p2
            xm, ym = (x1 + x2) / 2.0, (y1 + y2) / 2.0
            dx, dy = x2 - x1, y2 - y1
            dist = np.hypot(dx, dy)
            if dist > 1e-4:
                nx, ny = -dy / dist, dx / dist
                arc_offset = rad * (dist * 0.45)
                lx = xm + nx * arc_offset
                ly = ym + ny * arc_offset
            else:
                lx, ly = xm, ym
        ax.text(lx, ly, label, fontsize=fontsize, fontweight="bold", color=label_color, ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=color, lw=1.0, alpha=0.96), zorder=6)

def draw_self_loop(ax, center, r, direction="top", color="#2563eb", lw=1.8, label="", label_color="#0f172a", fontsize=9.2):
    cx, cy = center
    if direction == "top":
        start = (cx - r * 0.5, cy + r * 0.866)
        end = (cx + r * 0.5, cy + r * 0.866)
        rad = -1.2
        label_pos = (cx, cy + r + 0.55)
    elif direction == "bottom":
        start = (cx + r * 0.5, cy - r * 0.866)
        end = (cx - r * 0.5, cy - r * 0.866)
        rad = -1.2
        label_pos = (cx, cy - r - 0.55)
    elif direction == "left":
        start = (cx - r * 0.866, cy - r * 0.5)
        end = (cx - r * 0.866, cy + r * 0.5)
        rad = -1.2
        label_pos = (cx - r - 0.65, cy)
    else:
        start = (cx + r * 0.866, cy + r * 0.5)
        end = (cx + r * 0.866, cy - r * 0.5)
        rad = -1.2
        label_pos = (cx + r + 0.65, cy)
    arrow = FancyArrowPatch(start, end, connectionstyle=f"arc3,rad={rad}", arrowstyle="-|>", mutation_scale=13, color=color, linewidth=lw, zorder=3)
    ax.add_patch(arrow)
    if label:
        ax.text(label_pos[0], label_pos[1], label, fontsize=fontsize, fontweight="bold", color=label_color, ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.18", fc="white", ec=color, lw=1.0, alpha=0.96), zorder=6)

# ==============================================================================
# 1. Paper 1 Q1: Reverse D-to-JK Flip-Flop Conversion Schematic
# ==============================================================================
def render_paper1_q1_reverse_conversion():
    fig, ax = plt.subplots(figsize=(8.5, 4.2), dpi=300)
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.8, 5.2)
    ax.axis("off")

    # D Flip-Flop Box
    ff_box = patches.Rectangle((6.2, 1.2), 2.2, 2.8, facecolor="#eff6ff", edgecolor="#1e3a8a", linewidth=2.0)
    ax.add_patch(ff_box)
    ax.text(7.3, 3.2, "D-FF", fontsize=11, fontweight="bold", color="#1e3a8a", ha="center")
    ax.text(6.4, 2.6, "D", fontsize=10, fontweight="bold", color="#0f172a", va="center")
    ax.text(8.2, 3.4, "Q", fontsize=10, fontweight="bold", color="#0f172a", ha="right", va="center")
    ax.text(8.2, 1.8, "Q'", fontsize=10, fontweight="bold", color="#0f172a", ha="right", va="center")

    # CLK triangle
    clk_poly = patches.Polygon([[6.2, 1.4], [6.5, 1.55], [6.2, 1.7]], closed=True, facecolor="none", edgecolor="#1e3a8a", lw=1.5)
    ax.add_patch(clk_poly)
    ax.plot([5.2, 6.2], [1.55, 1.55], color="#1e293b", lw=1.8)
    ax.text(5.1, 1.55, "CLK", fontsize=8.5, fontweight="bold", color="#475569", ha="right", va="center")

    # Top AND gate y1
    top_and = patches.Rectangle((2.2, 3.2), 1.2, 1.2, facecolor="#f8fafc", edgecolor="#1e293b", lw=1.8)
    ax.add_patch(top_and)
    ax.text(2.8, 3.8, "AND", fontsize=8.5, fontweight="bold", color="#334155", ha="center", va="center")

    # Bottom AND gate y2
    bot_and = patches.Rectangle((2.2, 1.0), 1.2, 1.2, facecolor="#f8fafc", edgecolor="#1e293b", lw=1.8)
    ax.add_patch(bot_and)
    ax.text(2.8, 1.6, "AND", fontsize=8.5, fontweight="bold", color="#334155", ha="center", va="center")

    # Inverter on K input
    inv_tri = patches.Polygon([[1.0, 1.6], [1.5, 1.85], [1.0, 2.1]], closed=True, facecolor="#f8fafc", edgecolor="#1e293b", lw=1.5)
    ax.add_patch(inv_tri)
    inv_bub = patches.Circle((1.58, 1.85), 0.08, facecolor="white", edgecolor="#1e293b", lw=1.5)
    ax.add_patch(inv_bub)
    ax.plot([0.3, 1.0], [1.85, 1.85], color="#1e293b", lw=1.8)
    ax.plot([1.66, 2.2], [1.85, 1.85], color="#1e293b", lw=1.8)
    ax.text(0.2, 1.85, "K", fontsize=10, fontweight="bold", color="#0f172a", ha="right", va="center")

    # J input
    ax.plot([0.3, 2.2], [4.1, 4.1], color="#1e293b", lw=1.8)
    ax.text(0.2, 4.1, "J", fontsize=10, fontweight="bold", color="#0f172a", ha="right", va="center")

    # OR gate y3
    or_gate = patches.Rectangle((4.4, 2.0), 1.2, 1.2, facecolor="#f8fafc", edgecolor="#1e293b", lw=1.8)
    ax.add_patch(or_gate)
    ax.text(5.0, 2.6, "OR", fontsize=8.5, fontweight="bold", color="#334155", ha="center", va="center")

    # Wires from AND gates to OR gate
    ax.plot([3.4, 3.9, 3.9, 4.4], [3.8, 3.8, 2.9, 2.9], color="#1e293b", lw=1.8)
    ax.text(3.7, 4.05, "y1 = J·Q'", fontsize=8.5, fontweight="bold", color="#2563eb", ha="center")
    ax.plot([3.4, 3.9, 3.9, 4.4], [1.6, 1.6, 2.3, 2.3], color="#1e293b", lw=1.8)
    ax.text(3.7, 1.35, "y2 = K'·Q", fontsize=8.5, fontweight="bold", color="#2563eb", ha="center")

    # OR to D input
    ax.plot([5.6, 6.2], [2.6, 2.6], color="#1e293b", lw=2.0)
    ax.text(5.9, 2.85, "y3 = D", fontsize=8.5, fontweight="bold", color="#059669", ha="center")

    # Feedback wires
    # Q output feedback to bottom AND gate
    ax.plot([8.4, 9.3, 9.3, 1.8, 1.8, 2.2], [3.4, 3.4, 4.8, 4.8, 1.3, 1.3], color="#1e293b", lw=1.6)
    ax.plot([8.4, 9.8], [3.4, 3.4], color="#1e293b", lw=2.0)
    ax.text(10.0, 3.4, "Q", fontsize=10, fontweight="bold", color="#0f172a", va="center")

    # Q' output feedback to top AND gate
    ax.plot([8.4, 9.0, 9.0, 1.9, 1.9, 2.2], [1.8, 1.8, 0.4, 0.4, 3.5, 3.5], color="#1e293b", lw=1.6)
    ax.plot([8.4, 9.8], [1.8, 1.8], color="#1e293b", lw=2.0)
    ax.text(10.0, 1.8, "Q'", fontsize=10, fontweight="bold", color="#0f172a", va="center")

    # Dots
    ax.plot([9.3], [3.4], 'o', color="#1e293b", markersize=5)
    ax.plot([9.0], [1.8], 'o', color="#1e293b", markersize=5)

    ax.text(5.0, 5.0, "Identified Flip-Flop Conversion: D Flip-Flop Converted to JK Flip-Flop", fontsize=11.5, fontweight="bold", color="#1e3a8a", ha="center")
    ax.text(5.0, -0.5, "Equation: D = y3 = y1 + y2 = J·Q' + K'·Q = Characteristic Equation of JK Flip-Flop", fontsize=9.0, color="#475569", ha="center")

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "circuit_paper1_q1_d_to_jk.png"), dpi=300, facecolor=BG_COLOR)
    plt.close()
    print("Rendered circuit_paper1_q1_d_to_jk.png")

# ==============================================================================
# 2. Paper 1 Q2: Medical Monitoring Device State Diagram
# ==============================================================================
def render_medical_device_state_diagram():
    fig, ax = plt.subplots(figsize=(8.8, 5.8), dpi=300)
    ax.set_xlim(-1.2, 9.8)
    ax.set_ylim(-1.0, 6.2)
    ax.axis("off")

    r = 0.72
    coords = {
        "A": (1.8, 4.4),  # Standby (00)
        "B": (6.6, 4.4),  # Monitoring (01)
        "C": (6.6, 1.2),  # Warning (11)
        "D": (1.8, 1.2),  # Emergency Shutdown (10)
    }

    draw_state_node(ax, coords["A"], r, "A (00)", "Standby", fc="#f8fafc", ec="#475569")
    draw_state_node(ax, coords["B"], r, "B (01)", "Monitoring", fc="#eff6ff", ec="#2563eb")
    draw_state_node(ax, coords["C"], r, "C (11)", "Warning", fc="#fef3c7", ec="#d97706")
    draw_state_node(ax, coords["D"], r, "D (10)", "Shutdown", fc="#fef2f2", ec="#dc2626")

    # A -> A (self loop X=0)
    draw_self_loop(ax, coords["A"], r, direction="left", color="#475569", label="X = 0")
    # A -> B (X=1)
    p1 = (coords["A"][0] + r, coords["A"][1] + 0.15)
    p2 = (coords["B"][0] - r, coords["B"][1] + 0.15)
    draw_curved_arrow(ax, p1, p2, rad=-0.12, color="#2563eb", lw=2.0, label="X = 1 (Activate)", label_pos=(4.2, 4.9))

    # B -> B (self loop X=0 normal)
    draw_self_loop(ax, coords["B"], r, direction="top", color="#2563eb", label="X = 0 (Normal)")
    # B -> C (X=1 anomaly)
    p1 = (coords["B"][0] + 0.15, coords["B"][1] - r)
    p2 = (coords["C"][0] + 0.15, coords["C"][1] + r)
    draw_curved_arrow(ax, p1, p2, rad=-0.12, color="#d97706", lw=2.0, label="X = 1 (Vitals Alert)", label_pos=(7.7, 2.8))

    # C -> B (X=0 recovered)
    p1 = (coords["C"][0] - 0.2, coords["C"][1] + r)
    p2 = (coords["B"][0] - 0.2, coords["B"][1] - r)
    draw_curved_arrow(ax, p1, p2, rad=-0.12, color="#059669", lw=2.0, label="X = 0 (Recovered)", label_pos=(5.5, 2.8))
    # C -> D (X=1 critical)
    p1 = (coords["C"][0] - r, coords["C"][1] - 0.15)
    p2 = (coords["D"][0] + r, coords["D"][1] - 0.15)
    draw_curved_arrow(ax, p1, p2, rad=-0.12, color="#dc2626", lw=2.2, label="X = 1 (Critical Failure)", label_pos=(4.2, 0.7))

    # D -> D (Latch shutdown)
    draw_self_loop(ax, coords["D"], r, direction="left", color="#dc2626", label="X = 0, 1 (Locked)")

    ax.text(4.2, 5.8, "Medical Monitoring Device — Synchronous FSM State Diagram", fontsize=12.5, fontweight="bold", color="#0f172a", ha="center")
    ax.text(4.2, -0.7, "Gray Code Assignment (00 → 01 → 11 → 10) prevents hazardous glitches in medical telemetry", fontsize=8.8, color="#475569", ha="center")

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "state_diag_medical_device_fsm.png"), dpi=300, facecolor=BG_COLOR)
    plt.close()
    print("Rendered state_diag_medical_device_fsm.png")

# ==============================================================================
# 3. Paper 1 Q4: MOD-10 Synchronous BCD Counter State Diagram
# ==============================================================================
def render_mod10_sync_state_diagram():
    fig, ax = plt.subplots(figsize=(9.2, 6.2), dpi=300)
    ax.set_xlim(-1.2, 9.8)
    ax.set_ylim(-1.2, 6.8)
    ax.axis("off")

    r = 0.52
    # 10 states in an ellipse/oval
    theta = np.linspace(0, 2*np.pi, 10, endpoint=False)
    # Arrange clockwise starting from 0 at top
    theta = np.pi/2 - theta
    cx, cy = 4.3, 3.2
    rx, ry = 3.6, 2.4

    coords = {}
    names = ["0 (0000)", "1 (0001)", "2 (0010)", "3 (0011)", "4 (0100)", "5 (0101)", "6 (0110)", "7 (0111)", "8 (1000)", "9 (1001)"]
    for i in range(10):
        x = cx + rx * np.cos(theta[i])
        y = cy + ry * np.sin(theta[i])
        coords[i] = (x, y)
        draw_state_node(ax, (x, y), r, str(i), names[i].split()[1], fc="#ecfdf5", ec="#059669")

    # Connect cycle 0 -> 1 -> ... -> 9 -> 0
    for i in range(10):
        nxt = (i + 1) % 10
        p1 = coords[i]
        p2 = coords[nxt]
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        dist = np.hypot(dx, dy)
        ux, uy = dx / dist, dy / dist
        start = (p1[0] + r * ux, p1[1] + r * uy)
        end = (p2[0] - r * ux, p2[1] - r * uy)
        draw_curved_arrow(ax, start, end, rad=-0.08, color="#059669", lw=2.0)

    # Center lockout box
    ax.text(cx, cy, "MOD-10 (BCD)\nCount 0 to 9\nResets to 0 on 10th Pulse\n(States 10-15 Recover to 0)",
            fontsize=8.5, fontweight="bold", color="#065f46", ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.35", fc="#d1fae5", ec="#059669", lw=1.2))

    ax.text(cx, 6.3, "MOD-10 Synchronous Decade Counter — State Transition Cycle", fontsize=12.5, fontweight="bold", color="#0f172a", ha="center")

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "state_diag_mod10_sync_counter.png"), dpi=300, facecolor=BG_COLOR)
    plt.close()
    print("Rendered state_diag_mod10_sync_counter.png")

# ==============================================================================
# 4. Paper 1 Q5: 101 Overlapping Mealy Sequence Detector State Diagram
# ==============================================================================
def render_sequence_101_state_diagram():
    fig, ax = plt.subplots(figsize=(8.8, 4.4), dpi=300)
    ax.set_xlim(-1.2, 9.8)
    ax.set_ylim(-1.8, 4.4)
    ax.axis("off")

    r = 0.65
    coords = {
        "S0": (1.4, 1.4),  # Reset (00)
        "S1": (4.5, 1.4),  # Got '1' (01)
        "S2": (7.6, 1.4),  # Got '10' (10)
    }

    # Reset arrow
    ax.annotate("RESET", xy=(coords["S0"][0] - r, coords["S0"][1]), xytext=(coords["S0"][0] - r - 1.0, coords["S0"][1]),
                arrowprops=dict(facecolor="#475569", edgecolor="#475569", width=2.0, headwidth=7),
                fontsize=9, fontweight="bold", color="#334155", va="center", ha="right")

    draw_state_node(ax, coords["S0"], r, "S0", "00 (Reset)", fc="#f8fafc", ec="#475569")
    draw_state_node(ax, coords["S1"], r, "S1", "01 ('1')", fc="#eff6ff", ec="#2563eb")
    draw_state_node(ax, coords["S2"], r, "S2", "10 ('10')", fc="#fef3c7", ec="#d97706")

    # S0: X=0 -> S0
    draw_self_loop(ax, coords["S0"], r, direction="left", color="#475569", label="0 / 0")
    # S0: X=1 -> S1
    p1 = (coords["S0"][0] + r * 0.7, coords["S0"][1] + r * 0.7)
    p2 = (coords["S1"][0] - r * 0.7, coords["S1"][1] + r * 0.7)
    draw_curved_arrow(ax, p1, p2, rad=-0.28, color="#2563eb", label="1 / 0", label_pos=(2.95, 2.4))

    # S1: X=1 -> S1 (self loop)
    draw_self_loop(ax, coords["S1"], r, direction="top", color="#2563eb", label="1 / 0")
    # S1: X=0 -> S2
    p1 = (coords["S1"][0] + r * 0.7, coords["S1"][1] + r * 0.7)
    p2 = (coords["S2"][0] - r * 0.7, coords["S2"][1] + r * 0.7)
    draw_curved_arrow(ax, p1, p2, rad=-0.28, color="#2563eb", label="0 / 0", label_pos=(6.05, 2.4))

    # S2: X=0 -> S0 (reset)
    p1 = (coords["S2"][0] - r * 0.5, coords["S2"][1] - r * 0.866)
    p2 = (coords["S0"][0] + r * 0.5, coords["S0"][1] - r * 0.866)
    draw_curved_arrow(ax, p1, p2, rad=-0.38, color="#64748b", label="0 / 0 (to Reset)", label_pos=(4.5, -0.2))

    # S2: X=1 -> S1 (Overlapping detection! Z = 1!)
    p1 = (coords["S2"][0] - r * 0.8, coords["S2"][1] - r * 0.5)
    p2 = (coords["S1"][0] + r * 0.8, coords["S1"][1] - r * 0.5)
    draw_curved_arrow(ax, p1, p2, rad=-0.32, color="#059669", lw=2.4, label="1 / 1  ★ MATCH!", label_pos=(6.05, 0.2), label_color="#065f46")

    ax.text(4.5, 3.9, "Sequence Detector '101' — Mealy State Diagram", fontsize=13, fontweight="bold", color="#0f172a", ha="center")
    ax.text(4.5, 3.45, "Overlapping detection: On S2, Input X=1 produces Output Z=1 and loops to S1 (suffix '1')", fontsize=8.8, color="#475569", ha="center")

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "state_diag_sequence_101.png"), dpi=300, facecolor=BG_COLOR)
    plt.close()
    print("Rendered state_diag_sequence_101.png")

# ==============================================================================
# 5. Paper 2 Q1: 8-State Diagram & 5-State Reduced Diagram
# ==============================================================================
def render_8state_and_reduced_diagram():
    # Reduced 5-state diagram
    fig, ax = plt.subplots(figsize=(8.8, 5.6), dpi=300)
    ax.set_xlim(-1.2, 9.8)
    ax.set_ylim(-1.0, 6.2)
    ax.axis("off")

    r = 0.65
    coords = {
        "A": (1.8, 4.4),   # S0 = (a, c)
        "B": (6.6, 4.4),   # S1 = (b, e)
        "F": (4.2, 2.6),   # S3 = (f)
        "D": (1.8, 0.8),   # S2 = (d, h)
        "G": (6.6, 0.8),   # S4 = (g)
    }

    draw_state_node(ax, coords["A"], r, "S0", "(a, c)", fc="#eff6ff", ec="#2563eb")
    draw_state_node(ax, coords["B"], r, "S1", "(b, e)", fc="#eff6ff", ec="#2563eb")
    draw_state_node(ax, coords["F"], r, "S3", "(f)", fc="#fef3c7", ec="#d97706")
    draw_state_node(ax, coords["D"], r, "S2", "(d, h)", fc="#eff6ff", ec="#2563eb")
    draw_state_node(ax, coords["G"], r, "S4", "(g)", fc="#eff6ff", ec="#2563eb")

    # Transitions
    # S0: x=0 -> S3 (0), x=1 -> S1 (0)
    p1 = (coords["A"][0] + r * 0.7, coords["A"][1] - r * 0.7)
    p2 = (coords["F"][0] - r * 0.7, coords["F"][1] + r * 0.7)
    draw_curved_arrow(ax, p1, p2, rad=-0.1, color="#2563eb", label="0 / 0")

    p1 = (coords["A"][0] + r, coords["A"][1])
    p2 = (coords["B"][0] - r, coords["B"][1])
    draw_curved_arrow(ax, p1, p2, rad=-0.15, color="#2563eb", label="1 / 0")

    # S1: x=0 -> S2 (0), x=1 -> S0 (0)
    p1 = (coords["B"][0] - r * 0.7, coords["B"][1] - r * 0.7)
    p2 = (coords["D"][0] + r * 0.7, coords["D"][1] + r * 0.7)
    draw_curved_arrow(ax, p1, p2, rad=0.1, color="#2563eb", label="0 / 0", label_pos=(3.8, 1.8))

    p1 = (coords["B"][0] - r, coords["B"][1] + 0.1)
    p2 = (coords["A"][0] + r, coords["A"][1] + 0.1)
    draw_curved_arrow(ax, p1, p2, rad=-0.15, color="#2563eb", label="1 / 0", label_pos=(4.2, 5.2))

    # S2: x=0 -> S4 (1), x=1 -> S0 (0)
    p1 = (coords["D"][0] + r, coords["D"][1])
    p2 = (coords["G"][0] - r, coords["G"][1])
    draw_curved_arrow(ax, p1, p2, rad=-0.12, color="#059669", label="0 / 1", label_pos=(4.2, 0.4))

    p1 = (coords["D"][0], coords["D"][1] + r)
    p2 = (coords["A"][0], coords["A"][1] - r)
    draw_curved_arrow(ax, p1, p2, rad=-0.12, color="#2563eb", label="1 / 0", label_pos=(1.2, 2.6))

    # S3 (f): x=0 -> S3 (1), x=1 -> S1 (1)
    draw_self_loop(ax, coords["F"], r, direction="left", color="#d97706", label="0 / 1")
    p1 = (coords["F"][0] + r * 0.7, coords["F"][1] + r * 0.7)
    p2 = (coords["B"][0] - r * 0.7, coords["B"][1] - r * 0.7)
    draw_curved_arrow(ax, p1, p2, rad=-0.1, color="#d97706", label="1 / 1")

    # S4 (g): x=0 -> S4 (0), x=1 -> S2 (1)
    draw_self_loop(ax, coords["G"], r, direction="right", color="#2563eb", label="0 / 0")
    p1 = (coords["G"][0] - r, coords["G"][1] + 0.15)
    p2 = (coords["D"][0] + r, coords["D"][1] + 0.15)
    draw_curved_arrow(ax, p1, p2, rad=-0.15, color="#059669", label="1 / 1", label_pos=(4.2, 1.2))

    ax.text(4.2, 5.9, "Reduced State Diagram (5 Equivalent States from 8 States)", fontsize=13, fontweight="bold", color="#0f172a", ha="center")
    ax.text(4.2, -0.65, "Equivalence Partitions: S0={a, c}, S1={b, e}, S2={d, h}, S3={f}, S4={g} | Reduced via Row Matching", fontsize=8.8, color="#475569", ha="center")

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "state_diag_8state_reduced.png"), dpi=300, facecolor=BG_COLOR)
    plt.close()
    print("Rendered state_diag_8state_reduced.png")

# ==============================================================================
# 6. Paper 2 Q3: Asynchronous Decade Up-Counter Timing Diagram
# ==============================================================================
def render_asynch_decade_timing_diagram():
    fig, ax = plt.subplots(figsize=(10.5, 5.5), dpi=300)
    ax.set_xlim(-0.5, 23.5)
    ax.set_ylim(-0.8, 5.8)
    ax.axis("off")

    # Signal names
    signals = ["CLK", "Q0 (LSB)", "Q1", "Q2", "Q3 (MSB)", "CLR' (NAND)"]
    y_bases = [4.8, 3.8, 2.8, 1.8, 0.8, -0.2]

    # Draw clock pulses: 11 cycles (0 to 10)
    # Each cycle width = 2 units
    t = np.linspace(0, 22, 1000)

    for i, name in enumerate(signals):
        ax.text(-0.3, y_bases[i] + 0.3, name, fontsize=9.5, fontweight="bold", color="#1e3a8a", ha="right", va="center")

    # 1. Clock line (Square wave, active low falling edges)
    clk_x = []
    clk_y = []
    for c in range(11):
        x0 = c * 2.0
        clk_x.extend([x0, x0 + 1.0, x0 + 1.0, x0 + 2.0])
        clk_y.extend([y_bases[0] + 0.6, y_bases[0] + 0.6, y_bases[0], y_bases[0]])
    ax.plot(clk_x, clk_y, color="#1e293b", lw=1.8)

    # Label clock numbers 0 to 10
    for c in range(11):
        ax.text(c * 2.0 + 1.0, y_bases[0] + 0.8, f"P{c+1}", fontsize=8.0, fontweight="bold", color="#64748b", ha="center")

    # 2. Q0: Toggles on every falling edge of CLK (at x = 2, 4, 6, ...)
    q0_x = [0]
    q0_y = [y_bases[1]]
    val = 0
    for c in range(1, 12):
        x = c * 2.0
        q0_x.extend([x, x])
        val = 1 - val
        q0_y.extend([y_bases[1] + (1 - val) * 0.6, y_bases[1] + val * 0.6])
    ax.plot(q0_x, q0_y, color="#2563eb", lw=2.0)

    # 3. Q1: Toggles on falling edge of Q0 (when Q0 goes 1 -> 0, at x = 4, 8, 12, 16, 20)
    # At pulse 10 (x=20), Q1 goes HIGH, then resets immediately!
    q1_x = [0, 4, 4, 8, 8, 12, 12, 16, 16, 20, 20, 20.3, 20.3, 22]
    q1_y = [0, 0, 1, 1, 0,  0,  1,  1,  0,  0,  1,   1,    0,    0]
    q1_y = [y_bases[2] + v * 0.6 for v in q1_y]
    ax.plot(q1_x, q1_y, color="#2563eb", lw=2.0)

    # 4. Q2: Toggles on falling edge of Q1 (at x = 8, 16)
    q2_x = [0, 8, 8, 16, 16, 22]
    q2_y = [0, 0, 1,  1,  0,  0]
    q2_y = [y_bases[3] + v * 0.6 for v in q2_y]
    ax.plot(q2_x, q2_y, color="#2563eb", lw=2.0)

    # 5. Q3: Toggles on falling edge of Q2 (at x = 16). At pulse 10 (x=20), resets with Q1!
    q3_x = [0, 16, 16, 20.3, 20.3, 22]
    q3_y = [0,  0,  1,    1,    0,  0]
    q3_y = [y_bases[4] + v * 0.6 for v in q3_y]
    ax.plot(q3_x, q3_y, color="#2563eb", lw=2.0)

    # 6. CLR' NAND output: Normally HIGH (1), dips LOW at count 10 (x=20 to 20.3)
    clr_x = [0, 20, 20, 20.3, 20.3, 22]
    clr_y = [1,  1,  0,    0,    1,  1]
    clr_y = [y_bases[5] + v * 0.6 for v in clr_y]
    ax.plot(clr_x, clr_y, color="#dc2626", lw=2.2)

    # Callout arrow for reset glitch
    ax.annotate("Reset Glitch (Q3·Q1 = 1010₂)\nClears all FFs back to 0000₂",
                xy=(20.15, y_bases[5] + 0.1), xytext=(17.5, y_bases[5] - 0.4),
                arrowprops=dict(facecolor="#dc2626", edgecolor="#dc2626", width=1.5, headwidth=6),
                fontsize=8.5, fontweight="bold", color="#991b1b")

    # Annotate Decimal Counts 0 to 9 under waveforms
    counts = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0 (Reset)"]
    for c in range(11):
        ax.text(c * 2.0 + 1.0, 5.5, f"Count {counts[c]}", fontsize=8.0, fontweight="bold", color="#059669", ha="center",
                bbox=dict(boxstyle="square,pad=0.15", fc="#ecfdf5", ec="#a7f3d0", lw=0.8))

    ax.text(11.0, 5.8, "Asynchronous (Ripple) Decade Counter — Complete Timing Diagram", fontsize=12, fontweight="bold", color="#0f172a", ha="center")

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "timing_diag_asynch_decade_counter.png"), dpi=300, facecolor=BG_COLOR)
    plt.close()
    print("Rendered timing_diag_asynch_decade_counter.png")

# ==============================================================================
# 7. Paper 2 Q4: MOD-8 Johnson Counter State Diagram
# ==============================================================================
def render_mod8_johnson_state_diagram():
    fig, ax = plt.subplots(figsize=(8.8, 5.8), dpi=300)
    ax.set_xlim(-1.2, 9.8)
    ax.set_ylim(-1.0, 6.2)
    ax.axis("off")

    r = 0.58
    theta = np.linspace(0, 2*np.pi, 8, endpoint=False)
    theta = np.pi/2 - theta
    cx, cy = 4.3, 2.6
    rx, ry = 3.4, 2.1

    states = ["0000 (0)", "1000 (8)", "1100 (12)", "1110 (14)", "1111 (15)", "0111 (7)", "0011 (3)", "0001 (1)"]
    coords = {}
    for i in range(8):
        x = cx + rx * np.cos(theta[i])
        y = cy + ry * np.sin(theta[i])
        coords[i] = (x, y)
        draw_state_node(ax, (x, y), r, states[i].split()[0], f"State {i}", fc="#eff6ff", ec="#2563eb")

    # Connect cycle 0 -> 1 -> ... -> 7 -> 0
    for i in range(8):
        nxt = (i + 1) % 8
        p1 = coords[i]
        p2 = coords[nxt]
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        dist = np.hypot(dx, dy)
        ux, uy = dx / dist, dy / dist
        start = (p1[0] + r * ux, p1[1] + r * uy)
        end = (p2[0] - r * ux, p2[1] - r * uy)
        draw_curved_arrow(ax, start, end, rad=-0.08, color="#2563eb", lw=2.0, label="CLK" if i == 0 else "")

    ax.text(cx, cy, "MOD-8 Johnson Counter\n4 D Flip-Flops (D3 = Q0')\n8 Valid States | fout = fclk / 8\n(8 Unused States Lockout)",
            fontsize=8.5, fontweight="bold", color="#1e3a8a", ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.35", fc="#eff6ff", ec="#2563eb", lw=1.2))

    ax.text(cx, 5.7, "MOD-8 Johnson (Twisted Ring) Counter — State Diagram", fontsize=12.5, fontweight="bold", color="#0f172a", ha="center")

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "state_diag_mod8_johnson.png"), dpi=300, facecolor=BG_COLOR)
    plt.close()
    print("Rendered state_diag_mod8_johnson.png")

# ==============================================================================
# 8. Paper 2 Q5: 1001 Mealy Sequence Detector State Diagram
# ==============================================================================
def render_sequence_1001_state_diagram():
    fig, ax = plt.subplots(figsize=(10.5, 4.4), dpi=300)
    ax.set_xlim(-1.2, 12.8)
    ax.set_ylim(-2.0, 4.4)
    ax.axis("off")

    r = 0.65
    coords = {
        "S0": (1.4, 1.4),   # Reset (00)
        "S1": (4.4, 1.4),   # Got '1' (01)
        "S2": (7.4, 1.4),   # Got '10' (10)
        "S3": (10.4, 1.4),  # Got '100' (11)
    }

    # Reset arrow (top-left diagonal entry)
    ax.annotate("RESET", xy=(coords["S0"][0] - r * 0.707, coords["S0"][1] + r * 0.707),
                xytext=(coords["S0"][0] - r * 0.707 - 0.9, coords["S0"][1] + r * 0.707 + 0.7),
                arrowprops=dict(facecolor="#475569", edgecolor="#475569", width=2.0, headwidth=7),
                fontsize=9, fontweight="bold", color="#334155", va="bottom", ha="right")

    draw_state_node(ax, coords["S0"], r, "S0", "00 (Reset)", fc="#f8fafc", ec="#475569")
    draw_state_node(ax, coords["S1"], r, "S1", "01 ('1')", fc="#eff6ff", ec="#2563eb")
    draw_state_node(ax, coords["S2"], r, "S2", "10 ('10')", fc="#eff6ff", ec="#2563eb")
    draw_state_node(ax, coords["S3"], r, "S3", "11 ('100')", fc="#fef3c7", ec="#d97706")

    # S0: X=0 -> S0
    draw_self_loop(ax, coords["S0"], r, direction="left", color="#475569", label="0 / 0")
    # S0: X=1 -> S1
    p1 = (coords["S0"][0] + r * 0.7, coords["S0"][1] + r * 0.7)
    p2 = (coords["S1"][0] - r * 0.7, coords["S1"][1] + r * 0.7)
    draw_curved_arrow(ax, p1, p2, rad=-0.28, color="#2563eb", label="1 / 0", label_pos=(2.9, 2.35))

    # S1: X=1 -> S1 (self loop)
    draw_self_loop(ax, coords["S1"], r, direction="top", color="#2563eb", label="1 / 0")
    # S1: X=0 -> S2
    p1 = (coords["S1"][0] + r * 0.7, coords["S1"][1] + r * 0.7)
    p2 = (coords["S2"][0] - r * 0.7, coords["S2"][1] + r * 0.7)
    draw_curved_arrow(ax, p1, p2, rad=-0.28, color="#2563eb", label="0 / 0", label_pos=(5.9, 2.35))

    # S2: X=0 -> S3
    p1 = (coords["S2"][0] + r * 0.7, coords["S2"][1] + r * 0.7)
    p2 = (coords["S3"][0] - r * 0.7, coords["S3"][1] + r * 0.7)
    draw_curved_arrow(ax, p1, p2, rad=-0.28, color="#2563eb", label="0 / 0", label_pos=(8.9, 2.35))
    # S2: X=1 -> S1 (loop back to '1')
    p1 = (coords["S2"][0] - r * 0.7, coords["S2"][1] - r * 0.7)
    p2 = (coords["S1"][0] + r * 0.7, coords["S1"][1] - r * 0.7)
    draw_curved_arrow(ax, p1, p2, rad=-0.25, color="#64748b", label="1 / 0 (to '1')", label_pos=(5.9, 0.4))

    # S3: X=0 -> S0 (reset on '1000')
    p1 = (coords["S3"][0] - r * 0.5, coords["S3"][1] - r * 0.866)
    p2 = (coords["S0"][0] + r * 0.5, coords["S0"][1] - r * 0.866)
    draw_curved_arrow(ax, p1, p2, rad=-0.38, color="#64748b", label="0 / 0 (to Reset)", label_pos=(5.9, -0.6))

    # S3: X=1 -> S1 (Overlapping match! '1001' detected! Suffix '1' matches S1!)
    p1 = (coords["S3"][0] - r * 0.3, coords["S3"][1] - r * 0.95)
    p2 = (coords["S1"][0] + r * 0.3, coords["S1"][1] - r * 0.95)
    draw_curved_arrow(ax, p1, p2, rad=-0.44, color="#059669", lw=2.4, label="1 / 1  ★ MATCH!", label_pos=(7.4, -1.4), label_color="#065f46")

    ax.text(5.9, 3.9, "1001 Overlapping Sequence Detector — Mealy State Diagram", fontsize=13, fontweight="bold", color="#0f172a", ha="center")
    ax.text(5.9, 3.45, "Target '1001' detected on transition S3 → S1 with Output Z = 1 (Overlaps with prefix '1')", fontsize=8.8, color="#475569", ha="center")

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "state_diag_sequence_1001.png"), dpi=300, facecolor=BG_COLOR)
    plt.close()
    print("Rendered state_diag_sequence_1001.png")


if __name__ == "__main__":
    render_paper1_q1_reverse_conversion()
    render_medical_device_state_diagram()
    render_mod10_sync_state_diagram()
    render_sequence_101_state_diagram()
    render_8state_and_reduced_diagram()
    render_asynch_decade_timing_diagram()
    render_mod8_johnson_state_diagram()
    render_sequence_1001_state_diagram()
    print("All exam paper diagrams rendered successfully!")
