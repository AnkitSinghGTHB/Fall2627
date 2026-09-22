import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

IMG_DIR = r"c:\Users\ankit\Fall2627\TOC\notes\cat2\img"
os.makedirs(IMG_DIR, exist_ok=True)

fig, ax = plt.subplots(figsize=(10, 6.2), dpi=300)
ax.set_title("Turing Machine Transition Diagram: Even 0s & Odd 1s (and Vice Versa)", fontsize=13, fontweight='bold', color='#1e3a8a', pad=15)

# Positions for the 4 parity states and the accept state
pos = {
    'q_ee': (1.8, 3.8),   # Even 0, Even 1 (Start)
    'q_eo': (5.2, 3.8),   # Even 0, Odd 1 (Accept for L1)
    'q_oe': (1.8, 1.2),   # Odd 0, Even 1 (Accept for L2)
    'q_oo': (5.2, 1.2),   # Odd 0, Odd 1
    'q_acc': (8.2, 2.5)   # Final Accept State
}

# Draw states
for state, (x, y) in pos.items():
    if state == 'q_acc':
        # Double circle for accept
        c_outer = patches.Circle((x, y), 0.55, facecolor='#dcfce7', edgecolor='#16a34a', lw=2.5, zorder=3)
        c_inner = patches.Circle((x, y), 0.46, facecolor='none', edgecolor='#16a34a', lw=1.8, zorder=4)
        ax.add_patch(c_outer)
        ax.add_patch(c_inner)
        ax.text(x, y + 0.05, r"$q_{acc}$", fontsize=11, fontweight='bold', ha='center', va='center', color='#15803d', zorder=5)
        ax.text(x, y - 0.22, "ACCEPT", fontsize=7.5, fontweight='bold', ha='center', va='center', color='#16a34a', zorder=5)
    else:
        # Standard circle
        is_l1_acc = (state == 'q_eo')
        is_l2_acc = (state == 'q_oe')
        fc = '#eff6ff'
        ec = '#2563eb'
        tc = '#1e40af'
        
        c = patches.Circle((x, y), 0.52, facecolor=fc, edgecolor=ec, lw=2.2, zorder=3)
        ax.add_patch(c)
        
        sub_desc = ""
        if state == 'q_ee':
            sub_desc = "Even 0, Even 1"
        elif state == 'q_eo':
            sub_desc = "Even 0, Odd 1"
        elif state == 'q_oe':
            sub_desc = "Odd 0, Even 1"
        elif state == 'q_oo':
            sub_desc = "Odd 0, Odd 1"
            
        ax.text(x, y + 0.1, f"${state.replace('_', '_{') + '}'}$", fontsize=11, fontweight='bold', ha='center', va='center', color=tc, zorder=5)
        ax.text(x, y - 0.2, sub_desc, fontsize=6.8, fontweight='bold', ha='center', va='center', color='#64748b', zorder=5)

# Start arrow pointing to q_ee
ax.annotate('', xy=(pos['q_ee'][0] - 0.53, pos['q_ee'][1]), xytext=(pos['q_ee'][0] - 1.25, pos['q_ee'][1]),
            arrowprops=dict(arrowstyle="-|>", color='#1e3a8a', lw=2.5, mutation_scale=15))
ax.text(pos['q_ee'][0] - 1.3, pos['q_ee'][1], "START", fontsize=8.5, fontweight='bold', ha='right', va='center', color='#1e3a8a')

