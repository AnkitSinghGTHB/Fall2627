import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

IMG_DIR = r"c:\Users\ankit\Fall2627\TOC\notes\cat2\img"
os.makedirs(IMG_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. Turing Machine for Proper Unary Subtraction (m .- n)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 4.5), dpi=300)
ax.set_title(r"Turing Machine: Proper Unary Subtraction $f(m, n) = m \dot{-} n = \max(m-n, 0)$", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)

pos_sub = {
    'q0': (1.2, 2.5),
    'q1': (3.6, 3.5),
    'q2': (6.4, 3.5),
    'q3': (8.6, 2.5),
    'q4': (6.4, 1.3),
    'q5': (3.6, 1.3),
    'qf': (1.2, 1.3)
}

# Start arrow
ax.annotate('', xy=(pos_sub['q0'][0] - 0.45, pos_sub['q0'][1]), xytext=(pos_sub['q0'][0] - 1.1, pos_sub['q0'][1]),
            arrowprops=dict(arrowstyle="-|>", color='#1e3a8a', lw=2.2, mutation_scale=14))
ax.text(pos_sub['q0'][0] - 1.15, pos_sub['q0'][1], "START", fontsize=8.5, fontweight='bold', ha='right', va='center', color='#1e3a8a')

for state, (x, y) in pos_sub.items():
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

def draw_arrow(p1, p2, label, offset, color='#2563eb', rad=0.0):
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

# Self loops
def draw_loop(pos, label, direction='up', color='#2563eb'):
    x, y = pos
    dy = 0.42 if direction == 'up' else -0.42
    arc = patches.Arc((x, y + dy), 0.65, 0.65, theta1=0 if direction=='up' else 180, theta2=180 if direction=='up' else 360, edgecolor=color, lw=1.7)
    ax.add_patch(arc)
    ax.text(x, y + (0.9 if direction == 'up' else -0.9), label, fontsize=8.2, fontweight='bold', color=color, ha='center')

draw_arrow((pos_sub['q0'][0] + 0.42, pos_sub['q0'][1] + 0.2), (pos_sub['q1'][0] - 0.42, pos_sub['q1'][1] - 0.1), "1 / B, R", (0, 0.2))
draw_arrow((pos_sub['q0'][0], pos_sub['q0'][1] - 0.42), (pos_sub['qf'][0], pos_sub['qf'][1] + 0.45), "- / B, R", (-0.35, 0), color='#16a34a')

draw_loop(pos_sub['q1'], "1 / 1, R", 'up')
draw_arrow((pos_sub['q1'][0] + 0.42, pos_sub['q1'][1]), (pos_sub['q2'][0] - 0.42, pos_sub['q2'][1]), "- / -, R", (0, 0.2))

draw_loop(pos_sub['q2'], "1 / 1, R", 'up')
draw_arrow((pos_sub['q2'][0] + 0.42, pos_sub['q2'][1] - 0.2), (pos_sub['q3'][0] - 0.42, pos_sub['q3'][1] + 0.2), "B / B, L", (0, 0.2))

draw_arrow((pos_sub['q3'][0] - 0.42, pos_sub['q3'][1] - 0.2), (pos_sub['q4'][0] + 0.42, pos_sub['q4'][1] + 0.1), "1 / B, L", (0, 0.2))
draw_arrow((pos_sub['q3'][0] - 0.3, pos_sub['q3'][1] - 0.42), (pos_sub['qf'][0] + 0.45, pos_sub['qf'][1]), "- / B, R", (0, -0.35), color='#16a34a', rad=0.2)

draw_loop(pos_sub['q4'], "1 / 1, L", 'down')
draw_arrow((pos_sub['q4'][0] - 0.42, pos_sub['q4'][1]), (pos_sub['q5'][0] + 0.42, pos_sub['q5'][1]), "- / -, L", (0, -0.25))

draw_loop(pos_sub['q5'], "1 / 1, L", 'down')
draw_arrow((pos_sub['q5'][0] - 0.42, pos_sub['q5'][1] + 0.2), (pos_sub['q0'][0] + 0.2, pos_sub['q0'][1] - 0.42), "B / B, R", (-0.1, 0.2))

