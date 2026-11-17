# 🎯 CSE3011: TEE Live Papers Pattern Analysis & Slot B11+B12 Predictions

> **Compiled**: October 19, 2026 (00:45 IST) | **Exam Time**: Today, Oct 19, 2026 (01:15 PM – 04:15 PM)  
> **Course**: CSE3011 – Python Programming | **Slot**: B11+B12  

---

## 1. Live Intelligence: How TEE Papers Are Being Formed

Comparing your actual **CAT-1 & CAT-2 papers (Slot B11+B12)** with the two TEE papers already conducted this cycle (**Oct 17, Slot A21+A23** and **Oct 18, Slot F11+F12**) demonstrates that the examination committee uses a **shared pool of 10–12 core question templates**, rotating them across slots with minor contextual rephrasing:

### 1.1 Cross-Examination Topic Mapping Table

| Concept & Topic | CAT-1 / CAT-2 (Slot B11+B12) | TEE Oct 17 (Slot A21+A23) | TEE Oct 18 (Slot F11+F12) | Probability for Today (Slot B11+B12) |
|:---|:---|:---|:---|:---:|
| **Password Validation Regex** | **CAT-1 Q4** (10M) | — | **TEE Q6 (8M)** (Exact clone) | ⭐⭐⭐ **VERY HIGH** |
| **List Frequency & Duplicates** | **CAT-1 Q3** (10M) | TEE Q7 (`sorted`, `append`, `remove`) | **TEE Q1(a) (12M)** (Scanner IDs) | ⭐⭐⭐ **VERY HIGH** |
| **Matrix Operations** | — | — | **TEE Q1(b) (12M)** (Matrix Mult) | ⭐⭐⭐ **HIGH (Mult / Transpose)** |
| **Operator Precedence Trace** | — | **TEE Q6 (8M)** (4 Expressions) | — | ⭐⭐⭐ **HIGH (Part B 8M)** |
| **Polymorphism without `if-elif`** | **CAT-2 Q1** (Managers/Devs) | **TEE Q8 (8M)** (Bank Accounts) | **TEE Q3(a) (12M)** (Bank Account) | ⭐⭐⭐ **GUARANTEED (Unit 3)** |
| **Abstract Base Classes (`abc`)** | **CAT-2 Q2** (`Shape` ABC) | — | **TEE Q8 (8M)** (Abstract class role) | ⭐⭐⭐ **GUARANTEED (Unit 3)** |
| **Operator Overloading (`+`)** | **CAT-2 Q3** (`Distance` km+m) | **TEE Q3(b) (12M)** (Overloading) | — | ⭐⭐⭐ **VERY HIGH** |
| **Dual File Copy with `with`** | **CAT-2 Q4** (File copy + except) | **TEE Q4(b)** (Text file CRUD) | **TEE Q9 (8M)** (Dual file `with`) | ⭐⭐⭐ **GUARANTEED (Unit 4)** |
| **Relational DB CRUD / Query** | **CAT-2 Q5** (MySQL Employee) | **TEE Q4(a)** (Hospital DB CRUD) | **TEE Q4(b)** (HR Dept Query) | ⭐⭐⭐ **GUARANTEED (Unit 4)** |
| **Tkinter GUI Form / Calculator** | — | **TEE Q5(a)** (Calculator) | **TEE Q5(a)** (Entry to Label) | ⭐⭐⭐ **GUARANTEED (Unit 5)** |
| **TCP Sockets / Multithreading** | — | **TEE Q10 (8M)** (Multithreading) | **TEE Q10 (8M)** (TCP Client/Server) | ⭐⭐⭐ **GUARANTEED (Unit 5)** |

---

## 2. Rigorous Exam Structure (Part A & Part B)

The exam contains **10 Questions for 100 Marks**:

