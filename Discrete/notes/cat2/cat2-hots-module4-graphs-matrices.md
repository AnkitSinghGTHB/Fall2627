# ⚡ CAT-2 HOTS Master Crib — Module 4: Graphs & Matrix Representations
**Course**: MAT2002 — Discrete Mathematics & Graph Theory  
**Level**: Self-Contained / Zero-Assumption (From Bedrock Basics to HOTS)  
**Exam Mode**: Open Book / Handwritten Notes Allowed | **Target Score**: 45+ / 50

---

## 🧱 TIER 0: The "Explain Like I'm 5" Bedrock Basics
*(Read this first if you forgot everything about graphs)*

### 1. What is a Graph, Vertex, and Edge?
* **Vertex (plural: Vertices)**: Just a dot or node (like a city).
* **Edge**: A line connecting two dots (like a road between two cities).
* **Simple Graph**: No road connects a city to itself (no loops), and at most one road connects any two cities (no parallel edges).

---

### 2. What is Degree & The Handshaking Theorem?
* **Degree of a vertex ($\deg(v)$)**: Count how many lines are sticking out of that dot.
* **The Handshaking Rule**:
  > Every time two people shake hands, **TWO hands are involved**.  
  > So if you sum up all the degrees of all vertices, it **MUST EQUAL $2 \times \text{number of edges}$** ($\sum \deg(v) = 2|E|$).
* **Exam Super-Trick**:
  Because $\sum \deg(v) = 2|E|$ is always an EVEN number, **the number of vertices with ODD degrees MUST BE EVEN**.
  * If a question gives you a sequence with an ODD number of odd numbers (like $3, 3, 3, 2$) $\implies$ **INSTANT IMPOSSIBILITY ❌**.

---

### 3. What is a "Degree Sequence" & What Does "Graphic" Mean?
* A list of the degrees of all vertices, usually written from biggest to smallest: e.g., $(4, 3, 3, 2, 2)$.
* **"Is it graphic?"** means: *Can you actually draw a real simple graph using these exact numbers?*
* You test this using the **Havel-Hakimi Algorithm** (peeling off the biggest number and subtracting 1 from its neighbors).

---

### 4. What is a Bipartite Graph? (The "Two Teams" Concept)
* Can you color all the dots using only **TWO colors (Red and Blue)** such that **NO line connects two dots of the same color**?
* *Think of it like a dance*: Boys (Red) only dance with Girls (Blue). A boy never dances with a boy, and a girl never dances with a girl.
* **The Triangle Rule**:
  If a graph has a triangle ($3$ dots in a cycle) or ANY odd cycle ($5$ dots, $7$ dots), it is **IMPOSSIBLE to be bipartite!**
  * *Why?* Try coloring a triangle with 2 colors: Dot 1 is Red, Dot 2 is Blue, Dot 3 touches both $\implies$ trapped!

---

### 5. What is Graph Isomorphism? (Identical Twins in Disguise)
* Two graphs $G_1$ and $G_2$ are **isomorphic ($G_1 \cong G_2$)** if they are the **exact same graph drawn differently** (like rotating or stretching a rubber band network).
* How to prove they are the same: Give a 1-to-1 matching dictionary $f$ matching each dot in $G_1$ to its twin in $G_2$.

---

### 6. What is an Adjacency Matrix & Why Multiply It ($A^k$)?
* An $n \times n$ grid where row $i$ and column $j$ has a **$1$** if there's a line between dot $i$ and dot $j$, and **$0$** if there isn't.
* **The Matrix Power Magic**:
  * $A^1$: Shows direct 1-step roads.
  * $A^2$: The number in cell $(i, j)$ of $A^2$ tells you **how many 2-step walks exist from city $i$ to city $j$!** (Which is just the number of common friends they share!).
  * Cell $(i, i)$ on the diagonal of $A^2$ is simply the **degree of vertex $i$**!

---

### 7. What is Euler vs Hamilton? (The Line vs Dot Challenge)
* **Euler Path / Circuit**: Visits every **ROAD (Edge)** exactly once.
  * *Rule*: If every dot has an **EVEN degree** $\implies$ **Euler Circuit** exists.
  * *Rule*: If exactly **TWO dots have ODD degree** $\implies$ **Euler Path** exists (starts at one odd dot, ends at the other).