ax.text(5.0, 0.15, "Strategy: Erase leading '1' in first block -> scan to rightmost '1' in second block -> erase it -> loop back.",
        fontsize=8.5, ha='center', color='#334155', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8fafc', edgecolor='#cbd5e1'))

ax.set_xlim(-0.2, 9.8)
ax.set_ylim(-0.1, 4.3)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "tm_unary_subtraction_diagram.png"), bbox_inches='tight')
plt.close()
print("Generated tm_unary_subtraction_diagram.png")


# -------------------------------------------------------------
# 2. Turing Machine for L = { a^n b^n c^n | n >= 1 }
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10.5, 4.6), dpi=300)
ax.set_title(r"Turing Machine: $L = \{a^n b^n c^n \mid n \geq 1\}$ (Equal Counts of Three Symbols)", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)

pos_abc = {
    'q0': (1.2, 2.5),
    'q1': (3.6, 3.5),
    'q2': (6.4, 3.5),
    'q3': (9.0, 2.5),
    'q4': (5.0, 1.2),
    'qf': (1.2, 1.2)
}

# Start arrow
ax.annotate('', xy=(pos_abc['q0'][0] - 0.45, pos_abc['q0'][1]), xytext=(pos_abc['q0'][0] - 1.1, pos_abc['q0'][1]),
            arrowprops=dict(arrowstyle="-|>", color='#1e3a8a', lw=2.2, mutation_scale=14))
ax.text(pos_abc['q0'][0] - 1.15, pos_abc['q0'][1], "START", fontsize=8.5, fontweight='bold', ha='right', va='center', color='#1e3a8a')

for state, (x, y) in pos_abc.items():
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

draw_arrow((pos_abc['q0'][0] + 0.42, pos_abc['q0'][1] + 0.2), (pos_abc['q1'][0] - 0.42, pos_abc['q1'][1] - 0.1), "a / X, R", (0, 0.2))
draw_arrow((pos_abc['q0'][0], pos_abc['q0'][1] - 0.42), (pos_abc['qf'][0], pos_abc['qf'][1] + 0.45), "B / B, R\nY / Y, R", (-0.35, 0), color='#16a34a')

draw_loop(pos_abc['q1'], "a / a, R\nY / Y, R", 'up')
draw_arrow((pos_abc['q1'][0] + 0.42, pos_abc['q1'][1]), (pos_abc['q2'][0] - 0.42, pos_abc['q2'][1]), "b / Y, R", (0, 0.2))

draw_loop(pos_abc['q2'], "b / b, R\nZ / Z, R", 'up')
draw_arrow((pos_abc['q2'][0] + 0.42, pos_abc['q2'][1] - 0.2), (pos_abc['q3'][0] - 0.42, pos_abc['q3'][1] + 0.2), "c / Z, L", (0, 0.2))

draw_loop(pos_abc['q3'], "a/a, b/b\nY/Y, Z/Z, L", 'right')
draw_arrow((pos_abc['q3'][0] - 0.42, pos_abc['q3'][1] - 0.2), (pos_abc['q4'][0] + 0.42, pos_abc['q4'][1] + 0.2), "X / X, R", (0, 0.2))
draw_arrow((pos_abc['q4'][0] - 0.42, pos_abc['q4'][1] + 0.2), (pos_abc['q0'][0] + 0.42, pos_abc['q0'][1] - 0.2), "a / a, stay", (-0.2, 0.2))

ax.text(5.2, 0.15, "Strategy: Mark 'a' -> X, scan to first 'b' -> Y, scan to first 'c' -> Z, rewind to X, advance to next 'a'.",
        fontsize=8.5, ha='center', color='#334155', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8fafc', edgecolor='#cbd5e1'))

ax.set_xlim(-0.2, 10.2)
ax.set_ylim(-0.1, 4.3)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "tm_anbncn_diagram.png"), bbox_inches='tight')
plt.close()
print("Generated tm_anbncn_diagram.png")


