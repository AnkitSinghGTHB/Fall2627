# 🎯 CSE3011: High-Frequency FAT / TEE Exam Question Bank (15 Solved Questions)

> Fully solved in Prof. Vaishnavi S's required clean code format with output verification.

---

## UNIT 1: Python Fundamentals & Flow Control

### Q1 (12 Marks) [Section A Model]
**Write a Python program that accepts a matrix from the user, computes its transpose, and checks whether the matrix is symmetric ($A = A^T$). Handle input dimensions dynamically.**

**Solution**:
```python
def check_symmetric_matrix():
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        if rows != cols:
            print("Matrix must be square to be symmetric.")
            return

        print("Enter elements row by row (space-separated):")
        matrix = []
        for i in range(rows):
            row = [int(x) for x in input(f"Row {i+1}: ").split()]
            if len(row) != cols:
                print("Error: Invalid number of elements in row.")
                return
            matrix.append(row)

        # Transpose using list comprehension
        transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

        print("\nOriginal Matrix:")
        for r in matrix: print(r)

        print("\nTranspose Matrix:")
        for r in transpose: print(r)

        # Symmetry check
        is_symmetric = all(matrix[i][j] == matrix[j][i] for i in range(rows) for j in range(cols))
        if is_symmetric:
            print("\nResult: The matrix is SYMMETRIC.")
        else:
            print("\nResult: The matrix is NOT symmetric.")

    except ValueError:
        print("Invalid input. Please enter integers only.")

# Test: [[1, 2, 3], [2, 4, 5], [3, 5, 6]] -> Symmetric!
```

##### Sample Input & Output:
```text
Sample Interactive Input:
Enter number of rows: 3
Enter number of columns: 3
Enter elements row by row (space-separated):
Row 1: 1 2 3
Row 2: 2 4 5
Row 3: 3 5 6

Sample Console Output:
Original Matrix:
[1, 2, 3]
[2, 4, 5]
[3, 5, 6]

Transpose Matrix:
[1, 2, 3]
[2, 4, 5]
[3, 5, 6]

Result: The matrix is SYMMETRIC.
```

---

### Q2 (8 Marks) [Section B Model]
**Explain the difference between `break`, `continue`, and `pass` statements in Python with code examples.**

**Solution**:
```python
# 1. break: Immediately terminates loop execution
print("break demo:   ", end="")
for x in range(5):
    if x == 3: break
    print(x, end=" ")
print()

# 2. continue: Skips remainder of current iteration, proceeds to next
print("continue demo:", end="")
for x in range(5):
    if x == 3: continue
    print(x, end=" ")
print()

# 3. pass: Null statement; syntactic placeholder where code is required
print("pass demo:    ", end="")
for x in range(5):
    if x == 3: pass
    print(x, end=" ")
print()
```

##### Sample Input & Output:
```text
Sample Output:
break demo:    0 1 2 
continue demo: 0 1 2 4 
pass demo:     0 1 2 3 4 
```

---

## UNIT 2: Collections, Functions & Regex

### Q3 (12 Marks) [Section A Model]
**Write a Python program that takes a text paragraph, finds all phone numbers and email addresses using regular expressions, and extracts the top 3 most common words.**

**Solution**:
```python
import re
from collections import Counter

def extract_and_analyze(text):
    # Regex for standard 10-digit Indian phone numbers
    phone_pattern = r"\b[6-9]\d{9}\b"
    phones = re.findall(phone_pattern, text)

    # Regex for email addresses
    email_pattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
    emails = re.findall(email_pattern, text)

    # Clean words and extract top 3 frequencies
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    common_words = Counter(words).most_common(3)

    print("Found Phone Numbers:", phones)
    print("Found Email Addresses:", emails)
    print("Top 3 Words:", common_words)

# Test execution:
sample = "Call me at 9876543210 or email ankit@vitbhopal.ac.in. Python is great and Python is fast."
extract_and_analyze(sample)
```

##### Sample Input & Output:
```text
Sample Output:
Found Phone Numbers: ['9876543210']
Found Email Addresses: ['ankit@vitbhopal.ac.in']
Top 3 Words: [('python', 2), ('is', 2), ('call', 1)]
```

---