* **Hamilton Path / Circuit**: Visits every **CITY (Vertex)** exactly once.
  * *Rule (Dirac's Theorem)*: If every city has degree $\ge n/2$ $\implies$ Hamilton circuit is guaranteed.

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If Question Shows... | It Means This Exact Problem | What You Do (In 5 Seconds) |
| :--- | :--- | :--- |
| Numbers like $(5, 4, 3, 3, 2, 1)$, "Is it graphic?" | **Havel-Hakimi Algorithm** | Check sum $\to$ if odd, reject. If even $\to$ delete first number $d_1$, subtract 1 from next $d_1$ numbers. Repeat. |
| "Is the graph bipartite?" | **Bipartite Check** | Start coloring with Red and Blue. If you ever need to color two connected dots the same color $\implies$ **NOT bipartite (odd cycle found)**. |
| Two pictures of graphs, "Are they isomorphic?" | **Isomorphism Proof** | Count vertices, edges, and degree list. If all match $\to$ match unique vertices and write bijective table $f(u) = v$. |
| Adjacency matrix $A$, "Find number of walks of length 2" | **Matrix Walks** | Entry $(i, j)$ of $A^2 = \text{Row } i \cdot \text{Column } j = \text{common neighbors of } i \text{ and } j$. |
| Weighted map with distances, "Shortest path" | **Dijkstra's Algorithm** | Use the distance update table. Box the smallest unvisited dot at each turn. |

---

## 🛠️ TIER 2: Step-by-Step Execution Recipes

### Recipe 1: Havel-Hakimi Graphic Test (The Subtraction Dance)
1. **Sum Check**: Add up all the numbers in the sequence. If the sum is **ODD**, stop and write: *"Sum of degrees is odd, violates Handshaking Theorem, NOT graphic ❌."*
2. **Sort**: Put numbers in descending order (e.g. $4, 3, 3, 2, 2$).
3. **Drop and Subtract**:
   - Take the first number, say $d_1 = 4$.
   - Cross it off.
   - Subtract $1$ from the next $4$ numbers.
4. **Re-sort**: Put the new list in descending order.
5. **Repeat** until:
   - All numbers are $0 \implies$ **GRAPHIC ✅** (It can be drawn!).
   - Any number becomes negative OR you need to subtract from more numbers than exist $\implies$ **NOT GRAPHIC ❌**.

---

### Recipe 2: 2-Coloring Test for Bipartite Graphs
1. Pick any dot, label it **R (Red)**.
2. Label all its immediate neighbors **B (Blue)**.
3. Label all neighbors of Blue dots as **R (Red)**.
4. If at any step, two connected dots are forced to have the same color:
   - STOP! Trace the dots that caused the conflict.
   - Write: *"The graph contains an odd-length cycle [list vertices, e.g., $v_1-v_2-v_3-v_1$]. By Konig's Theorem, a graph is bipartite $\iff$ it has no odd cycles. Therefore, NOT bipartite ❌."*
5. If you finish coloring all dots with no conflicts:
   - Write: *"Graph is bipartite with partitions $V_1 = \{\text{Red dots}\}$ and $V_2 = \{\text{Blue dots}\}$ ✅."*

---

### Recipe 3: Calculating Walks of Length 2 Without Doing Big Matrix Multiplication
If an exam asks for walks of length 2 between vertex $v_i$ and vertex $v_j$:
* **Do NOT multiply the entire $n \times n$ matrix!** That takes 15 minutes.
* Instead, simply calculate the **dot product of Row $i$ and Row $j$** of $A$:
  $$(A^2)_{ij} = \sum_{k=1}^n A_{ik} \times A_{jk}$$
* *Plain English Meaning*: Just count how many vertices are connected to **BOTH $v_i$ AND $v_j$**! Each common friend gives exactly one 2-step walk ($v_i \to \text{friend} \to v_j$).

---

## 🚨 TIER 3: Faculty Trap Radar

1. **"Does degree sequence check prove isomorphism?"**: NO! Two graphs can have the exact same degree sequence (e.g. two separate triangles vs one 6-cycle $C_6$; both have degrees $2, 2, 2, 2, 2, 2$) but are **NOT isomorphic** (one has triangles, the other doesn't!).
2. **"Does an Euler path start anywhere?"**: NO! If a graph has two odd-degree vertices, the Euler path **MUST start at one odd vertex and end at the OTHER odd vertex**. Starting at an even vertex will get you stuck!
3. **"Dirac's Theorem Failure"**: If a vertex has degree $< n/2$, it does **NOT** mean the graph is not Hamiltonian. Dirac's theorem is a *one-way guarantee*, not a disqualifier.

---

## 📝 TIER 4: Master Solved HOTS Archetypes

### Archetype 1: Havel-Hakimi Test on $(5, 3, 3, 3, 2, 2)$
**Question**: Can a simple graph exist with degree sequence $S = (5, 3, 3, 3, 2, 2)$?

**Step-by-Step Solution**:
1. **Sum Check**: $5 + 3 + 3 + 3 + 2 + 2 = 18$ (Even $\implies$ pass).
2. **Iteration 1**:
   * Sequence: $(5, 3, 3, 3, 2, 2)$.
   * Drop $5$. Subtract 1 from the next 5 numbers:
     $$(3-1, 3-1, 3-1, 2-1, 2-1) = (2, 2, 2, 1, 1)$$
3. **Iteration 2**:
   * Sequence is already sorted: $(2, 2, 2, 1, 1)$.
   * Drop $2$. Subtract 1 from next 2 numbers:
     $$(2-1, 2-1, 1, 1) = (1, 1, 1, 1)$$
4. **Iteration 3**:
   * Sequence: $(1, 1, 1, 1)$.
   * Drop $1$. Subtract 1 from next 1 number:
     $$(1-1, 1, 1) = (0, 1, 1)$$
   * Re-sort: $(1, 1, 0)$.
5. **Iteration 4**:
   * Drop $1$. Subtract 1 from next 1 number:
     $$(1-1, 0) = (0, 0)$$
6. **Conclusion**: All remaining elements are $0$. By the Havel-Hakimi Theorem, the degree sequence is **GRAPHIC ✅**. A simple graph with these degrees exists!

---

### Archetype 2: 2-Coloring Bipartite Proof with Odd-Cycle Trap
**Question**: Determine whether the graph $G$ with vertices $\{1, 2, 3, 4, 5, 6\}$ and edges $(1,2), (2,3), (3,4), (4,5), (5,6), (6,1)$ and additional edge $(2,5)$ is bipartite.

**Step-by-Step Solution**:
1. **Attempt 2-Coloring**:
   * Color vertex $1$: **RED**.
   * Neighbors of $1$ are $2$ and $6 \implies$ Color $2$: **BLUE**, Color $6$: **BLUE**.
   * Look at neighbor of $2$: vertex $3 \implies$ Color $3$: **RED**.
   * Look at neighbor of $3$: vertex $4 \implies$ Color $4$: **BLUE**.
   * Look at neighbor of $4$: vertex $5 \implies$ Color $5$: **RED**.
2. **Conflict Check on Cross-Edge $(2, 5)$**:
   * Look at the edge $(2, 5)$:
     * Vertex $2$ is **BLUE**.
     * Vertex $5$ is **RED**. (Different colors $\implies$ edge $(2, 5)$ is valid).
   * Now look at neighbor of $5$: vertex $6$:
     * Vertex $5$ is **RED**.
     * Vertex $6$ was already colored **BLUE**. (Different colors $\implies$ edge $(5, 6)$ is valid).
3. **Partitions**:
   * Partition $V_1 = \{1, 3, 5\}$ (All RED).
   * Partition $V_2 = \{2, 4, 6\}$ (All BLUE).
   * Every edge connects a vertex in $V_1$ to a vertex in $V_2$.
4. **Conclusion**: The graph is **BIPARTITE ✅** with partitions $\{1, 3, 5\}$ and $\{2, 4, 6\}$.