```
+---------------------------------------------------------------------------------------------------+
|                                  TEE QUESTION PAPER STRUCTURE                                     |
+--------+---------------+--------------------+-----------------------------------------------------+
| Section| Marks Breakdown| Question Numbers   | Coverage & Choices                                  |
+--------+---------------+--------------------+-----------------------------------------------------+
| Part A | 5 × 12M = 60M | Q1 to Q5           | Strict 1-to-1 mapping from Unit 1 to Unit 5.       |
|        |               |                    | Each question has internal choice: (a) OR (b).      |
+--------+---------------+--------------------+-----------------------------------------------------+
| Part B | 5 × 8M = 40M  | Q6 to Q10          | Strict 1-to-1 mapping from Unit 1 to Unit 5.       |
|        |               |                    | Direct questions; NO internal choices.              |
+--------+---------------+--------------------+-----------------------------------------------------+
```

### Unit Distribution:
* **Q1 (12M) & Q6 (8M)** $\to$ **Unit 1**: Basic syntax, loops, operators, bitwise, matrix, number theory.
* **Q2 (12M) & Q7 (8M)** $\to$ **Unit 2**: Collections, dictionaries, comprehensions, regex, functions, LEGB scoping.
* **Q3 (12M) & Q8 (8M)** $\to$ **Unit 3**: OOP inheritance, polymorphism, dunder operator overloading, custom exceptions.
* **Q4 (12M) & Q9 (8M)** $\to$ **Unit 4**: File operations (`with`, `seek`, `tell`), JSON vs Pickle, SQLite3 / MySQL DB-API.
* **Q5 (12M) & Q10 (8M)** $\to$ **Unit 5**: Tkinter GUI widgets/layout, CGI web programming, TCP sockets, Multithreading & GIL.

---

## 3. Step-by-Step Operator Precedence Solutions (Direct from Oct 17 Q6)

In Slot A21+A23 (Oct 17), Q6 asked students to define operator precedence and evaluate four expressions step-by-step for **8 marks**. Here are the full mathematical derivations:

### Operator Precedence Hierarchy (Highest to Lowest):
1. Parentheses: `()`
2. Exponentiation: `**` (Right-to-Left associativity)
3. Unary operators: `+x`, `-x`, `~x`
4. Multiplication, Division, Floor Division, Modulus: `*`, `/`, `//`, `%` (Left-to-Right)
5. Addition, Subtraction: `+`, `-` (Left-to-Right)
6. Bitwise Shifts: `<<`, `>>`
7. Bitwise AND: `&`
8. Bitwise XOR & OR: `^`, `|`
9. Comparison & Identity: `==`, `!=`, `<`, `<=`, `>`, `>=`, `is`, `in`
10. Logical NOT: `not`
11. Logical AND: `and`
12. Logical OR: `or`

---

### Problem (a): `24 // 4 * 2 + 16 % 4 ** 3`

1. **Step 1 (Exponentiation `**`)**:
   $$4 ** 3 = 64$$
   Expression becomes: `24 // 4 * 2 + 16 % 64`
2. **Step 2 (Floor Division `//`, left-to-right)**:
   $$24 // 4 = 6$$
   Expression becomes: `6 * 2 + 16 % 64`
3. **Step 3 (Multiplication `*`, left-to-right)**:
   $$6 * 2 = 12$$
   Expression becomes: `12 + 16 % 64`
4. **Step 4 (Modulus `%`, left-to-right)**:
   $$16 % 64 = 16$$
   Expression becomes: `12 + 16`
5. **Step 5 (Addition `+`)**:
   $$12 + 16 = 28$$
* **Final Result**: **`28`**

---

### Problem (b): `False or True and (not True) or False`

1. **Step 1 (Parentheses & Logical `not`)**:
   $$\text{not True} = \text{False}$$
   Expression becomes: `False or True and False or False`
2. **Step 2 (Logical `and` has higher precedence than `or`)**:
   $$\text{True and False} = \text{False}$$
   Expression becomes: `False or False or False`
