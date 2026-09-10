# ⚡ DLD Day 3+ — Master Cheatsheet

> **Covers Modules 3, 4, 5: Boolean Algebra, K-Maps, Combinational & Sequential Logic**

---

## 📐 Boolean Algebra Quick Rules
* **Identity:** $A + 0 = A$ | $A \cdot 1 = A$
* **Null:** $A + 1 = 1$ | $A \cdot 0 = 0$
* **Idempotent:** $A + A = A$ | $A \cdot A = A$
* **Complement:** $A + \overline{A} = 1$ | $A \cdot \overline{A} = 0$
* **Absorption:** $A + AB = A$
* **De Morgan's:** $\overline{A \cdot B} = \overline{A} + \overline{B}$ (Break the bar, change the sign)

---

## 🚪 Logic Gates
* **AND ($A \cdot B$)**: 1 only if BOTH are 1
* **OR ($A + B$)**: 1 if ANY is 1
* **XOR ($A \oplus B$)**: 1 only if inputs are DIFFERENT
* **XNOR ($\overline{A \oplus B}$)**: 1 only if inputs are SAME
* **NAND / NOR**: Universal gates (can build any other gate).

---

## 🗺️ K-Map Grouping Rules
1. Group sizes must be powers of 2 (1, 2, 4, 8, 16).
2. Groups can overlap.
3. Groups can wrap around edges (top connects to bottom, left to right).
4. Bigger groups = simpler terms. (Group of 8 eliminates 3 variables, group of 4 eliminates 2).

---

## 🧩 Combinational Logic (No Memory)

| Component | What it does |
|---|---|
| **Multiplexer (MUX)** | Many inputs $\rightarrow$ 1 output. Uses select lines to choose. |
| **Demultiplexer (DeMUX)** | 1 input $\rightarrow$ Many outputs. |
| **Decoder** | $n$ inputs $\rightarrow$ $2^n$ outputs. Converts binary to a specific active line. |
| **Encoder** | $2^n$ inputs $\rightarrow$ $n$ outputs. (Reverse of Decoder). |
| **Half Adder** | Adds 2 bits. Outputs Sum ($A \oplus B$) and Carry ($A \cdot B$). |
| **Full Adder** | Adds 3 bits (A, B, Carry-in). |

---

## ⏱️ Sequential Logic (Has Memory)

* **SR Latch:** $S=1$ (Set output to 1). $R=1$ (Reset output to 0). $S=1, R=1$ is **INVALID**.
* **D Flip-Flop:** "Data" flip-flop. Output $Q$ just follows input $D$ on the clock edge. (Used in Registers).
* **JK Flip-Flop:** Like SR, but $J=1, K=1$ is allowed and it **toggles** the output.
* **T Flip-Flop:** "Toggle" flip-flop. $T=1$ toggles the output, $T=0$ keeps it same. (Used in Counters).

### Counters
* **Asynchronous (Ripple):** Clock only goes to the first flip-flop. The output of one triggers the next. (Slower).
* **Synchronous:** Clock goes to ALL flip-flops simultaneously. (Faster).

---

## 💻 Verilog HDL Syntax (Basics)

**Dataflow Modeling (using `assign`):**
```verilog
module my_and(input a, input b, output y);
    assign y = a & b;
endmodule
```

**Gate-Level Modeling (using built-in gates):**
```verilog
module my_xor(input a, input b, output y);
    xor G1 (y, a, b); // syntax: gate_name instance_name (output, inputs...);
endmodule
```
