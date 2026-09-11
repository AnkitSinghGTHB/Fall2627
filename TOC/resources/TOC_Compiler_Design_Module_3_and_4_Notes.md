# Discrete Theory of Computation & Compiler Design
## Modules 3 & 4: Syntax Analysis & Parsing (CAT-2 Comprehensive Notes)

---

## Table of Contents
1. [Module Overview & Parsing Hierarchy](#1-module-overview--parsing-hierarchy)
2. [Grammar Transformations for Top-Down Parsing](#2-grammar-transformations-for-top-down-parsing)
   - 2.1 [Elimination of Left Recursion](#21-elimination-of-left-recursion)
   - 2.2 [Left Factoring](#22-left-factoring)
3. [Computation of FIRST and FOLLOW Sets](#3-computation-of-first-and-follow-sets)
   - 3.1 [Formal Definitions and Rules](#31-formal-definitions-and-rules)
   - 3.2 [Comprehensive Classroom Problems & Solutions](#32-comprehensive-classroom-problems--solutions)
4. [LL(1) Predictive Parsing](#4-ll1-predictive-parsing)
   - 4.1 [Necessary & Sufficient Conditions for LL(1) Grammars](#41-necessary--sufficient-conditions-for-ll1-grammars)
   - 4.2 [LL(1) Parse Table Construction](#42-ll1-parse-table-construction)
   - 4.3 [Case Study: Dangling-Else Ambiguity & Non-LL(1) Proof](#43-case-study-dangling-else-ambiguity--non-ll1-proof)
   - 4.4 [Non-Recursive Predictive Parser (Stack Simulation Trace)](#44-non-recursive-predictive-parser-stack-simulation-trace)
5. [Bottom-Up Parsing & LR Parsers](#5-bottom-up-parsing--lr-parsers)
   - 5.1 [Introduction to LR Parsing & Shift-Reduce Operations](#51-introduction-to-lr-parsing--shift-reduce-operations)
   - 5.2 [LR(0) Items and the Closure & GOTO Operations](#52-lr0-items-and-the-closure--goto-operations)
6. [SLR(1) Parsing Table Construction](#6-slr1-parsing-table-construction)
   - 6.1 [SLR(1) Parsing Algorithm & Rules](#61-slr1-parsing-algorithm--rules)
   - 6.2 [Detailed Classroom Example 1: Arithmetic Expression Grammar](#62-detailed-classroom-example-1-arithmetic-expression-grammar)
   - 6.3 [Detailed Classroom Example 2: Assignment Grammar & S/R Conflict](#63-detailed-classroom-example-2-assignment-grammar--sr-conflict)
7. [Gap Filling, Confusions Resolved, and Exam Tips](#7-gap-filling-confusions-resolved-and-exam-tips)

---

## 1. Module Overview & Parsing Hierarchy

Syntax Analysis (the parser) is the second phase of a compiler. It takes tokens produced by the lexical analyzer and verifies whether the sequence conforms to the syntactic rules defined by a Context-Free Grammar (CFG) $G = (V, T, P, S)$.

### Parsing Hierarchy:
```
                       [ Parsers ]
                            |
         +------------------+------------------+
         |                                     |
   [ Top-Down ]                          [ Bottom-Up ]
   (Derivation)                           (Reduction)
         |                                     |
   +-----+-----+                         +-----+-----+
   |           |                         |           |
With         Without                 Operator      LR Parsers
Backtracking Backtracking            Precedence        |
             (LL(1))                                   |
                                         +------+------+------+
                                         |      |      |      |
                                       LR(0)  SLR(1) LALR(1) CLR(1)
```

- **LL(k)**: Left-to-right scan; Leftmost derivation; $k$ tokens of lookahead.
- **LR(k)**: Left-to-right scan; Rightmost derivation in reverse; $k$ tokens of lookahead.
- **Power Hierarchy**: $	ext{LR}(0) < 	ext{SLR}(1) < 	ext{LALR}(1) < 	ext{CLR}(1)$.
- All LL(1) grammars are unambiguous, but not all unambiguous grammars are LL(1).

---

## 2. Grammar Transformations for Top-Down Parsing

Top-down parsers (specifically recursive descent and LL(1) predictive parsers) cannot handle **left recursion** (causes infinite loops) or **common prefixes** (causes non-deterministic choices).

### 2.1 Elimination of Left Recursion

#### Immediate (Direct) Left Recursion
A production of the form $A \to A\alpha$ is directly left-recursive.

**General Pattern:**
If a non-terminal $A$ has productions:
$$A \to A\alpha_1 \mid A\alpha_2 \mid \dots \mid A\alpha_n \mid \beta_1 \mid \beta_2 \mid \dots \mid \beta_m$$
where no $\beta_i$ begins with $A$.

**Transformed Equivalent Grammar:**
$$A \to \beta_1 A' \mid \beta_2 A' \mid \dots \mid \beta_m A'$$
$$A' \to \alpha_1 A' \mid \alpha_2 A' \mid \dots \mid \alpha_n A' \mid \epsilon$$

#### Classroom Example (from Notes Page 1):
**Original Grammar:**
$$S \to S b A \mid S a b \mid a \mid b \mid c$$

- Here:
  - $\alpha_1 = b A$, $\alpha_2 = a b$
  - $\beta_1 = a$, $\beta_2 = b$, $\beta_3 = c$

**Resulting Grammar:**
$$S \to a S' \mid b S' \mid c S'$$
$$S' \to b A S' \mid a b S' \mid \epsilon$$

---

### 2.2 Left Factoring

Left factoring is a grammar transformation that extracts common prefixes from alternate productions of a single non-terminal to defer the decision until enough input has been seen.

**General Pattern:**
$$A \to \alpha \beta_1 \mid \alpha \beta_2 \mid \dots \mid \alpha \beta_n \mid \gamma$$

**Transformed Equivalent Grammar:**
$$A \to \alpha A' \mid \gamma$$
$$A' \to \beta_1 \mid \beta_2 \mid \dots \mid \beta_n$$

#### Classroom Examples (from Notes Page 6):
**Example 1:**
$$S \to a b A \mid a b B \mid c$$
- Common prefix is $\alpha = a b$.
- Transformed:
  $$S \to a b S' \mid c$$
  $$S' \to A \mid B$$

**Example 2:**
$$A \to a B c \mid a B B \mid a \mid d$$
- Common prefix among the first three alternatives is $a$:
  $$A \to a A' \mid d$$
  $$A' \to B c \mid B B \mid \epsilon$$
- Note: If further common prefixes exist (e.g., $B$), further factoring can be applied:
  $$A' \to B A'' \mid \epsilon$$
  $$A'' \to c \mid B$$

---

## 3. Computation of FIRST and FOLLOW Sets

FIRST and FOLLOW sets are foundational data structures used to construct predictive parsing tables (LL(1)) and SLR(1) parsing tables.

### 3.1 Formal Definitions and Rules

#### Rules to Calculate $\text{FIRST}(X)$:
1. If $X$ is a terminal, $\text{FIRST}(X) = \{X\}$.
2. If $X \to \epsilon$ is a production, then add $\epsilon$ to $\text{FIRST}(X)$.
3. If $X$ is a non-terminal and $X \to Y_1 Y_2 \dots Y_k$:
   - Add all non-$\epsilon$ symbols of $\text{FIRST}(Y_1)$ to $\text{FIRST}(X)$.
   - If $\epsilon \in \text{FIRST}(Y_1)$, add all non-$\epsilon$ symbols of $\text{FIRST}(Y_2)$ to $\text{FIRST}(X)$, and so on.
   - If for all $1 \le i \le k$, $\epsilon \in \text{FIRST}(Y_i)$, then add $\epsilon$ to $\text{FIRST}(X)$.

#### Rules to Calculate $\text{FOLLOW}(A)$ (Notes Page 1 & 2):
1. **Start Symbol Rule:** Include $\$$ (end-of-input marker) in $\text{FOLLOW}(S)$, where $S$ is the start symbol.
2. **Right-Neighbor Rule:** If there is a production $A \to \alpha B \beta$, then everything in $\text{FIRST}(\beta)$ except $\epsilon$ is in $\text{FOLLOW}(B)$:
   $$\text{FIRST}(\beta) \setminus \{\epsilon\} \subseteq \text{FOLLOW}(B)$$
3. **Epsilon-Propagation Rule:** If there is a production $A \to \alpha B$, OR $A \to \alpha B \beta$ where $\beta \Rightarrow^* \epsilon$ (i.e., $\epsilon \in \text{FIRST}(\beta)$), then everything in $\text{FOLLOW}(A)$ is in $\text{FOLLOW}(B)$:
   $$\text{FOLLOW}(A) \subseteq \text{FOLLOW}(B)$$
4. **Golden Rule:** $\epsilon$ is **NEVER** included in any FOLLOW set.

---

### 3.2 Comprehensive Classroom Problems & Solutions

#### Problem 1 (Notes Page 2)
**Grammar:**
$$S \to a S a \mid A$$
$$A \to b S A \mid a$$

- **FIRST Sets:**
  - From $S \to a S a$, $a \in \text{FIRST}(S)$.
  - From $S \to A$, $\text{FIRST}(A) \subseteq \text{FIRST}(S)$.
  - From $A \to b S A$, $b \in \text{FIRST}(A)$.
  - From $A \to a$, $a \in \text{FIRST}(A)$.
  - Hence:
    $$\text{FIRST}(A) = \{a, b\}$$
    $$\text{FIRST}(S) = \{a, b\}$$

- **FOLLOW Sets:**
  - Since $S$ is start symbol $\implies \$ \in \text{FOLLOW}(S)$.
  - From $S \to a S a$, $a$ follows $S \implies a \in \text{FOLLOW}(S)$.
  - From $A \to b S A$, $A$ follows $S \implies (\text{FIRST}(A) \setminus \{\epsilon\}) \subseteq \text{FOLLOW}(S) \implies \{a, b\} \subseteq \text{FOLLOW}(S)$.
  - Hence:
    $$\text{FOLLOW}(S) = \{\$, a, b\}$$
  - From $S \to A$, $\text{FOLLOW}(S) \subseteq \text{FOLLOW}(A)$.
  - From $A \to b S A$, $A$ is at the right end, so $\text{FOLLOW}(A) \subseteq \text{FOLLOW}(A)$.
  - Hence:
    $$\text{FOLLOW}(A) = \text{FOLLOW}(S) = \{\$, a, b\}$$

| Non-Terminal | FIRST | FOLLOW |
| :--- | :--- | :--- |
| **S** | $\{a, b\}$ | $\{\$, a, b\}$ |
| **A** | $\{a, b\}$ | $\{\$, a, b\}$ |

---

#### Problem 2 (Notes Page 2 - 3)
**Grammar:**
$$S \to A B \mid d$$
$$A \to b A \mid c \mid \epsilon$$
$$B \to e B \mid b$$

- **FIRST Sets:**
  - $\text{FIRST}(B) = \{b, e\}$
  - $\text{FIRST}(A) = \{b, c, \epsilon\}$
  - $\text{FIRST}(S)$:
    - From $S \to d \implies d \in \text{FIRST}(S)$.
    - From $S \to A B \implies (\text{FIRST}(A) \setminus \{\epsilon\}) \cup \text{FIRST}(B) = \{b, c\} \cup \{b, e\} = \{b, c, e\}$.
    - (Since $\epsilon \in \text{FIRST}(A)$ but $\epsilon \notin \text{FIRST}(B)$, $\epsilon \notin \text{FIRST}(S)$).
  - Hence:
    $$\text{FIRST}(S) = \{b, c, d, e\}$$

- **FOLLOW Sets:**
  - Start symbol: $\text{FOLLOW}(S) = \{\$\}$.
  - For $A$ in $S \to A B$:
    $$\text{FOLLOW}(A) = \text{FIRST}(B) = \{b, e\}$$
  - For $B$ in $S \to A B$:
    $$\text{FOLLOW}(B) = \text{FOLLOW}(S) = \{\$}$$
    From $B \to e B$, $B$ at the end adds nothing new.
    $$\text{FOLLOW}(B) = \{\$}$$

| Non-Terminal | FIRST | FOLLOW |
| :--- | :--- | :--- |
| **S** | $\{b, c, d, e\}$ | $\{\$}$ |
| **A** | $\{b, c, \epsilon\}$ | $\{b, e\}$ |
| **B** | $\{b, e\}$ | $\{\$}$ |

---

#### Problem 3 (Notes Page 3 - The `<how?>` Problem Resolved)
**Grammar:**
$$S \to A B C D \mid a$$
$$A \to A b \mid B c \mid \epsilon$$
$$B \to d B \mid \epsilon$$
$$C \to c \mid \epsilon$$
$$D \to g \mid h$$

> **Gap Filled & Note Clarification:**
> In the handwritten notes, there is a question mark and `<how?>` noted next to $B$ and $S$. Here is the rigorous breakdown:
>
> 1. Look at $A \to A b \mid B c \mid \epsilon$. This has direct left recursion. Even without eliminating it, we find:
>    - $\text{FIRST}(B) = \{d, \epsilon\}$
>    - $\text{FIRST}(C) = \{c, \epsilon\}$
>    - $\text{FIRST}(D) = \{g, h\}$
> 2. For $\text{FIRST}(A)$:
>    - $A \to \epsilon \implies \epsilon \in \text{FIRST}(A)$.
>    - $A \to B c$: since $\text{FIRST}(B) = \{d, \epsilon\}$, it yields $d$, and since $\epsilon \in \text{FIRST}(B)$, it also yields $c$.
>    - $A \to A b$ does not introduce any new initial terminal.
>    - Thus: $\text{FIRST}(A) = \{c, d, \epsilon\}$.
> 3. For $\text{FIRST}(S)$:
>    - From $S \to a \implies a \in \text{FIRST}(S)$.
>    - From $S \to A B C D$:
>      - $\text{FIRST}(A) \setminus \{\epsilon\} = \{c, d\} \subseteq \text{FIRST}(S)$.
>      - Since $\epsilon \in \text{FIRST}(A)$, look at $B$: $\text{FIRST}(B) \setminus \{\epsilon\} = \{d\} \subseteq \text{FIRST}(S)$.
>      - Since $\epsilon \in \text{FIRST}(B)$, look at $C$: $\text{FIRST}(C) \setminus \{\epsilon\} = \{c\} \subseteq \text{FIRST}(S)$.
>      - Since $\epsilon \in \text{FIRST}(C)$, look at $D$: $\text{FIRST}(D) = \{g, h\} \subseteq \text{FIRST}(S)$.
>      - Since $\epsilon \notin \text{FIRST}(D)$, chain stops.
>    - Hence: $\text{FIRST}(S) = \{a, c, d, g, h\}$.
> 4. For FOLLOW sets:
>    - $\text{FOLLOW}(S) = \{\$}$
>    - $\text{FOLLOW}(D)$: $D$ is at end of $S \to A B C D \implies \text{FOLLOW}(D) = \text{FOLLOW}(S) = \{\$}$.
>    - $\text{FOLLOW}(C)$: Followed by $D \implies \text{FIRST}(D) = \{g, h\}$.
>    - $\text{FOLLOW}(B)$:
>      - In $S \to A B C D$, $B$ is followed by $C D$.
>        $\text{FIRST}(C D) = (\text{FIRST}(C) \setminus \{\epsilon\}) \cup \text{FIRST}(D) = \{c, g, h\}$.
>      - In $A \to B c$, $B$ is followed by $c \implies c \in \text{FOLLOW}(B)$.
>      - In $B \to d B$, $B$ at the end gives $\text{FOLLOW}(B) \subseteq \text{FOLLOW}(B)$.
>      - Thus: $\text{FOLLOW}(B) = \{c, g, h\}$.
>    - $\text{FOLLOW}(A)$:
>      - In $S \to A B C D$, $A$ is followed by $B C D$.
>        $\text{FIRST}(B C D) = (\text{FIRST}(B) \setminus \{\epsilon\}) \cup (\text{FIRST}(C) \setminus \{\epsilon\}) \cup \text{FIRST}(D) = \{d, c, g, h\}$.
>      - In $A \to A b$, $A$ is followed by $b \implies b \in \text{FOLLOW}(A)$.
>      - Thus: $\text{FOLLOW}(A) = \{b, c, d, g, h\}$.

| Non-Terminal | FIRST | FOLLOW |
| :--- | :--- | :--- |
| **S** | $\{a, c, d, g, h\}$ | $\{\$}$ |
| **A** | $\{c, d, \epsilon\}$ | $\{b, c, d, g, h\}$ |
| **B** | $\{d, \epsilon\}$ | $\{c, g, h\}$ |
| **C** | $\{c, \epsilon\}$ | $\{g, h\}$ |
| **D** | $\{g, h\}$ | $\{\$}$ |

---

#### Problem 4 (Notes Page 3)
**Grammar:**
$$S \to A B \mid a$$
$$A \to B b \mid \epsilon$$
$$B \to a \mid \epsilon$$

- **FIRST Sets:**
  - $\text{FIRST}(B) = \{a, \epsilon\}$
  - For $A \to B b \mid \epsilon$:
    - $\text{FIRST}(B b) = (\text{FIRST}(B) \setminus \{\epsilon\}) \cup \{b\} = \{a, b\}$.
    - Plus $\epsilon \implies \text{FIRST}(A) = \{a, b, \epsilon\}$.
  - For $S \to A B \mid a$:
    - From $a$: $a \in \text{FIRST}(S)$.
    - From $A B$: $(\text{FIRST}(A) \setminus \{\epsilon\}) = \{a, b\}$.
    - Since $\epsilon \in \text{FIRST}(A)$, include $\text{FIRST}(B) = \{a, \epsilon\}$.
    - Since both $A \Rightarrow^* \epsilon$ and $B \Rightarrow^* \epsilon$, $\epsilon \in \text{FIRST}(S)$.
    - Hence: $\text{FIRST}(S) = \{a, b, \epsilon\}$.

- **FOLLOW Sets:**
  - $\text{FOLLOW}(S) = \{\$}$
  - For $A$ in $S \to A B$:
    - $\text{FIRST}(B) \setminus \{\epsilon\} = \{a\}$.
    - Since $\epsilon \in \text{FIRST}(B)$, include $\text{FOLLOW}(S) = \{\$}$.
    - Hence: $\text{FOLLOW}(A) = \{a, \$}$.
  - For $B$:
    - In $A \to B b$: followed by $b \implies b \in \text{FOLLOW}(B)$.
    - In $S \to A B$: $B$ is at end $\implies \text{FOLLOW}(S) = \{\$} \subseteq \text{FOLLOW}(B)$.
    - Hence: $\text{FOLLOW}(B) = \{b, \$}$.

| Non-Terminal | FIRST | FOLLOW |
| :--- | :--- | :--- |
| **S** | $\{a, b, \epsilon\}$ | $\{\$}$ |
| **A** | $\{a, b, \epsilon\}$ | $\{a, \$}$ |
| **B** | $\{a, \epsilon\}$ | $\{b, \$}$ |

---

## 4. LL(1) Predictive Parsing

### 4.1 Necessary & Sufficient Conditions for LL(1) Grammars

A context-free grammar $G$ is **LL(1)** if and only if for every non-terminal $A$ with multiple productions $A \to \alpha_1 \mid \alpha_2 \mid \dots \mid \alpha_n$:

1. **Disjoint FIRST Sets:**
   $$\text{FIRST}(\alpha_i) \cap \text{FIRST}(\alpha_j) = \emptyset \quad \forall i \ne j$$
2. **At Most One Can Derive $\epsilon$:**
   At most one of $\alpha_1, \alpha_2, \dots, \alpha_n$ can derive $\epsilon$.
3. **FIRST and FOLLOW Disjointness (if $\epsilon$-producer exists):**
   If $\alpha_j \Rightarrow^* \epsilon$, then:
   $$\text{FIRST}(\alpha_i) \cap \text{FOLLOW}(A) = \emptyset \quad \forall i \ne j$$

#### Equivalently:
For every production $A \to \alpha$:
- For each terminal $a \in \text{FIRST}(\alpha)$, add $A \to \alpha$ to $M[A, a]$.
- If $\epsilon \in \text{FIRST}(\alpha)$, for each terminal $b \in \text{FOLLOW}(A)$ (including $\$$), add $A \to \alpha$ to $M[A, b]$.
- If any cell $M[A, x]$ contains more than one production, the grammar is **NOT LL(1)**.

---

### 4.2 LL(1) Parse Table Construction

#### Problem: Classic Arithmetic Expression Grammar (Notes Page 4 - 5)
**Original Left-Recursive Grammar:**
$$E \to E + T \mid T$$
$$T \to T * F \mid F$$
$$F \to (E) \mid a \quad (\text{or } id)$$

**Step 1: Eliminate Left Recursion**
$$E \to T E'$$
$$E' \to + T E' \mid \epsilon$$
$$T \to F T'$$
$$T' \to * F T' \mid \epsilon$$
$$F \to (E) \mid a$$

**Step 2: Compute FIRST and FOLLOW**
- $\text{FIRST}(F) = \{(, a\}$
- $\text{FIRST}(T') = \{*, \epsilon\}$
- $\text{FIRST}(T) = \text{FIRST}(F) = \{(, a\}$
- $\text{FIRST}(E') = \{+, \epsilon\}$
- $\text{FIRST}(E) = \text{FIRST}(T) = \{(, a\}$

- $\text{FOLLOW}(E) = \{\$, )\}$
- $\text{FOLLOW}(E') = \text{FOLLOW}(E) = \{\$, )\}$
- $\text{FOLLOW}(T) = (\text{FIRST}(E') \setminus \{\epsilon\}) \cup \text{FOLLOW}(E') = \{+, \$, )\}$
- $\text{FOLLOW}(T') = \text{FOLLOW}(T) = \{+, \$, )\}$
- $\text{FOLLOW}(F) = (\text{FIRST}(T') \setminus \{\epsilon\}) \cup \text{FOLLOW}(T') = \{*, +, \$, )\}$

**Summary Table:**
| Non-Terminal | FIRST | FOLLOW |
| :--- | :--- | :--- |
| **E** | $\{(, a\}$ | $\{\$, )\}$ |
| **E'** | $\{+, \epsilon\}$ | $\{\$, )\}$ |
| **T** | $\{(, a\}$ | $\{+, \$, )\}$ |
| **T'** | $\{*, \epsilon\}$ | $\{+, \$, )\}$ |
| **F** | $\{(, a\}$ | $\{*, +, \$, )\}$ |

**Step 3: Complete LL(1) Parsing Table $M[A, a]$ (Notes Page 5 - Filled Completely):**

| Non-Terminal | $+$ | $*$ | $($ | $)$ | $a$ | $\$$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **E** | | | $E \to T E'$ | | $E \to T E'$ | |
| **E'** | $E' \to + T E'$ | | | $E' \to \epsilon$ | | $E' \to \epsilon$ |
| **T** | | | $T \to F T'$ | | $T \to F T'$ | |
| **T'** | $T' \to \epsilon$ | $T' \to * F T'$ | | $T' \to \epsilon$ | | $T' \to \epsilon$ |
| **F** | | | $F \to (E)$ | | $F \to a$ | |

*Observation:* No cell contains multiple entries. Hence, this grammar is **strictly LL(1)**.

---

### 4.3 Case Study: Dangling-Else Ambiguity & Non-LL(1) Proof

*(Notes Page 6 - 7)*
**Original Grammar:**
$$S \to i E t S e S \mid i E t S \mid a$$
$$E \to b$$
*(where $i = \text{if}, t = \text{then}, e = \text{else}, a = \text{other statement}, b = \text{condition}$)*

**Left Factoring:**
Common prefix $\alpha = i E t S$:
$$S \to i E t S S' \mid a$$
$$S' \to e S \mid \epsilon$$
$$E \to b$$

**FIRST and FOLLOW Computation:**
- $\text{FIRST}(S) = \{i, a\}$
- $\text{FIRST}(S') = \{e, \epsilon\}$
- $\text{FIRST}(E) = \{b\}$
- $\text{FOLLOW}(S) = \{e, \$}$ (since $S$ is followed by $S'$, $\text{FIRST}(S') = \{e\}$, and $S' \Rightarrow \epsilon \implies \text{FOLLOW}(S)$)
- $\text{FOLLOW}(S') = \text{FOLLOW}(S) = \{e, \$}$
- $\text{FOLLOW}(E) = \{t\}$

**Constructing Parsing Table for $S'$:**
1. From $S' \to e S$: since $\text{FIRST}(e S) = \{e\}$, add $S' \to e S$ to $M[S', e]$.
2. From $S' \to \epsilon$: since $\epsilon \in \text{FIRST}(S')$, add $S' \to \epsilon$ to $M[S', b]$ for all $b \in \text{FOLLOW}(S') = \{e, \$}$.
   - Add $S' \to \epsilon$ to $M[S', e]$.
   - Add $S' \to \epsilon$ to $M[S', \$]$.

**Conflict in Table Cell $M[S', e]$:**
$$M[S', e] = \{S' \to e S, \; S' \to \epsilon\}$$

> **Conclusion (Exam Note):**
> Since cell $M[S', e]$ contains **two entries**, a conflict arises. The parser cannot decide whether to match `else` with the innermost `if` ($S' \to eS$) or leave it unmatched ($S' \to \epsilon$). Hence, the grammar is **NOT LL(1)**.

---

### 4.4 Non-Recursive Predictive Parser (Stack Simulation Trace)

*(Notes Page 8 - 9)*
**Grammar:**
$$E \to T E', \quad E' \to + T E' \mid \epsilon, \quad T \to F T', \quad T' \to * F T' \mid \epsilon, \quad F \to (E) \mid id$$
**Input String:** `id + id * id $`

The stack holds grammar symbols prefixed with `$` at the bottom.
At each step:
- If stack top $X ==$ input symbol $a == \$$: **Accept**.
- If stack top $X ==$ input symbol $a \ne \$$: **Match & Pop $X$, advance input**.
- If stack top $X$ is non-terminal: Look up $M[X, a]$. Pop $X$ and push RHS of production in **reverse order**.

#### Complete Execution Table:

| Step | Stack | Input Buffer | Action / Production Applied |
| :---: | :--- | :--- | :--- |
| **1** | `$ E` | `id + id * id $` | Pop $E$, Push $T E'$ (from $E \to T E'$) |
| **2** | `$ E' T` | `id + id * id $` | Pop $T$, Push $F T'$ (from $T \to F T'$) |
| **3** | `$ E' T' F` | `id + id * id $` | Pop $F$, Push $id$ (from $F \to id$) |
| **4** | `$ E' T' id` | `id + id * id $` | Match `id` (Pop `id`, Advance input) |
| **5** | `$ E' T'` | `+ id * id $` | Pop $T'$, Push $\epsilon$ (from $T' \to \epsilon$) |
| **6** | `$ E'` | `+ id * id $` | Pop $E'$, Push $+ T E'$ (from $E' \to + T E'$) |
| **7** | `$ E' T +` | `+ id * id $` | Match `+` (Pop `+`, Advance input) |
| **8** | `$ E' T` | `id * id $` | Pop $T$, Push $F T'$ (from $T \to F T'$) |
| **9** | `$ E' T' F` | `id * id $` | Pop $F$, Push $id$ (from $F \to id$) |
| **10** | `$ E' T' id` | `id * id $` | Match `id` (Pop `id`, Advance input) |
| **11** | `$ E' T'` | `* id $` | Pop $T'$, Push $* F T'$ (from $T' \to * F T'$) |
| **12** | `$ E' T' F *` | `* id $` | Match `*` (Pop `*`, Advance input) |
| **13** | `$ E' T' F` | `id $` | Pop $F$, Push $id$ (from $F \to id$) |
| **14** | `$ E' T' id` | `id $` | Match `id` (Pop `id`, Advance input) |
| **15** | `$ E' T'` | `$` | Pop $T'$, Push $\epsilon$ (from $T' \to \epsilon$) |
| **16** | `$ E'` | `$` | Pop $E'$, Push $\epsilon$ (from $E' \to \epsilon$) |
| **17** | `$` | `$` | **ACCEPT (String is syntactically valid)** |

---

## 5. Bottom-Up Parsing & LR Parsers

### 5.1 Introduction to LR Parsing & Shift-Reduce Operations

Bottom-up parsers reconstruct the parse tree beginning at the leaves (tokens) and working up toward the root (start symbol).
- **Core Mechanism:** Handle pruning (finding the substring matching a production RHS and reducing it to the LHS non-terminal).
- **Four Parser Actions:**
  1. **Shift ($s_j$):** Push the next input terminal and target state $j$ onto the stack.
  2. **Reduce ($r_k$):** Replace RHS symbols on top of stack with LHS non-terminal of production $k$.
  3. **Accept:** Parsing completed successfully.
  4. **Error:** No valid transition exists.

---

### 5.2 LR(0) Items and the Closure & GOTO Operations

An **LR(0) item** of a grammar $G$ is a production of $G$ with a dot ($\cdot$) at some position of the RHS.
- Example: $A \to X Y Z$ yields four items:
  $$A \to \cdot X Y Z, \quad A \to X \cdot Y Z, \quad A \to X Y \cdot Z, \quad A \to X Y Z \cdot$$
- An item $A \to \alpha \cdot$ is called a **completed item**.

#### Operations on Item Sets:
1. **CLOSURE($I$):**
   - Every item in $I$ is in $\text{CLOSURE}(I)$.
   - If $A \to \alpha \cdot B \beta \in \text{CLOSURE}(I)$ and $B \to \gamma$ is a production, then add item $B \to \cdot \gamma$ to $\text{CLOSURE}(I)$, if not already there. Repeat until no new items can be added.
2. **GOTO($I, X$):**
   - Let $J = \{ A \to \alpha X \cdot \beta \mid A \to \alpha \cdot X \beta \in I \}$.
   - $\text{GOTO}(I, X) = \text{CLOSURE}(J)$.

---

## 6. SLR(1) Parsing Table Construction

### 6.1 SLR(1) Parsing Algorithm & Rules

Given an augmented grammar $G'$ with start production $S' \to S$:

1. Number the productions of the original grammar from $1$ to $n$.
2. Compute $\text{FOLLOW}(A)$ for all non-terminals $A$.
3. Construct the Canonical Collection of LR(0) Item Sets: $\mathcal{C} = \{I_0, I_1, \dots, I_m\}$.
4. Fill the parsing table:
   - **Shift Action:** If $[A \to \alpha \cdot a \beta] \in I_i$ and $\text{GOTO}(I_i, a) = I_j$ (where $a$ is a terminal), set $\text{ACTION}[i, a] = s_j$.
   - **Reduce Action:** If $[A \to \alpha \cdot] \in I_i$ (where $A \to \alpha$ is production $k$), set $\text{ACTION}[i, a] = r_k$ for **ALL** $a \in \text{FOLLOW}(A)$.
   - **Accept Action:** If $[S' \to S \cdot] \in I_i$, set $\text{ACTION}[i, \$] = \text{Accept}$.
   - **GOTO Action:** If $\text{GOTO}(I_i, A) = I_j$ (where $A$ is a non-terminal), set $\text{GOTO}[i, A] = j$.
   - All other entries are **Error**.

---

### 6.2 Detailed Classroom Example 1: Arithmetic Expression Grammar

*(Notes Pages 10, 11, 12, 13)*

**Numbered Productions:**
0. $E' \to E$ (Augmented)
1. $E \to E + T$
2. $E \to T$
3. $T \to T * F$
4. $T \to F$
5. $F \to (E)$
6. $F \to id$

**FIRST & FOLLOW Sets:**
- $\text{FOLLOW}(E) = \{+, ), \$}$
- $\text{FOLLOW}(T) = \{+, *, ), \$}$
- $\text{FOLLOW}(F) = \{+, *, ), \$}$

#### Canonical Collection of LR(0) Items:

- **State $I_0 = \text{CLOSURE}(\{E' \to \cdot E\})$:**
  $$E' \to \cdot E$$
  $$E \to \cdot E + T$$
  $$E \to \cdot T$$
  $$T \to \cdot T * F$$
  $$T \to \cdot F$$
  $$F \to \cdot (E)$$
  $$F \to \cdot id$$

- **Transitions from $I_0$:**
  - $\text{GOTO}(I_0, E) = I_1$:
    $$E' \to E \cdot$$
    $$E \to E \cdot + T$$
  - $\text{GOTO}(I_0, T) = I_2$:
    $$E \to T \cdot$$
    $$T \to T \cdot * F$$
  - $\text{GOTO}(I_0, F) = I_3$:
    $$T \to F \cdot$$
  - $\text{GOTO}(I_0, '(') = I_4$:
    $$F \to (\cdot E)$$
    $$E \to \cdot E + T, \quad E \to \cdot T, \quad T \to \cdot T * F, \quad T \to \cdot F, \quad F \to \cdot (E), \quad F \to \cdot id$$
  - $\text{GOTO}(I_0, id) = I_5$:
    $$F \to id \cdot$$

- **Transitions from $I_1$:**
  - $\text{GOTO}(I_1, +) = I_6$:
    $$E \to E + \cdot T$$
    $$T \to \cdot T * F, \quad T \to \cdot F, \quad F \to \cdot (E), \quad F \to \cdot id$$

- **Transitions from $I_2$:**
  - $\text{GOTO}(I_2, *) = I_7$:
    $$T \to T * \cdot F$$
    $$F \to \cdot (E), \quad F \to \cdot id$$

- **Transitions from $I_4$:**
  - $\text{GOTO}(I_4, E) = I_8$:
    $$F \to (E \cdot)$$
    $$E \to E \cdot + T$$
  - $\text{GOTO}(I_4, T) = I_2$
  - $\text{GOTO}(I_4, F) = I_3$
  - $\text{GOTO}(I_4, '(') = I_4$
  - $\text{GOTO}(I_4, id) = I_5$

- **Transitions from $I_6$:**
  - $\text{GOTO}(I_6, T) = I_9$:
    $$E \to E + T \cdot$$
    $$T \to T \cdot * F$$
  - $\text{GOTO}(I_6, F) = I_3$
  - $\text{GOTO}(I_6, '(') = I_4$
  - $\text{GOTO}(I_6, id) = I_5$

- **Transitions from $I_7$:**
  - $\text{GOTO}(I_7, F) = I_{10}$:
    $$T \to T * F \cdot$$
  - $\text{GOTO}(I_7, '(') = I_4$
  - $\text{GOTO}(I_7, id) = I_5$

- **Transitions from $I_8$:**
  - $\text{GOTO}(I_8, ')') = I_{11}$:
    $$F \to (E) \cdot$$
  - $\text{GOTO}(I_8, +) = I_6$

- **Transitions from $I_9$:**
  - $\text{GOTO}(I_9, *) = I_7$

---

#### Complete SLR(1) Parsing Table:

| State | $id$ | $+$ | $*$ | $($ | $)$ | $\$$ | $E$ | $T$ | $F$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | $s_5$ | | | $s_4$ | | | 1 | 2 | 3 |
| **1** | | $s_6$ | | | | **Accept** | | | |
| **2** | | $r_2$ | $s_7$ | | $r_2$ | $r_2$ | | | |
| **3** | | $r_4$ | $r_4$ | | $r_4$ | $r_4$ | | | |
| **4** | $s_5$ | | | $s_4$ | | | 8 | 2 | 3 |
| **5** | | $r_6$ | $r_6$ | | $r_6$ | $r_6$ | | | |
| **6** | $s_5$ | | | $s_4$ | | | | 9 | 3 |
| **7** | $s_5$ | | | $s_4$ | | | | | 10 |
| **8** | | $s_6$ | | | $s_{11}$ | | | | |
| **9** | | $r_1$ | $s_7$ | | $r_1$ | $r_1$ | | | |
| **10** | | $r_3$ | $r_3$ | | $r_3$ | $r_3$ | | | |
| **11** | | $r_5$ | $r_5$ | | $r_5$ | $r_5$ | | | |

---

### 6.3 Detailed Classroom Example 2: Assignment Grammar & S/R Conflict

*(Notes Pages 12 & 13 - Completed from Scratch)*

**Problem Statement from Notes:**
Construct the SLR parser for the grammar:
$$S \to L = R \mid R$$
$$L \to * R \mid id$$
$$R \to L$$

#### Step 1: Augment Grammar and Number Productions
0. $S' \to S$
1. $S \to L = R$
2. $S \to R$
3. $L \to * R$
4. $L \to id$
5. $R \to L$

#### Step 2: Compute FIRST and FOLLOW
- $\text{FIRST}(L) = \{*, id\}$
- $\text{FIRST}(R) = \text{FIRST}(L) = \{*, id\}$
- $\text{FIRST}(S) = \text{FIRST}(L) \cup \text{FIRST}(R) = \{*, id\}$

- $\text{FOLLOW}(S) = \{\$}$
- $\text{FOLLOW}(L)$:
  - In $S \to L = R$: followed by $=$ $\implies = \in \text{FOLLOW}(L)$.
  - In $R \to L$: $\text{FOLLOW}(R) \subseteq \text{FOLLOW}(L)$.
  - Hence: $\text{FOLLOW}(L) = \{=, \$}$.
- $\text{FOLLOW}(R)$:
  - In $S \to L = R$: $R$ is at end $\implies \text{FOLLOW}(S) = \{\$} \subseteq \text{FOLLOW}(R)$.
  - In $S \to R$: $R$ is at end $\implies \text{FOLLOW}(S) \subseteq \text{FOLLOW}(R)$.
  - In $L \to * R$: $R$ is at end $\implies \text{FOLLOW}(L) \subseteq \text{FOLLOW}(R)$.
  - Since $\text{FOLLOW}(L) = \{=, \$}$, this adds $=$ to $\text{FOLLOW}(R)$.
  - Hence: $\text{FOLLOW}(R) = \{=, \$}$.

#### Step 3: Canonical Collection of LR(0) Items

- **State $I_0$:**
  $$S' \to \cdot S$$
  $$S \to \cdot L = R$$
  $$S \to \cdot R$$
  $$L \to \cdot * R$$
  $$L \to \cdot id$$
  $$R \to \cdot L$$

- **Transitions from $I_0$:**
  - $\text{GOTO}(I_0, S) = I_1$:
    $$S' \to S \cdot$$
  - $\text{GOTO}(I_0, L) = I_2$:
    $$S \to L \cdot = R$$
    $$R \to L \cdot$$
  - $\text{GOTO}(I_0, R) = I_3$:
    $$S \to R \cdot$$
  - $\text{GOTO}(I_0, *) = I_4$:
    $$L \to * \cdot R$$
    $$R \to \cdot L, \quad L \to \cdot * R, \quad L \to \cdot id$$
  - $\text{GOTO}(I_0, id) = I_5$:
    $$L \to id \cdot$$

#### Step 4: SLR(1) Conflict Analysis in State $I_2$
In State $I_2$:
1. $S \to L \cdot = R$: Dot is before terminal $=$. By the Shift rule, since $\text{GOTO}(I_2, =) = I_6$, add **Shift 6 ($s_6$)** under column $=$.
2. $R \to L \cdot$: Dot is at the end. This is production rule (5) $R \to L$. By the SLR Reduce rule, add **Reduce 5 ($r_5$)** under all terminals in $\text{FOLLOW}(R)$.
   - Since $\text{FOLLOW}(R) = \{=, \$}$, we must place $r_5$ under column $=$ and column $\$.

**The Conflict:**
Under column $=$ for State 2:
$$\text{ACTION}[2, =] = \{s_6, \; r_5\}$$

> **Key Exam Takeaway:**
> State 2 exhibits a **Shift/Reduce (S/R) conflict** on symbol $=$.
> Therefore, this grammar is **NOT SLR(1)**!
> *(Note: This grammar IS LR(1) and LALR(1), because in LR(1), lookaheads are tracked precisely, and $R \to L$ only has lookahead $\{\$}$, not $=$. This is why LR(1) and LALR(1) are more powerful than SLR(1)).*

---

## 7. Gap Filling, Confusions Resolved, and Exam Tips

### 1. Clarification on the Student's Note Scribble:
> *"when . reaches end, see follow of left hand symbol... check follow of E... also r (what number then?)... this number depends state/step in original ques"*

- **Explanation:** When an item has the dot at the end $[A \to \alpha \cdot]$, it represents a completed production.
- To know which row/column to place the reduce action:
  1. The row is the current state number (e.g., State 2).
  2. The production number $k$ is its position in the original numbered grammar (e.g., $E \to T$ is production 2, so action is $r_2$).
  3. The columns are all terminals in $\text{FOLLOW}(A)$ of the LHS non-terminal $A$.

### 2. Clarification on GOTO Table:
> *"when . is before variable, then check where it goes... since E -> .T, right after the var, goto table... use that number"*

- **Explanation:** The parsing table is split into two halves:
  - **ACTION table:** Terminals $+$ $\$$ (Shift, Reduce, Accept, Error).
  - **GOTO table:** Non-terminals (Pure state transitions: e.g., on $E$, transition from state $0$ goes to state $1$).
  - Never put an $s$ or $r$ in the GOTO table; write only the integer state index.

### 3. Comparison of Parser Classes:
| Feature | LL(1) | LR(0) | SLR(1) | LALR(1) | CLR(1) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Parsing Type** | Top-Down | Bottom-Up | Bottom-Up | Bottom-Up | Bottom-Up |
| **Grammar Class** | Unambiguous, No Left Recursion, Factored | Extremely Restricted | Needs Disjoint FOLLOW for Reductions | Same states as LR(0), Lookahead-aware | Maximum Power |
| **Conflicts** | First/First, First/Follow | S/R, R/R | S/R, R/R on FOLLOW sets | S/R, R/R on LALR lookaheads | Minimal conflicts |
| **Table Size** | Small ($|V| \times |T|$) | Small ($|\text{Items}| \times (|T|+|V|)$) | Same as LR(0) | Same as LR(0) | Very Large ($O(2^n)$ states) |

---
*Document compiled and verified from class lecture notes and standard compiler design theory.*
