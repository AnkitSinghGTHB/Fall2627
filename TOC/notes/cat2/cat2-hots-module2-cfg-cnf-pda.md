# ⚡ CAT-2 HOTS Master Crib — Module 2 & 3: CFG, CNF, GNF & Pushdown Automata
**Course**: CSE2004 — Theory of Computation & Compiler Design  
**Coverage**: Context-Free Grammars & Pushdown Automata | **Exam Mode**: Open Book / Notes Allowed  
**Target Score**: 45+ / 50 (S-Grade Boundary)

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If Question Mentions / Shows... | It Means This Exact Topic | Your Immediate Formula / Action |
| :--- | :--- | :--- |
| "Show the grammar is ambiguous" | **CFG Ambiguity Proof** | Pick ONE short string $w$. Draw **TWO distinct parse trees** OR write **TWO distinct leftmost derivations** for $w$. |
| "Convert grammar to CNF" | **Chomsky Normal Form** | **Strict Order**: 1. Remove $\epsilon$-productions $\to$ 2. Remove Unit productions $\to$ 3. Remove Useless symbols $\to$ 4. Replace terminals & long RHS. Form: $A \to BC$ or $A \to a$. |
| "Convert to GNF" | **Greibach Normal Form** | Eliminate left recursion ($A \to A\alpha$). Form: $A \to a \alpha$ (starts with exactly ONE terminal followed by $\ge 0$ variables). |
| "Design a PDA for $L = \{a^n b^n\}$", $\{w w^R\}$ | **PDA Construction** | Define 7-tuple $M = (Q, \Sigma, \Gamma, \delta, q_0, Z_0, F)$. Write explicit transition table $\delta(q, a, X) = \{(p, \gamma)\}$. |
| "Acceptance by Empty Stack vs Final State" | **PDA Acceptance Modes** | Final State: ends in $q_f \in F$. Empty Stack: stack contains nothing ($\text{stack} = \epsilon$). Inter-conversion requires adding $q_{start}, Z_0'$ and $q_{dump}$. |
| "Prove $L = \{a^n b^n c^n\}$ is not context-free" | **Pumping Lemma for CFL** | Assume CFL $\to$ Pick $s = a^p b^p c^p$ ($|s| \ge p$). Split $s = u v w x y$ with $|vwx| \le p, |vx| \ge 1$. Show $s' = u v^2 w x^2 y \notin L$. |

---

## 🛠️ TIER 2: Deterministic Algorithmic Recipes

### Recipe 2.1: The 4-Step Chomsky Normal Form (CNF) Algorithm
A grammar is in CNF if every production is of the form:
$$A \to BC \quad \text{or} \quad A \to a$$

> ⚠️ **CRITICAL TRAP**: You **MUST** execute these 4 steps in this exact order. Swapping Step 1 and Step 2 will fail!

#### Step 1: Eliminate $\epsilon$-productions ($A \to \epsilon$)
1. Find all **nullable variables** (variables that can derive $\epsilon$ directly or indirectly):
   - If $A \to \epsilon$, $A$ is nullable.
   - If $B \to A_1 A_2 \dots A_k$ and all $A_i$ are nullable, then $B$ is nullable.
2. For every production containing nullable variables, write all combinations of presence and absence of those nullable variables (except creating $A \to \epsilon$).

#### Step 2: Eliminate Unit Productions ($A \to B$ where $B \in V$)
1. Find all pairs $(A, B)$ such that $A \stackrel{*}{\implies} B$:
   - Reflexive: $(A, A)$ for all $A$.
   - If $A \to B$, then $(A, B)$.
   - Transitive: If $(A, B)$ and $B \to C$, then $(A, C)$.
2. For each pair $(A, B)$, if $B \to \alpha$ is a non-unit production, add $A \to \alpha$.
3. Delete all unit productions $A \to B$.

#### Step 3: Eliminate Useless & Unreachable Symbols
1. **Eliminate Non-generating symbols**: Keep only symbols that can derive strings of terminals.
2. **Eliminate Unreachable symbols**: Draw reachability graph from start symbol $S$. Delete symbols not reachable from $S$.

#### Step 4: Convert Remaining Productions to Binary Form
1. For terminals mixed in RHS (e.g. $A \to a B$): Replace $a$ with a new variable $T_a$, and add production $T_a \to a$.
2. For productions with RHS length $\ge 3$ (e.g. $A \to B C D$): Introduce intermediate variable $X_1$:
   $$A \to B X_1, \quad X_1 \to C D$$

---

### Recipe 2.2: Pushdown Automata (PDA) Design Cookbook
A PDA is defined as $M = (Q, \Sigma, \Gamma, \delta, q_0, Z_0, F)$:
* $Q$: Finite set of states
* $\Sigma$: Input alphabet (e.g. $\{a, b\}$)
* $\Gamma$: Stack alphabet (e.g. $\{A, Z_0\}$)
* $Z_0$: Initial stack symbol
* $\delta(q, a, X) \to (p, \alpha)$ means: In state $q$, reading input $a$, with top of stack $X$, change state to $p$ and replace $X$ with string $\alpha$.

