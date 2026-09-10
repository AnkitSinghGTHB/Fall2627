# ⚡ CAT-2 HOTS Master Crib — Module 2: CFG, CNF, GNF & Pushdown Automata
**Course**: CSE2004 — Theory of Computation & Compiler Design  
**Level**: Self-Contained / Zero-Assumption (From Bedrock Basics to HOTS)  
**Exam Mode**: Open Book / Handwritten Notes Allowed | **Target Score**: 45+ / 50

---

## 🧱 TIER 0: The "Explain Like I'm 5" Bedrock Basics
*(Read this first if you think TOC makes zero sense)*

### 1. What on Earth is a Grammar?
A grammar is just a **word-replacement factory**:
* **Variables / Non-Terminals (CAPITAL letters: $S, A, B$)**:
  * These are temporary placeholders. They can be replaced.
* **Terminals (lowercase letters, numbers, symbols: $a, b, +, *, id$)**:
  * These are the final bricks. Once a terminal is produced, it **CANNOT be replaced**.
* **Production Rule ($A \to a B$)**:
  * Means: *"Whenever you see the capital letter $A$, you can swap it for the letters $a B$."*
* **Start Symbol ($S$)**:
  * The initial placeholder you must always start with.

---

### 2. What is a "Derivation" & "Parse Tree"?
* **Derivation**: The step-by-step substitution process starting from $S$ until NO capital letters remain.
* **Leftmost Derivation (LMD)**: At every step, you are strictly forced to replace the **LEFTMOST capital letter first**.
* **Parse Tree**: A family tree showing which parent variable produced which children. Leaves of the tree are the final terminal letters.

---

### 3. What is Ambiguity? (The Most Common 5-Mark Question)
Think of the confusing English sentence:
> *"I saw the man with the telescope."*  
> (Did I use a telescope to see him, or was the man holding a telescope?)

In programming languages, ambiguity is disastrous!
* Consider the math expression: **$2 + 3 \times 4$**.
  * If the parser builds Tree 1: $(2 + 3) \times 4 = 20$.
  * If the parser builds Tree 2: $2 + (3 \times 4) = 14$.
* **Definition of Ambiguity**: A grammar is **AMBIGUOUS** if there exists **AT LEAST ONE string** that can produce:
  1. **TWO different parse trees**, OR
  2. **TWO different leftmost derivations**.
* **How to prove it in an exam**: Pick a simple test string (e.g. $a + a * a$). Show two different leftmost derivations for it. Boom, full marks!

---

### 4. What is Chomsky Normal Form (CNF)? (The Strict Grammar Diet)
Faculties love asking you to convert an ugly grammar into CNF.
A grammar is in **CNF** if EVERY single rule looks like ONE of these two:
1. **$A \to B C$** (Exactly **TWO capital letters** on the right).
2. **$A \to a$** (Exactly **ONE small letter** on the right).

*Nothing else is allowed!* No empty strings ($\epsilon$), no single capital letters ($A \to B$), no mixed strings ($A \to a B$).

---

### 5. What is a Pushdown Automaton (PDA)?
In CAT-1, you learned DFA/NFA. But a DFA has **finite memory**—it cannot remember how many $a$'s it saw. If you ask a DFA to check if $a^n b^n$ has equal $a$'s and $b$'s for $n = 1,000,000$, the DFA crashes!

* **A PDA is just a DFA with a Pringles Can (Stack) attached!**
  * The stack has infinite depth.
  * **$Z_0$**: A special marker sitting at the very bottom of the can so you know when it's empty.
* **How PDA checks $a^n b^n$**:
  1. Every time it sees an $a$ in the input, it drops a chip ($A$) into the can (**PUSH**).
  2. When it starts seeing $b$'s, for every $b$, it takes one chip ($A$) out of the can (**POP**).
  3. When the input finishes, if the can is back to only having $Z_0$ at the bottom, the number of $a$'s and $b$'s were equal $\implies$ **ACCEPT!**

#### How to Read PDA Transition Notation:
$$\delta(q_0, a, Z_0) = (q_0, A Z_0)$$
In plain English:
* *"I am currently in State $q_0$."*
* *"I see input letter $a$."*
* *"The top of the stack currently has $Z_0$."*
* *"Action: Stay in state $q_0$, and replace $Z_0$ with $A Z_0$ (which effectively PUSHES $A$ on top of $Z_0$)."*

