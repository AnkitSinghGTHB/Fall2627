# 📘 Module 1: Predicate Calculus & Formal Logic (From Zero to Mastery)

> **Module Focus**: Propositional Logic, Truth Tables, Logical Equivalences, Rules of Inference, Predicates, Quantifiers, and Formal Proofs.  
> **Weightage in FAT**: Approx 15–20 Marks.  
> **Philosophy**: Logic is just the language of computers and proofs. If you understand the rules like a game of chess, you can never get a single step wrong.

---

## 1. Propositional Logic: The Fundamentals

### 1.1 What is a Proposition?
* **Plain English Intuition**: A proposition is a declarative sentence that is **strictly True (T) or False (F)**, but **never both**, and never an opinion, question, or command.
* **Examples**:
  * *"VIT Bhopal is in Madhya Pradesh."* $\to$ Proposition (True).
  * *"2 + 3 = 99."* $\to$ Proposition (False).
  * *"What is your name?"* $\to$ **NOT** a proposition (Question).
  * *"Please submit the assignment."* $\to$ **NOT** a proposition (Command).
  * *"$x + 5 = 10$."* $\to$ **NOT** a proposition yet (Truth depends on variable $x$; this is a *predicate*).

---

### 1.2 The 5 Logical Connectives (The Building Blocks)

Think of connectives like arithmetic operators ($+, -, \times, \div$), but for truth values.

| Name | Symbol | Plain English Meaning | The "Gold Rule" to Remember |
| :--- | :---: | :--- | :--- |
| **Negation** | $\neg p$ or $\sim p$ | "NOT $p$" | Flips truth value ($T \to F, F \to T$). |
| **Conjunction** | $p \wedge q$ | "$p$ AND $q$" | **True ONLY IF BOTH are True**. Otherwise False. |
| **Disjunction** | $p \vee q$ | "$p$ OR $q$" (Inclusive) | **False ONLY IF BOTH are False**. Otherwise True. |
| **Conditional** | $p \to q$ | "If $p$, then $q$" | **False ONLY IF $p$ is True AND $q$ is False** ($T \to F = F$). In all other cases, it is True! |
| **Biconditional**| $p \leftrightarrow q$ | "$p$ if and only if $q$" (iff) | **True when both have the SAME truth value** ($T \leftrightarrow T = T$, $F \leftrightarrow F = T$). |
| **Exclusive OR** | $p \oplus q$ | "Either $p$ or $q$, but not both" | **True when truth values are DIFFERENT**. |

```text
        TRUTH TABLE SUMMARY FOR QUICK REVISION:
┌───────┬───────┬────────┬────────┬───────┬──────────┬───────────┐
│   p   │   q   │  ¬ p   │ p ∧ q  │ p ∨ q │  p → q   │  p ↔ q    │
├───────┼───────┼────────┼────────┼───────┼──────────┼───────────┤
│   T   │   T   │   F    │   T    │   T   │    T     │    T      │
│   T   │   F   │   F    │   F    │   T   │    F ◄──!│    F      │
│   F   │   T   │   T    │   F    │   T   │    T     │    F      │
│   F   │   F   │   T    │   F    │   F   │    T     │    T      │
└───────┴───────┴────────┴────────┴───────┴──────────┴───────────┘
   ▲ Note: The ONLY way p → q is False is if a true promise leads to a false outcome!
```

---

### 1.3 Tautology, Contradiction, and Contingency
* **Tautology**: A compound proposition that is **always TRUE** for every combination of truth values (e.g., $p \vee \neg p$).
* **Contradiction (Fallacy)**: A compound proposition that is **always FALSE** for every combination (e.g., $p \wedge \neg p$).
* **Contingency**: A proposition that is neither a tautology nor a contradiction (it has a mix of T and F in its final truth table column).

---

### 1.4 Converse, Inverse, and Contrapositive (Guaranteed 2-3 Mark Question)

Given a conditional statement: **$p \to q$** ("If $p$, then $q$"):

1. **Converse**: **$q \to p$** (Swap the hypothesis and conclusion).
2. **Inverse**: **$\neg p \to \neg q$** (Negate both sides).
3. **Contrapositive**: **$\neg q \to \neg p$** (Swap AND negate both sides).

> ⚠️ **CRITICAL THEOREM**:  
> **A conditional statement is LOGICALLY EQUIVALENT to its CONTRAPOSITIVE**:  
> 
> $$p \to q \equiv \neg q \to \neg p$$
> 
> *(The Converse and Inverse are equivalent to each other, but **NOT** to the original conditional!)*

