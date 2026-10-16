# -*- coding: utf-8 -*-
"""
Append Faculty Revision Hacks directly to 08-dld-faculty-imp-curated-master-solutions.md
"""
target_file = r"c:\Users\ankit\Fall2627\DLD\notes\term_end\08-dld-faculty-imp-curated-master-solutions.md"

appendix = """

---

# 🎯 SPECIAL SECTION: Faculty Classroom Revision Hacks & Exam Directives
*(Extracted directly from Dr. Kanimozhi M's blackboard revision notes & hints)*

---

### ⚡ HACK 1: The Register Clock Pulse Rule (Exam Numerical Guaranteed!)
**Question**: *For an n-bit (4-bit or 8-bit) shift register, how many clock pulses are required to load and retrieve data?*

| Shift Register Mode | Pulses to LOAD Data | Pulses to READ / UNLOAD Data | Total Clock Pulses (Load + Unload) |
|:---|:---:|:---:|:---:|
| **SISO** (Serial-In Serial-Out) | **n pulses** | **n - 1 pulses** | **2n - 1 pulses** (e.g. 4-bit = 7 pulses, 8-bit = 15 pulses) |
| **SIPO** (Serial-In Parallel-Out) | **n pulses** | **0 pulses** (Instantaneous in parallel) | **n pulses** (4-bit = 4, 8-bit = 8) |
| **PISO** (Parallel-In Serial-Out) | **1 pulse** (Parallel load) | **n - 1 pulses** (Serial shift) | **n pulses** (4-bit = 4, 8-bit = 8) |
| **PIPO** (Parallel-In Parallel-Out) | **1 pulse** | **0 pulses** | **1 pulse** (Fastest register) |

---

### ⚡ HACK 2: Sequence Detector — Always Default to D Flip-Flop!
> **Faculty Instruction**: *"Agar nhi likha kis FF se krna hai to D FF se kro!"*
- **Why D Flip-Flop?** Because the characteristic equation of D-FF is:
  $$D = Q_{next}$$
  This means you **never need an excitation table**! The K-map for input $D_A$ is literally the column of $Q_A^+$, and $D_B$ is literally $Q_B^+$. This cuts your exam solving time by 70%!

#### Worked Example: Overlapping '1010' Sequence Detector using D Flip-Flops
1. **States**: $S_0 (00), S_1 (01), S_2 (10), S_3 (11)$ with 2 state variables $Q_1, Q_0$.
2. **State Transition Table**:
   | Present State ($Q_1 Q_0$) | Input $x=0$ ($Q_1^+ Q_0^+, y$) | Input $x=1$ ($Q_1^+ Q_0^+, y$) |
   |:---:|:---:|:---:|
   | $S_0$ (00) | 00, 0 | 01, 0 |
   | $S_1$ (01) | 10, 0 | 01, 0 |
   | $S_2$ (10) | 00, 0 | 11, 0 |
   | $S_3$ (11) | **10, 1 (Detected!)** | 01, 0 |
3. **D Inputs**:
   - $D_1 = Q_1^+ = \\sum m(1, 7)$ (for inputs $x, Q_1, Q_0$) $\\implies \\mathbf{D_1 = x' Q_1' Q_0 + x Q_1 Q_0'}$
   - $D_0 = Q_0^+ = x$ (simply equals input $x$!)
   - Output $y = x' Q_1 Q_0$
4. **Schematic**: Two D flip-flops with $D_0 = x$, $D_1 = x' Q_1' Q_0 + x Q_1 Q_0'$, and $y = x' Q_1 Q_0$. Done in under 5 minutes!

---

### ⚡ HACK 3: Mod-6 Synchronous Counter (Mod-N Design)
**Sequence**: $0 \\to 1 \\to 2 \\to 3 \\to 4 \\to 5 \\to 0$. Unused states: $6 (110_2), 7 (111_2)$.
1. **Number of FFs**: $2^n \\ge 6 \\implies n = 3$ FFs ($Q_C, Q_B, Q_A$).
2. **Transition & D-FF Excitation Table ($D = Q^+$)**:
   | Present ($Q_C Q_B Q_A$) | Next ($Q_C^+ Q_B^+ Q_A^+$) | $D_C$ | $D_B$ | $D_A$ |
   |:---:|:---:|:---:|:---:|:---:|
   | 0 0 0 | 0 0 1 | 0 | 0 | 1 |
   | 0 0 1 | 0 1 0 | 0 | 1 | 0 |
   | 0 1 0 | 0 1 1 | 0 | 1 | 1 |
   | 0 1 1 | 1 0 0 | 1 | 0 | 0 |
   | 1 0 0 | 1 0 1 | 1 | 0 | 1 |
   | 1 0 1 | 0 0 0 | 0 | 0 | 0 |
   | 1 1 0 (Unused) | X X X | X | X | X |
   | 1 1 1 (Unused) | X X X | X | X | X |

3. **K-Maps (with Don't Cares 6, 7)**:
   - $D_C = Q_C Q_A' + Q_B Q_A$
   - $D_B = Q_C' Q_B' Q_A + Q_B Q_A' = Q_C' (Q_B \\oplus Q_A)$
   - $D_A = Q_A'$
4. **Schematic**: 3 D flip-flops clocked simultaneously.

---

### ⚡ HACK 4: Module 5 "Only Coding" — 4:1 MUX & 2:4 Decoder with `case`
> **Faculty Instruction**: *"Truth table de denge, fir code likhna hoga... use case statement!"*

#### 1. 2:4 Decoder with Enable in Behavioral Verilog (`case` statement):
```verilog
module decoder2to4_behavioral (
    input [1:0] a,
    input en,
    output reg [3:0] y
);
    always @(*) begin
        if (!en)
            y = 4'b0000;
        else begin
            case (a)
                2'b00: y = 4'b0001;
                2'b01: y = 4'b0010;
                2'b10: y = 4'b0100;
                2'b11: y = 4'b1000;
                default: y = 4'b0000;
            endcase
        end
    end
endmodule
```

#### 2. 4:1 Multiplexer in Behavioral Verilog (`case` statement):
```verilog
module mux4to1_behavioral (
    input [3:0] in,
    input [1:0] sel,
    output reg y
);
    always @(*) begin
        case (sel)
            2'b00: y = in[0];
            2'b01: y = in[1];
            2'b10: y = in[2];
            2'b11: y = in[3];
            default: y = 1'b0;
        endcase
    end
endmodule
```

---

### ⚡ HACK 5: SR and D Latches using NAND and NOR Gates

#### 1. SR Latch using NOR Gates:
```text
R ───┤ NOR 1 ├─────── Q
     │       │   ┌───┘
     │       └───┼───┐
S ───┤ NOR 2 ├─────── Q'
```
* **Truth Table**:
  - $S=0, R=0 \\implies$ No change ($Q_n$)
  - $S=0, R=1 \\implies$ Reset ($Q=0, Q'=1$)
  - $S=1, R=0 \\implies$ Set ($Q=1, Q'=0$)
  - $S=1, R=1 \\implies$ **Forbidden / Invalid ($Q=0, Q'=0$)**

#### 2. SR Latch using NAND Gates:
* Cross-coupled NAND gates operate with **active-low inputs** ($\\overline{S}, \\overline{R}$):
  - $\\overline{S}=1, \\overline{R}=1 \\implies$ No change
  - $\\overline{S}=1, \\overline{R}=0 \\implies$ Reset ($Q=0$)
  - $\\overline{S}=0, \\overline{R}=1 \\implies$ Set ($Q=1$)
  - $\\overline{S}=0, \\overline{R}=0 \\implies$ **Invalid ($Q=1, Q'=1$)**

#### 3. D Latch (Transparent Latch):
* Formed from an enabled SR latch where $S = D$ and $R = \\overline{D}$ (via an inverter).
* When $EN = 1$: Output tracks input ($Q = D$).
* When $EN = 0$: Output retains previous state ($Q = Q_{prev}$).
"""

with open(target_file, "a", encoding="utf-8") as f:
    f.write(appendix)

print("Appended successfully!")
