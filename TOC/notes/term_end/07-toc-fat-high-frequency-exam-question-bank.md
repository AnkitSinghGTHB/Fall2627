# 🏆 TOC & Compiler Design: High-Frequency FAT Solved Question Bank

> **Faculty**: Dr. Gaurav Soni  
> **Course**: CSE2004 — Theory of Computation and Compiler Design  
> **Source**: Compiled directly from VIT Bhopal End-Term (FAT) papers and CAT papers.  
> **Objective**: Solved with Dr. Soni's **EXACT marking-scheme steps** so evaluators cannot deduct even half a mark.

---

## 📌 MODULE 1: FINITE AUTOMATA & MINIMIZATION

### ❓ Question 1.1 (10 Marks): DFA Minimization via Table-Filling Method
> **Problem (VIT FAT 2024)**:  
> Minimize the following DFA using the Myhill-Nerode Table-Filling Method.  
> States: $\{q_0, q_1, q_2, q_3, q_4, q_5\}$, Start state: $q_0$, Final state: $\{q_2\}$, Alphabet: $\{0, 1\}$.  
> Transitions:  
> $\delta(q_0, 0) = q_1, \delta(q_0, 1) = q_3$  
> $\delta(q_1, 0) = q_2, \delta(q_1, 1) = q_4$  
> $\delta(q_2, 0) = q_1, \delta(q_2, 1) = q_4$ (Final)  
> $\delta(q_3, 0) = q_2, \delta(q_3, 1) = q_4$  
> $\delta(q_4, 0) = q_4, \delta(q_4, 1) = q_4$  
> $\delta(q_5, 0) = q_5, \delta(q_5, 1) = q_4$

#### Step-by-Step Model Solution:

* **Step 1: Reachability Analysis** `[1 Mark]`  
  - From start state $q_0$: Reachable states are $q_1, q_2, q_3, q_4$.  
  - State $q_5$ has no incoming transitions from $q_0$. Therefore, **$q_5$ is unreachable** and is eliminated immediately!  
  - Remaining active states: $\{q_0, q_1, q_2, q_3, q_4\}$.

* **Step 2 & 3: Basis Marking (Final vs Non-Final)** `[3 Marks]`  
  - Final state set: $F = \{q_2\}$.  
  - Non-final state set: $\{q_0, q_1, q_3, q_4\}$.  
  - Mark with **`X`** all pairs containing $q_2$: $(q_2, q_0), (q_2, q_1), (q_2, q_3), (q_2, q_4)$.

```text
Triangular Grid:
q₁ |  -
q₂ |  X   X
q₃ |  -   -   X
q₄ |  -   -   X   -
   +-------------------
      q₀  q₁  q₂  q₃
```

* **Step 4: Inductive State Pair Evaluation** `[4 Marks]`  
  1. Check pair $(q_1, q_3)$:  
     - On input 0: $(\delta(q_1,0), \delta(q_3,0)) = (q_2, q_2)$ (Identical states $\to$ no mark).  
     - On input 1: $(\delta(q_1,1), \delta(q_3,1)) = (q_4, q_4)$ (Identical states $\to$ no mark).  
     - Since both transitions lead to identical states, **pair $(q_1, q_3)$ remains UNMARKED!**
  2. Check pair $(q_0, q_1)$:  
     - On input 0: $(\delta(q_0,0), \delta(q_1,0)) = (q_1, q_2) \to$ **Marked with `X`**!  
     - Therefore, mark $(q_0, q_1)$ with **`X`**.
  3. Check pair $(q_0, q_3)$:  
     - On input 0: $(q_1, q_2) \to$ **Marked with `X`**! Mark $(q_0, q_3)$ with **`X`**.
  4. Check pair $(q_1, q_4)$:  
     - On input 0: $(q_2, q_4) \to$ **Marked with `X`**! Mark $(q_1, q_4)$ with **`X`**.
  5. Check pair $(q_3, q_4)$:  
     - On input 0: $(q_2, q_4) \to$ **Marked with `X`**! Mark $(q_3, q_4)$ with **`X`**.
  6. Check pair $(q_0, q_4)$:  
     - On input 0: $(q_1, q_4) \to$ **Marked with `X`**! Mark $(q_0, q_4)$ with **`X`**.