#### Standard Stack Actions:
* **Push $A$ on top of $X$**: $\delta(q, a, X) = (q, A X)$
* **Pop top of stack $X$**: $\delta(q, a, X) = (q, \epsilon)$
* **Keep top unchanged (Read-only)**: $\delta(q, a, X) = (q, X)$

#### Master Transition Table for $L = \{a^n b^n \mid n \ge 1\}$:
1. State $q_0$ (Push phase): For every input $a$, push $A$ onto stack:
   $$\delta(q_0, a, Z_0) = (q_0, A Z_0)$$
   $$\delta(q_0, a, A) = (q_0, A A)$$
2. Transition on first $b$: Change state to $q_1$ and pop first $A$:
   $$\delta(q_0, b, A) = (q_1, \epsilon)$$
3. State $q_1$ (Pop phase): For every subsequent $b$, pop one $A$:
   $$\delta(q_1, b, A) = (q_1, \epsilon)$$
4. End of input ($\epsilon$): When input finishes and stack returns to $Z_0$, transition to final state $q_f$:
   $$\delta(q_1, \epsilon, Z_0) = (q_f, Z_0)$$

---

## 🚨 TIER 3: Faculty Trap Radar

1. **The Leftmost Derivation Ambiguity Trap**: If you give one leftmost derivation and one *rightmost* derivation, faculties will **give 0 marks**! You must give **TWO DIFFERENT LEFTMOST DERIVATIONS** (or two different parse trees) for the SAME string.
2. **DPDA vs NPDA Power Difference**: Unlike Finite Automata (where DFA $\equiv$ NFA), **NPDA is strictly MORE powerful than DPDA**! The language of even palindromes $\{w w^R\}$ cannot be recognized by any deterministic PDA (DPDA) because it requires non-deterministically guessing the midpoint!
3. **Empty Stack to Final State PDA Conversion**:
   - Given PDA $M_E$ (accepts by empty stack), to construct $M_F$ (accepts by final state):
     - Add new start symbol $X_0$ and new start state $p_0$: $\delta(p_0, \epsilon, X_0) = (q_0, Z_0 X_0)$.
     - Add a new final state $p_f$: For all $q \in Q$, $\delta(q, \epsilon, X_0) = (p_f, X_0)$.
     - This prevents premature acceptance if stack temporarily empties.

---

## 📝 TIER 4: Master Solved HOTS Archetypes

### Archetype 1: Rigorous Grammar Ambiguity Proof
**Question**: Show that the grammar with productions:
$$E \to E + E \mid E * E \mid (E) \mid id$$
is ambiguous. Provide two distinct parse trees and two distinct leftmost derivations for the string: $id + id * id$.

**Solution Template**:
1. **Target String**: $w = id + id * id$.
2. **Leftmost Derivation 1 (Addition first)**:
   $$E \implies E + E \implies id + E \implies id + E * E \implies id + id * E \implies id + id * id$$
3. **Leftmost Derivation 2 (Multiplication first)**:
   $$E \implies E * E \implies E + E * E \implies id + E * E \implies id + id * E \implies id + id * id$$
4. **Parse Trees**:
   * Tree 1: Root is $E$. Children are $E, +, E$. Right child $E$ branches into $E, *, E$. (Evaluates as $id + (id * id)$).
   * Tree 2: Root is $E$. Children are $E, *, E$. Left child $E$ branches into $E, +, E$. (Evaluates as $(id + id) * id$).
5. **Conclusion**: Since there exist two distinct leftmost derivations (and two distinct parse trees) for the identical string $w = id + id * id$, the grammar is **AMBIGUOUS ✅**.

---

### Archetype 2: Full Chomsky Normal Form (CNF) Conversion
**Question**: Convert the following grammar $G$ into Chomsky Normal Form (CNF):
$$S \to a B \mid b A$$
$$A \to a \mid a S \mid b A A$$
$$B \to b \mid b S \mid a B B$$

**Solution Template**:
1. **Step 1 ($\epsilon$-productions)**: None exist.
2. **Step 2 (Unit productions)**: None exist.
3. **Step 3 (Useless symbols)**: All symbols generate terminals and are reachable from $S$.
4. **Step 4 (Binary & Terminal Normalization)**:
   - Introduce terminal variables: $T_a \to a$ and $T_b \to b$.
   - Replace terminals in mixed productions:
     * $S \to T_a B \mid T_b A$
     * $A \to a \mid T_a S \mid T_b A A$
     * $B \to b \mid T_b S \mid T_a B B$
   - Break length $\ge 3$ productions:
     * For $A \to T_b A A$: Introduce $X_1 \to A A \implies A \to T_b X_1$.
     * For $B \to T_a B B$: Introduce $X_2 \to B B \implies B \to T_a X_2$.
5. **Final CNF Grammar**:
   $$S \to T_a B \mid T_b A$$
   $$A \to a \mid T_a S \mid T_b X_1$$
   $$B \to b \mid T_b S \mid T_a X_2$$
   $$X_1 \to A A, \quad X_2 \to B B$$
   $$T_a \to a, \quad T_b \to b$$
   All productions are of the form $A \to B C$ or $A \to a \implies$ **In CNF ✅**.
