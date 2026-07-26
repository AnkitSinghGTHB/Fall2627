# ⚙️ Lesson 8 — Combinational Logic Circuits

> **TL;DR**: Combinational circuits are like vending machines — put in the right inputs, you always get the same output. No memory involved. This lesson covers: **Adders** (the math circuits), **MUX** (the channel selector), and **Decoders** (the address translator).

---

## ➕ Adders & Subtractors — The Calculator Inside Your CPU

### Half Adder: Adds 2 bits. That's it.
Think of it as the simplest possible calculator:

```
Inputs: A, B
Outputs: Sum = A XOR B      (the "ones" digit)
         Carry = A AND B     (the "tens" digit... err, twos digit)
```

### Full Adder: Adds 2 bits + a carry-in from the previous column
This is the one that actually matters — it's chained together to build 4-bit, 8-bit, 32-bit adders.

```
Inputs: A, B, Cin
Outputs: Sum = A ⊕ B ⊕ Cin
         Cout = AB + BCin + ACin   (majority function — carry if 2+ inputs are 1)
```

> 🧠 **Memory Trick**: A Full Adder = **2 Half Adders + 1 OR gate**. That's a guaranteed 2-mark question.

> 🤦 **Common Exam Mistake**: Writing $C_{out} = AB + C_{in}$ and forgetting the $BC_{in} + AC_{in}$ terms. The carry generates if ANY two inputs are 1, not just $A$ and $B$!

---

## 🔀 Multiplexer (MUX) — The TV Channel Selector

Imagine your TV remote with a channel selector. You have 100 channels (inputs) but your screen shows only 1 at a time (output). The channel number you press = the **select lines**.

- **4:1 MUX**: 4 data inputs ($I_0$ to $I_3$), 2 select lines ($S_1, S_0$), 1 output.
- **8:1 MUX**: 8 data inputs, 3 select lines, 1 output.

> 🎯 **Formula to remember**: An $N:1$ MUX needs $\log_2 N$ select lines. So 8:1 MUX → $\log_2 8 = 3$ select lines.

---

## 🔢 Decoder — The Address Translator

A Decoder takes an $n$-bit binary address and activates exactly ONE of $2^n$ output lines.

Think of it like a hotel: you type room number "101" (3-bit input) into the elevator, and it lights up ONLY the floor/room that matches. All other rooms stay dark.

- **3:8 Decoder**: 3 input lines → 8 output lines (only 1 is HIGH at any time).

> 🎯 **Exam tip**: Decoders are used in **memory address decoding** — this phrase appears in every exam.

---

## 🏋️ Solved Exam Practice Questions

### Question 1 (This Exact Question Appears Every Year)
**How many Half Adders and OR gates are needed to build a Full Adder?**

<details>
<summary>💡 Solution</summary>

**2 Half Adders + 1 OR gate.**
- HA₁: Computes $S_1 = A \oplus B$ and $C_1 = AB$.
- HA₂: Computes $\text{Sum} = S_1 \oplus C_{in}$ and $C_2 = S_1 \cdot C_{in}$.
- OR: $C_{out} = C_1 + C_2$. ✅
</details>

### Question 2 (MUX Select Lines)
**How many select lines does a 16:1 MUX need?**

<details>
<summary>💡 Solution</summary>

$\log_2 16 = 4$ select lines. That's it. ✅
</details>

---

## ✅ Quick Self-Check (30 seconds)

1. What's the difference between a Half Adder and a Full Adder?
2. How many select lines for an 8:1 MUX?
3. What does a Decoder do in one sentence?

<details>
<summary>🔑 Answers</summary>

1. Half Adder adds 2 bits. Full Adder adds 2 bits + a carry from the previous stage.
2. 3 select lines ($2^3 = 8$).
3. Converts an $n$-bit input code into one of $2^n$ active output lines.

</details>

---

**⏱️ Time spent: ~15 mins. Next →** [09 - Flip-Flops](./09-sequential-flipflops.md)
