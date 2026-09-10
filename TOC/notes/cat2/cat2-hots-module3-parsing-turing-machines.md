# ⚡ CAT-2 HOTS Master Crib — Module 3 & 4: Parsing & Turing Machines
**Course**: CSE2004 — Theory of Computation & Compiler Design  
**Coverage**: LL(1), SLR(1) Parsing & Turing Machines | **Exam Mode**: Open Book / Notes Allowed  
**Target Score**: 45+ / 50 (S-Grade Boundary)

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If Question Mentions / Shows... | It Means This Exact Topic | Your Immediate Formula / Action |
| :--- | :--- | :--- |
| "Compute FIRST and FOLLOW sets" | **First & Follow Algorithm** | First: first terminal generated. Follow: immediate terminal following variable across ALL RHS productions + add $\$$ to start variable! |
| "Construct LL(1) parsing table", "Is it LL(1)?" | **Top-Down LL(1) Parsing** | For $A \to \alpha$: Place $A \to \alpha$ in $M[A, a]$ for all $a \in \text{First}(\alpha)$. If $\epsilon \in \text{First}(\alpha)$, place in $M[A, b]$ for all $b \in \text{Follow}(A)$. Grammar is LL(1) $\iff$ **NO cell has $>1$ entry**. |
| "Left Recursion", "Left Factoring" | **LL(1) Pre-requisites** | Left Recursion ($A \to A\alpha \mid \beta$) causes infinite loop in top-down parser! Replace with $A \to \beta A'$, $A' \to \alpha A' \mid \epsilon$. |
| "Construct LR(0) items", "SLR(1) Parsing Table" | **Bottom-Up SLR(1) Parsing** | Augmented grammar $S' \to S$. Form Canonical Items using $\text{CLOSURE}$ and $\text{GOTO}$. In table: Shift on terminals; Reduce $r_j$ ONLY in columns of $\text{Follow}(A)$! |
| "Shift-Reduce / Reduce-Reduce conflict" | **Parsing Conflicts** | Cell contains both Shift and Reduce ($S_i / r_j$) or two Reduces ($r_i / r_j$). Proves grammar is **NOT SLR(1)**. |
| "Design a Turing Machine for $0^n 1^n$", Instantaneous Description (ID) | **Turing Machine Design** | 7-tuple $M = (Q, \Sigma, \Gamma, \delta, q_0, B, F)$. Transition: $\delta(q, X) = (p, Y, D)$ where $D \in \{L, R\}$. |
| "Decidability", "Halting Problem", "Chomsky Hierarchy" | **Computability & Decidability** | Halting Problem is **Undecidable**. Regular $\subset$ CFL $\subset$ CSL $\subset$ Recursive $\subset$ Recursively Enumerable. |

---

## 🛠️ TIER 2: Deterministic Algorithmic Recipes

### Recipe 3.1: FIRST and FOLLOW Master Calculation Rules
To compute sets for variables in grammar $G$:

#### Rules for $\text{FIRST}(X)$:
1. If $X$ is a terminal, $\text{FIRST}(X) = \{X\}$.
2. If $X \to \epsilon$ is a production, then add $\epsilon$ to $\text{FIRST}(X)$.
3. If $X \to Y_1 Y_2 \dots Y_k$ is a production:
   - Add all non-$\epsilon$ symbols from $\text{FIRST}(Y_1)$ to $\text{FIRST}(X)$.
   - If $\epsilon \in \text{FIRST}(Y_1)$, add $\text{FIRST}(Y_2)$, and continue through $Y_k$ as long as each preceding $Y_i$ derives $\epsilon$.
   - If all $Y_1, \dots, Y_k$ derive $\epsilon$, add $\epsilon$ to $\text{FIRST}(X)$.

#### Rules for $\text{FOLLOW}(A)$ (Variables only):
1. **Rule 1**: Add $\$$ (end-marker) to $\text{FOLLOW}(S)$, where $S$ is the start symbol.
2. **Rule 2**: If there is a production $A \to \alpha B \beta$:
   - Everything in $\text{FIRST}(\beta)$ (except $\epsilon$) is in $\text{FOLLOW}(B)$.
3. **Rule 3 (The Propagation Rule)**: If there is a production $A \to \alpha B$, OR $A \to \alpha B \beta$ where $\epsilon \in \text{FIRST}(\beta)$:
   - Everything in $\text{FOLLOW}(A)$ is also in $\text{FOLLOW}(B)$.
   - *(Note: Follow sets NEVER contain $\epsilon$!)*

---

### Recipe 3.2: Constructing an SLR(1) Parsing Table
Given grammar $G$:
1. **Augment Grammar**: Add $S' \to S$. Number all productions $0, 1, 2, \dots, n$.
2. **Canonical Collection of $LR(0)$ Items**:
   - Item: A production with a dot $\cdot$ (e.g. $A \to \alpha \cdot \beta$).
   - $\text{CLOSURE}(I)$: If $A \to \alpha \cdot B \beta \in I$, add $B \to \cdot \gamma$ for all productions of $B$.
   - $\text{GOTO}(I, X)$: Shift dot over $X$ ($A \to \alpha X \cdot \beta$) and take closure.
