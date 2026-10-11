# 📘 Module 5: Trees & Graph Coloring (From Zero to Mastery)

> **Module Focus**: Tree Characterizations, Centers & Distance, Spanning Trees, Kruskal's & Prim's MST Algorithms, Cut Sets & Fundamental Circuits, Chromatic Number $\chi(G)$, Welsh-Powell Coloring, Chromatic Index, and Chromatic Polynomials.  
> **Weightage in FAT**: Approx 20–25 Marks.  
> **Exam Advantage**: This module was NOT in CAT-1 or CAT-2! It is brand new for Term End. Mastering it gives you an immediate scoring edge over other students.

---

## 1. Trees: Definitions & Characterizations

### 1.1 What is a Tree?
* A **Tree** $T$ is a connected undirected graph with **no cycles (acyclic)**.
* A **Forest** is a collection of disjoint trees (an acyclic graph that may be disconnected).

```text
       A TREE (Connected + Acyclic)           NOT A TREE (Has a Cycle)
                 (1)                                    (1)
                /   \                                  /   \
              (2)   (3)                              (2)───(3) ◄── Cycle!
             /   \     \                               \   /
           (4)   (5)   (6)                              (4)
```

---

### 1.2 The 6 Equivalent Characterizations of a Tree (Guaranteed 5-Mark Proof)

In exams, you are frequently asked: *"Prove that a connected graph with $n$ vertices and $n-1$ edges is a tree."*  
Any one of the following 6 statements can be used to define a tree of $n$ vertices:

1. **$G$ is connected and acyclic.** (Standard definition).
2. **$G$ is connected and has exactly $e = n - 1$ edges.**
3. **$G$ is acyclic and has exactly $e = n - 1$ edges.**
4. **There exists a UNIQUE simple path between every pair of vertices in $G$.**
5. **$G$ is minimally connected**: Removing any single edge disconnects $G$ (every edge is a bridge!).
6. **$G$ is maximally acyclic**: Adding any new edge between non-adjacent vertices creates **exactly one cycle**.

---

### 1.3 Key Properties of Trees
* **Pendant Vertices (Leaves)**: Every tree with $n \ge 2$ vertices has **at least TWO vertices of degree 1 (leaves)**.  
  *(Proof via Handshaking: $\sum \deg(v) = 2(n-1) = 2n - 2$. If all degrees were $\ge 2$, the sum would be $\ge 2n$, a contradiction!).*
* **Bipartite Nature**: Every tree is a **Bipartite Graph** (because it has no cycles, hence no odd cycles!). Therefore, its chromatic number is always $\mathbf{\chi(T) = 2}$.

---

## 2. Tree Metrics: Distance, Eccentricity, and Centers

### 2.1 Definitions
Let $u, v$ be vertices in a tree $T$:
1. **Distance $d(u, v)$**: The length (number of edges) of the unique simple path between $u$ and $v$.
2. **Eccentricity $e(v)$**: The greatest distance from $v$ to any other vertex in the tree:
   $$e(v) = \max_{u \in V} d(u, v)$$
3. **Radius $R(T)$**: The minimum eccentricity among all vertices: $R(T) = \min_{v \in V} e(v)$.
4. **Diameter $D(T)$**: The maximum eccentricity among all vertices: $D(T) = \max_{v \in V} e(v)$.
5. **Center of a Tree**: A vertex whose eccentricity equals the radius ($e(v) = R(T)$).

---

### 2.2 Jordan's Theorem & The Leaf-Pruning Algorithm

> 🏆 **JORDAN'S THEOREM**:  
> **Every tree has either EXACTLY ONE CENTER or EXACTLY TWO ADJACENT CENTERS!**

```text
    THE EXAM RECIPE TO FIND THE CENTER OF A TREE:
    1. Identify all leaves (vertices of degree 1).
    2. Delete all leaves and their incident edges simultaneously.
    3. In the remaining smaller tree, repeat: delete all new leaves.
    4. Continue until either:
       - Exactly ONE vertex remains  ──► That vertex is the UNIQUE CENTER!
       - Exactly TWO adjacent vertices remain ──► Both vertices are BICENTERS!
```

---

## 3. Rooted & Binary Trees

* **Rooted Tree**: A tree with one designated vertex called the **root**. Edges are directed away from the root.
* **Level of a Vertex**: Distance from root (Root is at Level 0).
* **Height of a Tree**: Maximum level of any leaf.
* **$m$-ary Tree**: Every internal vertex has at most $m$ children. If every internal vertex has exactly $m$ children, it is a **full $m$-ary tree**.
* **Binary Tree ($m=2$)**:
  * Every internal vertex has at most 2 children (left child, right child).
  * **Full Binary Tree Theorem**: If a full binary tree has $i$ internal vertices, then:
    * Total vertices: $n = 2i + 1$
    * Number of leaves: $l = i + 1$

