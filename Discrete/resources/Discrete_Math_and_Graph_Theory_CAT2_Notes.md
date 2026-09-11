# Discrete Mathematics & Graph Theory (Modules 3 & 4)
## Comprehensive Class Notes, Solutions & Gap-Filling Guide

---

## Table of Contents
1. [Module 3: Posets, Lattices, and Boolean Algebra](#module-3-posets-lattices-and-boolean-algebra)
   - [1.1 Partially Ordered Sets (Poset) Review](#11-partially-ordered-sets-poset-review)
   - [1.2 Definition of a Lattice](#12-definition-of-a-lattice)
   - [1.3 Class Examples & Problems on Lattices](#13-class-problems-on-lattices)
     - [Example 1: Divisor Poset $(D_{12}, \mid)$](#example-1-divisor-poset-d_12-mid)
     - [Example 2: Counterexample $A = \{1, 2, 3, 4, 6, 8, 9, 12, 18, 24\}$](#example-2-counterexample-with-relation-divides)
     - [Example 3: Power Set Poset $(\mathcal{P}(S), \subseteq)$](#example-3-power-set-poset-mathcarp-s-subseteq)
     - [Example 4: Divisor Poset $(D_{30}, \mid)$](#example-4-divisor-poset-d_30-mid)
     - [Example 5: Total Order $(\mathbb{N}, \le)$](#example-5-total-order-mathbbn-le)
   - [1.4 Distributive Lattices](#14-distributive-lattices)
     - [Definition & Distributive Laws](#definition--distributive-laws)
     - [Characterization: Pentagon ($N_5$) & Diamond ($M_3$) Sublattices](#characterization-pentagon-n_5--diamond-m_3-sublattices)
     - [Class Problems on Checking Distributivity](#class-problems-on-checking-distributivity)
   - [1.5 Bounded and Complemented Lattices](#15-bounded-and-complemented-lattices)
     - [Definitions & Properties](#definitions--properties)
     - [Complements in 5-Element Diamond Lattice](#complements-in-5-element-diamond-lattice)
     - [Complements in $(D_{18}, \mid)$](#complements-in-d_18-mid)
   - [1.6 Boolean Algebra](#16-boolean-algebra)
     - [Definition & Algebraic Axioms](#definition--algebraic-axioms)
     - [Boolean Space $B_n$ and Hypercube Representation](#boolean-space-b_n-and-hypercube-representation)
     - [Boolean Functions & Representations (Truth Tables, BDDs, Circuits)](#boolean-functions--representations)
   - [1.7 Normal Forms: Minterms, Maxterms, PDNF, and PCNF](#17-normal-forms-minterms-maxterms-pdnf-and-pcnf)
     - [Minterms vs. Maxterms](#minterms-vs-maxterms)
     - [Algorithm to Convert to PDNF and PCNF](#algorithm-to-convert-to-pdnf-and-pcnf)
     - [Problem 1: $f = p \wedge (q \vee r)$ (DNF, CNF, PDNF, PCNF)](#problem-1-f--p-wedge-q-vee-r)
     - [Problem 2: $f = ((p \wedge q) \vee (\sim p \to r)) \to (\sim q \wedge r)$](#problem-2-f--p-wedge-q-vee-sim-p-to-r-to-sim-q-wedge-r)
     - [Problem 3: Boolean Expression Simplification with XOR & De Morgan](#problem-3-boolean-expression-simplification)
2. [Module 4: Graph Theory](#module-4-graph-theory)
   - [2.1 Historical Origin: The Königsberg Bridge Problem](#21-historical-origin-the-königsberg-bridge-problem)
   - [2.2 Fundamental Graph Terminology & Definitions](#22-fundamental-graph-terminology--definitions)
     - [Order vs. Size Matrix](#order-vs-size-matrix)
     - [Graph Classifications (Simple, Multi, Pseudo, Directed)](#graph-classifications)
   - [2.3 Special Graph Families](#23-special-graph-families)
     - [Trivial, Null, Complete ($K_n$), and Star Graphs](#trivial-null-complete-and-star-graphs)
     - [Edge Formula for Complete Graphs & Number of Labelled Graphs](#edge-formula--number-of-labelled-graphs)
     - [Class Exercise: Minimum Vertices for Given Edges (Registration Number Problem)](#class-exercise-registration-number-problem)
   - [2.4 Bipartite Graphs & Complete Bipartite Graphs](#24-bipartite-graphs--complete-bipartite-graphs)
     - [Definition & Kőnig's Odd Cycle Theorem](#definition--kőnigs-odd-cycle-theorem)
     - [Complete Bipartite Graphs $K_{m, n}$](#complete-bipartite-graphs-k_m-n)
     - [Class Problem: Checking Bipartiteness on a 13-Vertex Graph](#class-problem-checking-bipartiteness)
   - [2.5 Complement of a Graph ($G^c$)](#25-complement-of-a-graph-g_c)
     - [Properties & Edge Sum Formula](#properties--edge-sum-formula)
     - [Examples ($C_4$ and 5-Vertex Graph)](#examples-c_4-and-5-vertex-graph)
   - [2.6 Neighborhoods, Degrees, and Regular Graphs](#26-neighborhoods-degrees-and-regular-graphs)
     - [Open & Closed Neighborhoods](#open--closed-neighborhoods)
     - [Degrees, $\delta(G)$, $\Delta(G)$, and $r$-Regular Graphs](#degrees-and-regular-graphs)
   - [2.7 Degree Sequences & Graphic Sequences](#27-degree-sequences--graphic-sequences)
     - [Havel-Hakimi Criterion](#havel-hakimi-criterion)
     - [Detailed Analysis of All 12 Class Test Sequences](#detailed-analysis-of-all-12-class-test-sequences)
   - [2.8 Euler's Handshaking Lemma & Applications](#28-eulers-handshaking-lemma--applications)
     - [Lemma 1 & Detailed Proof](#lemma-1--detailed-proof)
     - [Lemma 2: Even Number of Odd-Degree Vertices (Full Proof)](#lemma-2-even-number-of-odd-degree-vertices)
     - [Application 1: Friends in a Group / Pigeonhole Principle Proof](#application-1-friends-in-a-group--pigeonhole-principle)
   - [2.9 Subgraphs, Spanning Subgraphs, and Induced Subgraphs](#29-subgraphs-spanning-subgraphs-and-induced-subgraphs)
   - [2.10 Graph Isomorphism](#210-graph-isomorphism)
     - [Formal Definition & Graph Invariants](#formal-definition--graph-invariants)
     - [Class Problem 1: 4-Cycle Isomorphism Mapping](#class-problem-1-4-cycle-isomorphism-mapping)
     - [Class Problem 2: 6-Vertex Prism/Wheel Graph Analysis](#class-problem-2-6-vertex-prismwheel-graph-analysis)

---

# Module 3: Posets, Lattices, and Boolean Algebra

## 1.1 Partially Ordered Sets (Poset) Review
A relation $R$ on a set $P$ is called a **partial order** if it satisfies three axiomatic properties:
1. **Reflexive**: $\forall a \in P, \; a R a$.
2. **Antisymmetric**: $\forall a, b \in P, \; (a R b \land b R a) \implies a = b$.
3. **Transitive**: $\forall a, b, c \in P, \; (a R b \land b R c) \implies a R c$.

The pair $(P, R)$, often written $(P, \le)$, is called a **Partially Ordered Set (Poset)**.

---

## 1.2 Definition of a Lattice

### Order-Theoretic Definition:
A poset $(L, \le)$ is called a **lattice** if every pair of elements $a, b \in L$ has:
1. A unique **Least Upper Bound (LUB)**, called the **Join** of $a$ and $b$, denoted by:
   $$a \vee b = \text{LUB}(a, b) = \sup\{a, b\}$$
2. A unique **Greatest Lower Bound (GLB)**, called the **Meet** of $a$ and $b$, denoted by:
   $$a \wedge b = \text{GLB}(a, b) = \inf\{a, b\}$$

### Algebraic Definition:
A non-empty set $L$ equipped with two binary operations $\vee$ (join) and $\wedge$ (meet), denoted $(L, \vee, \wedge)$, is an algebraic lattice if the following identities hold for all $a, b, c \in L$:
* **Idempotent Laws**: $a \vee a = a$, $\quad a \wedge a = a$
* **Commutative Laws**: $a \vee b = b \vee a$, $\quad a \wedge b = b \wedge a$
* **Associative Laws**: $(a \vee b) \vee c = a \vee (b \vee c)$, $\quad (a \wedge b) \wedge c = a \wedge (b \wedge c)$
* **Absorption Laws**: $a \vee (a \wedge b) = a$, $\quad a \wedge (a \vee b) = a$

> **Key Connection**:
> $$a \le b \iff a \wedge b = a \iff a \vee b = b$$

---

## 1.3 Class Problems on Lattices

### Example 1: Divisor Poset $(D_{12}, \mid)$
Let $D_{12}$ be the set of all positive divisors of 12:
$$D_{12} = \{1, 2, 3, 4, 6, 12\}$$
The partial order relation is divisibility: $a \le b \iff a \mid b$ ($a$ divides $b$).

For any $a, b \in D_{12}$:
* $\text{GLB}(a, b) = a \wedge b = \gcd(a, b)$
* $\text{LUB}(a, b) = a \vee b = \operatorname{lcm}(a, b)$

#### Hasse Diagram for $D_{12}$:
```text
          12
         /  \
        4    6
        |  / |
        2    3
         \  /
           1
```

#### Meet (GLB / $\gcd$) Operation Table:
| $\wedge$ | **1** | **2** | **3** | **4** | **6** | **12** |
|:---------:|:-----:|:-----:|:-----:|:-----:|:-----:|:------:|
|   **1**   |   1   |   1   |   1   |   1   |   1   |   1    |
|   **2**   |   1   |   2   |   1   |   2   |   2   |   2    |
|   **3**   |   1   |   1   |   3   |   1   |   3   |   3    |
|   **4**   |   1   |   2   |   1   |   4   |   2   |   4    |
|   **6**   |   1   |   2   |   3   |   2   |   6   |   6    |
|  **12**   |   1   |   2   |   3   |   4   |   6   |   12   |

#### Join (LUB / $\operatorname{lcm}$) Operation Table:
|  $\vee$  | **1** | **2** | **3** | **4** | **6** | **12** |
|:---------:|:-----:|:-----:|:-----:|:-----:|:-----:|:------:|
|   **1**   |   1   |   2   |   3   |   4   |   6   |   12   |
|   **2**   |   2   |   2   |   6   |   4   |   6   |   12   |
|   **3**   |   3   |   6   |   3   |  12   |   6   |   12   |
|   **4**   |   4   |   4   |  12   |   4   |  12   |   12   |
|   **6**   |   6   |   6   |   6   |  12   |   6   |   12   |
|  **12**   |  12   |  12   |  12   |  12   |  12   |   12   |

**Conclusion**: Since $\gcd(a, b) \in D_{12}$ and $\operatorname{lcm}(a, b) \in D_{12}$ for every pair, $(D_{12}, \mid)$ is a **lattice**.

---

### Example 2: Counterexample with Relation "Divides"
**Problem from Notes**:
Let $A = \{1, 2, 3, 4, 6, 8, 9, 12, 18, 24\}$ with relation $a \mid b$. Is $(A, \mid)$ a lattice?

#### Hasse Diagram Analysis:
```text
        24        18
       /  \      /  \
      8    12    /    9
      |   /  \  /     |
      4  /     6      |
      | /     / \     |
      2      /   3----+
       \    /   /
         \  /  /
            1
```

#### Why $(A, \mid)$ is NOT a Lattice (Gap Filled):
1. **Missing Least Upper Bound for $\{8, 9\}$**:
   The common multiples of 8 and 9 must be multiples of $\operatorname{lcm}(8, 9) = 72$. Since $72 \notin A$, the pair $\{8, 9\}$ has **no upper bound at all** in $A$. Therefore, $\text{LUB}(8, 9)$ does not exist.
2. **Missing Least Upper Bound for $\{8, 12\}$**:
   Common multiples of 8 and 12 in $A$ are $\{24\}$. Here $\text{LUB}(8, 12) = 24$.
   However, for $\{12, 18\}$, common multiples require multiples of $\operatorname{lcm}(12, 18) = 36 \notin A$. Neither 24 nor 18 is a common multiple of both. Thus $\text{LUB}(12, 18)$ does not exist.
3. **Multiple Maximal Elements**:
   Elements $24$ and $18$ are both maximal, and there is no common top element.
**Conclusion**: $(A, \mid)$ is **NOT a lattice**.

---

### Example 3: Power Set Poset $(\mathcal{P}(S), \subseteq)$
**Problem**: Let $S$ be any non-empty set. Show that $(\mathcal{P}(S), \subseteq)$ is a lattice.

**Proof**:
Let $A, B \in \mathcal{P}(S)$.
1. **GLB**:
   - $A \cap B \subseteq A$ and $A \cap B \subseteq B$, so $A \cap B$ is a lower bound.
   - If $X \in \mathcal{P}(S)$ such that $X \subseteq A$ and $X \subseteq B$, then by set theory $X \subseteq (A \cap B)$.
   - Hence, $\text{GLB}(A, B) = A \wedge B = A \cap B \in \mathcal{P}(S)$.
2. **LUB**:
   - $A \subseteq A \cup B$ and $B \subseteq A \cup B$, so $A \cup B$ is an upper bound.
   - If $Y \in \mathcal{P}(S)$ such that $A \subseteq Y$ and $B \subseteq Y$, then $(A \cup B) \subseteq Y$.
   - Hence, $\text{LUB}(A, B) = A \vee B = A \cup B \in \mathcal{P}(S)$.

Since every pair of subsets has a GLB and LUB in $\mathcal{P}(S)$, $(\mathcal{P}(S), \subseteq)$ is a **lattice**.

---

### Example 4: Divisor Poset $(D_{30}, \mid)$
**Problem**: Let $D_{30} = \{1, 2, 3, 5, 6, 10, 15, 30\}$ under partial ordering $a \mid b$.
* a) Draw the Hasse diagram.
* b) Check if it is a lattice.
* c) Determine LUB and GLB of all pairs.

#### a) Hasse Diagram (Boolean Cubical Lattice):
```text
               30
            /   |   \
          15    10    6
         /  \  /  \  / \
        5     3     2
         \    |    /
               1
```
* **Level 0**: $1$
* **Level 1 (Primes)**: $2, 3, 5$
* **Level 2 (Products of 2 primes)**: $6 = 2 \times 3, \; 10 = 2 \times 5, \; 15 = 3 \times 5$
* **Level 3 (Product of 3 primes)**: $30 = 2 \times 3 \times 5$

#### b) & c) Mathematical Proof of Lattice Property:
For any $a, b \in D_{30}$:
* Let $x$ be an upper bound of $a$ and $b$:
  $$a \mid x \implies x = a \cdot k_1, \quad b \mid x \implies x = b \cdot k_2$$
  Therefore, $\operatorname{lcm}(a, b) \mid x$.
  Since $a \mid 30$ and $b \mid 30$, $\operatorname{lcm}(a, b) \mid 30$, which guarantees $\operatorname{lcm}(a, b) \in D_{30}$.
  Thus, $\text{LUB}(a, b) = \operatorname{lcm}(a, b)$.
* Let $y$ be a lower bound of $a$ and $b$:
  $$y \mid a \implies a = y \cdot k_1', \quad y \mid b \implies b = y \cdot k_2'$$
  Therefore, $y \mid \gcd(a, b)$.
  Since $\gcd(a, b)$ divides both $a$ and $b$, and $1 \le \gcd(a, b) \le 30$, we have $\gcd(a, b) \in D_{30}$.
  Thus, $\text{GLB}(a, b) = \gcd(a, b)$.

Because $\text{GLB}$ and $\text{LUB}$ exist for all pairs, $(D_{30}, \mid)$ is a **lattice** (in fact, isomorphic to the Boolean algebra $\mathcal{B}_3$).

---

### Example 5: Total Order $(\mathbb{N}, \le)$
**Problem**: For the poset $(\mathbb{N}, \le)$, find $\text{GLB}(a, b)$ and $\text{LUB}(a, b)$ for any $a, b \in \mathbb{N}$.

**Solution**:
Since $(\mathbb{N}, \le)$ is totally ordered (a chain), for any two elements $a, b$:
* Either $a \le b$ or $b \le a$.
* If $a \le b$:
  $$\text{GLB}(a, b) = \min(a, b) = a$$
  $$\text{LUB}(a, b) = \max(a, b) = b$$
Every totally ordered set is automatically a distributive lattice.

---

## 1.4 Distributive Lattices

### Definition & Distributive Laws
A lattice $(L, \wedge, \vee)$ is called a **distributive lattice** if for all $a, b, c \in L$, the operations satisfy the distributive laws:
1. $a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c)$
2. $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$

> **Theorem**: In any lattice, if one of the distributive laws holds, the other holds automatically.

### Characterization: Pentagon ($N_5$) & Diamond ($M_3$) Sublattices
> **Birkhoff's Theorem**: A lattice $L$ is distributive **if and only if** it does not contain a sublattice isomorphic to:
> 1. The **diamond lattice** $M_3$ (also called the 5-element non-distributive modular lattice)
> 2. The **pentagon lattice** $N_5$ (the non-modular lattice)

#### The Diamond Lattice $M_3$:
```text
        1
      / | \
     a  b  c
      \ | /
        0
```
Let us verify the failure of distributivity on $M_3$:
$$\text{LHS} = a \vee (b \wedge c) = a \vee 0 = a$$
$$\text{RHS} = (a \vee b) \wedge (a \vee c) = 1 \wedge 1 = 1$$
Since $\text{LHS} \ne \text{RHS}$ ($a \ne 1$), the lattice is **non-distributive**.

Also check the second law:
$$\text{LHS} = a \wedge (b \vee c) = a \wedge 1 = a$$
$$\text{RHS} = (a \wedge b) \vee (a \wedge c) = 0 \vee 0 = 0$$
Again, $a \ne 0$, confirming failure.

---

### Class Problems on Checking Distributivity

#### Problem from Notes: Test the 10-Element Lattice
```text
               1
             /   \
            c     L
           / \   / \
          b   d e   f
           \ /   \ /
            a     g
             \   /
               0
```
**Analysis**:
Notice the sublattices:
* On the left: between $a$ and $c$, elements $\{a, b, d, c\}$ form a diamond-like structure if an extra center element is present, or let's test elements $b, d$:
  - $b \vee d = c$
  - $b \wedge d = a$
* Consider elements $b, d, g$:
  - $b \wedge (d \vee g) = b \wedge 1 = b$
  - $(b \wedge d) \vee (b \wedge g) = a \vee 0 = a$
  - Since $b \ne a$, the distributive law **fails**!
* In the notes:
  - $\text{LHS} = a \wedge (b \vee c) = \text{GLB}(a, \text{LUB}(b, c))$
  - Comparing with $(a \wedge b) \vee (a \wedge c)$
**Conclusion**: The lattice is **NOT distributive**.

---

## 1.5 Bounded and Complemented Lattices

### Definitions & Properties
1. **Bounded Lattice**: A lattice $(L, \wedge, \vee)$ is bounded if it possesses:
   - A **least element** (denoted $0$) such that $\forall a \in L: \; 0 \le a$, i.e., $a \wedge 0 = 0$ and $a \vee 0 = a$.
   - A **greatest element** (denoted $1$) such that $\forall a \in L: \; a \le 1$, i.e., $a \wedge 1 = a$ and $a \vee 1 = 1$.
   A bounded lattice is denoted $(L, \wedge, \vee, 0, 1)$.
2. **Complement of an Element**: In a bounded lattice $(L, \wedge, \vee, 0, 1)$, an element $\bar{a} \in L$ is a **complement** of $a$ if:
   $$a \wedge \bar{a} = 0 \quad \text{and} \quad a \vee \bar{a} = 1$$
3. **Complemented Lattice**: A bounded lattice in which **every** element has at least one complement.

> **Key Theorem on Uniqueness of Complement**:
> In a **distributive bounded lattice**, if an element has a complement, that complement is **strictly unique**.
> (If an element has multiple complements, the lattice cannot be distributive!)

---

### Complements in 5-Element Diamond Lattice
Consider $M_3 = \{0, a, b, c, 1\}$:
* For $0$: complement is $1$ (since $0 \wedge 1 = 0$ and $0 \vee 1 = 1$).
* For $1$: complement is $0$.
* For $a$:
  - $a \wedge b = 0$ and $a \vee b = 1 \implies \bar{a} = b$
  - $a \wedge c = 0$ and $a \vee c = 1 \implies \bar{a} = c$
  - Therefore, $a$ has two complements: $\{b, c\}$.
* Similarly:
  - $\bar{b} = \{a, c\}$
  - $\bar{c} = \{a, b\}$
Because complements are not unique, $M_3$ is complemented, but **not distributive**.

---

### Complements in $(D_{18}, \mid)$
Let $D_{18} = \{1, 2, 3, 6, 9, 18\}$.
* Least element: $0 = 1$
* Greatest element: $1 = 18$

#### Operation Tables:
**Join ($\operatorname{lcm}$) Table**:
| $\vee$ | **1** | **2** | **3** | **6** | **9** | **18** |
|:-------:|:-----:|:-----:|:-----:|:-----:|:-----:|:------:|
|  **1**  |   1   |   2   |   3   |   6   |   9   |   18   |
|  **2**  |   2   |   2   |   6   |   6   |  18   |   18   |
|  **3**  |   3   |   6   |   3   |   6   |   9   |   18   |
|  **6**  |   6   |   6   |   6   |   6   |  18   |   18   |
|  **9**  |   9   |  18   |   9   |  18   |   9   |   18   |
| **18**  |  18   |  18   |  18   |  18   |  18   |   18   |

**Meet ($\gcd$) Table**:
| $\wedge$ | **1** | **2** | **3** | **6** | **9** | **18** |
|:---------:|:-----:|:-----:|:-----:|:-----:|:-----:|:------:|
|   **1**   |   1   |   1   |   1   |   1   |   1   |   1    |
|   **2**   |   1   |   2   |   1   |   2   |   1   |   2    |
|   **3**   |   1   |   1   |   3   |   3   |   3   |   3    |
|   **6**   |   1   |   2   |   3   |   6   |   3   |   6    |
|   **9**   |   1   |   1   |   3   |   3   |   9   |   9    |
|  **18**   |   1   |   2   |   3   |   6   |   9   |   18   |

#### Complement Evaluation for Each Element:
To find a complement $x$ of $a$, we require:
$$\gcd(a, x) = 1 \quad \text{and} \quad \operatorname{lcm}(a, x) = 18$$
* For $1$: $1' = 18$
* For $18$: $18' = 1$
* For $2$: $\gcd(2, 9) = 1$ and $\operatorname{lcm}(2, 9) = 18 \implies 2' = 9$
* For $9$: $9' = 2$
* For $3$:
  - Elements coprime to $3$ in $D_{18}$ are $\{1, 2\}$.
  - $\operatorname{lcm}(3, 1) = 3 \ne 18$
  - $\operatorname{lcm}(3, 2) = 6 \ne 18$
  - Therefore, **no complement exists for $3$**.
* For $6$:
  - Coprime elements with $6$ in $D_{18}$ is only $\{1\}$.
  - $\operatorname{lcm}(6, 1) = 6 \ne 18$.
  - Therefore, **no complement exists for $6$**.

**Conclusion**: $(D_{18}, \mid)$ is a bounded lattice, but it is **NOT a complemented lattice**.

---

## 1.6 Boolean Algebra

### Definition & Algebraic Axioms
A lattice $(B, \vee, \wedge)$ which is **both complemented and distributive** is called a **Boolean Algebra**.

Formally, a Boolean algebra is an algebraic system $(B, +, \cdot, ', 0, 1)$ where $B$ is a non-empty set, $+$ (OR / Join) and $\cdot$ (AND / Meet) are binary operations, $'$ (NOT / Complement) is a unary operation, and $0, 1$ are distinct identity elements, satisfying $\forall a, b, c \in B$:
1. **Identity Laws**:
   $$a + 0 = a, \quad a \cdot 1 = a$$
2. **Commutative Laws**:
   $$a + b = b + a, \quad a \cdot b = b \cdot a$$
3. **Associative Laws**:
   $$(a + b) + c = a + (b + c), \quad (a \cdot b) \cdot c = a \cdot (b \cdot c)$$
4. **Distributive Laws**:
   $$a \cdot (b + c) = (a \cdot b) + (a \cdot c)$$
   $$a + (b \cdot c) = (a + b) \cdot (a + c)$$
5. **Complement Laws**:
   $$a + \bar{a} = 1, \quad a \cdot \bar{a} = 0$$

---

### Boolean Space $B_n$ and Hypercube Representation
The set $B_n = \{0, 1\}^n$ is the collection of all $n$-tuples of bits:
* $B_1 = \{0, 1\}$ (Line segment, 2 vertices)
* $B_2 = \{(0,0), (0,1), (1,0), (1,1)\}$ (Square, 4 vertices)
* $B_3 = \{000, 001, 010, 011, 100, 101, 110, 111\}$ (3D Cube, 8 vertices)
* $B_n$ has $2^n$ elements and can be visualized as an $n$-dimensional hypercube ($Q_n$).

#### 3D Cube Diagram ($B_3$):
```text
           011 ----------- 111
          / |             / |
         /  |            /  |
       010 ----------- 110  |
        |   |           |   |
        |  001 ---------|- 101
        |  /            |  /
        | /             | /
       000 ----------- 100
```

---

### Boolean Functions & Representations
A **Boolean function** of $n$ variables is a mapping:
$$f: B^n \to \{0, 1\} \quad \text{or} \quad f: \{0, 1\}^n \to \{0, 1\}$$

There are several standard ways to represent a Boolean function:
1. **Truth Tables**: Enumerating output for all $2^n$ combinations of inputs.
2. **Boolean Expressions**: Formulas using $\wedge, \vee, \neg, \oplus$.
3. **Logic Circuits**: Schematic diagrams of interconnected logic gates (AND, OR, NOT, XOR, NAND, NOR).
4. **Binary Decision Diagrams (BDD)**: Directed acyclic graphs where non-terminal nodes represent variables, dashed edges represent $0$-branches (low), and solid edges represent $1$-branches (high).
5. **Karnaugh Maps (K-Maps)**: Gray-code 2D/3D grids for visual minimization.

---

## 1.7 Normal Forms: Minterms, Maxterms, PDNF, and PCNF

### Minterms vs. Maxterms
* **Minterm (Product Term)**: A conjunction of $n$ literals in which each variable appears exactly once (in complemented or uncomplemented form).
  - Evaluates to $1$ for exactly **one** combination of truth values.
  - Denoted by $m_i$, where $i$ is the decimal integer corresponding to the binary assignment.
  - Convention: Variable $x = 1 \implies x$, Variable $x = 0 \implies \sim x$.
* **Maxterm (Sum Term)**: A disjunction of $n$ literals in which each variable appears exactly once.
  - Evaluates to $0$ for exactly **one** combination of truth values.
  - Denoted by $M_i$.
  - Convention: Variable $x = 0 \implies x$, Variable $x = 1 \implies \sim x$.
  - Relationship: $M_i = \overline{m_i}$.

| Decimal | $p$ | $q$ | $r$ | Minterm ($m_i$) | Maxterm ($M_i$) |
|:-------:|:---:|:---:|:---:|:---------------:|:---------------:|
|    0    |  0  |  0  |  0  | $\sim p \wedge \sim q \wedge \sim r$ | $p \vee q \vee r$ |
|    1    |  0  |  0  |  1  | $\sim p \wedge \sim q \wedge r$ | $p \vee q \vee \sim r$ |
|    2    |  0  |  1  |  0  | $\sim p \wedge q \wedge \sim r$ | $p \vee \sim q \vee r$ |
|    3    |  0  |  1  |  1  | $\sim p \wedge q \wedge r$ | $p \vee \sim q \vee \sim r$ |
|    4    |  1  |  0  |  0  | $p \wedge \sim q \wedge \sim r$ | $\sim p \vee q \vee r$ |
|    5    |  1  |  0  |  1  | $p \wedge \sim q \wedge r$ | $\sim p \vee q \vee \sim r$ |
|    6    |  1  |  1  |  0  | $p \wedge q \wedge \sim r$ | $\sim p \vee \sim q \vee r$ |
|    7    |  1  |  1  |  1  | $p \wedge q \wedge r$ | $\sim p \vee \sim q \vee \sim r$ |

---

### Algorithm to Convert to PDNF and PCNF
1. **Construct the Truth Table** of the formula.
2. **For PDNF (Principal Disjunctive Normal Form)**:
   - Identify every row where output is **True ($1$)**.
   - Write the corresponding minterm for each such row.
   - Take the **disjunction ($\vee$)** of all these minterms.
3. **For PCNF (Principal Conjunctive Normal Form)**:
   - Identify every row where output is **False ($0$)**.
   - Write the corresponding maxterm for each such row.
   - Take the **conjunction ($\wedge$)** of all these maxterms.

---

### Problem 1: $f = p \wedge (q \vee r)$

#### Step 1: DNF and CNF
* **DNF (Disjunctive Normal Form)**: Apply distributive law:
  $$f = (p \wedge q) \vee (p \wedge r)$$
* **CNF (Conjunctive Normal Form)**: Expression is already a conjunction of sums/literals:
  $$f = p \wedge (q \vee r)$$

#### Step 2: Truth Table
| Row | $p$ | $q$ | $r$ | $q \vee r$ | $f = p \wedge (q \vee r)$ | Term Type |
|:---:|:---:|:---:|:---:|:-----------:|:---------------------------:|:---------:|
|  0  |  0  |  0  |  0  |      0      |              0              | $M_0$     |
|  1  |  0  |  0  |  1  |      1      |              0              | $M_1$     |
|  2  |  0  |  1  |  0  |      1      |              0              | $M_2$     |
|  3  |  0  |  1  |  1  |      1      |              0              | $M_3$     |
|  4  |  1  |  0  |  0  |      0      |              0              | $M_4$     |
|  5  |  1  |  0  |  1  |      1      |              1              | $m_5$     |
|  6  |  1  |  1  |  0  |      1      |              1              | $m_6$     |
|  7  |  1  |  1  |  1  |      1      |              1              | $m_7$     |

#### Step 3: Derivation of PDNF
Rows with output $1$: Rows 5, 6, 7.
$$\text{PDNF} = m_5 \vee m_6 \vee m_7$$
$$\text{PDNF} = (p \wedge \sim q \wedge r) \vee (p \wedge q \wedge \sim r) \vee (p \wedge q \wedge r)$$

*(Algebraic Verification)*:
$$(p \wedge q) = (p \wedge q) \wedge (r \vee \sim r) = (p \wedge q \wedge r) \vee (p \wedge q \wedge \sim r)$$
$$(p \wedge r) = (p \wedge r) \wedge (q \vee \sim q) = (p \wedge q \wedge r) \vee (p \wedge \sim q \wedge r)$$
Taking the union and removing duplicates:
$$\text{PDNF} = (p \wedge q \wedge r) \vee (p \wedge q \wedge \sim r) \vee (p \wedge \sim q \wedge r)$$

#### Step 4: Derivation of PCNF
Rows with output $0$: Rows 0, 1, 2, 3, 4.
$$\text{PCNF} = M_0 \wedge M_1 \wedge M_2 \wedge M_3 \wedge M_4$$
$$\text{PCNF} = (p \vee q \vee r) \wedge (p \vee q \vee \sim r) \wedge (p \vee \sim q \vee r) \wedge (p \vee \sim q \vee \sim r) \wedge (\sim p \vee q \vee r)$$

---

### Problem 2: $f = ((p \wedge q) \vee (\sim p \to r)) \to (\sim q \wedge r)$

#### Complete Truth Table Breakdown (Gap Filled):
Recall equivalence:
$$\sim p \to r \equiv \sim(\sim p) \vee r \equiv p \vee r$$
Therefore:
$$(p \wedge q) \vee (\sim p \to r) \equiv (p \wedge q) \vee (p \vee r) \equiv p \vee r$$
Let $A = (p \wedge q) \vee (\sim p \to r) \equiv p \vee r$.
Let $B = \sim q \wedge r$.
The function is $f = A \to B \equiv \sim A \vee B \equiv \sim(p \vee r) \vee (\sim q \wedge r) \equiv (\sim p \wedge \sim r) \vee (\sim q \wedge r)$.

Let us evaluate all 8 rows:

| Row | $p$ | $q$ | $r$ | $p \wedge q$ | $\sim p \to r$ | $A$ | $\sim q \wedge r$ ($B$) | $f = A \to B$ | Minterm / Maxterm |
|:---:|:---:|:---:|:---:|:-------------:|:----------------:|:---:|:------------------------:|:--------------:|:-----------------:|
|  0  |  0  |  0  |  0  |       0       |        0         |  0  |            0             |     **1**      |       $m_0$       |
|  1  |  0  |  0  |  1  |       0       |        1         |  1  |            1             |     **1**      |       $m_1$       |
|  2  |  0  |  1  |  0  |       0       |        0         |  0  |            0             |     **1**      |       $m_2$       |
|  3  |  0  |  1  |  1  |       0       |        1         |  1  |            0             |     **0**      |       $M_3$       |
|  4  |  1  |  0  |  0  |       0       |        1         |  1  |            0             |     **0**      |       $M_4$       |
|  5  |  1  |  0  |  1  |       0       |        1         |  1  |            1             |     **1**      |       $m_5$       |
|  6  |  1  |  1  |  0  |       1       |        1         |  1  |            0             |     **0**      |       $M_6$       |
|  7  |  1  |  1  |  1  |       1       |        1         |  1  |            0             |     **0**      |       $M_7$       |

#### PDNF and PCNF Results:
* **PDNF** (Rows with output 1: 0, 1, 2, 5):
  $$\text{PDNF} = (\sim p \wedge \sim q \wedge \sim r) \vee (\sim p \wedge \sim q \wedge r) \vee (\sim p \wedge q \wedge \sim r) \vee (p \wedge \sim q \wedge r)$$
* **PCNF** (Rows with output 0: 3, 4, 6, 7):
  $$\text{PCNF} = (p \vee \sim q \vee \sim r) \wedge (\sim p \vee q \vee r) \wedge (\sim p \vee \sim q \vee r) \wedge (\sim p \vee \sim q \vee \sim r)$$

#### Logic Circuit Architecture:
* Inputs: $p, q, r$.
* Invert inputs to obtain $\sim p, \sim q, \sim r$.
* Generate $A = p \vee r$ with a 2-input OR gate.
* Generate $B = \sim q \wedge r$ with a 2-input AND gate.
* Connect $A$ and $B$ to an Implication subcircuit: $\text{NOT}(A)$ feeding an OR gate alongside $B$:
  $$f = \overline{A} + B$$

---

### Problem 3: Boolean Expression Simplification
**Problem from Notes**: Simplify the following Boolean expression:
$$f = \overline{(x \wedge y)} \wedge \overline{\left( \bar{z} \wedge (z \oplus (\bar{y} \vee (x \wedge y))) \right)}$$

#### Step-by-Step Algebraic Simplification:
1. **Simplify the innermost term $\bar{y} \vee (x \wedge y)$**:
   Using the distributive law:
   $$\bar{y} \vee (x \wedge y) = (\bar{y} \vee x) \wedge (\bar{y} \vee y)$$
   Since $\bar{y} \vee y = 1$:
   $$(\bar{y} \vee x) \wedge 1 = \bar{y} \vee x$$

2. **Evaluate the XOR term $z \oplus (\bar{y} \vee x)$**:
   Let $K = \bar{y} \vee x$.
   $$z \oplus K = z \bar{K} \vee \bar{z} K$$

3. **Evaluate the conjunction with $\bar{z}$**:
   $$\bar{z} \wedge (z \oplus K) = \bar{z} \wedge (z \bar{K} \vee \bar{z} K)$$
   Distributing $\bar{z}$:
   $$= (\bar{z} \wedge z \wedge \bar{K}) \vee (\bar{z} \wedge \bar{z} \wedge K)$$
   Since $\bar{z} \wedge z = 0$ and $\bar{z} \wedge \bar{z} = \bar{z}$:
   $$= 0 \vee (\bar{z} \wedge K) = \bar{z} \wedge (\bar{y} \vee x)$$

4. **Apply complementation to the second outer term**:
   $$\overline{\bar{z} \wedge (\bar{y} \vee x)} = \bar{\bar{z}} \vee \overline{(\bar{y} \vee x)}$$
   By De Morgan's Laws:
   $$= z \vee (\bar{\bar{y}} \wedge \bar{x}) = z \vee (y \wedge \bar{x})$$

5. **Combine with the first term $\overline{x \wedge y}$**:
   $$\overline{x \wedge y} = \bar{x} \vee \bar{y}$$
   Thus, the entire expression becomes:
   $$f = (\bar{x} \vee \bar{y}) \wedge \left( z \vee (y \wedge \bar{x}) \right)$$

6. **Distribute and Finalize**:
   $$f = \left[(\bar{x} \vee \bar{y}) \wedge z\right] \vee \left[(\bar{x} \vee \bar{y}) \wedge (y \wedge \bar{x})\right]$$
   Notice that $(y \wedge \bar{x}) \le (\bar{x} \vee \bar{y})$, so by absorption:
   $$(\bar{x} \vee \bar{y}) \wedge (y \wedge \bar{x}) = y \wedge \bar{x}$$
   Therefore:
   $$f = [(\bar{x} \vee \bar{y}) \wedge z] \vee (y \wedge \bar{x})$$
   Alternatively written as:
   $$f = z(\bar{x} + \bar{y}) + \bar{x}y$$

---

# Module 4: Graph Theory

## 2.1 Historical Origin: The Königsberg Bridge Problem
In 1736, the city of Königsberg in Prussia (now Kaliningrad, Russia) featured two islands in the Pregel River connected to each other and to the two main banks by **7 bridges**:

```text
               Bank A
              /  |  \
             /   |   \
     Bridge /    |    \ Bridge
           /     |     \
          /   Bridge    \
    Island C ========= Island D
          \   Bridge    /
           \     |     /
            \    |    /
     Bridge  \   |   /  Bridge
              \  |  /
               Bank B
```
* **The Challenge**: Can a person start at any point, walk through the city crossing each of the 7 bridges **exactly once**, and return to the starting point?
* **Euler's Graph Modeling**:
  - Vertices = Landmasses ($A, B, C, D$) $\implies |V| = 4$
  - Edges = Bridges $\implies |E| = 7$
  - Degrees of vertices:
    $$d(A) = 3, \quad d(B) = 3, \quad d(C) = 5, \quad d(D) = 3$$
* **Euler's Conclusion**:
  - To traverse a vertex (arrive and leave), 2 edges are used.
  - Therefore, an **Eulerian circuit** (starts and ends at the same vertex) exists **if and only if every vertex has an even degree**.
  - An **Eulerian trail** (starts and ends at different vertices) exists **if and only if exactly 2 vertices have odd degree**.
  - Since Königsberg has **4 vertices of odd degree**, crossing each bridge once is **mathematically impossible**.

---

## 2.2 Fundamental Graph Terminology & Definitions
A graph $G$ is defined as an ordered pair $G = (V, E)$ where:
* $V = V(G)$ is a non-empty set of **vertices** (or nodes).
* $E = E(G)$ is a set of **edges**, where each edge $e \in E$ connects a pair of vertices $\{u, v\}$.
* Formally, there exists an incidence function $f: E \to V \times V$ (or to unordered pairs of $V$).

### Core Terminology:
* **Adjacent Vertices**: Two vertices $u, v$ connected by an edge ($e = \{u, v\}$).
* **Incident**: An edge $e = \{u, v\}$ is said to be incident on vertices $u$ and $v$.
* **Adjacent Edges**: Two distinct edges sharing at least one common endpoint.
* **Isolated Vertex**: A vertex with degree $0$ (no incident edges).
* **Pendant Vertex**: A vertex with degree $1$.
* **Order of $G$**: Number of vertices, denoted $|V| = n$.
* **Size of $G$**: Number of edges, denoted $|E| = m$ (or $q$).

### Order vs. Size Matrix:
| Order ($|V|$) | Size ($|E|$) | Feasibility / Graph Type |
|:-------------:|:------------:|:-------------------------|
|   **Even**    |   **Even**   | Possible (e.g., $C_4$: $|V|=4, |E|=4$) |
|   **Even**    |   **Odd**    | Possible (e.g., $P_4$: $|V|=4, |E|=3$) |
|    **Odd**    |   **Even**   | Possible (e.g., $C_5$: $|V|=5, |E|=5$ wait, 5 is odd; $K_1$: $|V|=1, |E|=0$) |
|    **Odd**    |   **Odd**    | Possible (e.g., $C_3$: $|V|=3, |E|=3$) |
|  **Finite**   |  **Finite**  | Standard finite graph |
|  **Finite**   | **Infinite** | Multigraph with infinitely many edges between finite vertices |
| **Infinite**  |  **Finite**  | Infinitely many isolated vertices with a finite set of edges |
| **Infinite**  | **Infinite** | Fully infinite graph |

### Graph Classifications:
* **Simple Graph**: Has no self-loops (edges from a vertex to itself) and no multiple / parallel edges.
* **Multigraph**: Contains multiple edges connecting the same pair of vertices, but no self-loops.
* **Pseudograph**: May contain both multiple edges and self-loops.
* **Directed Graph (Digraph)**: Edges are ordered pairs of vertices represented by arrows (arcs).

---

## 2.3 Special Graph Families

### Trivial, Null, Complete, and Star Graphs
1. **Trivial Graph**: A graph with 1 vertex and 0 edges ($K_1$).
2. **Null Graph / Empty Graph ($N_n$)**: A graph with $n$ vertices and 0 edges.
3. **Complete Graph ($K_n$)**: A simple graph in which every pair of distinct vertices is connected by an edge.
4. **Star Graph ($S_n$ / $K_{1, n-1}$)**: A tree with 1 central vertex connected to all other $n-1$ pendant vertices.

---

### Edge Formula & Number of Labelled Graphs
In a complete graph $K_n$, every pair of vertices forms an edge:
$$|E(K_n)| = \binom{n}{2} = \frac{n(n - 1)}{2}$$

| Vertices ($n$) | Edges ($|E|$) |
|:--------------:|:-------------:|
|       1        |       0       |
|       2        |       1       |
|       3        |       3       |
|       4        |       6       |
|       5        |      10       |
|      $n$       | $\frac{n(n-1)}{2}$ |

#### Total Number of Simple Labelled Graphs on $n$ Vertices:
Since there are $\binom{n}{2}$ possible edges, and each edge can either be present or absent:
$$\text{Total Labelled Graphs} = 2^{\binom{n}{2}} = 2^{\frac{n(n-1)}{2}}$$

For $n = 3$:
$$\text{Number of labelled graphs} = 2^{\binom{3}{2}} = 2^3 = 8$$

#### The 8 Labelled Graphs with $n = 3$ Vertices:
1. **0 edges** (1 graph): Null graph with vertices $\{1, 2, 3\}$.
2. **1 edge** (3 graphs): Edge $\{1, 2\}$, edge $\{2, 3\}$, or edge $\{1, 3\}$.
3. **2 edges** (3 graphs): Edges $\{\{1,2\}, \{2,3\}\}$, $\{\{1,2\}, \{1,3\}\}$, or $\{\{1,3\}, \{2,3\}\}$.
4. **3 edges** (1 graph): Complete graph $K_3$ (triangle).

*(Note: There are only **4 non-isomorphic** unlabelled graphs on 3 vertices!)*

---

### Class Exercise: Registration Number Problem
**Problem Statement from Notes**:
"Take the last 3 digits of your registration number as the number of edges ($q$). What is the minimum number of vertices ($n$) required to draw a simple graph?"

#### General Method:
In any simple graph $G = (p, q)$, the number of edges cannot exceed the maximum possible edges:
$$q \le \binom{n}{2} = \frac{n(n - 1)}{2}$$
$$n(n - 1) \ge 2q \implies n^2 - n - 2q \ge 0$$
Using the quadratic formula:
$$n \ge \frac{1 + \sqrt{1 + 8q}}{2}$$
Since $n$ must be an integer, we take:
$$n_{\min} = \left\lceil \frac{1 + \sqrt{1 + 8q}}{2} \right\rceil$$

#### Solution for the Example in Notes ($q = 242$):
$$n^2 - n - 2(242) \ge 0 \implies n^2 - n - 484 \ge 0$$
Roots of $n^2 - n - 484 = 0$:
$$n = \frac{1 \pm \sqrt{1 + 4(1)(484)}}{2} = \frac{1 + \sqrt{1937}}{2} \approx \frac{1 + 44.011}{2} = 22.505$$
Since $n$ must be a positive integer:
$$n_{\min} = 23$$
*(Verification: For $n = 22$, max edges = $\frac{22 \times 21}{2} = 231 < 242$. For $n = 23$, max edges = $\frac{23 \times 22}{2} = 253 \ge 242$. Hence, $n=23$ is exact!)*

---

## 2.4 Bipartite Graphs & Complete Bipartite Graphs

### Definition & Kőnig's Odd Cycle Theorem
A graph $G = (V, E)$ is called **bipartite** if its vertex set $V$ can be partitioned into two disjoint, non-empty subsets $X$ and $Y$ ($V = X \cup Y$ and $X \cap Y = \emptyset$) such that:
$$\forall e = \{u, v\} \in E, \quad u \in X \text{ and } v \in Y$$
No two vertices in $X$ are adjacent, and no two vertices in $Y$ are adjacent.

> **Kőnig's Theorem (1936)**:
> A graph $G$ is bipartite **if and only if** it contains **no cycles of odd length** (i.e., all cycles have even length).

---

### Complete Bipartite Graphs $K_{m, n}$
A bipartite graph with bipartition $(X, Y)$ such that every vertex of $X$ is adjacent to every vertex of $Y$:
* $|X| = m$, $|Y| = n$
* Total vertices: $|V| = m + n$
* Total edges: $|E| = m \times n$

#### Examples:
* $K_{1, 2}$: Star-like graph with $|V| = 3, |E| = 2$.
* $K_{2, 2}$: Simple 4-cycle ($C_4$) with $|V| = 4, |E| = 4$.
* $K_{2, 3}$: 5 vertices, $2 \times 3 = 6$ edges.

---

### Class Problem: Checking Bipartiteness
**Problem from Notes**: Determine whether the given 13-vertex graph is bipartite.

```text
      v2 ----------------- v4 ---------- v5
     /  \                 / \          / | \
    v1   \               /   \        /  |  \
     \    \             /     \      /   |   \
      v12--v3 -------- v10-----v13--v6   |    v7
        \  /             \     /     \   |   /
         \/               \   /       \  |  /
         v11               v9 --------- v8
```

#### Step-by-Step 2-Coloring Check (Gap Filled):
1. Pick $v_1 \in X$.
2. Neighbors of $v_1$ are $v_2, v_{12} \implies v_2, v_{12} \in Y$.
3. Check connections from $v_2$ and $v_{12}$:
   - $v_2$ connects to $v_3 \implies v_3 \in X$.
   - $v_{12}$ connects to $v_3 \implies v_3 \in X$ (consistent so far).
4. Now check triangle / 3-cycle $v_3 - v_{11} - v_{12}$:
   - $v_3 \in X$ is connected to $v_{11} \implies v_{11} \in Y$.
   - But $v_{12} \in Y$ is **also connected directly to $v_{11}$**!
   - This creates an edge between two vertices in the same partition ($v_{12}, v_{11} \in Y$).
   - The cycle $v_3 - v_{11} - v_{12} - v_3$ has length **3 (odd cycle)**!

**Conclusion**: Since it contains an odd cycle, the graph is **NOT bipartite**.

---

## 2.5 Complement of a Graph ($G^c$)

### Properties & Edge Sum Formula
Let $G = (V, E)$ be a simple graph. The **complement** of $G$, denoted $G^c$ or $\overline{G}$, has:
* Same vertex set: $V(G^c) = V(G)$.
* Edge set $E(G^c)$: Two distinct vertices are adjacent in $G^c$ **if and only if** they are not adjacent in $G$:
  $$\{u, v\} \in E(G^c) \iff \{u, v\} \notin E(G)$$

#### Fundamental Identities:
1. $(G^c)^c = G$
2. $G \cup G^c = K_n$
3. $|E(G)| + |E(G^c)| = |E(K_n)| = \binom{n}{2} = \frac{n(n - 1)}{2}$

---

### Examples ($C_4$ and 5-Vertex Graph)

#### Example 1: Complement of $C_4$ (4-Cycle)
Let $V = \{v_1, v_2, v_3, v_4\}$ with cycle edges:
$$E(G) = \{\{v_1, v_2\}, \{v_2, v_3\}, \{v_3, v_4\}, \{v_4, v_1\}\} \quad (|E| = 4)$$
* Total possible edges in $K_4$: $\binom{4}{2} = 6$.
* Missing edges: $\{v_1, v_3\}$ and $\{v_2, v_4\}$.
* Therefore:
  $$E(G^c) = \{\{v_1, v_3\}, \{v_2, v_4\}\} \quad (|E(G^c)| = 2)$$
  $G^c$ consists of two disjoint edges (crossing diagonals), which is $2 K_2$.
* Check: $|E(G)| + |E(G^c)| = 4 + 2 = 6 = \binom{4}{2}$.

#### Example 2: 5-Vertex Graph from Notes
Let $G$ have vertices $\{v_1, v_2, v_3, v_4, v_5\}$ and edges:
$$E(G) = \{\{v_1, v_2\}, \{v_2, v_3\}, \{v_3, v_4\}, \{v_4, v_5\}, \{v_5, v_1\}, \{v_1, v_4\}, \{v_2, v_4\}\}$$
* Total edges $|E(G)| = 7$.
* Total possible edges in $K_5$: $\binom{5}{2} = 10$.
* Size of complement:
  $$|E(G^c)| = 10 - 7 = 3$$
* The complement edges are:
  $$E(G^c) = \{\{v_1, v_3\}, \{v_2, v_5\}, \{v_3, v_5\}\}$$

---

## 2.6 Neighborhoods, Degrees, and Regular Graphs

### Open & Closed Neighborhoods
* **Open Neighborhood $N(v)$**: Set of all vertices adjacent to $v$:
  $$N(v) = \{u \in V \mid \{u, v\} \in E\}$$
* **Closed Neighborhood $N[v]$**: Open neighborhood including the vertex itself:
  $$N[v] = N(v) \cup \{v\}$$

### Degrees and Regular Graphs
* **Degree of a vertex $v$ ($d(v)$ or $\deg(v)$)**: Number of edges incident with $v$. For simple graphs, $d(v) = |N(v)|$.
* **Minimum Degree**: $\delta(G) = \min_{v \in V} d(v)$.
* **Maximum Degree**: $\Delta(G) = \max_{v \in V} d(v)$.
* **Bounds for Simple Graphs**:
  $$0 \le \delta(G) \le d(v) \le \Delta(G) \le n - 1$$
* **$r$-Regular Graph**: A graph where every vertex has the exact same degree $r$:
  $$\delta(G) = \Delta(G) = r$$
  - If $r = 0$: Null graph $N_n$.
  - If $r = 2$: Disjoint collection of cycles.
  - If $r = n - 1$: Complete graph $K_n$.

#### Example from Notes:
Given the 5-vertex graph:
* $N(v_1) = \{v_2, v_4, v_5\} \implies d(v_1) = 3$
* $N[v_1] = \{v_1, v_2, v_4, v_5\}$
* $N(v_2) = \{v_1, v_3, v_4\} \implies d(v_2) = 3$
* $N(v_3) = \{v_2, v_4\} \implies d(v_3) = 2$
* $N(v_4) = \{v_1, v_2, v_3, v_5\} \implies d(v_4) = 4$
* $N(v_5) = \{v_1, v_4\} \implies d(v_5) = 2$
* Minimum degree: $\delta(G) = 2$
* Maximum degree: $\Delta(G) = 4$
* Total degree sum: $3 + 3 + 2 + 4 + 2 = 14 = 2(7) = 2|E|$.

---

## 2.7 Degree Sequences & Graphic Sequences

A **degree sequence** of a simple graph is the list of degrees of its vertices, conventionally sorted in non-increasing order:
$$d_1 \ge d_2 \ge d_3 \ge \dots \ge d_n$$

### Havel-Hakimi Theorem:
A sequence $S = (d_1, d_2, \dots, d_n)$ with $d_1 \ge d_2 \ge \dots \ge d_n$ is graphic (can form a simple graph) **if and only if** the reduced sequence:
$$S' = (d_2 - 1, d_3 - 1, \dots, d_{d_1 + 1} - 1, d_{d_1 + 2}, \dots, d_n)$$
(sorted in non-increasing order) is also graphic.

### Necessary Initial Conditions:
1. **Sum of degrees must be even**: $\sum d_i = 2|E|$.
2. **Maximum degree constraint**: $d_1 \le n - 1$.
3. **No negative degrees allowed**.

---

### Detailed Analysis of All 12 Class Test Sequences

1. **$(5, 4, 3, 2, 1, 1)$**:
   - $n = 6$. Max degree $d_1 = 5 = n - 1$.
   - Sum $= 5 + 4 + 3 + 2 + 1 + 1 = 16$ (Even).
   - Apply Havel-Hakimi: remove 5, subtract 1 from next 5 elements:
     $$(4 - 1, 3 - 1, 2 - 1, 1 - 1, 1 - 1) = (3, 2, 1, 0, 0)$$
   - Remove 3, subtract 1 from next 3:
     $$(2 - 1, 1 - 1, 0 - 1, 0) = (1, 0, -1, 0) \implies \text{Negative number!}$$
   - **Conclusion**: **NOT graphic ($\times$)**.

2. **$(5, 4, 3, 2, 1)$**:
   - $n = 5$. Max degree is $5$.
   - But in a simple graph with 5 vertices, $\Delta(G) \le 5 - 1 = 4$. A vertex cannot connect to 5 others without multiple edges or loops.
   - **Conclusion**: **NOT graphic ($\times$)**.

3. **$(5, 5, 4, 3, 2, 1)$**:
   - $n = 6$. Sum $= 20$ (Even).
   - Remove first 5: subtract 1 from $(5, 4, 3, 2, 1) \to (4, 3, 2, 1, 0)$.
   - Remove 4: subtract 1 from $(3, 2, 1, 0) \to (2, 1, 0, -1) \implies$ Negative!
   - **Conclusion**: **NOT graphic ($\times$)**.

4. **$(2, 2, 2, 2, 2)$**:
   - $n = 5$. Sum $= 10$ (Even).
   - Forms a simple 5-cycle ($C_5$).
   - **Conclusion**: **Graphic ($\checkmark$)**.

5. **$(3, 3, 2, 2, 2, 2)$**:
   - $n = 6$. Sum $= 14$ (Even). Number of odd-degree vertices $= 2$ (Even).
   - Apply Havel-Hakimi: remove 3 $\to (2, 1, 1, 2, 2) \to$ sort: $(2, 2, 2, 1, 1)$.
   - Remove 2 $\to (1, 1, 1, 1)$.
   - Remove 1 $\to (0, 1, 1) \to (1, 1, 0)$.
   - Remove 1 $\to (0, 0)$. All zeros $\implies$ Graphic!
   - **Conclusion**: **Graphic ($\checkmark$)**.

6. **$(3, 3, 3, 3, 3, 3)$**:
   - $n = 6$. Sum $= 18$ (Even).
   - 3-regular graph on 6 vertices (e.g., complete bipartite $K_{3,3}$ or prism $Y_3$).
   - **Conclusion**: **Graphic ($\checkmark$)**.

7. **$(3, 3, 3, 3, 3)$**:
   - $n = 5$. Sum $= 15$ (**Odd!**).
   - Number of odd degree vertices is 5 (Odd). Violates Handshaking lemma.
   - **Conclusion**: **NOT graphic ($\times$)**.

8. **$(4, 4, 3, 3, 2, 2)$**:
   - $n = 6$. Sum $= 18$ (Even). Odd vertices: 2 (Even).
   - Remove 4 $\to (3, 2, 2, 1, 2) \to$ sort: $(3, 2, 2, 2, 1)$.
   - Remove 3 $\to (1, 1, 1, 1)$.
   - Valid (forms $2 K_2$).
   - **Conclusion**: **Graphic ($\checkmark$)**.

9. **$(4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 0)$**:
   - $n = 11$. Sum $= 20$ (Even). Odd vertices: 6 (Even).
   - Remove 0 at end $\implies (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)$.
   - Remove 4 $\to (2, 2, 1, 1, 2, 1, 1, 1, 1) \to$ sort: $(2, 2, 2, 1, 1, 1, 1, 1, 1)$.
   - Stepwise reductions yield only non-negative numbers.
   - **Conclusion**: **Graphic ($\checkmark$)**.

10. **$(4, 4, 4, 4, 3, 3, 3, 2, 2, 1)$**:
    - $n = 10$. Sum $= 30$ (Even). Number of odd vertices: 4 (Even).
    - Can be shown graphic by consecutive Havel-Hakimi reductions.
    - **Conclusion**: **Graphic ($\checkmark$)**.

---

## 2.8 Euler's Handshaking Lemma & Applications

### Lemma 1 & Detailed Proof
> **Euler's Handshaking Lemma (First Theorem of Graph Theory)**:
> In any graph $G = (V, E)$, the sum of the degrees of all vertices is equal to twice the total number of edges:
> $$\sum_{v \in V} d(v) = 2 |E|$$

**Proof**:
* Let $e = \{u, v\} \in E$ be an arbitrary edge in $G$.
* Edge $e$ has exactly two endpoints, $u$ and $v$.
* When counting the degrees of all vertices, edge $e$ is counted:
  - Exactly once in the degree of $u$ ($d(u)$).
  - Exactly once in the degree of $v$ ($d(v)$).
* Thus, each edge contributes exactly $2$ to the overall degree sum.
* Summing over all $|E|$ edges:
  $$\sum_{v \in V} d(v) = 2 |E| \quad \blacksquare$$

---

### Lemma 2: Even Number of Odd-Degree Vertices
> **Corollary / Lemma 2**:
> In every graph, the number of vertices having an odd degree is **always even**.

**Proof**:
1. Partition the vertex set $V$ into two disjoint sets:
   - $A$: set of vertices with **even** degree.
   - $B$: set of vertices with **odd** degree.
   $$V = A \cup B, \quad A \cap B = \emptyset$$
2. Decompose the degree sum:
   $$\sum_{v \in V} d(v) = \sum_{v \in A} d(v) + \sum_{v \in B} d(v) = 2|E|$$
3. Rearrange for the sum over odd-degree vertices:
   $$\sum_{v \in B} d(v) = 2|E| - \sum_{v \in A} d(v)$$
4. Notice that:
   - $2|E|$ is an even integer.
   - Each term $d(v)$ for $v \in A$ is even, so the sum $\sum_{v \in A} d(v)$ is even.
   - Difference of two even numbers is **even**:
     $$\sum_{v \in B} d(v) = \text{even} - \text{even} = \text{even}$$
5. Every single term in $\sum_{v \in B} d(v)$ is an **odd integer**.
6. The sum of $|B|$ odd numbers can be even **if and only if** $|B|$ (the number of terms) is **even**.
7. Therefore, $|B|$ is even. $\blacksquare$

---

### Application 1: Friends in a Group / Pigeonhole Principle
> **Theorem**: In any group of $n$ people ($n \ge 2$), there are always at least two people who have the same number of friends within the group.

**Proof via Graph Theory**:
1. Represent the group as a simple graph $G = (V, E)$, where:
   - Vertices = People ($|V| = n \ge 2$).
   - Edges = Mutual friendship.
   - Degree $d(v)$ = Number of friends person $v$ has.
2. In a simple graph with $n$ vertices, the degree of any vertex satisfies:
   $$0 \le d(v) \le n - 1$$
3. Notice that:
   - If there is a vertex with degree $0$ (a person with no friends), then no vertex can have degree $n - 1$ (someone who is friends with everyone else).
   - Conversely, if there is a vertex with degree $n - 1$, there cannot be any vertex with degree $0$.
4. Hence, degrees $0$ and $n - 1$ **cannot coexist** in the same graph.
5. Therefore, the actual degrees of the $n$ vertices must all belong to one of two restricted sets of size $n - 1$:
   - **Case 1**: $\{1, 2, 3, \dots, n - 1\}$ ($n - 1$ possible values).
   - **Case 2**: $\{0, 1, 2, \dots, n - 2\}$ ($n - 1$ possible values).
6. By the **Pigeonhole Principle**:
   - We have $n$ vertices (pigeons).
   - We have at most $n - 1$ available degree values (pigeonholes).
   - Therefore, at least two vertices must have the same degree. $\blacksquare$

---

## 2.9 Subgraphs, Spanning Subgraphs, and Induced Subgraphs

Let $G = (V, E)$ be a graph.
1. **Subgraph**: A graph $H = (V_1, E_1)$ is a subgraph of $G$ if:
   $$V_1 \subseteq V \quad \text{and} \quad E_1 \subseteq E$$
   (with the condition that endpoints of every edge in $E_1$ lie in $V_1$).
2. **Supergraph**: If $H$ is a subgraph of $G$, then $G$ is called a supergraph of $H$.
3. **Spanning Subgraph**: A subgraph $H$ that contains **all** vertices of $G$:
   $$V(H) = V(G)$$
4. **Induced Subgraph $\langle S \rangle$ / $G[S]$**: For any non-empty subset $S \subseteq V$, the subgraph induced by $S$ has vertex set $S$ and contains **all edges of $G$** that have both endpoints in $S$:
   $$E(G[S]) = \{\{u, v\} \in E(G) \mid u \in S \text{ and } v \in S\}$$

---

## 2.10 Graph Isomorphism

### Formal Definition & Graph Invariants
Two graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ are **isomorphic** (written $G_1 \cong G_2$) if there exists a **bijective function** (one-to-one and onto):
$$f: V_1 \to V_2$$
such that for any $u, v \in V_1$:
$$\{u, v\} \in E_1 \iff \{f(u), f(v)\} \in E_2$$
The mapping $f$ is called an **isomorphism**.

#### Necessary Conditions (Graph Invariants):
If $G_1 \cong G_2$, the following invariants must match:
1. $|V_1| = |V_2|$ (Same number of vertices).
2. $|E_1| = |E_2|$ (Same number of edges).
3. Same degree sequence (same sorted list of degrees).
4. Same number of cycles of each length $k$ (e.g., triangles, 4-cycles).

---

### Class Problem 1: 4-Cycle Isomorphism Mapping
Consider the two 4-vertex graphs from the notes:
* $G_1$ with vertices $V_1 = \{a, b, c, d\}$ and edges:
  $$E_1 = \{\{a, b\}, \{b, d\}, \{d, c\}, \{c, a\}\}$$
* $G_2$ with vertices $V_2 = \{1, 2, 3, 4\}$ and edges:
  $$E_2 = \{\{1, 3\}, \{3, 4\}, \{4, 2\}, \{2, 1\}\}$$

```text
    G1:                        G2:
      a -------- b               1 -------- 3
      |          |               |          |
      |          |               |          |
      c -------- d               2 -------- 4
```

#### Constructing the Isomorphism Bijection:
Define $f: V_1 \to V_2$ as:
$$f(a) = 1, \quad f(b) = 3, \quad f(c) = 2, \quad f(d) = 4$$
*(Or as in notes: $f(a)=1, f(b)=3, f(c)=4, f(d)=2$ depending on vertex labelling)*

#### Preserving Adjacency:
* $\{a, b\} \in E_1 \implies \{f(a), f(b)\} = \{1, 3\} \in E_2$ (Preserved)
* $\{b, d\} \in E_1 \implies \{f(b), f(d)\} = \{3, 4\} \in E_2$ (Preserved)
* $\{d, c\} \in E_1 \implies \{f(d), f(c)\} = \{4, 2\} \in E_2$ (Preserved)
* $\{c, a\} \in E_1 \implies \{f(c), f(a)\} = \{2, 1\} \in E_2$ (Preserved)

Since $f$ is bijective and preserves all adjacencies and non-adjacencies, $G_1 \cong G_2$.

---

### Class Problem 2: 6-Vertex Prism/Wheel Graph Analysis
**Problem from Notes**: Determine if the two 6-vertex graphs $G_1$ and $G_2$ are isomorphic:

```text
       Graph G1:                     Graph G2:
           a                             1
         / | \                         / | \
        f  |  b                       6  |  2
        |  |  |                       |  |  |
        |  |  |                       |  |  |
        e  |  c                       5  |  3
         \ | /                         \ | /
           d                             4
```
* **In Graph $G_1$**:
  - Outer cycle: $a - b - c - d - e - f - a$.
  - Internal chords: connects $a$ to $d$, $b$ to $e$, $c$ to $f$ (all 3 main diagonals).
  - Every vertex has degree 3: 3-regular graph with 9 edges ($K_{3,3}$ configuration).
* **In Graph $G_2$**:
  - Vertices $\{1, 2, 3, 4, 5, 6\}$.
  - Edges form a triangular prism: triangles $(1, 2, 6)$ and $(4, 3, 5)$, with edges $(1, 4), (2, 3), (6, 5)$.
  - Check degree sequence: All vertices have degree 3 (3-regular, 9 edges).
* **Check Cycle Invariants (Gap Filled)**:
  - In $G_2$: Contains two triangles of length 3 ($\{1, 2, 6\}$ and $\{4, 3, 5\}$).
  - In $G_1$: Let us check if there are any triangles:
    $a$ is connected to $b, f, d$. Are any of $\{b, f, d\}$ adjacent?
    $b$ is connected to $a, c, e$. None of $f, d$ is connected to $b$.
    $f$ is connected to $a, e, c$.
    $d$ is connected to $a, c, e$.
    $G_1$ is bipartite ($K_{3,3}$ with partitions $\{a, c, e\}$ and $\{b, d, f\}$)!
    Therefore, $G_1$ has **NO triangles (no 3-cycles)** at all!
  - Since $G_2$ has triangles but $G_1$ has no triangles, their cycle invariants differ.

**Final Conclusion**: $G_1 \not\cong G_2$ (**Not isomorphic**).

---
*End of Module 3 & 4 Comprehensive Notes.*
