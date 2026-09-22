# 🎯 MAT2002: CAT-2 Question-Language Decoder & Master Universal Solver
## Module 3 (Lattices & Boolean Algebra) & Module 4 (Graphs & Matrix Representations)
> **Open-Book Exam Hall Strategy**: When you receive your question paper, do not guess or read textbook theory.
> 1. **Identify** the question pattern in the **Rapid Topic Selection Matrix (Part I)**.
> 2. **Turn** to the matching **Universal Algorithmic Blueprint in Part II (Solvers 1 to 10)**.
> 3. **Plug in** your exam paper's specific numbers/variables into the pre-formatted tables, cite the required theorems/axioms, and write the full-credit concluding sentences.
> 4. For exact worked examples, refer to the **Questionnaire Banks (Parts III & IV)** or the **Actual September 2026 Paper** in Section 2.

---

# ⏱️ 30-SECOND EXAM-HALL MASTER ACTION PROTOCOL

When the invigilator says "You may begin writing":
1. **Locate Question Type**: Skim the first 5 words of each exam question. Compare with the **Question-Language Matrix (Part I)** below.
2. **Match the Universal Blueprint**:
   * *Proving an equation with meets ($\wedge$) and joins ($\vee$)* $\implies$ Go to **Blueprint 1** (Lattice Identity Engine).
   * *Constructing truth table / finding PDNF / PCNF from verbal conditions* $\implies$ Go to **Blueprint 2** (Boolean Normal Forms Engine).
   * *Divisor posets $(D_n, \mid)$, zero/unit elements, complements, or Boolean algebra check* $\implies$ Go to **Blueprint 3** (Divisor Lattice Evaluator).
   * *Degree partition equation (e.g. $|V_1| = 2|V_2|$), edge count, graph feasibility* $\implies$ Go to **Blueprint 4** (Handshaking Degree Solver).
   * *Testing if two graphs $G_1$ and $G_2$ are isomorphic* $\implies$ Go to **Blueprint 5** (2-Graph Isomorphism Decision Engine).
   * *Testing if a degree sequence is graphic (e.g. $(5, 4, 3, 3, 2, 2, 1)$)* $\implies$ Go to **Blueprint 6** (Havel-Hakimi Table Generator).
   * *Finding all-pairs shortest paths on directed graph (matrices $D^{(0)} \dots D^{(n)}$)* $\implies$ Go to **Blueprint 7** (Floyd-Warshall Matrix Blueprint).
   * *Finding single-source shortest path from vertex $S$* $\implies$ Go to **Blueprint 8** (Dijkstra Shortest Path Engine).
   * *Testing if graph is bipartite / finding odd cycle* $\implies$ Go to **Blueprint 9** (Bipartite 2-Coloring Engine).
   * *Planar graphs, face count, $v - e + f = 2$, or non-planarity ($K_5, K_{3,3}$)* $\implies$ Go to **Blueprint 10** (Planarity & Polyhedral Formulas).
3. **Copy-Paste Execution**: Open the corresponding blueprint, write down the formula, copy the table column structure, perform the simple arithmetic, and write the standard closing proof sentence.

---

# PART I: QUESTION-LANGUAGE TO TOPIC SELECTION MATRIX

Use this rapid lookup table during the exam to convert the exam question prompt into the exact topic, test condition, and universal blueprint:

| Exact Question Language / Phrasing | Syllabus Topic | Instant Decision Rule / Condition | Direct Exam Action & Blueprint |
| :--- | :--- | :--- | :--- |
| *"Prove that in a distributive lattice: $x = y$..."* / *"Show that $(a \wedge b) \vee (b \wedge c) \vee (c \wedge a) = \dots$"* | **Distributive Lattice Identities** (Mod 3) | Distributive laws hold both ways. Group terms, factor out common variables, apply absorption $u \wedge (u \vee v) = u$. | Go to **Blueprint 1** (Lattice Identity Engine). Cite the 5 governing axioms at each step. |
| *"Prove that complement of an element in a distributive lattice is unique..."* / *"Prove cancellation law..."* | **Lattice Theorems** (Mod 3) | If $a \wedge b = 0, a \vee b = 1$ and $a \wedge c = 0, a \vee c = 1$, then $b = b \wedge (a \vee c) = \dots = c$. | Go to **Blueprint 1 (Templates 1.2 & 1.3)**. Copy the algebraic proof word-for-word. |
| *"Construct truth table and find PDNF and PCNF of $f$ which takes value 1 if..."* | **Boolean Function Normal Forms** (Mod 3) | $\text{PDNF} = \sum m(\text{rows where } f=1)$.<br>$\text{PCNF} = \prod M(\text{rows where } f=0)$. | Go to **Blueprint 2** (Boolean Normal Forms Engine). Fill the universal 8-row table. |
| *"Find zero and unit elements of $(D_n, \mid)$..."* / *"Is $(D_n, \mid)$ a complemented lattice / Boolean algebra?"* | **Divisor Posets & Lattices** (Mod 3) | Zero $= 1$, Unit $= n$. Complemented $\iff n$ is **square-free** (no repeated prime factors). | Go to **Blueprint 3** (Divisor Lattice Evaluator). Read prime factors, find complements or state counterexample $p_i$. |
| *"A graph has vertices partitioned into $V_1, V_2$ with degrees $d_1, d_2$ and $m$ edges. Can it exist?"* | **Handshaking Lemma & Degree Partition** (Mod 4) | Equate $2|E| = \sum |V_i| d_i$. Solve for $k$. Check: (1) $k \in \mathbb{Z}^+$, (2) odd vertices even, (3) $\Delta \le |V|-1$. | Go to **Blueprint 4** (Degree Partition Solver). Run the 4-Gate Impossibility Test. |
| *"Determine whether graphs $G_1$ and $G_2$ are isomorphic..."* | **Graph Isomorphism** (Mod 4) | If non-isomorphic: find 1 failing invariant (triangles, components). If isomorphic: write explicit bijection $f(u_i) = v_j$. | Go to **Blueprint 5** (2-Graph Isomorphism Engine). Draw 5-invariant table, then write bijection. |
| *"Determine whether the degree sequence is graphic..."* / *"Apply Havel-Hakimi theorem..."* | **Havel-Hakimi Algorithm** (Mod 4) | Delete $d_1$, subtract 1 from next $d_1$ elements, re-sort descending. All zeros $\implies$ graphic. | Go to **Blueprint 6** (Havel-Hakimi Table Generator). Set up standard 4-column reduction table. |
| *"Find all-pairs shortest paths using Floyd-Warshall algorithm..."* | **Floyd-Warshall Algorithm** (Mod 4) | $d_{ij}^{(k)} = \min(d_{ij}^{(k-1)}, d_{ik}^{(k-1)} + d_{kj}^{(k-1)})$. Row $k$ and Col $k$ never change at step $k$. | Go to **Blueprint 7** (Floyd-Warshall Matrix Blueprint). Fill matrices $D^{(0)} \dots D^{(4)}$ with zero error. |
| *"Find shortest path from vertex $S$ to all other vertices..."* | **Dijkstra's Algorithm** (Mod 4) | Greedy relaxation of tentative labels $d[v] = \min(d[v], d[u^*] + w(u^*, v))$. | Go to **Blueprint 8** (Dijkstra Shortest Path Engine). Draw standard iteration table. |
| *"Determine whether graph $G$ is bipartite..."* / *"Check if $G$ has an odd cycle..."* | **Bipartite Graphs & Kőnig's Theorem** (Mod 4) | Bipartite $\iff$ 2-colorable $\iff$ contains **NO odd cycles**. | Go to **Blueprint 9** (Bipartite 2-Coloring Engine). Execute BFS 2-coloring (Red/Blue). |
| *"Find number of faces in a connected planar graph with $v$ vertices and $e$ edges..."* | **Euler's Formula & Planarity** (Mod 4) | $v - e + f = 2 \implies f = e - v + 2$. Planar simple graph has $e \le 3v - 6$. | Go to **Blueprint 10** (Planarity & Polyhedral Formulas). |
| *"Prove that a simple graph is self-complementary only if $n \equiv 0, 1 \pmod 4$..."* | **Self-Complementary Graphs** (Mod 4) | $|E(G)| = \frac{n(n-1)}{4} \in \mathbb{Z}^+ \implies 4 \mid n(n-1) \implies n \equiv 0, 1 \pmod 4$. | Refer to **Section 1 Q10** or **Section 7 (Module 4 HOTS)**. Copy 4-line proof. |
| *"Prove that in any group of $n \ge 2$ people, at least two have the same number of friends..."* | **Pigeonhole Principle & Handshaking** (Mod 4) | Degrees in simple graph cannot contain both $0$ and $n-1$. Degree values map to $\le n-1$ pigeonholes for $n$ vertices. | Refer to **Section 1 Q15** or **Section 7 (Module 4 HOTS)**. Copy PHP proof. |

