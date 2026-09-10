# 🐍 Lesson 1 — Python Introduction, Data Types & Operators

> **TL;DR**: Python is an interpreted, high-level, dynamically-typed language created by Guido van Rossum (1991). No semicolons needed! Understand fundamental data types (`int`, `float`, `str`, `bool`) and operators to solve exam code outputs.

---

## 💡 Key Characteristics of Python

1. **Interpreted**: Code is executed line-by-line (no separate compilation step).
2. **Dynamically Typed**: Variable types are determined automatically at runtime (e.g., `x = 10`, no need for `int x = 10;`).
3. **High-Level & Readable**: Uses indentation (whitespace) instead of curly braces `{}`.

---

## 📦 Data Types Summary

| Data Type | Description | Example | Mutable? |
|---|---|---|:---:|
| `int` | Whole integers | `x = 42` | ❌ No |
| `float` | Decimal numbers | `pi = 3.14` | ❌ No |
| `str` | Text string | `name = "VIT"` | ❌ No |
| `bool` | Logical truth | `is_valid = True` | ❌ No |

---

## ⚡ Arithmetic & Logical Operators

### Trick Operators to Remember for Exams:
- **Floor Division (`//`)**: Divides and rounds *down* to the nearest integer.
  - `7 // 2` $\to$ `3`
  - `-7 // 2` $\to$ `-4` *(Rounds towards negative infinity!)*
- **Exponentiation (`**`)**: Power operator.
  - `2 ** 3` $\to$ `8`
- **Modulus (`%`)**: Returns remainder.
  - `7 % 2` $\to$ `1`

---

## 🏋️ Solved Exam Practice Questions

### Question 1 (Tricky Code Output)
**What will be the output of the following Python code?**
```python
a = True
b = False
print(a + a + b * 5)
print(7 // 2 + 7 % 2)
```

<details>
<summary>💡 Step-by-Step Solution</summary>

1. In Python, `True` converts to `1` and `False` converts to `0` in arithmetic operations.
   - `a + a + b * 5` $\implies 1 + 1 + 0 \times 5 = \mathbf{2}$.
2. `7 // 2` $= 3$, `7 % 2` $= 1$.
   - $3 + 1 = \mathbf{4}$.

**Output:**
```text
2
4
```
✅
</details>

### Question 2 (The `is` vs `==` Trap)
**What will be the output?**
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
```

<details>
<summary>💡 Solution</summary>

- `a == b` → `True` (values are the same)
- `a is b` → `False` (they're two different objects in memory!)

> `==` checks **value equality**. `is` checks **identity** (same object in RAM). ✅
</details>

### Question 3 (Type Coercion Surprise)
**What will be the output?**
```python
print(type(3 + 4.0))
print(type(True + 2))
print("ha" * 3)
```

<details>
<summary>💡 Solution</summary>

1. `3 + 4.0` = `7.0` → `<class 'float'>` (int + float = float)
2. `True + 2` = `1 + 2` = `3` → `<class 'int'>` (bool is secretly int!)
3. `"ha" * 3` = `"hahaha"` (string repetition)

```text
<class 'float'>
<class 'int'>
hahaha
```
✅
</details>

### Question 4 (Negative Floor Division — Professor's Favorite)
**What will be the output?**
```python
print(-7 // 2)
print(-7 % 2)
print(10 // 3)
print(10 % 3)
```

<details>
<summary>💡 Solution</summary>

- `-7 // 2` = `-4` (NOT -3! It rounds towards **negative infinity**)
- `-7 % 2` = `1` (because $-7 = (-4) \times 2 + 1$)
- `10 // 3` = `3`
- `10 % 3` = `1`

```text
-4
1
3
1
```


> 🤦 **This is THE trap**: Students write -3 for -7//2. Python rounds DOWN (toward -∞), not toward zero! ✅
</details>

---

## ✅ Quick Self-Check

1. Who developed Python and in what year?
2. What is the output of `-9 // 2` in Python?
3. Are Python strings mutable or immutable?

<details>
<summary>🔑 Answers</summary>

1. Guido van Rossum in 1991.
2. `-5` (rounds down towards negative infinity).
3. **Immutable**.

</details>

---

**⏱️ Study time: ~10 mins | Next →** [02 - Flow Control & Loops](./02-flow-control-and-loops.md)
