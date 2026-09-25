import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

IMG_DIR = r"c:\Users\ankit\Fall2627\TOC\notes\cat2\img"
os.makedirs(IMG_DIR, exist_ok=True)

# =====================================================================
# 1. Turing Machine for L = {a^n b^n | n >= 1}
# =====================================================================
fig, ax = plt.subplots(figsize=(10, 4.2), dpi=300)
ax.set_title(r"Turing Machine State Transition Diagram: $L = \{a^n b^n \mid n \geq 1\}$", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)

pos_anbn = {
    'q0': (1.5, 2.5),
    'q1': (4.2, 2.5),
    'q2': (7.0, 2.5),
    'q3': (4.2, 1.0),
    'qf': (7.5, 1.0)
}

# Start arrow
ax.annotate('', xy=(pos_anbn['q0'][0] - 0.45, pos_anbn['q0'][1]), xytext=(pos_anbn['q0'][0] - 1.1, pos_anbn['q0'][1]),
            arrowprops=dict(arrowstyle="-|>", color='#1e3a8a', lw=2.2, mutation_scale=14))
ax.text(pos_anbn['q0'][0] - 1.15, pos_anbn['q0'][1], "START", fontsize=8.5, fontweight='bold', ha='right', va='center', color='#1e3a8a')

for state, (x, y) in pos_anbn.items():
    if state == 'qf':
        c_out = patches.Circle((x, y), 0.45, facecolor='#dcfce7', edgecolor='#16a34a', lw=2.2, zorder=3)
        c_in = patches.Circle((x, y), 0.37, facecolor='none', edgecolor='#16a34a', lw=1.6, zorder=4)
        ax.add_patch(c_out)
        ax.add_patch(c_in)
        ax.text(x, y, r"$q_f$", fontsize=10.5, fontweight='bold', ha='center', va='center', color='#15803d', zorder=5)
    else:
        c = patches.Circle((x, y), 0.42, facecolor='#eff6ff', edgecolor='#2563eb', lw=2.0, zorder=3)
        ax.add_patch(c)
        ax.text(x, y, f"${state[0]}_{state[1]}$", fontsize=10.5, fontweight='bold', ha='center', va='center', color='#1e40af', zorder=5)

def draw_arrow(ax, p1, p2, label, offset, color='#2563eb', rad=0.0):
    if rad == 0.0:
        ax.annotate("", xy=p2, xytext=p1,
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=1.7, mutation_scale=12), zorder=2)
    else:
        ax.annotate("", xy=p2, xytext=p1,
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=1.7, mutation_scale=12,
                                    connectionstyle=f"arc3,rad={rad}"), zorder=2)
    mx = (p1[0] + p2[0]) / 2 + offset[0]
    my = (p1[1] + p2[1]) / 2 + offset[1]
    ax.text(mx, my, label, fontsize=8.2, fontweight='bold', color=color, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffffff', edgecolor='#cbd5e1', lw=0.7, alpha=0.92), zorder=6)

def draw_loop(ax, pos, label, direction='up', color='#2563eb'):
    x, y = pos
    dy = 0.42 if direction == 'up' else -0.42
    arc = patches.Arc((x, y + dy), 0.65, 0.65, theta1=0 if direction=='up' else 180, theta2=180 if direction=='up' else 360, edgecolor=color, lw=1.7)
    ax.add_patch(arc)
    ax.text(x, y + (0.9 if direction == 'up' else -0.9), label, fontsize=8.2, fontweight='bold', color=color, ha='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffffff', edgecolor='#cbd5e1', lw=0.7, alpha=0.92))

draw_arrow(ax, (pos_anbn['q0'][0]+0.42, 2.5), (pos_anbn['q1'][0]-0.42, 2.5), "a -> X, R", (0, 0.25))
draw_loop(ax, pos_anbn['q1'], "a -> a, R\nY -> Y, R", 'up')
draw_arrow(ax, (pos_anbn['q1'][0]+0.42, 2.5), (pos_anbn['q2'][0]-0.42, 2.5), "b -> Y, L", (0, 0.25))
draw_loop(ax, pos_anbn['q2'], "a -> a, L\nY -> Y, L", 'up')
draw_arrow(ax, (pos_anbn['q2'][0]-0.3, 2.2), (pos_anbn['q0'][0]+0.3, 2.2), "X -> X, R", (0, -0.45), rad=0.35)

draw_arrow(ax, (pos_anbn['q0'][0]+0.2, 2.1), (pos_anbn['q3'][0]-0.3, 1.3), "Y -> Y, R", (-0.35, -0.15))
draw_loop(ax, pos_anbn['q3'], "Y -> Y, R", 'down')
draw_arrow(ax, (pos_anbn['q3'][0]+0.42, 1.0), (pos_anbn['qf'][0]-0.45, 1.0), "B -> B, R", (0, 0.25), color='#16a34a')

