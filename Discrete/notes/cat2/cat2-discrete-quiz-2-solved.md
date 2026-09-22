# MAT2002: Discrete Mathematics & Graph Theory
## QUIZ-2 Master Solutions — Module 4 (Graphs & Matrix Representations)
**Faculty**: Dr. Suresh Dara | **Scope**: Module 4 (CAT-2)  
**Format**: Ready for Direct Exam-Hall Copy / Open-Book Reference

---

## Question 1: Complements and Isomorphism of Graphs

### Problem Statement
Draw the complements of the following two graphs. Are these complements isomorphic to each other? Justify your answer.

![Quiz 2 Question 1 Graphs](file:///c:/Users/ankit/Fall2627/Discrete/resources/quiz2_q1_graphs.png)

---

### Step-by-Step Solution

#### Step 1: Formal Characterization of Given Graphs $G$ and $H$

Both graphs have order $n = |V| = 6$ and size $e = |E| = 8$.

1. **Graph $G = (V_G, E_G)$**:
   * **Vertex Set**: $V_G = \{u_1, u_2, u_3, u_4, u_5, u_6\}$
   * **Edge Set**: 
     $$E_G = \{(u_1, u_2), (u_1, u_6), (u_2, u_3), (u_2, u_5), (u_6, u_5), (u_6, u_3), (u_4, u_3), (u_4, u_5)\}$$
   * **Degree of each vertex in $G$**:
     $$\deg_G(u_1) = 2, \quad \deg_G(u_4) = 2, \quad \deg_G(u_2) = 3, \quad \deg_G(u_3) = 3, \quad \deg_G(u_5) = 3, \quad \deg_G(u_6) = 3$$
     * Degree sequence of $G$: $(3, 3, 3, 3, 2, 2)$
   * **Bipartite Property**:
     * Partition $V_G$ into two disjoint sets: $V_1 = \{u_1, u_3, u_5\}$ and $V_2 = \{u_2, u_4, u_6\}$.
     * Notice:
       * $u_1$ connects only to $\{u_2, u_6\} \subset V_2$.
       * $u_3$ connects only to $\{u_2, u_4, u_6\} = V_2$.
       * $u_5$ connects only to $\{u_2, u_4, u_6\} = V_2$.
     * There is NO edge between any pair of vertices within $V_1$, and NO edge within $V_2$.
     * Thus, **$G$ is a bipartite graph** ($G \cong K_{3,3} - \{(u_1, u_4)\}$).
     * By Kőnig's Theorem, **$G$ contains NO odd cycles** (it contains 0 triangles, i.e., zero 3-cycles).

2. **Graph $H = (V_H, E_H)$**:
   * **Vertex Set**: $V_H = \{v_1, v_2, v_3, v_4, v_5, v_6\}$
   * **Edge Set**:
     $$E_H = \{(v_1, v_2), (v_1, v_6), (v_2, v_6), (v_2, v_3), (v_6, v_5), (v_5, v_3), (v_4, v_3), (v_4, v_5)\}$$
   * **Degree of each vertex in $H$**:
     $$\deg_H(v_1) = 2, \quad \deg_H(v_4) = 2, \quad \deg_H(v_2) = 3, \quad \deg_H(v_3) = 3, \quad \deg_H(v_5) = 3, \quad \deg_H(v_6) = 3$$
     * Degree sequence of $H$: $(3, 3, 3, 3, 2, 2)$
   * **Triangles in $H$**:
     * Triangle 1: on vertices $\{v_1, v_2, v_6\}$ with edges $(v_1, v_2), (v_2, v_6), (v_6, v_1)$.
     * Triangle 2: on vertices $\{v_4, v_3, v_5\}$ with edges $(v_4, v_3), (v_3, v_5), (v_5, v_4)$.
     * Thus, **$H$ contains exactly TWO triangles (3-cycles)**.

---

#### Step 2: Construction and Edge Lists of Complements $\overline{G}$ and $\overline{H}$

For any simple graph on $n = 6$ vertices, the complete graph $K_6$ has $\binom{6}{2} = 15$ edges.
Since $|E(G)| = |E(H)| = 8$, both complements have:
$$|E(\overline{G})| = 15 - 8 = 7 \text{ edges}, \qquad |E(\overline{H})| = 15 - 8 = 7 \text{ edges}$$

The degree of each vertex in the complement is given by $\deg_{\overline{G}}(v) = (n - 1) - \deg_G(v) = 5 - \deg_G(v)$:
* Vertices of degree 2 in $G$ have degree $5 - 2 = 3$ in $\overline{G}$.
* Vertices of degree 3 in $G$ have degree $5 - 3 = 2$ in $\overline{G}$.
* Degree sequence of both $\overline{G}$ and $\overline{H}$: $(3, 3, 2, 2, 2, 2)$.

##### Explicit Edge Set of Complement $\overline{G}$:
In $G$, $V_1 = \{u_1, u_3, u_5\}$ and $V_2 = \{u_2, u_4, u_6\}$ had no internal edges, and the cross edge $(u_1, u_4)$ was missing. Therefore, $\overline{G}$ contains:
1. All 3 edges within $V_1$: $\{(u_1, u_3), (u_3, u_5), (u_1, u_5)\}$ (forms a triangle $C_3$ on $V_1$).
2. All 3 edges within $V_2$: $\{(u_2, u_4), (u_4, u_6), (u_2, u_6)\}$ (forms a triangle $C_3$ on $V_2$).
3. The 1 missing cross-edge between $V_1$ and $V_2$: $(u_1, u_4)$.
$$E(\overline{G}) = \{(u_1, u_3), (u_3, u_5), (u_1, u_5), (u_2, u_4), (u_4, u_6), (u_2, u_6), (u_1, u_4)\}$$

##### Explicit Edge Set of Complement $\overline{H}$:
The missing edges in $H$ are:
1. From $v_1$ (non-adjacent to $v_3, v_4, v_5$): $\{(v_1, v_3), (v_1, v_4), (v_1, v_5)\}$.
2. From $v_4$ (non-adjacent to $v_1, v_2, v_6$): $\{(v_4, v_1), (v_4, v_2), (v_4, v_6)\}$.
3. Cross-diagonal non-edges: $(v_2, v_5)$ and $(v_3, v_6)$.
$$E(\overline{H}) = \{(v_1, v_3), (v_1, v_4), (v_1, v_5), (v_4, v_2), (v_4, v_6), (v_2, v_5), (v_3, v_6)\}$$

---

#### Step 3: Visual Structure / Drawings of $\overline{G}$ and $\overline{H}$

```
        COMPLEMENT G-BAR                             COMPLEMENT H-BAR
       ------------------                           ------------------

         u1 -------- u4                                     v1
        /  \        /  \                                  / | \
       /    \      /    \                                /  |  \
      u3 -- u5    u2 -- u6                             v3   |   v5
                                                       |    |   |
  (Two disjoint triangles:                             v6   |   v2
   {u1, u3, u5} and {u2, u4, u6},                       \   |   /
   connected by the bridge edge (u1, u4))                \  |  /
                                                            v4

                                               (A 6-cycle v1-v3-v6-v4-v2-v5-v1
                                                plus one chord (v1, v4))
```

---

#### Step 4: Isomorphism Investigation & Rigorous Justification

**Question**: Are the complements $\overline{G}$ and $\overline{H}$ isomorphic?  
**Answer**: **NO, $\overline{G}$ and $\overline{H}$ are NOT isomorphic ($\overline{G} \not\cong \overline{H}$)**.

##### Justification Method 1 (Via the Fundamental Complement Isomorphism Theorem):
* **Theorem**: Two simple graphs $G_1$ and $G_2$ are isomorphic if and only if their complements are isomorphic:
  $$G_1 \cong G_2 \iff \overline{G_1} \cong \overline{G_2}$$
* In the original graphs:
  * $G$ is bipartite, so it contains **0 triangles** ($N_{C_3}(G) = 0$).
  * $H$ contains **2 triangles**: $\{v_1, v_2, v_6\}$ and $\{v_4, v_3, v_5\}$ ($N_{C_3}(H) = 2$).
  * Since the number of 3-cycles is a preserved graph invariant under isomorphism, $G \not\cong H$.
* Therefore, by the biconditional theorem, their complements cannot be isomorphic:
  $$G \not\cong H \implies \mathbf{\overline{G} \not\cong \overline{H}}$$

##### Justification Method 2 (Direct Invariant Analysis on $\overline{G}$ and $\overline{H}$):
1. **Cycle Invariant (Number of Triangles $C_3$)**:
   * In $\overline{G}$:
     * The subgraph induced by $\{u_1, u_3, u_5\}$ is a triangle $K_3$.
     * The subgraph induced by $\{u_2, u_4, u_6\}$ is a triangle $K_3$.
     * Total number of triangles in $\overline{G}$ is **2**.
   * In $\overline{H}$:
     * The edges form a Hamiltonian 6-cycle $C_6 = (v_1 - v_3 - v_6 - v_4 - v_2 - v_5 - v_1)$ with a single chord $(v_1, v_4)$ between opposite vertices.
     * The chord divides the 6-cycle into two 4-cycles: $(v_1 - v_3 - v_6 - v_4 - v_1)$ and $(v_1 - v_5 - v_2 - v_4 - v_1)$.
     * Total number of triangles in $\overline{H}$ is **0**.
   * Since graph isomorphism preserves the number of cycles of each length, and $N_{C_3}(\overline{G}) = 2 \ne 0 = N_{C_3}(\overline{H})$, **$\overline{G}$ and $\overline{H}$ are non-isomorphic**.

2. **Bridge / Cut-Edge Invariant**:
   * In $\overline{G}$, the edge $(u_1, u_4)$ is a **bridge** (cut-edge); removing it disconnects $\overline{G}$ into two separate components.
   * In $\overline{H}$, there are **no bridges**; every edge lies on at least one cycle (2-edge-connected).
   * Since the number of bridges is an isomorphism invariant, **$\overline{G} \not\cong \overline{H}$**.

---

## Question 2: Self-Complementary Graph with 6 Vertices

### Problem Statement
Can there exist a self-complementary graph with 6 vertices? Justify your answer.

---

### Step-by-Step Solution

#### 1. Definition
A simple graph $G = (V, E)$ is called **self-complementary** if it is isomorphic to its complement:
$$G \cong \overline{G}$$

#### 2. Derivation of Edge Formula
Let $n = |V|$ be the number of vertices, and $q = |E(G)|$ be the number of edges.
* The complete graph $K_n$ has $\binom{n}{2} = \frac{n(n-1)}{2}$ edges.
* The sum of edges in $G$ and its complement $\overline{G}$ is:
  $$|E(G)| + |E(\overline{G})| = \frac{n(n-1)}{2}$$
* Since $G \cong \overline{G}$, an isomorphism preserves the number of edges:
  $$|E(G)| = |E(\overline{G})| = q$$
* Substituting:
  $$q + q = \frac{n(n-1)}{2} \implies 2q = \frac{n(n-1)}{2} \implies \mathbf{q = \frac{n(n-1)}{4}}$$

#### 3. Test for $n = 6$ Vertices
Substitute $n = 6$ into the edge formula:
$$q = \frac{6(6 - 1)}{4} = \frac{6 \times 5}{4} = \frac{30}{4} = 7.5$$

#### 4. Conclusion & Justification
* In any graph, the number of edges $q$ must be a **non-negative integer** ($q \in \mathbb{Z}_{\ge 0}$).
* Because $7.5 \notin \mathbb{Z}$, it is mathematically impossible to divide the 15 edges of $K_6$ equally between $G$ and $\overline{G}$.
* **General Necessary Condition**: For $q = \frac{n(n-1)}{4}$ to be an integer, $n(n-1)$ must be divisible by 4. This requires:
  $$n \equiv 0 \pmod 4 \quad \text{or} \quad n \equiv 1 \pmod 4$$
* For $n = 6$: $6 \equiv 2 \pmod 4$, which fails the condition.
* **Final Answer**: **NO**, there cannot exist a self-complementary graph with 6 vertices.

---

## Question 3: Havel-Hakimi Test on Degree Sequence (6,6,5,5,4,4,3,3)

### Problem Statement
Does the given degree sequence $(6, 6, 5, 5, 4, 4, 3, 3)$ represent a graph? Justify your answer.

---

### Step-by-Step Solution

#### Step 1: Preliminary Checks
1. **Number of vertices**: $n = 8$.
2. **Maximum degree check**: $\Delta = 6 \le n - 1 = 7$. (Valid)
3. **Euler's Handshaking Lemma Check (Sum of Degrees)**:
   $$\sum_{i=1}^{8} d_i = 6 + 6 + 5 + 5 + 4 + 4 + 3 + 3 = 36$$
   * Since $36$ is an **even number**, it satisfies the necessary condition that $\sum d_i = 2e$.
   * Number of odd-degree vertices = 4 (which is even). (Valid)

#### Step 2: Application of Havel-Hakimi Theorem
**Havel-Hakimi Theorem**: A non-increasing sequence of non-negative integers $S = (d_1, d_2, \dots, d_n)$ is graphic if and only if the sequence:
$$S' = (d_2 - 1, d_3 - 1, \dots, d_{d_1 + 1} - 1, d_{d_1 + 2}, \dots, d_n)$$
(sorted in non-increasing order) is graphic.

Let us execute the reduction step by step:

* **Initial Sequence $S_0$**:
  $$S_0 = (6, 6, 5, 5, 4, 4, 3, 3)$$
  * $d_1 = 6$. Delete $6$, subtract $1$ from the next $6$ elements:
    $$(6-1, 5-1, 5-1, 4-1, 4-1, 3-1, 3) = (5, 4, 4, 3, 3, 2, 3)$$
  * Sort in non-increasing order:
    $$S_1 = (5, 4, 4, 3, 3, 3, 2)$$

* **Iteration 1 on $S_1$**:
  * $d_1 = 5$. Delete $5$, subtract $1$ from the next $5$ elements:
    $$(4-1, 4-1, 3-1, 3-1, 3-1, 2) = (3, 3, 2, 2, 2, 2)$$
  * Already sorted:
    $$S_2 = (3, 3, 2, 2, 2, 2)$$

* **Iteration 2 on $S_2$**:
  * $d_1 = 3$. Delete $3$, subtract $1$ from the next $3$ elements:
    $$(3-1, 2-1, 2-1, 2, 2) = (2, 1, 1, 2, 2)$$
  * Sort in non-increasing order:
    $$S_3 = (2, 2, 2, 1, 1)$$

* **Iteration 3 on $S_3$**:
  * $d_1 = 2$. Delete $2$, subtract $1$ from the next $2$ elements:
    $$(2-1, 2-1, 1, 1) = (1, 1, 1, 1)$$
  * Already sorted:
    $$S_4 = (1, 1, 1, 1)$$

* **Iteration 4 on $S_4$**:
  * The sequence $(1, 1, 1, 1)$ consists of 4 vertices, each of degree 1.
  * This is clearly graphic: it represents two disjoint edges ($2K_2$, i.e., $u-v$ and $w-z$).
  * Formally, deleting $d_1 = 1$: $(1-1, 1, 1) = (0, 1, 1) \to (1, 1, 0) \to (0, 0, 0)$ (all zeros, which is trivially graphic).

#### Step 3: Conclusion
Since the reduction terminates in an all-zero sequence $(0, 0, 0)$ without generating negative numbers:
* **YES**, the given degree sequence $(6, 6, 5, 5, 4, 4, 3, 3)$ **represents a simple graph (it is graphic)**.

---

## Question 4: 3-Regular Graph with More Than 5 Vertices

### Problem Statement
Draw the 3-regular graph with more than 5 vertices.

---

### Step-by-Step Solution

#### 1. Parity Constraint for 3-Regular Graphs
* In an $r$-regular graph on $n$ vertices, every vertex has degree $r = 3$.
* By Euler's Handshaking Lemma:
  $$\sum_{v \in V} \deg(v) = 3n = 2e \implies e = \frac{3n}{2}$$
* For $e$ to be an integer, **$n$ must be an even integer**.
* Given $n > 5$, the smallest possible order is **$n = 6$** (since $n = 7$ is impossible for a 3-regular graph).

---

#### 2. Construction 1: Complete Bipartite Graph $K_{3,3}$ (Utility Graph)
* **Order**: $n = 6$ vertices.
* **Partition**: $V = V_1 \cup V_2$ where $V_1 = \{u_1, u_2, u_3\}$ and $V_2 = \{v_1, v_2, v_3\}$.
* **Edges**: Every vertex in $V_1$ is connected to every vertex in $V_2$:
  $$E = \{(u_i, v_j) \mid i, j \in \{1, 2, 3\}\}$$
  $$\text{Total Edges } e = 3 \times 3 = 9$$
* **Degree**: $\deg(u_i) = 3$ and $\deg(v_j) = 3$ for all vertices $\implies$ **3-regular**.

```
          u1 ------------ u2 ------------ u3       (Set V1)
          |  \          / | \          /  |
          |    \      /   |   \      /    |
          |      \  /     |     \  /      |
          |       /\      |      /\       |
          |     /    \    |    /    \     |
          |   /        \  |  /        \   |
          v1 ------------ v2 ------------ v3       (Set V2)
```

---

#### 3. Construction 2: 3-Prism Graph $Y_3$ ($K_3 \times K_2$)
* **Order**: $n = 6$ vertices.
* **Structure**: Two disjoint triangles (3-cycles) connected by 3 matching vertical edges:
  * Triangle 1: $\{u_1, u_2, u_3\}$ with edges $(u_1, u_2), (u_2, u_3), (u_3, u_1)$.
  * Triangle 2: $\{v_1, v_2, v_3\}$ with edges $(v_1, v_2), (v_2, v_3), (v_3, v_1)$.
  * Vertical Matching: $(u_1, v_1), (u_2, v_2), (u_3, v_3)$.
* **Total Edges**: $3 + 3 + 3 = 9$.
* **Degree**: Each vertex has 2 edges in its triangle $+ 1$ matching edge $= 3$.

```
               u1
              /  \
             /    \
            u2 -- u3
            |      |
            |  v1  |
            | /  \ |
            |/    \|
            v2 -- v3
```

*(Both $K_{3,3}$ and $Y_3$ are valid 3-regular graphs on 6 vertices. $K_{3,3}$ is bipartite; $Y_3$ is planar).*

---

## Question 5: Graph with Specific Parity and Degree Bounds

### Problem Statement
Give an example of a graph $G$ with an even number of odd degree vertices and an odd number of even degree vertices, minimum degree is 2, and maximum degree greater than 4.

---

### Step-by-Step Solution

#### 1. Specification Analysis
We need to construct a simple graph $G$ satisfying all 4 constraints simultaneously:
1. **$n_{\text{odd}}$ is even**: (Mandated by Handshaking Lemma; let $n_{\text{odd}} = 2$).
2. **$n_{\text{even}}$ is odd**: (Let $n_{\text{even}} = 5$).
   * Total vertices: $n = n_{\text{odd}} + n_{\text{even}} = 2 + 5 = 7$.
3. **Minimum degree $\delta(G) \ge 2$**: Every vertex has degree $\ge 2$ (no leaves or isolated vertices).
4. **Maximum degree $\Delta(G) > 4$**: At least one vertex has degree $\ge 5$.

#### 2. Choosing the Degree Sequence
Let the 2 odd vertices have degree 5:
* Odd vertices: $d_1 = 5, d_2 = 5$ (Count = 2, which is even; $\Delta = 5 > 4$).
Let the 5 even vertices have degree 2:
* Even vertices: $d_3 = 2, d_4 = 2, d_5 = 2, d_6 = 2, d_7 = 2$ (Count = 5, which is odd; $\delta = 2 \ge 2$).

Degree sequence:
$$S = (5, 5, 2, 2, 2, 2, 2)$$

#### 3. Verification of Graphic Nature (Havel-Hakimi)
* Sum of degrees $= 5 + 5 + 2 + 2 + 2 + 2 + 2 = 20$ (even!).
* Apply Havel-Hakimi:
  * $S_0 = (5, 5, 2, 2, 2, 2, 2)$
  * Delete first 5, subtract 1 from next 5 elements:
    $$(5-1, 2-1, 2-1, 2-1, 2-1, 2) = (4, 1, 1, 1, 1, 2)$$
  * Sort descending:
    $$S_1 = (4, 2, 1, 1, 1, 1)$$
  * Delete 4, subtract 1 from next 4 elements:
    $$(2-1, 1-1, 1-1, 1-1, 1) = (1, 0, 0, 0, 1) \to (1, 1, 0, 0, 0)$$
  * Sequence $(1, 1, 0, 0, 0)$ is clearly graphic (a single edge and 3 isolated vertices).
  * Hence, the degree sequence is graphic!

#### 4. Explicit Graph Construction & Adjacency
* **Vertices**: $V = \{A, B, v_1, v_2, v_3, v_4, v_5\}$.
* Connect both hubs $A$ and $B$ to each other, and connect both $A$ and $B$ to all 4 vertices $v_1, v_2, v_3, v_4$:
  * Edge between hubs: $(A, B)$ (adds 1 to degree of $A$ and $B$).
  * Connect $A$ to $\{v_1, v_2, v_3, v_4\}$: edges $(A, v_1), (A, v_2), (A, v_3), (A, v_4)$.
  * Connect $B$ to $\{v_1, v_2, v_3, v_5\}$: edges $(B, v_1), (B, v_2), (B, v_3), (B, v_5)$.
  * Connect $v_4$ and $v_5$ to each other: edge $(v_4, v_5)$.
* **Check Degrees**:
  * $\deg(A) = 1 (\text{to } B) + 4 (\text{to } v_1, v_2, v_3, v_4) = 5$ (Odd degree, $\Delta = 5 > 4$).
  * $\deg(B) = 1 (\text{to } A) + 4 (\text{to } v_1, v_2, v_3, v_5) = 5$ (Odd degree).
  * $\deg(v_1) = 2$ (connected to $A, B$) $\implies$ Even.
  * $\deg(v_2) = 2$ (connected to $A, B$) $\implies$ Even.
  * $\deg(v_3) = 2$ (connected to $A, B$) $\implies$ Even.
  * $\deg(v_4) = 2$ (connected to $A, v_5$) $\implies$ Even.
  * $\deg(v_5) = 2$ (connected to $B, v_4$) $\implies$ Even.
* **Summary Table**:
  | Condition | Required | In This Graph | Satisfied? |
  | :--- | :--- | :--- | :---: |
  | Odd-degree vertices count | Even | 2 (vertices $A, B$ have degree 5) | **YES** |
  | Even-degree vertices count | Odd | 5 (vertices $v_1, v_2, v_3, v_4, v_5$ have degree 2) | **YES** |
  | Minimum degree $\delta(G)$ | $\ge 2$ | $\min\{5, 5, 2, 2, 2, 2, 2\} = 2$ | **YES** |
  | Maximum degree $\Delta(G)$ | $> 4$ | $\max\{5, 5, 2, 2, 2, 2, 2\} = 5$ | **YES** |

---

## Question 6: Test on Degree Sequence (5,5,4,3,3,2,1)

### Problem Statement
Can there exist a graph with the given degree sequence $(5, 5, 4, 3, 3, 2, 1)$? Justify your answer.

---

### Step-by-Step Solution

#### 1. Identification of Odd-Degree Vertices
In the sequence $(5, 5, 4, 3, 3, 2, 1)$, list the degrees of each vertex:
* Degree 5 (Odd)
* Degree 5 (Odd)
* Degree 4 (Even)
* Degree 3 (Odd)
* Degree 3 (Odd)
* Degree 2 (Even)
* Degree 1 (Odd)

Total count of odd-degree vertices:
$$n_{\text{odd}} = 5 \quad (\text{the vertices with degrees } 5, 5, 3, 3, 1)$$

Notice that $n_{\text{odd}} = 5$ is an **ODD number**.

#### 2. Theoretical Proof via Euler's Handshaking Lemma
* **Euler's Handshaking Lemma**: For any undirected graph $G = (V, E)$:
  $$\sum_{v \in V} \deg(v) = 2 |E|$$
* Partition the vertex set $V$ into two disjoint sets:
  * $V_{\text{even}} = \{v \in V \mid \deg(v) \text{ is even}\}$
  * $V_{\text{odd}} = \{v \in V \mid \deg(v) \text{ is odd}\}$
* The sum of all degrees is:
  $$\sum_{v \in V_{\text{even}}} \deg(v) + \sum_{v \in V_{\text{odd}}} \deg(v) = 2 |E|$$
* Analysis of terms:
  1. The right-hand side $2|E|$ is always **even**.
  2. The sum of even integers $\sum_{v \in V_{\text{even}}} \deg(v)$ is always **even**.
  3. Therefore, the remaining sum must be even:
     $$\sum_{v \in V_{\text{odd}}} \deg(v) = 2|E| - \sum_{v \in V_{\text{even}}} \deg(v) = \text{Even} - \text{Even} = \mathbf{\text{Even}}$$
  4. The sum of $k$ odd numbers is even if and only if $k$ is **EVEN**.
  5. Therefore, $|V_{\text{odd}}|$ must be an **EVEN integer**.

#### 3. Handshaking Sum Calculation
Alternatively, summing the given degrees directly:
$$\sum d_i = 5 + 5 + 4 + 3 + 3 + 2 + 1 = 23$$
If this were a graph with size $e$, then:
$$2e = 23 \implies e = \frac{23}{2} = 11.5 \notin \mathbb{Z}$$
Since the number of edges must be an integer, $2e$ cannot be odd.

#### 4. Final Answer
**NO, such a graph CANNOT exist**, because:
1. The sum of the degrees is 23 (an odd number), which violates Euler's Handshaking Lemma ($2e$ must be even).
2. The number of odd-degree vertices is 5 (an odd count), which contradicts the theorem that every graph must have an even number of odd-degree vertices.

---

## Question 7: General Degree Formula Proof

### Problem Statement
If a $(p, q)$ graph $G$ has $n$ points of degree $k$ and the remaining points are of degree $k + 1$, then prove that:
$$n = (k + 1)p - 2q$$

---

### Step-by-Step Formal Proof

#### Given Information:
1. Order of graph $G$: Total number of points (vertices) $|V| = p$.
2. Size of graph $G$: Total number of lines (edges) $|E| = q$.
3. Exactly $n$ vertices have degree $k$.
4. The remaining vertices have degree $k + 1$.
   * Number of remaining vertices $= p - n$.

#### Proof:
1. By **Euler's Handshaking Lemma**, the sum of degrees of all vertices in any graph is equal to twice the number of edges:
   $$\sum_{v \in V} \deg(v) = 2q$$

2. Partition the sum into the two groups of vertices:
   $$\sum_{\substack{v \in V \\ \deg(v) = k}} \deg(v) + \sum_{\substack{v \in V \\ \deg(v) = k + 1}} \deg(v) = 2q$$

3. Substitute the degrees and vertex counts:
   $$n \cdot k + (p - n) \cdot (k + 1) = 2q$$

4. Expand the algebraic expression:
   $$n \cdot k + p(k + 1) - n(k + 1) = 2q$$
   $$n k + p(k + 1) - n k - n = 2q$$

5. Notice that the terms $+nk$ and $-nk$ cancel out:
   $$p(k + 1) - n = 2q$$

6. Rearrange to isolate $n$:
   $$-n = 2q - p(k + 1)$$
   $$\mathbf{n = (k + 1)p - 2q}$$

**Hence Proved (Q.E.D.)**.

---

## Question 8: Non-Isomorphic Graphs with Same Vertices and Edges

### Problem Statement
Give an example of non-isomorphic graphs with the same number of vertices and the same number of edges. Justify your answer.

---

### Step-by-Step Solution

#### Example 1: Connected vs. Disconnected Graphs ($p = 6, q = 6$)

Construct two graphs $G_1$ and $G_2$ with $n = 6$ vertices and $e = 6$ edges:

1. **Graph $G_1$**: The 6-Cycle Graph $C_6$
   * Vertices: $\{1, 2, 3, 4, 5, 6\}$
   * Edges: $\{(1,2), (2,3), (3,4), (4,5), (5,6), (6,1)\}$
   * Degree sequence: $(2, 2, 2, 2, 2, 2)$
   * Number of connected components: $c(G_1) = 1$ (Connected).

2. **Graph $G_2$**: Union of two disjoint 3-Cycles $2C_3 = C_3 \cup C_3$
   * Vertices: $\{a, b, c\} \cup \{d, e, f\}$
   * Edges: $\{(a,b), (b,c), (c,a)\} \cup \{(d,e), (e,f), (f,d)\}$
   * Degree sequence: $(2, 2, 2, 2, 2, 2)$
   * Number of connected components: $c(G_2) = 2$ (Disconnected).

```
         GRAPH G1 (C6)                       GRAPH G2 (2 C3)
        ---------------                     -----------------
             1 --- 2                             a           d
            /       \                           / \         / \
           6         3                         b---c       e---f
            \       /
             5 --- 4                     (Two disjoint triangles)
          (One single loop)
```

##### Justification:
* Both graphs have identical order: $|V(G_1)| = |V(G_2)| = 6$.
* Both graphs have identical size: $|E(G_1)| = |E(G_2)| = 6$.
* Both graphs have identical degree sequence: $(2, 2, 2, 2, 2, 2)$ (both are 2-regular).
* **Proof of Non-Isomorphism**:
  * The number of connected components is a preserved graph invariant under isomorphism.
  * $G_1$ has **1 connected component**; $G_2$ has **2 connected components**.
  * Cycle length invariant: $G_2$ contains cycles of length 3 ($C_3$), whereas $G_1$ contains no cycles of length 3 (shortest cycle length in $G_1$ is 6).
  * Since an isomorphism must preserve connectivity and cycle lengths, **$G_1 \not\cong G_2$**.

---

#### Example 2: Trees on 4 Vertices ($p = 4, q = 3$) with Distinct Degree Sequences

1. **Path Graph $P_4$**:
   * Vertices: $\{1, 2, 3, 4\}$, Edges: $\{(1,2), (2,3), (3,4)\}$.
   * Degree sequence: $(2, 2, 1, 1)$.
   * Maximum degree: $\Delta = 2$.

2. **Star Graph $K_{1,3}$**:
   * Vertices: $\{c, l_1, l_2, l_3\}$, Edges: $\{(c, l_1), (c, l_2), (c, l_3)\}$.
   * Degree sequence: $(3, 1, 1, 1)$.
   * Maximum degree: $\Delta = 3$.

```
         PATH P4                             STAR K1,3
       -----------                          -----------
                                                 l1
                                                 |
       1 --- 2 --- 3 --- 4                  l2 - c - l3
```

##### Justification:
* Both have $|V| = 4$ and $|E| = 3$.
* Under any isomorphism $f: V(P_4) \to V(K_{1,3})$, degree must be preserved: $\deg(f(v)) = \deg(v)$.
* $K_{1,3}$ has a vertex of degree 3, but $P_4$ has no vertex of degree 3.
* Therefore, no bijection can preserve degrees, so **$P_4 \not\cong K_{1,3}$**.
