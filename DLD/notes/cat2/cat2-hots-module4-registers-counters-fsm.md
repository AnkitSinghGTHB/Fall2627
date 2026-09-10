# ⚡ CAT-2 HOTS Master Crib — Module 4: Registers, Counters & FSMs
**Course**: ECE2002 — Digital Logic Design  
**Coverage**: Module 4 (CO2, CO4) | **Exam Mode**: Open Book / Handwritten Notes Allowed  
**Target Score**: 45+ / 50 (S-Grade Boundary)

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If Question Mentions / Shows... | It Means This Exact Topic | Your Immediate Formula / Action |
| :--- | :--- | :--- |
| "Design counter with sequence $0 \to 4 \to 6 \to 1 \dots$" | **Synchronous Counter Design** | 1. State transition table $\to$ 2. Excitation columns for chosen FF $\to$ 3. K-Maps with Don't Cares for unused states $\to$ 4. Lockout check! |
| "Decade ripple counter", "Mod-10 asynchronous counter" | **Asynchronous (Ripple) Counter** | Use T/JK FFs ($J=K=1$). Reset condition: $Q_3 Q_2 Q_1 Q_0 = 1010$ ($10_{10}$) $\implies$ Feed $Q_3$ and $Q_1$ into NAND to trigger active-low $\overline{\text{CLR}}$. |
| "Ripple counter counts UP or DOWN?" | **Ripple Counter Direction Rule** | **Negative Edge-Triggered**: Clock from $Q \implies$ **DOWN**; Clock from $Q' \implies$ **UP**.<br>**Positive Edge-Triggered**: Clock from $Q \implies$ **UP**; Clock from $Q' \implies$ **DOWN**. |
| "Ring counter vs Johnson counter", "Twisted ring" | **Ring & Johnson Counters** | Ring: $N$ FFs $= N$ states (No decoding gates needed).<br>Johnson: $N$ FFs $= 2N$ states ($Q_N'$ fed back to $D_1$; 2-input AND decoding). |
| "Sequence detector for 1011 / 1101", "Overlapping / Non-overlapping" | **FSM Sequence Detector** | Draw state bubble for each recognized bit. In overlapping: after complete match, return to longest matching prefix state. |
| SISO, SIPO, PISO, PIPO, Universal Shift Register | **Shift Registers** | Universal 74194 Mode Select: $S_1 S_0 = 00$ (Hold), $01$ (Shift Right), $10$ (Shift Left), $11$ (Parallel Load). |

---

## 🛠️ TIER 2: Deterministic Algorithmic Recipes

### Recipe 4.1: Synchronous Counter Design for Any Arbitrary Sequence
Follow this exact 5-step template for full marks:

1. **Step 1 (Determine Flip-Flops)**: If maximum state is $M$, find minimum $n$ such that $2^n > M$.
2. **Step 2 (State Transition & Excitation Table)**:
   - List Present State ($Q_A, Q_B, Q_C$) and Next State ($Q_A^+, Q_B^+, Q_C^+$) for the sequence.
   - For all unused states, set Next States to **$X X X$ (Don't Care)**.
   - Fill excitation inputs:
     - For D Flip-Flops: $D_A = Q_A^+$, $D_B = Q_B^+$, $D_C = Q_C^+$.
     - For T Flip-Flops: $T_i = Q_i \oplus Q_i^+$.
     - For JK Flip-Flops: Use standard JK excitation table.
3. **Step 3 (K-Map Simplification)**: Solve K-Map for each flip-flop input. Include all unused state don't-cares to minimize gate count!
4. **Step 4 (The Mandatory Lockout / Self-Starting Check)**:
   - **Faculty love deducting 4 marks here!**
   - Take the simplified input equations and evaluate Next States for each **unused state**.
   - If from every unused state the counter eventually enters a valid sequence state $\implies$ **Self-Starting ✅**.
   - If an unused state transitions only to other unused states $\implies$ **Lockout ❌** (must modify logic or tie asynchronous $\overline{\text{PRE}}/\overline{\text{CLR}}$).
5. **Step 5 (Logic Diagram)**: Draw common clock to all FFs. Draw logic gates connected to FF inputs.

---

### Recipe 4.2: FSM Sequence Detector Design (Overlapping vs Non-Overlapping)
To detect an $m$-bit sequence (e.g. $1011$):
* **Moore Machine**: Needs $m+1$ states (States = Number of bits recognized: $S_0=\epsilon, S_1=1, S_2=10, S_3=101, S_4=1011$). Output is associated with state $S_4$.
* **Mealy Machine**: Needs $m$ states ($S_0, S_1, S_2, S_3$). Output $Y=1$ occurs on the transition arrow out of $S_3$ when the last bit is received.

#### The Overlapping vs Non-Overlapping Rule:
* In **Non-Overlapping**: After recognizing sequence $1011$, on the next bit, the machine resets back to $S_0$ (or $S_1$ if bit is 1).
* In **Overlapping**: After recognizing sequence $1011$, the trailing bit $1$ serves as the first bit of the next possible sequence! So machine transitions to $S_1$ (if next bit is 0, path continues).

---

## 🚨 TIER 3: Faculty Trap Radar

1. **The Asynchronous Mod-N Glitch Trap**: In an asynchronous counter reset with a NAND gate, the counter briefly enters the reset state (e.g. state $10$ in decade counter) for a few nanoseconds before clearing back to $0$. Examiners ask: *"What is the maximum transient state?"* Answer: State $N$ is transiently entered before output resets!
2. **Johnson Counter Unused States**: A 4-bit Johnson counter has 8 valid states and 8 **unused states**. Without self-starting logic, if noise hits an unused state, it cycles through the other 7 unused states forever! Self-starting equation for Johnson: $D_1 = Q_4' \cdot (Q_1' + Q_2' + \dots)$.
3. **Clock Skew in Ripple Counters**: In ripple counters, propagation delay accumulates ($n \times t_{pd}$). Maximum operating frequency is strictly limited:
   $$f_{max} \le \frac{1}{n \cdot t_{pd}}$$

---

## 📝 TIER 4: Master Solved HOTS Archetypes

### Archetype 1: Non-Standard Sequence Synchronous Counter (From Assignment 4)
**Question**: Design a 3-bit synchronous counter that counts the sequence:
$$0 \to 4 \to 6 \to 1 \to 3 \to 7 \to 2 \to 5 \to 0 \dots$$
using D flip-flops. Check whether the counter is self-starting.

**Solution Template**:
1. **Number of states**: 8 states ($0, 1, 2, 3, 4, 5, 6, 7$). All $2^3 = 8$ states are used $\implies$ No unused states!
2. **State Transition Table**:
   $$\begin{array}{|c|c|c|c|c|c|c|c|c|} \hline \text{State} & Q_2 & Q_1 & Q_0 & Q_2^+ & Q_1^+ & Q_0^+ & D_2 & D_1 & D_0 \\ \hline 0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 0 \\ 4 & 1 & 0 & 0 & 1 & 1 & 0 & 1 & 1 & 0 \\ 6 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 1 \\ 1 & 0 & 0 & 1 & 0 & 1 & 1 & 0 & 1 & 1 \\ 3 & 0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\ 7 & 1 & 1 & 1 & 0 & 1 & 0 & 0 & 1 & 0 \\ 2 & 0 & 1 & 0 & 1 & 0 & 1 & 1 & 0 & 1 \\ 5 & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline \end{array}$$
3. **K-Map Simplification**:
   * **For $D_2(Q_2, Q_1, Q_0)$**:
     * Minterms: $m(0, 4, 3, 2) \implies m(0, 2, 3, 4)$.
     * Group $m(0, 2) \implies Q_2' Q_0'$.
     * Group $m(2, 3) \implies Q_2' Q_1$.
     * Term $m(4) \implies Q_2 Q_1' Q_0'$.
     * Simplified: $\mathbf{D_2 = Q_2' Q_0' + Q_2' Q_1 + Q_2 Q_1' Q_0' = Q_2'(Q_1 + Q_0') + Q_2 Q_1' Q_0'}$.
   * **For $D_1(Q_2, Q_1, Q_0)$**:
     * Minterms: $m(4, 1, 3, 7) \implies m(1, 3, 4, 7)$.
     * Group $m(1, 3, 7)$ or factor: $\mathbf{D_1 = Q_2' Q_0 + Q_1 Q_0 + Q_2 Q_1' Q_0'}$.
   * **For $D_0(Q_2, Q_1, Q_0)$**:
     * Minterms: $m(6, 1, 3, 2) \implies m(1, 2, 3, 6)$.
     * Group $m(1, 3) \implies Q_2' Q_0$; Group $m(2, 3) \implies Q_2' Q_1$; Term $m(6) \implies Q_2 Q_1 Q_0'$.
     * Simplified: $\mathbf{D_0 = Q_2'(Q_1 + Q_0) + Q_2 Q_1 Q_0'}$.
4. **Self-Starting Verification**: Since all 8 states are part of the main counting loop, there are no unused states, so the counter is **trivially self-starting ✅**.

---

### Archetype 2: Sequence Detector for "1011" (Overlapping Mealy Machine)
**Question**: Design a Mealy FSM to detect the sequence "1011" with overlapping allowed.
Construct the state diagram, state table, and derive flip-flop excitation equations using D flip-flops.

**Solution Template**:
1. **State Assignment**:
   * $S_0$ ($00$): Reset state (no matching bits).
   * $S_1$ ($01$): Got '1'.
   * $S_2$ ($10$): Got '10'.
   * $S_3$ ($11$): Got '101'.
2. **Transitions & Outputs ($x / Y$)**:
   * From $S_0$: on $x=0 \to S_0/0$; on $x=1 \to S_1/0$.
   * From $S_1$: on $x=0 \to S_2/0$; on $x=1 \to S_1/0$ (holds on 1).
   * From $S_2$: on $x=0 \to S_0/0$ (resets); on $x=1 \to S_3/0$.
   * From $S_3$: on $x=0 \to S_2/0$; on $x=1 \to S_1/1$ (Outputs 1! Since it's overlapping, last '1' matches $S_1$).
3. **State Table (with $A, B$ state bits)**:
   $$\begin{array}{|c|c|c|c|c|c|c|} \hline \text{Present State} & A & B & A^+ (x=0) & B^+ (x=0) & A^+ (x=1) & B^+ (x=1) & Y (x=0) & Y (x=1) \\ \hline S_0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ S_1 & 0 & 1 & 1 & 0 & 0 & 1 & 0 & 0 \\ S_2 & 1 & 0 & 0 & 0 & 1 & 1 & 0 & 0 \\ S_3 & 1 & 1 & 1 & 0 & 0 & 1 & 0 & 1 \\ \hline \end{array}$$
4. **Equations for D Flip-Flops**:
   * $D_A = A^+ = A' B x' + A B' x + A B x' = B x' + A B' x$.
   * $D_B = B^+ = x$.
   * Output: $\mathbf{Y = A \cdot B \cdot x}$.
