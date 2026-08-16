# ⚡ DLD CAT-1 Faculty Assignment Solutions (100% Solved!)

> **Official Solutions for ALL 13 Assignment Problems specified by your Faculty for CAT-1!**  
> Exam Date: Tomorrow (Aug 13, 2:30 PM). Print or review this document line-by-line!

---

## 📌 Table of Contents
1. [Base $b$ Quadratic Equation Problem](#prob-1)
2. [Base $b$ Conversion Equation $(144)_b = 49$](#prob-2)
3. [Fixed-Point Arithmetic (1's & 2's Complement)](#prob-3)
4. [Decimal Arithmetic (9's & 10's Complement)](#prob-4)
5. [Boolean Simplification $(A+B+C)(A+B+C')\dots$](#prob-5)
6. [Canonical SOP/POS & Equivalence Verification](#prob-6)
7. [POS to SOP Conversion & Simplification](#prob-7)
8. [Minimal SOP K-Map (11 Minterms)](#prob-8)
9. [Minimal POS K-Map (8 Maxterms)](#prob-9)
10. [Essential Prime Implicants (EPI) Identification](#prob-10)
11. [K-Map with Don't Cares (Problem 1)](#prob-11)
12. [K-Map with Don't Cares (Problem 2)](#prob-12)
13. [Full Circuit Synthesis & NOR-Only Realization](#prob-13)

---

<a id="prob-1"></a>
## 1️⃣ Base $b$ Quadratic Equation Problem

### ❓ Question:
> **The roots of the equation $x^2 - 11x + 22 = 0$ in some base $b$ are $4$ and $5$. Evaluate $b$.**

### ✍️ Solution:
In a base-$b$ positional number system, an equation $x^2 - (11)_b x + (22)_b = 0$ has roots $x_1 = 4$ and $x_2 = 5$.

By Vieta's formulas for quadratic equations:
1. **Sum of roots:**
   $$x_1 + x_2 = (11)_b$$
   $$4 + 5 = 1 \cdot b^1 + 1 \cdot b^0$$
   $$9 = b + 1 \implies b = 8$$

2. **Product of roots:**
   $$x_1 \cdot x_2 = (22)_b$$
   $$4 \times 5 = 2 \cdot b^1 + 2 \cdot b^0$$
   $$20 = 2b + 2 \implies 2b = 18 \implies b = 9$$

> 💡 **Exam Explanation Note:**
> - If $(11)_b$ represents the sum $4+5=9_{10}$, then $(11)_8 = 1(8)+1 = 9_{10} \implies \mathbf{b=8}$.
> - If $(22)_b$ represents the product $4 \times 5 = 20_{10}$, then $(22)_9 = 2(9)+2 = 20_{10} \implies \mathbf{b=9}$.
> - If the constant term was $(24)_b$, then $2b+4 = 20 \implies b=8$ consistently for both sum and product!
> - **Answer to write in exam:** State $b=8$ (from sum of roots equation $b+1=9$) and $b=9$ (from product of roots equation $2b+2=20$).

---

<a id="prob-2"></a>
## 2️⃣ Base $b$ Conversion Equation

### ❓ Question:
> **$(144)_b = 49$, find $b$.**

### ✍️ Solution:
Convert $(144)_b$ to decimal (base 10):
$$(144)_b = 1 \cdot b^2 + 4 \cdot b^1 + 4 \cdot b^0 = b^2 + 4b + 4$$

Set equal to 49:
$$b^2 + 4b + 4 = 49$$
$$(b + 2)^2 = 49$$
$$b + 2 = \sqrt{49} = 7$$
$$b = 7 - 2 = \mathbf{5}$$

**Verification:**
In base 5: $(144)_5 = 1(5^2) + 4(5^1) + 4(5^0) = 25 + 20 + 4 = 49_{10}$. ✅

---

<a id="prob-3"></a>
## 3️⃣ Fixed-Point Arithmetic (1's & 2's Complement)

### ❓ Question:
> **Solve $-45.625 + 16.75$ using fixed-point representation with 8 bits for the integer part and a minimum of 4 bits for the fractional part, applying both 1's complement and 2's complement arithmetic.**

### ✍️ Solution:

#### Step 1: Binary Conversion (8 Integer bits, 4 Fraction bits)
- **$+45.625_{10}$:**
  - Integer $45_{10} = 00101101_2$
  - Fraction $0.625_{10} = 0.1010_2$ ($0.625 \times 2 = 1.25 \to 1; 0.25 \times 2 = 0.5 \to 0; 0.5 \times 2 = 1.0 \to 1$)
  - $+45.625 = \mathbf{00101101.1010_2}$

- **$+16.75_{10}$:**
  - Integer $16_{10} = 00010000_2$
  - Fraction $0.75_{10} = 0.1100_2$
  - $+16.75 = \mathbf{00010000.1100_2}$

- **Complement Representations for $-45.625$:**
  - 1's Complement of $-45.625 = \mathbf{11010010.0101_2}$
  - 2's Complement of $-45.625 = 11010010.0101 + 0.0001 = \mathbf{11010010.0110_2}$

---

#### Part A: Using 1's Complement Arithmetic

$$\begin{array}{r@{\quad}l}
  11010010.0101 & (-45.625 \text{ in 1's comp}) \\
+ 00010000.1100 & (+16.75) \\
\hline
  11100010.0001 & (\text{Sum})
\end{array}$$

- **Sign bit = 1** (Negative result).
- Take 1's complement to find magnitude: $\text{1's comp}(11100010.0001) = 00011101.1110_2$.
- Magnitude $= 16 + 8 + 4 + 1 + 0.5 + 0.25 + 0.125 = \mathbf{28.875_{10}}$.
- **Final Result:** $\mathbf{-28.875_{10}}$ ✅

---

#### Part B: Using 2's Complement Arithmetic

$$\begin{array}{r@{\quad}l}
  11010010.0110 & (-45.625 \text{ in 2's comp}) \\
+ 00010000.1100 & (+16.75) \\
\hline
  11100010.0010 & (\text{Sum})
\end{array}$$

- **Sign bit = 1** (Negative result).
- Take 2's complement to find magnitude: $\text{2's comp}(11100010.0010) = 00011101.1101 + 0.0001 = 00011101.1110_2 = \mathbf{28.875_{10}}$.
- **Final Result:** $\mathbf{-28.875_{10}}$ ✅

---

<a id="prob-4"></a>
## 4️⃣ Decimal Arithmetic (9's & 10's Complement)

### ❓ Question:
> **Add $-45.625 - 16.75$ using 9's and 10's complement arithmetic.**

### ✍️ Solution:
We express numbers in 5-digit decimal format: $XX.XXX$.
$+45.625$ and $+16.750$.

#### Part A: Using 9's Complement Arithmetic
- 9's comp of $45.625 = 99.999 - 45.625 = \mathbf{54.374}$
- 9's comp of $16.750 = 99.999 - 16.750 = \mathbf{83.249}$

Add the two 9's complements:
$$\begin{array}{r@{\quad}l}
  54.374 \\
+ 83.249 \\
\hline
 137.623
\end{array}$$

- Carry of 1 generated $\to$ Perform **End-Around Carry**:
  $$37.623 + 0.001 = \mathbf{37.624}$$
- Result is negative (in 9's comp). Magnitude $= 99.999 - 37.624 = \mathbf{62.375_{10}}$.
- **Final Answer:** $\mathbf{-62.375_{10}}$ ✅

---

#### Part B: Using 10's Complement Arithmetic
- 10's comp of $45.625 = 54.374 + 0.001 = \mathbf{54.375}$
- 10's comp of $16.750 = 83.249 + 0.001 = \mathbf{83.250}$

Add the two 10's complements:
$$\begin{array}{r@{\quad}l}
  54.375 \\
+ 83.250 \\
\hline
 137.625
\end{array}$$

- **Discard the end carry of 1** $\to$ Result $= \mathbf{37.625}$ (in 10's comp).
- Magnitude $= 100.000 - 37.625 = \mathbf{62.375_{10}}$.
- **Final Answer:** $\mathbf{-62.375_{10}}$ ✅

---

<a id="prob-5"></a>
## 5️⃣ Boolean Expression Simplification

### ❓ Question:
> **Simplify the Boolean expression $F(A, B, C, D) = (A + B + C)(A + B + C')(A + B' + C)(A' + B + C)$**

### ✍️ Solution:
Using Boolean algebra distributive law $(X + Y)(X + Y') = X$:

1. Combine term 1 and term 2:
   $$(A + B + C)(A + B + C') = (A + B)$$

2. Combine term 1 and term 3:
   $$(A + B + C)(A + B' + C) = (A + C)$$

3. Combine term 1 and term 4:
   $$(A + B + C)(A' + B + C) = (B + C)$$

Multiply the simplified factors:
$$F = (A + B)(A + C)(B + C)$$

**Convert to SOP Form:**
$$(A + B)(A + C) = A + BC$$
$$F = (A + BC)(B + C) = AB + AC + BC + BCC$$
$$\mathbf{F = AB + AC + BC}$$ ✅

---

<a id="prob-6"></a>
## 6️⃣ Canonical SOP/POS & Equivalence Verification

### ❓ Question:
> **Convert $F(A,B,C,D) = A'B + BC'D + AD'$ into canonical SOP and canonical POS forms and verify both are equivalent.**

### ✍️ Solution:

#### Step 1: Canonical SOP Form ($\Sigma m$)
Expand each term into minterms by inserting missing variables:
- $A'B = A'B(C+C')(D+D') = A'BCD + A'BCD' + A'BC'D + A'BC'D' = m_7 + m_6 + m_5 + m_4$
- $BC'D = BC'D(A+A') = ABC'D + A'BC'D = m_{13} + m_5$
- $AD' = AD'(B+B')(C+C') = ABCD' + ABC'D' + AB'CD' + AB'C'D' = m_{14} + m_{12} + m_{10} + m_8$

**Canonical SOP ($\Sigma m$):**
$$\mathbf{F(A,B,C,D) = \Sigma m(4, 5, 6, 7, 8, 10, 12, 13, 14)}$$

#### Step 2: Canonical POS Form ($\Pi M$)
The maxterms are the remaining numbers from $\{0..15\}$ not in $\Sigma m$:
$$\mathbf{F(A,B,C,D) = \Pi M(0, 1, 2, 3, 9, 11, 15)}$$

#### Step 3: Verification of Equivalence
- Both forms represent the exact same truth table (Output $= 1$ for minterms $\{4,5,6,7,8,10,12,13,14\}$ and Output $= 0$ for maxterms $\{0,1,2,3,9,11,15\}$).
- Minimizing SOP gives: $\mathbf{F = A'B + BC' + AD'}$.
- Minimizing POS gives: $(A+B)(B+D')(A'+C'+D') = A'B + BC' + AD'$.
Hence, both forms are **100% Equivalent**! ✅

---

<a id="prob-7"></a>
## 7️⃣ POS to SOP Conversion & Simplification

### ❓ Question:
> **Given $F(A,B,C,D) = (A + B' + C)(A' + C + D')(B + C' + D)$, convert into SOP form and simplify.**

### ✍️ Solution:
1. **Find Maxterms ($\Pi M$):**
   - $(A + B' + C) \to M_2, M_3$
   - $(A' + C + D') \to M_9, M_{13}$
   - $(B + C' + D) \to M_2, M_{10}$
   - $\Pi M(2, 3, 9, 10, 13)$

2. **Convert to Canonical SOP ($\Sigma m$):**
   $$\Sigma m(0, 1, 4, 5, 6, 7, 8, 11, 12, 14, 15)$$

3. **Simplify using 4-Variable K-Map:**
   - Quad $\{4,5,6,7\} \to A'B$
   - Quad $\{0,1,4,5\} \to A'C'$
   - Quad $\{0,4,8,12\} \to C'D'$
   - Quad $\{14,15,11,10\} \text{ or } \{6,7,14,15\} \to BC \text{ and } ACD$

**Minimal SOP Expression:**
$$\mathbf{F = A'C' + C'D' + BC + ACD}$$ ✅

---

<a id="prob-8"></a>
## 8️⃣ Minimal SOP K-Map (11 Minterms)

### ❓ Question:
> **Simplify $F(A,B,C,D) = \Sigma m(0,1,2,5,6,7,8,9,10,14,15)$ using 4-variable K-Map.**

### ✍️ Solution:

K-Map Grid:
```
       CD  C'D'  C'D   CD   CD'
  AB      (00)  (01)  (11) (10)
A'B' (00)   1     1     0    1
A'B  (01)   0     1     1    1
AB   (11)   0     0     1    1
AB'  (10)   1     1     0    1
```

**Groups formed:**
1. **Corner Quad $\{0, 2, 8, 10\}$:** Gives $\mathbf{B'D'}$
2. **Quad $\{0, 1, 8, 9\}$:** Gives $\mathbf{B'C'}$
3. **Quad $\{6, 7, 14, 15\}$:** Gives $\mathbf{BC}$
4. **Group $\{1, 5\}$:** Gives $\mathbf{A'C'D}$

**Minimal SOP:**
$$\mathbf{F = B'C' + BC + B'D' + A'C'D}$$ ✅

---

<a id="prob-9"></a>
## 9️⃣ Minimal POS K-Map (8 Maxterms)

### ❓ Question:
> **Simplify $F(A,B,C,D) = \Pi M(1,3,4,6,9,11,12,14)$ using K-Map and obtain minimal POS.**

### ✍️ Solution:
Place 0s at Maxterms $\{1, 3, 4, 6, 9, 11, 12, 14\}$.

**Group 0s for POS:**
- Quad of 0s at $\{1, 3, 9, 11\} \implies \mathbf{(B + D')}$
- Quad of 0s at $\{4, 6, 12, 14\} \implies \mathbf{(B' + D)}$

**Minimal POS Expression:**
$$\mathbf{F = (B + D')(B' + D)}$$ ✅

---

<a id="prob-10"></a>
## 🔟 Essential Prime Implicants (EPI) Identification

### ❓ Question:
> **Given $F(A,B,C,D) = \Sigma m(2,3,4,5,6,7,10,11,14,15)$:**  
> **a) Simplify using K-Map**  
> **b) Identify all Essential Prime Implicants**  
> **c) Write the minimal expression**

### ✍️ Solution:

#### a) K-Map Grouping:
- **Octet $\{2, 3, 6, 7, 10, 11, 14, 15\}$:** Eliminates 3 variables $\to$ Gives $\mathbf{C}$
- **Quad $\{4, 5, 6, 7\}$:** Gives $\mathbf{A'B}$

#### b) Essential Prime Implicants (EPIs):
- **EPI 1:** $\mathbf{C}$ (covers minterms 2, 3, 10, 11, 14, 15 uniquely)
- **EPI 2:** $\mathbf{A'B}$ (covers minterm 4 uniquely)

#### c) Minimal Expression:
$$\mathbf{F = C + A'B}$$ ✅

---

<a id="prob-11"></a>
## 1️⃣1️⃣ K-Map with Don't Cares (Problem 1)

### ❓ Question:
> **Simplify $F(A,B,C,D) = \Sigma m(1,3,7,11,15) + d(0,2,5,8,10)$**

### ✍️ Solution:
- Combine 1s at $\{1, 3\}$ with don't cares $\{0, 2\}$ to form **Quad $\{0, 1, 2, 3\}$** $\to$ Gives $\mathbf{A'B'}$
- Combine 1s at $\{3, 7, 11, 15\}$ to form **Quad $\{3, 7, 11, 15\}$** $\to$ Gives $\mathbf{CD}$

**Minimal SOP:**
$$\mathbf{F = A'B' + CD}$$ ✅

---

<a id="prob-12"></a>
## 1️⃣2️⃣ K-Map with Don't Cares (Problem 2)

### ❓ Question:
> **Simplify $Y(A,B,C,D) = \Sigma m(0,1,3,4,7,8,9,11,12,15) + d(2,5,6,10,13,14)$**

### ✍️ Solution:
- Minterms count $= 10$
- Don't care count $= 6$
- **Total cells covered $= 10 + 6 = 16$ cells!**
- All 16 cells in the K-Map are filled with 1s or $X$s.
- Form a single **Octet of 16 cells** covering the entire K-Map.

**Minimal Expression:**
$$\mathbf{Y = 1}$$ ✅

---

<a id="prob-13"></a>
## 1️⃣3️⃣ Full Circuit Synthesis & NOR-Only Realization

### ❓ Question:
> **A Boolean function is given as $F(A,B,C,D) = A'B'C + AB'D + ABC + ACD'$:**  
> **a) Convert to canonical SOP**  
> **b) Simplify using K-Map**  
> **c) Realize using NOR-only implementation**

### ✍️ Solution:

#### a) Canonical SOP:
- $A'B'C(D+D') = m_3 + m_2$
- $AB'D(C+C') = m_{11} + m_9$
- $ABC(D+D') = m_{15} + m_{14}$
- $ACD'(B+B') = m_{14} + m_{10}$
$$\mathbf{F(A,B,C,D) = \Sigma m(2, 3, 9, 10, 11, 14, 15)}$$

#### b) Simplify using K-Map:
- Quad $\{3, 11, 15, 7? \dots \text{Group } \{3,2,11,10\} \to \mathbf{B'C}\}$
- Quad $\{10, 11, 14, 15\} \to \mathbf{AC}$
- Group $\{9, 11\} \to \mathbf{AB'D}$
$$\mathbf{F = AC + B'C + AB'D}$$

#### c) NOR-Only Implementation (2-Level NOR-NOR):
To implement SOP using NOR gates only, apply double negation:
$$F = \overline{\overline{AC + B'C + AB'D}} = \overline{\overline{AC} \cdot \overline{B'C} \cdot \overline{AB'D}}$$

**NOR Gate Configuration:**
1. **Level 1 NOR Gates:**
   - Gate 1: Inputs $\overline{A}, \overline{C} \implies \text{Output} = \overline{\overline{A} + \overline{C}} = AC$
   - Gate 2: Inputs $B, \overline{C} \implies \text{Output} = \overline{B + \overline{C}} = B'C$
   - Gate 3: Inputs $\overline{A}, B, \overline{D} \implies \text{Output} = \overline{\overline{A} + B + \overline{D}} = AB'D$
2. **Level 2 NOR Gate:**
   - Combine outputs of Level 1 NOR gates using a NOR gate to get final $F$! ✅
