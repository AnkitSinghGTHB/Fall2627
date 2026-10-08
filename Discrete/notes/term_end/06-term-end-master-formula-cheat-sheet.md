# ⚡ MAT2002: Term End (FAT) Master Formula & Theorem Cheat Sheet

> **Purpose**: 10-Minute quick revision of all critical formulas, rules, and theorems across **Modules 1 through 5** for the Term End Examination.

---

## 📌 Module 1: Predicate Calculus & Logic

* **Connectives Rules**:
  * $p \wedge q = T \iff$ BOTH are True.
  * $p \vee q = F \iff$ BOTH are False.
  * $p \to q = F \iff p = T$ and $q = F$ ($T \to F = F$, all other cases $T$).
  * $p \leftrightarrow q = T \iff$ BOTH have the SAME truth value.
* **Conditionals**:
  * Original: $p \to q \equiv \neg q \to \neg p$ (**Contrapositive**).
  * Converse: $q \to p$. Inverse: $\neg p \to \neg q$. (Converse $\equiv$ Inverse).
* **Key Equivalences**:
  * $p \to q \equiv \neg p \vee q$ &nbsp;&nbsp;|&nbsp;&nbsp; $\neg(p \to q) \equiv p \wedge \neg q$
  * De Morgan: $\neg(p \vee q) \equiv \neg p \wedge \neg q$ &nbsp;&nbsp;|&nbsp;&nbsp; $\neg(p \wedge q) \equiv \neg p \vee \neg q$
  * Absorption: $p \vee (p \wedge q) \equiv p$ &nbsp;&nbsp;|&nbsp;&nbsp; $p \wedge (p \vee q) \equiv p$
  * Distributive: $p \wedge (q \vee r) \equiv (p \wedge q) \vee (p \wedge r)$
* **Rules of Inference**:
  * **Modus Ponens (MP)**: $p, p \to q \vdash q$
  * **Modus Tollens (MT)**: $\neg q, p \to q \vdash \neg p$
  * **Hypothetical Syllogism (HS)**: $p \to q, q \to r \vdash p \to r$
  * **Disjunctive Syllogism (DS)**: $p \vee q, \neg p \vdash q$
* **Quantifiers**:
  * $\neg \forall x P(x) \equiv \exists x \neg P(x)$ &nbsp;&nbsp;|&nbsp;&nbsp; $\neg \exists x P(x) \equiv \forall x \neg P(x)$
  * **Rule of Thumb**: Perform **EI (Existential Instantiation) BEFORE UI (Universal Instantiation)**!

---

## 📌 Module 2: Sets, Relations & Hasse Diagrams

* **Relation Properties on Set $A$**:
  * **Reflexive**: $\forall a, (a, a) \in R$ &nbsp;&nbsp;(Matrix diagonal all 1s).
  * **Symmetric**: $(a, b) \in R \implies (b, a) \in R$ &nbsp;&nbsp;($M_R = M_R^T$).
  * **Anti-symmetric**: $(a, b) \in R \text{ and } (b, a) \in R \implies a = b$ &nbsp;&nbsp;(No off-diagonal two-way pairs).
  * **Transitive**: $(a, b) \in R \text{ and } (b, c) \in R \implies (a, c) \in R$.
* **Equivalence Relation**: Reflexive + Symmetric + Transitive. Equivalence classes $[a]$ form a partition of $A$.
* **POSET (Partially Ordered Set)**: Reflexive + Anti-symmetric + Transitive.
* **Hasse Diagram Recipe**: Remove self-loops $\to$ remove transitive shortcuts $\to$ draw smaller elements lower, larger higher $\to$ omit arrows.
* **Divisibility Poset $(D_n, \mid)$**:
  * Bottom element $= 1$. Top element $= n$.
  * $\text{GLB}(a, b) = \gcd(a, b)$ &nbsp;&nbsp;|&nbsp;&nbsp; $\text{LUB}(a, b) = \operatorname{lcm}(a, b)$.
* **Extremal Elements**:
  * Maximal = nothing strictly above it (can be multiple).
  * Greatest = unique element above everything (at most one).
  * Minimal = nothing strictly below it (can be multiple).
  * Least = unique element below everything (at most one).

---

## 📌 Module 3: Lattices & Boolean Algebra

* **Lattice Condition**: Every pair $\{a, b\}$ must have a unique $\text{GLB}(a, b) = a \wedge b$ and a unique $\text{LUB}(a, b) = a \vee b$.
* **Fast Failure Check**: If finite poset has $>1$ top or $>1$ bottom, it is **NOT a lattice**!
* **Sub-Lattice Test**: A subset $S \subseteq L$ must be closed under operations of $L$: $\forall a, b \in S \implies (a \wedge_L b) \in S \text{ and } (a \vee_L b) \in S$.
* **Lattice Types**:
  * **Bounded**: Has least element $0$ and greatest element $1$.
  * **Complemented**: Bounded, and every element $a$ has at least one complement $a'$ such that $a \wedge a' = 0$ and $a \vee a' = 1$.
  * **Distributive**: Meet distributes over join, and join distributes over meet. (Complements are unique!).
* **Birkhoff's Theorem**: A lattice is Distributive $\iff$ It contains **NO sub-lattice isomorphic to $M_5$ (Diamond) or $N_5$ (Pentagon)**.
* **Boolean Algebra**: Lattice that is BOTH **Complemented AND Distributive**.
* **Square-Free Rule for $D_n$**: $(D_n, \mid)$ is a Boolean algebra $\iff n$ is **square-free** (no $p^2$ in prime factorization). Number of elements $= 2^k$.
* **Normal Forms**:
  * $\text{PDNF} = \sum m(\text{indices of 1s in truth table})$.
  * $\text{PCNF} = \prod M(\text{indices of 0s in truth table})$.
