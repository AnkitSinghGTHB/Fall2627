# 🗺️ Lesson 7 — Karnaugh Maps (K-Maps)

> **TL;DR**: K-Maps are basically a puzzle game — you draw a grid, fill in 1s and 0s, then find the biggest rectangular groups of 1s you can. Each group becomes one simple term in your answer. It's like Candy Crush but for Boolean algebra. Seriously.

---

## 🧩 First — SOP vs POS (The Two Answer Formats)

Before K-Maps, know what format your answer should be in:

| Format | What it means | You group... | Example |
|---|---|---|---|
| **SOP** (Sum of Products) | OR of AND terms | The **1s** in the K-Map | $F = AB + \overline{A}C$ |
| **POS** (Product of Sums) | AND of OR terms | The **0s** in the K-Map | $F = (A+B)(\overline{A}+C)$ |

> 🎯 **Exam tip**: 90% of K-Map questions ask for SOP. If the question says "minimize" without specifying, assume SOP.

---

## 🗺️ How K-Maps Actually Work (The Candy Crush Method)

### The Rules:
1. **Label rows/columns in Gray Code order**: $00, 01, 11, 10$ — NOT binary order! The trick is: only 1 bit changes between neighbors.
2. **Group only in powers of 2**: Groups can be 1, 2, 4, 8, or 16 cells. **Never 3, 5, 6, 7**.
3. **Groups must be rectangles** (including squares). No L-shapes, no diagonals.
4. **Edges wrap around!** Top connects to bottom. Left connects to right. The 4 corners are also adjacent.
5. **Bigger groups = simpler terms**. Always go as big as possible.

> 🤦 **Common Exam Mistake**: Forgetting that the edges wrap around! A cell in row 1, column 1 IS adjacent to the cell in row 1, column 4. Many students miss groups because of this.

---

## 📊 The 4-Variable K-Map Template (Memorize This Layout!)

```
         CD
         00   01   11   10
    ┌────┬────┬────┬────┬────┐
AB  │    │ m0 │ m1 │ m3 │ m2 │
00  │    │    │    │    │    │
    ├────┼────┼────┼────┼────┤
01  │    │ m4 │ m5 │ m7 │ m6 │
    ├────┼────┼────┼────┼────┤
11  │    │m12 │m13 │m15 │m14 │
    ├────┼────┼────┼────┼────┤
10  │    │ m8 │ m9 │m11 │m10 │
    └────┴────┴────┴────┴────┘
```

> 🧠 **Memory Trick**: The column/row labels go $00, 01, 11, 10$. Remember: "**0, 1, 3, 2**" — it's Gray Code. If you write $00, 01, 10, 11$ on the exam, you'll get the wrong answer!

---

## 🎲 Don't Care Conditions ($X$ or $d$)

Sometimes certain input combinations are impossible or don't matter. These are **Don't Cares**.

- Treat them as **1** if it helps you make a bigger group.
- Treat them as **0** if they don't help.
- They're basically free wildcards — use them!

---

## 🏋️ Solved Exam Practice Questions

### Question 1 (The Classic 4-Variable K-Map)
**Simplify $F(A, B, C, D) = \Sigma m(0, 1, 2, 8, 9) + d(10, 11)$ into minimal SOP form.**

<details>
<summary>💡 Step-by-Step Solution</summary>

**Step 1**: Plot all the $1$s and $X$s on the map.

**Step 2**: Find groups:
- Group 1: Cells $0, 1, 8, 9$ (a quad) → These share $\overline{B}\overline{C}$ in common.
- Group 2: Cells $0, 2, 8, 10$ (using don't care at 10) → These share $\overline{B}\overline{D}$ in common.

**Step 3**: Write the minimal SOP:
$$F = \overline{B}\overline{C} + \overline{B}\overline{D}$$

**Bonus**: Factor out → $F = \overline{B}(\overline{C} + \overline{D})$

**Result:** Minimal SOP $= \overline{B}\overline{C} + \overline{B}\overline{D}$ ✅

</details>

---

## ✅ Quick Self-Check (30 seconds)

1. What order do you label K-Map rows/columns?
2. Can you have a group of 6 cells?
3. If there's a Don't Care ($X$), do you have to include it in a group?

<details>
<summary>🔑 Answers</summary>

1. Gray Code: $00, 01, 11, 10$.
2. **No** — only powers of 2 (1, 2, 4, 8, 16).
3. **No** — include it only if it helps make a bigger group.

</details>

---

**⏱️ Time spent: ~15 mins. Next →** [08 - Combinational Circuits](./08-combinational-circuits.md)
