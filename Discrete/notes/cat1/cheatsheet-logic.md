# ⚡ Discrete Math — Logic + Quantifiers + Inference Cheatsheet

> **Print this. One page. All the formulas.**

---

## Connectives Truth Table
| p | q | ¬p | p∧q | p∨q | p→q | p↔q |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | F | T | T | T | T |
| T | F | F | F | T | **F** | F |
| F | T | T | F | T | T | F |
| F | F | T | F | F | T | T |

**p→q is FALSE only when T→F**

---

## Key Equivalences
```
p → q  ≡  ¬p ∨ q                  ← MOST TESTED
¬(p∧q) ≡ ¬p ∨ ¬q                  ← De Morgan's
¬(p∨q) ≡ ¬p ∧ ¬q                  ← De Morgan's
p → q  ≡  ¬q → ¬p                 ← Contrapositive
p↔q   ≡  (p→q) ∧ (q→p)
```

## Absorption: `p∧(p∨q) = p` &nbsp;&nbsp; `p∨(p∧q) = p`

---

## Quantifiers
```
∀x = "for all x"       ∃x = "there exists x"

¬(∀x P(x)) ≡ ∃x ¬P(x)     ← flip ∀↔∃, negate inside
¬(∃x P(x)) ≡ ∀x ¬P(x)
```

**"All A are B"** → ∀x(A(x) → B(x)) &nbsp;&nbsp; **"Some A are B"** → ∃x(A(x) ∧ B(x))

---

## Rules of Inference
| Rule | Form |
|------|------|
| Modus Ponens | p→q, p ∴ q |
| Modus Tollens | p→q, ¬q ∴ ¬p |
| Hypothetical Syllogism | p→q, q→r ∴ p→r |
| Disjunctive Syllogism | p∨q, ¬p ∴ q |
| Addition | p ∴ p∨q |
| Simplification | p∧q ∴ p |

---

## Relations
| Type | Properties |
|------|-----------|
| Equivalence | Reflexive + Symmetric + Transitive |
| Partial Order | Reflexive + Antisymmetric + Transitive |

## Euler vs Hamilton
| | Euler (every EDGE once) | Hamilton (every VERTEX once) |
|---|---|---|
| Circuit | All vertices even degree | No simple rule (Dirac: deg ≥ n/2) |
| Path | Exactly 2 odd-degree vertices | No simple rule |

## Handshaking: **Σ deg(v) = 2|E|**

## Lattice: POSET where every pair has unique LUB (∨) and GLB (∧)
## Boolean Algebra: Bounded + Complemented + Distributive lattice
## Complement: x∧x'=0, x∨x'=1

---

*One page. All of discrete math logic.*