---

## 4. Spanning Trees & Minimal Spanning Trees (MST)

### 4.1 What is a Spanning Tree?
A **Spanning Tree** of a connected graph $G = (V, E)$ is a subgraph $T = (V, E_T)$ that is a tree containing **all vertices of $G$**.
* If $G$ has $n$ vertices and $m$ edges:
  * Any spanning tree contains **all $n$ vertices** and exactly **$n - 1$ edges**.
  * Edges in $T$ are called **Branches** (Count = $n - 1$).
  * Edges of $G$ NOT in $T$ are called **Chords** or ties (Count = $m - (n - 1) = m - n + 1$).
* **Cayley's Formula**: The complete graph $K_n$ has exactly **$n^{n-2}$ labeled spanning trees**!  
  *(e.g., $K_3$ has $3^{3-2} = 3$ trees; $K_4$ has $4^{4-2} = 16$ trees; $K_5$ has $5^3 = 125$ trees).*

---

### 4.2 Minimal Spanning Tree (MST) Algorithms

In a weighted graph, an MST is a spanning tree whose total edge weight $\sum w(e)$ is **minimized**.

```text
┌─────────────────────────┬────────────────────────────────────────────────────────┐
│ KRUSKAL'S ALGORITHM     │ PRIM'S ALGORITHM                                       │
│ (Greedy Edge-by-Edge)   │ (Greedy Vertex Growth)                                 │
├─────────────────────────┼────────────────────────────────────────────────────────┤
│ 1. List ALL edges and   │ 1. Start with any single root vertex v₁.               │
│    sort by weight       │ 2. At each step, look at all edges connecting a vertex │
│    ascending.           │    INSIDE the growing tree to a vertex OUTSIDE.        │
│ 2. Pick the smallest    │ 3. Pick the edge with MINIMUM weight. Add the new edge │
│    edge that DOES NOT   │    and vertex to the tree.                             │
│    create a cycle!      │ 4. Repeat until all n vertices are included            │
│ 3. Repeat until n-1     │    (n-1 edges chosen).                                 │
│    edges are chosen.    │                                                        │
│ • Best for SPARSE graphs│ • Best for DENSE graphs.                               │
└─────────────────────────┴────────────────────────────────────────────────────────┘
```

---

### 📝 Worked Past Exam Problem: Kruskal's vs Prim's Trace
> **Question**: Find the Minimum Spanning Tree (MST) for the graph with vertices $\{A, B, C, D, E\}$ and weighted edges:  
> $(A, B)=1, (B, C)=4, (A, C)=3, (C, D)=2, (B, D)=5, (D, E)=7, (C, E)=6$.
>
> **Solution by Kruskal's Algorithm**:
> 1. Sort all edges ascending:
>    * $(A, B) = 1$
>    * $(C, D) = 2$
>    * $(A, C) = 3$
>    * $(B, C) = 4$
>    * $(B, D) = 5$
>    * $(C, E) = 6$
>    * $(D, E) = 7$
> 2. Select edges avoiding cycles (need $n-1 = 5-1 = 4$ edges):
>    * Pick $(A, B) = 1$: Accepted. (Edges: $\{AB\}$)
>    * Pick $(C, D) = 2$: Accepted. (Edges: $\{AB, CD\}$)
>    * Pick $(A, C) = 3$: Accepted. (Connects components $\{AB\}$ and $\{CD\}$! No cycle).
>    * Look at $(B, C) = 4$: **REJECTED!** (Adding $BC$ creates cycle $A-B-C-A$).
>    * Look at $(B, D) = 5$: **REJECTED!** (Adding $BD$ creates cycle $A-B-D-C-A$).
>    * Pick $(C, E) = 6$: Accepted. (Connects $E$ to tree).
> 3. We now have 4 edges: $\{ (A, B), (C, D), (A, C), (C, E) \}$.
> 
> **Total MST Weight**: $1 + 2 + 3 + 6 = \mathbf{12}$.

---

## 5. Cut Sets & Fundamental Systems

### 5.1 Cut Sets (Edge Cut)
* A **Cut Set** (or edge cut) of a connected graph $G$ is a **minimal set of edges whose removal disconnects $G$** (increases the number of connected components).
* *"Minimal"* means that if you remove all edges in the cut set, the graph is disconnected; but if you leave even one edge, it remains connected!
* **Cut Vertex (Articulation Point)**: A single vertex whose removal disconnects the graph.
* **Bridge (Cut Edge)**: A single edge whose removal disconnects the graph (a cut set of size 1).

