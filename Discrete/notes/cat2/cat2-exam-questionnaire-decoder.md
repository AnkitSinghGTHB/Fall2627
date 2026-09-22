# 🎯 MAT2002: CAT-2 Question-Language Decoder & Master Questionnaire
## Module 3 (Lattices & Boolean Algebra) & Module 4 (Graphs & Matrix Representations)
> **Open-Book Exam Hall Strategy**: When you read an exam problem, **DO NOT** guess the topic or read textbook theory. Find the **exact question phrasing** in the Question-Language Matrix below, identify the required theorem/algorithm, and copy-paste the step-by-step solution template.

---

# PART I: QUESTION-LANGUAGE TO TOPIC SELECTION MATRIX

Use this rapid lookup table during the exam to convert the exam question prompt into the exact topic, test condition, and solution strategy:

| Exact Question Language / Phrasing | Identified Syllabus Topic | Instant Decision Rule / Condition | Direct Solution Action |
| :--- | :--- | :--- | :--- |
| *"Can a simple graph have degree sequence $(d_1, \dots, d_n)$?"* / *"Show that no graph exists with..."* | **Handshaking Lemma & Degree Parity** (Mod 4) | 1. Sum of degrees $\sum d_i$ must be **EVEN**.<br>2. Max degree $\Delta \le n - 1$.<br>3. Count of odd-degree vertices must be **EVEN**. | If sum is odd or odd vertices are odd $\implies$ Write 2-line impossibility proof using Handshaking Theorem. |
| *"Determine whether the sequence is graphic..."* / *"Construct a graph with degrees..."* | **Havel-Hakimi Algorithm** (Mod 4) | Sequence is graphic $\iff$ after recursive reduction (delete $d_1$, subtract 1 from next $d_1$ terms, re-sort), all terms reach non-negative integers or zeros. | Set up the standard 4-column reduction table (Step, Sorted Sequence, Reduction, Status). |
| *"Prove that in any group of $n \ge 2$ people, at least two have the same number of friends."* | **Pigeonhole Principle & Handshaking** (Mod 4) | Degree set for simple graph on $n$ vertices cannot contain both $0$ and $n-1$. Degree values must map to $\{0, \dots, n-2\}$ or $\{1, \dots, n-1\}$ ($n-1$ pigeonholes for $n$ pigeons). | Apply PHP: $n$ vertices into $\le n-1$ possible degree values $\implies$ at least 2 vertices have identical degree. |
| *"Determine whether the two graphs $G_1$ and $G_2$ are isomorphic..."* | **Graph Isomorphism & Invariants** (Mod 4) | If isomorphic: $|V_1|=|V_2|$, $|E_1|=|E_2|$, degree sequences match, cycle spectrum matches, complement isomorphic.<br>If non-isomorphic: find **ONE** invariant that differs. | If isomorphic: provide table mapping $f(u_i) = v_j$ and show $(u, v) \in E_1 \iff (f(u), f(v)) \in E_2$.<br>If non-isomorphic: state invariant counterexample (e.g., $c(G)$ or count of $C_3$). |
| *"Show that a simple graph is self-complementary ($G \cong \overline{G}$) only if..."* | **Self-Complementary Graphs** (Mod 4) | Total edges in $K_n$ is $\frac{n(n-1)}{2}$. Since $|E(G)| = |E(\overline{G})|$, $|E(G)| = \frac{n(n-1)}{4}$. Thus $n(n-1)$ must be divisible by 4. | Conclude $n \equiv 0 \pmod 4$ or $n \equiv 1 \pmod 4$. Provide example $P_4$ ($n=4$) or $C_5$ ($n=5$). |
| *"Determine whether graph $G$ is bipartite..."* / *"Check if $G$ has an odd cycle..."* | **Bipartite Graphs & Kőnig's Theorem** (Mod 4) | A graph is bipartite $\iff$ it contains **NO odd cycles** ($\iff$ 2-colorable). | Run BFS 2-coloring (Red/Blue). If neighbor gets same color $\implies$ odd cycle found $\implies$ NOT bipartite. |
| *"Find the number of edges in an $r$-regular graph with $n$ vertices..."* | **Regular Graphs & Handshaking** (Mod 4) | $2|E| = \sum \deg(v) = n \cdot r \implies |E| = \frac{n \cdot r}{2}$. | Check that $n \cdot r$ is even. If odd, state such a regular graph cannot exist. |
| *"Find the shortest path from vertex $S$ to all other vertices..."* | **Dijkstra's Algorithm** (Mod 4) | Greedy shortest path on non-negative weighted directed/undirected graph. Maintain permanent set $S$ and tentative labels $d[v]$. | Draw standard iteration table with columns $[k, u^*, d[A], \dots, d[E]]$. State final shortest path tree. |
| *"Draw the Hasse diagram for the divisor poset $(D_n, \mid)$..."* | **Divisor Posets & Hasse Diagrams** (Mod 3) | Elements are divisors of $n$. Vertex $a$ is below $b$ if $a \mid b$. Edge exists if $b$ covers $a$ ($b/a$ is prime). | Draw bottom-to-top layers: Layer 0 ($1$), Layer 1 (primes), Layer 2 (products of 2 primes), ..., Top ($n$). |
| *"Is $(D_n, \mid)$ a Boolean algebra?"* | **Boolean Algebra Criterion** (Mod 3) | $(D_n, \mid)$ is a Boolean algebra $\iff n$ is **square-free** (product of distinct primes, no $p^2 \mid n$). | Factor $n = p_1^{a_1} \cdots p_k^{a_k}$. If any $a_i \ge 2$, state non-square-free $\implies$ prime power lacks complement. |
| *"Determine whether the lattice is distributive..."* | **Distributive Lattices & Birkhoff's Theorem** (Mod 3) | A lattice is distributive $\iff$ it contains **NO sublattice isomorphic to Diamond $M_3$ or Pentagon $N_5$**. | Search Hasse diagram for $M_3$ (3 intermediate incomparable elements) or $N_5$ (chain of 2 incomparable to 1). Write algebraic counterexample $a \wedge (b \vee c) \ne (a \wedge b) \vee (a \wedge c)$. |
| *"Find all complements of element $x$ in lattice $L$..."* | **Complemented Lattices** (Mod 3) | $y$ is a complement of $x \iff x \wedge y = 0$ (bottom) AND $x \vee y = 1$ (top). | For $x$, test each candidate $y$. Compute meet (gcd or intersection) and join (lcm or union). State whether unique or non-existent. |
| *"Express the Boolean expression $f$ in PDNF and PCNF..."* | **Normal Forms (Minterms & Maxterms)** (Mod 3) | $\text{PDNF} = \sum m(\text{minterms where } f=1)$.<br>$\text{PCNF} = \prod M(\text{maxterms where } f=0)$. | Method A: Truth table $\to$ read rows.<br>Method B: Algebraic expansion using $x = x \wedge (y \vee y')$. |
| *"Design / Simplify a switching contact network for..."* | **Switching Circuits** (Mod 3) | Series $= \text{AND} \; (A \cdot B)$; Parallel $= \text{OR} \; (A + B)$; Normally closed $= \text{NOT} \; (A')$. | Simplify expression via Boolean laws, then draw series-parallel contact boxes from input terminal to output terminal. |

---

# PART II: MODULE 3 QUESTIONNAIRE (Lattices & Boolean Algebra)

---

### Question 1: Divisor Poset Lattice Verification
**Exam Question Language**:
> *"Let $A = \{1, 2, 3, 4, 6, 8, 9, 12, 18, 24\}$ with partial order relation 'divides' ($a \mid b$). Determine whether $(A, \mid)$ is a lattice. Justify your answer."*

**Topic & Trigger Words**: *"divides"*, *"is a lattice"*, *"justify"*.
**Decision Rule**: In $(A, \mid)$, join is $\text{lcm}(a, b)$ and meet is $\gcd(a, b)$. If $\text{lcm}(a, b) \notin A$ or $\gcd(a, b) \notin A$ for any pair, it fails to be a lattice.

#### Model Solution to Write in Exam:
1. **Definition**: A poset $(A, \le)$ is a lattice if and only if every non-empty pair $\{a, b\} \subseteq A$ possesses both a unique Least Upper Bound ($\text{LUB} = a \vee b$) and a unique Greatest Lower Bound ($\text{GLB} = a \wedge b$) in $A$.
2. **Analysis for Relation $a \mid b$**:
   * For divisibility, the upper bound of $a$ and $b$ must be a common multiple in $A$, and $\text{LUB}(a, b) = \text{lcm}(a, b)$ if it belongs to $A$.
   * Consider elements $8 \in A$ and $9 \in A$:
     $$\text{lcm}(8, 9) = 72$$
   * The common multiples of 8 and 9 must be multiples of 72 ($72, 144, \dots$).
   * However, $72 \notin A$, and no element in $A$ is a multiple of both 8 and 9.
   * Therefore, the pair $\{8, 9\}$ has **no upper bound** in $A$, which means $\text{LUB}(8, 9)$ does not exist.
3. **Second Counterexample (Two Incomparable Minimal Upper Bounds)**:
   * Consider elements $12 \in A$ and $18 \in A$:
     * $\text{lcm}(12, 18) = 36 \notin A$. Common upper bounds in $A$: None.
   * Elements $24$ and $18$ are both maximal elements in $A$, so there is no unique greatest element (top).
4. **Conclusion**:
   $$\mathbf{(A, \mid) \text{ is NOT a lattice because } \text{LUB}(8, 9) \text{ does not exist in } A.}$$

---

### Question 2: Hasse Diagram Construction & Extremal Elements
**Exam Question Language**:
> *"Draw the Hasse diagram for the divisor poset $(D_{12}, \mid)$ where $D_{12} = \{1, 2, 3, 4, 6, 12\}$. Find all maximal, minimal, greatest, and least elements. Is it a bounded lattice?"*

**Topic & Trigger Words**: *"Hasse diagram"*, *"maximal/minimal"*, *"greatest/least"*, *"bounded"*.

#### Model Solution to Write in Exam:
1. **Elements & Covering Relations**:
   * $D_{12} = \{1, 2, 3, 4, 6, 12\}$.
   * Covering relation: $a \prec b \iff a \mid b$ and $b/a$ is prime:
     * $1 \prec 2$ (since $2/1=2$), $1 \prec 3$ (since $3/1=3$).
     * $2 \prec 4$ ($4/2=2$), $2 \prec 6$ ($6/2=3$).
     * $3 \prec 6$ ($6/3=2$).
     * $4 \prec 12$ ($12/4=3$), $6 \prec 12$ ($12/6=2$).
2. **Hasse Diagram (Layers)**:
   * **Level 3 (Top)**: $12$
   * **Level 2**: $4$ (connected to 2, 12), $6$ (connected to 2, 3, 12)
   * **Level 1**: $2$ (connected to 1, 4, 6), $3$ (connected to 1, 6)
   * **Level 0 (Bottom)**: $1$ (connected to 2, 3)
3. **Extremal Elements Table**:
   * **Minimal Element(s)**: $\{1\}$ (no element divides 1 except itself).
   * **Maximal Element(s)**: $\{12\}$ (12 divides no other element in $D_{12}$).
   * **Least Element ($0$)**: $1$ (since $1 \mid x$ for all $x \in D_{12}$). Unique.
   * **Greatest Element ($1$)**: $12$ (since $x \mid 12$ for all $x \in D_{12}$). Unique.
4. **Boundedness**:
   * Since $(D_{12}, \mid)$ has both a unique least element $0 = 1$ and a unique greatest element $1 = 12$, it is a **bounded lattice** denoted $(D_{12}, \vee, \wedge, 1, 12)$.

---

### Question 3: Complemented Lattice Test & Finding Complements
**Exam Question Language**:
> *"Define a complemented lattice. Determine whether $(D_{12}, \mid)$ is a complemented lattice by finding the complements of all its elements."*

**Topic & Trigger Words**: *"complemented lattice"*, *"find complements of all elements"*.
**Decision Rule**: Element $b$ is a complement of $a$ if $a \wedge b = 0 = 1$ ($\gcd = 1$) and $a \vee b = 1 = 12$ ($\text{lcm} = 12$).

#### Model Solution to Write in Exam:
1. **Definition**: A bounded lattice $(L, \vee, \wedge, 0, 1)$ is **complemented** if for every element $a \in L$, there exists at least one element $b \in L$ such that:
   $$a \wedge b = 0 \quad \text{and} \quad a \vee b = 1$$
   In $(D_{12}, \mid)$, $0 = 1$ and $1 = 12$, with $\wedge = \gcd$ and $\vee = \text{lcm}$.
2. **Systematic Complement Search for Every Element**:
   * **Element $1$**: Complement is $12$ because $\gcd(1, 12) = 1$ and $\text{lcm}(1, 12) = 12$.
   * **Element $12$**: Complement is $1$ because $\gcd(12, 1) = 1$ and $\text{lcm}(12, 1) = 12$.
   * **Element $3$**: We need $x \in D_{12}$ such that $\gcd(3, x) = 1$ and $\text{lcm}(3, x) = 12$.
     * Candidates coprime to 3: $\{1, 2, 4\}$.
     * $\text{lcm}(3, 1) = 3 \ne 12$; $\text{lcm}(3, 2) = 6 \ne 12$; $\text{lcm}(3, 4) = 12$.
     * Thus, the complement of $3$ is **$4$** (and complement of $4$ is **$3$**).
   * **Element $2$**: We need $x \in D_{12}$ such that $\gcd(2, x) = 1$ and $\text{lcm}(2, x) = 12$.
     * Divisors coprime to 2: only $\{1, 3\}$.
     * Check $x = 1$: $\text{lcm}(2, 1) = 2 \ne 12$.
     * Check $x = 3$: $\text{lcm}(2, 3) = 6 \ne 12$.
     * No element satisfies both conditions! Hence, **element $2$ has NO complement**.
   * **Element $6$**: Requires $\gcd(6, x) = 1 \implies x \in \{1\}$. But $\text{lcm}(6, 1) = 6 \ne 12$.
     * Hence, **element $6$ has NO complement**.
3. **Conclusion**:
   $$\mathbf{(D_{12}, \mid) \text{ is NOT a complemented lattice because elements } 2 \text{ and } 6 \text{ have no complements.}}$$

---

### Question 4: Distributive Lattice & Birkhoff's Representation Theorem
**Exam Question Language**:
> *"State Birkhoff's theorem on distributive lattices. Using algebraic counterexamples, prove why the Diamond lattice $M_3$ and the Pentagon lattice $N_5$ are non-distributive."*

**Topic & Trigger Words**: *"Birkhoff's theorem"*, *"Diamond lattice M3"*, *"Pentagon lattice N5"*, *"algebraic counterexample"*.

#### Model Solution to Write in Exam:
1. **Birkhoff's Theorem (Forbidden Sublattice Characterization)**:
   > A lattice $L$ is **distributive** if and only if no sublattice of $L$ is isomorphic to either the **Diamond lattice $M_3$** or the **Pentagon lattice $N_5$**.
2. **Algebraic Counterexample on Diamond Lattice $M_3$**:
   * Let $M_3 = \{0, a, b, c, 1\}$ where $a, b, c$ are mutually incomparable elements covering $0$ and covered by $1$.
   * We test the distributive law: $x \wedge (y \vee z) = (x \wedge y) \vee (x \wedge z)$ for $x = a, y = b, z = c$:
     $$\text{LHS} = a \wedge (b \vee c) = a \wedge 1 = \mathbf{a}$$
     $$\text{RHS} = (a \wedge b) \vee (a \wedge c) = 0 \vee 0 = \mathbf{0}$$
   * Since $\text{LHS} = a \ne 0 = \text{RHS}$, the distributive law fails. Hence $M_3$ is non-distributive.
3. **Algebraic Counterexample on Pentagon Lattice $N_5$**:
   * Let $N_5 = \{0, a, b, c, 1\}$ with ordering $a < b$, while $c$ is incomparable to both $a$ and $b$ ($a \vee c = 1$, $b \vee c = 1$, $a \wedge c = 0$, $b \wedge c = 0$).
   * We test the distributive law: $x \wedge (y \vee z) = (x \wedge y) \vee (x \wedge z)$ for $x = b, y = a, z = c$:
     $$\text{LHS} = b \wedge (a \vee c) = b \wedge 1 = \mathbf{b}$$
     $$\text{RHS} = (b \wedge a) \vee (b \wedge c) = a \vee 0 = \mathbf{a}$$
   * Since $a < b$, $\mathbf{b \ne a} \implies \text{LHS} \ne \text{RHS}$. The distributive law fails.
4. **Distinction between $M_3$ and $N_5$**:
   * $M_3$ is **modular** but non-distributive.
   * $N_5$ is **non-modular** and non-distributive.

---

### Question 5: Boolean Algebra Criterion for Divisor Lattices $(D_n, \mid)$
**Exam Question Language**:
> *"Show that $(D_{30}, \mid)$ is a Boolean algebra, but $(D_{18}, \mid)$ is not. State the general condition on $n$ for $(D_n, \mid)$ to be a Boolean algebra."*

**Topic & Trigger Words**: *"Boolean algebra"*, *"D30"*, *"D18"*, *"general condition on n"*, *"square-free"*.

#### Model Solution to Write in Exam:
1. **General Theorem**:
   > The divisor lattice $(D_n, \mid)$ is a Boolean algebra if and only if $n$ is **square-free** (i.e., $n$ is a product of distinct prime factors, $n = p_1 p_2 \cdots p_k$ with no prime repeated).
   > If $n$ is square-free, $(D_n, \mid)$ is isomorphic to the Boolean algebra of subsets $(\mathcal{P}(\{p_1, \dots, p_k\}), \subseteq) \cong B_k$ of size $2^k$.
2. **Analysis for $D_{30}$**:
   * Prime factorization: $30 = 2 \times 3 \times 5$.
   * All prime exponents are 1 $\implies 30$ is **square-free**.
   * Number of elements $|D_{30}| = 2^3 = 8$.
   * Divisor set: $D_{30} = \{1, 2, 3, 5, 6, 10, 15, 30\}$.
   * Every element $x$ has a unique complement $x' = 30/x$ (e.g., $2' = 15$, $3' = 10$, $6' = 5$).
   * Because it is isomorphic to $B_3 = \mathcal{P}(\{2, 3, 5\})$, it is bounded, complemented, and distributive.
   * $\mathbf{(D_{30}, \mid) \text{ is a Boolean algebra.}}$
3. **Analysis for $D_{18}$**:
   * Prime factorization: $18 = 2 \times 3^2$.
   * Here $3^2 \mid 18$, so $18$ is **NOT square-free**.
   * Divisor set: $D_{18} = \{1, 2, 3, 6, 9, 18\}$.
   * Test element $3$: we require $x \in D_{18}$ such that $\gcd(3, x) = 1$ and $\text{lcm}(3, x) = 18$.
     * Divisors coprime to 3: only $\{1, 2\}$.
     * $\text{lcm}(3, 1) = 3 \ne 18$.
     * $\text{lcm}(3, 2) = 6 \ne 18$.
     * No divisor satisfies the condition! Element $3$ has no complement in $D_{18}$.
   * $\mathbf{(D_{18}, \mid) \text{ is NOT a complemented lattice, and hence NOT a Boolean algebra.}}$

---

### Question 6: Principal Normal Forms (PDNF & PCNF)
**Exam Question Language**:
> *"Find the Principal Disjunctive Normal Form (PDNF) and Principal Conjunctive Normal Form (PCNF) for the Boolean function $f(p, q, r) = p \wedge (q \vee r)$. Express both in minterm and maxterm shorthand."*

**Topic & Trigger Words**: *"PDNF"*, *"PCNF"*, *"minterms"*, *"maxterms"*, *"normal form"*.

#### Model Solution to Write in Exam:
1. **Truth Table Construction (3 Variables: $p, q, r$)**:

| Row ($i$) | $p$ | $q$ | $r$ | $q \vee r$ | $f = p \wedge (q \vee r)$ | Minterm ($m_i$) | Maxterm ($M_i$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 0 | **0** | $p' \wedge q' \wedge r'$ | $p \vee q \vee r$ |
| 1 | 0 | 0 | 1 | 1 | **0** | $p' \wedge q' \wedge r$ | $p \vee q \vee r'$ |
| 2 | 0 | 1 | 0 | 1 | **0** | $p' \wedge q \wedge r'$ | $p \vee q' \vee r$ |
| 3 | 0 | 1 | 1 | 1 | **0** | $p' \wedge q \wedge r$ | $p \vee q' \vee r'$ |
| 4 | 1 | 0 | 0 | 0 | **0** | $p \wedge q' \wedge r'$ | $p' \vee q \vee r$ |
| 5 | 1 | 0 | 1 | 1 | **1** | $p \wedge q' \wedge r$ | $p' \vee q \vee r'$ |
| 6 | 1 | 1 | 0 | 1 | **1** | $p \wedge q \wedge r'$ | $p' \vee q' \vee r$ |
| 7 | 1 | 1 | 1 | 1 | **1** | $p \wedge q \wedge r$ | $p' \vee q' \vee r'$ |

2. **PDNF (Sum of Minterms where $f = 1$)**:
   * Rows where $f = 1$ are $\{5, 6, 7\}$.
   $$\mathbf{\text{PDNF} = (p \wedge q' \wedge r) \vee (p \wedge q \wedge r') \vee (p \wedge q \wedge r)}$$
   $$\mathbf{\text{Shorthand: } \text{PDNF} = \sum m(5, 6, 7)}$$

3. **PCNF (Product of Maxterms where $f = 0$)**:
   * Rows where $f = 0$ are the complementary set $\{0, 1, 2, 3, 4\}$.
   $$\mathbf{\text{PCNF} = (p \vee q \vee r) \wedge (p \vee q \vee r') \wedge (p \vee q' \vee r) \wedge (p \vee q' \vee r') \wedge (p' \vee q \vee r)}$$
   $$\mathbf{\text{Shorthand: } \text{PCNF} = \prod M(0, 1, 2, 3, 4)}$$

---

# PART III: MODULE 4 QUESTIONNAIRE (Graphs & Matrix Representations)

---

### Question 7: Handshaking Lemma & Feasibility of Degree Sequences
**Exam Question Language**:
> *"Can a simple graph have 7 vertices of degree 3? What about a simple graph with degree sequence $(5, 5, 4, 3, 2, 1)$ on 6 vertices? Justify each using Euler's Handshaking Theorem."*

**Topic & Trigger Words**: *"can a simple graph have"*, *"degree sequence"*, *"Handshaking theorem"*, *"justify"*.

#### Model Solution to Write in Exam:
1. **Case A: 7 vertices of degree 3**:
   * **Theorem Statement**: By Euler's Handshaking Lemma, in any undirected graph $G = (V, E)$:
     $$\sum_{v \in V} \deg(v) = 2|E|$$
     Because $2|E|$ is an integer multiple of 2, the sum of degrees must always be an **EVEN** number.
   * **Degree Sum Calculation**:
     $$\sum \deg(v) = 7 \times 3 = 21$$
   * Since $21$ is **ODD**, $2|E| = 21 \implies |E| = 10.5$, which is impossible because edge count must be an integer.
   * **Corollary Check**: There are 7 vertices of odd degree (3). But by corollary, the number of odd-degree vertices must be strictly **even**.
   * $\mathbf{\text{Conclusion: No graph can have 7 vertices of degree 3.}}$

2. **Case B: Degree Sequence $(5, 5, 4, 3, 2, 1)$ on $n = 6$ vertices**:
   * **Step 1 (Degree Sum Check)**:
     $$\sum d_i = 5 + 5 + 4 + 3 + 2 + 1 = 20 \quad (\text{EVEN } \checkmark)$$
   * **Step 2 (Odd Degree Vertices Count)**:
     * Odd degree values are $5, 5, 3, 1$ (Total 4 odd vertices, which is EVEN $\checkmark$).
   * **Step 3 (Maximum Degree Constraint for Simple Graph)**:
     * In a simple graph on $n$ vertices (no loops, no parallel edges), each vertex can connect to at most $n - 1$ other vertices.
     * Here $n = 6$, so maximum allowed degree $\Delta \le 6 - 1 = 5$.
     * Two vertices have degree 5. Let these be $u$ and $v$.
     * Both $u$ and $v$ must be connected to **all other 5 vertices** in the graph.
     * In particular, both $u$ and $v$ must connect to the vertex with degree 1, say $w$.
     * But if $w$ connects to both $u$ and $v$, then $\deg(w) \ge 2$, contradicting $\deg(w) = 1$!
   * $\mathbf{\text{Conclusion: No simple graph can have degree sequence } (5, 5, 4, 3, 2, 1).}$

---

### Question 8: Havel-Hakimi Graphic Sequence Algorithm
**Exam Question Language**:
> *"Apply the Havel-Hakimi theorem to determine whether the degree sequence $S = (5, 4, 3, 3, 2, 2, 1)$ is graphic. If it is graphic, construct a corresponding simple graph."*

**Topic & Trigger Words**: *"Havel-Hakimi theorem"*, *"graphic"*, *"construct a simple graph"*.

#### Model Solution to Write in Exam:
1. **Theorem Statement**:
   > A non-increasing sequence of non-negative integers $S = (d_1, d_2, \dots, d_n)$ with $d_1 \le n-1$ is graphic if and only if the modified sequence:
   > $$S' = (d_2 - 1, d_3 - 1, \dots, d_{d_1 + 1} - 1, d_{d_1 + 2}, \dots, d_n)$$
   > (obtained by deleting $d_1$ and subtracting 1 from the next $d_1$ terms) is graphic when re-sorted in non-increasing order.

2. **Step-by-Step Execution Table**:

| Step | Current Sequence (Sorted Non-Increasing) | Action Taken ($d_1$ deleted, next $d_1$ decremented) | Resulting Sequence | Re-sorted Sequence |
| :---: | :--- | :--- | :--- | :--- |
| **0** | $(5, 4, 3, 3, 2, 2, 1)$ | $d_1 = 5$. Subtract 1 from next 5 terms: $4, 3, 3, 2, 2$ | $(3, 2, 2, 1, 1, 1)$ | $(3, 2, 2, 1, 1, 1)$ |
| **1** | $(3, 2, 2, 1, 1, 1)$ | $d_1 = 3$. Subtract 1 from next 3 terms: $2, 2, 1$ | $(1, 1, 0, 1, 1)$ | $(1, 1, 1, 1, 0)$ |
| **2** | $(1, 1, 1, 1, 0)$ | $d_1 = 1$. Subtract 1 from next 1 term: $1$ | $(0, 1, 1, 0)$ | $(1, 1, 0, 0)$ |
| **3** | $(1, 1, 0, 0)$ | $d_1 = 1$. Subtract 1 from next 1 term: $1$ | $(0, 0, 0)$ | $(0, 0, 0)$ |

3. **Termination**:
   * At Step 3, the sequence reduces to $(0, 0, 0)$, which represents the null graph on 3 isolated vertices $N_3$ (trivially graphic).
   * By the Havel-Hakimi equivalence theorem, the original sequence:
     $$\mathbf{S = (5, 4, 3, 3, 2, 2, 1) \text{ is GRAPHIC.} \quad \blacksquare}$$

---

### Question 9: Graph Isomorphism Proof & Preserved Invariants
**Exam Question Language**:
> *"Determine whether the 6-cycle $C_6$ and the disjoint union of two triangles $2C_3$ are isomorphic. State at least three preserved invariants that match and one that fails."*

**Topic & Trigger Words**: *"determine whether isomorphic"*, *"preserved invariants"*, *"C6"*, *"2C3"*.

#### Model Solution to Write in Exam:
1. **Definitions**:
   * $C_6$: Single simple cycle on 6 vertices: $V(C_6) = \{1, 2, 3, 4, 5, 6\}$, $E(C_6) = \{(1,2), (2,3), (3,4), (4,5), (5,6), (6,1)\}$.
   * $2C_3$: Disjoint union of two 3-cycles: $G = H_1 \cup H_2$, where $H_1 \cong C_3$ on $\{a, b, c\}$ and $H_2 \cong C_3$ on $\{d, e, f\}$.
2. **Matching Graph Invariants (Necessary Conditions)**:
   * **Invariant 1 (Order $|V|$)**: $|V(C_6)| = 6$, $|V(2C_3)| = 3 + 3 = 6$ (Match $\checkmark$).
   * **Invariant 2 (Size $|E|$)**: $|E(C_6)| = 6$, $|E(2C_3)| = 3 + 3 = 6$ (Match $\checkmark$).
   * **Invariant 3 (Degree Sequence)**:
     * In $C_6$, every vertex has degree 2 $\implies (2, 2, 2, 2, 2, 2)$.
     * In $2C_3$, every vertex has degree 2 $\implies (2, 2, 2, 2, 2, 2)$ (Match $\checkmark$).
   * **Invariant 4 (Regularity)**: Both graphs are 2-regular (Match $\checkmark$).
3. **Failing Invariants (Rigorous Non-Isomorphism Proof)**:
   * **Failing Invariant 1 (Number of Connected Components $c(G)$)**:
     * $C_6$ is a **connected** graph $\implies c(C_6) = \mathbf{1}$.
     * $2C_3$ consists of two disconnected components $\implies c(2C_3) = \mathbf{2}$.
     * Since graph isomorphism preserves the number of connected components ($c(G_1) = c(G_2)$), $C_6 \not\cong 2C_3$.
   * **Failing Invariant 2 (Cycle Length Spectrum / 3-Cycles)**:
     * $2C_3$ contains **two** cycles of length 3 ($C_3$).
     * $C_6$ is a bipartite graph ($C_6 \cong K_{3,3} - \text{edges}$) containing **zero** cycles of length 3 (only even cycles).
4. **Conclusion**:
   $$\mathbf{C_6 \not\cong 2C_3 \quad (\text{Non-Isomorphic}).}$$

---

### Question 10: Self-Complementary Graph Order Proof
**Exam Question Language**:
> *"Define a self-complementary graph. Prove that if a simple graph $G$ with $n$ vertices is self-complementary ($G \cong \overline{G}$), then $n \equiv 0 \pmod 4$ or $n \equiv 1 \pmod 4$."*

**Topic & Trigger Words**: *"self-complementary graph"*, *"n = 4k or 4k+1"*, *"n = 0 or 1 mod 4"*.

#### Model Solution to Write in Exam:
1. **Definition**: A simple graph $G = (V, E)$ is **self-complementary** if it is isomorphic to its complement graph $\overline{G} = (V, \overline{E})$, denoted $G \cong \overline{G}$.
2. **Edge Count Derivation**:
   * In the complete graph $K_n$, the total number of edges is:
     $$|E(K_n)| = \binom{n}{2} = \frac{n(n - 1)}{2}$$
   * By definition of the complement graph:
     $$E(G) \cup E(\overline{G}) = E(K_n) \quad \text{and} \quad E(G) \cap E(\overline{G}) = \emptyset$$
     $$|E(G)| + |E(\overline{G})| = \frac{n(n - 1)}{2}$$
   * Since $G \cong \overline{G}$, isomorphism preserves the size of the graph: $|E(G)| = |E(\overline{G})|$.
   * Substituting:
     $$2|E(G)| = \frac{n(n - 1)}{2} \implies \mathbf{|E(G)| = \frac{n(n - 1)}{4}}$$
3. **Divisibility Condition**:
   * Because the number of edges $|E(G)|$ must be a non-negative **integer**:
     $$4 \mid n(n - 1)$$
   * The terms $n$ and $n - 1$ are consecutive integers, so exactly one of them is even and the other is odd.
   * Therefore, the factor of 4 must divide the even term completely:
     * **Case 1**: $4 \mid n \implies \mathbf{n \equiv 0 \pmod 4}$ (e.g., $n = 4, 8, 12, \dots$).
     * **Case 2**: $4 \mid (n - 1) \implies \mathbf{n \equiv 1 \pmod 4}$ (e.g., $n = 5, 9, 13, \dots$).
4. **Examples**:
   * $n = 4$: The 4-vertex path $P_4$ has $|E| = 4(3)/4 = 3$ edges, and $\overline{P_4} \cong P_4$.
   * $n = 5$: The 5-cycle $C_5$ has $|E| = 5(4)/4 = 5$ edges, and $\overline{C_5} \cong C_5$. $\blacksquare$

---

### Question 11: Bipartite Graph Verification (2-Coloring Algorithm)
**Exam Question Language**:
> *"State Kőnig's theorem for bipartite graphs. Using the 2-coloring algorithm, test whether the graph with edge set $E = \{(1,2), (2,3), (3,4), (4,5), (5,1), (1,3)\}$ is bipartite."*

**Topic & Trigger Words**: *"Kőnig's theorem"*, *"bipartite"*, *"2-coloring"*.

#### Model Solution to Write in Exam:
1. **Kőnig's Theorem**:
   > A graph $G$ is **bipartite** if and only if it contains **NO odd cycles** (every cycle in $G$ has even length $\ge 4$). Equivalently, $G$ is 2-colorable.
2. **2-Coloring Breadth-First Search (BFS) Algorithm**:
   * Assign Color 1 (**RED**) and Color 2 (**BLUE**).
   * **Step 1**: Color vertex $1 \to$ **RED**.
   * **Step 2**: Neighbors of vertex $1$ in $E$ are $\{2, 5, 3\}$:
     * Edge $(1, 2) \implies$ Color vertex $2 \to$ **BLUE**.
     * Edge $(1, 5) \implies$ Color vertex $5 \to$ **BLUE**.
     * Edge $(1, 3) \implies$ Color vertex $3 \to$ **BLUE**.
   * **Step 3**: Examine edges between neighbors:
     * Check edge $(2, 3) \in E$:
       * Vertex $2$ has color **BLUE**.
       * Vertex $3$ has color **BLUE**.
       * Both endpoints of edge $(2, 3)$ share the **SAME color (BLUE)**!
3. **Chromatic Conflict Analysis**:
   * Vertices $\{1, 2, 3\}$ form a cycle of length 3 ($C_3$, a triangle):
     $$(1, 2) \in E, \quad (2, 3) \in E, \quad (3, 1) \in E$$
   * Because $C_3$ is an odd cycle ($k = 3$), 2-coloring is impossible.
4. **Conclusion**:
   $$\mathbf{\text{The graph is NOT bipartite because it contains an odd cycle } (1-2-3-1).}$$

---

### Question 12: Dijkstra's Shortest Path Algorithm on Directed Graphs
**Exam Question Language**:
> *"Apply Dijkstra's algorithm to compute the shortest path from source vertex $S$ to all other vertices in the directed graph with vertices $\{S, A, B, C, D, E\}$ and edge weights: $(S, A)=2, (S, C)=5, (A, B)=3, (A, C)=2, (C, B)=1, (B, D)=4, (C, D)=2, (C, E)=7, (D, E)=1$. Show the complete iteration table."*

**Topic & Trigger Words**: *"Dijkstra's algorithm"*, *"shortest path"*, *"directed graph"*, *"iteration table"*.

#### Model Solution to Write in Exam:
1. **Initialization**:
   * Set of permanently settled vertices $S_V = \emptyset$.
   * Tentative distance vector: $d[S] = 0$, $d[v] = \infty$ for $v \ne S$.
   * Predecessor vector: $\pi[v] = \text{NIL}$.
2. **Step-by-Step Iteration Table**:

| Step $k$ | Selected Vertex $u^* = \arg\min_{v \notin S_V} d[v]$ | $d[u^*]$ | Edge Relaxation Updates: $d[v] = \min(d[v], d[u^*] + w(u^*, v))$ | Settled Set $S_V$ |
| :---: | :---: | :---: | :--- | :--- |
| **1** | **$S$** | $0$ | $d[A] = \min(\infty, 0+2) = \mathbf{2} \; (S)$<br>$d[C] = \min(\infty, 0+5) = \mathbf{5} \; (S)$ | $\{S\}$ |
| **2** | **$A$** | $2$ | $d[B] = \min(\infty, 2+3) = \mathbf{5} \; (A)$<br>$d[C] = \min(5, 2+2) = \mathbf{4} \; (A)$ [Updated!] | $\{S, A\}$ |
| **3** | **$C$** | $4$ | $d[B] = \min(5, 4+1) = \mathbf{5}$ [Unchanged]<br>$d[D] = \min(\infty, 4+2) = \mathbf{6} \; (C)$<br>$d[E] = \min(\infty, 4+7) = \mathbf{11} \; (C)$ | $\{S, A, C\}$ |
| **4** | **$B$** | $5$ | $d[D] = \min(6, 5+4) = \mathbf{6}$ [Unchanged] | $\{S, A, C, B\}$ |
| **5** | **$D$** | $6$ | $d[E] = \min(11, 6+1) = \mathbf{7} \; (D)$ [Updated!] | $\{S, A, C, B, D\}$ |
| **6** | **$E$** | $7$ | No outgoing edges to relax. | $\{S, A, C, B, D, E\}$ |

3. **Final Shortest Distance & Path Summary**:

| Destination | Shortest Distance $d[v]$ | Predecessor $\pi[v]$ | Reconstructed Shortest Path |
| :---: | :---: | :---: | :--- |
| **$S$** | **0** | — | $S$ |
| **$A$** | **2** | $S$ | $S \to A$ |
| **$B$** | **5** | $A$ | $S \to A \to B$ |
| **$C$** | **4** | $A$ | $S \to A \to C$ |
| **$D$** | **6** | $C$ | $S \to A \to C \to D$ |
| **$E$** | **7** | $D$ | $S \to A \to C \to D \to E$ |

### Question 13: Graph Matrix Representations (Adjacency Matrix, Incidence Matrix & Path Counting)
**Exam Question Language**:
> *"Write down the adjacency matrix $A(G)$ and incidence matrix $M(G)$ for the graph with vertices $\{1, 2, 3, 4\}$ and edges $e_1=(1,2), e_2=(2,3), e_3=(3,4), e_4=(4,1), e_5=(1,3)$. Using matrix multiplication, determine the number of distinct walks of length 2 and length 3 between vertex 1 and vertex 3."*

**Topic & Trigger Words**: *"adjacency matrix"*, *"incidence matrix"*, *"number of walks of length k"*, *"A^k"*.

#### Model Solution to Write in Exam:
1. **Adjacency Matrix $A(G)$**:
   * Order $n = 4$. $A_{ij} = 1$ if $(i, j) \in E$, else $0$:
     $$A = \begin{bmatrix}
     0 & 1 & 1 & 1 \\
     1 & 0 & 1 & 0 \\
     1 & 1 & 0 & 1 \\
     1 & 0 & 1 & 0
     \end{bmatrix}$$
2. **Incidence Matrix $M(G)$**:
   * Rows correspond to vertices $\{1, 2, 3, 4\}$, columns to edges $\{e_1, e_2, e_3, e_4, e_5\}$.
   * $M_{iv} = 1$ if vertex $i$ is an endpoint of edge $e_j$:
     $$M = \begin{bmatrix}
     1 & 0 & 0 & 1 & 1 \\
     1 & 1 & 0 & 0 & 0 \\
     0 & 1 & 1 & 0 & 1 \\
     0 & 0 & 1 & 1 & 0
     \end{bmatrix}$$
   * *Property Check*: Every column sum equals strictly $2$ (each edge touches 2 vertices $\checkmark$).
3. **Walk Counting Theorem**:
   > The number of distinct walks of length $k$ between vertex $i$ and vertex $j$ in graph $G$ equals the $(i, j)$-th entry of the matrix power $A^k$, denoted $(A^k)_{ij}$.
4. **Compute $A^2$ for Walks of Length 2**:
   * Row 1 of $A$: $[0, 1, 1, 1]$. Column 3 of $A$: $[1, 1, 0, 1]^T$.
     $$(A^2)_{1, 3} = (0)(1) + (1)(1) + (1)(0) + (1)(1) = 0 + 1 + 0 + 1 = \mathbf{2}$$
   * The 2 distinct walks of length 2 between 1 and 3 are:
     1. $1 \to 2 \to 3$
     2. $1 \to 4 \to 3$
5. **Compute $A^3$ for Walks of Length 3**:
   * Compute full Row 1 of $A^2$:
     * $(A^2)_{1,1} = 0+1+1+1 = 3$
     * $(A^2)_{1,2} = 0+0+1+0 = 1$
     * $(A^2)_{1,3} = 2$
     * $(A^2)_{1,4} = 0+0+1+0 = 1$
     * $\text{Row}_1(A^2) = [3, 1, 2, 1]$
   * Multiplying with Column 3 of $A$: $[1, 1, 0, 1]^T$:
     $$(A^3)_{1, 3} = (3)(1) + (1)(1) + (2)(0) + (1)(1) = 3 + 1 + 0 + 1 = \mathbf{5}$$
   * $\mathbf{\text{Conclusion: There are } 2 \text{ walks of length 2 and } 5 \text{ walks of length 3 between vertex 1 and vertex 3.}}$

---

### Question 14: Regular Graphs & Non-Isomorphic 3-Regular Graphs
**Exam Question Language**:
> *"Find all distinct, non-isomorphic 3-regular (cubic) simple graphs on 6 vertices. Prove why they are pairwise non-isomorphic."*

**Topic & Trigger Words**: *"3-regular"*, *"cubic graphs"*, *"non-isomorphic"*, *"6 vertices"*.

#### Model Solution to Write in Exam:
1. **Size Derivation by Handshaking**:
   * Order $n = 6$, degree of each vertex $r = 3$.
   * $|E| = \frac{n \cdot r}{2} = \frac{6 \times 3}{2} = \mathbf{9}$ edges.
2. **Catalog of the 3 Non-Isomorphic Graphs**:
   There are exactly **three** pairwise non-isomorphic 3-regular graphs on 6 vertices:
   * **Graph 1 ($G_1 = K_{3,3}$ - Complete Bipartite Utility Graph)**:
     * Partition $V_1 = \{1, 2, 3\}$, $V_2 = \{4, 5, 6\}$. Every vertex in $V_1$ connects to all in $V_2$.
     * **Bipartite**: Contains **zero** 3-cycles ($C_3$).
   * **Graph 2 ($G_2 = Y_3$ - Triangular Prism Graph)**:
     * Formed by two disjoint 3-cycles $\{1, 2, 3\}$ and $\{4, 5, 6\}$ connected by matching edges $\{(1,4), (2,5), (3,6)\}$.
     * **Non-Bipartite**: Contains **two** 3-cycles ($C_3$).
   * **Graph 3 ($G_3 = 2K_4$ - Disjoint Union)**:
     * Note: If $n = 6$, $2K_4$ has $4+4=8$ vertices, so for 6 vertices, $G_3$ is the **Möbius Ladder / Complete Graph with 3 independent edges removed ($K_6 - 3K_2$)** or the **Octahedral dual / $K_3 \square K_2$**.
     * More precisely, the 3rd graph has **four** triangles $C_3$.
3. **Non-Isomorphism Proof via Cycle Invariant**:
   * Count of 3-cycles ($C_3$ triangles):
     * $G_1$ has **0** triangles (it is bipartite).
     * $G_2$ has **2** triangles.
     * $G_3$ has **4** triangles.
   * Since graph isomorphism strictly preserves the number of cycles of length 3 ($C_3$), no two of these graphs can be isomorphic:
     $$\mathbf{G_1 \not\cong G_2 \not\cong G_3 \quad (\text{Pairwise Non-Isomorphic}). \quad \blacksquare}$$

---

### Question 15: Sublattice Closure Verification
**Exam Question Language**:
> *"Let $L = (D_{30}, \mid)$. Determine whether the following subsets are sublattices of $L$: (a) $S_1 = \{1, 2, 3, 6\}$, (b) $S_2 = \{1, 2, 5, 10\}$, (c) $S_3 = \{1, 2, 5\}$."*

**Topic & Trigger Words**: *"sublattice"*, *"closed under meet and join"*, *"D30"*.

#### Model Solution to Write in Exam:
1. **Definition of Sublattice**:
   > A subset $S \subseteq L$ of a lattice $(L, \vee, \wedge)$ is a **sublattice** if and only if $S$ is closed under the same lattice operations $\vee$ and $\wedge$:
   > $$\forall a, b \in S \implies (a \wedge b) \in S \quad \text{and} \quad (a \vee b) \in S$$
   > For $(D_{30}, \mid)$, $a \wedge b = \gcd(a, b)$ and $a \vee b = \text{lcm}(a, b)$.
2. **Analysis for $S_1 = \{1, 2, 3, 6\}$**:
   * For all pairs in $S_1$:
     * $\gcd(2, 3) = 1 \in S_1$, $\text{lcm}(2, 3) = 6 \in S_1$.
     * All divisors of 6 are in $S_1$.
     * Hence $S_1$ is closed under $\gcd$ and $\text{lcm}$.
   * $\mathbf{S_1 \text{ IS a sublattice of } D_{30}.}$
3. **Analysis for $S_2 = \{1, 2, 5, 10\}$**:
   * For all pairs: $\gcd(2, 5) = 1 \in S_2$, $\text{lcm}(2, 5) = 10 \in S_2$.
   * Closed under $\gcd$ and $\text{lcm}$.
   * $\mathbf{S_2 \text{ IS a sublattice of } D_{30}.}$
4. **Analysis for $S_3 = \{1, 2, 5\}$**:
   * Test pair $\{2, 5\} \subseteq S_3$:
     $$\text{lcm}(2, 5) = 10$$
   * But **$10 \notin S_3$**!
   * $S_3$ is NOT closed under the join operation $\vee$.
   * $\mathbf{S_3 \text{ is NOT a sublattice of } D_{30}.}$

---

### Question 16: Modular Lattice Property & Proof
**Exam Question Language**:
> *"Define a modular lattice. Prove that every distributive lattice is modular. Give an example of a lattice that is modular but not distributive."*

**Topic & Trigger Words**: *"modular lattice"*, *"every distributive lattice is modular"*, *"modular not distributive"*.

#### Model Solution to Write in Exam:
1. **Definition**: A lattice $(L, \vee, \wedge)$ is **modular** if for all $a, b, c \in L$ with $a \le c$:
   $$a \vee (b \wedge c) = (a \vee b) \wedge c$$
2. **Proof: Distributive $\implies$ Modular**:
   * Assume $L$ is a distributive lattice. Then meet distributes over join:
     $$(a \vee b) \wedge c = (a \wedge c) \vee (b \wedge c) \quad \forall a, b, c \in L$$
   * Now assume the hypothesis $a \le c$.
   * By the Bridge Theorem of posets, $a \le c \iff a \wedge c = a$.
   * Substitute $a \wedge c = a$ into the distributive expression:
     $$(a \vee b) \wedge c = \mathbf{a} \vee (b \wedge c)$$
   * This is precisely the modular law.
   * Therefore, **every distributive lattice is modular**. $\blacksquare$
3. **Counterexample: Modular but Non-Distributive**:
   * The **Diamond Lattice $M_3$** (5 elements: $0, a, b, c, 1$) is **modular**, but it is **NOT distributive** (as proven in Question 4: $a \wedge (b \vee c) = a \ne 0 = (a \wedge b) \vee (a \wedge c)$).

---

### Question 17: Lexicographical Ordering on $\mathbb{R}^2$
**Exam Question Language**:
> *"Define the lexicographical (dictionary) relation $\le_{\text{lex}}$ on $\mathbb{R}^2$. Prove that $(\mathbb{R}^2, \le_{\text{lex}})$ is a partially ordered set (poset). Is it totally ordered?"*

**Topic & Trigger Words**: *"lexicographical order"*, *"R^2"*, *"poset proof"*, *"total order"*.

#### Model Solution to Write in Exam:
1. **Formal Definition**:
   For $(x_1, y_1), (x_2, y_2) \in \mathbb{R}^2$:
   $$(x_1, y_1) \le_{\text{lex}} (x_2, y_2) \iff (x_1 < x_2) \quad \text{or} \quad (x_1 = x_2 \text{ and } y_1 \le y_2)$$
2. **Poset Proof (3 Axioms)**:
   * **Reflexivity**: For any $(x, y) \in \mathbb{R}^2$, since $x = x$ and $y \le y$ in $(\mathbb{R}, \le)$, $(x, y) \le_{\text{lex}} (x, y)$ holds $\checkmark$.
   * **Antisymmetry**: Suppose $(x_1, y_1) \le_{\text{lex}} (x_2, y_2)$ and $(x_2, y_2) \le_{\text{lex}} (x_1, y_1)$:
     * If $x_1 < x_2$, then $x_2 \not< x_1$ and $x_2 \ne x_1$, contradicting $(x_2, y_2) \le_{\text{lex}} (x_1, y_1)$.
     * Hence we must have $x_1 = x_2$.
     * Then $y_1 \le y_2$ and $y_2 \le y_1 \implies y_1 = y_2$ by antisymmetry of $\le$ on $\mathbb{R}$.
     * Therefore $(x_1, y_1) = (x_2, y_2)$ $\checkmark$.
   * **Transitivity**: Suppose $(x_1, y_1) \le_{\text{lex}} (x_2, y_2)$ and $(x_2, y_2) \le_{\text{lex}} (x_3, y_3)$:
     * If $x_1 < x_2$ or $x_2 < x_3$, then $x_1 < x_3 \implies (x_1, y_1) \le_{\text{lex}} (x_3, y_3)$.
     * If $x_1 = x_2 = x_3$, then $y_1 \le y_2 \le y_3 \implies y_1 \le y_3 \implies (x_1, y_1) \le_{\text{lex}} (x_3, y_3)$ $\checkmark$.
3. **Total Ordering**:
   * For any two pairs $(x_1, y_1)$ and $(x_2, y_2)$:
     * If $x_1 \ne x_2$, either $x_1 < x_2$ or $x_2 < x_1$.
     * If $x_1 = x_2$, either $y_1 \le y_2$ or $y_2 \le y_1$.
   * Every pair is comparable. Therefore, $(\mathbb{R}^2, \le_{\text{lex}})$ is a **totally ordered set (chain)**. $\blacksquare$

---

### Question 18: Relation Composition & Inverse Equality Proof
**Exam Question Language**:
> *"Let $R \subseteq A \times B$ and $S \subseteq B \times C$ be two binary relations. Prove formally that $(S \circ R)^{-1} = R^{-1} \circ S^{-1}$."*

**Topic & Trigger Words**: *"relation composition"*, *"inverse relation"*, *"(S o R)^-1 = R^-1 o S^-1"*.

#### Model Solution to Write in Exam:
1. **Definitions**:
   * $(a, c) \in S \circ R \iff \exists b \in B \text{ such that } (a, b) \in R \text{ and } (b, c) \in S$.
   * $(x, y) \in T^{-1} \iff (y, x) \in T$.
2. **Double Inclusion Proof**:
   * **Part 1: Show $(S \circ R)^{-1} \subseteq R^{-1} \circ S^{-1}$**:
     1. Let $(c, a) \in (S \circ R)^{-1}$ be an arbitrary element.
     2. By definition of inverse, $(a, c) \in S \circ R$.
     3. By definition of composition, $\exists b \in B$ such that $(a, b) \in R$ and $(b, c) \in S$.
     4. Applying inverse definitions:
        * $(a, b) \in R \implies (b, a) \in R^{-1}$.
        * $(b, c) \in S \implies (c, b) \in S^{-1}$.
     5. Since $(c, b) \in S^{-1}$ and $(b, a) \in R^{-1}$, by definition of composition:
        $$(c, a) \in R^{-1} \circ S^{-1}$$
     6. Hence, $(S \circ R)^{-1} \subseteq R^{-1} \circ S^{-1}$.
   * **Part 2: Show $R^{-1} \circ S^{-1} \subseteq (S \circ R)^{-1}$**:
     1. Let $(c, a) \in R^{-1} \circ S^{-1}$ be an arbitrary element.
     2. By definition of composition, $\exists b \in B$ such that $(c, b) \in S^{-1}$ and $(b, a) \in R^{-1}$.
     3. Applying inverse definitions:
        * $(c, b) \in S^{-1} \implies (b, c) \in S$.
        * $(b, a) \in R^{-1} \implies (a, b) \in R$.
     4. Rearranging: $(a, b) \in R$ and $(b, c) \in S \implies (a, c) \in S \circ R$.
     5. By definition of inverse: $(c, a) \in (S \circ R)^{-1}$.
     6. Hence, $R^{-1} \circ S^{-1} \subseteq (S \circ R)^{-1}$.
3. **Conclusion**:
   $$\mathbf{(S \circ R)^{-1} = R^{-1} \circ S^{-1} \quad \blacksquare}$$

---

# PART IV: COMMON EXAM TRAPS & PROFESSOR MARKING CRITERIA

### ⚠️ Where Students Lose Marks (Dr. Suresh Dara's Evaluation Style):
1. **Havel-Hakimi Sorting**:
   * *Common Mistake*: Forgetting to **re-sort** the sequence in descending order after each subtraction step. If you subtract and do not re-sort before deleting the next term, the algorithm will yield false conclusions and marks will be halved.
2. **Isomorphism Proofs**:
   * *Common Mistake*: Merely stating "both have 6 vertices and 6 edges and are 2-regular, so isomorphic" or stating "degree sequence matches". Matching degree sequence is **necessary, NOT sufficient**! If isomorphic, you **MUST** write the explicit bijection mapping $f(u_i) = v_j$. If non-isomorphic, you must name the specific failing invariant.
3. **Square-Free Boolean Algebra Proofs**:
   * *Common Mistake*: Claiming that $(D_n, \mid)$ is a Boolean algebra for any divisor lattice. Remember: if $n$ has any repeated prime factor (like $4 = 2^2$, $12 = 2^2 \cdot 3$, $18 = 2 \cdot 3^2$, $36 = 2^2 \cdot 3^2$), it is **NOT** a Boolean algebra because prime powers lack complements.
4. **Bipartite Odd Cycle Justification**:
   * *Common Mistake*: Writing "graph looks bipartite" without doing the 2-coloring. You must show the 2-coloring assignment and explicitly name the chromatic conflict edge or the odd cycle vertices.
5. **Dijkstra Predecessor Tracking**:
   * *Common Mistake*: Writing only the final numerical distances without the predecessor labels or the iteration table. Full marks require the table showing step $k$, settled vertex $u^*$, and relaxed distance updates.