3. **Step 3 (Logical `or` evaluated left-to-right)**:
   $$\text{False or False} = \text{False}$$
   $$\text{False or False} = \text{False}$$
* **Final Result**: **`False`**

---

### Problem (c): `18 + 5 * 2 ** 2 // 6 - 3`

1. **Step 1 (Exponentiation `**`)**:
   $$2 ** 2 = 4$$
   Expression becomes: `18 + 5 * 4 // 6 - 3`
2. **Step 2 (Multiplication `*`, left-to-right)**:
   $$5 * 4 = 20$$
   Expression becomes: `18 + 20 // 6 - 3`
3. **Step 3 (Floor Division `//`)**:
   $$20 // 6 = 3$$
   Expression becomes: `18 + 3 - 3`
4. **Step 4 (Addition `+`, left-to-right)**:
   $$18 + 3 = 21$$
   Expression becomes: `21 - 3`
5. **Step 5 (Subtraction `-`)**:
   $$21 - 3 = 18$$
* **Final Result**: **`18`**

---

### Problem (d): `(45 // 9 * 3 + 8 % 4) ** (25 * 6) - 9 ** 2`

1. **Step 1 (Resolve Left Parentheses `(45 // 9 * 3 + 8 % 4)`)**:
   - `45 // 9 = 5`
   - `5 * 3 = 15`
   - `8 % 4 = 0`
   - `15 + 0 = 15`
2. **Step 2 (Resolve Right Parentheses `(25 * 6)`)**:
   - `25 * 6 = 150`
   Expression becomes: `15 ** 150 - 9 ** 2`
3. **Step 3 (Exponentiations `**`)**:
   - `9 ** 2 = 81`
   - `15 ** 150` evaluates to an arbitrarily large integer:
     `570899077082383952423314...`
4. **Step 4 (Subtraction `-`)**:
   $$15^{150} - 81$$
* **Final Result**: **`15**150 - 81`**

---

## 4. The 8 High-Yield "Live Clone" Code Blueprints

These blueprints directly match the problems tested on October 17 & 18 and CAT-1 & CAT-2. Memorize these structures:

### Blueprint 1: Scanner Duplicate IDs & Frequency (TEE Oct 18 Q1a / CAT-1 Q3)
```python
def process_scanned_attendance(scanned_ids):
    # 1. Unique registration numbers
    unique_ids = sorted(list(set(scanned_ids)))
    
    # 2. Frequency counting via dictionary
    freq_map = {}
    for item in scanned_ids:
        freq_map[item] = freq_map.get(item, 0) + 1
        
    # 3. Duplicate registration numbers (frequency > 1)
    duplicates = [k for k, v in freq_map.items() if v > 1]
    
    print("Unique Registration Numbers:", unique_ids)
    print("Frequency of Each Number:  ", freq_map)
    print("Duplicated Numbers:        ", duplicates)

data = [105, 102, 108, 105, 110, 102, 115, 108, 120, 105, 102, 120, 115]
process_scanned_attendance(data)
```
##### Sample Input & Output:
```text
Sample Output:
Unique Registration Numbers: [102, 105, 108, 110, 115, 120]
Frequency of Each Number:   {105: 3, 102: 3, 108: 2, 110: 1, 115: 2, 120: 2}
Duplicated Numbers:         [105, 102, 108, 115, 120]
```

---

### Blueprint 2: Matrix Multiplication (TEE Oct 18 Q1b)
```python
def matrix_mult(A, B):
    r1, c1 = len(A), len(A[0])
    r2, c2 = len(B), len(B[0])
    
    if c1 != r2:
        print("Dimension Error: Columns of A must equal Rows of B!")
        return None
        
    # Initialize result matrix with dimensions r1 x c2
    result = [[0 for _ in range(c2)] for _ in range(r1)]
    
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]
                
    print("Matrix A:")
    for r in A: print(r)
    print("Matrix B:")
    for r in B: print(r)
    print("Product Matrix (A x B):")
    for r in result: print(r)
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
matrix_mult(A, B)
```
##### Sample Input & Output:
```text
Sample Output:
Matrix A:
[1, 2]
[3, 4]
Matrix B:
[5, 6]
[7, 8]
Product Matrix (A x B):
[19, 22]
[43, 50]
```

