# 🏆 TOC & Compiler Design (CSE2004) — Term End FAT Survival & S-Grade Guide

> **Faculty**: Dr. Gaurav Soni  
> **Course**: CSE2004 — Theory of Computation and Compiler Design (4 Credits)  
> **Exam Date**: October 13–21, 2026 (FAT / TEE)  
> **Target**: 80+/100 in FAT to secure an **A or S Grade**

---

## 🔍 The CAT-2 Post-Mortem: Why You Got 28 While 12 People Got 50/50

You studied hard for CAT-2, but only got **28/50**, while 12 people scored **50/50** and the class average rose to ~37. 

**Here is the exact reason why:**  
Dr. Gaurav Soni is an ultra-rigid, formalist evaluator. In TOC, he **does not award marks for correct logic if it lacks formal syntactic presentation**. 

Students who got 28 simply drew a state diagram and hoped the faculty would trace it.  
Students who got 50 wrote their answers following a **strict 6-part university template**:

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│       DR. GAURAV SONI'S MANDATORY 6-PART AUTOMATA / TM RUBRIC                │
├──────────────────────────────────────────────────────────────────────────────┤
│ 1. Language Description    : Exact mathematical set definition.            │
│ 2. Design Logic (Strategy) : Plain-English algorithm explaining the tape head│
│                              or stack behavior step by step.                 │
│ 3. Formal Tuples           : Explicitly defining Q, Σ, Γ, δ, q₀, B, F       │
│                              (every single set enumerated!).                 │
│ 4. Transition Table        : Complete matrix of δ(state, symbol).           │
│ 5. State Transition Diagram: Clean circles, start arrow, double-circle final.│
│ 6. Validation (ID Tracing) : Formal Instantaneous Description (⊢) trace on a  │
│                              sample valid string and invalid string.         │
└──────────────────────────────────────────────────────────────────────────────┘
```

If you miss *even one* of these 6 components (e.g. you skip the transition table or the $\vdash$ validation trace), he immediately chops **4 to 5 marks per question**. Over a 50-mark paper, that is how a 50 becomes a 28!

---

## 📊 Relative Grading Reality in TOC (CSE2004)

Let's look at your actual standing in TOC:

| Assessment | Your Score | Class Average | Standing |
| :--- | :---: | :---: | :---: |
| **CAT-1** ($\times 0.30$) | $31 \times 0.30 = 9.3$ | $30 \times 0.30 = 9.0$ | $+0.3$ |
| **CAT-2** ($\times 0.30$) | $28 \times 0.30 = 8.4$ | $34 \times 0.30 = 10.2$ | $-1.8$ |
| **Internals** | $\approx 32.0$ | $\approx 32.0$ | $0.0$ |
| **Attendance** | $5.0$ | $5.0$ | $0.0$ |
| **Pre-TEE Total (out of 70)**| **$54.7 / 70$** | **$56.2 / 70$** | **$-1.5$ deficit** |

### The Good News:
Unlike Discrete (where you were $-8.1$ marks behind), in TOC you are **only $-1.5$ marks behind the class average**!
- In TEE (30% weightage), if you score **72–75 out of 100**, your total reaches **77+**, which comfortably puts you in the **A Grade band** ($\ge \mu + 0.5\sigma$).
- If you use Dr. Soni's 6-part template and score **85+**, you can even snatch an **S Grade**!

---

## 🗂️ Term End Notes Structure

1. **[`00-7-day-toc-emergency-plan.md`](./00-7-day-toc-emergency-plan.md)**: Day-by-day 1.5-hour study checklist for Oct 6–12.
2. **[`01-module1-finite-automata-and-minimization.md`](./01-module1-finite-automata-and-minimization.md)**: DFA/NFA design, Table-Filling Minimization, Pumping Lemma for Regular Languages, and LEX.
3. **[`02-module2-cfg-cnf-and-pda.md`](./02-module2-cfg-cnf-and-pda.md)**: Ambiguity proofs (2 trees), CNF 4-step conversion, PDA 7-tuple design with $\vdash$ IDs.
4. **[`03-module3-parsing-ll1-slr-clr-lalr.md`](./03-module3-parsing-ll1-slr-clr-lalr.md)**: FIRST/FOLLOW computation, LL(1) table, SLR(1) items + Shift-Reduce conflicts, CLR(1)/LALR(1) Reduce-Reduce conflicts.
5. **[`04-module4-turing-machines-and-undecidability.md`](./04-module4-turing-machines-and-undecidability.md)**: The 6-part mandatory TM format, solved TMs ($a^n b^n c^n$, even/odd, etc.), Chomsky Hierarchy, and Halting Problem.
6. **[`05-module5-intermediate-code-and-optimization.md`](./05-module5-intermediate-code-and-optimization.md)**: Three Address Code (Quadruples/Triples), Basic Blocks & Flow Graphs, and Code Optimization techniques.
7. **[`06-toc-master-formula-sheet.md`](./06-toc-master-formula-sheet.md)**: 1-page quick formula & tuple lookup.
8. **[`07-toc-fat-high-frequency-exam-question-bank.md`](./07-toc-fat-high-frequency-exam-question-bank.md)**: 15 past university questions solved in Dr. Soni's exact 100% full-mark layout.
