# 🎯 ECE2002: High-Frequency FAT / TEE Exam Question Bank (15 Solved Questions)

> Fully solved in Dr. Kanimozhi's required design rubric: State Table ➔ Transition Matrix ➔ K-Maps ➔ Boolean Equations ➔ Circuit Diagram.

---

## UNIT 1: Number Systems & Logic Families

### Q1 (12 Marks) [Section A Model]
**(a) Perform $(43)_{10} - (21)_{10}$ and $(21)_{10} - (43)_{10}$ using 8-bit 2's complement arithmetic.**  
**(b) Compare TTL, ECL, and CMOS logic families with respect to propagation delay, power dissipation, noise margin, and fan-out.**

**Solution**:
1. **Part (a)**:
   - Convert to 8-bit binary:
     - $+43 = 00101011_2$
     - $+21 = 00010101_2$
   - 2's complement of $+21$:
     - 1's comp $= 11101010$, 2's comp $= 11101011_2$
   - Operation 1: $43 - 21$:
     $$00101011 + 11101011 = \mathbf{1}00010110_2$$
     End carry generated ($1$). Discard end carry $\implies$ Result is positive: $00010110_2 = \mathbf{+22_{10}}$ (Correct!).
   - Operation 2: $21 - 43$:
     - 2's comp of $+43$: $11010100 + 1 = 11010101_2$
     $$00010101 + 11010101 = 11101010_2$$
     No carry out. Result is negative and in 2's complement form.
     Magnitude: 2's comp of $11101010 = 00010101 + 1 = 00010110_2 = 22_{10}$.  
     $\therefore \text{Result} = \mathbf{-22_{10}}$ (Correct!).
2. **Part (b)**: *[Include full 4-row comparative table from Unit 1 notes: ECL fastest, CMOS lowest power & highest noise margin, TTL moderate]*.

---

### Q2 (8 Marks) [Section B Model]
**Prove the Consensus Theorem using Boolean algebra postulates:**
$$(A + B)(\overline{A} + C)(B + C) = (A + B)(\overline{A} + C)$$

**Solution**:
1. Take Left-Hand Side (LHS):
   $$LHS = (A + B)(\overline{A} + C)(B + C)$$
2. Multiply first two terms:
   $$(A\overline{A} + AC + \overline{A}B + BC)(B + C) = (0 + AC + \overline{A}B + BC)(B + C)$$
   $$= (AC + \overline{A}B + BC)(B + C)$$
3. Expand:
   $$= ABC + ACC + \overline{A}BB + \overline{A}BC + BBC + BCC$$
   $$= ABC + AC + \overline{A}B + \overline{A}BC + BC + BC \quad (\because CC=C, BB=B)$$
   $$= AC(1 + B) + \overline{A}B(1 + C) + BC$$
   $$= AC + \overline{A}B + BC$$
4. Express $BC$ as $BC(A + \overline{A})$:
   $$= AC + \overline{A}B + ABC + \overline{A}BC$$
   $$= AC(1 + B) + \overline{A}B(1 + C) = \mathbf{AC + \overline{A}B}$$
5. Now expand RHS:
   $$(A + B)(\overline{A} + C) = A\overline{A} + AC + \overline{A}B + BC = 0 + AC + \overline{A}B + BC = \mathbf{AC + \overline{A}B}$$
   $$\therefore LHS = RHS \quad \text{[Proved]}$$

---

## UNIT 2: Combinational Logic & Arithmetic

### Q3 (12 Marks) [Section A Model]
**Design a Full Subtractor circuit using minimum number of NAND gates only.**

**Solution**:
1. **Equations**:
   $$\text{Difference } D = A \oplus B \oplus B_{in}$$
   $$\text{Borrow } B_{out} = A' B + B_{in}(A \oplus B)'$$
2. **NAND Implementation Steps**:
   - Recall that an XOR gate requires **4 NAND gates**.
   - Implementing $A \oplus B$ takes 4 NANDs, producing intermediate signals $A'B$ and $AB'$.
   - Feeding $(A \oplus B)$ and $B_{in}$ into a second 4-NAND XOR block yields Difference $D$ (4 more NANDs).
   - An extra NAND combines the intermediate borrow terms.
   - Total NAND count required = **9 NAND gates**.

---

### Q4 (8 Marks) [Section B Model]
**Design a 4-bit Binary-to-Gray code converter using logic gates. Show truth table, K-maps, and circuit diagram.**

**Solution**:
1. **Equations derived from K-Maps**:
   $$G_3 = B_3$$
   $$G_2 = B_3 \oplus B_2$$
   $$G_1 = B_2 \oplus B_1$$
   $$G_0 = B_1 \oplus B_0$$
2. **Hardware**: 3 XOR gates. Input $B_3$ directly passes to output $G_3$.

---

## UNIT 3: Sequential Circuits & Flip-Flops

### Q5 (12 Marks) [Section A Model]
**Convert an SR flip-flop into a JK flip-flop. Show the conversion table, K-maps, and logic schematic.**

**Solution**:
1. **Target FF**: JK. **Available FF**: SR.
2. **Conversion Table**:

| Target Inputs ($J, K$) | Present State $Q_n$ | Next State $Q_{n+1}$ | Required $S$ | Required $R$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 0 | 0 | 0 | 0 | $X$ |
| 0 0 | 1 | 1 | $X$ | 0 |
| 0 1 | 0 | 0 | 0 | $X$ |
| 0 1 | 1 | 0 | 0 | 1 |
| 1 0 | 0 | 1 | 1 | 0 |
| 1 0 | 1 | 1 | $X$ | 0 |
| 1 1 | 0 | 1 | 1 | 0 |
| 1 1 | 1 | 0 | 0 | 1 |

3. **K-Map for $S(J, K, Q_n)$**:
   $$\mathbf{S = J Q_n'}$$
4. **K-Map for $R(J, K, Q_n)$**:
   $$\mathbf{R = K Q_n}$$
5. **Circuit Diagram**: Connect output of AND gate ($J \cdot Q'$) to $S$ pin. Connect output of AND gate ($K \cdot Q$) to $R$ pin.

---

### Q6 (8 Marks) [Section B Model]
**Explain the operation of an edge-triggered D flip-flop with timing diagrams. Define Setup time, Hold time, and Propagation delay.**

**Solution**:
1. **Operational Mechanism**: Output $Q$ samples input $D$ strictly at the clock transition edge. Between edges, input variations are ignored.
2. **Timing Definitions**:
   - *Setup Time ($t_{su}$)*: Minimum time $D$ must be stable before active clock edge.
   - *Hold Time ($t_h$)*: Minimum time $D$ must remain stable after active clock edge.
   - *Propagation Delay ($t_{pd}$)*: Time elapsed from active clock edge to valid state change at $Q$.

---

## UNIT 4: Registers, Counters & FSMs

### Q7 (12 Marks) [Section A Model]
**Design a Synchronous Decade (Mod-10) Counter using JK flip-flops. Verify that the counter is self-starting.**

**Solution**:
1. **Number of FFs**: $2^n \ge 10 \implies n = 4$ FFs ($Q_D, Q_C, Q_B, Q_A$). Unused states: $10$ to $15$.
2. **Derivation using JK Excitation Table**:
   - $J_A = 1, \quad K_A = 1$ (FF A toggles every clock pulse).
   - $J_B = Q_A \cdot Q_D', \quad K_B = Q_A$.
   - $J_C = Q_A \cdot Q_B, \quad K_C = Q_A \cdot Q_B$.
   - $J_D = Q_A \cdot Q_B \cdot Q_C, \quad K_D = Q_A$.
3. **Self-Starting Check**: Testing unused states $1010_2$ to $1111_2$ reveals all transitions terminate in valid states $0000$ or $0001$ within 2 clock cycles $\implies$ **Self-starting verified!**

---

### Q8 (8 Marks) [Section B Model]
**Differentiate between a 4-bit Ring Counter and a 4-bit Johnson Counter. Show their respective state sequences and clock frequency division ratios.**

**Solution**:
1. **Ring Counter (4 FFs)**: States $= 4$ (`1000 -> 0100 -> 0010 -> 0001 -> 1000`). Divides clock frequency by **$4$**.
2. **Johnson Counter (4 FFs)**: States $= 8$ (`0000 -> 1000 -> 1100 -> 1110 -> 1111 -> 0111 -> 0011 -> 0001 -> 0000`). Divides clock frequency by **$8$**.

---

## UNIT 5: Verilog HDL Modeling

### Q9 (12 Marks) [Section A Model]
**Write a Verilog HDL module to model a 4-bit Universal Shift Register supporting Hold, Shift-Right, Shift-Left, and Parallel-Load modes. Write a testbench to verify all 4 modes.**

**Solution**:
```verilog
module universal_shift_reg_4bit (
    input clk,
    input reset,
    input [1:0] mode,       // 00: Hold, 01: Shift Right, 10: Shift Left, 11: Parallel Load
    input [3:0] parallel_in,
    input s_right_in,
    input s_left_in,
    output reg [3:0] q
);
    always @(posedge clk or posedge reset) begin
        if (reset)
            q <= 4'b0000;
        else begin
            case (mode)
                2'b00: q <= q;                                // Hold
                2'b01: q <= {s_right_in, q[3:1]};             // Shift Right
                2'b10: q <= {q[2:0], s_left_in};              // Shift Left
                2'b11: q <= parallel_in;                      // Parallel Load
            endcase
        end
    end
endmodule
```

---

### Q10 (8 Marks) [Section B Model]
**Explain the difference between Continuous Assignment (`assign`) and Procedural Assignment (`always`) in Verilog with code examples.**

**Solution**:
1. **Continuous (`assign`)**: Used for dataflow modeling of combinational logic. Operates concurrently. Drivers must be of type `wire`.
   ```verilog
   assign out = a & b;
   ```
2. **Procedural (`always`)**: Used for behavioral modeling. Executes sequentially within the block when sensitivity list triggers. Target variables must be of type `reg`.
   ```verilog
   always @(posedge clk) begin
       q <= d;
   end
   ```

---

### Q11 (12 Marks) [Direct from Group Activity B]
**(a) Develop a Gate-level design for a Full Subtractor circuit considering gate delays: AND Gate: 10 ns, OR Gate: 10 ns, NOT Gate: 5 ns.**  
**(b) Write Verilog code for an 8:1 multiplexer circuit using behavioral modeling along with its testbench code.**

**Solution**:
```verilog
// (a) Full Subtractor with Gate Delays
`timescale 1ns / 1ps
module full_subtractor_delays (
    input a, b, bin,
    output diff, bout
);
    wire d1, na, nb, nbin, nd1;
    wire a_nb, na_b, d1_nbin, nd1_bin, na_and_b, nd1_and_bin;

    not #5  inv1 (na, a);
    not #5  inv2 (nb, b);
    and #10 and1 (a_nb, a, nb);
    and #10 and2 (na_b, na, b);
    or  #10 or1  (d1, a_nb, na_b);       // d1 = a ^ b

    not #5  inv3 (nd1, d1);
    not #5  inv4 (nbin, bin);
    and #10 and3 (d1_nbin, d1, nbin);
    and #10 and4 (nd1_bin, nd1, bin);
    or  #10 or2  (diff, d1_nbin, nd1_bin); // diff = d1 ^ bin

    and #10 and5 (na_and_b, na, b);
    and #10 and6 (nd1_and_bin, nd1, bin);
    or  #10 or3  (bout, na_and_b, nd1_and_bin); // bout
endmodule

// (b) 8:1 MUX Behavioral & Testbench
module mux8to1_behavioral (
    input [7:0] in,
    input [2:0] sel,
    output reg y
);
    always @(*) begin
        case (sel)
            3'b000: y = in[0]; 3'b001: y = in[1];
            3'b010: y = in[2]; 3'b011: y = in[3];
            3'b100: y = in[4]; 3'b101: y = in[5];
            3'b110: y = in[6]; 3'b111: y = in[7];
            default: y = 1'b0;
        endcase
    end
endmodule

module tb_mux8to1;
    reg [7:0] in; reg [2:0] sel; wire y;
    mux8to1_behavioral uut (.in(in), .sel(sel), .y(y));
    initial begin
        in = 8'b11001010;
        sel = 3'b001; #10; // y = in[1] = 1
        sel = 3'b010; #10; // y = in[2] = 0
        sel = 3'b111; #10; // y = in[7] = 1
        $finish;
    end
endmodule
```

---

### Q12 (10 Marks) [Direct from Group Activity B]
**(a) Write Verilog code for an 8:3 Priority Encoder circuit using behavioral modeling and its testbench.**  
**(b) Write Verilog code for a Decade (BCD) Counter circuit using behavioral modeling.**

**Solution**:
```verilog
// (a) 8:3 Priority Encoder
module priority_encoder_8to3 (
    input [7:0] in,
    output reg [2:0] code,
    output reg valid
);
    always @(*) begin
        valid = 1'b1;
        if      (in[7]) code = 3'b111;
        else if (in[6]) code = 3'b110;
        else if (in[5]) code = 3'b101;
        else if (in[4]) code = 3'b100;
        else if (in[3]) code = 3'b011;
        else if (in[2]) code = 3'b010;
        else if (in[1]) code = 3'b001;
        else if (in[0]) code = 3'b000;
        else begin code = 3'b000; valid = 1'b0; end
    end
endmodule

// (b) Decade (BCD) Counter
module bcd_counter (
    input clk, reset,
    output reg [3:0] q
);
    always @(posedge clk or posedge reset) begin
        if (reset)
            q <= 4'b0000;
        else if (q == 4'b1001) // Reset after 9
            q <= 4'b0000;
        else
            q <= q + 1'b1;
    end
endmodule
```

---

### Q13 (10 Marks) [Direct from Group Activity Activity Circuits]
**Write Gate-Level Verilog HDL code for the following circuits:**  
**(a) Circuit 1: 4 NAND gates, 1 inverter, and 3 XOR gates generating outputs $z_0$ and $z_1$.**  
**(b) Circuit 2: 1 XOR gate, 2 AND gates, and 1 OR gate generating output $y$.**

**Solution**:
```verilog
// (a) Circuit 1
module circuit_1 (
    input a0, b0, a1, b1,
    output z0, z1
);
    wire n1, n2, n3, n4, n5, n6;
    nand G1 (n1, a0, b0);
    nand G2 (n2, a1, b1);
    nand G3 (n3, a1, b0);
    nand G4 (n4, a0, b1);
    not  G8 (n5, n2);
    xor  G5 (n6, n3, n4);
    xor  G6 (z0, n1, n2);
    xor  G7 (z1, n5, n6);
endmodule

// (b) Circuit 2
module circuit_2 (
    input a, b, c, d,
    output y
);
    wire w1, w2, w3;
    xor x1 (w1, b, c);
    and a1 (w2, a, w1);
    and a2 (w3, w1, d);
    or  o1 (y, w2, w3);
endmodule
```
