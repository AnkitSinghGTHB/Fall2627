# ⚡ CAT-2 HOTS Master Crib — Module 3: Lattices & Boolean Algebra
**Course**: MAT2002 — Discrete Mathematics & Graph Theory  
**Level**: Self-Contained & Fully Visual (From Bedrock Basics to Class Notes & HOTS)  
**Exam Mode**: Open Book / Handwritten Notes Allowed | **Target Score**: 45+ / 50

---

## 🧱 TIER 0: The "Explain Like I'm 5" Bedrock Basics
*(Read this first if you forgot everything from CAT-1 or previous classes)*

### 1. What on Earth is a Hasse Diagram?
A Hasse diagram is just a **ladder drawing** showing which element is "smaller" and which is "bigger":
* If $a$ is connected to $b$ and $b$ is **higher up**, it means **$a \le b$** (or $a$ divides $b$, or $a \subseteq b$).
* You **only walk UPWARDS** along the lines.

#### Visual Hasse Diagram of Divisor Lattice $D_{30}$:
```mermaid
graph BT
    d1["1 (Bottom / Floor / 0)"] --> d2["2"]
    d1 --> d3["3"]
    d1 --> d5["5"]
    d2 --> d6["6"]
    d2 --> d10["10"]
    d3 --> d6
    d3 --> d15["15"]
    d5 --> d10
    d5 --> d15
    d6 --> d30["30 (Top / Ceiling / 1)"]
    d10 --> d30
    d15 --> d30
```

---

### 2. What is Upper Bound, Lower Bound, LUB and GLB?
Imagine two dots on the diagram, say $2$ and $3$.

* **Upper Bound (Common Roof)**: Any dot you can reach going **UP** from both $2$ and $3$.
  * Looking at the diagram above, going up from $2$ and $3$, you can reach $\{6, 30\}$.
* **LUB (Least Upper Bound / Join / $2 \vee 3$)**:
  * Among the roofs $\{6, 30\}$, which is lowest down? **$6$**!
  * So $2 \vee 3 = \text{lcm}(2, 3) = \mathbf{6}$.
* **Lower Bound (Common Basement)**: Any dot you can reach going **DOWN** from both $2$ and $3$.
  * Going down from $2$ and $3$, they both reach $\{1\}$.
* **GLB (Greatest Lower Bound / Meet / $2 \wedge 3$)**:
  * The highest common basement is **$1$**.
  * So $2 \wedge 3 = \gcd(2, 3) = \mathbf{1}$.

---

### 3. What is a LATTICE? (And Why Do Drawings Fail?)
A drawing is a **LATTICE** $\iff$ **EVERY pair has a unique LUB and unique GLB**.

#### The Two Visual Shapes that DESTROY a Lattice:
```mermaid
graph BT
    subgraph FAIL_1 ["Fail 1: Two Separate Roofs (No Unique LUB)"]
    a1["a"] --> c1["c (Roof 1)"]
    a1 --> d1["d (Roof 2)"]
    b1["b"] --> c1
    b1 --> d1
    end

    subgraph FAIL_2 ["Fail 2: Two Separate Basements (No Unique GLB)"]
    c2["a (Basement 1)"]
    d2["b (Basement 2)"]
    c2 --> a2["c"]
    d2 --> a2
    c2 --> b2["d"]
    d2 --> b2
    end
```
* In Fail 1: Dots $a$ and $b$ meet at both $c$ and $d$. Since $c$ and $d$ are side-by-side, **neither is lower** $\implies$ **NOT A LATTICE ❌**.

---

### 4. What is a "Distributive Lattice"? (The Forbidden Sublattices)
Birkhoff's Theorem: A lattice is distributive $\iff$ it contains **NO Diamond ($M_5$) or Pentagon ($N_5$) sublattices**!

