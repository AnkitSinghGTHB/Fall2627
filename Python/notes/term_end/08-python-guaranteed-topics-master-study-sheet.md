# 🎯 CSE3011: Python Programming — Official TEE Master Study Sheet
## Full 100-Mark Model Question Paper & Exam-Ready Solutions with Sample Outputs

> **Course**: CSE3011 — Python Programming | **Slot**: B11+B12 | **Faculty**: Prof. Vaishnavi S  
> **Exam Pattern**: Section A (5 × 12 Marks = 60M, with internal `OR`) + Section B (5 × 8 Marks = 40M)  
> **Pre-TEE Standing**: **63.4 / 70.0** (+3.3 marks ahead of class average!)  
> **Target for A Grade**: **60–64 / 100** | **Target for S Grade**: **85–88+ / 100**

---

# ========================================================
# SECTION A: 5 QUESTIONS × 12 MARKS = 60 MARKS
# (1 Question from Each Unit with Internal Choice `OR`)
# ========================================================

---

## UNIT 1: PYTHON FUNDAMENTALS & CONTROL FLOW

### Q1 [OPTION 1] (12 Marks)

#### Part (a) [6 Marks]
**Differentiate between Python 2 and Python 3 across core features. Provide a clean comparison table and concise explanations.**

##### Answer:
Python 3 was introduced as a backwards-incompatible major release designed to rectify fundamental design flaws of Python 2.

```
+---------------------------------------------------------------------------------------------------+
| Feature               | Python 2 (Legacy)                 | Python 3 (Modern Standard)            |
+-----------------------+-----------------------------------+---------------------------------------+
| Print Mechanism       | Statement: print "Hello"          | Function: print("Hello", end="\n")    |
| Integer Division      | 5 / 2 = 2 (Truncates integer)     | 5 / 2 = 2.5 (Float); 5 // 2 = 2 (Floor)|
| Default String Type   | ASCII (Unicode needed u'text')    | Unicode UTF-8 (Bytes need b'data')    |
| User Input Function   | raw_input() for str, input() eval | raw_input() removed; input() gives str|
| Range Memory Model    | range() allocated full list       | xrange() merged; range() is iterator  |
| Exception Syntax      | except Exception, e:              | except Exception as e:                |
+---------------------------------------------------------------------------------------------------+
```

* **Core Keywords for Marks**:
  1. **Unicode Default**: Python 3 prevents string encoding/decoding bugs by treating all string literals as native **Unicode**.
  2. **True Division**: The `/` operator always returns a float; `//` is required for integer floor division.
  3. **Memory Iterator**: In Python 3, `range()` yields values lazily on-demand with $O(1)$ memory consumption.

---

#### Part (b) [6 Marks]
**Write a Python program to multiply two user-input matrices $A$ ($m \times k$) and $B$ ($k \times n$) and check if the resultant matrix is an Identity matrix.**

##### Answer:

```python
def matrix_multiplication():
    # 1. Input dimensions
    r1 = int(input("Enter rows of Matrix A: "))
    c1 = int(input("Enter cols of Matrix A: "))
    r2 = int(input("Enter rows of Matrix B: "))
    c2 = int(input("Enter cols of Matrix B: "))

    # Dimension validation check
    if c1 != r2:
        print("Error: Columns of A must equal rows of B for multiplication!")
        return

    # 2. Input Matrix A
    print("Enter Matrix A row-wise (space-separated):")
    A = [[int(x) for x in input().split()] for _ in range(r1)]

    # 3. Input Matrix B
    print("Enter Matrix B row-wise (space-separated):")
    B = [[int(x) for x in input().split()] for _ in range(r2)]

    # 4. Matrix Multiplication: C[i][j] = sum(A[i][k] * B[k][j])
    C = [[0 for _ in range(c2)] for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                C[i][j] += A[i][k] * B[k][j]

    print("\nResultant Matrix C:")
    for row in C:
        print(row)

    # 5. Identity Matrix Verification (Square + 1 on diagonal + 0 elsewhere)
    is_identity = (r1 == c2)
    if is_identity:
        for i in range(r1):
            for j in range(c2):
                if i == j and C[i][j] != 1:
                    is_identity = False
                elif i != j and C[i][j] != 0:
                    is_identity = False

    if is_identity:
        print("\nResult: Matrix C is an IDENTITY Matrix.")
    else:
        print("\nResult: Matrix C is NOT an Identity Matrix.")

if __name__ == "__main__":
    matrix_multiplication()
```

##### Sample Input & Output:
```text
Sample Input:
Enter rows of Matrix A: 2
Enter cols of Matrix A: 2
Enter rows of Matrix B: 2
Enter cols of Matrix B: 2
Enter Matrix A row-wise (space-separated):
1 0
0 1
Enter Matrix B row-wise (space-separated):
1 0
0 1

Sample Output:
Resultant Matrix C:
[1, 0]
[0, 1]

Result: Matrix C is an IDENTITY Matrix.
```

---

### [OR] Q1 [OPTION 2] (12 Marks)

#### Part (a) [6 Marks]
**Differentiate between Value Equality (`==`) and Identity Equality (`is`). Explain integer caching in Python ($-5$ to $256$) with memory diagrams.**

##### Answer:

