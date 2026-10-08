# 📘 Module 5: Intermediate Code Generation & Code Optimization

> **Module Focus**: Three Address Code (TAC), Quadruples, Triples, Indirect Triples, Basic Blocks & Leader Rules, Directed Acyclic Graphs (DAG), and Code Optimization Techniques.  
> **Weightage in FAT**: Approx 15–20 Marks.  
> **Faculty Requirement**: Complete Quadruple/Triple tables with exact column headings, and clear before/after code snippets for optimization techniques.

---

## 1. Three Address Code (TAC) Representations (Guaranteed 10 Marks)

Three Address Code is an intermediate language where every instruction has **at most one operator** and **at most three address locations**:
$$x = y \text{ op } z \quad \text{or} \quad x = \text{op } y \quad \text{or} \quad x = y$$

There are **three standard data structure representations** for TAC in a compiler. Evaluators often give an arithmetic expression and ask for all three representations:

```text
┌─────────────────┬────────────────────────────────────────────────────────────────────────┐
│ Representation  │ Key Distinct Feature                                                   │
├─────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 1. Quadruples   │ 4 fields: [op, arg1, arg2, result]. Uses explicit temporary variables. │
│ 2. Triples      │ 3 fields: [op, arg1, arg2]. Refers to results by row index (0), (1).   │
│ 3. Indirect     │ Array of pointers to triples. Allows easy reordering for optimization. │
└─────────────────┴────────────────────────────────────────────────────────────────────────┘
```

---

### 📝 Worked 10-Mark Exam Problem: Quadruples, Triples & Indirect Triples

> **Problem**: Translate the assignment statement into Three Address Code, Quadruples, Triples, and Indirect Triples:
> $$a = b * -c + b * -c$$

#### Step 1: Three Address Code Generation
1. $t_1 = \text{uminus } c$
2. $t_2 = b * t_1$
3. $t_3 = \text{uminus } c$
4. $t_4 = b * t_3$
5. $t_5 = t_2 + t_4$
6. $a = t_5$

---

#### Step 2: Quadruples Table
| Index | `op` | `arg1` | `arg2` | `result` |
| :---: | :---: | :---: | :---: | :---: |
| **(0)** | `uminus` | $c$ | — | $t_1$ |
| **(1)** | `*` | $b$ | $t_1$ | $t_2$ |
| **(2)** | `uminus` | $c$ | — | $t_3$ |
| **(3)** | `*` | $b$ | $t_3$ | $t_4$ |
| **(4)** | `+` | $t_2$ | $t_4$ | $t_5$ |
| **(5)** | `=` | $t_5$ | — | $a$ |

---

#### Step 3: Triples Table (No Temporary Variables)
Results of previous computations are referred to using their table indices `(0)`, `(1)`, etc.:

| Index | `op` | `arg1` | `arg2` |
| :---: | :---: | :---: | :---: |
| **(0)** | `uminus` | $c$ | — |
| **(1)** | `*` | $b$ | `(0)` |
| **(2)** | `uminus` | $c$ | — |
| **(3)** | `*` | $b$ | `(2)` |
| **(4)** | `+` | `(1)` | `(3)` |
| **(5)** | `assign` | $a$ | `(4)` |

---

#### Step 4: Indirect Triples
Consists of an array of pointers `statement[]` pointing to an underlying table of triples. If a code optimizer needs to reorder or delete an instruction, it moves the pointers in the statement array without moving heavy triple records:

```text
Statement Array:            Triples Table:
┌─────────┬────────┐        ┌─────────┬─────────┬─────────┬─────────┐
│ Pointer │ Points │        │  Index  │   op    │  arg1   │  arg2   │
├─────────┼────────┤        ├─────────┼─────────┼─────────┼─────────┤
│   [0]   │  (10)  │───────►│  (10)   │ uminus  │    c    │    —    │
│   [1]   │  (11)  │───────►│  (11)   │    *    │    b    │  (10)   │
│   [2]   │  (12)  │───────►│  (12)   │ uminus  │    c    │    —    │
│   [3]   │  (13)  │───────►│  (13)   │    *    │    b    │  (12)   │
│   [4]   │  (14)  │───────►│  (14)   │    +    │  (11)   │  (13)   │
│   [5]   │  (15)  │───────►│  (15)   │ assign  │    a    │  (14)   │
└─────────┴────────┘        └─────────┴─────────┴─────────┴─────────┘
```

---

## 2. Basic Blocks and Flow Graphs (Guaranteed 5–10 Marks)

### What is a Basic Block?
A Basic Block is a sequence of consecutive three-address statements in which:
1. Control flow enters **only at the first statement** of the block.
2. Control leaves the block **only at the last statement**, without halting or branching anywhere in the middle.

