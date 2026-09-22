import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import networkx as nx
import numpy as np

IMG_DIR = r"c:\Users\ankit\Fall2627\Discrete\notes\cat2\img"
os.makedirs(IMG_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. Q2: Original and Simplified Switching Circuits
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7.5), dpi=300)

# (A) Original Circuit
ax1.set_title("VIT Bhopal CAT-II Q2: Original Switching Contact Network", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)

def draw_switch(ax, x1, x2, y, label, is_closed=False):
    ax.plot([x1, x1 + 0.3], [y, y], color='#0f172a', lw=2)
    ax.plot([x2 - 0.3, x2], [y, y], color='#0f172a', lw=2)
    # Switch contacts
    circle1 = patches.Circle((x1 + 0.3, y), 0.04, facecolor='#ffffff', edgecolor='#0f172a', lw=1.8, zorder=4)
    circle2 = patches.Circle((x2 - 0.3, y), 0.04, facecolor='#ffffff', edgecolor='#0f172a', lw=1.8, zorder=4)
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    # Blade
    if is_closed:
        ax.plot([x1 + 0.3, x2 - 0.3], [y, y], color='#1d4ed8', lw=2.2, zorder=3)
    else:
        ax.plot([x1 + 0.3, x2 - 0.35], [y, y + 0.22], color='#1d4ed8', lw=2.2, zorder=3)
    # Label
    ax.text((x1 + x2)/2, y + 0.32, label, fontsize=11, fontweight='bold', ha='center', va='center', color='#1e3a8a')

# Terminals & Main Rails
ax1.plot([0.5, 1.5], [1.5, 1.5], color='#0f172a', lw=2.5) # Input
ax1.text(0.3, 1.5, "Input T1", fontsize=10, fontweight='bold', ha='right', va='center', color='#334155')
ax1.plot([1.5, 1.5], [0.5, 2.5], color='#0f172a', lw=2.5) # Split

# Top branch (y=2.5): r in series with t
ax1.plot([1.5, 2.0], [2.5, 2.5], color='#0f172a', lw=2)
draw_switch(ax1, 2.0, 4.0, 2.5, "r")
ax1.plot([4.0, 5.0], [2.5, 2.5], color='#0f172a', lw=2)
draw_switch(ax1, 5.0, 7.0, 2.5, "t")
ax1.plot([7.0, 9.5], [2.5, 2.5], color='#0f172a', lw=2)

# Bottom branch: s in series with block1 and block2
ax1.plot([1.5, 2.0], [0.5, 0.5], color='#0f172a', lw=2)
draw_switch(ax1, 2.0, 3.2, 0.5, "s")
ax1.plot([3.2, 3.6], [0.5, 0.5], color='#0f172a', lw=2)

# Block 1 split (s' || t)
ax1.plot([3.6, 3.6], [0.0, 1.0], color='#0f172a', lw=2)
ax1.plot([3.6, 4.0], [1.0, 1.0], color='#0f172a', lw=2)
draw_switch(ax1, 4.0, 5.2, 1.0, "s'")
ax1.plot([5.2, 5.6], [1.0, 1.0], color='#0f172a', lw=2)

ax1.plot([3.6, 4.0], [0.0, 0.0], color='#0f172a', lw=2)
draw_switch(ax1, 4.0, 5.2, 0.0, "t")
ax1.plot([5.2, 5.6], [0.0, 0.0], color='#0f172a', lw=2)
ax1.plot([5.6, 5.6], [0.0, 1.0], color='#0f172a', lw=2)

# Mid wire between block 1 and block 2
ax1.plot([5.6, 6.2], [0.5, 0.5], color='#0f172a', lw=2)

# Block 2 split (r' || (s . t'))
ax1.plot([6.2, 6.2], [0.0, 1.0], color='#0f172a', lw=2)
# Top of block 2: r'
ax1.plot([6.2, 6.6], [1.0, 1.0], color='#0f172a', lw=2)
draw_switch(ax1, 6.6, 8.8, 1.0, "r'")
ax1.plot([8.8, 9.2], [1.0, 1.0], color='#0f172a', lw=2)