* **Switching Circuits**: Series $= A \cdot B$ (AND) &nbsp;|&nbsp; Parallel $= A + B$ (OR).

---

## 📌 Module 4: Graphs & Matrix Representations

* **Handshaking Lemma**: $\sum_{v \in V} \deg(v) = 2|E|$. Number of odd-degree vertices is **ALWAYS EVEN**.
* **Havel-Hakimi Algorithm**: Sort descending $\to$ delete 1st element $d_1$ $\to$ subtract 1 from next $d_1$ elements $\to$ re-sort $\to$ repeat. Success if all 0s; Failure if negative.
* **Standard Graphs**:
  * $K_n$: Edges $= \frac{n(n-1)}{2}$, $(n-1)$-regular.
  * $C_n$: Edges $= n$, 2-regular.
  * $W_n$: Edges $= 2(n-1)$, $n$ vertices.
  * $K_{m,n}$: Edges $= m \cdot n$, $m+n$ vertices.
* **Bipartite Graph Theorem**: $G$ is Bipartite $\iff$ **$G$ contains NO ODD CYCLES!**
* **Graph Isomorphism 5 Invariants**: Vertices count $\to$ Edges count $\to$ Degree sequence $\to$ Cycle counts (triangles, 4-cycles) $\to$ Neighbor degree matching. *(Must provide explicit bijection table $u_i \mapsto v_j$)*.
* **Self-Complementary Graph**: $|E| = \frac{n(n-1)}{4} \implies n \equiv 0 \text{ or } 1 \pmod 4$.
* **Eulerian vs Hamiltonian**:
  * **Euler Circuit (Closed)**: Connected + **ALL vertices have EVEN degree**.
  * **Euler Trail (Open)**: Connected + **EXACTLY TWO vertices have ODD degree**.
  * **Dirac's Theorem (Hamiltonian)**: $n \ge 3$, $\deg(v) \ge n/2$ for all $v \implies$ Hamiltonian.
  * **Ore's Theorem (Hamiltonian)**: $n \ge 3$, non-adjacent $\deg(u) + \deg(v) \ge n \implies$ Hamiltonian.
* **Adjacency Matrix $A(G)$**: Entry $(i, j)$ in $A^k =$ number of walks of length $k$ between $v_i$ and $v_j$.
* **Incidence Matrix $M(G)$**: Size $n \times m$. Every column in an undirected graph has **exactly two 1s**.
* **Dijkstra's Algorithm**: $D[v] = \min(D[v], D[u] + w(u, v))$. Always maintain visited set $S$ and update table.

---

## 📌 Module 5: Trees & Graph Coloring

* **6 Tree Characterizations** (any one implies the other 5):
  1. Connected and acyclic.
  2. Connected with $e = n - 1$.
  3. Acyclic with $e = n - 1$.
  4. Unique simple path between every pair of vertices.
  5. Minimally connected (every edge is a bridge).
  6. Maximally acyclic (adding any edge creates a unique cycle).
* **Tree Properties**: Every tree ($n \ge 2$) has at least **two pendant vertices (leaves, degree 1)**. Trees are bipartite ($\chi = 2$).
* **Jordan's Center Theorem**: Every tree has either **1 center or 2 adjacent centers**. Find it by successively pruning leaves.
* **Cayley's Formula**: Complete graph $K_n$ has **$n^{n-2}$ labeled spanning trees**.
* **MST Algorithms**:
  * **Kruskal**: Sort all edges globally; greedily add smallest edge that does NOT create a cycle.
  * **Prim**: Start at a vertex; greedily add the smallest edge connecting inside tree to outside.
* **Cut Sets & Fundamental Systems**:
  * Rank (Branches / Fundamental Cut Sets) $= \mathbf{n - 1}$.
  * Nullity / Cyclomatic Number (Chords / Fundamental Circuits) $= \mathbf{m - n + 1}$.
  * $\text{Rank} + \text{Nullity} = (n - 1) + (m - n + 1) = \mathbf{m\text{ (Total Edges)}}$.
* **Chromatic Number $\chi(G)$ Table**:
  * Complete graph $K_n$: $\mathbf{n}$
  * Bipartite graph $K_{m,n}$: $\mathbf{2}$
  * Trees: $\mathbf{2}$
  * Cycle $C_n$: $\mathbf{2}$ if $n$ is even; $\mathbf{3}$ if $n$ is odd.
  * Wheel $W_n$: $\mathbf{3}$ if $n$ is odd; $\mathbf{4}$ if $n$ is even.
  * Planar graphs: **$\le 4$** (Four Color Theorem).
* **Chromatic Index $\chi'(G)$ (Edge Coloring)**:
  * Vizing's Theorem: $\mathbf{\Delta \le \chi'(G) \le \Delta + 1}$.
* **Chromatic Polynomial $P(G, \lambda)$**:
  * Null graph $N_n$: $\lambda^n$
  * Tree with $n$ vertices $T_n$: $\mathbf{\lambda(\lambda - 1)^{n-1}}$
  * Complete graph $K_n$: $\lambda(\lambda - 1)\dots(\lambda - n + 1)$
  * Cycle $C_n$: $(\lambda - 1)^n + (-1)^n(\lambda - 1)$
  * **Deletion-Contraction Theorem**: $P(G, \lambda) = P(G - e, \lambda) - P(G / e, \lambda)$.
