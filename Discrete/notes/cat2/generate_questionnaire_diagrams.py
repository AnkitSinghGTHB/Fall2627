import os
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

IMG_DIR = r"c:\Users\ankit\Fall2627\Discrete\notes\cat2\img"
os.makedirs(IMG_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# 1. Question 13: Graph Matrix Representation (4 vertices, 5 edges: square + diagonal chord)
def draw_q13_graph():
    fig, ax = plt.subplots(figsize=(6, 5), dpi=300)
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3, 4])
    edges = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]
    G.add_edges_from(edges)
    
    pos = {
        1: (0, 1),
        2: (1, 1),
        3: (1, 0),
        4: (0, 0)
    }
    
    ax.set_title("Question 13: Graph G for Adjacency/Incidence Matrices\nWalks Between Vertex 1 and Vertex 3", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)
    
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color='#1e3a8a', node_size=700)
    nx.draw_networkx_labels(G, pos, ax=ax, font_color='white', font_size=11, font_weight='bold')
    
    # Outer cycle edges
    outer_edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
    nx.draw_networkx_edges(G, pos, edgelist=outer_edges, ax=ax, edge_color='#475569', width=2.5)
    
    # Diagonal chord (1, 3) highlighted
    nx.draw_networkx_edges(G, pos, edgelist=[(1, 3)], ax=ax, edge_color='#dc2626', width=2.8, style='dashed')
    
    # Edge labels
    edge_labels = {
        (1, 2): 'e1',
        (2, 3): 'e2',
        (3, 4): 'e3',
        (4, 1): 'e4',
        (1, 3): 'e5 (chord)'
    }
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax, font_color='#0f172a', font_size=9, font_weight='bold')
    
    ax.text(0.5, -0.25, "Walks of Length 2: 1->2->3 and 1->4->3 ((A^2)_{1,3} = 2)\nWalks of Length 3: (A^3)_{1,3} = 5", 
            ha='center', fontsize=9.5, fontweight='bold', color='#1e293b', 
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#eff6ff', edgecolor='#2563eb', alpha=0.9))
    
    ax.axis('off')
    ax.set_xlim(-0.3, 1.3)
    ax.set_ylim(-0.4, 1.3)
    plt.tight_layout()
    out_path = os.path.join(IMG_DIR, "questionnaire_q13_walks_graph.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"Generated: {out_path}")

# 2. Question 11: 5-Cycle with Chord (1, 3) showing 2-coloring odd-cycle conflict
def draw_q11_odd_cycle():
    fig, ax = plt.subplots(figsize=(6, 5), dpi=300)
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3, 4, 5])
    edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3)]
    G.add_edges_from(edges)
    
    angles = np.linspace(np.pi/2, np.pi/2 + 2*np.pi, 5, endpoint=False)
    pos = {i+1: (np.cos(angles[i]), np.sin(angles[i])) for i in range(5)}
    
    ax.set_title("Question 11: 2-Coloring Conflict in Graph G\nTriangle Cycle (1-2-3) Violates Bipartiteness", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)
    
    # 2-Coloring attempt: 1=Red, 2=Blue, 5=Blue, 3=Blue (conflict with 2!)
    color_map = {1: '#dc2626', 2: '#2563eb', 3: '#2563eb', 4: '#94a3b8', 5: '#2563eb'}
    node_colors = [color_map[node] for node in G.nodes()]
    
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_colors, node_size=650)
    nx.draw_networkx_labels(G, pos, ax=ax, font_color='white', font_size=11, font_weight='bold')
    
    # Cycle edges
    nx.draw_networkx_edges(G, pos, edgelist=[(1, 2), (3, 4), (4, 5), (5, 1)], ax=ax, edge_color='#64748b', width=2)
    
    # Chord edge (1, 3)
    nx.draw_networkx_edges(G, pos, edgelist=[(1, 3)], ax=ax, edge_color='#ea580c', width=2.5, style='dotted')
    
    # Monochromatic conflicting edge (2, 3) between BLUE and BLUE!
    nx.draw_networkx_edges(G, pos, edgelist=[(2, 3)], ax=ax, edge_color='#dc2626', width=3.5)
    
    ax.text(0, -1.35, "CONFLICT: Edge (2, 3) connects two BLUE vertices!\nOdd Cycle (1-2-3-1) of length 3 => NOT BIPARTITE", 
            ha='center', fontsize=9.5, fontweight='bold', color='#991b1b',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#fef2f2', edgecolor='#dc2626', alpha=0.9))
    
    ax.axis('off')
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.5, 1.3)
    plt.tight_layout()
    out_path = os.path.join(IMG_DIR, "questionnaire_q11_odd_cycle_graph.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"Generated: {out_path}")

# 3. Blueprint 10: Non-Planarity Proofs (K5 and K3,3)
def draw_blueprint10_planarity():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), dpi=300)
    
    # K_5
    ax1.set_title("K5 Complete Graph (Non-Planar: e=10 > 3v-6=9)", fontsize=10.5, fontweight='bold', color='#1e3a8a', pad=10)
    K5 = nx.complete_graph(5)
    angles = np.linspace(np.pi/2, np.pi/2 + 2*np.pi, 5, endpoint=False)
    pos_k5 = {i: (np.cos(angles[i]), np.sin(angles[i])) for i in range(5)}
    nx.draw_networkx_nodes(K5, pos_k5, ax=ax1, node_color='#1e3a8a', node_size=550)
    nx.draw_networkx_labels(K5, pos_k5, ax=ax1, labels={i: f"v{i+1}" for i in range(5)}, font_color='white', font_size=9, font_weight='bold')
    nx.draw_networkx_edges(K5, pos_k5, ax=ax1, edge_color='#dc2626', width=1.8, alpha=0.85)
    ax1.text(0, -1.35, "v = 5, e = 10\ne <= 3v - 6 => 10 <= 9 (VIOLATED!)", ha='center', fontsize=9, fontweight='bold', color='#991b1b',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#fef2f2', edgecolor='#dc2626', alpha=0.9))
    ax1.axis('off')
    ax1.set_xlim(-1.3, 1.3)
    ax1.set_ylim(-1.5, 1.3)
    
    # K_3,3
    ax2.set_title("K3,3 Utility Graph (Non-Planar: e=9 > 2v-4=8)", fontsize=10.5, fontweight='bold', color='#1e3a8a', pad=10)
    pos_k33 = {
        'u1': (-0.8, 1), 'u2': (0, 1), 'u3': (0.8, 1),
        'v1': (-0.8, 0), 'v2': (0, 0), 'v3': (0.8, 0)
    }
    K33 = nx.Graph()
    for u in ['u1', 'u2', 'u3']:
        for v in ['v1', 'v2', 'v3']:
            K33.add_edge(u, v)
    nx.draw_networkx_nodes(K33, pos_k33, nodelist=['u1', 'u2', 'u3'], ax=ax2, node_color='#2563eb', node_size=550)
    nx.draw_networkx_nodes(K33, pos_k33, nodelist=['v1', 'v2', 'v3'], ax=ax2, node_color='#0284c7', node_size=550)
    nx.draw_networkx_labels(K33, pos_k33, ax=ax2, font_color='white', font_size=9, font_weight='bold')
    nx.draw_networkx_edges(K33, pos_k33, ax=ax2, edge_color='#64748b', width=1.8, alpha=0.85)
    ax2.text(0, -0.4, "Bipartite: No triangles (deg(f) >= 4)\ne <= 2v - 4 => 9 <= 8 (VIOLATED!)", ha='center', fontsize=9, fontweight='bold', color='#991b1b',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#fef2f2', edgecolor='#dc2626', alpha=0.9))
    ax2.axis('off')
    ax2.set_xlim(-1.2, 1.2)
    ax2.set_ylim(-0.55, 1.3)
    
    plt.tight_layout()
    out_path = os.path.join(IMG_DIR, "blueprint10_k5_k33_planarity.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"Generated: {out_path}")

if __name__ == "__main__":
    draw_q13_graph()
    draw_q11_odd_cycle()
    draw_blueprint10_planarity()