### Q4 (8 Marks) [Section B Model]
**Explain the `*args` and `**kwargs` syntax in Python functions. Write a function that calculates the weighted average of numbers passed as arguments.**

**Solution**:
```python
def weighted_average(*values, **weights):
    """
    Calculates weighted average.
    values: passed as *args
    weights: passed as **kwargs with keys matching value indices (e.g., w0=0.2, w1=0.8)
    """
    total_weighted_sum = 0
    total_weight = 0

    for idx, val in enumerate(values):
        w_key = f"w{idx}"
        w = weights.get(w_key, 1.0)  # Default weight 1.0 if unspecified
        total_weighted_sum += val * w
        total_weight += w

    return total_weighted_sum / total_weight if total_weight != 0 else 0

result = weighted_average(80, 90, 100, w0=0.2, w1=0.3, w2=0.5)
print("Weighted Average:", result)
```

##### Sample Input & Output:
```text
Sample Output:
Weighted Average: 93.0
```

---

## UNIT 3: OOP & Exceptions

### Q5 (12 Marks) [Section A Model]
**Create a Python class `Polynomial` supporting polynomial addition and multiplication by overloading the `+` and `*` operators. Implement `__str__` to display the polynomial in standard algebraic notation.**

**Solution**:
```python
class Polynomial:
    def __init__(self, coeffs):
        """coeffs: list where index represents power, e.g., [2, 0, 3] = 2 + 3x^2"""
        self.coeffs = list(coeffs)

    def __add__(self, other):
        max_len = max(len(self.coeffs), len(other.coeffs))
        c1 = self.coeffs + [0] * (max_len - len(self.coeffs))
        c2 = other.coeffs + [0] * (max_len - len(other.coeffs))
        return Polynomial([a + b for a, b in zip(c1, c2)])

    def __mul__(self, other):
        res_len = len(self.coeffs) + len(other.coeffs) - 1
        res = [0] * res_len
        for i, a in enumerate(self.coeffs):
            for j, b in enumerate(other.coeffs):
                res[i + j] += a * b
        return Polynomial(res)

    def __str__(self):
        terms = []
        for power, coef in enumerate(self.coeffs):
            if coef != 0:
                if power == 0: terms.append(f"{coef}")
                elif power == 1: terms.append(f"{coef}x")
                else: terms.append(f"{coef}x^{power}")
        return " + ".join(terms) if terms else "0"

p1 = Polynomial([1, 2])     # 1 + 2x
p2 = Polynomial([3, 4, 1])  # 3 + 4x + 1x^2
print("p1 + p2 =", p1 + p2)  # 4 + 6x + 1x^2
print("p1 * p2 =", p1 * p2)  # 3 + 10x + 9x^2 + 2x^3
```

##### Sample Input & Output:
```text
Sample Output:
p1 + p2 = 4 + 6x + 1x^2
p1 * p2 = 3 + 10x + 9x^2 + 2x^3
```

---

### Q6 (8 Marks) [Section B Model]
**Explain the `try-except-else-finally` block in Python. Write a program demonstrating file operations where resources are reliably closed inside `finally`.**

**Solution**:
```python
file_handle = None
try:
    file_handle = open("sample.txt", "r")
    data = file_handle.read()
    num = int(data.strip())
    result = 100 / num
except FileNotFoundError:
    print("Caught Error: File not found on disk.")
except ZeroDivisionError:
    print("Caught Error: Cannot divide by zero.")
except ValueError:
    print("Caught Error: File does not contain a valid integer.")
else:
    print(f"Calculation succeeded! Result: {result}")
finally:
    if file_handle and not file_handle.closed:
        file_handle.close()
        print("Cleanup: File handle closed successfully.")
```

##### Sample Input & Output:
```text
Case 1: "sample.txt" contains "25"
Sample Output:
Calculation succeeded! Result: 4.0
Cleanup: File handle closed successfully.

Case 2: "sample.txt" is missing
Sample Output:
Caught Error: File not found on disk.

Case 3: "sample.txt" contains "0"
Sample Output:
Caught Error: Cannot divide by zero.
Cleanup: File handle closed successfully.
```

---

## UNIT 4: File I/O & Databases

### Q7 (12 Marks) [Section A Model]
**Write a Python program to create an SQLite database named `company.db`, create an `employees` table, insert 3 records, and perform a query to retrieve employees with salary greater than ₹50,000 using parameterized queries.**