```
               [Variable a] ───┐
                               ├───▶ Memory Address: 0x1040 [ Integer: 100 ]
               [Variable b] ───┘
               (a is b is TRUE: same id(a) and id(b))

               [List x] ───────▶ Memory Address: 0x5010 [ 1, 2, 3 ]
               [List y] ───────▶ Memory Address: 0x8090 [ 1, 2, 3 ]
               (x == y is TRUE: identical contents)
               (x is y is FALSE: different memory locations)
```

1. **Value Equality (`==`)**: Compares the **data values** stored inside two objects. It internally invokes the dunder method `__eq__()`.
2. **Identity Equality (`is`)**: Checks whether two variables point to the **exact same memory address** (`id(a) == id(b)`).
3. **Small Integer Caching Mechanism**:
   * CPython pre-allocates an array of integer objects in memory for numbers in the range **$[-5, 256]$** at interpreter startup.
   * Any assignment within this range binds directly to the existing cached memory block.
   * Outside this range, Python creates distinct heap objects.

```python
# Integer Caching Demonstration Code
x = 250
y = 250
print("x == y:", x == y)
print("x is y:", x is y)

p = 500
q = 500
print("p == q:", p == q)
print("p is q:", p is q)

l1 = [1, 2]
l2 = [1, 2]
print("l1 == l2:", l1 == l2)
print("l1 is l2:", l1 is l2)
```

##### Sample Input & Output:
```text
Sample Output:
x == y: True
x is y: True
p == q: True
p is q: False
l1 == l2: True
l1 is l2: False
```

---

#### Part (b) [6 Marks]
**Write a Python program to find all Armstrong numbers within a given range $[L, U]$ and display their sum and total count.**

##### Answer:

```python
def find_armstrong_numbers(lower, upper):
    """
    An Armstrong number of n digits is equal to the sum
    of the nth power of its individual digits.
    Example: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    """
    armstrong_list = []

    for num in range(lower, upper + 1):
        if num < 0:
            continue
        digits = str(num)
        n = len(digits)
        digit_sum = sum(int(d) ** n for d in digits)
        
        if digit_sum == num:
            armstrong_list.append(num)

    print(f"Armstrong numbers between {lower} and {upper}: {armstrong_list}")
    print(f"Total Count = {len(armstrong_list)}")
    print(f"Total Sum   = {sum(armstrong_list)}")

# Execute function
find_armstrong_numbers(1, 500)
```

##### Sample Input & Output:
```text
Sample Input:
lower = 1, upper = 500

Sample Output:
Armstrong numbers between 1 and 500: [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
Total Count = 13
Total Sum   = 1339
```

---

## UNIT 2: COLLECTIONS, FUNCTIONS & REGEX

### Q2 [OPTION 1] (12 Marks)

#### Part (a) [6 Marks]
**Explain the LEGB variable scoping rule in Python with a clear schematic diagram. Show code examples using the `global` and `nonlocal` keywords.**

##### Answer:

```
        +-------------------------------------------------------------+
        |                 BUILT-IN (B)                                |
        |                 e.g., print, len, range, sum                |
        |   +-----------------------------------------------------+   |
        |   |             GLOBAL (G)                              |   |
        |   |             Module-level variables                  |   |
        |   |   +---------------------------------------------+   |   |
        |   |   |         ENCLOSING (E)                       |   |   |
        |   |   |         Outer nested function scope         |   |   |
        |   |   |   +-------------------------------------+   |   |   |
        |   |   |   |     LOCAL (L)                       |   |   |   |
        |   |   |   |     Inside current function/lambda  |   |   |   |
        |   |   |   +-------------------------------------+   |   |   |
        |   |   +---------------------------------------------+   |   |
        |   +-----------------------------------------------------+   |
        +-------------------------------------------------------------+
        Search Order: Local ──▶ Enclosing ──▶ Global ──▶ Built-in
```

* **`global` keyword**: Declares that a variable inside a function refers to the module-level scope, allowing modification of global state.
* **`nonlocal` keyword**: Used inside nested functions to bind to the variable in the nearest **enclosing (outer function)** scope.

```python
x = "Global"

def outer_func():
    y = "Enclosing"

    def inner_func():
        nonlocal y          # Modifies enclosing variable y
        global x            # Modifies global variable x
        y = "Modified Enclosing"
        x = "Modified Global"

    inner_func()
    print("Outer y:", y)    # Shows modification by inner_func

outer_func()
print("Global x:", x)       # Shows modification by inner_func
```

##### Sample Input & Output:
```text
Sample Output:
Outer y: Modified Enclosing
Global x: Modified Global
```

---

#### Part (b) [6 Marks]
**Write a Python program using regular expressions to validate student emails (must end with `@vitbhopal.ac.in`) and extract 10-digit Indian mobile numbers (starting with 6, 7, 8, or 9) from an input paragraph.**

##### Answer:

```python
import re

def extract_vit_credentials(paragraph):
    # 1. Regex pattern for 10-digit Indian mobile numbers
    phone_pattern = r"\b[6-9]\d{9}\b"
    phones = re.findall(phone_pattern, paragraph)

    # 2. Regex pattern for official VIT Bhopal student email IDs
    email_pattern = r"\b[a-zA-Z0-9._%+-]+@vitbhopal\.ac\.in\b"
    emails = re.findall(email_pattern, paragraph)

    print("--- Extracted Valid Details ---")
    print("Found Phone Numbers:", phones)
    print("Found Student Emails:", emails)

# Test Execution
sample_text = """
Contact Ankit at 9876543210 or alternate 5123456789.
Send projects to ankit.s2026@vitbhopal.ac.in or external test@gmail.com.
Faculty contact: 8123456789.
"""
extract_vit_credentials(sample_text)
```

##### Sample Input & Output:
```text
Sample Input:
Contact Ankit at 9876543210 or alternate 5123456789.
Send projects to ankit.s2026@vitbhopal.ac.in or external test@gmail.com.
Faculty contact: 8123456789.

Sample Output:
--- Extracted Valid Details ---
Found Phone Numbers: ['9876543210', '8123456789']
Found Student Emails: ['ankit.s2026@vitbhopal.ac.in']
```

---

### [OR] Q2 [OPTION 2] (12 Marks)

#### Part (a) [6 Marks]
**Explain `*args` and `**kwargs` syntax with variable-length argument passing. Write a function `calculate_stats(*scores, **options)` that computes statistics based on options.**

##### Answer:
* **`*args` (Non-Keyword Arguments)**: Packs an arbitrary number of positional arguments into a **tuple**.
* **`**kwargs` (Keyword Arguments)**: Packs arbitrary key-value named parameters into a **dictionary**.

```python
def calculate_stats(*scores, **options):
    if not scores:
        return "No scores provided."

    results = {}
    if options.get("average", True):
        results["Average"] = sum(scores) / len(scores)
    if options.get("highest", False):
        results["Highest"] = max(scores)
    if options.get("lowest", False):
        results["Lowest"] = min(scores)
    if options.get("rounded", False):
        results = {k: round(v, 2) for k, v in results.items()}

    return results

# Calling function with positional and keyword arguments
output1 = calculate_stats(78, 85, 92, 88, highest=True, lowest=True, rounded=True)
print("Stats 1:", output1)

output2 = calculate_stats(50, 60, 70, highest=True)
print("Stats 2:", output2)
```

##### Sample Input & Output:
```text
Sample Input:
calculate_stats(78, 85, 92, 88, highest=True, lowest=True, rounded=True)
calculate_stats(50, 60, 70, highest=True)

Sample Output:
Stats 1: {'Average': 85.75, 'Highest': 92, 'Lowest': 78}
Stats 2: {'Average': 60.0, 'Highest': 70}
```

---

#### Part (b) [6 Marks]
**Write a Python program that takes a sentence, removes duplicate words, prints words in alphabetical order, and identifies the longest word.**

##### Answer:

```python
import re

def process_sentence(sentence):
    # 1. Clean punctuation and split into words
    words = re.findall(r"\b[a-zA-Z]+\b", sentence.lower())

    if not words:
        print("Empty sentence!")
        return

    # 2. Remove duplicates using set
    unique_words = list(set(words))

    # 3. Sort alphabetically
    sorted_words = sorted(unique_words)

    # 4. Find the longest word
    longest_word = max(unique_words, key=len)

    print("Unique Words (Alphabetical):", sorted_words)
    print(f"Longest Word: '{longest_word}' (Length: {len(longest_word)})")

# Test Execution
process_sentence("Python is great and python is dynamic programming language")
```

##### Sample Input & Output:
```text
Sample Input:
"Python is great and python is dynamic programming language"

Sample Output:
Unique Words (Alphabetical): ['and', 'dynamic', 'great', 'is', 'language', 'programming', 'python']
Longest Word: 'programming' (Length: 11)
```

---

## UNIT 3: OBJECT-ORIENTED PROGRAMMING & EXCEPTIONS

### Q3 [OPTION 1] (12 Marks)

**Design an Object-Oriented system for a 2D Vector / Complex Number class supporting operator overloading. Implement `__init__`, `__add__` (addition), `__sub__` (subtraction), `__mul__` (dot product), and `__str__` (formatted string representation). Demonstrate complete working with sample objects.**

##### Answer:

```python
class Vector2D:
    """
    Represents a mathematical 2D vector (x, y)
    supporting vector arithmetic through operator overloading.
    """
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    # Overloading '+' operator: v1 + v2
    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        raise TypeError("Operand must be of type Vector2D")

    # Overloading '-' operator: v1 - v2
    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        raise TypeError("Operand must be of type Vector2D")

    # Overloading '*' operator: v1 * v2 (Dot Product) or v1 * scalar
    def __mul__(self, other):
        if isinstance(other, Vector2D):
            # Dot Product: x1*x2 + y1*y2
            return (self.x * other.x) + (self.y * other.y)
        elif isinstance(other, (int, float)):
            # Scalar Multiplication
            return Vector2D(self.x * other, self.y * other)
        raise TypeError("Multiplication requires Vector2D or scalar number")

    # Overloading string conversion: print(v)
    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

    # Overloading equality: v1 == v2
    def __eq__(self, other):
        return isinstance(other, Vector2D) and self.x == other.x and self.y == other.y

# --- Execution Test ---
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print("v1           =", v1)
print("v2           =", v2)
print("v1 + v2      =", v1 + v2)
print("v1 - v2      =", v1 - v2)
print("Dot Product  =", v1 * v2)
print("Scalar Mult  =", v1 * 3)
```

