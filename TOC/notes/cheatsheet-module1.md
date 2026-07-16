# ⚡ TOC Module 1 — Master Cheatsheet

> **One page. Everything. Print it.**

---

## Chomsky Hierarchy
| Type | Grammar | Machine | Language |
|:---:|---|---|---|
| 3 | Regular | FA (DFA/NFA) | Regular |
| 2 | Context-Free | PDA | Context-Free |
| 1 | Context-Sensitive | LBA | Context-Sensitive |
| 0 | Unrestricted | TM | Recursively Enumerable |

---

## Strings & Languages
- **Σ*** = all strings (including ε) &nbsp;&nbsp; **Σ⁺** = all strings (excluding ε)
- **|w|** = length &nbsp;&nbsp; **wᴿ** = reverse &nbsp;&nbsp; **ε** = empty string
- **{ε} ≠ ∅** → {ε} has one element, ∅ has zero

---

## DFA: M = (Q, Σ, δ, q₀, F)
- δ(state, symbol) = **exactly one** state
- Accepts when string ends on a **final state**

## NFA: N = (Q, Σ, δ, q₀, F)
- δ(state, symbol) = **set of states** (0, 1, or many)
- Accepts if **any path** ends on a final state
- **DFA ≡ NFA ≡ ε-NFA** (all = Regular Languages)

## NFA → DFA (Subset Construction)
1. Start: ε-closure(q₀)
2. Each DFA state = **set of NFA states**
3. For each set + symbol → compute union of transitions + ε-closure
4. Accepting if set **contains any** NFA accepting state

---

## Regular Expressions
| Operator | Precedence | Meaning |
|:---:|:---:|---|
| **\*** | Highest | Zero or more |
| **.** (concat) | Middle | Followed by |
| **+** (union) | Lowest | Or |

### Key Patterns
| Pattern | Regex |
|---|---|
| All strings over {a,b} | `(a+b)*` |
| Ends in b | `(a+b)*b` |
| Contains "01" | `(0+1)*01(0+1)*` |
| Even length | `((a+b)(a+b))*` |

### ⚠️ NOT the same
`a*b*` ≠ `(ab)*` ≠ `(a+b)*`

---

## Regular Grammars
- **Right-linear**: A → xB or A → x
- **Left-linear**: A → Bx or A → x
- **Don't mix** left and right in the same grammar
- Regular Grammar ↔ NFA ↔ Regex (all equivalent)

## Grammar → NFA
- Variable → state, Production A→aB → transition, Final state for A→a

## NFA → Grammar
- Transition δ(q,a)=p → production q→ap, Final state qf → qf→ε

---

## 6 Compiler Phases
```
Lexical (DFA) → Syntax (PDA) → Semantic → IR Gen → Optimizer → Code Gen
```

---

*Module 1 done. Now go draw 10 DFAs by hand.*
