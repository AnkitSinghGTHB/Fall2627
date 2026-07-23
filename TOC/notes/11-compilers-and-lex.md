# 💻 Lesson 11 — Compilers and the LEX Tool

> **TL;DR**: A compiler translates human-readable source code into machine code (0s and 1s). The **LEX** tool helps automate the very first step of this translation!

---

## 🏗️ The 6 Phases of a Compiler

Compilers are split into 6 distinct phases. They act like an assembly line, passing data structures (like the **Symbol Table** and **Syntax Tree**) down the line.

Here is the exact order:

1. **Lexical Analysis**: Reads characters and groups them into **Tokens** (e.g., `int`, `a`, `=`, `5`).
2. **Syntax Analysis (Parser)**: Checks if the tokens form a valid sentence using CFG rules (creates a Parse Tree).
3. **Semantic Analysis**: Checks if the sentence actually makes logical sense (e.g., Type checking - you can't add a `string` to an `int`).
4. **Intermediate Code Generation**: Translates into an easy-to-manipulate middle language (like 3-Address Code).
5. **Code Optimization**: Makes the code run faster and use less memory.
6. **Code Generation**: Translates into the final target Machine Language (e.g., `LOAD a`, `MOV B, A`).

> **💡 Exam Memorization Trick**: **L**et **S**tudents **S**ee **I**nside **C**ompiler **C**lasses (Lexical, Syntax, Semantic, Intermediate, Code Opt, Code Gen).

---

## 🔎 What is Lexical Analysis?

The Lexical Analyzer (or "Scanner") reads the raw input code character by character. 
It throws away spaces and comments, and groups the remaining characters into **Tokens**.

**Example:**
Code: `a[index] = 4 + 2`
Tokens: `a`, `[`, `index`, `]`, `=`, `4`, `+`, `2`

---

## 🛠️ The LEX Tool

**LEX** is a software tool that automatically generates a Lexical Analyzer for you, using Regular Expressions!

A LEX program file is always divided into **3 sections**, separated by `%%`:

```text
DECLARATIONS
(Include headers, define variables)
%%
RULES
(Regular expressions and what C code to run when they match)
%%
AUXILIARY ROUTINES
(Extra C functions like main())
```

### ⚔️ Conflict Resolution in LEX

What happens if a string matches two different rules in LEX?

1. **Longest Prefix Rule**: LEX always prefers the rule that matches the *longest* possible string.
   *(e.g., if you have `if` and `iffy`, it will match the whole word `iffy` rather than stopping at `if`)*.
2. **First Rule Priority**: If two rules match the exact same number of characters, LEX picks whichever rule was written **first** in the file.
