# 🔷 Lesson 4 — Lattices & Boolean Algebra

> **TL;DR**: A lattice = a POSET where every pair has a LUB (join ∨) and GLB (meet ∧). Boolean algebra = a special type of lattice used to simplify digital circuits. Learn to check if something's a lattice, find complements, and simplify Boolean expressions.

---

## 🎯 Question Language to Topic Selection Guide (Exam Hall Lookup)

| If Exam Question Asks... | Identified Syllabus Topic | Instant Decision Rule / Formula |
| :--- | :--- | :--- |
| *"Determine whether $(A, \mid)$ is a lattice..."* | **Lattice Verification** | Poset is a lattice $\iff$ every pair has $\text{LUB} = \text{lcm}(a,b) \in A$ and $\text{GLB} = \gcd(a,b) \in A$. If $\text{lcm} \notin A \implies$ NOT a lattice. |
| *"Is $(D_n, \mid)$ a Boolean algebra?"* | **Square-Free Criterion** | $(D_n, \mid)$ is Boolean $\iff n$ is **square-free** (no $p^2 \mid n$). E.g., $D_{30} = 2 \cdot 3 \cdot 5$ is Boolean; $D_{12} = 2^2 \cdot 3$ is NOT. |
| *"Determine if lattice is distributive / modular..."* | **Birkhoff's Forbidden Sublattices** | Distributive $\iff$ NO sublattice isomorphic to Diamond $M_3$ or Pentagon $N_5$. Counterexample: $a \wedge (b \vee c) \ne (a \wedge b) \vee (a \wedge c)$. |
| *"Find complements of all elements in lattice..."* | **Complemented Lattice** | Complement $x'$ satisfies $x \wedge x' = 0$ (bottom) and $x \vee x' = 1$ (top). In $D_n$, $\gcd(x, x') = 1$ and $\text{lcm}(x, x') = n$. |
| *"Find PDNF and PCNF for expression $f$..."* | **Principal Normal Forms** | $\text{PDNF} = \sum m(\text{rows where } f=1)$; $\text{PCNF} = \prod M(\text{rows where } f=0)$. Shorthands are complementary! |
| *"Design series/parallel contact network..."* | **Switching Circuits** | Series $= A \cdot B$ (AND); Parallel $= A + B$ (OR); Inverted $= A'$ (NOT). |

> 📖 **Full Questionnaire & 18 Exam Problem Solutions**: See [CAT-2 Question-Language Decoder](./cat2-exam-questionnaire-decoder.md) and [Module 3 HOTS Notes](./cat2-hots-module3-lattices-boolean.md).

---

## 1️⃣ What is a Lattice?

A POSET becomes a **lattice** if:
- Every pair {a, b} has a **unique LUB** (join, written a ∨ b)
- Every pair {a, b} has a **unique GLB** (meet, written a ∧ b)

### Quick Test: Is it a Lattice?

```
Ask for EVERY pair of elements: "Do they have a unique LUB AND a unique GLB?"
  YES for all pairs → It's a lattice ✅
  NO for even one pair → NOT a lattice ❌
```

### Common Lattice: Divisors

(D₃₀, |) where D₃₀ = {1, 2, 3, 5, 6, 10, 15, 30}
- Meet (∧) = **gcd**(a, b)
- Join (∨) = **lcm**(a, b)

Every pair has a unique gcd and lcm → **It's a lattice** ✅

---

## 2️⃣ Types of Lattices

| Type | Extra Property | Example |
|------|---------------|---------|
| **Bounded** | Has a greatest (1) and least (0) element | D₃₀: least=1, greatest=30 |
| **Complemented** | Every element has a complement | x∧x'=0 and x∨x'=1 |
| **Distributive** | ∧ distributes over ∨ (and vice versa) | D₃₀ is distributive |
| **Boolean Algebra** | Complemented + Distributive | Power set P(S) under ⊆ |

### Complement

In a bounded lattice (with top=1, bottom=0):

**x' is the complement of x** if:
```
x ∧ x' = 0   (meet = bottom)
x ∨ x' = 1   (join = top)
```

**Example**: In D₃₀ with 0=1 and 1=30:
- Complement of 2? Need gcd(2,x)=1 AND lcm(2,x)=30 → x=15 ✅
- Complement of 6? Need gcd(6,x)=1 AND lcm(6,x)=30 → x=5 ✅

---

## 3️⃣ Sub-lattice Check

A subset L₁ ⊆ L is a **sub-lattice** if it's **closed** under ∧ and ∨:

```
For ALL a,b in L₁:  a ∧ b must be in L₁  AND  a ∨ b must be in L₁
```

**Example**: L = D₃₀
- L₁ = {1, 2, 3, 6}: gcd(2,3)=1 ∈ L₁, lcm(2,3)=6 ∈ L₁ → **sub-lattice** ✅
- L₂ = {1, 2, 5}: lcm(2,5) = 10 ∉ L₂ → **NOT a sub-lattice** ❌

---

## 4️⃣ Boolean Algebra

A Boolean Algebra is a lattice that is **bounded + complemented + distributive**.

### Laws of Boolean Algebra

| Law | AND form | OR form |
|-----|----------|---------|
| Identity | a · 1 = a | a + 0 = a |
| Domination | a · 0 = 0 | a + 1 = 1 |
| Idempotent | a · a = a | a + a = a |
| Complement | a · a' = 0 | a + a' = 1 |
| Commutative | a · b = b · a | a + b = b + a |
| Associative | (a·b)·c = a·(b·c) | (a+b)+c = a+(b+c) |
| Distributive | a·(b+c) = ab+ac | a+(b·c) = (a+b)·(a+c) |
| **De Morgan's** | **(a·b)' = a'+b'** | **(a+b)' = a'·b'** |
| Absorption | a·(a+b) = a | a+(a·b) = a |
| Involution | (a')' = a | |

---

## 5️⃣ Boolean Functions & Normal Forms

### Minterms & Maxterms

For n variables, there are 2ⁿ possible input combinations.

**Minterm** = an AND of all variables (each either complemented or not) that = 1 for exactly one input combination.

| A | B | C | Minterm | Notation |
|:---:|:---:|:---:|---|:---:|
| 0 | 0 | 0 | A'B'C' | m₀ |
| 0 | 0 | 1 | A'B'C | m₁ |
| 0 | 1 | 0 | A'BC' | m₂ |
| 0 | 1 | 1 | A'BC | m₃ |
| 1 | 0 | 0 | AB'C' | m₄ |
| 1 | 0 | 1 | AB'C | m₅ |
| 1 | 1 | 0 | ABC' | m₆ |
| 1 | 1 | 1 | ABC | m₇ |

### PDNF (Sum of Minterms)

Find all rows where f = 1, take those minterms, OR them together.

**Example**: f(A,B,C) = (A+B)·C'

| A | B | C | f |
|:---:|:---:|:---:|:---:|
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 |

**PDNF**: f = A'BC' + AB'C' + ABC' = Σm(2, 4, 6)

---

## 6️⃣ Switching Circuits

Boolean algebra directly applies to circuit simplification:

| Boolean | Circuit |
|---------|---------|
| a + b | **Parallel** switches |
| a · b | **Series** switches |
| a' | Switch in **opposite** state |

### Simplification Example

```
F = a·b·c + a·b'·c + a'·b'·c'

Step 1: Factor common terms from first two: a·c·(b + b') + a'·b'·c'
Step 2: b + b' = 1:                         a·c·1 + a'·b'·c'
Step 3: Simplify:                            a·c + a'·b'·c'
```

Draw the simplified circuit:
```
+--- [ a ] --- [ c ] ---+
|                        |
+--- [ a'] --- [b'] --- [c'] ---+
```

Two branches in parallel. Much simpler than the original!

## 🏋️ Solved Exam Practice Questions

### Question 1 (Sub-lattice Check — Very Common)
**In the lattice $(D_{12}, |)$ where $D_{12} = \{1, 2, 3, 4, 6, 12\}$, check if $L_1 = \{1, 2, 4\}$ is a sub-lattice.**

<details>
<summary>💡 Step-by-Step Solution</summary>

Check every pair in $L_1$ for closure under meet (gcd) and join (lcm):

| Pair | gcd (meet) | ∈ $L_1$? | lcm (join) | ∈ $L_1$? |
|------|:---:|:---:|:---:|:---:|
| (1, 2) | 1 | ✅ | 2 | ✅ |
| (1, 4) | 1 | ✅ | 4 | ✅ |
| (2, 4) | 2 | ✅ | 4 | ✅ |

All pairs are closed under both operations → **$L_1$ IS a sub-lattice** ✅

</details>

### Question 2 (PDNF & PCNF — Guaranteed 5+ Marks)
**Find the PDNF and PCNF of $f(A, B) = A + B'$.**

<details>
<summary>💡 Step-by-Step Solution</summary>

**Step 1**: Build the truth table:

| A | B | B' | A + B' | f |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 1 | 1 |

**Step 2 — PDNF** (OR the minterms where $f = 1$): Rows 0, 2, 3.
$$\text{PDNF} = A'B' + AB' + AB = \Sigma m(0, 2, 3)$$

**Step 3 — PCNF** (AND the maxterms where $f = 0$): Row 1.
$$\text{PCNF} = (A + B') = \Pi M(1)$$

**Verification**: Simplify PDNF → $A'B' + AB' + AB = B'(A' + A) + AB = B' + AB = B' + A$ ✓ ✅
</details>

---

## ✅ Quick Self-Check

1. What two conditions make a POSET a lattice?
2. What's a complement of element x?
3. How do you check if a subset is a sub-lattice?
4. Express f = Σm(1, 3, 5) for 3 variables in PDNF
5. In circuits, what does "+" mean? What does "·" mean?

<details>
<summary>🔑 Answers</summary>

1. Every pair has a unique **LUB** (join) and **GLB** (meet)
2. An element x' where x ∧ x' = 0 (bottom) and x ∨ x' = 1 (top)
3. Check that meet and join of every pair in the subset stay IN the subset
4. f = A'B'C + A'BC + AB'C
5. "+" = parallel connection, "·" = series connection

</details>

---

**⏱️ Time spent: ~20 min. Next →** [05 - Graphs](./05-graphs.md)
