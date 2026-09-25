# ✍️ MAT2002 Discrete Mathematics — Final Notebook Copy-Writing Crib
> **Purpose**: A ultra-dense, 4-page handwritten-style summary designed to be written down directly into your physical notebook or copy before entering the exam hall.

---

## 📘 MODULE 3: LATTICES & BOOLEAN ALGEBRA

### 1. Lattice Definition & Axioms
* A poset $(L, \le)$ is a **lattice** if $\forall a, b \in L$, $\text{GLB}(a, b) = a \wedge b$ (Meet) and $\text{LUB}(a, b) = a \vee b$ (Join) exist uniquely.
* **4 Mandatory Axioms**:
  1. Idempotent: $a \wedge a = a$, $a \vee a = a$.
  2. Commutative: $a \wedge b = b \wedge a$, $a \vee b = b \vee a$.
  3. Associative: $(a \wedge b) \wedge c = a \wedge (b \wedge c)$, $(a \vee b) \vee c = a \vee (b \vee c)$.
  4. Absorption: $a \wedge (a \vee b) = a$, $a \vee (a \wedge b) = a$.
* **Bridge Theorem**: $a \le b \iff a \wedge b = a \iff a \vee b = b$.

### 2. Distributive Lattices & Median Identity
* **Distributive Laws**:
  * $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$
  * $a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c)$
* **Golden Factoring Trick for $(a \vee b) \wedge (b \vee c) \wedge (c \vee a)$**:
  * Step 1: Let $T = (b \vee a) \wedge (b \vee c) = \mathbf{b \vee (a \wedge c)}$.
  * Step 2: Multiply by $(c \vee a) \implies [b \wedge (c \vee a)] \vee [(a \wedge c) \wedge (c \vee a)]$.
  * Step 3: By absorption, $(a \wedge c) \wedge (a \vee c) = a \wedge c$.
  * Step 4: Expand $b \wedge (c \vee a) = (a \wedge b) \vee (b \wedge c)$.
  * Result: $(a \wedge b) \vee (b \wedge c) \vee (c \wedge a) \quad \blacksquare$.