* **Step 5: Equivalent Partition & Minimized Automaton** `[2 Marks]`  
  - The only unmarked pair is **$(q_1, q_3)$**.  
  - Equivalent states: $[q_1, q_3]$.  
  - Minimized States: $\{q_0\}$, $\{q_2\}$, $\{q_4\}$, and composite state $\{q_1, q_3\}$.

```text
Minimized DFA Transition Table:
┌─────────────────┬───────────────────┬───────────────────┐
│     State       │     Input: 0      │     Input: 1      │
├─────────────────┼───────────────────┼───────────────────┤
│    → q₀         │      [q₁, q₃]     │      [q₁, q₃]     │
│   * q₂          │      [q₁, q₃]     │         q₄        │
│    [q₁, q₃]     │         q₂        │         q₄        │
│      q₄         │         q₄        │         q₄        │
└─────────────────┴───────────────────┴───────────────────┘
```

---

## 📌 MODULE 2: CONTEXT-FREE GRAMMARS & PDA

### ❓ Question 2.1 (10 Marks): Convert CFG to Chomsky Normal Form (CNF)
> **Problem (VIT FAT 2023)**:  
> Convert the following Context-Free Grammar into Chomsky Normal Form (CNF):  
> $$S \to aAB \mid BA$$  
> $$A \to bA \mid a \mid \epsilon$$  
> $$B \to aB \mid b$$

#### Step-by-Step Model Solution:

* **Step 1: Elimination of $\epsilon$-Productions** `[2.5 Marks]`  
  - Nullable variable: $A \to \epsilon$. ($A$ is nullable).  
  - Replace $A$ in rules:  
    From $S \to aAB \implies S \to aB$.  
    From $S \to BA \implies S \to B$.  
    From $A \to bA \implies A \to b$.  
  - Remove $A \to \epsilon$.  
  - Resulting grammar $P_1$:  
    $$S \to aAB \mid aB \mid BA \mid B$$  
    $$A \to bA \mid b \mid a$$  
    $$B \to aB \mid b$$

* **Step 2: Elimination of Unit Productions** `[2.5 Marks]`  
  - Unit production: $S \to B$.  
  - Productions of $B$: $B \to aB \mid b$.  
  - Substitute productions of $B$ into $S$:  
    $$S \to aAB \mid aB \mid BA \mid aB \mid b \implies S \to aAB \mid aB \mid BA \mid b$$  
  - Resulting grammar $P_2$:  
    $$S \to aAB \mid aB \mid BA \mid b$$  
    $$A \to bA \mid b \mid a$$  
    $$B \to aB \mid b$$

* **Step 3: Elimination of Useless Symbols** `[2 Marks]`  
  - Generating test: All variables $\{S, A, B\}$ derive terminal strings.  
  - Reachability test: From start symbol $S$, variables $A$ and $B$ are both reachable.  
  - No useless symbols exist.

* **Step 4: Conversion to CNF ($A \to BC$ or $A \to a$)** `[3 Marks]`  
  - Introduce terminal variables: $T_a \to a$ and $T_b \to b$.  
  - Rules already in valid CNF: $S \to b$, $A \to a$, $A \to b$, $B \to b$.  
  - Convert binary mixed productions:  
    $S \to BA$ is already in CNF ($A \to BC$).  
    $S \to aB \implies S \to T_a B$.  
    $A \to bA \implies A \to T_b A$.  
    $B \to aB \implies B \to T_a B$.  
  - Convert long production:  
    $S \to aAB \implies S \to T_a (AB)$.  
    Introduce variable $C_1 \to AB$.  
    Then $S \to T_a C_1$.

#### Final CNF Grammar:
$$\begin{aligned}
S &\to T_a C_1 \mid T_a B \mid BA \mid b \\
C_1 &\to AB \\
A &\to T_b A \mid a \mid b \\
B &\to T_a B \mid b \\
T_a &\to a \\
T_b &\to b
\end{aligned}$$
*(Every single rule strictly conforms to $A \to BC$ or $A \to a$. Full 10 Marks!)*

---

## 📌 MODULE 3: TOP-DOWN & BOTTOM-UP PARSING

