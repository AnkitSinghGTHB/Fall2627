# 📘 Module 1: Finite Automata, Minimization & Regular Languages

> **Module Focus**: DFA, NFA, $\epsilon$-NFA, Subset Construction, DFA Minimization (Table-Filling Method), Regular Expressions, Arden's Theorem, Pumping Lemma for Regular Languages, and LEX.  
> **Weightage in FAT**: Approx 15–20 Marks.  
> **Faculty Requirement**: Formal 5-Tuples, complete transition tables, and step-by-step algorithms.

---

## 1. Formal Definition of Finite Automata (The Mandatory 5-Tuple)

> ⚠️ **DR. SONI MARKING RULE**:  
> Whenever a question asks *"Design a DFA/NFA to accept..."*, **never just draw the state diagram**. You MUST write the formal 5-tuple first, or you will lose up to 40% of the marks!

A Finite Automaton is formally defined as a 5-tuple:
$$M = (Q, \Sigma, \delta, q_0, F)$$

| Component | Meaning | Mathematical Specification |
| :--- | :--- | :--- |
| **$Q$** | Finite set of internal states | Explicitly list all states: e.g., $Q = \{q_0, q_1, q_2\}$ |
| **$\Sigma$** | Finite input alphabet | Explicitly list symbols: e.g., $\Sigma = \{a, b\}$ or $\{0, 1\}$ |
| **$\delta$** | State transition function | **DFA**: $\delta: Q \times \Sigma \to Q$<br>**NFA**: $\delta: Q \times \Sigma \to 2^Q$ (Power set)<br>**$\epsilon$-NFA**: $\delta: Q \times (\Sigma \cup \{\epsilon\}) \to 2^Q$ |
| **$q_0$** | Initial / start state | $q_0 \in Q$ (Indicated by an incoming arrow $\to$) |
| **$F$** | Set of accepting / final states | $F \subseteq Q$ (Indicated by double concentric circles) |

---

## 2. NFA to DFA Conversion: Subset Construction Method

### The Algorithm (Step-by-Step)
1. **Initial DFA State**: Start state of DFA is $[q_0]$ (or $\epsilon\text{-closure}(q_0)$ for $\epsilon$-NFA).
2. **Transition Computation**: For each new composite DFA state $[q_1, q_2, \dots]$ and each input symbol $a \in \Sigma$:
   $$\delta_{\text{DFA}}([q_1, q_2, \dots], a) = \bigcup_{i} \delta_{\text{NFA}}(q_i, a)$$
3. **Dead State**: If $\delta(q_i, a) = \emptyset$, create a trap/dead state $[\phi]$.
4. **Final States Identification**: Any composite DFA state that contains **at least one** original final state of the NFA becomes a final state in the DFA.

```text
Example NFA to DFA Transition Table:
┌─────────────────┬───────────────────┬───────────────────┐
│   DFA State     │     Input: 0      │     Input: 1      │
├─────────────────┼───────────────────┼───────────────────┤
│  → [q₀]         │     [q₀, q₁]      │       [q₀]        │
│  * [q₀, q₁]     │     [q₀, q₁]      │     [q₀, q₂]      │
│  * [q₀, q₂]     │     [q₀, q₁]      │       [q₀]        │
└─────────────────┴───────────────────┴───────────────────┘
(* indicates accepting state if q₁ or q₂ was final in NFA)
```

---

## 3. DFA Minimization: Myhill-Nerode Table-Filling Method (Guaranteed 10 Marks)

This is one of Dr. Gaurav Soni's favorite 10-mark questions. Evaluators check your **triangular table** and **step-by-step reasoning**.

### 🛠️ The 5-Step Minimization Recipe

* **Step 1: Remove Unreachable States**  
  Trace all paths from the start state $q_0$. Any state that has no path leading to it from $q_0$ is deleted immediately.

