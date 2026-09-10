# ⚡ CAT-2 HOTS Master Crib — Module 3 & 4: Parsing & Turing Machines
**Course**: CSE2004 — Theory of Computation & Compiler Design  
**Level**: Self-Contained / Zero-Assumption (From Bedrock Basics to HOTS)  
**Exam Mode**: Open Book / Handwritten Notes Allowed | **Target Score**: 45+ / 50

---

## 🧱 TIER 0: The "Explain Like I'm 5" Bedrock Basics
*(Read this first if parsing tables look like alien hieroglyphics)*

### 1. What on Earth is a Compiler Parser?
When you write code like `int a = 5 + ;`, your compiler immediately throws a **Syntax Error**.
How did it know? The **Parser** checked your code against the grammar of the programming language.
* The parser's job is to read your stream of tokens ($id, +, *$) and construct a **Parse Tree**.

---

### 2. Top-Down vs Bottom-Up Parsing (The Two Philosophies)
* **Top-Down Parsing (LL(1))**:
  * Like an architect: Starts at the very top with the start symbol $S$, and tries to predict which child branches to build downwards to match the user's code words, looking ahead by **1 letter**.
* **Bottom-Up Parsing (SLR(1) / LR(1))**:
  * Like a bricklayer: Starts with the raw code words at the bottom ($id, +, id$) and groups them together into variables, working upwards until reaching $S$. (Much more powerful than Top-Down!).

---

### 3. What are FIRST and FOLLOW Sets in Plain English?
Before building a parser, you must calculate two sets for every variable:

#### A. $\text{FIRST}(A)$ (The Starting Letters):
* If you start replacing variable $A$ using its grammar rules, **what are all the possible FIRST terminal letters that can ever appear?**
* Example: If $A \to + T \mid * F \mid id$, then $\text{FIRST}(A) = \{+, *, id\}$.

#### B. $\text{FOLLOW}(A)$ (The Immediate Right Neighbors):
* Imagine all valid sentences in the programming language.
* If variable $A$ is sitting in a sentence, **what terminal letters are allowed to sit IMMEDIATELY to its right?**
* **The $\$ Rule$**: The start symbol $S$ always has **$\$$ (End of File)** in its $\text{FOLLOW}$ set, because nothing sits after the program except the end of the file!

---

### 4. What is Left Recursion & Why Does it Break Top-Down Parsers?
* If a grammar has a rule like:
  $$A \to A \alpha \mid \beta$$
* A top-down parser trying to expand $A$ will call $A$ again, which calls $A$ again, which calls $A$ again...
* **It gets stuck in an infinite recursion loop!**
* **The Elimination Trick**:
  $$A \to \beta A'$$
  $$A' \to \alpha A' \mid \epsilon$$
  *(Turns the dangerous left-recursion into safe right-recursion!).*

---

### 5. What is a Turing Machine (TM)?
In CAT-1 you had DFA (No memory). In Module 2 you had PDA (Pringles Can stack memory).
A **Turing Machine** is the ultimate mathematical model of a computer:
* **The Tape**: An infinite paper strip divided into squares, carrying characters or blank spaces ($B$).
* **The Head**: A pointer that can look at one square at a time.
* At every step, the Turing Machine can do 3 simple things:
  1. Read the symbol under the head.
  2. Overwrite it with a new symbol.
  3. Move the head **ONE square Left ($L$) or Right ($R$)**.
* That's it! Every computer, smartphone, and supercomputer on Earth is computationally equivalent to a simple Turing Machine.

#### How to Read TM Transition Notation:
$$\delta(q_0, 0) = (q_1, X, R)$$
In plain English:
* *"I am currently in State $q_0$."*
* *"The tape square currently has symbol $0$."*
* *"Action: Change state to $q_1$, overwrite the square with $X$, and move the tape head ONE step to the Right ($R$)."*

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If Question Shows / Asks... | It Means This Exact Topic | What You Do (In 5 Seconds) |
| :--- | :--- | :--- |
| "Compute FIRST and FOLLOW sets" | **First & Follow Algorithm** | First = first terminal generated. Follow = terminal immediately following variable + add $\$$ to start variable! |
| "Construct LL(1) parsing table", "Is it LL(1)?" | **LL(1) Table Construction** | For rule $A \to \alpha$: put it in row $A$ under columns of $\text{First}(\alpha)$. If $\epsilon \in \text{First}$, put under columns of $\text{Follow}(A)$. |
| Cell in table has 2 productions | **Grammar Conflict** | If ANY table cell has $>1$ entry $\implies$ **Grammar is NOT LL(1) ❌** (Ambiguous or not factored). |
| "Construct LR(0) items", Canonical collection | **LR Items Closure & Goto** | Put a dot $\cdot$ in rules ($A \to \cdot \alpha$). Expand variables immediately after the dot using $\text{CLOSURE}$. |
| "Design a Turing Machine for $0^n 1^n$" | **TM Design** | Cross off leftmost $0$ with $X \to$ move right to find matching $1 \to$ cross off with $Y \to$ move left back to next $0 \to$ repeat. |

---

## 🛠️ TIER 2: Step-by-Step Execution Recipes

