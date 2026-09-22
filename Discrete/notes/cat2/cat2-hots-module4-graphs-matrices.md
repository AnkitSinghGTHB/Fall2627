# ⚡ CAT-2 Master Crib: Module 4 — Graphs & Matrix Representations
**Course**: MAT2002 — Discrete Mathematics & Graph Theory  
**Faculty / Syllabus Scope**: CO4 / Module 4 (CAT-2 Strict Coverage)  
**Format**: Comprehensive, Rigorous, Fully Worked Examples, Theorems & Formal Proofs

---

## Table of Contents
1. [Fundamental Graph Terminology & Classifications](#1-fundamental-graph-terminology--classifications)
2. [Degrees, Degree Sequences & Havel-Hakimi Theorem](#2-degrees-degree-sequences--havel-hakimi-theorem)
3. [Bipartite Graphs & Kőnig's Odd-Cycle Theorem](#3-bipartite-graphs--kőnigs-odd-cycle-theorem)
4. [Graph Isomorphism & Preserved Invariants](#4-graph-isomorphism--preserved-invariants)
5. [Graph Complements & Self-Complementary Graphs](#5-graph-complements--self-complementary-graphs)
6. [Walks, Trails, Paths, Circuits, Cycles & Connectivity](#6-walks-trails-paths-circuits-cycles--connectivity)
7. [Eulerian & Hamiltonian Graphs](#7-eulerian--hamiltonian-graphs)
8. [Matrix Representations: Adjacency, Powers of $A$, and Incidence](#8-matrix-representations)
9. [Shortest Path Algorithm for Directed Graphs (Dijkstra)](#9-shortest-path-algorithm-for-directed-graphs-dijkstra)
10. [Comprehensive Classroom & Exam Solved HOTS Problems](#10-comprehensive-classroom--exam-solved-hots-problems)

---

## 1. Fundamental Graph Terminology & Classifications

### 1.1 Formal Definition of a Graph
An undirected graph $G$ is an ordered pair $G = (V, E)$ consisting of:
* **Vertex Set $V = V(G)$**: A non-empty finite set of vertices (or nodes). The cardinality $|V| = n$ (or $p$) is the **Order** of $G$.
* **Edge Set $E = E(G)$**: A set of unordered pairs of vertices $\{u, v\} \subseteq V$. The cardinality $|E| = m$ (or $q$) is the **Size** of $G$.

### 1.2 Graph Typology
* **Simple Graph**: No self-loops (edges from $u$ to $u$) and no parallel/multiple edges (more than one edge between the same pair of vertices).
* **Multigraph**: Contains parallel edges between pairs of vertices, but no self-loops.
* **Pseudograph**: May contain both self-loops and parallel edges. (A self-loop at vertex $v$ contributes **2** to $\deg(v)$).
* **Directed Graph (Digraph)**: Edges are ordered pairs $(u, v)$, representing directed arrows from source $u$ to destination $v$.

---

### 1.3 Special Graph Families

| Graph Family | Notation | Vertices ($n$) | Edges ($m$) | Regularity | Properties |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Complete Graph** | $K_n$ | $n$ | $\frac{n(n-1)}{2}$ | $(n-1)$-regular | Every pair of distinct vertices is adjacent. |
| **Cycle Graph** | $C_n$ ($n \ge 3$) | $n$ | $n$ | $2$-regular | A single closed loop of length $n$. Bipartite $\iff n$ is even. |
| **Path Graph** | $P_n$ | $n$ | $n - 1$ | Not regular | Linear sequence of $n-1$ edges. Max degree 2, 2 leaves (deg 1). |
| **Wheel Graph** | $W_n = C_n * K_1$ | $n + 1$ | $2n$ | Not regular | $C_n$ rim connected to 1 central hub vertex ($\deg(\text{hub}) = n$). |
| **Complete Bipartite** | $K_{r, s}$ | $r + s$ | $r \cdot s$ | Regular $\iff r = s$ | Vertices partitioned into $V_1$ ($|V_1|=r$) and $V_2$ ($|V_2|=s$). |
| **Hypercube Graph** | $Q_k$ | $2^k$ | $k \cdot 2^{k-1}$ | $k$-regular | Vertices are $k$-bit strings; edges connect strings differing in 1 bit. |

---

## 2. Degrees, Degree Sequences & Havel-Hakimi Theorem

### 2.1 Neighborhood and Degree
* **Open Neighborhood**: $N(v) = \{u \in V \mid (u, v) \in E\}$.
* **Closed Neighborhood**: $N[v] = N(v) \cup \{v\}$.
* **Degree**: $\deg(v) = |N(v)|$.
* **Extremal Degrees**: $\delta(G) = \min_{v \in V} \deg(v)$, and $\Delta(G) = \max_{v \in V} \deg(v)$.
* **$r$-Regular Graph**: A graph where $\forall v \in V, \; \deg(v) = r$.

---

### 2.2 Euler's Handshaking Lemma & Corollaries

#### Theorem 1 (Handshaking Lemma):
> In any undirected graph $G = (V, E)$:
> $$\sum_{v \in V} \deg(v) = 2 |E| = 2m$$
> *Proof*: Each edge $e = (u, v)$ connects exactly two vertices, contributing $1$ to $\deg(u)$ and $1$ to $\deg(v)$. Summing across all vertices counts every edge exactly twice. $\blacksquare$

#### Corollary 1 (Even Number of Odd-Degree Vertices):
> In any undirected graph, the number of vertices of odd degree is **always EVEN**.
> *Proof*: Partition $V$ into $V_{\text{even}}$ and $V_{\text{odd}}$:
> $$\sum_{v \in V_{\text{even}}} \deg(v) + \sum_{v \in V_{\text{odd}}} \deg(v) = 2m$$
> The right-hand side $2m$ is even, and $\sum_{v \in V_{\text{even}}} \deg(v)$ is a sum of even numbers (hence even).
> Therefore, $\sum_{v \in V_{\text{odd}}} \deg(v) = \text{Even} - \text{Even} = \text{Even}$.
> A sum of odd integers is even if and only if there is an **even count** of such integers. Thus, $|V_{\text{odd}}|$ must be even. $\blacksquare$

#### Corollary 2 (Handshaking in Digraphs):
> In any directed graph $D = (V, E)$:
> $$\sum_{v \in V} \deg^+(v) = \sum_{v \in V} \deg^-(v) = |E|$$
> Where $\deg^+(v)$ is the out-degree and $\deg^-(v)$ is the in-degree.

---

### 2.3 The Havel-Hakimi Criterion for Graphic Sequences
A sequence of non-negative integers $S = (d_1, d_2, \dots, d_n)$ in descending order ($d_1 \ge d_2 \ge \dots \ge d_n$) is called **graphic** if there exists a simple graph with $S$ as its degree sequence.

#### Havel-Hakimi Algorithm:
1. **Sanity Check 1**: Max degree $d_1 \le n - 1$. If $d_1 \ge n$, **REJECT** (not graphic).
2. **Sanity Check 2**: Degree sum $\sum d_i$ must be **EVEN**. If odd, **REJECT**.
3. **Reduction Step**: Delete the first element $d_1$.
4. Subtract $1$ from each of the next $d_1$ elements:
   $$S' = (d_2 - 1, d_3 - 1, \dots, d_{d_1 + 1} - 1, d_{d_1 + 2}, \dots, d_n)$$
5. If any element in $S'$ becomes negative, **REJECT** (not graphic).
6. Sort $S'$ in descending order.
7. Repeat until the sequence consists entirely of zeros (**ACCEPT $\implies$ Graphic**).

#### Quick Reference Table: Analysis of Classroom Degree Sequences
| Degree Sequence | Sum | Odd Count | Havel-Hakimi Reduction Steps | Graphic? |
| :--- | :---: | :---: | :--- | :---: |
| $(6,6,5,5,4,4,3,3)$ | 36 | 4 (Even) | $(5,4,4,3,3,3,2) \to (3,3,2,2,2,2) \to (2,2,2,1,1) \to (1,1,1,1) \to (0,0,0)$ | **YES ✅** |
| $(5,5,4,3,3,2,1)$ | 23 | 5 (Odd!) | Violates Handshaking Lemma ($\sum d_i = 23$ is odd) | **NO ❌** |
| $(3,3,3,3,2)$ | 14 | 4 (Even) | $(2,2,2,2) \to (1,1,2) \to (2,1,1) \to (0,0)$ | **YES ✅** |
| $(4,4,3,3,3)$ | 17 | 3 (Odd!) | Violates Handshaking Lemma ($\sum d_i = 17$ is odd) | **NO ❌** |
| $(4,3,3,2,2)$ | 14 | 2 (Even) | $(2,2,1,1) \to (1,0,1) \to (1,1,0) \to (0,0)$ | **YES ✅** |
| $(3,3,3,1)$ | 10 | 4 (Even) | $d_1 = 3$: $(2,2,0) \to d_1 = 2$: $(1,-1)$ (negative!) | **NO ❌** |

---

## 3. Bipartite Graphs & Kőnig's Odd-Cycle Theorem

### 3.1 Definition of Bipartite Graph
A graph $G = (V, E)$ is **bipartite** if its vertex set $V$ can be partitioned into two disjoint non-empty sets $V_1$ and $V_2$ ($V = V_1 \cup V_2$ and $V_1 \cap V_2 = \emptyset$) such that every edge in $E$ has one endpoint in $V_1$ and the other endpoint in $V_2$.
* No edge connects two vertices within the same partition set.

### 3.2 Kőnig's Theorem (Fundamental Characterization)
> **Theorem**: A graph $G$ is bipartite if and only if it contains **NO odd cycles** (all cycles in $G$ have even length).

```
         BIPARTITE GRAPH                       ODD CYCLE (NON-BIPARTITE)
       (V1 Red, V2 Blue)                           (3-Cycle Triangle)
       -----------------                       -------------------------
         v1(R) --- u1(B)                                 1(R)
           \        /                                   /    \
            \      /                                   /      \
             \    /                                  2(B) --- 3(Conflict!)
         v2(R) --- u2(B)
```

#### Verification Algorithm:
Use **2-Coloring (Breadth-First Search / BFS)**:
1. Color root vertex RED.
2. Color all adjacent neighbors BLUE.
3. For each visited vertex, color its unvisited neighbors with the opposite color.
4. If at any step an edge connects two vertices of the **same color**, an odd cycle exists $\implies \mathbf{G}$ is NOT bipartite.

---

## 4. Graph Isomorphism & Preserved Invariants

### 4.1 Formal Definition
Two simple graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ are **isomorphic** (denoted $G_1 \cong G_2$) if there exists a **bijective function**:
$$f: V_1 \to V_2$$
such that for every pair of vertices $u, v \in V_1$:
$$(u, v) \in E_1 \iff (f(u), f(v)) \in E_2$$

---

### 4.2 Theorem 3: Degree Preservation under Isomorphism
> **Theorem**: If $f: V_1 \to V_2$ is a graph isomorphism from $G_1$ to $G_2$, then for every vertex $v \in V_1$:
> $$\deg_{G_2}(f(v)) = \deg_{G_1}(v)$$

#### Formal Proof:
1. Let $v \in V_1$ be an arbitrary vertex with degree $\deg_{G_1}(v) = k$.
2. By definition of degree, the open neighborhood $N_{G_1}(v) = \{u \in V_1 \mid (u, v) \in E_1\}$ has size $|N_{G_1}(v)| = k$.
3. Let $N_{G_1}(v) = \{u_1, u_2, \dots, u_k\}$.
4. Because $f$ is an isomorphism, $(u_i, v) \in E_1 \implies (f(u_i), f(v)) \in E_2$ for all $i \in \{1, \dots, k\}$.
5. Because $f$ is injective (one-to-one), the images $f(u_1), f(u_2), \dots, f(u_k)$ are distinct vertices in $V_2$, all adjacent to $f(v)$. Hence $\deg_{G_2}(f(v)) \ge k$.
6. Conversely, if $w \in V_2$ is adjacent to $f(v)$ in $G_2$, because $f$ is surjective (onto), $\exists u \in V_1$ such that $f(u) = w$.
7. Since $f$ preserves non-adjacency: $(f(u), f(v)) \in E_2 \implies (u, v) \in E_1 \implies u \in N_{G_1}(v)$.
8. Thus, the neighborhood mapping $f: N_{G_1}(v) \to N_{G_2}(f(v))$ is a bijection, which implies:
   $$|N_{G_2}(f(v))| = |N_{G_1}(v)| \implies \mathbf{\deg_{G_2}(f(v)) = \deg_{G_1}(v)} \quad \blacksquare$$

---

### 4.3 Complete Catalog of Preserved Graph Invariants
If $G_1 \cong G_2$, they MUST have identical:
1. **Order**: $|V(G_1)| = |V(G_2)|$.
2. **Size**: $|E(G_1)| = |E(G_2)|$.
3. **Degree Sequence**: Sorted degree lists must be strictly identical.
4. **Number of Connected Components**: $c(G_1) = c(G_2)$.
5. **Cycle Spectrum**: Number of cycles of length $k$ ($C_3, C_4, C_5, \dots$) must be identical.
6. **Bipartiteness**: $G_1$ is bipartite $\iff G_2$ is bipartite.
7. **Complement Isomorphism**: $\overline{G_1} \cong \overline{G_2}$.
8. **Bridge / Cut-Edge Count**: Same number of bridges and cut-vertices.

> **Exam Warning**: Matching degree sequences is a **necessary condition**, NOT a sufficient condition! (e.g., $C_6$ and $2C_3$ have identical degree sequences $(2,2,2,2,2,2)$, but $C_6 \not\cong 2C_3$ because $c(C_6)=1 \ne c(2C_3)=2$).

---

## 5. Graph Complements & Self-Complementary Graphs

### 5.1 Complement of a Graph $\overline{G}$
For a simple graph $G = (V, E)$, its **complement** $\overline{G} = (V, \overline{E})$ has the same vertex set $V$, and an edge $(u, v) \in \overline{E} \iff (u, v) \notin E$.
* **Edge Sum Formula**:
  $$|E(G)| + |E(\overline{G})| = \binom{n}{2} = \frac{n(n-1)}{2}$$
* **Complement Degree Formula**:
  $$\forall v \in V: \quad \deg_{\overline{G}}(v) = (n - 1) - \deg_G(v)$$
* **Fundamental Complement Isomorphism Theorem**:
  $$G_1 \cong G_2 \iff \overline{G_1} \cong \overline{G_2}$$

---

### 5.2 Self-Complementary Graphs
A simple graph $G$ is called **self-complementary** if $G \cong \overline{G}$.

#### Theorem (Permissible Orders for Self-Complementary Graphs):
> A self-complementary graph of order $n$ exists if and only if:
> $$n \equiv 0 \pmod 4 \quad \text{or} \quad n \equiv 1 \pmod 4$$
> *(i.e., $n = 4k$ or $n = 4k + 1$ for some non-negative integer $k$)*.

#### Formal Proof:
1. By definition, $G \cong \overline{G} \implies |E(G)| = |E(\overline{G})| = q$.
2. Substituting into the edge sum formula:
   $$q + q = \binom{n}{2} \implies 2q = \frac{n(n-1)}{2} \implies \mathbf{q = \frac{n(n-1)}{4}}$$
3. The number of edges $q$ must be an integer ($q \in \mathbb{Z}$).
4. Therefore, $n(n - 1)$ must be divisible by 4.
5. In the product $n(n - 1)$, one factor is even and the other is odd.
   * If $n$ is even, $n - 1$ is odd, so $4 \mid n \implies \mathbf{n \equiv 0 \pmod 4}$.
   * If $n$ is odd, $n - 1$ is even, so $4 \mid (n - 1) \implies \mathbf{n \equiv 1 \pmod 4}$.
6. Thus, no self-complementary graph can exist for orders $n \equiv 2 \pmod 4$ (like $n = 2, 6, 10$) or $n \equiv 3 \pmod 4$ (like $n = 3, 7, 11$). $\blacksquare$

#### Explicit Constructions:
* **$n = 1$**: Single vertex $K_1$ ($q = 0$).
* **$n = 4$**: The Path Graph $P_4$ ($q = 3$). ($P_4 \cong \overline{P_4}$).
* **$n = 5$**: The 5-Cycle Graph $C_5$ ($q = 5$). ($\overline{C_5} \cong C_5$).

---

## 6. Walks, Trails, Paths, Circuits, Cycles & Connectivity

### 6.1 Traversal Taxonomy

| Term | Edge Repetition | Vertex Repetition | Open / Closed |
| :--- | :---: | :---: | :---: |
| **Walk** | Allowed | Allowed | Either |
| **Trail** | **NO** (All edges distinct) | Allowed | Open |
| **Path (Simple Path)** | **NO** (All edges distinct) | **NO** (All vertices distinct) | Open |
| **Closed Walk** | Allowed | Allowed | Closed ($v_0 = v_k$) |
| **Circuit** | **NO** (All edges distinct) | Allowed (except endpoints) | Closed ($v_0 = v_k$) |
| **Cycle (Simple Cycle)** | **NO** (All edges distinct) | **NO** (except $v_0 = v_k$) | Closed ($v_0 = v_k$) |

---

### 6.2 Connectivity & Components
* A graph $G$ is **connected** if there exists a path between every pair of distinct vertices.
* A maximal connected subgraph of $G$ is called a **connected component**.
* **Cut-Vertex**: A vertex whose removal increases the number of connected components.
* **Bridge (Cut-Edge)**: An edge whose removal increases the number of connected components. (An edge $e$ is a bridge $\iff e$ does NOT lie on any cycle).

#### Proposition 1 (Minimum Degree Bound for Connectivity):
> **Proposition**: If a simple graph $G$ has $n$ vertices and minimum degree $\delta(G) \ge \frac{n - 1}{2}$, then **$G$ is connected**.

#### Formal Proof:
1. Assume for contradiction that $G$ is disconnected.
2. Then $G$ has at least two connected components, say $C_1$ and $C_2$.
3. Let $u \in C_1$ and $v \in C_2$.
4. Since $u$ and $v$ belong to different components, there is no path between $u$ and $v$. In particular, $u$ and $v$ cannot share any common neighbor:
   $$N(u) \cap N(v) = \emptyset$$
5. Furthermore, $u$ and $v$ are non-adjacent: $u \notin N(v)$ and $v \notin N(u)$.
6. Therefore, the sets $\{u\}$, $\{v\}$, $N(u)$, and $N(v)$ are mutually disjoint subsets of $V$.
7. Summing their sizes:
   $$|V| \ge |\{u\}| + |\{v\}| + |N(u)| + |N(v)| = 1 + 1 + \deg(u) + \deg(v)$$
   $$n \ge 2 + \deg(u) + \deg(v)$$
8. By hypothesis, $\deg(u) \ge \delta(G) \ge \frac{n - 1}{2}$ and $\deg(v) \ge \delta(G) \ge \frac{n - 1}{2}$:
   $$n \ge 2 + \frac{n - 1}{2} + \frac{n - 1}{2} = 2 + (n - 1) = n + 1$$
   $$n \ge n + 1 \quad (\text{CONTRADICTION!})$$
9. Therefore, $G$ cannot be disconnected. $G$ must be **connected**. $\blacksquare$

---

## 7. Eulerian & Hamiltonian Graphs

### 7.1 Eulerian Graphs
* **Euler Trail**: A trail that traverses every edge of graph $G$ exactly once.
* **Euler Circuit (Tour)**: A closed trail that traverses every edge of graph $G$ exactly once and returns to the start vertex.
* **Eulerian Graph**: A graph containing an Euler circuit.

#### Euler's Theorems:
1. **Euler Circuit Criterion**: A connected graph $G$ has an Euler circuit $\iff$ **every vertex has EVEN degree**.
2. **Euler Trail Criterion**: A connected graph $G$ has an Euler trail (from $u$ to $v$) $\iff$ **exactly TWO vertices have odd degree** (which are the start and end vertices $u$ and $v$).

---

### 7.2 Hamiltonian Graphs
* **Hamiltonian Path**: A path that visits every vertex in $G$ exactly once.
* **Hamiltonian Cycle**: A closed cycle that visits every vertex in $G$ exactly once (except returning to the start).
* **Hamiltonian Graph**: A graph containing a Hamiltonian cycle.

#### Sufficient Conditions for Hamiltonian Graphs:
1. **Dirac's Theorem (1952)**: If $G$ is a simple graph with $n \ge 3$ vertices such that:
   $$\forall v \in V: \quad \deg(v) \ge \frac{n}{2}$$
   then $G$ is Hamiltonian.
2. **Ore's Theorem (1960)**: If $G$ is a simple graph with $n \ge 3$ vertices such that for every pair of non-adjacent vertices $u, v$:
   $$\deg(u) + \deg(v) \ge n$$
   then $G$ is Hamiltonian.

---

## 8. Matrix Representations

### 8.1 Adjacency Matrix $A(G)$ for Undirected Graphs
For a graph $G$ with vertices ordered as $v_1, v_2, \dots, v_n$, the **Adjacency Matrix** $A = [a_{ij}]_{n \times n}$ is defined by:
$$a_{ij} = \begin{cases} 1 & \text{if } (v_i, v_j) \in E \\ 0 & \text{otherwise} \end{cases}$$

#### Mathematical Invariants:
1. **Symmetry**: $A = A^T$ ($a_{ij} = a_{ji}$).
2. **Zero Diagonal**: $a_{ii} = 0$ for all $i$ (simple graphs have no loops).
3. **Row and Column Sums**: The $i$-th row sum equals $\deg(v_i)$:
   $$\sum_{j=1}^n a_{ij} = \deg(v_i)$$
4. **Total Matrix Sum**: $\sum_{i=1}^n \sum_{j=1}^n a_{ij} = 2m$.

---

### 8.2 Powers of Adjacency Matrix: Walks of Length $k$
> **Theorem**: Let $A$ be the adjacency matrix of a graph $G$. Then the $(i, j)$-th entry of the matrix power $A^k$, denoted $(A^k)_{ij}$, is equal to the **exact number of walks of length $k$** from vertex $v_i$ to vertex $v_j$.

* **$A^2[i, j]$**: Counts walks of length 2 from $v_i$ to $v_j$ (equals the number of common neighbors of $v_i$ and $v_j$).
* **$A^2[i, i]$**: Diagonal entry $(A^2)_{ii} = \deg(v_i)$ (walks of length 2 from $v_i$ back to $v_i$ traverse an edge and return).
* **$\text{Trace}(A^3) = \sum_{i=1}^n (A^3)_{ii} = 6 \times (\text{Number of Triangles in } G)$**.

---

### 8.3 Digraph Adjacency Matrix (Signed Skew-Symmetric vs. Standard Binary)
Two formulations appear in exam questions:
1. **Standard Binary Digraph Matrix**:
   $$a_{ij} = 1 \quad \text{if directed edge } (v_i \to v_j) \in E, \quad \text{else } 0$$
   * Row $i$ sum $= \deg^+(v_i)$ (out-degree).
   * Column $j$ sum $= \deg^-(v_j)$ (in-degree).
2. **Signed Skew-Symmetric Formulation (Class Notes Convention)**:
   $$a_{ij} = \begin{cases} +1 & \text{if directed edge goes OUT from } v_i \text{ to } v_j \\ -1 & \text{if directed edge comes IN to } v_i \text{ from } v_j \\ 0 & \text{if no edge between } v_i \text{ and } v_j \end{cases}$$
   * Skew-symmetric: $a_{ji} = -a_{ij}$.

---

### 8.4 Incidence Matrix $I(G)$
For a graph with $n$ vertices $v_1, \dots, v_n$ and $m$ edges $e_1, \dots, e_m$, the **Incidence Matrix** $I(G) = [b_{ij}]_{n \times m}$ is defined by:
$$b_{ij} = \begin{cases} 1 & \text{if vertex } v_i \text{ is incident to edge } e_j \\ 0 & \text{otherwise} \end{cases}$$

#### Invariants of Incidence Matrix:
1. **Column Sum = 2**: Every column $e_j$ has exactly two 1's (the two endpoints of that edge):
   $$\sum_{i=1}^n b_{ij} = 2 \quad \forall j$$
2. **Row Sum = $\deg(v_i)$**: The $i$-th row sum equals the degree of vertex $v_i$:
   $$\sum_{j=1}^m b_{ij} = \deg(v_i)$$
3. **Total Sum**: $\sum_{i=1}^n \sum_{j=1}^m b_{ij} = 2m$.

---

## 9. Shortest Path Algorithm for Directed Graphs (Dijkstra)

### Algorithmic Execution Template
1. Initialize $d[s] = 0$, $d[v] = \infty$ for all $v \ne s$, and permanent set $S = \emptyset$.
2. While $S \ne V$:
   * Select $u \in V \setminus S$ with minimum tentative label $d[u]$.
   * Add $u$ to $S$ ($u$ is now permanent).
   * For every directed edge $(u \to v)$ with $v \notin S$:
     $$\text{If } d[u] + w(u, v) < d[v], \quad \text{update } d[v] = d[u] + w(u, v), \quad \pi[v] = u$$
3. If all remaining vertices have $d[v] = \infty$, they are **unreachable** from $s$.

---

## 10. Comprehensive Classroom & Exam Solved HOTS Problems

### Problem 1: Minimum Vertices for Given Edges (Registration Number Problem)
**Question**: A simple undirected graph has $q = 242$ edges. What is the minimum number of vertices $n$ required to construct this graph?

#### Solution:
1. In any simple graph on $n$ vertices, the maximum possible number of edges occurs in the complete graph $K_n$:
   $$q_{\text{max}} = \binom{n}{2} = \frac{n(n-1)}{2}$$
2. For the graph to exist:
   $$\frac{n(n-1)}{2} \ge 242 \implies n(n-1) \ge 484$$
3. Solve quadratic $n^2 - n - 484 \ge 0$:
   $$n \approx \frac{1 + \sqrt{1 + 4(484)}}{2} = \frac{1 + \sqrt{1937}}{2} \approx \frac{1 + 44.01}{2} = 22.505$$
4. Check integers:
   * $n = 22 \implies \frac{22 \times 21}{2} = 231 < 242$ (Insufficient!).
   * $n = 23 \implies \frac{23 \times 22}{2} = 253 \ge 242$ (Sufficient!).
5. **Answer**: Minimum number of vertices required is **$n = 23$**.

---

### Problem 2: Walks of Length 2 Using Matrix Multiplication
**Question**: Let $G$ have adjacency matrix:
$$A = \begin{pmatrix} 0 & 1 & 1 & 0 \\ 1 & 0 & 1 & 1 \\ 1 & 1 & 0 & 1 \\ 0 & 1 & 1 & 0 \end{pmatrix}$$
Find the number of walks of length 2 between vertex 1 and vertex 4.

#### Solution:
1. The number of walks of length 2 between $v_1$ and $v_4$ is given by the $(1, 4)$-th entry of $A^2$:
   $$(A^2)_{14} = \sum_{k=1}^4 a_{1k} a_{k4} = a_{11}a_{14} + a_{12}a_{24} + a_{13}a_{34} + a_{14}a_{44}$$
2. Substitute values from Row 1 and Column 4:
   * Row 1: $(0, 1, 1, 0)$
   * Column 4: $\begin{pmatrix} 0 \\ 1 \\ 1 \\ 0 \end{pmatrix}$
3. Dot product:
   $$(A^2)_{14} = (0)(0) + (1)(1) + (1)(1) + (0)(0) = 0 + 1 + 1 + 0 = \mathbf{2}$$
4. The two walks of length 2 are:
   * $v_1 \to v_2 \to v_4$
   * $v_1 \to v_3 \to v_4$
5. **Answer**: Exactly **2 walks** of length 2 exist between $v_1$ and $v_4$.