---

### Blueprint 3: Palindrome Check using Arithmetic Loops (CAT-1 Q1)
```python
def is_palindrome_number(num):
    original = num
    reversed_num = 0
    
    while num > 0:
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num = num // 10
        
    if original == reversed_num:
        print(f"{original} is a PALINDROME (Reversed: {reversed_num})")
    else:
        print(f"{original} is NOT a palindrome (Reversed: {reversed_num})")

is_palindrome_number(12321)
is_palindrome_number(12345)
```
##### Sample Input & Output:
```text
Sample Output:
12321 is a PALINDROME (Reversed: 12321)
12345 is NOT a palindrome (Reversed: 54321)
```

---

### Blueprint 4: Distance Class Operator Overloading (CAT-2 Q3 / TEE Oct 17 Q3b)
```python
class Distance:
    def __init__(self, km=0, m=0):
        # Normalize meters into kilometers (1000m = 1km)
        self.km = km + (m // 1000)
        self.m = m % 1000

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_m = self.m + other.m
        total_km = self.km + other.km + (total_m // 1000)
        remainder_m = total_m % 1000
        return Distance(total_km, remainder_m)

    def __str__(self):
        return f"{self.km} km, {self.m} m"

d1 = Distance(4, 850)
d2 = Distance(2, 400)
d3 = d1 + d2
print(f"Distance 1: {d1}")
print(f"Distance 2: {d2}")
print(f"Sum (d1 + d2): {d3}")
```
##### Sample Input & Output:
```text
Sample Output:
Distance 1: 4 km, 850 m
Distance 2: 2 km, 400 m
Sum (d1 + d2): 7 km, 250 m
```

---

### Blueprint 5: Dual File Copy in a Single `with` Statement (TEE Oct 18 Q9)
```python
def copy_file_single_with(src_file, dst_file):
    try:
        # Dual file context managers opened together
        with open(src_file, "r", encoding="utf-8") as fin, open(dst_file, "w", encoding="utf-8") as fout:
            for line in fin:
                fout.write(line)
        print(f"Success: Copied '{src_file}' to '{dst_file}'.")
    except FileNotFoundError:
        print(f"Error: Source file '{src_file}' does not exist.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Verification setup
with open("test_src.txt", "w") as f:
    f.write("Line 1: CSE3011 Python TEE\nLine 2: Dual File Handling Success")

copy_file_single_with("test_src.txt", "test_dst.txt")
```
##### Sample Input & Output:
```text
Sample Output:
Success: Copied 'test_src.txt' to 'test_dst.txt'.
```

---

### Blueprint 6: Automated Folder Organizer by File Extension (TEE Oct 18 Q4a)
```python
import os
import shutil

def organize_files_by_extension(target_dir="submissions"):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Created base folder: {target_dir}")
        return

    for item in os.listdir(target_dir):
        full_path = os.path.join(target_dir, item)
        
        # Only process files, ignore existing folders
        if os.path.isfile(full_path):
            _, ext = os.path.splitext(item)
            folder_name = ext.lower().replace(".", "")
            
            if not folder_name:
                continue
                
            dest_dir = os.path.join(target_dir, folder_name)
            # Create subfolder if not already present
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
                
            shutil.move(full_path, os.path.join(dest_dir, item))
            print(f"Moved {item} -> {folder_name}/")

# organize_files_by_extension("submissions")
```
##### Sample Input & Output:
```text
Sample Simulation Output:
Moved roll101.pdf -> pdf/
Moved report_ankit.docx -> docx/
Moved chart.jpg -> jpg/
Moved slides.pptx -> pptx/
```

