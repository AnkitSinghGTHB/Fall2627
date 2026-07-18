# 🔮 Lesson 2 — Predicates, Quantifiers & Rules of Inference

> **TL;DR**: Predicates = propositions with variables. Quantifiers = "for all" (∀) and "there exists" (∃). Rules of inference = valid argument patterns (like Modus Ponens: if p→q and p, then q). This is the logic toolkit you'll use in proofs.

---

## Part A: Predicates

### What's a Predicate?

A predicate is a statement that **becomes** a proposition once you fill in the variable.

```
P(x): "x is greater than 5"

P(3) = "3 is greater than 5" = FALSE     ← now it's a proposition
P(8) = "8 is greater than 5" = TRUE      ← now it's a proposition
P(x) = ???                                ← still a predicate (depends on x)
```

The variable's **domain** = the set of allowed values (integers, real numbers, students, etc.)

---

## Part B: Quantifiers

Quantifiers turn predicates into propositions by specifying **how many** values make it true.

| Quantifier | Symbol | Meaning | English |
|:---:|:---:|---|---|
| **Universal** | **∀** | "For ALL x" | Every single one |
| **Existential** | **∃** | "There EXISTS an x" | At least one |
| **Uniqueness** | **∃!** | "There exists EXACTLY ONE x" | One and only one |

### Examples

| Logical Expression | English | True/False (domain: integers) |
|---|---|:---:|
| ∀x (x² ≥ 0) | "Every integer squared is ≥ 0" | TRUE |
| ∃x (x + 3 = 3x) | "Some integer satisfies x+3=3x" | TRUE (x=3/2... wait, not an integer. FALSE for integers!) |
| ∀x (x > 0) | "All integers are positive" | FALSE (−1 exists) |
| ∃x (x = −x) | "Some integer equals its own negative" | TRUE (x = 0) |

---

### Negating Quantifiers

This is **heavily tested**. The rules are simple:

```
¬(∀x P(x))  ≡  ∃x ¬P(x)      "Not everyone is P"  =  "Someone is NOT P"
¬(∃x P(x))  ≡  ∀x ¬P(x)      "Nothing is P"       =  "Everything is NOT P"
```

> 🧠 **Memory trick**: Negation **flips** the quantifier (∀ ↔ ∃) and **negates** the predicate inside.

### Nested Quantifiers

Order matters!

```
∀x ∃y (x + y = 0)    "For every x, there's a y such that x+y=0"  → TRUE (y = -x)
∃y ∀x (x + y = 0)    "There's one y that works for ALL x"         → FALSE
```

> ⚠️ **∀x ∃y ≠ ∃y ∀x** — Order changes the meaning!

---

### Translating English ↔ Logic

| English | Logic |
|---------|-------|
| "All dogs are mammals" | ∀x (Dog(x) → Mammal(x)) |
| "Some students passed" | ∃x (Student(x) ∧ Passed(x)) |
| "No cat is a dog" | ∀x (Cat(x) → ¬Dog(x)) |
| "Everyone loves someone" | ∀x ∃y Loves(x, y) |
| "Someone is loved by everyone" | ∃y ∀x Loves(x, y) |

> 🎯 **Pattern**: "All A are B" uses → (implication). "Some A are B" uses ∧ (and).

---

## Part C: Rules of Inference

Rules of inference = **valid argument templates**. If the premises are true, the conclusion MUST be true.

### The 8 Essential Rules

| Rule | Pattern | In English |
|------|---------|------------|
| **Modus Ponens** | p→q, p ∴ q | "If rain then wet. It rained. So it's wet." |
| **Modus Tollens** | p→q, ¬q ∴ ¬p | "If rain then wet. Not wet. So no rain." |
| **Hypothetical Syllogism** | p→q, q→r ∴ p→r | "If A then B. If B then C. So if A then C." |
| **Disjunctive Syllogism** | p∨q, ¬p ∴ q | "Tea or coffee. Not tea. So coffee." |
| **Addition** | p ∴ p∨q | "It's raining. So it's raining or snowing." |
| **Simplification** | p∧q ∴ p | "It's hot and humid. So it's hot." |
| **Conjunction** | p, q ∴ p∧q | "It's hot. It's humid. So it's hot and humid." |
| **Resolution** | p∨q, ¬p∨r ∴ q∨r | (Used in automated theorem proving) |

### For Quantifiers

| Rule | Pattern |
|------|---------|
| **Universal Instantiation** | ∀x P(x) ∴ P(c) for any c |
| **Universal Generalization** | P(c) for arbitrary c ∴ ∀x P(x) |
| **Existential Instantiation** | ∃x P(x) ∴ P(c) for some specific c |
| **Existential Generalization** | P(c) for some c ∴ ∃x P(x) |

---

### Example Proof Using Inference Rules

**Prove**: "Socrates is mortal" given:
1. All men are mortal: ∀x (Man(x) → Mortal(x))
2. Socrates is a man: Man(Socrates)

```
Step 1: ∀x (Man(x) → Mortal(x))          ← Premise 1
Step 2: Man(Socrates) → Mortal(Socrates)  ← Universal Instantiation (x = Socrates)
Step 3: Man(Socrates)                      ← Premise 2
Step 4: Mortal(Socrates)                   ← Modus Ponens (Steps 2 + 3)  ∎
```

---

## ✅ Quick Self-Check

1. What's ¬(∀x P(x)) equivalent to?
2. Translate "No student failed" into logic
3. Which inference rule: p→q, p, therefore q?
4. Is ∀x ∃y the same as ∃y ∀x?
5. What's Modus Tollens in one sentence?

<details>
<summary>🔑 Answers</summary>

1. ∃x ¬P(x) ("there exists an x that is NOT P")
2. ∀x (Student(x) → ¬Failed(x))  OR  ¬∃x (Student(x) ∧ Failed(x))
3. **Modus Ponens**
4. **No!** Order of quantifiers matters
5. "If p implies q, and q is false, then p must be false" (contrapositive reasoning)

</details>

---

**⏱️ Time spent: ~20 min. Next →** [03 - Sets, Relations & Hasse Diagrams](./03-sets-relations-hasse.md)
