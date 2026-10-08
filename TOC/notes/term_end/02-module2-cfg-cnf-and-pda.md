# 📘 Module 2: Context-Free Grammars, CNF & Pushdown Automata

> **Module Focus**: CFG 4-Tuple, Ambiguity Proofs, Chomsky Normal Form (CNF) 4-Step Conversion, Pushdown Automata (PDA) 7-Tuple, and Instantaneous Description (ID) Traces.  
> **Weightage in FAT**: Approx 20 Marks.  
> **Faculty Requirement**: 2 parse trees for ambiguity, strict sequence for CNF, and full 7-tuples for PDA.

---

## 1. Context-Free Grammar (CFG) Formal 4-Tuple

A Context-Free Grammar is formally defined as:
$$G = (V, T, P, S)$$

* **$V$**: Finite set of **Variables / Non-terminals** (written in uppercase: $S, A, B, E$).
* **$T$**: Finite set of **Terminals / Alphabet** (written in lowercase: $a, b, id, +, *$).
* **$P$**: Finite set of **Production rules** of the form $A \to \alpha$, where $A \in V$ and $\alpha \in (V \cup T)^*$.
* **$S$**: The **Start symbol** ($S \in V$).

---

## 2. Ambiguity Proof (Guaranteed 5-Mark Question)

> ⚠️ **EXAM RULE**:  
> To prove that a grammar $G$ is **ambiguous**, you MUST pick **one specific string $w$** and show either:
> 1. Two distinct **Parse Trees**, OR
> 2. Two distinct **Leftmost Derivations (LMD)**.

### 📝 Classic Exam Problem: Ambiguity of Expression Grammar
> **Problem**: Prove that the grammar $E \to E + E \mid E * E \mid id$ is ambiguous.
>
> **Solution**:
> Pick the string: **$w = id + id * id$**.
>
> **Leftmost Derivation 1 (Addition first)**:
> $$E \implies E + E \implies id + E \implies id + E * E \implies id + id * E \implies id + id * id$$
>
> **Leftmost Derivation 2 (Multiplication first)**:
> $$E \implies E * E \implies E + E * E \implies id + E * E \implies id + id * E \implies id + id * id$$
>
> **Parse Tree 1** (Left-heavy: evaluates `(id + id) * id`):
> ```text
>        E
>       /|\
>      E  *  E
>     /|\    |
>    E + E   id
>    |   |
>   id   id
> ```
>
> **Parse Tree 2** (Right-heavy: evaluates `id + (id * id)`):
> ```text
>        E
>       /|\
>      E  +  E
>      |    /|\
>     id   E  *  E
>          |     |
>         id    id
> ```
> **Conclusion**: Since the string $w = id + id * id$ has two distinct parse trees (and two distinct leftmost derivations), the grammar is **AMBIGUOUS**. *(Full 5 Marks!)*

---

## 3. Chomsky Normal Form (CNF) Conversion: The Strict 4-Step Algorithm (10 Marks)

> 💡 **What is CNF?**  
> A grammar is in Chomsky Normal Form if all production rules are strictly of the form:
> 1. **$A \to BC$** (Exactly two non-terminals)
> 2. **$A \to a$** (Exactly one terminal)
> *(Exception: $S \to \epsilon$ is allowed only if $\epsilon \in L(G)$, and $S$ never appears on any RHS).*

Dr. Gaurav Soni demands that you follow the **strict sequence of 4 steps**. Swapping the order loses marks!

```text
┌────────────────────────────────────────────────────────────────────────┐
│           THE STRICT 4-STEP CNF CONVERSION ALGORITHM                   │
├────────────────────────────────────────────────────────────────────────┤
│ Step 1: Eliminate ε-productions (Find nullable variables)             │
│ Step 2: Eliminate Unit productions (A → B)                             │
│ Step 3: Eliminate Useless symbols (Non-generating & Non-reachable)     │
│ Step 4: Convert remaining productions to binary variables & terminals  │
└────────────────────────────────────────────────────────────────────────┘
```

---

### 📝 Worked 10-Mark Exam Problem: CNF Conversion

> **Problem**: Convert the following CFG into Chomsky Normal Form (CNF):
> $$S \to aSa \mid bSb \mid a \mid b \mid \epsilon$$

#### Step 1: Eliminate $\epsilon$-Productions
* Nullable variables: $S$ is nullable since $S \to \epsilon$.
* For each rule containing $S$, write all combinations with and without $S$:
  - From $S \to aSa$: without $S$, we get $S \to aa$.
  - From $S \to bSb$: without $S$, we get $S \to bb$.
* Delete $S \to \epsilon$.
* The resulting grammar $P_1$:
  $$S \to aSa \mid aa \mid bSb \mid bb \mid a \mid b$$