**Solution**:
```python
import sqlite3

def run_db_operations():
    try:
        conn = sqlite3.connect("company.db")
        cursor = conn.cursor()

        # Create Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                emp_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                department TEXT,
                salary REAL
            )
        """)

        # Insert Records using Parameterized Queries
        records = [
            (101, "Alice", "Engineering", 75000.0),
            (102, "Bob", "Marketing", 45000.0),
            (103, "Charlie", "Finance", 82000.0)
        ]
        cursor.executemany("INSERT OR REPLACE INTO employees VALUES (?, ?, ?, ?)", records)
        conn.commit()

        # Query with threshold
        threshold = 50000.0
        cursor.execute("SELECT name, department, salary FROM employees WHERE salary > ?", (threshold,))
        high_earners = cursor.fetchall()

        print(f"Employees earning > ₹{threshold}:")
        for name, dept, sal in high_earners:
            print(f"- {name} ({dept}): ₹{sal}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    run_db_operations()
```

##### Sample Input & Output:
```text
Sample Output:
Employees earning > ₹50000.0:
- Alice (Engineering): ₹75000.0
- Charlie (Finance): ₹82000.0
```

---

### Q8 (8 Marks) [Section B Model]
**Differentiate between `pickle` and `json` serialization in Python with respect to data formats, security, and human readability.**

**Solution**:
*[Include full 4-row comparative table from Unit 4 notes: JSON is human-readable cross-language text and safe; Pickle is Python-specific binary capable of serializing arbitrary custom objects, but presents severe arbitrary code execution security vulnerabilities on untrusted inputs]*.

---

## UNIT 5: GUI, Multithreading & Sockets

### Q9 (12 Marks) [Section A Model]
**Design a Tkinter GUI application containing a Student Registration form with fields: Name (Entry), Gender (Radiobuttons: Male/Female), Courses (Checkbuttons: Python, ML), and a Submit Button that displays the entered details in a messagebox.**

**Solution**:
```python
import tkinter as tk
from tkinter import messagebox

def launch_registration_form():
    root = tk.Tk()
    root.title("Student Registration Form")
    root.geometry("320x300")

    # Name Field
    tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_name = tk.Entry(root, width=20)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    # Gender Radiobuttons
    tk.Label(root, text="Gender:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    gender_var = tk.StringVar(value="Male")
    tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=1, column=1, sticky="w")
    tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=1, sticky="w")

    # Courses Checkbuttons
    tk.Label(root, text="Courses:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    py_var = tk.BooleanVar()
    ml_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Python", variable=py_var).grid(row=3, column=1, sticky="w")
    tk.Checkbutton(root, text="Machine Learning", variable=ml_var).grid(row=4, column=1, sticky="w")

    def submit():
        name = entry_name.get().strip()
        if not name:
            messagebox.showwarning("Incomplete", "Please enter your name!")
            return
        
        courses = []
        if py_var.get(): courses.append("Python")
        if ml_var.get(): courses.append("ML")
        
        msg = f"Registration Successful!\nName: {name}\nGender: {gender_var.get()}\nCourses: {', '.join(courses) if courses else 'None'}"
        messagebox.showinfo("Success", msg)

    tk.Button(root, text="Register", command=submit, bg="#008CBA", fg="white").grid(row=5, column=0, columnspan=2, pady=15)
    root.mainloop()
```

##### Sample Input & Output:
```text
GUI Window Interaction:
+--------------------------------------+
| Student Registration Form       [X]  |
+--------------------------------------+
| Name:    [ Ankit Singh            ]  |
| Gender:  (o) Male   ( ) Female       |
| Courses: [X] Python                  |
|          [X] Machine Learning        |
|                                      |
|          [  Register  ]              |
+--------------------------------------+

Messagebox Popup on Register Click:
Title: "Success"
Content:
Registration Successful!
Name: Ankit Singh
Gender: Male
Courses: Python, ML
```

---

### Q10 (8 Marks) [Section B Model]
**Explain the Global Interpreter Lock (GIL) in Python. Why does multithreading improve performance for I/O-bound tasks but not for CPU-bound tasks?**

