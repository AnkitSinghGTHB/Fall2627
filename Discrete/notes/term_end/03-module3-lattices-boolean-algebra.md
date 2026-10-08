# 📘 Module 3: Lattices & Boolean Algebra (From Zero to Mastery)

> **Module Focus**: Lattice Definition & Verification, Sub-lattices, Bounded/Complemented/Distributive Lattices, Birkhoff's $M_5/N_5$ Test, Boolean Algebra, PDNF/PCNF Normal Forms, and Switching Circuits.  
> **Weightage in FAT**: Approx 20 Marks.  
> **Why Students Lost Marks in CAT-2**: Distributivity checks done blindly, confusing subsets that are lattices with sub-lattices, and algebraic errors in PDNF/PCNF. Here, we fix all of them with foolproof algorithms!

---

## 1. What is a Lattice? (The 2-Minute Intuition)

### 1.1 Definition
A poset $(L, \le)$ is called a **Lattice** if and only if **EVERY pair of elements $\{a, b\}$ has**:
1. A **Unique Greatest Lower Bound (GLB)**, denoted as **Meet**: $$a \wedge b = \text{GLB}(a, b)$$
2. A **Unique Least Upper Bound (LUB)**, denoted as **Join**: $$a \vee b = \text{LUB}(a, b)$$

```text
    VISUALIZING MEET AND JOIN IN A HASSE DIAGRAM:

            LUB(a, b) = a ∨ b   ◄── First common node where paths upwards MEET
                 /    \
                a      b
                 \    /
            GLB(a, b) = a ∧ b   ◄── First common node where paths downwards MEET
```

---

### 1.2 The 3-Step Exam Algorithm: "Is this Poset a Lattice?"

When an exam question gives you a Hasse diagram and asks: *"Is this poset a lattice?"*:

* **Step 1: Check the Ends (Immediate Disqualification Test)**:
  * Does the finite poset have a **unique single bottom element**? (If it has multiple minimal elements $\to$ **NOT a lattice!**)
  * Does the finite poset have a **unique single top element**? (If it has multiple maximal elements $\to$ **NOT a lattice!**)
* **Step 2: Look for the "Double Roof" or "Double Floor" Trap**:
  * If two elements $a$ and $b$ branch upwards to two different nodes $c$ and $d$ with **no single lowest node** between them, then $\text{LUB}(a, b)$ does not exist $\to$ **NOT a lattice!**
* **Step 3: State the Pair and Conclusion**:
  * To prove it is NOT a lattice, you only need to show **ONE counterexample pair** where LUB or GLB fails to exist or is not unique!

```text
    EXAMPLE OF A NON-LATTICE (Double Top Trap):
           e       f     ◄── Two upper bounds for {c, d}!
            \     / \
             \   /   \
               c       d
                \     /
                   b
                   │
                   a
    Why is this NOT a lattice?
    Look at pair {c, d}: Their upper bounds are {e, f}.
    Neither e ≤ f nor f ≤ e. There is NO LEAST upper bound!
    Therefore, LUB(c, d) does NOT exist. G is NOT a lattice!
```

---

## 2. Sub-Lattices: The #1 Trap Question in Exams

### 2.1 The Definition
Let $(L, \wedge, \vee)$ be a lattice. A non-empty subset $S \subseteq L$ is called a **Sub-Lattice** of $L$ if and only if $S$ is **closed under the meet ($\wedge$) and join ($\vee$) operations of $L$**:
$$\forall a, b \in S \implies (a \wedge_L b) \in S \quad \text{AND} \quad (a \vee_L b) \in S$$

### 2.2 The Trap: "A Lattice in its own right" vs "A Sub-Lattice"
> ⚠️ **CRITICAL EXAM TRAP**:  
> A subset $S$ can be a lattice by itself under its own induced order, but **FAIL to be a sub-lattice of $L$** because its meet or join computed in $L$ falls outside $S$!

