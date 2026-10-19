# ⚡ CSE3011: Last-Hour Walk-In Cram Sheet (Exam Hall Ready)

> **Exam Window**: Monday, Oct 19, 2026 | **1:15 PM – 4:15 PM** (Under 1 Hour Remaining!)  
> **Target**: Read this in 10 minutes right outside the hall to refresh the exact syntax, built-ins, and code skeletons.

---

## 🚨 1. Top 10 Syntax Traps (Do NOT Lose Free Marks Here!)

1. **Socket Data is BYTES, Not Strings**:
   * Always encode on send: `sock.sendall(message.encode('utf-8'))`
   * Always decode on receive: `data = sock.recv(1024).decode('utf-8')`
2. **Tkinter Button Callback**:
   * Do **NOT** call the function in `command`:  
     ✅ `tk.Button(root, text="Submit", command=on_click)`  
     ❌ `command=on_click()` *(Calls function immediately at startup!)*
3. **Parameter Placeholders (SQL Injection Prevention)**:
   * **SQLite3**: Uses `?` $\to$ `cur.execute("SELECT * FROM t WHERE id = ?", (val,))`
   * **MySQL**: Uses `%s` $\to$ `cur.execute("SELECT * FROM t WHERE id = %s", (val,))`
   * *Always pass parameters as a tuple, even for a single value: `(val,)`!*
4. **Dual File Context Manager**:
   * Open both in one line:  
     `with open("src.txt", "r") as src, open("dst.txt", "w") as dst:`
5. **Custom Module (`mymath.py`) & Import (CAT-1 Q5)**:
   * File 1 (`mymath.py`):
     ```python
     def factorial(n):
         return 1 if n <= 1 else n * factorial(n - 1)
     ```
   * File 2 (`main.py`):
     ```python
     import mymath
     print(mymath.factorial(5))  # Output: 120
     # OR: from mymath import factorial
     ```
6. **Abstract Class Boilerplate**:
   ```python
   from abc import ABC, abstractmethod
   class Shape(ABC):
       @abstractmethod
       def area(self): pass
   ```
7. **Operator Overloading Return Type**:
   * `__add__(self, other)` must return a **new instance**, not mutate `self`:  
     `return Distance(total_km, remainder_m)`
8. **Loop `else` Clause Execution**:
   * The `else` block on a `for` or `while` loop runs **ONLY IF NO `break` OCCURRED**.
9. **Private Attribute Name Mangling**:
   * `self.__salary` $\to$ accessible outside class only as `obj._ClassName__salary`.
10. **`range()` Bounds**:
    * `range(1, 11)` produces numbers from `1` to `10` (stops at `11 - 1`).

---

## ⚡ 2. The 4 Function Prototypes (Direct from Oct 17 Q2b - 12 Marks)

| Prototype Type | Function Signature & Definition | Usage / Call Example |
|:---|:---|:---|
| **1. No Parameters, No Return** | `def greet():`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print("Hello, Welcome!")` | `greet()` |
| **2. With Parameters, No Return** | `def print_user(name, reg):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print(f"{name} ({reg})")` | `print_user("Ankit", "22BCE1001")` |
| **3. No Parameters, With Return** | `def get_system_status():`<br>&nbsp;&nbsp;&nbsp;&nbsp;`return "SYSTEM_ONLINE"` | `status = get_system_status()` |
| **4. With Parameters, With Return** | `def add(a, b):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`return a + b` | `result = add(10, 20)` |

---

## ⚡ 3. The 4 List Built-ins (Direct from Oct 17 Q7 - 8 Marks)

* **`sorted(iterable, key=..., reverse=...)`**: Returns a **new** sorted list without modifying the original:  
  `nums = [3, 1, 4]; new_nums = sorted(nums)  # new_nums = [1, 3, 4], nums unchanged`
* **`list.append(x)`**: Adds single element `x` to the end of the list in-place:  
  `nums.append(5)  # [3, 1, 4, 5]`
* **`list.remove(x)`**: Removes the **first occurrence** of value `x`; raises `ValueError` if not found:  
  `nums.remove(1)  # [3, 4, 5]`