---
# PART II: 10 UNIVERSAL COPY-PASTE ALGORITHMIC BLUEPRINTS (PARAMETRIC SOLVERS)

---

## 🏛️ BLUEPRINT 1: Distributive & Boolean Lattice Identity Proof Engine

### Applicable Question Archetypes:
* *"Prove that in a distributive lattice $L$, $(a \wedge b) \vee (b \wedge c) \vee (c \wedge a) = (a \vee b) \wedge (b \vee c) \wedge (c \vee a)$."*
* *"Prove that the complement of an element in a distributive lattice, if it exists, is unique."*
* *"Prove the Cancellation Laws: $a \wedge x = a \wedge y$ and $a \vee x = a \vee y \implies x = y$."*
* *"State and prove De Morgan's laws in a Boolean lattice."*
* *"Prove that every distributive lattice is modular: $a \le c \implies a \vee (b \wedge c) = (a \vee b) \wedge c$."*
* *"Prove the Isotonicity property: $a \le b \implies a \wedge c \le b \wedge c$ and $a \vee c \le b \vee c$."*

### The 5 Foundational Lattice Laws (Write this first to secure 2 marks):
In any lattice $(L, \wedge, \vee)$, the following axioms hold identically $\forall u, v, w \in L$:
1. **Idempotent Laws**: $u \wedge u = u$ and $u \vee u = u$.
2. **Commutative Laws**: $u \wedge v = v \wedge u$ and $u \vee v = v \vee u$.
3. **Associative Laws**: $(u \wedge v) \wedge w = u \wedge (v \wedge w)$ and $(u \vee v) \vee w = u \vee (v \vee w)$.
4. **Absorption Laws**: $u \wedge (u \vee v) = u$ and $u \vee (u \wedge v) = u$.
5. **Distributive Laws** (in a Distributive Lattice):
   * *Meet over Join*: $u \wedge (v \vee w) = (u \wedge v) \vee (u \wedge w)$
   * *Join over Meet*: $u \vee (v \wedge w) = (u \vee v) \wedge (u \vee w)$
6. **Bridge Theorem**: $u \le v \iff u \wedge v = u \iff u \vee v = v$.

---

### Master Template 1.1: Proving the Median Self-Dual Identity
**Goal**: Prove $(a \wedge b) \vee (b \wedge c) \vee (c \wedge a) = (a \vee b) \wedge (b \vee c) \wedge (c \vee a)$.

**Model Solution to Copy into Answer Sheet**:
1. Let the Left-Hand Side be $x = (a \wedge b) \vee (b \wedge c) \vee (c \wedge a)$ and Right-Hand Side be $y = (a \vee b) \wedge (b \vee c) \wedge (c \vee a)$.
2. Consider the first two factors of $y$:
   $$T = (a \vee b) \wedge (b \vee c) = (b \vee a) \wedge (b \vee c) \quad [\text{Commutative Law}]$$
   Applying the **second distributive law** (factoring out $b$):
   $$T = b \vee (a \wedge c)$$
3. Substitute $T$ back into $y$:
   $$y = [b \vee (a \wedge c)] \wedge (c \vee a)$$
4. Apply the **first distributive law** to distribute $\wedge (c \vee a)$ over the join:
   $$y = \Big( b \wedge (c \vee a) \Big) \vee \Big( (a \wedge c) \wedge (c \vee a) \Big)$$
5. Simplify the two bracketed terms separately:
   * **Term 1**: $b \wedge (c \vee a) = (b \wedge c) \vee (b \wedge a) = (a \wedge b) \vee (b \wedge c)$ $[By Distributive & Commutative Laws]$
   * **Term 2**: Let $u = a \wedge c$. Notice that $u \wedge (a \vee c) = u = a \wedge c = c \wedge a$ $[By Absorption Law, since  \wedge c \le a \le a \vee c$]$
6. Recombining:
   $$y = \Big[ (a \wedge b) \vee (b \wedge c) \Big] \vee (c \wedge a) = (a \wedge b) \vee (b \wedge c) \vee (c \wedge a) = x$$
