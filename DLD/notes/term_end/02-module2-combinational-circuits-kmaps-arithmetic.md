# 📘 Unit 2: Combinational Logic Circuits, K-Maps & Arithmetic Units

---

## 1. Karnaugh Map (K-Map) Minimization

### 1.1 K-Map Rules & Gray Coding
* Adjacent cells differ by **exactly one bit** (Gray code ordering: `00, 01, 11, 10`).
* Group sizes must be powers of 2 ($1, 2, 4, 8, 16$).
* Wrap-around grouping allowed (corners and outer edges).
* **Prime Implicant (PI)**: A maximal group of minterms that cannot be combined with another group.
* **Essential Prime Implicant (EPI)**: A prime implicant covering at least one minterm that is not covered by any other prime implicant.

### 1.2 5-Variable K-Map Structure ($A, B, C, D, E$)
Split into two 4-variable ($B, C, D, E$) sub-maps side by side:
* **Map 1 ($A = 0$)**: Minterms $0$ to $15$.
* **Map 2 ($A = 1$)**: Minterms $16$ to $31$.
* Superposition rule: Cells at identical row/column positions in both sub-maps are physically adjacent and can be grouped together.

---

## 2. Arithmetic Combinational Circuits

### 2.1 Full Adder & Full Subtractor Equations

```
+--------------------------------------------------------------------------------+
| FULL ADDER                                  | FULL SUBTRACTOR                  |
+---------------------------------------------+----------------------------------+
| Inputs: A, B, Cin                           | Inputs: A, B, Bin                |
| Outputs:                                    | Outputs:                         |
|   Sum   S = A ⊕ B ⊕ Cin                     |   Diff   D = A ⊕ B ⊕ Bin         |
|   Carry Cout = AB + BCin + ACin             |   Borrow Bout = A'B + B Bin +    |
|              = AB + Cin(A ⊕ B)              |                 A' Bin           |
+---------------------------------------------+----------------------------------+
```

### 2.2 Carry Look-Ahead Adder (CLA)
* Eliminates the ripple carry propagation delay:
  * **Carry Generate**: $G_i = A_i \cdot B_i$ (generates carry regardless of input carry).
  * **Carry Propagate**: $P_i = A_i \oplus B_i$ (propagates input carry to output).
* Closed-form carry equations:
  $$C_1 = G_0 + P_0 C_0$$
  $$C_2 = G_1 + P_1 G_0 + P_1 P_0 C_0$$
  $$C_3 = G_2 + P_2 G_1 + P_2 P_1 G_0 + P_2 P_1 P_0 C_0$$
  $$C_4 = G_3 + P_3 G_2 + P_3 P_2 G_1 + P_3 P_2 P_1 G_0 + P_3 P_2 P_1 P_0 C_0$$
* All carries generated simultaneously in **$2$ gate levels of delay**, independent of bit width $n$.

### 2.3 BCD Adder Architecture
* Adds two BCD digits ($0$ to $9$). When preliminary 4-bit binary sum exceeds $9$ (i.e., sum is $10$ to $19$), binary representation is invalid in BCD.
* **Correction Logic**: Add $(0110)_2 = (6)_{10}$ to preliminary sum when:
  $$\text{Correction Carry } C = K + S_3 S_2 + S_3 S_1$$
  *(where $K$ is carry-out of the 4-bit binary adder, and $S_3, S_2, S_1$ are binary sum bits).*

---

## 3. Non-Arithmetic Combinational Logic Units

### 3.1 Multiplexers (Data Selectors)
* $2^n \times 1$ MUX: $2^n$ data inputs, $n$ selection lines, $1$ output line.
* Output equation for 4:1 MUX:
  $$Y = S_1' S_0' I_0 + S_1' S_0 I_1 + S_1 S_0' I_2 + S_1 S_0 I_3$$