---

### 📜 The 3 Golden Rules to Find Leaders
To partition a sequence of TAC statements into Basic Blocks, first identify the **Leaders**:

1. **Rule 1**: The **first statement** of the three-address code is a Leader.
2. **Rule 2**: Any statement that is the **target of a conditional or unconditional goto** is a Leader.
3. **Rule 3**: Any statement that **immediately follows a conditional or unconditional goto** is a Leader.

> **Forming the Blocks**:  
> For each Leader, its Basic Block consists of the Leader and all subsequent statements up to, but not including, the next Leader or the end of the program.

---

### 📝 Worked Exam Example: Basic Block Partitioning
Given TAC:
```text
(1)  i = 1
(2)  j = 1
(3)  t1 = 10 * i
(4)  t2 = t1 + j
(5)  t3 = 8 * t2
(6)  t4 = t3 - 88
(7)  a[t4] = 0.0
(8)  j = j + 1
(9)  if j <= 10 goto (3)
(10) i = i + 1
(11) if i <= 10 goto (2)
(12) i = 1
(13) t5 = i - 1
(14) if t5 < 10 goto (13)
```

#### Step 1: Identify Leaders
* **Statement (1)**: First statement $\implies$ **Leader** (Rule 1).
* **Statement (2)**: Target of `goto (2)` in line 11 $\implies$ **Leader** (Rule 2).
* **Statement (3)**: Target of `goto (3)` in line 9 $\implies$ **Leader** (Rule 2).
* **Statement (10)**: Follows `if ... goto` in line 9 $\implies$ **Leader** (Rule 3).
* **Statement (12)**: Follows `if ... goto` in line 11 $\implies$ **Leader** (Rule 3).
* **Statement (13)**: Target of `goto (13)` in line 14 $\implies$ **Leader** (Rule 2).

#### Step 2: Construct Basic Blocks
* **Block $B_1$**: Statement (1)
* **Block $B_2$**: Statement (2)
* **Block $B_3$**: Statements (3) through (9)
* **Block $B_4$**: Statements (10) and (11)
* **Block $B_5$**: Statement (12)
* **Block $B_6$**: Statements (13) and (14)

---

## 3. Principal Code Optimization Techniques (5–10 Marks)

Dr. Gaurav Soni frequently asks: *"Explain 4 code optimization techniques with examples."* Provide these exact four with before/after snippets:

### 3.1 Common Subexpression Elimination
An occurrence of an expression $E$ is a common subexpression if $E$ was previously computed and the values of its operands have not changed since the previous computation.

```text
Before Optimization:            After Optimization:
t1 = 4 * i                      t1 = 4 * i
b = a[t1]                       b = a[t1]
t2 = 4 * i  ◄── Repeated!       c = b      ◄── Reused t1 / b!
c = a[t2]
```

---

### 3.2 Dead Code Elimination
Statements that compute values that are never used subsequently, or code that is unreachable, are removed from the compiled output.

```text
Before Optimization:            After Optimization:
x = 5;                          y = 10;
y = 10;                         z = y * 2;
x = 20;  ◄── x=5 was dead!
z = y * 2;
```

---

### 3.3 Constant Folding and Constant Propagation
* **Constant Folding**: Deduce at compile time that the value of an expression is a constant and compute it ahead of time.
* **Constant Propagation**: Replace variables that have known constant values with the constants themselves.

```text
Before Optimization:            After Optimization:
pi = 3.14159;                   area = 314.159;  ◄── Evaluated at compile time!
r = 10;
area = pi * r * r;
```

---

### 3.4 Loop Optimization: Code Motion (Loop Invariant Computation)
Move statements that compute the same value during every iteration of a loop **outside the loop body** into a pre-header:

```text
Before Optimization:            After Loop Code Motion:
while (i <= limit) {            t1 = 2 * PI;     ◄── Moved outside loop!
    x = 2 * PI; ◄── Invariant!  while (i <= limit) {
    y = x * i;                      y = t1 * i;
    i = i + 1;                      i = i + 1;
}                               }
```

---

### 3.5 Strength Reduction (Induction Variables)
Replace an expensive operation (such as multiplication) with a cheaper operation (such as addition) inside a loop:

```text
Before Optimization:            After Strength Reduction:
for (i = 1; i <= 10; i++) {     t = 4;
    t = i * 4;  ◄── Costly!     for (i = 1; i <= 10; i++) {
    a[t] = 0;                       a[t] = 0;
}                                   t = t + 4;  ◄── Cheap addition!
                                }
```