ax.set_xlim(0, 9.0)
ax.set_ylim(0, 3.8)
ax.axis('off')
plt.tight_layout()
p1 = os.path.join(IMG_DIR, "tm_an_bn_diagram.png")
plt.savefig(p1, bbox_inches='tight', dpi=300)
plt.close()
print("Saved:", p1)


# =====================================================================
# 2. Turing Machine for L = {a^(2n) b^n | n >= 1}
# =====================================================================
fig, ax = plt.subplots(figsize=(10.5, 4.4), dpi=300)
ax.set_title(r"Turing Machine State Transition Diagram: $L = \{a^{2n} b^n \mid n \geq 1\}$", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)

pos_a2nbn = {
    'q0': (1.2, 2.6),
    'q1': (3.6, 2.6),
    'q2': (6.2, 2.6),
    'q3': (8.8, 2.6),
    'q4': (3.6, 1.0),
    'qf': (7.0, 1.0)
}

# Start arrow
ax.annotate('', xy=(pos_a2nbn['q0'][0] - 0.45, pos_a2nbn['q0'][1]), xytext=(pos_a2nbn['q0'][0] - 1.1, pos_a2nbn['q0'][1]),
            arrowprops=dict(arrowstyle="-|>", color='#1e3a8a', lw=2.2, mutation_scale=14))
ax.text(pos_a2nbn['q0'][0] - 1.15, pos_a2nbn['q0'][1], "START", fontsize=8.5, fontweight='bold', ha='right', va='center', color='#1e3a8a')

for state, (x, y) in pos_a2nbn.items():
    if state == 'qf':
        c_out = patches.Circle((x, y), 0.45, facecolor='#dcfce7', edgecolor='#16a34a', lw=2.2, zorder=3)
        c_in = patches.Circle((x, y), 0.37, facecolor='none', edgecolor='#16a34a', lw=1.6, zorder=4)
        ax.add_patch(c_out)
        ax.add_patch(c_in)
        ax.text(x, y, r"$q_f$", fontsize=10.5, fontweight='bold', ha='center', va='center', color='#15803d', zorder=5)
    else:
        c = patches.Circle((x, y), 0.42, facecolor='#eff6ff', edgecolor='#2563eb', lw=2.0, zorder=3)
        ax.add_patch(c)
        ax.text(x, y, f"${state[0]}_{state[1]}$", fontsize=10.5, fontweight='bold', ha='center', va='center', color='#1e40af', zorder=5)

# q0 -> q1: 1st 'a' -> X
draw_arrow(ax, (pos_a2nbn['q0'][0]+0.42, 2.6), (pos_a2nbn['q1'][0]-0.42, 2.6), "a -> X, R", (0, 0.25))

# q1 -> q2: 2nd 'a' -> X
draw_arrow(ax, (pos_a2nbn['q1'][0]+0.42, 2.6), (pos_a2nbn['q2'][0]-0.42, 2.6), "a -> X, R", (0, 0.25))

# q2: loop on 'a' and 'Y' -> scan to find 'b'
draw_loop(ax, pos_a2nbn['q2'], "a -> a, R\nY -> Y, R", 'up')

# q2 -> q3: match 'b' -> Y
draw_arrow(ax, (pos_a2nbn['q2'][0]+0.42, 2.6), (pos_a2nbn['q3'][0]-0.42, 2.6), "b -> Y, L", (0, 0.25))

# q3: loop on 'a' and 'Y' leftwards
draw_loop(ax, pos_a2nbn['q3'], "a -> a, L\nY -> Y, L", 'up')

# q3 -> q0: hit X -> move right to start next pair of 'a's
draw_arrow(ax, (pos_a2nbn['q3'][0]-0.3, 2.2), (pos_a2nbn['q0'][0]+0.3, 2.2), "X -> X, R", (0, -0.45), rad=0.35)

# q0 -> q4: if see Y, all 'a's consumed
draw_arrow(ax, (pos_a2nbn['q0'][0]+0.2, 2.2), (pos_a2nbn['q4'][0]-0.3, 1.3), "Y -> Y, R", (-0.35, -0.15))
draw_loop(ax, pos_a2nbn['q4'], "Y -> Y, R", 'down')

# q4 -> qf: if see B, all b's verified -> Accept
draw_arrow(ax, (pos_a2nbn['q4'][0]+0.42, 1.0), (pos_a2nbn['qf'][0]-0.45, 1.0), "B -> B, R", (0, 0.25), color='#16a34a')

ax.set_xlim(0, 10.0)
ax.set_ylim(0, 3.8)
ax.axis('off')
plt.tight_layout()
p2 = os.path.join(IMG_DIR, "tm_a2n_bn_diagram.png")
plt.savefig(p2, bbox_inches='tight', dpi=300)
plt.close()
print("Saved:", p2)
