# ⚡ CAT-2 HOTS Master Crib — Module 4: Graphs & Matrix Representations
**Course**: MAT2002 — Discrete Mathematics & Graph Theory  
**Coverage**: Module 4 (CO4) | **Exam Mode**: Open Book / Handwritten Notes Allowed  
**Target Score**: 45+ / 50 (S-Grade Boundary)

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If Question Mentions / Shows... | It Means This Exact Topic | Your Immediate Formula / Action |
| :--- | :--- | :--- |
| Degree sequence $(d_1, d_2, \dots, d_n)$, "Is it graphic?" | **Havel-Hakimi Algorithm** | Sort descending $\rightarrow$ delete $d_1$, subtract 1 from next $d_1$ numbers $\rightarrow$ repeat until all zeros (Graphic) or negative/impossible (NOT Graphic). |
| "Is the graph bipartite?", $K_{m,n}$ | **Bipartite Verification** | Apply 2-Coloring BFS. Graph is Bipartite $\iff$ **NO odd-length cycles**! ($C_3, C_5, C_7$ forbidden). |
| Two graphs $G_1, G_2$, "Are they isomorphic?" | **Graph Isomorphism** | Check 4 Invariants: (1) $|V_1|=|V_2|$, (2) $|E_1|=|E_2|$, (3) Degree sequences match, (4) Cycles of length $k$ match. Then write explicit vertex map $f(u) = v$. |
| Adjacency matrix $A$, "Number of walks of length $k$" | **Walks via Matrix Power $A^k$** | The $(i, j)$-th entry of $A^k$ gives the exact number of walks of length $k$ from $v_i$ to $v_j$. For length 2: $(A^2)_{ij} = \text{common neighbors}$. |
| "Self-complementary graph", $G \cong \overline{G}$ | **Self-Complementary Formula** | Number of edges $|E| = \frac{n(n-1)}{4}$. Thus, $n(n-1)$ must be divisible by 4 $\implies n \equiv 0 \text{ or } 1 \pmod 4$. |
| "Euler circuit / Euler trail", "Can you draw without lifting pen?" | **Eulerian Graphs** | All degrees even $\implies$ **Euler Circuit**. Exactly two odd degrees $\implies$ **Euler Trail** (starts and ends at odd vertices). |
| "Hamiltonian circuit / path", Travelling Salesperson | **Hamiltonian Graphs** | Check Dirac's: $\deg(v) \ge n/2$ $\forall v$. Check Ore's: $\deg(u) + \deg(v) \ge n$ for all non-adjacent pairs. |
| Directed weighted graph, "Shortest path from $s$ to $t$" | **Dijkstra's Algorithm** | Use the step-by-step Vertex-Distance Table. Permanently mark minimum distance vertex at each step. |

---

## 🛠️ TIER 2: Deterministic Algorithmic Recipes

### Recipe 4.1: The Havel-Hakimi Graphic Sequence Test
Given a sequence of non-negative integers $S = (d_1, d_2, \dots, d_n)$:
1. **Sanity Check**: Sum of degrees $\sum d_i$ **must be even** (Handshaking Theorem). If odd $\implies$ **STOP: Not Graphic ❌**.
2. **Sort**: Arrange $S$ in non-increasing order: $d_1 \ge d_2 \ge \dots \ge d_n$.
3. **Check Termination**:
   - If all numbers are $0 \implies$ **Graphic ✅** (Graph is a collection of isolated vertices).
   - If any number becomes $< 0$ or $d_1 > \text{remaining elements} \implies$ **NOT Graphic ❌**.
4. **Reduction Step**: Remove the first element $d_1$. Subtract $1$ from each of the next $d_1$ elements.
5. **Re-sort** and repeat from Step 2.

---

### Recipe 4.2: Graph Isomorphism Proof / Disproof System
To test if $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ are isomorphic:

#### Step A: The 4 Necessary Invariants (Quick Disproof)
If ANY of these fails, $G_1 \not\cong G_2$:
1. $|V_1| = |V_2|$ (Same number of vertices).
2. $|E_1| = |E_2|$ (Same number of edges).
3. Sorted degree sequences must be identical.
4. **Cycle Invariant (Crucial)**: If $G_1$ has a triangle ($C_3$) or 4-cycle ($C_4$), $G_2$ must have the same number of triangles or 4-cycles among vertices with matching degrees!
5. **Complement Invariant**: $G_1 \cong G_2 \iff \overline{G_1} \cong \overline{G_2}$ (often much easier to check if graphs are dense!).

#### Step B: Constructing the Bijective Map $f: V_1 \to V_2$
To prove they **ARE** isomorphic:
1. Pair unique degree vertices first (e.g. if only one vertex has degree 4, it must map to the unique degree 4 vertex).
2. Trace neighbor connections: If $u \sim v$ in $G_1$, then $f(u) \sim f(v)$ in $G_2$.
3. Present the mapping table:
   $$\begin{array}{|c|c|c|c|c|} \hline u \in V_1 & v_1 & v_2 & v_3 & \dots \\ \hline f(u) \in V_2 & w_2 & w_5 & w_1 & \dots \\ \hline \end{array}$$
4. Verify edge preservation: For every edge $(u, v) \in E_1$, show $(f(u), f(v)) \in E_2$.

---

### Recipe 4.3: Bipartite Testing via 2-Coloring BFS
1. Pick any starting vertex $v_0$ and color it **RED**.
2. Put all uncolored neighbors of $v_0$ into the queue and color them **BLUE**.
3. For each vertex in the queue:
   - Examine its neighbors:
     - If a neighbor has the **SAME color** $\implies$ **STOP: Graph is NOT Bipartite ❌** (an odd-length cycle exists).
     - If uncolored, assign the **OPPOSITE color**.
4. If all vertices in all components are colored without conflict $\implies$ **Graph is Bipartite ✅**.
5. Partition: $V_1 = \{ \text{all RED vertices} \}$, $V_2 = \{ \text{all BLUE vertices} \}$.

---

### Recipe 4.4: Walks of Length 2 and 3 via Adjacency Matrix
Let $A$ be the $n \times n$ adjacency matrix ($A_{ij} = 1$ if edge exists, $0$ otherwise).
* **Length 1 walks from $i$ to $j$**: $A_{ij}$ (direct edges).
* **Length 2 walks from $i$ to $j$**:
  $$(A^2)_{ij} = \sum_{k=1}^n A_{ik} A_{kj} = \text{number of common neighbors between } v_i \text{ and } v_j$$
  * *Special Case*: $(A^2)_{ii} = \deg(v_i)$ (walk $v_i \to v_k \to v_i$).
* **Total number of length 2 walks in graph**:
  $$\sum_{i=1}^n (A^2)_{ii} = \sum \deg(v_i) = 2|E|$$
* **Length 3 closed walks (Triangles)**:
  $$\text{Trace}(A^3) = \sum_{i=1}^n (A^3)_{ii} = 6 \times (\text{number of triangles in } G)$$

---

### Recipe 4.5: Dijkstra's Tabular Execution (Guaranteed Full Marks)
Create a table with columns: `Step | Selected Vertex | Updated Distances [v1, v2, ... vn]`
1. Set distance $d(s) = 0$, all other $d(v) = \infty$.
2. At each step:
   - Find the unvisited vertex $u$ with minimum current distance $d(u)$.
   - Mark $u$ as **Permanent** (box it).
   - For every unvisited neighbor $v$ of $u$:
     $$d(v) = \min(d(v), d(u) + w(u, v))$$
3. Repeat until the destination is marked permanent.

---

## 🚨 TIER 3: Faculty Trap Radar

