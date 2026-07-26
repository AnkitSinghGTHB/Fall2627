# 🔁 Lesson 2 — Flow Control Statements & Loops

> **TL;DR**: Control execution flow using `if-elif-else`, `while`, and `for` loops. Master loop control statements: `break` (exits loop), `continue` (skips current iteration), and `pass` (do-nothing placeholder).

---

## 🔀 Conditionals (`if-elif-else`)

```python
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
else:
    print("Grade C")
```

---

## 🔄 Loops in Python

### 1. `while` Loop
Executes as long as a condition remains `True`.

```python
count = 1
while count <= 3:
    print(count)
    count += 1
```

### 2. `for` Loop with `range()`
Iterates over a sequence of numbers.

- `range(stop)` $\to$ `0` to `stop - 1`
- `range(start, stop)` $\to$ `start` to `stop - 1`
- `range(start, stop, step)` $\to$ `start` to `stop - 1` with `step` increment

```python
for i in range(1, 6, 2):
    print(i) # Prints 1, 3, 5
```

---

## ⏹️ Loop Jump Statements

| Statement | Action |
|---|---|
| `break` | Immediately terminates the loop execution |
| `continue` | Skips the rest of current iteration and moves to next |
| `pass` | Placeholder statement that does nothing (prevents syntax errors) |

---

## 🏋️ Solved Exam Practice Questions

### Question 1 (Loop Output Tracing)
**Trace the output of the following Python snippet:**
```python
for i in range(1, 5):
    if i == 3:
        continue
    if i == 4:
        break
    print(i, end=" ")
```

<details>
<summary>💡 Step-by-Step Solution</summary>

- `i = 1`: `i != 3`, `i != 4` $\implies$ Prints `1 `
- `i = 2`: `i != 3`, `i != 4` $\implies$ Prints `2 `
- `i = 3`: `i == 3` $\implies$ `continue` triggered, skips print!
- `i = 4`: `i == 4` $\implies$ `break` triggered, loop terminates!

**Output:** `1 2 ` ✅
</details>

### Question 2 (Nested Loop Output — Common 5-Marker)
**What will be the output?**
```python
for i in range(3):
    for j in range(i + 1):
        print("*", end="")
    print()
```

<details>
<summary>💡 Step-by-Step Solution</summary>

- `i = 0`: inner loop runs `range(1)` → 1 star → `*`
- `i = 1`: inner loop runs `range(2)` → 2 stars → `**`
- `i = 2`: inner loop runs `range(3)` → 3 stars → `***`

**Output:**
```text
*
**
***
```
✅ (This is the classic "staircase pattern" question)
</details>

### Question 3 (Range Edge Cases — The Gotchas)
**What will be the output?**
```python
print(list(range(5, 2)))
print(list(range(5, 2, -1)))
print(list(range(0)))
```

<details>
<summary>💡 Solution</summary>

1. `range(5, 2)` → empty! (start > stop with default step +1) → `[]`
2. `range(5, 2, -1)` → counts down: `[5, 4, 3]`
3. `range(0)` → nothing to iterate → `[]`

> 🤦 **Exam Trap**: `range(5, 2)` is NOT `[5, 4, 3, 2]`! You need a negative step for that. ✅
</details>

### Question 4 (While-Else — Nobody Expects This)
**What will be the output?**
```python
i = 1
while i < 4:
    print(i, end=" ")
    i += 1
else:
    print("done")
```

<details>
<summary>💡 Solution</summary>

The `while-else` block: the `else` runs when the while condition becomes `False` (NOT when `break` is used).

- Prints: `1 2 3` (normal loop)
- Then condition `4 < 4` is `False` → `else` triggers → prints `done`

**Output:** `1 2 3 done` ✅
</details>

---

## ✅ Quick Self-Check

1. What does `range(2, 10, 3)` generate?
2. Which statement is used as a null operation placeholder in Python?
3. What is the difference between `break` and `continue`?

<details>
<summary>🔑 Answers</summary>

1. `2, 5, 8`.
2. `pass`.
3. `break` exits the loop entirely; `continue` skips only the current iteration.

</details>

---

**⏱️ Study time: ~10 mins | Cheatsheet →** [Python Cheatsheet](./cheatsheet-python.md)
