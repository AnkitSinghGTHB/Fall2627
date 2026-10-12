# 🚨 7-Day TOC & Compiler Design FAT Battle Plan: From 28/50 to 80+/100

> **Time Budget**: 1.5 to 2 hours per day (Oct 6 to Oct 12 | FAT starts Oct 13)  
> **Faculty Target**: Satisfying Dr. Gaurav Soni's exact syntactic rubric  
> **Golden Principle**: Dr. Soni never grades on intuition; he grades on **tables, tuples, and derivation steps**. If you give him the exact headings he looks for, he is forced to give full marks.

---

## 🎯 Official TEE Paper Pattern & Guaranteed Questions (100 Marks Total)

Per `TEE.txt`, the official Term End Exam structure is:
* **Section A (60 Marks)**: 5 Questions (1 from each module), **12 Marks each** in `OR` format (either 12M full or 6M + 6M subparts).
* **Section B (40 Marks)**: 5 Questions (1 from each module), **8 Marks each**, strictly **WITHOUT SUBPARTS**.

```text
┌───┬──────────────────────────────────────────┬──────────┬─────────────────────────────┐
│ # │ High-Frequency Exam Question             │ Section  │ TEE Weightage               │
├───┼──────────────────────────────────────────┼──────────┼─────────────────────────────┤
│ 1 │ Arden's Theorem / DFA Minimization       │ Sec A/B  │ 12M (Sec A) / 8M (Sec B)    │
│ 2 │ PDA Design / PDA to CFG Conversion       │ Sec A/B  │ 12M (Sec A) / 8M (Sec B)    │
│ 3 │ Turing Machine in 6-Part Mandatory Format│ Sec A/B  │ 12M (Sec A) / 8M (Sec B)    │
│ 4 │ LL(1) Table + Trace / SLR(1) Conflict    │ Sec A/B  │ 12M (Sec A) / 8M (Sec B)    │
│ 5 │ TAC Quad/Triple/Indirect / DAG & Opt.    │ Sec A/B  │ 12M (Sec A) / 8M (Sec B)    │
└───┴──────────────────────────────────────────┴──────────┴─────────────────────────────┘
```

---

## 📅 The Day-by-Day Daily Checklist (1.5 to 2 Hours / Day)

