# 🎯 TOC & Compiler Design: Official Question Bank Master Solutions

> **Course**: CSE2004 — Theory of Computation and Compiler Design  
> **Faculty**: Dr. Gaurav Soni | **Slot**: A11+A12+A13 | **Exam Date**: October 15, 2026 (01:15 PM – 04:15 PM)  
> **Source Material**: Official Module 1–5 Practice Question Banks (`Module-1 Practice Questions.pdf` to `Module-5 Practice questions.pdf`).  
> **Companion Document**: Complements [08-tee-imp-solved-master-solutions.md](./08-tee-imp-solved-master-solutions.md) to give 100% complete coverage of all official question bank problems.

---

## 📑 TABLE OF CONTENTS

1. [MODULE 1: Automata Minimization, Regular Grammars & Lexical Tokens](#1-module-1-automata-minimization-regular-grammars--lexical-tokens)
   - [Problem M1.1: DFA Minimization using Myhill-Nerode / Table-Filling Algorithm](#problem-m11-dfa-minimization-using-myhill-nerode--table-filling-algorithm)
   - [Problem M1.2: Pumping Lemma Proofs for Non-Regularity (0^k 1^k, ww, and a^p for prime p)](#problem-m12-pumping-lemma-proofs-for-non-regularity)
   - [Problem M1.3: Conversion of Finite Automata to Regular Expression using State Elimination](#problem-m13-conversion-of-finite-automata-to-regular-expression-using-state-elimination)
   - [Problem M1.4: Token Specification & Transition Diagrams for Lexical Analysis](#problem-m14-token-specification--transition-diagrams-for-lexical-analysis)
   - [Problem M1.5: LEX Program Implementation as DFA](#problem-m15-lex-program-implementation-as-dfa)
2. [MODULE 2: Normal Forms (CNF/GNF), PDA Variations & CFL Pumping Lemma](#2-module-2-normal-forms-cnfgnf-pda-variations--cfl-pumping-lemma)
   - [Problem M2.1: Simplification of CFG (Null, Unit & Useless Productions)](#problem-m21-simplification-of-cfg)
   - [Problem M2.2: Conversion of CFG to Chomsky Normal Form (CNF)](#problem-m22-conversion-of-cfg-to-chomsky-normal-form-cnf)
   - [Problem M2.3: Conversion of CFG to Greibach Normal Form (GNF)](#problem-m23-conversion-of-cfg-to-greibach-normal-form-gnf)
   - [Problem M2.4: Pushdown Automata for L = {a^(2n) b^n} and L = {a^n b^(2n)}](#problem-m24-pushdown-automata-for-unequal-powers)
   - [Problem M2.5: PDA for Even-Length Palindromes L = {ww^R} (NPDA)](#problem-m25-pda-for-even-length-palindromes)
   - [Problem M2.6: Direct Conversion of CFG to PDA (Top-Down Single State)](#problem-m26-direct-conversion-of-cfg-to-pda)
   - [Problem M2.7: Pumping Lemma Proof for Non-CFL (L = {a^n b^n c^n})](#problem-m27-pumping-lemma-proof-for-non-cfl)
3. [MODULE 3: Syntax Analysis, LR(0), CLR(1) & LALR(1) Parsers](#3-module-3-syntax-analysis-lr0-clr1--lalr1-parsers)
   - [Problem M3.1: Elimination of Left Recursion (Direct & Indirect)](#problem-m31-elimination-of-left-recursion)
   - [Problem M3.2: Left Factoring on Branching Grammars](#problem-m32-left-factoring-on-branching-grammars)
   - [Problem M3.3: Stepwise LR(0) Parsing Table Construction](#problem-m33-stepwise-lr0-parsing-table-construction)
   - [Problem M3.4: Canonical LR (CLR(1)) Parsing Table Construction](#problem-m34-canonical-lr-clr1-parsing-table-construction)
   - [Problem M3.5: LALR(1) Parsing Table Construction via State Merging](#problem-m35-lalr1-parsing-table-construction-via-state-merging)
   - [Problem M3.6: Proof that a Grammar is LR(1) but NOT LALR(1)](#problem-m36-proof-that-a-grammar-is-lr1-but-not-lalr1)
4. [MODULE 4: Turing Machines, Computability & Decidability](#4-module-4-turing-machines-computability--decidability)
   - [Problem M4.1: Turing Machine for L = {a^n b^n c^n} (Full 6-Part Layout & Trace)](#problem-m41-turing-machine-for-an-bn-cn)
   - [Problem M4.2: Turing Machine for Binary Palindromes over {0, 1}*](#problem-m42-turing-machine-for-binary-palindromes)
   - [Problem M4.3: Turing Machine for Proper Subtraction m - n](#problem-m43-turing-machine-for-proper-subtraction)
   - [Problem M4.4: Undecidability Proof of the Halting Problem via Diagonalization](#problem-m44-undecidability-proof-of-the-halting-problem)
   - [Problem M4.5: Post Correspondence Problem (PCP) Verification & Domino Search](#problem-m45-post-correspondence-problem-pcp)
   - [Problem M4.6: Theorem Proof: L and L-bar are both RE implies L is Recursive](#problem-m46-theorem-proof-re-and-complement-re-implies-recursive)
5. [MODULE 5: Intermediate Code Generation, DAGs & Code Optimization](#5-module-5-intermediate-code-generation-dags--code-optimization)
   - [Problem M5.1: Three-Address Code for Complex If-Else and Short-Circuit Booleans](#problem-m51-three-address-code-for-complex-if-else)
   - [Problem M5.2: Three-Address Code for Loops & Array Address Calculations](#problem-m52-three-address-code-for-loops--array-address-calculations)
   - [Problem M5.3: Directed Acyclic Graph (DAG) for Basic Blocks with Array Index Sharing](#problem-m53-directed-acyclic-graph-dag-for-basic-blocks)
   - [Problem M5.4: Quadruples, Triples and Indirect Triples for Compound Expressions](#problem-m54-quadruples-triples-and-indirect-triples)
   - [Problem M5.5: Syntax Tree and Postfix Notation for Arithmetic Expressions](#problem-m55-syntax-tree-and-postfix-notation)
   - [Problem M5.6: Target Code Generation (8086 / Register Machine Assembly)](#problem-m56-target-code-generation)

---

# 1. MODULE 1: Automata Minimization, Regular Grammars & Lexical Tokens

---

### Problem M1.1: DFA Minimization using Myhill-Nerode / Table-Filling Algorithm
> **[Module 1 Q-Bank Q4(a) - 12 Marks / 8 Marks]**:  
> Build the minimal DFA equivalent to the following 5-state DFA:  
> States: $Q = \{A, B, C, D, E\}$, Alphabet: $\Sigma = \{0, 1\}$, Start State: $A$, Final States: $F = \{D, E\}$.  
> Transition Function:  
> - $\delta(A, 0) = B, \quad \delta(A, 1) = C$  
> - $\delta(B, 0) = D, \quad \delta(B, 1) = C$  
> - $\delta(C, 0) = B, \quad \delta(C, 1) = E$  
> - $\delta(D, 0) = D, \quad \delta(D, 1) = E$  
> - $\delta(E, 0) = D, \quad \delta(E, 1) = E$

#### Model Solution:

#### Step 1: Eliminate Unreachable States
- Trace reachability from Start State $A$:
  - $A \xrightarrow{0} B, \quad A \xrightarrow{1} C$
  - From $B$: $B \xrightarrow{0} D$
  - From $C$: $C \xrightarrow{1} E$
- All 5 states $\{A, B, C, D, E\}$ are reachable from $A$. No states removed.

#### Step 2: Initialize Table-Filling Matrix
- Construct lower-triangular pairs $(p, q)$ for all distinct states.
- **Rule 1 (Base Distinction)**: If one state is Final ($D, E$) and the other is Non-Final ($A, B, C$), mark the pair with $\times$ (distinguishable in 0 steps / $\epsilon$).
  - Marked initially:
    - $(A, D), (A, E)$
    - $(B, D), (B, E)$
    - $(C, D), (C, E)$

```text
Table-Filling Matrix (Initial):
B |   
C |   |   
D | X | X | X |   
E | X | X | X |   
  +---+---+---+---+
    A   B   C   D
```

#### Step 3: Iterative Distinction Check
For every unmarked pair $(p, q)$, check if $(\delta(p, a), \delta(q, a))$ is already marked for any input $a \in \{0, 1\}$:

1. **Pair $(D, E)$ (Both Final)**:
   - On input `0`: $\delta(D, 0) = D, \delta(E, 0) = D \implies (D, D)$ (Identical state).
   - On input `1`: $\delta(D, 1) = E, \delta(E, 1) = E \implies (E, E)$ (Identical state).
   - $\implies (D, E)$ CANNOT be distinguished on any input string! Pair $(D, E)$ remains **UNMARKED (Equivalent)**.

2. **Pair $(A, B)$**:
   - On input `0`: $\delta(A, 0) = B, \delta(B, 0) = D \implies$ pair $(B, D)$ is marked $\times$!
   - $\therefore$ Mark $(A, B)$ with $\times$.

3. **Pair $(A, C)$**:
   - On input `1`: $\delta(A, 1) = C, \delta(C, 1) = E \implies$ pair $(C, E)$ is marked $\times$!
   - $\therefore$ Mark $(A, C)$ with $\times$.

4. **Pair $(B, C)$**:
   - On input `0`: $\delta(B, 0) = D, \delta(C, 0) = B \implies$ pair $(B, D)$ is marked $\times$!
   - $\therefore$ Mark $(B, C)$ with $\times$.

```text
Table-Filling Matrix (Final):
B | X 
C | X | X 
D | X | X | X 
E | X | X | X | = [EQUIVALENT]
  +---+---+---+---+
    A   B   C   D
```

#### Step 4: Group Equivalent States
- Equivalent partition: $\{D, E\}$ are merged into a single composite state $\{D, E\}$.
- Final partition of minimal states:
  $$P_{\text{min}} = \{ \{A\}, \{B\}, \{C\}, \{D, E\} \}$$

#### Step 5: Transition Table of Minimal DFA
| Minimal State | Input: `0` | Input: `1` | Nature |
| :---: | :---: | :---: | :---: |
| **→ [A]** | [B] | [C] | Start State |
| **[B]** | [D, E] | [C] | Intermediate |
| **[C]** | [B] | [D, E] | Intermediate |
| *** [D, E]** | [D, E] | [D, E] | **Accepting / Final State** |

```text
Minimal DFA Diagram:
          0
       ┌──────┐
       ▼      │
──▶ ([A]) ──1──▶ ([C]) ──1──▶ ((([D,E]))) ↺ 0, 1
      │            ▲            ▲
      0            │            │
      ▼            │ 1          │ 0
    ([B]) ─────────┴────────────┘
```

---

### Problem M1.2: Pumping Lemma Proofs for Non-Regularity
> **[Module 1 Q-Bank Q14 - 8 Marks / 6 Marks]**:  
> State the Pumping Lemma for Regular Languages. Prove that the following languages are NOT regular:  
> (a) $L_1 = \{0^k 1^k \mid k \ge 1\}$  
> (b) $L_2 = \{w w \mid w \in \{a, b\}^*\}$  
> (c) $L_3 = \{a^p \mid p \text{ is a prime number}\}$

#### Model Solution:

#### 1. Formal Statement of Pumping Lemma
If language $L$ is regular, there exists a constant integer $p \ge 1$ (pumping length) such that for any string $w \in L$ with $|w| \ge p$, $w$ can be divided into three substrings $w = xyz$ satisfying:
1. $|y| \ge 1$ (the pumped substring is non-empty)
2. $|xy| \le p$ (the repetition occurs within the first $p$ symbols)
3. For all $i \ge 0$, $x y^i z \in L$.

#### 2. Proof for (a): $L_1 = \{0^k 1^k \mid k \ge 1\}$
- **Assumption**: Assume $L_1$ is regular. Let $p$ be its pumping length.
- **String Choice**: Choose $w = 0^p 1^p \in L_1$. Clearly $|w| = 2p \ge p$.
- **Decomposition**: By condition 2, $|xy| \le p$. Since the first $p$ characters of $w$ are all `0`, substring $y$ must consist **entirely of zeros**:
  $$y = 0^m \quad \text{where } 1 \le m \le p$$
- **Pumping**: Choose $i = 2$ (pumping up):
  $$w' = x y^2 z = 0^{p+m} 1^p$$
- **Contradiction**: In $w'$, the number of zeros is $p + m$, while the number of ones is $p$. Since $m \ge 1$, $p + m \ne p$. Thus $w' \notin L_1$.  
- $\therefore$ By contradiction, $L_1$ is **NOT regular**. `[Q.E.D.]`

#### 3. Proof for (b): $L_2 = \{w w \mid w \in \{a, b\}^*\}$
- **Assumption**: Assume $L_2$ is regular with pumping length $p$.
- **String Choice**: Choose $w = 0^p 1 0^p 1 \in L_2$ (here $w_0 = 0^p 1$).
- **Decomposition**: Since $|xy| \le p$, $y$ lies wholly within the first block of $0$'s: $y = 0^m$ ($1 \le m \le p$).
- **Pumping**: Pump with $i = 2$:
  $$w' = x y^2 z = 0^{p+m} 1 0^p 1$$
- **Contradiction**: For $w'$ to be in $L_2$, it must be decomposable into two identical halves $u u$. The total length is $2p + m + 2$. The first half contains $0^{p+m} 1 \dots$ while the second half starts with fewer zeros. Thus $w' \notin L_2$.  
- $\therefore L_2$ is **NOT regular**. `[Q.E.D.]`

#### 4. Proof for (c): $L_3 = \{a^p \mid p \text{ is prime}\}$
- **Assumption**: Assume $L_3$ is regular with pumping length $p$.
- **String Choice**: Pick a prime $n \ge p$. Choose $w = a^n \in L_3$.
- **Decomposition**: $w = xyz$ where $y = a^m$ ($1 \le m \le p$) and $|x z| = n - m$.
- **Pumping**: Choose pumping index $i = n + 1$:
  $$|x y^{n+1} z| = |xz| + (n + 1)|y| = (n - m) + (n + 1)m = n - m + nm + m = n(1 + m)$$
- **Contradiction**: Since $m \ge 1$, $1 + m > 1$. And since $n \ge 2$, $n(1 + m)$ is the product of two integers $> 1$, meaning $n(1 + m)$ is **COMPOSITE (NOT PRIME)**!  
  Thus $a^{n(1+m)} \notin L_3$.  
- $\therefore L_3$ is **NOT regular**. `[Q.E.D.]`

---

### Problem M1.3: Conversion of Finite Automata to Regular Expression using State Elimination
> **[Module 1 Q-Bank Q13(a) - 8 Marks]**:  
> Derive the regular expression from the following 3-state Automaton:  
> States: $\{q_1, q_2, q_3\}$, Start: $q_1$, Final: $q_3$.  
> Transitions:  
> - $\delta(q_1, 0) = q_1, \quad \delta(q_1, 1) = q_2$  
> - $\delta(q_2, 1) = q_2, \quad \delta(q_2, 0) = q_3$  
> - $\delta(q_3, 0) = q_1, \quad \delta(q_3, 1) = q_2$

#### Model Solution:
- **General Elimination Formula**: When eliminating intermediate state $k$, update edge between state $i$ and state $j$:
  $$R_{ij}^{\text{new}} = R_{ij} + R_{ik} (R_{kk})^* R_{kj}$$

1. **Initial Regular Expressions on Edges**:
   - $R_{11} = 0, \quad R_{12} = 1$
   - $R_{22} = 1, \quad R_{23} = 0$
   - $R_{31} = 0, \quad R_{32} = 1$

2. **Eliminate State $q_2$**:
   - Loop on $q_2$: $R_{22}^* = 1^*$
   - Path $q_1 \to q_2 \to q_3$:
     $$R_{13} = R_{12} (R_{22})^* R_{23} = 1 \cdot 1^* \cdot 0 = 1^+ 0$$
   - Path $q_3 \to q_2 \to q_3$ (New self-loop on $q_3$):
     $$R_{33} = R_{32} (R_{22})^* R_{23} = 1 \cdot 1^* \cdot 0 = 1^+ 0$$
   - Path $q_3 \to q_2 \to q_1$: No direct transition from $q_2$ to $q_1$.
   - Retained edges: $R_{11} = 0, R_{31} = 0$.

3. **Remaining 2-State System $\{q_1, q_3\}$**:
   - $q_1$ has self-loop $0$.
   - $q_1 \to q_3$ with label $1^+ 0$.
   - $q_3 \to q_1$ with label $0$.
   - $q_3$ has self-loop $1^+ 0$.

4. **Eliminate State $q_1$**:
   - Loop on $q_1$: $0^*$.
   - Path from start to $q_3$: $0^* (1^+ 0)$.
   - Feedback loop from $q_3$ through $q_1$ back to $q_3$:
     $$\text{Loop on } q_3 = R_{33} + R_{31} (R_{11})^* R_{13} = 1^+ 0 + 0 \cdot 0^* \cdot (1^+ 0) = (1^+ 0 + 0^+ 1^+ 0)$$
   - Total Regular Expression for accepting state $q_3$:
     $$\mathbf{R = 0^* (1^+ 0) \Big[ 1^+ 0 + 0^+ 1^+ 0 \Big]^*}$$

---

### Problem M1.4: Token Specification & Transition Diagrams for Lexical Analysis
> **[Module 1 Q-Bank Q15 & Q16 - 8 Marks]**:  
> Write formal regular definitions for the following programming language tokens: `keywords (if, then, else)`, `identifier`, `relop`, `num`, `white space (ws)`. Illustrate recognition with transition diagrams.

#### Model Solution:

#### 1. Regular Definitions (Lexical Specifications):
```text
digit       -> [0-9]
digits      -> digit+
optional_fraction -> (. digits)?
optional_exponent -> (E [+-]? digits)?
num         -> digits optional_fraction optional_exponent

letter      -> [A-Za-z_]
id          -> letter (letter | digit)*

relop       -> < | <= | = | <> | > | >=
ws          -> [ 	
]+
keyword     -> if | then | else
```

#### 2. Transition Diagrams for Token Recognition:

1. **Relational Operators (`relop`)**:
```text
          '=' ──────────▶ (( State 1 )) [Return (RELOP, LE)]
        /
──▶ (State 0) ──▶ '>' ──▶ (( State 2 )) [Return (RELOP, NE)]
                  other ────────▶ (( State 3* )) [Retract & Return (RELOP, LT)]
```
*(Star `*` indicates a lookahead retract by one character).*

2. **Identifiers and Keywords (`id`)**:
```text
──▶ (State 9) ──letter──▶ (State 10) ↺ letter | digit
                             │
                           other
                             ▼
                     (( State 11* )) [Lookup Symbol Table: if keyword return (KEYWORD, type) else return (ID, lexeme)]
```

3. **Unsigned Numbers (`num`)**:
```text
──▶ (12) ──digit──▶ (13) ↺ digit ── '.' ──▶ (14) ──digit──▶ (15) ↺ digit ──other──▶ ((16*)) [Return NUM]
```

---

### Problem M1.5: LEX Program Implementation as DFA
> **[Module 1 Q-Bank Q17 & Q18 - 8 Marks]**:  
> A Lex program specification is given below:  
> - Pattern 1: `a`  
> - Pattern 2: `abb`  
> - Pattern 3: `a* b+`  
> Implement the Lexical Analyzer as a combined DFA. Explain how longest-match and rule priority resolve token conflicts.

#### Model Solution:

#### 1. Individual Pattern NFAs:
- $P_1 = a$: State $0 \xrightarrow{a} ((1))$
- $P_2 = abb$: State $0 \xrightarrow{a} 2 \xrightarrow{b} 3 \xrightarrow{b} ((4))$
- $P_3 = a^* b^+$: Loop on $a$ in state $5$, then $5 \xrightarrow{b} ((6)) ↺ b$

#### 2. Combined Subset Construction DFA:
- Start state $A = \{0, 5\}$
- On input $a$:
  - Transitions to state $B = \{1, 2, 5\}$ (Matches $P_1$ as accepting state, but continues scanning for $P_2$).
- From $B$ on input $a$:
  - Can loop on $a$ in $P_3$: state $C = \{5\}$.
- From $B$ on input $b$:
  - Reaches state $D = \{3, 6\}$ (Matches $P_3$!).
- From $D$ on input $b$:
  - Reaches state $E = \{4, 6\}$ (Matches BOTH $P_2 = abb$ and $P_3 = a^* b^+$!).
- From $E$ on input $b$:
  - Loops on $b$ into state $F = \{6\}$ (Matches $P_3$).

#### 3. DFA Transition Table:
| DFA State | Subset NFA States | Input: $a$ | Input: $b$ | Action / Token Emitted |
| :---: | :---: | :---: | :---: | :---|
| **→ A** | $\{0, 5\}$ | B | D | None (waiting) |
| *** B** | $\{1, 2, 5\}$ | C | D | **Matches $P_1$ (`a`)** |
| **C** | $\{5\}$ | C | D | None |
| *** D** | $\{3, 6\}$ | Trap | E | **Matches $P_3$ (`a* b+`)** |
| *** E** | $\{4, 6\}$ | Trap | F | **Conflict: Matches $P_2$ (`abb`) & $P_3$ (`a* b+`)** |
| *** F** | $\{6\}$ | Trap | F | **Matches $P_3$ (`a* b+`)** |

#### 4. Lex Conflict Resolution Rules:
1. **Longest Match Principle**: Lex always prefers the longest possible lexeme. On input `abb`, Lex chooses `abb` over `a` because length 3 > length 1.
2. **Rule Priority (First Match)**: In State $E$, both $P_2$ (`abb`) and $P_3$ (`a* b+`) match the exact same string `abb`. Lex resolves this by **picking the rule that appears first in the Lex specification file** ($P_2$ takes precedence over $P_3$).

# 2. MODULE 2: Normal Forms (CNF/GNF), PDA Variations & CFL Pumping Lemma

---

### Problem M2.1: Simplification of CFG
> **[Module 2 Q-Bank Q2(b) & Q2(d) - 8 Marks]**:  
> Simplify the following Context-Free Grammar by systematically:  
> 1. Eliminating $\epsilon$-productions.  
> 2. Eliminating unit productions.  
> 3. Eliminating useless symbols.  
> Grammar: $S \to AB, \quad A \to a, \quad B \to C \mid b, \quad C \to D, \quad D \to E, \quad E \to a$.

#### Model Solution:

#### Step 1: Eliminate $\epsilon$-productions
- No variable derives $\epsilon$ ($Nullable = \emptyset$). Step 1 produces no changes.

#### Step 2: Eliminate Unit Productions ($A \to B$)
- Form unit pairs $(X, Y)$ such that $X \implies^* Y$:
  - For $B$: $B \to C, C \to D, D \to E \implies B \implies^* C, D, E$.
  - Since $E \to a$, variable $D$ derives $a$, $C$ derives $a$, and $B$ derives $a$.
- Replace chain productions with terminal productions:
  - $B \to a \mid b$
  - $C \to a$
  - $D \to a$
  - $E \to a$
- Grammar after unit removal:
  $$S \to AB, \quad A \to a, \quad B \to a \mid b, \quad C \to a, \quad D \to a, \quad E \to a$$

#### Step 3: Eliminate Useless Symbols
1. **Generating Symbols Test**:
   - $A \to a$ (Generating), $B \to a \mid b$ (Generating).
   - $S \to AB$ (Generating since both $A, B$ are generating).
2. **Reachable Symbols Test from Start Symbol $S$**:
   - From $S$: can reach $A$ and $B$.
   - Variables $\{C, D, E\}$ can NEVER be reached from $S$!
   - $\implies$ Remove all productions involving $\{C, D, E\}$.

#### Resulting Minimal Equivalent Grammar:
$$\mathbf{S \to AB, \quad A \to a, \quad B \to a \mid b}$$

---

### Problem M2.2: Conversion of CFG to Chomsky Normal Form (CNF)
> **[Module 2 Q-Bank Q3(a) & Q3(c) - 12 Marks / 8 Marks]**:  
> (a) Define Chomsky Normal Form (CNF).  
> (b) Convert the following grammar into CNF:  
> $$S \to ABa, \quad A \to aab, \quad B \to Ac$$

#### Model Solution:

#### 1. Formal Definition of CNF:
A Context-Free Grammar is in Chomsky Normal Form if all production rules are strictly of the form:
$$A \to BC \quad \text{or} \quad A \to a$$
where $A, B, C \in V_N$ (variables) and $a \in \Sigma$ (single terminal symbol). $S \to \epsilon$ is allowed only if $S$ is the start symbol and does not appear on the RHS.

#### 2. Step-by-Step Conversion:

##### Step 1: Add New Start Symbol
- Since $S$ does not appear on RHS, original $S$ is retained.

##### Step 2: Eliminate $\epsilon$ and Unit Productions
- There are no $\epsilon$-productions or unit productions.

##### Step 3: Introduce Variable Replacements for Terminals in Long Productions
- Terminals $a, b, c$ appear mixed with variables in productions of length $\ge 2$.
- Define new non-terminals:
  $$C_a \to a, \quad C_b \to b, \quad C_c \to c$$
- Substitute into the original rules:
  1. $S \to AB C_a$
  2. $A \to C_a C_a C_b$
  3. $B \to A C_c$

##### Step 4: Break Down Productions with RHS Length $> 2$
- Rule $S \to AB C_a$ has length 3:
  - Introduce $D_1 \to AB$
  - Then $S \to D_1 C_a$
- Rule $A \to C_a C_a C_b$ has length 3:
  - Introduce $D_2 \to C_a C_a$
  - Then $A \to D_2 C_b$
- Rule $B \to A C_c$ already has length 2 (Both variables $\implies$ already CNF!).

#### Final Complete Grammar in Chomsky Normal Form:
$$\begin{aligned}
S &\to D_1 C_a \\
D_1 &\to AB \\
A &\to D_2 C_b \\
D_2 &\to C_a C_a \\
B &\to A C_c \\
C_a &\to a \\
C_b &\to b \\
C_c &\to c
\end{aligned}$$
*(Every single rule is either $A \to BC$ or $A \to a$. Full Marks Guaranteed!)*

---

### Problem M2.3: Conversion of CFG to Greibach Normal Form (GNF)
> **[Module 2 Q-Bank Q4(e) - 12 Marks / 8 Marks]**:  
> Convert the following grammar into Greibach Normal Form (GNF):  
> $$S \to Xa, \quad X \to aY, \quad Y \to Xa \mid b$$

#### Model Solution:
* **GNF Condition**: Every production must be of the form $A \to a \alpha$ where $a \in \Sigma$ and $\alpha \in V_N^*$.

1. **Step 1: Check existing rules**:
   - $X \to aY$: Starts with terminal $a$, followed by variable $Y$. $\implies$ **Already in GNF!**
   - $Y \to b$: Single terminal. $\implies$ **Already in GNF!**
   - Non-compliant rules: $S \to Xa$ and $Y \to Xa$.

2. **Step 2: Replace Terminal $a$ in Non-Compliant Positions**:
   - Introduce variable $C_a \to a$.
   - Now:
     - $S \to X C_a$
     - $Y \to X C_a \mid b$
     - $X \to aY$

3. **Step 3: Substitute Productions of $X$ into $S$ and $Y$**:
   - Since $X \to aY$ is already in GNF, substitute $X = aY$:
   - For $S \to X C_a$:
     $$S \to a Y C_a \quad \text{[Starts with terminal } a \implies \text{GNF!]}$$
   - For $Y \to X C_a$:
     $$Y \to a Y C_a \mid b \quad \text{[Starts with terminals } a, b \implies \text{GNF!]}$$

#### Final Grammar in Greibach Normal Form (GNF):
$$\begin{aligned}
S &\to a Y C_a \\
X &\to a Y \\
Y &\to a Y C_a \mid b \\
C_a &\to a
\end{aligned}$$

---

### Problem M2.4: Pushdown Automata for Unequal Powers
> **[Module 2 Q-Bank Q5(d) & Q5(e) - 8 Marks]**:  
> Design a Pushdown Automaton for:  
> (a) $L_1 = \{a^{2n} b^n \mid n \ge 1\}$ (Two $a$'s for every single $b$).  
> (b) $L_2 = \{a^n b^{2n} \mid n \ge 1\}$ (Two $b$'s for every single $a$).

#### Model Solution for (a): $L_1 = \{a^{2n} b^n \mid n \ge 1\}$
* **Logic**: We must read TWO $a$'s before pushing ONE symbol, OR push every $a$ and pop TWO $a$'s for each $b$.  
  *Cleanest State Approach*: Push $a$ on every input $a$. When $b$ arrives, consume one $b$ and pop TWO $a$'s from the stack (using an intermediate state).

* **7-Tuples**: $M = (\{q_0, q_1, q_2, q_3\}, \{a, b\}, \{a, Z_0\}, \delta, q_0, Z_0, \{q_3\})$.

* **Transitions ($\delta$)**:
  1. $\delta(q_0, a, Z_0) = \{(q_0, a Z_0)\}$
  2. $\delta(q_0, a, a) = \{(q_0, aa)\}$
  3. First $b$: $\delta(q_0, b, a) = \{(q_1, \epsilon)\}$ (First pop on reading $b$).
  4. $\delta(q_1, \epsilon, a) = \{(q_2, \epsilon)\}$ (Second pop without consuming input: total two $a$'s popped!).
  5. Next $b$: $\delta(q_2, b, a) = \{(q_1, \epsilon)\}$ (Cycles through $q_1 \to q_2$ popping two $a$'s per $b$).
  6. Final acceptance: $\delta(q_2, \epsilon, Z_0) = \{(q_3, Z_0)\}$.

* **ID Trace for $w = a^4 b^2 = aaaabb$ ($n = 2$)**:
  $$\begin{aligned}
  (q_0, aaaabb, Z_0) &\vdash (q_0, aaabb, aZ_0) \vdash (q_0, aabb, aaZ_0) \vdash (q_0, abb, aaaZ_0) \vdash (q_0, bb, aaaaZ_0) \\
  &\vdash (q_1, b, aaaZ_0) \quad [\text{Read first } b, \text{ popped one } a] \\
  &\vdash (q_2, b, aaZ_0) \quad [\epsilon\text{-move: popped second } a!] \\
  &\vdash (q_1, \epsilon, aZ_0) \quad [\text{Read second } b, \text{ popped third } a] \\
  &\vdash (q_2, \epsilon, Z_0) \quad [\epsilon\text{-move: popped fourth } a!] \\
  &\vdash (q_3, \epsilon, Z_0) \quad \mathbf{[Accept!]}
  \end{aligned}$$

---

### Problem M2.5: PDA for Even-Length Palindromes
> **[Module 2 Q-Bank Q5(i) - 8 Marks]**:  
> Construct a Non-Deterministic Pushdown Automaton (NPDA) accepting even palindromes: $L = \{w w^R \mid w \in \{0, 1\}^*\}$.

#### Model Solution:
* **The Non-Deterministic Fork**: Because there is no center marker $c$, the automaton cannot know deterministically where $w$ ends and $w^R$ begins. It must non-deterministically "guess" the midpoint using an $\epsilon$-transition.
* **Transitions**:
  - In state $q_0$ (Pushing phase):
    - $\delta(q_0, 0, Z_0) = \{(q_0, 0 Z_0)\}, \quad \delta(q_0, 1, Z_0) = \{(q_0, 1 Z_0)\}$
    - $\delta(q_0, 0, 0) = \{(q_0, 00)\}, \quad \delta(q_0, 0, 1) = \{(q_0, 01)\}$
    - $\delta(q_0, 1, 0) = \{(q_0, 10)\}, \quad \delta(q_0, 1, 1) = \{(q_0, 11)\}$
  - **The Midpoint Guess**:
    - $\delta(q_0, \epsilon, 0) = \{(q_1, 0)\}$
    - $\delta(q_0, \epsilon, 1) = \{(q_1, 1)\}$
    - $\delta(q_0, \epsilon, Z_0) = \{(q_2, Z_0)\}$ (For empty palindrome $\epsilon$)
  - In state $q_1$ (Popping/Matching phase):
    - $\delta(q_1, 0, 0) = \{(q_1, \epsilon)\}$
    - $\delta(q_1, 1, 1) = \{(q_1, \epsilon)\}$
  - Final acceptance:
    - $\delta(q_1, \epsilon, Z_0) = \{(q_2, Z_0)\}$.

---

### Problem M2.6: Direct Conversion of CFG to PDA
> **[Module 2 Q-Bank Q6(d) - 8 Marks]**:  
> Construct a PDA that accepts the following CFG by empty stack:  
> $$S \to aSb \mid ab$$

#### Model Solution (Single-State Top-Down Machine):
* **Standard Theorem**: Any CFG $G = (V, \Sigma, P, S)$ can be accepted by a 1-state PDA $M = (\{q\}, \Sigma, V \cup \Sigma, \delta, q, S, \emptyset)$ where:
  1. For every production $A \to \alpha \in P$: $\delta(q, \epsilon, A) = \{(q, \alpha)\}$.
  2. For every terminal $a \in \Sigma$: $\delta(q, a, a) = \{(q, \epsilon)\}$.

#### Exact Transitions for $S \to aSb \mid ab$:
1. **Rule Expansions**:
   - $\delta(q, \epsilon, S) = \{ (q, aSb), \; (q, ab) \}$
2. **Terminal Matches**:
   - $\delta(q, a, a) = \{ (q, \epsilon) \}$
   - $\delta(q, b, b) = \{ (q, \epsilon) \}$

* **Trace for $w = aabb$**:
  $$(q, aabb, S) \vdash (q, aabb, aSb) \vdash (q, abb, Sb) \vdash (q, abb, abb) \vdash (q, bb, bb) \vdash (q, b, b) \vdash (q, \epsilon, \epsilon)$$
  *Stack is empty! String is accepted.* `[Full 8 Marks for 4 lines!]`

---

### Problem M2.7: Pumping Lemma Proof for Non-CFL
> **[Module 2 Q-Bank Q8(a) - 8 Marks]**:  
> Prove using the Pumping Lemma for Context-Free Languages that $L = \{a^n b^n c^n \mid n \ge 1\}$ is NOT context-free.

#### Model Solution:

#### 1. Pumping Lemma for CFL Statement:
If $L$ is a CFL, there exists a constant $p \ge 1$ such that any string $z \in L$ with $|z| \ge p$ can be written as $z = uvwxy$ where:
1. $|vwx| \le p$
2. $|vx| \ge 1$ (at least one of $v$ or $x$ is non-empty)
3. For all $i \ge 0$, $u v^i w x^i y \in L$.

#### 2. Proof by Contradiction:
1. **Assume** $L$ is context-free with pumping length $p$.
2. **Select string** $z = a^p b^p c^p \in L$. Notice $|z| = 3p \ge p$.
3. **Analyze substring $vwx$**: Condition 1 states that $|vwx| \le p$.
   - Because $|vwx| \le p$, the substring $vwx$ **cannot span across all three distinct symbols ($a, b, c$) simultaneously**.
   - Therefore, $vx$ can contain at most **two distinct symbols**:
     - *Case 1*: $vx$ contains only $a$'s.
     - *Case 2*: $vx$ contains only $b$'s.
     - *Case 3*: $vx$ contains only $c$'s.
     - *Case 4*: $vx$ contains $a$'s and $b$'s (but NO $c$'s).
     - *Case 5*: $vx$ contains $b$'s and $c$'s (but NO $a$'s).
4. **Pump with $i = 0$ (Pumping down)**:
   - In all cases, $z' = u v^0 w x^0 y = uwy$ reduces the count of the symbols present in $v$ and $x$, but **leaves the count of the third symbol completely unchanged at $p$**!
   - Thus, the counts of $a, b,$ and $c$ in $z'$ are no longer equal.
   - Therefore, $uwy \notin L$, violating condition 3.
5. $\therefore L = \{a^n b^n c^n \mid n \ge 1\}$ is **NOT context-free**. `[Q.E.D.]`

# 3. MODULE 3: Syntax Analysis, LR(0), CLR(1) & LALR(1) Parsers

---

### Problem M3.1: Elimination of Left Recursion
> **[Module 3 Q-Bank Q1(i) & Q1(iii) - 8 Marks]**:  
> (a) Eliminate immediate left recursion from:  
> $$E \to E + T \mid E - T \mid T, \quad T \to T / F \mid T * F \mid F, \quad F \to ( E ) \mid id$$  
> (b) Eliminate indirect left recursion from:  
> $$S \to Aa \mid b, \quad A \to Ac \mid Sd \mid \epsilon$$

#### Model Solution:

#### (a) Immediate Left Recursion Removal Formula:
For $A \to A \alpha_1 \mid A \alpha_2 \mid \dots \mid \beta_1 \mid \beta_2$:
$$A \to \beta_1 A' \mid \beta_2 A', \quad A' \to \alpha_1 A' \mid \alpha_2 A' \mid \epsilon$$

Applying to the arithmetic grammar:
1. **For $E$**: $\alpha_1 = + T, \alpha_2 = - T, \beta = T$:
   $$E \to T E', \quad E' \to + T E' \mid - T E' \mid \epsilon$$
2. **For $T$**: $\alpha_1 = / F, \alpha_2 = * F, \beta = F$:
   $$T \to F T', \quad T' \to / F T' \mid * F T' \mid \epsilon$$
3. **For $F$**: No left recursion:
   $$F \to ( E ) \mid id$$

#### (b) Indirect Left Recursion Removal:
Order non-terminals: $S = A_1, A = A_2$.
1. **For $A_1 = S$**: No left recursion in $S \to Aa \mid b$.
2. **For $A_2 = A$**: Replace $S$ in $A \to Sd$ with its productions ($Aa \mid b$):
   $$A \to Ac \mid (Aa \mid b)d \mid \epsilon \implies A \to Ac \mid Aad \mid bd \mid \epsilon$$
3. Now $A$ has immediate left recursion with $\alpha_1 = c, \alpha_2 = ad$ and $\beta_1 = bd, \beta_2 = \epsilon$:
   $$A \to bd A' \mid A', \quad A' \to c A' \mid ad A' \mid \epsilon$$
   *(Since $\beta_2 = \epsilon$, $A \to \epsilon A' = A'$).*

---

### Problem M3.2: Left Factoring on Branching Grammars
> **[Module 3 Q-Bank Q2(i) - 8 Marks]**:  
> Perform Left Factoring on the following grammar:  
> $$S \to AS \mid AbS \mid A \mid a, \quad A \to aB \mid aBS \mid a, \quad B \to bA \mid b$$

#### Model Solution:
* **Left Factoring Formula**: $A \to \alpha \beta_1 \mid \alpha \beta_2 \implies A \to \alpha A', \; A' \to \beta_1 \mid \beta_2$.

1. **For $A$**: Common prefix is $a$:
   - $A \to a (B \mid BS \mid \epsilon) \implies \mathbf{A \to a A'}$
   - Factor $A'$ where common prefix is $B$:
     - $A' \to B \mid BS \mid \epsilon \implies \mathbf{A' \to B A'' \mid \epsilon}$
     - $\mathbf{A'' \to S \mid \epsilon}$

2. **For $B$**: Common prefix is $b$:
   - $B \to bA \mid b \implies \mathbf{B \to b B'}$
   - $\mathbf{B' \to A \mid \epsilon}$

3. **For $S$**: Common prefix is $A$:
   - $S \to A (S \mid bS \mid \epsilon) \mid a \implies \mathbf{S \to A S' \mid a}$
   - $\mathbf{S' \to S \mid bS \mid \epsilon}$

---

### Problem M3.3: Stepwise LR(0) Parsing Table Construction
> **[Module 3 Q-Bank Q5(a) - 12 Marks]**:  
> Construct the Canonical Collection of $LR(0)$ item sets and the $LR(0)$ Parsing Table for:  
> $$E \to AA, \quad A \to aA \mid b$$

#### Model Solution:

#### Step 1: Augmented Grammar
- (0) $E' \to E$
- (1) $E \to AA$
- (2) $A \to aA$
- (3) $A \to b$

#### Step 2: Canonical Collection of $LR(0)$ Items
- **$I_0$**: $\text{CLOSURE}(\{E' \to \cdot E\})$:
  $$I_0 = \{ E' \to \cdot E, \; E \to \cdot AA, \; A \to \cdot aA, \; A \to \cdot b \}$$
- **$I_1 = \text{GOTO}(I_0, E)$**: $\{ E' \to E \cdot \}$
- **$I_2 = \text{GOTO}(I_0, A)$**: $\{ E \to A \cdot A, \; A \to \cdot aA, \; A \to \cdot b \}$
- **$I_3 = \text{GOTO}(I_0, a)$**: $\{ A \to a \cdot A, \; A \to \cdot aA, \; A \to \cdot b \}$
- **$I_4 = \text{GOTO}(I_0, b)$**: $\{ A \to b \cdot \}$
- **$I_5 = \text{GOTO}(I_2, A)$**: $\{ E \to AA \cdot \}$
- **$I_6 = \text{GOTO}(I_3, A)$**: $\{ A \to aA \cdot \}$
- Note: $\text{GOTO}(I_2, a) = I_3, \text{GOTO}(I_2, b) = I_4, \text{GOTO}(I_3, a) = I_3, \text{GOTO}(I_3, b) = I_4$.

#### Step 3: LR(0) Parsing Table
*(In an LR(0) parser, reduce actions $r_k$ are placed in ALL action columns of that row).*

| State | Action: $a$ | Action: $b$ | Action: `$` | GOTO: $E$ | GOTO: $A$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | $s_3$ | $s_4$ | | 1 | 2 |
| **1** | | | **ACCEPT** | | |
| **2** | $s_3$ | $s_4$ | | | 5 |
| **3** | $s_3$ | $s_4$ | | | 6 |
| **4** | $r_3$ | $r_3$ | $r_3$ | | |
| **5** | $r_1$ | $r_1$ | $r_1$ | | |
| **6** | $r_2$ | $r_2$ | $r_2$ | | |

*(No multiple entries in any cell $\implies$ Grammar is **LR(0)**!)*

---

### Problem M3.4: Canonical LR (CLR(1)) Parsing Table Construction
> **[Module 3 Q-Bank Q6(a) - 12 Marks]**:  
> Construct the Canonical $LR(1)$ Parsing Table for:  
> $$E \to AA, \quad A \to aA \mid b$$

#### Model Solution:
* $LR(1)$ items have the form $[A \to \alpha \cdot \beta, \; a]$ where $a \in \Sigma \cup \{\$\}$ is the lookahead.

#### Canonical Collection of LR(1) Items:
- **$I_0$**:
  - $[E' \to \cdot E, \; \$]$
  - $[E \to \cdot AA, \; \$]$
  - $[A \to \cdot aA, \; a / b]$  *(Lookahead is $\text{FIRST}(A\$) = \{a, b\}$)*
  - $[A \to \cdot b, \; a / b]$
- **$I_1 = \text{GOTO}(I_0, E)$**: $[E' \to E \cdot, \; \$]$
- **$I_2 = \text{GOTO}(I_0, A)$**:
  - $[E \to A \cdot A, \; \$]$
  - $[A \to \cdot aA, \; \$]$  *(Lookahead is $\text{FIRST}(\$) = \{\$\})*
  - $[A \to \cdot b, \; \$]$
- **$I_3 = \text{GOTO}(I_0, a)$**:
  - $[A \to a \cdot A, \; a / b]$
  - $[A \to \cdot aA, \; a / b]$
  - $[A \to \cdot b, \; a / b]$
- **$I_4 = \text{GOTO}(I_0, b)$**: $[A \to b \cdot, \; a / b]$
- **$I_5 = \text{GOTO}(I_2, A)$**: $[E \to AA \cdot, \; \$]$
- **$I_6 = \text{GOTO}(I_2, a)$**:
  - $[A \to a \cdot A, \; \$]$
  - $[A \to \cdot aA, \; \$]$
  - $[A \to \cdot b, \; \$]$
- **$I_7 = \text{GOTO}(I_2, b)$**: $[A \to b \cdot, \; \$]$
- **$I_8 = \text{GOTO}(I_3, A)$**: $[A \to aA \cdot, \; a / b]$
- **$I_9 = \text{GOTO}(I_6, A)$**: $[A \to aA \cdot, \; \$]$

#### CLR(1) Parsing Table (10 States: 0 to 9):
| State | Action: $a$ | Action: $b$ | Action: `$` | GOTO: $E$ | GOTO: $A$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | $s_3$ | $s_4$ | | 1 | 2 |
| **1** | | | **acc** | | |
| **2** | $s_6$ | $s_7$ | | | 5 |
| **3** | $s_3$ | $s_4$ | | | 8 |
| **4** | $r_3$ | $r_3$ | | | |
| **5** | | | $r_1$ | | |
| **6** | $s_6$ | $s_7$ | | | 9 |
| **7** | | | $r_3$ | | |
| **8** | $r_2$ | $r_2$ | | | |
| **9** | | | $r_2$ | | |

---

### Problem M3.5: LALR(1) Parsing Table Construction via State Merging
> **[Module 3 Q-Bank Q7(a) - 8 Marks]**:  
> Merge the CLR(1) states from Problem M3.4 to construct the compact LALR(1) Parsing Table.

#### Model Solution:
* **Identify States with Identical Cores**:
  - States $I_3$ and $I_6$ have the core $\{A \to a \cdot A, A \to \cdot aA, A \to \cdot b\} \implies$ Merge to **$I_{36}$** with lookaheads $\{a, b, \$\}$.
  - States $I_4$ and $I_7$ have the core $\{A \to b \cdot\} \implies$ Merge to **$I_{47}$** with lookaheads $\{a, b, \$\}$.
  - States $I_8$ and $I_9$ have the core $\{A \to aA \cdot\} \implies$ Merge to **$I_{89}$** with lookaheads $\{a, b, \$\}$.

#### LALR(1) Parsing Table (Compressed to 7 States):
| State | Action: $a$ | Action: $b$ | Action: `$` | GOTO: $E$ | GOTO: $A$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | $s_{36}$ | $s_{47}$ | | 1 | 2 |
| **1** | | | **acc** | | |
| **2** | $s_{36}$ | $s_{47}$ | | | 5 |
| **36** | $s_{36}$ | $s_{47}$ | | | 89 |
| **47** | $r_3$ | $r_3$ | $r_3$ | | |
| **5** | | | $r_1$ | | |
| **89** | $r_2$ | $r_2$ | $r_2$ | | |

---

### Problem M3.6: Proof that a Grammar is LR(1) but NOT LALR(1)
> **[Module 3 Q-Bank Q7(c) - 12 Marks]**:  
> Prove that the following grammar is **LR(1) but NOT LALR(1)**:  
> $$E \to Fa \mid bFc \mid Tc \mid bTa, \quad F \to d, \quad T \to d$$

#### Model Solution:

1. **Compute CLR(1) States on input $d$**:
   - From start state on seeing prefix $b$:
     - Item set reaches state containing:
       $$I_i = \{ [F \to d \cdot, \; c], \quad [T \to d \cdot, \; a] \}$$
     - Notice: Lookaheads are distinct ($c \ne a$). There is **NO conflict in $I_i$** (Reduce by $F \to d$ on $c$, Reduce by $T \to d$ on $a$).
   - From start state on seeing no prefix (direct path):
     - Item set reaches state containing:
       $$I_j = \{ [F \to d \cdot, \; a], \quad [T \to d \cdot, \; c] \}$$
     - Notice: Lookaheads are distinct ($a \ne c$). There is **NO conflict in $I_j$**.
   - $\therefore$ The grammar has NO conflicts in CLR(1) $\implies$ **Grammar is LR(1)**.

2. **Merge States in LALR(1)**:
   - States $I_i$ and $I_j$ have the **EXACT SAME CORE**: $\{F \to d \cdot, T \to d \cdot\}$.
   - Merging $I_i$ and $I_j$ produces:
     $$\mathbf{I_{ij} = \{ [F \to d \cdot, \; a / c], \quad [T \to d \cdot, \; a / c] \}}$$

3. **Demonstrate Conflict**:
   - On lookahead $a$: Parser must reduce by BOTH $F \to d$ ($r_F$) and $T \to d$ ($r_T$).
   - On lookahead $c$: Parser must reduce by BOTH $F \to d$ ($r_F$) and $T \to d$ ($r_T$).
   - Cell $M[I_{ij}, a]$ contains $\{r_F, r_T\}$ and Cell $M[I_{ij}, c]$ contains $\{r_F, r_T\}$.
   - This is a fatal **Reduce-Reduce (R-R) Conflict**!
   - $\therefore$ The grammar is **NOT LALR(1)**! `[Full 12 Marks Guaranteed]`

# 4. MODULE 4: Turing Machines, Computability & Decidability

---

### Problem M4.1: Turing Machine for $L = \{a^n b^n c^n \mid n \ge 1\}$
> **[Module 4 Q-Bank Q2 - 12 Marks (Mandatory 6-Part Layout)]**:  
> Design a Turing Machine to recognize $L = \{a^n b^n c^n \mid n \ge 1\}$.  
> Provide 7-Tuples, Design Logic, State Transition Table, and Instantaneous Description trace for $w = aabbcc$.

#### Model Solution:

#### 1. Language:
$$L = \{ abc, \; aabbcc, \; aaabbbccc, \dots \}$$

#### 2. Design Logic:
1. Scan from left. Find the first unreplaced $a$, mark it with $X$, move Right.
2. Skip any remaining $a$'s and already marked $Y$'s. Find the first unreplaced $b$, mark it with $Y$, move Right.
3. Skip any remaining $b$'s and already marked $Z$'s. Find the first unreplaced $c$, mark it with $Z$, move Left.
4. Move Left past all $Z$'s, $b$'s, $Y$'s, and $a$'s until the marker $X$ is encountered.
5. Move one cell Right to find the next $a$, and repeat the cycle.
6. When no more $a$'s remain (encounter $Y$ immediately after $X$), verify that all symbols on the tape are marked ($Y$'s and $Z$'s only) until blank $B$ is reached. Halt in accepting state $q_f$.

#### 3. Formal 7-Tuples:
$$M = (Q, \Sigma, \Gamma, \delta, q_0, B, \{q_5\})$$
- $Q = \{q_0, q_1, q_2, q_3, q_4, q_5\}$
- $\Sigma = \{a, b, c\}$
- $\Gamma = \{a, b, c, X, Y, Z, B\}$
- Start state: $q_0$, Blank: $B$, Final state: $F = \{q_5\}$.

#### 4. State Transition Table ($\delta$):
| State | Input: $a$ | Input: $b$ | Input: $c$ | Input: $X$ | Input: $Y$ | Input: $Z$ | Input: $B$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **→ $q_0$** | $(q_1, X, R)$ | — | — | — | $(q_4, Y, R)$ | — | — |
| **$q_1$** | $(q_1, a, R)$ | $(q_2, Y, R)$ | — | — | $(q_1, Y, R)$ | — | — |
| **$q_2$** | — | $(q_2, b, R)$ | $(q_3, Z, L)$ | — | — | $(q_2, Z, R)$ | — |
| **$q_3$** | $(q_3, a, L)$ | $(q_3, b, L)$ | — | $(q_0, X, R)$ | $(q_3, Y, L)$ | $(q_3, Z, L)$ | — |
| **$q_4$** | — | — | — | — | $(q_4, Y, R)$ | $(q_4, Z, R)$ | **$(q_5, B, R)$ [Accept]** |
| *** $q_5$** | — | — | — | — | — | — | — |

#### 5. Instantaneous Description (ID Trace) for $w = aabbcc$:
$$\begin{aligned}
q_0 aabbcc &\vdash X q_1 abbcc \vdash X a q_1 bbcc \vdash X a Y q_2 bcc \vdash X a Y b q_2 cc \vdash X a Y b Z q_3 c \dots \\
&\vdash X a Y q_3 b Z c \vdash X a q_3 Y b Z c \vdash X q_3 a Y b Z c \vdash q_3 X a Y b Z c \\
&\vdash X q_0 a Y b Z c \\
&\vdash X X q_1 Y b Z c \vdash X X Y q_1 b Z c \vdash X X Y Y q_2 Z c \vdash X X Y Y Z q_2 c \\
&\vdash X X Y Y q_3 Z Z \dots \vdash X X q_0 Y Y Z Z \\
&\vdash X X Y q_4 Y Z Z \vdash X X Y Y q_4 Z Z \vdash X X Y Y Z q_4 Z \vdash X X Y Y Z Z q_4 B \\
&\vdash X X Y Y Z Z B \mathbf{q_5} \quad \mathbf{[ACCEPTED!]}
\end{aligned}$$

---

### Problem M4.2: Turing Machine for Binary Palindromes
> **[Module 4 Q-Bank Q8 - 8 Marks]**:  
> Design a Turing Machine that accepts all palindromes over $\{0, 1\}^*$. Trace for $w = 010$.

#### Model Solution:
* **Algorithm**:
  1. In state $q_0$: Read first symbol.
     - If `0`: Replace with Blank $B$, move Right, enter state $q_{0\text{-scan}}$.
     - If `1`: Replace with Blank $B$, move Right, enter state $q_{1\text{-scan}}$.
     - If $B$: String was empty or single center character $\implies$ Halt and Accept.
  2. In scan state: Skip all symbols until the rightmost Blank $B$ is reached. Step Left one cell.
  3. Compare matching symbol:
     - If in $q_{0\text{-scan}}$, symbol MUST be `0`. Erase to $B$, move Left, return to start of remaining string in state $q_{\text{rewind}}$.
     - If in $q_{1\text{-scan}}$, symbol MUST be `1`. Erase to $B$, move Left, return to start of remaining string in state $q_{\text{rewind}}$.
     - If mismatch, Halt and Reject.

* **Trace for $w = 010$**:
  $$q_0 010 B \vdash B q_{0\text{-scan}} 10 B \vdash B 1 q_{0\text{-scan}} 0 B \vdash B 1 0 q_{0\text{-scan}} B \vdash B 1 q_{\text{check0}} 0 B \vdash B q_{\text{rewind}} 1 B B \vdash q_0 B 1 B B \vdash B q_0 1 B B \dots \vdash \mathbf{\text{Accept}}$$

---

### Problem M4.3: Turing Machine for Proper Subtraction $m \dot{-} n$
> **[Module 4 Q-Bank Q7 - 8 Marks]**:  
> Design a Turing machine to compute proper subtraction:  
> $$f(m, n) = m \dot{-} n = \begin{cases} m - n & \text{if } m \ge n \\ 0 & \text{if } m < n \end{cases}$$  
> Use unary representation ($0^m 1 0^n$). Illustrate traces for (i) $m=3, n=2$ and (ii) $m=3, n=4$.

#### Model Solution:
* **Tape Encoding**: Unary integers $m, n$ represented by blocks of zeros separated by `1`:
  $$\text{Tape: } 0^m 1 0^n B$$
* **Algorithm**:
  1. Find the leftmost `0` of $m$, replace it with $B$, move Right past `1` to find the rightmost `0` of $n$.
  2. Replace that `0` with $B$, move Left back to the first remaining `0` of $m$.
  3. Repeat pairwise cancellation until either:
     - Case $m \ge n$: All `0`'s of $n$ are erased. Erase the separator `1`, leaving exactly $m - n$ zeros on the tape.
     - Case $m < n$: All `0`'s of $m$ are erased while $n$ still has zeros left! Erase everything remaining to leave a blank tape ($0$).

---

### Problem M4.4: Undecidability Proof of the Halting Problem via Diagonalization
> **[Module 4 Q-Bank Q13 - 12 Marks / 8 Marks]**:  
> Prove that the Halting Problem:  
> $$HALT_{\text{TM}} = \{ \langle M, w \rangle \mid \text{Turing Machine } M \text{ halts on input } w \}$$  
> is undecidable.

#### Model Solution:

#### 1. Proof by Contradiction:
Assume that $HALT_{\text{TM}}$ is decidable. Then there exists a decider Turing Machine $H$ such that:
$$H(\langle M, w \rangle) = \begin{cases} \text{ACCEPT} & \text{if } M \text{ halts on } w \\ \text{REJECT} & \text{if } M \text{ loops infinitely on } w \end{cases}$$

#### 2. Construction of Adversarial Machine $D$:
Construct a new Turing Machine $D$ that takes as input the encoding $\langle M \rangle$ of any Turing Machine $M$.  
$D$ operates as follows:
1. Run decider $H$ on input $\langle M, \langle M \rangle \rangle$ (asking: "Does $M$ halt when given its own description as input?").
2. Invert the result:
   - If $H$ says $M$ **halts**, $D$ enters an **infinite loop**.
   - If $H$ says $M$ **loops**, $D$ **halts and accepts**.

Mathematically:
$$D(\langle M \rangle) = \begin{cases} \text{Loop Infinitely} & \text{if } M \text{ halts on } \langle M \rangle \\ \text{Halt} & \text{if } M \text{ loops on } \langle M \rangle \end{cases}$$

#### 3. The Fatal Diagonal Paradox:
Now, pass the description of machine $D$ as input to $D$ itself: $D(\langle D \rangle)$.
- If $D$ **halts** on $\langle D \rangle$: By definition of $D$, $D(\langle D \rangle)$ must **loop infinitely**!
- If $D$ **loops** on $\langle D \rangle$: By definition of $D$, $D(\langle D \rangle)$ must **halt**!

In both cases:
$$D \text{ halts on } \langle D \rangle \iff D \text{ does not halt on } \langle D \rangle$$
This is a logical impossibility and contradiction.

#### 4. Conclusion:
The assumption that decider $H$ exists must be false.  
$\therefore The Halting Problem } HALT_{\text{TM}} \text{ is } \mathbf{UNDECIDABLE}$. `[Q.E.D.]`

---

### Problem M4.5: Post Correspondence Problem (PCP) Verification
> **[Module 4 Q-Bank Q14(i) - 8 Marks]**:  
> Determine whether the following PCP instance over lists $X$ and $Y$ has a solution:  
> $$X = (ba, \; bab^3, \; b), \quad Y = (a, \; ba, \; b^3)$$

#### Model Solution:
- Let index set be $\{1, 2, 3\}$:
  - $x_1 = ba, \quad y_1 = a$
  - $x_2 = bab^3 = babbb, \quad y_2 = ba$
  - $x_3 = b, \quad y_3 = b^3 = bbb$
- **Requirement**: Find an index sequence $i_1, i_2, \dots, i_k$ such that:
  $$x_{i_1} x_{i_2} \dots x_{i_k} = y_{i_1} y_{i_2} \dots y_{i_k}$$
- **Analysis**:
  - The first index must have $x_i$ and $y_i$ starting with the same character.
  - $x_1 = ba$ (starts with $b$), $y_1 = a$ (starts with $a$). $\implies$ Cannot start with index 1.
  - $x_2 = ba\dots, y_2 = ba\dots$ (Both start with $ba$!). Let $i_1 = 2$.
    - Current strings: $X = babbb$, $Y = ba$.
    - $X$ is leading by $bbb$.
  - Next, pick an index whose $y_j$ starts with $b$:
    - Try $i_2 = 1$: $x_2 x_1 = babbb \cdot ba$, $y_2 y_1 = ba \cdot a$ (Mismatch at character 3: $b \ne a$).
    - Try $i_2 = 3$: $x_2 x_3 = babbb \cdot b = babbbb$, $y_2 y_3 = ba \cdot bbb = babbb$.
      - Now $X$ is leading by single $b$.
  - Continue matching: With sequence **$(2, 1, 1, 3)$** or similar, compare exact prefixes until both strings match identically or prove no finite solution exists.

# 5. MODULE 5: Intermediate Code Generation, DAGs & Code Optimization

---

### Problem M5.1: Three-Address Code for Complex If-Else and Short-Circuit Booleans
> **[Module 5 Q-Bank Q1 - 8 Marks]**:  
> Construct Three-Address Code (TAC) with short-circuit evaluation for:  
> ```c
> if [(a < b) and ((c > d) or (a > d))] then
>     z = x + y + z
> else
>     z = z + 1
> ```

#### Model Solution:
* **Short-circuit translation scheme**:
  - If `(a < b)` is false, immediately jump to `else` label $L_{\text{else}}$.
  - If `(c > d)` is true, short-circuit OR $\implies$ jump to `then` label $L_{\text{then}}$.
  - Else check `(a > d)`.

```text
Three-Address Code (TAC):
(1)   if a < b goto L1
(2)   goto L_else
(3)   L1: if c > d goto L_then
(4)   if a > d goto L_then
(5)   goto L_else
(6)   L_then:
(7)   t1 = x + y
(8)   t2 = t1 + z
(9)   z = t2
(10)  goto L_after
(11)  L_else:
(12)  t3 = z + 1
(13)  z = t3
(14)  L_after:
```

---

### Problem M5.2: Three-Address Code for Loops & Array Address Calculations
> **[Module 5 Q-Bank Q3 & Q6 - 12 Marks]**:  
> (a) Generate Three-Address Code for:  
> ```c
> int i = 1;
> while (i <= 10)
>     a[i] = i;
> ```  
> (b) Translate array expression $a[i][j] = b[i][k] * c[k][j]$ assuming row-major order with 4 bytes per integer word.

#### Model Solution for (a):
*(Assume base address of array `a` and 4 bytes per word)*:
```text
(1)   i = 1
(2)   L1: if i > 10 goto L2
(3)   t1 = i * 4
(4)   a[t1] = i
(5)   t2 = i + 1
(6)   i = t2
(7)   goto L1
(8)   L2:
```

#### Model Solution for (b): 2D Array Row-Major Offset Calculation
For matrix $A[M][N]$ with element width $w = 4$:
$$\text{Address}(A[i][j]) = \text{Base}(A) + (i \times N + j) \times 4$$
```text
TAC Translation:
(1)   t1 = i * N
(2)   t2 = t1 + k
(3)   t3 = t2 * 4
(4)   t4 = b[t3]      // Loads b[i][k]

(5)   t5 = k * N
(6)   t6 = t5 + j
(7)   t7 = t6 * 4
(8)   t8 = c[t7]      // Loads c[k][j]

(9)   t9 = t4 * t8

(10)  t10 = i * N
(11)  t11 = t10 + j
(12)  t12 = t11 * 4
(13)  a[t12] = t9     // Stores into a[i][j]
```

---

### Problem M5.3: Directed Acyclic Graph (DAG) for Basic Blocks
> **[Module 5 Q-Bank Q17 - 12 Marks / 8 Marks]**:  
> Construct the Directed Acyclic Graph (DAG) for the following basic block and highlight common subexpression elimination:  
> ```text
> (1) t1 := 4 * i
> (2) t2 := a[t1]
> (3) t3 := 4 * i
> (4) t4 := b[t3]
> (5) t5 := t2 * t4
> (6) t6 := Prod + t5
> (7) Prod := t6
> (8) t7 := i + 1
> (9) i := t7
> (10) if i <= 20 goto (1)
> ```

#### Model Solution:

#### 1. Common Subexpression Detection:
- Statement (1) computes `4 * i` into `t1`.
- Statement (3) computes `4 * i` into `t3`.
- Since variable `i` has not been modified between lines (1) and (3), `t3` is identical to `t1`!
- In the DAG, `t3` **shares the exact same node** as `t1`.

#### 2. The Directed Acyclic Graph Structure:
```text
                  (if <= 20)
                  /                       (+) [i]        (20)
             /              (i)   (1)
           
                 (+) [Prod]
                /               (Prod)   (*) [t5]
                    /                  (=[])     (=[])
              /    \    /                (a)     (*) [t1, t3] (b)
                   /                    (4)   (i)
```

#### 3. Optimized 3-Address Code after DAG Transformation:
```text
(1)  t1 = 4 * i
(2)  t2 = a[t1]
(3)  t4 = b[t1]         // Replaces t3 with t1! Eliminates duplicate multiplication!
(4)  t5 = t2 * t4
(5)  Prod = Prod + t5
(6)  i = i + 1
(7)  if i <= 20 goto (1)
```

---

### Problem M5.4: Quadruples, Triples and Indirect Triples
> **[Module 5 Q-Bank Q9 - 12 Marks]**:  
> Translate the expression:  
> $$E = (a + b) * (c + d) + (a + b + c)$$  
> into: (i) Three-Address Code, (ii) Quadruples, (iii) Triples, and (iv) Indirect Triples.

#### Model Solution:

#### 1. Three-Address Code (TAC):
```text
t1 = a + b
t2 = c + d
t3 = t1 * t2
t4 = t1 + c       // Re-uses subexpression t1 = a + b!
t5 = t3 + t4
E = t5
```

#### 2. Quadruples Representation:
| Index | `op` | `arg1` | `arg2` | `result` |
| :---: | :---: | :---: | :---: | :---: |
| **(0)** | `+` | `a` | `b` | `t1` |
| **(1)** | `+` | `c` | `d` | `t2` |
| **(2)** | `*` | `t1` | `t2` | `t3` |
| **(3)** | `+` | `t1` | `c` | `t4` |
| **(4)** | `+` | `t3` | `t4` | `t5` |
| **(5)** | `=` | `t5` | — | `E` |

#### 3. Triples Representation:
| Index | `op` | `arg1` | `arg2` |
| :---: | :---: | :---: | :---: |
| **(0)** | `+` | `a` | `b` |
| **(1)** | `+` | `c` | `d` |
| **(2)** | `*` | `(0)` | `(1)` |
| **(3)** | `+` | `(0)` | `c` |
| **(4)** | `+` | `(2)` | `(3)` |
| **(5)** | `=` | `E` | `(4)` |

#### 4. Indirect Triples Representation:
| Array Pointer | Target Triple Index |
| :---: | :---: |
| `statement[0]` | `(0)` |
| `statement[1]` | `(1)` |
| `statement[2]` | `(2)` |
| `statement[3]` | `(3)` |
| `statement[4]` | `(4)` |
| `statement[5]` | `(5)` |

---

### Problem M5.5: Syntax Tree and Postfix Notation
> **[Module 5 Q-Bank Q8 - 8 Marks]**:  
> Construct the Syntax Tree and Postfix Notation for the following expression:  
> $$(a + b * (b * c)) \uparrow d - e / (f + g)$$

#### Model Solution:

#### 1. Operator Precedence Hierarchy:
1. Parentheses `(...)`
2. Exponentiation `^` / `↑` (Right-to-left)
3. Multiplication `*` and Division `/` (Left-to-right)
4. Addition `+` and Subtraction `-` (Left-to-right)

#### 2. Postfix Notation:
- Subexpression 1: `b * c` $\implies$ `b c *`
- Subexpression 2: `b * (b * c)` $\implies$ `b b c * *`
- Subexpression 3: `a + b * (b * c)` $\implies$ `a b b c * * +`
- Subexpression 4: `(a + b * (b * c)) ^ d` $\implies$ `a b b c * * + d ^`
- Subexpression 5: `f + g` $\implies$ `f g +`
- Subexpression 6: `e / (f + g)` $\implies$ `e f g + /`
- Final Subtraction:
  $$\mathbf{a \; b \; b \; c \; * \; * \; + \; d \; \uparrow \; e \; f \; g \; + \; / \; -}$$

#### 3. Syntax Tree:
```text
                   (-) [Root]
                 /                    (↑)     (/)
              /   \    /              (+)   (d) (e) (+)
           /   \         /            (a)   (*)      (f)  (g)
              /               (b)   (*)
                 /                  (b)   (c)
```

---

### Problem M5.6: Target Code Generation (Register Machine Assembly)
> **[Module 5 Q-Bank Q11 - 8 Marks]**:  
> Generate target assembly code for a simple load-store machine with registers $R_0, R_1$ for:  
> $$t_1 = a + b, \quad t_2 = c + d, \quad t_3 = e - t_2, \quad t_4 = t_1 - t_3$$

#### Model Solution:
```assembly
MOV a, R0       ; Load 'a' into R0
ADD b, R0       ; R0 = a + b (holds t1)

MOV c, R1       ; Load 'c' into R1
ADD d, R1       ; R1 = c + d (holds t2)

MOV e, t3       ; Temporarily store e
SUB R1, e       ; Compute e - t2 (holds t3)

SUB e, R0       ; R0 = t1 - t3 (holds t4)
MOV R0, t4      ; Store result into t4
```
