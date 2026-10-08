# 📘 Module 3: Syntax Analysis — LL(1), SLR(1), CLR(1) & Conflicts

> **Module Focus**: Left Recursion & Left Factoring, FIRST & FOLLOW Sets, LL(1) Predictive Parsing Table, SLR(1) Parsing Table, and Mathematical Proofs of Shift-Reduce (S/R) and Reduce-Reduce (R/R) Conflicts.  
> **Weightage in FAT**: Approx 20–25 Marks.  
> **Faculty Requirement**: Complete First/Follow lists, numbered LR(0) items, explicit Action/Goto table, and conflict formulas.

---

## 1. Grammar Pre-requisites for Predictive Parsing

Before building an LL(1) parser, the grammar must satisfy three prerequisites:
1. **It must be Unambiguous**.
2. **It must be Non-Left Recursive**.
3. **It must be Left Factored**.

### 1.1 Elimination of Left Recursion
* **Immediate Left Recursion**: A rule of the form $A \to A\alpha \mid \beta$ (where $\beta$ does not start with $A$).
* **Elimination Formula**:
  $$\begin{aligned}
  A &\to \beta A' \\
  A' &\to \alpha A' \mid \epsilon
  \end{aligned}$$

#### 📝 Worked Example:
Given: $E \to E + T \mid T$
* Here, $A = E$, $\alpha = + T$, and $\beta = T$.
* Replacing with formula gives:
  $$\begin{aligned}
  E &\to T E' \\
  E' &\to + T E' \mid \epsilon
  \end{aligned}$$

---

### 1.2 Left Factoring (Deferred Decision)
* Given: $A \to \alpha \beta_1 \mid \alpha \beta_2$ (Common prefix $\alpha$).
* **Formula**:
  $$\begin{aligned}
  A &\to \alpha A' \\
  A' &\to \beta_1 \mid \beta_2
  \end{aligned}$$

---

## 2. Computing FIRST and FOLLOW Lists (Guaranteed 5–10 Marks)

Dr. Gaurav Soni always asks for explicit FIRST and FOLLOW lists. Follow these formal mathematical rules:

### 2.1 The 3 Golden Rules of FIRST
1. If $X$ is a terminal, then $\text{FIRST}(X) = \{X\}$.
2. If $X \to \epsilon$ is a production, then add $\epsilon$ to $\text{FIRST}(X)$.
3. If $X$ is a non-terminal and $X \to Y_1 Y_2 \dots Y_k$:
   - Add all non-$\epsilon$ symbols of $\text{FIRST}(Y_1)$ to $\text{FIRST}(X)$.
   - If $\epsilon \in \text{FIRST}(Y_1)$, add $\text{FIRST}(Y_2) \setminus \{\epsilon\}$.
   - If $\epsilon \in \text{FIRST}(Y_i)$ for all $i = 1 \dots k$, add $\epsilon$ to $\text{FIRST}(X)$.

---

### 2.2 The 3 Golden Rules of FOLLOW
1. **Always add `$` to $\text{FOLLOW}(S)$**, where $S$ is the start symbol (representing the End of Input).
2. If there is a production $A \to \alpha B \beta$, then everything in $\text{FIRST}(\beta)$ (except $\epsilon$) is in $\text{FOLLOW}(B)$.
3. If there is a production $A \to \alpha B$, OR a production $A \to \alpha B \beta$ where $\epsilon \in \text{FIRST}(\beta)$, then **everything in $\text{FOLLOW}(A)$ is in $\text{FOLLOW}(B)$**.

> ⚠️ **CRITICAL TRAP**:  
> $\epsilon$ can NEVER appear in a FOLLOW set! If you write $\epsilon$ inside any $\text{FOLLOW}(A)$, you immediately lose marks.

---

### 📝 Worked Example: Computing FIRST and FOLLOW
Consider the standard expression grammar:
1. $E \to T E'$
2. $E' \to + T E' \mid \epsilon$
3. $T \to F T'$
4. $T' \to * F T' \mid \epsilon$
5. $F \to ( E ) \mid id$