##### Sample Input & Output:
```text
Sample Input:
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

Sample Output:
v1           = Vector2D(3.0, 4.0)
v2           = Vector2D(1.0, 2.0)
v1 + v2      = Vector2D(4.0, 6.0)
v1 - v2      = Vector2D(2.0, 2.0)
Dot Product  = 11.0
Scalar Mult  = Vector2D(9.0, 12.0)
```

---

### [OR] Q3 [OPTION 2] (12 Marks)

#### Part (a) [6 Marks]
**What is Method Resolution Order (MRO)? Explain C3 Linearization with a classic Diamond Inheritance hierarchy (`A -> B, C -> D`) and show the step-by-step trace of `D.mro()`.**

##### Answer:

```
                            [ Class A ]
                             /       \
                            /         \
                     [ Class B ]   [ Class C ]
                            \         /
                             \       /
                            [ Class D ]
                    class D(B, C): pass
```

1. **Definition of MRO**: Method Resolution Order defines the exact sequence in which Python searches base classes when looking for a method or attribute on an object instance.
2. **C3 Linearization Algorithm**:
   Python uses the **C3 algorithm** enforcing three rules:
   * **Subclasses come before superclasses** ($D$ before $B$ and $C$).
   * **Maintains base class declaration order** (if `class D(B, C)`, $B$ is checked before $C$).
   * **Monotonicity**: If $B$ precedes $A$ in one class resolution, it must precede $A$ across all derived classes.

```
Step-by-step C3 derivation for D(B, C):
  L[A] = [A, object]
  L[B] = [B, A, object]
  L[C] = [C, A, object]
  L[D] = [D] + merge(L[B], L[C], [B, C])
       = [D] + merge([B, A, object], [C, A, object], [B, C])
  Pick B (head of L[B], not in tail of any other list):
       = [D, B] + merge([A, object], [C, A, object], [C])
  Pick C (head of L[C], A is in tail of L[C], so cannot pick A yet):
       = [D, B, C] + merge([A, object], [A, object])
  Pick A:
       = [D, B, C, A, object]
```

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print("D MRO Sequence:", [cls.__name__ for cls in D.mro()])
```

##### Sample Input & Output:
```text
Sample Output:
D MRO Sequence: ['D', 'B', 'C', 'A', 'object']
```

---

#### Part (b) [6 Marks]
**Design an abstract class `Polygon` using Python's `abc` module with abstract methods `area()` and `perimeter()`. Implement derived concrete classes `Rectangle` and `Triangle`.**

##### Answer:

```python
from abc import ABC, abstractmethod
import math

class Polygon(ABC):
    """Abstract Base Class enforcing interface contract"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Heron's Formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# Instantiate and verify
rect = Rectangle(10, 5)
tri = Triangle(3, 4, 5)
print(f"Rectangle -> Area: {rect.area()}, Perimeter: {rect.perimeter()}")
print(f"Triangle  -> Area: {tri.area()}, Perimeter: {tri.perimeter()}")
```

##### Sample Input & Output:
```text
Sample Input:
rect = Rectangle(10, 5)
tri = Triangle(3, 4, 5)

Sample Output:
Rectangle -> Area: 50, Perimeter: 30
Triangle  -> Area: 6.0, Perimeter: 12
```

---

## UNIT 4: FILE HANDLING & DATABASE PROGRAMMING

### Q4 [OPTION 1] (12 Marks)

**Write a complete Python program using the `sqlite3` module to manage a `Students` database (`university.db`). Implement table creation, parameterized insertion, querying records with $\text{CGPA} \ge 9.0$, and safe resource cleanup inside `finally`.**

##### Answer:

```python
import sqlite3

def run_student_db_manager():
    conn = None
    try:
        # 1. Connect to SQLite database file
        conn = sqlite3.connect("university.db")
        cursor = conn.cursor()

        # 2. Create Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                reg_no TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                cgpa REAL
            )
        """)

        # 3. Parameterized INSERT (Safe against SQL Injection attacks)
        student_records = [
            ("26BCE1001", "Ankit Singh", 9.25),
            ("26BCE1002", "Rahul Sharma", 8.40),
            ("26BCE1003", "Priya Nair", 9.10),
            ("26BCE1004", "Thomas Alva", 7.85)
        ]
        cursor.executemany("""
            INSERT OR REPLACE INTO students (reg_no, name, cgpa)
            VALUES (?, ?, ?)
        """, student_records)

        # Commit transaction to disk
        conn.commit()
        print("Records inserted successfully.")

        # 4. Query students with CGPA >= 9.0
        threshold = 9.0
        cursor.execute("""
            SELECT reg_no, name, cgpa
            FROM students
            WHERE cgpa >= ?
            ORDER BY cgpa DESC
        """, (threshold,))

        high_achievers = cursor.fetchall()
        print(f"\nStudents with CGPA >= {threshold}:")
        for reg, name, cgpa in high_achievers:
            print(f"- [{reg}] {name}: CGPA = {cgpa}")

    except sqlite3.Error as e:
        print(f"Database error encountered: {e}")
        if conn:
            conn.rollback()
    finally:
        # 5. Clean up connection
        if conn:
            conn.close()
            print("Database connection closed cleanly.")