def draw_curved_arrow(ax, p1, p2, rad, label, offset, color='#2563eb', linestyle='solid'):
    ax.annotate("",
                xy=p2, xytext=p1,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8, linestyle=linestyle,
                                connectionstyle=f"arc3,rad={rad}", mutation_scale=14),
                zorder=2)
    mx = (p1[0] + p2[0]) / 2 + offset[0]
    my = (p1[1] + p2[1]) / 2 + offset[1]
    ax.text(mx, my, label, fontsize=9.2, fontweight='bold', color=color, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffffff', edgecolor='#cbd5e1', lw=0.8, alpha=0.9), zorder=6)

# Horizontal 1-transitions: q_ee <-> q_eo
p_ee_r = (pos['q_ee'][0] + 0.52, pos['q_ee'][1] + 0.15)
p_eo_l1 = (pos['q_eo'][0] - 0.52, pos['q_eo'][1] + 0.15)
draw_curved_arrow(ax, p_ee_r, p_eo_l1, -0.22, "1/1, R", (0, 0.32), color='#2563eb')

p_eo_l2 = (pos['q_eo'][0] - 0.52, pos['q_eo'][1] - 0.15)
p_ee_r2 = (pos['q_ee'][0] + 0.52, pos['q_ee'][1] - 0.15)
draw_curved_arrow(ax, p_eo_l2, p_ee_r2, -0.22, "1/1, R", (0, -0.32), color='#2563eb')

# Horizontal 1-transitions: q_oe <-> q_oo
p_oe_r = (pos['q_oe'][0] + 0.52, pos['q_oe'][1] + 0.15)
p_oo_l1 = (pos['q_oo'][0] - 0.52, pos['q_oo'][1] + 0.15)
draw_curved_arrow(ax, p_oe_r, p_oo_l1, -0.22, "1/1, R", (0, 0.32), color='#2563eb')

p_oo_l2 = (pos['q_oo'][0] - 0.52, pos['q_oo'][1] - 0.15)
p_oe_r2 = (pos['q_oe'][0] + 0.52, pos['q_oe'][1] - 0.15)
draw_curved_arrow(ax, p_oo_l2, p_oe_r2, -0.22, "1/1, R", (0, -0.32), color='#2563eb')

# Vertical 0-transitions: q_ee <-> q_oe
p_ee_b1 = (pos['q_ee'][0] - 0.15, pos['q_ee'][1] - 0.52)
p_oe_t1 = (pos['q_oe'][0] - 0.15, pos['q_oe'][1] + 0.52)
draw_curved_arrow(ax, p_ee_b1, p_oe_t1, -0.22, "0/0, R", (-0.45, 0), color='#0891b2')

p_oe_t2 = (pos['q_oe'][0] + 0.15, pos['q_oe'][1] + 0.52)
p_ee_b2 = (pos['q_ee'][0] + 0.15, pos['q_ee'][1] - 0.52)
draw_curved_arrow(ax, p_oe_t2, p_ee_b2, -0.22, "0/0, R", (0.45, 0), color='#0891b2')

# Vertical 0-transitions: q_eo <-> q_oo
p_eo_b1 = (pos['q_eo'][0] - 0.15, pos['q_eo'][1] - 0.52)
p_oo_t1 = (pos['q_oo'][0] - 0.15, pos['q_oo'][1] + 0.52)
draw_curved_arrow(ax, p_eo_b1, p_oo_t1, -0.22, "0/0, R", (-0.45, 0), color='#0891b2')

p_oo_t2 = (pos['q_oo'][0] + 0.15, pos['q_oo'][1] + 0.52)
p_eo_b2 = (pos['q_eo'][0] + 0.15, pos['q_eo'][1] - 0.52)
draw_curved_arrow(ax, p_oo_t2, p_eo_b2, -0.22, "0/0, R", (0.45, 0), color='#0891b2')

# Blank Accept transitions:
# 1. For L1 (Even 0s, Odd 1s): q_eo -> q_acc on B/B, R
p_eo_acc = (pos['q_eo'][0] + 0.52, pos['q_eo'][1])
p_acc_l1 = (pos['q_acc'][0] - 0.45, pos['q_acc'][1] + 0.3)
draw_curved_arrow(ax, p_eo_acc, p_acc_l1, -0.15, "B/B, R (L1 Accept)", (0.1, 0.3), color='#16a34a')

# 2. For L2 (Odd 0s, Even 1s - Vice Versa): q_oe -> q_acc on B/B, R
p_oe_acc = (pos['q_oe'][0] + 0.52, pos['q_oe'][1])
p_acc_l2 = (pos['q_acc'][0] - 0.45, pos['q_acc'][1] - 0.3)
draw_curved_arrow(ax, p_oe_acc, p_acc_l2, 0.18, "B/B, R (L2 Accept)", (0.8, -0.35), color='#d97706')

# Annotations & Legend
ax.text(5.0, 0.15,
        r"$\mathbf{L_1}$ (Even 0s, Odd 1s): Halts & Accepts from $q_{eo}$ on $B$" + "\n" +
        r"$\mathbf{L_2}$ (Odd 0s, Even 1s - Vice Versa): Halts & Accepts from $q_{oe}$ on $B$" + "\n" +
        r"$\mathbf{L_{combined}}$ (Both): Either $q_{eo}$ or $q_{oe}$ accepts on $B$",
        fontsize=9, ha='center', color='#1e293b',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#f8fafc', edgecolor='#cbd5e1', lw=1.2))

ax.set_xlim(0.1, 9.3)
ax.set_ylim(-0.3, 4.8)
ax.axis('off')
plt.tight_layout()

out_path = os.path.join(IMG_DIR, "tm_even0_odd1_transition_diagram.png")
plt.savefig(out_path, bbox_inches='tight')
plt.close()
print("Generated:", out_path)
