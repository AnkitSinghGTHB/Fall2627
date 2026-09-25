# ⚡ DLD CAT-II: FINAL HANDWRITTEN COPY CHEAT SHEET
### (Compact Last-Minute Notebook Reference — Copy this directly into your notes!)

> 🎯 **Teacher's Golden Instructions:**
> 1. **Only MEALY FSM** (No Moore! Outputs go on arrows $X/Z$).
> 2. **No Flip-Flop Mentioned $\implies$ Use D Flip-Flop by DEFAULT** ($D = Q_{next}$, easiest K-map!).
> 3. **Vending Machine FSM is HIGH PRIORITY** $\implies$ Must draw circuit schematic!
> 4. **"Given Sequence $\to$ Design Circuit"** (Sequence Generator / Arbitrary Counter).
> 5. **Classnotes + Assignments = 80% of Paper**.

---

## 📌 RULE 1: The D-Flip-Flop "Zero-Thinking" Default Formula

Whenever a question says *"Design a sequential circuit / counter / FSM"* and **does NOT specify** the flip-flop type:
$$\mathbf{D_A = A_{next}, \quad D_B = B_{next}, \quad D_C = C_{next}}$$
* You **NEVER** need excitation tables ($0X, 1X$).
* Just copy the Next State column directly into your $D$ column, draw the K-Map, and connect gates to the $D$ pin!

---

## 📌 RULE 2: Mealy Machine Fast-Rules (No Moore!)
* **Output Placement:** On transition arrows: **$\text{Input} / \text{Output}$** ($\mathbf{X / Z}$).
* **State Circles:** Write **ONLY** the State Name and Binary: $\mathbf{S_0(00)}$. (Do NOT put output inside circle!).
* **State Count:** For pattern length $k \implies$ exactly **$k$ states** ($S_0, S_1, \dots, S_{k-1}$).
* **Output Timing:** Output $Z$ becomes 1 **during the clock pulse** when the last bit arrives!

---

## 🏆 PRIORITY 1: The Classic Vending Machine Mealy FSM (Complete with Circuit)

### Problem Statement:
> *"Design a vending machine FSM that dispenses a drink costing 15 cents ($Z=1$). It accepts 5-cent coins ($X=0$, Nickel) and 10-cent coins ($X=1$, Dime). The machine resets to 0 cents after dispensing. Use D flip-flops and draw the complete circuit diagram."*

