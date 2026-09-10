# ⚡ CAT-2 HOTS Master Crib — Module 3: Lattices & Boolean Algebra
**Course**: MAT2002 — Discrete Mathematics & Graph Theory  
**Coverage**: Module 3 (CO3) | **Exam Mode**: Open Book / Handwritten Notes Allowed  
**Target Score**: 45+ / 50 (S-Grade Boundary)

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

Use this table the second you see a question on the question paper to identify the exact topic:

| If Question Mentions / Shows... | It Means This Exact Topic | Your Immediate Formula / Action |
| :--- | :--- | :--- |
| Hasse Diagram, "Is it a lattice?", LUB, GLB | **Lattice Verification** | Check every pair for unique LUB ($\vee$) and unique GLB ($\wedge$). Look for the 2-top or 2-bottom split! |
| $(D_n, \mid)$, "divisors of $n$", "Is it Boolean Algebra?" | **Divisor Lattice $(D_n, \mid)$** | Check if $n$ is **square-free**. If $n$ has $p^2$, it is **NEVER** a Boolean Algebra! |
| "Distributive lattice", "Prove/Disprove distributive" | **Distributivity Check** | Check for **$M_5$ (Diamond)** or **$N_5$ (Pentagon)** sublattices. If either exists $\rightarrow$ NOT distributive. |
| "Complemented lattice", "Find complement of element $x$" | **Complements in Lattice** | Find $y$ such that $x \wedge y = 0$ (bottom) AND $x \vee y = 1$ (top). |
| "Boolean Algebra as a lattice", "Atoms", $(B, \wedge, \vee, ', 0, 1)$ | **Boolean Algebra Properties** | Number of elements $|B|$ **must be $2^k$**. If $|L| \ne 2^k$, it cannot be Boolean Algebra! |
| "Principal Disjunctive / Conjunctive Normal Form", PDNF, PCNF | **Canonical Normal Forms** | PDNF = Sum of Minterms ($\sum m$); PCNF = Product of Maxterms ($\prod M$). |
| Switching network, contacts, bridge circuit, simplify circuit | **Switching Circuits** | Series = AND ($\cdot$), Parallel = OR ($+$). Simplify via Boolean laws, redraw with fewer switches. |

---

## 🛠️ TIER 2: Deterministic Algorithmic Recipes

### Recipe 3.1: The 10-Second Hasse Diagram Lattice Test
* **Definition**: A POSET $(L, \le)$ is a lattice $\iff \forall a, b \in L$, $\text{LUB}(a,b) = a \vee b$ and $\text{GLB}(a,b) = a \wedge b$ exist and are **unique**.
* **The Shortcut**: You do NOT need to test all pairs! Only test pairs that do **not** have an edge directly connecting them and share multiple upper or lower neighbors.
* **Fail Condition 1 (No Unique LUB)**: If two elements $a, b$ both have upward paths to *both* $c$ and $d$, and neither $c \le d$ nor $d \le c$, then $\text{LUB}(a, b)$ is not unique $\implies$ **NOT a lattice**.
* **Fail Condition 2 (No Unique GLB)**: If two elements $c, d$ both connect downwards to *both* $a$ and $b$, and neither $a \le b$ nor $b \le a$, then $\text{GLB}(c, d)$ is not unique $\implies$ **NOT a lattice**.

---

### Recipe 3.2: The Birkhoff $M_5$ & $N_5$ Distributivity Theorem
> **Theorem**: A lattice $L$ is distributive $\iff$ it contains **NO sublattice isomorphic to $M_5$ (Diamond) or $N_5$ (Pentagon)**.

#### 1. The Diamond Lattice ($M_5$):
* 5 elements: $\{0, a, b, c, 1\}$.
* Top is $1$, bottom is $0$.
* Three incomparable elements $a, b, c$ where:
  $$a \wedge b = a \wedge c = b \wedge c = 0 \quad \text{and} \quad a \vee b = a \vee c = b \vee c = 1$$
* **Distributive Law Failure in $M_5$**:
  $$a \vee (b \wedge c) = a \vee 0 = a$$
  $$(a \vee b) \wedge (a \vee c) = 1 \wedge 1 = 1 \quad \implies a \ne 1 \implies \text{FAILS!}$$

#### 2. The Pentagon Lattice ($N_5$):
* 5 elements: $\{0, a, b, c, 1\}$ with $b < a$, and $c$ incomparable to both.
* **Distributive Law Failure in $N_5$**:
  $$c \vee (a \wedge b) = c \vee b$$
  $$(c \vee a) \wedge (c \vee b) = 1 \wedge (c \vee b) = c \vee b$$
  *Test other direction*: $b \vee (a \wedge c) = b \vee 0 = b$, whereas $(b \vee a) \wedge (b \vee c) = a \wedge (b \vee c) = a \implies b \ne a \implies \text{FAILS!}$

> 📝 **Exam Template**: To prove a given lattice is NOT distributive:  
> Find 3 elements $a, b, c$ and show $a \wedge (b \vee c) \ne (a \wedge b) \vee (a \wedge c)$ with explicit calculation!

---

### Recipe 3.3: The Square-Free Rule for Divisor Lattices $(D_n, \mid)$
In $(D_n, \mid)$:
* Meet $a \wedge b = \gcd(a, b)$
* Join $a \vee b = \text{lcm}(a, b)$
* Bottom element $0 = 1$
* Top element $1 = n$

> ⚡ **Golden Rule for Exams**:  
> $(D_n, \mid)$ is a **Boolean Algebra $\iff n$ is SQUARE-FREE** (i.e., prime factorization has no powers $\ge 2$: $n = p_1 \cdot p_2 \cdots p_k$).
> * Example: $D_{30}$ ($30 = 2 \times 3 \times 5$) $\implies$ Square-free $\implies$ **Boolean Algebra** ($|D_{30}| = 2^3 = 8$ elements).
> * Example: $D_{12}$ ($12 = 2^2 \times 3$) $\implies$ Not square-free $\implies$ **NOT a Boolean Algebra** (element $2$ has no complement because $\text{lcm}(2, x) = 12 \implies x \in \{6, 12\}$, but $\gcd(2, 6) = 2 \ne 1$ and $\gcd(2, 12) = 2 \ne 1$).

---

### Recipe 3.4: Finding Complements in Any Bounded Lattice
For an element $x \in L$:
1. Identify the Least element $0$ and Greatest element $1$.
2. List all elements $y \in L$.
3. Check both conditions:
   $$\text{Condition 1: } x \wedge y = 0$$
   $$\text{Condition 2: } x \vee y = 1$$
4. If such a $y$ exists, $y$ is a complement of $x$.
* **Crucial Property**: In a **Distributive Lattice**, if a complement exists, it is **UNIQUE**. If any element has two distinct complements, the lattice is **NOT distributive**!

---

### Recipe 3.5: Switching Circuits to Boolean Algebra
1. **Parallel Switches** = OR operation ($x + y$).
2. **Series Switches** = AND operation ($x \cdot y$).
3. **Normally Closed Switch** = Inversion ($x'$).
4. **Execution Steps**:
   - Step 1: Trace all independent paths from Input terminal to Output terminal.
   - Step 2: Write Boolean transmission function $T = \sum (\text{Path}_i)$.
   - Step 3: Apply Boolean Algebra theorems (Absorption: $A + AB = A$, Consensus: $AB + A'C + BC = AB + A'C$, De Morgan's).
   - Step 4: Redraw the simplified circuit showing minimum switches.

---

## 🚨 TIER 3: Faculty Trap Radar (Where Students Lose Marks)

1. **The "POSET is automatically a Lattice" Trap**: Students assume that because a Hasse diagram is drawn, it is a lattice. Look at the top and bottom: if there are two maximal elements with no single common upper bound, it is **NOT** a bounded lattice!
2. **The "Number of elements" Trap**: A Boolean Algebra **MUST** have $2^k$ elements ($1, 2, 4, 8, 16, 32\dots$). If a question asks *"Can a lattice of 6 elements be a Boolean Algebra?"*, immediately answer: **NO, because $6 \ne 2^k$**.
3. **The Sublattice Closedness Trap**: A subset $S \subseteq L$ may be a lattice on its own, but **NOT a sublattice of $L$** if the LUB/GLB in $S$ differs from the LUB/GLB in $L$!  
   *Always verify: $\forall a,b \in S$, $a \vee_L b \in S$ and $a \wedge_L b \in S$.*
4. **The Complement of 0 and 1 Trap**: In any bounded lattice, $0' = 1$ and $1' = 0$ always.

---

## 📝 TIER 4: Master Solved HOTS Archetypes (Copy Directly to Notebook)

### Archetype 1: Complete Lattice Analysis on $D_{36}$ vs $D_{30}$
**Question**: Let $D_n$ denote the set of positive divisors of $n$ ordered by divisibility.
1. Draw the Hasse diagram for $D_{30}$ and $D_{36}$.
2. Determine whether each is a Bounded, Distributive, and Complemented lattice.
3. Conclude whether each is a Boolean Algebra.

**Solution Template**:
* **For $D_{30} = \{1, 2, 3, 5, 6, 10, 15, 30\}$**:
  1. Prime factorization: $30 = 2 \times 3 \times 5$ (all exponents are 1 $\implies$ square-free).
  2. Number of elements: $2^3 = 8$.
  3. Bounded: Least element $0 = 1$, Greatest element $1 = 30$.
  4. Distributive: For any divisors, $\gcd(a, \text{lcm}(b,c)) = \text{lcm}(\gcd(a,b), \gcd(a,c))$ holds for all integers $\implies$ Distributive.
  5. Complements:
     * $1' = 30$, $30' = 1$
     * $2' = 30/2 = 15$ ($\gcd(2,15)=1, \text{lcm}(2,15)=30$)
     * $3' = 30/3 = 10$ ($\gcd(3,10)=1, \text{lcm}(3,10)=30$)
     * $5' = 30/5 = 6$ ($\gcd(5,6)=1, \text{lcm}(5,6)=30$)
     * Every element has a unique complement $\implies$ **Complemented**.
  6. **Conclusion**: $D_{30}$ is Bounded + Distributive + Complemented $\implies$ **It is a Boolean Algebra isomorphic to $(\mathcal{P}(\{a,b,c\}), \subseteq)$**.

* **For $D_{36} = \{1, 2, 3, 4, 6, 9, 12, 18, 36\}$**:
  1. Prime factorization: $36 = 2^2 \times 3^2$ (exponents $> 1 \implies$ NOT square-free).
  2. Number of elements: $(2+1)(2+1) = 9 \ne 2^k$.
  3. Check element $2$:
     * We need $\text{lcm}(2, x) = 36 \implies x \in \{18, 36\}$.
     * But $\gcd(2, 18) = 2 \ne 1$ and $\gcd(2, 36) = 2 \ne 1$.
     * Thus, $2$ has **no complement**.
  4. **Conclusion**: $D_{36}$ is a distributive lattice, but **NOT complemented**, and since $|D_{36}| = 9 \ne 2^k$, it **cannot be a Boolean Algebra**.

---

### Archetype 2: Distributivity Proof / Disproof via Pentagon Sublattice
**Question**: Let $L = \{0, a, b, c, d, 1\}$ be a lattice whose Hasse diagram has covers:
$0 \prec a, 0 \prec b, a \prec c, b \prec d, c \prec 1, d \prec 1$, with an additional cross-edge $b \prec c$.
Show whether $L$ is a modular and distributive lattice.

**Solution Template**:
1. Identify the pentagon subset: $\{0, b, c, d, 1\}$.
   - Notice $b < c$.
   - Test element $d$ which is incomparable to $c$ and $b$:
     $$d \wedge c = 0 \quad (\text{their only common lower bound is } 0)$$
     $$d \vee b = 1 \quad (\text{their join is } 1)$$
2. Compute the distributive test expressions:
   $$\text{LHS} = d \vee (b \wedge c) = d \vee b = 1$$
   $$\text{RHS} = (d \vee b) \wedge (d \vee c) = 1 \wedge 1 = 1$$
   *Now check dual*:
   $$\text{LHS} = b \vee (c \wedge d) = b \vee 0 = b$$
   $$\text{RHS} = (b \vee c) \wedge (b \vee d) = c \wedge 1 = c$$
3. Since $\text{LHS} = b$ and $\text{RHS} = c$, and $b \ne c$:
   $$b \vee (c \wedge d) \ne (b \vee c) \wedge (b \vee d)$$
4. **Conclusion**: The distributive law fails. The sublattice $\{0, b, c, d, 1\}$ is isomorphic to $N_5$ (Pentagon). Therefore, $L$ is **NOT a distributive lattice**.

---

### Archetype 3: Switching Circuit Rigorous Simplification
**Question**: Find the Boolean transmission function $T(x, y, z)$ for the switching circuit with paths:
* Path 1: $x$ in series with $y$ in series with $z$
* Path 2: $x$ in series with $y'$ in series with $z$
* Path 3: $x'$ in series with $y$ in series with $z$
* Path 4: $x$ in series with $z'$
Simplify the circuit using Boolean Algebra laws and draw the simplified circuit.

**Solution Template**:
1. **Write transmission expression**:
   $$T = (x \cdot y \cdot z) + (x \cdot y' \cdot z) + (x' \cdot y \cdot z) + (x \cdot z')$$
2. **Apply Distributive / Factoring Law on Terms 1 & 2**:
   $$x \cdot y \cdot z + x \cdot y' \cdot z = x \cdot z \cdot (y + y')$$
   Since $y + y' = 1$:
   $$= x \cdot z \cdot 1 = x \cdot z$$
3. **Substitute back into $T$**:
   $$T = x \cdot z + x' \cdot y \cdot z + x \cdot z'$$
4. **Group Terms 1 & 4 ($x \cdot z + x \cdot z'$)**:
   $$x \cdot z + x \cdot z' = x \cdot (z + z') = x \cdot 1 = x$$
5. **Substitute back**:
   $$T = x + x' \cdot y \cdot z$$
6. **Apply Absorption / Distributive Law ($A + A'B = A + B$)**:
   Here $A = x$, $B = y \cdot z$:
   $$T = x + y \cdot z$$
7. **Circuit Interpretation**:
   * Original circuit: 11 switches.
   * Simplified circuit: Switch $x$ in parallel with the series pair $(y \text{ and } z)$.
   * Total switches: **3 switches** (Reduction of 8 switches!).
