# 📘 Unit 5: Hardware Description Language (Verilog HDL) & Testbenches

---

## 1. Verilog HDL Lexical Rules & Data Types

### 1.1 Four-Valued Logic System
Verilog models real physical hardware states using 4 discrete values:
* `0`: Logic low / False / Ground ($0\text{ V}$).
* `1`: Logic high / True / Supply ($V_{DD}$).
* `x` or `X`: Unknown logic value (uninitialized reg, contention).
* `z` or `Z`: High impedance / Floating state (tri-state buffer disabled).

### 1.2 Net Types vs Variable Types
* **`wire`**: Represents a physical connecting conductor. Cannot store energy or state; must be continuously driven by a gate or continuous assignment (`assign`).
* **`reg`**: Represents a data storage variable. Retains its assigned value until updated inside a procedural block (`initial` or `always`). *Note: A `reg` does NOT necessarily synthesize to a physical hardware register/flip-flop unless updated on a clock edge.*

### 1.3 Number Formatting Syntax
Syntax: `<size>'<base><value>`
* `4'b1010`: 4-bit binary number (`10`).
* `8'hFF`: 8-bit hexadecimal number (`255`).
* `16'd42`: 16-bit decimal number (`42`).

---

## 2. The Three Levels of Modeling Abstraction

```
                               VERILOG MODELING HIERARCHY
                                           │
         ┌─────────────────────────────────┼────────────────────────────────┐
         ▼                                 ▼                                ▼
   Gate-Level                        Dataflow                         Behavioral
   Built-in primitives:              Concurrent assignment:           Procedural blocks:
   and, or, not, xor                 assign out = A & B;              always @(posedge clk)
```

### 2.1 Gate-Level Modeling (Structural)
Instantiates built-in gate primitives:
```verilog
module full_adder_gate (
    input a, b, cin,
    output sum, cout
);
    wire s1, c1, c2;
    xor g1 (s1, a, b);
    xor g2 (sum, s1, cin);
    and g3 (c1, a, b);
    and g4 (c2, s1, cin);
    or  g5 (cout, c1, c2);
endmodule
```

### 2.2 Dataflow Modeling (`assign`)
Uses Boolean operators in continuous assignments executed concurrently:
```verilog
module full_adder_dataflow (
    input a, b, cin,
    output sum, cout
);
    assign sum  = a ^ b ^ cin;
    assign cout = (a & b) | (cin & (a ^ b));
endmodule
```

### 2.3 Behavioral Modeling (`always`)
Uses procedural constructs executed algorithmically:
* **Blocking Assignment (`=`)**: Evaluated sequentially in execution order; used for purely **combinational logic**.
* **Non-Blocking Assignment (`<=`)**: Evaluated concurrently at the end of the time step; **MANDATORY for sequential circuits / flip-flops** to avoid race conditions.

---

## 3. High-Frequency Verilog Circuit Implementations

### 3.1 Positive-Edge D Flip-Flop with Asynchronous Active-Low Reset
```verilog
module d_ff_async_reset (
    input clk,
    input rst_n,    // Active-low asynchronous reset
    input d,
    output reg q
);
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            q <= 1'b0;
        else
            q <= d;
    end
endmodule
```

### 3.2 4-Bit Synchronous Up-Counter with Synchronous Clear
```verilog
module sync_counter_4bit (
    input clk,
    input reset,
    output reg [3:0] count
);
    always @(posedge clk) begin
        if (reset)
            count <= 4'b0000;
        else
            count <= count + 1'b1;
    end
endmodule
```

---

## 4. Testbench Architecture Template

A testbench is a top-level simulation wrapper containing **no external ports**:

```verilog
`timescale 1ns / 1ps

