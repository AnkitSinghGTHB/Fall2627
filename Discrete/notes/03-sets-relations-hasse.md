# 🔗 Lesson 3 — Sets, Relations & Hasse Diagrams

> **TL;DR**: A relation is a set of pairs (a,b) from set A. Relations can be reflexive, symmetric, transitive, etc. A partial order (reflexive + antisymmetric + transitive) creates a POSET that you can draw as a Hasse diagram. Learn to draw and read Hasse diagrams — they appear on every exam.

---

## 1️⃣ Relations — The Basics

A **relation** R on set A = a subset of A × A (i.e., a set of ordered pairs).

```
A = {1, 2, 3}
R = {(1,1), (1,2), (2,2), (3,3)}

This means: 1 is related to 1, 1 is related to 2, 2 is related to 2, 3 is related to 3
```

---

## 2️⃣ Properties of Relations

| Property | Definition | Test |
|----------|-----------|------|
| **Reflexive** | Every element relates to itself | (a,a) ∈ R for all a |
| **Irreflexive** | NO element relates to itself | (a,a) ∉ R for all a |
| **Symmetric** | If a→b then b→a | (a,b) ∈ R ⟹ (b,a) ∈ R |
| **Antisymmetric** | If a→b AND b→a then a=b | (a,b) ∈ R and (b,a) ∈ R ⟹ a = b |
| **Transitive** | If a→b and b→c then a→c | (a,b) ∈ R and (b,c) ∈ R ⟹ (a,c) ∈ R |

### Quick Check Example

```
A = {1, 2, 3}, R = {(1,1), (2,2), (3,3), (1,2)}

Reflexive?      ✅ (1,1), (2,2), (3,3) all present
Symmetric?      ❌ (1,2) is in R but (2,1) is NOT
Antisymmetric?  ✅ Only (1,2) is a one-directional pair — no conflict
Transitive?     ✅ No chain to check (1→2 but 2 doesn't go anywhere new)
```

---

## 3️⃣ Special Relation Types

| Type | Properties Required | Example |
|------|-------------------|---------|
| **Equivalence Relation** | Reflexive + Symmetric + Transitive | "same remainder when divided by 3" |
| **Partial Order** | Reflexive + Antisymmetric + Transitive | "divides" (a \| b) |
| **Total Order** | Partial order + every pair is comparable | ≤ on integers |

### Equivalence Classes

If R is an equivalence relation on A, it partitions A into **equivalence classes** [a].

```
A = integers, R: a R b iff (a - b) is divisible by 3

[0] = {..., -6, -3, 0, 3, 6, 9, ...}
[1] = {..., -5, -2, 1, 4, 7, 10, ...}
[2] = {..., -4, -1, 2, 5, 8, 11, ...}

These three classes partition ALL integers. No overlap, no gaps.
```

---

## 4️⃣ POSET (Partially Ordered Set)

A POSET = a set + a partial order relation.

Written as **(A, ≤)** where ≤ is a partial order on A.

```
Example: (D₁₂, |) where D₁₂ = {1, 2, 3, 4, 6, 12} and | means "divides"

1 | 2  ✅    2 | 3  ❌ (2 doesn't divide 3 — they're INCOMPARABLE)
1 | 12 ✅    4 | 6  ❌ (incomparable)
```

> "Partial" because NOT every pair is comparable. Some elements can't be ranked.

---

## 5️⃣ Hasse Diagrams — How to Draw Them

A Hasse diagram is a **simplified drawing** of a POSET. Rules:

1. **Smaller elements go lower**, larger go higher
2. **Draw edges** only for the **covering relation** (immediate relationships)
3. **Remove** reflexive loops (a→a) — implied
4. **Remove** transitive edges — if a→b→c, don't draw a→c
5. **Remove** arrow directions — always read bottom-to-top

### Example: (D₁₂, |) = Divisors of 12

```
        12
       / \
      4    6
      |   / \
      2  3   (2 already drawn)
       \ |
        1

Actually:
         12
        /  \
       4    6
       |  / |
       2 /  3
        \| /
         1
```

### Key Terms from Hasse Diagrams

| Term | Definition | In D₁₂ example |
|------|-----------|-----------------|
| **Maximal** | No element above it | 12 |
| **Minimal** | No element below it | 1 |
| **Greatest** | Above ALL others | 12 (also called maximum) |
| **Least** | Below ALL others | 1 (also called minimum) |
| **LUB** (Join) | Least Upper Bound of {a,b} | LUB(4,6) = 12 |
| **GLB** (Meet) | Greatest Lower Bound of {a,b} | GLB(4,6) = 2 |

> **LUB(a,b)** = smallest element that's ≥ both a and b
> **GLB(a,b)** = largest element that's ≤ both a and b

---

## 🏋️ Practice: Draw Hasse Diagrams

1. D₆ = {1, 2, 3, 6} under divisibility
2. D₂₄ = {1, 2, 3, 4, 6, 8, 12, 24} under divisibility
3. P({a,b}) = {∅, {a}, {b}, {a,b}} under subset inclusion (⊆)
4. {1, 2, 3, 4, 5} under ≤ (total order — what does the diagram look like?)

<details>
<summary>🔑 Answers</summary>

1. D₆: `6` at top, `2` and `3` in middle (incomparable), `1` at bottom
2. D₂₄: `24` top → `8,12` → `4,6` → `2,3` → `1` bottom (draw the divisibility edges)
3. P({a,b}): `{a,b}` at top, `{a}` and `{b}` incomparable in middle, `∅` at bottom
4. It's a straight vertical line: `1—2—3—4—5` (total order = chain)

</details>

---

## ✅ Quick Self-Check

1. What 3 properties make an equivalence relation?
2. What 3 properties make a partial order?
3. In a Hasse diagram, why don't we draw transitive edges?
4. What's LUB(2,3) in (D₁₂, |)?
5. Is ≤ on integers a partial or total order?

<details>
<summary>🔑 Answers</summary>

1. Reflexive, Symmetric, Transitive
2. Reflexive, Antisymmetric, Transitive
3. They're redundant — implied by the edges already present
4. **6** (smallest number divisible by both 2 and 3)
5. **Total** order (every pair of integers is comparable)

</details>

---

**⏱️ Time spent: ~20 min. Next →** [04 - Lattices & Boolean Algebra](./04-lattices-boolean-algebra.md)