if __name__ == "__main__":
    run_student_db_manager()
```

##### Sample Input & Output:
```text
Sample Output:
Records inserted successfully.

Students with CGPA >= 9.0:
- [26BCE1001] Ankit Singh: CGPA = 9.25
- [26BCE1003] Priya Nair: CGPA = 9.1
Database connection closed cleanly.
```

---

### [OR] Q4 [OPTION 2] (12 Marks)

#### Part (a) [6 Marks]
**Differentiate between `seek()` and `tell()` methods in file pointer navigation. Explain the three `whence` modes ($0, 1, 2$) with an illustrative diagram.**

##### Answer:

```
File Byte Stream: [B0][B1][B2][B3][B4][B5][B6][B7][B8][B9]
                  ▲                       ▲              ▲
                  │                       │              │
             whence=0 (Start)          Current         whence=2 (End)
                                       whence=1
```

* **`f.tell()`**: Returns an integer giving the file pointer's current byte offset position from the beginning of the file.
* **`f.seek(offset, whence)`**: Repositions the internal read/write pointer.
  - **`whence = 0` (`os.SEEK_SET`)**: Move relative to the **beginning** of the file (Default). `f.seek(0, 0)` rewinds to start.
  - **`whence = 1` (`os.SEEK_CUR`)**: Move relative to the **current** pointer location (requires binary mode `'rb'`).
  - **`whence = 2` (`os.SEEK_END`)**: Move relative to the **end** of the file (requires binary mode `'rb'`).

```python
# Demonstrating seek and tell
with open("sample.bin", "wb") as f:
    f.write(b"0123456789ABCDEF")

with open("sample.bin", "rb") as f:
    print("Initial Position:", f.tell())
    f.seek(5, 0)                          # Move to index 5
    print("After seek(5, 0):", f.tell())
    print("Read 3 bytes:", f.read(3))     # Reads bytes at 5, 6, 7
    f.seek(-4, 2)                         # Move 4 bytes before end
    print("Tail bytes:", f.read(4))
```

##### Sample Input & Output:
```text
Sample Output:
Initial Position: 0
After seek(5, 0): 5
Read 3 bytes: b'567'
Tail bytes: b'CDEF'
```

---

#### Part (b) [6 Marks]
**Write a Python program to read `input.txt`, count the occurrences of each word (ignoring case and punctuation), and write the word-frequency results sorted in descending order into `output.txt`.**

##### Answer:

```python
import re

def word_frequency_pipeline(input_path="input.txt", output_path="output.txt"):
    try:
        # 1. Read input file
        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read().lower()

        # 2. Clean punctuation and tokenize words
        words = re.findall(r"\b[a-zA-Z0-9]+\b", content)

        # 3. Count frequencies
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1

        # 4. Sort by count descending, then alphabetically
        sorted_freq = sorted(freq.items(), key=lambda item: (-item[1], item[0]))

        # 5. Write to output.txt
        with open(output_path, "w", encoding="utf-8") as out:
            out.write("Word Frequency Analysis Report\n")
            out.write("==============================\n")
            for word, count in sorted_freq:
                out.write(f"{word:<15}: {count}\n")

        print(f"Analysis complete. Results saved to '{output_path}'.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found!")

# Execute analysis
word_frequency_pipeline()
```

##### Sample Input & Output:
```text
Sample Input File (input.txt):
Python is powerful. Python is easy, and python is fast!

Sample Output File (output.txt):
Word Frequency Analysis Report
==============================
is             : 3
python         : 3
and            : 1
easy           : 1
fast           : 1
powerful       : 1

Terminal Console Message:
Analysis complete. Results saved to 'output.txt'.
```

---

## UNIT 5: GUI, MULTITHREADING & NETWORK PROGRAMMING

### Q5 [OPTION 1] (12 Marks)

**Design a desktop Student Registration Form using `tkinter`. The GUI must contain: Name Entry, Gender Radiobuttons, Courses Checkbuttons, and a Submit Button that validates non-empty inputs and displays a confirmation alert box. Use the `grid()` layout manager.**

##### Answer:

```python
import tkinter as tk
from tkinter import messagebox