module tb_full_adder;
    // 1. Declare stimulus inputs as regs, outputs as wires
    reg a, b, cin;
    wire sum, cout;

    // 2. Instantiate Unit Under Test (UUT)
    full_adder_dataflow uut (
        .a(a),
        .b(b),
        .cin(cin),
        .sum(sum),
        .cout(cout)
    );

    // 3. Generate Stimulus
    initial begin
        $monitor("Time=%0t | a=%b b=%b cin=%b | sum=%b cout=%b", $time, a, b, cin, sum, cout);
        
        a = 0; b = 0; cin = 0; #10;
        a = 0; b = 1; cin = 0; #10;
        a = 1; b = 1; cin = 0; #10;
        a = 1; b = 1; cin = 1; #10;
        
        $finish;
    end
endmodule
```

---

## 5. Model Exam Questions & Answers

### Question 1 (12 Marks)
**Differentiate between Blocking and Non-Blocking procedural assignments in Verilog with code examples. Write a complete Verilog behavioral module for a 4-to-1 Multiplexer and write its corresponding simulation testbench.**

**Solution**:
1. **Blocking (`=`) vs Non-Blocking (`<=`) Comparative Table**:

| Feature | Blocking Assignment (`=`) | Non-Blocking Assignment (`<=`) |
|:---|:---|:---|
| **Execution Order** | Executes sequentially line-by-line before proceeding to next statement | All right-hand expressions evaluated simultaneously; schedules updates at end of time step |
| **Hardware Target** | Combinational logic blocks (`always @(*)`) | Sequential circuits, flip-flops, registers (`always @(posedge clk)`) |
| **Race Hazard Risk** | High risk in clocked flip-flop chains | Eliminates simulation-synthesis race mismatches |

2. **Verilog 4:1 Multiplexer Module**:
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
3. **Testbench Module**:
```verilog
module tb_mux4to1;
    reg [3:0] in;
    reg [1:0] sel;
    wire y;

    mux4to1_behavioral uut (.in(in), .sel(sel), .y(y));

    initial begin
        in = 4'b1010;
        sel = 2'b00; #10; // y = 0
        sel = 2'b01; #10; // y = 1
        sel = 2'b10; #10; // y = 0
        sel = 2'b11; #10; // y = 1
        $finish;
    end
endmodule
```

### Question 2 (8 Marks)
**Write a Verilog HDL module to model an active-low reset D Flip-Flop. Explain the importance of the sensitivity list in an `always` block.**

**Solution**:
1. **Module Code**: *[Provide the complete `d_ff_async_reset` code from Section 3.1]*.
2. **Sensitivity List Role**: The list of signals following `@(...)` defining the triggering events that activate execution of the procedural `always` block.
   - In combinational logic: `always @(*)` senses all input signals.
   - In sequential logic: `always @(posedge clk or negedge rst_n)` guarantees state updates occur strictly on active physical voltage transitions.

---

### Question 3 (12 Marks) [Direct from Group Activity Docx]
**(a) Write the Verilog code for an EX-OR gate using all three modeling styles (Gate-level, Dataflow, Behavioral) and explain each.**  
**(b) Develop a Gate-level design for a Full Adder considering gate delays: AND = 10ns, OR = 10ns, NOT = 5ns.**

**Solution**:
1. **Part (a): XOR Gate in All 3 Modeling Styles**:
   - **Style 1: Gate-Level (Structural)**:
     ```verilog
     module xor_gate_level (input a, b, output y);
         xor g1 (y, a, b);
     endmodule
     ```
   - **Style 2: Dataflow Modeling**:
     ```verilog
     module xor_dataflow (input a, b, output y);
         assign y = a ^ b;
     endmodule
     ```
   - **Style 3: Behavioral Modeling**:
     ```verilog
     module xor_behavioral (input a, b, output reg y);
         always @(*) begin
             if (a == b)
                 y = 1'b0;
             else
                 y = 1'b1;
         end
     endmodule
     ```
2. **Part (b): Gate-Level Full Adder with Delays**:
   ```verilog
   `timescale 1ns / 1ps

   module full_adder_delays (
       input a, b, cin,
       output sum, cout
   );
       wire s1, c1, c2;
       // XOR synthesized from NOT, AND, OR to apply specified delays:
       // AND = 10ns, OR = 10ns, NOT = 5ns
       wire na, nb, ncin, ns1;
       wire a_nb, na_b, s1_ncin, ns1_cin;

       not #5  inv1 (na, a);
       not #5  inv2 (nb, b);
       and #10 and1 (a_nb, a, nb);
       and #10 and2 (na_b, na, b);
       or  #10 or1  (s1, a_nb, na_b);       // s1 = a ^ b

       not #5  inv3 (ns1, s1);
       not #5  inv4 (ncin, cin);
       and #10 and3 (s1_ncin, s1, ncin);
       and #10 and4 (ns1_cin, ns1, cin);
       or  #10 or2  (sum, s1_ncin, ns1_cin); // sum = s1 ^ cin

       and #10 and5 (c1, a, b);
       and #10 and6 (c2, s1, cin);
       or  #10 or3  (cout, c1, c2);          // cout = ab + cin(a ^ b)
   endmodule
   ```

