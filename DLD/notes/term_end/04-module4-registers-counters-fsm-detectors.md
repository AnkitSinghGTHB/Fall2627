# 📘 Unit 4: Registers, Shift Registers, Counters & FSM Design

---

## 1. Shift Registers Architectures & Pulse Budget

A register of $n$ flip-flops stores an $n$-bit binary word.

```
+-----------------------------------------------------------------------------------------+
| Architecture | Data Entry | Data Output | Loading Pulses | Unloading Pulses | Total     |
+--------------+------------+-------------+----------------+------------------+-----------+
| **SISO**     | Serial     | Serial      | n              | n - 1            | 2n - 1    |
| **SIPO**     | Serial     | Parallel    | n              | 0 (Immediate)    | n         |
| **PISO**     | Parallel   | Serial      | 1 (Load)       | n - 1 (Shift)    | n         |
| **PIPO**     | Parallel   | Parallel    | 1              | 0 (Immediate)    | 1         |
+-----------------------------------------------------------------------------------------+
```

### 1.1 Universal Shift Register (4-Bit)
Operates in 4 distinct operational modes selected via control inputs $S_1 S_0$:
* **$00$**: No Change / Hold state ($I_0 \leftarrow Q_i$)
* **$01$**: Shift-Right operation ($I_1 \leftarrow Q_{i-1}$)
* **$10$**: Shift-Left operation ($I_2 \leftarrow Q_{i+1}$)
* **$11$**: Parallel Load operation ($I_3 \leftarrow \text{Data In}_i$)

---

## 2. Counters: Asynchronous (Ripple) vs Synchronous

| Dimension | Asynchronous (Ripple) Counter | Synchronous Counter |
|:---|:---|:---|
| **Clock Connection** | Clock applied **only to first FF**; succeeding FFs clocked by previous FF outputs | **Common clock** connected simultaneously to all flip-flops |
| **Propagation Delay** | Cumulative ($t_{total} = n \times t_{pd}$); limits maximum frequency | Constant ($t_{total} = t_{pd} + t_{gate}$); operates at very high clock speeds |
| **Glitches / Decoding Errors** | High susceptibility due to ripple delay skew | Minimal / eliminated |
| **Design Complexity** | Simple hardware wiring | Requires excitation tables and K-map logic networks |

### 2.1 Ripple Counter Direction Rules
* **Negative-edge triggered FFs**: Clocking from normal output $Q$ yields an **UP-counter**; clocking from inverted output $Q'$ yields a **DOWN-counter**.
* **Positive-edge triggered FFs**: Clocking from normal output $Q$ yields a **DOWN-counter**; clocking from inverted output $Q'$ yields an **UP-counter**.

### 2.2 Modulo-$N$ Ripple Counter Reset Logic
To design a Modulo-$N$ counter using $n$ flip-flops ($2^n > N$):
* Identify binary representation of count $N$.
* Feed the flip-flop outputs that are `$1$` at count $N$ into an active-low **NAND gate** tied to the asynchronous $\overline{\text{CLR}}$ pins.
* *Example (Mod-10 Decade Counter)*: $10_{10} = 1010_2$ ($Q_3 Q_2 Q_1 Q_0$). Connect $Q_3$ and $Q_1$ into a 2-input NAND gate whose output drives all $\overline{\text{CLR}}$ inputs.

---

## 3. Ring Counter vs Johnson Counter

| Characteristic | Ring Counter | Johnson (Twisted Ring) Counter |
|:---|:---|:---|
| **Feedback Connection** | Normal output of last FF fed back: $D_0 = Q_{n-1}$ | Inverted output of last FF fed back: $D_0 = Q'_{n-1}$ |
| **Number of Distinct States** | **$N$ States** | **$2N$ States** |
| **Unused States** | $2^N - N$ | $2^N - 2N$ |
| **Decoding Complexity** | Zero (Output state directly indicated by the active single bit) | Requires 2-input AND gates for each state |
| **Frequency Division** | Divides clock frequency by **$N$** | Divides clock frequency by **$2N$** |

---

## 4. Finite State Machines: Mealy vs Moore

```
+-----------------------------------------------------------------------------------------+
|                  MEALY MACHINE                 |                 MOORE MACHINE                  |
+------------------------------------------------+------------------------------------------------+
| Output depends on:                             | Output depends on:                             |
|   Present State AND Current Input              |   Present State ONLY                           |
| Outputs change asynchronously on input change  | Outputs change synchronously on clock edge     |
| Fewer states required (typically N states)     | More states required (typically N + 1 states)  |
| Output written on transition edge (X / Z)      | Output written inside state circle (S_i / Z)   |
+-----------------------------------------------------------------------------------------+
```

