# 📝 Discrete Math Module 1 — Master Practice Question Bank & Worked Solutions

> **Source**: `MAT2002_Module 1-Practice questions.pdf` (VIT Course Outcomes & Rosen Textbook Exercises).  
> **Target**: Practice these exact solved problems before MTE/TEE exams!

---

## 📌 Section 1: Propositional Logic & Equivalences

### Problem 1 (CNF & DNF Conversion)
**Convert the formula $(p \to q) \land (q \to r)$ into Conjunctive Normal Form (CNF) and Disjunctive Normal Form (DNF).**

<details>
<summary>💡 Step-by-Step Solution</summary>

**Step 1:** Eliminate implication symbols using $A \to B \equiv \neg A \lor B$:
$$(p \to q) \land (q \to r) \equiv (\neg p \lor q) \land (\neg q \lor r)$$

**Conjunctive Normal Form (CNF):**
The expression $(\neg p \lor q) \land (\neg q \lor r)$ is ALREADY a conjunction of disjunctions!
$$\text{CNF} = (\neg p \lor q) \land (\neg q \lor r)$$

**Disjunctive Normal Form (DNF):**
Distribute the terms to obtain a disjunction of conjunctions:
$$(\neg p \lor q) \land (\neg q \lor r) \equiv (\neg p \land \neg q) \lor (\neg p \land r) \lor (q \land \neg q) \lor (q \land r)$$
Since $q \land \neg q = \mathbf{F}$, drop it:
$$\text{DNF} = (\neg p \land \neg q) \lor (\neg p \land r) \lor (q \land r)$$

**Result:** Correct ✅

</details>

---

## 📌 Section 2: Predicates & Quantifiers

### Problem 2 (Prenex Normal Form Transformation)
**Transform $\exists x \, P(x) \longrightarrow \exists x \, Q(x)$ into Prenex Normal Form (PNF).**

<details>
<summary>💡 Step-by-Step Solution</summary>

**Step 1:** Rename bound variables to avoid name collisions:
$$\exists x \, P(x) \longrightarrow \exists y \, Q(y)$$

**Step 2:** Eliminate implication using $A \to B \equiv \neg A \lor B$:
$$\neg (\exists x \, P(x)) \lor \exists y \, Q(y)$$

**Step 3:** Push negation $\neg$ inside the quantifier:
$$\forall x \, \neg P(x) \lor \exists y \, Q(y)$$

**Step 4:** Pull quantifiers to the front (since $x$ is not free in $Q(y)$ and $y$ is not free in $P(x)$):
$$\mathbf{\forall x \exists y \, (\neg P(x) \lor Q(y))}$$  
*(or equivalently $\mathbf{\forall x \exists y \, (P(x) \to Q(y))}$)* ✅
</details>

---

## 📌 Section 3: Rules of Inference & Multi-Premise Proofs

### Problem 3 (Hard Exam Proof with 4 Premises)
**Use the rules of inference to show that if the premises:**
1. $\forall x \, (P(x) \lor Q(x))$
2. $\forall x \, (\neg Q(x) \lor S(x))$
3. $\forall x \, (R(x) \to \neg S(x))$
4. $\exists x \, \neg P(x)$

**are true, then $\exists x \, \neg R(x)$ is also true.**

<details>
<summary>💡 Step-by-Step Solution</summary>

| Step | Statement | Reason |
|:---:|---|---|
| 1 | $\exists x \, \neg P(x)$ | Premise 4 |
| 2 | $\neg P(c)$ | Existential Instantiation (1) for some specific element $c$ |
| 3 | $\forall x \, (P(x) \lor Q(x))$ | Premise 1 |
| 4 | $P(c) \lor Q(c)$ | Universal Instantiation (3) for $c$ |
| 5 | $Q(c)$ | Disjunctive Syllogism from (2) and (4) |
| 6 | $\forall x \, (\neg Q(x) \lor S(x))$ | Premise 2 |
| 7 | $\neg Q(c) \lor S(c)$ | Universal Instantiation (6) for $c$ |
| 8 | $S(c)$ | Disjunctive Syllogism from (5) and (7) |
| 9 | $\forall x \, (R(x) \to \neg S(x))$ | Premise 3 |
| 10 | $R(c) \to \neg S(c)$ | Universal Instantiation (9) for $c$ |
| 11 | $\neg \neg S(c)$ | Double Negation on (8), i.e. $S(c)$ is true |
| 12 | $\neg R(c)$ | Modus Tollens from (10) and (11) |
| 13 | $\exists x \, \neg R(x)$ | Existential Generalization from (12) ∎ ✅ |

</details>

---

**⏱️ Study time: ~20 mins | Master Hub →** [README.md](./README.md)