### 3. Complements & Non-Square-Free Divisor Trap ($D_n$)
* Element $x'$ is complement of $x$ if $x \wedge x' = 0$ and $x \vee x' = 1$. In $D_n$: $0 = 1$ and $1 = n$.
* $\gcd(x, x') = 1$ and $\text{lcm}(x, x') = n$.
* **Square-Free Rule**: $(D_n, \mid)$ is a Boolean algebra $\iff n$ is **square-free** ($n = p_1 p_2 \dots p_k$).
  * $D_{30} = 2 \cdot 3 \cdot 5 \implies$ Square-free $\implies$ Boolean algebra ($B_3$).
  * $D_{70} = 2 \cdot 5 \cdot 7 \implies$ Square-free $\implies$ Boolean algebra ($B_3$).
  * $D_{12} = 2^2 \cdot 3 \implies$ NOT square-free $\implies$ Element 2 has **NO complement** (since $\gcd(2, x')=1 \implies x'$ is odd $\implies \text{lcm}(2, x')$ cannot contain $2^2 \implies \text{lcm} \ne 12$).
  * $D_{18} = 2 \cdot 3^2 \implies 3$ has no complement; $D_{36} = 2^2 \cdot 3^2 \implies 2, 3$ fail.

### 4. Modular vs Distributive ($M_3$ vs $N_5$)
* **Modular Law**: $a \le c \implies a \vee (b \wedge c) = (a \vee b) \wedge c$.
* $L$ is modular $\iff$ no sublattice is $N_5$ (Pentagon).
* $L$ is distributive $\iff$ no sublattice is $M_3$ (Diamond) or $N_5$.
* Diamond $M_3$ is **modular but NOT distributive**.
* Pentagon $N_5$ is **NEITHER modular NOR distributive**.

### 5. Switching Circuit Rules
* Series $= \cdot$ (AND) | Parallel $= +$ (OR).
* Normally open $= x$ | Normally closed $= x'$.
* **Key Simplifications**:
  * $x + x' y = x + y$ (Redundancy)
  * $x(x' + y) = x y$
  * $x y + x' z + y z = x y + x' z$ (Consensus)
  * Bridge network $T = x_1 x_2 + x_3 x_4 + x_1 x_5 x_4 + x_3 x_5 x_2$.

---

## 📗 MODULE 4: GRAPHS & MATRIX ALGORITHMS

### 1. Handshaking Lemma & Degree Partition
* $\sum_{v \in V} \deg(v) = 2|E|$.
* Corollary: Number of odd-degree vertices is always **EVEN**.
* **Multigraph Rule**: Each self-loop adds **$+2$** to vertex degree!
* **Directed Graph Rule**: $\sum \text{indeg}(v) = \sum \text{outdeg}(v) = |E|$.

### 2. Havel-Hakimi Graphical Sequence Test
1. Sort sequence descending: $S = (d_1, d_2, \dots, d_n)$.
2. Remove $d_1$. Subtract 1 from next $d_1$ elements.
3. If negative appears or length $< d_1 \implies$ **NOT GRAPHICAL**.
4. Re-sort descending. Repeat until all zeros ($\checkmark$ Graphical).

### 3. Graph Complements & Self-Complementary Graphs
* $|E(\overline{G})| = \binom{n}{2} - |E(G)| = \frac{n(n-1)}{2} - |E(G)|$.
* $\deg_{\overline{G}}(v) = (n - 1) - \deg_G(v)$.
* **Self-Complementary ($G \cong \overline{G}$)**:
  * $|E(G)| = \frac{n(n-1)}{4} \implies 4 \mid n(n-1) \implies \mathbf{n \equiv 0 \text{ or } 1 \pmod 4}$.
  * Impossible for $n = 6$ ($|E| = 7.5$). Possible for $n = 4 (P_4), 5 (C_5), 8, 9$.

### 4. Graph Isomorphism Traps
* **5 Invariants to Check**:
  1. $|V_1| = |V_2|$
  2. $|E_1| = |E_2|$
  3. Degree sequences match
  4. Number of connected components match
  5. Number of cycles of each length ($C_3, C_4$) match
* **Trap: 3-Regular Graphs on 6 Vertices ($|V|=6, |E|=9$)**:
  * $K_{3,3}$ (bipartite, 0 triangles, girth 4) $\not\cong$ Prism $Y_3$ (contains 2 triangles $C_3$, girth 3).
* **Trap: $C_6$ vs $2C_3$**: Connected (1 component) vs Disconnected (2 components) $\implies C_6 \not\cong 2C_3$.
* **Trap: $P_4$ vs $K_{1,3}$**: Max degree 2 vs Max degree 3 $\implies P_4 \not\cong K_{1,3}$.

### 5. Bipartite Graphs & Kőnig's Theorem
* $G$ is bipartite $\iff G$ has **NO ODD CYCLES** ($C_3, C_5, C_7$).
* 2-Colorable using BFS (Red/Blue).
* Maximum edges in simple bipartite graph on $n$ vertices $= \lfloor \frac{n^2}{4} \rfloor$.

### 6. Floyd-Warshall All-Pairs Algorithm
* **Recurrence**:
  $$D^{(k)}[i, j] = \min\Big( D^{(k-1)}[i, j], \; D^{(k-1)}[i, k] + D^{(k-1)}[k, j] \Big)$$
* At step $k$: Row $k$ and Column $k$ **NEVER CHANGE**. Diagonal is always 0.

### 7. Dijkstra Algorithm & 4-Case Sensitivity Analysis
* Greedy label relaxation: $d(v) = \min(d(v), d(u^*) + w(u^*, v))$.
* **Sensitivity Analysis when Edge $e$ changes by $\Delta w$**:
  1. $e \in P^*$ and $\Delta w > 0$: Compare $d(P^*) + \Delta w$ with second-best path $d(P_2^*)$. If $\Delta w < \text{Gap}$, route stays.
  2. $e \in P^*$ and $\Delta w < 0$: $P^*$ remains strictly optimal (cost drops by $|\Delta w|$).
  3. $e \notin P^*$ and $\Delta w > 0$: Path totally unaffected.
  4. $e \notin P^*$ and $\Delta w < 0$: Route switches only if $d(u) + w_{\text{new}} + \text{dist}(v, \text{dest}) < d(P^*)$.
