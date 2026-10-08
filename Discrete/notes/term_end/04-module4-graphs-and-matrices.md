# 📘 Module 4: Graphs & Matrix Representations (From Zero to Mastery)

> **Module Focus**: Handshaking Lemma, Havel-Hakimi Graphic Test, Bipartite Graphs, Graph Isomorphism Invariant Radar, Euler vs Hamiltonian Graphs, Adjacency/Incidence Matrices, and Dijkstra's Shortest Path Algorithm.  
> **Weightage in FAT**: Approx 20–25 Marks.  
> **Why Students Lost Marks in CAT-2**: Failing to prove graph isomorphism properly, missing the odd-cycle test for bipartite graphs, and arithmetic mistakes in Dijkstra's table. We eliminate all those errors here!

---

## 1. Graph Basics & The Handshaking Lemma

### 1.1 Core Definitions
* A graph $G = (V, E)$ consists of a set of **vertices (nodes)** $V$ and a set of **edges** $E$.
* **Simple Graph**: No self-loops and no parallel (multiple) edges.
* **Degree of a Vertex $\deg(v)$**: Number of edges incident on vertex $v$ (a self-loop counts twice!).
* **In-degree $\deg^-(v)$ & Out-degree $\deg^+(v)$** (in directed graphs): Number of incoming and outgoing arrows.

---

### 1.2 The Handshaking Lemma (Guaranteed 2–4 Mark Proof/Problem)

