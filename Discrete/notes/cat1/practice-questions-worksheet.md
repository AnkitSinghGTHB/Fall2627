# 🏋️ Discrete Math Module 1 — Practice Questions Worksheet

> **Instructions**: Try solving these questions on paper *before* checking the solutions! Answers are hidden inside the collapsible solution blocks at the bottom of each section.

---

## 🎯 Section A: Propositional Logic & Truth Tables

### Question 1
Construct a truth table to determine whether $(p \to q) \land (q \to p)$ is logically equivalent to $p \leftrightarrow q$.

### Question 2
Without using a truth table, prove the following logical equivalence using algebraic laws:
$$\neg(p \lor (\neg p \land q)) \equiv \neg p \land \neg q$$

### Question 3
Convert the formula $(p \to q) \land (q \to r)$ into:
1. Conjunctive Normal Form (CNF)
2. Disjunctive Normal Form (DNF)

<details>
<summary>💡 Check Solutions for Section A</summary>

#### Solution 1:
| $p$ | $q$ | $p \to q$ | $q \to p$ | $(p \to q) \land (q \to p)$ | $p \leftrightarrow q$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | **T** | **T** |
| T | F | F | T | **F** | **F** |
| F | T | T | F | **F** | **F** |
| F | F | T | T | **T** | **T** |
Both final columns are identical, so they are logically equivalent.

#### Solution 2:
1. $\neg(p \lor (\neg p \land q)) \equiv \neg p \land \neg(\neg p \land q)$ *(De Morgan's Law)*
2. $\equiv \neg p \land (\neg(\neg p) \lor \neg q)$ *(De Morgan's Law)*
3. $\equiv \neg p \land (p \lor \neg q)$ *(Double Negation Law)*
4. $\equiv (\neg p \land p) \lor (\neg p \land \neg q)$ *(Distributive Law)*
5. $\equiv \mathbf{F} \lor (\neg p \land \neg q)$ *(Negation Law)*
6. $\equiv \neg p \land \neg q$ *(Identity Law)*

#### Solution 3:
- **CNF**: $(\neg p \lor q) \land (\neg q \lor r)$
- **DNF**: $(\neg p \land \neg q) \lor (\neg p \land r) \lor (q \land r)$

</details>

---

## 🔮 Section B: Predicates, Quantifiers & Translations

### Question 4
Express the following system specification using predicates and quantifiers:  
*"When there is less than 30 megabytes free on the hard disk, a warning message is sent to all users."*

### Question 5
Rewrite the following statement so that negations appear only immediately within predicates (push $\neg$ inside):
$$\neg \exists y (\forall x \exists z \, T(x, y, z) \lor \exists x \forall z \, U(x, y, z))$$

### Question 6
Transform the following expression into **Prenex Normal Form (PNF)**:
$$\exists x \, P(x) \longrightarrow \exists x \, Q(x)$$

<details>
<summary>💡 Check Solutions for Section B</summary>

#### Solution 4:
Let $P$: "Free disk space $< 30$MB", $W(u)$: "Warning sent to user $u$".  
Expression: $P \longrightarrow \forall u \, W(u)$

#### Solution 5:
$$\forall y \, ((\exists x \forall z \, \neg T(x, y, z)) \land (\forall x \exists z \, \neg U(x, y, z)))$$

#### Solution 6:
$$\forall x \exists y \, (\neg P(x) \lor Q(y)) \quad \text{or} \quad \forall x \exists y \, (P(x) \to Q(y))$$

</details>

---

## ⚖️ Section C: Rules of Inference & Formal Proofs

### Question 7
Use rules of inference to show that if:
1. $\forall x (P(x) \to (Q(x) \land S(x)))$
2. $\forall x (P(x) \land R(x))$

are true, then $\forall x (R(x) \land S(x))$ is also true.

### Question 8 (Hard Exam Proof)
Use rules of inference to show that if the premises:
1. $\forall x (P(x) \lor Q(x))$
2. $\forall x (\neg Q(x) \lor S(x))$
3. $\forall x (R(x) \to \neg S(x))$
4. $\exists x \neg P(x)$

are true, then $\exists x \neg R(x)$ is also true.

<details>
<summary>💡 Check Solutions for Section C</summary>

#### Solution 7:
1. $\forall x (P(x) \land R(x))$ [Premise]
2. $P(c) \land R(c)$ [Universal Instantiation for arbitrary $c$]
3. $P(c)$ [Simplification]
4. $R(c)$ [Simplification]
5. $\forall x (P(x) \to (Q(x) \land S(x)))$ [Premise]
6. $P(c) \to (Q(c) \land S(c))$ [Universal Instantiation]
7. $Q(c) \land S(c)$ [Modus Ponens from 3 & 6]
8. $S(c)$ [Simplification]
9. $R(c) \land S(c)$ [Conjunction from 4 & 8]
10. $\forall x (R(x) \land S(x))$ [Universal Generalization]

#### Solution 8:
1. $\exists x \neg P(x)$ [Premise 4]
2. $\neg P(c)$ [Existential Instantiation]
3. $\forall x (P(x) \lor Q(x))$ [Premise 1]
4. $P(c) \lor Q(c)$ [Universal Instantiation]
5. $Q(c)$ [Disjunctive Syllogism from 2 & 4]
6. $\forall x (\neg Q(x) \lor S(x))$ [Premise 2]
7. $\neg Q(c) \lor S(c)$ [Universal Instantiation]
8. $S(c)$ [Disjunctive Syllogism from 5 & 7]
9. $\forall x (R(x) \to \neg S(x))$ [Premise 3]
10. $R(c) \to \neg S(c)$ [Universal Instantiation]
11. $\neg R(c)$ [Modus Tollens from 8 & 10]
12. $\exists x \neg R(x)$ [Existential Generalization]

</details>

---

**⏱️ Ready to revise? Back to Master Guide →** [README.md](./README.md)