```mermaid
graph BT
    subgraph Diamond ["Diamond Lattice M5 (NOT Distributive)"]
    zero1["0"] --> a["a"]
    zero1 --> b["b"]
    zero1 --> c["c"]
    a --> one1["1"]
    b --> one1
    c --> one1
    end

    subgraph Pentagon ["Pentagon Lattice N5 (NOT Distributive)"]
    zero2["0"] --> b2["b"]
    zero2 --> c2["c"]
    b2 --> a2["a"]
    a2 --> one2["1"]
    c2 --> one2
    end
```

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If Question Shows... | It Means This Exact Problem | What You Do (In 5 Seconds) |
| :--- | :--- | :--- |
| A Hasse diagram and asks: *"Is this a lattice?"* | **Lattice Check** | Check non-adjacent side-by-side elements. Look for the "two roofs" or "two basements" trap! |
| $(D_n, \mid)$ and asks: *"Is it a Boolean Algebra?"* | **Divisor Lattice Test** | Factor $n$. If $n$ has ANY squared prime factor ($p^2$ like $4, 9, 12, 18, 36$), say: **NO, $n$ is not square-free!** |
| Hasse diagram and asks: *"Is it distributive?"* | **Distributivity Test** | Search for Pentagon ($N_5$) or Diamond ($M_5$) sub-shapes. Write down the 3 elements where $a \wedge (b \vee c) \ne (a \wedge b) \vee (a \wedge c)$. |
| "Find PDNF and PCNF" for logic proposition | **Normal Forms** | Build truth table. PDNF = rows where $f=1$ (Minterms $\sum m$). PCNF = rows where $f=0$ (Maxterms $\prod M$). |

---

## 📝 TIER 4: Solved Classroom & Exam Archetypes (From Lecture Notes)

### Classroom Problem 1: Hasse Diagram of $D_{18}$ & Complements
*(From Class Notes Page 8)*  
**Question**: Draw the Hasse diagram for $D_{18} = \{1, 2, 3, 6, 9, 18\}$ and find complements of all elements.

```mermaid
graph BT
    e1["1 (Bottom)"] --> e2["2"]
    e1 --> e3["3"]
    e2 --> e6["6"]
    e3 --> e6
    e3 --> e9["9"]
    e6 --> e18["18 (Top)"]
    e9 --> e18
```

**Step-by-Step Complement Evaluation**:
* $1' = 18$ and $18' = 1$
* For element $2$: $\gcd(2, 9) = 1$ and $\text{lcm}(2, 9) = 18 \implies \mathbf{2' = 9}$.
* For element $3$: To get $\text{lcm}(3, x) = 18$, $x$ must be a multiple of $2$ and $9 \implies x \in \{18\}$. But $\gcd(3, 18) = 3 \ne 1$.
  * **Element $3$ has NO COMPLEMENT ❌**.
* **Verdict**: $D_{18}$ is **NOT a Boolean Algebra**!

---

### Classroom Problem 2: Distributivity Check on the 10-Element Lattice
*(From Class Notes Page 6)*  
**Question**: Determine whether the 10-element lattice below is distributive:

```mermaid
graph BT
    zero["0 (Bottom)"] --> a["a"]
    zero --> g["g"]
    a --> b["b"]
    a --> d["d"]
    g --> e["e"]
    g --> f["f"]
    b --> c["c"]
    d --> c
    e --> L["L"]
    f --> L
    c --> one["1 (Top)"]
    L --> one
```

**Step-by-Step Solution**:
1. Select elements $b, d, g$:
   - Join $d \vee g$: The lowest upper bound of $d$ and $g$ is the top element **$1$**.
   - Compute LHS:
     $$\text{LHS} = b \wedge (d \vee g) = b \wedge 1 = \mathbf{b}$$
   - Meet $b \wedge d = \mathbf{a}$.
   - Meet $b \wedge g = \mathbf{0}$.
   - Compute RHS:
     $$\text{RHS} = (b \wedge d) \vee (b \wedge g) = a \vee 0 = \mathbf{a}$$
2. **Comparison**: $\text{LHS} = b \ne \text{RHS} = a$.
3. **Verdict**: **The lattice is NOT distributive ❌**.

---

### Classroom Problem 3: Switching Circuit Simplification & Redraw
**Question**: Simplify the circuit $T = (A \cdot B) + (A \cdot B') + (A' \cdot C)$ and redraw.

#### Original Circuit (6 Switches):
```mermaid
graph LR
    IN[Input] --> B1["Switch A + Switch B"]
    IN --> B2["Switch A + Switch B'"]
    IN --> B3["Switch A' + Switch C"]
    B1 --> OUT[Output]
    B2 --> OUT
    B3 --> OUT
```

#### Minimized Circuit (2 Switches):
* $A \cdot B + A \cdot B' = A(B + B') = A \cdot 1 = A$.
* $T = A + A' C = \mathbf{A + C}$.

```mermaid
graph LR
    IN[Input] --> B1["Switch A"]
    IN --> B2["Switch C"]
    B1 --> OUT[Output]
    B2 --> OUT
```
