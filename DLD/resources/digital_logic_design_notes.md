# Digital Logic Design: Modules 3 & 4 Complete Notes

---

## Module 3: Registers & Shift Registers

### 1. Overview and Fundamental Concepts
* **Register**: A group of flip-flops used to store binary data. Each flip-flop stores $1$ bit of information; thus, an $n$-bit register contains $n$ flip-flops.
* **Shift Register**: A sequential logic circuit designed to store binary data and shift it left or right by one position during each clock pulse.
* **Primary Applications**:
  * Temporary data storage and data buffering.
  * Serial-to-parallel and parallel-to-serial data conversion.
  * Arithmetic operations (shifting left by 1 bit multiplies by 2; shifting right by 1 bit divides by 2 in unsigned binary).
  * Sequence generation and frequency division (Ring and Johnson counters).

Shift registers are classified into four primary architectures based on how data enters and leaves the register:
1. **SISO**: Serial-In Serial-Out
2. **SIPO**: Serial-In Parallel-Out
3. **PIPO**: Parallel-In Parallel-Out
4. **PISO**: Parallel-In Serial-Out

---

### 2. Serial-In Serial-Out (SISO) Shift Register

In a SISO shift register, data is presented serially (one bit per clock cycle) at the input of the first flip-flop and retrieved serially from the output of the final flip-flop.

#### Block Diagram (4-Bit SISO)
```text
Serial In ---> [ D   Q ] ---> [ D   Q ] ---> [ D   Q ] ---> [ D   Q ] ---> Serial Out
                 FF A           FF B           FF C           FF D
                 (Q_A)          (Q_B)          (Q_C)          (Q_D)
                   ^              ^              ^              ^
 Clock ------------+--------------+--------------+--------------+
```

#### Clock Pulse Analysis
* **Clock pulses to load $n$ bits**: $n$ clock pulses.
* **Clock pulses to completely read out $n$ bits**: $n - 1$ additional clock pulses (since the first bit appears at the output on the $n$-th loading pulse).
* **Total clock pulses**:
  $$\text{Total Pulses} = n + (n - 1) = 2n - 1$$
  For a 4-bit word (`1111`), the total number of clock pulses required is $2(4) - 1 = \mathbf{7\text{ clock pulses}}$.

#### State Transition Table (Loading and Unloading `1111`)
Assuming the register is initially reset ($Q_A Q_B Q_C Q_D = 0000$):

| Clock Pulse | Serial Input ($D_A$) | $Q_A$ | $Q_B$ | $Q_C$ | $Q_D$ (Serial Out) | Action / Description |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Initial** | — | 0 | 0 | 0 | 0 | Register cleared |
| **$1\uparrow$** | 1 | 1 | 0 | 0 | 0 | 1st bit enters FF A |
| **$2\uparrow$** | 1 | 1 | 1 | 0 | 0 | 2nd bit enters; 1st bit shifts to FF B |
| **$3\uparrow$** | 1 | 1 | 1 | 1 | 0 | 3rd bit enters; bits shift right |
| **$4\uparrow$** | 1 | 1 | 1 | 1 | 1 | 4th bit enters; register holds `1111` (Bit 1 at output) |
| **$5\uparrow$** | 0 | 0 | 1 | 1 | 1 | 2nd bit shifted to output |
| **$6\uparrow$** | 0 | 0 | 0 | 1 | 1 | 3rd bit shifted to output |
| **$7\uparrow$** | 0 | 0 | 0 | 0 | 1 | 4th bit shifted to output |

---

### 3. Serial-In Parallel-Out (SIPO) Shift Register

In a SIPO shift register, data is loaded serially bit-by-bit, but the outputs of all flip-flops are accessible simultaneously.

#### Block Diagram (4-Bit SIPO)
```text
Serial In ---> [ D   Q ] -------> [ D   Q ] -------> [ D   Q ] -------> [ D   Q ]
                 FF A               FF B               FF C               FF D
                   |                  |                  |                  |
                   v                  v                  v                  v
                  Q_A                Q_B                Q_C                Q_D
                   ^                  ^                  ^                  ^
 Clock ------------+------------------+------------------+------------------+
```

#### Clock Pulse Analysis
* To load an $n$-bit word into the register and read it out in parallel requires exactly **$n$ clock pulses**.
* For a 4-bit word (`1111`): **4 clock pulses**.

#### State Transition Table (Loading `1111`)

