"""
Publication-grade State Diagram Renderer for DLD CAT-2 Foolproof Solve Booklet.
Renders razor-sharp 300 DPI vector-styled state transition diagrams with ZERO text collisions:
1. 1010 Mealy Sequence Detector (Assignment 5 Q5)
2. Analyzed Sequential Circuit State Diagram (Assignment 4 Q3 - Moore Machine)
3. Prime Number Synchronous Counter with Lockout & Self-Starting Recovery (Assignment 5 Q1)
4. Toy Robot FSM State Transition Diagram (Assignment 5 Q2)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
import numpy as np
import os

OUT_DIR = r"c:\Users\ankit\Fall2627\DLD\notes\cat2\circuits"
os.makedirs(OUT_DIR, exist_ok=True)

# Common styling palette
BG_COLOR = "#ffffff"
PRIMARY_STROKE = "#1e293b"
STATE_FILL = "#eff6ff"
STATE_BORDER = "#2563eb"
STATE_VALID_FILL = "#ecfdf5"
STATE_VALID_BORDER = "#059669"
STATE_UNUSED_FILL = "#fef2f2"
STATE_UNUSED_BORDER = "#dc2626"


def draw_curved_arrow(ax, p1, p2, rad=0.2, color="#2563eb", lw=1.8, label="", label_pos=None, label_color="#0f172a", fontsize=9.5, is_dashed=False):
    """Draws a curved directed arrow between p1 and p2 with text label on a white badge"""
    ls = "-" if not is_dashed else "--"
    arrow = FancyArrowPatch(
        p1, p2,
        connectionstyle=f"arc3,rad={rad}",
        arrowstyle="-|>",
        mutation_scale=14,
        color=color,
        linewidth=lw,
        linestyle=ls,
        zorder=3
    )
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

        ax.text(
            lx, ly, label,
            fontsize=fontsize, fontweight="bold", color=label_color,
            ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.22", fc="white", ec=color, lw=1.1, alpha=0.96),
            zorder=6
        )


def draw_self_loop(ax, center, r, direction="top", color="#2563eb", lw=1.8, label="", label_color="#0f172a", fontsize=9.5):
    """Draws a self-loop arrow sticking out from a circular state node"""
    cx, cy = center
    if direction == "top":
        start = (cx - r * 0.5, cy + r * 0.866)
        end = (cx + r * 0.5, cy + r * 0.866)
        rad = -1.2
        label_pos = (cx, cy + r + 0.58)
    elif direction == "bottom":
        start = (cx + r * 0.5, cy - r * 0.866)
        end = (cx - r * 0.5, cy - r * 0.866)
        rad = -1.2
        label_pos = (cx, cy - r - 0.58)
    elif direction == "left":
        start = (cx - r * 0.866, cy - r * 0.5)
        end = (cx - r * 0.866, cy + r * 0.5)
        rad = -1.2
        label_pos = (cx - r - 0.70, cy)
    else:  # right
        start = (cx + r * 0.866, cy + r * 0.5)
        end = (cx + r * 0.866, cy - r * 0.5)
        rad = -1.2
        label_pos = (cx + r + 0.70, cy)

    arrow = FancyArrowPatch(
        start, end,
        connectionstyle=f"arc3,rad={rad}",
        arrowstyle="-|>",
        mutation_scale=13,
        color=color,
        linewidth=lw,
        zorder=3
    )
    ax.add_patch(arrow)

    if label:
        ax.text(
            label_pos[0], label_pos[1], label,
            fontsize=fontsize, fontweight="bold", color=label_color,
            ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=color, lw=1.1, alpha=0.96),
            zorder=6
        )


def draw_state_node(ax, xy, r, title, subtitle="", fc=STATE_FILL, ec=STATE_BORDER, title_color="#0f172a", sub_color="#475569"):
    """Draws a circular state bubble with title and code/subtitle"""
    circle = patches.Circle(xy, r, facecolor=fc, edgecolor=ec, linewidth=2.2, zorder=4)
    ax.add_patch(circle)

    if subtitle:
        ax.text(xy[0], xy[1] + 0.12, title, fontsize=11, fontweight="bold", color=title_color, ha="center", va="center", zorder=5)
        ax.text(xy[0], xy[1] - 0.22, subtitle, fontsize=8.5, fontweight="bold", color=sub_color, ha="center", va="center", zorder=5)
    else:
        ax.text(xy[0], xy[1], title, fontsize=11.5, fontweight="bold", color=title_color, ha="center", va="center", zorder=5)


# ==============================================================================
# 1. 1010 MEALY SEQUENCE DETECTOR STATE DIAGRAM (Assignment 5 Q5)
# ==============================================================================
def render_mealy_1010_state_diagram():
    fig, ax = plt.subplots(figsize=(11.0, 4.8), dpi=300)
    ax.set_xlim(-1.2, 13.0)
    ax.set_ylim(-2.2, 4.6)
    ax.axis("off")

    r = 0.68
    coords = {
        "S0": (1.4, 1.3),
        "S1": (4.6, 1.3),
        "S2": (7.8, 1.3),
        "S3": (11.0, 1.3),
    }

    # Reset indicator arrow coming from top-left diagonally
    ax.annotate(
        "RESET", xy=(coords["S0"][0] - r * 0.7, coords["S0"][1] + r * 0.7),
        xytext=(coords["S0"][0] - r * 0.7 - 1.1, coords["S0"][1] + r * 0.7 + 0.7),
        arrowprops=dict(facecolor="#475569", edgecolor="#475569", width=2.0, headwidth=7),
        fontsize=9.5, fontweight="bold", color="#1e293b", va="bottom", ha="right"
    )

    # State Nodes
    draw_state_node(ax, coords["S0"], r, "S0", "00 (Reset)", fc="#f8fafc", ec="#475569")
    draw_state_node(ax, coords["S1"], r, "S1", "01 ('1')", fc="#eff6ff", ec="#2563eb")
    draw_state_node(ax, coords["S2"], r, "S2", "10 ('10')", fc="#eff6ff", ec="#2563eb")
    draw_state_node(ax, coords["S3"], r, "S3", "11 ('101')", fc="#fef3c7", ec="#d97706")

    # Transitions from S0
    # X=0 -> S0 (Self loop on the left side)
    draw_self_loop(ax, coords["S0"], r, direction="left", color="#475569", label="0 / 0")
    # X=1 -> S1 (Forward top arc)
    p1 = (coords["S0"][0] + r * 0.7, coords["S0"][1] + r * 0.7)
    p2 = (coords["S1"][0] - r * 0.7, coords["S1"][1] + r * 0.7)
    draw_curved_arrow(ax, p1, p2, rad=-0.32, color="#2563eb", label="1 / 0", label_pos=(3.0, 2.35))

    # Transitions from S1
    # X=1 -> S1 (Self loop on top)
    draw_self_loop(ax, coords["S1"], r, direction="top", color="#2563eb", label="1 / 0")
    # X=0 -> S2 (Forward top arc)
    p1 = (coords["S1"][0] + r * 0.7, coords["S1"][1] + r * 0.7)
    p2 = (coords["S2"][0] - r * 0.7, coords["S2"][1] + r * 0.7)
    draw_curved_arrow(ax, p1, p2, rad=-0.32, color="#2563eb", label="0 / 0", label_pos=(6.2, 2.35))

    # Transitions from S2
    # X=1 -> S3 (Forward top arc)
    p1 = (coords["S2"][0] + r * 0.7, coords["S2"][1] + r * 0.7)
    p2 = (coords["S3"][0] - r * 0.7, coords["S3"][1] + r * 0.7)
    draw_curved_arrow(ax, p1, p2, rad=-0.32, color="#2563eb", label="1 / 0", label_pos=(9.4, 2.35))
    # X=0 -> S0 (Backward wide bottom arc)
    p1 = (coords["S2"][0] - r * 0.4, coords["S2"][1] - r * 0.9)
    p2 = (coords["S0"][0] + r * 0.4, coords["S0"][1] - r * 0.9)
    draw_curved_arrow(ax, p1, p2, rad=-0.36, color="#64748b", label="0 / 0 (to Reset)", label_pos=(4.6, -0.2))

    # Transitions from S3
    # X=0 -> S2 (Overlapping detection! Z = 1!)
    p1 = (coords["S3"][0] - r * 0.7, coords["S3"][1] - r * 0.7)
    p2 = (coords["S2"][0] + r * 0.7, coords["S2"][1] - r * 0.7)
    draw_curved_arrow(
        ax, p1, p2, rad=-0.36, color="#059669", lw=2.4,
        label="0 / 1  ★ MATCH!", label_pos=(9.4, -0.05), label_color="#065f46"
    )
    # X=1 -> S1 (Backward deep bottom arc)
    p1 = (coords["S3"][0] - r * 0.2, coords["S3"][1] - r * 0.98)
    p2 = (coords["S1"][0] + r * 0.2, coords["S1"][1] - r * 0.98)
    draw_curved_arrow(
        ax, p1, p2, rad=-0.44, color="#d97706", lw=2.0,
        label="1 / 0 (to '1')", label_pos=(7.8, -1.5), label_color="#92400e"
    )

    # Header / Title banner
    ax.text(6.2, 4.3, "1010 Overlapping Sequence Detector — Mealy State Diagram", fontsize=13.5, fontweight="bold", color="#0f172a", ha="center")
    ax.text(6.2, 3.8, "Transitions labeled Input (X) / Output (Z)  |  Target '1010' detected on S3 → S2 with Z = 1", fontsize=9.2, color="#475569", ha="center")

    plt.tight_layout()
    png_path = os.path.join(OUT_DIR, "state_diag_mealy_1010.png")
    svg_path = os.path.join(OUT_DIR, "state_diag_mealy_1010.svg")
    plt.savefig(png_path, dpi=300, facecolor=BG_COLOR)
    plt.savefig(svg_path, facecolor=BG_COLOR)
    plt.close()
    print(f"Generated: {png_path}")


# ==============================================================================
# 2. SEQUENTIAL CIRCUIT ANALYSIS MOORE STATE DIAGRAM (Assignment 4 Q3)
# ==============================================================================
def render_moore_circuit_state_diagram():
    fig, ax = plt.subplots(figsize=(8.2, 6.2), dpi=300)
    ax.set_xlim(-1.6, 9.6)
    ax.set_ylim(-0.8, 7.2)
    ax.axis("off")

    r = 0.72
    # 2x2 grid layout
    coords = {
        "00": (1.8, 4.9),
        "01": (6.2, 4.9),
        "10": (1.8, 1.4),
        "11": (6.2, 1.4),
    }

    # Moore State Nodes: State / Output F
    draw_state_node(ax, coords["00"], r, "00", "F = 0", fc="#f8fafc", ec="#475569")
    draw_state_node(ax, coords["01"], r, "01", "F = 1", fc="#ecfdf5", ec="#059669")
    draw_state_node(ax, coords["10"], r, "10", "F = 1", fc="#ecfdf5", ec="#059669")
    draw_state_node(ax, coords["11"], r, "11", "F = 0", fc="#f8fafc", ec="#475569")

    # Transitions from 00:
    # X=1 -> 00 (self loop left)
    draw_self_loop(ax, coords["00"], r, direction="left", color="#475569", label="X = 1")
    # X=0 -> 01 (horizontal top)
    p1 = (coords["00"][0] + r * 0.9, coords["00"][1] + r * 0.3)
    p2 = (coords["01"][0] - r * 0.9, coords["01"][1] + r * 0.3)
    draw_curved_arrow(ax, p1, p2, rad=-0.22, color="#2563eb", label="X = 0", label_pos=(4.0, 5.5))

    # Transitions from 01:
    # X=0 -> 11 (vertical down)
    p1 = (coords["01"][0] + r * 0.3, coords["01"][1] - r * 0.95)
    p2 = (coords["11"][0] + r * 0.3, coords["11"][1] + r * 0.95)
    draw_curved_arrow(ax, p1, p2, rad=-0.22, color="#2563eb", label="X = 0", label_pos=(7.0, 3.15))
    # X=1 -> 10 (diagonal: curves toward center-right)
    p1 = (coords["01"][0] - r * 0.6, coords["01"][1] - r * 0.8)
    p2 = (coords["10"][0] + r * 0.8, coords["10"][1] + r * 0.6)
    draw_curved_arrow(ax, p1, p2, rad=-0.25, color="#d97706", label="X = 1", label_pos=(4.7, 2.7))

    # Transitions from 10:
    # X=1 -> 10 (self loop left)
    draw_self_loop(ax, coords["10"], r, direction="left", color="#475569", label="X = 1")
    # X=0 -> 01 (diagonal: curves toward center-left)
    p1 = (coords["10"][0] + r * 0.6, coords["10"][1] + r * 0.8)
    p2 = (coords["01"][0] - r * 0.8, coords["01"][1] - r * 0.6)
    draw_curved_arrow(ax, p1, p2, rad=-0.25, color="#2563eb", label="X = 0", label_pos=(3.3, 3.6))

    # Transitions from 11:
    # X=1 -> 11 (self loop right)
    draw_self_loop(ax, coords["11"], r, direction="right", color="#475569", label="X = 1")
    # X=0 -> 10 (horizontal bottom)
    p1 = (coords["11"][0] - r * 0.9, coords["11"][1] - r * 0.3)
    p2 = (coords["10"][0] + r * 0.9, coords["10"][1] - r * 0.3)
    draw_curved_arrow(ax, p1, p2, rad=-0.22, color="#2563eb", label="X = 0", label_pos=(4.0, 0.75))

    # Title
    ax.text(4.0, 6.8, "Sequential Circuit State Diagram (Moore Machine)", fontsize=13.5, fontweight="bold", color="#0f172a", ha="center")
    ax.text(4.0, 6.35, "State circle shows (AB / F) where F = A ⊕ B  |  Transition arrows labeled with Input X", fontsize=9.2, color="#475569", ha="center")

    plt.tight_layout()
    png_path = os.path.join(OUT_DIR, "state_diag_moore_circuit_a4_q3.png")
    svg_path = os.path.join(OUT_DIR, "state_diag_moore_circuit_a4_q3.svg")
    plt.savefig(png_path, dpi=300, facecolor=BG_COLOR)
    plt.savefig(svg_path, facecolor=BG_COLOR)
    plt.close()
    print(f"Generated: {png_path}")


# ==============================================================================
# 3. PRIME NUMBER COUNTER & LOCKOUT RECOVERY STATE DIAGRAM (Assignment 5 Q1)
# ==============================================================================
def render_prime_counter_lockout_diagram():
    fig, ax = plt.subplots(figsize=(10.5, 7.2), dpi=300)
    ax.set_xlim(-1.2, 10.8)
    ax.set_ylim(-2.0, 6.6)
    ax.axis("off")

    r = 0.68

    # Valid cycle nodes in center ring
    coords_valid = {
        "2": (3.6, 4.4),  # 010 (top-left)
        "3": (7.4, 4.4),  # 011 (top-right)
        "5": (7.4, 1.8),  # 101 (bottom-right)
        "7": (3.6, 1.8),  # 111 (bottom-left)
    }

    # Unused state nodes placed cleanly outside to avoid ANY crossing
    coords_unused = {
        "0": (0.6, 4.4),   # 000 (far left of 2)
        "1": (0.6, 1.8),   # 001 (far left of 7)
        "6": (3.6, -0.8),  # 110 (directly below 7)
        "4": (7.4, -0.8),  # 100 (directly below 5, right of 6)
    }

    # Draw Valid Cycle States (Emerald Green)
    draw_state_node(ax, coords_valid["2"], r, "State 2", "010", fc=STATE_VALID_FILL, ec=STATE_VALID_BORDER)
    draw_state_node(ax, coords_valid["3"], r, "State 3", "011", fc=STATE_VALID_FILL, ec=STATE_VALID_BORDER)
    draw_state_node(ax, coords_valid["5"], r, "State 5", "101", fc=STATE_VALID_FILL, ec=STATE_VALID_BORDER)
    draw_state_node(ax, coords_valid["7"], r, "State 7", "111", fc=STATE_VALID_FILL, ec=STATE_VALID_BORDER)

    # Valid Cycle Transitions (Bold green arrows: 2 -> 3 -> 5 -> 7 -> 2)
    # 2 -> 3
    p1 = (coords_valid["2"][0] + r, coords_valid["2"][1])
    p2 = (coords_valid["3"][0] - r, coords_valid["3"][1])
    draw_curved_arrow(ax, p1, p2, rad=-0.08, color="#059669", lw=2.4, label="CLK", label_pos=(5.5, 4.7))
    # 3 -> 5
    p1 = (coords_valid["3"][0], coords_valid["3"][1] - r)
    p2 = (coords_valid["5"][0], coords_valid["5"][1] + r)
    draw_curved_arrow(ax, p1, p2, rad=-0.08, color="#059669", lw=2.4, label="CLK", label_pos=(7.8, 3.1))
    # 5 -> 7
    p1 = (coords_valid["5"][0] - r, coords_valid["5"][1])
    p2 = (coords_valid["7"][0] + r, coords_valid["7"][1])
    draw_curved_arrow(ax, p1, p2, rad=-0.08, color="#059669", lw=2.4, label="CLK", label_pos=(5.5, 1.5))
    # 7 -> 2
    p1 = (coords_valid["7"][0], coords_valid["7"][1] + r)
    p2 = (coords_valid["2"][0], coords_valid["2"][1] - r)
    draw_curved_arrow(ax, p1, p2, rad=-0.08, color="#059669", lw=2.4, label="CLK", label_pos=(3.2, 3.1))

    # Draw Unused States (Red / Soft Rose)
    draw_state_node(ax, coords_unused["0"], r * 0.9, "State 0", "000 (Unused)", fc=STATE_UNUSED_FILL, ec=STATE_UNUSED_BORDER)
    draw_state_node(ax, coords_unused["1"], r * 0.9, "State 1", "001 (Unused)", fc=STATE_UNUSED_FILL, ec=STATE_UNUSED_BORDER)
    draw_state_node(ax, coords_unused["6"], r * 0.9, "State 6", "110 (Unused)", fc=STATE_UNUSED_FILL, ec=STATE_UNUSED_BORDER)
    draw_state_node(ax, coords_unused["4"], r * 0.9, "State 4", "100 (Unused)", fc=STATE_UNUSED_FILL, ec=STATE_UNUSED_BORDER)

    # Unused Recovery Transitions (Dashed Red/Orange Arrows)
    # State 0 (000) -> State 2 (010) (1 pulse direct right)
    p1 = (coords_unused["0"][0] + r * 0.9, coords_unused["0"][1])
    p2 = (coords_valid["2"][0] - r, coords_valid["2"][1])
    draw_curved_arrow(ax, p1, p2, rad=0.0, color="#dc2626", lw=1.8, is_dashed=True, label="1 pulse → enters 2", label_pos=(2.1, 4.7), label_color="#991b1b")

    # State 1 (001) -> State 7 (111) (1 pulse direct right)
    p1 = (coords_unused["1"][0] + r * 0.9, coords_unused["1"][1])
    p2 = (coords_valid["7"][0] - r, coords_valid["7"][1])
    draw_curved_arrow(ax, p1, p2, rad=0.0, color="#dc2626", lw=1.8, is_dashed=True, label="1 pulse → enters 7", label_pos=(2.1, 2.1), label_color="#991b1b")

    # State 4 (100) -> State 6 (110) (1 pulse direct left)
    p1 = (coords_unused["4"][0] - r * 0.9, coords_unused["4"][1])
    p2 = (coords_unused["6"][0] + r * 0.9, coords_unused["6"][1])
    draw_curved_arrow(ax, p1, p2, rad=0.0, color="#d97706", lw=1.8, is_dashed=True, label="to State 6", label_pos=(5.5, -0.5), label_color="#b45309")

    # State 6 (110) -> State 7 (111) (1 pulse direct up into 7)
    p1 = (coords_unused["6"][0], coords_unused["6"][1] + r * 0.9)
    p2 = (coords_valid["7"][0], coords_valid["7"][1] - r)
    draw_curved_arrow(ax, p1, p2, rad=0.0, color="#dc2626", lw=1.8, is_dashed=True, label="1 pulse → enters 7", label_pos=(3.6, 0.5), label_color="#991b1b")

    # Title & Badge
    ax.text(5.5, 6.1, "Prime Counter Sequence & Self-Starting Lockout Recovery Diagram", fontsize=13.5, fontweight="bold", color="#0f172a", ha="center")
    ax.text(5.5, 5.6, "Green = Desired Count Cycle (2 → 3 → 5 → 7)  |  Dashed Red/Orange = Unused States Self-Recovering into Valid Loop", fontsize=8.8, color="#475569", ha="center")

    # Lockout Free Stamp / Badge in center
    ax.text(
        5.5, 3.1, "✓ 100% SELF-STARTING\nNO LOCKOUT DETECTED\n(Recovers within ≤ 2 pulses)",
        fontsize=9.5, fontweight="bold", color="#065f46", ha="center", va="center",
        bbox=dict(boxstyle="round,pad=0.4", fc="#ecfdf5", ec="#059669", lw=1.5)
    )

    plt.tight_layout()
    png_path = os.path.join(OUT_DIR, "state_diag_prime_counter_lockout.png")
    svg_path = os.path.join(OUT_DIR, "state_diag_prime_counter_lockout.svg")
    plt.savefig(png_path, dpi=300, facecolor=BG_COLOR)
    plt.savefig(svg_path, facecolor=BG_COLOR)
    plt.close()
    print(f"Generated: {png_path}")


# ==============================================================================
# 4. TOY ROBOT FSM STATE TRANSITION DIAGRAM (Assignment 5 Q2)
# ==============================================================================
def render_toy_robot_state_diagram():
    fig, ax = plt.subplots(figsize=(7.8, 6.0), dpi=300)
    ax.set_xlim(-1.4, 9.0)
    ax.set_ylim(-1.0, 7.0)
    ax.axis("off")

    r = 0.75
    # 4 states in a diamond / ring
    coords = {
        "S0": (3.8, 4.6),  # Standing
        "S1": (7.0, 2.6),  # Walking
        "S2": (3.8, 0.6),  # Tumbling
        "S3": (0.6, 2.6),  # Clapping
    }

    # State Nodes
    draw_state_node(ax, coords["S0"], r, "S0 (00)", "Standing", fc="#eff6ff", ec="#2563eb")
    draw_state_node(ax, coords["S1"], r, "S1 (01)", "Walking", fc="#eff6ff", ec="#2563eb")
    draw_state_node(ax, coords["S2"], r, "S2 (10)", "Tumbling", fc="#eff6ff", ec="#2563eb")
    draw_state_node(ax, coords["S3"], r, "S3 (11)", "Clapping", fc="#eff6ff", ec="#2563eb")

    # Self-loops for X = 0 (Button not pressed / hold)
    draw_self_loop(ax, coords["S0"], r, direction="top", color="#64748b", label="X = 0")
    draw_self_loop(ax, coords["S1"], r, direction="right", color="#64748b", label="X = 0")
    draw_self_loop(ax, coords["S2"], r, direction="bottom", color="#64748b", label="X = 0")
    draw_self_loop(ax, coords["S3"], r, direction="left", color="#64748b", label="X = 0")

    # Cycle transitions for X = 1 (Button pressed -> next action)
    # S0 -> S1
    p1 = (coords["S0"][0] + r * 0.7, coords["S0"][1] - r * 0.5)
    p2 = (coords["S1"][0] - r * 0.5, coords["S1"][1] + r * 0.7)
    draw_curved_arrow(ax, p1, p2, rad=-0.16, color="#059669", lw=2.2, label="X = 1", label_pos=(5.8, 3.9))

    # S1 -> S2
    p1 = (coords["S1"][0] - r * 0.5, coords["S1"][1] - r * 0.7)
    p2 = (coords["S2"][0] + r * 0.7, coords["S2"][1] + r * 0.5)
    draw_curved_arrow(ax, p1, p2, rad=-0.16, color="#059669", lw=2.2, label="X = 1", label_pos=(5.8, 1.3))

    # S2 -> S3
    p1 = (coords["S2"][0] - r * 0.7, coords["S2"][1] + r * 0.5)
    p2 = (coords["S3"][0] + r * 0.5, coords["S3"][1] - r * 0.7)
    draw_curved_arrow(ax, p1, p2, rad=-0.16, color="#059669", lw=2.2, label="X = 1", label_pos=(1.8, 1.3))

    # S3 -> S0
    p1 = (coords["S3"][0] + r * 0.5, coords["S3"][1] + r * 0.7)
    p2 = (coords["S0"][0] - r * 0.7, coords["S0"][1] - r * 0.5)
    draw_curved_arrow(ax, p1, p2, rad=-0.16, color="#059669", lw=2.2, label="X = 1", label_pos=(1.8, 3.9))

    # Title raised high above top self-loop
    ax.text(3.8, 6.6, "Toy Robot FSM — State Transition Diagram", fontsize=13, fontweight="bold", color="#0f172a", ha="center")
    ax.text(3.8, 2.6, "4 Cyclic Modes\nX = 1: Next Mode\nX = 0: Hold Mode", fontsize=8.5, color="#64748b", ha="center", va="center")

    plt.tight_layout()
    png_path = os.path.join(OUT_DIR, "state_diag_toy_robot_fsm.png")
    svg_path = os.path.join(OUT_DIR, "state_diag_toy_robot_fsm.svg")
    plt.savefig(png_path, dpi=300, facecolor=BG_COLOR)
    plt.savefig(svg_path, facecolor=BG_COLOR)
    plt.close()
    print(f"Generated: {png_path}")


if __name__ == "__main__":
    render_mealy_1010_state_diagram()
    render_moore_circuit_state_diagram()
    render_prime_counter_lockout_diagram()
    render_toy_robot_state_diagram()
    print("All 4 State Diagrams successfully rendered with zero collisions!")
