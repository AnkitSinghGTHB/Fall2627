"""
High-Resolution Graphic Generator for Discrete Mathematics (MAT2002) CAT-2 Suite
Renders 12 publication-grade 300 DPI figures replacing all ASCII and Mermaid diagrams.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import networkx as nx
import numpy as np

IMG_DIR = r"c:\Users\ankit\Fall2627\Discrete\notes\cat2\img"
os.makedirs(IMG_DIR, exist_ok=True)

# Common styling
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# -------------------------------------------------------------
# DIAGRAM 1: Quiz 2 Q1 Complements (G-bar and H-bar)
# -------------------------------------------------------------
def draw_quiz2_q1_complements():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), dpi=300)
    
    # Left: Complement G-bar (Two triangles joined by bridge (u1, u4))
    ax1.set_title("Complement G-Bar (2 Triangles + Bridge (u1, u4))", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)
    pos_g = {
        'u1': (0.8, 1.2), 'u3': (0.2, 0.2), 'u5': (1.4, 0.2),  # Triangle 1
        'u4': (2.4, 1.2), 'u2': (1.8, 0.2), 'u6': (3.0, 0.2)   # Triangle 2
    }
    G_bar = nx.Graph()
    G_bar.add_edges_from([
        ('u1', 'u3'), ('u3', 'u5'), ('u5', 'u1'),  # Triangle 1
        ('u2', 'u4'), ('u4', 'u6'), ('u6', 'u2'),  # Triangle 2
        ('u1', 'u4')                               # Bridge
    ])
    nx.draw_networkx_nodes(G_bar, pos_g, ax=ax1, node_color='#1e3a8a', node_size=600)
    nx.draw_networkx_labels(G_bar, pos_g, ax=ax1, font_color='white', font_size=10, font_weight='bold')
    nx.draw_networkx_edges(G_bar, pos_g, ax=ax1, edge_color='#475569', width=2)
    # Highlight bridge
    nx.draw_networkx_edges(G_bar, pos_g, edgelist=[('u1', 'u4')], ax=ax1, edge_color='#dc2626', width=2.5, style='dashed')
    ax1.text(1.6, 1.4, "Bridge (u1, u4)", color='#dc2626', fontsize=9, fontweight='bold', ha='center')
    ax1.text(1.6, -0.2, "Contains 2 Triangles (N_C3 = 2)", color='#1e3a8a', fontsize=9.5, fontweight='bold', ha='center')
    ax1.axis('off')
    ax1.set_xlim(-0.3, 3.5)
    ax1.set_ylim(-0.4, 1.7)

    # Right: Complement H-bar (6-cycle with chord (v1, v4))
    ax2.set_title("Complement H-Bar (6-Cycle + Chord (v1, v4))", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)
    cycle_order = ['v1', 'v3', 'v6', 'v4', 'v2', 'v5']
    angles = np.linspace(np.pi/2, np.pi/2 + 2*np.pi, 6, endpoint=False)
    pos_h = {cycle_order[i]: (np.cos(angles[i]), np.sin(angles[i])) for i in range(6)}
    H_bar = nx.Graph()
    for i in range(6):
        H_bar.add_edge(cycle_order[i], cycle_order[(i+1)%6])
    H_bar.add_edge('v1', 'v4') # Chord

    nx.draw_networkx_nodes(H_bar, pos_h, ax=ax2, node_color='#0284c7', node_size=600)
    nx.draw_networkx_labels(H_bar, pos_h, ax=ax2, font_color='white', font_size=10, font_weight='bold')
    nx.draw_networkx_edges(H_bar, pos_h, ax=ax2, edge_color='#475569', width=2)
    nx.draw_networkx_edges(H_bar, pos_h, edgelist=[('v1', 'v4')], ax=ax2, edge_color='#16a34a', width=2.5, style='dashed')
    ax2.text(0, 0.15, "Chord (v1, v4)", color='#16a34a', fontsize=9, fontweight='bold', ha='center')
    ax2.text(0, -1.35, "Contains 0 Triangles (N_C3 = 0) -> Non-Isomorphic!", color='#dc2626', fontsize=9.5, fontweight='bold', ha='center')
    ax2.axis('off')
    ax2.set_xlim(-1.5, 1.5)
    ax2.set_ylim(-1.5, 1.4)

    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "quiz2_q1_complements.png"), bbox_inches='tight')
    plt.close()
    print("Generated: quiz2_q1_complements.png")

# -------------------------------------------------------------
# DIAGRAM 2: Quiz 2 Q4 3-Regular Graphs (K3,3 and Y3)
# -------------------------------------------------------------
def draw_quiz2_q4_regular():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), dpi=300)

    # Left: K_3,3 Complete Bipartite
    ax1.set_title("Complete Bipartite K3,3 (3-Regular, Bipartite)", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)
    pos_k = {
        'u1': (0, 2), 'u2': (1, 2), 'u3': (2, 2),
        'v1': (0, 0), 'v2': (1, 0), 'v3': (2, 0)
    }
    K33 = nx.Graph()
    for u in ['u1', 'u2', 'u3']:
        for v in ['v1', 'v2', 'v3']:
            K33.add_edge(u, v)
    nx.draw_networkx_nodes(K33, pos_k, nodelist=['u1', 'u2', 'u3'], ax=ax1, node_color='#2563eb', node_size=600)
    nx.draw_networkx_nodes(K33, pos_k, nodelist=['v1', 'v2', 'v3'], ax=ax1, node_color='#0284c7', node_size=600)
    nx.draw_networkx_labels(K33, pos_k, ax=ax1, font_color='white', font_size=10, font_weight='bold')
    nx.draw_networkx_edges(K33, pos_k, ax=ax1, edge_color='#64748b', width=1.8, alpha=0.85)
    ax1.text(1, -0.45, "n = 6, m = 9, deg(v) = 3 for all v", fontsize=9.5, fontweight='bold', ha='center', color='#1e293b')
    ax1.axis('off')
    ax1.set_xlim(-0.5, 2.5)
    ax1.set_ylim(-0.6, 2.4)

    # Right: Triangular Prism Y_3 (K_3 x K_2)
    ax2.set_title("Triangular Prism Y3 (K3 x K2, 3-Regular, Planar)", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)
    pos_y = {
        'u1': (0, 1.8), 'u2': (-1.2, 0.4), 'u3': (1.2, 0.4),   # Outer Triangle
        'v1': (0, 1.0), 'v2': (-0.6, 0.0), 'v3': (0.6, 0.0)    # Inner Triangle
    }
    Y3 = nx.Graph()
    Y3.add_edges_from([
        ('u1', 'u2'), ('u2', 'u3'), ('u3', 'u1'),  # Outer
        ('v1', 'v2'), ('v2', 'v3'), ('v3', 'u1'),  # Inner
        ('u1', 'v1'), ('u2', 'v2'), ('u3', 'v3')   # Matching
    ])
    nx.draw_networkx_nodes(Y3, pos_y, nodelist=['u1', 'u2', 'u3'], ax=ax2, node_color='#7c3aed', node_size=600)
    nx.draw_networkx_nodes(Y3, pos_y, nodelist=['v1', 'v2', 'v3'], ax=ax2, node_color='#a855f7', node_size=600)
    nx.draw_networkx_labels(Y3, pos_y, ax=ax2, font_color='white', font_size=10, font_weight='bold')
    nx.draw_networkx_edges(Y3, pos_y, ax=ax2, edge_color='#64748b', width=1.8)
    nx.draw_networkx_edges(Y3, pos_y, edgelist=[('u1','v1'), ('u2','v2'), ('u3','v3')], ax=ax2, edge_color='#ec4899', width=2.2)
    ax2.text(0, -0.45, "Two triangles connected by matching edges", fontsize=9.5, fontweight='bold', ha='center', color='#1e293b')
    ax2.axis('off')
    ax2.set_xlim(-1.6, 1.6)
    ax2.set_ylim(-0.6, 2.2)

    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "quiz2_q4_regular_graphs.png"), bbox_inches='tight')
    plt.close()
    print("Generated: quiz2_q4_regular_graphs.png")

# -------------------------------------------------------------
# DIAGRAM 3: Quiz 2 Q8 C6 vs 2C3
# -------------------------------------------------------------
def draw_quiz2_q8_c6_vs_2c3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.5), dpi=300)

    # Left: C6 (Single 6-cycle)
    ax1.set_title("Graph G1 = C6 (Connected, 1 Component)", fontsize=11, fontweight='bold', color='#1e3a8a', pad=10)
    c6_nodes = ['1', '2', '3', '4', '5', '6']
    angles = np.linspace(np.pi/2, np.pi/2 + 2*np.pi, 6, endpoint=False)
    pos_c6 = {c6_nodes[i]: (np.cos(angles[i]), np.sin(angles[i])) for i in range(6)}
    G1 = nx.cycle_graph(6)
    mapping = {i: str(i+1) for i in range(6)}
    G1 = nx.relabel_nodes(G1, mapping)
    nx.draw_networkx_nodes(G1, pos_c6, ax=ax1, node_color='#2563eb', node_size=550)
    nx.draw_networkx_labels(G1, pos_c6, ax=ax1, font_color='white', font_size=10, font_weight='bold')
    nx.draw_networkx_edges(G1, pos_c6, ax=ax1, edge_color='#334155', width=2)
    ax1.text(0, -1.3, "|V|=6, |E|=6, c(G1) = 1 (Connected)", color='#1e3a8a', fontsize=9.5, fontweight='bold', ha='center')
    ax1.axis('off')
    ax1.set_xlim(-1.4, 1.4)
    ax1.set_ylim(-1.4, 1.4)

    # Right: 2C3 (Two disjoint triangles)
    ax2.set_title("Graph G2 = 2C3 (Disconnected, 2 Components)", fontsize=11, fontweight='bold', color='#dc2626', pad=10)
    pos_2c3 = {
        'a': (-1.4, 0.8), 'b': (-2.1, -0.4), 'c': (-0.7, -0.4),
        'd': (1.4, 0.8), 'e': (0.7, -0.4), 'f': (2.1, -0.4)
    }
    G2 = nx.Graph()
    G2.add_edges_from([('a','b'), ('b','c'), ('c','a'), ('d','e'), ('e','f'), ('f','d')])
    nx.draw_networkx_nodes(G2, pos_2c3, ax=ax2, node_color='#dc2626', node_size=550)
    nx.draw_networkx_labels(G2, pos_2c3, ax=ax2, font_color='white', font_size=10, font_weight='bold')
    nx.draw_networkx_edges(G2, pos_2c3, ax=ax2, edge_color='#334155', width=2)
    ax2.text(0, -1.3, "|V|=6, |E|=6, c(G2) = 2 (Disconnected) -> G1 != G2", color='#dc2626', fontsize=9.5, fontweight='bold', ha='center')
    ax2.axis('off')
    ax2.set_xlim(-2.5, 2.5)
    ax2.set_ylim(-1.4, 1.4)

    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "quiz2_q8_c6_vs_2c3.png"), bbox_inches='tight')
    plt.close()
    print("Generated: quiz2_q8_c6_vs_2c3.png")

# -------------------------------------------------------------
# DIAGRAM 4: Quiz 2 Q8 P4 vs K1,3
# -------------------------------------------------------------
def draw_quiz2_q8_p4_vs_k13():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4), dpi=300)

    # Left: Path P4
    ax1.set_title("Path Graph P4 (Max Degree = 2)", fontsize=11, fontweight='bold', color='#1e3a8a', pad=10)
    pos_p4 = {'1': (0, 0), '2': (1, 0), '3': (2, 0), '4': (3, 0)}
    P4 = nx.path_graph(4)
    P4 = nx.relabel_nodes(P4, {i: str(i+1) for i in range(4)})
    nx.draw_networkx_nodes(P4, pos_p4, ax=ax1, node_color='#0284c7', node_size=550)
    nx.draw_networkx_labels(P4, pos_p4, ax=ax1, font_color='white', font_size=10, font_weight='bold')
    nx.draw_networkx_edges(P4, pos_p4, ax=ax1, edge_color='#334155', width=2.2)
    ax1.text(1.5, -0.6, "Degree sequence: (2, 2, 1, 1)", color='#1e3a8a', fontsize=9.5, fontweight='bold', ha='center')
    ax1.axis('off')
    ax1.set_xlim(-0.5, 3.5)
    ax1.set_ylim(-0.8, 0.8)

    # Right: Star K1,3
    ax2.set_title("Star Graph K1,3 (Max Degree = 3)", fontsize=11, fontweight='bold', color='#7c3aed', pad=10)
    pos_k13 = {'c': (1.5, 0), 'l1': (1.5, 0.8), 'l2': (0.7, -0.6), 'l3': (2.3, -0.6)}
    K13 = nx.star_graph(3)
    K13 = nx.relabel_nodes(K13, {0: 'c', 1: 'l1', 2: 'l2', 3: 'l3'})
    nx.draw_networkx_nodes(K13, pos_k13, nodelist=['c'], ax=ax2, node_color='#7c3aed', node_size=650)
    nx.draw_networkx_nodes(K13, pos_k13, nodelist=['l1','l2','l3'], ax=ax2, node_color='#a855f7', node_size=500)
    nx.draw_networkx_labels(K13, pos_k13, ax=ax2, font_color='white', font_size=10, font_weight='bold')
    nx.draw_networkx_edges(K13, pos_k13, ax=ax2, edge_color='#334155', width=2.2)
    ax2.text(1.5, -0.9, "Degree sequence: (3, 1, 1, 1) -> P4 != K1,3", color='#7c3aed', fontsize=9.5, fontweight='bold', ha='center')
    ax2.axis('off')
    ax2.set_xlim(0.2, 2.8)
    ax2.set_ylim(-1.1, 1.1)

    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "quiz2_q8_p4_vs_k13.png"), bbox_inches='tight')
    plt.close()
    print("Generated: quiz2_q8_p4_vs_k13.png")

# -------------------------------------------------------------
# DIAGRAM 5: Tutorial 4 Problem 1 Shortest Path Tree
# -------------------------------------------------------------
def draw_tut4_p1_tree():
    fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)
    ax.set_title("Dijkstra Shortest Path Tree from Source S (Problem 1)", fontsize=12, fontweight='bold', color='#1e3a8a', pad=15)
    
    pos = {
        's': (0, 3.0),
        'a': (0, 1.8),
        'b': (-1.8, 0.6),
        'c': (1.8, 0.6),
        'd': (0, 0.6),
        'e': (0, -0.7)
    }
    
    labels_dist = {
        's': 's\n[d=0]',
        'a': 'a\n[d=1]',
        'b': 'b\n[d=3]',
        'c': 'c\n[d=3]',
        'd': 'd\n[d=2]',
        'e': 'e\n[d=4]'
    }

    tree_edges = [('s', 'a', 1), ('a', 'b', 2), ('a', 'c', 2), ('a', 'd', 1), ('d', 'e', 2)]
    
    # Draw nodes
    for node, (x, y) in pos.items():
        circle = patches.Circle((x, y), 0.35, facecolor='#eff6ff', edgecolor='#2563eb', linewidth=2.5, zorder=3)
        ax.add_patch(circle)
        ax.text(x, y, labels_dist[node], ha='center', va='center', fontsize=9, fontweight='bold', color='#1e3a8a', zorder=4)

    # Draw directed edges
    for u, v, w in tree_edges:
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        dx = x2 - x1
        dy = y2 - y1
        dist = np.sqrt(dx**2 + dy**2)
        start_x = x1 + dx * (0.35 / dist)
        start_y = y1 + dy * (0.35 / dist)
        end_x = x2 - dx * (0.38 / dist)
        end_y = y2 - dy * (0.38 / dist)
        
        ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                    arrowprops=dict(facecolor='#1e293b', edgecolor='#1e293b', width=2, headwidth=8, shrink=0),
                    zorder=2)
        mx, my = (start_x + end_x) / 2, (start_y + end_y) / 2
        offset_x = 0.15 if dx == 0 else 0
        offset_y = 0.12 if dy == 0 else 0
        bbox_props = dict(boxstyle="circle,pad=0.2", fc="#fef3c7", ec="#f59e0b", lw=1.5)
        ax.text(mx + offset_x, my + offset_y, str(w), ha='center', va='center', fontsize=9, fontweight='bold', color='#b45309', bbox=bbox_props, zorder=5)

    ax.text(0, -1.2, "Optimal Paths: s->a (1), s->a->b (3), s->a->c (3), s->a->d (2), s->a->d->e (4)",
            ha='center', fontsize=9.5, fontweight='bold', color='#0f172a')

    ax.set_xlim(-2.6, 2.6)
    ax.set_ylim(-1.4, 3.6)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "tutorial4_p1_shortest_tree.png"), bbox_inches='tight')
    plt.close()
    print("Generated: tutorial4_p1_shortest_tree.png")

# -------------------------------------------------------------
# DIAGRAM 6: Tutorial 4 Problem 2 Shortest Path Tree
# -------------------------------------------------------------
def draw_tut4_p2_tree():
    fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
    ax.set_title("Dijkstra Shortest Path Tree from Source 1 (Problem 2)", fontsize=12, fontweight='bold', color='#1e3a8a', pad=15)
    
    pos = {
        '1': (0, 2.2),
        '4': (0, 0.9),
        '2': (-1.4, -0.4),
        '3': (1.4, -0.4),
        '5': (2.4, 1.5)
    }
    
    labels_dist = {
        '1': '1\n[d=0]',
        '4': '4\n[d=3]',
        '2': '2\n[d=4]',
        '3': '3\n[d=4]'
    }

    tree_edges = [('1', '4', 3), ('4', '2', 1), ('4', '3', 1)]
    
    for node in ['1', '4', '2', '3']:
        x, y = pos[node]
        circle = patches.Circle((x, y), 0.35, facecolor='#eff6ff', edgecolor='#2563eb', linewidth=2.5, zorder=3)
        ax.add_patch(circle)
        ax.text(x, y, labels_dist[node], ha='center', va='center', fontsize=9, fontweight='bold', color='#1e3a8a', zorder=4)

    for u, v, w in tree_edges:
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        dx = x2 - x1
        dy = y2 - y1
        dist = np.sqrt(dx**2 + dy**2)
        start_x = x1 + dx * (0.35 / dist)
        start_y = y1 + dy * (0.35 / dist)
        end_x = x2 - dx * (0.38 / dist)
        end_y = y2 - dy * (0.38 / dist)
        
        ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                    arrowprops=dict(facecolor='#1e293b', edgecolor='#1e293b', width=2, headwidth=8, shrink=0),
                    zorder=2)
        mx, my = (start_x + end_x) / 2, (start_y + end_y) / 2
        bbox_props = dict(boxstyle="circle,pad=0.2", fc="#fef3c7", ec="#f59e0b", lw=1.5)
        ax.text(mx + (0.15 if dx==0 else 0), my, str(w), ha='center', va='center', fontsize=9, fontweight='bold', color='#b45309', bbox=bbox_props, zorder=5)

    x5, y5 = pos['5']
    circle5 = patches.Circle((x5, y5), 0.45, facecolor='#fee2e2', edgecolor='#dc2626', linewidth=2.5, linestyle='--', zorder=3)
    ax.add_patch(circle5)
    ax.text(x5, y5, "5\n[d=inf]\nUnreachable", ha='center', va='center', fontsize=8, fontweight='bold', color='#991b1b', zorder=4)
    ax.text(x5, y5 - 0.7, "In-degree deg-(5) = 0", ha='center', fontsize=8.5, fontweight='bold', color='#dc2626')

    ax.text(0, -1.0, "Optimal Paths: 1->4 (3), 1->4->2 (4), 1->4->3 (4), Vertex 5 is Unreachable (d(5)=inf)",
            ha='center', fontsize=9.5, fontweight='bold', color='#0f172a')

    ax.set_xlim(-2.2, 3.4)
    ax.set_ylim(-1.2, 2.8)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "tutorial4_p2_shortest_tree.png"), bbox_inches='tight')
    plt.close()
    print("Generated: tutorial4_p2_shortest_tree.png")

# -------------------------------------------------------------
# DIAGRAM 7: Tutorial 2 Q4 D12 Hasse Diagram
# -------------------------------------------------------------
def draw_tut2_q4_d12():
    fig, ax = plt.subplots(figsize=(6.5, 6), dpi=300)
    ax.set_title("Hasse Diagram of Divisor Lattice (D12, |)", fontsize=12, fontweight='bold', color='#1e3a8a', pad=15)

    pos = {
        '1': (0, 0),
        '2': (-1.0, 1.2), '3': (1.0, 1.2),
        '4': (-1.0, 2.4), '6': (1.0, 2.4),
        '12': (0, 3.6)
    }

    edges = [('1', '2'), ('1', '3'), ('2', '4'), ('2', '6'), ('3', '6'), ('4', '12'), ('6', '12')]

    for u, v in edges:
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        ax.plot([x1, x2], [y1, y2], color='#475569', lw=2.2, zorder=1)

    for node, (x, y) in pos.items():
        if node == '12':
            fc, ec, tc = '#dbeafe', '#1d4ed8', '#1e3a8a'
            sub = " (Top / 1)"
        elif node == '1':
            fc, ec, tc = '#fef3c7', '#d97706', '#92400e'
            sub = " (Bottom / 0)"
        else:
            fc, ec, tc = '#f8fafc', '#64748b', '#0f172a'
            sub = ""
        
        circle = patches.Circle((x, y), 0.28, facecolor=fc, edgecolor=ec, linewidth=2.2, zorder=2)
        ax.add_patch(circle)
        ax.text(x, y, node, ha='center', va='center', fontsize=11, fontweight='bold', color=tc, zorder=3)
        if sub:
            ax.text(x + 0.35, y, sub, ha='left', va='center', fontsize=8.5, fontweight='bold', color=tc)

    ax.text(0, -0.6, "D12 is a Bounded Distributive Lattice, but NOT Complemented (2 and 6 lack complements)",
            ha='center', fontsize=8.8, fontweight='bold', color='#dc2626')

    ax.set_xlim(-1.8, 2.2)
    ax.set_ylim(-0.8, 4.0)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "tutorial2_q4_d12_hasse.png"), bbox_inches='tight')
    plt.close()
    print("Generated: tutorial2_q4_d12_hasse.png")

# -------------------------------------------------------------
# DIAGRAM 8: Module 3 D30 Hasse Diagram
# -------------------------------------------------------------
def draw_module3_d30():
    fig, ax = plt.subplots(figsize=(7.5, 6.5), dpi=300)
    ax.set_title("Hasse Diagram of D30 (Isomorphic to Boolean Algebra B3)", fontsize=12, fontweight='bold', color='#1e3a8a', pad=15)

    pos = {
        '1': (0, 0),
        '2': (-1.6, 1.2), '3': (0, 1.2), '5': (1.6, 1.2),
        '6': (-1.6, 2.6), '10': (0, 2.6), '15': (1.6, 2.6),
        '30': (0, 3.8)
    }

    edges = [
        ('1', '2'), ('1', '3'), ('1', '5'),
        ('2', '6'), ('2', '10'),
        ('3', '6'), ('3', '15'),
        ('5', '10'), ('5', '15'),
        ('6', '30'), ('10', '30'), ('15', '30')
    ]

    for u, v in edges:
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        ax.plot([x1, x2], [y1, y2], color='#64748b', lw=1.8, zorder=1)

    for node, (x, y) in pos.items():
        fc = '#dbeafe' if node in ['1', '30'] else '#f8fafc'
        ec = '#1d4ed8' if node in ['1', '30'] else '#475569'
        circle = patches.Circle((x, y), 0.32, facecolor=fc, edgecolor=ec, linewidth=2.2, zorder=2)
        ax.add_patch(circle)
        ax.text(x, y, node, ha='center', va='center', fontsize=10.5, fontweight='bold', color='#0f172a', zorder=3)

    ax.text(0, -0.55, "Square-free 30 = 2 x 3 x 5 -> Complemented & Distributive -> Boolean Algebra",
            ha='center', fontsize=9, fontweight='bold', color='#16a34a')

    ax.set_xlim(-2.4, 2.4)
    ax.set_ylim(-0.7, 4.2)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "module3_d30_hasse.png"), bbox_inches='tight')
    plt.close()
    print("Generated: module3_d30_hasse.png")

# -------------------------------------------------------------
# DIAGRAM 9: Module 3 Lattice Fails (Fail 1 & Fail 2)
# -------------------------------------------------------------
def draw_module3_lattice_fails():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.5), dpi=300)

    # Fail 1: Two Separate Roofs
    ax1.set_title("Fail 1: Two Separate Roofs (No Unique LUB)", fontsize=10.5, fontweight='bold', color='#dc2626', pad=10)
    pos1 = {'a': (-0.6, 0.2), 'b': (0.6, 0.2), 'c': (-0.6, 1.6), 'd': (0.6, 1.6)}
    edges1 = [('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd')]
    for u, v in edges1:
        ax1.plot([pos1[u][0], pos1[v][0]], [pos1[u][1], pos1[v][1]], color='#94a3b8', lw=2)
    for node, (x, y) in pos1.items():
        fc = '#fee2e2' if node in ['c', 'd'] else '#f8fafc'
        ec = '#dc2626' if node in ['c', 'd'] else '#475569'
        circle = patches.Circle((x, y), 0.22, facecolor=fc, edgecolor=ec, linewidth=2, zorder=2)
        ax1.add_patch(circle)
        ax1.text(x, y, node, ha='center', va='center', fontsize=10, fontweight='bold', color='#0f172a', zorder=3)
    ax1.text(0, -0.3, "Both c and d are minimal upper bounds of {a, b}. No lowest roof!", ha='center', fontsize=8.5, color='#991b1b', fontweight='bold')
    ax1.axis('off')
    ax1.set_xlim(-1.2, 1.2)
    ax1.set_ylim(-0.5, 2.0)

    # Fail 2: Two Separate Basements
    ax2.set_title("Fail 2: Two Separate Basements (No Unique GLB)", fontsize=10.5, fontweight='bold', color='#dc2626', pad=10)
    pos2 = {'a': (-0.6, 0.2), 'b': (0.6, 0.2), 'c': (-0.6, 1.6), 'd': (0.6, 1.6)}
    edges2 = [('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd')]
    for u, v in edges2:
        ax2.plot([pos2[u][0], pos2[u][1]], [pos2[v][0], pos2[v][1]], color='#94a3b8', lw=2)
    for node, (x, y) in pos2.items():
        fc = '#fee2e2' if node in ['a', 'b'] else '#f8fafc'
        ec = '#dc2626' if node in ['a', 'b'] else '#475569'
        circle = patches.Circle((x, y), 0.22, facecolor=fc, edgecolor=ec, linewidth=2, zorder=2)
        ax2.add_patch(circle)
        ax2.text(x, y, node, ha='center', va='center', fontsize=10, fontweight='bold', color='#0f172a', zorder=3)
    ax2.text(0, -0.3, "Both a and b are maximal lower bounds of {c, d}. No highest basement!", ha='center', fontsize=8.5, color='#991b1b', fontweight='bold')
    ax2.axis('off')
    ax2.set_xlim(-1.2, 1.2)
    ax2.set_ylim(-0.5, 2.0)

    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "module3_lattice_fails.png"), bbox_inches='tight')
    plt.close()
    print("Generated: module3_lattice_fails.png")

# -------------------------------------------------------------
# DIAGRAM 10: Module 3 M3 & N5 Lattices
# -------------------------------------------------------------
def draw_module3_m3_n5():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 5), dpi=300)

    # Left: Diamond M3
    ax1.set_title("Diamond Lattice M3 (Modular, Non-Distributive)", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)
    pos1 = {'0': (0, 0), 'a': (-1.0, 1.3), 'b': (0, 1.3), 'c': (1.0, 1.3), '1': (0, 2.6)}
    edges1 = [('0','a'), ('0','b'), ('0','c'), ('a','1'), ('b','1'), ('c','1')]
    for u, v in edges1:
        ax1.plot([pos1[u][0], pos1[v][0]], [pos1[u][1], pos1[v][1]], color='#475569', lw=2)
    for node, (x, y) in pos1.items():
        circle = patches.Circle((x, y), 0.22, facecolor='#eff6ff', edgecolor='#2563eb', linewidth=2, zorder=2)
        ax1.add_patch(circle)
        ax1.text(x, y, node, ha='center', va='center', fontsize=10, fontweight='bold', color='#1e3a8a', zorder=3)
    ax1.text(0, -0.4, "a ^ (b v c) = a ^ 1 = a != (a ^ b) v (a ^ c) = 0", ha='center', fontsize=8.5, color='#dc2626', fontweight='bold')
    ax1.axis('off')
    ax1.set_xlim(-1.6, 1.6)
    ax1.set_ylim(-0.6, 2.9)

    # Right: Pentagon N5
    ax2.set_title("Pentagon Lattice N5 (Non-Modular, Non-Distributive)", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)
    pos2 = {'0': (0, 0), 'a': (-0.9, 0.9), 'b': (-0.9, 1.8), 'c': (0.9, 1.35), '1': (0, 2.6)}
    edges2 = [('0','a'), ('a','b'), ('b','1'), ('0','c'), ('c','1')]
    for u, v in edges2:
        ax2.plot([pos2[u][0], pos2[v][0]], [pos2[u][1], pos2[v][1]], color='#475569', lw=2)
    for node, (x, y) in pos2.items():
        circle = patches.Circle((x, y), 0.22, facecolor='#eff6ff', edgecolor='#2563eb', linewidth=2, zorder=2)
        ax2.add_patch(circle)
        ax2.text(x, y, node, ha='center', va='center', fontsize=10, fontweight='bold', color='#1e3a8a', zorder=3)
    ax2.text(0, -0.4, "b ^ (a v c) = b ^ 1 = b != (b ^ a) v (b ^ c) = a", ha='center', fontsize=8.5, color='#dc2626', fontweight='bold')
    ax2.axis('off')
    ax2.set_xlim(-1.6, 1.6)
    ax2.set_ylim(-0.6, 2.9)

    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "module3_m3_n5_lattices.png"), bbox_inches='tight')
    plt.close()
    print("Generated: module3_m3_n5_lattices.png")

# -------------------------------------------------------------
# DIAGRAM 11: Module 3 Switching Circuits (Series & Parallel)
# -------------------------------------------------------------
def draw_module3_switching():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4.5), dpi=300)

    # Top: Series AND Circuit
    ax1.set_title("Series Connection (AND Operation: T = A . B)", fontsize=11, fontweight='bold', color='#1e3a8a', pad=8)
    ax1.plot([0, 1.0], [0, 0], color='#1e293b', lw=2.5)
    rect_a = patches.Rectangle((1.0, -0.25), 1.0, 0.5, fc='#eff6ff', ec='#2563eb', lw=2)
    ax1.add_patch(rect_a)
    ax1.text(1.5, 0, "Switch A", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1e3a8a')
    ax1.plot([2.0, 3.0], [0, 0], color='#1e293b', lw=2.5)
    rect_b = patches.Rectangle((3.0, -0.25), 1.0, 0.5, fc='#eff6ff', ec='#2563eb', lw=2)
    ax1.add_patch(rect_b)
    ax1.text(3.5, 0, "Switch B", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1e3a8a')
    ax1.plot([4.0, 5.0], [0, 0], color='#1e293b', lw=2.5)
    ax1.plot(0, 0, 'o', color='#1e293b', ms=7)
    ax1.plot(5, 0, 'o', color='#1e293b', ms=7)
    ax1.text(-0.15, 0, "IN", ha='right', va='center', fontsize=9, fontweight='bold', color='#475569')
    ax1.text(5.15, 0, "OUT", ha='left', va='center', fontsize=9, fontweight='bold', color='#475569')
    ax1.axis('off')
    ax1.set_xlim(-0.8, 5.8)
    ax1.set_ylim(-0.6, 0.6)

    # Bottom: Parallel OR Circuit
    ax2.set_title("Parallel Connection (OR Operation: T = A + B)", fontsize=11, fontweight='bold', color='#1e3a8a', pad=8)
    ax2.plot([0, 0.8], [0, 0], color='#1e293b', lw=2.5)
    ax2.plot([0.8, 0.8], [-0.6, 0.6], color='#1e293b', lw=2.5)
    ax2.plot([0.8, 1.5], [0.6, 0.6], color='#1e293b', lw=2.5)
    rect_a2 = patches.Rectangle((1.5, 0.35), 1.2, 0.5, fc='#eff6ff', ec='#2563eb', lw=2)
    ax2.add_patch(rect_a2)
    ax2.text(2.1, 0.6, "Switch A", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1e3a8a')
    ax2.plot([2.7, 3.4], [0.6, 0.6], color='#1e293b', lw=2.5)
    ax2.plot([0.8, 1.5], [-0.6, -0.6], color='#1e293b', lw=2.5)
    rect_b2 = patches.Rectangle((1.5, -0.85), 1.2, 0.5, fc='#eff6ff', ec='#2563eb', lw=2)
    ax2.add_patch(rect_b2)
    ax2.text(2.1, -0.6, "Switch B", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1e3a8a')
    ax2.plot([2.7, 3.4], [-0.6, -0.6], color='#1e293b', lw=2.5)
    ax2.plot([3.4, 3.4], [-0.6, 0.6], color='#1e293b', lw=2.5)
    ax2.plot([3.4, 4.2], [0, 0], color='#1e293b', lw=2.5)
    ax2.plot(0, 0, 'o', color='#1e293b', ms=7)
    ax2.plot(4.2, 0, 'o', color='#1e293b', ms=7)
    ax2.text(-0.15, 0, "IN", ha='right', va='center', fontsize=9, fontweight='bold', color='#475569')
    ax2.text(4.35, 0, "OUT", ha='left', va='center', fontsize=9, fontweight='bold', color='#475569')
    ax2.axis('off')
    ax2.set_xlim(-0.8, 5.0)
    ax2.set_ylim(-1.1, 1.1)

    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "module3_switching_circuits.png"), bbox_inches='tight')
    plt.close()
    print("Generated: module3_switching_circuits.png")

# -------------------------------------------------------------
# DIAGRAM 12: Module 4 Bipartite vs Odd Cycle
# -------------------------------------------------------------
def draw_module4_bipartite_odd():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.5), dpi=300)

    # Left: Bipartite Graph
    ax1.set_title("Bipartite Graph (2-Colorable, Even Cycles Only)", fontsize=10.5, fontweight='bold', color='#1e3a8a', pad=10)
    pos1 = {
        'v1': (-0.8, 1.0), 'v2': (-0.8, 0.0), 'v3': (-0.8, -1.0),
        'u1': (0.8, 0.6), 'u2': (0.8, -0.6)
    }
    B_graph = nx.Graph()
    B_graph.add_edges_from([('v1', 'u1'), ('v2', 'u1'), ('v2', 'u2'), ('v3', 'u2')])
    nx.draw_networkx_nodes(B_graph, pos1, nodelist=['v1', 'v2', 'v3'], ax=ax1, node_color='#ef4444', node_size=550)
    nx.draw_networkx_nodes(B_graph, pos1, nodelist=['u1', 'u2'], ax=ax1, node_color='#3b82f6', node_size=550)
    nx.draw_networkx_labels(B_graph, pos1, ax=ax1, font_color='white', font_size=10, font_weight='bold')
    nx.draw_networkx_edges(B_graph, pos1, ax=ax1, edge_color='#64748b', width=2)
    ax1.text(-0.8, 1.4, "Set V1 (Red)", color='#b91c1c', fontsize=9.5, fontweight='bold', ha='center')
    ax1.text(0.8, 1.4, "Set V2 (Blue)", color='#1d4ed8', fontsize=9.5, fontweight='bold', ha='center')
    ax1.text(0, -1.5, "No edges within the same color set", color='#16a34a', fontsize=9, fontweight='bold', ha='center')
    ax1.axis('off')
    ax1.set_xlim(-1.4, 1.4)
    ax1.set_ylim(-1.7, 1.7)

    # Right: Odd Cycle Triangle (Conflict)
    ax2.set_title("Odd Cycle C3 (Non-Bipartite, Color Conflict)", fontsize=10.5, fontweight='bold', color='#dc2626', pad=10)
    pos2 = {'1': (0, 1.0), '2': (-0.9, -0.5), '3': (0.9, -0.5)}
    C3 = nx.cycle_graph(3)
    C3 = nx.relabel_nodes(C3, {0: '1', 1: '2', 2: '3'})
    nx.draw_networkx_nodes(C3, pos2, nodelist=['1'], ax=ax2, node_color='#ef4444', node_size=600)
    nx.draw_networkx_nodes(C3, pos2, nodelist=['2'], ax=ax2, node_color='#3b82f6', node_size=600)
    nx.draw_networkx_nodes(C3, pos2, nodelist=['3'], ax=ax2, node_color='#a855f7', node_size=600)
    nx.draw_networkx_labels(C3, pos2, ax=ax2, font_color='white', font_size=10, font_weight='bold')
    nx.draw_networkx_edges(C3, pos2, ax=ax2, edge_color='#64748b', width=2.2)
    ax2.text(0, 1.35, "1 (Red)", color='#b91c1c', fontsize=9, fontweight='bold', ha='center')
    ax2.text(-0.9, -0.85, "2 (Blue)", color='#1d4ed8', fontsize=9, fontweight='bold', ha='center')
    ax2.text(0.9, -0.85, "3 (Conflict!)", color='#7c3aed', fontsize=9, fontweight='bold', ha='center')
    ax2.text(0, -1.5, "Cannot color vertex 3 with Red or Blue", color='#dc2626', fontsize=9, fontweight='bold', ha='center')
    ax2.axis('off')
    ax2.set_xlim(-1.5, 1.5)
    ax2.set_ylim(-1.7, 1.7)

    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "module4_bipartite_vs_odd_cycle.png"), bbox_inches='tight')
    plt.close()
    print("Generated: module4_bipartite_vs_odd_cycle.png")

if __name__ == "__main__":
    print("Generating all 12 Discrete Mathematics Figures...")
    draw_quiz2_q1_complements()
    draw_quiz2_q4_regular()
    draw_quiz2_q8_c6_vs_2c3()
    draw_quiz2_q8_p4_vs_k13()
    draw_tut4_p1_tree()
    draw_tut4_p2_tree()
    draw_tut2_q4_d12()
    draw_module3_d30()
    draw_module3_lattice_fails()
    draw_module3_m3_n5()
    draw_module3_switching()
    draw_module4_bipartite_odd()
    print("All 12 Figures Generated Successfully!")