* **Function Implementation Strategy**:
  - To implement an $n$-variable Boolean function with a $2^{n-1} \times 1$ MUX: Connect $(n-1)$ variables to select lines; connect the remaining variable ($0, 1, V, V'$) to data inputs.

### 3.2 Decoders & Encoders
* **Decoder ($n \times 2^n$)**: Converts binary code into $2^n$ distinct output lines (each representing a minterm).
* **Priority Encoder**: If multiple inputs are simultaneously active, the output reflects the input with the highest numeric priority. Also generates a **Valid bit ($V$)** indicating if any input is asserted.

### 3.3 Code Converters (Formulas to Memorize)
* **Binary to Gray Code**:
  $$G_3 = B_3$$
  $$G_2 = B_3 \oplus B_2$$
  $$G_1 = B_2 \oplus B_1$$
  $$G_0 = B_1 \oplus B_0$$
* **Gray to Binary Code**:
  $$B_3 = G_3$$
  $$B_2 = B_3 \oplus G_2$$
  $$B_1 = B_2 \oplus G_1$$
  $$B_0 = B_1 \oplus G_0$$

---

## 4. Model Exam Questions & Answers

### Question 1 (12 Marks)
**Design a BCD Adder circuit using two 4-bit binary parallel adders and NAND/AND logic gates. Derive the correction logic equation and explain its working.**

**Solution**:
1. **Problem Statement**: BCD digits range from $0000_2$ to $1001_2$. The maximum sum of two BCD digits plus carry is $9 + 9 + 1 = 19$. Binary sum produces $0000$ to $10011$.
2. **Identification of Invalid Codes ($10$ to $15$)**:
   - For sums $0000$ to $1001$ (0 to 9) with $K = 0$: Valid BCD. No correction needed.
   - For sums $1010$ to $1111$ (10 to 15) with $K = 0$: $S_3$ is high AND either $S_2 = 1$ or $S_1 = 1$.  
     Condition: $S_3 S_2 + S_3 S_1$.
   - For sums $16$ to $19$: Binary carry out $K = 1$.
3. **Correction Boolean Equation**:
   $$C = K + S_3 S_2 + S_3 S_1$$
4. **Circuit Design**:
   - First 4-bit Binary Adder adds $A_3 A_2 A_1 A_0$ and $B_3 B_2 B_1 B_0$ with carry-in $C_{in}$, producing sum $S_3 S_2 S_1 S_0$ and carry $K$.
   - Output $K, S_3, S_2, S_1$ fed into logic circuit generating correction signal $C$.
   - Second 4-bit Binary Adder adds preliminary sum $S_3 S_2 S_1 S_0$ with $0 C C 0$ (which is $0110_2$ if $C = 1$, or $0000_2$ if $C = 0$).
   - Output of second adder provides the final corrected BCD sum bits and BCD carry-out $C$.

### Question 2 (8 Marks)
**Implement the Boolean function $F(A, B, C, D) = \sum m(1, 3, 4, 11, 12, 13, 14, 15)$ using an 8:1 Multiplexer.**

**Solution**:
1. Choose $A, B, C$ as select inputs ($S_2 = A, S_1 = B, S_0 = C$). Let $D$ be data input.
2. Construct Implementation Table (Columns $I_0$ to $I_7$, Rows $D' (0)$ and $D (1)$):

| Select ($ABC$) | Minterm with $D=0$ | Minterm with $D=1$ | Input Expression |
|:---:|:---:|:---:|:---:|
| **$I_0$ ($000$)** | $m_0$ | **$m_1$** (circled) | **$D$** |
| **$I_1$ ($001$)** | $m_2$ | **$m_3$** (circled) | **$D$** |
| **$I_2$ ($010$)** | **$m_4$** (circled) | $m_5$ | **$D'$** |
| **$I_3$ ($011$)** | $m_6$ | $m_7$ | **$0$** |
| **$I_4$ ($100$)** | $m_8$ | $m_9$ | **$0$** |
| **$I_5$ ($101$)** | $m_{10}$ | **$m_{11}$** (circled) | **$D$** |
| **$I_6$ ($110$)** | **$m_{12}$** (circled) | **$m_{13}$** (circled) | **$1$** |
| **$I_7$ ($111$)** | **$m_{14}$** (circled) | **$m_{15}$** (circled) | **$1$** |

3. Connect $I_0 = D, I_1 = D, I_2 = D', I_3 = 0, I_4 = 0, I_5 = D, I_6 = 1, I_7 = 1$ to the 8:1 MUX data pins.
