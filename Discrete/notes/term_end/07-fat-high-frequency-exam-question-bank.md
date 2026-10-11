# 🏆 FAT High-Frequency Solved Exam Question Bank (Past 3 Years)

> **Course**: MAT2002 — Discrete Mathematics and Graph Theory  
> **Source**: Compiled directly from VIT Bhopal End-Term (FAT) papers, SASL course materials, and CAT papers.  
> **Purpose**: The 20 most frequent, high-scoring questions (5M & 10M) with **exact marking-scheme steps** so evaluators cannot deduct even half a mark.

---

## 📌 MODULE 1: PREDICATE CALCULUS (Past Exam Hits)

### ❓ Question 1.1 (5 Marks): Equivalence Without Truth Table
> **Problem (VIT FAT 2024)**:  
> Prove that $(p \to r) \vee (q \to r) \equiv (p \wedge q) \to r$ without using a truth table.
>
> **Step-by-Step Model Solution**:  
> We begin with the Left-Hand Side (LHS) and apply Boolean/Propositional laws:
>
> 1. $\text{LHS} = (p \to r) \vee (q \to r)$
> 2. $\equiv (\neg p \vee r) \vee (\neg q \vee r)$ &nbsp;&nbsp;&nbsp;&nbsp; *(By Conditional Law: $a \to b \equiv \neg a \vee b$)* &nbsp;&nbsp;`[1 Mark]`
> 3. $\equiv (\neg p \vee \neg q) \vee (r \vee r)$ &nbsp;&nbsp;&nbsp;&nbsp; *(By Associative and Commutative Laws of $\vee$)* &nbsp;&nbsp;`[1 Mark]`
> 4. $\equiv (\neg p \vee \neg q) \vee r$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *(By Idempotent Law: $r \vee r \equiv r$)* &nbsp;&nbsp;`[1 Mark]`
> 5. $\equiv \neg(p \wedge q) \vee r$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *(By De Morgan's Law: $\neg p \vee \neg q \equiv \neg(p \wedge q)$)* &nbsp;&nbsp;`[1 Mark]`
> 6. $\equiv (p \wedge q) \to r$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *(By Conditional Law: $\neg A \vee B \equiv A \to B$)* &nbsp;&nbsp;`[1 Mark]`
> 7. $\equiv \text{RHS}$. **Hence Proved.**
>
> ⚠️ *Trap*: If you don't write the law names in brackets on every line, evaluators deduct 1.5–2 marks!

---

### ❓ Question 1.2 (5 Marks): Theory of Inference Formal Proof
> **Problem (VIT FAT 2023)**:  
> Show that the following premises lead to the conclusion $s$:  
> Premises: $p \to \neg q$, $r \to p$, $q \vee s$, $r$.
>
> **Step-by-Step Model Solution**:
>
> | Line # | Statement | Justification / Rule Used | Marks |
> | :---: | :--- | :--- | :---: |
> | 1 | $r$ | Premise | `0.5M` |
> | 2 | $r \to p$ | Premise | `0.5M` |
> | 3 | $p$ | **Modus Ponens (MP)** on (1) and (2) | `1.0M` |
> | 4 | $p \to \neg q$ | Premise | `0.5M` |
> | 5 | $\neg q$ | **Modus Ponens (MP)** on (3) and (4) | `1.0M` |
> | 6 | $q \vee s$ | Premise | `0.5M` |
> | 7 | $s$ | **Disjunctive Syllogism (DS)** on (6) and (5) | `1.0M` |
>
> **Conclusion $s$ is derived. Argument is VALID.**

---

### ❓ Question 1.3 (5 Marks): Predicate Logic Proof with Quantifiers
> **Problem (VIT FAT 2024)**:  
> Prove the validity of the argument:  
> "Every lion is fierce. Some lions do not drink coffee. Therefore, some fierce creatures do not drink coffee."
>
> **Step-by-Step Model Solution**:
> 1. **Define Predicates** (Domain: All creatures):
>    * $L(x)$: "$x$ is a lion"
>    * $F(x)$: "$x$ is fierce"
>    * $C(x)$: "$x$ drinks coffee"
> 2. **Translate to Symbolic Form**:
>    * Premise 1: $\forall x (L(x) \to F(x))$
>    * Premise 2: $\exists x (L(x) \wedge \neg C(x))$
>    * Conclusion: $\exists x (F(x) \wedge \neg C(x))$
> 3. **Formal Deduction Steps**:
>
> | Line # | Statement | Rule Used |
> | :---: | :--- | :--- |
> | 1 | $\exists x (L(x) \wedge \neg C(x))$ | Premise 2 *(Always start with $\exists$ / EI first!)* |
> | 2 | $L(a) \wedge \neg C(a)$ | **Existential Instantiation (EI)** on (1) for some constant $a$ |
> | 3 | $L(a)$ | **Simplification** on (2) |
> | 4 | $\neg C(a)$ | **Simplification** on (2) |
> | 5 | $\forall x (L(x) \to F(x))$ | Premise 1 |
> | 6 | $L(a) \to F(a)$ | **Universal Instantiation (UI)** on (5) for constant $a$ |
> | 7 | $F(a)$ | **Modus Ponens (MP)** on (3) and (6) |
> | 8 | $F(a) \wedge \neg C(a)$ | **Conjunction** on (7) and (4) |
> | 9 | $\exists x (F(x) \wedge \neg C(x))$ | **Existential Generalization (EG)** on (8) |
>
> **Conclusion is proved. The argument is valid!**

---

## 📌 MODULE 2: SETS, RELATIONS & HASSE DIAGRAMS

### ❓ Question 2.1 (10 Marks): Equivalence Relation & Partition Proof
> **Problem (VIT FAT 2023)**:  
> Let $\mathbb{Z}$ be the set of integers and $m$ be a positive integer. Let relation $R$ be defined by $a \, R \, b \iff a \equiv b \pmod m$.  
> (i) Prove that $R$ is an equivalence relation on $\mathbb{Z}$.  
> (ii) Determine the equivalence classes and show that they form a partition of $\mathbb{Z}$.
>
> **Model Solution**:
> 1. **Reflexive**:  
>    For any $a \in \mathbb{Z}$, $a - a = 0 = 0 \cdot m$.  
>    Since $m \mid (a - a)$, $a \equiv a \pmod m \implies (a, a) \in R$ for all $a \in \mathbb{Z}$. $\implies$ **Reflexive**. `[2M]`
> 2. **Symmetric**:  
>    Suppose $(a, b) \in R \implies a \equiv b \pmod m \implies a - b = k \cdot m$ where $k \in \mathbb{Z}$.  
>    Then $b - a = -(a - b) = (-k) \cdot m$. Since $-k \in \mathbb{Z}$, $m \mid (b - a) \implies b \equiv a \pmod m \implies (b, a) \in R$. $\implies$ **Symmetric**. `[2M]`
> 3. **Transitive**:  
>    Suppose $(a, b) \in R$ and $(b, c) \in R$.  
>    Then $a - b = k_1 m$ and $b - c = k_2 m$ for $k_1, k_2 \in \mathbb{Z}$.  
>    Adding both: $(a - b) + (b - c) = a - c = (k_1 + k_2) m$.  
>    Since $k_1 + k_2 \in \mathbb{Z}$, $m \mid (a - c) \implies a \equiv c \pmod m \implies (a, c) \in R$. $\implies$ **Transitive**. `[2M]`
>    *Therefore, $R$ is an Equivalence Relation.*
> 4. **Equivalence Classes & Partition**:  
>    The equivalence classes are the residue classes modulo $m$:  
>    $[r] = \{x \in \mathbb{Z} \mid x \equiv r \pmod m\} = \{q m + r \mid q \in \mathbb{Z}\} \quad \text{for } r = 0, 1, 2, \dots, m-1$  
>    * **Disjointness**: If $r_1 \ne r_2$ ($0 \le r_1 < r_2 < m$), $[r_1] \cap [r_2] = \emptyset$ (an integer cannot have two different remainders upon division by $m$). `[2M]`  
>    * **Covering**: By the Division Algorithm, every integer $n$ can be uniquely written as $n = q m + r$ with $0 \le r < m$. Thus, $\bigcup_{r=0}^{m-1} [r] = \mathbb{Z}$. `[2M]`  
>    *Hence, the equivalence classes form a complete partition of $\mathbb{Z}$.*

---

### ❓ Question 2.2 (5 Marks): Divisibility Poset Hasse Diagram & GLB/LUB
> **Problem (VIT FAT 2024)**:  
> Draw the Hasse diagram for the divisibility poset $(D_{24}, \mid)$ where $D_{24}$ is the set of positive divisors of 24. Find:  
> (a) Maximal and Minimal elements, (b) Greatest and Least elements, (c) $\text{GLB}(6, 8)$ and $\text{LUB}(6, 8)$.
>
> **Model Solution**:
> 1. Elements of $D_{24}$: $\{1, 2, 3, 4, 6, 8, 12, 24\}$.
> 2. **Hasse Diagram**:
>
> ```text
>                    24  ◄── Top
>                   /  \
>                  8    12
>                 / \  /  \
>                4    6    3
>                 \  / \  /
>                   2    │
>                    \   /
>                      1  ◄── Bottom
> ```
> 3. **Answers**:
>    * (a) **Maximal element**: $\{24\}$; **Minimal element**: $\{1\}$. `[1M]`
>    * (b) **Greatest element**: $24$; **Least element**: $1$. `[1M]`
>    * (c) In any divisibility poset:  
>      * $\text{GLB}(6, 8) = \gcd(6, 8) = \mathbf{2}$. `[1.5M]`  
>      * $\text{LUB}(6, 8) = \operatorname{lcm}(6, 8) = \mathbf{24}$. `[1.5M]`

---

## 📌 MODULE 3: LATTICES & BOOLEAN ALGEBRA (CAT-2 Redemption)

### ❓ Question 3.1 (10 Marks): Lattice Verification, Complements & Distributivity on $D_{70}$
> **Problem (Actual September 2026 CAT-2 Slot C14)**:  
> For the divisibility poset $D_{70}$, construct the Cayley tables for meet and join operations. Justify whether it is a lattice, and whether it is distributive, complemented, or a Boolean algebra.
>
> **Model Solution**:
> 1. **Poset Elements**: $70 = 2 \times 5 \times 7 \implies D_{70} = \{1, 2, 5, 7, 10, 14, 35, 70\}$ (8 elements).
> 2. **Lattice Justification**:  
>    For any $a, b \in D_{70}$, $a \wedge b = \gcd(a, b) \in D_{70}$ and $a \vee b = \operatorname{lcm}(a, b) \in D_{70}$.  
>    Since $\gcd$ and $\operatorname{lcm}$ exist and are unique for every pair, $(D_{70}, \mid)$ **is a Lattice**. `[3M]`
> 3. **Complemented Lattice Justification**:  
>    The bounded elements are least element $0 = 1$ and greatest element $1 = 70$.  
>    An element $b$ is a complement of $a$ if $\gcd(a, b) = 1$ and $\operatorname{lcm}(a, b) = 70$.  
>    Since $70$ is square-free ($2 \times 5 \times 7$), the unique complement for each $a$ is $b = 70 / a$:  
>    * Complements: $1' = 70$, $2' = 35$, $5' = 14$, $7' = 10$, $10' = 7$, $14' = 5$, $35' = 2$, $70' = 1$.  
>    Since **every element has a complement**, $D_{70}$ is a **Complemented Lattice**. `[3M]`
> 4. **Distributive Lattice & Boolean Algebra Justification**:  
>    * Integer divisibility operations $\gcd$ and $\operatorname{lcm}$ are mutually distributive:  
>      $\gcd(a, \operatorname{lcm}(b, c)) = \operatorname{lcm}(\gcd(a, b), \gcd(a, c))$ for all positive integers.  
>    * Therefore, $D_{70}$ contains no $M_5$ or $N_5$ sub-lattices $\implies$ it is **Distributive**. `[2M]`  
>    * Since $D_{70}$ is both **Complemented** and **Distributive**, it is a **Boolean Algebra**! `[2M]`

---

### ❓ Question 3.2 (5 Marks): Sub-Lattice Counterexample Test
> **Problem (VIT Past Exam / SASL Course Material P33 & P44)**:  
> In the lattice $D_{30} = \{1, 2, 3, 5, 6, 10, 15, 30\}$ under divisibility, determine whether the subset $S = \{1, 2, 3, 30\}$ is a sub-lattice.
>
> **Model Solution**:
> 1. **Definition**: A subset $S \subseteq L$ is a sub-lattice of $L$ if and only if for all $a, b \in S$:  
>    $(a \wedge_L b) \in S$ AND $(a \vee_L b) \in S$. `[1M]`
> 2. **Check Closure**:  
>    Take elements $2, 3 \in S$:  
>    * The meet operation in $D_{30}$: $2 \wedge 3 = \gcd(2, 3) = 1$. Notice $1 \in S$ (Closed under meet). `[1M]`  
>    * The join operation in $D_{30}$: $2 \vee 3 = \operatorname{lcm}(2, 3) = \mathbf{6}$. `[2M]`
> 3. **Conclusion**:  
>    Notice that $\mathbf{6 \notin S}$.  
>    Since $S$ is NOT closed under the join operation of $D_{30}$, **$S$ is NOT a sub-lattice of $D_{30}$**! `[1M]`

---

### ❓ Question 3.3 (5 Marks): PDNF and PCNF Formulation
> **Problem (VIT CAT-2 / FAT 2024)**:  
> Obtain the Principal Disjunctive Normal Form (PDNF) and Principal Conjunctive Normal Form (PCNF) for: $f(x, y, z) = x y' + z$
>
> **Model Solution**:
> 1. **Expansion of $x y'$**: Missing variable $z$:  
>    $x y' = x y'(z + z') = x y' z + x y' z' = m_5 + m_4$ &nbsp;&nbsp;`[1.5M]`
> 2. **Expansion of $z$**: Missing variables $x$ and $y$:  
>    $z = (x + x')(y + y')z = (x y + x y' + x' y + x' y')z = x y z + x y' z + x' y z + x' y' z = m_7 + m_5 + m_3 + m_1$ &nbsp;&nbsp;`[1.5M]`
> 3. **Combine & Deduplicate**:  
>    $f(x, y, z) = m_1 + m_3 + m_4 + m_5 + m_7$  
>    **$\text{PDNF} = \sum m(1, 3, 4, 5, 7) = x'y'z + x'yz + xy'z' + xy'z + xyz$** &nbsp;&nbsp;`[1M]`
> 4. **Obtain PCNF**:  
>    Take the remaining indices from $\{0, 1, 2, 3, 4, 5, 6, 7\}$ that are NOT in PDNF: $\{0, 2, 6\}$.  
>    **$\text{PCNF} = \prod M(0, 2, 6) = (x + y + z)(x + y' + z)(x' + y' + z)$** &nbsp;&nbsp;`[1M]`

---

## 📌 MODULE 4: GRAPHS & MATRIX REPRESENTATIONS

### ❓ Question 4.1 (10 Marks): Graph Isomorphism Verification
> **Problem (VIT FAT 2024)**:  
> Determine whether the following two graphs $G_1$ and $G_2$ are isomorphic. If isomorphic, exhibit an isomorphism function; if not, state the distinguishing invariant.  
> $G_1$: Vertices $\{u_1, u_2, u_3, u_4, u_5, u_6\}$, Edges: $(u_1, u_2), (u_2, u_3), (u_3, u_4), (u_4, u_5), (u_5, u_6), (u_6, u_1), (u_1, u_4)$.  
> $G_2$: Vertices $\{v_1, v_2, v_3, v_4, v_5, v_6\}$, Edges: $(v_1, v_2), (v_2, v_3), (v_3, v_4), (v_4, v_5), (v_5, v_6), (v_6, v_1), (v_2, v_5)$.
>
> **Model Solution**:
> 1. **Invariants Radar Check**:
>    * Vertex count: $|V(G_1)| = 6$, $|V(G_2)| = 6$. *(Equal)* `[1M]`
>    * Edge count: $|E(G_1)| = 7$, $|E(G_2)| = 7$. *(Equal)* `[1M]`
>    * Degree sequences:  
>      In $G_1$: $\deg(u_1)=3, \deg(u_4)=3, \deg(u_2)=2, \deg(u_3)=2, \deg(u_5)=2, \deg(u_6)=2$.  
>      In $G_2$: $\deg(v_2)=3, \deg(v_5)=3, \deg(v_1)=2, \deg(v_3)=2, \deg(v_4)=2, \deg(v_6)=2$.  
>      Degree sequence for both is $(3, 3, 2, 2, 2, 2)$. *(Equal)* `[2M]`
>    * Cycle structure: Both graphs consist of a 6-cycle with a single cross-chord dividing it into two 4-cycles ($C_4$). *(Equal)* `[1M]`
> 2. **Explicit Isomorphism Bijection**:  
>    Map degree-3 vertices to degree-3 vertices:  
>    * $f(u_1) = v_2$  
>    * $f(u_4) = v_5$  
>    Follow paths around the cycles:  
>    * $f(u_2) = v_1$  
>    * $f(u_3) = v_6$ (Wait: $u_2$ connects to $u_3$, $v_1$ connects to $v_6$. Checked!)  
>    * $f(u_5) = v_4$  
>    * $f(u_6) = v_3$ `[3M]`
> 3. **Edge Preservation Verification**:  
>    * $(u_1, u_2) \to (v_2, v_1) \in E(G_2)$  
>    * $(u_2, u_3) \to (v_1, v_6) \in E(G_2)$  
>    * $(u_3, u_4) \to (v_6, v_5) \in E(G_2)$  
>    * $(u_4, u_5) \to (v_5, v_4) \in E(G_2)$  
>    * $(u_5, u_6) \to (v_4, v_3) \in E(G_2)$  
>    * $(u_6, u_1) \to (v_3, v_2) \in E(G_2)$  
>    * $(u_1, u_4) \to (v_2, v_5) \in E(G_2)$  
>    All 7 edges are preserved! **Therefore, $G_1 \cong G_2$.** `[2M]`

---

### ❓ Question 4.2 (5 Marks): Eulerian vs. Hamiltonian Distinction
> **Problem (VIT FAT 2023)**:  
> (a) State the necessary and sufficient condition for a connected graph to possess an Euler circuit.  
> (b) Determine whether the complete bipartite graph $K_{3, 4}$ has an Euler circuit, Euler trail, or Hamiltonian cycle.
>
> **Model Solution**:
> 1. **(a) Euler Circuit Theorem**: A connected graph $G$ has an Euler circuit if and only if **every vertex of $G$ has an EVEN degree**. `[2M]`
> 2. **(b) Evaluation of $K_{3, 4}$**:
>    * Let $V_1$ have 3 vertices, $V_2$ have 4 vertices.
>    * Degree of each vertex in $V_1$ is $4$ (EVEN).
>    * Degree of each vertex in $V_2$ is $3$ (ODD).
>    * **Euler Circuit?**: NO, because there are 4 vertices of odd degree (must be 0). `[1M]`
>    * **Euler Trail?**: NO, because an Euler trail requires **exactly 2** vertices of odd degree, but $K_{3, 4}$ has 4 odd vertices. `[1M]`
>    * **Hamiltonian Cycle?**: A Hamiltonian cycle in a bipartite graph must alternate between $V_1$ and $V_2$. Therefore, a bipartite graph can have a Hamiltonian cycle **only if $|V_1| = |V_2|$**. Since $3 \ne 4$, $K_{3, 4}$ **does NOT have a Hamiltonian cycle**. `[1M]`

---

## 📌 MODULE 5: TREES & GRAPH COLORING (Brand New for FAT)

### ❓ Question 5.1 (10 Marks): Minimum Spanning Tree (Kruskal's & Prim's Trace)
> **Problem (VIT FAT 2024)**:  
> For the given weighted graph with vertices $\{1, 2, 3, 4, 5, 6\}$ and edges:  
> $(1, 2)=6, (1, 3)=1, (1, 4)=5, (2, 3)=5, (2, 5)=3, (3, 4)=5, (3, 5)=6, (3, 6)=4, (4, 6)=2, (5, 6)=6$:  
> Find the Minimum Spanning Tree (MST) using: (a) Kruskal's Algorithm, (b) Prim's Algorithm starting at vertex 1. State the minimum total weight.
>
> **Model Solution**:
>
> #### (a) Kruskal's Algorithm Execution:
> 1. Sort all 10 edges in ascending order of weights:  
>    $(1, 3)=1, (4, 6)=2, (2, 5)=3, (3, 6)=4, (1, 4)=5, (2, 3)=5, (3, 4)=5, (1, 2)=6, (5, 6)=6, (3, 5)=6$. `[1M]`
> 2. Iterative Selection ($n-1 = 6-1 = 5$ edges needed):
>    * Edge $(1, 3)$ wt 1: Accepted.
>    * Edge $(4, 6)$ wt 2: Accepted.
>    * Edge $(2, 5)$ wt 3: Accepted.
>    * Edge $(3, 6)$ wt 4: Accepted. (Connects $\{1, 3\}$ and $\{4, 6\}$; no cycle).
>    * Edge $(1, 4)$ wt 5: **REJECTED** (creates cycle $1-3-6-4-1$).
>    * Edge $(2, 3)$ wt 5: Accepted. (Connects $\{2, 5\}$ to $\{1, 3, 4, 6\}$; no cycle).
> 3. We now have 5 edges: $\{(1, 3), (4, 6), (2, 5), (3, 6), (2, 3)\}$.  
>    **Total Weight**: $1 + 2 + 3 + 4 + 5 = \mathbf{15}$. `[4M]`
>
> #### (b) Prim's Algorithm Execution (Start at vertex 1):
> * Step 1: Tree $V_T = \{1\}$. Edges from $1$: $(1, 3)=1, (1, 4)=5, (1, 2)=6$.  
>   Pick minimum: **$(1, 3)$ with weight 1**. $V_T = \{1, 3\}$.
> * Step 2: Available edges from $V_T$: $(3, 6)=4, (3, 2)=5, (3, 4)=5, (1, 4)=5, (1, 2)=6, (3, 5)=6$.  
>   Pick minimum: **$(3, 6)$ with weight 4**. $V_T = \{1, 3, 6\}$.
> * Step 3: Available edges from $V_T$ to unvisited $\{2, 4, 5\}$: $(6, 4)=2, (3, 2)=5, (1, 4)=5, (6, 5)=6$.  
>   Pick minimum: **$(6, 4)$ with weight 2**. $V_T = \{1, 3, 6, 4\}$.
> * Step 4: Available edges from $V_T$ to unvisited $\{2, 5\}$: $(3, 2)=5, (1, 2)=6, (6, 5)=6$.  
>   Pick minimum: **$(3, 2)$ with weight 5**. $V_T = \{1, 3, 6, 4, 2\}$.
> * Step 5: Available edges from $V_T$ to unvisited $\{5\}$: $(2, 5)=3, (3, 5)=6, (6, 5)=6$.  
>   Pick minimum: **$(2, 5)$ with weight 3**. $V_T = \{1, 2, 3, 4, 5, 6\}$.
> 
> All 6 vertices are included.  
> **MST Edges**: $\{(1, 3), (3, 6), (6, 4), (3, 2), (2, 5)\}$.  
> **Total Weight**: $1 + 4 + 2 + 5 + 3 = \mathbf{15}$. `[5M]`

---

### ❓ Question 5.2 (5 Marks): Chromatic Polynomial via Deletion-Contraction
> **Problem (VIT FAT 2024)**:  
> Find the chromatic polynomial $P(G, \lambda)$ of the graph formed by two triangles sharing a common edge (the "Kite" graph / $K_4 - e$).
>
> **Model Solution**:
> 1. Let $G$ be two triangles sharing common edge $e = (u, v)$.
> 2. **Apply Deletion-Contraction Theorem**:  
>    $P(G, \lambda) = P(G - e, \lambda) - P(G / e, \lambda)$ &nbsp;&nbsp;`[1M]`
> 3. **Analyze $G - e$**:  
>    Deleting the shared edge $e$ leaves a 4-cycle $C_4$.  
>    We know: $P(C_4, \lambda) = (\lambda - 1)^4 + (\lambda - 1) = \lambda(\lambda - 1)(\lambda^2 - 3\lambda + 3)$. &nbsp;&nbsp;`[2M]`
> 4. **Analyze $G / e$**:  
>    Contracting the shared edge $e$ merges vertices $u$ and $v$. The two remaining vertices are each connected to the merged vertex, and they are not connected to each other. This forms a star graph / path of length 2 / tree with 3 vertices ($T_3$)!  
>    $P(G / e, \lambda) = P(T_3, \lambda) = \lambda(\lambda - 1)^2$ &nbsp;&nbsp;`[1M]`
> 5. **Subtract**:  
>    $P(G, \lambda) = \lambda(\lambda - 1)(\lambda^2 - 3\lambda + 3) - \lambda(\lambda - 1)^2$  
>    Factor out $\lambda(\lambda - 1)$:  
>    $= \lambda(\lambda - 1) [ (\lambda^2 - 3\lambda + 3) - (\lambda - 1) ]$  
>    $= \lambda(\lambda - 1) [ \lambda^2 - 4\lambda + 4 ]$  
>    $= \mathbf{\lambda(\lambda - 1)(\lambda - 2)^2}$ &nbsp;&nbsp;`[1M]`
>
> *(Verification: If $\lambda = 2$, $P(G, 2) = 0$ because $G$ contains a triangle $K_3$ which needs at least 3 colors. If $\lambda = 3$, $P(G, 3) = 3(2)(1)^2 = 6$ valid colorings!).*

---

### ❓ Question 5.3 (12 Marks): Graph Complement, Isomorphism, Eulerian/Hamiltonian & Chromatic Number (Direct from `some imp.txt`)
> **Problem**:  
> Given two graphs $G_1$ and $G_2$ with 5 vertices each:  
> - $G_1 = (V_1, E_1)$ where $V_1 = \{v_1, v_2, v_3, v_4, v_5\}$ forming a cycle $C_5$: $(v_1, v_2), (v_2, v_3), (v_3, v_4), (v_4, v_5), (v_5, v_1)$.  
> - $G_2 = (V_2, E_2)$ where $V_2 = \{u_1, u_2, u_3, u_4, u_5\}$ forming a star/pentagram cycle: $(u_1, u_3), (u_3, u_5), (u_5, u_2), (u_2, u_4), (u_4, u_1)$.  
> **Questions**:  
> 1. Check whether $G_1$ and $G_2$ are isomorphic.  
> 2. Determine whether $G_1$ and $G_2$ are Eulerian, Hamiltonian, or both.  
> 3. Draw the complement graphs $\overline{G_1}$ and $\overline{G_2}$.  
> 4. Check whether $\overline{G_1}$ and $\overline{G_2}$ are isomorphic, Eulerian, and Hamiltonian.  
> 5. Find the chromatic numbers $\chi(G_1), \chi(G_2), \chi(\overline{G_1}), \chi(\overline{G_2})$.

#### Model Solution:

* **Part 1: Isomorphism of $G_1$ and $G_2$** `[3 Marks]`:
  - Invariants: $|V| = 5$, $|E| = 5$.
  - Degrees: In both graphs, every vertex has degree exactly 2 (2-regular graphs).
  - Cycle Structure: Both are connected simple graphs consisting of a single cycle of length 5 ($C_5$).
  - **Isomorphism Mapping Function $f: V_1 \to V_2$**:
    - $f(v_1) = u_1$
    - $f(v_2) = u_3$
    - $f(v_3) = u_5$
    - $f(v_4) = u_2$
    - $f(v_5) = u_4$
  - Edge preservation: $(v_1, v_2) \to (u_1, u_3) \in E_2$, $(v_2, v_3) \to (u_3, u_5) \in E_2$, etc. All edges preserved.  
    $\therefore \mathbf{G_1 \cong G_2}$ (Isomorphic!).

* **Part 2: Eulerian & Hamiltonian Nature of $G_1$ and $G_2$** `[2 Marks]`:
  - **Eulerian?**: A connected graph has an Euler circuit if and only if every vertex has an **even degree**. Here, $\deg(v) = 2$ (even) for all vertices.  
    $\implies$ **Both $G_1$ and $G_2$ are EULERIAN.** (Euler circuit: $v_1-v_2-v_3-v_4-v_5-v_1$).
  - **Hamiltonian?**: A cycle $C_5$ visits every vertex exactly once and returns to the start.  
    $\implies$ **Both $G_1$ and $G_2$ are HAMILTONIAN.**

* **Part 3: Complement Graphs $\overline{G_1}$ and $\overline{G_2}$** `[2 Marks]`:
  - Complete graph $K_5$ has $\binom{5}{2} = 10$ edges.
  - Number of edges in complement: $|E(\overline{G})| = 10 - 5 = \mathbf{5\text{ edges}}$.
  - In $\overline{G_1}$, edges are the chords: $(v_1, v_3), (v_1, v_4), (v_2, v_4), (v_2, v_5), (v_3, v_5)$.
  - Notice that these 5 edges in $\overline{G_1}$ form another 5-cycle ($C_5$)!  
    *(In fact, the 5-cycle $C_5$ is **self-complementary**: $\overline{C_5} \cong C_5$).*

* **Part 4: Isomorphism, Eulerian & Hamiltonian for Complements** `[2 Marks]`:
  - **Theorem**: Two graphs are isomorphic if and only if their complements are isomorphic:
    $$G_1 \cong G_2 \iff \overline{G_1} \cong \overline{G_2}$$
  - Since $G_1 \cong G_2$, **$\overline{G_1} \cong \overline{G_2}$ is guaranteed.**
  - Since $\overline{G_1}$ and $\overline{G_2}$ are also 5-cycles ($C_5$), every vertex has degree 2 (even).
  - $\implies$ **Both $\overline{G_1}$ and $\overline{G_2}$ are EULERIAN and HAMILTONIAN.**

* **Part 5: Chromatic Numbers** `[3 Marks]`:
  - **Rule for Odd Cycles $C_{2k+1}$**: Any odd cycle has chromatic number $\chi(C_{2k+1}) = 3$. (Requires 3 colors: alternating 2 colors on an odd cycle leaves the last vertex adjacent to two different colors).
  - Therefore:
    - $\mathbf{\chi(G_1) = 3}$
    - $\mathbf{\chi(G_2) = 3}$
    - Since $\overline{G_1} \cong C_5$ and $\overline{G_2} \cong C_5$:
      - $\mathbf{\chi(\overline{G_1}) = 3}$
      - $\mathbf{\chi(\overline{G_2}) = 3}$
  - *(Full 12/12 Marks!)*

---

## 🎯 The Golden Rules to Guarantee Full Marks on FAT Day

1. **State the theorem name** before using it: *"By Euler's Handshaking Lemma"*, *"By Birkhoff's Characterization Theorem"*, *"By the Deletion-Contraction Theorem"*.
2. **Never skip truth table columns**: Show all intermediate components ($p \vee q$, $\neg r$, etc.).
3. **In Graph Isomorphism**: Never just list invariants. **Always provide the mapping table $f(u_i) = v_j$** and verify that every edge matches.
4. **In Prim's / Kruskal's / Dijkstra's**: Write out the full table of steps. Evaluators grade the steps, not just the final number!
