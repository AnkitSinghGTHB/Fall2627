# ⚡ TOC & Compiler Design: 1-Page Master Formula & Rubric Cheat Sheet

> **Print or copy this 1-page cheat sheet before the FAT exam.**  
> Contains every formal tuple, parsing rule, conflict formula, and Dr. Soni's evaluation rubric.

---

## 1. Formal Automata Tuples Summary

| Model | Tuples Specification | Transition Function ($\delta$) Mapping |
| :--- | :--- | :--- |
| **DFA** | $M = (Q, \Sigma, \delta, q_0, F)$ | $\delta: Q \times \Sigma \to Q$ |
| **NFA** | $M = (Q, \Sigma, \delta, q_0, F)$ | $\delta: Q \times \Sigma \to 2^Q$ |
| **$\epsilon$-NFA** | $M = (Q, \Sigma, \delta, q_0, F)$ | $\delta: Q \times (\Sigma \cup \{\epsilon\}) \to 2^Q$ |
| **PDA** | $M = (Q, \Sigma, \Gamma, \delta, q_0, Z_0, F)$ | $\delta: Q \times (\Sigma \cup \{\epsilon\}) \times \Gamma \to 2^{Q \times \Gamma^*}$ |
| **Turing Machine** | $M = (Q, \Sigma, \Gamma, \delta, q_0, B, F)$ | $\delta: Q \times \Gamma \to Q \times \Gamma \times \{L, R\}$ |

---

## 2. Chomsky Hierarchy of Languages

| Type | Language | Automaton Model | Production Form |
| :---: | :--- | :--- | :--- |
| **Type 3** | Regular Language | Deterministic Finite Automaton (DFA) | $A \to aB$ or $A \to a$ |
| **Type 2** | Context-Free Language (CFL) | Pushdown Automaton (PDA) | $A \to \alpha$ ($A \in V$) |
| **Type 1** | Context-Sensitive Language (CSL) | Linear Bounded Automaton (LBA) | $\alpha \to \beta$ with $|\alpha| \le |\beta|$ |
| **Type 0** | Recursively Enumerable (RE) | Turing Machine (TM) | $\alpha \to \beta$ (Arbitrary) |

* **Chomsky Normal Form (CNF)**: Every rule is strictly $A \to BC$ or $A \to a$.
* **Greibach Normal Form (GNF)**: Every rule is strictly $A \to a\alpha$ (terminal followed by non-terminals).

---

## 3. Parsing Rules & Conflict Formulas

### 3.1 FIRST & FOLLOW Rules
* **$\text{FIRST}(X)$**: If terminal $\to \{X\}$. If $X \to Y_1 Y_2$, include $\text{FIRST}(Y_1) \setminus \{\epsilon\}$. If $\epsilon \in \text{FIRST}(Y_1)$, include $\text{FIRST}(Y_2)$.
* **$\text{FOLLOW}(A)$**:
  - Always add `$` to $\text{FOLLOW}(S)$.
  - If $A \to \alpha B \beta \implies \text{FIRST}(\beta) \setminus \{\epsilon\} \subseteq \text{FOLLOW}(B)$.
  - If $A \to \alpha B$ or $\epsilon \in \text{FIRST}(\beta) \implies \text{FOLLOW}(A) \subseteq \text{FOLLOW}(B)$.
  - ⚠️ *$\epsilon$ is NEVER in any FOLLOW set!*

---

### 3.2 Parser Conflict Formulas
* **LL(1) Conflict**: Occurs if cell $M[A, a]$ contains $\ge 2$ production rules.
* **SLR(1) Shift-Reduce (S/R) Conflict**: Occurs if in state $I_i$:
  $$[A \to \alpha \cdot a \beta] \in I_i \quad \text{AND} \quad [B \to \gamma \cdot] \in I_i \quad \text{where } a \in \text{FOLLOW}(B)$$
  Cell $\text{ACTION}[i, a] = \{s_j, r_k\} \implies$ Parser cannot choose between shift and reduce!
* **LALR(1) Reduce-Reduce (R/R) Conflict**: Occurs when merging two CLR states creates:
  $$[A \to \alpha \cdot, a] \quad \text{AND} \quad [B \to \beta \cdot, a] \quad \text{in the same state!}$$

---

## 4. Dr. Gaurav Soni's Mandatory TM 6-Part Checklist

When writing ANY Turing Machine question, check off all 6 boxes:
1. `[ ]` **Part 1: Language Description** ($L = \{a^n b^n c^n \mid n \ge 1\}$).
2. `[ ]` **Part 2: Design Logic** (Strategy in English: tape head, markers $X, Y, Z$, backtrack).
3. `[ ]` **Part 3: Formal 7-Tuples** ($Q, \Sigma, \Gamma, \delta, q_0, B, F$).
4. `[ ]` **Part 4: Transition Table** ($\delta$ rows = states, columns = tape symbols).
5. `[ ]` **Part 5: State Transition Diagram** (Clean graph, double circle final state).
6. `[ ]` **Part 6: Validation** (Instantaneous Description $\vdash$ string trace).

---

## 5. Basic Blocks & Code Optimization Checklist

* **The 3 Leader Rules**:
  1. Statement 1 is a Leader.
  2. Target of any conditional / unconditional `goto` is a Leader.
  3. Statement immediately following any conditional / unconditional `goto` is a Leader.
* **The 4 Code Optimization Techniques**:
  1. **Common Subexpression Elimination**: Reusing already calculated values.
  2. **Dead Code Elimination**: Removing unused variables or unreachable code.
  3. **Constant Folding / Propagation**: Evaluating constant math at compile time ($3 + 2 \to 5$).
  4. **Loop Invariant Code Motion**: Moving expressions that don't change outside the loop body.
  5. **Strength Reduction**: Replacing costly operations (e.g. $i * 4 \to t = t + 4$).