* **Step 2: Construct the Lower Triangular Grid**  
  Draw a table of all unordered pairs of states $(p, q)$ where $p \neq q$:
  - Columns: $q_0$ to $q_{n-1}$
  - Rows: $q_1$ to $q_n$

* **Step 3: Basis Marking (0-Equivalence)**  
  For every pair $(p, q)$, mark it with an **`X`** if **one state is final ($p \in F$) and the other is non-final ($q \notin F$)**.  
  *(A final state can never be equivalent to a non-final state!)*

* **Step 4: Inductive Marking (1-Equivalence and Beyond)**  
  For each currently **unmarked** pair $(p, q)$:
  - For every input symbol $a \in \Sigma$, find their target pair: $(p', q') = (\delta(p, a), \delta(q, a))$.
  - If the target pair $(p', q')$ is **already marked with `X`**, then mark $(p, q)$ with **`X`**.
  - Repeat this loop until an entire pass completes with **no new marks added**.

* **Step 5: Merge Unmarked States & Draw Minimized DFA**  
  Any pairs that remain unmarked at the end are **indistinguishable (equivalent)**. Merge them into a single state (e.g. $[B, D]$) and draw the final minimized DFA.

---

### 📝 Worked 10-Mark Exam Problem: DFA Minimization

> **Problem**: Minimize the following DFA with states $\{A, B, C, D, E, F\}$, start state $A$, final state $C$, and transitions:
> * $\delta(A, 0) = B$, $\delta(A, 1) = C$
> * $\delta(B, 0) = A$, $\delta(B, 1) = D$
> * $\delta(C, 0) = E$, $\delta(C, 1) = F$ (Final State)
> * $\delta(D, 0) = E$, $\delta(D, 1) = F$
> * $\delta(E, 0) = E$, $\delta(E, 1) = F$
> * $\delta(F, 0) = F$, $\delta(F, 1) = F$

#### Step 1: Reachability Check
* Start state $A \to B, C$. From $B \to D$. From $C, D \to E, F$. All states $\{A, B, C, D, E, F\}$ are reachable. None removed.

#### Step 2 & 3: Basis Marking (Final vs Non-Final)
* Final state: $\{C\}$. Non-final states: $\{A, B, D, E, F\}$.
* Mark all pairs involving $C$ with `X`: $(C, A), (C, B), (C, D), (C, E), (C, F)$ are marked `X`.

```text
Triangular Grid after Basis Step:
B  |  -
C  |  X   X
D  |  -   -   X
E  |  -   -   X   -
F  |  -   -   X   -   -
   +-------------------
      A   B   C   D   E
```

#### Step 4: Inductive Checking
1. Check $(A, B)$:
   - On $0$: $(\delta(A,0), \delta(B,0)) = (B, A) \to$ unmarked.
   - On $1$: $(\delta(A,1), \delta(B,1)) = (C, D) \to$ **MARKED `X`**!
   - Therefore, mark $(A, B)$ with **`X`**.
2. Check $(D, E)$:
   - On $0$: $(\delta(D,0), \delta(E,0)) = (E, E) \to$ same state (no mark).
   - On $1$: $(\delta(D,1), \delta(E,1)) = (F, F) \to$ same state (no mark).
   - Both targets are identical! **$(D, E)$ remains UNMARKED.**
3. Check $(D, F)$:
   - On $0$: $(E, F) \to$ currently unmarked.
   - On $1$: $(F, F) \to$ same.
4. Check $(E, F)$:
   - On $0$: $(E, F) \to$ same pair.
   - On $1$: $(F, F) \to$ same.
   - **$(E, F)$ remains UNMARKED.**
5. By transitivity, $\{D, E, F\}$ are all pairwise equivalent!

#### Step 5: Minimized States & Final Diagram
* Equivalent groups: $\{A\}$, $\{B\}$, $\{C\}$, $\{D, E, F\}$.
* The 6-state DFA reduces to a **4-state DFA**!