#### 📝 Worked Exam Example (VIT Past Paper):
> Let $L = D_{30} = \{1, 2, 3, 5, 6, 10, 15, 30\}$.  
> Consider the subset $S = \{1, 2, 3, 30\}$. Is $S$ a sub-lattice of $D_{30}$?
>
> **Solution**:  
> Check if $S$ is closed under the operations of $L$:
> * Pick $2, 3 \in S$:
>   * In $L$, the join is the least common multiple: $2 \vee_L 3 = \operatorname{lcm}(2, 3) = \mathbf{6}$.
>   * But is $6 \in S$? **NO! $6 \notin S$.**
> * Since $2 \vee_L 3 \notin S$, $S$ is **NOT closed under the join operation of $L$**.
> * **Conclusion: $S$ is NOT a sub-lattice of $D_{30}$**, even though $S$ as an isolated 4-element poset has a top and bottom!

---

## 3. Special Classes of Lattices

### 3.1 Bounded Lattice
A lattice $L$ is **Bounded** if it has:
* A least element, denoted **$0$** (or bottom), such that $0 \le a$ for all $a \in L$ ($a \wedge 0 = 0, a \vee 0 = a$).
* A greatest element, denoted **$1$** (or top), such that $a \le 1$ for all $a \in L$ ($a \wedge 1 = a, a \vee 1 = 1$).
* *Fact*: Every finite lattice is bounded!

---

### 3.2 Complemented Lattice
In a bounded lattice $(L, \wedge, \vee, 0, 1)$, an element $b \in L$ is called a **complement** of $a \in L$ if:
$$a \wedge b = 0 \quad \text{AND} \quad a \vee b = 1$$

* A lattice is **Complemented** if **EVERY element in $L$ has at least one complement**.
* **Key Observations**:
  * $0$ and $1$ are always complements of each other ($0 \wedge 1 = 0, 0 \vee 1 = 1$).
  * In general lattices, an element can have **zero complements, exactly one complement, or multiple complements**!

---

### 3.3 Distributive Lattice
A lattice $L$ is **Distributive** if the meet and join operations distribute over each other:
1. $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$ for all $a, b, c \in L$.
2. $a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c)$ for all $a, b, c \in L$.

#### 🔑 The 2 Unbreakable Theorems of Distributive Lattices:
1. **Uniqueness of Complements**: In a distributive lattice, if an element $a$ has a complement, **that complement is strictly UNIQUE**! (It can never have two different complements).
2. **Cancellation Law**: If $a \vee b = a \vee c$ AND $a \wedge b = a \wedge c$, then **$b = c$**.

---

### 3.4 Birkhoff's $M_5$ and $N_5$ Sub-Lattice Test (How to Check Distributivity in 5 Seconds!)

Instead of testing thousands of algebraic combinations $(a \wedge (b \vee c))$, use the famous **Birkhoff Theorem**:

> **Birkhoff's Characterization Theorem**:  
> A lattice $L$ is **Distributive** if and only if it does **NOT contain a sub-lattice isomorphic to either $M_5$ (The Diamond Lattice) or $N_5$ (The Pentagon Lattice)**.

```text
       THE TWO "FORBIDDEN" NON-DISTRIBUTIVE SUB-LATTICES:

       M₅ (Diamond Lattice)              N₅ (Pentagon Lattice)
                 1                                 1
              /  │  \                            /   \
             /   │   \                          b     │
            a    b    c                         │     c
             \   │   /                          a     │
              \  │  /                            \   /
                 0                                 0
   Non-distributive because:          Non-distributive because:
   b has TWO complements (a & c)!    b ∧ (a ∨ c) = b ∧ 1 = b
   a ∧ (b ∨ c) = a ∧ 1 = a           (b ∧ a) ∨ (b ∧ c) = a ∨ 0 = a
   (a ∧ b) ∨ (a ∧ c) = 0 ∨ 0 = 0     Since b ≠ a, distributivity fails!
   a ≠ 0! Distributivity fails!
```

* **Exam Recipe**: If you spot either a 3-way diamond ($M_5$) or a lopsided pentagon ($N_5$) inside your Hasse diagram that forms a sub-lattice, immediately cite Birkhoff's Theorem to declare the lattice **Non-Distributive**!

---

## 4. Boolean Algebra: The Ultimate Goal

