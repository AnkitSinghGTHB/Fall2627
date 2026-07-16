# ✳️ Lesson 6 — Regular Expressions

> **TL;DR**: A regular expression (RE) is a **pattern** that describes a set of strings. It's just another way of writing what a DFA/NFA accepts — but as text instead of a diagram. Three operators: union (+), concatenation (.), and star (*). Master these and you can describe any regular language.

---

## 🤔 What is a Regular Expression?

A regular expression is a **compact formula** that defines a language.

```
DFA/NFA → draws the language as a machine diagram
Grammar → writes rules to generate the language
Regex   → writes a formula that matches the language
```

All three describe **the same set of languages** = Regular Languages.

---

## 🧱 Building Blocks (Three Atomic Expressions)

| Expression | Language it represents |
|:---:|---|
| **∅** | The empty language {} (no strings) |
| **ε** | The language {ε} (only the empty string) |
| **a** (any symbol) | The language {a} (only the string "a") |

---

## 🔧 Three Operators

| Operator | Symbol | What it does | Example |
|----------|:---:|---|---|
| **Union** | + (or \|) | "OR" — strings from either side | a + b = {a, b} |
| **Concatenation** | . (or just write together) | "AND THEN" — glue strings | ab = {ab} |
| **Kleene Star** | * | "ZERO or MORE repeats" | a* = {ε, a, aa, aaa, ...} |

### Operator Precedence (like math!)

```
Highest:  * (star)           — like exponentiation
Middle:   . (concatenation)  — like multiplication
Lowest:   + (union)          — like addition

So:  a + b*c  means  a + ((b*)(c))  =  {a} ∪ {c, bc, bbc, bbbc, ...}
```

---

## 📖 Reading Regular Expressions — Examples

| Regex | Language | In words |
|-------|----------|----------|
| `a` | {a} | Just "a" |
| `a + b` | {a, b} | "a" or "b" |
| `ab` | {ab} | "a" followed by "b" |
| `a*` | {ε, a, aa, aaa, ...} | Zero or more a's |
| `a⁺` | {a, aa, aaa, ...} | One or more a's (no ε) |
| `(a + b)*` | {ε, a, b, aa, ab, ba, bb, ...} | Any string over {a,b} |
| `(a + b)*b` | {b, ab, bb, aab, ...} | Any string ending in b |
| `a*b*` | {ε, a, b, aa, ab, bb, aab, ...} | Some a's then some b's |
| `(ab)*` | {ε, ab, abab, ababab, ...} | Repetitions of "ab" |

> ⚠️ **Common mistake**: `a*b*` ≠ `(ab)*` ≠ `(a+b)*`
> - `a*b*` = a's then b's (e.g., "aaabb" ✅, "aba" ❌)
> - `(ab)*` = repeating "ab" blocks (e.g., "abab" ✅, "aabb" ❌)
> - `(a+b)*` = any mix of a's and b's (e.g., "aba" ✅, "aabb" ✅)

---

## 🎯 Writing Regex — Common Patterns

### "All strings over {a,b}"
```
(a + b)*
```

### "Strings ending in 'b'"
```
(a + b)*b
```

### "Strings containing '01' as a substring"
```
(0 + 1)*01(0 + 1)*
```

### "Strings of even length" over {a,b}
```
((a + b)(a + b))*
```
Or equivalently: `(aa + ab + ba + bb)*`

### "Strings with odd number of a's" over {a,b}
```
b*(ab*ab*)*ab*
```

### "Strings without two consecutive 0's" over {0,1}
```
(1 + 01)*(0 + ε)
```

### "All strings with at least two consecutive 0's"
```
(0 + 1)*00(0 + 1)*
```

---

## 🔄 Regex ↔ Automata (Kleene's Theorem)

> **Kleene's Theorem**: Regular expressions and finite automata define **the exact same class** of languages.

This means:
1. For every regex, you can build an NFA that accepts the same language
2. For every DFA, you can write a regex that describes the same language

### Regex → NFA (Thompson's Construction)

Build small NFAs for the base cases, then combine them:

```
Base cases:
  ε:  → (( q ))              (start = accept)
  a:  → ( q₀ ) ──a──→ (( q₁ ))

Combining:
  R₁ + R₂ (union):     Branch from new start to both NFAs via ε
  R₁R₂ (concatenation): Chain NFA₁'s accept to NFA₂'s start via ε
  R₁* (star):          Add ε-loop from accept back to start + ε bypass
```

### DFA → Regex (State Elimination)

1. Add a new unique start state and new unique accept state
2. Remove states one by one, replacing transitions with regex labels
3. When only start and accept remain, the label on the single arrow = your regex

> This can get messy for complex DFAs — that's normal. The procedure is mechanical.

---

## 📝 Useful Identities

| Identity | Meaning |
|----------|---------|
| ∅ + R = R | Union with empty set does nothing |
| εR = Rε = R | Concatenating ε does nothing |
| ∅R = R∅ = ∅ | Concatenating with ∅ gives ∅ |
| ∅* = ε | Star of empty set = {ε} |
| ε* = ε | Star of ε = {ε} |
| R + R = R | Union with itself = itself |
| (R*)* = R* | Double star = single star |
| R*R* = R* | Two stars in sequence = one star |

---

## ✅ Quick Self-Check

1. What does `(0+1)*0` represent?
2. Is `a*b*` the same as `(a+b)*`?
3. What's the precedence order (highest to lowest)?
4. Write a regex for "strings over {a,b} that start with 'a'"
5. What does Kleene's Theorem say in one sentence?

<details>
<summary>🔑 Answers</summary>

1. All binary strings ending in 0
2. **No!** `a*b*` = all a's then all b's (no mixing). `(a+b)*` = any arrangement.
3. Star (*) > Concatenation (.) > Union (+)
4. `a(a+b)*`
5. Regular expressions and finite automata define exactly the same class of languages (regular languages)

</details>

---

**⏱️ Time spent: ~20 min. Next →** [07 - Regular Grammars & Compiler Intro](./07-regular-grammars-and-compilers.md)