```text
Minimized DFA Transition Table:
┌─────────────────┬───────────────────┬───────────────────┐
│     State       │     Input: 0      │     Input: 1      │
├─────────────────┼───────────────────┼───────────────────┤
│    → A          │         B         │         C         │
│      B          │         A         │      [D,E,F]      │
│    * C          │      [D,E,F]      │      [D,E,F]      │
│   [D,E,F]       │      [D,E,F]      │      [D,E,F]      │
└─────────────────┴───────────────────┴───────────────────┘
```

---

## 4. Pumping Lemma for Regular Languages (Proof by Contradiction)

To prove a language $L$ is **NOT regular**, you play a 4-step game of contradiction against an adversary.

### 📜 The Formal Statement of Pumping Lemma
If $L$ is a regular language, there exists an integer $p \ge 1$ (the pumping length) such that any string $s \in L$ with $|s| \ge p$ can be divided into three parts:
$$s = x y z$$
satisfying the following **3 Mandatory Conditions**:
1. $|y| \ge 1$ ($y$ is not empty, i.e., $y \neq \epsilon$).
2. $|xy| \le p$ (the pumped part $y$ occurs within the first $p$ symbols).
3. For all $i \ge 0$, $x y^i z \in L$.

---

### 📝 Classic Exam Proof: Show $L = \{0^n 1^n \mid n \ge 1\}$ is Not Regular

> **Model Solution for Exam**:
> 1. **Assumption**: Assume for the sake of contradiction that $L$ is regular.
> 2. **Pumping Length**: By the Pumping Lemma, there exists a pumping length $p \ge 1$.
> 3. **Choose String $s$**: Choose string $s = 0^p 1^p$. Clearly, $s \in L$ and $|s| = 2p \ge p$.
> 4. **Decomposition $s = xyz$**: By condition (2), $|xy| \le p$. Since the first $p$ symbols of $s$ are all zeros, both $x$ and $y$ must consist exclusively of zeros:
>    $$x = 0^j, \quad y = 0^k \ (k \ge 1), \quad z = 0^{p - j - k} 1^p$$
> 5. **Pumping Step**: Choose $i = 2$. Consider the pumped string $s' = x y^2 z$:
>    $$s' = 0^j (0^k)^2 0^{p - j - k} 1^p = 0^{p + k} 1^p$$
> 6. **Contradiction**: Since $k \ge 1$, the number of zeros is $p + k > p$, while the number of ones remains $p$.  
>    Therefore, the number of zeros does not equal the number of ones $\implies s' \notin L$.
> 7. **Conclusion**: This contradicts condition (3) of the Pumping Lemma. Hence, our initial assumption was false. **$L$ is NOT a regular language.** *(Full 5/5 Marks!)*

---

## 5. Lexical Analysis & LEX Program Structure (2–5 Marks)

In Compiler Design (CO1), the Lexical Analyzer converts source code text into **tokens**.

* **Token**: Abstract symbol representing a grammatical unit (e.g., `id`, `num`, `if`, `relop`).
* **Lexeme**: The actual character sequence matching the token pattern (e.g., `count`, `3.14`, `==`).
* **Pattern**: The formal rule (usually a Regular Expression) describing the lexeme.

### Structure of a LEX Specification File (`.l`)
```c
%{
/* Section 1: Declarations (C headers, macros) */
#include <stdio.h>
%}

/* Definitions / Aliases */
digit   [0-9]
letter  [a-zA-Z]

%%
/* Section 2: Translation Rules (Pattern { Action }) */
"if"            { printf("Keyword: IF\n"); }
"else"          { printf("Keyword: ELSE\n"); }
{letter}({letter}|{digit})*  { printf("Identifier: %s\n", yytext); }
{digit}+        { printf("Integer: %s\n", yytext); }
[ \t\n]+        { /* Ignore whitespace */ }
.               { printf("Unknown character: %s\n", yytext); }
%%

/* Section 3: Auxiliary C Functions */
int main() {
    yylex();
    return 0;
}
int yywrap() { return 1; }
```