### 1. State Assignment (3 States $\implies 2$ D Flip-Flops $A, B$):
* $\mathbf{S_0 (00)}$: 0 cents deposited (Reset).
* $\mathbf{S_1 (01)}$: 5 cents deposited.
* $\mathbf{S_2 (10)}$: 10 cents deposited.
* $S_3 (11)$: Unused state (Don't Care $X$).

### 2. State & Output Logic (Mealy Model):
* From $S_0 (0¢)$:
  * Insert 5¢ ($X=0$) $\to$ Total 5¢ $\implies$ Go to **$S_1 (01)$**, Output **$Z=0$**.
  * Insert 10¢ ($X=1$) $\to$ Total 10¢ $\implies$ Go to **$S_2 (10)$**, Output **$Z=0$**.
* From $S_1 (5¢)$:
  * Insert 5¢ ($X=0$) $\to$ Total 10¢ $\implies$ Go to **$S_2 (10)$**, Output **$Z=0$**.
  * Insert 10¢ ($X=1$) $\to$ Total 15¢ $\implies$ **DISPENSE!** Go to **$S_0 (00)$**, Output **$\mathbf{Z=1}$**!
* From $S_2 (10¢)$:
  * Insert 5¢ ($X=0$) $\to$ Total 15¢ $\implies$ **DISPENSE!** Go to **$S_0 (00)$**, Output **$\mathbf{Z=1}$**!
  * Insert 10¢ ($X=1$) $\to$ Total 20¢ $\implies$ **DISPENSE!** Go to **$S_0 (00)$**, Output **$\mathbf{Z=1}$**!

---

### 3. Mealy State Transition Diagram:
```
           +--- [X=0 (5¢) / Z=0] ---> S1 (01) --- [X=0 (5¢) / Z=0] ---+
           |                            |                             |
           |                            +--- [X=1 (10¢) / Z=1] --+    v
        S0 (00)                                                  +--> S2 (10)
           ^                            +--- [X=0 (5¢) / Z=1] ---+    |
           |                            |                             |
           +--- [X=1 (10¢) / Z=0] ------+--- [X=1 (10¢) / Z=1] -------+
```

---

### 4. State & D-FF Excitation Table ($D_A = A^+, D_B = B^+$):

| Present State ($AB$) | Input ($X$) | Next State ($A^+ B^+$) | $D_A = A^+$ | $D_B = B^+$ | Dispense Output ($Z$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0 0 ($S_0$)** | 0 (5¢) | 0 1 | **0** | **1** | **0** |
| **0 0 ($S_0$)** | 1 (10¢)| 1 0 | **1** | **0** | **0** |
| **0 1 ($S_1$)** | 0 (5¢) | 1 0 | **1** | **0** | **0** |
| **0 1 ($S_1$)** | 1 (10¢)| 0 0 | **0** | **0** | **1** |
| **1 0 ($S_2$)** | 0 (5¢) | 0 0 | **0** | **0** | **1** |
| **1 0 ($S_2$)** | 1 (10¢)| 0 0 | **0** | **0** | **1** |
| **1 1 (Unused)** | 0 | $X X$ | $X$ | $X$ | $X$ |
| **1 1 (Unused)** | 1 | $X X$ | $X$ | $X$ | $X$ |

---

### 5. K-Map Minimization Equations:
1. **For Dispense Output $Z(A, B, X)$:**
   * Active at $(0,1,1)$, $(1,0,0)$, $(1,0,1)$ with unused $11X$ as $X$:
   $$\mathbf{Z = A + B \cdot X}$$
   *(Meaning: Dispense if already at 10¢ ($A=1$), OR if at 5¢ ($B=1$) and insert 10¢ ($X=1$))*.

2. **For $D_A(A, B, X)$:**
   * Active at $(0,0,1)$ and $(0,1,0)$:
   $$\mathbf{D_A = \bar{A} \cdot (B \oplus X)}$$

3. **For $D_B(A, B, X)$:**
   * Active only at $(0,0,0)$:
   $$\mathbf{D_B = \bar{A} \cdot \bar{B} \cdot \bar{X}}$$

---

### 6. Vending Machine Logic Circuit Schematic:
```
           +-------+       +-------------------+
  X -------|  XOR  |-------| AND (DA)          |-------> D_A [ FF-A (MSB) ]
  B -------|       |   +---|                   |             CLK
           +-------+   |   +-------------------+              |
                       |                                      |
  A' ------------------+                                      |
                       |   +-------------------+              |
  B' ------------------+---| AND (DB)          |-------> D_B [ FF-B (LSB) ]
  X' ----------------------|                   |             CLK
                           +-------------------+              |
                                                              |
  B -----------------------+ AND                              |
  X -----------------------+-------+ OR                       |
                                   |                   CLK ---+
  A -------------------------------+-------------------> Z (Dispense Solenoid)
```

---

## 🏆 PRIORITY 2: "Given Sequence $\to$ Design Circuit" Master Recipe

### Type A: Periodic Bit Sequence Generator (e.g. Generates `1 0 1 1` repeatedly)
* **Goal:** A circuit with **no external input** that outputs periodic bits $Y = 1, 0, 1, 1 \dots$ on every clock pulse.
* **Step 1:** Sequence length $L = 4 \implies n = 2$ D Flip-Flops ($A, B$).
* **Step 2:** Form a 2-bit counter cycling $00 \to 01 \to 10 \to 11 \to 00$:
  * $D_A = A \oplus B$
  * $D_B = \bar{B}$
* **Step 3:** Assign target output bit $Y$ to each state:
  * State $00 \implies Y = 1$
  * State $01 \implies Y = 0$
  * State $10 \implies Y = 1$
  * State $11 \implies Y = 1$
* **Step 4: Output K-Map for $Y(A, B)$:**
  * Minterms: $m_0, m_2, m_3 \implies \mathbf{Y = A + \bar{B}}$.
* **Step 5: Circuit:** 2 D Flip-Flops connected as 2-bit counter, with an OR gate ($A + \bar{B}$) driving output $Y$!

---

### Type B: Arbitrary State Counter (Assignment 4, Q4: $0 \to 4 \to 6 \to 1 \to 3 \to 7 \to 2 \to 5 \to 0$)
* **Use D Flip-Flops ($D = Q_{next}$)**:
  * $D_2 = \bar{Q}_1 \bar{Q}_0 + \bar{Q}_2 Q_1$
  * $D_1 = (\bar{Q}_2 + Q_1) Q_0 + Q_2 \bar{Q}_1 \bar{Q}_0$
  * $D_0 = Q_1 \bar{Q}_0 + \bar{Q}_2 Q_0$
* **Lockout Note:** All 8 states present $\implies$ **100% lockout-free (self-starting)**!

---

### Type C: Sequence Detector (Mealy Machine with D Flip-Flops)
* **Target `101` (Paper 1 Q5):**
  * 3 states: $S_0(00)=\text{Reset}, S_1(01)=\text{'1'}, S_2(10)=\text{'10'}$.
  * Equations: $\mathbf{Z = A \cdot X}, \quad \mathbf{D_A = \bar{A} B \bar{X}}, \quad \mathbf{D_B = X}$.
* **Target `1001` (Paper 2 Q5):**
  * 4 states: $S_0(00), S_1(01), S_2(10), S_3(11)$.
  * Equations: $\mathbf{Z = A B X}, \quad \mathbf{D_A = (A \oplus B) \bar{X}}, \quad \mathbf{D_B = X + A \bar{B}}$.
* **Target `1010` (Assignment 5 Q5):**
  * Output: $\mathbf{Z = A B \bar{X}}$ (Overlap to $S_2$).

---

## 🏆 PRIORITY 3: The 80% Core Checklist (Classnotes + Assignments)

| Topic | Key Formula / Answer to Write | Trap to Avoid |
| :--- | :--- | :--- |
| **SR 5-Pulse Response (A4 Q1)** | $Q_1=1, Q_2=\text{Inv}, Q_3=0, Q_4=\text{Inv}, Q_5=\text{Indeterminate}$ | $S=R=1 \to$ Metastability & race condition! |
| **NAND T-FF Waveform (A4 Q2)** | $Q_{init}=1, T=[0,1,0,0,1,1] \implies Q=[1,0,0,0,1,0]$ | Initial is $Q=1$ (NOT 0!). |
| **Dual JK Circuit Analysis (A4 Q3)** | $A^+ = (A \oplus B) + AX, \quad F = A \oplus B$ (Moore) | $F$ depends only on $A, B \implies$ Moore! |
| **Prime Counter (A5 Q1)** | Sequence: $2 \to 3 \to 5 \to 7 \to 2$; $T_2=Q_0, T_1=\overline{Q_2 Q_1}, T_0=Q_1$ | **Must show lockout table** for $0, 1, 4, 6$! |
| **SISO 6-Pulse Shift (A5 Q3)** | Initial `1100`, In `110011` $\implies$ Final: $\mathbf{1100_2\ (12_{10})}$ | Takes $2n-1 = 7$ pulses to read out serially. |
| **Ring vs Johnson Freq (A5 Q4 / P2 Q4)** | Ring: $f_{clk}/N$; Johnson: $f_{clk}/(2N) = f_{clk}/8$ | Johnson has $2N$ states, Ring has $N$ states. |
| **Decade Ripple Counter (A4 Q5 / P2 Q3)** | $\overline{\text{CLR}} = \overline{Q_3 Q_1}$ (Active-Low NAND) | Draw timing glitch at count 10 ($1010_2$). |
| **Reverse FF Conversion (P1 Q1)** | $D = y_3 = J\bar{Q} + \bar{K}Q \implies$ **D to JK Flip-Flop** | Name both source and target flip-flops! |
| **Medical Device FSM (P1 Q2)** | Use Gray Code ($00 \to 01 \to 11 \to 10$) | **Justify:** Eliminates dynamic race hazards! |
| **8-State Reduction (P2 Q1)** | $b \equiv e, d \equiv h \implies c \equiv a \implies 5\text{ States: } \{a,c\},\{b,e\},\{d,h\},\{f\},\{g\}$ | Inspect identical Next State & Output rows! |

---

## ⚡ 30-Second Emergency Formula Card

* **JK Characteristic:** $Q^+ = J\bar{Q} + \bar{K}Q$
* **T Characteristic:** $Q^+ = T \oplus Q$
* **D Characteristic:** $Q^+ = D$
* **D Flip-Flop Excitation:** $D = Q_{next}$
* **T Flip-Flop Excitation:** $T = Q \oplus Q_{next}$
* **Ripple Max Frequency:** $f_{max} = \frac{1}{n \cdot t_{pd}}$
* **Master-Slave JK:** Eliminates race-around because Master is active at $\text{CLK}=1$, Slave at $\text{CLK}=0$.
