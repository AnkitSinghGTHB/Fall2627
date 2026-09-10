# ⚡ Lesson 6 — Boolean Algebra, Logic Gates & Logic Families

> **TL;DR**: Boolean algebra is just math with only two numbers: 0 and 1. Logic gates are the tiny switches that actually *do* this math inside your computer. NAND and NOR are called **Universal Gates** because you can build literally ANY circuit using just one of them. That's it. That's the whole subject.

---

## 📐 The Laws You Need to Memorize (Sorry, No Way Around This)

Think of these like math identities — except way easier because there's only 0 and 1:

| Law | AND Version (·) | OR Version (+) |
|---|---|---|
| **Identity** | $A \cdot 1 = A$ | $A + 0 = A$ |
| **Null** | $A \cdot 0 = 0$ | $A + 1 = 1$ |
| **Idempotent** | $A \cdot A = A$ | $A + A = A$ |
| **Complement** | $A \cdot \overline{A} = 0$ | $A + \overline{A} = 1$ |
| **De Morgan's** | $\overline{A \cdot B} = \overline{A} + \overline{B}$ | $\overline{A + B} = \overline{A} \cdot \overline{B}$ |
| **Absorption** | $A + AB = A$ | $A(A + B) = A$ |

> 🧠 **Memory Trick for De Morgan's**: "Break the bar, change the sign." When you break the NOT bar over a group, AND becomes OR and OR becomes AND. Every. Single. Time.

> 🤦 **Common Exam Mistake**: Students forget Absorption. If you see $A + AB$, the answer is just $A$. Don't expand it — simplify it!

---

## 🚪 Logic Gates — The 7 Building Blocks

Think of gates like bouncers at a club. They check your inputs and decide if you're in (1) or out (0):

| Gate | What it does | One-liner to remember |
|:---:|---|---|
| **AND** | $Y = A \cdot B$ | "Both must be 1" — strict bouncer |
| **OR** | $Y = A + B$ | "Either one works" — chill bouncer |
| **NOT** | $Y = \overline{A}$ | "Whatever you say, I say the opposite" |
| **NAND** | $Y = \overline{A \cdot B}$ | AND + NOT = "I reject perfection" |
| **NOR** | $Y = \overline{A + B}$ | OR + NOT = "I reject everyone" |
| **XOR** | $Y = A \oplus B$ | "Only if you're different" — the hipster |
| **XNOR** | $Y = \overline{A \oplus B}$ | "Only if you're the same" — the conformist |

> 💡 **Why NAND & NOR are called Universal**: Because any gate (AND, OR, NOT, XOR... anything) can be built using ONLY NAND gates or ONLY NOR gates. It's like saying "give me enough LEGO bricks of one type and I'll build the whole city."

---

## 🏭 Logic Families — Just Memorize This Table

This is a 2-mark theory question. Don't overthink it:

| Family | Made Of | Speed | Power | Used In |
|---|---|:---:|:---:|---|
| **TTL** | Bipolar Transistors | Fast | Medium | Old-school 5V circuits |
| **CMOS** | MOSFETs | Fast | **Super Low** | Your phone, laptop, EVERYTHING modern |
| **ECL** | Non-saturating BJTs | **Fastest** | High | Supercomputers, radar |

> 🎯 **Exam tip**: If they ask "which family dominates modern electronics?" → **CMOS**. Always.

---

## 🏋️ Solved Exam Practice Questions

### Question 1 (De Morgan's Simplification — This Type ALWAYS Appears)
**Simplify: $F = \overline{\overline{A} \cdot B + A \cdot \overline{B}}$**

<details>
<summary>💡 Step-by-Step Solution</summary>

The expression inside the outer bar is actually XOR ($A \oplus B = \overline{A}B + A\overline{B}$).

So we're finding $\overline{\text{XOR}} = \text{XNOR}$.

Let's prove it step by step:
1. Apply De Morgan's: $\overline{X + Y} = \overline{X} \cdot \overline{Y}$
   $$F = \overline{(\overline{A}B)} \cdot \overline{(A\overline{B})}$$
2. Apply De Morgan's again on each part:
   $$F = (A + \overline{B}) \cdot (\overline{A} + B)$$
3. FOIL it out:
   $$F = A\overline{A} + AB + \overline{A}\overline{B} + \overline{B}B$$
4. Cancel the contradictions ($A\overline{A} = 0$, $B\overline{B} = 0$):
   $$F = AB + \overline{A}\overline{B}$$

**Answer**: $F = AB + \overline{A}\overline{B}$ = **XNOR gate** ✅

</details>

---

## ✅ Quick Self-Check (30 seconds)

1. What does "break the bar, change the sign" refer to?
2. What is $A + AB$ simplified to?
3. Which logic family runs your phone?
4. Why is NAND called a universal gate?

<details>
<summary>🔑 Answers</summary>

1. **De Morgan's Law** — break the NOT bar, AND↔OR swap.
2. **$A$** (Absorption Law).
3. **CMOS**.
4. Because ANY other gate can be built using only NAND gates.

</details>

---

**⏱️ Time spent: ~15 mins. Next →** [07 - K-Maps](./07-kmap-minimization.md)
