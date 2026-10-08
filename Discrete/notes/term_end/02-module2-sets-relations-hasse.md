# 📘 Module 2: Sets, Relations & Hasse Diagrams (From Zero to Mastery)

> **Module Focus**: Sets, Cartesian Products, Relation Properties, Equivalence Relations & Classes, Posets, Drawing Hasse Diagrams, and Finding GLB/LUB.  
> **Weightage in FAT**: Approx 15–20 Marks.  
> **Philosophy**: A relation is simply a set of ordered pairs showing "who is connected to whom". Once you visualize relations as matrices or directed arrows, the proofs become straightforward.

---

## 1. Relations: The Core Definitions

### 1.1 What is a Relation?
* Given sets $A$ and $B$, the **Cartesian Product** $A \times B = \{(a, b) \mid a \in A, b \in B\}$.
* A **binary relation** $R$ from $A$ to $B$ is simply any subset of $A \times B$:
  $$R \subseteq A \times B$$
* If $A = B$, we say $R$ is a **relation on $A$** ($R \subseteq A \times A$).
* If $(a, b) \in R$, we write $a \, R \, b$ ("$a$ is related to $b$").

---

### 1.2 The 4 Cardinal Properties of Relations on a Set $A$

This is the most tested foundation in Discrete Math. Master these 4 tests:

```text
1. REFLEXIVE:       Every element points to ITSELF.
                    ∀a ∈ A, (a, a) ∈ R.
                    [Matrix View: The entire main diagonal must be all 1s!]

2. SYMMETRIC:       Every arrow is a TWO-WAY street.
                    If (a, b) ∈ R, then (b, a) MUST be in R.
                    [Matrix View: The relation matrix is symmetric, M_R = (M_R)^T]

3. ANTI-SYMMETRIC:  NO TWO-WAY streets between distinct elements!
                    If (a, b) ∈ R and (b, a) ∈ R, then a MUST EQUAL b.
                    In other words: If a ≠ b and (a, b) ∈ R, then (b, a) CANNOT be in R.
                    [Matrix View: You can never have 1s at both (i, j) and (j, i) off-diagonal!]

4. TRANSITIVE:      Shortcuts exist!
                    If (a, b) ∈ R and (b, c) ∈ R, then (a, c) MUST be in R.
                    [Matrix View: If path of length 2 exists, direct edge must exist!]
```

> ⚠️ **COMMON CONFUSION: Anti-symmetric vs NOT Symmetric**:  
> * Anti-symmetric is **NOT** the opposite of symmetric!  
> * A relation can be:
>   * Both Symmetric and Anti-symmetric (e.g., Equality relation $R = \{(1, 1), (2, 2)\}$).
>   * Neither Symmetric nor Anti-symmetric (e.g., $R = \{(1, 2), (2, 1), (2, 3)\}$ on $\{1, 2, 3\}$).

---

## 2. Equivalence Relations & Equivalence Classes

### 2.1 Definition of an Equivalence Relation
A relation $R$ on a set $A$ is an **Equivalence Relation** if and only if it satisfies all 3 conditions:
1. **Reflexive**
2. **Symmetric**
3. **Transitive**

*Everyday Analogy*: "Has the same color as", "Has the same age as", or "Is congruent to modulo $m$".

---

### 2.2 Equivalence Classes $[a]$
* For any element $a \in A$, the **equivalence class of $a$**, denoted $[a]$, is the set of all elements in $A$ related to $a$:
  $$[a] = \{x \in A \mid (x, a) \in R\}$$

#### 🔑 Fundamental Theorem of Equivalence Relations:
The equivalence classes of an equivalence relation on $A$ form a **partition** of $A$:
1. Every equivalence class is non-empty ($a \in [a]$ by reflexivity).
2. Any two equivalence classes are either **completely identical** or **completely disjoint** (no overlap!):
   $$[a] = [b] \iff (a, b) \in R, \quad \text{otherwise } [a] \cap [b] = \emptyset$$
3. The union of all equivalence classes equals the entire set $A$: $\bigcup_{a \in A} [a] = A$.

---