1. **The Isolated Vertex Handshaking Trap**: Isolated vertices have degree 0. They contribute 0 to the sum $\sum \deg(v) = 2|E|$, but they **do count** in $|V|$!
2. **The "Dirac's Theorem is a Converse" Trap**: Dirac's theorem ($\deg \ge n/2$) is **sufficient, NOT necessary**! A graph with $\deg < n/2$ can still be Hamiltonian (e.g. cycle $C_6$ has degrees 2, $6/2 = 3$, but $C_6$ is obviously Hamiltonian!).
3. **The Euler Path Endpoints**: If an Euler path exists, it **MUST start at one odd-degree vertex and end at the OTHER odd-degree vertex**. It cannot start at an even-degree vertex!
4. **The Complete Bipartite Edges Formula**: $K_{m,n}$ has $m+n$ vertices and **$m \times n$ edges**. It has no triangles ($C_3$) because it is bipartite.

---

## 📝 TIER 4: Master Solved HOTS Archetypes

### Archetype 1: Havel-Hakimi Test & Graph Construction
**Question**: Determine whether the sequence $S = (5, 4, 3, 3, 3, 2, 2)$ is graphic. If graphic, construct a simple graph with this degree sequence.

**Solution Template**:
1. **Sum Check**: $5 + 4 + 3 + 3 + 3 + 2 + 2 = 22$ (Even $\implies$ passes Handshaking test).
2. **Step 1**: $S = (5, 4, 3, 3, 3, 2, 2)$. $d_1 = 5$.
   - Subtract 1 from the next 5 elements:
     $$4-1=3, \quad 3-1=2, \quad 3-1=2, \quad 3-1=2, \quad 2-1=1$$
   - Result: $(3, 2, 2, 2, 1, 2)$.
3. **Step 2**: Re-sort in descending order:
   $$S_1 = (3, 2, 2, 2, 2, 1)$$
4. **Step 3**: $d_1 = 3$. Subtract 1 from next 3 elements:
   $$2-1=1, \quad 2-1=1, \quad 2-1=1$$
   - Result: $(1, 1, 1, 2, 1)$.
5. **Step 4**: Re-sort in descending order:
   $$S_2 = (2, 1, 1, 1, 1)$$
6. **Step 5**: $d_1 = 2$. Subtract 1 from next 2 elements:
   $$1-1=0, \quad 1-1=0$$
   - Result: $(0, 0, 1, 1)$.
7. **Step 6**: Re-sort:
   $$S_3 = (1, 1, 0, 0)$$
8. **Step 7**: $d_1 = 1$. Subtract 1 from next 1 element:
   - Result: $(0, 0, 0)$.
9. **Conclusion**: All remaining degrees are $0$. By the Havel-Hakimi Theorem, the degree sequence $S$ is **GRAPHIC ✅**.

---

### Archetype 2: Isomorphism Rigorous Proof
**Question**: Let $G_1$ and $G_2$ be two graphs on 6 vertices:
* $G_1$: Vertices $\{1, 2, 3, 4, 5, 6\}$, Edges: $(1,2), (2,3), (3,4), (4,5), (5,6), (6,1)$ and chord $(1,4)$.
* $G_2$: Vertices $\{a, b, c, d, e, f\}$, Edges: $(a,b), (b,c), (c,d), (d,e), (e,f), (f,a)$ and chord $(b,e)$.
Prove whether $G_1 \cong G_2$.

**Solution Template**:
1. **Invariant 1 (|V|)**: $|V_1| = 6 = |V_2|$.
2. **Invariant 2 (|E|)**: $|E_1| = 7$ (6 cycle edges + 1 chord) = $|E_2|$.
3. **Invariant 3 (Degree sequence)**:
   * In $G_1$: $\deg(1)=3, \deg(4)=3$, and $\deg(2)=\deg(3)=\deg(5)=\deg(6)=2$. Sequence: $(3, 3, 2, 2, 2, 2)$.
   * In $G_2$: $\deg(b)=3, \deg(e)=3$, and $\deg(a)=\deg(c)=\deg(d)=\deg(f)=2$. Sequence: $(3, 3, 2, 2, 2, 2)$. Matches!