### 4.1 Definition
A **Boolean Algebra** is a lattice $(B, \wedge, \vee, ', 0, 1)$ that is:
1. **Distributive**
2. **Complemented**

Because it is distributive, **every element has a UNIQUE complement** $a'$.

---

### 4.2 The Square-Free Rule for Divisor Posets $(D_n, \mid)$

One of the most frequent exam questions is: *"Is $(D_n, \mid)$ a Boolean algebra?"*

> 🏆 **THE SQUARE-FREE SHORTCUT RULE**:  
> The divisor lattice $(D_n, \mid)$ is a **Boolean Algebra** if and only if **$n$ is SQUARE-FREE** (i.e., its prime factorization contains no repeated prime factors, no $p^2$).
>
> Furthermore, any finite Boolean algebra has exactly **$2^k$ elements** (where $k$ is the number of distinct prime factors).

* **$D_{30}$**: $30 = 2 \times 3 \times 5$.  
  All prime exponents are 1 (square-free).  
  Number of elements = $2^3 = 8$.  
  $\implies \mathbf{D_{30}\text{ IS a Boolean Algebra!}}$
* **$D_{12}$**: $12 = 2^2 \times 3$.  
  Has $2^2$ (not square-free!).  
  $\implies \mathbf{D_{12}\text{ is NOT a Boolean Algebra}}$ (in fact, $2$ has no complement in $D_{12}$ because $2 \wedge x = 1 \implies x \in \{1, 3\}$, but $2 \vee 1 = 2 \ne 12$ and $2 \vee 3 = 6 \ne 12$).
* **$D_{70}$**: $70 = 2 \times 5 \times 7$. Square-free $\implies \mathbf{D_{70}\text{ IS a Boolean Algebra!}}$
* **$D_{36}$**: $36 = 2^2 \times 3^2$. Not square-free $\implies \mathbf{D_{36}\text{ is NOT a Boolean Algebra!}}$

---

## 5. Boolean Functions & Normal Forms (PDNF & PCNF)

Every Boolean function of $n$ variables can be written in two canonical (standardized) forms.

### 5.1 Definitions: Minterms vs Maxterms

| Concept | Minterm ($m$) | Maxterm ($M$) |
| :--- | :--- | :--- |
| **Form** | Product (AND) of all variables: $x \wedge y \wedge z$ | Sum (OR) of all variables: $x \vee y \vee z$ |
| **Variable Convention**| Uncomplemented = $1$, Complemented ($'$) = $0$ | Uncomplemented = $0$, Complemented ($'$) = $1$ |
| **Output Value** | Evaluates to **1** for exactly ONE input row | Evaluates to **0** for exactly ONE input row |
| **Full Expansion Name**| **PDNF** (Principal Disjunctive Normal Form) / SOP | **PCNF** (Principal Conjunctive Normal Form) / POS |

---

### 5.2 Converting to PDNF and PCNF (The Exam Recipe)

You can find PDNF and PCNF via two methods:

#### Method A: The Truth Table Method (Safest, 100% Error-Free)
1. Construct the truth table for the given formula.
2. **For PDNF (Sum of Minterms $\sum m$)**: Look at all rows where the output is **$1$ (True)**. Write the minterm for each row and join them with $\vee$.
3. **For PCNF (Product of Maxterms $\prod M$)**: Look at all rows where the output is **$0$ (False)**. Write the maxterm for each row and join them with $\wedge$.

#### Method B: Algebraic Expansion
* To convert a term missing variable $y$ into minterms: Multiply by $(y \vee y')$.  
  *Example*: $x = x \wedge (y \vee y') = (x \wedge y) \vee (x \wedge y')$.
* To convert a term missing variable $y$ into maxterms: Add $(y \wedge y')$.  
  *Example*: $x = x \vee (y \wedge y') = (x \vee y) \wedge (x \vee y')$.

---

### 📝 Worked Past Exam Problem: Obtain PDNF and PCNF
> **Question**: Obtain the Principal Disjunctive Normal Form (PDNF) and Principal Conjunctive Normal Form (PCNF) for the Boolean expression:  
> $$f(x, y, z) = (x \wedge y) \vee (\neg x \wedge z)$$
>
> **Solution**:
> Let's expand algebraically to minterms:
> 1. First term: $(x \wedge y)$ is missing variable $z$.  
>    $$(x \wedge y) \wedge (z \vee \neg z) = (x \wedge y \wedge z) \vee (x \wedge y \wedge \neg z) = m_7 \vee m_6$$
> 2. Second term: $(\neg x \wedge z)$ is missing variable $y$.  
>    $$(\neg x \wedge z) \wedge (y \vee \neg y) = (\neg x \wedge y \wedge z) \vee (\neg x \wedge \neg y \wedge z) = m_3 \vee m_1$$
> 3. Combine and remove duplicates:  
>    $$f(x, y, z) = m_1 \vee m_3 \vee m_6 \vee m_7$$  
>    $$\mathbf{\text{PDNF} = (\neg x \wedge \neg y \wedge z) \vee (\neg x \wedge y \wedge z) \vee (x \wedge y \wedge \neg z) \vee (x \wedge y \wedge z) = \sum m(1, 3, 6, 7)}$$
>
> 4. **Obtaining PCNF**:  
>    The maxterms are simply all indices from $\{0, 1, 2, 3, 4, 5, 6, 7\}$ that are **NOT** in the PDNF!  
>    Missing indices: $\{0, 2, 4, 5\}$.  
>    $$\mathbf{\text{PCNF} = \prod M(0, 2, 4, 5) = M_0 \wedge M_2 \wedge M_4 \wedge M_5}$$  
>    Where:
>    * $M_0 = (x \vee y \vee z)$
>    * $M_2 = (x \vee \neg y \vee z)$
>    * $M_4 = (\neg x \vee y \vee z)$
>    * $M_5 = (\neg x \vee y \vee \neg z)$

---

## 6. Switching Circuits: Design & Minimization

In electrical circuits:
* **Switches in Series**: Current flows only if BOTH switches are closed $\implies A \cdot B$ (Conjunction $\wedge$).
* **Switches in Parallel**: Current flows if EITHER switch is closed $\implies A + B$ (Disjunction $\vee$).

```text
        SWITCHES IN SERIES:                    SWITCHES IN PARALLEL:
                                                     ┌──[ A ]──┐
        ───[ A ]─────[ B ]───                  ───┤         ├───
             (A ∧ B)                                 └──[ B ]──┘
                                                       (A ∨ B)
```

### 📝 Worked Past Exam Problem: Circuit Simplification
> **Question**: Simplify the switching expression:  
> $$E = A \cdot B + A \cdot (B + C) + B \cdot (B + C)$$  
> and draw the simplified circuit.
>
> **Solution**:
> 1. Apply absorption and distributive laws:  
>    $E = A B + (A B + A C) + (B B + B C)$
> 2. $B B = B$, so:  
>    $E = A B + A C + B + B C$
> 3. Notice $B + B C = B$ (Absorption law):  
>    $E = A B + A C + B$
> 4. Notice $A B + B = B$ (Absorption law):  
>    $E = B + A C$
>
> **Simplified Expression**: $E = B + (A \cdot C)$  
> **Circuit**: Switch $B$ in parallel with the series pair $(A \text{ and } C)$.  
> (Original circuit required 6 switches; simplified circuit requires only 3 switches!).

---

## 💡 Module 3 Summary Checklist & Exam Traps

- [ ] Does a poset have multiple tops or bottoms? Immediately declare: **NOT a lattice**!
- [ ] For sub-lattice check: Never just say "it looks like a lattice". You must show that join ($\operatorname{lcm}$) and meet ($\gcd$) of any two elements remain inside the subset.
- [ ] To test distributivity fast: Look for $M_5$ (diamond) or $N_5$ (pentagon) sub-lattices.
- [ ] For $D_n$ Boolean algebra: Check if $n$ is square-free ($D_{12}$ is not, $D_{30}$ is!).
- [ ] For PCNF from PDNF: Just list the complement set of minterm indices as maxterm indices!
