# ⚡ CAT-2 HOTS Master Crib — Module 3: Lattices & Boolean Algebra
**Course**: MAT2002 — Discrete Mathematics & Graph Theory  
**Level**: Self-Contained / Zero-Assumption (From Bedrock Basics to HOTS)  
**Exam Mode**: Open Book / Handwritten Notes Allowed | **Target Score**: 45+ / 50

---

## 🧱 TIER 0: The "Explain Like I'm 5" Bedrock Basics
*(Read this first if you forgot everything from CAT-1 or previous classes)*

### 1. What on Earth is a Hasse Diagram?
A Hasse diagram is just a **ladder drawing** showing which element is "smaller" and which is "bigger":
* If $a$ is connected to $b$ and $b$ is **higher up**, it means **$a \le b$** (or $a$ divides $b$, or $a \subseteq b$).
* You **only walk UPWARDS** along the lines. Never walk down unless looking for lower things.

```
       30  <-- Highest element (Ceiling / Top / 1)
      / | \
     6 10  15
     | X \ /
     2   3 5
      \ | /
        1  <-- Lowest element (Floor / Bottom / 0)
```

---

### 2. What is Upper Bound, Lower Bound, LUB and GLB?
Imagine two elements (dots) on the diagram, say $a$ and $b$.

#### A. Upper Bound (Common Roof):
* Put one finger on $a$ and one finger on $b$.
* Walk **UP** along the lines from both fingers until they meet at the same dot.
* **ANY dot they can both reach going UP is an "Upper Bound" (Common Roof)**.

#### B. LUB (Least Upper Bound / Join / written as $a \vee b$):
* Among all the common roofs $a$ and $b$ can reach, **which one is the LOWEST down?**
* That single lowest roof is the **LUB**.
* *In divisor math ($D_n$)*: $\text{LUB}(a, b) = \text{lcm}(a, b)$ (Least Common Multiple).

#### C. Lower Bound (Common Basement):
* Put one finger on $a$ and one finger on $b$.
* Walk **DOWN** along the lines until your fingers meet.
* **ANY dot they can both reach going DOWN is a "Lower Bound" (Common Basement)**.

#### D. GLB (Greatest Lower Bound / Meet / written as $a \wedge b$):
* Among all common basements, **which one is HIGHEST up?**
* That single highest basement is the **GLB**.
* *In divisor math ($D_n$)*: $\text{GLB}(a, b) = \gcd(a, b)$ (Greatest Common Divisor).

---

### 3. What is a LATTICE? (The Whole Point of the Chapter)
A drawing is a **LATTICE** if and only if:
> **EVERY SINGLE PAIR of elements has EXACTLY ONE LUB and EXACTLY ONE GLB.**

#### How Does a Drawing FAIL to be a Lattice? (Exam Goldmine):
It fails in only two common ways:
1. **The "Two Separate Roofs" Fail (No unique LUB)**:
   Suppose dots $a$ and $b$ both connect up to dot $c$ AND dot $d$. But $c$ and $d$ are side-by-side (neither is higher than the other).
   * Which one is the lowest common roof? Neither! They are tied at the same level!
   * Result: **No unique LUB $\implies$ NOT A LATTICE ❌**.
2. **The "Two Separate Basements" Fail (No unique GLB)**:
   Suppose dots $c$ and $d$ both connect down to $a$ and $b$, and $a$ and $b$ are side-by-side.
   * Result: **No unique GLB $\implies$ NOT A LATTICE ❌**.

---

### 4. What is a "Bounded Lattice"?
* **Bottom element (called 0)**: A single element that sits below EVERY other element in the whole diagram.
* **Top element (called 1)**: A single element that sits above EVERY other element in the whole diagram.
* If a diagram has two separate lowest points with no single bottom, it is **NOT bounded**.

---

### 5. What is a "Complement" ($a'$)?
In a bounded lattice (with Top $1$ and Bottom $0$), two elements $a$ and $b$ are **complements** of each other if:
1. When you go **UP** to their LUB, you reach the absolute **Top ($1$)**: $a \vee b = 1$.
2. When you go **DOWN** to their GLB, you reach the absolute **Bottom ($0$)**: $a \wedge b = 0$.

