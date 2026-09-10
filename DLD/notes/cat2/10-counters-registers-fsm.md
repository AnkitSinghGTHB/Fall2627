# ⏱️ Lesson 10 — Registers, Counters & Finite State Machines

> **TL;DR**: Chain flip-flops together and you get **Registers** (stores multiple bits) and **Counters** (counts clock pulses). Counters are just "automated binary odometers." FSMs (Mealy/Moore machines) are pattern detectors — they watch a stream of bits and yell "FOUND IT!" when they spot a target sequence.

---

## 📻 Shift Registers — Just Flip-Flops Holding Hands

Imagine a line of students passing a note. Each student = 1 flip-flop. Each "pass" = 1 clock tick.

| Type | How data goes IN | How data comes OUT | Real-life analogy |
|---|---|---|---|
| **SISO** | One bit at a time | One bit at a time | Passing a note down a row |
| **SIPO** | One bit at a time | All bits at once | Loading a clip, then firing all at once |
| **PISO** | All bits at once | One bit at a time | Taking a group photo, then sending pixels one by one |
| **PIPO** | All bits at once | All bits at once | Copy-paste (instant transfer) |

> 🧠 **Memory Trick**: S = Serial (one at a time), P = Parallel (all at once). Just read the letters!

---

## 🔢 Counters — Binary Odometers

A counter is just a chain of T flip-flops (toggle flip-flops) that counts clock pulses in binary.

### Two Types:

| | Ripple (Asynchronous) | Synchronous |
|---|---|---|
| **Clock connection** | Only first FF gets the clock; each FF triggers the next | ALL FFs get the clock simultaneously |
| **Speed** | Slower (delay accumulates) | Faster (no delay buildup) |
| **Analogy** | Dominoes falling one by one | Everyone jumping at the same time |

### MOD-N Counters

A MOD-N counter counts from $0$ to $N-1$ and then resets. To find how many flip-flops you need:

$$\text{Number of FFs} = \lceil \log_2 N \rceil$$

> 🎯 **Exam shortcut**: Just find the smallest power of 2 that's $\ge N$.
> - MOD-10 → $2^4 = 16 \ge 10$ → **4 flip-flops**
> - MOD-6 → $2^3 = 8 \ge 6$ → **3 flip-flops**

---

## 🏋️ Solved Exam Practice Questions

### Question 1 (This Appears Every Single Exam)
**How many flip-flops for a MOD-12 counter?**

<details>
<summary>💡 Solution</summary>

$2^3 = 8 < 12$, but $2^4 = 16 \ge 12$.
**Answer**: 4 flip-flops. ✅
</details>

### Question 2 (Register Types)
**Name the shift register type where data enters serially and comes out in parallel.**

<details>
<summary>💡 Solution</summary>

**SIPO** — Serial-In Parallel-Out. ✅
</details>

---

## ✅ Quick Self-Check (30 seconds)

1. What does PISO stand for?
2. Why are synchronous counters faster than ripple counters?
3. How many FFs for MOD-5?

<details>
<summary>🔑 Answers</summary>

1. Parallel-In Serial-Out.
2. Because all flip-flops get the clock at the same time (no domino delay).
3. $2^3 = 8 \ge 5$ → **3 flip-flops**.

</details>

---

**⏱️ Time spent: ~15 mins. Next →** [11 - Verilog HDL](./11-verilog-hdl.md)
