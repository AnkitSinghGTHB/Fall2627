# 🚨 7-Day Emergency FAT Crash Course: From 17/50 to 85+/100

> **Time Remaining**: 7 Days (Oct 6 to Oct 12 | Exams start Oct 13)  
> **Target**: Minimum 85/100 in Term End (FAT) to rescue your grade  
> **Student Mindset**: You don't like studying, you don't have time for theory fluff, and you need maximum marks per minute of effort.

---

## 🎯 The "Guaranteed 60 Marks" Safety Net

Before studying anything else, realize that **60 out of 100 marks in the FAT paper come from 6 completely predictable, mechanical question templates**. If you only learn these 6 templates, you already pass with flying colors:

```text
┌───┬──────────────────────────────────────────┬──────────┬─────────────────────────────┐
│ # │ The 6 Guaranteed Exam Question Templates │ Marks    │ Exact Time to Master        │
├───┼──────────────────────────────────────────┼──────────┼─────────────────────────────┤
│ 1 │ Equivalence without truth tables         │ 5 Marks  │ 45 mins (Learn 5 laws)      │
│ 2 │ Congruence modulo m Equivalence proof    │ 5–10 M   │ 30 mins (Memorize 3 steps)  │
│ 3 │ Hasse Diagram of Dₙ + GLB (gcd)/LUB (lcm)│ 5–10 M   │ 30 mins (Pure arithmetic)   │
│ 4 │ Kruskal's / Prim's MST Table             │ 10 Marks │ 45 mins (Sorting edges)     │
│ 5 │ Dijkstra's Shortest Path Table           │ 10 Marks │ 45 mins (Table filling)     │
│ 6 │ Havel-Hakimi Graphic Sequence Test       │ 5 Marks  │ 20 mins (Simple subtraction)│
├───┴──────────────────────────────────────────┴──────────┴─────────────────────────────┤
│ TOTAL "FREE" REPEATABLE MARKS                │ 40–45 M  │ Less than 4 hours total!    │
└─────────────────────────────────────────────────────────┴─────────────────────────────┘
```

The remaining 40–45 marks come from:
* PDNF/PCNF minterm expansion (10M)
* Graph Isomorphism with bijection table (10M)
* Chromatic number & Welsh-Powell / Polynomials (10M)
* Rules of Inference / Quantifier proof (10M)

---

## 📅 The 7-Day Day-by-Day Battle Plan (2 to 2.5 Hours / Day)

### 🗓️ DAY 1 (Tuesday, Oct 6): Module 1 — Logic & Inference (Target: 20 Marks)
* **What to Read**: [`01-module1-predicate-calculus.md`](./01-module1-predicate-calculus.md)
* **Key Tasks**:
  1. Memorize the 5 core laws: Conditional law ($p \to q \equiv \neg p \vee q$), De Morgan's, Distributive, Absorption.
  2. Write out by hand: Proof of $(p \to r) \vee (q \to r) \equiv (p \wedge q) \to r$ without truth table.
  3. Master the 4 Rules of Inference: Modus Ponens (MP), Modus Tollens (MT), Hypothetical Syllogism (HS), Disjunctive Syllogism (DS).
  4. Learn the **EI-before-UI rule** for Socrates-style quantifier proofs.
* **Done Benchmark**: You can solve Question 1.1 and Question 1.2 from the [Question Bank](./07-fat-high-frequency-exam-question-bank.md) in under 15 minutes.

---

### 🗓️ DAY 2 (Wednesday, Oct 7): Module 2 — Relations, Posets & Hasse (Target: 20 Marks)
* **What to Read**: [`02-module2-sets-relations-hasse.md`](./02-module2-sets-relations-hasse.md)
* **Key Tasks**:
  1. Write out the 3-step proof for $a \equiv b \pmod m$ (Reflexive, Symmetric, Transitive). This is repeated in almost every FAT!
  2. Draw Hasse diagrams for $D_{12}$, $D_{24}$, and $D_{30}$.
  3. Remember the golden rule for $D_n$: **$\text{GLB}(a, b) = \gcd(a, b)$**, **$\text{LUB}(a, b) = \operatorname{lcm}(a, b)$**.
  4. Write down the difference between Maximal (multiple allowed) vs Greatest (at most one).
* **Done Benchmark**: You can draw $D_{24}$, label its maximal/minimal elements, and find $\text{GLB}(6, 8)$ and $\text{LUB}(6, 8)$ without looking.

---

### 🗓️ DAY 3 (Thursday, Oct 8): Module 5 — Trees & Graph Coloring (Target: 25 Marks)
> *Why study Module 5 before 3 & 4? Because it is fresh, easy, and has ZERO tricky algebra!*
* **What to Read**: [`05-module5-trees-and-graph-coloring.md`](./05-module5-trees-and-graph-coloring.md)
* **Key Tasks**:
  1. Learn **Kruskal's Algorithm** (sort all edges, pick smallest avoiding cycles) and **Prim's Algorithm** (grow from vertex). Practice Question 5.1 from the Question Bank.
  2. Learn the **Leaf-Pruning rule** to find the center of a tree (delete leaves until 1 or 2 nodes remain).
  3. Memorize the Chromatic Number table: Complete $K_n = n$, Bipartite $= 2$, Trees $= 2$, Even Cycles $= 2$, Odd Cycles $= 3$.
  4. Learn Chromatic Polynomial for a tree: $P(T_n, \lambda) = \lambda(\lambda - 1)^{n-1}$.