---

### 5.2 Fundamental Circuits & Fundamental Cut Sets (Crucial Exam Concept)

Given a connected graph $G(V, E)$ with $n$ vertices, $m$ edges, and a fixed spanning tree $T$:

1. **Fundamental Circuits**:
   * A spanning tree $T$ has $n-1$ branches and $m - n + 1$ chords.
   * If you add any **single chord** $c$ back into $T$, it creates **EXACTLY ONE CYCLE**, called a **Fundamental Circuit**.
   * Total number of fundamental circuits = Number of chords = **$m - n + 1$** (This number $\mu = m - n + 1$ is called the **Cyclomatic Number** or **Nullity** of $G$!).

2. **Fundamental Cut Sets**:
   * If you remove any **single branch** $b$ from $T$, it splits the tree into two disjoint components $V_1$ and $V_2$.
   * The set of edges in $G$ having one endpoint in $V_1$ and one in $V_2$ forms a **Fundamental Cut Set** containing $b$ and no other branches of $T$.
   * Total number of fundamental cut sets = Number of tree branches = **$n - 1$** (This number is called the **Rank** of $G$!).

> 🏆 **THE RANK-NULLITY THEOREM OF GRAPHS**:  
> 
> $$\text{Rank } r(G) + \text{Nullity } \mu(G) = (n - 1) + (m - n + 1) = \mathbf{m \text{ (Total Edges!)}}$$
>

---

## 6. Graph Coloring: Chromatic Number & Algorithms

### 6.1 What is Vertex Coloring?
* A **Proper Vertex Coloring** assigns a color to each vertex such that **no two adjacent vertices share the same color**.
* The **Chromatic Number $\chi(G)$** is the **minimum number of colors** required to properly color $G$.

---

### 6.2 Chromatic Numbers of Standard Graph Families (Memorize!)

| Graph Family | Notation | Chromatic Number $\chi(G)$ | Reason / Intuition |
| :--- | :---: | :---: | :--- |
| **Complete Graph** | $K_n$ | **$n$** | Every vertex connects to every other; all must have different colors! |
| **Bipartite Graph**| $K_{m,n}$ | **$2$** | Set $V_1$ gets Color 1, Set $V_2$ gets Color 2. |
| **Tree** | $T$ | **$2$** | Trees are bipartite (no odd cycles!). |
| **Cycle (Even)** | $C_{2k}$ ($C_4, C_6, \dots$) | **$2$** | Alternate colors around the cycle: 1, 2, 1, 2... |
| **Cycle (Odd)** | $C_{2k+1}$ ($C_3, C_5, \dots$)| **$3$** | Last vertex connects to both 1st (color 1) and second-to-last (color 2). |
| **Wheel Graph** | $W_n$ | **$3$** if $n$ is odd<br>**$4$** if $n$ is even | Central hub needs 1 unique color; outer cycle $C_{n-1}$ needs 2 (if even) or 3 (if odd). |
| **Planar Graph** | Any planar graph | **$\le 4$** | **The Four Color Theorem** (Appel & Haken, 1976). |

---

### 6.3 The Welsh-Powell Coloring Algorithm (The Exam Recipe)

Use Welsh-Powell when an exam asks you to color an arbitrary graph with minimum colors:

1. Find the degree of every vertex.
2. **List all vertices in decreasing order of degree**: $v_1, v_2, \dots, v_n$.
3. Pick the first uncolored vertex on the list; assign it **Color 1**.
4. Scan down the list in order: assign **Color 1** to any vertex that is **NOT adjacent** to any vertex already colored with Color 1.
5. Pick the next uncolored vertex from the top of the list; assign it **Color 2**.
6. Repeat step 4 for Color 2, then Color 3, until all vertices are colored.

---

### 6.4 Chromatic Index $\chi'(G)$ (Edge Coloring)
* A **Proper Edge Coloring** assigns colors to edges so that edges sharing a common vertex get different colors.
* The minimum colors needed is the **Chromatic Index $\chi'(G)$**.
* **Vizing's Theorem**: For any simple graph with maximum degree $\Delta$:
  $$\Delta \le \chi'(G) \le \Delta + 1$$
  *(It is ALWAYS either $\Delta$ or $\Delta + 1$! Never anything else!).*

---

## 7. Chromatic Polynomials $P(G, \lambda)$

### 7.1 What is $P(G, \lambda)$?
The **Chromatic Polynomial** $P(G, \lambda)$ is a polynomial in $\lambda$ that gives the **exact number of ways to properly color graph $G$ using at most $\lambda$ colors**.