def launch_registration_form():
    root = tk.Tk()
    root.title("VIT Student Registration Form")
    root.geometry("360x320")
    root.configure(padx=15, pady=15)

    # 1. Title Header
    tk.Label(root, text="Student Registration", font=("Helvetica", 14, "bold")).grid(
        row=0, column=0, columnspan=2, pady=10
    )

    # 2. Name Field
    tk.Label(root, text="Full Name:").grid(row=1, column=0, sticky="w", pady=5)
    entry_name = tk.Entry(root, width=22)
    entry_name.grid(row=1, column=1, sticky="w", pady=5)

    # 3. Gender Radio Buttons
    tk.Label(root, text="Gender:").grid(row=2, column=0, sticky="w", pady=5)
    gender_var = tk.StringVar(value="Male")
    frame_gender = tk.Frame(root)
    frame_gender.grid(row=2, column=1, sticky="w")
    tk.Radiobutton(frame_gender, text="Male", variable=gender_var, value="Male").pack(side="left")
    tk.Radiobutton(frame_gender, text="Female", variable=gender_var, value="Female").pack(side="left")

    # 4. Courses Check Buttons
    tk.Label(root, text="Courses:").grid(row=3, column=0, sticky="nw", pady=5)
    py_var = tk.BooleanVar()
    ml_var = tk.BooleanVar()
    iot_var = tk.BooleanVar()
    frame_courses = tk.Frame(root)
    frame_courses.grid(row=3, column=1, sticky="w")
    tk.Checkbutton(frame_courses, text="Python Programming", variable=py_var).pack(anchor="w")
    tk.Checkbutton(frame_courses, text="Machine Learning", variable=ml_var).pack(anchor="w")
    tk.Checkbutton(frame_courses, text="Internet of Things", variable=iot_var).pack(anchor="w")

    # 5. Submit Action Callback
    def on_submit():
        name = entry_name.get().strip()
        if not name:
            messagebox.showwarning("Validation Error", "Student Name cannot be empty!")
            return

        selected_courses = []
        if py_var.get(): selected_courses.append("Python")
        if ml_var.get(): selected_courses.append("ML")
        if iot_var.get(): selected_courses.append("IoT")

        details = (
            f"Registration Confirmed!\n\n"
            f"Name: {name}\n"
            f"Gender: {gender_var.get()}\n"
            f"Courses: {', '.join(selected_courses) if selected_courses else 'None'}"
        )
        messagebox.showinfo("Success", details)

    # 6. Submit Button
    btn_submit = tk.Button(
        root, text="Submit Registration", command=on_submit,
        bg="#007ACC", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5
    )
    btn_submit.grid(row=4, column=0, columnspan=2, pady=20)

    root.mainloop()

if __name__ == "__main__":
    launch_registration_form()
```

##### Sample GUI Visual Layout & Dialog Output:
```text
Sample GUI Window Layout:
+-------------------------------------------------------+
|             VIT Student Registration Form        [X]  |
+-------------------------------------------------------+
|                 Student Registration                  |
|                                                       |
|  Full Name: [ Ankit Singh                         ]   |
|                                                       |
|  Gender:    (o) Male      ( ) Female                  |
|                                                       |
|  Courses:   [X] Python Programming                    |
|             [X] Machine Learning                      |
|             [ ] Internet of Things                    |
|                                                       |
|             [   Submit Registration   ]               |
+-------------------------------------------------------+

Sample Pop-up Alert Box on Clicking Submit:
+-------------------------------------------------------+
| Success                                          [X]  |
+-------------------------------------------------------+
|  Registration Confirmed!                              |
|                                                       |
|  Name: Ankit Singh                                    |
|  Gender: Male                                         |
|  Courses: Python, ML                                  |
|                                                       |
|                        [  OK  ]                       |
+-------------------------------------------------------+
```

---

### [OR] Q5 [OPTION 2] (12 Marks)

#### Part (a) [6 Marks]
**What is the Global Interpreter Lock (GIL) in Python? Explain why multithreading improves I/O-bound performance but does not speed up CPU-bound tasks.**

##### Answer:

```
+-----------------------------------------------------------------------------------------+
|                  CPU-BOUND THREADS VS I/O-BOUND THREADS UNDER THE GIL                   |
+-----------------------------------------------------------------------------------------+

CPU-Bound (Matrix Math, Heavy Computation):
Thread 1: [ ACQUIRES GIL ] ──[ Computing Bytecode ]──▶ [ Must Release GIL ]
Thread 2:                                             [ ACQUIRES GIL ] ──[ Computing ]
Result: Serialized execution on 1 CPU core + switching overhead (No parallel speedup!)

I/O-Bound (Network, File I/O, Database Queries):
Thread 1: [ ACQUIRES GIL ] ──▶ [ Initiates Network Socket Read ──▶ RELEASES GIL ] ──[ Waiting ]
Thread 2:                      [ ACQUIRES GIL IMMEDIATELY ] ──▶ [ Processing Data ]
Result: True concurrency! Multiple threads wait on background I/O simultaneously.
```

* **Core Keywords**:
  1. **CPython Mutex**: The GIL is a mutual exclusion lock protecting CPython internal memory structures against concurrent race conditions in reference counting.
  2. **I/O GIL Release**: Python automatically releases the GIL whenever a thread blocks on OS-level I/O operations (file reading, socket communication).
  3. **Multiprocessing Alternative**: To achieve parallel multi-core speedup for CPU-bound programs, Python uses the `multiprocessing` module, which spawns independent OS processes with separate Python interpreter instances.

---

#### Part (b) [6 Marks]
**Write a multi-threaded Python banking application where two threads attempt concurrent withdrawals from a shared balance. Use `threading.Lock` to prevent race conditions.**

##### Answer:

```python
import threading
import time

