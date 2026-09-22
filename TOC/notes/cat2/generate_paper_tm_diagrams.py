import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

IMG_DIR = r"c:\Users\ankit\Fall2627\TOC\notes\cat2\img"
os.makedirs(IMG_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. Turing Machine for Unary Addition (Q3)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 3.8), dpi=300)
ax.set_title("Turing Machine Transition Diagram: Unary Addition (1^m + 1^n -> 1^(m+n))", fontsize=12, fontweight='bold', color='#1e3a8a', pad=15)

pos_add = {
    'q0': (1.2, 1.5),
    'q1': (3.8, 1.5),
    'q2': (6.4, 1.5),
    'qf': (8.4, 1.5)
}

# Start arrow
ax.annotate('', xy=(pos_add['q0'][0] - 0.45, pos_add['q0'][1]), xytext=(pos_add['q0'][0] - 1.1, pos_add['q0'][1]),
            arrowprops=dict(arrowstyle="-|>", color='#1e3a8a', lw=2.2, mutation_scale=14))
ax.text(pos_add['q0'][0] - 1.15, pos_add['q0'][1], "START", fontsize=8.5, fontweight='bold', ha='right', va='center', color='#1e3a8a')

for state, (x, y) in pos_add.items():
    if state == 'qf':
        c_out = patches.Circle((x, y), 0.45, facecolor='#dcfce7', edgecolor='#16a34a', lw=2.2, zorder=3)
        c_in = patches.Circle((x, y), 0.37, facecolor='none', edgecolor='#16a34a', lw=1.6, zorder=4)
        ax.add_patch(c_out)
        ax.add_patch(c_in)
        ax.text(x, y, r"$q_f$", fontsize=11, fontweight='bold', ha='center', va='center', color='#15803d', zorder=5)
    else:
        c = patches.Circle((x, y), 0.42, facecolor='#eff6ff', edgecolor='#2563eb', lw=2.0, zorder=3)
        ax.add_patch(c)
        ax.text(x, y, f"${state[0]}_{state[1]}$", fontsize=11, fontweight='bold', ha='center', va='center', color='#1e40af', zorder=5)

def draw_arrow(p1, p2, label, offset, color='#2563eb'):
    ax.annotate("", xy=p2, xytext=p1,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8, mutation_scale=13), zorder=2)
    mx = (p1[0] + p2[0]) / 2 + offset[0]
    my = (p1[1] + p2[1]) / 2 + offset[1]
    ax.text(mx, my, label, fontsize=9, fontweight='bold', color=color, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffffff', edgecolor='#cbd5e1', lw=0.8, alpha=0.9), zorder=6)

# Self loop on q0
arc0 = patches.Arc((pos_add['q0'][0], pos_add['q0'][1] + 0.42), 0.7, 0.7, theta1=0, theta2=180, edgecolor='#2563eb', lw=1.8)
ax.add_patch(arc0)
ax.annotate("", xy=(pos_add['q0'][0] - 0.35, pos_add['q0'][1] + 0.42), xytext=(pos_add['q0'][0] - 0.35, pos_add['q0'][1] + 0.5),
            arrowprops=dict(arrowstyle="-|>", color='#2563eb', lw=1.8, mutation_scale=12))
ax.text(pos_add['q0'][0], pos_add['q0'][1] + 0.95, "1 / 1, R", fontsize=8.5, fontweight='bold', color='#2563eb', ha='center')

# Transition q0 -> q1
draw_arrow((pos_add['q0'][0] + 0.42, pos_add['q0'][1]), (pos_add['q1'][0] - 0.42, pos_add['q1'][1]), "+ / 1, R", (0, 0.25))

# Self loop on q1
arc1 = patches.Arc((pos_add['q1'][0], pos_add['q1'][1] + 0.42), 0.7, 0.7, theta1=0, theta2=180, edgecolor='#2563eb', lw=1.8)
ax.add_patch(arc1)
ax.annotate("", xy=(pos_add['q1'][0] - 0.35, pos_add['q1'][1] + 0.42), xytext=(pos_add['q1'][0] - 0.35, pos_add['q1'][1] + 0.5),
            arrowprops=dict(arrowstyle="-|>", color='#2563eb', lw=1.8, mutation_scale=12))
ax.text(pos_add['q1'][0], pos_add['q1'][1] + 0.95, "1 / 1, R", fontsize=8.5, fontweight='bold', color='#2563eb', ha='center')

# Transition q1 -> q2
draw_arrow((pos_add['q1'][0] + 0.42, pos_add['q1'][1]), (pos_add['q2'][0] - 0.42, pos_add['q2'][1]), "B / B, L", (0, 0.25))

# Transition q2 -> qf
draw_arrow((pos_add['q2'][0] + 0.42, pos_add['q2'][1]), (pos_add['qf'][0] - 0.45, pos_add['qf'][1]), "1 / B, R", (0, 0.25), color='#16a34a')

ax.text(4.8, 0.4, "Algorithm: Replace '+' with '1', scan to end, erase the last '1' with 'B'. Result = m + n ones.",
        fontsize=8.5, ha='center', color='#334155', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8fafc', edgecolor='#cbd5e1'))

ax.set_xlim(-0.2, 9.4)
ax.set_ylim(0.1, 2.7)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "tm_unary_addition_diagram.png"), bbox_inches='tight')
plt.close()
print("Generated tm_unary_addition_diagram.png")


