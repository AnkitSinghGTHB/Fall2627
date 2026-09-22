# Graph Theory: Isomorphism to Matrix Representations
## Complete Consolidated Class Notes, Formal Proofs & Gap-Filling Guide

---

## Table of Contents
1. [Graph Isomorphism](#1-graph-isomorphism)
   - [1.1 Formal Definition & Graph Invariants](#11-formal-definition--graph-invariants)
   - [1.2 Theorem 3: Degree Preservation under Isomorphism (Full Proof)](#12-theorem-3-degree-preservation-under-isomorphism)
   - [1.3 Non-Isomorphism Case Study: $K_{3,3}$ vs. Triangular Prism](#13-non-isomorphism-case-study-k_33-vs-triangular-prism)
   - [1.4 Alternative Bipartite Layout of $K_{3,3}$ ($G_1 \cong G_3$)](#14-alternative-bipartite-layout-of-k_33-g_1-cong-g_3)
   - [1.5 Three Foundational Non-Isomorphism Class Exercises](#15-three-foundational-non-isomorphism-class-exercises)
     - [Exercise 1: Same $|V|$ and Same $|E|$, But Non-Isomorphic](#exercise-1-same-v-and-same-e-but-non-isomorphic)
     - [Exercise 2: Even $|V|$, Odd $|E|$, and $\delta(G) \ge 2$](#exercise-2-even-v-odd-e-and-deltag-ge-2)
     - [Exercise 3: Identical Degree Sequence with $\ge 2$ Vertices of Degree 2](#exercise-3-identical-degree-sequence-with-ge-2-vertices-of-degree-2)
2. [Self-Complementary Graphs](#2-self-complementary-graphs)
   - [2.1 Definition](#21-definition)
   - [2.2 Proof: Order of Self-Complementary Graphs ($p = 4k$ or $4k + 1$)](#22-proof-order-of-self-complementary-graphs-p--4k-or-4k--1)
   - [2.3 Explicit Constructions for Small Orders ($n = 1, 4, 5$)](#23-explicit-constructions-for-small-orders-n--1-4-5)
3. [Walks, Trails, Paths, Circuits, and Cycles](#3-walks-trails-paths-circuits-and-cycles)
   - [3.1 Taxonomy of Graph Traversals](#31-taxonomy-of-graph-traversals)
   - [3.2 Summary Comparison Table](#32-summary-comparison-table)
   - [3.3 Comprehensive Walk/Trail/Path Analysis on Class Graph](#33-comprehensive-walktrailpath-analysis-on-class-graph)
4. [Graph Connectivity & Components](#4-graph-connectivity--components)
   - [4.1 Path Length, Shortest Paths, and Distance Metrics](#41-path-length-shortest-paths-and-distance-metrics)
   - [4.2 Connected Graphs & Connected Components](#42-connected-graphs--connected-components)
   - [4.3 Class Exercise: Component Counting Across 7 Test Graphs](#43-class-exercise-component-counting-across-7-test-graphs)
   - [4.4 Proposition 1: Minimum Degree Bound for Connectivity (Full Proof)](#44-proposition-1-minimum-degree-bound-for-connectivity)
5. [Dijkstra's Shortest Path Algorithm](#5-dijkstras-shortest-path-algorithm)
   - [5.1 Algorithmic Framework (Permanent vs. Tentative Labels)](#51-algorithmic-framework-permanent-vs-tentative-labels)
   - [5.2 Problem 1: 7-Vertex Directed Graph (Full 6-Iteration Trace & Tree)](#52-problem-1-7-vertex-directed-graph-full-6-iteration-trace)
   - [5.3 Problem 2: Five Cities Road Network (Complete 4-Iteration Trace & Tree)](#53-problem-2-five-cities-road-network-complete-4-iteration-trace)
6. [Matrix Representations of Graphs](#6-matrix-representations-of-graphs)
   - [6.1 Adjacency Matrix for Undirected Graphs](#61-adjacency-matrix-for-undirected-graphs)
     - [Definition & Algebraic Properties](#definition--algebraic-properties)
     - [6-Vertex Detailed Example from Notes](#6-vertex-detailed-example-from-notes)
     - [Theorem: Powers of Adjacency Matrix and Walks of Length $k$](#theorem-powers-of-adjacency-matrix-and-walks-of-length-k)
   - [6.2 Adjacency Matrix for Directed Graphs (Digraphs)](#62-adjacency-matrix-for-directed-graphs-digraphs)
     - [Signed Skew-Symmetric Formulation (Class Notes Convention)](#signed-skew-symmetric-formulation-class-notes-convention)
     - [Standard Binary Formulation (Comparison)](#standard-binary-formulation-comparison)
     - [4-Vertex Digraph Worked Example](#4-vertex-digraph-worked-example)
   - [6.3 Incidence Matrix of a Graph ($I(G)$ or $B_{	ext{inc}}(G)$)](#63-incidence-matrix-of-a-graph-ig-or-b_textincg)
     - [Definition & Matrix Dimensions](#definition--matrix-dimensions)
     - [Fundamental Invariants (Column Sums, Row Sums, Total Sum)](#fundamental-invariants-column-sums-row-sums-total-sum)
7. [Comprehensive Exam Problem: Complement Matrices & Isomorphism](#7-comprehensive-exam-problem-complement-matrices--isomorphism)
   - [7.1 Problem Statement & Initial Adjacency Matrices](#71-problem-statement--initial-adjacency-matrices)
   - [7.2 Reconstruction of Graphs $G_1$ and $G_2$](#72-reconstruction-of-graphs-g_1-and-g_2)
   - [7.3 Construction of Complement Graphs $G_1^c$ and $G_2^c$](#73-construction-of-complement-graphs-g_1c-and-g_2c)
   - [7.4 Formal Proof of Isomorphism Between $G_1^c$ and $G_2^c$](#74-formal-proof-of-isomorphism-between-g_1c-and-g_2c)
   - [7.5 Adjacency Matrices of Complements $A(G_1^c)$ and $A(G_2^c)$](#75-adjacency-matrices-of-complements-ag_1c-and-ag_2c)
   - [7.6 Incidence Matrices of Complements $I(G_1^c)$ and $I(G_2^c)$](#76-incidence-matrices-of-complements-ig_1c-and-ig_2c)

---

# 1. Graph Isomorphism

## 1.1 Formal Definition & Graph Invariants
Two simple graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ are said to be **isomorphic** (denoted $G_1 \cong G_2$) if there exists a **bijective function**:
$$f: V_1 	o V_2$$
such that for any pair of vertices $u, v \in V_1$:
$$\{u, v\} \in E_1 \iff \{f(u), f(v)\} \in E_2$$

The map $f$ is called an **isomorphism** from $G_1$ to $G_2$. If no such bijective mapping exists, the graphs are **non-isomorphic** ($G_1 
ot\cong G_2$).

### Fundamental Graph Invariants:
An invariant is a structural property that must be preserved under isomorphism. If $G_1 \cong G_2$:
1. **Order**: $|V(G_1)| = |V(G_2)|$
2. **Size**: $|E(G_1)| = |E(G_2)|$
3. **Degree Sequence**: The sorted list of vertex degrees must be identical.
4. **Cycle Structure**: $G_1$ and $G_2$ must have the exact same number of cycles of each length $k$.
5. **Connectedness & Bipartiteness**: If $G_1$ is connected or bipartite, $G_2$ must also be connected or bipartite.

---

## 1.2 Theorem 3: Degree Preservation under Isomorphism

> **Theorem 3**: Let $f: V_1 	o V_2$ be an isomorphism from graph $G_1 = (V_1, E_1)$ to graph $G_2 = (V_2, E_2)$. Then for every vertex $v \in V_1$:
> $$\deg(v) = \deg(f(v))$$

### Formal Proof:
1. Let $v \in V_1$ and denote its open neighborhood in $G_1$ by:
   $$N(v) = \{u \in V_1 \mid \{u, v\} \in E_1\}$$
2. In a simple graph, the degree of $v$ is the cardinality of its neighborhood: $\deg(v) = |N(v)|$.
3. By the definition of isomorphism:
   $$u \in N(v) \iff \{u, v\} \in E_1 \iff \{f(u), f(v)\} \in E_2 \iff f(u) \in N(f(v))$$
4. Therefore, the restricted function $f|_{N(v)}: N(v) 	o N(f(v))$ maps neighbors of $v$ in $G_1$ directly to neighbors of $f(v)$ in $G_2$.
5. Because $f$ is a bijection on $V_1$:
   - It is injective (one-to-one), so distinct neighbors in $N(v)$ map to distinct neighbors in $N(f(v))$.
   - It is surjective (onto), because every neighbor $w \in N(f(v))$ must be the image $f(u)$ of some vertex $u \in V_1$ where $\{u, v\} \in E_1$.
6. Consequently, $|N(v)| = |N(f(v))|$, which proves:
   $$\deg(v) = \deg(f(v)) \quad lacksquare$$

> **Note**: Two isomorphic graphs have the same number of vertices and the same number of edges. It also follows from Theorem 3 that two isomorphic graphs have an equal number of vertices with a given degree (i.e., identical degree sequences).

---

## 1.3 Non-Isomorphism Case Study: $K_{3,3}$ vs. Triangular Prism

Consider the two 6-vertex, 3-regular graphs from the notes:
* **Graph $G_1$**: Hexagon cycle $a - b - c - d - e - f - a$ plus three main diagonals $\{a, d\}$, $\{b, e\}$, and $\{c, f\}$.
* **Graph $G_2$**: Triangular prism consisting of two disjoint triangles $\{1, 2, 6\}$ and $\{4, 3, 5\}$ connected by vertical edges $\{1, 4\}$, $\{2, 3\}$, and $\{6, 5\}$.

```text
       Graph G1:                             Graph G2:
           a                                     1
         / | \                                 / |         f  |  b                               6  |  2
        |  |  |                               |  |  |
        |  |  |                               |  |  |
        e  |  c                               5  |  3
         \ | /                                 \ | /
           d                                     4
```

### Invariant Verification & Comparison:
| Invariant | Graph $G_1$ | Graph $G_2$ | Preserved? |
|:----------|:-----------:|:-----------:|:----------:|
| Number of Vertices $|V|$ | 6 | 6 | Yes |
| Number of Edges $|E|$ | 9 | 9 | Yes |
| Degree Sequence | $(3, 3, 3, 3, 3, 3)$ | $(3, 3, 3, 3, 3, 3)$ | Yes |
| Bipartite? | **Yes** ($V = \{a, c, e\} \cup \{b, d, f\}$) | **No** (contains odd cycles) | **NO** |
| 3-Cycles (Triangles) | **0** | **2** ($\{1, 2, 6\}$ and $\{3, 4, 5\}$) | **NO** |

**Conclusion**: Because cycle length and bipartiteness are graph invariants, $G_1 
ot\cong G_2$.

---

## 1.4 Alternative Bipartite Layout of $K_{3,3}$ ($G_1 \cong G_3$)
In the notebook, graph $G_3$ is drawn in standard complete bipartite form with partition sets $\{p, q, r\}$ and $\{s, t, u\}$:

```text
       p --------- s
        \ \     / /
         \ \   / /
          \ \ / /
       q --X-X-X-- t
          / / \          / /   \         / /     \        r --------- u
```

* Every vertex in $\{p, q, r\}$ is adjacent to every vertex in $\{s, t, u\}$.
* By mapping:
  $$p \mapsto a, \quad q \mapsto c, \quad r \mapsto e, \quad s \mapsto b, \quad t \mapsto f, \quad u \mapsto d$$
  we find an exact bijection preserving all 9 edges.
* Hence:
  $$G_1 \cong G_3$$
* Since $G_1 
ot\cong G_2$ and $G_1 \cong G_3$, it follows immediately that:
  $$G_2 
ot\cong G_3$$

---

## 1.5 Three Foundational Non-Isomorphism Class Exercises

### Exercise 1: Same $|V|$ and Same $|E|$, But Non-Isomorphic
**Problem**: Give an example of graphs with the same number of vertices and edges that are not isomorphic.

* **Graph A (Paw Graph)**: Triangle with a pendant tail.
  - $V = \{1, 2, 3, 4\}$, $|V| = 4$.
  - $E = \{\{1, 2\}, \{2, 3\}, \{3, 1\}, \{3, 4\}\}$, $|E| = 4$.
  - Degrees: $d(3)=3, \; d(1)=2, \; d(2)=2, \; d(4)=1$. Degree sequence: $(3, 2, 2, 1)$.
* **Graph B (4-Cycle $C_4$)**:
  - $V = \{a, b, c, d\}$, $|V| = 4$.
  - $E = \{\{a, b\}, \{b, c\}, \{c, d\}, \{d, a\}\}$, $|E| = 4$.
  - Degrees: $d(a)=d(b)=d(c)=d(d)=2$. Degree sequence: $(2, 2, 2, 2)$.

```text
       Graph A (Paw):                   Graph B (C4):
          1                                 a ------- b
         / \                                |         |
        2---3 --- 4                         |         |
                                            d ------- c
```
* **Distinction**: Degree sequences differ, so $A 
ot\cong B$.

---

### Exercise 2: Even $|V|$, Odd $|E|$, and $\delta(G) \ge 2$
**Problem**: Give an example of non-isomorphic graphs with an even number of vertices, an odd number of edges, and minimum degree $\delta(G) \ge 2$.

* **Parameters**: $|V| = 6$ (even), $|E| = 7$ (odd), $\delta \ge 2$.
* **Graph $H_1$**: 6-cycle with a chord between vertices at distance 3 (no 3-cycles).
  - Edges: $(1-2-3-4-5-6-1)$ plus diagonal $\{1, 4\}$.
  - Vertices: $d(1)=3, d(4)=3$, and $d(2)=d(3)=d(5)=d(6)=2$.
  - Minimum degree: $\delta = 2$.
  - Cycles: Two 4-cycles $(1-2-3-4)$ and $(1-6-5-4)$. **Zero triangles**.
* **Graph $H_2$**: 6-cycle with a chord between vertices at distance 2 (contains a 3-cycle).
  - Edges: $(a-b-c-d-e-f-a)$ plus chord $\{a, c\}$.
  - Vertices: $d(a)=3, d(c)=3$, and $d(b)=d(d)=d(e)=d(f)=2$.
  - Minimum degree: $\delta = 2$.
  - Cycles: **One triangle** $(a-b-c)$ and one 5-cycle $(a-c-d-e-f)$.

```text
       Graph H1 (Girth 4):                Graph H2 (Contains Triangle):
               1                                     a
             / | \                                 /               6  |  2                               f     b
            |  |  |                               |     |
            5  |  3                               e     c
             \ | /                                 \   /
               4                                     d
```
* **Distinction**: Although $|V|=6$, $|E|=7$, and $\delta=2$ for both, $H_2$ has a 3-cycle while $H_1$ has no 3-cycles. Hence, $H_1 
ot\cong H_2$.

---

### Exercise 3: Identical Degree Sequence with $\ge 2$ Vertices of Degree 2
**Problem**: Give an example of non-isomorphic graphs with the same degree sequence having at least two vertices of degree 2.

* **Solution**: The pair $H_1$ and $H_2$ constructed in Exercise 2 satisfies all conditions:
  - Both share the degree sequence $(3, 3, 2, 2, 2, 2)$.
  - Both contain four vertices of degree 2 ($\ge 2$).
  - As proved above, $H_1 
ot\cong H_2$ due to differing cycle invariants.

---

# 2. Self-Complementary Graphs

## 2.1 Definition
A simple graph $G$ is called **self-complementary** if it is isomorphic to its own complement:
$$G \cong G^c$$

---

## 2.2 Proof: Order of Self-Complementary Graphs ($p = 4k$ or $4k + 1$)

> **Theorem**: If a $(p, q)$ graph $G$ is self-complementary, then its order $p$ is of the form $p = 4k$ or $p = 4k + 1$ for some integer $k \ge 0$.

### Formal Proof:
1. Let $|V(G)| = p$ and $|E(G)| = q$.
2. By the definition of the graph complement, $V(G^c) = V(G)$, so $|V(G^c)| = p$.
3. Any pair of vertices is an edge in exactly one of $G$ or $G^c$. Therefore:
   $$|E(G)| + |E(G^c)| = |E(K_p)| = inom{p}{2} = rac{p(p - 1)}{2}$$
4. Since $G \cong G^c$, isomorphism preserves the number of edges:
   $$|E(G)| = |E(G^c)| = q$$
5. Substituting this into the equation:
   $$q + q = rac{p(p - 1)}{2} \implies 2q = rac{p(p - 1)}{2} \implies q = rac{p(p - 1)}{4}$$
6. Because the number of edges $q$ must be an integer:
   $$4 \mid p(p - 1)$$
7. The terms $p$ and $p - 1$ are consecutive integers, which implies they are coprime:
   $$\gcd(p, p - 1) = 1$$
8. Therefore, the factor of 4 cannot be distributed between them; it must divide one of the factors entirely:
   - **Case 1**: $4 \mid p \implies p = 4k$ for some integer $k$.
   - **Case 2**: $4 \mid (p - 1) \implies p - 1 = 4k \implies p = 4k + 1$ for some integer $k$.
9. Hence, $p$ is either $4k$ or $4k + 1$. $lacksquare$

---

## 2.3 Explicit Constructions for Small Orders ($n = 1, 4, 5$)

| $k$ | Form | Order ($p$) | Size $q = rac{p(p-1)}{4}$ | Graph Structure |
|:---:|:----:|:-----------:|:---------------------------:|:----------------|
|  0  | $4k+1$ | 1 | 0 | Trivial graph $K_1$ |
|  1  | $4k$   | 4 | 3 | Path graph on 4 vertices ($P_4$) |
|  1  | $4k+1$ | 5 | 5 | 5-Cycle ($C_5$) |
|  2  | $4k$   | 8 | 14 | 8-vertex self-complementary graph |
|  2  | $4k+1$ | 9 | 18 | 9-vertex self-complementary graph |

### Verification for $n = 4$ ($P_4$):
* Let $V = \{a, b, c, d\}$ and $E(G) = \{\{a, b\}, \{b, c\}, \{c, d\}\}$ (a path of length 3).
* Complete graph $K_4$ has 6 edges.
* The missing edges form $G^c$:
  $$E(G^c) = \{\{a, c\}, \{a, d\}, \{b, d\}\}$$
* $G^c$ forms the path $b - d - a - c$, which is isomorphic to $P_4$ under the bijection:
  $$f(a) = b, \quad f(b) = d, \quad f(c) = a, \quad f(d) = c$$

### Verification for $n = 5$ ($C_5$):
* Let $V = \{1, 2, 3, 4, 5\}$ and $E(G)$ form the pentagon cycle:
  $$E(G) = \{\{1, 2\}, \{2, 3\}, \{3, 4\}, \{4, 5\}, \{5, 1\}\}$$
* The missing edges form the pentagram (5-pointed star):
  $$E(G^c) = \{\{1, 3\}, \{3, 5\}, \{5, 2\}, \{2, 4\}, \{4, 1\}\}$$
* Tracing the star in order $1 - 3 - 5 - 2 - 4 - 1$ demonstrates that $G^c$ is also a single 5-cycle ($C_5$).
* Thus, $C_5 \cong C_5^c$.

---

# 3. Walks, Trails, Paths, Circuits, and Cycles

## 3.1 Taxonomy of Graph Traversals
* **Walk**: A finite sequence $W = v_0, e_1, v_1, e_2, v_2, \dots, e_k, v_k$ whose terms are alternately vertices $v_i$ and edges $e_i$, such that edge $e_i$ connects endpoints $v_{i-1}$ and $v_i$.
  - Vertices and edges may repeat arbitrarily.
* **Trail**: A walk in which **no edge is repeated** (all edges are distinct). Vertices may still repeat.
* **Path ($P_n$)**: A trail in which **no vertex is repeated** (which automatically prevents edge repetition).
* **Closed Prefix**: Used when the starting and terminating vertices are identical ($v_0 = v_k$):
  - **Closed Walk**: $v_0 = v_k$.
  - **Closed Trail / Circuit**: A closed walk with no repeated edges.
  - **Closed Path / Cycle ($C_n$)**: A closed trail with no repeated vertices except $v_0 = v_k$.

---

## 3.2 Summary Comparison Table

| Traversal Type | Edges Repeatable? | Vertices Repeatable? | Start Vertex = End Vertex? |
|:--------------:|:-----------------:|:--------------------:|:--------------------------:|
| **Walk**       | Yes               | Yes                  | Not necessarily            |
| **Trail**      | **No**            | Yes                  | Not necessarily            |
| **Path**       | **No**            | **No**               | **No**                     |
| **Closed Walk**| Yes               | Yes                  | **Yes**                    |
| **Circuit**    | **No**            | Yes                  | **Yes**                    |
| **Cycle**      | **No**            | **No** (except ends) | **Yes**                    |

---

## 3.3 Comprehensive Walk/Trail/Path Analysis on Class Graph
Consider the 8-vertex graph from the class notebook:

```text
       v1 -------(e1)------- v2 -------(e2)------- v3 -------(e3)------- v4
        \                   / |                   / |                   / |
         \                 /  |                  /  |                  /  |
         (e8)             (e9) |                (e12)|                (e13)|
           \             /     |                /    |                /    |
            \           /      |               /     |               /     |
             \         /      (e11)          /     (e10)           /     (e4)
              \       /       |             /       |             /       |
               \     /        |            /        |            /        |
                \   /         |           /         |           /         |
                  v8 ----(e7)--- v7 ---(e6)--- v6 ---(e5)--- v5 ---------+
```

### Concrete Traces from Notes:
1. **Walk Example**:
   $$W = v_1, e_1, v_2, e_2, v_3, e_2, v_2, e_8, v_8, e_8, v_2$$
   - Edge $e_2$ and vertices $v_2, v_8$ repeat.
2. **Trail Example**:
   $$T = v_1, e_1, v_2, e_2, v_3, e_3, v_4, e_4, v_5, e_{12}, v_3$$
   - All edges $\{e_1, e_2, e_3, e_4, e_{12}\}$ are distinct. Vertex $v_3$ is revisited.
3. **Path Example**:
   $$P = v_1, e_1, v_2, e_2, v_3, e_{12}, v_5, e_5, v_6$$
   - All vertices $\{v_1, v_2, v_3, v_5, v_6\}$ are distinct.

---

# 4. Graph Connectivity & Components

## 4.1 Path Length, Shortest Paths, and Distance Metrics
* **Length of a Path $P$ ($L(P)$)**: Total number of edges in $P$.
* **Shortest Path**: A path between vertices $u$ and $v$ such that $L(P) \le L(P')$ for all other paths $P'$ between $u$ and $v$.
* **Distance $d(u, v)$**: Length of the shortest path between $u$ and $v$. If no path exists, $d(u, v) = \infty$.

---

## 4.2 Connected Graphs & Connected Components
* **Connected Vertices**: Vertices $u$ and $v$ are connected if there is at least one path between them.
* **Connected Graph**: A graph in which every pair of vertices is connected by a path.
* **Connected Component**: A **maximal connected subgraph** of $G$ (a connected subgraph not contained in any larger connected subgraph).
  - Denoted $c(G)$.
  - $G$ is connected $\iff c(G) = 1$.

---

## 4.3 Class Exercise: Component Counting Across 7 Test Graphs

| Graph Identifier | Visual Description | Number of Components ($c(G)$) | Explanation |
|:----------------:|:-------------------|:------------------------------:|:------------|
| **(a)** | Two disjoint triangles | **2** | Two separated $C_3$ cycles. |
| **(b)** | Five disjoint 4-cycles | **5** | Five separated squares with no connecting edges. |
| **(c)** | Two disjoint bowties | **2** | Two independent components. |
| **(d)** | Two disjoint open paths | **2** | Two separate zig-zag paths. |
| **(e)** | Two disjoint diamonds | **2** | Two separated connected components. |
| **(f)** | Wheel graph $W_5$ | **1** | Fully connected via the central hub. |
| **(g)** | Interconnected ladder network | **1** | Path exists between all vertex pairs. |

---

## 4.4 Proposition 1: Minimum Degree Bound for Connectivity

> **Proposition 1**: If $G$ is a simple graph of order $n$ and minimum degree satisfies:
> $$\delta(G) \ge rac{n - 1}{2}$$
> then $G$ is **connected**.

### Formal Proof (by Contrapositive):
1. Let $p: \delta(G) \ge rac{n - 1}{2}$ and $q: G 	ext{ is connected}$.
2. The contrapositive statement is $\sim q \implies \sim p$:
   *"If $G$ is not connected, then $\delta(G) < rac{n - 1}{2}$."*
3. Suppose $G$ is **not connected**.
4. Then $G$ has at least two connected components: $c(G) = k \ge 2$.
5. Let the components have orders $n_1, n_2, \dots, n_k$, where $\sum_{i=1}^k n_i = n$.
6. By the generalized Pigeonhole Principle, at least one component, say $C_1$, satisfies:
   $$n_1 \le rac{n}{k} \le rac{n}{2}$$
7. Pick any vertex $u \in C_1$. Since $C_1$ is disconnected from the rest of $G$, $u$ has no neighbors outside $C_1$.
8. In a simple graph:
   $$\deg(u) \le n_1 - 1 \le rac{n}{2} - 1 = rac{n - 2}{2}$$
9. Therefore, the minimum degree satisfies:
   $$\delta(G) \le \deg(u) \le rac{n - 2}{2} < rac{n - 1}{2}$$
10. This proves $\sim p$, establishing the theorem. $lacksquare$

---

# 5. Dijkstra's Shortest Path Algorithm

## 5.1 Algorithmic Framework
Dijkstra's algorithm determines the shortest path from a designated source vertex $s$ to all other vertices in a weighted graph with non-negative edge weights ($w(e) \ge 0$).

### Core Notations:
* $P$: Set of vertices with **permanent labels** (shortest distance finalized).
* $T$: Set of vertices with **tentative labels** (current best estimate).
* $p_i$: Permanent distance label of vertex $v_i$.
* $t_i$: Tentative distance label of vertex $v_i$.
* $q_{ij}$: Weight of directed edge $v_i 	o v_j$ ($q_{ij} = \infty$ if no directed edge exists).
* Predecessor label $(u, v)$: The optimal edge entering $v$ originates from $u$.

---

## 5.2 Problem 1: 7-Vertex Directed Graph (Full Class Trace)

### Graph Specification:
* Vertices: $V = \{A, B, C, D, E, F, G\}$, Source = $A$.
* Directed Edge Weights:
  $A 	o B = 2, \; A 	o D = 1, \; C 	o A = 4, \; D 	o C = 2, \; B 	o D = 3$
  $B 	o E = 10, \; D 	o E = 2, \; D 	o F = 8, \; D 	o G = 4, \; E 	o G = 6$
  $F 	o C = 5, \; G 	o F = 1$.

```text
               (2)
          A ----------> B
         / \          / |
     (4)/   \(1)  (3)/  |
       /     \      /   |
      v   (2) v    v (2)|(10)
      C <---- D ------> E
      ^      / \       |
      |  (8)/   \(4)   |(6)
   (5)|    /     \     |
      |   v   (1) v    v
      F <-------- G <--+
```

### Iteration Trace:
* **Iteration 1**:
  - $P = \{A\}$, $P_A = 0$, $T = \{B, C, D, E, F, G\}$.
  - Initial labels: $t_B = 2, \; t_D = 1, \; t_C = \infty, \; t_E = \infty, \; t_F = \infty, \; t_G = \infty$.
  - Minimum: $t_D = 1 \implies$ Add $D$ to $P$: $P_D = 1$, Label $(A, D)$.
  - $P = \{A, D\}$, $T = \{B, C, E, F, G\}$.
  - Updates via $P_D = 1$:
    - $t_B = \min(2, 1 + \infty) = 2$
    - $t_C = \min(\infty, 1 + 2) = 3$ [Predecessor: $(D, C)$]
    - $t_E = \min(\infty, 1 + 2) = 3$ [Predecessor: $(D, E)$]
    - $t_F = \min(\infty, 1 + 8) = 9$ [Predecessor: $(D, F)$]
    - $t_G = \min(\infty, 1 + 4) = 5$ [Predecessor: $(D, G)$]
* **Iteration 2**:
  - Minimum in $T$: $t_B = 2 \implies$ Add $B$ to $P$: $P_B = 2$, Label $(A, B)$.
  - $P = \{A, D, B\}$, $T = \{C, E, F, G\}$.
  - Updates via $P_B = 2$:
    - $t_E = \min(3, 2 + 10) = 3$ (unchanged)
* **Iteration 3**:
  - Tie between $C$ and $E$ ($t_C = 3, t_E = 3$). Select $C$:
  - Add $C$ to $P$: $P_C = 3$, Label $(D, C)$.
  - $P = \{A, D, B, C\}$, $T = \{E, F, G\}$.
  - Updates via $P_C = 3$:
    - $t_F = \min(9, 3 + 5) = 8$ [Predecessor: $(C, F)$]
* **Iteration 4**:
  - Minimum in $T$: $t_E = 3 \implies$ Add $E$ to $P$: $P_E = 3$, Label $(D, E)$.
  - $P = \{A, D, B, C, E\}$, $T = \{F, G\}$.
  - Updates via $P_E = 3$:
    - $t_G = \min(5, 3 + 6) = 5$ (unchanged)
* **Iteration 5**:
  - Minimum in $T$: $t_G = 5 \implies$ Add $G$ to $P$: $P_G = 5$, Label $(D, G)$.
  - $P = \{A, D, B, C, E, G\}$, $T = \{F\}$.
  - Updates via $P_G = 5$:
    - $t_F = \min(8, 5 + 1) = 6$ [Predecessor: $(G, F)$]
* **Iteration 6**:
  - Minimum in $T$: $t_F = 6 \implies$ Add $F$ to $P$: $P_F = 6$, Label $(G, F)$.
  - $P = \{A, B, C, D, E, F, G\}$, $T = \emptyset$. Process terminates.

### Summary Table for Problem 1:
| Vertex ($v$) | Shortest Distance ($P_v$) | Predecessor Chain | Optimal Shortest Path |
|:------------:|:-------------------------:|:-----------------:|:----------------------|
| **A** | **0** | *Source* | $A$ |
| **B** | **2** | $(A, B)$ | $A 	o B$ |
| **C** | **3** | $(D, C) \leftarrow (A, D)$ | $A 	o D 	o C$ |
| **D** | **1** | $(A, D)$ | $A 	o D$ |
| **E** | **3** | $(D, E) \leftarrow (A, D)$ | $A 	o D 	o E$ |
| **F** | **6** | $(G, F) \leftarrow (D, G) \leftarrow (A, D)$ | $A 	o D 	o G 	o F$ |
| **G** | **5** | $(D, G) \leftarrow (A, D)$ | $A 	o D 	o G$ |

---

## 5.3 Problem 2: Five Cities Road Network (Complete 4-Iteration Trace)

### Problem Statement:
Five cities ($S, A, B, C, D$) are connected by roads with directed edge weights:
$$SA = 10, \quad SC = 5, \quad AC = 2, \quad CA = 3, \quad AB = 1$$
$$BD = 4, \quad DB = 6, \quad CB = 9, \quad CD = 2, \quad DS = 7$$
Find the shortest path from source city $S$ to all other cities using Dijkstra's algorithm.

---

### Step-by-Step Execution:

#### Iteration 1:
* $P = \{S\}$, $P_S = 0$, $T = \{A, B, C, D\}$.
* Initial Labels: $t_A = 10, \; t_B = \infty, \; t_C = 5, \; t_D = \infty$.
* **Step 1 (Select Min)**: $t_C = 5 \implies$ Add $C$ to $P$: $P_C = 5$, Label $(S, C)$.
* $P = \{S, C\}$, $T = \{A, B, D\}$.
* **Step 2 (Update Labels via $P_C = 5$)**:
  - $	ext{New } t_A = \min\{	ext{old } t_A, P_C + q_{CA}\} = \min\{10, 5 + 3\} = 8$ [Predecessor: $(C, A)$]
  - $	ext{New } t_B = \min\{\infty, 5 + 9\} = 14$ [Predecessor: $(C, B)$]
  - $	ext{New } t_D = \min\{\infty, 5 + 2\} = 7$ [Predecessor: $(C, D)$]

#### Iteration 2:
* $T = \{A, B, D\}$ with $t_A = 8, \; t_B = 14, \; t_D = 7$.
* **Step 1 (Select Min)**: $t_D = 7 \implies$ Add $D$ to $P$: $P_D = 7$, Label $(C, D)$.
* $P = \{S, C, D\}$, $T = \{A, B\}$.
* **Step 2 (Update Labels via $P_D = 7$)**:
  - Outgoing edges: $D 	o B = 6$, $D 	o S = 7$ ($S \in P$).
  - $	ext{New } t_A = \min\{8, 7 + \infty\} = 8$
  - $	ext{New } t_B = \min\{14, 7 + 6\} = 13$ [Predecessor updated to $(D, B)$]

#### Iteration 3:
* $T = \{A, B\}$ with $t_A = 8, \; t_B = 13$.
* **Step 1 (Select Min)**: $t_A = 8 \implies$ Add $A$ to $P$: $P_A = 8$, Label $(C, A)$.
* $P = \{S, C, D, A\}$, $T = \{B\}$.
* **Step 2 (Update Labels via $P_A = 8$)**:
  - Outgoing edges: $A 	o B = 1, \; A 	o C = 2$ ($C \in P$).
  - $	ext{New } t_B = \min\{13, 8 + 1\} = 9$ [Predecessor updated to $(A, B)$]

#### Iteration 4:
* $T = \{B\}$ with $t_B = 9$.
* **Step 1 (Select Min)**: $t_B = 9 \implies$ Add $B$ to $P$: $P_B = 9$, Label $(A, B)$.
* $P = \{S, C, D, A, B\}$, $T = \emptyset$.
* Stop process! All vertices are permanently labeled.

---

### Final Summary Table & Shortest Path Tree for Problem 2:
| City (Destination) | Shortest Distance from $S$ | Predecessor Chain | Complete Optimal Shortest Path |
|:------------------:|:-------------------------:|:-----------------:|:-------------------------------|
| **S** | **0** | *Source* | $S$ |
| **C** | **5** | $(S, C)$ | $S 	o C$ |
| **D** | **7** | $(C, D) \leftarrow (S, C)$ | $S 	o C 	o D$ |
| **A** | **8** | $(C, A) \leftarrow (S, C)$ | $S 	o C 	o A$ |
| **B** | **9** | $(A, B) \leftarrow (C, A) \leftarrow (S, C)$ | $S 	o C 	o A 	o B$ |

```text
               (5)             (3)             (1)
        (S) ----------> (C) ----------> (A) ----------> (B)
                         |
                         | (2)
                         v
                        (D)
```

---

# 6. Matrix Representations of Graphs

## 6.1 Adjacency Matrix for Undirected Graphs

### Definition & Algebraic Properties
Let $G = (V, E)$ be a simple labelled undirected graph with $p$ vertices $V = \{v_1, v_2, \dots, v_p\}$ and $q$ edges $E = \{e_1, e_2, \dots, e_q\}$.

The **Adjacency Matrix** $A(G)$ of order $p 	imes p$ is defined as $A(G) = [a_{ij}]_{p 	imes p}$ where:
$$a_{ij} = egin{cases} 1, & 	ext{if } v_i 	ext{ is adjacent to } v_j 	ext{ (i.e., } \{v_i, v_j\} \in E) \ 0, & 	ext{otherwise} \end{cases}$$

#### Properties:
1. **Symmetric**: $a_{ij} = a_{ji} \implies A(G) = A(G)^T$.
2. **Zero Diagonal**: $a_{ii} = 0 \implies \operatorname{trace}(A(G)) = 0$ (no loops in simple graphs).
3. **Degree Sum**: $\sum_{j=1}^p a_{ij} = \deg(v_i)$.
4. **Total Sum**: $\sum_{i=1}^p \sum_{j=1}^p a_{ij} = 2|E| = 2q$.

---

### 6-Vertex Detailed Example from Notes
For the graph $G$ with vertices $\{A, B, C, D, E, F\}$:
* $N(A) = \{B, E, F\} \implies \deg(A) = 3$
* $N(B) = \{A, C\} \implies \deg(B) = 2$
* $N(C) = \{B, D, F\} \implies \deg(C) = 3$
* $N(D) = \{C, E, F\} \implies \deg(D) = 3$
* $N(E) = \{A, D, F\} \implies \deg(E) = 3$
* $N(F) = \{A, C, D, E\} \implies \deg(F) = 4$

#### Adjacency Matrix:
$$A(G) = egin{pmatrix}
 & \mathbf{A} & \mathbf{B} & \mathbf{C} & \mathbf{D} & \mathbf{E} & \mathbf{F} \
\mathbf{A} & 0 & 1 & 0 & 0 & 1 & 1 \
\mathbf{B} & 1 & 0 & 1 & 0 & 0 & 0 \
\mathbf{C} & 0 & 1 & 0 & 1 & 0 & 1 \
\mathbf{D} & 0 & 0 & 1 & 0 & 1 & 1 \
\mathbf{E} & 1 & 0 & 0 & 1 & 0 & 1 \
\mathbf{F} & 1 & 0 & 1 & 1 & 1 & 0
\end{pmatrix}$$

---

### Theorem: Powers of Adjacency Matrix and Walks of Length $k$
> **Theorem**: If $A$ is the adjacency matrix of a simple graph $G$, the $(i, j)$-th entry of $A^k$, denoted $(A^k)_{ij}$, equals the number of distinct walks of length $k$ connecting vertex $v_i$ and vertex $v_j$.

*(Proof by Induction)*:
* Base case ($k=1$): $(A^1)_{ij} = a_{ij}$, which is 1 if an edge (walk of length 1) exists, and 0 otherwise.
* Inductive step: Assume $(A^{k-1})_{im}$ counts walks of length $k-1$ from $v_i$ to $v_m$. By matrix multiplication:
  $$(A^k)_{ij} = \sum_{m=1}^p (A^{k-1})_{im} \cdot a_{mj}$$
  Every walk of length $k$ from $v_i$ to $v_j$ is a walk of length $k-1$ from $v_i$ to some neighbor $v_m$ followed by edge $\{v_m, v_j\}$ ($a_{mj}=1$). Summing over all $m$ yields all distinct walks of length $k$. $lacksquare$

---

## 6.2 Adjacency Matrix for Directed Graphs (Digraphs)

### Signed Skew-Symmetric Formulation (Class Notes Convention)
For a directed graph $G = (V, E)$, the notebook defines the signed adjacency matrix $A(G) = [a_{ij}]_{p 	imes p}$ as:
$$a_{ij} = egin{cases} 1, & 	ext{if } v_i 	ext{ is adjacent to } v_j 	ext{ with direction } v_i 	o v_j \ -1, & 	ext{if } v_i 	ext{ is adjacent to } v_j 	ext{ with direction } v_j 	o v_i \ 0, & 	ext{otherwise} \end{cases}$$

#### Algebraic Properties:
1. **Skew-Symmetry**: $a_{ij} = -a_{ji} \implies A(G) = -A(G)^T$.
2. **Zero Diagonal**: $a_{ii} = 0$.

---

### Standard Binary Formulation (Comparison)
In standard graph theory literature, the binary adjacency matrix of a directed graph uses:
$$a_{ij} = egin{cases} 1, & 	ext{if arc } (v_i, v_j) 	ext{ exists} \ 0, & 	ext{otherwise} \end{cases}$$
Row sums yield out-degrees, while column sums yield in-degrees.

---

### 4-Vertex Digraph Worked Example
Consider the directed graph from the notes with vertices $\{v_1, v_2, v_3, v_4\}$ and directed arcs:
* $v_2 	o v_1 \implies a_{21} = 1, \; a_{12} = -1$
* $v_2 	o v_3 \implies a_{23} = 1, \; a_{32} = -1$
* $v_4 	o v_2 \implies a_{42} = 1, \; a_{24} = -1$
* $v_3 	o v_4 \implies a_{34} = 1, \; a_{43} = -1$

$$A(G) = egin{pmatrix}
 & \mathbf{v_1} & \mathbf{v_2} & \mathbf{v_3} & \mathbf{v_4} \
\mathbf{v_1} & 0 & -1 & 0 & 0 \
\mathbf{v_2} & 1 & 0 & 1 & -1 \
\mathbf{v_3} & 0 & -1 & 0 & 1 \
\mathbf{v_4} & 0 & 1 & -1 & 0
\end{pmatrix}$$

Notice $A(G)^T = -A(G)$, verifying skew-symmetry.

---

## 6.3 Incidence Matrix of a Graph ($I(G)$ or $B_{	ext{inc}}(G)$)

### Definition & Matrix Dimensions
Let $G = (V, E)$ be a labelled graph with $p$ vertices and $q$ edges.
The **Incidence Matrix** $I(G)$ is of order **$p 	imes q$** (Vertices $	imes$ Edges):
$$I(G) = [b_{ij}]_{p 	imes q}$$
where:
$$b_{ij} = egin{cases} 1, & 	ext{if vertex } v_i 	ext{ is incident with edge } e_j \ 0, & 	ext{otherwise} \end{cases}$$

---

### Fundamental Invariants:
1. **Column Sum Invariant**: Every edge has exactly two endpoints. Therefore, every column contains **exactly two 1s**:
   $$\sum_{i=1}^p b_{ij} = 2 \quad orall j \in \{1, 2, \dots, q\}$$
2. **Row Sum Degree Invariant**: The sum of entries in row $i$ equals the degree of $v_i$:
   $$\sum_{j=1}^q b_{ij} = \deg(v_i) \quad orall i \in \{1, 2, \dots, p\}$$
3. **Total Sum of Elements**:
   $$\sum_{i=1}^p \sum_{j=1}^q b_{ij} = 2q = 2|E|$$

---

# 7. Comprehensive Exam Problem: Complement Matrices & Isomorphism

## 7.1 Problem Statement & Initial Adjacency Matrices
**Problem**:
Given the adjacency matrices of graphs $G_1$ and $G_2$:
$$A(G_1) = egin{pmatrix}
 & \mathbf{1} & \mathbf{2} & \mathbf{3} & \mathbf{4} \
\mathbf{1} & 0 & 1 & 0 & 1 \
\mathbf{2} & 1 & 0 & 1 & 0 \
\mathbf{3} & 0 & 1 & 0 & 1 \
\mathbf{4} & 1 & 0 & 1 & 0
\end{pmatrix}, \qquad
A(G_2) = egin{pmatrix}
 & \mathbf{A} & \mathbf{B} & \mathbf{C} & \mathbf{D} \
\mathbf{A} & 0 & 1 & 1 & 0 \
\mathbf{B} & 1 & 0 & 0 & 1 \
\mathbf{C} & 1 & 0 & 0 & 1 \
\mathbf{D} & 0 & 1 & 1 & 0
\end{pmatrix}$$

1. Draw graphs $G_1$ and $G_2$.
2. Construct and draw their complement graphs $G_1^c$ and $G_2^c$.
3. Check whether $G_1^c \cong G_2^c$.
4. Find the adjacency matrices $A(G_1^c)$ and $A(G_2^c)$.
5. Find the incidence matrices $I(G_1^c)$ and $I(G_2^c)$.

---

## 7.2 Reconstruction of Graphs $G_1$ and $G_2$

### Graph $G_1$:
* Vertices: $\{1, 2, 3, 4\}$.
* Edges: $\{\{1, 2\}, \{2, 3\}, \{3, 4\}, \{4, 1\}\}$.
* Structure: 4-cycle $C_4$ ($1 - 2 - 3 - 4 - 1$).

### Graph $G_2$:
* Vertices: $\{A, B, C, D\}$.
* Edges: $\{\{A, B\}, \{A, C\}, \{B, D\}, \{C, D\}\}$.
* Structure: 4-cycle $C_4$ ($A - B - D - C - A$).

```text
       Graph G1:                          Graph G2:
       1 --------- 2                      A --------- B
       |           |                      |           |
       |           |                      |           |
       4 --------- 3                      C --------- D
```

---

## 7.3 Construction of Complement Graphs $G_1^c$ and $G_2^c$
In $K_4$, total edges $= inom{4}{2} = 6$. Since $|E(G_1)| = |E(G_2)| = 4$:
$$|E(G_1^c)| = |E(G_2^c)| = 6 - 4 = 2 	ext{ edges}$$

* **Complement $G_1^c$**:
  - Missing diagonal pairs: $\{1, 3\}$ and $\{2, 4\}$.
  - Let edge $i = \{1, 3\}$ and edge $ii = \{2, 4\}$.
  - Structure: Two disconnected edges ($2K_2$).
* **Complement $G_2^c$**:
  - Missing diagonal pairs: $\{A, D\}$ and $\{B, C\}$.
  - Let edge $a = \{A, D\}$ and edge $b = \{B, C\}$.
  - Structure: Two disconnected edges ($2K_2$).

```text
       Complement G1^c:                   Complement G2^c:
       1           2                      A           B
        \         /                        \         /
         \ (i)   / (ii)                     \ (a)   / (b)
          \     /                            \     /
           \   /                              \   /
             X                                  X
            / \                                /            /   \                              /             4     3                            C     D
```

---

## 7.4 Formal Proof of Isomorphism Between $G_1^c$ and $G_2^c$

Define the bijection $f: V(G_1^c) 	o V(G_2^c)$ as:
$$f(1) = A, \quad f(2) = B, \quad f(3) = D, \quad f(4) = C$$

### Adjacency Preservation Check:
1. **Edges in $G_1^c$**:
   - $\{1, 3\} \in E(G_1^c) \implies \{f(1), f(3)\} = \{A, D\} \in E(G_2^c)$ (Preserved)
   - $\{2, 4\} \in E(G_1^c) \implies \{f(2), f(4)\} = \{B, C\} \in E(G_2^c)$ (Preserved)
2. **Non-Edges in $G_1^c$**:
   - $\{1, 2\} 
otin E(G_1^c) \implies \{A, B\} 
otin E(G_2^c)$
   - $\{1, 4\} 
otin E(G_1^c) \implies \{A, C\} 
otin E(G_2^c)$
   - $\{2, 3\} 
otin E(G_1^c) \implies \{B, D\} 
otin E(G_2^c)$
   - $\{3, 4\} 
otin E(G_1^c) \implies \{D, C\} 
otin E(G_2^c)$

Because $f$ is a bijection and strictly preserves adjacency and non-adjacency:
$$G_1^c \cong G_2^c \quad (	ext{Isomorphic})$$

---

## 7.5 Adjacency Matrices of Complements $A(G_1^c)$ and $A(G_2^c)$

Using the algebraic complement formula $A(G^c) = J_4 - I_4 - A(G)$:

$$A(G_1^c) = egin{pmatrix}
 & \mathbf{1} & \mathbf{2} & \mathbf{3} & \mathbf{4} \
\mathbf{1} & 0 & 0 & 1 & 0 \
\mathbf{2} & 0 & 0 & 0 & 1 \
\mathbf{3} & 1 & 0 & 0 & 0 \
\mathbf{4} & 0 & 1 & 0 & 0
\end{pmatrix}$$

$$A(G_2^c) = egin{pmatrix}
 & \mathbf{A} & \mathbf{B} & \mathbf{C} & \mathbf{D} \
\mathbf{A} & 0 & 0 & 0 & 1 \
\mathbf{B} & 0 & 0 & 1 & 0 \
\mathbf{C} & 0 & 1 & 0 & 0 \
\mathbf{D} & 1 & 0 & 0 & 0
\end{pmatrix}$$

---

## 7.6 Incidence Matrices of Complements $I(G_1^c)$ and $I(G_2^c)$

Each complement has 4 vertices and 2 edges, giving dimension **$4 	imes 2$**:

### Incidence Matrix $I(G_1^c)$:
* Edge $i = \{1, 3\}$
* Edge $ii = \{2, 4\}$

$$I(G_1^c) = egin{pmatrix}
 & \mathbf{i} & \mathbf{ii} \
\mathbf{1} & 1 & 0 \
\mathbf{2} & 0 & 1 \
\mathbf{3} & 1 & 0 \
\mathbf{4} & 0 & 1
\end{pmatrix}_{4 	imes 2}$$

### Incidence Matrix $I(G_2^c)$:
* Edge $a = \{A, D\}$
* Edge $b = \{B, C\}$

$$I(G_2^c) = egin{pmatrix}
 & \mathbf{a} & \mathbf{b} \
\mathbf{A} & 1 & 0 \
\mathbf{B} & 0 & 1 \
\mathbf{C} & 0 & 1 \
\mathbf{D} & 1 & 0
\end{pmatrix}_{4 	imes 2}$$

* For both matrices: every column sum is exactly 2, and every row sum is 1.

---
*End of Module 4 Notes.*