#### 📝 Worked Exam Example:
> **Question**: For the statement *"If it rains, then the match is cancelled"*, write the Converse, Inverse, and Contrapositive.
>
> **Solution**:
> * Let $p$: "It rains", $q$: "The match is cancelled".
> * Original ($p \to q$): "If it rains, then the match is cancelled."
> * **Converse ($q \to p$)**: *"If the match is cancelled, then it rains."*
> * **Inverse ($\neg p \to \neg q$)**: *"If it does not rain, then the match is not cancelled."*
> * **Contrapositive ($\neg q \to \neg p$)**: *"If the match is not cancelled, then it does not rain."*

---

## 2. Logical Equivalences Without Truth Tables (Laws of Statement Calculus)

In Term End, professors love giving: **"Prove the equivalence WITHOUT using truth tables"** (5 Marks).  
To score full marks, you must apply the formal laws line by line and state the law name in brackets!

### 2.1 The Master Laws Table

| Law Name | Disjunction ($\vee$) Form | Conjunction ($\wedge$) Form |
| :--- | :--- | :--- |
| **Identity Laws** | $p \vee F \equiv p$ | $p \wedge T \equiv p$ |
| **Domination Laws** | $p \vee T \equiv T$ | $p \wedge F \equiv F$ |
| **Idempotent Laws** | $p \vee p \equiv p$ | $p \wedge p \equiv p$ |
| **Double Negation** | $\neg(\neg p) \equiv p$ | — |
| **Commutative Laws**| $p \vee q \equiv q \vee p$ | $p \wedge q \equiv q \wedge p$ |
| **Associative Laws**| $(p \vee q) \vee r \equiv p \vee (q \vee r)$ | $(p \wedge q) \wedge r \equiv p \wedge (q \wedge r)$ |
| **Distributive Laws**| $p \vee (q \wedge r) \equiv (p \vee q) \wedge (p \vee r)$ | $p \wedge (q \vee r) \equiv (p \wedge q) \vee (p \wedge r)$ |
| **De Morgan's Laws** | $\neg(p \vee q) \equiv \neg p \wedge \neg q$ | $\neg(p \wedge q) \equiv \neg p \vee \neg q$ |
| **Absorption Laws** | $p \vee (p \wedge q) \equiv p$ | $p \wedge (p \vee q) \equiv p$ |
| **Complement Laws** | $p \vee \neg p \equiv T$ | $p \wedge \neg p \equiv F$ |

### 2.2 Crucial Conditional Equivalence Laws (Memorize These!)
1. **Conditional Identity**: $p \to q \equiv \neg p \vee q$
2. **Negation of Conditional**: $\neg(p \to q) \equiv p \wedge \neg q$
3. **Contrapositive Law**: $p \to q \equiv \neg q \to \neg p$
4. **Biconditional Identity**: $p \leftrightarrow q \equiv (p \to q) \wedge (q \to p) \equiv (\neg p \vee q) \wedge (\neg q \vee p)$
5. **Exportation Law**: $(p \wedge q) \to r \equiv p \to (q \to r)$

---