---

### Question 4 (12 Marks) [Direct from Group Activity Docx]
**(a) Write Verilog code for an 8:1 Multiplexer and its testbench using behavioral modeling.**  
**(b) Write Verilog code for a Decade (BCD) Counter circuit using behavioral modeling.**

**Solution**:
1. **8:1 Multiplexer with Testbench**:
   ```verilog
   module mux8to1_behavioral (
       input [7:0] in,
       input [2:0] sel,
       output reg y
   );
       always @(*) begin
           case (sel)
               3'b000: y = in[0];
               3'b001: y = in[1];
               3'b010: y = in[2];
               3'b011: y = in[3];
               3'b100: y = in[4];
               3'b101: y = in[5];
               3'b110: y = in[6];
               3'b111: y = in[7];
               default: y = 1'b0;
           endcase
       end
   endmodule

   // Testbench for 8:1 MUX
   module tb_mux8to1;
       reg [7:0] in;
       reg [2:0] sel;
       wire y;

       mux8to1_behavioral uut (.in(in), .sel(sel), .y(y));

       initial begin
           in = 8'b10101100;
           sel = 3'b000; #10; // y = in[0] = 0
           sel = 3'b010; #10; // y = in[2] = 1
           sel = 3'b111; #10; // y = in[7] = 1
           $finish;
       end
   endmodule
   ```
2. **Decade (BCD) Counter Behavioral Code**:
   ```verilog
   module bcd_counter (
       input clk,
       input reset,
       output reg [3:0] q
   );
       always @(posedge clk or posedge reset) begin
           if (reset)
               q <= 4'b0000;
           else if (q == 4'b1001) // Clears after 9 (counts 0 to 9)
               q <= 4'b0000;
           else
               q <= q + 1'b1;
       end
   endmodule
   ```

---

### Question 5 (12 Marks) [Direct from Group Activity B]
**Develop a Gate-level design for a Full Subtractor circuit considering gate delays: AND Gate: 10 ns, OR Gate: 10 ns, NOT Gate: 5 ns.**

**Solution**:
```verilog
`timescale 1ns / 1ps

module full_subtractor_delays (
    input a, b, bin,
    output diff, bout
);
    wire d1, na, nb, nbin, nd1;
    wire a_nb, na_b, d1_nbin, nd1_bin;
    wire na_and_b, nd1_and_bin;

    // XOR logic for Diff: d1 = a ^ b using NOT, AND, OR with delays
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

    // Borrow logic: bout = (~a & b) | (~d1 & bin)
    and #10 and5 (na_and_b, na, b);
    and #10 and6 (nd1_and_bin, nd1, bin);
    or  #10 or3  (bout, na_and_b, nd1_and_bin); // bout