# Bottom of block 2: s in series with t'
ax1.plot([6.2, 6.5], [0.0, 0.0], color='#0f172a', lw=2)
draw_switch(ax1, 6.5, 7.6, 0.0, "s")
ax1.plot([7.6, 7.8], [0.0, 0.0], color='#0f172a', lw=2)
draw_switch(ax1, 7.8, 8.9, 0.0, "t'")
ax1.plot([8.9, 9.2], [0.0, 0.0], color='#0f172a', lw=2)
ax1.plot([9.2, 9.2], [0.0, 1.0], color='#0f172a', lw=2)

# Join back to main bottom rail
ax1.plot([9.2, 9.5], [0.5, 0.5], color='#0f172a', lw=2)
ax1.plot([9.5, 9.5], [0.5, 2.5], color='#0f172a', lw=2)
ax1.plot([9.5, 10.5], [1.5, 1.5], color='#0f172a', lw=2.5) # Output
ax1.text(10.7, 1.5, "Output T2", fontsize=10, fontweight='bold', ha='left', va='center', color='#334155')

ax1.text(5.5, -0.65, r"Full Expression: $F(r, s, t) = (r \cdot t) + [ s \cdot (s' + t) \cdot (r' + s \cdot t') ]$ (8 Switches)",
         fontsize=10, ha='center', color='#1e3a8a', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#eff6ff', edgecolor='#93c5fd'))

ax1.set_xlim(0, 11.5)
ax1.set_ylim(-0.9, 3.2)
ax1.axis('off')

# (B) Simplified Circuit
ax2.set_title("Equivalent Simplified Switching Circuit: F(r, s, t) = (r + s) . t (Only 3 Switches)", fontsize=11, fontweight='bold', color='#15803d', pad=12)

ax2.plot([1.5, 2.8], [1.5, 1.5], color='#0f172a', lw=2.5) # Input
ax2.text(1.3, 1.5, "Input T1", fontsize=10, fontweight='bold', ha='right', va='center', color='#334155')
ax2.plot([2.8, 2.8], [0.8, 2.2], color='#0f172a', lw=2.5) # Split

# Parallel block: r || s
ax2.plot([2.8, 3.4], [2.2, 2.2], color='#0f172a', lw=2)
draw_switch(ax2, 3.4, 5.0, 2.2, "r")
ax2.plot([5.0, 5.6], [2.2, 2.2], color='#0f172a', lw=2)

ax2.plot([2.8, 3.4], [0.8, 0.8], color='#0f172a', lw=2)
draw_switch(ax2, 3.4, 5.0, 0.8, "s")
ax2.plot([5.0, 5.6], [0.8, 0.8], color='#0f172a', lw=2)

ax2.plot([5.6, 5.6], [0.8, 2.2], color='#0f172a', lw=2.5) # Merge

# Series switch: t
ax2.plot([5.6, 6.4], [1.5, 1.5], color='#0f172a', lw=2.5)
draw_switch(ax2, 6.4, 8.0, 1.5, "t")
ax2.plot([8.0, 9.5], [1.5, 1.5], color='#0f172a', lw=2.5) # Output
ax2.text(9.7, 1.5, "Output T2", fontsize=10, fontweight='bold', ha='left', va='center', color='#334155')

ax2.text(5.5, 0.05, r"Simplified Expression: $F(r, s, t) = (r + s) \cdot t$ (Savings: 5 Switches Eliminated)",
         fontsize=10, ha='center', color='#15803d', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0fdf4', edgecolor='#86efac'))

ax2.set_xlim(0, 11.5)
ax2.set_ylim(-0.3, 2.9)
ax2.axis('off')

plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "cat2_slot_c14_q2_circuit.png"), bbox_inches='tight')
plt.close()
print("Generated: cat2_slot_c14_q2_circuit.png")

# -------------------------------------------------------------
# 2. Q3(b): Undirected Multigraph with Loops
# -------------------------------------------------------------
plt.figure(figsize=(7.5, 4.8), dpi=300)
ax = plt.gca()
ax.set_title("VIT Bhopal CAT-II Q3(b): Undirected Multigraph with Loops & Handshaking", fontsize=11, fontweight='bold', color='#1e3a8a', pad=15)

pos_q3 = {
    'V1': (-2.5, 0.5),
    'V2': (0.0, 0.5),
    'V3': (-1.0, -1.5),
    'V4': (1.0, -1.5),
    'V5': (2.8, 0.5)
}