$$\delta(q_1, b, A) = (q_1, \epsilon)$$
In plain English:
* *"I see input $b$, top of stack is $A$. Action: replace $A$ with $\epsilon$ (which effectively POPS $A$ off the stack!)."*

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If Question Shows / Asks... | It Means This Exact Topic | Your Immediate Formula / Action |
| :--- | :--- | :--- |
| "Show the grammar is ambiguous" | **CFG Ambiguity Proof** | Pick ONE short string $w$. Draw **TWO distinct parse trees** OR write **TWO distinct leftmost derivations** for $w$. |
| "Convert grammar to CNF" | **Chomsky Normal Form** | **Strict Order**: 1. Remove $\epsilon$-productions $\to$ 2. Remove Unit productions $\to$ 3. Remove Useless symbols $\to$ 4. Make all RHS binary variables or single terminals. |
| "Design a PDA for $L = \{a^n b^n\}$", $\{w w^R\}$ | **PDA Construction** | Define 7-tuple $M = (Q, \Sigma, \Gamma, \delta, q_0, Z_0, F)$. Write explicit transition table $\delta$. |
| "Acceptance by Empty Stack vs Final State" | **PDA Acceptance Modes** | Final State: ends in $q_f \in F$. Empty Stack: stack is empty ($\epsilon$). Inter-conversion requires adding $q_{start}, Z_0'$ and $q_{dump}$. |

---

## 🛠️ TIER 2: Step-by-Step Execution Recipes

### Recipe 1: The Strict 4-Step CNF Conversion Algorithm
> ⚠️ **DO NOT SWAP STEPS 1 AND 2!** If you do unit productions before $\epsilon$, the $\epsilon$-elimination will create new unit productions!

#### Step 1: Remove $\epsilon$-Productions ($A \to \epsilon$)
1. Find all **nullable variables** (variables that can shrink into nothing):
   - If $A \to \epsilon$, $A$ is nullable.
   - If $B \to A$ and $A$ is nullable, then $B$ is nullable.
2. Rewrite rules: For any rule containing a nullable variable, create versions with that variable present AND versions with it missing. (Delete $A \to \epsilon$).

#### Step 2: Remove Unit Productions ($A \to B$ where $B$ is a single variable)
1. If $A \to B$ and $B \to \alpha$, add $A \to \alpha$ directly to $A$.
2. Delete the unit production $A \to B$.

#### Step 3: Remove Useless Symbols
1. Remove non-generating symbols (symbols that never produce terminals).
2. Remove unreachable symbols (symbols you can never reach starting from $S$).

#### Step 4: Convert RHS to Valid CNF
1. For terminals mixed in RHS (e.g. $A \to a B$): Create variable $T_a \to a$, and rewrite as $A \to T_a B$.
2. For long RHS (e.g. $A \to B C D$): Split with new variables: $A \to B X_1$, $X_1 \to C D$.

---

### Recipe 2: PDA Design Recipe for $L = \{w c w^R \mid w \in \{a, b\}^*\}$
1. **Push Phase ($q_0$)**: As long as reading $w$ before $c$, push symbols into stack:
   - Read $a$: $\delta(q_0, a, X) = (q_0, a X)$
   - Read $b$: $\delta(q_0, b, X) = (q_0, b X)$
2. **Center Marker ($c$)**: When read $c$, do not touch stack, transition to pop state $q_1$:
   - $\delta(q_0, c, X) = (q_1, X)$
3. **Pop Phase ($q_1$)**: Read $w^R$ and verify it matches the top of stack:
   - Read $a$ and top is $a$: $\delta(q_1, a, a) = (q_1, \epsilon)$ (Match! Pop $a$).
   - Read $b$ and top is $b$: $\delta(q_1, b, b) = (q_1, \epsilon)$ (Match! Pop $b$).
4. **Acceptance ($q_f$)**: When input is finished ($\epsilon$) and stack is at $Z_0$:
   - $\delta(q_1, \epsilon, Z_0) = (q_f, Z_0)$.

---

## 🚨 TIER 3: Faculty Trap Radar

1. **One Leftmost + One Rightmost $\ne$ Ambiguity Proof**: If you give one leftmost derivation and one rightmost derivation, examiners give 0 marks! You MUST provide **TWO DIFFERENT LEFTMOST DERIVATIONS** for the exact same terminal string.
2. **DPDA vs NPDA Difference**: A deterministic PDA (DPDA) cannot recognize even palindromes $\{w w^R\}$ because it has no way to know where the middle of the word is without guessing! Only an **NPDA (Non-deterministic PDA)** can recognize $\{w w^R\}$.

---

## 📝 TIER 4: Master Solved HOTS Archetypes

### Archetype 1: Ambiguity Proof for $E \to E + E \mid E * E \mid id$
**Question**: Prove that the expression grammar $E \to E + E \mid E * E \mid id$ is ambiguous.

**Step-by-Step Solution**:
1. Choose the test string: $w = id + id * id$.
2. **Leftmost Derivation 1 (Tree 1 - Plus evaluated last)**:
   $$E \implies E * E \implies E + E * E \implies id + E * E \implies id + id * E \implies id + id * id$$
   *(Structure: $(id + id) * id$)*
3. **Leftmost Derivation 2 (Tree 2 - Multiply evaluated last)**:
   $$E \implies E + E \implies id + E \implies id + E * E \implies id + id * E \implies id + id * id$$
   *(Structure: $id + (id * id)$)*
4. **Conclusion**: Since there exist two distinct leftmost derivations (and two distinct parse trees) for the identical terminal string $w = id + id * id$, the grammar is **AMBIGUOUS ✅**.