---

## 5. Model Exam Questions & Answers

### Question 1 (12 Marks)
**Design a 3-bit Synchronous Counter that counts through the sequence $0 \to 1 \to 3 \to 5 \to 6 \to 0$ using T Flip-Flops. Verify whether the counter is self-starting.**

**Solution**:
1. **Flip-Flops Needed**: $n = 3$ FFs ($Q_A, Q_B, Q_C$) for 5 states. Unused states: $2, 4, 7$.
2. **State Transition & Excitation Table (using T Excitation: $T = Q_n \oplus Q_{n+1}$)**:

| Present State ($Q_A Q_B Q_C$) | Next State ($Q_A^+ Q_B^+ Q_C^+$) | $T_A$ | $T_B$ | $T_C$ |
|:---:|:---:|:---:|:---:|:---:|
| **$000$ (0)** | $001$ (1) | 0 | 0 | 1 |
| **$001$ (1)** | $011$ (3) | 0 | 1 | 0 |
| **$011$ (3)** | $101$ (5) | 1 | 1 | 0 |
| **$101$ (5)** | $110$ (6) | 0 | 1 | 1 |
| **$110$ (6)** | $000$ (0) | 1 | 1 | 0 |
| **$010$ (2)** | $X X X$ (Unused) | $X$ | $X$ | $X$ |
| **$100$ (4)** | $X X X$ (Unused) | $X$ | $X$ | $X$ |
| **$111$ (7)** | $X X X$ (Unused) | $X$ | $X$ | $X$ |

3. **K-Map Simplifications**:
   - $T_A(Q_A, Q_B, Q_C)$: Minterms $3, 6$; Don't cares $2, 4, 7$. Group $(3, 7)$ and $(6, 2) \implies \mathbf{T_A = Q_B}$.
   - $T_B(Q_A, Q_B, Q_C)$: Minterms $1, 3, 5, 6$; Don't cares $2, 4, 7$. Group $(1, 3, 5, 7) \implies Q_C$, and $(6, 7, 2, 3) \implies Q_B$.  
     Simplifies to $\mathbf{T_B = Q_C + Q_A}$.
   - $T_C(Q_A, Q_B, Q_C)$: Minterms $0, 5$; Don't cares $2, 4, 7$. Group $(0, 4) \implies Q_B' Q_C'$, group $(5, 7) \implies Q_A Q_C$.  
     Simplifies to $\mathbf{T_C = Q_A Q_C + Q_B' Q_C'}$.
4. **Self-Starting Check**:
   - For unused state $2$ ($010$): $T_A = 1, T_B = 0, T_C = 1 \implies \text{Next State} = 111$ (State 7).
   - For unused state $7$ ($111$): $T_A = 1, T_B = 1, T_C = 1 \implies \text{Next State} = 000$ (State 0, enters valid cycle!).
   - For unused state $4$ ($100$): $T_A = 0, T_B = 1, T_C = 1 \implies \text{Next State} = 111$ (State 7 ➔ State 0).
   - **Conclusion**: All unused states enter the valid loop within 2 clock cycles $\implies$ **Counter is 100% self-starting!**

### Question 2 (8 Marks)
**Design a Mealy Sequence Detector to detect the binary sequence `101` with overlapping capability. Draw the state diagram and state transition table.**

**Solution**:
1. **States Definition**:
   - $S_0$: Reset state (no bits matched).
   - $S_1$: First bit `1` detected.
   - $S_2$: Sequence `10` detected.
2. **Transition Rules**:
   - From $S_0$: Input `1` $\to S_1/0$; Input `0` $\to S_0/0$.
   - From $S_1$: Input `0` $\to S_2/0$; Input `1` $\to S_1/0$.
   - From $S_2$: Input `1` $\to S_1/1$ (Sequence `101` detected! Because overlapping is enabled, the trailing `1` serves as the first bit of the next sequence, transitioning back to $S_1$ with output $Z = 1$); Input `0` $\to S_0/0$.
3. **State Table**:

| Present State | Next State ($X=0$) | Output $Z$ ($X=0$) | Next State ($X=1$) | Output $Z$ ($X=1$) |
|:---:|:---:|:---:|:---:|:---:|
| **$S_0$** | $S_0$ | 0 | $S_1$ | 0 |
| **$S_1$** | $S_2$ | 0 | $S_1$ | 0 |
| **$S_2$** | $S_0$ | 0 | **$S_1$** | **1** |