# Draw vertices
nx.draw_networkx_nodes(None, pos_q3, nodelist=list(pos_q3.keys()), node_color='#dbeafe', node_size=1500, edgecolors='#1d4ed8', linewidths=2.5, ax=ax)
nx.draw_networkx_labels(None, pos_q3, labels={k: f'${k}$' for k in pos_q3}, font_size=12, font_weight='bold', font_color='#1e3a8a', ax=ax)

# Self-loop on V1
loop_v1 = patches.Circle((-3.25, 0.5), 0.75, facecolor='none', edgecolor='#0284c7', lw=2.2)
ax.add_patch(loop_v1)
ax.text(-3.3, 1.45, "Loop 1 (deg +2)", fontsize=8.5, fontweight='bold', color='#0369a1', ha='center')

# Self-loop on V5
loop_v5 = patches.Circle((3.55, 0.5), 0.75, facecolor='none', edgecolor='#0284c7', lw=2.2)
ax.add_patch(loop_v5)
ax.text(3.6, 1.45, "Loop 2 (deg +2)", fontsize=8.5, fontweight='bold', color='#0369a1', ha='center')

# Parallel edges between V1 and V2
# Top curved
arc_top = patches.Arc((-1.25, 0.5), 2.5, 1.2, theta1=0, theta2=180, edgecolor='#0284c7', lw=2.2)
ax.add_patch(arc_top)
# Bottom curved
arc_bot = patches.Arc((-1.25, 0.5), 2.5, 1.2, theta1=180, theta2=360, edgecolor='#0284c7', lw=2.2)
ax.add_patch(arc_bot)
ax.text(-1.25, 1.25, "Parallel Edge $e_1$", fontsize=8, color='#0284c7', ha='center')
ax.text(-1.25, -0.3, "Parallel Edge $e_2$", fontsize=8, color='#0284c7', ha='center')

# Straight edges
straight_edges = [
    ('V2', 'V3'),
    ('V2', 'V4'),
    ('V3', 'V4'),
    ('V2', 'V5')
]
for u, v in straight_edges:
    x1, y1 = pos_q3[u]
    x2, y2 = pos_q3[v]
    ax.plot([x1, x2], [y1, y2], color='#0284c7', lw=2.2, zorder=1)

# Degree badges
deg_labels = {
    'V1': r"$\deg=4$",
    'V2': r"$\deg=5$",
    'V3': r"$\deg=2$",
    'V4': r"$\deg=2$",
    'V5': r"$\deg=3$"
}
deg_pos = {
    'V1': (-2.5, 1.1),
    'V2': (0.0, 1.1),
    'V3': (-1.0, -2.1),
    'V4': (1.0, -2.1),
    'V5': (2.8, 1.1)
}
for v, txt in deg_labels.items():
    px, py = deg_pos[v]
    ax.text(px, py, txt, fontsize=9.5, fontweight='bold', color='#b91c1c', ha='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#fef2f2', edgecolor='#fca5a5', lw=1.2))

ax.text(0, -2.6, r"Handshaking Verification: $\sum \deg(v) = 4 + 5 + 2 + 2 + 3 = 16 = 2 \times 8 = 2|E|$ $\checkmark$",
        fontsize=9.5, fontweight='bold', ha='center', color='#15803d',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0fdf4', edgecolor='#86efac'))

ax.set_xlim(-4.3, 4.6)
ax.set_ylim(-2.9, 1.8)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "cat2_slot_c14_q3b_graph.png"), bbox_inches='tight')
plt.close()
print("Generated: cat2_slot_c14_q3b_graph.png")

# -------------------------------------------------------------
# 3. Q4: Graph Isomorphism G1 vs G2
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.2), dpi=300)

pos_g1 = {
    'A': (-1.2, 1.0),
    'B': (0.8, 1.0),
    'C': (1.4, -0.3),
    'D': (-0.2, -1.3),
    'E': (-1.5, -0.3)
}

ax1.set_title(r"Graph $G_1$ (Order 5, Size 7)", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)
nx.draw_networkx_nodes(None, pos_g1, nodelist=list(pos_g1.keys()), node_color='#dbeafe', node_size=1300, edgecolors='#1d4ed8', linewidths=2.2, ax=ax1)
nx.draw_networkx_labels(None, pos_g1, labels={k: f'${k}$' for k in pos_g1}, font_size=11, font_weight='bold', font_color='#1e3a8a', ax=ax1)

