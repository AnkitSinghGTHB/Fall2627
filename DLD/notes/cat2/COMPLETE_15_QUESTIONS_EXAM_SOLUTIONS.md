# ⚡ ECE2002: Digital Logic Design (CAT-II)
## Complete Solutions to the 15 High-Yield Exam & Assignment Questions

> **Course:** ECE2002 — Digital Logic Design | **Institution:** VIT Bhopal  
> **Coverage:** All 15 Questions across Sequence Detectors, Counters, Shift Registers, FSMs & Flip-Flops  
> **Format:** 100% Step-by-Step, Formula-Backed, Exam-Ready Solutions with Tables and Schematics

---

# PART 1: Sequence Detectors & FSM Design

---

## 📝 QUESTION 1: Synchronous Sequence Detector for "101"

### Problem Statement:
> *"Design a synchronous sequential circuit for output $Z = 1$ when sequence '101' is detected."*

### 1. Model & State Definition (Mealy Overlapping Model)
* Target sequence: `101` (Length $k=3 \implies 3$ states in Mealy model).
* **State Definitions:**
  * $\mathbf{S_0 (00)}$: Reset / Initial State (No bits matched).
  * $\mathbf{S_1 (01)}$: Detected first bit `'1'`.
  * $\mathbf{S_2 (10)}$: Detected first two bits `'10'`.
  * $S_3 (11)$: Unused State (Don't Care $X$).

### 2. State Transition & Output Logic
* From $S_0$: If $X=0 \to S_0 (Z=0)$; If $X=1 \to S_1 (Z=0)$.
* From $S_1$: If $X=1 \to S_1 (Z=0)$ (Self-loop on consecutive 1s); If $X=0 \to S_2 (Z=0)$.
* From $S_2$:
  * If $X=0 \to S_0 (Z=0)$ (Bit string `100` breaks pattern, reset).
  * If $X=1 \to \mathbf{S_1 (Z=1)}$! (Pattern `101` found! Suffix `'1'` matches $S_1$ for overlapping detection).

### 3. State & D Flip-Flop Excitation Table ($D_A = A^+, D_B = B^+$)
| Present State ($AB$) | Input ($X$) | Next State ($A^+ B^+$) | $D_A = A^+$ | $D_B = B^+$ | Output ($Z$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0 0 ($S_0$)** | 0 | 0 0 | 0 | 0 | 0 |
| **0 0 ($S_0$)** | 1 | 0 1 | 0 | 1 | 0 |
| **0 1 ($S_1$)** | 0 | 1 0 | 1 | 0 | 0 |
| **0 1 ($S_1$)** | 1 | 0 1 | 0 | 1 | 0 |
| **1 0 ($S_2$)** | 0 | 0 0 | 0 | 0 | 0 |
| **1 0 ($S_2$)** | 1 | 0 1 | 0 | 1 | **1** |
| **1 1 (Unused)**| 0, 1 | $X X$ | $X$ | $X$ | $X$ |

### 4. K-Map Minimization Equations
* **Output:** $\mathbf{Z = A \cdot X}$
* **Flip-Flop A:** $\mathbf{D_A = \bar{A} B \bar{X}}$
* **Flip-Flop B:** $\mathbf{D_B = X}$

### 5. Logic Circuit Schematic
* 2 D Flip-Flops ($A$ and $B$) with common clock.
* $D_A$ driven by 3-input AND gate: $\bar{A} \cdot B \cdot \bar{X}$.
* $D_B$ connected directly to input line $X$.
* Output $Z$ driven by 2-input AND gate: $A \cdot X$.

---

## 📝 QUESTION 2: Mealy Sequence Detector for "1011" (Overlapping, D Flip-Flops)

### Problem Statement:
> *"Design a Mealy sequence detector for 1011 with overlapping detection. Draw the state diagram and state table, derive the next-state/output equations, and implement it using D flip-flops."*

### 1. State Formulation (4 States $\implies 2$ D Flip-Flops $A, B$)
* Target: `1011` ($k=4$).
* $\mathbf{S_0 (00)}$: Reset / No match.
* $\mathbf{S_1 (01)}$: Got `'1'`.
* $\mathbf{S_2 (10)}$: Got `'10'`.
* $\mathbf{S_3 (11)}$: Got `'101'`.

### 2. State Transition & Output Rules (Overlapping)
* In $S_3$ (we have `101`):
  * If $X=1$ arrives $\implies$ Target `1011` completed! Output $\mathbf{Z = 1}$. The longest suffix is `'1'`, so transition to **$S_1$**.
  * If $X=0$ arrives $\implies$ Sequence becomes `1010`. The longest suffix is `'10'`, which matches **$S_2$** ($Z=0$).

### 3. State & D-FF Excitation Table ($D_A = A^+, D_B = B^+$)
| Present State ($AB$) | Input ($X$) | Next State ($A^+ B^+$) | $D_A = A^+$ | $D_B = B^+$ | Output ($Z$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0 0 ($S_0$)** | 0 | 0 0 | 0 | 0 | 0 |
| **0 0 ($S_0$)** | 1 | 0 1 | 0 | 1 | 0 |
| **0 1 ($S_1$)** | 0 | 1 0 | 1 | 0 | 0 |
| **0 1 ($S_1$)** | 1 | 0 1 | 0 | 1 | 0 |
| **1 0 ($S_2$)** | 0 | 0 0 | 0 | 0 | 0 |
| **1 0 ($S_2$)** | 1 | 1 1 | 1 | 1 | 0 |
| **1 1 ($S_3$)** | 0 | 1 0 | 1 | 0 | 0 |
| **1 1 ($S_3$)** | 1 | 0 1 | 0 | 1 | **1** |

### 4. K-Map Derivation
* **$D_A(A, B, X)$:** Active at $(0,1,0), (1,0,1), (1,1,0)$:
  $$\mathbf{D_A = B\bar{X} + A\bar{B}X}$$
* **$D_B(A, B, X)$:** Active at all odd rows where $X=1$:
  $$\mathbf{D_B = X}$$
* **Output $Z(A, B, X)$:** Active only at $(1,1,1)$:
  $$\mathbf{Z = A \cdot B \cdot X}$$

### 5. Circuit Implementation
* Flip-Flop $B$ has $D_B = X$.
* Flip-Flop $A$ has $D_A = (B \cdot \bar{X}) + (A \cdot \bar{B} \cdot X)$.
* Output $Z = A \cdot B \cdot X$ (3-input AND gate).

---

## 📝 QUESTION 3: Synchronous Sequence Detector for "1100" (Overlapping, T Flip-Flops)

### Problem Statement:
> *"Design a synchronous sequential circuit for a sequence detector that produces output $Z=1$ whenever the input sequence '1100' is detected (overlapping). Draw state diagram and state table, derive next-state and output equations, and implement using T flip-flops."*

### 1. State Definition (4 States $\implies 2$ T Flip-Flops $A, B$)
* $\mathbf{S_0 (00)}$: Reset.
* $\mathbf{S_1 (01)}$: Got `'1'`.
* $\mathbf{S_2 (10)}$: Got `'11'`.
* $\mathbf{S_3 (11)}$: Got `'110'`.

### 2. Transition Rules (Overlapping)
* From $S_3$ (have `110`):
  * If $X=0 \implies$ string `1100` matched! Output $\mathbf{Z = 1}$. Suffix `0` has no match in `11`, resets to **$S_0$**.
  * If $X=1 \implies$ string `1101`. Longest matching suffix is `'1'`, transitions to **$S_1$** ($Z=0$).

### 3. State & T-FF Excitation Table ($T = Q \oplus Q^+$)
| Present State ($AB$) | Input ($X$) | Next State ($A^+ B^+$) | $T_A = A \oplus A^+$ | $T_B = B \oplus B^+$ | Output ($Z$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0 0 ($S_0$)** | 0 | 0 0 | 0 | 0 | 0 |
| **0 0 ($S_0$)** | 1 | 0 1 | 0 | 1 | 0 |
| **0 1 ($S_1$)** | 0 | 0 0 | 0 | 1 | 0 |
| **0 1 ($S_1$)** | 1 | 1 0 | 1 | 1 | 0 |
| **1 0 ($S_2$)** | 0 | 1 1 | 0 | 1 | 0 |
| **1 0 ($S_2$)** | 1 | 1 0 | 0 | 0 | 0 |
| **1 1 ($S_3$)** | 0 | 0 0 | 1 | 1 | **1** |
| **1 1 ($S_3$)** | 1 | 0 1 | 1 | 0 | 0 |

### 4. K-Map Derivation
* **Output:** $\mathbf{Z = A \cdot B \cdot \bar{X}}$
* **$T_A(A, B, X)$:** Minterms $m_3(011), m_6(110), m_7(111)$:
  $$\mathbf{T_A = A B + \bar{A} B X = B(A + X)}$$
* **$T_B(A, B, X)$:** Minterms $m_1(001), m_2(010), m_3(011), m_4(100), m_6(110)$:
  $$\mathbf{T_B = \bar{A}X + B\bar{X} + A\bar{B}\bar{X}}$$

---

## 📝 QUESTION 4: Moore Sequence Detector for "1001" (Overlapping, D Flip-Flops)

### Problem Statement:
> *"Design a Moore sequence detector for the sequence '1001' with overlapping detection. Construct state diagram and state transition table, assign binary states, derive excitation equations for D flip-flops, and determine output equation. Verify operation for input sequence 1001001."*

### 1. Moore State Assignment ($k+1 = 5$ States $\implies 3$ Flip-Flops $Q_2 Q_1 Q_0$)
In a Moore machine, output depends strictly on the state. To indicate detection, an explicit state $S_4$ with $Z=1$ is required:
* $\mathbf{S_0 (000)}$: Reset ($Z=0$)
* $\mathbf{S_1 (001)}$: Got `'1'` ($Z=0$)
* $\mathbf{S_2 (010)}$: Got `'10'` ($Z=0$)
* $\mathbf{S_3 (011)}$: Got `'100'` ($Z=0$)
* $\mathbf{S_4 (100)}$: Got `'1001'` ($\mathbf{Z=1}$!)
* States $101, 110, 111$ are unused ($X$).

### 2. Moore State Table
| Present State ($Q_2 Q_1 Q_0$) | Next State ($X=0$) | Next State ($X=1$) | Moore Output ($Z$) |
| :---: | :---: | :---: | :---: |
| **$S_0$ (000)** | 000 ($S_0$) | 001 ($S_1$) | 0 |
| **$S_1$ (001)** | 010 ($S_2$) | 001 ($S_1$) | 0 |
| **$S_2$ (010)** | 011 ($S_3$) | 001 ($S_1$) | 0 |
| **$S_3$ (011)** | 000 ($S_0$) | 100 ($S_4$) | 0 |
| **$S_4$ (100)** | 010 ($S_2$) | 001 ($S_1$) | **1** |

### 3. D Flip-Flop Equations ($D = Q^+$)
* **Output Equation:** $\mathbf{Z = Q_2}$ (Active only in state $S_4$).
* **$D_2 = Q_1 Q_0 X$** (Transition $S_3 \xrightarrow{X=1} S_4$).
* **$D_1 = \bar{Q}_2 \bar{Q}_1 Q_0 \bar{X} + \bar{Q}_2 Q_1 \bar{Q}_0 \bar{X} + Q_2 \bar{X} = (\bar{Q}_2 Q_0 + Q_1 \bar{Q}_0 + Q_2)\bar{X}$**.
* **$D_0 = X$** (Every state transitions to $S_1(001)$ when $X=1$, except $S_3$ which transitions to $S_4(100)$).

### 4. Verification for Input Sequence `1 0 0 1 0 0 1`:
| Clock Cycle | Input $X$ | Current State | State Code ($Q_2 Q_1 Q_0$) | Moore Output $Z$ | Sequence Status |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **$t_0$** | — | $S_0$ | 000 | 0 | Initial Reset |
| **$t_1$** | **1** | $S_1$ | 001 | 0 | Got `'1'` |
| **$t_2$** | **0** | $S_2$ | 010 | 0 | Got `'10'` |
| **$t_3$** | **0** | $S_3$ | 011 | 0 | Got `'100'` |
| **$t_4$** | **1** | **$S_4$** | **100** | **1** | **1st '1001' Detected!** |
| **$t_5$** | **0** | $S_2$ | 010 | 0 | Overlapping suffix `'10'` |
| **$t_6$** | **0** | $S_3$ | 011 | 0 | Got `'100'` |
| **$t_7$** | **1** | **$S_4$** | **100** | **1** | **2nd '1001' Detected!** |

* **Verified:** Detected at $t_4$ and $t_7$.

---

## 📝 QUESTION 5: Detect Two Consecutive Occurrences of "01" (Three D Flip-Flops)

### Problem Statement:
> *"Design a synchronous sequential circuit that detects two consecutive occurrences of the bit pattern '01' (i.e. '0101'). Generate $Z=1$ only when detected (overlapping). Draw state diagram, state table, derive D flip-flop equations, and implement using three D flip-flops."*

### 1. State Definition (5 States $\implies 3$ D Flip-Flops $A, B, C$)
* $\mathbf{S_0 (000)}$: Reset / Idle.
* $\mathbf{S_1 (001)}$: Got first `'0'`.
* $\mathbf{S_2 (010)}$: Got first `'01'` (1st occurrence complete!).
* $\mathbf{S_3 (011)}$: Got `'010'` (1st occurrence + second `'0'`).
* $\mathbf{S_4 (100)}$: Got `'0101'` ($\mathbf{Z=1}$, 2nd occurrence complete!).
* Unused states: $101, 110, 111$.

### 2. State Transition Table (Mealy Model)
| Present State ($ABC$) | Next State ($X=0$) | Output ($X=0$) | Next State ($X=1$) | Output ($X=1$) |
| :---: | :---: | :---: | :---: | :---: |
| **$S_0$ (000)** | 001 ($S_1$) | 0 | 000 ($S_0$) | 0 |
| **$S_1$ (001)** | 001 ($S_1$) | 0 | 010 ($S_2$) | 0 |
| **$S_2$ (010)** | 011 ($S_3$) | 0 | 000 ($S_0$) | 0 |
| **$S_3$ (011)** | 001 ($S_1$) | 0 | **010 ($S_2$)** | **1 (Pattern Found!)** |
| **$S_4$ (100)** | 011 ($S_3$) | 0 | 000 ($S_0$) | 0 |

### 3. D Flip-Flop Input Equations ($D = Q_{next}$)
* **Output:** $\mathbf{Z = \bar{A} B C X}$ (Active in $S_3$ on input $X=1$).
* **$D_A = 0$** (In Mealy model, state $S_4$ is folded into the transition from $S_3 \xrightarrow{X=1} S_2$ with $Z=1$, allowing $D_A=0$ or keeping $A$ for state retention).
* **$D_B = \bar{A}\bar{B}CX + \bar{A}B\bar{C}\bar{X} + \bar{A}BCX$**.
* **$D_C = \bar{A}\bar{B}\bar{C}\bar{X} + \bar{A}\bar{B}C\bar{X} + \bar{A}B\bar{C}\bar{X} + \bar{A}BC\bar{X} = \mathbf{\bar{A}\bar{X}}$**.

---

# PART 2: Counters, Shift Registers & State Table Reduction

---

## 📝 QUESTION 6: Synchronous Prime Number Counter (1 to 10) Using T Flip-Flops

### 1. Count Sequence & Flip-Flops
* Primes between 1 and 10: $\mathbf{2 \to 3 \to 5 \to 7 \to 2}$.
* Highest count is $7 \implies 3$ Flip-Flops ($Q_2 Q_1 Q_0$).
* Valid states: $2(010), 3(011), 5(101), 7(111)$. Unused: $0, 1, 4, 6$ (Don't care $X$).

### 2. State & T-FF Excitation Table ($T = Q \oplus Q^+$)
| State Dec | Present State ($Q_2 Q_1 Q_0$) | Next State ($Q_2^+ Q_1^+ Q_0^+$) | $T_2$ | $T_1$ | $T_0$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **2** | 0 1 0 | 0 1 1 | **0** | **0** | **1** |
| **3** | 0 1 1 | 1 0 1 | **1** | **1** | **0** |
| **5** | 1 0 1 | 1 1 1 | **0** | **1** | **0** |
| **7** | 1 1 1 | 0 1 0 | **1** | **0** | **1** |
| **0, 1, 4, 6** | Unused | $X X X$ | $X$ | $X$ | $X$ |

### 3. K-Map Derivation:
* $\mathbf{T_2 = Q_0}$
* $\mathbf{T_1 = \bar{Q}_1 + \bar{Q}_2 = \overline{Q_2 Q_1}}$
* $\mathbf{T_0 = Q_1}$

### 4. Lockout Analysis (Tracing Unused States):
* State $0 (000) \implies T_2=0, T_1=1, T_0=0 \implies \mathbf{010_2\ (2)}$ (Enters valid cycle!).
* State $1 (001) \implies T_2=1, T_1=1, T_0=0 \implies \mathbf{111_2\ (7)}$ (Enters valid cycle!).
* State $4 (100) \implies T_2=0, T_1=1, T_0=0 \implies \mathbf{110_2\ (6)} \to \mathbf{010_2\ (2)}$ (Enters in 2 pulses!).
* State $6 (110) \implies T_2=0, T_1=0, T_0=1 \implies \mathbf{111_2\ (7)}$ (Enters valid cycle!).
* **Conclusion: 100% Lockout-Free and Self-Starting!**

---

## 📝 QUESTION 7: MOD-10 Synchronous Counter for Filtration System

### 1. Specification & State Diagram
* Maintenance triggered after 10 cycles $\implies$ Counts $0 \to 1 \to 2 \dots \to 9 \to 0$.
* Flip-Flops: $2^4 = 16 \ge 10 \implies \mathbf{4\text{ Flip-Flops}}$ ($Q_3 Q_2 Q_1 Q_0$).
* Valid: 0 to 9. Unused: 10 to 15 ($X$).

### 2. Excitation Equations (T Flip-Flops):
* $\mathbf{T_0 = 1}$ (Toggles every clock pulse).
* $\mathbf{T_1 = Q_0 \bar{Q}_3}$ (Toggles on $Q_0=1$, blocked at state 9).
* $\mathbf{T_2 = Q_1 Q_0}$ (Toggles on $Q_1 Q_0 = 1$).
* $\mathbf{T_3 = Q_2 Q_1 Q_0 + Q_3 Q_0}$ (Sets on 7 to 8, resets on 9 to 0).

### 3. Explanation of Automatic Reset After 10th Cycle:
* At state 9 ($Q_3 Q_2 Q_1 Q_0 = \mathbf{1001_2}$):
  * $T_0 = 1 \implies Q_0^+ = 0$.
  * $T_1 = 1 \cdot \bar{1} = 0 \implies Q_1^+ = 0$.
  * $T_2 = 0 \cdot 1 = 0 \implies Q_2^+ = 0$.
  * $T_3 = 0 + (1 \cdot 1) = 1 \implies Q_3^+ = 0$.
* Flip-flops flip synchronously from $\mathbf{1001_2 \to 0000_2}$ on the 10th clock pulse! No external gates or glitches occur.

---

## 📝 QUESTION 8: Digital Locker 4-Bit Shift Register

### 1. Suitable Shift Register Selection:
* **Serial-In Parallel-Out (SIPO)** Shift Register.
* User keys in 4 bits serially; lock comparator checks all 4 bits in parallel.

### 2. 4-Clock-Pulse Execution Trace (Loading Code `1011`):
| Clock Pulse | Keypad Serial In | $Q_3$ | $Q_2$ | $Q_1$ | $Q_0$ | Stored Code Word |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Initial** | — | 0 | 0 | 0 | 0 | `0000` |
| **$t_1$** | **1** | **1** | 0 | 0 | 0 | `1000` |
| **$t_2$** | **0** | **0** | **1** | 0 | 0 | `0100` |
| **$t_3$** | **1** | **1** | **0** | **1** | 0 | `1010` |
| **$t_4$** | **1** | **1** | **1** | **0** | **1** | **`1101` (or `1011`)** |

* At $t_4$, code comparator strobe opens the locker!

---

## 📝 QUESTION 9: Serial & Parallel "1001" Shift Register System

### Problem Statement:
> *"Serial bit '1001' needs to be obtained serially after every clock cycle. Also this data needs to be obtained at the same time after 4 clock cycles. Design the logic using a single digital system using shift registers."*

### 1. System Architecture: 4-Bit Circulating Shift Register with Parallel Taps
* **Hardware Components:**
  * 4 D Flip-Flops: $FF_3, FF_2, FF_1, FF_0$ with common clock.
  * Asynchronous Preset/Clear pins initialized to: $Q_3 Q_2 Q_1 Q_0 = \mathbf{1001_2}$.
  * **Circulating Feedback:** Connect output $Q_0$ of the last flip-flop directly back to data input $D_3$ of the first flip-flop:
    $$\mathbf{D_3 = Q_0}, \quad D_2 = Q_3, \quad D_1 = Q_2, \quad D_0 = Q_1$$

### 2. Verification of Dual Requirements:
1. **Serial Bit Stream Every Clock Cycle:**
   * Look at serial output pin $Q_0$:
     * Clock 1: $Q_0$ outputs bit **`1`**.
     * Clock 2: $Q_0$ outputs bit **`0`**.
     * Clock 3: $Q_0$ outputs bit **`0`**.
     * Clock 4: $Q_0$ outputs bit **`1`**.
   * It delivers the bit sequence `1, 0, 0, 1` continuously!
2. **Parallel Word After 4 Clock Cycles:**
   * Because data circulates ($MOD = 4$), after exactly 4 clock cycles, all bits rotate back to their original positions:
     $$Q_3 Q_2 Q_1 Q_0 = \mathbf{1001_2}$$
   * The complete 4-bit word is available simultaneously on parallel bus $[Q_3, Q_2, Q_1, Q_0]$!

---

## 📝 QUESTION 10: State Table Response, Minimization & T Flip-Flop Implementation

### Given State Table:
| Present State | Next State, Output ($X=0$) | Next State, Output ($X=1$) |
| :---: | :---: | :---: |
| **A** | B, 1 | C, 0 |
| **B** | A, 0 | D, 1 |
| **C** | D, 1 | B, 1 |
| **D** | A, 0 | C, 0 |

### Part (i): Output Sequence for Input `0 1 1 1 0 0` Starting at State `A`:
1. Start at $A$. Input $X=0 \implies$ Next State = **$B$**, Output $Z = \mathbf{1}$.
2. At $B$. Input $X=1 \implies$ Next State = **$D$**, Output $Z = \mathbf{1}$.
3. At $D$. Input $X=1 \implies$ Next State = **$C$**, Output $Z = \mathbf{0}$.
4. At $C$. Input $X=1 \implies$ Next State = **$B$**, Output $Z = \mathbf{1}$.
5. At $B$. Input $X=0 \implies$ Next State = **$A$**, Output $Z = \mathbf{0}$.
6. At $A$. Input $X=0 \implies$ Next State = **$B$**, Output $Z = \mathbf{1}$.

* **State Path:** $A \to B \to D \to C \to B \to A \to B$.
* **Output Sequence:** $\mathbf{1, 1, 0, 1, 0, 1}$!

### Part (ii): State Reduction & T Flip-Flop Implementation:
* **Reduction Analysis:**
  * Outputs on $(X=0, X=1)$ for each state:
    * $A: (1, 0)$
    * $B: (0, 1)$
    * $C: (1, 1)$
    * $D: (0, 0)$
  * **Every single state has a completely unique output vector!**
  * No two states can be equivalent. The table is **ALREADY MINIMAL (4 States)**.
* **T Flip-Flop Implementation:**
  * State assignment: $A=00, B=01, C=10, D=11$ (Flip-Flops $y_1, y_2$).
  * Excitation: $T_1 = y_1 \oplus y_1^+, \quad T_2 = y_2 \oplus y_2^+$.
  * K-Maps:
    * $\mathbf{T_1 = y_2 \bar{X} + y_1 X}$
    * $\mathbf{T_2 = \bar{y}_1 \bar{y}_2 \bar{X} + y_1 y_2 X + \bar{y}_1 y_2 X}$
    * $\mathbf{Z = \bar{y}_1 \bar{y}_2 \bar{X} + \bar{y}_1 y_2 X + y_1 \bar{y}_2}$

---

# PART 3: Flip-Flop Concepts & Real-World FSMs

---

## 📝 QUESTION 11: Flip-Flop for Transparent Output (Same as Input)

* **Chosen Flip-Flop:** **D Flip-Flop (Data / Delay Flip-Flop)**.
* **Why:** Characteristic equation is:
  $$\mathbf{Q_{next} = D}$$
* The stored state and output $Q$ replicate input $D$ on each clock edge with a 1-clock delay. Used in shift registers, pipeline registers, and data buffers.

---

## 📝 QUESTION 12: Flip-Flop to Flip Output at Every Clock Cycle

* **Chosen Flip-Flop:** **T Flip-Flop** with $T = 1$ (or **JK Flip-Flop** with $J = K = 1$).
* **Why:** Characteristic equation is $Q_{next} = T \oplus Q$.
  * When $T = 1 \implies \mathbf{Q_{next} = \bar{Q}}$.
* Output inverts continuously ($0 \to 1 \to 0 \to 1$), dividing clock frequency by 2: $\mathbf{f_{out} = f_{clk} / 2}$.

---

## 📝 QUESTION 13: Flip-Flop with Unstable Output (Identification & Explanation)

1. **SR Flip-Flop under $S=1, R=1$ (Metastability / Invalid Condition):**
   * In cross-coupled NAND/NOR gates, active inputs on both $S$ and $R$ force both $Q$ and $\bar{Q}$ to identical levels ($Q=\bar{Q}=1$).
   * Transitioning to $S=R=0$ creates a race condition. Unequal propagation delays cause the output to hover in a **metastable state** before collapsing unpredictably to 0 or 1.
2. **Level-Triggered JK Flip-Flop (Race-Around Condition):**
   * When $J=K=1$ and clock pulse width $t_w > t_{pd}$, the output toggles repeatedly within a single clock pulse, leaving $Q$ unstable and indeterminate.
   * **Cure:** Master-Slave structure or edge-triggering.

---

## 📝 QUESTION 14: Medical Monitoring Device FSM (JK Flip-Flops)

* 4 States: A (Standby), B (Monitoring), C (Warning), D (Emergency Shutdown).
* **State Assignment Justification (The Critical Mark):**
  * Binary assignment ($01 \to 10$) switches 2 bits at once, risking transient glitch states ($00$ or $11$) due to unequal gate delays. A momentary false "Shutdown" could halt life-support pumps!
  * **Gray Code ($A=00, B=01, C=11, D=10$)** changes only **1 bit per valid transition**, 100% eliminating dynamic hazards.
* JK-FF Equations:
  $$\mathbf{J_A = B \cdot X}, \quad \mathbf{K_A = B \cdot \bar{X}}, \quad \mathbf{J_B = \bar{A} \cdot X}, \quad \mathbf{K_B = A \cdot X}$$

---

## 📝 QUESTION 15: Toy Robot State Machine (D Flip-Flops)

* 4 Modes: Standing (00) $\to$ Walking (01) $\to$ Tumbling (10) $\to$ Clapping (11) $\to$ Standing (00).
* Button $X=1$ advances mode; $X=0$ holds mode.
* **D Flip-Flop Equations:**
  $$\mathbf{D_1 = A \oplus (B \cdot X)}$$
  $$\mathbf{D_0 = B \oplus X}$$
* Logic schematic uses 2 D Flip-Flops, 1 AND gate ($B \cdot X$), and 2 XOR gates.
