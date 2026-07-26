# 💻 Lesson 11 — Verilog HDL (The Coding Part of DLD)

> **TL;DR**: Verilog is a programming language... but for hardware. Instead of telling a CPU what to compute, you're describing what *circuits* to build. There are 3 ways to write it: Gate-Level (draw the circuit in code), Dataflow (write equations), and Behavioral (write if-else like normal code). The exam tests syntax memorization — so this is basically rote learning.

---

## 🏗️ Every Verilog File Looks Like This

```verilog
module ModuleName (input a, input b, output y);
    // Your circuit description goes here
endmodule
```

That's it. Every. Single. Time. `module` → stuff → `endmodule`.

---

## 🎨 The 3 Modeling Styles (From Hardest to Easiest)

### Style 1: Gate-Level — "I'm Drawing the Circuit"
You literally type out which gates to use:

```verilog
module HalfAdder (input A, input B, output Sum, output Carry);
    xor g1 (Sum, A, B);    // XOR gate named g1
    and g2 (Carry, A, B);  // AND gate named g2
endmodule
```

> 🧠 **Pattern**: `gate_type name (output, input1, input2);` — output comes FIRST!

### Style 2: Dataflow — "I'm Writing the Equations"
Uses `assign` keyword — clean and simple:

```verilog
module HalfAdder (input A, input B, output Sum, output Carry);
    assign Sum = A ^ B;     // ^ means XOR
    assign Carry = A & B;   // & means AND
endmodule
```

### Style 3: Behavioral — "I'm Writing Normal Code"
Uses `always @(...)` blocks with `if-else`. Feels like writing Python/C:

```verilog
module FullAdder (input A, input B, input Cin, output reg Sum, output reg Cout);
    always @(A or B or Cin) begin
        {Cout, Sum} = A + B + Cin;   // {} is concatenation!
    end
endmodule
```

> 🤦 **THE #1 Exam Mistake**: If you assign a variable inside an `always` block, it MUST be declared as `reg`. Writing `output Y` instead of `output reg Y` = instant marks lost.

---

## 🧪 Testbenches — Testing Your Circuit

A testbench is a separate module with NO inputs/outputs. It just generates test signals:

```verilog
module tb_HalfAdder;
    reg A, B;              // inputs are reg (you control them)
    wire Sum, Carry;       // outputs are wire (circuit controls them)

    HalfAdder uut (.A(A), .B(B), .Sum(Sum), .Carry(Carry));

    initial begin
        A = 0; B = 0; #10;   // wait 10 time units
        A = 0; B = 1; #10;
        A = 1; B = 0; #10;
        A = 1; B = 1; #10;
        $finish;
    end
endmodule
```

> 🧠 **Memory Trick**: In testbenches: inputs = `reg` (you're the driver), outputs = `wire` (circuit drives them).

---

## 🏋️ Solved Exam Practice Questions

### Question 1 (Spot the Bug — Exam Classic)
**What's wrong with this 2:1 MUX code?**
```verilog
module Mux (input A, input B, input S, output Y);
    always @(A or B or S) begin
        if (S) Y = B;
        else Y = A;
    end
endmodule
```

<details>
<summary>💡 Solution</summary>

`Y` is assigned inside `always`, so it must be `output reg Y`.

**Fixed**: `module Mux (input A, input B, input S, output reg Y);` ✅

</details>

---

## ✅ Quick Self-Check (30 seconds)

1. What keyword is used in Dataflow modeling?
2. Variables inside `always` blocks must be what type?
3. In a testbench, are inputs `reg` or `wire`?

<details>
<summary>🔑 Answers</summary>

1. `assign`.
2. `reg`.
3. `reg` (because you're generating the test values yourself).

</details>

---

**⏱️ Time spent: ~15 mins. Practice →** [DLD Practice Worksheet](./dld-practice-worksheet.md)
