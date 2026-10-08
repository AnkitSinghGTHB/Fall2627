# 📘 Module 4: Turing Machines, Chomsky Hierarchy & Undecidability

> **Module Focus**: Dr. Gaurav Soni's Mandatory 6-Part TM Construction Rubric, Solved High-Frequency TMs ($a^n b^n c^n$, Parity of 0s/1s, $a^n b^{2n}$), Chomsky Hierarchy, and the Halting Problem.  
> **Weightage in FAT**: Approx 20–25 Marks.  
> **Golden Principle**: A diagram alone gets 3/10. A complete 6-part writeup gets 10/10 every time.

---

## 1. The Mandatory 6-Part Turing Machine Rubric (How to Get 10/10)

Whenever Dr. Gaurav Soni asks for a Turing Machine, write your answer with these **exact 6 numbered headings**:

```text
┌────────────────────────────────────────────────────────────────────────┐
│       DR. GAURAV SONI'S MANDATORY 6-PART ANATOMY OF A TM ANSWER        │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Language Description    : Exact mathematical set definition.       │
│ 2. Design Logic (Strategy) : Plain-English algorithm describing tape   │
│                              head movements (L, R) and symbol writes.  │
│ 3. Formal 7-Tuples         : M = (Q, Σ, Γ, δ, q₀, B, F)                │
│                              (Every single set explicitly enumerated!) │
│ 4. Transition Table        : Complete matrix of δ(q, X) = (p, Y, D).   │
│ 5. State Transition Diagram: Clean circles, start arrow, final state.  │
│ 6. Validation (ID Tracing) : Step-by-step Instantaneous Description (⊢)│
│                              demonstrating acceptance of a test string.│
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Solved Master TM 1: $L = \{a^n b^n c^n \mid n \ge 1\}$ (Guaranteed 10 Marks)

### Part 1: Language Description
$$L = \{a^n b^n c^n \mid n \ge 1\} = \{abc, aabbcc, aaabbbccc, \dots\}$$
The language consists of strings over alphabet $\Sigma = \{a, b, c\}$ where the number of $a$'s, $b$'s, and $c$'s are strictly equal and appear in sequential order.

### Part 2: Design Logic (Strategy)
1. In start state $q_0$, find the leftmost $a$, replace it with marker $X$, and move Right to state $q_1$.
2. In state $q_1$, skip over remaining $a$'s and existing $Y$'s until the first $b$ is found. Replace $b$ with marker $Y$, and move Right to state $q_2$.
3. In state $q_2$, skip over remaining $b$'s and existing $Z$'s until the first $c$ is found. Replace $c$ with marker $Z$, and move Left to state $q_3$.
4. In state $q_3$, backtrack Left across all $Z$'s, $Y$'s, $b$'s, and $a$'s until the marker $X$ is hit. Move one step Right and return to state $q_0$.
5. Repeat steps 1–4. When all $a$'s are exhausted in state $q_0$ (encountering $Y$), transition to state $q_4$ to verify that no stray $b$'s or $c$'s remain.
6. When the blank symbol $B$ is reached in state $q_4$, transition to the accepting state $q_f$ and Halt.

---

### Part 3: Formal 7-Tuples
The Turing Machine is formally defined as $M = (Q, \Sigma, \Gamma, \delta, q_0, B, F)$ where:
* **$Q$** $= \{q_0, q_1, q_2, q_3, q_4, q_f\}$
* **$\Sigma$** $= \{a, b, c\}$
* **$\Gamma$** $= \{a, b, c, X, Y, Z, B\}$
* **$q_0$** is the initial start state
* **$B$** is the blank tape symbol
* **$F$** $= \{q_f\}$ is the set of final/accepting states
* **$\delta$** is the transition function specified below:

---

### Part 4: State Transition Table
$$\delta(q, \text{Input}) = (\text{Next State}, \text{Write Symbol}, \text{Head Direction})$$

| State | Tape Symbol: $a$ | Tape Symbol: $b$ | Tape Symbol: $c$ | Tape Symbol: $X$ | Tape Symbol: $Y$ | Tape Symbol: $Z$ | Blank: $B$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$q_0$** | $(q_1, X, R)$ | — | — | — | $(q_4, Y, R)$ | — | — |
| **$q_1$** | $(q_1, a, R)$ | $(q_2, Y, R)$ | — | — | $(q_1, Y, R)$ | — | — |
| **$q_2$** | — | $(q_2, b, R)$ | $(q_3, Z, L)$ | — | — | $(q_2, Z, R)$ | — |
| **$q_3$** | $(q_3, a, L)$ | $(q_3, b, L)$ | — | $(q_0, X, R)$ | $(q_3, Y, L)$ | $(q_3, Z, L)$ | — |
| **$q_4$** | — | — | — | — | $(q_4, Y, R)$ | $(q_4, Z, R)$ | $(q_f, B, R)$ |
| ***$q_f$**| — | — | — | — | — | — | **HALT** |

---

### Part 5: State Transition Diagram
```text
           (a, a, R), (Y, Y, R)              (b, b, R), (Z, Z, R)
               ┌──────┐                          ┌──────┐
               │  ↺   │                          │  ↺   │
               ▼      │                          ▼      │
   ──►( q₀ ) ───────► ( q₁ ) ──────────────────► ( q₂ )
        │   (a,X,R)             (b,Y,R)             │
        │                                           │ (c,Z,L)
        │ (Y,Y,R)                                   ▼
        │             (a,a,L), (b,b,L), (Y,Y,L), (Z,Z,L)
        ▼                   ┌──────┐                │
      ( q₄ ) ◄──────────────│  ↺   │◄───────────────┘
        │      (X,X,R)      ▼      │     (q₃)
        │                 ( q₃ )───┘
        │ (B,B,R)
        ▼
     (( q_f )) [HALT & ACCEPT]