### 📝 Worked Past Exam Problem: Equivalence Without Truth Table
> **Question**: Prove that $(p \to r) \vee (q \to r) \equiv (p \wedge q) \to r$ without using a truth table.
>
> **Solution**:  
> Start with the Left-Hand Side (LHS):
> 1. $\text{LHS} = (p \to r) \vee (q \to r)$
> 2. $\equiv (\neg p \vee r) \vee (\neg q \vee r)$ &nbsp;&nbsp;&nbsp;&nbsp; *(By Conditional Law: $a \to b \equiv \neg a \vee b$)*
> 3. $\equiv (\neg p \vee \neg q) \vee (r \vee r)$ &nbsp;&nbsp;&nbsp;&nbsp; *(By Associative & Commutative Laws)*
> 4. $\equiv (\neg p \vee \neg q) \vee r$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *(By Idempotent Law: $r \vee r \equiv r$)*
> 5. $\equiv \neg(p \wedge q) \vee r$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *(By De Morgan's Law)*
> 6. $\equiv (p \wedge q) \to r$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *(By Conditional Law: $\neg A \vee B \equiv A \to B$)*
> 7. $\equiv \text{RHS}$. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Hence Proved!**

---

## 3. Theory of Inference for Statement Calculus

An argument is a sequence of statements: Premises $P_1, P_2, \dots, P_k$, concluding in $C$.  
The argument is **valid** if:
$$(P_1 \wedge P_2 \wedge \dots \wedge P_k) \to C \text{ is a TAUTOLOGY}$$

### 3.1 The 8 Fundamental Rules of Inference

| Rule of Inference | Name | Plain English Intuition |
| :--- | :--- | :--- |
| $p, \ p \to q$<br>$\therefore q$ | **Modus Ponens (MP)** | If $p$ is true and $p$ implies $q$, then $q$ must be true. |
| $\neg q, \ p \to q$<br>$\therefore \neg p$ | **Modus Tollens (MT)** | If $q$ is false, then $p$ couldn't have been true. |
| $p \to q, \ q \to r$<br>$\therefore p \to r$ | **Hypothetical Syllogism (HS)** | Chain rule: $p$ leads to $q$, and $q$ leads to $r$, so $p$ leads to $r$. |
| $p \vee q, \ \neg p$<br>$\therefore q$ | **Disjunctive Syllogism (DS)** | Either $p$ or $q$. But not $p$. So it must be $q$. |
| $p$<br>$\therefore p \vee q$ | **Addition (Add)** | If $p$ is true, then "$p$ OR anything" is also true. |
| $p \wedge q$<br>$\therefore p$ | **Simplification (Simp)** | If both $p$ and $q$ are true, then $p$ is certainly true. |
| $p, \ q$<br>$\therefore p \wedge q$ | **Conjunction (Conj)** | If $p$ is true and $q$ is true, you can join them with AND. |
| $p \vee q, \ \neg p \vee r$<br>$\therefore q \vee r$ | **Resolution (Res)** | Resolves complementary literals $p$ and $\neg p$. |

---

### 3.2 Proof Techniques: Direct, Conditional (CP), and Indirect

1. **Direct Proof**: Start with premises, apply inference rules step by step until reaching the conclusion.
2. **Rule CP (Conditional Proof)**: When the conclusion is in conditional form $A \to B$:
   * **Temporarily assume $A$ as an extra premise**.
   * Derive $B$ using standard rules.
   * Conclude $A \to B$.
3. **Indirect Proof (Proof by Contradiction / Reductio ad Absurdum)**:
   * **Assume the NEGATION of the conclusion ($\neg C$) as an additional premise**.
   * Derive a contradiction of the form $R \wedge \neg R$.
   * Since a contradiction cannot be true, the assumption $\neg C$ must be false, so $C$ is TRUE!

---

### 📝 Worked Past Exam Problem: Formal Proof of Validity
> **Question**: Show that the following argument is valid:  
> Premises: $p \to (q \to r)$, $p \vee \neg s$, $q$.  
> Conclusion: $s \to r$.
>
> **Solution (Using Rule CP)**:  
> Since the conclusion is $s \to r$, assume $s$ as an additional premise (Rule CP). We need to derive $r$.
>
> | Step # | Statement | Justification / Rule |
> | :---: | :--- | :--- |
> | 1 | $s$ | Assumed premise (Rule CP) |
> | 2 | $p \vee \neg s$ | Premise |
> | 3 | $\neg(\neg s)$ | Double Negation on Step 1 ($\equiv s$) |
> | 4 | $p$ | Disjunctive Syllogism (DS) on Steps 2 and 3 |
> | 5 | $p \to (q \to r)$ | Premise |
> | 6 | $q \to r$ | Modus Ponens (MP) on Steps 4 and 5 |
> | 7 | $q$ | Premise |
> | 8 | $r$ | Modus Ponens (MP) on Steps 7 and 6 |
> | 9 | $s \to r$ | Rule CP (from Step 1 to Step 8) |
>
> **Hence, the argument is valid!**

---

## 4. Predicates & Quantifiers

### 4.1 Predicates & Domain of Discourse
* A **Predicate** is a statement involving variables, written as $P(x)$, where $P$ is the property and $x$ is the subject.
* Example: $P(x)$: "$x > 3$". If domain is integers, $P(4)$ is True, $P(1)$ is False.
* **Domain of Discourse (Universe)**: The set of all possible values that variable $x$ can take.

---

### 4.2 The Two Quantifiers

1. **Universal Quantifier ($\forall x$)**:
   * "For all $x$", "For every $x$", "For each $x$".
   * $\forall x P(x)$ is **True** iff $P(x)$ is True for **every single element** in the domain.
   * $\forall x P(x)$ is **False** if there is **even ONE counterexample** where $P(x)$ is False.

2. **Existential Quantifier ($\exists x$)**:
   * "There exists an $x$", "For some $x$", "At least one $x$".
   * $\exists x P(x)$ is **True** if there is **at least one element** where $P(x)$ is True.
   * $\exists x P(x)$ is **False** iff $P(x)$ is False for **every element** in the domain.

---

### 4.3 Negation of Quantified Statements (De Morgan's for Quantifiers)
$$\neg \forall x P(x) \equiv \exists x \neg P(x)$$
$$\neg \exists x P(x) \equiv \forall x \neg P(x)$$

* *Intuition*: "Not all students passed" $\equiv$ "At least one student did not pass".
* *Intuition*: "No student failed" $\equiv$ "Every student passed".

---

### 4.4 Nested Quantifiers: Order Matters!
* $\forall x \forall y P(x, y) \equiv \forall y \forall x P(x, y)$ (Order does NOT matter if quantifiers are the same).
* $\exists x \exists y P(x, y) \equiv \exists y \exists x P(x, y)$ (Order does NOT matter).
* **$\forall x \exists y P(x, y) \not\equiv \exists y \forall x P(x, y)$ (ORDER MATTERS CRITICALLY!)**:
  * $\forall x \exists y (x + y = 0)$: "Every number $x$ has an additive inverse $y$." (TRUE in $\mathbb{R}$: for $x=5$, $y=-5$; for $x=8$, $y=-8$).
  * $\exists y \forall x (x + y = 0)$: "There exists a single magic number $y$ that adds to EVERY number $x$ to make 0." (FALSE! No single number works for all).

---

## 5. Rules of Inference for Quantified Statements

To do proofs with quantifiers, you follow a 3-step cycle:
```text
[Quantified Premise] ──(Strip Quantifier)──► [Propositional Form] ──(Apply MP/MT/DS)──► [Derived Proposition] ──(Re-add Quantifier)──► [Quantified Conclusion]
```

### 5.1 The 4 Rules of Quantifier Inference

| Rule | Name | When & How to Use It |
| :--- | :--- | :--- |
| $\forall x \, P(x)$<br>$\therefore P(c)$ | **Universal Instantiation (UI)** | If something is true for **everyone**, it is true for any specific individual $c$ in the domain. |
| $P(c) \text{ (arbitrary } c\text{)}$<br>$\therefore \forall x \, P(x)$ | **Universal Generalization (UG)** | If $P(c)$ was proved for an **arbitrary (generic)** element $c$ without assuming special properties, it holds for all $x$. |
| $\exists x \, P(x)$<br>$\therefore P(c) \text{ (fresh } c\text{)}$ | **Existential Instantiation (EI)** | If an element exists, give it a **fresh temporary name** $c$. (*Warning: $c$ must be brand new, not previously used!*) |
| $P(c) \text{ (known } c\text{)}$<br>$\therefore \exists x \, P(x)$ | **Existential Generalization (EG)** | If you found a specific element $c$ that works, then "there exists at least one $x$" is true. |

> ⚠️ **THE GOLDEN RULE OF EI BEFORE UI**:  
> Always perform **Existential Instantiation (EI) FIRST** to name the unknown element $c$, and then apply **Universal Instantiation (UI)** to that same $c$! If you do UI first, you cannot use that symbol for EI.

---

### 📝 Worked Past Exam Problem: Socrates Syllogism
> **Question**: Show that the premises:  
> 1. "All men are mortal."  
> 2. "Socrates is a man."  
> imply the conclusion: "Socrates is mortal."
>
> **Solution**:  
> * Let $M(x)$: "$x$ is a man".  
> * Let $H(x)$: "$x$ is mortal".  
> * Let $s$: Socrates.  
> 
> Premises in symbolic form:  
> 1. $\forall x (M(x) \to H(x))$  
> 2. $M(s)$  
> Conclusion to prove: $H(s)$  
>
> | Step # | Statement | Justification / Rule |
> | :---: | :--- | :--- |
> | 1 | $\forall x (M(x) \to H(x))$ | Premise 1 |
> | 2 | $M(s) \to H(s)$ | Universal Instantiation (UI) on Step 1 with $x = s$ |
> | 3 | $M(s)$ | Premise 2 |
> | 4 | $H(s)$ | Modus Ponens (MP) on Steps 3 and 2 |
>
> **Conclusion $H(s)$ is proved. Hence, Socrates is mortal!**

---

## 💡 Module 1 Summary Checklist & Exam Traps

- [ ] Can you construct an 8-row truth table for 3 variables without copying errors?
- [ ] Do you remember: $p \to q$ is false **only** when $p=T$ and $q=F$?
- [ ] For equivalence proofs without truth tables: Always start with the more complex side (LHS) and justify every single step with the exact law name.
- [ ] In quantifier proofs: Remember **EI must be done before UI** to avoid illegal variable reuse!
