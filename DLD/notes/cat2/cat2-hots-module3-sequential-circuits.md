# ⚡ CAT-2 HOTS Master Crib — Module 3: Sequential Logic Circuits
**Course**: ECE2002 — Digital Logic Design  
**Coverage**: Module 3 (CO2, CO4) | **Exam Mode**: Open Book / Handwritten Notes Allowed  
**Target Score**: 45+ / 50 (S-Grade Boundary)

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If Question Mentions / Shows... | It Means This Exact Topic | Your Immediate Formula / Action |
| :--- | :--- | :--- |
| "Convert Flip-Flop X to Flip-Flop Y" | **Flip-Flop Conversion** | Write Excitation Table of available FF + Truth Table of required FF $\to$ Solve K-Map for inputs. |
| Circuit with flip-flops and logic gates, "Analyze circuit" | **Sequential Circuit Analysis** | 1. Write input equations (e.g. $J_A, K_A$) $\to$ 2. Characteristic eqns $\to$ 3. State Table $\to$ 4. State Diagram. |
| "Find characteristic equation", "Excitation table" | **FF Equations & Tables** | SR: $Q^+ = S + R'Q$; JK: $Q^+ = JQ' + K'Q$; D: $Q^+ = D$; T: $Q^+ = T \oplus Q$. |
| State table with many rows, "Reduce the number of states" | **State Reduction** | Use the **Implication Chart (Table) Method** or Row Equivalence (same next states & same outputs). |
| Race-around condition, Master-Slave | **JK Timing Anomaly** | Occurs when $J=K=1$, Clock width $t_p > t_{pd}$ (propagation delay). Solution: Edge-triggered or Master-Slave JK. |
| Set-up time ($t_s$), Hold time ($t_h$), Clock frequency | **Sequential Timing Analysis** | $T_{clk} \ge t_{pd(FF)} + t_{comb} + t_s$. Max frequency $f_{max} = 1 / T_{clk}$. |

---

## 🛠️ TIER 2: Deterministic Algorithmic Recipes

### Recipe 3.1: The Universal Flip-Flop Conversion Template
Faculty love asking: *"Convert a JK Flip-Flop into a D Flip-Flop"* or *"Convert SR to T"*. Follow this 4-step plug-and-play procedure:

```
[Available FF: Given hardware] <----- Need Logic Network <----- [Required FF: Target behavior]
```

1. **Step 1**: Write the table combining the **Target FF inputs**, **Present State $Q_n$**, and **Next State $Q_{n+1}$**.
2. **Step 2**: Look at $Q_n \to Q_{n+1}$ and fill in the **Required inputs for the Available FF** using its **Excitation Table**:

#### Universal Excitation Table (MEMORIZE):
| $Q_n \to Q_{n+1}$ | SR Inputs ($S, R$) | JK Inputs ($J, K$) | D Input ($D$) | T Input ($T$) |
| :---: | :---: | :---: | :---: | :---: |
| **$0 \to 0$** | $0, X$ | $0, X$ | $0$ | $0$ |
| **$0 \to 1$** | $1, 0$ | $1, X$ | $1$ | $1$ |
| **$1 \to 0$** | $0, 1$ | $X, 1$ | $0$ | $1$ |
| **$1 \to 1$** | $X, 0$ | $X, 0$ | $1$ | $0$ |

3. **Step 3**: Draw K-Maps for each Available FF input in terms of Target inputs and $Q_n$.
4. **Step 4**: Write simplified Boolean expressions and draw the circuit connecting the logic gates to the available FF inputs.

---

### Recipe 3.2: Analysis of Clocked Sequential Circuits
When given a circuit diagram with Flip-Flops and logic gates:
1. **Step 1 (Input Equations)**: Trace wires to the flip-flop inputs.
   - Example: $J_A = B \cdot x$, $K_A = B'$, $D_B = A \oplus x$, etc.
2. **Step 2 (Next State Equations)**: Substitute input equations into characteristic equations:
   - For JK: $A_{n+1} = J_A A' + K_A' A$
   - For D: $B_{n+1} = D_B$
   - For T: $A_{n+1} = T_A \oplus A$
3. **Step 3 (Output Equation)**: Write equation for external output $Y$ (if present).
   - If $Y = f(\text{States only}) \implies$ **Moore Machine**.
   - If $Y = f(\text{States, Input } x) \implies$ **Mealy Machine**.
4. **Step 4 (State Table)**: List all combinations of Present State ($A, B$) and Input ($x$), compute Next State ($A^+, B^+$) and Output ($Y$).
5. **Step 5 (State Diagram)**: Draw bubbles for states ($00, 01, 10, 11$). Draw directed arrows labeled $x / Y$ (Mealy) or arrows labeled $x$ with state bubbles $S / Y$ (Moore).

---