7. $\mathbf{\therefore x = y \quad \forall a, b, c \in L. \quad \blacksquare}$

---

### Master Template 1.2: Uniqueness of Complements in Distributive Lattices
**Theorem**: In a bounded distributive lattice $(L, \wedge, \vee, 0, 1)$, if an element $a$ has a complement, it is **unique**.

**Model Solution to Copy into Answer Sheet**:
1. **Hypothesis**: Let $b$ and $c$ both be complements of $a \in L$. By definition of complement:
   $$a \wedge b = 0, \quad a \vee b = 1$$
   $$a \wedge c = 0, \quad a \vee c = 1$$
2. **Proof that $b = c$**:
   $$\begin{aligned}
   b &= b \wedge 1 & & [\text{Identity of } 1] \\\\
   &= b \wedge (a \vee c) & & [\text{Substitute } 1 = a \vee c] \\\\
   &= (b \wedge a) \vee (b \wedge c) & & [\text{Distributive Law of } \wedge \text{ over } \vee] \\\\
   &= (a \wedge b) \vee (b \wedge c) & & [\text{Commutative Law}] \\\\
   &= 0 \vee (b \wedge c) & & [\text{Substitute } a \wedge b = 0] \\\\
   &= (a \wedge c) \vee (b \wedge c) & & [\text{Substitute } 0 = a \wedge c] \\\\
   &= (a \vee b) \wedge c & & [\text{Distributive Law, factoring out } c] \\\\
   &= 1 \wedge c & & [\text{Substitute } a \vee b = 1] \\\\
   &= c & & [\text{Identity of } 1]
   \end{aligned}$$
3. $\mathbf{\therefore b = c. \text{ The complement of } a \text{ is strictly unique.} \quad \blacksquare}$

---

### Master Template 1.3: Cancellation Law in Distributive Lattices
**Theorem**: If $L$ is a distributive lattice, then $a \wedge x = a \wedge y$ and $a \vee x = a \vee y \implies x = y$.

**Model Solution to Copy into Answer Sheet**:
$$\begin{aligned}
x &= x \wedge (x \vee a) & & [\text{Absorption Law}] \\\\
&= x \wedge (a \vee x) & & [\text{Commutative Law}] \\\\
&= x \wedge (a \vee y) & & [\text{Given: } a \vee x = a \vee y] \\\\
&= (x \wedge a) \vee (x \wedge y) & & [\text{Distributive Law}] \\\\
&= (a \wedge x) \vee (x \wedge y) & & [\text{Commutative Law}] \\\\
&= (a \wedge y) \vee (x \wedge y) & & [\text{Given: } a \wedge x = a \wedge y] \\\\
&= (y \wedge a) \vee (y \wedge x) & & [\text{Commutative Law}] \\\\
&= y \wedge (a \vee x) & & [\text{Distributive Law}] \\\\
&= y \wedge (a \vee y) & & [\text{Given: } a \vee x = a \vee y] \\\\
&= y & & [\text{Absorption Law}]
\end{aligned}$$
$\mathbf{\therefore x = y. \quad \blacksquare}$

---