### 🗓️ DAY 1 (Tuesday, Oct 6): Module 1 — Finite Automata & Minimization
* **File to Read**: [`01-module1-finite-automata-and-minimization.md`](./01-module1-finite-automata-and-minimization.md)
* **Tasks**:
  1. Learn how to write the **5-Tuple $M = (Q, \Sigma, \delta, q_0, F)$** with sets explicitly listed.
  2. Master the **Myhill-Nerode Table-Filling Method** for DFA Minimization (Step 1: Unreachable removal $\to$ Step 2: Final vs Non-final partition $\to$ Step 3: Triangular check table $\to$ Step 4: Minimized diagram).
  3. Memorize the **4-step template for Pumping Lemma for Regular Languages** (Contradiction $\to p \to s = 0^p 1^p \to y = 0^k \to s' = x y^2 z \notin L$).
* **Target Check**: Solve Question 1.1 from the [Question Bank](./07-toc-fat-high-frequency-exam-question-bank.md) in 15 minutes.

---

### 🗓️ DAY 2 (Wednesday, Oct 7): Module 2 — CFG, CNF & Pushdown Automata
* **File to Read**: [`02-module2-cfg-cnf-and-pda.md`](./02-module2-cfg-cnf-and-pda.md)
* **Tasks**:
  1. **Ambiguity Proof**: Draw **2 different Parse Trees** AND write **2 different Leftmost Derivations (LMD)** for the string `id + id * id`.
  2. Master the **4-Step CNF Recipe**:
     * Step 1: Eliminate $\epsilon$-productions ($A \to \epsilon$).
     * Step 2: Eliminate Unit productions ($A \to B$).
     * Step 3: Eliminate Useless symbols (non-generating & non-reachable).
     * Step 4: Enforce binary form $A \to BC$ and $A \to a$.
  3. Design PDA for $L = \{w c w^R \mid w \in \{a,b\}^*\}$ or $\{a^n b^n\}$ using the **7-Tuple and Instantaneous Description ($\vdash$) trace**.
* **Target Check**: Convert an expression grammar to CNF without missing intermediate steps.

---

### 🗓️ DAY 3 (Thursday, Oct 8): Module 3 — Top-Down LL(1) Parsing
* **File to Read**: [`03-module3-parsing-ll1-slr-clr-lalr.md`](./03-module3-parsing-ll1-slr-clr-lalr.md)
* **Tasks**:
  1. Learn the formula to eliminate **Left Recursion** ($A \to A\alpha \mid \beta \implies A \to \beta A', A' \to \alpha A' \mid \epsilon$).
  2. Master the **3 Golden Rules of FIRST** and **3 Golden Rules of FOLLOW** (Always put `$` in $\text{FOLLOW}(S)$!).
  3. Build an **LL(1) Parsing Table** and trace string validation using the `[Stack | Input | Action]` table.
* **Target Check**: Compute FIRST and FOLLOW for the classic grammar $E \to TE', E' \to +TE' \mid \epsilon \dots$ with 100% accuracy.

---

### 🗓️ DAY 4 (Friday, Oct 9): Module 3 (Part 2) — Bottom-Up SLR(1) & Conflicts
* **File to Read**: [`03-module3-parsing-ll1-slr-clr-lalr.md`](./03-module3-parsing-ll1-slr-clr-lalr.md)
* **Tasks**:
  1. Write the **Augmented Grammar** ($S' \to \cdot S$).
  2. Construct the **Canonical Collection of $LR(0)$ Items** using $\text{CLOSURE}$ and $\text{GOTO}$.
  3. Fill the **SLR(1) Parsing Table**:
     * Shift entries: on terminals $\to s_j$.
     * Reduce entries: on $\text{FOLLOW}(A) \to r_k$.
  4. Write the **mathematical proof for Shift-Reduce (S/R) conflict** (two entries in the same cell $[I_i, a]$).
* **Target Check**: Construct LR(0) items for the grammar $E \to E + T \mid T$ and show why ambiguous grammars have S/R conflicts.

---

### 🗓️ DAY 5 (Saturday, Oct 10): Module 4 — Turing Machines (Dr. Soni's Style)
* **File to Read**: [`04-module4-turing-machines-and-undecidability.md`](./04-module4-turing-machines-and-undecidability.md)
* **Tasks**:
  1. Write out the **6-Part Mandatory TM Template** for $L = \{a^n b^n c^n \mid n \ge 1\}$.
  2. Write the 6-Part TM for **Even number of 0s and Odd number of 1s** (a favorite in Dr. Soni's tests!).
  3. Memorize the **Chomsky Hierarchy Table** (Type 0, Type 1, Type 2, Type 3: Grammar, Automaton, Language).
  4. Write the 1-page standard answer for **Halting Problem of Turing Machine** (Proof by Contradiction using diagonal machine $D$).
* **Target Check**: Write a complete TM solution including the delta table and $\vdash$ string trace in 25 minutes.

---

### 🗓️ DAY 6 (Sunday, Oct 11): Module 5 — Intermediate Code & Optimization
* **File to Read**: [`05-module5-intermediate-code-and-optimization.md`](./05-module5-intermediate-code-and-optimization.md)
* **Tasks**:
  1. Given an arithmetic statement, write:
     * Three Address Code (TAC).
     * **Quadruples Table** `[Op, Arg1, Arg2, Result]`.
     * **Triples Table** `[(i), Op, Arg1, Arg2]`.
     * **Indirect Triples** (pointers array).
  2. Partition TAC into **Basic Blocks using the 3 Leader Rules**.
  3. Draw the **Control Flow Graph (CFG)**.
  4. Explain and give examples of: Common Subexpression Elimination, Dead Code Elimination, Loop Invariant Code Motion, and Strength Reduction.
* **Target Check**: Convert an expression into Quadruples and Triples without making index errors.

---

### 🗓️ DAY 7 (Monday, Oct 12): Full Exam Simulation & Formula Polish
* **Files to Review**: 
  * [`06-toc-master-formula-sheet.md`](./06-toc-master-formula-sheet.md)
  * [`07-toc-fat-high-frequency-exam-question-bank.md`](./07-toc-fat-high-frequency-exam-question-bank.md)
* **Tasks**:
  1. Review the 1-page formula sheet.
  2. Speed-write 3 question templates: (1) DFA Minimization, (2) SLR(1) Table, (3) Turing Machine 6-part format.