| Clock Pulse | Serial Input ($D_A$) | $Q_A$ | $Q_B$ | $Q_C$ | $Q_D$ | Parallel Output ($Q_A Q_B Q_C Q_D$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Initial** | — | 0 | 0 | 0 | 0 | `0000` |
| **$1\uparrow$** | 1 | 1 | 0 | 0 | 0 | `1000` |
| **$2\uparrow$** | 1 | 1 | 1 | 0 | 0 | `1100` |
| **$3\uparrow$** | 1 | 1 | 1 | 1 | 0 | `1110` |
| **$4\uparrow$** | 1 | 1 | 1 | 1 | 1 | `1111` |

---

### 4. Parallel-In Parallel-Out (PIPO) Shift Register

In a PIPO shift register, all bits are loaded simultaneously from parallel inputs on a single active clock transition, and all bits are simultaneously read from their parallel outputs.

#### Block Diagram (4-Bit PIPO)
```text
          Parallel In:    D_A          D_B          D_C          D_D
                           |            |            |            |
                           v            v            v            v
                        [ D  Q ]     [ D  Q ]     [ D  Q ]     [ D  Q ]
                          FF A         FF B         FF C         FF D
                           |            |            |            |
                           v            v            v            v
         Parallel Out:    Q_A          Q_B          Q_C          Q_D
                           ^            ^            ^            ^
 Clock --------------------+------------+------------+------------+
```

* **Clock Requirement**: Only **1 clock pulse** is needed for parallel load and parallel read.
* **Speed**: Highest throughput among all register architectures.

---

### 5. Parallel-In Serial-Out (PISO) Shift Register

Data is loaded into the register in parallel and shifted out serially one bit per clock cycle.

* **Control Signal**: A control line $\text{Shift}/\overline{\text{Load}}$ determines the operation mode:
  * When $\text{Shift}/\overline{\text{Load}} = 0$ (Load Mode): Parallel inputs $X_A, X_B, X_C, X_D$ are gated directly into flip-flop inputs.
  * When $\text{Shift}/\overline{\text{Load}} = 1$ (Shift Mode): Flip-flops receive data from the output of the preceding flip-flop, shifting bits toward the serial output.
* **Input Steering Combinational Logic for Stage $k$**:
  $$D_k = (\text{Shift} \cdot Q_{k-1}) + (\overline{\text{Shift}} \cdot X_k)$$
* **Clock Requirement**: 1 clock pulse to load the data in parallel + $(n - 1)$ clock pulses to shift the remaining bits out serially = **$n$ clock pulses**.

---

### 6. Ring Counter and Johnson Counter

#### A. Ring Counter
A ring counter is a circulating shift register where the output of the final stage is connected directly back to the data input of the first stage:
$$D_A = Q_D$$

```text
        +-------------------------------------------------------------+
        |                                                             |
        v                                                             |
     [ D  Q ] --------> [ D  Q ] --------> [ D  Q ] --------> [ D  Q ]+
       FF A               FF B               FF C               FF D
      (Q_A)              (Q_B)              (Q_C)              (Q_D)
        ^                  ^                  ^                  ^
 Clock -+------------------+------------------+------------------+
```

* **States & Modulus**: An $n$-bit ring counter has **$n$ unique states** (Modulus $\text{MOD} = n$).
* **Pre-loading Condition**: A single bit (`1`) must be pre-loaded into stage A, with all other stages cleared (`1000`).
* **State Sequence (4-Bit Ring Counter)**:
  $$\text{1000} \to \text{0100} \to \text{0010} \to \text{0001} \to \text{1000}$$
* **Unused States**: $2^n - n$ states ($16 - 4 = 12$ unused states in a 4-bit counter).
* **Advantage**: No decoding gates are required; the active state is directly read by inspecting which output is high.

#### B. Johnson Counter (Twisted-Ring / Switch-Tail Counter)
In a Johnson counter, the inverted output of the final flip-flop is fed back to the data input of the first flip-flop:
$$D_A = \overline{Q}_D$$

```text
        +-------------------------------------------------------------+
        |                                                             |
        v                                                             |
     [ D  Q ] --------> [ D  Q ] --------> [ D  Q ] --------> [ D  Q ]|
       FF A               FF B               FF C               FF D  |
                                                              (\bar{Q})+
        ^                  ^                  ^                  ^
 Clock -+------------------+------------------+------------------+
```

* **States & Modulus**: An $n$-bit Johnson counter yields **$2n$ valid states** (Modulus $\text{MOD} = 2n$).
* **Initialization**: Does not require pre-loading a 1; it self-starts from the all-zero state (`0000`).
* **State Transition Table (4-Bit, MOD-8 Counter)**:

| Clock Pulse | $Q_A$ | $Q_B$ | $Q_C$ | $Q_D$ | Decoding Logic |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 0 | $\overline{Q}_A \cdot \overline{Q}_D$ |
| 1 | 1 | 0 | 0 | 0 | $Q_A \cdot \overline{Q}_B$ |
| 2 | 1 | 1 | 0 | 0 | $Q_B \cdot \overline{Q}_C$ |
| 3 | 1 | 1 | 1 | 0 | $Q_C \cdot \overline{Q}_D$ |
| 4 | 1 | 1 | 1 | 1 | $Q_A \cdot Q_D$ |
| 5 | 0 | 1 | 1 | 1 | $\overline{Q}_A \cdot Q_B$ |
| 6 | 0 | 0 | 1 | 1 | $\overline{Q}_B \cdot Q_C$ |
| 7 | 0 | 0 | 0 | 1 | $\overline{Q}_C \cdot Q_D$ |

* **Advantage**: Provides double the count states of a standard ring counter ($2n$ vs $n$) using the same number of flip-flops. Each state is uniquely decoded using a single 2-input AND gate.

---

## Module 4: Counters

A **counter** is a sequential logic circuit that cycles through a prescribed sequence of binary states upon receiving clock pulses.

### 1. Comparison: Asynchronous vs Synchronous Counters

| Feature | Asynchronous (Ripple) Counter | Synchronous Counter |
| :--- | :--- | :--- |
| **Clock Application** | Clock is applied **only to the first flip-flop (LSB)**; subsequent stages are clocked by preceding stage outputs. | Clock pulses are applied **simultaneously to all flip-flops**. |
| **Propagation Delay** | Cumulative delay ($n \times t_{pd}$), which limits operating frequency. | Delay is independent of counter bit-width; equals one flip-flop delay plus gate delay. |
| **Glitches & Hazards** | Prone to decode spikes / glitches due to intermediate switching states. | Free from ripple-induced transient states. |
| **Hardware Complexity** | Minimal logic; only flip-flops and simple feedback gates. | Requires combinational steering logic at the flip-flop inputs. |
| **Speed** | Slow for large bit-widths. | High speed. |

---

### 2. Modulus of a Counter
* The **Modulus (MOD number)** represents the number of unique states the counter cycles through before recycling.
* For $n$ flip-flops:
  $$\text{Maximum Modulus } N = 2^n$$
* To design a counter of modulus $N$, the required number of flip-flops $n$ satisfies:
  $$2^{n-1} < N \le 2^n$$

---

### 3. Asynchronous (Ripple) Counters

In ripple counters, flip-flops are operated in **toggle mode** ($T = 1$ or $J = K = 1$).

#### Direction Rules for Ripple Counters

| Clock Trigger Active Edge | Triggering Signal Source | Counter Counting Direction |
| :--- | :--- | :--- |
| **Negative Edge ($\downarrow$)** | Normal output $Q$ connects to next clock | **UP Counter** |
| **Negative Edge ($\downarrow$)** | Inverted output $\overline{Q}$ connects to next clock | **DOWN Counter** |
| **Positive Edge ($\uparrow$)** | Normal output $Q$ connects to next clock | **DOWN Counter** |
| **Positive Edge ($\uparrow$)** | Inverted output $\overline{Q}$ connects to next clock | **UP Counter** |

---

#### 3-Bit Asynchronous UP Counter
* Counts from $0$ to $7$ (`000` to `111`).
* Uses 3 negative-edge triggered T flip-flops:
  * External clock connects to flip-flop A (LSB).
  * $Q_A$ connects to the clock input of flip-flop B.
  * $Q_B$ connects to the clock input of flip-flop C (MSB).
  * All $T$ inputs tied high ($T_A = T_B = T_C = 1$).

#### 3-Bit Asynchronous DOWN Counter (Filled In From Page 3)
* Sequence: $7 \to 6 \to 5 \to 4 \to 3 \to 2 \to 1 \to 0 \to 7$.
* Using negative-edge triggered T flip-flops:
  * Tie $T_A = T_B = T_C = 1$.
  * Connect external clock to flip-flop A (LSB).
  * Connect $\overline{Q}_A$ to the clock of flip-flop B.
  * Connect $\overline{Q}_B$ to the clock of flip-flop C.

```text
  1 (Vcc) ------------+-----------------+-----------------+
                      |                 |                 |
                   +--+---+          +--+---+          +--+---+
                   |T    Q|--Q_A     |T    Q|--Q_B     |T    Q|--Q_C (MSB)
  CLK (Neg-Edge) ->|>   _ |        ->|>   _ |        ->|>   _ |
                   |    Q |--CLK_B---|    Q |--CLK_C---|    Q |
                   +------+          +------+          +------+
                     FF A              FF B              FF C
```

| Pulse Count | $Q_C$ (MSB) | $Q_B$ | $Q_A$ (LSB) | Decimal Equivalent |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 1 | 1 | 1 | 7 |
| 1 | 1 | 1 | 0 | 6 |
| 2 | 1 | 0 | 1 | 5 |
| 3 | 1 | 0 | 0 | 4 |
| 4 | 0 | 1 | 1 | 3 |
| 5 | 0 | 1 | 0 | 2 |
| 6 | 0 | 0 | 1 | 1 |
| 7 | 0 | 0 | 0 | 0 |

---

### 4. Asynchronous Mod-N Counters with Reset Logic

To design a counter with modulus $N < 2^n$, combinational gates detect the binary count representing $N$ and immediately assert the active-low asynchronous clear ($\overline{\text{CLR}}$) inputs of all flip-flops.

#### A. Mod-6 Asynchronous UP Counter
* **Count Sequence**: $0, 1, 2, 3, 4, 5$ (`000` to `101`).
* **Reset State**: State 6 (`110`), where $Q_C = 1, Q_B = 1, Q_A = 0$.
* **Feedback Logic**:
  $$\overline{\text{CLR}} = \overline{Q_C \cdot Q_B}$$
* A 2-input NAND gate takes inputs $Q_C$ and $Q_B$ and feeds the active-low $\overline{\text{CLR}}$ pins.

#### B. Mod-10 Asynchronous (BCD / Decade) Counter
* **Count Sequence**: $0$ to $9$ (`0000` to `1001`).
* **Required Flip-Flops**: 4 ($2^3 < 10 \le 2^4$).
* **Reset State**: State 10 (`1010`), where $Q_D = 1, Q_C = 0, Q_B = 1, Q_A = 0$.
* **Feedback Logic**:
  $$\overline{\text{CLR}} = \overline{Q_D \cdot Q_B}$$

---

### 5. Synchronous Counter Design Procedure

Follow this systematic 5-step method for any synchronous counter:
1. **Determine Flip-Flop Count**: Find the smallest integer $n$ such that $2^n \ge N$.
2. **Choose Flip-Flop Type**: (T, D, or JK).
3. **Set Up State and Excitation Table**: List all Present States, their corresponding Next States, and the required flip-flop input values based on the flip-flop excitation table.
4. **K-Map Simplification**: Plot the required inputs on Karnaugh maps (assigning Don't Cares, $X$, to unused states) to obtain minimal Boolean equations.
5. **Circuit Realization**: Draw the logic schematic connecting gates to flip-flop inputs.

#### Flip-Flop Excitation Reference Table
$$T = Q_n \oplus Q_{n+1}, \quad D = Q_{n+1}$$

| $Q_n \to Q_{n+1}$ | Required $T$ | Required $D$ | Required $J$ | Required $K$ |
| :---: | :---: | :---: | :---: | :---: |
| $0 \to 0$ | 0 | 0 | 0 | $X$ |
| $0 \to 1$ | 1 | 1 | 1 | $X$ |
| $1 \to 0$ | 1 | 0 | $X$ | 1 |
| $1 \to 1$ | 0 | 1 | $X$ | 0 |

---

### 6. Solved Lecture Examples

#### Example 1: 3-Bit Synchronous UP Counter using T Flip-Flops
* **Sequence**: `000` $\to$ `001` $\to$ `010` $\to$ `011` $\to$ `100` $\to$ `101` $\to$ `110` $\to$ `111` $\to$ `000`.

##### Excitation Table

| Present State ($Q_C Q_B Q_A$) | Next State ($Q_{C+1} Q_{B+1} Q_{A+1}$) | Inputs ($T_C, T_B, T_A$) |
| :---: | :---: | :---: |
| 0 0 0 | 0 0 1 | 0 0 1 |
| 0 0 1 | 0 1 0 | 0 1 1 |
| 0 1 0 | 0 1 1 | 0 0 1 |
| 0 1 1 | 1 0 0 | 1 1 1 |
| 1 0 0 | 1 0 1 | 0 0 1 |
| 1 0 1 | 1 1 0 | 0 1 1 |
| 1 1 0 | 1 1 1 | 0 0 1 |
| 1 1 1 | 0 0 0 | 1 1 1 |

##### Minimized Expressions
* **$T_A$**: All cells are $1 \implies T_A = 1$
* **$T_B$**: $1$s at minterms $(1, 3, 5, 7) \implies T_B = Q_A$
* **$T_C$**: $1$s at minterms $(3, 7) \implies T_C = Q_B \cdot Q_A$

---

#### Example 2: Mod-6 Synchronous Counter using D Flip-Flops
* **Sequence**: $0 \to 1 \to 2 \to 3 \to 4 \to 5 \to 0$ (`000` to `101`).
* **Unused States**: 6 (`110`), 7 (`111`) are treated as Don't Cares ($X$).
* **Excitation Property**: $D = Q_{n+1}$.

##### Excitation Table

| Present State ($Q_C Q_B Q_A$) | Next State ($Q_{C+1} Q_{B+1} Q_{A+1}$) | Inputs ($D_C = Q_{C+1}, D_B = Q_{B+1}, D_A = Q_{A+1}$) |
| :---: | :---: | :---: |
| 0 0 0 | 0 0 1 | 0 0 1 |
| 0 0 1 | 0 1 0 | 0 1 0 |
| 0 1 0 | 0 1 1 | 0 1 1 |
| 0 1 1 | 1 0 0 | 1 0 0 |
| 1 0 0 | 1 0 1 | 1 0 1 |
| 1 0 1 | 0 0 0 | 0 0 0 |
| 1 1 0 | X X X | X X X |
| 1 1 1 | X X X | X X X |

##### K-Map Minimization
* **$D_C$**:
  * Minterms: $m(3, 4)$; Don't cares: $d(6, 7)$
  * Group $(3, 7) \implies Q_B Q_A$; Group $(4, 6) \implies Q_C \overline{Q}_A$
  $$D_C = Q_C \overline{Q}_A + Q_B Q_A$$

* **$D_B$**:
  * Minterms: $m(1, 2)$; Don't cares: $d(6, 7)$
  * Group $(1) \implies \overline{Q}_C \overline{Q}_B Q_A$; Group $(2, 6) \implies Q_B \overline{Q}_A$
  $$D_B = \overline{Q}_C \overline{Q}_B Q_A + Q_B \overline{Q}_A$$

* **$D_A$**:
  * Minterms: $m(0, 2, 4)$; Don't cares: $d(6, 7)$
  * Group quad $(0, 2, 4, 6) \implies \overline{Q}_A$
  $$D_A = \overline{Q}_A$$

---

#### Example 3: Synchronous Counter for Arbitrary Sequence
* **Specified Sequence**:
  $$\text{000} \to \text{110} \to \text{010} \to \text{011} \to \text{101} \to \text{000}$$
* **Unused States**: 1 (`001`), 4 (`100`), 7 (`111`) are treated as Don't Cares ($X$).
* **Flip-Flops**: 3 T Flip-Flops ($T = Q_n \oplus Q_{n+1}$).

##### Excitation Table

| Present State ($Q_C Q_B Q_A$) | Next State ($Q_{C+1} Q_{B+1} Q_{A+1}$) | Inputs ($T_C, T_B, T_A$) |
| :---: | :---: | :---: |
| **0 0 0** (0) | 1 1 0 | 1 1 0 |
| **0 0 1** (1) | X X X | X X X |
| **0 1 0** (2) | 0 1 1 | 0 0 1 |
| **0 1 1** (3) | 1 0 1 | 1 1 0 |
| **1 0 0** (4) | X X X | X X X |
| **1 0 1** (5) | 0 0 0 | 1 0 1 |
| **1 1 0** (6) | 0 1 0 | 1 0 0 |
| **1 1 1** (7) | X X X | X X X |

##### K-Map Minimization
* **$T_C$**:
  * 1s at $m(0, 3, 5, 6)$; Don't cares at $d(1, 4, 7)$
  * Only cell 2 is 0 $\implies$ Minimal SOP:
    $$T_C = Q_C + Q_A + \overline{Q}_B$$

* **$T_B$**:
  * 1s at $m(0, 3)$; Don't cares at $d(1, 4, 7)$
  * Group $(0, 1) \implies \overline{Q}_C \overline{Q}_B$; Group $(1, 3) \implies \overline{Q}_C Q_A$
    $$T_B = \overline{Q}_C \overline{Q}_B + \overline{Q}_C Q_A = \overline{Q}_C (\overline{Q}_B + Q_A)$$

* **$T_A$**:
  * 1s at $m(2, 5)$; Don't cares at $d(1, 4, 7)$
  * Group cell 5 with cell 1 ($X$) $\implies \overline{Q}_B Q_A$; cell 2 is $\overline{Q}_C Q_B \overline{Q}_A$
    $$T_A = \overline{Q}_B Q_A + \overline{Q}_C Q_B \overline{Q}_A$$

---

### 7. Solutions to Homework Problems

#### Homework 1: Mod-10 Synchronous UP Counter using JK Flip-Flops
* **Sequence**: $0 \to 1 \to 2 \to 3 \to 4 \to 5 \to 6 \to 7 \to 8 \to 9 \to 0$.
* **Flip-Flops**: 4 ($Q_D$ MSB, $Q_A$ LSB).
* **Unused States**: $10, 11, 12, 13, 14, 15$ are Don't Cares ($d(10\dots15)$).

##### Excitation Table

| Present State ($Q_D Q_C Q_B Q_A$) | Next State ($Q_D Q_C Q_B Q_A$) | $J_D$ | $K_D$ | $J_C$ | $K_C$ | $J_B$ | $K_B$ | $J_A$ | $K_A$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0000** | **0001** | 0 | X | 0 | X | 0 | X | 1 | X |
| **0001** | **0010** | 0 | X | 0 | X | 1 | X | X | 1 |
| **0010** | **0011** | 0 | X | 0 | X | X | 0 | 1 | X |
| **0011** | **0100** | 0 | X | 1 | X | X | 1 | X | 1 |
| **0100** | **0101** | 0 | X | X | 0 | 0 | X | 1 | X |
| **0101** | **0110** | 0 | X | X | 0 | 1 | X | X | 1 |
| **0110** | **0111** | 0 | X | X | 0 | X | 0 | 1 | X |
| **0111** | **1000** | 1 | X | X | 1 | X | 1 | X | 1 |
| **1000** | **1001** | X | 0 | 0 | X | 0 | X | 1 | X |
| **1001** | **0000** | X | 1 | 0 | X | 0 | X | X | 1 |

##### Final Minimal Logic Equations
$$\begin{aligned}
J_A &= 1, & K_A &= 1 \\
J_B &= \overline{Q}_D \cdot Q_A, & K_B &= Q_A \\
J_C &= Q_B \cdot Q_A, & K_C &= Q_B \cdot Q_A \\
J_D &= Q_C \cdot Q_B \cdot Q_A, & K_D &= Q_A
\end{aligned}$$

---

#### Homework 2: 3-Bit Synchronous Gray Code Counter using T Flip-Flops
* **Sequence**: `000` $\to$ `001` $\to$ `011` $\to$ `010` $\to$ `110` $\to$ `111` $\to$ `101` $\to$ `100` $\to$ `000`.
* All 8 combinations are valid ($	ext{MOD} = 8$, no unused states).

##### Excitation Table

| State Name | Present State ($Q_C Q_B Q_A$) | Next State ($Q_C Q_B Q_A$) | $T_C$ | $T_B$ | $T_A$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $S_0$ | 0 0 0 | 0 0 1 | 0 | 0 | 1 |
| $S_1$ | 0 0 1 | 0 1 1 | 0 | 1 | 0 |
| $S_2$ | 0 1 1 | 0 1 0 | 0 | 0 | 1 |
| $S_3$ | 0 1 0 | 1 1 0 | 1 | 0 | 0 |
| $S_4$ | 1 1 0 | 1 1 1 | 0 | 0 | 1 |
| $S_5$ | 1 1 1 | 1 0 1 | 0 | 1 | 0 |
| $S_6$ | 1 0 1 | 1 0 0 | 0 | 0 | 1 |
| $S_7$ | 1 0 0 | 0 0 0 | 1 | 0 | 0 |

##### Final Minimal Logic Equations
$$\begin{aligned}
T_A &= Q_C \odot (Q_B \oplus Q_A) \\
T_B &= \overline{Q_C \oplus Q_B} \cdot Q_A \\
T_C &= (Q_C \oplus Q_B) \cdot \overline{Q}_A
\end{aligned}$$
