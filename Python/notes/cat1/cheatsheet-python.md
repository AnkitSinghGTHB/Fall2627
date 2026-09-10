# ⚡ Python Programming — Master Cheatsheet

> **Print this. One page. All core syntax and exam tricks.**

---

## 🔢 Core Operators & Math

| Operator | What it does | Example |
|---|---|---|
| `//` | Floor Division (rounds down) | `10 // 3 == 3`, `-7 // 2 == -4` |
| `**` | Exponentiation (power) | `2 ** 4 == 16` |
| `%` | Modulus (remainder) | `10 % 3 == 1` |

---

## 🔁 Loops & Control Flow

### `range()` Tricks
```python
list(range(5))        # [0, 1, 2, 3, 4]  (stops BEFORE 5)
list(range(1, 5))     # [1, 2, 3, 4]     (start, stop)
list(range(1, 10, 2)) # [1, 3, 5, 7, 9]  (start, stop, step)
list(range(5, 0, -1)) # [5, 4, 3, 2, 1]  (reverse step)
```

### Loop Keywords
- `break`: Terminate loop completely
- `continue`: Skip the rest of this iteration, move to the next one
- `pass`: Do nothing (used as a syntactic placeholder)
- `for ... else:` The `else` block runs ONLY if the loop finishes normally (without hitting a `break`).

---

## ✂️ Slicing (Lists & Strings)
Syntax: `[start : stop : step]`

```python
s = "PYTHON"
s[0:3]    # "PYT" (indices 0, 1, 2)
s[:4]     # "PYTH" (start to 3)
s[2:]     # "THON" (index 2 to end)
s[-1]     # "N" (last character)
s[::-1]   # "NOHTYP" (reverses the string!)
```

---

## 🧵 Essential String Methods
- `s.split(",")`: Splits string into a list `["a", "b"]` based on comma.
- `",".join(list)`: Joins a list into a string `"a,b"`.
- `s.strip()`: Removes whitespace from both ends.
- `s.replace("old", "new")`: Replaces substrings.
- `s.upper()`, `s.lower()`, `s.title()`: Case conversions.
- `s.find("th")`: Returns index of first occurrence, or `-1` if not found.

---

## 📦 Lists & Dictionaries

### List Methods
```python
L = [1, 2, 3]
L.append(4)     # Adds 4 to end: [1, 2, 3, 4]
L.insert(0, 9)  # Inserts 9 at index 0: [9, 1, 2, 3, 4]
L.pop()         # Removes & returns last item
L.remove(2)     # Removes the FIRST occurrence of value 2
```

### Dictionary Methods
```python
d = {"a": 1, "b": 2}
d.keys()        # dict_keys(['a', 'b'])
d.values()      # dict_values([1, 2])
d.items()       # dict_items([('a', 1), ('b', 2)])
d.get("c", 0)   # Safely get key "c", default to 0 if not found
```

---

## 🚀 List Comprehensions (One-liners)
Syntax: `[expression for item in iterable if condition]`

```python
# Create a list of squares for even numbers from 0 to 9
squares = [x**2 for x in range(10) if x % 2 == 0]
# Result: [0, 4, 16, 36, 64]
```

---

## 💡 Lambda Functions
Anonymous, one-line functions.
Syntax: `lambda arguments: expression`

```python
add = lambda x, y: x + y
print(add(5, 3))  # 8

# Often used with map() or filter()
nums = [1, 2, 3]
doubled = list(map(lambda x: x*2, nums)) # [2, 4, 6]
```

---

## 📁 Basic File I/O
```python
# Reading
with open("file.txt", "r") as f:
    text = f.read()       # Reads entire file
    lines = f.readlines() # Reads into a list of strings

# Writing (overwrites)
with open("file.txt", "w") as f:
    f.write("Hello")
```