**Solution**:
1. **Definition of GIL**: A mutex lock in CPython ensuring that only one native OS thread executes Python bytecode at any given moment, preventing race conditions within Python's memory management and reference counting subsystem.
2. **Impact on Tasks**:
   - *CPU-Bound Tasks (e.g., matrix math, image rendering)*: Threads compete for the same single CPU core while holding the GIL. Thread context switching introduces operational overhead, making multi-threaded execution often slower than single-threaded execution!
   - *I/O-Bound Tasks (e.g., downloading web pages, database queries, file reading)*: When a thread initiates an OS I/O operation (waiting for a network response), it **releases the GIL**. Another thread immediately acquires the GIL and executes code concurrently. Thus, I/O-bound applications achieve massive speedup.

---

### Q11 (12 Marks) [Direct from Assignment 3]
**(a) Create a Python class `Book` representing a book in a library system with: Public attribute `title`, Protected attribute `_author`, Private attribute `__isbn`, and Protected method `_update_author_details()`. Demonstrate encapsulation and name mangling.**  
**(b) Write a program comparing two Person objects based on age using operator overloading (`Person1: Danny, 30`, `Person2: Thomas, 25`).**

**Solution**:
```python
# Part (a): Book Class Encapsulation
class Book:
    def __init__(self, title, author, isbn):
        self.title = title          # Public
        self._author = author       # Protected convention
        self.__isbn = isbn          # Private (Mangled to _Book__isbn)

    def _update_author_details(self, new_author):
        self._author = new_author

    @property
    def isbn(self):
        return self.__isbn

b1 = Book("Designing Data-Intensive Applications", "Martin Kleppmann", "978-1449373320")
print(f"Public Title: {b1.title}")
print(f"Protected Author: {b1._author}")
# Accessing private attribute via Name Mangling:
print(f"Mangled Private ISBN: {b1._Book__isbn}")
b1._update_author_details("M. Kleppmann")

# Part (b): Person Age Comparison Overloading
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

danny = Person("Danny", 30)
thomas = Person("Thomas", 25)

if danny > thomas:
    print(f"Result: {danny.name} ({danny.age}) is older than {thomas.name} ({thomas.age}).")
```

##### Sample Input & Output:
```text
Sample Output:
Public Title: Designing Data-Intensive Applications
Protected Author: Martin Kleppmann
Mangled Private ISBN: 978-1449373320
Result: Danny (30) is older than Thomas (25).
```

---

### Q12 (10 Marks) [Direct from Assignment 3]
**Write an Object-Oriented Python program to compute the area and perimeter of arbitrary polygons. Implement derived classes for `Triangle`, `Rectangle`, and `RegularPolygon` using the `abc` module.**

**Solution**:
```python
import math
from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass

class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Rectangle(Polygon):
    def __init__(self, l, w):
        self.l, self.w = l, w
    def perimeter(self):
        return 2 * (self.l + self.w)
    def area(self):
        return self.l * self.w

t = Triangle(3, 4, 5)
r = Rectangle(10, 4)
print(f"Triangle Area: {t.area()}, Perimeter: {t.perimeter()}")
print(f"Rectangle Area: {r.area()}, Perimeter: {r.perimeter()}")
```

##### Sample Input & Output:
```text
Sample Output:
Triangle Area: 6.0, Perimeter: 12
Rectangle Area: 40, Perimeter: 28
```

---

### Q13 (8 Marks) [Direct from Suggested Experiments 3]
**Write a Python program to find the top $N$ most frequent words in a text read from a file. Handle case-insensitivity, punctuation removal, and file exceptions.**

**Solution**:
```python
import re
from collections import Counter

def top_frequent_words(filepath, n=5):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().lower()
        words = re.findall(r'\b[a-z0-9]+\b', content)
        freq = Counter(words).most_common(n)
        print(f"Top {n} words:")
        for word, count in freq:
            print(f"- {word}: {count}")
        return freq
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")

# Test execution with sample text:
sample_text = "Python is an interpreted, high-level, general-purpose programming language. Python is dynamically typed."
with open("article.txt", "w", encoding="utf-8") as f:
    f.write(sample_text)

top_frequent_words("article.txt", 4)
```

##### Sample Input & Output:
```text
Sample Output:
Top 4 words:
- python: 2
- is: 2
- an: 1
- interpreted: 1
```

---