### ❓ Question 3.1 (10 Marks): SLR(1) Table & Shift-Reduce Conflict Proof
> **Problem (VIT FAT 2024)**:  
> Given the grammar:  
> $$S \to L = R \mid R$$  
> $$L \to * R \mid id$$  
> $$R \to L$$  
> 1. Find the canonical collection of $LR(0)$ items.  
> 2. Construct the SLR(1) parsing table.  
> 3. Mathematically prove that the grammar has a Shift-Reduce conflict and is NOT SLR(1).

#### Model Solution:

* **Step 1: Augmented Grammar & Numbered Rules** `[1.5 Marks]`  
  (0) $S' \to S$  
  (1) $S \to L = R$  
  (2) $S \to R$  
  (3) $L \to * R$  
  (4) $L \to id$  
  (5) $R \to L$

* **Step 2: FIRST and FOLLOW Sets** `[1.5 Marks]`  
  - $\text{FOLLOW}(S) = \{\$\}$  
  - $\text{FOLLOW}(L) = \{=, \$\}$  
  - $\text{FOLLOW}(R) = \{=, \$\}$

* **Step 3: Canonical Collection of $LR(0)$ Items** `[3 Marks]`  
  - **$I_0$**: $\text{CLOSURE}(\{S' \to \cdot S\})$:  
    $[S' \to \cdot S]$  
    $[S \to \cdot L = R]$  
    $[S \to \cdot R]$  
    $[L \to \cdot * R]$  
    $[L \to \cdot id]$  
    $[R \to \cdot L]$  
  - $\text{GOTO}(I_0, S) = I_1 = \{[S' \to S \cdot]\}$  
  - $\text{GOTO}(I_0, L) = \mathbf{I_2}$:  
    $[S \to L \cdot = R]$ &nbsp;&nbsp;&nbsp;&nbsp;*(Shift item on terminal $=$)*  
    $[R \to L \cdot]$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*(Reduce item by rule 5)*

* **Step 4: Mathematical Proof of Shift-Reduce Conflict** `[4 Marks]`  
  - Consider state **$I_2$**:  
    1. Item $[S \to L \cdot = R]$ specifies a **Shift action on terminal $=$**:  
       $\text{ACTION}[2, =] \text{ contains } s_6$ (where $\text{GOTO}(I_2, =) = I_6$).  
    2. Item $[R \to L \cdot]$ specifies a **Reduce action by production rule (5) on all terminals in $\text{FOLLOW}(R)$**.  
       Since $\text{FOLLOW}(R) = \{=, \$\}$, terminal $=$ is in $\text{FOLLOW}(R)$:  
       $\text{ACTION}[2, =] \text{ contains } r_5$.  
  - **Conflict**: The table cell $\text{ACTION}[2, =]$ contains **BOTH a Shift and a Reduce action**:  
    $$\text{ACTION}[2, =] = \{s_6, r_5\}$$  
  - **Conclusion**: Because there is a multi-action collision in cell $[2, =]$, the grammar exhibits a **Shift-Reduce (S/R) Conflict**.  
  - Therefore, the grammar is **NOT SLR(1)**. **Hence Proved.** *(Full 10 Marks!)*

---

## 📌 MODULE 4: TURING MACHINES (Dr. Soni's 6-Part Layout)

### ❓ Question 4.1 (10 Marks): Turing Machine for $L = \{a^n b^n c^n \mid n \ge 1\}$
*(See complete 6-Part model answer written under Module 4: [04-module4-turing-machines-and-undecidability.md](./04-module4-turing-machines-and-undecidability.md#2-solved-master-tm-1-l--an-bn-cn-mid-n-ge-1-guaranteed-10-marks)).*

---

## 📌 MODULE 5: THREE ADDRESS CODE & BASIC BLOCKS

### ❓ Question 5.1 (10 Marks): Quadruples, Triples & Indirect Triples
> **Problem (VIT FAT 2024)**:  
> Generate Quadruples, Triples, and Indirect Triples for the statement:  
> $$x = (a + b) * (c - d) / (a + b)$$

#### Model Solution:

* **Step 1: Three Address Code (TAC)** `[2.5 Marks]`  
  1. $t_1 = a + b$  
  2. $t_2 = c - d$  
  3. $t_3 = t_1 * t_2$  
  4. $t_4 = a + b$  
  5. $t_5 = t_3 / t_4$  
  6. $x = t_5$

* **Step 2: Quadruples Table** `[2.5 Marks]`  
  | Index | `op` | `arg1` | `arg2` | `result` |
  | :---: | :---: | :---: | :---: | :---: |
  | **(0)** | `+` | $a$ | $b$ | $t_1$ |
  | **(1)** | `-` | $c$ | $d$ | $t_2$ |
  | **(2)** | `*` | $t_1$ | $t_2$ | $t_3$ |
  | **(3)** | `+` | $a$ | $b$ | $t_4$ |
  | **(4)** | `/` | $t_3$ | $t_4$ | $t_5$ |
  | **(5)** | `=` | $t_5$ | — | $x$ |

* **Step 3: Triples Table** `[2.5 Marks]`  
  | Index | `op` | `arg1` | `arg2` |
  | :---: | :---: | :---: | :---: |
  | **(0)** | `+` | $a$ | $b$ |
  | **(1)** | `-` | $c$ | $d$ |
  | **(2)** | `*` | `(0)` | `(1)` |
  | **(3)** | `+` | $a$ | $b$ |
  | **(4)** | `/` | `(2)` | `(3)` |
  | **(5)** | `assign` | $x$ | `(4)` |

* **Step 4: Indirect Triples Table** `[2.5 Marks]`  
  | Statement Array Pointer | Target Triples Index |
  | :---: | :---: |
  | `statement[0]` | `(0)` |
  | `statement[1]` | `(1)` |
  | `statement[2]` | `(2)` |
  | `statement[3]` | `(3)` |
  | `statement[4]` | `(4)` |
  | `statement[5]` | `(5)` |

*(Full 10/10 Marks!)*

---

### ❓ Question 5.2 (10/12 Marks): TAC Translation for Array & While Loop (Direct from Assignment 2 Q5)
> **Problem**: Translate the following program into Three-Address Code, Quadruples, and Triples:
> ```c
> main() {
>     int i;
>     int a[10];
>     i = 1;
>     while (i < 10) {
>         a[i] = 0;
>         i = i + 1;
>     }
> }
> ```

#### Step-by-Step Model Solution:

* **Step 1: Intermediate Three Address Code (TAC)**:
  *(Assuming 4 bytes per integer element in array `a`)*:
  ```text
  (1)  i = 1
  (2)  L1: if i >= 10 goto L2
  (3)  t1 = i * 4
  (4)  a[t1] = 0
  (5)  t2 = i + 1
  (6)  i = t2
  (7)  goto L1
  (8)  L2:
  ```

* **Step 2: Quadruples Table**:
  | Line | `op` | `arg1` | `arg2` | `result` |
  | :---: | :---: | :---: | :---: | :---: |
  | **(0)** | `=` | `1` | — | `i` |
  | **(1)** | `>=` | `i` | `10` | `t0` |
  | **(2)** | `if_true`| `t0` | — | `(7)` *(goto L2)* |
  | **(3)** | `*` | `i` | `4` | `t1` |
  | **(4)** | `[]=` | `0` | — | `a[t1]` |
  | **(5)** | `+` | `i` | `1` | `t2` |
  | **(6)** | `=` | `t2` | — | `i` |
  | **(7)** | `goto` | — | — | `(1)` *(goto L1)* |

---

### ❓ Question 5.3 (8/10 Marks): Directed Acyclic Graph (DAG) for Expression (From tee_imp.txt)
> **Problem**: Construct the Directed Acyclic Graph (DAG) for the arithmetic expression:
> $$E = (a + b) \wedge c + (c + d)$$
> Also identify the common subexpressions and generate optimal code.

#### Model Solution:
* **Step 1: Subexpression Breakdown**:
  1. $n_1 = a + b$
  2. $n_2 = n_1 \wedge c$ (Power / XOR operation depending on operator definition)
  3. $n_3 = c + d$
  4. $n_4 = n_2 + n_3$
* **Step 2: DAG Construction**:
  - Leaf nodes: `a`, `b`, `c`, `d`.
  - Node `c` is shared by both $(n_1 \wedge c)$ and $(c + d)$. In an Abstract Syntax Tree (AST), node `c` is duplicated. In a **DAG**, node `c` has **two parent pointers**:
  ```text
            (+) [n4 - Root]
           /   \
         (^)   (+) [n3]
        /   \  / \
      (+)    (c) (d)
      / \
    (a) (b)
  ```
  *(Node `c` has in-degree 0 and out-degree to parents `^` and `+`. This eliminates redundant memory accesses).*

---

### ❓ Question 2.2 (10/12 Marks): Pushdown Automaton for $L = \{0^n 1^n \mid n \ge 1\}$ (Assignment 2 Q2)
> **Problem**: Design a Pushdown Automaton (PDA) for language $L = \{0^n 1^n \mid n \ge 1\}$ by empty store and final state.

#### Model Solution (Dr. Soni's 6-Part Rubric):
* **Part 1: Language Specification**:
  $$L = \{0^n 1^n \mid n \ge 1\} = \{01, 0011, 000111, \dots\}$$
* **Part 2: Design Logic**:
  - For every input symbol `0` read in state $q_0$, push a marker `0` onto the stack.
  - On the first input symbol `1`, transition to state $q_1$ and pop one `0` from stack.
  - For every subsequent `1`, continue popping `0` in state $q_1$.
  - When input ends ($\epsilon$) and stack shows initial marker $Z_0$, transition to final state $q_2$.
* **Part 3: Formal 7-Tuples**:
  $$M = (Q, \Sigma, \Gamma, \delta, q_0, Z_0, F)$$
  - $Q = \{q_0, q_1, q_2\}$
  - $\Sigma = \{0, 1\}$
  - $\Gamma = \{0, Z_0\}$
  - Start state: $q_0$; Initial stack symbol: $Z_0$
  - Final state set: $F = \{q_2\}$
* **Part 4: Transition Function ($\delta$)**:
  1. $\delta(q_0, 0, Z_0) = \{(q_0, 0 Z_0)\}$ (Push first 0)
  2. $\delta(q_0, 0, 0) = \{(q_0, 0 0)\}$ (Push subsequent 0)
  3. $\delta(q_0, 1, 0) = \{(q_1, \epsilon)\}$ (Match first 1, pop 0)
  4. $\delta(q_1, 1, 0) = \{(q_1, \epsilon)\}$ (Match subsequent 1s, pop 0)
  5. $\delta(q_1, \epsilon, Z_0) = \{(q_2, Z_0)\}$ (Acceptance by final state)
* **Part 5: State Transition Diagram**:
  `[Draw states q0, q1, q2 with labeled edges: (0, Z0 -> 0Z0), (0, 0 -> 00), (1, 0 -> eps), (eps, Z0 -> Z0)]`
* **Part 6: Instantaneous Description ($\vdash$) for $w = 0011$**:
  $$(q_0, 0011, Z_0) \vdash (q_0, 011, 0 Z_0) \vdash (q_0, 11, 00 Z_0) \vdash (q_1, 1, 0 Z_0) \vdash (q_1, \epsilon, Z_0) \vdash (q_2, \epsilon, Z_0)$$
  *(Accepted! String accepted by final state).*

---

### ❓ Question 2.3 (10/12 Marks): GNF Conversion for $S \to SS \mid 0S1 \mid 01$ (Assignment 2 Q4)
> **Problem**: Convert the grammar into Greibach Normal Form (GNF):
> $$S \to SS \mid 0S1 \mid 01$$

#### Model Solution:
* **Step 1: Rename Variables and Terminals**:
  Let $A_1 = S$. Let terminals be $a = 0, b = 1$.
  Introduce non-terminals for terminals: $B \to 1$.
  Rules become:
  $$A_1 \to A_1 A_1 \mid 0 A_1 B \mid 0 B$$
  *(Notice: $A_1 \to A_1 A_1$ is in left-recursive form $A_r \to A_s \alpha$ where $r = s = 1$).*
* **Step 2: Eliminate Left Recursion ($A_1 \to A_1 \alpha \mid \beta$)**:
  - Here $\alpha = A_1$.
  - Non-left-recursive productions: $\beta = 0 A_1 B \mid 0 B$.
  - Introduce new variable $Z$:
    $$A_1 \to 0 A_1 B \mid 0 B \mid 0 A_1 B Z \mid 0 B Z$$
    $$Z \to A_1 \mid A_1 Z$$
* **Step 3: Substitute $A_1$ into $Z$ to satisfy GNF ($A \to a \alpha$)**:
  Substitute all right-hand expansions of $A_1$ into $Z$:
  $$Z \to 0 A_1 B \mid 0 B \mid 0 A_1 B Z \mid 0 B Z \mid 0 A_1 B Z \mid 0 B Z \mid 0 A_1 B Z Z \mid 0 B Z Z$$
  $$B \to 1$$
* **Final GNF Productions**:
  Every rule begins with exactly one terminal symbol ($0$ or $1$) followed by zero or more variables:
  $$\begin{aligned}
  A_1 &\to 0 A_1 B \mid 0 B \mid 0 A_1 B Z \mid 0 B Z \\
  Z &\to 0 A_1 B \mid 0 B \mid 0 A_1 B Z \mid 0 B Z \mid 0 A_1 B Z Z \mid 0 B Z Z \\
  B &\to 1
  \end{aligned}$$
  *(Full Marks!)*

---

### ❓ Question 1.2 (8 Marks): Arden's Theorem (Statement, Proof & Application)
> **Problem (From tee_imp.txt)**:  
> State and prove Arden's Theorem. Use it to find the regular expression for a DFA with transitions:  
> $q_1 = q_1 0 + \epsilon$, $q_2 = q_1 1 + q_2 1$.

#### Model Solution:
* **Statement**: Let $P$ and $Q$ be two regular expressions over alphabet $\Sigma$. If $P$ does not contain $\epsilon$ (the null string), then the equation:
  $$R = Q + RP$$
  has a **unique solution** given by:
  $$R = QP^*$$
* **Proof**:
  1. *Existence*: Substitute $R = QP^*$ into RHS:
     $$\text{RHS} = Q + (QP^*)P = Q(\epsilon + P^* P) = Q P^* = \text{LHS}$$
  2. *Uniqueness*: Repeatedly expand $R$:
     $$R = Q + (Q + RP)P = Q + QP + RP^2 = Q( \epsilon + P + P^2 + \dots + P^k ) + RP^{k+1}$$
     In the limit as $k \to \infty$, $R = QP^*$.
* **Application to System**:
  - $q_1 = q_1 0 + \epsilon \implies$ By Arden's Theorem ($Q = \epsilon, P = 0$):  
    $$\mathbf{q_1 = \epsilon \cdot 0^* = 0^*}$$
  - $q_2 = q_1 1 + q_2 1 \implies q_2 = (0^* 1) + q_2 1$.
  - By Arden's Theorem ($Q = 0^* 1, P = 1$):  
    $$\mathbf{q_2 = (0^* 1) 1^* = 0^* 1^+}$$

---

### ❓ Question 3.2 (8 Marks): CLR(1) vs LALR(1) Parsers (From tee_imp.txt)
> **Problem**: Differentiate between CLR(1) and LALR(1) parsers. Why is LALR(1) preferred in practical compiler construction like Yacc/Bison?

#### Model Solution:

| Feature | CLR(1) Parser (Canonical LR) | LALR(1) Parser (Lookahead LR) |
|:---|:---|:---|
| **State Construction** | Keeps all LR(1) items $[A \to \alpha \cdot \beta, a]$ distinct | Merges LR(1) states having **identical cores** (same production and dot position) differing only in lookahead |
| **Number of States** | Massive (often thousands of states: $O(|LR(0)| \times |\Sigma|)$) | Exactly equal to the number of states in an **$LR(0)$ / $SLR(1)$ parser** |
| **Parsing Power** | Highest among deterministic LR parsers | Slightly less than CLR(1); handles vast majority of programming language constructs |
| **Conflict Generation** | Free of reduce-reduce conflicts if grammar is LR(1) | Merging states **CAN NEVER produce a Shift-Reduce conflict**, but can rarely introduce **Reduce-Reduce conflicts** |
| **Industry Usage** | Rarely used due to impractical memory footprint | **Universal industry standard** (Used by Yacc, Bison) |