### 📝 Worked Past Exam Problem: Congruence Modulo $m$
> **Question**: Prove that the relation $R$ on the set of integers $\mathbb{Z}$ defined by $a \, R \, b \iff a \equiv b \pmod m$ (i.e., $m$ divides $a - b$) is an equivalence relation. What are its equivalence classes?
>
> **Solution**:
> 1. **Reflexive**:  
>    For any $a \in \mathbb{Z}$, $a - a = 0 = 0 \cdot m$.  
>    Since $m \mid 0$, $a \equiv a \pmod m$, so $(a, a) \in R$. $\implies$ **Reflexive**.
>
> 2. **Symmetric**:  
>    Suppose $(a, b) \in R$. Then $m \mid (a - b) \implies a - b = k \cdot m$ for some integer $k$.  
>    Multiply by $-1$: $b - a = (-k) \cdot m$.  
>    Since $-k \in \mathbb{Z}$, $m \mid (b - a) \implies b \equiv a \pmod m$, so $(b, a) \in R$. $\implies$ **Symmetric**.
>
> 3. **Transitive**:  
>    Suppose $(a, b) \in R$ and $(b, c) \in R$.  
>    Then $a - b = k_1 m$ and $b - c = k_2 m$ for integers $k_1, k_2$.  
>    Add the two equations:  
>    $$(a - b) + (b - c) = a - c = (k_1 + k_2) m$$  
>    Since $(k_1 + k_2) \in \mathbb{Z}$, $m \mid (a - c) \implies a \equiv c \pmod m$, so $(a, c) \in R$. $\implies$ **Transitive**.
>
> **Conclusion**: Since $R$ is reflexive, symmetric, and transitive, it is an **Equivalence Relation**.
>
> **Equivalence Classes**:  
> For modulo $m$, there are exactly $m$ disjoint equivalence classes corresponding to the possible remainders upon division by $m$:
> $$[0] = \{\dots, -2m, -m, 0, m, 2m, \dots\}$$
> $$[1] = \{\dots, -2m+1, -m+1, 1, m+1, 2m+1, \dots\}$$
> $$\dots$$
> $$[m-1] = \{\dots, -m-1, -1, m-1, 2m-1, \dots\}$$

---

## 3. Partial Order Relations & Posets

### 3.1 What is a POSET?
A relation $R$ on a set $A$ is a **Partial Ordering** (or Partial Order) if and only if it satisfies all 3 conditions:
1. **Reflexive**
2. **Anti-symmetric**
3. **Transitive**

A set $A$ together with a partial order $\le$ is called a **Partially Ordered Set**, denoted as **$(A, \le)$** or simply a **POSET**.

*Everyday Analogies*:
* $(\mathbb{Z}, \le)$ — standard "less than or equal to" order.
* $(P(S), \subseteq)$ — subset inclusion on the power set of $S$.
* $(\mathbb{Z}^+, \mid)$ — divisibility relation ("$a$ divides $b$").

---

### 3.2 Comparable vs Incomparable Elements
In a poset $(A, \le)$:
* Two elements $a, b \in A$ are **comparable** if either $a \le b$ or $b \le a$.
* Two elements are **incomparable** if neither $a \le b$ nor $b \le a$ holds.
* **Total Order (Chain)**: If **every pair** of elements in $A$ is comparable, $(A, \le)$ is a **Totally Ordered Set** or a **Chain**.

---

## 4. Hasse Diagrams: Drawing & Reading (Guaranteed 5-Mark Question)

### 4.1 What is a Hasse Diagram?
A Hasse diagram is a simplified visual representation of a finite poset that strips away redundant information:

```text
               HOW TO BUILD A HASSE DIAGRAM:
1. Remove all self-loops:       Reflexivity is assumed (every element is related to itself).
2. Remove all transitive edges: If a → b and b → c, erase the shortcut edge a → c!
3. Orient edges upwards:        If a ≤ b, place b strictly HIGHER than a.
4. Replace arrows with lines:   Direction is always bottom-to-top by convention.
```

---

### 4.2 Standard Poset 1: Divisibility Poset $(D_n, \mid)$
$D_n$ is the set of all positive integer divisors of $n$, ordered by divisibility ($a \le b \iff a \mid b$).

#### 📝 Worked Example: Draw Hasse Diagram for $D_{12}$
* Divisors of 12: $D_{12} = \{1, 2, 3, 4, 6, 12\}$.
* Divisibility relations:
  * $1$ divides everything (bottom element).
  * $2 \mid 4$, $2 \mid 6$.
  * $3 \mid 6$.
  * $4 \mid 12$, $6 \mid 12$.
  * $12$ is divisible by everything (top element).

```text
                  12  ◄── Top (Greatest Element)
                 /  \
                4    6
                │   / │
                │  3  │
                │ /   │
                2 ────┘
                 \   /
                   1  ◄── Bottom (Least Element)
```

#### 📝 Worked Example: Draw Hasse Diagram for $D_{30}$
* Divisors of 30 ($2 \times 3 \times 5$): $D_{30} = \{1, 2, 3, 5, 6, 10, 15, 30\}$.
* Notice it forms a **3-dimensional Boolean Cube**!

