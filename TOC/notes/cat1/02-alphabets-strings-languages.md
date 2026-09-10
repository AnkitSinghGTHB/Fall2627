# 🔤 Lesson 2 — Alphabets, Strings & Languages

> **TL;DR**: Alphabet = a set of symbols. String = symbols in a row. Language = a set of strings that follow some rule. These 3 definitions are the foundation of EVERYTHING in TOC.

---

## 📌 The Three Building Blocks

| Concept | What it is | Notation | Example |
|---------|-----------|:---:|---------|
| **Symbol** | A single character/element | — | `a`, `b`, `0`, `1`, `#` |
| **Alphabet** | A finite set of symbols | **Σ** (sigma) | Σ = {0, 1} |
| **String** | A sequence of symbols from Σ | **w** | w = `01011` |
| **Language** | A set of strings that follow a rule | **L** | L = {0ⁿ1ⁿ : n ≥ 0} |

---

## 1️⃣ Alphabet (Σ)

A **finite, non-empty set** of symbols.

```
Σ = {0, 1}              ← Binary alphabet
Σ = {a, b, c, ..., z}   ← English lowercase
Σ = {a, c, g, t}        ← DNA alphabet
Σ = {0, 1, ..., 9}      ← Decimal digits
```

---

## 2️⃣ Strings

A **finite sequence** of symbols from Σ.

### Key Terms

| Term | Symbol | Meaning | Example (Σ = {a, b}) |
|------|:---:|---------|---------|
| **String** | w | A sequence of symbols | w = `abba` |
| **Empty string** | **ε** (epsilon) | String with zero symbols | ε (length = 0) |
| **Length** | \|w\| | Number of symbols in w | \|`abba`\| = 4 |

### String Operations

#### Concatenation — glue two strings together
```
x = "abc",  y = "de"
xy = "abcde"
|xy| = |x| + |y| = 3 + 2 = 5
```

> **Special case**: xε = εx = x (concatenating empty string changes nothing)

#### Reverse — flip the string
```
w = "abcd"
wᴿ = "dcba"

|w| = |wᴿ|  (length stays the same)
```

#### Substring — any consecutive chunk
```
w = "string"

Prefixes: ε, s, st, str, stri, strin, string
Suffixes: ε, g, ng, ing, ring, tring, string
Substrings: s, st, tr, ri, in, ng, str, tri, rin, ...
```

---

## 3️⃣ Powers of an Alphabet (Σᵏ)

Σᵏ = the set of **all strings of length k** from alphabet Σ.

```
Σ = {0, 1}

Σ⁰ = {ε}                           (only the empty string)
Σ¹ = {0, 1}                        (all length-1 strings)
Σ² = {00, 01, 10, 11}              (all length-2 strings)
Σ³ = {000, 001, 010, 011, 100, 101, 110, 111}
```

### Kleene Star (Σ*) and Kleene Plus (Σ⁺)

| Notation | Meaning |
|:---:|---------|
| **Σ\*** | ALL strings of ALL lengths (including ε) = Σ⁰ ∪ Σ¹ ∪ Σ² ∪ ... |
| **Σ⁺** | ALL strings of ALL lengths (EXCLUDING ε) = Σ¹ ∪ Σ² ∪ Σ³ ∪ ... |

```
Σ⁺ = Σ* − {ε}
```

> 🧠 **Memory trick**: Star (*) includes **ε**verything including empty. Plus (+) means "at least one symbol."

---

## 4️⃣ Languages

A **language** L over alphabet Σ is **any subset of Σ\***.

### Examples

```
Σ = {0, 1}

L₁ = {ε, 01, 0011, 000111, ...}     = {0ⁿ1ⁿ : n ≥ 0}
L₂ = {0, 1, 00, 11, 010, 101, ...}  = all palindromes
L₃ = {ε}                             = language with only empty string
L₄ = ∅                               = empty language (NO strings)
```

> ⚠️ **Tricky distinction**: `{ε}` ≠ `∅`
> - `{ε}` has ONE element (the empty string)
> - `∅` has ZERO elements (nothing at all)

---

## 5️⃣ Operations on Languages

| Operation | Symbol | What it does | Example |
|-----------|:---:|---|---|
| **Union** | L₁ ∪ L₂ | Strings in L₁ OR L₂ | {0,1} ∪ {111} = {0, 1, 111} |
| **Intersection** | L₁ ∩ L₂ | Strings in BOTH | — |
| **Concatenation** | L₁·L₂ | Take one from L₁, one from L₂, glue them | {0,1}·{ε,010} = {0, 1, 0010, 1010} |
| **Set Difference** | L₁ − L₂ | In L₁ but NOT in L₂ | — |
| **Complement** | Lᶜ | Everything in Σ* that's NOT in L | Lᶜ = Σ* − L |
| **Kleene Star** | L* | Concatenate 0 or more strings from L | {0,10}* = {ε, 0, 10, 00, 010, ...} |
| **Reverse** | Lᴿ | Reverse every string in L | — |

### Kleene Star of a Language — Example

```
L = {0, 10}

L⁰ = {ε}
L¹ = {0, 10}
L² = {00, 010, 100, 1010}
L³ = {000, 0010, 0100, 01010, 1000, 10010, 10100, 101010}
...
L* = L⁰ ∪ L¹ ∪ L² ∪ L³ ∪ ...   (infinite set)
```

---

## ✅ Quick Self-Check (1 minute)

1. What's the difference between Σ* and Σ⁺?
2. If Σ = {a, b}, how many strings are in Σ²?
3. Is {ε} the same as ∅?
4. What is |`abcde`|?
5. What's the reverse of `10110`?
6. If L = {a, b} and M = {c}, what is L·M?

<details>
<summary>🔑 Answers</summary>

1. Σ* includes ε (the empty string), Σ⁺ does not
2. 4 strings: {aa, ab, ba, bb}
3. **No!** {ε} has one element, ∅ has zero elements
4. 5
5. `01101`
6. {ac, bc}

</details>

---

**⏱️ Time spent: ~10 min. Next →** [03 - Grammars & Derivations](./03-grammars-and-derivations.md)