```

---

### Part 6: Validation (Instantaneous Description Trace)
Test with input string: **$w = aabbcc$**:
$$\begin{aligned}
q_0 aabbcc B &\vdash X q_1 abbcc B \\
&\vdash Xa q_1 bbcc B \\
&\vdash XaY q_2 bcc B \\
&\vdash XaYb q_2 cc B \\
&\vdash XaY q_3 bZc B \\
&\vdash Xa q_3 YbZc B \\
&\vdash X q_3 aYbZc B \\
&\vdash q_3 XaYbZc B \\
&\vdash X q_0 aYbZc B \\
&\vdash XX q_1 YbZc B \\
&\vdash XXY q_1 bZc B \\
&\vdash XXYY q_2 Zc B \\
&\vdash XXYYZ q_2 c B \\
&\vdash XXYY q_3 ZZ B \\
&\dots \vdash XX q_0 YYZZ B \\
&\vdash XXY q_4 YZZ B \vdash XXYY q_4 ZZ B \vdash XXYYZZ q_4 B \vdash XXYYZZ B q_f B \text{ (ACCEPT!)}
\end{aligned}$$
**Conclusion**: Since the TM reaches final state $q_f$ and halts, the string $aabbcc$ is **ACCEPTED**. *(Full 10/10 Marks!)*

---

## 3. Solved Master TM 2: Even Number of 0s and Odd Number of 1s (10 Marks)

> **Source**: Directly listed in `turing.txt` and past CAT-2 questions.

### 1. Language Description
$$L = \{w \in \{0, 1\}^* \mid \text{Count of 0's is EVEN and Count of 1's is ODD}\}$$

### 2. Design Logic (4 Modulo States)
A Turing Machine only needs 4 states to track the parity of two independent binary variables:
* **$q_{00}$**: Even 0s, Even 1s (Start State).
* **$q_{01}$**: Even 0s, **Odd 1s** (**Final / Accepting State**).
* **$q_{10}$**: Odd 0s, Even 1s.
* **$q_{11}$**: Odd 0s, Odd 1s.

The tape head scans the input from left to right without changing the tape symbols:
* Reading `0` toggles the first index ($0 \leftrightarrow 1$).
* Reading `1` toggles the second index ($0 \leftrightarrow 1$).
* When blank $B$ is reached, if the machine is in state $q_{01}$, it transitions to $q_f$ and halts.

### 3. Formal 7-Tuples
$M = (Q, \Sigma, \Gamma, \delta, q_{00}, B, \{q_f\})$ where:
* $Q = \{q_{00}, q_{01}, q_{10}, q_{11}, q_f\}$
* $\Sigma = \{0, 1\}$, $\Gamma = \{0, 1, B\}$
* Start state $= q_{00}$, Final state $= \{q_f\}$

### 4. Transition Table
| State | Tape Symbol: 0 | Tape Symbol: 1 | Blank: $B$ |
| :---: | :---: | :---: | :---: |
| **→ $q_{00}$** | $(q_{10}, 0, R)$ | $(q_{01}, 1, R)$ | — |
| **$q_{01}$** | $(q_{11}, 0, R)$ | $(q_{00}, 1, R)$ | $(q_f, B, R)$ **[ACCEPT]** |
| **$q_{10}$** | $(q_{00}, 0, R)$ | $(q_{11}, 1, R)$ | — |
| **$q_{11}$** | $(q_{01}, 0, R)$ | $(q_{10}, 1, R)$ | — |
| ***$q_f$** | — | — | **HALT** |

### 5. Validation Trace for String $w = 001$:
$$q_{00} 001 B \vdash 0 q_{10} 01 B \vdash 00 q_{00} 1 B \vdash 001 q_{01} B \vdash 001 B q_f B \text{ (ACCEPTED!)}$$
String has two 0s (Even) and one 1 (Odd) $\implies$ Correctly accepted!

---

## 4. The Chomsky Hierarchy Table (High-Frequency 5-Mark Question)

```text
┌───────┬──────────────────────────┬──────────────────────┬───────────────────────────────┐
│ Type  │ Language Recognized      │ Automaton Model      │ Production Rule Format        │
├───────┼──────────────────────────┼──────────────────────┼───────────────────────────────┤
│Type 0 │ Recursively Enumerable   │ Turing Machine       │ α → β (No restrictions)       │
│Type 1 │ Context-Sensitive (CSL)  │ Linear Bounded (LBA) │ α → β with |α| ≤ |β|          │
│Type 2 │ Context-Free (CFL)       │ Pushdown Automata    │ A → α (Single variable on LHS)│
│Type 3 │ Regular Language         │ Finite Automaton     │ A → aB or A → a (Linear)      │
└───────┴──────────────────────────┴──────────────────────┴───────────────────────────────┘
```

---

## 5. The Halting Problem of Turing Machine (Proof of Undecidability)

> **Theorem**: The Halting Problem of a Turing Machine is **UNDECIDABLE**. There is no general algorithm that can decide whether an arbitrary Turing Machine $M$ will halt on input $w$.

### 📝 Proof by Contradiction (Diagonalization):
1. **Assumption**: Suppose there exists a decider Turing Machine $H$ that solves the halting problem:
   $$H(M, w) = \begin{cases} \text{HALT / YES}, & \text{if } M \text{ halts on input } w \\ \text{LOOP / NO}, & \text{if } M \text{ loops forever on input } w \end{cases}$$
2. **Construct Adversary Machine $D$**: Construct a new machine $D$ that takes the description of a Turing Machine $\langle M \rangle$ as input and runs $H$ on $(M, \langle M \rangle)$:
   - If $H$ says $M$ halts on $\langle M \rangle$, then $D$ enters an **infinite loop**.
   - If $H$ says $M$ loops on $\langle M \rangle$, then $D$ **halts immediately**.
3. **The Contradiction**: What happens when $D$ is fed its own description $\langle D \rangle$?
   - If $D$ halts on $\langle D \rangle \implies H(D, \langle D \rangle) = \text{YES} \implies D$ loops forever! (Contradiction!)
   - If $D$ loops on $\langle D \rangle \implies H(D, \langle D \rangle) = \text{NO} \implies D$ halts! (Contradiction!)
4. **Conclusion**: The assumption that machine $H$ exists leads to an impossible logical contradiction. Therefore, **the Halting Problem is UNDECIDABLE**. *(Full 5 Marks!)*
