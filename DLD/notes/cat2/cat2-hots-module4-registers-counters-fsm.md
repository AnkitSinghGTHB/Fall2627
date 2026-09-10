# ⚡ CAT-2 HOTS Master Crib — Module 4: Registers, Counters & FSMs
**Course**: ECE2002 — Digital Logic Design  
**Level**: Self-Contained / Zero-Assumption (From Bedrock Basics to HOTS)  
**Exam Mode**: Open Book / Handwritten Notes Allowed | **Target Score**: 45+ / 50

---

## 🧱 TIER 0: The "Explain Like I'm 5" Bedrock Basics
*(Read this first if you forgot everything about counters and FSMs)*

### 1. What on Earth is a Counter?
* A counter is just a chain of flip-flops connected so that with each clock tick, their combined binary value increments:
  $$000 (0) \to 001 (1) \to 010 (2) \to 011 (3) \dots$$
* **What does "Mod-N" mean?**
  * Modulo $N$ (or Mod-$N$) simply means: **How many distinct numbers does it count before resetting back to 0?**
  * Example: A **Mod-6 counter** counts 6 numbers: $0, 1, 2, 3, 4, 5$, and on the next tick, resets back to $0$.
  * A **Decade Counter (Mod-10)** counts 10 numbers: $0$ through $9$, then resets to $0$.

---

### 2. Synchronous vs Asynchronous (Ripple) Counters
This is the single most tested comparison in digital exams:

| Feature | Synchronous Counter | Asynchronous (Ripple) Counter |
| :--- | :--- | :--- |
| **Clock Connection** | **ALL flip-flops share the exact SAME clock pulse wire.** | **ONLY Flip-Flop 0 gets the clock.** Flip-flop 1 gets its clock from Flip-flop 0's output! |
| **How they update** | All flip-flops update **simultaneously** at the exact same instant. | **Domino effect**: FF0 flips $\to$ triggers FF1 $\to$ triggers FF2. |
| **Speed** | **Very Fast**. Delay does not depend on number of flip-flops. | **Slow**. Propagation delay accumulates: $n \times t_{pd}$. |
| **Glitches / Noise** | Clean outputs. | Suffers from transient glitch states during transitions. |

---

### 3. How to Know if a Ripple Counter counts UP or DOWN?
Faculty love asking this 2-mark trick question. Memorize this 4-box table:

| Clock Trigger Type | Clock Input Connected to: | Counting Direction |
| :---: | :---: | :---: |
| **Negative Edge ($\downarrow$)** | Normal output **$Q$** | **UP** counting |
| **Negative Edge ($\downarrow$)** | Inverted output **$Q'$** | **DOWN** counting |
| **Positive Edge ($\uparrow$)** | Normal output **$Q$** | **DOWN** counting |
| **Positive Edge ($\uparrow$)** | Inverted output **$Q'$** | **UP** counting |

> 🧠 **Memory Rule**: Negative Edge + $Q = \text{UP}$. If you flip either the edge or the output, the direction flips!

---

### 4. What is a Shift Register? (The Bucket Brigade)
* A chain of flip-flops where each bit is passed from one flip-flop to the next on every clock tick.
* **SISO** (Serial In, Serial Out): 1 bit in at a time, 1 bit out at a time (Slowest).
* **SIPO** (Serial In, Parallel Out): Bits enter 1-by-1, but all outputs are read simultaneously in 1 clock tick.
* **PISO** (Parallel In, Serial Out): All bits loaded at once, shifted out 1-by-1.
* **PIPO** (Parallel In, Parallel Out): All loaded at once, all read at once (Fastest, just a storage register).

---

### 5. Ring Counter vs Johnson (Twisted Ring) Counter
* **Ring Counter**:
  * Output of last flip-flop ($Q_N$) is fed directly back into input of first flip-flop ($D_1$).
  * A single $1$ circulates in a circle: $1000 \to 0100 \to 0010 \to 0001 \to 1000$.
  * $N$ flip-flops give **$N$ states**.
