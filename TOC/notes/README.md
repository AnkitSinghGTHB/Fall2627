# 🎯 TOC — Theory of Computation

> **The "just tell me what I need to know to ace this" edition**
>
> TOC sounds scary. It's not. It's pattern recognition — draw the machine, trace the string, follow the rules. That's 90% of the exam.

---

## 📚 How to Use These Notes

1. **Read in order** — later modules build on earlier ones heavily
2. **Draw the diagrams yourself** — TOC is visual, you MUST draw the automata by hand
3. **Check the TL;DR** at the top — if you know it, skip it
4. **Use the Cheatsheets** the night before — they're designed for last-minute revision

---

## 🗺️ Module 1 — Map

| # | Topic | File | Time | Difficulty |
|---|-------|------|:---:|:---:|
| 1 | **What is TOC? (The Big Picture)** | [01-what-is-toc.md](./01-what-is-toc.md) | ☕ 5 min | 🟢 Easy |
| 2 | **Alphabets, Strings & Languages** | [02-alphabets-strings-languages.md](./02-alphabets-strings-languages.md) | ☕☕ 10 min | 🟢 Easy |
| 3 | **Grammars & Derivations** | [03-grammars-and-derivations.md](./03-grammars-and-derivations.md) | ☕☕ 15 min | 🟡 Medium |
| 4 | **Finite Automata (DFA)** | [04-dfa.md](./04-dfa.md) | ☕☕☕ 20 min | 🟡 Medium |
| 5 | **NFA & ε-NFA** | [05-nfa.md](./05-nfa.md) | ☕☕☕ 20 min | 🟡 Medium |
| 6 | **Regular Expressions** | [06-regular-expressions.md](./06-regular-expressions.md) | ☕☕☕ 20 min | 🟡 Medium |
| 7 | **Regular Grammars & Compiler Intro** | [07-regular-grammars-and-compilers.md](./07-regular-grammars-and-compilers.md) | ☕☕ 15 min | 🟡 Medium |

### 📄 Cheatsheets

| Covers | File |
|--------|------|
| Module 1 — Everything in one page | [cheatsheet-module1.md](./cheatsheet-module1.md) |

---

## 🧠 What You're Actually Learning

```
TOC = Theory of Computation

Three pillars:
┌─────────────────┐  ┌──────────────────┐  ┌───────────────┐
│ Automata Theory │  │ Computability    │  │ Complexity    │
│ "What machines  │  │ "Can this be     │  │ "How hard is  │
│  exist?"        │  │  solved at all?" │  │  this problem?"│
└────────┬────────┘  └────────┬─────────┘  └───────┬───────┘
         │                    │                     │
    Module 1 focus       Mentioned briefly     P vs NP stuff
    (DFA, NFA, RE)       (halting problem)     (mentioned)
```

---

## 💡 Study Strategy for TOC

### The 80/20 Rule:
- **50%** = DFA/NFA construction + string tracing (draw it → trace it → done)
- **25%** = Regular expressions ↔ Automata conversion (mechanical process)
- **15%** = Grammars (follow the production rules)
- **10%** = Theory questions (definitions, Chomsky hierarchy — memorize)

### Time Budget per Week:
- 🎯 **2 hours** = Read the notes
- 🎯 **1.5 hours** = Practice drawing DFAs/NFAs by hand (this is NON-NEGOTIABLE)
- 🎯 **30 min** = Review cheatsheet

---

## ⚠️ The #1 Mistake in TOC

> Students try to "understand the theory" without drawing. **TOC is a drawing subject.** If you're not sketching automata on paper, you're studying it wrong.

---

*Made with ❤️ by a friend who wants you to clear this without pain.*