#### Step 2: Eliminate Unit Productions
* Check for productions of the form $A \to B$ where both are single non-terminals.
* There are no unit productions in $P_1$. (Skip to Step 3).

#### Step 3: Eliminate Useless Symbols
* **Generating Symbols**: All symbols generate strings of terminals ($S \to a$). All are generating.
* **Reachable Symbols**: $S$ can reach all symbols. All are reachable.
* No useless symbols to delete.

#### Step 4: Enforce Binary Variables & Terminals
All rules must be $A \to BC$ or $A \to a$.
Current rules:
- $S \to a$ and $S \to b$ are already in valid CNF form ($A \to a$).
- $S \to aa$: Introduce variable $X_a \to a$. Then $S \to X_a X_a$ (Valid CNF!).
- $S \to bb$: Introduce variable $X_b \to b$. Then $S \to X_b X_b$ (Valid CNF!).
- $S \to aSa$: Replace terminals with variables $\to S \to X_a S X_a$.
  Length is 3 (too long). Break into binary:
  Introduce $C_1 \to S X_a$.
  Then $S \to X_a C_1$ (Valid CNF!).
- $S \to bSb$: Replace terminals with variables $\to S \to X_b S X_b$.
  Introduce $C_2 \to S X_b$.
  Then $S \to X_b C_2$ (Valid CNF!).

#### Final CNF Grammar:
$$\begin{aligned}
S &\to X_a C_1 \mid X_b C_2 \mid X_a X_a \mid X_b X_b \mid a \mid b \\
C_1 &\to S X_a \\
C_2 &\to S X_b \\
X_a &\to a \\
X_b &\to b
\end{aligned}$$
*(Every single production is either $A \to BC$ or $A \to a$. Full 10 Marks!)*

---

## 4. Pushdown Automata (PDA): Formal 7-Tuple & String Tracing (10 Marks)

A Pushdown Automaton is a finite automaton equipped with an auxiliary **LIFO Stack** of infinite capacity.

### The Formal 7-Tuple Definition
A PDA is formally defined as:
$$M = (Q, \Sigma, \Gamma, \delta, q_0, Z_0, F)$$

| Tuple | Meaning | Exam Example |
| :--- | :--- | :--- |
| **$Q$** | Finite set of states | $Q = \{q_0, q_1, q_2\}$ |
| **$\Sigma$** | Finite input alphabet | $\Sigma = \{0, 1\}$ |
| **$\Gamma$** | Finite stack alphabet | $\Gamma = \{0, Z_0\}$ |
| **$\delta$** | Transition function | $\delta: Q \times (\Sigma \cup \{\epsilon\}) \times \Gamma \to 2^{Q \times \Gamma^*}$ |
| **$q_0$** | Initial state | $q_0 \in Q$ |
| **$Z_0$** | Initial stack start symbol | $Z_0 \in \Gamma$ |
| **$F$** | Set of final / accepting states | $F = \{q_2\}$ |

---

### 📝 Worked 10-Mark Problem: Design PDA for $L = \{0^n 1^n \mid n \ge 1\}$

> **Design Strategy**:
> 1. In state $q_0$, for every $0$ read from input, push $0$ onto the stack.
> 2. When the first $1$ is encountered, transition to state $q_1$ and pop a $0$ from the stack.
> 3. For each subsequent $1$, remain in state $q_1$ and pop a $0$.
> 4. If all input is read and the stack top is $Z_0$, transition to accepting state $q_2$.

#### Formal Transition Function $\delta$:
1. $\delta(q_0, 0, Z_0) = \{(q_0, 0Z_0)\}$ &nbsp;&nbsp;*(Push first 0)*
2. $\delta(q_0, 0, 0) = \{(q_0, 00)\}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*(Push subsequent 0s)*
3. $\delta(q_0, 1, 0) = \{(q_1, \epsilon)\}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*(First 1: switch to $q_1$, pop 0)*
4. $\delta(q_1, 1, 0) = \{(q_1, \epsilon)\}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*(Pop 0 for each 1)*
5. $\delta(q_1, \epsilon, Z_0) = \{(q_2, Z_0)\}$ &nbsp;&nbsp;&nbsp;&nbsp;*(Input finished, stack clean $\to$ move to final state)*

#### Validation: Instantaneous Description (ID) Trace for String $w = 0011$
> You must write the $\vdash$ sequence line by line:
> $$\begin{aligned}
> (q_0, 0011, Z_0) &\vdash (q_0, 011, 0Z_0) \\
> &\vdash (q_0, 11, 00Z_0) \\
> &\vdash (q_1, 1, 0Z_0) \\
> &\vdash (q_1, \epsilon, Z_0) \\
> &\vdash (q_2, \epsilon, Z_0)
> \end{aligned}$$
> Since the PDA reached final state $q_2 \in F$ after consuming all input symbols, the string $0011$ is **ACCEPTED**. *(Full 10 Marks!)*
