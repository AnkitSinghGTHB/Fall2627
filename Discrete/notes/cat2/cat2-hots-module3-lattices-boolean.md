# ⚡ CAT-2 Master Crib: Module 3 — Lattices & Boolean Algebra
**Course**: MAT2002 — Discrete Mathematics & Graph Theory  
**Faculty / Syllabus Scope**: CO3 / Module 3 (CAT-2 Strict Coverage)  
**Format**: Comprehensive, Rigorous, Fully Worked Examples & Copy-Ready Solutions

---

## Table of Contents
1. [Partially Ordered Sets (Posets) & Hasse Diagrams](#1-partially-ordered-sets-posets--hasse-diagrams)
2. [Lattices as Posets & Algebraic Lattices](#2-lattices-as-posets--algebraic-lattices)
3. [Special Lattice Families: Distributive, Modular, Bounded & Complemented](#3-special-lattice-families)
4. [Boolean Algebra as a Lattice](#4-boolean-algebra-as-a-lattice)
5. [Canonical Normal Forms: Minterms, Maxterms, PDNF & PCNF](#5-canonical-normal-forms-minterms-maxterms-pdnf--pcnf)
6. [Switching Circuits & Contact Networks](#6-switching-circuits--contact-networks)
7. [Comprehensive Classroom & Exam Solved HOTS Problems](#7-comprehensive-classroom--exam-solved-hots-problems)

---

## 1. Partially Ordered Sets (Posets) & Hasse Diagrams

### 1.1 Formal Definition of a Poset
A binary relation $R$ (often written $\le$) on a non-empty set $P$ is called a **partial order** if and only if it satisfies three foundational axioms:
1. **Reflexive**: $\forall a \in P, \; a \le a$.
2. **Antisymmetric**: $\forall a, b \in P, \; (a \le b \land b \le a) \implies a = b$.
3. **Transitive**: $\forall a, b, c \in P, \; (a \le b \land b \le c) \implies a \le c$.

The pair $(P, \le)$ is called a **Partially Ordered Set (Poset)**. If every pair of elements $a, b \in P$ is comparable (either $a \le b$ or $b \le a$), $(P, \le)$ is a **Totally Ordered Set (Chain)**.

---

### 1.2 Canonical Poset Examples

#### 1. Divisibility Poset $(D_n, \mid)$
Let $D_n$ be the set of all positive divisors of an integer $n$, ordered by divisibility ($a \mid b \iff \exists k \in \mathbb{Z}^+ \text{ such that } b = k a$).
* **Divisibility is Reflexive**: $a \mid a$ since $a = 1 \cdot a$.
* **Divisibility is Antisymmetric**: If $a \mid b$ and $b \mid a$, then $b = k_1 a$ and $a = k_2 b \implies k_1 k_2 = 1 \implies a = b$.
* **Divisibility is Transitive**: If $a \mid b$ and $b \mid c$, then $b = k_1 a$ and $c = k_2 b \implies c = (k_1 k_2) a \implies a \mid c$.

#### 2. Power Set Poset $(\mathcal{P}(S), \subseteq)$
For any set $S$, the power set $\mathcal{P}(S)$ ordered by subset inclusion $\subseteq$ is a poset.
* Size of $\mathcal{P}(S)$ is $2^{|S|}$.

#### 3. Lexicographical Poset on Cartesian Products $(A \times B, \le_{\text{lex}})$
Defined by $(a_1, b_1) \le_{\text{lex}} (a_2, b_2) \iff a_1 < a_2 \lor (a_1 = a_2 \land b_1 \le b_2)$.

---

### 1.3 Hasse Diagrams
A **Hasse diagram** is an undirected visual representation of a finite poset where:
1. Reflexive loops $(a \le a)$ are omitted.
2. Transitive edges (if $a \le b$ and $b \le c$, the direct line $a \to c$) are omitted.
3. If $a < b$, vertex $b$ is placed **strictly higher vertically** than vertex $a$.
4. An edge connects $a$ and $b$ if and only if $b$ **covers** $a$ ($a \prec b$), meaning $a < b$ and no element $c$ satisfies $a < c < b$.

```
       Hasse Diagram of D30 = {1, 2, 3, 5, 6, 10, 15, 30}
       ----------------------------------------------------
                            30 (Top / 1)
                           / | \
                          /  |  \
                         6   10  15
                        / \ /  \ / \
                       /   X    X   \
                      2       3      5
                       \      |     /
                        \     |    /
                          1 (Bottom / 0)
```

---

### 1.4 Extremal Elements in Posets

| Term | Formal Definition | Uniqueness |
| :--- | :--- | :--- |
| **Maximal Element** | $m \in P$ is maximal if $\nexists x \in P$ such that $m < x$. | Can have **multiple** maximal elements. |
| **Minimal Element** | $m \in P$ is minimal if $\nexists x \in P$ such that $x < m$. | Can have **multiple** minimal elements. |
| **Greatest Element (Top / 1)** | $g \in P$ is greatest if $\forall x \in P, \; x \le g$. | If it exists, it is **strictly UNIQUE**. |
| **Least Element (Bottom / 0)** | $l \in P$ is least if $\forall x \in P, \; l \le x$. | If it exists, it is **strictly UNIQUE**. |

> **Critical Distinction**: Every greatest element is maximal, but a maximal element is NOT necessarily greatest! If a finite poset has a unique maximal element, that element is the greatest element.

---

## 2. Lattices as Posets & Algebraic Lattices

### 2.1 Order-Theoretic Definition
A poset $(L, \le)$ is called a **Lattice** if for every pair of elements $a, b \in L$:
1. The set $\{a, b\}$ has a **unique Least Upper Bound (LUB)**, denoted $a \vee b$ (**Join** or $\sup\{a, b\}$).
2. The set $\{a, b\}$ has a **unique Greatest Lower Bound (GLB)**, denoted $a \wedge b$ (**Meet** or $\inf\{a, b\}$).

$$\forall a, b \in L: \quad \exists ! \; (a \vee b) \in L \quad \text{and} \quad \exists ! \; (a \wedge b) \in L$$

* In $(D_n, \mid)$: $a \vee b = \text{lcm}(a, b)$, and $a \wedge b = \gcd(a, b)$.
* In $(\mathcal{P}(S), \subseteq)$: $A \vee B = A \cup B$, and $A \wedge B = A \cap B$.
* In $(\mathbb{R}, \le)$: $a \vee b = \max(a, b)$, and $a \wedge b = \min(a, b)$.

---

### 2.2 Algebraic Definition of a Lattice
An algebraic structure $(L, \vee, \wedge)$ with two binary operations is a lattice if and only if for all $a, b, c \in L$:
1. **Idempotent Laws**:
   $$a \vee a = a, \qquad a \wedge a = a$$
2. **Commutative Laws**:
   $$a \vee b = b \vee a, \qquad a \wedge b = b \wedge a$$
3. **Associative Laws**:
   $$(a \vee b) \vee c = a \vee (b \vee c), \qquad (a \wedge b) \wedge c = a \wedge (b \wedge c)$$
4. **Absorption Laws**:
   $$a \vee (a \wedge b) = a, \qquad a \wedge (a \vee b) = a$$

> **The Bridge Theorem (Equivalence of Order and Algebra)**:
> In any lattice $(L, \le)$:
> $$a \le b \iff a \wedge b = a \iff a \vee b = b$$

---

### 2.3 Visual Signatures of Non-Lattices
A finite poset fails to be a lattice if any pair of elements has:
1. **No upper bound** or **multiple minimal upper bounds** (no unique lowest roof).
2. **No lower bound** or **multiple maximal lower bounds** (no unique highest floor).

```
   FAIL 1: Two Separate Roofs               FAIL 2: Two Separate Basements
   --------------------------               ------------------------------
             c     d                                    c     d
              \   /                                      \   /
               \ /                                        \ /
                a                                          a
              (LUB(a,b) does not exist!                 (GLB(c,d) does not exist!
               Both c and d are minimal upper bounds)    Both a and b are maximal lower bounds)
```

---

## 3. Special Lattice Families

### 3.1 Distributive Lattices
A lattice $(L, \vee, \wedge)$ is **Distributive** if meet distributes over join AND join distributes over meet:
1. $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c) \quad \forall a, b, c \in L$
2. $a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c) \quad \forall a, b, c \in L$

> **Key Fact**: In any lattice, if one distributive law holds, the other holds automatically!

#### Birkhoff's Representation Theorem (Forbidden Sublattices)
> **Theorem**: A lattice $L$ is distributive if and only if **no sublattice** of $L$ is isomorphic to either:
> 1. The **Diamond Lattice $M_3$** (5-element non-distributive modular lattice).
> 2. The **Pentagon Lattice $N_5$** (5-element non-distributive non-modular lattice).

```
        DIAMOND LATTICE M3                       PENTAGON LATTICE N5
      (Non-Distributive, Modular)           (Non-Distributive, Non-Modular)
      ---------------------------           -------------------------------
                   1                                       1
                 / | \                                    / \
                /  |  \                                  /   \
               a   b   c                                b     \
                \  |  /                                 |      c
                 \ | /                                  a     /
                   0                                     \   /
                                                           0
```

##### Algebraic Counterexample on $M_3$:
* $a \wedge (b \vee c) = a \wedge 1 = \mathbf{a}$.
* $(a \wedge b) \vee (a \wedge c) = 0 \vee 0 = \mathbf{0}$.
* Since $a \ne 0$, distributivity fails!

##### Algebraic Counterexample on $N_5$ (with $a < b$):
* $b \wedge (a \vee c) = b \wedge 1 = \mathbf{b}$.
* $(b \wedge a) \vee (b \wedge c) = a \vee 0 = \mathbf{a}$.
* Since $b \ne a$, distributivity fails!

---

### 3.2 Bounded Lattices
A lattice $(L, \vee, \wedge)$ is **bounded** if it contains a least element $0$ and a greatest element $1$:
$$\forall a \in L: \quad a \vee 0 = a, \quad a \wedge 0 = 0, \quad a \vee 1 = 1, \quad a \wedge 1 = a$$
* Every finite lattice is bounded: $0 = \bigwedge_{x \in L} x$ and $1 = \bigvee_{x \in L} x$.

---

### 3.3 Complemented Lattices
In a bounded lattice $(L, \vee, \wedge, 0, 1)$, an element $b \in L$ is called a **complement** of $a \in L$ if:
$$a \vee b = 1 \quad \text{and} \quad a \wedge b = 0$$
* A lattice is **complemented** if **every element** in $L$ has at least one complement.

#### Fundamental Theorems on Complements:
1. **Uniqueness Theorem**: In a **distributive lattice**, if an element has a complement, that complement is **strictly unique**!
   * *Proof*: Suppose $b_1$ and $b_2$ are both complements of $a$.
     $$b_1 = b_1 \wedge 1 = b_1 \wedge (a \vee b_2) = (b_1 \wedge a) \vee (b_1 \wedge b_2) = 0 \vee (b_1 \wedge b_2) = b_1 \wedge b_2$$
     Similarly, $b_2 = b_2 \wedge (a \vee b_1) = b_1 \wedge b_2$.
     Therefore, $b_1 = b_2$.
2. **Non-Uniqueness in $M_3$**: In the Diamond lattice $M_3$, element $a$ has two complements: $b$ and $c$. (Complements are NOT unique because $M_3$ is not distributive).
3. **Divisor Lattice Square-Free Condition**: $(D_n, \mid)$ is complemented $\iff$ $n$ is **square-free** (no repeated prime factors: $n = p_1 p_2 \dots p_k$).
   * $D_{12} = D_{2^2 \times 3}$: NOT complemented (2 and 6 have no complements).
   * $D_{18} = D_{2 \times 3^2}$: NOT complemented (3 and 6 have no complements).
   * $D_{30} = D_{2 \times 3 \times 5}$: Complemented!

---

## 4. Boolean Algebra as a Lattice

### 4.1 Definition
A **Boolean Algebra** is a complemented, distributive bounded lattice:
$$\mathcal{B} = (B, \vee, \wedge, ', 0, 1)$$

### 4.2 Axiomatic Laws of Boolean Algebra

| Law Name | Join ($\vee$ / OR / $+$) Form | Meet ($\wedge$ / AND / $\cdot$) Form |
| :--- | :--- | :--- |
| **Closure** | $a \vee b \in B$ | $a \wedge b \in B$ |
| **Commutative** | $a \vee b = b \vee a$ | $a \wedge b = b \wedge a$ |
| **Associative** | $(a \vee b) \vee c = a \vee (b \vee c)$ | $(a \wedge b) \wedge c = a \wedge (b \wedge c)$ |
| **Distributive** | $a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c)$ | $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$ |
| **Identity** | $a \vee 0 = a$ | $a \wedge 1 = a$ |
| **Complement** | $a \vee a' = 1$ | $a \wedge a' = 0$ |
| **Idempotent** | $a \vee a = a$ | $a \wedge a = a$ |
| **Domination / Boundedness** | $a \vee 1 = 1$ | $a \wedge 0 = 0$ |
| **Absorption** | $a \vee (a \wedge b) = a$ | $a \wedge (a \vee b) = a$ |
| **Involution (Double Negation)** | $(a')' = a$ | $(a')' = a$ |
| **De Morgan's Laws** | $(a \vee b)' = a' \wedge b'$ | $(a \wedge b)' = a' \vee b'$ |

> **Duality Principle**: Any true Boolean identity remains true if we interchange $\vee \leftrightarrow \wedge$ and $0 \leftrightarrow 1$.

### 4.3 Size of Finite Boolean Algebras
* **Stone's Representation Theorem Corollary**: Every finite Boolean algebra is isomorphic to the power set $\mathcal{P}(S)$ for some finite set $S$.
* Therefore, the number of elements in any finite Boolean algebra must be a power of 2:
  $$|B| = 2^n \quad \text{for some integer } n \ge 1$$
* Any lattice with order $3, 5, 6, 7, 9, 10, 11, 12, \dots$ **CANNOT be a Boolean Algebra**!

---

## 5. Canonical Normal Forms: Minterms, Maxterms, PDNF & PCNF

### 5.1 Definitions
Let $x_1, x_2, \dots, x_n$ be $n$ Boolean variables.
* A **literal** is a variable $x_i$ or its complement $x_i'$.
* A **Minterm** (Boolean product term) is a conjunction of $n$ literals in which each variable appears exactly once (uncomplemented or complemented).
  * Evaluates to $1$ for exactly **one** truth assignment.
  * For $n=3$ variables $(x, y, z)$:
    $$m_0 = x' y' z' \; (000), \quad m_1 = x' y' z \; (001), \quad \dots, \quad m_7 = x y z \; (111)$$
* A **Maxterm** (Boolean sum term) is a disjunction of $n$ literals in which each variable appears exactly once.
  * Evaluates to $0$ for exactly **one** truth assignment.
  * For $n=3$:
    $$M_0 = x + y + z \; (000), \quad M_1 = x + y + z' \; (001), \quad \dots, \quad M_7 = x' + y' + z' \; (111)$$

> **Fundamental Duality**:
> $$M_i = (m_i)' \quad \text{and} \quad m_i = (M_i)'$$

---

### 5.2 PDNF (Principal Disjunctive Normal Form / Sum of Minterms)
* **Definition**: A sum-of-products expression containing **only minterms**:
  $$\text{PDNF} = \sum m(i_1, i_2, \dots, i_k) = m_{i_1} \vee m_{i_2} \vee \dots \vee m_{i_k}$$
* **Step-by-Step Construction via Truth Table**:
  1. Construct the complete truth table for the formula $f(x_1, \dots, x_n)$.
  2. Identify all rows where the output $f = 1$.
  3. Write the minterm for each row ($x_i$ if value is 1, $x_i'$ if value is 0).
  4. Disjoin (OR / $\vee$) all corresponding minterms.

* **Algebraic Construction Method**:
  1. Put expression into Disjunctive Normal Form (sum of product terms).
  2. If a product term lacks variable $x_k$, multiply it by $(x_k \vee x_k')$:
     $$P = P \wedge (x_k \vee x_k') = (P \wedge x_k) \vee (P \wedge x_k')$$
  3. Expand using distributive laws and remove duplicates using $A \vee A = A$.

---

### 5.3 PCNF (Principal Conjunctive Normal Form / Product of Maxterms)
* **Definition**: A product-of-sums expression containing **only maxterms**:
  $$\text{PCNF} = \prod M(j_1, j_2, \dots, j_m) = M_{j_1} \wedge M_{j_2} \wedge \dots \wedge M_{j_m}$$
* **Step-by-Step Construction via Truth Table**:
  1. From the truth table, identify all rows where the output $f = 0$.
  2. Write the maxterm for each row ($x_i'$ if value is 1, $x_i$ if value is 0).
  3. Conjoin (AND / $\wedge$) all corresponding maxterms.

> **Master Complementary Relationship**:
> If a 3-variable function has:
> $$\text{PDNF} = \sum m(1, 3, 5, 7) \implies \text{PCNF} = \prod M(0, 2, 4, 6)$$
> The indices of PCNF are exactly the complement of the minterm index set $\{0, 1, \dots, 2^n - 1\} \setminus \text{PDNF}$!

---

## 6. Switching Circuits & Contact Networks

In switching theory (Shannon's application of Boolean algebra):
* **Switch $A$ Closed**: $A = 1$ (Current flows).
* **Switch $A$ Open**: $A = 0$ (No current).
* **Series Connection**: Current flows $\iff$ both switch $A$ AND switch $B$ are closed $\implies \mathbf{A \cdot B}$ (Conjunction).
* **Parallel Connection**: Current flows $\iff$ switch $A$ OR switch $B$ is closed $\implies \mathbf{A + B}$ (Disjunction).
* **Inverted Switch**: Normally closed switch operated by relay $\implies \mathbf{A'}$ (NOT).

```
   SERIES (AND: A * B)                  PARALLEL (OR: A + B)
   -------------------                  --------------------
       A         B                               +--- A ---+
   o--[ ]-------[ ]--o                       o---|         |---o
                                                 +--- B ---+
```

---

## 7. Comprehensive Classroom & Exam Solved HOTS Problems

### Problem 1: Full Conversion of $f = p \wedge (q \vee r)$ into PDNF and PCNF

#### Algebraic Method:
1. **Find PDNF**:
   $$f = p \wedge (q \vee r) = (p \wedge q) \vee (p \wedge r)$$
   * Term $(p \wedge q)$ lacks $r$:
     $$(p \wedge q) \wedge (r \vee r') = (p \wedge q \wedge r) \vee (p \wedge q \wedge r')$$
   * Term $(p \wedge r)$ lacks $q$:
     $$(p \wedge r) \wedge (q \vee q') = (p \wedge q \wedge r) \vee (p \wedge q' \wedge r)$$
   * Combine and eliminate duplicate $(p \wedge q \wedge r)$:
     $$\mathbf{\text{PDNF} = (p \wedge q \wedge r) \vee (p \wedge q \wedge r') \vee (p \wedge q' \wedge r)}$$
     $$\text{PDNF} = m_7 \vee m_6 \vee m_5 = \sum m(5, 6, 7)$$

2. **Find PCNF**:
   The full set of 3-variable indices is $\{0, 1, 2, 3, 4, 5, 6, 7\}$.
   The indices where $f = 0$ are:
   $$\{0, 1, 2, 3, 4\}$$
   Therefore:
   $$\text{PCNF} = \prod M(0, 1, 2, 3, 4) = M_0 \wedge M_1 \wedge M_2 \wedge M_3 \wedge M_4$$
   $$\mathbf{\text{PCNF} = (p \vee q \vee r) \wedge (p \vee q \vee r') \wedge (p \vee q' \vee r) \wedge (p \vee q' \vee r') \wedge (p' \vee q \vee r)}$$

#### Verification Truth Table:
| $p$ | $q$ | $r$ | $q \vee r$ | $f = p \wedge (q \vee r)$ | Minterm ($f=1$) | Maxterm ($f=0$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | **0** | — | $M_0 = p \vee q \vee r$ |
| 0 | 0 | 1 | 1 | **0** | — | $M_1 = p \vee q \vee r'$ |
| 0 | 1 | 0 | 1 | **0** | — | $M_2 = p \vee q' \vee r$ |
| 0 | 1 | 1 | 1 | **0** | — | $M_3 = p \vee q' \vee r'$ |
| 1 | 0 | 0 | 0 | **0** | — | $M_4 = p' \vee q \vee r$ |
| 1 | 0 | 1 | 1 | **1** | $m_5 = p \wedge q' \wedge r$ | — |
| 1 | 1 | 0 | 1 | **1** | $m_6 = p \wedge q \wedge r'$ | — |
| 1 | 1 | 1 | 1 | **1** | $m_7 = p \wedge q \wedge r$ | — |

---

### Problem 2: Full PDNF and PCNF of Complex Implication
**Question**: Obtain the PDNF and PCNF of the formula:
$$f = ((p \wedge q) \vee (\sim p \to r)) \to (\sim q \wedge r)$$

#### Step-by-Step Truth Table Construction:
1. Recall standard equivalences:
   * $\sim p \to r \equiv \sim(\sim p) \vee r \equiv p \vee r$.
   * Antecedent: $A = (p \wedge q) \vee (p \vee r) \equiv p \vee r$ (since $p \wedge q \le p \le p \vee r$ by absorption).
   * Consequent: $B = \sim q \wedge r$.
   * $f = A \to B \equiv \sim A \vee B \equiv \sim(p \vee r) \vee (\sim q \wedge r) \equiv (\sim p \wedge \sim r) \vee (\sim q \wedge r)$.

2. **Evaluate Rows**:
   * Row 0 $(p=0, q=0, r=0)$: $\sim p \wedge \sim r = 1 \wedge 1 = 1 \implies \mathbf{f = 1} \implies m_0$.
   * Row 1 $(p=0, q=0, r=1)$: $\sim q \wedge r = 1 \wedge 1 = 1 \implies \mathbf{f = 1} \implies m_1$.
   * Row 2 $(p=0, q=1, r=0)$: $\sim p \wedge \sim r = 1 \wedge 1 = 1 \implies \mathbf{f = 1} \implies m_2$.
   * Row 3 $(p=0, q=1, r=1)$: Both terms 0 $\implies \mathbf{f = 0} \implies M_3$.
   * Row 4 $(p=1, q=0, r=0)$: Both terms 0 $\implies \mathbf{f = 0} \implies M_4$.
   * Row 5 $(p=1, q=0, r=1)$: $\sim q \wedge r = 1 \wedge 1 = 1 \implies \mathbf{f = 1} \implies m_5$.
   * Row 6 $(p=1, q=1, r=0)$: Both terms 0 $\implies \mathbf{f = 0} \implies M_6$.
   * Row 7 $(p=1, q=1, r=1)$: Both terms 0 $\implies \mathbf{f = 0} \implies M_7$.

3. **Final Forms**:
   * Rows where $f=1$: $\{0, 1, 2, 5\}$
     $$\mathbf{\text{PDNF} = m_0 \vee m_1 \vee m_2 \vee m_5 = \sum m(0, 1, 2, 5)}$$
     $$\text{PDNF} = (\sim p \wedge \sim q \wedge \sim r) \vee (\sim p \wedge \sim q \wedge r) \vee (\sim p \wedge q \wedge \sim r) \vee (p \wedge \sim q \wedge r)$$
   * Rows where $f=0$: $\{3, 4, 6, 7\}$
     $$\mathbf{\text{PCNF} = M_3 \wedge M_4 \wedge M_6 \wedge M_7 = \prod M(3, 4, 6, 7)}$$
     $$\text{PCNF} = (p \vee \sim q \vee \sim r) \wedge (\sim p \vee q \vee r) \wedge (\sim p \vee \sim q \vee r) \wedge (\sim p \vee \sim q \vee \sim r)$$

---

### Problem 3: Distributivity Test on Diamond Sublattice ($D_8$ vs $D_{30}$)
**Question**: Prove whether $(D_8, \mid)$ and $(D_{30}, \mid)$ are distributive lattices and Boolean algebras.

1. **Analysis of $(D_8, \mid)$**:
   * Divisors of 8: $D_8 = \{1, 2, 4, 8\}$.
   * Order: $1 \mid 2 \mid 4 \mid 8$.
   * This is a **Total Order (Chain)** of length 4.
   * Every chain is automatically a **distributive lattice**!
   * *Is it complemented?*
     * In a chain with $> 2$ elements, the intermediate elements have no complements.
     * For element $2$: $2 \wedge x = 1 \implies x = 1$. But $2 \vee 1 = 2 \ne 8$.
     * Thus, 2 has no complement.
   * **Conclusion**: $(D_8, \mid)$ is **distributive**, but **NOT complemented** $\implies$ **NOT a Boolean Algebra**.

2. **Analysis of $(D_{30}, \mid)$**:
   * Divisors of 30: $D_{30} = \{1, 2, 3, 5, 6, 10, 15, 30\}$.
   * $30 = 2 \times 3 \times 5$ (product of 3 distinct primes $\implies$ **square-free**).
   * For every divisor $d \in D_{30}$, its unique complement is $d' = 30 / d$:
     * $\gcd(d, 30/d) = 1$ (since no prime factor is repeated).
     * $\text{lcm}(d, 30/d) = 30$.
   * Distributivity: Integer $\gcd$ and $\text{lcm}$ always satisfy distributive laws.
   * Size: $|D_{30}| = 8 = 2^3$.
   * **Conclusion**: $(D_{30}, \mid)$ is **distributive AND complemented** $\implies$ **IS a Boolean Algebra** (isomorphic to $(\mathcal{P}(\{2, 3, 5\}), \subseteq)$).