# -------------------------------------------------------------
# 2. Turing Machine for L = { a^n b^(2n) | n >= 1 } (Q4)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.0), dpi=300)
ax.set_title(r"Turing Machine Transition Diagram: $L = \{a^n b^{2n} \mid n \geq 1\}$", fontsize=12, fontweight='bold', color='#1e3a8a', pad=15)

pos_anb2n = {
    'q0': (1.2, 2.5),
    'q1': (3.6, 3.6),
    'q2': (6.4, 3.6),
    'q3': (5.0, 1.2),
    'q4': (3.6, 2.5),
    'qf': (6.4, 2.5)
}

# Start arrow
ax.annotate('', xy=(pos_anb2n['q0'][0] - 0.45, pos_anb2n['q0'][1]), xytext=(pos_anb2n['q0'][0] - 1.1, pos_anb2n['q0'][1]),
            arrowprops=dict(arrowstyle="-|>", color='#1e3a8a', lw=2.2, mutation_scale=14))
ax.text(pos_anb2n['q0'][0] - 1.15, pos_anb2n['q0'][1], "START", fontsize=8.5, fontweight='bold', ha='right', va='center', color='#1e3a8a')

for state, (x, y) in pos_anb2n.items():
    if state == 'qf':
        c_out = patches.Circle((x, y), 0.44, facecolor='#dcfce7', edgecolor='#16a34a', lw=2.2, zorder=3)
        c_in = patches.Circle((x, y), 0.36, facecolor='none', edgecolor='#16a34a', lw=1.6, zorder=4)
        ax.add_patch(c_out)
        ax.add_patch(c_in)
        ax.text(x, y, r"$q_f$", fontsize=11, fontweight='bold', ha='center', va='center', color='#15803d', zorder=5)
    else:
        c = patches.Circle((x, y), 0.42, facecolor='#eff6ff', edgecolor='#2563eb', lw=2.0, zorder=3)
        ax.add_patch(c)
        ax.text(x, y, f"${state[0]}_{state[1]}$", fontsize=11, fontweight='bold', ha='center', va='center', color='#1e40af', zorder=5)

