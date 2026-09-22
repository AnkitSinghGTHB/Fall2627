import os
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

IMG_DIR = r"c:\Users\ankit\Fall2627\Discrete\notes\cat2\img"
os.makedirs(IMG_DIR, exist_ok=True)

# 1. Q5: Weighted Directed Graph for Floyd-Warshall
plt.figure(figsize=(6.5, 5), dpi=300)
ax = plt.gca()
ax.set_title("VIT Bhopal CAT-II Q5: Weighted Directed Graph for Floyd-Warshall", fontsize=11, fontweight='bold', color='#1e3a8a', pad=15)

pos = {
    'v1': (0, 1),
    'v2': (1.5, 1),
    'v3': (1.5, 0),
    'v4': (0, 0)
}

# Draw nodes
nx.draw_networkx_nodes(None, pos, nodelist=['v1', 'v2', 'v3', 'v4'], node_color='#dbeafe', node_size=1600, edgecolors='#1d4ed8', linewidths=2.5, ax=ax)
nx.draw_networkx_labels(None, pos, labels={'v1': '$v_1$', 'v2': '$v_2$', 'v3': '$v_3$', 'v4': '$v_4$'}, font_size=13, font_weight='bold', font_color='#1e3a8a', ax=ax)

# Directed edges
edges = [
    ('v1', 'v2', 4),
    ('v1', 'v4', 10),
    ('v2', 'v3', 2),
    ('v3', 'v4', 5),
    ('v4', 'v2', 3),
    ('v3', 'v1', 1)
]

for u, v, w in edges:
    x1, y1 = pos[u]
    x2, y2 = pos[v]
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='-|>', color='#0284c7', lw=2.2, mutation_scale=18,
                                shrinkA=18, shrinkB=18))

# Weight labels
weight_positions = {
    ('v1', 'v2'): (0.75, 1.08, '4'),
    ('v1', 'v4'): (-0.14, 0.5, '10'),
    ('v2', 'v3'): (1.64, 0.5, '2'),
    ('v3', 'v4'): (0.75, -0.10, '5'),
    ('v4', 'v2'): (0.92, 0.68, '3'),
    ('v3', 'v1'): (0.58, 0.68, '1')
}

for (u, v), (wx, wy, lbl) in weight_positions.items():
    ax.text(wx, wy, lbl, fontsize=12, fontweight='bold', color='#b91c1c', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#fef2f2', edgecolor='#fca5a5', lw=1.2))

ax.set_xlim(-0.4, 1.9)
ax.set_ylim(-0.3, 1.3)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "cat2_actual_q5_graph.png"), bbox_inches='tight')
plt.close()
print("Generated: cat2_actual_q5_graph.png")

# 2. Q4: Isomorphism between G1 (C6) and G2
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.2), dpi=300)

ax1.set_title("Graph G1: Single Cycle of Length 6 (C6)", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)
angles = np.linspace(np.pi/2, np.pi/2 - 2*np.pi, 6, endpoint=False)
pos_g1 = {f'v{i+1}': (np.cos(ang), np.sin(ang)) for i, ang in enumerate(angles)}

nx.draw_networkx_nodes(None, pos_g1, nodelist=list(pos_g1.keys()), node_color='#dbeafe', node_size=1300, edgecolors='#1d4ed8', linewidths=2.2, ax=ax1)
nx.draw_networkx_labels(None, pos_g1, labels={k: f'${k}$' for k in pos_g1}, font_size=11, font_weight='bold', font_color='#1e3a8a', ax=ax1)
edges_g1 = [(f'v{i+1}', f'v{((i+1)%6)+1}') for i in range(6)]
for u, v in edges_g1:
    x1, y1 = pos_g1[u]
    x2, y2 = pos_g1[v]
    ax1.plot([x1, x2], [y1, y2], color='#0284c7', lw=2.2, zorder=1)

ax1.set_xlim(-1.4, 1.4)
ax1.set_ylim(-1.4, 1.4)
ax1.axis('off')
ax1.text(0, -1.3, "Cycle Traversal: v1 - v2 - v3 - v4 - v5 - v6 - v1", fontsize=9.5, ha='center', color='#334155', fontweight='bold')

# Right: G2 (Shown with isomorphic cycle ordering)
ax2.set_title("Graph G2: Cycle Structure under Bijection f", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)
cycle_order_g2 = ['u1', 'u4', 'u2', 'u6', 'u3', 'u5']
pos_g2 = {u: (np.cos(ang), np.sin(ang)) for u, ang in zip(cycle_order_g2, angles)}

nx.draw_networkx_nodes(None, pos_g2, nodelist=cycle_order_g2, node_color='#fef3c7', node_size=1300, edgecolors='#d97706', linewidths=2.2, ax=ax2)
nx.draw_networkx_labels(None, pos_g2, labels={k: f'${k}$' for k in pos_g2}, font_size=11, font_weight='bold', font_color='#92400e', ax=ax2)
edges_g2 = [
    ('u1', 'u4'), ('u1', 'u5'),
    ('u2', 'u4'), ('u2', 'u6'),
    ('u3', 'u5'), ('u3', 'u6')
]
for u, v in edges_g2:
    x1, y1 = pos_g2[u]
    x2, y2 = pos_g2[v]
    ax2.plot([x1, x2], [y1, y2], color='#d97706', lw=2.2, zorder=1)

ax2.set_xlim(-1.4, 1.4)
ax2.set_ylim(-1.4, 1.4)
ax2.axis('off')
ax2.text(0, -1.3, "Cycle Traversal: u1 - u4 - u2 - u6 - u3 - u5 - u1", fontsize=9.5, ha='center', color='#334155', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "cat2_actual_q4_isomorphism.png"), bbox_inches='tight')
plt.close()
print("Generated: cat2_actual_q4_isomorphism.png")