#### 🔑 Standard Chromatic Polynomials:
1. **Null Graph $N_n$ (no edges, $n$ vertices)**:  
   Each vertex can independently pick any of the $\lambda$ colors:  
   $$P(N_n, \lambda) = \lambda^n$$
2. **Complete Graph $K_n$**:  
   1st vertex has $\lambda$ choices, 2nd has $(\lambda-1)$, $\dots$, $n$-th has $(\lambda - n + 1)$:  
   $$P(K_n, \lambda) = \lambda(\lambda - 1)(\lambda - 2)\dots(\lambda - n + 1)$$
3. **Tree $T_n$ with $n$ vertices**:  
   Root has $\lambda$ choices; each of the remaining $n-1$ vertices has $(\lambda-1)$ choices:  
   $$P(T_n, \lambda) = \lambda(\lambda - 1)^{n-1}$$
4. **Cycle Graph $C_n$**:  
   $$P(C_n, \lambda) = (\lambda - 1)^n + (-1)^n(\lambda - 1)$$

---

### 7.2 The Deletion-Contraction Theorem (How to Find $P(G, \lambda)$ for Any Graph)

> 🏆 **DELETION-CONTRACTION THEOREM**:  
> For any edge $e = (u, v)$ in graph $G$:  
> 
> $$P(G, \lambda) = P(G - e, \lambda) - P(G / e, \lambda)$$
> 
> * Where $G - e$ is the graph with edge $e$ **deleted**.  
> * Where $G / e$ is the graph with edge $e$ **contracted** (merge vertices $u$ and $v$ into a single vertex, deleting edge $e$ and any duplicate parallel edges).

#### 📝 Worked Exam Example: Chromatic Polynomial of $C_4$
> Find $P(C_4, \lambda)$ using Deletion-Contraction.
>
> **Solution**:
> Pick any edge $e$ of the 4-cycle $C_4$:
> 1. **Delete $e$ ($C_4 - e$)**: Deleting an edge from a cycle produces a path graph $P_4$ (which is a tree of 4 vertices!).  
>    Since $P_4$ is a tree of 4 vertices: $P(C_4 - e, \lambda) = P(T_4, \lambda) = \lambda(\lambda - 1)^3$.
> 2. **Contract $e$ ($C_4 / e$)**: Merging the two endpoints of $e$ turns the 4-cycle into a 3-cycle ($K_3$ / triangle)!  
>    $P(C_4 / e, \lambda) = P(K_3, \lambda) = \lambda(\lambda - 1)(\lambda - 2)$.
> 3. **Apply Theorem**:  
>    $P(C_4, \lambda) = \lambda(\lambda - 1)^3 - \lambda(\lambda - 1)(\lambda - 2)$  
>    Factor out $\lambda(\lambda - 1)$:  
>    $= \lambda(\lambda - 1) \left[ (\lambda - 1)^2 - (\lambda - 2) \right]$  
>    $= \lambda(\lambda - 1) \left[ \lambda^2 - 2\lambda + 1 - \lambda + 2 \right]$  
>    $= \lambda(\lambda - 1) \left[ \lambda^2 - 3\lambda + 3 \right] = (\lambda - 1)^4 + (\lambda - 1)$
> 
> **Conclusion**: $P(C_4, \lambda) = \lambda(\lambda - 1)(\lambda^2 - 3\lambda + 3)$.  
> *(Notice: If $\lambda = 2$, $P(C_4, 2) = 2(1)(4 - 6 + 3) = 2$ colorings, which matches our knowledge that an even cycle can be properly 2-colored in exactly 2 ways!).*

---

## 💡 Module 5 Summary Checklist & Exam Traps

- [ ] A tree has $n$ vertices and $n-1$ edges. Every non-trivial tree has at least 2 leaves.
- [ ] To find tree centers: Successively delete all leaves simultaneously until 1 or 2 nodes remain.
- [ ] Kruskal's = sort all edges globally, pick smallest without cycles.
- [ ] Prim's = grow outward from a starting vertex, always picking the lowest weight cut-edge.
- [ ] Rank $= n - 1$ (branches / fundamental cut sets). Nullity $= m - n + 1$ (chords / fundamental circuits).
- [ ] Chromatic number: Trees $= 2$, Bipartite $= 2$, Even Cycles $= 2$, Odd Cycles $= 3$, $K_n = n$.
- [ ] Chromatic polynomial: Tree with $n$ nodes is ALWAYS $\lambda(\lambda - 1)^{n-1}$.
