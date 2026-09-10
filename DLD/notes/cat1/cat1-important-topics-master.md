# 🚀 DLD CAT-1 Handwritten Important Topics Master Guide

> **Transcribed & Fully Solved from your Handwritten Exam Topics Note!**  
> Exam Date: Today/Tomorrow (Aug 13, 2:30 PM). Print or review this document line-by-line!

---

## 📌 Index of 6 Core Exam Topics

1. [i) Number System Conversions & Subtraction](#topic-1)
2. [ii) Subtraction using Complements (9's & 10's, 1's & 2's)](#topic-2)
3. [iii) Canonical & Minimal SOP & POS](#topic-3)
4. [iv) K-Map Minimization with Don't Care Conditions](#topic-4)
5. [v) Half Subtractor & Full Subtractor (Complete Design)](#topic-5)
6. [vi) $3 \times 8$ Decoder, $4 \times 16$ Cascading & Full Adder Implementation](#topic-6)

---

<a id="topic-1"></a>
## 1️⃣ Topic i: Number System Conversions

### 💡 Quick Conversion Rules:

| From $\to$ To | Method | Example |
|---|---|---|
| **Decimal $\to$ Base $b$** | Integer: Divide by $b$ (keep remainders bottom-up).<br>Fraction: Multiply by $b$ (keep integer parts top-down). | $25_{10} \to 25/2=12\,r1, 12/2=6\,r0, 6/2=3\,r0, 3/2=1\,r1, 1/2=0\,r1 \implies 11001_2$ |
| **Base $b \to$ Decimal** | Multiply each digit by positional power $b^k$ and sum. | $11001_2 = 1(16) + 1(8) + 0(4) + 0(2) + 1(1) = 25_{10}$ |
| **Binary $\leftrightarrow$ Octal (Base 8)** | Group bits in **sets of 3** from binary point. | $110\,101_2 \to 6\,5_8 = 65_8$ |
| **Binary $\leftrightarrow$ Hex (Base 16)** | Group bits in **sets of 4** from binary point. | $1101\,0110_2 \to D\,6_{16} = D6_{16}$ |

---

<a id="topic-2"></a>
## 2️⃣ Topic ii: Subtraction using Complements

### 🅰️ Binary Subtraction ($A - B$)

| Method | Steps for $A - B$ | If End Carry $= 1$ | If End Carry $= 0$ |
|---|---|---|---|
| **1's Complement** | Add $A$ + (1's comp of $B$) | Result is positive. **End-Around Carry** (add 1 to result). | Result is negative. Take 1's comp of result for magnitude. |
| **2's Complement** | Add $A$ + (2's comp of $B$) | Result is positive. **DISCARD the carry bit**. | Result is negative. Take 2's comp of result for magnitude. |

#### ✍️ Worked Example: Binary $101010_2 (42) - 010101_2 (21)$
- **Using 1's Complement:**
  $$101010 + 101010 = 1010100_2$$
  End Carry $= 1 \to$ End-around carry: $010100 + 1 = \mathbf{010101_2 = +21_{10}}$ ✅

- **Using 2's Complement:**
  $$101010 + 101011 = 1010101_2$$
  End Carry $= 1 \to$ Discard carry: $\mathbf{010101_2 = +21_{10}}$ ✅

---

### 🅱️ Decimal Subtraction ($M - N$)

| Method | Steps for $M - N$ | If End Carry $= 1$ | If End Carry $= 0$ |
|---|---|---|---|
| **9's Complement** | Add $M$ + (9's comp of $N$) | Result is positive. **End-Around Carry** (add 1 to result). | Result is negative. Take 9's comp of result for magnitude. |
| **10's Complement** | Add $M$ + (10's comp of $N$) | Result is positive. **DISCARD the carry**. | Result is negative. Take 10's comp of result for magnitude. |

#### ✍️ Worked Example: Decimal $725 - 318$
- 9's comp of $318 = 999 - 318 = 681$.
  $$725 + 681 = 1406$$
  End carry $= 1 \to$ Add 1: $406 + 1 = \mathbf{407}$ ✅

- 10's comp of $318 = 681 + 1 = 682$.
  $$725 + 682 = 1407$$
  End carry $= 1 \to$ Discard 1: $\mathbf{407}$ ✅

---

<a id="topic-3"></a>
## 3️⃣ Topic iii: Canonical & Minimal SOP & POS

- **Canonical SOP ($\Sigma m$):** Sum of Minterms ($m_i$). Every variable appears in complemented ($0$) or uncomplemented ($1$) form.
- **Canonical POS ($\Pi M$):** Product of Maxterms ($M_i$). Every variable appears in complemented ($1$) or uncomplemented ($0$) form.

### Conversion Relation:
$$\text{If } F = \Sigma m(1, 3, 5, 7) \implies F = \Pi M(0, 2, 4, 6)$$

---

<a id="topic-4"></a>
## 4️⃣ Topic iv: K-Map Minimization with Don't Care Conditions

### Golden Rules for Don't Cares ($d$ / $X$):
1. $X$ can be treated as **1** if it helps make a group BIGGER (e.g. turning a pair of 2 into a quad of 4, or a quad of 4 into an octet of 8).
2. $X$ can be treated as **0** if it doesn't help enlarge any 1s group.
3. **NEVER** form a group that consists *only* of $X$'s!

#### ✍️ Worked Example: $F(A,B,C,D) = \Sigma m(1, 3, 7, 11, 15) + d(0, 2, 5, 8, 10)$
- Combine minterms $\{1, 3\}$ with don't cares $\{0, 2\} \implies$ **Quad $\{0, 1, 2, 3\} = A'B'$**
- Combine minterms $\{3, 7, 11, 15\} \implies$ **Quad $\{3, 7, 11, 15\} = CD$**
- **Minimal SOP Answer:** $\mathbf{F = A'B' + CD}$ ✅