### Master Template 1.4: De Morgan's Laws in Boolean Lattices
**Theorem**: In any Boolean lattice $(B, \wedge, \vee, ', 0, 1)$, $(a \vee b)' = a' \wedge b'$ and $(a \wedge b)' = a' \vee b'$.

**Model Solution to Copy into Answer Sheet**:
To prove $(a \vee b)' = a' \wedge b'$, we must verify the two complement axioms: (i) $(a \vee b) \vee (a' \wedge b') = 1$, and (ii) $(a \vee b) \wedge (a' \wedge b') = 0$.
1. **Join Condition**:
   $$\begin{aligned}
   (a \vee b) \vee (a' \wedge b') &= \big[ (a \vee b) \vee a' \big] \wedge \big[ (a \vee b) \vee b' \big] & & [\text{Distributive Law}] \\\\
   &= \big[ (a \vee a') \vee b \big] \wedge \big[ a \vee (b \vee b') \big] & & [\text{Associative \\& Commutative}] \\\\
   &= (1 \vee b) \wedge (a \vee 1) = 1 \wedge 1 = 1 & & [\text{Complement Law } a \vee a' = 1]
   \end{aligned}$$
2. **Meet Condition**:
   $$\begin{aligned}
   (a \vee b) \wedge (a' \wedge b') &= \big( a \wedge (a' \wedge b') \big) \vee \big( b \wedge (a' \wedge b') \big) & & [\text{Distributive Law}] \\\\
   &= \big( (a \wedge a') \wedge b' \big) \vee \big( (b \wedge b') \wedge a' \big) & & [\text{Associative \\& Commutative}] \\\\
   &= (0 \wedge b') \vee (0 \wedge a') = 0 \vee 0 = 0 & & [\text{Complement Law } a \wedge a' = 0]
   \end{aligned}$$
By uniqueness of complements in distributive lattices, $\mathbf{(a \vee b)' = a' \wedge b'}$. The dual identity $(a \wedge b)' = a' \vee b'$ follows by lattice duality. $\blacksquare$

---

## ⚡ BLUEPRINT 2: Arbitrary Verbal Boolean Rule $\to$ Truth Table $\to$ PDNF & PCNF Factory

### Applicable Question Archetypes:
* *"Construct the truth table and find the PDNF and PCNF of the Boolean function $f(x, y, z)$ which takes the value 1 if the number of 1s in the tuple $(x, y', z)$ is greater than the number of 0s."*
* *"Find the PDNF and PCNF of the majority voting function $M(x, y, z)$."*
* *"Find the PDNF and PCNF of the parity check function $P(x, y, z)$ (odd/even parity)."*
* *"Find the PDNF and PCNF of the threshold function $T(x, y, z) = 1 \iff x + y + z \ge 2$."*

### Step-by-Step Universal Algorithm:
1. **Set Up Standard 8-Row Binary Ordering**: $000, 001, 010, 011, 100, 101, 110, 111$.
2. **Evaluate Tuple Transformations**:
   * If question specifies tuple $(x, y', z)$, invert $y$ (i.e. $0 \to 1, 1 \to 0$).
   * If question specifies $(x', y, z')$, invert $x$ and $z$.
3. **Count and Evaluate Condition**:
   * *Majority / More 1s than 0s*: In a 3-variable tuple, more 1s than 0s means $\ge 2$ ones (i.e. Count of 1s $\in \\{2, 3\\}$).
   * *Odd Parity*: Count of 1s is 1 or 3.
   * *Even Parity*: Count of 1s is 0 or 2.
   * *Threshold $k$*: Sum of input bits $\ge k$.
4. **Draw the Universal 8-Row Standardized Table**:

| Row $i$ | $x$ | $y$ | $z$ | Evaluated Tuple | Evaluation Condition | $f(x, y, z)$ | Minterm $m_i$ ($f=1$) | Maxterm $M_i$ ($f=0$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | 0 | 0 | 0 | $(t_1, t_2, t_3)$ | True / False | $0$ or $1$ | $x'y'z'$ | $(x + y + z)$ |
| **1** | 0 | 0 | 1 | $(t_1, t_2, t_3)$ | True / False | $0$ or $1$ | $x'y'z$ | $(x + y + z')$ |
| **2** | 0 | 1 | 0 | $(t_1, t_2, t_3)$ | True / False | $0$ or $1$ | $x'yz'$ | $(x + y' + z)$ |
| **3** | 0 | 1 | 1 | $(t_1, t_2, t_3)$ | True / False | $0$ or $1$ | $x'yz$ | $(x + y' + z')$ |
| **4** | 1 | 0 | 0 | $(t_1, t_2, t_3)$ | True / False | $0$ or $1$ | $xy'z'$ | $(x' + y + z)$ |
| **5** | 1 | 0 | 1 | $(t_1, t_2, t_3)$ | True / False | $0$ or $1$ | $xy'z$ | $(x' + y + z')$ |
| **6** | 1 | 1 | 0 | $(t_1, t_2, t_3)$ | True / False | $0$ or $1$ | $xyz'$ | $(x' + y' + z)$ |
| **7** | 1 | 1 | 1 | $(t_1, t_2, t_3)$ | True / False | $0$ or $1$ | $xyz$ | $(x' + y' + z')$ |

5. **Writing Full Marks PDNF & PCNF**:
   * **PDNF (Sum of Minterms)**:
     $$\text{PDNF} = \sum m(i_1, i_2, \dots) = m_{i_1} \vee m_{i_2} \vee \dots$$
     *(Literal rule: $1 \to$ unprimed variable, $0 \to$ primed variable, combined by $\wedge$)*.
   * **PCNF (Product of Maxterms)**:
     $$\text{PCNF} = \prod M(j_1, j_2, \dots) = M_{j_1} \wedge M_{j_2} \wedge \dots$$
     *(Literal rule: $0 \to$ unprimed variable, $1 \to$ primed variable, combined by $\vee$)*.
6. **Duality Sanity Check (Write this to impress the professor)**:
   $$\\{i \mid f(i) = 1\\} \cup \\{j \mid f(j) = 0\\} = \\{0, 1, 2, 3, 4, 5, 6, 7\\} \quad \text{and} \quad \\{i\\} \cap \\{j\\} = \emptyset$$

### Pre-Computed Standard Verbal Problem Answers:
* **Majority on $(x, y, z)$**: $\text{PDNF} = \sum m(3, 5, 6, 7)$; $\text{PCNF} = \prod M(0, 1, 2, 4)$.
* **Majority on $(x, y', z)$** *(Actual Sep 2026 Paper)*: $\text{PDNF} = \sum m(1, 4, 5, 7)$; $\text{PCNF} = \prod M(0, 2, 3, 6)$.
* **Odd Parity (XOR $x \oplus y \oplus z$)**: $\text{PDNF} = \sum m(1, 2, 4, 7)$; $\text{PCNF} = \prod M(0, 3, 5, 6)$.
* **Even Parity (XNOR)**: $\text{PDNF} = \sum m(0, 3, 5, 6)$; $\text{PCNF} = \prod M(1, 2, 4, 7)$.

---

## 💎 BLUEPRINT 3: Divisor Lattice $(D_n, \mid)$ Complete Instant Evaluator

### Applicable Question Archetypes:
* *"Let $D_n$ be the set of all positive divisors of $n$ under divisibility relation. Find the zero and unit elements."*
* *"Determine whether $(D_n, \mid)$ is a complemented lattice. Find complements of all elements."*
* *"Is $(D_n, \mid)$ a Boolean algebra? Justify."*

### Step-by-Step Universal Algorithm for ANY integer $n$:
1. **Prime Factorization**:
   $$n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$$
2. **Total Divisor Count**:
   $$|D_n| = \tau(n) = (e_1 + 1)(e_2 + 1) \cdots (e_k + 1)$$
3. **Zero and Unit Elements (Always the same!)**:
   * **Least / Zero Element ($0_L$)**: $\mathbf{0_L = 1}$ (since $1 \mid x$ for all $x \in D_n$).
   * **Greatest / Unit Element ($1_L$)**: $\mathbf{1_L = n}$ (since $x \mid n$ for all $x \in D_n$).
4. **Lattice Operations**:
   * Meet (Infimum / GLB): $a \wedge b = \gcd(a, b)$.
   * Join (Supremum / LUB): $a \vee b = \text{lcm}(a, b)$.
5. **Complementation Formula & Testing**:
   * An element $y$ is a complement of $x \iff x \wedge y = 1$ (i.e. $\gcd(x, y) = 1$) and $x \vee y = n$ (i.e. $\text{lcm}(x, y) = n$).
   * Since $\gcd(x, y) \cdot \text{lcm}(x, y) = x \cdot y$, we MUST have $1 \cdot n = x \cdot y \implies \mathbf{y = \frac{n}{x}}$.
   * **Golden Test**: The element $x$ has a complement $\iff \mathbf{\gcd\left(x, \frac{n}{x}\right) = 1}$.
     * If $\gcd(x, n/x) = 1$, then $y = n/x$ is its unique complement.
     * If $\gcd(x, n/x) > 1$, then $x$ has **NO COMPLEMENT**!
6. **The Master Square-Free Theorem (Instant 10/10 Marks)**:
   > **Theorem**: The divisor lattice $(D_n, \mid)$ is a **Boolean algebra** if and only if $n$ is **square-free** (i.e. $n$ is a product of distinct primes, with all exponents $e_i = 1$).
   * **If $n$ has any prime squared ($e_i \ge 2$)**: It is **NOT** a complemented lattice, and therefore **NOT** a Boolean algebra.
   * **Standard Counterexample to Write**: Choose element $x = p_i$. Candidate is $y = n/p_i$. Since $p_i \mid (n/p_i)$, $\gcd(p_i, n/p_i) = p_i > 1 \ne 1$. Hence element $p_i$ has no complement in $D_n$.

### Rapid Lookup Cheat Sheet for Standard Exam Values of $n$:

| Poset | Prime Factorization | $|D_n|$ | Zero | Unit | Complemented? | Boolean Algebra? | Failing Element(s) Without Complement |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **$D_6$** | $2 \times 3$ | 4 | 1 | 6 | **YES** | **YES** ($B_2$) | None (All have unique complements: $1\leftrightarrow 6, 2\leftrightarrow 3$) |
| **$D_8$** | $2^3$ | 4 | 1 | 8 | **NO** | **NO** (Chain) | $2$ (candidate $4$, $\gcd(2,4)=2$), $4$ (candidate $2$) |
| **$D_{12}$** | $2^2 \times 3$ | 6 | 1 | 12 | **NO** | **NO** | $2$ (candidate $6$, $\gcd(2,6)=2$), $6$ (candidate $2$) |
| **$D_{18}$** | $2 \times 3^2$ | 6 | 1 | 18 | **NO** | **NO** | $3$ (candidate $6$, $\gcd(3,6)=3$), $6$ (candidate $3$) |
| **$D_{20}$** | $2^2 \times 5$ | 6 | 1 | 20 | **NO** | **NO** | $2$ (candidate $10$, $\gcd(2,10)=2$), $10$ (candidate $2$) |
| **$D_{24}$** | $2^3 \times 3$ | 8 | 1 | 24 | **NO** | **NO** | $2, 4, 6, 12$ have no complements |
| **$D_{30}$** | $2 \times 3 \times 5$ | 8 | 1 | 30 | **YES** | **YES** ($B_3$, 3-cube) | None ($1\leftrightarrow 30, 2\leftrightarrow 15, 3\leftrightarrow 10, 5\leftrightarrow 6$) |
| **$D_{36}$** | $2^2 \times 3^2$ | 9 | 1 | 36 | **NO** | **NO** | $2, 3, 6, 12, 18$ have no complements |
| **$D_{42}$** | $2 \times 3 \times 7$ | 8 | 1 | 42 | **YES** | **YES** ($B_3$) | None ($1\leftrightarrow 42, 2\leftrightarrow 21, 3\leftrightarrow 14, 6\leftrightarrow 7$) |
| **$D_{70}$** | $2 \times 5 \times 7$ | 8 | 1 | 70 | **YES** | **YES** ($B_3$) | None ($1\leftrightarrow 70, 2\leftrightarrow 35, 5\leftrightarrow 14, 7\leftrightarrow 10$) |
| **$D_{210}$** | $2 \times 3 \times 5 \times 7$ | 16 | 1 | 210 | **YES** | **YES** ($B_4$, 4-cube) | None (All 16 elements complemented) |

---

## 📐 BLUEPRINT 4: Handshaking Lemma & Vertex Partition Degree Equation Solver

### Applicable Question Archetypes:
* *"Can a graph exist with vertices partitioned into $V_1$ and $V_2$ such that $|V_1| = 2|V_2|$, each vertex in $V_1$ has degree 2, each vertex in $V_2$ has degree 4, and $|E| = 15$?"*
* *"A simple graph has $n$ vertices, half of degree 3 and half of degree 4, with $m$ edges. Is this graph possible?"*
* *"Can a simple bipartite graph have partition sizes $n_1=5, n_2=6$ where every vertex in $V_1$ has degree 4 and $V_2$ has degree 3?"*

### Step-by-Step Universal Algorithm:
1. **Set Up the Parameter $k$**:
   * Express the vertex subset sizes in terms of integer variable $k$:
     $$|V_2| = k, \quad |V_1| = c \cdot k \implies |V| = (c + 1)k$$
2. **Apply Euler's Handshaking Theorem**:
   $$\sum_{v \in V} \deg(v) = 2|E|$$
   $$\sum_{i} |V_i| \cdot d_i = 2|E|$$
3. **Solve for $k$**:
   * Example: $(2k)(2) + (k)(4) = 2(15) \implies 8k = 30 \implies k = 3.75$.
4. **Execute the 4-Gate Impossibility / Feasibility Checklist**:
   * **Gate 1 (Integrality Test)**:
     * Condition: $k \in \mathbb{Z}^+$ (must be a positive whole integer).
     * If $k$ is fractional: **STOP**. Write:
       * *"By Euler's Handshaking theorem, $\sum \deg(v) = 2|E| \implies 8k = 30 \implies k = 3.75 \notin \mathbb{Z}^+$. Since the number of vertices in any graph must be a non-negative integer, no such graph can exist. $\blacksquare$"*
   * **Gate 2 (Degree Parity Corollary)**:
     * Condition: The count of vertices of **odd degree** must be **EVEN**.
     * If odd-degree vertex count is odd: **STOP**. Write:
       * *"The graph contains an odd number of odd-degree vertices, directly violating the Handshaking Corollary. Therefore, no such graph can exist. $\blacksquare$"*
   * **Gate 3 (Maximum Degree Constraint for Simple Graph)**:
     * Condition: $\Delta = \max(d_i) \le |V| - 1$.
     * If $\Delta \ge |V|$: **STOP**. Write:
       * *"In a simple graph of $|V|$ vertices, no vertex can have degree greater than $|V|-1$ (no self-loops or parallel edges). Here $\Delta = \dots \ge |V|$, which is impossible. $\blacksquare$"*
   * **Gate 4 (Edge Density Constraint)**:
     * Condition: $|E| \le \binom{|V|}{2} = \frac{|V|(|V|-1)}{2}$. For bipartite graphs, $|E| \le |V_1| \cdot |V_2|$.
     * If $|E|$ exceeds maximum allowed: **STOP**. Write density impossibility proof.

---

## 🔍 BLUEPRINT 5: 2-Graph Isomorphism Decision & Proof Engine

### Applicable Question Archetypes:
* *"Determine whether the two given graphs $G_1$ and $G_2$ are isomorphic."*
* *"Show that the two graphs are non-isomorphic by exhibiting a graph invariant that differs."*
* *"Verify graph isomorphism by providing an explicit vertex bijection and verifying edge preservation."*

### Phase 1: Draw the 5-Invariant Elimination Table First!
Before doing anything else, draw this exact table in your exam sheet:

| Invariant | Graph $G_1$ Value | Graph $G_2$ Value | Status |
| :--- | :---: | :---: | :---: |
| **1. Number of Vertices ($|V|$)** | $n_1$ | $n_2$ | Match $\checkmark$ / Differs $\times$ |
| **2. Number of Edges ($|E|$)** | $m_1$ | $m_2$ | Match $\checkmark$ / Differs $\times$ |
| **3. Degree Sequence (Sorted Descending)** | $(d_1, d_2, \dots)$ | $(d'_1, d'_2, \dots)$ | Match $\checkmark$ / Differs $\times$ |
| **4. Connected Components ($c(G)$)** | $c(G_1)$ | $c(G_2)$ | Match $\checkmark$ / Differs $\times$ |
| **5. Cycle Spectrum ($C_3$ Triangles, $C_4$ 4-Cycles)** | Count of $C_3, C_4$ | Count of $C_3, C_4$ | Match $\checkmark$ / Differs $\times$ |
| **6. Complement Graph Size ($|\overline{E}|$)** | $\binom{n}{2} - m_1$ | $\binom{n}{2} - m_2$ | Match $\checkmark$ / Differs $\times$ |

---

### Decision Branch A: If ANY Invariant Differs $\implies$ NON-ISOMORPHIC (Instant 1-Line Proof)
**Model Text to Write**:
> *"The two graphs $G_1$ and $G_2$ are **NOT isomorphic** ($G_1 \not\cong G_2$).  
> **Proof**: A graph invariant is a property preserved under all graph isomorphisms. Here, the invariant **[Insert Failing Invariant, e.g. Number of 3-Cycles $C_3$]** differs between $G_1$ and $G_2$:  
> - $G_1$ contains [e.g. 2 triangles: $(u_1, u_2, u_3)$ and $(u_4, u_5, u_6)$].  
> - $G_2$ contains [e.g. 0 triangles, as it is bipartite].  
> Since any isomorphism must map $k$-cycles to $k$-cycles, no edge-preserving bijection can exist between $V(G_1)$ and $V(G_2)$. Hence $G_1 \not\cong G_2$. $\blacksquare$"*

---

### Decision Branch B: If All Invariants Match $\implies$ ISOMORPHIC (Full-Credit Proof Protocol)
*(Remember: Matching invariants is necessary but NOT sufficient. You MUST write the explicit bijection table to get 10/10 marks!)*

1. **Step 1: Structural Cycle / Path Tracing**:
   * Trace the primary cycle in $G_1$: e.g. $u_1 - u_2 - u_3 - u_4 - u_5 - u_6 - u_1$.
   * Trace the corresponding cycle in $G_2$: e.g. $v_1 - v_3 - v_5 - v_2 - v_4 - v_6 - v_1$.
2. **Step 2: Construct the Vertex Bijection Table $f: V(G_1) \to V(G_2)$**:

| Vertex in $G_1$ ($u_i$) | Mapped Vertex in $G_2$ ($f(u_i)$) | $\deg(u_i)$ | $\deg(f(u_i))$ | Neighbor Set in $G_1$ | Image Neighbor Set in $G_2$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $u_1$ | $v_1$ | 2 | 2 | $\\{u_2, u_6\\}$ | $\\{f(u_2), f(u_6)\\} = \\{v_3, v_6\\}$ |
| $u_2$ | $v_3$ | 2 | 2 | $\\{u_1, u_3\\}$ | $\\{f(u_1), f(u_3)\\} = \\{v_1, v_5\\}$ |
| $u_3$ | $v_5$ | 2 | 2 | $\\{u_2, u_4\\}$ | $\\{f(u_2), f(u_4)\\} = \\{v_3, v_2\\}$ |
| $u_4$ | $v_2$ | 2 | 2 | $\\{u_3, u_5\\}$ | $\\{f(u_3), f(u_5)\\} = \\{v_5, v_4\\}$ |
| $u_5$ | $v_4$ | 2 | 2 | $\\{u_4, u_6\\}$ | $\\{f(u_4), f(u_6)\\} = \\{v_2, v_6\\}$ |
| $u_6$ | $v_6$ | 2 | 2 | $\\{u_5, u_1\\}$ | $\\{f(u_5), f(u_1)\\} = \\{v_4, v_1\\}$ |

3. **Step 3: Edge-Preservation Verification Table**:
   Show that $(u_i, u_j) \in E(G_1) \iff (f(u_i), f(u_j)) \in E(G_2)$ for every edge:

| Edge in $G_1$ | Image Edge in $G_2$ | Present in $E(G_2)$? |
| :---: | :---: | :---: |
| $(u_1, u_2)$ | $(v_1, v_3)$ | Yes $\checkmark$ |
| $(u_2, u_3)$ | $(v_3, v_5)$ | Yes $\checkmark$ |
| $(u_3, u_4)$ | $(v_5, v_2)$ | Yes $\checkmark$ |
| $(u_4, u_5)$ | $(v_2, v_4)$ | Yes $\checkmark$ |
| $(u_5, u_6)$ | $(v_4, v_6)$ | Yes $\checkmark$ |
| $(u_6, u_1)$ | $(v_6, v_1)$ | Yes $\checkmark$ |

4. **Step 4: Formal Concluding Sentence**:
   > *"Since $f: V(G_1) \to V(G_2)$ is a 1-to-1 and onto mapping (bijection) that preserves adjacency and non-adjacency across all pairs of vertices, the graphs $G_1$ and $G_2$ are **ISOMORPHIC** ($G_1 \cong G_2$). $\blacksquare$"*

---

## 🔢 BLUEPRINT 6: Havel-Hakimi Graphic Sequence Table Generator

### Applicable Question Archetypes:
* *"Determine whether the given degree sequence $S = (d_1, d_2, \dots, d_n)$ is graphic using the Havel-Hakimi algorithm."*
* *"Can a simple graph be constructed with degree sequence $(d_1, \dots, d_n)$?"*

### Havel-Hakimi Equivalence Theorem:
> A non-increasing sequence of non-negative integers $S = (d_1, d_2, \dots, d_n)$ with $d_1 \le n-1$ is **graphic** if and only if the modified sequence:
> $$S' = (d_2 - 1, d_3 - 1, \dots, d_{d_1 + 1} - 1, d_{d_1 + 2}, \dots, d_n)$$
> (obtained by deleting $d_1$ and subtracting 1 from the next $d_1$ terms) is graphic when re-sorted in non-increasing order.

### Step-by-Step Universal Algorithm:
1. **Pre-Screening Gate (Instant Disqualification)**:
   * Compute degree sum $\sum d_i$. If ODD $\implies$ NOT GRAPHIC (by Handshaking Lemma).
   * Check maximum degree $d_1$. If $d_1 \ge n$ $\implies$ NOT GRAPHIC (max degree in simple graph is $n-1$).
   * Check if any $d_i < 0$ $\implies$ NOT GRAPHIC.
2. **Execute the Standard 4-Column Table**:

| Step $k$ | Current Sequence (Sorted Non-Increasing) | Reduction Operation (Delete $d_1$, subtract 1 from next $d_1$ terms) | Resulting Sequence | Re-sorted Sequence $S^{(k+1)}$ |
| :---: | :--- | :--- | :--- | :--- |
| **0** | $(d_1, d_2, \dots, d_n)$ | $d_1 = \dots$; Subtract 1 from next $d_1$ terms | $(\dots)$ | $(\dots)$ |
| **1** | $(\dots)$ | $d_1 = \dots$; Subtract 1 from next $d_1$ terms | $(\dots)$ | $(\dots)$ |
| **2** | $(\dots)$ | $d_1 = \dots$; Subtract 1 from next $d_1$ terms | $(\dots)$ | $(\dots)$ |

3. **Termination Rules (Crucial!)**:
   * **Rule A (Graphic)**: If the sequence reduces to a sequence of all zeros (e.g. $(0, 0, \dots, 0)$), this represents an empty/null graph $N_k$ with $k$ isolated vertices (trivially graphic). Conclude:
     > *"At Step $k$, the sequence reduces to all zeros, which is trivially graphic (null graph). By the Havel-Hakimi Theorem, the original sequence $S$ is **GRAPHIC**. $\blacksquare$"*
   * **Rule B (Not Graphic)**: If at any step, a negative number appears (e.g. subtracting 1 from 0 yields $-1$) or there are fewer than $d_1$ remaining terms to subtract from, the sequence is **NOT GRAPHIC**. Conclude:
     > *"At Step $k$, subtraction produces a negative degree (or insufficient terms), which cannot occur in any simple graph. By the Havel-Hakimi Theorem, the original sequence $S$ is **NOT GRAPHIC**. $\blacksquare$"*

---

## 📊 BLUEPRINT 7: Floyd-Warshall All-Pairs Shortest Path Matrix Execution Blueprint

### Applicable Question Archetypes:
* *"Find all-pairs shortest paths for the given directed graph using Floyd-Warshall algorithm. Show all matrices $D^{(0)}, D^{(1)}, D^{(2)}, D^{(3)}, D^{(4)}$."*

### Mathematical Recurrence:
$$d_{ij}^{(k)} = \min\left( d_{ij}^{(k-1)}, \quad d_{ik}^{(k-1)} + d_{kj}^{(k-1)} \right)$$
$$k \in \\{1, 2, \dots, n\\}, \quad i, j \in \\{1, 2, \dots, n\\}$$

### Predecessor Update Rule:
$$\pi_{ij}^{(k)} = \begin{cases} \pi_{kj}^{(k-1)} & \text{if } d_{ik}^{(k-1)} + d_{kj}^{(k-1)} < d_{ij}^{(k-1)} \\\\ \pi_{ij}^{(k-1)} & \text{otherwise} \end{cases}$$

### The 4 Golden Speed Shortcuts (Never make an arithmetic mistake!):
1. **Row $k$ and Column $k$ NEVER Change**: When computing matrix $D^{(k)}$, Row $k$ and Column $k$ are identical to $D^{(k-1)}$. Copy them directly!
2. **Diagonal Entries are ALWAYS Zero**: $d_{ii}^{(k)} = 0$ for all $k$.
3. **Infinity Free Pass**: If entry $d_{ik}^{(k-1)} = \infty$ or $d_{kj}^{(k-1)} = \infty$, the candidate path length is $\infty$. The cell $(i, j)$ CANNOT change! Copy $d_{ij}^{(k)} = d_{ij}^{(k-1)}$ directly.
4. **Active Cell Filter**: In an $n=4$ matrix, typically only 2 to 4 cells have finite entries in both row $k$ and column $k$. Only compute those specific candidate sums!

### Universal Execution Walkthrough:
* **Initial Matrix $D^{(0)}$**:
  * Set $d_{ii} = 0$.
  * Set $d_{ij} = w(i, j)$ if directed edge $i \to j$ exists.
  * Set $d_{ij} = \infty$ if no direct edge exists.
* **Initial Matrix $\Pi^{(0)}$**:
  * Set $\pi_{ij} = i$ if $i \ne j$ and $w(i, j) < \infty$.
  * Set $\pi_{ij} = \text{NIL}$ if $i = j$ or $w(i, j) = \infty$.
* **Iterations**:
  * **$k=1$ (via Vertex 1)**: Keep Row 1 and Col 1 unchanged. Test cells $(i, j)$ where both $d_{i1} < \infty$ and $d_{1j} < \infty$.
  * **$k=2$ (via Vertex 2)**: Keep Row 2 and Col 2 unchanged. Test cells where $d_{i2} < \infty$ and $d_{2j} < \infty$.
  * **$k=3$ (via Vertex 3)**: Keep Row 3 and Col 3 unchanged. Test cells where $d_{i3} < \infty$ and $d_{3j} < \infty$.
  * **$k=4$ (via Vertex 4)**: Keep Row 4 and Col 4 unchanged. Test cells where $d_{i4} < \infty$ and $d_{4j} < \infty$.
* **Reconstructing the Shortest Path from $\Pi$**:
  * To find path from $i$ to $j$: start at $j$, read predecessor $p_1 = \pi_{ij}$. Then read $p_2 = \pi_{i, p_1}$, until reaching $i$. Reverse sequence $\implies i \to \dots \to j$.

---

## 🛣️ BLUEPRINT 8: Dijkstra Single-Source Shortest Path Blueprint

### Applicable Question Archetypes:
* *"Apply Dijkstra's algorithm to find the shortest path from source vertex $S$ to all other vertices."*

### Standard 5-Column Iteration Table Layout:
When solving on your exam paper, always format Dijkstra as follows:

| Step $k$ | Settled Vertex $u^*$ | Settled Set $S$ | Candidate Vertices Evaluated | Distance Vector $\big[ d(A), d(B), d(C), d(D), d(E) \big]$ |
| :---: | :---: | :---: | :---: | :--- |
| **Init** | - | $\emptyset$ | Initialize Source $S \to 0$, others $\to \infty$ | $[0_S, \infty, \infty, \infty, \infty]$ |
| **1** | $S$ | $\\{S\\}$ | Relax neighbors of $S$ | $[0_S, w(S,A)_S, w(S,B)_S, \dots]$ |
| **2** | $u_1^*$ (min $d$) | $\\{S, u_1^*\\}$ | Relax neighbors of $u_1^*$ | $[\dots]$ |
| **3** | $u_2^*$ | $\\{S, u_1^*, u_2^*\\}$ | Relax neighbors of $u_2^*$ | $[\dots]$ |

### Shortest Path Schedule Summary Table (Write this at the end):

| Destination Vertex | Shortest Distance from $S$ | Predecessor Chain / Full Path |
| :---: | :---: | :---: |
| **$A$** | $d[A]$ | $S \to \dots \to A$ |
| **$B$** | $d[B]$ | $S \to \dots \to B$ |
| **$C$** | $d[C]$ | $S \to \dots \to C$ |
| **$D$** | $d[D]$ | $S \to \dots \to D$ |

---

## 🔴🔵 BLUEPRINT 9: Bipartite Graph Detection & Kőnig's 2-Coloring Engine

### Applicable Question Archetypes:
* *"State Kőnig's theorem. Determine whether graph $G$ is bipartite."*
* *"Show that graph $G$ contains an odd cycle and hence is not 2-colorable."*

### Theorem Statement:
> **Kőnig's Theorem**: An undirected graph $G$ is **bipartite** if and only if it contains **NO odd cycles** (i.e. every cycle in $G$ has even length $\ge 4$). Equivalently, $G$ is **2-colorable** ($\chi(G) \le 2$).

### BFS 2-Coloring Algorithm Execution:
1. Choose an arbitrary starting vertex $v_1$ and assign Color **RED**.
2. Assign Color **BLUE** to all neighbors of $v_1$.
3. For each newly colored vertex, assign the opposite color to all its unvisited neighbors.
4. **Outcome Evaluation**:
   * **Case A: No Conflict Occurs**:
     * Partition vertices into $V_1 = \\{\text{All RED vertices}\\}$ and $V_2 = \\{\text{All BLUE vertices}\\}$.
     * Verify that every edge in $E(G)$ has one endpoint in $V_1$ and one in $V_2$.
     * Conclude: *"Graph $G$ is 2-colorable with no internal monochromatic edges. By Kőnig's Theorem, $G$ is **BIPARTITE** with bipartition $(V_1, V_2)$. $\blacksquare$"*
   * **Case B: Chromatic Conflict Occurs (Edge between two vertices of same color)**:
     * Identify the conflicting edge $(u, v)$ where $\text{Color}(u) = \text{Color}(v)$.
     * Trace back to their lowest common ancestor in the BFS tree $\implies$ Extract the odd cycle:
       $$u - \dots - w - \dots - v - u \quad (\text{Length } 2k+1)$$
     * Conclude: *"Edge $(u, v)$ connects two vertices of the same color, producing an odd cycle of length $2k+1$. By Kőnig's Theorem, a graph is bipartite if and only if it contains no odd cycles. Therefore, $G$ is **NOT BIPARTITE**. $\blacksquare$"*

---

## 🌐 BLUEPRINT 10: Planar Graph Polyhedral Formulas ($v - e + f = 2$)

### Applicable Question Archetypes:
* *"A connected planar graph has $v$ vertices and $e$ edges. How many faces does it divide the plane into?"*
* *"Prove using Euler's formula that $K_5$ (complete graph on 5 vertices) is non-planar."*
* *"Prove that $K_{3,3}$ (complete bipartite utility graph) is non-planar."*

### Core Formulas & Theorems:
1. **Euler's Polyhedral Formula**: For any connected planar graph $G = (V, E)$ with $v = |V|$ vertices, $e = |E|$ edges, and $f$ faces (including the unbounded outer face):
   $$\mathbf{v - e + f = 2} \implies \mathbf{f = e - v + 2}$$
2. **Face Degree Handshaking**: Each edge borders exactly two faces (or two sides of the same face):
   $$\sum_{i=1}^f \deg(f_i) = 2e$$
3. **Edge Upper Bound for Simple Planar Graphs**:
   * Since every face in a simple graph has at least 3 boundary edges ($\deg(f_i) \ge 3$):
     $$2e = \sum \deg(f_i) \ge 3f = 3(e - v + 2) = 3e - 3v + 6 \implies \mathbf{e \le 3v - 6} \quad (\forall v \ge 3)$$
4. **Edge Upper Bound for Triangle-Free / Bipartite Simple Planar Graphs**:
   * Since there are no triangles, every face has at least 4 boundary edges ($\deg(f_i) \ge 4$):
     $$2e = \sum \deg(f_i) \ge 4f = 4(e - v + 2) = 4e - 4v + 8 \implies 2e \le 4v - 8 \implies \mathbf{e \le 2v - 4}$$

### Ready-to-Copy Non-Planarity Proofs:
* **Proof that $K_5$ is Non-Planar**:
  For $K_5$: $v = 5$, $e = \binom{5}{2} = 10$.  
  If $K_5$ were planar, it must satisfy $e \le 3v - 6$.  
  $3v - 6 = 3(5) - 6 = 15 - 6 = 9$.  
  Since $e = 10 > 9$, the inequality is violated.  
  $\mathbf{\therefore K_5 \text{ is strictly NON-PLANAR.} \quad \blacksquare}$
* **Proof that $K_{3,3}$ is Non-Planar**:
  $K_{3,3}$ is a bipartite graph, so it contains no odd cycles (no triangles). Hence every face has $\deg(f) \ge 4$.  
  For $K_{3,3}$: $v = 3 + 3 = 6$, $e = 3 \times 3 = 9$.  
  If $K_{3,3}$ were planar, it must satisfy $e \le 2v - 4$.  
  $2v - 4 = 2(6) - 4 = 12 - 4 = 8$.  
  Since $e = 9 > 8$, the inequality is violated.  
  $\mathbf{\therefore K_{3,3} \text{ is strictly NON-PLANAR.} \quad \blacksquare}$

---
# PART III: MODULE 3 QUESTIONNAIRE BANK (Lattices & Boolean Algebra)

---
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

---

# PART IV: MODULE 4 QUESTIONNAIRE BANK (Graphs & Matrix Representations)

---
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

---

# PART V: COMMON EXAM TRAPS & PROFESSOR MARKING CRITERIA

---
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
