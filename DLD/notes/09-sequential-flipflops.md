# 🔄 Lesson 9 — Sequential Logic & Flip-Flops

> **TL;DR**: Combinational circuits forget everything the moment you change the input. Sequential circuits have **memory** — they remember the last state. Flip-flops are 1-bit memory cells, and there are only 4 types to learn: SR, D, JK, T. The JK is the "upgraded SR" and the T is just a "toggle switch."

---

## 💾 Latch vs Flip-Flop — The One Difference

| | Latch | Flip-Flop |
|---|---|---|
| **When does it update?** | Whenever the clock signal is HIGH (level) | Only on the clock **edge** (↑ or ↓) |
| **Analogy** | A door that's open as long as you push it | A turnstile that clicks once per push |

> 🎯 **Exam tip**: If they ask the difference — say "Latch = **level-triggered**, Flip-Flop = **edge-triggered**." That's the whole answer.

---

## 🔀 The 4 Flip-Flops (This is the Whole Chapter, Really)

### 1. SR Flip-Flop (Set-Reset) — The Basic One

| S | R | What happens | Output $Q_{n+1}$ |
|:---:|:---:|---|:---:|
| 0 | 0 | Nothing changes | $Q_n$ (hold) |
| 1 | 0 | SET (turn ON) | 1 |
| 0 | 1 | RESET (turn OFF) | 0 |
| 1 | 1 | ❌ INVALID! | 💀 Don't do this |

> 🤦 **Why is S=1, R=1 invalid?** Because you're telling it to turn ON and OFF at the same time. It's like pressing the gas and brake simultaneously — the circuit doesn't know what to do.

### 2. JK Flip-Flop — The "Fixed SR"

Same as SR, but when J=1 and K=1, it **toggles** instead of crashing:

| J | K | $Q_{n+1}$ |
|:---:|:---:|:---:|
| 0 | 0 | $Q_n$ (hold) |
| 1 | 0 | 1 (set) |
| 0 | 1 | 0 (reset) |
| 1 | 1 | $\overline{Q}_n$ (**toggle**) |

**Characteristic Equation**: $Q_{n+1} = J\overline{Q}_n + \overline{K}Q_n$

> 🧠 **Memory Trick**: "JK = SR but smarter." J=Set, K=Reset, both=Toggle.

### 3. D Flip-Flop (Data/Delay) — The Simplest

Output just copies the input on the clock edge. That's it!
- $Q_{n+1} = D$

> Think of it as a **sticky note**: whatever you write ($D$) gets saved ($Q$) when the clock ticks.

### 4. T Flip-Flop (Toggle) — The Light Switch

| T | $Q_{n+1}$ |
|:---:|:---:|
| 0 | $Q_n$ (no change) |
| 1 | $\overline{Q}_n$ (flip!) |

**Characteristic Equation**: $Q_{n+1} = T \oplus Q_n$

> Think of a **light switch**: press once ($T=1$) → it flips. Don't press ($T=0$) → stays the same.

---

## 🏋️ Solved Exam Practice Questions

### Question 1 (Conversion — Appears Every Exam)
**Convert a JK Flip-Flop into a D Flip-Flop.**

<details>
<summary>💡 Step-by-Step Solution</summary>

We want: $Q_{n+1} = D$ (that's what a D flip-flop does).

JK equation: $Q_{n+1} = J\overline{Q}_n + \overline{K}Q_n$

**The trick**: Set $J = D$ and $K = \overline{D}$. Then:
$$Q_{n+1} = D\overline{Q}_n + \overline{(\overline{D})}Q_n = D\overline{Q}_n + DQ_n = D(\overline{Q}_n + Q_n) = D$$

**Answer**: Connect $J = D$ and $K = \text{NOT}(D)$. Done! ✅

</details>

---

## ✅ Quick Self-Check (30 seconds)

1. What's the difference between a latch and a flip-flop? (ONE line)
2. What happens when J=1, K=1?
3. A T flip-flop with T=1 does what?

<details>
<summary>🔑 Answers</summary>

1. Latch = level-triggered, Flip-Flop = edge-triggered.
2. It **toggles** (flips the output).
3. Toggles (switches from 0→1 or 1→0).

</details>

---

**⏱️ Time spent: ~15 mins. Next →** [10 - Counters & FSMs](./10-counters-registers-fsm.md)