---

<a id="topic-5"></a>
## 5️⃣ Topic v: Half Subtractor & Full Subtractor

### 🅰️ Half Subtractor (Subtracts 2 bits: $A - B$)

#### Truth Table:
| $A$ | $B$ | Difference ($D$) | Borrow ($B_{out}$) |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | **1** |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

#### Logic Expressions:
- **Difference:** $D = A \oplus B = A'B + AB'$
- **Borrow:** $B_{out} = A'B$

#### Circuit Diagram:
- $D = \text{XOR}(A, B)$
- $B_{out} = \text{AND}(\text{NOT}(A), B)$

---

### 🅱️ Full Subtractor (Subtracts 3 bits: $A - B - B_{in}$)

#### Truth Table:
| $A$ | $B$ | $B_{in}$ | Difference ($D$) | Borrow ($B_{out}$) |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | **1** |
| 0 | 1 | 0 | 1 | **1** |
| 0 | 1 | 1 | 0 | **1** |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | **1** |

#### Logic Expressions:
- **Difference:**
  $$\mathbf{D = A \oplus B \oplus B_{in}}$$
- **Borrow Out ($B_{out}$):**
  $$B_{out} = A'B + A'B_{in} + B B_{in} = \mathbf{A'B + (A \oplus B)' B_{in}}$$

#### Full Subtractor using 2 Half Subtractors + OR Gate:
1. **HS 1:** Inputs $A, B \to$ Outputs $D_1 = A \oplus B$, $B_1 = A'B$.
2. **HS 2:** Inputs $D_1, B_{in} \to$ Outputs $D = D_1 \oplus B_{in} = A \oplus B \oplus B_{in}$, $B_2 = D_1' B_{in} = (A \oplus B)' B_{in}$.
3. **OR Gate:** $B_{out} = B_1 + B_2 = A'B + (A \oplus B)' B_{in}$.

---

<a id="topic-6"></a>
## 6️⃣ Topic vi: $3 \times 8$ Decoder, $4 \times 16$ Cascading & Full Adder Implementation

### 🅰️ $3 \times 8$ Decoder Basics
- **Inputs:** $A_2, A_1, A_0$ (Select lines), Enable ($E$).
- **Outputs:** 8 output lines $Y_0, Y_1, Y_2, Y_3, Y_4, Y_5, Y_6, Y_7$.
- Output expression for active-high decoder:
  $$Y_i = m_i \quad \text{for } i \in \{0 \dots 7\}$$
  (e.g., $Y_0 = A_2' A_1' A_0'$, $Y_7 = A_2 A_1 A_0$).

---

### 🅱️ Construct $4 \times 16$ Decoder using Two $3 \times 8$ Decoders

#### Architecture:
- We have 4 inputs: $A_3, A_2, A_1, A_0$ (where $A_3$ is MSB).
- Connect lower 3 bits $A_2, A_1, A_0$ in parallel to the select inputs of **BOTH** $3 \times 8$ decoders.
- Use the MSB $A_3$ as the **Enable ($E$)** control line:
  - Connect $A_3$ to **Decoder 1** enable via a **NOT gate** ($E_1 = \overline{A_3}$).
  - Connect $A_3$ directly to **Decoder 2** enable ($E_2 = A_3$).

```
                      ┌────────────────────────┐
                      │    3x8 Decoder 1       │
   A3 ───[NOT]───────►│ Enable (E1)            ├──────► Y0 - Y7  (Minterms 0-7)
                      │ Inputs: A2, A1, A0     │
                      └────────────────────────┘
                      ┌────────────────────────┐
                      │    3x8 Decoder 2       │
   A3 ───────────────►│ Enable (E2)            ├──────► Y8 - Y15 (Minterms 8-15)
                      │ Inputs: A2, A1, A0     │
                      └────────────────────────┘
```

#### Operation:
- When $A_3 = 0$: Decoder 1 is ENABLED ($Y_0 \dots Y_7$ active), Decoder 2 is DISABLED.
- When $A_3 = 1$: Decoder 2 is ENABLED ($Y_8 \dots Y_{15}$ active), Decoder 1 is DISABLED.

---

### ℂ Implementation of Full Adder using $3 \times 8$ Decoder

#### Full Adder Minterm Equations:
For inputs $A, B, C_{in}$:
- **Sum ($S$):** $\Sigma m(1, 2, 4, 7)$
- **Carry Out ($C_{out}$):** $\Sigma m(3, 5, 6, 7)$

#### Implementation Steps:
1. Connect inputs $A, B, C_{in}$ to the select lines $A_2, A_1, A_0$ of a $3 \times 8$ decoder (Enable $E = 1$).
2. Connect decoder outputs $Y_1, Y_2, Y_4, Y_7$ to a **4-input OR gate** to produce **Sum ($S$)**:
   $$S = Y_1 + Y_2 + Y_4 + Y_7$$
3. Connect decoder outputs $Y_3, Y_5, Y_6, Y_7$ to a **4-input OR gate** to produce **Carry Out ($C_{out}$)**:
   $$C_{out} = Y_3 + Y_5 + Y_6 + Y_7$$

```
                   ┌────────────────────────┐
   A ─────────────►│ A2                     │
   B ─────────────►│ A1   3x8 Decoder       ├─ Y1,Y2,Y4,Y7 ───► [ OR Gate ] ───► Sum (S)
  Cin ────────────►│ A0                     │
   E = 1 ─────────►│ Enable                 ├─ Y3,Y5,Y6,Y7 ───► [ OR Gate ] ───► Carry (Cout)
                   └────────────────────────┘
```
