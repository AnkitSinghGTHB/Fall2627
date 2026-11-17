# 🎯 TEE Examination Master Strategy & Preparation Guide

> **Semester**: Fall Semester 2026–27  
> **Course Architecture**: 7 Registered Core / Elective Courses  
> **Focus**: Relative grading mechanics, subject-wise exam blueprints, and high-yield scoring templates.

---

## 1. How VIT Bhopal Relative Grading Works

**Grade Cutoffs based on Class Mean ($\mu$) and Standard Deviation ($\sigma$):**
- **S Grade** : $\text{Total} \ge \mu + 1.5\sigma$ **with a minimum of 90% total**
- **A Grade** : $\text{Total} \ge \mu + 0.5\sigma$ and $< \mu + 1.5\sigma$ (Top ~30% of the class)
- **B Grade** : $\text{Total} \ge \mu - 0.5\sigma$ and $< \mu + 0.5\sigma$ (Middle ~38% of the class)
- **C Grade** : $\text{Total} \ge \mu - 1.0\sigma$ and $< \mu - 0.5\sigma$
- **D Grade** : $\text{Total} \ge \mu - 1.5\sigma$ and $< \mu - 1.0\sigma$
- **E Grade** : $\text{Total} \ge \mu - 2.0\sigma$ and $< \mu - 1.5\sigma$
- **F Grade** : $\text{Total} < \mu - 2.0\sigma$ OR $\text{Total} < 50$ OR $\text{TEE} < 40/100$

> [!IMPORTANT]
> TEE carries **30% of your total grade** (scored out of 100, scaled by $\times 0.30$).
> Every 10 raw marks scored in TEE shifts your final course total by **3.0 marks**, which can shift an entire letter grade on a tight curve.

---

## 2. Subject-by-Subject Examination Blueprints

| # | Subject Code & Title | Credits | Assessment Mode | Key High-Yield Focus Areas |
|:---:|:---|:---:|:---:|:---|
| 1 | **MGT2003**: Tech Entrepreneurship | 3 | LTM | Business model canvas, startup finance, valuation, IPR & patenting, marketing strategies. |
| 2 | **CSE2004**: TOC & Compiler Design | 4 | LTM | Pumping lemma, CFG/PDA, LL(1) and SLR(1) parse tables, 6-part formal Turing Machine rubric. |
| 3 | **ECE2002**: Digital Logic Design | 4 | LTPM | K-Maps, combinational logic (Adders, MUX, Decoders), sequential design (Flip-Flops, Counters, FSM state reduction). |
| 4 | **CSE4005**: Machine Learning | 3 | LPM | Decision trees (Entropy & Gain), Naive Bayes, PCA Lagrange derivation, SVM dual, AdaBoost updates, SMOTE. |
| 5 | **CSE3011**: Python Programming | 3 | LPM | OOP polymorphism/dunder methods, exceptions, regex search/match, SQLite operations, file handling. |
| 6 | **MAT2002**: Discrete Mathematics | 4 | LTM | Posets & Hasse diagrams ($D_n$), PDNF/PCNF, graph isomorphism, Eulerian/Hamiltonian circuits, MST, graph coloring. |
| 7 | **PLA1004**: Competitive Coding | 3 | LPM | Bit manipulation, arrays, sliding window, linked list cycle removal, monotonic stack, binary trees, graph BFS/DFS. |

---

## 3. Discrete Mathematics: 6 Core Mechanical Question Templates

60+ marks come from repeatable algorithmic procedures that do not rely on memorizing theory:
1. **Hasse Diagram of $D_n$ / Posets**: Finding divisors, drawing poset levels, calculating GLB (gcd) and LUB (lcm), checking bounded/complemented/distributive lattices.
2. **PDNF / PCNF Normal Forms**: Truth table minterms/maxterms expansion and algebraic Boolean reduction.
3. **Graph Isomorphism & Complements**: Degree sequence matching, adjacency bijections, and complement graphs $\overline{G}$.
4. **Eulerian & Hamiltonian Circuits**: Checking even-degree vertex conditions (Euler) and Dirac/Ore sufficiency theorems (Hamiltonian).
5. **Chromatic Number & Graph Coloring**: Welsh-Powell algorithm, chromatic polynomials $P(G, \lambda)$, and 4-color theorem for planar graphs.
6. **Dijkstra Shortest Path & MST**: Table-based shortest path trace and Prim/Kruskal edge selection table with cycle verification.

---

## 4. Theory of Computation: Mandatory 6-Part Syntactic Rubric

To maximize marks on Turing Machine and Automata design questions:
- **Part 1**: Language Description (Formal set builder notation $L = \{w \dots\}$)
- **Part 2**: Design Logic (Algorithm in plain English steps)
- **Part 3**: Formal 7-Tuples (Explicit enumeration of $Q, \Sigma, \Gamma, \delta, q_0, B, F$)
- **Part 4**: State Transition Table ($\delta$ matrix)
- **Part 5**: State Transition Diagram (Clean graph with start and double-circle final states)
- **Part 6**: Validation (Step-by-step Instantaneous Description $\vdash$ trace on acceptance & rejection strings)

---

## 5. TEE 3-Hour Time Allocation Strategy

* **First 10 Minutes**: Rapid scan of Section A and Section B. Mark direct matches.
* **Section A (100 Minutes)**: 5 Questions $\times$ 20 minutes each (12 Marks each = 60M). Write: Approach $\to$ Derivation/Code $\to$ Dry Run Trace $\to$ Complexity.
* **Section B (60 Minutes)**: 5 Questions $\times$ 12 minutes each (8 Marks each = 40M). Concise, direct solutions.
* **Final 10 Minutes**: Review, check edge cases, and verify all questions are attempted.