# -------------------------------------------------------------
# 3. Turing Machine for Palindromes L = { w c w^R | w in {a,b}* }
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10.5, 4.8), dpi=300)
ax.set_title(r"Turing Machine: Palindrome Recognizer $L = \{w c w^R \mid w \in \{a,b\}^*\}$", fontsize=11, fontweight='bold', color='#1e3a8a', pad=12)

pos_pal = {
    'q0': (1.2, 2.5),
    'q1': (3.8, 3.8),
    'q2': (6.8, 3.8),
    'q3': (3.8, 1.2),
    'q4': (6.8, 1.2),
    'q5': (5.0, 2.5),
    'qf': (9.0, 2.5)
}

# Start arrow
ax.annotate('', xy=(pos_pal['q0'][0] - 0.45, pos_pal['q0'][1]), xytext=(pos_pal['q0'][0] - 1.1, pos_pal['q0'][1]),
            arrowprops=dict(arrowstyle="-|>", color='#1e3a8a', lw=2.2, mutation_scale=14))
ax.text(pos_pal['q0'][0] - 1.15, pos_pal['q0'][1], "START", fontsize=8.5, fontweight='bold', ha='right', va='center', color='#1e3a8a')

for state, (x, y) in pos_pal.items():
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

draw_arrow((pos_pal['q0'][0] + 0.4, pos_pal['q0'][1] + 0.2), (pos_pal['q1'][0] - 0.4, pos_pal['q1'][1] - 0.1), "a / B, R", (-0.1, 0.2))
draw_arrow((pos_pal['q0'][0] + 0.4, pos_pal['q0'][1] - 0.2), (pos_pal['q3'][0] - 0.4, pos_pal['q3'][1] + 0.1), "b / B, R", (-0.1, -0.2))
draw_arrow((pos_pal['q0'][0] + 0.42, pos_pal['q0'][1]), (pos_pal['q5'][0] - 0.42, pos_pal['q5'][1]), "c / B, R", (0, 0.2))

draw_loop(pos_pal['q1'], "a/a, b/b, c/c, R", 'up')
draw_arrow((pos_pal['q1'][0] + 0.42, pos_pal['q1'][1]), (pos_pal['q2'][0] - 0.42, pos_pal['q2'][1]), "B / B, L", (0, 0.2))

draw_loop(pos_pal['q3'], "a/a, b/b, c/c, R", 'down')
draw_arrow((pos_pal['q3'][0] + 0.42, pos_pal['q3'][1]), (pos_pal['q4'][0] - 0.42, pos_pal['q4'][1]), "B / B, L", (0, -0.2))

draw_arrow((pos_pal['q2'][0] - 0.3, pos_pal['q2'][1] - 0.42), (pos_pal['q5'][0] + 0.2, pos_pal['q5'][1] + 0.42), "a / B, L", (0.2, 0.2))
draw_arrow((pos_pal['q4'][0] - 0.3, pos_pal['q4'][1] + 0.42), (pos_pal['q5'][0] + 0.2, pos_pal['q5'][1] - 0.42), "b / B, L", (0.2, -0.2))

draw_loop(pos_pal['q5'], "a/a, b/b, c/c, L", 'up')
draw_arrow((pos_pal['q5'][0] - 0.42, pos_pal['q5'][1] - 0.2), (pos_pal['q0'][0] + 0.42, pos_pal['q0'][1] - 0.2), "B / B, R", (0, -0.2), rad=0.2)
draw_arrow((pos_pal['q5'][0] + 0.42, pos_pal['q5'][1]), (pos_pal['qf'][0] - 0.45, pos_pal['qf'][1]), "B / B, R", (0, 0.2), color='#16a34a')

ax.text(5.2, 0.15, "Strategy: Remember leading char in state, replace with B -> scan to right end -> verify & erase matching char -> rewind.",
        fontsize=8.5, ha='center', color='#334155', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8fafc', edgecolor='#cbd5e1'))

ax.set_xlim(-0.2, 10.2)
ax.set_ylim(-0.1, 4.6)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(IMG_DIR, "tm_palindrome_diagram.png"), bbox_inches='tight')
plt.close()
print("Generated tm_palindrome_diagram.png")
