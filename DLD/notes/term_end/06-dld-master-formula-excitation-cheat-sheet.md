# 📑 ECE2002: DLD Master Formula & Excitation Cheat Sheet

> Print or keep this 1-page summary open for instant formula retrieval during revision!

---

## 1. Master Flip-Flop Excitation & Characteristic Table

| Present State $Q_n$ | Next State $Q_{n+1}$ | SR: $S, R$ | JK: $J, K$ | D: $D$ | T: $T$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$0$** | **$0$** | $0, X$ | $0, X$ | $0$ | $0$ |
| **$0$** | **$1$** | $1, 0$ | $1, X$ | $1$ | $1$ |
| **$1$** | **$0$** | $0, 1$ | $X, 1$ | $0$ | $1$ |
| **$1$** | **$1$** | $X, 0$ | $X, 0$ | $1$ | $0$ |

### Characteristic Equations
* **SR FF**: $Q_{n+1} = S + R' Q_n \quad (S \cdot R = 0)$
* **JK FF**: $Q_{n+1} = J Q_n' + K' Q_n$
* **D FF**: $Q_{n+1} = D$
* **T FF**: $Q_{n+1} = T \oplus Q_n$

---

## 2. Arithmetic & Combinational Building Blocks

* **Full Adder**:
  $$\text{Sum } S = A \oplus B \oplus C_{in}, \quad C_{out} = A B + C_{in}(A \oplus B)$$
* **Full Subtractor**:
  $$\text{Diff } D = A \oplus B \oplus B_{in}, \quad B_{out} = A' B + B_{in}(A \oplus B)'$$
* **Carry Look-Ahead**:
  $$G_i = A_i B_i \quad (\text{Generate}), \quad P_i = A_i \oplus B_i \quad (\text{Propagate})$$
  $$C_1 = G_0 + P_0 C_0, \quad C_2 = G_1 + P_1 G_0 + P_1 P_0 C_0$$
* **BCD Adder Correction**:
  $$\text{Add } 0110_2 \iff C = K + S_3 S_2 + S_3 S_1 = 1$$
* **Binary $\leftrightarrow$ Gray Code**:
  $$G_i = B_i \oplus B_{i+1}, \quad B_i = G_i \oplus B_{i+1}$$

---

## 3. Shift Register Clock Budgets
* **SISO**: $n$ to load, $n-1$ to unload $\implies \mathbf{2n - 1\text{ pulses}}$
* **SIPO**: $\mathbf{n\text{ pulses}}$
* **PISO**: $1$ to load, $n-1$ to unload $\implies \mathbf{n\text{ pulses}}$
* **PIPO**: $\mathbf{1\text{ pulse}}$

---

## 4. Counter Formulas
* **Ring Counter**: States $= N$, Frequency out $= f_{clk} / N$
* **Johnson Counter**: States $= 2N$, Frequency out $= f_{clk} / 2N$
* **Mod-$N$ Ripple Counter**: Connect output bits that are `1` at count $N$ to NAND gate driving $\overline{\text{CLR}}$.

---

## 5. Logic Families Rapid Metric Comparison
* **Fastest**: ECL ($1–2\text{ ns}$ delay, non-saturated transistors)
* **Lowest Static Power**: CMOS (Virtually zero, $\mu\text{W}$)
* **Highest Noise Margin**: CMOS ($0.45 \times V_{DD}$)
* **Highest Fan-Out**: CMOS ($> 50$)