#### Computation Table:
| Non-Terminal | FIRST List | FOLLOW List | Explanation |
| :---: | :--- | :--- | :--- |
| **$E$** | `{(, id}` | `{$, )}` | Start symbol gets `$`; rule (5) gives `)`. |
| **$E'$** | `{+, ε}` | `{$, )}` | Follow of $E'$ is same as Follow of $E$. |
| **$T$** | `{(, id}` | `{+, $, )}` | $\text{FIRST}(E') \setminus \{\epsilon\} = \{+\}$ plus $\text{FOLLOW}(E)$. |
| **$T'$** | `{*, ε}` | `{+, $, )}` | Follow of $T'$ is same as Follow of $T$. |
| **$F$** | `{(, id}` | `{*, +, $, )}` | $\text{FIRST}(T') \setminus \{\epsilon\} = \{*\}$ plus $\text{FOLLOW}(T)$. |

---

## 3. Construction of LL(1) Parsing Table & String Validation

### Table Construction Algorithm
For each production $A \to \alpha$ of the grammar:
1. For each terminal $a \in \text{FIRST}(\alpha)$, add $A \to \alpha$ to table cell $M[A, a]$.
2. If $\epsilon \in \text{FIRST}(\alpha)$, then for each symbol $b \in \text{FOLLOW}(A)$ (including `$`), add $A \to \alpha$ to table cell $M[A, b]$.
3. All empty cells are marked **Error**.

```text
LL(1) Parsing Table:
┌─────┬──────────────┬──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│ NT  │      id      │      +       │      *       │      (       │      )       │      $       │
├─────┼──────────────┼──────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│  E  │  E → T E'    │              │              │  E → T E'    │              │              │
│  E' │              │ E' → + T E'  │              │              │ E' → ε       │ E' → ε       │
│  T  │  T → F T'    │              │              │  T → F T'    │              │              │
│  T' │              │ T' → ε       │ T' → * F T'  │              │ T' → ε       │ T' → ε       │
│  F  │  F → id      │              │              │  F → ( E )   │              │              │
└─────┴──────────────┴──────────────┴──────────────┴──────────────┴──────────────┴──────────────┘
```

> **LL(1) Grammatical Test**:  
> Since **no cell in the parsing table contains more than one production rule**, the grammar is **LL(1)**!

---

## 4. Construction of SLR(1) Parsing Table & Shift-Reduce Conflict (10 Marks)

An SLR(1) parser is a Simple LR parser that uses $LR(0)$ items and resolves reduce actions using **$\text{FOLLOW}$ sets**.

### 🛠️ The 4-Step SLR(1) Construction Process

#### Step 1: Create the Augmented Grammar
Given grammar $G$ with start symbol $S$, add a new start symbol $S'$ and production:
$$S' \to S$$

#### Step 2: Construct the Canonical Collection of $LR(0)$ Items
An $LR(0)$ item is a production with a dot $\cdot$ indicating how much of the RHS has been parsed.
* **$\text{CLOSURE}(I)$ Rule**:
  - Add all items in $I$ to $\text{CLOSURE}(I)$.
  - If $[A \to \alpha \cdot B \beta] \in \text{CLOSURE}(I)$, add $[B \to \cdot \gamma]$ for every production $B \to \gamma$.
* **$\text{GOTO}(I, X)$ Rule**:
  - If $[A \to \alpha \cdot X \beta] \in I$, then $\text{GOTO}(I, X) = \text{CLOSURE}(\{[A \to \alpha X \cdot \beta]\})$.

#### Step 3: Populate the SLR(1) Table Cells
* **Shift Action**: If item $[A \to \alpha \cdot a \beta] \in I_i$ and $\text{GOTO}(I_i, a) = I_j$ (where $a$ is a terminal), set $\text{ACTION}[i, a] = s_j$ (Shift to state $j$).
* **Reduce Action**: If item $[A \to \alpha \cdot] \in I_i$ (where $A \neq S'$), then for **ALL terminals $a \in \text{FOLLOW}(A)$**, set $\text{ACTION}[i, a] = r_k$ (Reduce by production rule $k$).
* **Accept Action**: If $[S' \to S \cdot] \in I_i$, set $\text{ACTION}[i, \$] = \text{ACCEPT}$.
* **GOTO Table**: If $\text{GOTO}(I_i, A) = I_j$ (where $A$ is a non-terminal), set $\text{GOTO}[i, A] = j$.

---

### ⚠️ Mathematical Proof of Shift-Reduce (S/R) Conflict (High-Frequency Exam Hit)

> **Dr. Soni's Question**: *"Construct SLR(1) parsing table and prove whether the grammar is SLR(1) or not through Shift-Reduce conflict."*

#### Mathematical Condition for S/R Conflict:
A Shift-Reduce conflict occurs in an SLR(1) parser if and only if there exists a state $I_i$ containing:
1. A shift item: $[A \to \alpha \cdot a \beta]$ (where $a$ is a terminal), AND
2. A reduce item: $[B \to \gamma \cdot]$
such that:
$$a \in \text{FOLLOW}(B)$$

When this happens, the parser cannot decide whether to shift terminal $a$ (action $s_j$) or reduce by rule $B \to \gamma$ (action $r_k$) on input $a$:
$$\text{ACTION}[i, a] = \{s_j, r_k\} \implies \text{MULTIPLE ENTRIES IN CELL!}$$

#### 📝 Worked Exam Example (The "Dangling-Else" Grammar):
Grammar:
1. $S \to i E t S$
2. $S \to i E t S e S$
3. $S \to a$
4. $E \to b$

Consider item set $I_4$ containing:
* $[S \to i E t S \cdot e S]$ &nbsp;&nbsp;&nbsp;&nbsp;*(Wants to SHIFT on terminal $e$)*
* $[S \to i E t S \cdot]$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*(Wants to REDUCE by rule 1 on $\text{FOLLOW}(S)$)*

Since $e \in \text{FOLLOW}(S)$, on lookahead symbol $e$, the table cell $\text{ACTION}[4, e]$ receives:
$$\text{ACTION}[4, e] = \{s_5, r_1\}$$
**Conclusion**: Because cell $[4, e]$ contains both a Shift and a Reduce action, there is an **S/R Conflict**. Therefore, the grammar is **NOT SLR(1)**! *(Full 10 Marks!)*

---

## 5. CLR(1), LALR(1) & Reduce-Reduce (R/R) Conflict

* **LR(1) Item**: A pair $[A \to \alpha \cdot \beta, a]$ where $a \in T \cup \{\$\}$ is the lookahead terminal.
* **CLR(1) Table**: Uses exact lookaheads to place reduce actions. Has many states (up to hundreds).
* **LALR(1) Table**: Merges CLR(1) states that have the same core (the same productions without lookaheads).
* **Reduce-Reduce (R/R) Conflict**: Occurs when a single state contains two distinct completed items $[A \to \alpha \cdot, a]$ and $[B \to \beta \cdot, a]$ with the same lookahead $a$. LALR parsing may introduce R/R conflicts that did not exist in CLR(1).