endmodule
```

---

### Question 6 (12 Marks) [Direct from Group Activity B]
**Write Verilog code for an 8:3 Priority Encoder circuit using behavioral modeling and write a testbench code.**

**Solution**:
```verilog
module priority_encoder_8to3 (
    input [7:0] in,
    output reg [2:0] code,
    output reg valid
);
    always @(*) begin
        valid = 1'b1;
        if (in[7])      code = 3'b111;
        else if (in[6]) code = 3'b110;
        else if (in[5]) code = 3'b101;
        else if (in[4]) code = 3'b100;
        else if (in[3]) code = 3'b011;
        else if (in[2]) code = 3'b010;
        else if (in[1]) code = 3'b001;
        else if (in[0]) code = 3'b000;
        else begin
            code  = 3'b000;
            valid = 1'b0; // No active input
        end
    end
endmodule

// Testbench for 8:3 Priority Encoder
module tb_priority_encoder;
    reg [7:0] in;
    wire [2:0] code;
    wire valid;

    priority_encoder_8to3 uut (.in(in), .code(code), .valid(valid));

    initial begin
        in = 8'b00000000; #10; // valid=0
        in = 8'b00000100; #10; // code=2, valid=1
        in = 8'b00100100; #10; // code=5, valid=1 (higher priority in[5])
        in = 8'b10000001; #10; // code=7, valid=1 (highest priority in[7])
        $finish;
    end
endmodule
```

---

### Question 7 (10 Marks) [Direct from Group Activity A & B]
**Write Verilog code for: (a) SR Flip-Flop, and (b) JK Flip-Flop using behavioral modeling.**

**Solution**:
```verilog
// (a) SR Flip-Flop
module sr_ff (
    input clk, rst, s, r,
    output reg q, q_bar
);
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            q     <= 1'b0;
            q_bar <= 1'b1;
        end else begin
            case ({s, r})
                2'b00: q <= q;         // No change
                2'b01: q <= 1'b0;      // Reset
                2'b10: q <= 1'b1;      // Set
                2'b11: q <= 1'bx;      // Invalid / indeterminate
            endcase
            q_bar <= ~q;
        end
    end
endmodule

// (b) JK Flip-Flop
module jk_ff (
    input clk, rst, j, k,
    output reg q, q_bar
);
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            q     <= 1'b0;
            q_bar <= 1'b1;
        end else begin
            case ({j, k})
                2'b00: q <= q;         // Hold
                2'b01: q <= 1'b0;      // Reset
                2'b10: q <= 1'b1;      // Set
                2'b11: q <= ~q;        // Toggle
            endcase
            q_bar <= ~q;
        end
    end
endmodule
```

---

### Question 8 (12 Marks) [Direct from Group Activity Images]
**Write gate-level Verilog code for:**  
**(a) Circuit 1 (NAND-XOR-NOT network with inputs $a_0, b_0, a_1, b_1$ and outputs $z_0, z_1$).**  
**(b) Circuit 2 (XOR-AND-OR network with inputs $a, b, c, d$ and output $y$).**

**Solution**:
#### (a) Circuit 1 (`image1.png`):
```verilog
module circuit_activity_a (
    input a0, b0, a1, b1,
    output z0, z1
);
    wire n1, n2, n3, n4, n5, n6;

    // First layer: 4 NAND gates
    nand G1 (n1, a0, b0);
    nand G2 (n2, a1, b1);
    nand G3 (n3, a1, b0);
    nand G4 (n4, a0, b1);

    // Middle layer: Inverter and XOR gate
    not G8 (n5, n2);
    xor G5 (n6, n3, n4);

    // Output layer: 2 XOR gates
    xor G6 (z0, n1, n2);
    xor G7 (z1, n5, n6);
endmodule
```

#### (b) Circuit 2 (`image2.png`):
```verilog
module circuit_activity_b (
    input a, b, c, d,
    output y
);
    wire w1, w2, w3;

    // XOR gate x1
    xor x1 (w1, b, c);

    // AND gates a1 and a2
    and a1 (w2, a, w1);
    and a2 (w3, w1, d);

    // Output OR gate o1
    or o1 (y, w2, w3);
endmodule
```