* **Done Benchmark**: You can trace Kruskal's on a 6-vertex graph and calculate chromatic numbers of standard graphs in 30 seconds.

---

### 🗓️ DAY 4 (Friday, Oct 9): Module 3 — Lattices & Boolean Algebra (CAT-2 Redemption Part 1)
* **What to Read**: [`03-module3-lattices-boolean-algebra.md`](./03-module3-lattices-boolean-algebra.md)
* **Key Tasks**:
  1. Learn how to verify if a poset is a lattice (unique top 1 and unique bottom 0, no double roofs).
  2. Learn the **Sub-lattice Trap**: Show why $\{1, 2, 3, 30\}$ in $D_{30}$ fails because $2 \vee 3 = 6 \notin S$.
  3. Learn **Birkhoff's $M_5/N_5$ rule**: If a lattice contains a Diamond ($M_5$) or Pentagon ($N_5$), it is NOT distributive!
  4. Learn the **Square-Free Rule**: $D_n$ is a Boolean algebra $\iff n$ is square-free ($D_{30}$ is; $D_{12}$ is not).
  5. Practice converting a 3-variable expression to **PDNF ($\sum m$)** and **PCNF ($\prod M$)**.
* **Done Benchmark**: You can solve Question 3.1 and Question 3.3 from the Question Bank with full confidence.

---

### 🗓️ DAY 5 (Saturday, Oct 10): Module 4 — Graphs & Matrix Algorithms (CAT-2 Redemption Part 2)
* **What to Read**: [`04-module4-graphs-and-matrices.md`](./04-module4-graphs-and-matrices.md)
* **Key Tasks**:
  1. Handshaking Lemma: $\sum \deg(v) = 2|E|$ (Odd degree vertices count is ALWAYS even).
  2. Master **Havel-Hakimi algorithm**: Sort descending, peel off first element $d_1$, subtract 1 from next $d_1$ elements, re-sort.
  3. Master **Graph Isomorphism 5-Point Radar**: Check $|V|$, $|E|$, degree sequence, cycle lengths, and **write the explicit mapping table $f(u_i) = v_j$**.
  4. Euler vs Hamiltonian: Euler circuit = all even degrees; Euler trail = exactly 2 odd degrees.
  5. Fill a 5-step **Dijkstra shortest path table**.
* **Done Benchmark**: You can run Havel-Hakimi on $(5, 4, 3, 3, 2, 2, 1)$ and fill a Dijkstra table without arithmetic slips.

---

### 🗓️ DAY 6 (Sunday, Oct 11): Full Mock Exam Simulation (100-Mark Speedrun)
* **What to Read**: [`07-fat-high-frequency-exam-question-bank.md`](./07-fat-high-frequency-exam-question-bank.md)
* **Key Tasks**:
  1. Pick 10 questions from the Question Bank across all 5 modules.
  2. Set a timer for 2.5 hours. Write out the answers by hand on blank ruled paper.
  3. Grade yourself strictly using the marking scheme breakdown in the Question Bank.
  4. Note down the 2 or 3 specific formulas or steps you stumbled on.

---

### 🗓️ DAY 7 (Monday, Oct 12): Exam Eve Final Polish & Cheat Sheet Drill
* **What to Read**: [`06-term-end-master-formula-cheat-sheet.md`](./06-term-end-master-formula-cheat-sheet.md)
* **Key Tasks**:
  1. Read the 1-page formula sheet 3 times: morning, afternoon, night.
  2. Review the 4 high-frequency proofs:
     * Handshaking Lemma proof.
     * Congruence modulo $m$ equivalence proof.
     * Deletion-Contraction formula for chromatic polynomials.
     * Tree has at least 2 leaves proof.
  3. Pack your calculator, pens, scale, and admit card. Sleep at least 7 hours!

---

## ⚡ The Exam Hall Execution Rules (How to Pick Up 10 Extra Marks)

1. **Start with your strongest module first**: If you love Kruskal/Prim or Dijkstra, solve those first to build momentum and lock in 20 marks in the first 30 minutes.
2. **Never leave any question blank**:
   * For Graph Isomorphism: Write vertex count, edge count, and degree sequence (guarantees 4/10 marks even if you can't find the bijection).
   * For Inference proofs: Write out premises and identify which rule to apply (guarantees 2-3 marks).
   * For Lattices: Write the definitions of GLB and LUB.
3. **Always box your final answers**: Evaluators grade 50+ papers a day; make it effortless for them to spot your correct final result.
