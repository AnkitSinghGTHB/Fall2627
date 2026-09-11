# ⚡ CAT-2 HOTS Master Crib — Module 2: CFG, CNF, GNF & Pushdown Automata
**Course**: CSE2004 — Theory of Computation & Compiler Design  
**Level**: Self-Contained & Fully Visual (From Bedrock Basics to Class Notes & HOTS)  
**Exam Mode**: Open Book / Handwritten Notes Allowed | **Target Score**: 45+ / 50

---

## 🧱 TIER 0: The "Explain Like I'm 5" Bedrock Basics
*(Read this first if you think TOC makes zero sense)*

### 1. What is Ambiguity? (Visual Parse Trees)
A grammar is ambiguous if the SAME string has **TWO DIFFERENT PARSE TREES**:

#### String: $id + id * id$
```mermaid
graph TD
    subgraph Tree_1 ["Tree 1: Evaluates as (id + id) * id"]
    E1["E"] --> E2["E"]
    E1 --> MUL1["*"]
    E1 --> E3["E"]
    E2 --> E4["E"]
    E2 --> PLUS1["+"]
    E2 --> E5["E"]
    E4 --> id1["id"]
    E5 --> id2["id"]
    E3 --> id3["id"]
    end

    subgraph Tree_2 ["Tree 2: Evaluates as id + (id * id)"]
    T1["E"] --> T2["E"]
    T1 --> PLUS2["+"]
    T1 --> T3["E"]
    T2 --> id4["id"]
    T3 --> T4["E"]
    T3 --> MUL2["*"]
    T3 --> T5["E"]
    T4 --> id5["id"]
    T5 --> id6["id"]
    end
```
> Because both trees generate the identical string $id + id * id$ with different structures $\implies$ **AMBIGUOUS ✅**.

---

### 2. What is a Pushdown Automaton (PDA)? (State Diagram)
A DFA with an infinite **Pringles Can (Stack)**:

#### State Diagram for $L = \{a^n b^n \mid n \ge 1\}$:
```mermaid
stateDiagram-v2
    direction LR
    [*] --> q0: Start with Z0 on stack
    q0 --> q0: a, Z0 / A Z0<br>a, A / A A<br>(PUSH PHASE)
    q0 --> q1: b, A / ε<br>(TRANSITION: Pop first A)
    q1 --> q1: b, A / ε<br>(POP PHASE)
    q1 --> qf: ε, Z0 / Z0<br>(ACCEPTANCE)
    qf --> [*]
```

#### State Diagram for Palindrome with Center Marker $L = \{w c w^R\}$:
```mermaid
stateDiagram-v2
    direction LR
    [*] --> q0: Start
    q0 --> q0: a, X / a X<br>b, X / b X<br>(Push letters of w)
    q0 --> q1: c, X / X<br>(Center marker: don't touch stack)
    q1 --> q1: a, a / ε<br>b, b / ε<br>(Match & Pop letters of w^R)
    q1 --> qf: ε, Z0 / Z0<br>(Stack empty: ACCEPT)
    qf --> [*]
```

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If Question Shows / Asks... | It Means This Exact Topic | What You Do (In 5 Seconds) |
| :--- | :--- | :--- |
| Grammar with rules, "Compute FIRST and FOLLOW" | **First & Follow Calculation** | First = all initial letters generated. Follow = immediate right neighbor in all RHS + $\$$ to start symbol! |
| "Show the grammar is ambiguous" | **Ambiguity Proof** | Draw Tree 1 and Tree 2 side-by-side! |
| "Convert grammar to CNF" | **4-Step CNF Algorithm** | 1. Remove $\epsilon$-rules $\to$ 2. Remove Unit rules $\to$ 3. Remove Useless symbols $\to$ 4. Binary variables/single terminals. |

---

## 📝 TIER 4: Solved Classroom Archetypes (From Class Notes)

### Classroom Problem 1: The Infamous `<how?>` FIRST & FOLLOW Problem
*(From Class Notes Page 3)*  
$$S \to A B C D \mid a, \quad A \to A b \mid B c \mid \epsilon, \quad B \to d B \mid \epsilon, \quad C \to c \mid \epsilon, \quad D \to g \mid h$$
* $\mathbf{\text{FIRST}(D) = \{g, h\}}$
* $\mathbf{\text{FIRST}(C) = \{c, \epsilon\}}$
* $\mathbf{\text{FIRST}(B) = \{d, \epsilon\}}$
* $\mathbf{\text{FIRST}(A) = \{c, d, \epsilon\}}$
* $\mathbf{\text{FIRST}(S) = \{a, c, d, g, h\}}$