*Example in $D_{30}$* (Bottom = $1$, Top = $30$):
* What is the complement of $2$?
  * Need $\text{lcm}(2, x) = 30$ AND $\gcd(2, x) = 1$.
  * Look at $15$: $\text{lcm}(2, 15) = 30$ and $\gcd(2, 15) = 1$.
  * Therefore, **$15$ is the complement of $2$** ($2' = 15$).

---

### 6. What is a "Distributive Lattice"?
* Distributive means $\wedge$ and $\vee$ behave like normal multiplication and addition:
  $$a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$$
* **How to spot non-distributive immediately without doing algebra**:
  Look at your Hasse diagram. If you can spot a **Diamond ($M_5$)** or a **Pentagon ($N_5$)** shape inside it, it is **AUTOMATICALLY NOT DISTRIBUTIVE** (Birkhoff's Theorem).

---

### 7. What is a "Boolean Algebra"?
A Boolean Algebra is just an elite lattice that has **ALL THREE**:
1. **Bounded** (has top $1$ and bottom $0$).
2. **Distributive** (no Diamond or Pentagon sublattices).
3. **Complemented** (EVERY single element has a complement).
* **The Magic Number Rule**: A Boolean Algebra **MUST have $2^k$ elements** ($2, 4, 8, 16, 32, 64\dots$).
  * If a lattice has $5, 6, 7, 9, 10, 12$ elements $\implies$ **IMPOSSIBLE to be a Boolean Algebra!**

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If Question Shows... | It Means This Exact Problem | What You Do (In 5 Seconds) |
| :--- | :--- | :--- |
| A Hasse diagram and asks: *"Is this a lattice?"* | **Lattice Check** | Check non-adjacent side-by-side elements. Look for the "two roofs" or "two basements" trap! |
| $(D_n, \mid)$ and asks: *"Is it a Boolean Algebra?"* | **Divisor Lattice Test** | Factor $n$. If $n$ has ANY squared prime factor ($p^2$ like $4, 9, 12, 18, 36$), say: **NO, $n$ is not square-free!** |
| Hasse diagram and asks: *"Is it distributive?"* | **Distributivity Test** | Search for Pentagon ($N_5$) or Diamond ($M_5$) sub-shapes. If found, write down the 3 elements where $a \wedge (b \vee c) \ne (a \wedge b) \vee (a \wedge c)$. |
| "Find complements of all elements" | **Complement Finding** | For each element $x$, find $y$ such that $x \wedge y = \text{bottom}$ and $x \vee y = \text{top}$. |
| A circuit diagram with switches | **Switching Circuit** | Series = $(\cdot)$, Parallel = $(+)$. Write Boolean equation $\to$ simplify with Boolean rules $\to$ redraw with fewer switches. |

---

## 🛠️ TIER 2: Step-by-Step Execution Recipes

### Recipe 1: How to Prove a Diagram is NOT a Lattice
1. Scan the diagram for two dots $a$ and $b$ that are on the same level (incomparable).
2. Look above them. Do they both connect to dot $c$ AND dot $d$?
3. If neither $c \le d$ nor $d \le c$, write this exact sentence on your answer sheet:
   > *"Elements $a$ and $b$ have two upper bounds $c$ and $d$, but neither $c \le d$ nor $d \le c$. Hence, $\text{LUB}(a, b)$ is not unique. Therefore, the POSET is NOT a lattice."*
4. Full marks awarded in 2 lines.

---

### Recipe 2: The Instant Square-Free Rule for $(D_n, \mid)$
When given positive divisors of $n$:
1. Write prime factorization of $n$:
   - $30 = 2^1 \times 3^1 \times 5^1 \implies$ All powers are $1 \implies$ **Square-Free ✅**.
   - $12 = 2^2 \times 3^1 \implies$ Has $2^2 \implies$ **NOT Square-Free ❌**.
2. **The Verdict**:
   - If square-free $\implies (D_n, \mid)$ is a **Boolean Algebra** with $2^k$ elements.
   - If NOT square-free $\implies$ Element with the squared prime (e.g. $2$ in $D_{12}$) has **NO complement**, so it is **NOT a Boolean Algebra**.

---

### Recipe 3: Testing Distributivity Using the 3-Element Failure Test
If you suspect a lattice is NOT distributive:
1. Find three elements $a, b, c$ forming a Pentagon shape (where $b < a$ and $c$ is incomparable).
2. Calculate LHS: $a \wedge (b \vee c)$.
3. Calculate RHS: $(a \wedge b) \vee (a \wedge c)$.
4. Show $\text{LHS} \ne \text{RHS}$.
5. Write: *"Since $a \wedge (b \vee c) \ne (a \wedge b) \vee (a \wedge c)$, the distributive law does not hold. The lattice is NOT distributive."*

---

## 🚨 TIER 3: Faculty Trap Radar (Where Marks Get Lost)

1. **"Every Hasse diagram is a lattice"**: NO! Most exam questions deliberately give a diagram that has two top peaks or two bottom valleys.
2. **"Finding complement of Top or Bottom"**: The complement of Top ($1$) is ALWAYS Bottom ($0$), and complement of Bottom ($0$) is ALWAYS Top ($1$).
3. **"Can 6 elements form a Boolean Algebra?"**: NEVER. Number of elements must be a power of 2 ($2, 4, 8, 16, 32 \dots$).
4. **"Does every element have a complement in a distributive lattice?"**: NO. A lattice can be distributive without being complemented (e.g., $D_{12}$ is distributive, but element $2$ has no complement).

---

## 📝 TIER 4: Master Solved HOTS Archetypes (Copy Directly into Exam Notebook)

### Archetype 1: Complete Investigation of Divisor Lattice $D_{18}$
**Question**: Let $D_{18}$ be the set of divisors of 18 ordered by divisibility.
1. List the elements and draw the Hasse diagram.
2. Find the LUB and GLB of $\{6, 9\}$.
3. Is $D_{18}$ a bounded lattice? If so, state $0$ and $1$.
4. Find the complements of each element.
5. Is $D_{18}$ a Boolean Algebra? Justify.

**Step-by-Step Solution**:
1. **Elements**: $D_{18} = \{1, 2, 3, 6, 9, 18\}$. Total elements = $6$.
2. **Hasse Diagram**:
   * $1$ connects to $2$ and $3$.
   * $2$ connects to $6$.
   * $3$ connects to $6$ and $9$.
   * $6$ and $9$ connect to $18$.
3. **LUB and GLB of $\{6, 9\}$**:
   * $\text{LUB}(6, 9) = \text{lcm}(6, 9) = \mathbf{18}$.
   * $\text{GLB}(6, 9) = \gcd(6, 9) = \mathbf{3}$.
4. **Boundedness**:
   * Bottom element $0 = \mathbf{1}$ (divides all elements).
   * Top element $1 = \mathbf{18}$ (all elements divide 18).
   * Yes, $D_{18}$ is a **bounded lattice**.
5. **Complements**:
   * For element $1$: $1 \wedge 18 = 1$, $1 \vee 18 = 18 \implies 1' = \mathbf{18}$.
   * For element $18$: $18' = \mathbf{1}$.
   * For element $2$: We need $\text{lcm}(2, x) = 18$ and $\gcd(2, x) = 1$.
     * Divisors with $\text{lcm}(2, x) = 18$ are $x = 9$ or $18$.
     * Check $9$: $\gcd(2, 9) = 1$ and $\text{lcm}(2, 9) = 18 \implies 2' = \mathbf{9}$.
   * For element $3$: We need $\text{lcm}(3, x) = 18$ and $\gcd(3, x) = 1$.
     * To get $\text{lcm}(3, x) = 18$, $x$ must be a multiple of $2$ and $9$ $\implies x \in \{18\}$.
     * But $\gcd(3, 18) = 3 \ne 1$.
     * Thus, element $3$ has **NO COMPLEMENT**!
6. **Is it a Boolean Algebra?**:
   * **NO**, because:
     1. Element $3$ has no complement (not complemented).
     2. The number of elements is $|D_{18}| = 6$, which is not a power of $2$ ($6 \ne 2^k$).
     3. $18 = 2 \times 3^2$ is not square-free.

---

### Archetype 2: Switching Circuit Simplification
**Question**: Write the Boolean transmission function for a circuit containing:
- Branch 1: $A$ in series with $B$
- Branch 2: $A$ in series with $B'$
- Branch 3: $A'$ in series with $C$
all connected in parallel. Simplify the circuit and draw the minimized diagram.

**Step-by-Step Solution**:
1. **Write Transmission Function $T$**:
   * Parallel means OR ($+$). Series means AND ($\cdot$).
   $$T = (A \cdot B) + (A \cdot B') + (A' \cdot C)$$
2. **Apply Distributive Law to first two terms**:
   $$A \cdot B + A \cdot B' = A \cdot (B + B')$$
   Since $B + B' = 1$:
   $$= A \cdot 1 = A$$
3. **Substitute back**:
   $$T = A + (A' \cdot C)$$
4. **Apply Boolean Rule $(X + X'Y = X + Y)$**:
   $$T = A + C$$
5. **Result**:
   * Original circuit: 6 switches.
   * Minimized circuit: Just switch $A$ in parallel with switch $C$ (**2 switches**).