* **Johnson Counter (Twisted Ring)**:
  * Inverted output of last flip-flop ($Q_N'$) is fed back into $D_1$.
  * Creates a wave of 1s followed by a wave of 0s: $000 \to 100 \to 110 \to 111 \to 011 \to 001 \to 000$.
  * $N$ flip-flops give **$2N$ states** (Twice as many states as a standard ring counter!).

---

### 6. What is a Finite State Machine (FSM)?
An FSM is just an electronic brain that has a few specific "moods" (states) and transitions between them based on incoming inputs.
* **Moore Machine**: The output depends **ONLY on the current state**. (Output is written inside the state circle: $S_0 / 0$).
* **Mealy Machine**: The output depends on the **current state AND the current input wire**. (Output is written on the transition arrow: $x / Y$).

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If Question Shows / Asks... | It Means This Exact Topic | Your Immediate Formula / Action |
| :--- | :--- | :--- |
| "Design counter for sequence $0 \to 4 \to 6 \dots$" | **Synchronous Counter Design** | 1. Table with Present State $\to$ Next State $\to$ Excitation. 2. K-Map with unused states as $X$. 3. **Must do Lockout Check!** |
| "Design a Mod-10 / Decade ripple counter" | **Mod-N Asynchronous Counter** | 4 T/JK FFs. Reset count is $10_{10} = 1010_2$ ($Q_3 Q_2 Q_1 Q_0$). Connect $Q_3$ and $Q_1$ to a NAND gate $\to$ clear inputs $\overline{\text{CLR}}$. |
| "Detect sequence 1011", Overlapping | **Sequence Detector FSM** | Draw state bubble for each matching bit. Overlapping means after full match, the trailing $1$ counts towards next sequence! |
| "Unused states", "Self-starting counter" | **Lockout Verification** | Evaluate next states of all unused states using your derived K-Map equations. Must show they return to valid sequence! |

---

## 🛠️ TIER 2: Step-by-Step Execution Recipes

### Recipe 1: Complete Synchronous Counter Design for Any Sequence
Suppose you need to design a counter that counts an arbitrary sequence (e.g. $0 \to 2 \to 3 \to 5 \to 0$):
1. **Count Flip-Flops**: Max number is $5 \implies 2^n > 5 \implies n = 3$ flip-flops ($Q_2, Q_1, Q_0$).
2. **Transition Table**:
   - List the sequence states.
   - For all unused numbers ($1, 4, 6, 7$), write their next states as **$X X X$ (Don't Care)**.
3. **Excitation Columns**:
   - For D Flip-Flops: $D_2 = Q_2^+$, $D_1 = Q_1^+$, $D_0 = Q_0^+$. (Easiest flip-flop to use in exam!).
   - For T Flip-Flops: $T_i = Q_i \oplus Q_i^+$ (1 if bit changes, 0 if bit stays same).
4. **Solve K-Maps**: Minimize expressions including the $X$ don't cares.
5. **The Mandatory Self-Starting Check (4-Mark Question Trap)**:
   - For each unused state (e.g. $001$), plug its bits into your simplified equations.
   - Trace where it goes on the next clock tick.
   - If it eventually enters the valid loop $\implies$ **Self-Starting Counter ✅**.
   - If it loops among unused states $\implies$ **Not self-starting (Lockout) ❌**.

---

### Recipe 2: FSM Sequence Detector (Overlapping vs Non-Overlapping)
To design a detector for sequence `1011`:
* **State Definitions**:
  * $S_0$: Reset / Got nothing ($00$).
  * $S_1$: Got `1` ($01$).
  * $S_2$: Got `10` ($10$).
  * $S_3$: Got `101` ($11$).
* **Transitions**:
  * From $S_0$: on $0 \to S_0 / 0$; on $1 \to S_1 / 0$.
  * From $S_1$: on $0 \to S_2 / 0$; on $1 \to S_1 / 0$ (holds on 1).
  * From $S_2$: on $0 \to S_0 / 0$ (resets); on $1 \to S_3 / 0$.
  * From $S_3$:
    * If input is $0$: resets to $S_2 / 0$ (since `1010` ends with `10`).
    * If input is $1$: **MATCH!** Output $= 1$.
      * If **Overlapping**: Transition to $S_1 / 1$ (the last `1` starts the next pattern).
      * If **Non-Overlapping**: Transition to $S_0 / 1$ (clean reset).

---

## 🚨 TIER 3: Faculty Trap Radar

1. **Transient Glitch in Ripple Reset**: In a decade ripple counter, when count reaches $10_{10} = 1010_2$, the NAND gate activates and resets the counter to $0000_2$. For a few nanoseconds, the counter *is* in state 10. Examiners ask: *"What is the temporary state?"* Answer: State $10$!
2. **Lockout in Counters**: If you leave unused states out of your K-Map or don't check where they go, the counter might get stuck in an unused state forever upon power-up!

---

## 📝 TIER 4: Master Solved HOTS Archetypes

### Archetype 1: Design a Mod-6 Synchronous Counter using D Flip-Flops
**Question**: Design a synchronous counter counting $0 \to 1 \to 2 \to 3 \to 4 \to 5 \to 0$ using D flip-flops. Check if self-starting.

**Step-by-Step Solution**:
1. Max count is $5 \implies 3$ flip-flops ($Q_2, Q_1, Q_0$).
2. Unused states: $6 (110)$ and $7 (111)$.
3. **Transition Table with D Excitation ($D = Q^+$)**:
   $$\begin{array}{|c|c|c|c|c|c|c|c|c|} \hline \text{State} & Q_2 & Q_1 & Q_0 & Q_2^+ & Q_1^+ & Q_0^+ & D_2 & D_1 & D_0 \\ \hline 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 \\ 1 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 1 & 0 \\ 2 & 0 & 1 & 0 & 0 & 1 & 1 & 0 & 1 & 1 \\ 3 & 0 & 1 & 1 & 1 & 0 & 0 & 1 & 0 & 0 \\ 4 & 1 & 0 & 0 & 1 & 0 & 1 & 1 & 0 & 1 \\ 5 & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline 6 & 1 & 1 & 0 & X & X & X & X & X & X \\ 7 & 1 & 1 & 1 & X & X & X & X & X & X \\ \hline \end{array}$$
4. **K-Maps (with Don't Cares at cells 6 and 7)**:
   * **For $D_2$**: Minterms: $m(3, 4)$, Don't Cares: $d(6, 7)$.
     * Group $m(4)$ with $d(6) \implies Q_2 Q_0'$.
     * Group $m(3)$ with $d(7) \implies Q_1 Q_0$.
     * $\mathbf{D_2 = Q_2 Q_0' + Q_1 Q_0}$.
   * **For $D_1$**: Minterms: $m(1, 2)$, Don't Cares: $d(6, 7)$.
     * Group $m(1, 2) \implies Q_2' Q_1' Q_0 + Q_2' Q_1 Q_0' = Q_2'(Q_1 \oplus Q_0)$.
     * $\mathbf{D_1 = Q_2'(Q_1 \oplus Q_0)}$.
   * **For $D_0$**: Minterms: $m(0, 2, 4)$, Don't Cares: $d(6, 7)$.
     * Group $m(0, 2, 4, 6) \implies Q_0'$.
     * $\mathbf{D_0 = Q_0'}$.
5. **Self-Starting Check for Unused States 6 and 7**:
   * For State $6$ ($Q_2=1, Q_1=1, Q_0=0$):
     * $D_2 = (1)(1) + (1)(0) = 1$
     * $D_1 = 0 \cdot (1 \oplus 0) = 0$
     * $D_0 = 0' = 1$
     * Next State $= 101$ (State 5) $\implies$ **Enters valid sequence ✅**.
   * For State $7$ ($Q_2=1, Q_1=1, Q_0=1$):
     * $D_2 = (1)(0) + (1)(1) = 1$
     * $D_1 = 0$
     * $D_0 = 1' = 0$
     * Next State $= 100$ (State 4) $\implies$ **Enters valid sequence ✅**.
   * Both unused states converge into the main loop. **Counter is Self-Starting ✅**.