> 🏆 **THEOREM (Euler's Handshaking Lemma)**:  
> In any undirected graph $G = (V, E)$:  
> $$\sum_{v \in V} \deg(v) = 2|E|$$  
> *Plain English*: Every edge has two endpoints. Therefore, when you sum the degrees of all vertices, every single edge is counted exactly twice!

#### 🔑 The Crucial Corollary:
> **The number of vertices with ODD degree in any graph is ALWAYS EVEN!**  
> *(Proof: $\sum \deg(v) = \sum_{\text{even}} \deg(v) + \sum_{\text{odd}} \deg(v) = 2|E|$. Since $2|E|$ is even and $\sum_{\text{even}}$ is even, $\sum_{\text{odd}}$ must be even. A sum of odd numbers can be even only if there is an even count of them!).*

---

### 📝 Worked Past Exam Problem: Handshaking Lemma
> **Question (From QUIZ-2 / Past Exam)**: A graph $G$ has 10 vertices each of degree 3. How many edges does $G$ have? Can a simple graph have 11 vertices each of degree 3?
>
> **Solution**:
> 1. Total vertices $n = 10$, degree of each vertex = $3$.  
>    Sum of degrees $= 10 \times 3 = 30$.  
>    By Handshaking Lemma: $2|E| = 30 \implies \mathbf{|E| = 15\text{ edges}}$.
> 2. For 11 vertices of degree 3:  
>    Sum of degrees $= 11 \times 3 = 33$ (an ODD number!).  
>    By Handshaking Lemma, $2|E|$ must always be an even integer. 33 is odd $\implies$ **Impossible!**  
>    Alternatively, it would have 11 vertices of odd degree, which violates the corollary (odd-degree vertices must be an even count).

---

## 2. Degree Sequences & The Havel-Hakimi Algorithm

A sequence of non-negative integers $d = (d_1, d_2, \dots, d_n)$ in non-increasing order ($d_1 \ge d_2 \ge \dots \ge d_n$) is called **Graphic** if there exists a simple graph whose vertex degrees match this sequence.

### 2.1 The Havel-Hakimi Reduction Algorithm (The Exam Recipe)

To test if a degree sequence is graphic:
1. **Sort** the sequence in non-increasing order: $(d_1, d_2, \dots, d_n)$.
2. **Remove the first element** $d_1$.
3. **Subtract 1 from each of the next $d_1$ elements**.
4. **Re-sort** the resulting sequence in descending order (ignore any zeros if at the end).
5. **Repeat** steps 2–4 until:
   * **Base Case SUCCESS**: All remaining numbers are $0$ $\implies$ **The sequence IS Graphic!**
   * **Base Case FAILURE**: Any number becomes negative, or there are not enough elements left to subtract $1$ $\implies$ **The sequence is NOT Graphic!**

---

### 📝 Worked Past Exam Problem: Havel-Hakimi Test
> **Question**: Determine whether the degree sequence $d = (5, 4, 3, 3, 2, 2, 1)$ is graphic.
>
> **Solution**:
> * Step 1: Initial sorted sequence:  
>   $$(5, 4, 3, 3, 2, 2, 1)$$
> * Step 2: Remove the first element ($5$). Subtract $1$ from the next 5 elements:  
>   $$4-1=3, \quad 3-1=2, \quad 3-1=2, \quad 2-1=1, \quad 2-1=1, \quad \text{last } 1 \text{ untouched}$$  
>   Result: $(3, 2, 2, 1, 1, 1)$. (Already sorted).
> * Step 3: Remove the first element ($3$). Subtract $1$ from the next 3 elements:  
>   $$2-1=1, \quad 2-1=1, \quad 1-1=0, \quad \text{remaining: } 1, 1$$  
>   Result: $(1, 1, 0, 1, 1) \implies \text{Re-sort: } (1, 1, 1, 1, 0)$.
> * Step 4: Remove the first element ($1$). Subtract $1$ from the next 1 element:  
>   $$1-1=0, \quad \text{remaining: } 1, 1, 0$$  
>   Result: $(0, 1, 1, 0) \implies \text{Re-sort: } (1, 1, 0, 0)$.
> * Step 5: Remove the first element ($1$). Subtract $1$ from the next 1 element:  
>   $$1-1=0, \quad \text{remaining: } 0, 0$$  
>   Result: $(0, 0, 0)$.
>
> **Conclusion**: Since we reached a list of all zeros, by the Havel-Hakimi theorem, **the sequence $(5, 4, 3, 3, 2, 2, 1)$ IS GRAPHIC!**

---

## 3. Special Graph Families & Bipartite Graphs

| Graph Family | Notation | Number of Vertices | Number of Edges | Key Property |
| :--- | :---: | :---: | :---: | :--- |
| **Complete Graph** | $K_n$ | $n$ | $\frac{n(n-1)}{2}$ | Every pair of distinct vertices is adjacent; $(n-1)$-regular. |
| **Cycle Graph** | $C_n$ ($n \ge 3$) | $n$ | $n$ | Closed polygon; 2-regular. |
| **Wheel Graph** | $W_n$ ($n \ge 4$) | $n$ | $2(n-1)$ | $C_{n-1}$ cycle connected to a central hub vertex. |
| **Complete Bipartite**| $K_{m,n}$ | $m + n$ | $m \cdot n$ | Vertices partitioned into sets $V_1, V_2$; edges only between sets. |
| **Regular Graph** | $r$-regular | $n$ | $\frac{n \cdot r}{2}$ | Every vertex has the exact same degree $r$. |

---

### 3.3 Bipartite Graphs & The Odd-Cycle Theorem

A graph $G$ is **Bipartite** if its vertex set $V$ can be partitioned into two disjoint subsets $V_1$ and $V_2$ such that every edge connects a vertex in $V_1$ to a vertex in $V_2$ (no edge connects two vertices in the same set).

> 🏆 **THE GOLDEN THEOREM OF BIPARTITE GRAPHS**:  
> **A graph $G$ is Bipartite IF AND ONLY IF it contains NO ODD CYCLES!**  
> * Triangles ($C_3$), pentagons ($C_5$), heptagons ($C_7$) $\implies$ **CANNOT be bipartite!**  
> * Even cycles ($C_4, C_6, C_8$), trees, and hypercubes $\implies$ **ALWAYS bipartite!**

```text
    HOW TO PROVE A GRAPH IS BIPARTITE IN THE EXAM (2-Coloring Method):
    1. Start at any vertex v1. Color it RED (Set V1).
    2. Color all of its immediate neighbors BLUE (Set V2).
    3. Color all of their unvisited neighbors RED.
    4. Continue via BFS:
       - If you ever encounter an edge between TWO VERTICES OF THE SAME COLOR:
         STOP! The graph contains an odd cycle and is NOT bipartite.
       - If you color the entire graph with 2 colors without conflict:
         List the partition V1 and V2. The graph IS bipartite!
```

---

## 4. Graph Isomorphism: The Bulletproof 5-Point Radar

Two graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ are **isomorphic** ($G_1 \cong G_2$) if there exists a **bijective function (one-to-one and onto)** $f: V_1 \to V_2$ that preserves edge adjacency:
$$(u, v) \in E_1 \iff (f(u), f(v)) \in E_2$$

### 4.1 The 5 Invariants Radar (Use this to Disprove or Guide Isomorphism)

```text
       STEP-BY-STEP RADAR (Check in this exact order!):
┌───────────────────────────┬────────────────────────────────────────────────────────┐
│ 1. Vertex Count           │ |V₁| must equal |V₂|. (If not → NOT isomorphic!)       │
├───────────────────────────┼────────────────────────────────────────────────────────┤
│ 2. Edge Count             │ |E₁| must equal |E₂|. (If not → NOT isomorphic!)       │
├───────────────────────────┼────────────────────────────────────────────────────────┤
│ 3. Degree Sequence        │ Both graphs must have the EXACT same degree sequence.  │
│                           │ (e.g., both have degrees: 3, 3, 3, 3, 2, 2).           │
├───────────────────────────┼────────────────────────────────────────────────────────┤
│ 4. Cycle Structures       │ Count cycles of each length!                           │
│                           │ (e.g., if G₁ has a 3-cycle C₃ but G₂ has NO 3-cycles,  │
│                           │ they CANNOT be isomorphic!).                           │
├───────────────────────────┼────────────────────────────────────────────────────────┤
│ 5. Neighborhood Matching  │ Vertices of degree k must connect to vertices of the   │
│                           │ same degrees in both graphs.                           │
└───────────────────────────┴────────────────────────────────────────────────────────┘
```

> ⚠️ **TO PROVE ISOMORPHISM (Full Marks Requirement)**:  
> Finding that all 5 invariants match is **necessary, but NOT sufficient**!  
> You **MUST write down the explicit bijection table** showing the vertex mapping $u_i \mapsto v_j$, and confirm that all edges are preserved!

#### 📝 Worked Exam Example (Exhibiting an Isomorphism):
> Show that the following two graphs $G_1$ and $G_2$ with vertices $\{u_1, u_2, u_3, u_4\}$ and $\{v_1, v_2, v_3, v_4\}$ are isomorphic.
>
> **Solution**:
> 1. Invariants Check:
>    * $|V_1| = |V_2| = 4$.
>    * $|E_1| = |E_2| = 4$.
>    * Both are 2-regular (both form a 4-cycle $C_4$).
> 2. Explicit Bijection Table:  
>    * Map: $f(u_1) = v_1$, $f(u_2) = v_3$, $f(u_3) = v_2$, $f(u_4) = v_4$.
> 3. Verify edges:
>    * $(u_1, u_2) \in E_1 \implies (f(u_1), f(u_2)) = (v_1, v_3) \in E_2$.
>    * $(u_2, u_3) \in E_1 \implies (f(u_2), f(u_3)) = (v_3, v_2) \in E_2$.
>    * $(u_3, u_4) \in E_1 \implies (f(u_3), f(u_4)) = (v_2, v_4) \in E_2$.
>    * $(u_4, u_1) \in E_1 \implies (f(u_4), f(u_1)) = (v_4, v_1) \in E_2$.
>
> All adjacencies are preserved. **Therefore, $G_1 \cong G_2$**.

---

## 5. Eulerian vs. Hamiltonian Graphs (Never Mix Them Up!)

```text
┌──────────────────────┬────────────────────────────────────────────────────────┐
│ Concept              │ What it traverses                                      │
├──────────────────────┼────────────────────────────────────────────────────────┤
│ EULERIAN (Edges)     │ Visits EVERY EDGE exactly once.                        │
├──────────────────────┼────────────────────────────────────────────────────────┤
│ HAMILTONIAN (Vertices│ Visits EVERY VERTEX exactly once.                      │
└──────────────────────┴────────────────────────────────────────────────────────┘
```

### 5.1 Euler Trail & Euler Circuit Conditions (Easy & Exact)
In a connected graph $G$:
1. **Euler Circuit (Closed)**: A closed walk traversing every edge once.  
   $$\mathbf{\iff \text{EVERY vertex has an EVEN degree!}}$$
2. **Euler Trail (Open)**: An open walk traversing every edge once.  
   $$\mathbf{\iff \text{EXACTLY TWO vertices have an ODD degree!}}$$  
   *(The trail MUST start at one odd vertex and terminate at the other odd vertex!).*

---

### 5.2 Hamiltonian Paths & Cycles (Harder; Uses Sufficient Conditions)
* **Hamiltonian Cycle**: A closed cycle visiting every vertex of $G$ exactly once (except start=end).
* **Dirac's Theorem (Sufficient Condition)**:  
  If $G$ is a simple graph with $n \ge 3$ vertices, and:  
  $$\deg(v) \ge \frac{n}{2} \quad \text{for ALL } v \in V$$  
  then $G$ is Hamiltonian!
* **Ore's Theorem (Sufficient Condition)**:  
  If $G$ is a simple graph with $n \ge 3$ vertices, and for every pair of **non-adjacent** vertices $u$ and $v$:  
  $$\deg(u) + \deg(v) \ge n$$  
  then $G$ is Hamiltonian!

---

## 6. Matrix Representations of Graphs

### 6.1 Adjacency Matrix $A(G)$
For a graph with $n$ vertices labeled $v_1, v_2, \dots, v_n$, the Adjacency Matrix $A = [a_{ij}]$ is an $n \times n$ matrix where:
$$a_{ij} = \text{number of edges between } v_i \text{ and } v_j$$

* **For undirected simple graphs**:
  * $A(G)$ is **strictly symmetric** ($a_{ij} = a_{ji}$).
  * All main diagonal entries are **$0$** ($a_{ii} = 0$, no self-loops).
  * The sum of row $i$ equals $\deg(v_i)$.
* 🏆 **THE MATRIX WALK THEOREM (Frequently Asked!)**:  
  **The $(i, j)$-th entry of the matrix power $A^k$ equals the number of walks of length $k$ from vertex $v_i$ to vertex $v_j$!**

---

### 6.2 Incidence Matrix $M(G)$
For a graph with $n$ vertices and $m$ edges labeled $e_1, e_2, \dots, e_m$, the Incidence Matrix $M = [m_{ij}]$ is an $n \times m$ matrix where:
$$m_{ij} = \begin{cases} 1 & \text{if vertex } v_i \text{ is incident on edge } e_j \\ 0 & \text{otherwise} \end{cases}$$

* **Properties for undirected simple graphs**:
  * Every column contains **EXACTLY TWO 1s** (because every edge connects exactly two vertices).
  * The sum of row $i$ equals $\deg(v_i)$.

---

## 7. Shortest Path: Dijkstra's Algorithm (Step-by-Step Table)

Dijkstra's Algorithm finds the shortest path from a starting vertex $S$ to all other vertices in a weighted graph with non-negative edge weights.

### 7.1 The Standard Exam Tabular Method

1. Create a distance array $D[v]$ for all vertices: initialize $D[S] = 0$, and $D[v] = \infty$ for all $v \ne S$.
2. Maintain a set of visited vertices $Visited = \emptyset$.
3. **Loop**:
   * Pick unvisited vertex $u$ with the minimum $D[u]$.
   * Add $u$ to $Visited$.
   * For each unvisited neighbor $v$ of $u$:  
     $$\text{If } D[u] + w(u, v) < D[v] \implies D[v] = D[u] + w(u, v), \quad \text{Predecessor}[v] = u$$
   * Repeat until all vertices are visited.

#### 📝 Worked Exam Example (From Tutorial-4):
> Find the shortest path from source $S$ to all vertices in the graph:  
> Edges: $(S, A)=2, (S, B)=4, (A, B)=1, (A, C)=7, (B, C)=3, (B, D)=5, (C, D)=1$.
>
> | Iteration | Picked Vertex | $D[S]$ | $D[A]$ | $D[B]$ | $D[C]$ | $D[D]$ | Notes / Updates |
> | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
> | Initial | — | **0** | $\infty$ | $\infty$ | $\infty$ | $\infty$ | Source $S$ initialized to 0 |
> | 1 | **$S$** | [0] | $2$ (via S) | $4$ (via S) | $\infty$ | $\infty$ | Relax neighbors $A, B$ |
> | 2 | **$A$** (min=2) | [0] | [2] | $\min(4, 2+1) = \mathbf{3}$ (via A) | $2+7 = \mathbf{9}$ (via A) | $\infty$ | $B$ updated to 3 via $A$ |
> | 3 | **$B$** (min=3) | [0] | [2] | [3] | $\min(9, 3+3) = \mathbf{6}$ (via B) | $3+5 = \mathbf{8}$ (via B) | $C$ updated to 6, $D$ to 8 |
> | 4 | **$C$** (min=6) | [0] | [2] | [3] | [6] | $\min(8, 6+1) = \mathbf{7}$ (via C) | $D$ updated to 7 via $C$ |
> | 5 | **$D$** (min=7) | [0] | [2] | [3] | [6] | [7] | Final destination reached |
>
> **Final Shortest Paths**:
> * To $A$: Length $= 2$, Path $= S \to A$
> * To $B$: Length $= 3$, Path $= S \to A \to B$
> * To $C$: Length $= 6$, Path $= S \to A \to B \to C$
> * To $D$: Length $= 7$, Path $= S \to A \to B \to C \to D$

---

## 💡 Module 4 Summary Checklist & Exam Traps

- [ ] Sum of degrees = $2 \times |E|$. Odd-degree vertices count must be even.
- [ ] Havel-Hakimi: Always sort descending before and after each subtraction!
- [ ] Bipartite: Look for odd cycles ($C_3, C_5$). If none, 2-color it to prove.
- [ ] Euler Circuit: Every vertex degree must be even. Euler Trail: Exactly 2 vertices odd.
- [ ] Walks of length $k$: Compute $A^k$.
- [ ] Dijkstra: Always show the full iteration table to guarantee 10/10 marks.