4. **Invariant 4 (Subgraphs & Cycles)**:
   * Chord $(1,4)$ in $G_1$ splits $C_6$ into two cycles of length 4: $(1,2,3,4,1)$ and $(1,6,5,4,1)$.
   * Chord $(b,e)$ in $G_2$ splits $C_6$ into two cycles of length 4: $(b,c,d,e,b)$ and $(b,a,f,e,b)$. Matches!
5. **Construct Explicit Bijective Map $f: V_1 \to V_2$**:
   * Map degree 3 vertices: $f(1) = b$, $f(4) = e$.
   * Follow the path $1 \to 2 \to 3 \to 4$: Map $f(2) = c$, $f(3) = d$.
   * Follow the other path $1 \to 6 \to 5 \to 4$: Map $f(6) = a$, $f(5) = f$.
6. **Edge Verification**:
   $$(1,2) \to (b,c) \in E_2, \quad (2,3) \to (c,d) \in E_2, \quad (3,4) \to (d,e) \in E_2$$
   $$(4,5) \to (e,f) \in E_2, \quad (5,6) \to (f,a) \in E_2, \quad (6,1) \to (a,b) \in E_2$$
   $$(1,4) \to (b,e) \in E_2$$
   All 7 edges are preserved under $f$.
7. **Conclusion**: $f$ is a bijection that preserves adjacency $\implies$ **$G_1 \cong G_2$**.

---

### Archetype 3: Counting Walks of Length 2 and 3 via Adjacency Matrix
**Question**: A graph $G$ has adjacency matrix:
$$A = \begin{pmatrix} 0 & 1 & 1 & 0 \\ 1 & 0 & 1 & 1 \\ 1 & 1 & 0 & 1 \\ 0 & 1 & 1 & 0 \end{pmatrix}$$
1. Find the number of walks of length 2 from $v_1$ to $v_4$.
2. Find the number of closed walks of length 2 starting at $v_2$.
3. Find the number of triangles in $G$.

**Solution Template**:
1. **Walks of length 2 from $v_1$ to $v_4$**:
   $$(A^2)_{14} = \text{Row 1 of } A \cdot \text{Column 4 of } A = (0)(0) + (1)(1) + (1)(1) + (0)(0) = 0 + 1 + 1 + 0 = 2$$
   *(Intuition: $v_1$ and $v_4$ have 2 common neighbors: $v_2$ and $v_3$. The walks are $v_1 \to v_2 \to v_4$ and $v_1 \to v_3 \to v_4$.)*
2. **Closed walks of length 2 starting at $v_2$**:
   $$(A^2)_{22} = \deg(v_2) = \text{sum of Row 2} = 1 + 0 + 1 + 1 = 3$$
   *(The 3 walks are: $v_2 \to v_1 \to v_2$, $v_2 \to v_3 \to v_2$, $v_2 \to v_4 \to v_2$.)*
3. **Number of triangles**:
   * Compute $A^2$:
     $$A^2 = \begin{pmatrix} 2 & 1 & 1 & 2 \\ 1 & 3 & 2 & 1 \\ 1 & 2 & 3 & 1 \\ 2 & 1 & 1 & 2 \end{pmatrix}$$
   * Diagonal of $A^3$ is computed by taking dot product of Row $i$ of $A^2$ with Column $i$ of $A$:
     * $(A^3)_{11} = 2(0) + 1(1) + 1(1) + 2(0) = 2$
     * $(A^3)_{22} = 1(1) + 3(0) + 2(1) + 1(1) = 4$
     * $(A^3)_{33} = 1(1) + 2(1) + 3(0) + 1(1) = 4$
     * $(A^3)_{44} = 2(0) + 1(1) + 1(1) + 2(0) = 2$
   * $\text{Trace}(A^3) = 2 + 4 + 4 + 2 = 12$.
   * Number of triangles $= \frac{\text{Trace}(A^3)}{6} = \frac{12}{6} = \mathbf{2}$ triangles (specifically, $\{v_1, v_2, v_3\}$ and $\{v_2, v_3, v_4\}$).