3. **Fill SLR(1) Parsing Table ($ACTION$ and $GOTO$)**:
   - For state $I_i$:
     - If $[A \to \alpha \cdot a \beta] \in I_i$ and $\text{GOTO}(I_i, a) = I_j$ (where $a$ is terminal):  
       Set $ACTION[i, a] = \text{Shift } j$ ($S_j$).
     - If $[A \to \alpha \cdot] \in I_i$ (where production $A \to \alpha$ is rule $k$):  
       **Set $ACTION[i, a] = \text{Reduce } k$ ($r_k$) for all terminals $a \in \text{FOLLOW}(A)$!**
     - If $[S' \to S \cdot] \in I_i$:  
       Set $ACTION[i, \$] = \text{Accept}$.
     - For variable $A$: If $\text{GOTO}(I_i, A) = I_j$, set $GOTO[i, A] = j$.

---

### Recipe 3.3: Turing Machine Design for $L = \{0^n 1^n \mid n \ge 1\}$
Strategy: Match leftmost $0$ by replacing it with $X$, move right past all $0$'s and $Y$'s to find matching $1$, replace with $Y$, move left back to next $0$, repeat.

1. **State $q_0$**: Read $0$, overwrite with $X$, move Right $\to q_1$. (If read $Y$, move Right $\to q_3$ for acceptance check).
2. **State $q_1$**: Skip all $0$'s and $Y$'s moving Right. When read first $1$, overwrite with $Y$, move Left $\to q_2$.
3. **State $q_2$**: Skip all $Y$'s and $0$'s moving Left. When read $X$, move Right $\to q_0$.
4. **State $q_3$**: Skip all $Y$'s moving Right. When read Blank $B$, move Right $\to q_4$ (Accepting State).

#### Transition Function Table:
$$\begin{array}{|c|c|c|c|c|c|} \hline \text{State} & 0 & 1 & X & Y & B \\ \hline q_0 & (q_1, X, R) & - & - & (q_3, Y, R) & - \\ q_1 & (q_1, 0, R) & (q_2, Y, L) & - & (q_1, Y, R) & - \\ q_2 & (q_2, 0, L) & - & (q_0, X, R) & (q_2, Y, L) & - \\ q_3 & - & - & - & (q_3, Y, R) & (q_4, B, R) \\ q_4 (\text{Final}) & - & - & - & - & - \\ \hline \end{array}$$

---

## 🚨 TIER 3: Faculty Trap Radar

1. **The SLR(1) Reduce Placement Trap**: In LR(0) parsing, reduce actions are placed in **all** terminal columns. In **SLR(1)**, reduce action $r_k$ is placed **ONLY** in the columns of $\mathbf{\text{FOLLOW}(A)}$! Placing reduce in all columns causes false conflicts and loses all marks!
2. **Left-Factoring Necessity in LL(1)**: If a grammar has $A \to \alpha \beta_1 \mid \alpha \beta_2$, both productions have $\text{FIRST}$ starting with $\alpha$. They will collide in cell $M[A, \alpha]$. You **must left-factor** before making an LL(1) table:
   $$A \to \alpha A', \quad A' \to \beta_1 \mid \beta_2$$
3. **Turing Machine Acceptance vs Looping**: A TM can accept (enter $q_f$), reject (halt in non-accepting state with undefined transition), or **loop infinitely**. A language is **Decidable (Recursive)** $\iff$ the TM is guaranteed to halt on all inputs!

---

## 📝 TIER 4: Master Solved HOTS Archetypes

### Archetype 1: FIRST & FOLLOW Computation with LL(1) Table
**Question**: For the grammar:
$$E \to T E'$$
$$E' \to + T E' \mid \epsilon$$
$$T \to F T'$$
$$T' \to * F T' \mid \epsilon$$
$$F \to ( E ) \mid id$$
1. Compute $\text{FIRST}$ and $\text{FOLLOW}$ for all variables.
2. Construct the LL(1) parsing table and prove the grammar is LL(1).

**Solution Template**:
1. **FIRST Sets**:
   * $\text{FIRST}(F) = \{(, id\}$
   * $\text{FIRST}(T') = \{*, \epsilon\}$
   * $\text{FIRST}(T) = \text{FIRST}(F) = \{(, id\}$
   * $\text{FIRST}(E') = \{+, \epsilon\}$
   * $\text{FIRST}(E) = \text{FIRST}(T) = \{(, id\}$
2. **FOLLOW Sets**:
   * Start symbol: $\text{FOLLOW}(E) = \{\$, )\}$ (from rule $F \to ( E )$)
   * From $E \to T E'$: $\text{FOLLOW}(E') = \text{FOLLOW}(E) = \{\$, )\}$
   * From $E \to T E'$: $\text{FOLLOW}(T) = (\text{FIRST}(E') \setminus \{\epsilon\}) \cup \text{FOLLOW}(E') = \{+, \$, )\}$
   * From $T \to F T'$: $\text{FOLLOW}(T') = \text{FOLLOW}(T) = \{+, \$, )\}$
   * From $T \to F T'$: $\text{FOLLOW}(F) = (\text{FIRST}(T') \setminus \{\epsilon\}) \cup \text{FOLLOW}(T') = \{*, +, \$, )\}$
3. **LL(1) Parsing Table $M[A, a]$**:
   $$\begin{array}{|c|c|c|c|c|c|c|} \hline \text{Non-Term} & id & + & * & ( & ) & \$ \\ \hline E & E \to T E' & & & E \to T E' & & \\ E' & & E' \to + T E' & & & E' \to \epsilon & E' \to \epsilon \\ T & T \to F T' & & & T \to F T' & & \\ T' & & T' \to \epsilon & T' \to * F T' & & T' \to \epsilon & T' \to \epsilon \\ F & F \to id & & & F \to ( E ) & & \\ \hline \end{array}$$
4. **Conclusion**: Every cell in table $M$ contains **at most ONE production**. Therefore, the grammar is **LL(1) ✅**.