* **`list.index(x)`**: Returns the zero-based index of the first occurrence of `x`:  
  `idx = nums.index(4)  # idx = 1`

---

## ⚡ 4. Operator Precedence Hierarchy (Quick-Memory Peg)

$$\textbf{P} \to \textbf{E} \to \textbf{M / D / FD / Mod} \to \textbf{A / S} \to \textbf{Shifts} \to \textbf{Bitwise} \to \textbf{Comparisons} \to \textbf{not} \to \textbf{and} \to \textbf{or}$$

1. **Parentheses**: `()`
2. **Exponentiation**: `**` (Right-to-Left: `2 ** 3 ** 2` = $2^9 = 512$)
3. **Multiplication, Division, Floor Division, Modulus**: `*`, `/`, `//`, `%` (Left-to-Right)
4. **Addition, Subtraction**: `+`, `-`
5. **Logical**: `not` (Highest) $\to$ `and` (Middle) $\to$ `or` (Lowest)
   - *Example*: `False or True and False` $\to$ `False or False` $\to$ `False`

---

## ⚡ 5. Minimal 6-Line Skeletons (Ready to Pen Down)

### S1: Tkinter Window with Entry, Button, Label (Unit 5)
```python
import tkinter as tk

root = tk.Tk()
root.title("App")
entry = tk.Entry(root); entry.pack(pady=5)
lbl = tk.Label(root, text="Result"); lbl.pack(pady=5)

def click():
    lbl.config(text=f"Hello {entry.get()}!")

tk.Button(root, text="Submit", command=click).pack(pady=5)
root.mainloop()
```

### S2: TCP Client & Server (Unit 5)
```python
# Server
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 9999)); s.listen(1)
c, addr = s.accept()
msg = c.recv(1024).decode()
c.sendall(msg[::-1].encode())  # Echo reversed string
c.close(); s.close()

# Client
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9999))
s.sendall("Python".encode())
print("Server replied:", s.recv(1024).decode())  # nohtyP
s.close()
```

### S3: SQLite3 / MySQL Parameterized Query (Unit 4)
```python
import sqlite3
conn = sqlite3.connect("test.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS emp (id INT PRIMARY KEY, name TEXT, dept TEXT)")
cur.execute("INSERT OR REPLACE INTO emp VALUES (?, ?, ?)", (101, "Ankit", "CSE"))
conn.commit()
cur.execute("SELECT name FROM emp WHERE dept = ?", ("CSE",))
print(cur.fetchall())  # [('Ankit',)]
conn.close()
```

### S4: Distance Operator Overloading (Unit 3 / CAT-2 Q3)
```python
class Distance:
    def __init__(self, km=0, m=0):
        self.km = km + (m // 1000)
        self.m = m % 1000
    def __add__(self, other):
        total_m = self.m + other.m
        total_km = self.km + other.km + (total_m // 1000)
        return Distance(total_km, total_m % 1000)
    def __str__(self):
        return f"{self.km} km, {self.m} m"
```

### S5: Password Validation Regex (Unit 2 / CAT-1 Q4 / TEE Oct 18 Q6)
```python
import re
def validate_pwd(pwd):
    if len(pwd) > 16: return False
    if not re.search(r"[A-Z]", pwd): return False
    if not re.search(r"[a-z]", pwd): return False
    if not re.search(r"\d", pwd): return False
    if not re.search(r"[$#@]", pwd): return False
    return True
```

---

## 🎯 6. Timing in the Hall (01:15 PM – 04:15 PM)

* **01:15 – 01:55 (40 mins)**: Do **Part B (Q6 to Q10 = 40 Marks)** first! Short, crisp 8-mark questions.
* **01:55 – 03:45 (110 mins)**: Do **Part A (Q1 to Q5 = 60 Marks)**. 20 mins per question. Pick the code-heavy OR option.
* **03:45 – 04:15 (30 mins)**: Review indentation, check loop bounds, and make sure every code snippet has a boxed **`Sample Output:`**!

**You only need 60–64 raw marks for your A Grade.** You are already +3.3 marks ahead of the class. Stay calm, write cleanly, and ace it! 🚀
