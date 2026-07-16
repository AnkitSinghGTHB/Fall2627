# 🧠 Lesson 1 — What is Theory of Computation?

> **TL;DR**: TOC asks "what can computers solve, and how efficiently?" It has 3 branches — Automata (machines), Computability (solvable or not?), Complexity (easy or hard?). For this course, you mostly care about **Automata Theory**.

---

## 🤔 What is "Computation"?

Computation = any information processing that can be described as a step-by-step procedure (algorithm).

**Examples you already know:**
- Adding two numbers (mentally, on paper, or on a calculator)
- Converting decimal to binary
- Finding GCD of two numbers
- Sorting a list

If you can write steps for it → it's computation.

---

## 👤 Alan Turing — The Guy Behind It All

- English mathematician (1912–1954)
- **Father of Modern Computer Science**
- Created the concept of "Turing Machines" *before actual computers existed*
- Asked the big question: **"Can all math problems be solved by a machine?"**
- Answer: **No.** Some problems are unsolvable (e.g., the Halting Problem)

---

## 🏗️ Three Pillars of TOC

| Branch | The Question It Asks | Example |
|--------|---------------------|---------|
| **Automata Theory** | What types of abstract machines exist? | DFA, NFA, PDA, Turing Machine |
| **Computability Theory** | Can this problem be solved at all? | Halting problem = unsolvable |
| **Complexity Theory** | How hard/expensive is this to solve? | P vs NP |

### For this course, focus on: **Automata Theory** (90% of your exam)

---

## 🤖 Types of Automata (The Machine Hierarchy)

```
Power Level:     LOW ◄──────────────────────────────► HIGH

┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│    Finite     │  │   Pushdown   │  │    Turing     │
│   Automaton   │  │   Automaton  │  │   Machine     │
│   (FA/FSM)    │  │    (PDA)     │  │    (TM)       │
├──────────────┤  ├──────────────┤  ├──────────────┤
│ Memory: NONE  │  │ Memory: STACK│  │ Memory: RAM   │
│ Example:      │  │ Example:     │  │ Example:      │
│  Vending      │  │  Compilers   │  │  Any          │
│  machine,     │  │  (parsers)   │  │  algorithm    │
│  elevator     │  │              │  │              │
└──────────────┘  └──────────────┘  └──────────────┘
   Simple              Medium           Most powerful
   problems            problems         problems
```

> 💡 **Key insight**: More memory = can solve harder problems. FA has no memory, PDA has a stack, TM has unlimited memory.

---

## 🏛️ The Chomsky Hierarchy

This classifies languages by how "powerful" a machine you need to recognize them:

```
┌─────────────────────────────────────────┐
│        Recursively Enumerable           │  ← Turing Machine
│    ┌────────────────────────────────┐   │
│    │       Context-Sensitive        │   │  ← Linear Bounded Automaton
│    │   ┌────────────────────────┐   │   │
│    │   │     Context-Free       │   │   │  ← Pushdown Automaton
│    │   │  ┌─────────────────┐   │   │   │
│    │   │  │    Regular      │   │   │   │  ← Finite Automaton
│    │   │  └─────────────────┘   │   │   │
│    │   └────────────────────────┘   │   │
│    └────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

> **For Module 1**: You only need to care about the **Regular** circle (Finite Automata, Regular Expressions, Regular Grammars).

---

## 📌 P vs NP (Just Know This for Theory Questions)

| Class | Meaning | Example |
|-------|---------|---------|
| **P** | Problems solvable in **polynomial** time | Sorting, searching |
| **NP** | Problems whose solutions can be **verified** in polynomial time | Sudoku, traveling salesman |
| **NP-Hard** | At least as hard as the hardest NP problems | No efficient algorithm known |

> The million-dollar question: **Does P = NP?** Nobody knows. (Literally worth $1 million — Google "Millennium Prize")

---

## ✅ Quick Self-Check (30 seconds)

1. What are the 3 branches of TOC?
2. Who is the "father of computer science"?
3. Which automaton has no memory at all?
4. Which is more powerful — PDA or FA?
5. What's the Halting Problem in one sentence?

<details>
<summary>🔑 Answers</summary>

1. Automata Theory, Computability Theory, Complexity Theory
2. Alan Turing
3. Finite Automaton (FA)
4. PDA (it has a stack)
5. "You can't write a program that determines whether ANY given program will eventually halt or run forever"

</details>

---

**⏱️ Time spent: ~5 min. Next →** [02 - Alphabets, Strings & Languages](./02-alphabets-strings-languages.md)
