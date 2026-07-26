# 🕸️ Lesson 5 — Graphs & Matrix Representations

> **TL;DR**: A graph = dots (vertices) connected by lines (edges). Learn degree sequences, Euler/Hamilton paths, isomorphism checks, and how to represent graphs as matrices. Most questions are "draw it and count things."

---

## 1️⃣ What is a Graph?

A graph G = (V, E) where:
- **V** = set of vertices (nodes/dots)
- **E** = set of edges (connections/lines)

```
Types:
  Undirected graph: edges have no direction (a—b)
  Directed graph (digraph): edges have arrows (a→b)
  Multigraph: allows multiple edges between same vertices
  Pseudograph: allows loops (edge from vertex to itself)
```

---

## 2️⃣ Degree of a Vertex

**Degree** of vertex v = number of edges touching v. Written deg(v).

```
     b---c
    / \ /
   a   d

deg(a) = 1, deg(b) = 3, deg(c) = 2, deg(d) = 2
```

### The Handshaking Theorem

> **Σ deg(v) = 2|E|** (sum of all degrees = twice the number of edges)

This means: the sum of degrees is ALWAYS even.

**Corollary**: The number of vertices with **odd degree** is always **even**.

### For Directed Graphs
- **in-degree** deg⁻(v) = number of edges coming IN
- **out-degree** deg⁺(v) = number of edges going OUT
- Σ deg⁻ = Σ deg⁺ = |E|

---

## 3️⃣ Special Graphs

| Graph Type | Definition |
|-----------|-----------|
| **Complete (Kₙ)** | Every vertex connected to every other. Edges = n(n-1)/2 |
| **Bipartite** | Vertices split into 2 groups, edges only BETWEEN groups |
| **Complete Bipartite (Kₘ,ₙ)** | Every vertex in group 1 connects to every vertex in group 2 |
| **Cycle (Cₙ)** | Single loop through n vertices |
| **Path (Pₙ)** | Straight line through n vertices |
| **Subgraph** | A graph made from a subset of vertices and edges of G |

---

## 4️⃣ Walks, Paths, Circuits

| Term | What it is | Can repeat vertices? | Can repeat edges? |
|------|-----------|:---:|:---:|
| **Walk** | Any sequence of edges | ✅ | ✅ |
| **Trail** | Walk with no repeated edges | ✅ | ❌ |
| **Path** | Walk with no repeated vertices | ❌ | ❌ |
| **Circuit** | Walk that starts and ends at same vertex | ✅ | ❌ |
| **Cycle** | Circuit with no repeated vertices (except start=end) | ❌ | ❌ |

---

## 5️⃣ Euler Paths & Circuits

An **Euler path** visits every **edge** exactly once.
An **Euler circuit** = Euler path that starts and ends at the same vertex.

### The Rules (MEMORIZE)

| | Condition |
|---|---|
| **Euler CIRCUIT exists** | Every vertex has **even** degree |
| **Euler PATH exists** | Exactly **2** vertices have odd degree (start & end there) |
| **Neither exists** | More than 2 vertices have odd degree |

> 🧠 **Memory trick**: **C**ircuit = **C**ompletely even degrees. **P**ath = **P**air of odd degree vertices.

---

## 6️⃣ Hamilton Paths & Circuits

A **Hamilton path** visits every **vertex** exactly once.
A **Hamilton circuit** = Hamilton path that returns to start.

> ⚠️ There's no simple "check" like Euler. But some tricks help:

### Useful Conditions
- **Dirac's Theorem**: If deg(v) ≥ n/2 for all vertices → Hamilton circuit exists
- **Ore's Theorem**: If deg(u) + deg(v) ≥ n for every non-adjacent pair → Hamilton circuit exists
- If a vertex has degree 2, BOTH its edges must be in any Hamilton circuit

---

## 7️⃣ Graph Isomorphism

Two graphs are **isomorphic** if they have the same structure (just drawn differently).

### How to Check

**Must match (necessary conditions)**:
1. Same number of vertices
2. Same number of edges
3. Same **degree sequence** (sorted list of all degrees)

**If all match, try to find a mapping** f: V₁ → V₂ that preserves all edges.

**If any DON'T match** → NOT isomorphic ❌ (done!)

---

## 8️⃣ Matrix Representations

### Adjacency Matrix

For a graph with n vertices: an **n × n** matrix where:
- A[i][j] = 1 if there's an edge from vertex i to vertex j
- A[i][j] = 0 otherwise

```
Example:  a—b—c

     a  b  c
a  [ 0  1  0 ]
b  [ 1  0  1 ]
c  [ 0  1  0 ]
```

**Properties**:
- Undirected → symmetric matrix (A = Aᵀ)
- Diagonal = loops (self-edges)
- Sum of row i = deg(vertex i)

### Incidence Matrix

For a graph with n vertices and m edges: an **n × m** matrix where:
- M[i][j] = 1 if vertex i is incident to edge j
- M[i][j] = 0 otherwise

```
Example:  a—e₁—b—e₂—c

     e₁  e₂
a  [  1   0 ]
b  [  1   1 ]
c  [  0   1 ]
```

---

## 🏋️ Solved Exam Practice Questions

### Question 1 (Handshaking Theorem Numerical)
**A simple graph $G$ has 12 edges and 6 vertices. If 3 vertices have a degree of 4 each, and all other vertices have the same degree $k$, find the value of $k$.**

<details>
<summary>💡 Step-by-Step Solution</summary>

**Step 1:** Apply Handshaking Theorem: $\sum_{v \in V} \text{deg}(v) = 2 \cdot |E|$.  
**Step 2:** Substitute $|E| = 12$, so total sum of degrees $= 2 \times 12 = 24$.  
**Step 3:** The graph has 6 vertices total:
- 3 vertices have degree 4 $\implies$ Sum $= 3 \times 4 = 12$.
- Remaining 3 vertices have degree $k \implies$ Sum $= 3k$.  
**Step 4:** Set up equation:
$$12 + 3k = 24 \implies 3k = 12 \implies k = 4$$
**Answer:** $k = 4$. ✅
</details>

---

### Question 2 (Isomorphism Verification)
**Are two graphs with degree sequences $(3, 3, 2, 2)$ and $(3, 2, 2, 1)$ isomorphic?**

<details>
<summary>💡 Step-by-Step Solution</summary>

**Check Invariants:**
1. Number of vertices: Both have 4 vertices.
2. Degree sequences: Graph 1 has $(3, 3, 2, 2)$, Graph 2 has $(3, 2, 2, 1)$.
3. Sum of degrees: Graph 1 $= 10$, Graph 2 $= 8$.

**Conclusion:** Since the degree sequences and edge counts are not equal, the two graphs are **NOT isomorphic**. ✅
</details>

---

## ✅ Quick Self-Check

1. If a graph has 5 vertices with degrees 2,3,3,4,2 — how many edges?
2. Can a graph have an Euler circuit if one vertex has degree 3?
3. What's the adjacency matrix of K₃ (complete graph on 3 vertices)?
4. How do you quickly disprove isomorphism?
5. State Dirac's theorem in one sentence.

<details>
<summary>🔑 Answers</summary>

1. Σdeg = 2+3+3+4+2 = 14. Edges = 14/2 = **7**
2. **No** — Euler circuit requires ALL vertices to have even degree
3. All 1s except diagonal: `[[0,1,1],[1,0,1],[1,1,0]]`
4. Compare degree sequences — if different, they're NOT isomorphic
5. If every vertex has degree ≥ n/2, then a Hamilton circuit exists

</details>

---

**⏱️ Time spent: ~20 min. Module covered! 🎉**