```text
                    30
                 /   │  \
               6    10   15
              / \  /  \  / \
             2    3     5
              \   │    /
                  1
```

---

## 5. Extremal Elements in Posets (Definitions You Must Not Confuse)

Look at any Hasse diagram. Professors test your ability to distinguish **Maximal** vs **Greatest** and **Minimal** vs **Least**.

```text
┌────────────────────┬────────────────────────────────────────────────────────┐
│ Term               │ Precise Definition & How to Spot in Hasse Diagram      │
├────────────────────┼────────────────────────────────────────────────────────┤
│ Maximal Element    │ An element a such that NO element is strictly above it.│
│                    │ (Can be MULTIPLE maximal elements at the top level!)   │
├────────────────────┼────────────────────────────────────────────────────────┤
│ Greatest Element   │ A UNIQUE element that is above EVERY other element.    │
│ (Maximum / Top 1)  │ (If it exists, it is unique. Poset might NOT have one!)│
├────────────────────┼────────────────────────────────────────────────────────┤
│ Minimal Element    │ An element b such that NO element is strictly below it.│
│                    │ (Can be MULTIPLE minimal elements at the bottom level!)│
├────────────────────┼────────────────────────────────────────────────────────┤
│ Least Element      │ A UNIQUE element that is below EVERY other element.    │
│ (Minimum / Bot 0)  │ (If it exists, it is unique. Poset might NOT have one!)│
└────────────────────┴────────────────────────────────────────────────────────┘
```

> ⚠️ **THE GOLDEN DIFFERENCE**:  
> * A poset can have **several maximal elements**, but it can have **at most ONE greatest element**.  
> * If a poset has a unique greatest element, that element is also the only maximal element.  
> * If a poset has multiple maximal elements, it has **NO greatest element**!

---

## 6. Upper Bounds, Lower Bounds, LUB and GLB

Let $B$ be a subset of a poset $(A, \le)$:

1. **Upper Bound of $B$**: An element $u \in A$ such that $x \le u$ for **all** $x \in B$.
2. **Lower Bound of $B$**: An element $l \in A$ such that $l \le x$ for **all** $x \in B$.
3. **Least Upper Bound (LUB / Supremum / Join $\vee$)**:
   * An upper bound $M$ of $B$ such that for any other upper bound $u$, $M \le u$.
   * *Intuition*: The "lowest" among all common upper bounds.
4. **Greatest Lower Bound (GLB / Infimum / Meet $\wedge$)**:
   * A lower bound $m$ of $B$ such that for any other lower bound $l$, $l \le m$.
   * *Intuition*: The "highest" among all common lower bounds.

---

### 📝 Worked Past Exam Problem: Finding GLB and LUB in a Poset
> **Question**: In the poset $(D_{24}, \mid)$ where $D_{24} = \{1, 2, 3, 4, 6, 8, 12, 24\}$:  
> Find: (a) $\text{GLB}(6, 8)$ and $\text{LUB}(6, 8)$, (b) $\text{GLB}(4, 12)$ and $\text{LUB}(4, 12)$.
>
> **Solution**:
> * In any divisibility poset $(D_n, \mid)$:
>   * $\text{GLB}(a, b) = \gcd(a, b)$ (Greatest Common Divisor).
>   * $\text{LUB}(a, b) = \operatorname{lcm}(a, b)$ (Least Common Multiple).
>
> 1. For $a = 6, b = 8$:
>    * Lower bounds of $\{6, 8\}$ in $D_{24}$ are common divisors: $\{1, 2\}$.  
>      The greatest of these is $2$. $\implies \mathbf{\text{GLB}(6, 8) = \gcd(6, 8) = 2}$.
>    * Upper bounds of $\{6, 8\}$ in $D_{24}$ are common multiples: $\{24\}$.  
>      $\implies \mathbf{\text{LUB}(6, 8) = \operatorname{lcm}(6, 8) = 24}$.
>
> 2. For $a = 4, b = 12$:
>    * Since $4 \mid 12$:
>    * $\mathbf{\text{GLB}(4, 12) = 4}$.
>    * $\mathbf{\text{LUB}(4, 12) = 12}$.

---

## 💡 Module 2 Summary Checklist & Exam Traps

- [ ] To prove an Equivalence Relation: You MUST write out all 3 proofs (Reflexive, Symmetric, Transitive) with clear algebra.
- [ ] In drawing Hasse diagrams: NEVER draw horizontal edges; always place larger elements strictly higher up.
- [ ] Check divisibility posets: The bottom element is always $1$, and the top is always $n$.
- [ ] If a question asks for LUB/GLB in $D_n$, remember: **GLB = GCD**, **LUB = LCM**!
