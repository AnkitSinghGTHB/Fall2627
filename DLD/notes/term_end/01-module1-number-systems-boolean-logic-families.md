# 📘 Unit 1: Number Systems, Boolean Algebra & Logic Families

---

## 1. Number Systems & Signed Arithmetic

### 1.1 Number Base Conversions
* **Base-$r$ Positional Representation**:
  $$(N)_r = d_{n-1} r^{n-1} + \dots + d_0 r^0 + d_{-1} r^{-1} + \dots + d_{-m} r^{-m}$$
* **Rapid Binary $\leftrightarrow$ Octal / Hexadecimal**:
  - Octal: Group binary bits into sets of **3 bits** starting from the binary point.
  - Hexadecimal: Group binary bits into sets of **4 bits** starting from the binary point.

### 1.2 Signed Binary Representation & 2's Complement
* **Sign-Magnitude**: MSB is sign bit ($0 = +, 1 = -$); remaining $(n-1)$ bits represent magnitude. Problem: Dual representations of zero ($+0$ and $-0$).
* **1's Complement**: Invert all bits. Dual zero problem persists.
* **2's Complement**: Invert all bits and add $1$ ($\text{2's Comp} = \text{1's Comp} + 1$).
  - Range for $n$ bits: $-2^{n-1} \text{ to } +2^{n-1}-1$. Unique zero representation!
* **2's Complement Subtraction ($A - B$)**:
  - Compute $A + (\text{2's complement of } B)$.
  - If a carry out of the MSB occurs: Discard carry; result is positive.
  - If no carry occurs: Result is negative and in 2's complement form; take 2's complement of result to find magnitude.
* **Overflow Detection**:
  $$\text{Overflow } V = C_{n-1} \oplus C_n$$
  (Occurs when adding two numbers of like sign produces a result of opposite sign).

---

## 2. Boolean Algebra Laws & Theorems

### 2.1 Fundamental Theorems
* **Duality Principle**: Any true Boolean identity remains true if AND $(\cdot)$ and OR $(+)$ are interchanged, and $0$ and $1$ are interchanged.
* **De Morgan's Laws**:
  $$\overline{A + B} = \overline{A} \cdot \overline{B}, \quad \overline{A \cdot B} = \overline{A} + \overline{B}$$
* **Consensus Theorem**:
  $$A B + \overline{A} C + B C = A B + \overline{A} C$$
  $$(A + B)(\overline{A} + C)(B + C) = (A + B)(\overline{A} + C)$$
  *(The term $B C$ is redundant consensus).*
* **Absorption Laws**:
  $$A + A B = A, \quad A(A + B) = A, \quad A + \overline{A} B = A + B$$

### 2.2 Canonical Forms: Minterms and Maxterms
* **Minterm ($m$)**: Product of all literals (ANDed). A variable appears uncomplemented if $1$, complemented if $0$.
* **Maxterm ($M$)**: Sum of all literals (ORed). A variable appears uncomplemented if $0$, complemented if $1$.
* **Relationship**:
  $$m_i = \overline{M_i}$$
  $$f(A, B, C) = \sum m(1, 4, 6, 7) \iff f(A, B, C) = \prod M(0, 2, 3, 5)$$

---

## 3. Universal Gates (NAND & NOR Implementation)

Both **NAND** and **NOR** are universal gates capable of implementing any Boolean function without other gate types.

| Required Gate | NAND-Only Implementation | NOR-Only Implementation |
|:---|:---|:---|
| **NOT ($A'$)** | $\overline{A \cdot A}$ (Tie inputs together) | $\overline{A + A}$ (Tie inputs together) |
| **AND ($AB$)** | $\overline{\overline{AB} \cdot \overline{AB}}$ (NAND followed by NAND-inverter) | $\overline{\overline{A} + \overline{B}}$ (Invert inputs with NOR, then NOR them) |
| **OR ($A+B$)** | $\overline{\overline{A} \cdot \overline{B}}$ (Invert inputs with NAND, then NAND them) | $\overline{\overline{A+B} + \overline{A+B}}$ (NOR followed by NOR-inverter) |
| **XOR ($A \oplus B$)** | **4 NAND gates** | **5 NOR gates** |
| **XNOR ($A \odot B$)** | **5 NAND gates** | **4 NOR gates** |

---

## 4. Digital Logic Families Comparative Matrix

| Parameter | RTL (Resistor-Transistor) | TTL (Transistor-Transistor) | ECL (Emitter-Coupled) | CMOS (Complementary MOS) |
|:---|:---|:---|:---|:---|
| **Basic Gate** | NOR | NAND | OR / NOR (Dual output) | NAND / NOR |
| **Operating Speed** | Slow | Moderate | **Fastest (Sub-nanosecond)** | Moderate to Fast |
| **Propagation Delay** | $\sim 12\text{ ns}$ | $\sim 10\text{ ns}$ (Standard) / $3\text{ ns}$ (Schottky) | **$1–2\text{ ns}$** | $\sim 10–20\text{ ns}$ |
| **Power Dissipation** | $12\text{ mW}$ | $10\text{ mW}$ | **Highest ($25–50\text{ mW}$)** | **Lowest (Virtually zero static: $\sim \mu\text{W}$)** |
| **Noise Margin** | Poor ($0.2\text{ V}$) | Good ($0.4\text{ V}$) | Lowest ($0.2\text{–}0.25\text{ V}$) | **Highest ($0.45 \times V_{DD}$, $\sim 1.5\text{–}2.5\text{ V}$)** |
| **Fan-Out** | Low ($4–5$) | Moderate ($10$) | High ($25$) | **Highest ($> 50$)** |
| **Figure of Merit (PDP)** | Poor | Moderate ($\sim 100\text{ pJ}$) | High energy | **Best ($\sim 0.1–1\text{ pJ}$)** |

> 🔑 **Exam Key**: **ECL** is the fastest because its transistors operate in the non-saturated active mode (eliminating charge storage delays). **CMOS** is the global standard in VLSI because static power dissipation is negligible.

---

## 5. Model Exam Questions & Answers

### Question 1 (12 Marks)
**(a) Perform subtraction $(28)_{10} - (45)_{10}$ using 8-bit 2's complement representation. Detect if overflow occurred.**  
**(b) Simplify using Boolean algebra: $F = A B + A(B+C) + B(B+C)$. Implement the simplified function using NAND gates only.**

**Solution**:
1. **Part (a)**:
   - Convert magnitudes to 8-bit binary:
     - $+28 = 00011100_2$
     - $+45 = 00101101_2$
   - 2's complement of $+45$:
     - 1's comp = $11010010_2$
     - 2's comp = $11010010 + 1 = 11010011_2$
   - Perform addition:
     $$\begin{array}{r@{\quad}l}
       00011100 & (+28) \\
     + 11010011 & (-45) \\
     \hline
       11101111 & \text{Result}
     \end{array}$$
   - No carry out generated ($C_8 = 0$). Result is negative and stored in 2's complement form.
   - Magnitude: Take 2's complement of $11101111 \implies 00010000 + 1 = 00010001_2 = (17)_{10}$.  
     $\therefore \text{Result} = -17_{10}$ (Correct, since $28 - 45 = -17$).
   - Overflow Check: $C_7 = 0$, $C_8 = 0 \implies V = C_7 \oplus C_8 = 0 \oplus 0 = \mathbf{0}$ (No overflow).
2. **Part (b)**:
   - Expand expression:
     $$F = A B + A B + A C + B B + B C$$
     $$F = A B + A C + B + B C \quad (\because A B + A B = A B, B B = B)$$
     $$F = B(1 + A + C) + A C = B(1) + A C = B + A C$$
   - NAND-only Implementation:
     $$\overline{\overline{B + AC}} = \overline{\overline{B} \cdot \overline{AC}}$$
     Need: 1 NAND for $\overline{AC}$, 1 NAND for $\overline{B}$, and 1 NAND to combine them $\implies$ **3 NAND gates total**.