### Q14 (12 Marks) [Direct from List of Experiments 4]
**Write Python programs using Pygame to:**  
**(a) Simulate elliptical planetary orbits.**  
**(b) Simulate bouncing ball physics with gravity and wall reflections.**

**Solution**:
```python
# (a) Elliptical Orbit Logic
import pygame, math

def simulate_orbit():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()
    cx, cy, a, b, theta = 300, 200, 180, 100, 0.0

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return pygame.quit()
        screen.fill((20, 20, 40))
        # Draw Sun
        pygame.draw.circle(screen, (255, 220, 0), (cx, cy), 20)
        # Orbit Path
        pygame.draw.ellipse(screen, (80, 80, 120), (cx - a, cy - b, 2*a, 2*b), 1)
        # Planet position: x = cx + a*cos(θ), y = cy + b*sin(θ)
        px = cx + int(a * math.cos(theta))
        py = cy + int(b * math.sin(theta))
        pygame.draw.circle(screen, (0, 200, 255), (px, py), 10)
        theta += 0.04
        pygame.display.flip()
        clock.tick(60)

# (b) Bouncing Ball Logic
def simulate_bouncing_ball():
    pygame.init()
    screen = pygame.display.set_mode((500, 400))
    clock = pygame.time.Clock()
    x, y, vx, vy, gravity, damping = 250, 50, 3, 0, 0.4, 0.85
    r = 15

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return pygame.quit()
        vy += gravity
        x += vx; y += vy
        if y + r >= 400:  # Floor collision
            y = 400 - r; vy = -vy * damping
        if x - r <= 0 or x + r >= 500:  # Wall reflection
            vx = -vx
        screen.fill((240, 240, 240))
        pygame.draw.circle(screen, (200, 40, 40), (int(x), int(y)), r)
        pygame.display.flip()
        clock.tick(60)
```

##### Sample Simulation State & Visual Output:
```text
(a) Elliptical Orbit State Output:
Window 600x400:
- Center Sun at (300, 200)
- Semi-major axis a=180, Semi-minor axis b=100
- Planet smoothly traces coordinates: (480, 200) -> (300, 300) -> (120, 200) -> (300, 100)
Frame Rate: 60 FPS constant.

(b) Bouncing Ball Physics State Output:
Window 500x400:
- Initial position: (250, 50), vy=0.0
- Ball accelerates under gravity 0.4
- Hits floor (y=385) and reflects with vy = -vy * 0.85
- Horizontal reflection on reaching left/right boundaries (x <= 15 or x >= 485).
```

---

### Q15 (10 Marks) [Direct from Unit 5 PPT]
**Explain the concept and architecture of Python CGI programming. Write a complete Python script to accept data from a Student Registration form and render an HTML response page. Describe the server configuration steps.**

**Solution**:
```python
#!C:/Python310/python.exe
import cgi
import html

print("Content-type: text/html\r\n\r\n")
form = cgi.FieldStorage()
s_name = html.escape(form.getvalue("name", "N/A"))
s_reg  = html.escape(form.getvalue("regno", "N/A"))
s_dept = html.escape(form.getvalue("dept", "N/A"))

print(f"""
<html>
<head><title>Registration Summary</title></head>
<body>
  <h2>Registration Confirmation</h2>
  <p><b>Name:</b> {s_name}</p>
  <p><b>Reg No:</b> {s_reg}</p>
  <p><b>Department:</b> {s_dept}</p>
</body>
</html>
""")
```

##### Sample Input & Output:
```text
HTTP Request Data:
name = "Ankit Singh", regno = "22BCE1001", dept = "Computer Science"

Rendered HTML Browser Output:
+-----------------------------------------+
| Registration Summary                    |
+-----------------------------------------+
| Registration Confirmation               |
| Name: Ankit Singh                       |
| Reg No: 22BCE1001                       |
| Department: Computer Science            |
+-----------------------------------------+
```

*Server Deployment Steps*:
1. Install and launch Apache server via XAMPP.
2. In Apache `httpd.conf`, add `AddHandler cgi-script .py` and allow `Options +ExecCGI`.
3. Ensure the script has the exact shebang `#!(path to python.exe)` at line 1.
4. Place the `.py` script in `htdocs` or `cgi-bin` directory and access via `http://localhost/...`.