class BankAccount:
    def __init__(self, initial_balance=1000):
        self.balance = initial_balance
        self.lock = threading.Lock()

    def withdraw(self, amount, user_name):
        print(f"[{user_name}] Attempting to withdraw ₹{amount}...")
        
        # Acquire lock using context manager (ensures automatic release)
        with self.lock:
            print(f"[{user_name}] Lock acquired. Verifying balance...")
            time.sleep(0.1)  # Simulate processing delay
            if self.balance >= amount:
                self.balance -= amount
                print(f"[{user_name}] Withdrawal SUCCESS. Remaining Balance: ₹{self.balance}")
            else:
                print(f"[{user_name}] Withdrawal FAILED: Insufficient Funds! (Balance: ₹{self.balance})")

# Test Concurrent Execution
account = BankAccount(1000)
t1 = threading.Thread(target=account.withdraw, args=(700, "User-A"))
t2 = threading.Thread(target=account.withdraw, args=(500, "User-B"))

t1.start()
t2.start()
t1.join()
t2.join()

print(f"\nFinal Verified Account Balance: ₹{account.balance}")
```

##### Sample Input & Output:
```text
Sample Output:
[User-A] Attempting to withdraw ₹700...
[User-A] Lock acquired. Verifying balance...
[User-B] Attempting to withdraw ₹500...
[User-A] Withdrawal SUCCESS. Remaining Balance: ₹300
[User-B] Lock acquired. Verifying balance...
[User-B] Withdrawal FAILED: Insufficient Funds! (Balance: ₹300)

Final Verified Account Balance: ₹300
```

---

# ========================================================
# SECTION B: 5 QUESTIONS × 8 MARKS = 40 MARKS
# (1 Question from Each Unit, Direct without Subparts)
# ========================================================

---

### Q6 (Unit 1 - 8 Marks)
**Explain the loop `else` construct in Python. Write a program to check whether a given integer $N$ is prime or composite using `for-else`, explaining why the `else` block executes only on normal completion without `break`.**

##### Answer:

```
                for item in iterable:
                        │
                  [ Condition? ] ──YES──▶ break ────▶ Exits Loop Entirely
                        │                              (Skips else block!)
                       NO
                        │
                (Loop finishes naturally)
                        │
                        ▼
                [ ELSE BLOCK EXECUTES ]
```

1. **Mechanics**:
   * In Python, loops (`for` and `while`) feature an optional `else` block.
   * **Rule**: The `else` block executes **if and only if** the loop terminates normally (exhausts all iterable elements or while condition becomes False) **without encountering a `break` statement**.
   * If a `break` is triggered, the loop terminates immediately, bypassing the `else` block entirely.

```python
def check_prime(n):
    if n <= 1:
        print(f"{n} is neither prime nor composite.")
        return

    # Check divisors up to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} is COMPOSITE (divisible by {i}).")
            break  # Exits loop, skips else block
    else:
        # Executes only if no divisor was found (loop completed without break)
        print(f"{n} is a PRIME number.")

# Testing
check_prime(29)
check_prime(35)
```

##### Sample Input & Output:
```text
Sample Input 1:
check_prime(29)

Sample Output 1:
29 is a PRIME number.

Sample Input 2:
check_prime(35)

Sample Output 2:
35 is COMPOSITE (divisible by 5).
```

---

### Q7 (Unit 2 - 8 Marks)
**Write a Python function `analyze_string(s)` that finds: (1) character frequencies, (2) the first non-repeating character, and (3) returns the string with duplicate characters removed preserving original order.**

##### Answer:

```python
def analyze_string(s):
    # 1. Frequency calculation using standard dict
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # 2. First non-repeating character
    first_non_repeating = None
    for char in s:
        if freq[char] == 1:
            first_non_repeating = char
            break

    # 3. Remove duplicates while preserving original order
    seen = set()
    deduped_chars = []
    for char in s:
        if char not in seen:
            seen.add(char)
            deduped_chars.append(char)
    deduped_string = "".join(deduped_chars)

    print("--- String Analysis Report ---")
    print("Original String       :", s)
    print("Character Frequencies :", freq)
    print("First Non-Repeating   :", first_non_repeating if first_non_repeating else "None")
    print("Deduplicated String   :", deduped_string)

# Execute test
analyze_string("swiss")
```

##### Sample Input & Output:
```text
Sample Input:
analyze_string("swiss")

Sample Output:
--- String Analysis Report ---
Original String       : swiss
Character Frequencies : {'s': 3, 'w': 1, 'i': 1}
First Non-Repeating   : w
Deduplicated String   : swi
```

---

### Q8 (Unit 3 - 8 Marks)
**Explain the `try-except-else-finally` exception handling mechanism. Write a program demonstrating file parsing with division, explaining execution paths when an exception occurs vs when no exception occurs.**

##### Answer:

```
               [ try block ] ──────── Executes risky code
                    │
         Exception occurred?
            ├─── YES ──▶ [ except block ] ──▶ Handles error
            └─── NO  ──▶ [ else block ]   ──▶ Runs ONLY if NO exception occurred
                                │
                                ▼
                       [ finally block ] ───▶ ALWAYS runs (Cleanup / Close resources)
```

```python
def parse_and_divide(filename):
    f = None
    try:
        f = open(filename, "r")
        content = f.read().strip()
        num = int(content)
        result = 100 / num

    except FileNotFoundError:
        print("Except: File was not found on disk.")
    except ZeroDivisionError:
        print("Except: Cannot divide by zero in calculation.")
    except ValueError:
        print("Except: File content is not a valid integer.")

    else:
        # Executes ONLY when NO exception was raised in try
        print(f"Else: Operation successful! 100 / {num} = {result}")

    finally:
        # ALWAYS executes regardless of outcome
        if f and not f.closed:
            f.close()
            print("Finally: File descriptor closed safely.")
        else:
            print("Finally: Execution completed cleanup.")