### Recipe 3.3: State Reduction via Implication Chart
To eliminate redundant states and minimize flip-flops required:
1. Construct an implication grid: Rows = States $S_2$ to $S_n$; Columns = States $S_1$ to $S_{n-1}$.
2. **Pass 1 (Immediate Output Mismatch)**:
   - For cell $(S_i, S_j)$: If their outputs for ANY input are different ($Y(S_i) \ne Y(S_j)$), place an **$\times$** (They can NEVER be equivalent).
   - If outputs are identical, write down the pairs of next states required for equivalence: e.g., $(S_a, S_b), (S_c, S_d)$.
   - If next states are also identical (or self-referencing), put a **$\checkmark$**.
3. **Pass 2 (Chain Reaction Crossing)**:
   - Review each uncrossed cell: If it contains a next-state pair that has already received an $\times$, put an **$\times$** in this cell too!
   - Repeat until no new $\times$ marks can be placed.
4. **Step 4 (Equivalence Grouping)**: Combine all remaining uncrossed pairs into single merged states.

---

## 🚨 TIER 3: Faculty Trap Radar

1. **The SR Invalid State Physical Outcome**: When $S=1, R=1$, both NOR outputs become 0 (or NAND outputs become 1). When clock drops back to 0 simultaneously, the flip-flop enters a **metastable / unpredictable state** determined by gate propagation delay differences.
2. **The JK Don't Cares**: When filling excitation tables for JK, students forget that half the entries are **$X$ (Don't Care)**. Forgetting don't cares leads to unnecessarily complex logic expressions and lost marks!
3. **Mealy vs Moore Clock Delay**:
   - **Mealy output**: Changes immediately when input changes (asynchronous to clock edge for output).
   - **Moore output**: Changes ONLY at the clock edge when the state registers update.
4. **Unused States Lockout**: If a circuit has 3 flip-flops (8 possible states) but only uses 5 states, you **MUST** verify what happens if noise puts the circuit into an unused state ($101, 110, 111$). Does it return to a valid state, or get stuck in a death loop?

---

## 📝 TIER 4: Master Solved HOTS Archetypes

### Archetype 1: Complete Flip-Flop Conversion (JK to T Flip-Flop)
**Question**: Design a T flip-flop using an available JK flip-flop and minimal external logic gates.

**Solution Template**:
1. **Target**: T Flip-Flop. **Available**: JK Flip-Flop.
2. **Conversion Truth Table**:
   $$\begin{array}{|c|c|c|c|c|} \hline T & Q_n & Q_{n+1} & J & K \\ \hline 0 & 0 & 0 & 0 & X \\ 0 & 1 & 1 & X & 0 \\ 1 & 0 & 1 & 1 & X \\ 1 & 1 & 0 & X & 1 \\ \hline \end{array}$$
3. **K-Map for J ($T, Q_n$)**:
   * Cell $(0, 0) = 0$
   * Cell $(0, 1) = X$
   * Cell $(1, 0) = 1$
   * Cell $(1, 1) = X$
   * Grouping Cell $(1,0)$ with Don't Care $(1,1) \implies \mathbf{J = T}$.
4. **K-Map for K ($T, Q_n$)**:
   * Cell $(0, 0) = X$
   * Cell $(0, 1) = 0$
   * Cell $(1, 0) = X$
   * Cell $(1, 1) = 1$
   * Grouping Cell $(1,1)$ with Don't Care $(1,0) \implies \mathbf{K = T}$.
5. **Circuit Diagram**: Connect the external input $T$ directly to both $J$ and $K$ terminals ($J = K = T$). No additional gates required!

---

### Archetype 2: Analysis of Sequential Circuit with State Diagram
**Question**: A sequential circuit has two JK flip-flops $A$ and $B$, one input $x$, and one output $y$. The circuit is described by:
$$J_A = B \cdot x, \quad K_A = B$$
$$J_B = x', \quad K_B = A \oplus x$$
$$y = A \cdot B \cdot x$$
1. Derive the next-state equations for $A$ and $B$.
2. Construct the state table.
3. Draw the state diagram and identify if the machine is Mealy or Moore.

**Solution Template**:
1. **Next-State Equations**:
   * $A_{n+1} = J_A A' + K_A' A = (B x) A' + B' A = A' B x + A B'$
   * $B_{n+1} = J_B B' + K_B' B = x' B' + (A \oplus x)' B = x' B' + (A x + A' x') B$
2. **Output Type**: $y = A B x$ depends directly on input $x \implies$ **Mealy Machine**.
3. **State Table**:
   $$\begin{array}{|c|c|c|c|c|c|} \hline \text{Present State } (A B) & \text{Next State } (x=0) & \text{Next State } (x=1) & \text{Output } y (x=0) & \text{Output } y (x=1) \\ \hline 00 & 01 & 00 & 0 & 0 \\ 01 & 01 & 10 & 0 & 0 \\ 10 & 11 & 10 & 0 & 0 \\ 11 & 01 & 01 & 0 & 1 \\ \hline \end{array}$$
4. **State Transitions**:
   * From $00$: on $x=0 \to 01/0$; on $x=1 \to 00/0$.
   * From $01$: on $x=0 \to 01/0$; on $x=1 \to 10/0$.
   * From $10$: on $x=0 \to 11/0$; on $x=1 \to 10/0$.
   * From $11$: on $x=0 \to 01/0$; on $x=1 \to 01/1$.
