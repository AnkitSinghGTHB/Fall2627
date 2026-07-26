# 🏋️ Digital Logic Design (ECE2002) — Practice Questions Worksheet

> **Instructions**: Attempt all questions on paper *before* opening the collapsible solution blocks!

---

## 🔢 Section A: Number Systems, Base Conversions & Complements

### Question 1
Convert $(254.375)_{10}$ into:
1. Binary
2. Octal
3. Hexadecimal

### Question 2
Perform $(42)_{10} - (18)_{10}$ using 8-bit 2's complement arithmetic. Show all steps and verify if an overflow occurs.

### Question 3
Convert the BCD number $(0111\,1001)_{BCD}$ into Excess-3 code.

<details>
<summary>💡 Check Solutions for Section A</summary>

#### Solution 1:
- **Binary**: $(11111110.011)_2$
- **Octal**: $(376.3)_8$
- **Hexadecimal**: $(FE.6)_{16}$

#### Solution 2:
- $+42 = 00101010$
- $+18 = 00010010 \implies 2\text{'s complement of } 18 = 11101110$
- Add: $00101010 + 11101110 = 1\,00011000$
- Discard end carry $1 \implies 00011000_2 = (+24)_{10}$. No overflow.

#### Solution 3:
- BCD digits: $7$ and $9$.
- Add $3$ to each digit: $7+3 = 10 \implies (1010)_2$, $9+3 = 12 \implies (1100)_2$.
- Excess-3 Code: $(1010\,1100)_{\text{XS-3}}$.

</details>

---

## 🗺️ Section B: Boolean Algebra & K-Maps

### Question 4
Simplify the Boolean function $F(A, B, C, D) = \Sigma m(1, 3, 7, 11, 15) + d(0, 2, 5)$ into minimal SOP form using a 4-variable K-Map.

### Question 5
Convert the SOP function $F(A, B, C) = AB + \overline{A}C$ into Canonical SOP form ($\Sigma m$).

<details>
<summary>💡 Check Solutions for Section B</summary>

#### Solution 4:
- Grouping 8 cells $(0, 1, 2, 3, 5, 7, 11, 15)$ gives $F = \overline{A}\overline{B} + CD + \overline{A}D$.
- Minimal SOP: $F = \overline{A}\overline{B} + CD + \overline{A}D$.

#### Solution 5:
- $AB = AB(C + \overline{C}) = ABC + AB\overline{C}$
- $\overline{A}C = \overline{A}(B + \overline{B})C = \overline{A}BC + \overline{A}\overline{B}C$
- Canonical SOP: $F(A, B, C) = \Sigma m(1, 3, 6, 7)$.

</details>

---

## ⚙️ Section C: Combinational & Sequential Logic

### Question 6
Design a 4:1 Multiplexer using basic logic gates and write its output Boolean expression.

### Question 7
How many flip-flops are required to design a MOD-12 synchronous counter?

<details>
<summary>💡 Check Solutions for Section C</summary>

#### Solution 6:
- Output expression: $Y = \overline{S_1}\overline{S_0}I_0 + \overline{S_1}S_0I_1 + S_1\overline{S_0}I_2 + S_1S_0I_3$.

#### Solution 7:
- Formula: $2^{n-1} < 12 \le 2^n \implies 8 < 12 \le 16 \implies \mathbf{n = 4}$ flip-flops.

</details>

---

**⏱️ Ready to revise? Back to Master Guide →** [README.md](./README.md)