```

##### Sample Input & Output:
```text
Scenario A (Valid file 'num.txt' containing '5'):
Else: Operation successful! 100 / 5 = 20.0
Finally: File descriptor closed safely.

Scenario B (File 'missing.txt' does not exist):
Except: File was not found on disk.
Finally: Execution completed cleanup.

Scenario C (File 'zero.txt' containing '0'):
Except: Cannot divide by zero in calculation.
Finally: File descriptor closed safely.
```

---

### Q9 (Unit 4 - 8 Marks)
**Differentiate between `pickle` and `json` serialization in Python across data formats, interoperability, supported data types, and security. Provide working code snippets.**

##### Answer:

```
+---------------------------------------------------------------------------------------------------+
| Feature               | JSON Module                       | Pickle Module                         |
+-----------------------+-----------------------------------+---------------------------------------+
| Serialization Format  | Human-readable plain text (UTF-8) | Binary byte stream (Python-specific)  |
| Interoperability      | Universal across all languages    | Python-only; incompatible with others |
| Supported Data Types  | Basic (dict, list, str, num, bool)| Arbitrary Python class instances, fn  |
| Security Implication  | Safe against malicious payload    | Severe vulnerability: can run shell   |
+---------------------------------------------------------------------------------------------------+
```

```python
import json
import pickle

data = {"student": "Ankit", "semester": "Fall2627", "cgpa": 9.25}

# 1. JSON Demonstration
json_string = json.dumps(data, indent=2)        # Serialize to text
restored_from_json = json.loads(json_string)    # Deserialize from text

# 2. Pickle Demonstration
pickle_bytes = pickle.dumps(data)               # Serialize to binary bytes
restored_from_pickle = pickle.loads(pickle_bytes)# Deserialize from binary bytes

print("Restored JSON:", restored_from_json)
print("Restored PKL :", restored_from_pickle)
```

##### Sample Input & Output:
```text
Sample Input:
data = {"student": "Ankit", "semester": "Fall2627", "cgpa": 9.25}

Sample Output:
Restored JSON: {'student': 'Ankit', 'semester': 'Fall2627', 'cgpa': 9.25}
Restored PKL : {'student': 'Ankit', 'semester': 'Fall2627', 'cgpa': 9.25}
```

---

### Q10 (Unit 5 - 8 Marks)
**Write a complete TCP Client-Server communication program in Python using the `socket` module. The server receives a string, converts it to uppercase, and sends it back to the client.**

##### Answer:

```
             SERVER SOCKET                                CLIENT SOCKET
        socket(AF_INET, SOCK_STREAM)               socket(AF_INET, SOCK_STREAM)
                   │                                             │
             bind(('localhost', 9999))                           │
                   │                                             │
             listen(5)                                           │
                   │                                             │
             accept() ◀────── [ TCP 3-Way Handshake ] ────── connect(('localhost', 9999))
                   │                                             │
             recv(1024) ◀──── "hello python" ─────────────── send(b"hello python")
                   │                                             │
             send(b"HELLO PYTHON") ────────────────────────▶ recv(1024)
                   │                                             │
             close()                                           close()
```

```python
# --- SERVER CODE (server.py) ---
import socket

def run_server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(("localhost", 9999))
    server_sock.listen(1)
    print("Server listening on port 9999...")

    conn, addr = server_sock.accept()
    print(f"Connected by {addr}")

    data = conn.recv(1024).decode("utf-8")
    print(f"Received from client: '{data}'")

    response = data.upper()
    conn.send(response.encode("utf-8"))

    conn.close()
    server_sock.close()


# --- CLIENT CODE (client.py) ---
def run_client():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(("localhost", 9999))

    message = "vit bhopal python tee"
    print(f"Sending to server: '{message}'")
    client_sock.send(message.encode("utf-8"))

    response = client_sock.recv(1024).decode("utf-8")
    print(f"Echo response received from server: '{response}'")

    client_sock.close()
```

##### Sample Input & Output:
```text
Server Terminal:
Server listening on port 9999...
Connected by ('127.0.0.1', 54321)
Received from client: 'vit bhopal python tee'

Client Terminal:
Sending to server: 'vit bhopal python tee'
Echo response received from server: 'VIT BHOPAL PYTHON TEE'
```

---

# 🎯 EXAM HALL SCORING CHECKLIST FOR PROF. VAISHNAVI S

1. **Clean Syntax & Indentation**: Python examiners dock 2–3 marks immediately if indentation blocks are missing or inconsistent.
2. **Include Output Comments**: Under every script, write `# Output:` or `Sample Output:` showing 2 test cases.
3. **Use Descriptive Names**: Use `student_name`, `cgpa`, `connection`, not single letters like `x`, `y`, `z` for major data structures.
4. **Always Wrap I/O & DB in `try-except-finally`**: Prof. Vaishnavi emphasizes exception resilience in files and databases.
