# 🎯 TOC & Compiler Design: TEE Master Solutions Handbook

> **Course**: CSE2004 — Theory of Computation and Compiler Design  
> **Faculty**: Dr. Gaurav Soni  
> **Purpose**: Complete, step-by-step solved solutions for all topics listed in [tee_imp.txt](../../resources/tee_imp.txt).  
> **Official TEE Exam Pattern (100 Marks Total, per TEE.txt)**:
> - **Section A (60 Marks)**: 5 Questions (1 per module), **12 Marks each** in `OR` format (either 12M full or 6M + 6M subparts).
> - **Section B (40 Marks)**: 5 Questions (1 per module), **8 Marks each**, strictly **WITHOUT SUBPARTS**.
> - **Grading Standard**: Solved using Dr. Soni's strict **6-part layout** (Language Specification ➔ Logic ➔ 7-Tuples ➔ Transition Table ➔ State Diagram ➔ Instantaneous Description / String Verification).

---

## 📑 TABLE OF CONTENTS
1. [Finite Automata & Regular Languages](#1-finite-automata--regular-languages)
   - [Problem 1.1: DFA for Strings Ending in 101, Ending in 110 & Substring 110](#problem-11-dfa-for-strings-ending-in-101-ending-in-110--substring-110)
   - [Problem 1.2: String Acceptance Verification Trace for w = 100110](#problem-12-string-acceptance-verification-trace-for-w--100110)
   - [Problem 1.3: Convert Regular Expression (a⁺ + b⁺)ab to DFA](#problem-13-convert-regular-expression-a--bab-to-dfa)
   - [Problem 1.4: Conversion of ε-NFA to DFA via ε-Closure](#problem-14-conversion-of-ε-nfa-to-dfa-via-ε-closure)
   - [Problem 1.5: Arden's Theorem — Statement, Algebraic Proof & System Application](#problem-15-ardens-theorem--statement-algebraic-proof--system-application)
2. [Pushdown Automata & Context-Free Languages](#2-pushdown-automata--context-free-languages)
   - [Problem 2.1: PDA for L = {aⁿ bⁿ | n ≥ 1}](#problem-21-pda-for-l--an-bn--n--1)
   - [Problem 2.2: PDA for L = {w c wᴿ | w ∈ {a, b}*}](#problem-22-pda-for-l--w-c-wr--w--a-b)
   - [Problem 2.3: PDA for L = {aⁿ bᵐ | n ≠ m}](#problem-23-pda-for-l--an-bm--n--m)
   - [Problem 2.4: Deterministic Pushdown Automata (DPDA) for Equal a's and b's](#problem-24-deterministic-pushdown-automata-dpda-for-equal-as-and-bs)
   - [Problem 2.5: Leftmost Derivation (LMD), Rightmost Derivation (RMD) & Parse Trees](#problem-25-leftmost-derivation-lmd-rightmost-derivation-rmd--parse-trees)
   - [Problem 2.6: The Chomsky Hierarchy of Languages & Automata](#problem-26-the-chomsky-hierarchy-of-languages--automata)
   - [Problem 2.7: Conversion of PDA to CFG (Two Solved Exam Problems)](#problem-27-conversion-of-pda-to-cfg-two-solved-exam-problems)
3. [Turing Machines & Computability Theory](#3-turing-machines--computability-theory)
   - [Problem 3.1: Turing Machine for Equal 0s and 1s (Even 0s and Odd 1s)](#problem-31-turing-machine-for-equal-0s-and-1s-even-0s-and-odd-1s)
   - [Problem 3.2: Turing Machine for L = {aⁿ b²ⁿ | n ≥ 1}](#problem-32-turing-machine-for-l--an-b2n--n--1)
   - [Problem 3.3: Turing Machine for Unary Addition (0ᵐ 1 0ⁿ ➔ 0ᵐ⁺ⁿ)](#problem-33-turing-machine-for-unary-addition-0m-1-0n--0mn)
   - [Problem 3.4: Decidability, Recursive vs. Recursively Enumerable & Complement Property](#problem-34-decidability-recursive-vs-recursively-enumerable--complement-property)
4. [Compiler Design: Parsing, Syntax Trees & Three-Address Code](#4-compiler-design-parsing-syntax-trees--three-address-code)
   - [Problem 4.1: FIRST and FOLLOW Set Computation](#problem-41-first-and-follow-set-computation)
   - [Problem 4.2: Predictive LL(1) Parsing Table Construction & Stack Parsing](#problem-42-predictive-ll1-parsing-table-construction--stack-parsing)
   - [Problem 4.3: Stepwise SLR(1) Parsing Table Construction & Shift-Reduce Conflicts](#problem-43-stepwise-slr1-parsing-table-construction--shift-reduce-conflicts)
   - [Problem 4.4: Canonical LR (CLR(1)) vs. LALR(1) & Reduce-Reduce Conflicts](#problem-44-canonical-lr-clr1-vs-lalr1--reduce-reduce-conflicts)
   - [Problem 4.5: Directed Acyclic Graph (DAG) for Expression E = (a + b) ^ c + (c + d)](#problem-45-directed-acyclic-graph-dag-for-expression-e--a--b--c--c--d)
   - [Problem 4.6: TAC, Quadruples, Triples & Indirect Triples for Loops with Arrays](#problem-46-tac-quadruples-triples--indirect-triples-for-loops-with-arrays)
   - [Problem 4.7: Code Optimization Techniques & Target Machine Code Generation](#problem-47-code-optimization-techniques--target-machine-code-generation)

---

# 1. FINITE AUTOMATA & REGULAR LANGUAGES

---

### Problem 1.1: DFA for Strings Ending in 101, Ending in 110 & Substring 110
> **[TEE Section B: 8 Marks (Standalone - No Subparts)] / [TEE Section A: 6 Marks (Part a)]**:  
> Design Minimal Deterministic Finite Automata (DFA) over $\Sigma = \{0, 1\}$ for:  
> (a) Strings ending in `101`.  
> (b) Strings ending in `110`.  
> (c) Strings containing substring `110`.

#### (a) DFA for Strings Ending in `101`
* **States Meaning**:
  - $q_0$: Initial state / No progress or ended in `0`.
  - $q_1$: Last symbol seen was `1`.
  - $q_2$: Last two symbols seen were `10`.
  - $q_3$ (Final): Last three symbols seen were `101`.
* **Transition Table**:
  | State | Input: `0` | Input: `1` | Meaning |
  | :---: | :---: | :---: | :---|
  | **→ $q_0$** | $q_0$ | $q_1$ | Start / No match |
  | **$q_1$** | $q_2$ | $q_1$ | Saw `1` |
  | **$q_2$** | $q_0$ | $q_3$ | Saw `10` |
  | *** $q_3$** | $q_2$ | $q_1$ | Saw `101` (Accepting state; on `0` goes to $q_2$ since suffix is `10`; on `1` goes to $q_1$ since suffix is `1`) |

```
State Diagram:
       0           0
     ┌───┐       ┌───┐
     ▼   │       │   │
──▶ (q0) ──1──▶ (q1) ──0──▶ (q2) ──1──▶ ((q3))
      ▲          ▲ 1         │            │
      │          └───┘       │            │
      │               0      │            │
      └──────────────────────┘            │
      ▲                                   │
      │                 0                 │
      └───────────────────────────────────┤ (goes to q2 on 0, q1 on 1)
```

---

#### (b) DFA for Strings Ending in `110`
* **States Meaning**:
  - $q_0$: Start state.
  - $q_1$: Saw suffix `1`.
  - $q_2$: Saw suffix `11`.
  - $q_3$ (Final): Saw suffix `110`.
* **Transition Table**:
  | State | Input: `0` | Input: `1` |
  | :---: | :---: | :---: |
  | **→ $q_0$** | $q_0$ | $q_1$ |
  | **$q_1$** | $q_0$ | $q_2$ |
  | **$q_2$** | $q_3$ | $q_2$ |
  | *** $q_3$** | $q_0$ | $q_1$ |

---

#### (c) DFA for Strings Containing Substring `110`
* **Logic**: Once `110` is reached, transition to a **trap final state** that loops on all inputs.
* **Transition Table**:
  | State | Input: `0` | Input: `1` | Description |
  | :---: | :---: | :---: | :---|
  | **→ $q_0$** | $q_0$ | $q_1$ | Start |
  | **$q_1$** | $q_0$ | $q_2$ | Saw `1` |
  | **$q_2$** | $q_3$ | $q_2$ | Saw `11` |
  | *** $q_3$** | $q_3$ | $q_3$ | **Dead/Trap Accepting State** (Substring found!) |

---

### Problem 1.2: String Acceptance Verification Trace for $w = 100110$
> **[TEE Section A: 6 Marks (Part b)]**:  
> Trace the computation of the DFA accepting substring `110` on input string $w = 100110$. Prove formally whether $w$ is accepted.

#### Model Solution:
Use the extended transition function $\hat{\delta}$ or instantaneous state trace:
$$\begin{aligned}
\delta(q_0, 1) &= q_1 \\
\delta(q_1, 0) &= q_0 \\
\delta(q_0, 0) &= q_0 \\
\delta(q_0, 1) &= q_1 \\
\delta(q_1, 1) &= q_2 \\
\delta(q_2, 0) &= q_3
\end{aligned}$$
* **Formal Trace**:
  $$\hat{\delta}(q_0, 100110) = \hat{\delta}(q_1, 00110) = \hat{\delta}(q_0, 0110) = \hat{\delta}(q_0, 110) = \hat{\delta}(q_1, 10) = \hat{\delta}(q_2, 0) = \mathbf{q_3}$$
* **Conclusion**: Since the automaton reaches state $q_3$ and $q_3 \in F$, the string $w = 100110$ is **ACCEPTED**. `[Full Marks]`

---

### Problem 1.3: Convert Regular Expression $(a^+ + b^+)ab$ to DFA
> **[TEE Section B: 8 Marks (Standalone - No Subparts)] / [TEE Section A: 6 Marks (Part a)]**:  
> Convert the regular expression $R = (a^+ + b^+)ab$ into a minimal DFA.

#### Model Solution:
1. **Deconstruct the Regular Expression**:
   - $a^+ = a a^*$ (at least one $a$)
   - $b^+ = b b^*$ (at least one $b$)
   - $R$ matches strings that either:
     - Consist of one or more $a$'s followed by $ab$ (e.g., $aab, aaab, \dots$).
     - Consist of one or more $b$'s followed by $ab$ (e.g., $bab, bbab, \dots$).
2. **NFA Construction (Thompson's Method)**:
   - Branch 1: $q_0 \xrightarrow{a} q_1 \xrightarrow{a} q_1$ (absorbs $a^+$), then $\xrightarrow{a} q_3 \xrightarrow{b} q_4$.
   - Branch 2: $q_0 \xrightarrow{b} q_2 \xrightarrow{b} q_2$ (absorbs $b^+$), then $\xrightarrow{a} q_3 \xrightarrow{b} q_4$.
   - Notice $a^+ ab = a a^* a b$ requires at least **two $a$'s** before $b$.
   - $b^+ ab = b b^* a b$ requires at least one $b$ followed by $ab$.
3. **Subset Construction for DFA**:
   - Let start state $A = \{q_0\}$.
   - $\delta(A, a) = B$ (saw first $a$; must see another $a$ before $b$ is allowed).
   - $\delta(A, b) = C$ (saw first $b$; can loop on $b$, or see $a$ towards terminal $ab$).
   - $\delta(B, a) = D$ (now has at least two $a$'s $\implies a^+ a$).
   - $\delta(B, b) = \emptyset$ (DEAD: string $ab$ not generated because $a^+ ab$ requires $\ge 2$ $a$'s).
   - $\delta(C, b) = C$ (loops on $b^+$).
   - $\delta(C, a) = E$ (saw $b^+ a$; waiting for final $b$).
   - $\delta(D, a) = D$ (loops on additional $a$'s).
   - $\delta(D, b) = F$ (saw $a^+ a b \implies$ FINAL STATE!).
   - $\delta(E, b) = F$ (saw $b^+ a b \implies$ FINAL STATE!).
   - State $F$ is a dead state since there are no symbols after $ab$: $\delta(F, a) = \text{Trap}, \delta(F, b) = \text{Trap}$.
4. **DFA Transition Table**:
   | DFA State | Input: $a$ | Input: $b$ | Type |
   | :---: | :---: | :---: | :---: |
   | **→ $A$** | $B$ | $C$ | Start |
   | **$B$** | $D$ | Trap | Saw single $a$ |
   | **$C$** | $E$ | $C$ | Saw $b^+$ |
   | **$D$** | $D$ | $F$ | Saw $a^+ a$ |
   | **$E$** | Trap | $F$ | Saw $b^+ a$ |
   | *** $F$** | Trap | Trap | **Accepting** |
   | **Trap** | Trap | Trap | Dead state |

---

### Problem 1.4: Conversion of $\epsilon$-NFA to DFA via $\epsilon$-Closure
> **[TEE Section B: 8 Marks (Standalone - No Subparts)] / [TEE Section A: 6 Marks (Part a)]**:  
> Given an $\epsilon$-NFA with states $\{q_0, q_1, q_2\}$, transitions:  
> $\delta(q_0, \epsilon) = \{q_1\}, \delta(q_0, a) = \{q_0\}, \delta(q_1, b) = \{q_1\}, \delta(q_1, \epsilon) = \{q_2\}, \delta(q_2, c) = \{q_2\}$, Final State $= \{q_2\}$.  
> Convert to an equivalent DFA without $\epsilon$-transitions.

#### Model Solution:
* **Step 1: Compute $\epsilon$-Closures for each state**:
  - $\epsilon\text{-closure}(q_0) = \{q_0, q_1, q_2\}$ (since $q_0 \xrightarrow{\epsilon} q_1 \xrightarrow{\epsilon} q_2$).
  - $\epsilon\text{-closure}(q_1) = \{q_1, q_2\}$.
  - $\epsilon\text{-closure}(q_2) = \{q_2\}$.
* **Step 2: Determine Start State of DFA**:
  - $A = \epsilon\text{-closure}(q_0) = \{q_0, q_1, q_2\}$.
  - Since $q_2 \in A$, state $A$ is an **accepting state**!
* **Step 3: Compute Transitions for DFA**:
  - On input $a$:
    $\delta(A, a) = \epsilon\text{-closure}(\delta(\{q_0, q_1, q_2\}, a)) = \epsilon\text{-closure}(\{q_0\}) = \{q_0, q_1, q_2\} = A$.
  - On input $b$:
    $\delta(A, b) = \epsilon\text{-closure}(\delta(\{q_0, q_1, q_2\}, b)) = \epsilon\text{-closure}(\{q_1\}) = \{q_1, q_2\} = B$.
  - On input $c$:
    $\delta(A, c) = \epsilon\text{-closure}(\delta(\{q_0, q_1, q_2\}, c)) = \epsilon\text{-closure}(\{q_2\}) = \{q_2\} = C$.
* **Step 4: Transitions from $B = \{q_1, q_2\}$**:
  - $\delta(B, a) = \epsilon\text{-closure}(\emptyset) = \text{Trap}$.
  - $\delta(B, b) = \epsilon\text{-closure}(\{q_1\}) = \{q_1, q_2\} = B$.
  - $\delta(B, c) = \epsilon\text{-closure}(\{q_2\}) = \{q_2\} = C$.
* **Step 5: Transitions from $C = \{q_2\}$**:
  - $\delta(C, a) = \text{Trap}, \delta(C, b) = \text{Trap}$.
  - $\delta(C, c) = \epsilon\text{-closure}(\{q_2\}) = \{q_2\} = C$.
* **Resulting DFA Table**:
  | DFA State | Constituent NFA States | $a$ | $b$ | $c$ | Final? |
  | :---: | :---: | :---: | :---: | :---: | :---: |
  | **→* $A$** | $\{q_0, q_1, q_2\}$ | $A$ | $B$ | $C$ | **Yes** |
  | *** $B$** | $\{q_1, q_2\}$ | Trap | $B$ | $C$ | **Yes** |
  | *** $C$** | $\{q_2\}$ | Trap | Trap | $C$ | **Yes** |
  | **Trap** | $\emptyset$ | Trap | Trap | Trap | No |

---

### Problem 1.5: Arden's Theorem — Statement, Algebraic Proof & System Application
> **[TEE Section A: 12 Marks (Full Question with Proof + DFA Solution)]**:  
> (a) State and prove Arden's Theorem.  
> (b) Consider the equations for a 3-state DFA:  
> $q_1 = q_1 0 + \epsilon$, $q_2 = q_1 1 + q_2 1$, $q_3 = q_2 0 + q_3 (0 + 1)$.  
> Find the regular expression for state $q_2$ and $q_3$.

#### (a) Statement & Proof:
* **Theorem Statement**: Let $P$ and $Q$ be two regular expressions over alphabet $\Sigma$. If $P$ does not contain the null string $\epsilon$, then the equation:
  $$R = Q + RP$$
  has a **unique solution**:
  $$R = QP^*$$
* **Proof**:
  1. **Existence**: Substitute $R = QP^*$ into the RHS:
     $$\text{RHS} = Q + (QP^*)P = Q(\epsilon + P^* P)$$
     By regular expression identities, $\epsilon + P^* P = P^*$.
     $$\text{RHS} = QP^* = R = \text{LHS}$$
  2. **Uniqueness**: Substitute $R = Q + RP$ recursively into itself:
     $$R = Q + (Q + RP)P = Q + QP + RP^2$$
     $$R = Q + QP + (Q + RP)P^2 = Q + QP + QP^2 + RP^3$$
     $$R = Q(\epsilon + P + P^2 + \dots + P^k) + RP^{k+1}$$
     As $k \to \infty$, $RP^{k+1}$ vanishes for strings of length $\le k$ (since $P$ has no $\epsilon$, $P^{k+1}$ has length at least $k+1$).
     $$\therefore R = Q P^* \quad \text{[Unique solution proven!]}$$

#### (b) Solution of System:
1. For $q_1$:
   $$q_1 = \epsilon + q_1 0$$
   Here $Q = \epsilon, P = 0$. By Arden's Theorem:
   $$\mathbf{q_1 = \epsilon \cdot 0^* = 0^*}$$
2. For $q_2$:
   $$q_2 = q_1 1 + q_2 1 = (0^* 1) + q_2 1$$
   Here $Q = 0^* 1, P = 1$. By Arden's Theorem:
   $$\mathbf{q_2 = (0^* 1) 1^* = 0^* 1^+}$$
3. For $q_3$:
   $$q_3 = q_2 0 + q_3 (0 + 1) = (0^* 1^+ 0) + q_3 (0 + 1)$$
   Here $Q = 0^* 1^+ 0, P = (0 + 1)$. By Arden's Theorem:
   $$\mathbf{q_3 = (0^* 1^+ 0)(0 + 1)^*}$$

---

# 2. PUSHDOWN AUTOMATA & CONTEXT-FREE LANGUAGES

---

### Problem 2.1: PDA for $L = \{a^n b^n \mid n \ge 1\}$
> **[TEE Section B: 8 Marks (Standalone - No Subparts)] / [TEE Section A: 6 Marks]**:  
> Design a Pushdown Automaton for $L = \{a^n b^n \mid n \ge 1\}$ using acceptance by Final State. Provide formal 7-tuples, transition table, and Instantaneous Description for $w = aabb$.

#### Step-by-Step Model Solution:
* **Part 1: Language**: $L = \{ab, aabb, aaabbb, \dots\}$
* **Part 2: Design Logic**:
  - State $q_0$: Read $a$, push $a$ onto stack above $Z_0$.
  - First $b$: Transition to state $q_1$, pop matching $a$.
  - Subsequent $b$'s: Pop $a$ in state $q_1$.
  - On $\epsilon$ (end of input), if stack shows $Z_0$, transition to final state $q_2$.
* **Part 3: 7-Tuples**:
  $$M = (Q, \Sigma, \Gamma, \delta, q_0, Z_0, F)$$
  where $Q = \{q_0, q_1, q_2\}$, $\Sigma = \{a, b\}$, $\Gamma = \{a, Z_0\}$, $F = \{q_2\}$.
* **Part 4: Transitions ($\delta$)**:
  1. $\delta(q_0, a, Z_0) = \{(q_0, a Z_0)\}$
  2. $\delta(q_0, a, a) = \{(q_0, a a)\}$
  3. $\delta(q_0, b, a) = \{(q_1, \epsilon)\}$
  4. $\delta(q_1, b, a) = \{(q_1, \epsilon)\}$
  5. $\delta(q_1, \epsilon, Z_0) = \{(q_2, Z_0)\}$
* **Part 5: Instantaneous Description ($\vdash$) for $w = aabb$**:
  $$\begin{aligned}
  (q_0, aabb, Z_0) &\vdash (q_0, abb, a Z_0) \\
  &\vdash (q_0, bb, aa Z_0) \\
  &\vdash (q_1, b, a Z_0) \\
  &\vdash (q_1, \epsilon, Z_0) \\
  &\vdash (q_2, \epsilon, Z_0) \quad \text{[Accepted! Final State } q_2 \in F\text{ reached]}
  \end{aligned}$$

---

### Problem 2.2: PDA for $L = \{w c w^R \mid w \in \{a, b\}^*\}$
> **[TEE Section A: 12 Marks (Full Question with 6-Part Layout)] / [TEE Section B: 8 Marks]**:  
> Design a Deterministic PDA (DPDA) for palindrome language with center marker $c$: $L = \{w c w^R \mid w \in \{a, b\}^*\}$.

#### Step-by-Step Model Solution:
* **Logic**: Push all symbols of $w$ onto stack. Marker $c$ indicates exact middle; transition to match state without altering stack. Then compare incoming symbols of $w^R$ against top of stack, popping on match.
* **Formal Tuples**:
  - $Q = \{q_0, q_1, q_2\}$, $\Sigma = \{a, b, c\}$, $\Gamma = \{a, b, Z_0\}$, $F = \{q_2\}$.
* **Transition Table**:
  | Current State | Input | Stack Top | Next State, Stack Operation |
  | :---: | :---: | :---: | :---: |
  | $q_0$ | $a$ | $Z_0$ | $(q_0, a Z_0)$ (Push) |
  | $q_0$ | $b$ | $Z_0$ | $(q_0, b Z_0)$ (Push) |
  | $q_0$ | $a$ | $a$ | $(q_0, a a)$ (Push) |
  | $q_0$ | $a$ | $b$ | $(q_0, a b)$ (Push) |
  | $q_0$ | $b$ | $a$ | $(q_0, b a)$ (Push) |
  | $q_0$ | $b$ | $b$ | $(q_0, b b)$ (Push) |
  | $q_0$ | $c$ | Any ($X$) | $(q_1, X)$ (Center marker; switch state, leave stack unchanged) |
  | $q_1$ | $a$ | $a$ | $(q_1, \epsilon)$ (Match & Pop) |
  | $q_1$ | $b$ | $b$ | $(q_1, \epsilon)$ (Match & Pop) |
  | $q_1$ | $\epsilon$ | $Z_0$ | $(q_2, Z_0)$ (Accept by Final State) |

* **Trace for $w = abcba$**:
  $$(q_0, abcba, Z_0) \vdash (q_0, bcba, aZ_0) \vdash (q_0, cba, baZ_0) \vdash (q_1, ba, baZ_0) \vdash (q_1, a, aZ_0) \vdash (q_1, \epsilon, Z_0) \vdash (q_2, \epsilon, Z_0)$$

---

### Problem 2.3: PDA for $L = \{a^n b^m \mid n \ne m\}$
> **[TEE Section A: 6 Marks (Part a)] / [TEE Section B: 8 Marks]**:  
> Construct a Non-Deterministic Pushdown Automaton (NPDA) for the language $L = \{a^n b^m \mid n \ne m, n, m \ge 1\}$.

#### Model Solution:
* **Decomposition**: $L = \{a^n b^m \mid n > m\} \cup \{a^n b^m \mid n < m\}$.
* **Design Logic**:
  - Push all $a$'s onto the stack in $q_0$.
  - On seeing $b$, move to $q_1$ and pop an $a$ for each $b$.
  - **Case 1 ($n > m$)**: Input is exhausted ($\epsilon$), but the stack still has leftover $a$'s! Transition to final state $q_2$ and empty stack.
  - **Case 2 ($n < m$)**: Stack is exhausted (shows $Z_0$), but there are still $b$'s remaining in the input! Transition to state $q_3$, consume leftover $b$'s, and then accept in final state $q_4$.
* **Transitions**:
  1. $\delta(q_0, a, Z_0) = \{(q_0, a Z_0)\}, \quad \delta(q_0, a, a) = \{(q_0, aa)\}$
  2. $\delta(q_0, b, a) = \{(q_1, \epsilon)\}$
  3. $\delta(q_1, b, a) = \{(q_1, \epsilon)\}$
  4. *Case $n > m$*: $\delta(q_1, \epsilon, a) = \{(q_2, \epsilon)\}, \quad \delta(q_2, \epsilon, a) = \{(q_2, \epsilon)\}, \quad \delta(q_2, \epsilon, Z_0) = \{(q_{\text{final}}, Z_0)\}$
  5. *Case $n < m$*: $\delta(q_1, b, Z_0) = \{(q_3, Z_0)\}, \quad \delta(q_3, b, Z_0) = \{(q_3, Z_0)\}, \quad \delta(q_3, \epsilon, Z_0) = \{(q_{\text{final}}, Z_0)\}$

---

### Problem 2.4: Deterministic Pushdown Automata (DPDA) for Equal $a$'s and $b$'s
> **[TEE Section B: 8 Marks (Standalone - No Subparts)]**:  
> Explain Deterministic Context-Free Languages (DCFL). Construct a DPDA for strings over $\{a, b\}$ having an equal number of $a$'s and $b$'s.

#### Model Solution:
* **Definition of DPDA**: A PDA where at most one transition is possible for any state, input symbol, and stack top:
  $$|\delta(q, a, X)| + |\delta(q, \epsilon, X)| \le 1$$
* **Logic for Equal $a$'s and $b$'s**:
  - The stack maintains the **excess count** of whichever symbol is currently leading:
    - If stack holds $Z_0$ and input is $a$: push $a$.
    - If stack holds $Z_0$ and input is $b$: push $b$.
    - If stack holds $a$ and input is $a$: push $a$.
    - If stack holds $a$ and input is $b$: pop $a$ (cancels one excess $a$).
    - If stack holds $b$ and input is $b$: push $b$.
    - If stack holds $b$ and input is $a$: pop $b$ (cancels one excess $b$).
  - At the end of input ($\epsilon$), if stack top is $Z_0$, the counts were equal $\implies$ accept in final state $q_f$.

---

### Problem 2.5: Leftmost Derivation (LMD), Rightmost Derivation (RMD) & Parse Trees
> **[TEE Section A: 6 Marks (Part b)] / [TEE Section B: 8 Marks]**:  
> Given Grammar $G$:  
> $$E \to E + E \mid E * E \mid (E) \mid id$$  
> Derive string $w = id + id * id$ using: (a) Leftmost Derivation, (b) Rightmost Derivation, (c) Draw Parse Tree, (d) State whether $G$ is ambiguous.

#### Model Solution:
* **(a) Leftmost Derivation (LMD)** (Always expands the leftmost non-terminal):
  $$E \implies \mathbf{E} + E \implies id + \mathbf{E} \implies id + \mathbf{E} * E \implies id + id * \mathbf{E} \implies id + id * id$$
* **(b) Rightmost Derivation (RMD)** (Always expands the rightmost non-terminal):
  $$E \implies E + \mathbf{E} \implies E + E * \mathbf{E} \implies E + \mathbf{E} * id \implies \mathbf{E} + id * id \implies id + id * id$$
* **(c) Parse Tree**:
  ```text
          E
        / | \
       E  +  E
       |    /|\
      id   E * E
           |   |
          id  id
  ```
* **(d) Ambiguity Proof**:
  We can also construct an alternative LMD:
  $$E \implies \mathbf{E} * E \implies \mathbf{E} + E * E \implies id + id * id$$
  Since the string $id + id * id$ yields **two distinct parse trees** (one with $+$ at root, another with $*$ at root), grammar $G$ is **AMBIGUOUS**.

---

### Problem 2.6: The Chomsky Hierarchy of Languages & Automata
> **[TEE Section B: 8 Marks (Standalone - No Subparts)]**:  
> Explain the Chomsky Hierarchy with grammar production constraints, language classes, and recognizing automata.

| Type | Language Class | Grammar Production Format | Automaton Model | Real-world Use |
|:---:|:---|:---|:---|:---|
| **Type 3** | **Regular Languages** | $A \to aB \mid a$ (Right-Linear) or $A \to Ba \mid a$ (Left-Linear) | **Finite Automata (DFA/NFA)** | Lexical analyzers, regex, tokens |
| **Type 2** | **Context-Free Languages (CFL)** | $A \to \alpha$ where $A \in V_N$, $\alpha \in (V_N \cup \Sigma)^*$ | **Pushdown Automata (PDA)** | Programming syntax, compilers |
| **Type 1** | **Context-Sensitive Languages (CSL)** | $\alpha \to \beta$ where $|\alpha| \le |\beta|$ (Non-contracting) | **Linear Bounded Automata (LBA)** | Natural language syntax, types |
| **Type 0** | **Recursively Enumerable (RE)** | $\alpha \to \beta$ where $\alpha \in (V_N \cup \Sigma)^+$ (Unrestricted) | **Turing Machine (TM)** | Universal general computation |

$$\text{Type 3} \subset \text{Type 2} \subset \text{Type 1} \subset \text{Type 0}$$

---

### Problem 2.7: Conversion of Pushdown Automata (PDA) to Context-Free Grammar (CFG)
> **[TEE Section B: 8 Marks (Standalone - No Subparts)] / [TEE Section A: 6 Marks (Part a/b)]**:  
> Systematically convert a given Pushdown Automaton (PDA) accepting by empty stack into an equivalent Context-Free Grammar (CFG).

#### 📌 Theoretical Framework & Standard Conversion Rules
Given a PDA $M = (Q, \Sigma, \Gamma, \delta, q_0, Z_0, \emptyset)$ accepting by empty store, the equivalent CFG $G = (V_N, \Sigma, P, S)$ is constructed as follows:
- **Variables / Non-Terminals ($V_N$)**:
  - Start symbol $S$
  - Composite tri-bracket variables: $[q, X, p]$ where $q, p \in Q$ and $X \in \Gamma$.  
    *Interpretation*: $[q, X, p]$ derives all strings $w \in \Sigma^*$ that cause the PDA to transition from state $q$ to state $p$ while net-popping symbol $X$ off the stack for the first time.

##### Rule 1: Start Symbol Productions
For every state $q \in Q$:
$$S \to [q_0, Z_0, q]$$

##### Rule 2: Pop Transitions ($k = 0$)
If $\delta(q, a, X)$ contains $(p, \epsilon)$ where $a \in \Sigma \cup \{\epsilon\}$:
$$[q, X, p] \to a$$

##### Rule 3: Push / Multi-symbol Transitions ($k \ge 1$)
If $\delta(q, a, X)$ contains $(p, Y_1 Y_2 \dots Y_k)$ where $a \in \Sigma \cup \{\epsilon\}$ and $k \ge 1$:
For **every possible sequence of states** $r_1, r_2, \dots, r_k \in Q$:
$$[q, X, r_k] \to a \; [p, Y_1, r_1] \; [r_1, Y_2, r_2] \; [r_2, Y_3, r_3] \dots [r_{k-1}, Y_k, r_k]$$

---

#### 📝 Solved Question 1 (from `tee_imp.txt`)
> **Given PDA Transitions**:  
> 1. $\delta(q_0, a, Z_0) = \{(q_1, X Z_0)\}$  
> 2. $\delta(q_0, b, Y) = \{(q_1, Y)\}$  
> 3. $\delta(q_0, \epsilon, Z_0) = \{(q_1, \epsilon)\}$  
> 
> *States*: $Q = \{q_0, q_1\}$, *Alphabet*: $\Sigma = \{a, b\}$, *Stack Alphabet*: $\Gamma = \{X, Y, Z_0\}$, *Start State*: $q_0$, *Start Stack*: $Z_0$.

##### Step 1: Start Symbol Productions (Rule 1)
Since $Q = \{q_0, q_1\}$, start symbol $S$ expands to:
$$S \to [q_0, Z_0, q_0] \mid [q_0, Z_0, q_1]$$

##### Step 2: Pop Transition $\delta(q_0, \epsilon, Z_0) = \{(q_1, \epsilon)\}$ (Rule 2)
Here $q = q_0, a = \epsilon, X = Z_0, p = q_1$.
$$[q_0, Z_0, q_1] \to \epsilon$$

##### Step 3: Transition $\delta(q_0, b, Y) = \{(q_1, Y)\}$ (Rule 3 with $k = 1$)
Here $q = q_0, a = b, X = Y, p = q_1$, and $Y_1 = Y$.  
For each $r_1 \in \{q_0, q_1\}$:
$$[q_0, Y, r_1] \to b \; [q_1, Y, r_1]$$
- For $r_1 = q_0$: $[q_0, Y, q_0] \to b \; [q_1, Y, q_0]$
- For $r_1 = q_1$: $[q_0, Y, q_1] \to b \; [q_1, Y, q_1]$

##### Step 4: Transition $\delta(q_0, a, Z_0) = \{(q_1, X Z_0)\}$ (Rule 3 with $k = 2$)
Here $q = q_0, a = a, X = Z_0, p = q_1, Y_1 = X, Y_2 = Z_0$.  
For each pair $(r_1, r_2) \in \{q_0, q_1\} \times \{q_0, q_1\}$ ($2 \times 2 = 4$ productions):
$$[q_0, Z_0, r_2] \to a \; [q_1, X, r_1] \; [r_1, Z_0, r_2]$$
- When $r_2 = q_0$:
  1. $r_1 = q_0$: $[q_0, Z_0, q_0] \to a \; [q_1, X, q_0] \; [q_0, Z_0, q_0]$
  2. $r_1 = q_1$: $[q_0, Z_0, q_0] \to a \; [q_1, X, q_1] \; [q_1, Z_0, q_0]$
- When $r_2 = q_1$:
  3. $r_1 = q_0$: $[q_0, Z_0, q_1] \to a \; [q_1, X, q_0] \; [q_0, Z_0, q_1]$
  4. $r_1 = q_1$: $[q_0, Z_0, q_1] \to a \; [q_1, X, q_1] \; [q_1, Z_0, q_1]$

##### Step 5: Analysis & Grammar Simplification
- In this PDA fragment, there are no transitions starting from state $q_1$ ($\delta(q_1, \dots) = \emptyset$).
- Variables $[q_1, X, q_0]$, $[q_1, X, q_1]$, $[q_1, Y, q_0]$, etc., have no productions and are non-generating.
- The only generating production from start is $[q_0, Z_0, q_1] \to \epsilon$.
- **Simplified Grammar**:
  $$S \to [q_0, Z_0, q_1] \implies S \to \epsilon$$

---

#### 📝 Solved Question 2 (from `tee_imp.txt`)
> **Given PDA Transitions**:  
> 1. $\delta(q_0, b, Z_0) = \{(q_1, Y Z_0)\}$  
> 2. $\delta(q_0, a, Y) = \{(q_1, X)\}$  
> 3. $\delta(q_0, \epsilon, Z_0) = \{(q_1, \epsilon)\}$  
> 
> *States*: $Q = \{q_0, q_1\}$, *Alphabet*: $\Sigma = \{a, b\}$, *Stack Alphabet*: $\Gamma = \{X, Y, Z_0\}$, *Start State*: $q_0$, *Start Stack*: $Z_0$.

##### Step 1: Start Symbol Productions (Rule 1)
$$S \to [q_0, Z_0, q_0] \mid [q_0, Z_0, q_1]$$

##### Step 2: Pop Transition $\delta(q_0, \epsilon, Z_0) = \{(q_1, \epsilon)\}$ (Rule 2)
$$[q_0, Z_0, q_1] \to \epsilon$$

##### Step 3: Transition $\delta(q_0, a, Y) = \{(q_1, X)\}$ (Rule 3 with $k = 1$)
Here $q = q_0, a = a, X = Y, p = q_1, Y_1 = X$.  
For each $r_1 \in \{q_0, q_1\}$:
$$[q_0, Y, r_1] \to a \; [q_1, X, r_1]$$
- For $r_1 = q_0$: $[q_0, Y, q_0] \to a \; [q_1, X, q_0]$
- For $r_1 = q_1$: $[q_0, Y, q_1] \to a \; [q_1, X, q_1]$

##### Step 4: Transition $\delta(q_0, b, Z_0) = \{(q_1, Y Z_0)\}$ (Rule 3 with $k = 2$)
Here $q = q_0, a = b, X = Z_0, p = q_1, Y_1 = Y, Y_2 = Z_0$.  
For each pair $(r_1, r_2) \in \{q_0, q_1\} \times \{q_0, q_1\}$ ($2 \times 2 = 4$ productions):
$$[q_0, Z_0, r_2] \to b \; [q_1, Y, r_1] \; [r_1, Z_0, r_2]$$
- When $r_2 = q_0$:
  1. $r_1 = q_0$: $[q_0, Z_0, q_0] \to b \; [q_1, Y, q_0] \; [q_0, Z_0, q_0]$
  2. $r_1 = q_1$: $[q_0, Z_0, q_0] \to b \; [q_1, Y, q_1] \; [q_1, Z_0, q_0]$
- When $r_2 = q_1$:
  3. $r_1 = q_0$: $[q_0, Z_0, q_1] \to b \; [q_1, Y, q_0] \; [q_0, Z_0, q_1]$
  4. $r_1 = q_1$: $[q_0, Z_0, q_1] \to b \; [q_1, Y, q_1] \; [q_1, Z_0, q_1]$

##### Step 5: Summary of Productions
1. **From Start Symbol**:
   - $S \to [q_0, Z_0, q_0]$
   - $S \to [q_0, Z_0, q_1]$
2. **From Pop Action**:
   - $[q_0, Z_0, q_1] \to \epsilon$
3. **From Replacing $Y$ with $X$**:
   - $[q_0, Y, q_0] \to a [q_1, X, q_0]$
   - $[q_0, Y, q_1] \to a [q_1, X, q_1]$
4. **From Pushing $Y Z_0$**:
   - $[q_0, Z_0, q_0] \to b [q_1, Y, q_0] [q_0, Z_0, q_0]$
   - $[q_0, Z_0, q_0] \to b [q_1, Y, q_1] [q_1, Z_0, q_0]$
   - $[q_0, Z_0, q_1] \to b [q_1, Y, q_0] [q_0, Z_0, q_1]$
   - $[q_0, Z_0, q_1] \to b [q_1, Y, q_1] [q_1, Z_0, q_1]$

*(Total: $2 + 1 + 2 + 4 = 9$ productions in the unreduced CFG!)*

---

# 3. TURING MACHINES & COMPUTABILITY THEORY

---

### Problem 3.1: Turing Machine for Equal 0s and 1s (Even 0s and Odd 1s)
> **[TEE Section B: 8 Marks (Standalone - No Subparts)]**:  
> Design a Turing Machine that accepts strings with an **Even number of 0s and Odd number of 1s** over $\Sigma = \{0, 1\}$. Provide the transition table and state diagram.

#### Model Solution (Modulo 2 Parity State Machine):
* **Parity States Representation**:
  - $q_{EE}$: Even 0s, Even 1s (Start State).
  - $q_{EO}$: Even 0s, Odd 1s (**Final Accepting State**).
  - $q_{OE}$: Odd 0s, Even 1s.
  - $q_{OO}$: Odd 0s, Odd 1s.
* **Transition Mechanics**:
  - Scanning from left to right; tape head writes back the same symbol and moves `R`.
  - On reading blank $B$, if in state $q_{EO}$, transition to final state $q_{\text{accept}}$.
* **Transition Table**:
  | State | Symbol: `0` | Symbol: `1` | Symbol: `B` (Blank) |
  | :---: | :---: | :---: | :---: |
  | **→ $q_{EE}$** | $(q_{OE}, 0, R)$ | $(q_{EO}, 1, R)$ | Halt & Reject |
  | *** $q_{EO}$** | $(q_{OO}, 0, R)$ | $(q_{EE}, 1, R)$ | **$(q_{\text{accept}}, B, R)$ [Accept]** |
  | **$q_{OE}$** | $(q_{EE}, 0, R)$ | $(q_{OO}, 1, R)$ | Halt & Reject |
  | **$q_{OO}$** | $(q_{EO}, 0, R)$ | $(q_{OE}, 1, R)$ | Halt & Reject |

---

### Problem 3.2: Turing Machine for $L = \{a^n b^{2n} \mid n \ge 1\}$
> **[TEE Section A: 12 Marks (Full Question with 6-Part Layout & Trace)]**:  
> Design a Turing Machine for $L = \{a^n b^{2n} \mid n \ge 1\}$. Provide complete 6-Part model solution.

#### Model Solution:
* **Part 1: Language**: $L = \{abb, aabbbb, aaabbbbbb, \dots\}$
* **Part 2: Design Logic**:
  - For each $a$ replaced with $X$ on the left:
  - Traverse rightwards past all $a$'s and existing $Y$'s to find and replace **two consecutive $b$'s** with $Y$.
  - Return left past $Y$'s and $a$'s until $X$ is hit; step right to pick next $a$.
  - When no more $a$'s remain, verify that only $Y$'s and blank $B$ remain on tape.
* **Part 3: Formal Tuples**:
  $$M = (Q, \Sigma, \Gamma, \delta, q_0, B, F)$$
  where $Q = \{q_0, q_1, q_2, q_3, q_4, q_5\}$, $\Sigma = \{a, b\}$, $\Gamma = \{a, b, X, Y, B\}$, $F = \{q_5\}$.
* **Part 4: Transition Table ($\delta$)**:
  | State | Input: $a$ | Input: $b$ | Input: $X$ | Input: $Y$ | Input: $B$ |
  | :---: | :---: | :---: | :---: | :---: | :---: |
  | **→ $q_0$** | $(q_1, X, R)$ | — | — | $(q_4, Y, R)$ | — |
  | **$q_1$** | $(q_1, a, R)$ | $(q_2, Y, R)$ | — | $(q_1, Y, R)$ | — |
  | **$q_2$** | — | $(q_3, Y, L)$ | — | $(q_2, Y, R)$ | — |
  | **$q_3$** | $(q_3, a, L)$ | — | $(q_0, X, R)$ | $(q_3, Y, L)$ | — |
  | **$q_4$** | — | — | — | $(q_4, Y, R)$ | **$(q_5, B, R)$** |
  | *** $q_5$** | — | — | — | — | — |

* **Part 5: Instantaneous Description Trace for $w = abb$**:
  $$\begin{aligned}
  q_0 abb &\vdash X q_1 bb \vdash X Y q_2 b \vdash X q_3 Y Y \vdash q_3 X Y Y \vdash X q_0 Y Y \\
  &\vdash X Y q_4 Y \vdash X Y Y q_4 B \vdash X Y Y B q_5 \quad \text{[Accepted in state } q_5 \in F\text{]}
  \end{aligned}$$

---

### Problem 3.3: Turing Machine for Unary Addition ($0^m 1 0^n \to 0^{m+n}$)
> **[TEE Section A: 6 Marks (Part a)] / [TEE Section B: 8 Marks]**:  
> Design a Turing Machine that performs addition of two unary integers: takes tape input $0^m 1 0^n$ and produces $0^{m+n}$ on the tape.

#### Model Solution:
* **Concept**:
  - Initial tape: $\underline{0} 0 \dots 0 1 0 0 \dots 0 B$
  - The separator symbol is $1$.
  - Strategy: Convert the first $0$ to blank $B$, move to the $1$, replace $1$ with $0$, then move to the end of the second block and erase the last $0$ (replace with $B$).
  - Net effect: $m + 1 + n - 1 - 1 = m + n$ zeros!
* **Transitions**:
  1. $q_0$: Read $0$, replace with $B$, move $R \to q_1$.
  2. $q_1$: Read $0$, keep $0$, move $R \to q_1$. Read $1$, replace with $0$, move $R \to q_2$.
  3. $q_2$: Read $0$, keep $0$, move $R \to q_2$. Read $B$, keep $B$, move $L \to q_3$.
  4. $q_3$: Read $0$, replace with $B$, move $R \to q_4$ (Halt/Accept).

---

### Problem 3.4: Decidability, Recursive vs. Recursively Enumerable & Complement Property
> **[TEE Section A: 6 Marks (Part b)] / [TEE Section B: 8 Marks (Standalone)]**:  
> (a) Differentiate between Recursive (Decidable) and Recursively Enumerable (Semi-Decidable) Languages.  
> (b) State and explain the Complement Property of Recursive Languages.

#### Model Solution:
1. **Recursive vs. Recursively Enumerable**:
   - **Recursive Language ($L_{\text{REC}}$)**: A language for which there exists a Turing Machine (Halting Turing Machine / Algorithm) that **always halts** on every input string $w$. If $w \in L$, it halts in state $q_{\text{accept}}$; if $w \notin L$, it halts in state $q_{\text{reject}}$. $\implies$ **Decidable**.
   - **Recursively Enumerable ($L_{\text{RE}}$)**: A language for which a Turing Machine halts and accepts if $w \in L$. However, if $w \notin L$, the machine **may either halt and reject OR loop indefinitely**. $\implies$ **Semi-Decidable / Undecidable**.
2. **Complement Property Theorem**:
   > **Theorem**: If language $L$ is Recursive, then its complement $\overline{L} = \Sigma^* \setminus L$ is also Recursive.
   - **Explanation**: Let $M$ be the decider TM for $L$. To construct a decider $\overline{M}$ for $\overline{L}$:
     - Run $M$ on input $w$. Since $M$ is a decider, it is guaranteed to halt in finite steps.
     - Swap the output states: If $M$ accepts, $\overline{M}$ **rejects**. If $M$ rejects, $\overline{M}$ **accepts**.
     - Since $\overline{M}$ always halts and correctly inverts the decision, $\overline{L}$ is **Recursive**.

---

# 4. COMPILER DESIGN: PARSING, SYNTAX TREES & THREE-ADDRESS CODE

---

### Problem 4.1: FIRST and FOLLOW Set Computation
> **[TEE Section A: 6 Marks (Part a)] / [TEE Section B: 8 Marks]**:  
> Compute the `FIRST` and `FOLLOW` sets for the following grammar:  
> $$E \to T E'$$  
> $$E' \to + T E' \mid \epsilon$$  
> $$T \to F T'$$  
> $$T' \to * F T' \mid \epsilon$$  
> $$F \to ( E ) \mid id$$

#### Step-by-Step Model Solution:
* **Rules for FIRST**:
  1. If $X$ is terminal, $\text{FIRST}(X) = \{X\}$.
  2. If $X \to \epsilon$, add $\epsilon$ to $\text{FIRST}(X)$.
  3. If $X \to Y_1 Y_2 \dots Y_k$, add $\text{FIRST}(Y_1) \setminus \{\epsilon\}$. If $Y_1 \implies^* \epsilon$, add $\text{FIRST}(Y_2)$, etc.
* **FIRST Sets**:
  - $\text{FIRST}(F) = \{(, id\}$
  - $\text{FIRST}(T') = \{*, \epsilon\}$
  - $\text{FIRST}(T) = \text{FIRST}(F) = \{(, id\}$
  - $\text{FIRST}(E') = \{+, \epsilon\}$
  - $\text{FIRST}(E) = \text{FIRST}(T) = \{(, id\}$

* **Rules for FOLLOW**:
  1. Add `$` to $\text{FOLLOW}(S)$ where $S$ is start symbol.
  2. If $A \to \alpha B \beta$, add $\text{FIRST}(\beta) \setminus \{\epsilon\}$ to $\text{FOLLOW}(B)$.
  3. If $A \to \alpha B$ or $A \to \alpha B \beta$ where $\beta \implies^* \epsilon$, add $\text{FOLLOW}(A)$ to $\text{FOLLOW}(B)$.
* **FOLLOW Sets**:
  - $\text{FOLLOW}(E) = \{\$, )\}$ (Rule 1 for $\$$; from $F \to (E)$, `)` follows $E$).
  - $\text{FOLLOW}(E') = \text{FOLLOW}(E) = \{\$, )\}$.
  - $\text{FOLLOW}(T)$: From $E \to T E'$, add $\text{FIRST}(E') \setminus \{\epsilon\} = \{+\}$. Since $E' \to \epsilon$, also add $\text{FOLLOW}(E) = \{\$, )\}$. $\implies \mathbf{\{+, \$, )\}}$
  - $\text{FOLLOW}(T') = \text{FOLLOW}(T) = \{+, \$, )\}$.
  - $\text{FOLLOW}(F)$: From $T \to F T'$, add $\text{FIRST}(T') \setminus \{\epsilon\} = \{*\}$. Since $T' \to \epsilon$, add $\text{FOLLOW}(T) = \{+, \$, )\}$. $\implies \mathbf{\{*, +, \$, )\}}$

* **Summary Table**:
  | Non-Terminal | FIRST | FOLLOW |
  | :---: | :---: | :---: |
  | $E$ | `{(, id}` | `{$, )}` |
  | $E'$ | `{+, ε}` | `{$, )}` |
  | $T$ | `{(, id}` | `{+, $, )}` |
  | $T'$ | `{*, ε}` | `{+, $, )}` |
  | $F$ | `{(, id}` | `{*, +, $, )}` |

---

### Problem 4.2: Predictive LL(1) Parsing Table Construction & Stack Parsing
> **[TEE Section A: 12 Marks (Full Question with Table & 17-Step Trace)]**:  
> (a) Construct the LL(1) parsing table for the grammar in Problem 4.1.  
> (b) Trace the predictive stack parse for input string $w = id + id * id \$$.

#### (a) LL(1) Parsing Table Construction:
For each production $A \to \alpha$:
- For each terminal $a \in \text{FIRST}(\alpha)$, add $A \to \alpha$ to $M[A, a]$.
- If $\epsilon \in \text{FIRST}(\alpha)$, for each terminal $b \in \text{FOLLOW}(A)$, add $A \to \alpha$ to $M[A, b]$.

| Non-Terminal | `id` | `+` | `*` | `(` | `)` | `$` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$E$** | $E \to T E'$ | | | $E \to T E'$ | | |
| **$E'$** | | $E' \to + T E'$ | | | $E' \to \epsilon$ | $E' \to \epsilon$ |
| **$T$** | $T \to F T'$ | | | $T \to F T'$ | | |
| **$T'$** | | $T' \to \epsilon$ | $T' \to * F T'$ | | $T' \to \epsilon$ | $T' \to \epsilon$ |
| **$F$** | $F \to id$ | | | $F \to (E)$ | | |

*(Since no cell contains more than one production, the grammar is **LL(1)**!)*

#### (b) Stack Parse for $w = id + id * id \$ $:
| Step | Stack | Input | Action |
| :---: | :--- | :--- | :--- |
| 1 | `$ E` | `id + id * id $` | Output: $E \to T E'$ |
| 2 | `$ E' T` | `id + id * id $` | Output: $T \to F T'$ |
| 3 | `$ E' T' F` | `id + id * id $` | Output: $F \to id$ |
| 4 | `$ E' T' id` | `id + id * id $` | **Match `id`** |
| 5 | `$ E' T'` | `+ id * id $` | Output: $T' \to \epsilon$ |
| 6 | `$ E'` | `+ id * id $` | Output: $E' \to + T E'$ |
| 7 | `$ E' T +` | `+ id * id $` | **Match `+`** |
| 8 | `$ E' T` | `id * id $` | Output: $T \to F T'$ |
| 9 | `$ E' T' F` | `id * id $` | Output: $F \to id$ |
| 10 | `$ E' T' id` | `id * id $` | **Match `id`** |
| 11 | `$ E' T'` | `* id $` | Output: $T' \to * F T'$ |
| 12 | `$ E' T' F *` | `* id $` | **Match `*`** |
| 13 | `$ E' T' F` | `id $` | Output: $F \to id$ |
| 14 | `$ E' T' id` | `id $` | **Match `id`** |
| 15 | `$ E' T'` | `$` | Output: $T' \to \epsilon$ |
| 16 | `$ E'` | `$` | Output: $E' \to \epsilon$ |
| 17 | `$` | `$` | **ACCEPT! (Success)** |

---

### Problem 4.3: Stepwise SLR(1) Parsing Table Construction & Shift-Reduce Conflicts
> **[TEE Section A: 12 Marks (Full Question with Collection, Table & Conflict Proof)]**:  
> Given Grammar:  
> $$S \to L = R \mid R$$  
> $$L \to * R \mid id$$  
> $$R \to L$$  
> Show that this grammar is **NOT SLR(1)** by demonstrating a Shift-Reduce conflict in state $I_2$.

#### Model Solution:
1. **Augmented Grammar & $LR(0)$ Items**:
   - (0) $S' \to S$
   - (1) $S \to L = R$
   - (2) $S \to R$
   - (3) $L \to * R$
   - (4) $L \to id$
   - (5) $R \to L$
2. **Compute Canonical Collection of $LR(0)$ Item Sets**:
   - $I_0 = \text{CLOSURE}(\{S' \to \cdot S\})$:
     $$\{S' \to \cdot S, S \to \cdot L = R, S \to \cdot R, L \to \cdot * R, L \to \cdot id, R \to \cdot L\}$$
   - $I_2 = \text{GOTO}(I_0, L)$:
     $$\mathbf{I_2 = \{S \to L \cdot = R, \quad R \to L \cdot\}}$$
3. **Analyze State $I_2$ for Conflicts**:
   - Item $S \to L \cdot = R$: Dot is before terminal `=`, indicating a **SHIFT action** on `=` ($s_6$).
   - Item $R \to L \cdot$: Dot is at the end, indicating a **REDUCE action** by rule (5) ($R \to L$).
   - In an SLR(1) parser, the reduce action $R \to L$ is placed in all columns of $\text{FOLLOW}(R)$.
4. **Compute $\text{FOLLOW}(R)$**:
   - From $S \to L = R$, $\text{FOLLOW}(R)$ contains $\text{FOLLOW}(S) = \{\$\}$.
   - From $S \to L = R$, since $R \to L$, `=` can follow $R$. Therefore, **`=` $\in \text{FOLLOW}(R)$!**
5. **The Shift-Reduce Conflict**:
   - In row $I_2$ and column `=`:
     - Shift action: `s6` (from $S \to L \cdot = R$)
     - Reduce action: `r5` (from $R \to L \cdot$ since `=` $\in \text{FOLLOW}(R)$)
   - Cell $M[I_2, =]$ contains **BOTH $\{s6, r5\}$**!
   - $\therefore$ The grammar has a **Shift-Reduce Conflict** and is **NOT SLR(1)**! `[Full 12 Marks]`

---

### Problem 4.4: Canonical LR (CLR(1)) vs. LALR(1) & Reduce-Reduce Conflicts
> **[TEE Section B: 8 Marks (Standalone - No Subparts)]**:  
> Why does merging states in LALR(1) never introduce a Shift-Reduce conflict, but may introduce a Reduce-Reduce conflict?

#### Model Solution:
* **Why No Shift-Reduce Conflict**:
  - Suppose two CLR(1) states $I_i$ and $I_j$ have identical cores:
    $$I_i = \{A \to \alpha \cdot a \beta, c\}, \quad I_j = \{A \to \alpha \cdot a \beta, d\}$$
  - Merged state: $\{A \to \alpha \cdot a \beta, c / d\}$.
  - The shift action depends **strictly on the next terminal $a$ following the dot** (the core), NOT on the lookahead! Since both states had the exact same core, merging them cannot introduce any new terminal to shift on. Thus, **Shift-Reduce conflicts are IMPOSSIBLE**.
* **Why Reduce-Reduce Conflicts CAN Occur**:
  - Suppose $I_i$ has items: $\{A \to \alpha \cdot, a\}$ and $\{B \to \beta \cdot, b\}$. (No conflict in $I_i$ because lookaheads $a \ne b$).
  - Suppose $I_j$ has items: $\{A \to \alpha \cdot, b\}$ and $\{B \to \beta \cdot, a\}$. (No conflict in $I_j$ because lookaheads $b \ne a$).
  - When merged:
    $$I_{ij} = \{A \to \alpha \cdot, a / b\}, \quad \{B \to \beta \cdot, a / b\}$$
  - On input $a$: the parser must reduce by BOTH $A \to \alpha$ and $B \to \beta$!
  - On input $b$: the parser must reduce by BOTH $A \to \alpha$ and $B \to \beta$!
  - A fatal **Reduce-Reduce conflict** is created.

---

### Problem 4.5: Directed Acyclic Graph (DAG) for Expression $E = (a + b) \wedge c + (c + d)$
> **[TEE Section A: 6 Marks (Part a)] / [TEE Section B: 8 Marks]**:  
> Construct the Directed Acyclic Graph (DAG) and 3-Address Code for expression:  
> $$E = (a + b) \wedge c + (c + d)$$  
> Highlight node sharing and explain optimization benefits.

#### Model Solution:
1. **Three Address Code (TAC)**:
   - $t_1 = a + b$
   - $t_2 = t_1 \wedge c$
   - $t_3 = c + d$
   - $t_4 = t_2 + t_3$
2. **DAG Construction & Node Sharing**:
   - In an Abstract Syntax Tree (AST), variable `c` would appear twice as two independent leaf nodes.
   - In a **DAG**, subexpression/variable `c` is created **once** and shared by both operators `^` and `+`:

```text
               (+) [t4 - Root Output]
              /   \
            (^)   (+) [t3]
           /   \  / \
         (+)   (c)  (d)
        /   \
      (a)   (b)
```

3. **Optimization Rationale**:
   - Identifies that variable `c` needs to be loaded into a CPU register only **once**.
   - Reduces register pressure and eliminates duplicate memory bus read cycles.

---

### Problem 4.6: TAC, Quadruples, Triples & Indirect Triples for Loops with Arrays
> **[TEE Section A: 12 Marks (Full Question: TAC + Quadruple + Triple + Indirect Triple)]**:  
> Translate the following while loop into Three-Address Code, Quadruples, Triples, and Indirect Triples:
> ```c
> i = 1;
> while (i < 10) {
>     a[i] = 0;
>     i = i + 1;
> }
> ```

#### (a) Three-Address Code (TAC):
*(Assuming 4 bytes per integer element)*:
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

#### (b) Quadruples Representation:
| Index | `op` | `arg1` | `arg2` | `result` |
| :---: | :---: | :---: | :---: | :---: |
| **(0)** | `=` | `1` | — | `i` |
| **(1)** | `>=` | `i` | `10` | `t0` |
| **(2)** | `if_true` | `t0` | — | `(8)` *(goto L2)* |
| **(3)** | `*` | `i` | `4` | `t1` |
| **(4)** | `[]=` | `0` | — | `a[t1]` |
| **(5)** | `+` | `i` | `1` | `t2` |
| **(6)** | `=` | `t2` | — | `i` |
| **(7)** | `goto` | — | — | `(1)` *(goto L1)* |

#### (c) Triples Representation:
| Index | `op` | `arg1` | `arg2` |
| :---: | :---: | :---: | :---: |
| **(0)** | `=` | `i` | `1` |
| **(1)** | `>=` | `i` | `10` |
| **(2)** | `if_true` | `(1)` | `(8)` |
| **(3)** | `*` | `i` | `4` |
| **(4)** | `[]=` | `a[(3)]`| `0` |
| **(5)** | `+` | `i` | `1` |
| **(6)** | `=` | `i` | `(5)` |
| **(7)** | `goto` | `(1)` | — |

#### (d) Indirect Triples Representation:
Contains an array of pointers pointing to the Triples table:
| Pointers Array | Points To Triple |
| :---: | :---: |
| `statement[0]` | `(0)` |
| `statement[1]` | `(1)` |
| `statement[2]` | `(2)` |
| `statement[3]` | `(3)` |
| `statement[4]` | `(4)` |
| `statement[5]` | `(5)` |
| `statement[6]` | `(6)` |
| `statement[7]` | `(7)` |

*Advantage of Indirect Triples*: Optimizing or reordering instructions only requires swapping entries in the `statement` pointer array without modifying physical triple records!

---

### Problem 4.7: Code Optimization Techniques & Target Machine Code Generation
> **[TEE Section B: 8 Marks (Standalone - No Subparts)]**:  
> Explain the primary machine-independent code optimization techniques with before-and-after code snippets.

#### Model Solution:
1. **Constant Folding & Constant Propagation**:
   - *Folding*: Compute compile-time constants:
     ```text
     x = 3.14159 * 2;  ==>  x = 6.28318;
     ```
   - *Propagation*: Replace variable uses with known constant values:
     ```text
     pi = 3.14; r = 5; area = pi * r * r;  ==>  area = 3.14 * 5 * 5;
     ```
2. **Common Subexpression Elimination (CSE)**:
   - Avoid recalculating identical values:
     ```text
     // Before
     t1 = a + b;
     x = t1 * c;
     t2 = a + b;
     y = t2 * d;

     // After (Eliminates redundant addition)
     t1 = a + b;
     x = t1 * c;
     y = t1 * d;
     ```
3. **Dead Code Elimination**:
   - Remove statements computing values that are never read:
     ```text
     // Before
     debug = 0;
     if (debug) { print_logs(); }  // Dead code removed completely!
     ```
4. **Loop-Invariant Code Motion (Hoisting)**:
   - Move computations that do not change across loop iterations outside the loop header:
     ```text
     // Before
     while (i < n) {
         x = 2 * pi;  // Constant inside loop!
         a[i] = x * i;
         i++;
     }

     // After
     x = 2 * pi;      // Hoisted outside
     while (i < n) {
         a[i] = x * i;
         i++;
     }
     ```
5. **Strength Reduction**:
   - Replace computationally expensive operations (multiplication/division) with cheaper ones (shifts/additions):
     ```text
     x = y * 8;   ==>  x = y << 3;   // Shift left by 3 bits
     x = y * 2;   ==>  x = y + y;    // Addition instead of multiplication
     ```