edges_g1 = [
    ('A', 'B'), ('A', 'D'),
    ('B', 'C'), ('B', 'D'), ('B', 'E'),
    ('C', 'D'), ('C', 'E')
]
for u, v in edges_g1:
    x1, y1 = pos_g1[u]
    x2, y2 = pos_g1[v]
    ax1.plot([x1, x2], [y1, y2], color='#0284c7', lw=2.2, zorder=1)

# Degree annotations with specific clean offsets
deg_offsets_g1 = {
    'A': (-0.35, 0.25),
    'B': (0.35, 0.25),
    'C': (0.45, 0.0),
    'D': (-0.45, -0.25),
    'E': (-0.45, 0.0)
}
for v, (ox, oy) in deg_offsets_g1.items():
    x, y = pos_g1[v]
    deg = sum(1 for e in edges_g1 if v in e)
    ax1.text(x + ox, y + oy, f"deg={deg}", fontsize=9, color='#b91c1c', fontweight='bold', ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.2', facecolor='#fef2f2', edgecolor='#fca5a5', lw=1.0))

ax1.set_xlim(-2.4, 2.4)
ax1.set_ylim(-2.0, 1.8)
ax1.axis('off')
ax1.text(0, -1.75, r"Degree Sequence: $(4, 3, 3, 2, 2)$", fontsize=10, ha='center', color='#1e3a8a', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.25', facecolor='#eff6ff', edgecolor='#bfdbfe'))

# Graph G2
pos_g2 = {
    'c': (-1.3, 1.0),
    'e': (0.2, 1.0),
    'a': (1.5, 0.8),
    'b': (-0.7, -1.1),
    'd': (0.8, -1.1)
}

ax2.set_title(r"Graph $G_2$ (Order 5, Size 7)", fontsize=11, fontweight='bold', color='#92400e', pad=12)
nx.draw_networkx_nodes(None, pos_g2, nodelist=list(pos_g2.keys()), node_color='#fef3c7', node_size=1300, edgecolors='#d97706', linewidths=2.2, ax=ax2)
nx.draw_networkx_labels(None, pos_g2, labels={k: f'${k}$' for k in pos_g2}, font_size=11, font_weight='bold', font_color='#92400e', ax=ax2)

edges_g2 = [
    ('b', 'c'), ('b', 'e'), ('b', 'd'), ('b', 'a'),
    ('c', 'e'), ('c', 'd'),
    ('d', 'a')
]
for u, v in edges_g2:
    x1, y1 = pos_g2[u]
    x2, y2 = pos_g2[v]
    ax2.plot([x1, x2], [y1, y2], color='#d97706', lw=2.2, zorder=1)

deg_offsets_g2 = {
    'c': (-0.45, 0.2),
    'e': (0.0, 0.35),
    'a': (0.45, 0.2),
    'b': (-0.45, -0.25),
    'd': (0.45, -0.25)
}
for v, (ox, oy) in deg_offsets_g2.items():
    x, y = pos_g2[v]
    deg = sum(1 for e in edges_g2 if v in e)
    ax2.text(x + ox, y + oy, f"deg={deg}", fontsize=9, color='#92400e', fontweight='bold', ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.2', facecolor='#fffbeb', edgecolor='#fde68a', lw=1.0))

ax2.set_xlim(-2.4, 2.4)
ax2.set_ylim(-2.0, 1.8)
ax2.axis('off')
ax2.text(0, -1.75, r"Bijection: $B \mapsto b, D \mapsto d, C \mapsto c, A \mapsto a, E \mapsto e$", fontsize=9.5, ha='center', color='#15803d', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.25', facecolor='#f0fdf4', edgecolor='#bbf7d0'))

plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "cat2_slot_c14_q4_isomorphism.png"), bbox_inches='tight')
plt.close()
print("Generated: cat2_slot_c14_q4_isomorphism.png")

# -------------------------------------------------------------
# 4. Q5: Dijkstra Weighted Graph & Shortest Path Trace
# -------------------------------------------------------------
plt.figure(figsize=(9.5, 5.5), dpi=300)
ax = plt.gca()
ax.set_title("VIT Bhopal CAT-II Q5: Dijkstra Shortest Path from A to G (Optimal Cost = 74)", fontsize=11, fontweight='bold', color='#1e3a8a', pad=15)

pos_dijkstra = {
    'A': (0.0, 1.0),
    'B': (2.0, 2.2),
    'C': (2.0, -0.2),
    'D': (4.2, 1.0),
    'E': (6.4, 2.2),
    'F': (6.4, -0.2),
    'G': (8.4, 1.0)
}

nx.draw_networkx_nodes(None, pos_dijkstra, nodelist=list(pos_dijkstra.keys()), node_color='#dbeafe', node_size=1500, edgecolors='#1d4ed8', linewidths=2.5, ax=ax)
nx.draw_networkx_labels(None, pos_dijkstra, labels={k: f'${k}$' for k in pos_dijkstra}, font_size=12, font_weight='bold', font_color='#1e3a8a', ax=ax)

# Edge weights
all_edges = [
    ('A', 'B', 30),
    ('A', 'C', 45),
    ('B', 'C', 19),
    ('B', 'D', 6),
    ('B', 'E', 40),
    ('C', 'D', 12),
    ('C', 'F', 10),
    ('D', 'E', 35),
    ('D', 'F', 40),
    ('E', 'F', 11),
    ('E', 'G', 8),
    ('F', 'G', 20)
]

shortest_path_edges = [('A', 'C'), ('C', 'F'), ('F', 'E'), ('E', 'G')]

# Draw non-shortest edges
for u, v, w in all_edges:
    if (u, v) not in shortest_path_edges and (v, u) not in shortest_path_edges:
        x1, y1 = pos_dijkstra[u]
        x2, y2 = pos_dijkstra[v]
        ax.plot([x1, x2], [y1, y2], color='#94a3b8', lw=2.0, zorder=1)

# Draw shortest path edges with bold red line and arrows
for u, v in shortest_path_edges:
    x1, y1 = pos_dijkstra[u]
    x2, y2 = pos_dijkstra[v]
    ax.plot([x1, x2], [y1, y2], color='#dc2626', lw=4.0, zorder=2)
    # Add arrow indicator
    mx, my = (x1 + x2)/2, (y1 + y2)/2
    ax.annotate('', xy=(x2, y2), xytext=(mx, my),
                arrowprops=dict(arrowstyle='-|>', color='#dc2626', lw=3.0, mutation_scale=15))

# Edge weight text positions
weight_offsets = {
    ('A', 'B'): (0.9, 1.75),
    ('A', 'C'): (0.9, 0.25),
    ('B', 'C'): (1.8, 1.0),
    ('B', 'D'): (3.0, 1.75),
    ('B', 'E'): (4.2, 2.38),
    ('C', 'D'): (3.0, 0.25),
    ('C', 'F'): (4.2, -0.38),
    ('D', 'E'): (5.4, 1.75),
    ('D', 'F'): (5.4, 0.25),
    ('E', 'F'): (6.65, 1.0),
    ('E', 'G'): (7.5, 1.75),
    ('F', 'G'): (7.5, 0.25)
}

for (u, v, w) in all_edges:
    key = (u, v) if (u, v) in weight_offsets else (v, u)
    wx, wy = weight_offsets[key]
    is_sp = (u, v) in shortest_path_edges or (v, u) in shortest_path_edges
    fc = '#fef2f2' if is_sp else '#f8fafc'
    ec = '#dc2626' if is_sp else '#cbd5e1'
    tc = '#b91c1c' if is_sp else '#475569'
    ax.text(wx, wy, str(w), fontsize=10.5, fontweight='bold', color=tc, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.25', facecolor=fc, edgecolor=ec, lw=1.2))

ax.text(4.2, -1.0, r"Optimal Shortest Path: $A \to C \to F \to E \to G$ with Total Weight = $45 + 10 + 11 + 8 = 74$",
        fontsize=10.5, fontweight='bold', ha='center', color='#dc2626',
        bbox=dict(boxstyle='round,pad=0.35', facecolor='#fef2f2', edgecolor='#fca5a5', lw=1.5))

ax.set_xlim(-0.8, 9.2)
ax.set_ylim(-1.3, 2.7)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "cat2_slot_c14_q5_dijkstra.png"), bbox_inches='tight')
plt.close()
print("Generated: cat2_slot_c14_q5_dijkstra.png")