### Recipe 1: FIRST & FOLLOW Calculation Rules
#### Finding $\text{FIRST}(X)$:
1. If $X$ is a terminal (small letter/symbol), $\text{FIRST}(X) = \{X\}$.
2. If $X \to \epsilon$, add $\epsilon$ to $\text{FIRST}(X)$.
3. If $X \to Y_1 Y_2 \dots Y_k$:
   - Add everything from $\text{FIRST}(Y_1)$ (except $\epsilon$).
   - If $\epsilon \in \text{FIRST}(Y_1)$, add $\text{FIRST}(Y_2)$. Continue down the line as long as each preceding variable can dissolve into $\epsilon$.

#### Finding $\text{FOLLOW}(A)$ (Variables only):
1. **Rule 1**: Add $\$$ to $\text{FOLLOW}(S)$ (Start Symbol).
2. **Rule 2**: Look at the RIGHT HAND SIDE of all rules where $A$ appears:
   - If you see $B \to \alpha A \beta$, add everything in $\text{FIRST}(\beta)$ (except $\epsilon$) to $\text{FOLLOW}(A)$.
3. **Rule 3**: If you see $B \to \alpha A$, OR if you see $B \to \alpha A \beta$ where $\beta$ can dissolve into $\epsilon$:
   - Add everything in $\text{FOLLOW}(B)$ to $\text{FOLLOW}(A)$!
   - *(Note: Follow sets NEVER contain $\epsilon$!).*

---

### Recipe 2: Constructing an LL(1) Parsing Table
1. Compute $\text{FIRST}$ and $\text{FOLLOW}$ for all variables.
2. Draw a grid: Rows = Variables ($E, T, F$), Columns = Terminals ($+, *, id, (, ), \$$).
3. For each production $A \to \alpha$:
   - For every terminal $a \in \text{FIRST}(\alpha)$, place $A \to \alpha$ into cell $M[A, a]$.
   - If $\epsilon \in \text{FIRST}(\alpha)$, for every terminal $b \in \text{FOLLOW}(A)$, place $A \to \alpha$ into cell $M[A, b]$.
4. **The Verdict**: If every single cell has at most 1 production $\implies$ **LL(1) Grammar ✅**. If any cell has 2 productions $\implies$ **Conflict! NOT LL(1) ❌**.

---

## 🚨 TIER 3: Faculty Trap Radar

1. **The SLR(1) Reduce Rule Trap**: In LR(0) parsing, reduce actions are placed across ALL terminal columns. In **SLR(1)**, reduce action $r_k$ is placed **ONLY under the columns belonging to $\mathbf{\text{FOLLOW}(A)}$!** Putting reduce in all columns causes fake conflicts and zeroes out your score.
2. **The Missing $\$$ Trap**: If you forget to add $\$$ to $\text{FOLLOW}(S)$, your Follow sets will be incomplete and your entire parsing table will be corrupted!

---

## 📝 TIER 4: Master Solved HOTS Archetypes

### Archetype 1: Complete LL(1) Parsing Table for Expression Grammar
**Question**: For the grammar:
$$E \to T E', \quad E' \to + T E' \mid \epsilon$$
$$T \to F T', \quad T' \to * F T' \mid \epsilon$$
$$F \to ( E ) \mid id$$
Compute FIRST & FOLLOW sets and construct the LL(1) parsing table.

**Step-by-Step Solution**:
1. **FIRST Sets**:
   * $\text{FIRST}(F) = \{(, id\}$
   * $\text{FIRST}(T') = \{*, \epsilon\}$
   * $\text{FIRST}(T) = \text{FIRST}(F) = \{(, id\}$
   * $\text{FIRST}(E') = \{+, \epsilon\}$
   * $\text{FIRST}(E) = \text{FIRST}(T) = \{(, id\}$
2. **FOLLOW Sets**:
   * Start symbol: $\text{FOLLOW}(E) = \{\$, )\}$
   * From $E \to T E'$: $\text{FOLLOW}(E') = \text{FOLLOW}(E) = \{\$, )\}$
   * From $E \to T E'$: $\text{FOLLOW}(T) = (\text{FIRST}(E') \setminus \{\epsilon\}) \cup \text{FOLLOW}(E') = \{+, \$, )\}$
   * From $T \to F T'$: $\text{FOLLOW}(T') = \text{FOLLOW}(T) = \{+, \$, )\}$
   * From $T \to F T'$: $\text{FOLLOW}(F) = (\text{FIRST}(T') \setminus \{\epsilon\}) \cup \text{FOLLOW}(T') = \{*, +, \$, )\}$
3. **LL(1) Parsing Table $M[A, a]$**:
   $$\begin{array}{|c|c|c|c|c|c|c|} \hline \text{Variable} & id & + & * & ( & ) & \$ \\ \hline E & E \to T E' & & & E \to T E' & & \\ E' & & E' \to + T E' & & & E' \to \epsilon & E' \to \epsilon \\ T & T \to F T' & & & T \to F T' & & \\ T' & & T' \to \epsilon & T' \to * F T' & & T' \to \epsilon & T' \to \epsilon \\ F & F \to id & & & F \to ( E ) & & \\ \hline \end{array}$$
4. **Conclusion**: Every cell contains at most one production rule $\implies$ **Grammar is LL(1) ✅**.