def draw_curved_arrow(p1, p2, rad, label, offset, color='#2563eb'):
    ax.annotate("", xy=p2, xytext=p1,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8,
                                connectionstyle=f"arc3,rad={rad}", mutation_scale=13), zorder=2)
    mx = (p1[0] + p2[0]) / 2 + offset[0]
    my = (p1[1] + p2[1]) / 2 + offset[1]
    ax.text(mx, my, label, fontsize=8.5, fontweight='bold', color=color, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffffff', edgecolor='#cbd5e1', lw=0.8, alpha=0.9), zorder=6)

# q0 -> q1 on a / X, R
draw_curved_arrow((pos_anb2n['q0'][0] + 0.35, pos_anb2n['q0'][1] + 0.25),
                  (pos_anb2n['q1'][0] - 0.35, pos_anb2n['q1'][1] - 0.15), -0.15, "a / X, R", (-0.1, 0.28))

# Self loop on q1: a / a, R and Y / Y, R
arc_q1 = patches.Arc((pos_anb2n['q1'][0], pos_anb2n['q1'][1] + 0.42), 0.7, 0.7, theta1=0, theta2=180, edgecolor='#2563eb', lw=1.8)
ax.add_patch(arc_q1)
ax.annotate("", xy=(pos_anb2n['q1'][0] - 0.35, pos_anb2n['q1'][1] + 0.42), xytext=(pos_anb2n['q1'][0] - 0.35, pos_anb2n['q1'][1] + 0.5),
            arrowprops=dict(arrowstyle="-|>", color='#2563eb', lw=1.8, mutation_scale=12))
ax.text(pos_anb2n['q1'][0], pos_anb2n['q1'][1] + 0.95, "a/a, R\nY/Y, R", fontsize=7.8, fontweight='bold', color='#2563eb', ha='center')

# q1 -> q2 on b / Y, R (first b)
draw_curved_arrow((pos_anb2n['q1'][0] + 0.42, pos_anb2n['q1'][1]),
                  (pos_anb2n['q2'][0] - 0.42, pos_anb2n['q2'][1]), 0.0, "b / Y, R (1st b)", (0, 0.28))

# Self loop on q2: Y / Y, R
arc_q2 = patches.Arc((pos_anb2n['q2'][0], pos_anb2n['q2'][1] + 0.42), 0.7, 0.7, theta1=0, theta2=180, edgecolor='#2563eb', lw=1.8)
ax.add_patch(arc_q2)
ax.annotate("", xy=(pos_anb2n['q2'][0] - 0.35, pos_anb2n['q2'][1] + 0.42), xytext=(pos_anb2n['q2'][0] - 0.35, pos_anb2n['q2'][1] + 0.5),
            arrowprops=dict(arrowstyle="-|>", color='#2563eb', lw=1.8, mutation_scale=12))
ax.text(pos_anb2n['q2'][0], pos_anb2n['q2'][1] + 0.95, "Y / Y, R", fontsize=7.8, fontweight='bold', color='#2563eb', ha='center')

# q2 -> q3 on b / Y, L (second b)
draw_curved_arrow((pos_anb2n['q2'][0] - 0.25, pos_anb2n['q2'][1] - 0.35),
                  (pos_anb2n['q3'][0] + 0.35, pos_anb2n['q3'][1] + 0.25), 0.15, "b / Y, L (2nd b)", (0.45, 0.1))

# Self loop on q3: a / a, L and Y / Y, L
arc_q3 = patches.Arc((pos_anb2n['q3'][0], pos_anb2n['q3'][1] - 0.42), 0.7, 0.7, theta1=180, theta2=360, edgecolor='#2563eb', lw=1.8)
ax.add_patch(arc_q3)
ax.annotate("", xy=(pos_anb2n['q3'][0] - 0.35, pos_anb2n['q3'][1] - 0.42), xytext=(pos_anb2n['q3'][0] - 0.35, pos_anb2n['q3'][1] - 0.5),
            arrowprops=dict(arrowstyle="-|>", color='#2563eb', lw=1.8, mutation_scale=12))
ax.text(pos_anb2n['q3'][0], pos_anb2n['q3'][1] - 0.95, "a/a, L\nY/Y, L", fontsize=7.8, fontweight='bold', color='#2563eb', ha='center')

# q3 -> q0 on X / X, R (rewound to next a)
draw_curved_arrow((pos_anb2n['q3'][0] - 0.35, pos_anb2n['q3'][1] + 0.25),
                  (pos_anb2n['q0'][0] + 0.25, pos_anb2n['q0'][1] - 0.35), 0.15, "X / X, R", (-0.4, 0.1))

# q0 -> q4 on Y / Y, R (no more a's)
draw_curved_arrow((pos_anb2n['q0'][0] + 0.42, pos_anb2n['q0'][1]),
                  (pos_anb2n['q4'][0] - 0.42, pos_anb2n['q4'][1]), 0.0, "Y / Y, R", (0, 0.25))

# Self loop on q4: Y / Y, R
arc_q4 = patches.Arc((pos_anb2n['q4'][0], pos_anb2n['q4'][1] - 0.42), 0.6, 0.6, theta1=180, theta2=360, edgecolor='#2563eb', lw=1.8)
ax.add_patch(arc_q4)
ax.annotate("", xy=(pos_anb2n['q4'][0] - 0.3, pos_anb2n['q4'][1] - 0.42), xytext=(pos_anb2n['q4'][0] - 0.3, pos_anb2n['q4'][1] - 0.5),
            arrowprops=dict(arrowstyle="-|>", color='#2563eb', lw=1.8, mutation_scale=12))
ax.text(pos_anb2n['q4'][0], pos_anb2n['q4'][1] - 0.85, "Y / Y, R", fontsize=7.8, fontweight='bold', color='#2563eb', ha='center')

# q4 -> qf on B / B, R (Accept)
draw_curved_arrow((pos_anb2n['q4'][0] + 0.42, pos_anb2n['q4'][1]),
                  (pos_anb2n['qf'][0] - 0.45, pos_anb2n['qf'][1]), 0.0, "B / B, R", (0, 0.25), color='#16a34a')

ax.set_xlim(-0.2, 7.8)
ax.set_ylim(0.0, 4.8)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "tm_an_b2n_diagram.png"), bbox_inches='tight')
plt.close()
print("Generated tm_an_b2n_diagram.png")