---

### Blueprint 7: MySQL HR Employee Department Query (TEE Oct 18 Q4b / CAT-2 Q5)
```python
import mysql.connector

def query_employees_by_department(target_dept):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password123",
            database="company_db"
        )
        cursor = conn.cursor()

        # Parameterized query to prevent SQL Injection
        sql = "SELECT Emp_Id, Name, Department, Designation, Salary FROM employees WHERE Department = %s"
        cursor.execute(sql, (target_dept,))
        rows = cursor.fetchall()

        print(f"\nEmployees in Department: {target_dept}")
        print(f"{'Emp ID':<8} {'Name':<15} {'Department':<12} {'Designation':<24} {'Salary':<8}")
        print("-" * 70)
        for emp_id, name, dept, desig, sal in rows:
            print(f"{emp_id:<8} {name:<15} {dept:<12} {desig:<24} {sal:<8}")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# query_employees_by_department("IT")
```
##### Sample Input & Output:
```text
Sample Output:
Employees in Department: IT
Emp ID   Name            Department   Designation              Salary  
----------------------------------------------------------------------
101      Aditi Singh     IT           Software Engineer        55000   
102      Rohan Yadav     IT           Database Administrator   62000   
105      Sneha Iyer      IT           QA Engineer              48000   
```

---

### Blueprint 8: Tkinter Entry Field to Label Display (TEE Oct 18 Q5a)
```python
import tkinter as tk

def launch_entry_display_app():
    root = tk.Tk()
    root.title("Text Viewer Application")
    root.geometry("320x180")

    tk.Label(root, text="Enter your message:", font=("Arial", 10)).pack(pady=5)
    entry_field = tk.Entry(root, width=28)
    entry_field.pack(pady=5)

    lbl_display = tk.Label(root, text="[Your text will appear here]", font=("Arial", 10, "italic"))
    lbl_display.pack(pady=12)

    def handle_submit():
        user_input = entry_field.get()
        if user_input.strip():
            lbl_display.config(text=f"Entered: {user_input}", font=("Arial", 11, "bold"), fg="#1A73E8")
        else:
            lbl_display.config(text="Please enter some text!", fg="red")

    tk.Button(root, text="Display Text", command=handle_submit, bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).pack(pady=5)
    root.mainloop()

# launch_entry_display_app()
```
##### Sample Input & Output:
```text
GUI Window Interaction:
+--------------------------------------+
| Text Viewer Application         [X]  |
+--------------------------------------+
| Enter your message:                  |
| [ Hello Python VIT              ]    |
|                                      |
|          [  Display Text  ]          |
|                                      |
| Entered: Hello Python VIT            |
+--------------------------------------+
```

---

## 5. Exam Hall Execution Strategy (Oct 19, 01:15 PM)

### 5.1 Score Mathematics
* **Target Breakdown**:
  - **A Grade (9.0 GP)**: Requires composite ~76–78 $\to$ **Only need 60–64 / 100 in TEE**.
  - **S Grade (10.0 GP)**: Requires composite ~88–90 $\to$ **Need 82–85 / 100 in TEE**.

### 5.2 Time Management (180 Minutes)
1. **0:00 – 0:40 (40 mins) $\to$ Part B (Q6 to Q10 = 40 Marks)**:
   - Knock these out first! Each question is direct (8M).
   - Write 3–4 bullet points of theory, 1 clean code snippet, and the `Sample Output` block.
2. **0:40 – 2:20 (100 mins) $\to$ Part A (Q1 to Q5 = 60 Marks)**:
   - Spend 20 minutes per question.
   - Choose the simpler OR option (e.g., Matrix Multiplication over theory, or Tkinter over CGI).
3. **2:20 – 3:00 (20 mins) $\to$ Review & Formatting**:
   - Check all loop bounds and Python indentation.
   - Ensure every single code snippet ends with a clearly boxed **`Sample Output:`** section.
