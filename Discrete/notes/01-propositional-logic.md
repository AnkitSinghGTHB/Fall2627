# 🧩 Lesson 1 — Propositional Logic & Connectives

> **TL;DR**: Propositions = statements that are TRUE or FALSE. Connectives (AND, OR, NOT, IF-THEN, IFF) combine them. Truth tables show every possible outcome. Tautology = always true. Contradiction = always false. Master the equivalence laws and you can simplify anything.

---

## 🤔 What is a Proposition?

A **proposition** (or statement) = a sentence that is **definitely true** or **definitely false**. Not both, not neither.

| ✅ Proposition | ❌ NOT a Proposition |
|---|---|
| "2 + 3 = 5" (TRUE) | "What time is it?" (question) |
| "Delhi is in India" (TRUE) | "Close the door!" (command) |
| "5 > 10" (FALSE) | "x + 1 = 2" (depends on x) |

> We use lowercase letters **p, q, r, s** to represent propositions.

---

## 🔗 Logical Connectives — The 5 Operators

| Connective | Symbol | Name | In English | Example |
|:---:|:---:|---|---|---|
| **NOT** | ¬p | Negation | "not p" | ¬(it's raining) = it's not raining |
| **AND** | p ∧ q | Conjunction | "p and q" | It's hot AND humid |
| **OR** | p ∨ q | Disjunction | "p or q (or both)" | Tea OR coffee |
| **IF-THEN** | p → q | Implication | "if p then q" | If it rains, roads are wet |
| **IFF** | p ↔ q | Biconditional | "p if and only if q" | Pass IFF score ≥ 40 |

---

## 📊 Truth Tables — The Master Reference

### NOT (¬)
| p | ¬p |
|:---:|:---:|
| T | **F** |
| F | **T** |

### AND (∧) — TRUE only when BOTH are true
| p | q | p ∧ q |
|:---:|:---:|:---:|
| T | T | **T** |
| T | F | F |
| F | T | F |
| F | F | F |

### OR (∨) — FALSE only when BOTH are false
| p | q | p ∨ q |
|:---:|:---:|:---:|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | **F** |

### IMPLICATION (→) — FALSE only when TRUE implies FALSE
| p | q | p → q |
|:---:|:---:|:---:|
| T | T | T |
| T | F | **F** |
| F | T | T |
| F | F | T |

> 🧠 **Memory trick for →**: "A lie is only caught when a liar (T) makes a false promise (F)." All other cases give T.

### BICONDITIONAL (↔) — TRUE when both match
| p | q | p ↔ q |
|:---:|:---:|:---:|
| T | T | **T** |
| T | F | F |
| F | T | F |
| F | F | **T** |

---

## 🏷️ Special Types of Propositions

| Type | Definition | Example |
|------|-----------|---------|
| **Tautology** | ALWAYS true (every row = T) | p ∨ ¬p |
| **Contradiction** | ALWAYS false (every row = F) | p ∧ ¬p |
| **Contingency** | Sometimes true, sometimes false | p ∧ q |

---

## ⚖️ Logical Equivalence Laws (MEMORIZE THESE)

Two expressions are **logically equivalent** (≡) if they have identical truth tables.

### The Essential Laws

| Law | AND form (∧) | OR form (∨) |
|-----|:---:|:---:|
| **Identity** | p ∧ T ≡ p | p ∨ F ≡ p |
| **Domination** | p ∧ F ≡ F | p ∨ T ≡ T |
| **Idempotent** | p ∧ p ≡ p | p ∨ p ≡ p |
| **Complement** | p ∧ ¬p ≡ F | p ∨ ¬p ≡ T |
| **Double Negation** | ¬(¬p) ≡ p | |
| **Commutative** | p ∧ q ≡ q ∧ p | p ∨ q ≡ q ∨ p |
| **Associative** | (p∧q)∧r ≡ p∧(q∧r) | (p∨q)∨r ≡ p∨(q∨r) |
| **Distributive** | p∧(q∨r) ≡ (p∧q)∨(p∧r) | p∨(q∧r) ≡ (p∨q)∧(p∨r) |
| **De Morgan's** | **¬(p∧q) ≡ ¬p ∨ ¬q** | **¬(p∨q) ≡ ¬p ∧ ¬q** |
| **Absorption** | p ∧ (p∨q) ≡ p | p ∨ (p∧q) ≡ p |

### Implication Equivalences
```
p → q  ≡  ¬p ∨ q               ← MOST IMPORTANT ONE
p → q  ≡  ¬q → ¬p              ← Contrapositive (logically same)
p ↔ q  ≡  (p→q) ∧ (q→p)        ← Biconditional = two implications
```

> 🎯 **Exam tip**: The most commonly tested equivalence is **p → q ≡ ¬p ∨ q**. It appears everywhere.

---

## 🔧 How to Build a Truth Table (Step by Step)

**Example**: Show that p → q ≡ ¬p ∨ q

| p | q | ¬p | p → q | ¬p ∨ q |
|:---:|:---:|:---:|:---:|:---:|
| T | T | F | T | T |
| T | F | F | F | F |
| F | T | T | T | T |
| F | F | T | T | T |

Columns 4 and 5 are **identical** → they are logically equivalent ✅

---

## 🏋️ Solved Exam Practice Questions

### Question 1 (VIT TEE/MTE Style)
**Construct a truth table to determine whether $(p \to q) \land (q \to p)$ is logically equivalent to $p \leftrightarrow q$.**

<details>
<summary>💡 Step-by-Step Solution</summary>

**Step 1:** List all combinations for inputs $p$ and $q$.  
**Step 2:** Evaluate $(p \to q)$, $(q \to p)$, and their conjunction $(p \to q) \land (q \to p)$.  
**Step 3:** Compare with $p \leftrightarrow q$.

| $p$ | $q$ | $p \to q$ | $q \to p$ | $(p \to q) \land (q \to p)$ | $p \leftrightarrow q$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | **T** | **T** |
| T | F | F | T | **F** | **F** |
| F | T | T | F | **F** | **F** |
| F | F | T | T | **T** | **T** |

**Conclusion:** The last two columns are identical for all truth assignments. Hence, $(p \to q) \land (q \to p) \equiv p \leftrightarrow q$. ✅
</details>

---

### Question 2 (Simplification Proof)
**Without using a truth table, prove that $\neg(p \lor (\neg p \land q)) \equiv \neg p \land \neg q$.**

<details>
<summary>💡 Step-by-Step Solution</summary>

Apply logical equivalence laws step-by-step:
1. $\neg(p \lor (\neg p \land q))$
2. $\equiv \neg p \land \neg(\neg p \land q)$ *(De Morgan's Law on outer OR)*
3. $\equiv \neg p \land (\neg(\neg p) \lor \neg q)$ *(De Morgan's Law on inner AND)*
4. $\equiv \neg p \land (p \lor \neg q)$ *(Double Negation Law)*
5. $\equiv (\neg p \land p) \lor (\neg p \land \neg q)$ *(Distributive Law)*
6. $\equiv \mathbf{F} \lor (\neg p \land \neg q)$ *(Negation Law: $\neg p \land p = \mathbf{F}$)*
7. $\equiv \neg p \land \neg q$ *(Identity Law: $\mathbf{F} \lor A = A$)* ✅
</details>

---

## ✅ Quick Self-Check

1. Is "x + 5 = 10" a proposition?
2. What's the only case where p → q is FALSE?
3. What is ¬(p ∧ q) equivalent to? (De Morgan's)
4. Is p ∨ ¬p a tautology or contradiction?
5. Simplify: p ∧ (p ∨ q)

<details>
<summary>🔑 Answers</summary>

1. **No** — it depends on x (it's a predicate, not a proposition)
2. When p = TRUE and q = FALSE
3. ¬p ∨ ¬q (De Morgan's)
4. **Tautology** (always true)
5. **p** (Absorption law)

</details>

---

**⏱️ Time spent: ~15 min. Next →** [02 - Predicates & Quantifiers](./02-predicates-and-quantifiers.md)
