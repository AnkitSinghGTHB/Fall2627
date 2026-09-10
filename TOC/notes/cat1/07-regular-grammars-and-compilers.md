# 📐 Lesson 7 — Regular Grammars & Intro to Compilers

> **TL;DR**: Regular grammars are grammars where every rule has at most one variable, and it sits on the right end (right-linear) or left end (left-linear). They generate exactly the Regular Languages. The compiler section is mostly definitions — memorize the 6 phases.

---

## Part A: Regular Grammars

### What Makes a Grammar "Regular"?

A regular grammar = a grammar where **every production rule** has one of these forms:

#### Right-Linear Grammar
```
A → xB     (terminal string followed by ONE variable)
A → x      (just a terminal string, no variable)
```

#### Left-Linear Grammar
```
A → Bx     (ONE variable followed by terminal string)
A → x      (just a terminal string)
```

Where `x ∈ T*` (a string of terminals, possibly empty) and A, B are variables.

> ⚠️ A grammar is regular if it's **entirely** right-linear **OR entirely** left-linear. **Don't mix them!**

---

### Examples

#### Right-Linear ✅
```
S → abS | a

Derivation: S → abS → ababS → ababa
Language: L(G) = (ab)*a
```

#### Left-Linear ✅
```
S → Sab | Aab
A → Bb | a
B → a
```

#### NOT Regular ❌
```
S → aSb | ε        ← variable on BOTH sides of terminals
```
This generates {aⁿbⁿ : n ≥ 0} which is **not regular** (it's context-free).

---

### The Big Theorem

> **Regular Grammars ≡ Finite Automata ≡ Regular Expressions**
>
> All three describe **exactly the same** set of languages.

```
                Regular Grammar
                   ↗        ↘
        generates      equivalent to
              ↗              ↘
    Regular Language    Regular Language
              ↖              ↙
        accepts        describes
                   ↖        ↙
              DFA/NFA ←→ Regex
```

---

### Converting Between Them

#### Right-Linear Grammar → NFA

| Grammar Element | NFA Element |
|---|---|
| Each variable → a **state** | V₀, V₁, ... → q₀, q₁, ... |
| Start symbol S → **start state** | |
| Production `A → aB` → **transition** | δ(A, a) includes B |
| Production `A → a` → **transition to final state** | δ(A, a) includes F |
| Add a special **final state** F | |

**Example:**
```
Grammar:  S → aA | B        NFA:
          A → aaB
          B → bB | a             S ──a──→ A ──a──→ (intermediate) ──a──→ B
                                 S ──ε──→ B
                                 B ──b──→ B
                                 B ──a──→ F(accept)
```

#### NFA → Right-Linear Grammar

For every transition `δ(q, a) = p`, add production: `q → ap`
For every final state `qf`, add production: `qf → ε`

---

## Part B: Intro to Compilers (Just the Definitions)

> This section is mostly **memorization**. Know the 6 phases and what each does.

### What is a Compiler?

A compiler **translates** source code (e.g., C, Java) into target code (e.g., machine code).

```
Source Program → [ COMPILER ] → Target Program
                      ↓
                Error Messages
```

### Two Major Parts

| Part | Name | What it does |
|:---:|------|---|
| **Front End** | Analysis | Breaks down source code, checks for errors |
| **Back End** | Synthesis | Builds the target program from intermediate form |

### The 6 Phases of a Compiler

```
Source Code
    ↓
┌─────────────────────────┐
│ 1. Lexical Analyzer     │  → Breaks code into tokens
│    (Scanner)            │     e.g., "int x = 5;" → [int][x][=][5][;]
├─────────────────────────┤
│ 2. Syntax Analyzer      │  → Checks grammar, builds parse tree
│    (Parser)             │     Uses CFG rules
├─────────────────────────┤
│ 3. Semantic Analyzer    │  → Checks types, meaning
│                         │     e.g., can't add int + string
├─────────────────────────┤
│ 4. Intermediate Code    │  → Converts to machine-independent code
│    Generator            │     e.g., three-address code
├─────────────────────────┤
│ 5. Code Optimizer       │  → Makes intermediate code faster
│                         │     e.g., removes redundant operations
├─────────────────────────┤
│ 6. Code Generator       │  → Produces final machine code
│                         │     (architecture-specific)
└─────────────────────────┘
    ↓
Target Code
```

### Key Terms

| Term | Meaning |
|------|---------|
| **Token** | Smallest meaningful unit (keyword, identifier, operator) |
| **Parse Tree** | Tree showing the grammatical structure |
| **Symbol Table** | Database of all identifiers and their info |
| **Interpreter** | Executes source code directly (no target code produced) |
| **Bootstrapping** | Writing a compiler in the same language it compiles |

### The Connection to TOC

| Compiler Phase | TOC Concept Used |
|---|---|
| Lexical Analyzer (Scanner) | **DFA / Finite Automata** ← THIS IS WHY YOU LEARN FA |
| Syntax Analyzer (Parser) | **CFG / Pushdown Automata** |
| Semantic Analyzer | Type systems |

> 💡 **This is why TOC exists** — the entire front end of a compiler is built on automata theory and formal grammars!

---

## ✅ Quick Self-Check

1. What's the difference between right-linear and left-linear grammars?
2. Can you mix right-linear and left-linear rules in a regular grammar?
3. Name the 6 phases of a compiler in order
4. Which compiler phase uses DFA?
5. What does a parser build?

<details>
<summary>🔑 Answers</summary>

1. Right-linear: variable on the RIGHT (A → xB). Left-linear: variable on the LEFT (A → Bx)
2. **No!** A regular grammar must be entirely one or the other
3. Lexical Analysis → Syntax Analysis → Semantic Analysis → Intermediate Code Gen → Code Optimization → Code Generation
4. **Lexical Analyzer** (Scanner)
5. A **parse tree** (showing the grammatical structure of the code)

</details>

---

**⏱️ Time spent: ~15 min. Module 1 complete! 🎉**

---

*You now know the entire Module 1 of TOC. The key to acing this: draw DFAs/NFAs by hand until it's muscle memory. Everything else is definitions + procedures.*
