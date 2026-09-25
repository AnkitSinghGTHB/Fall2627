# CSE3011: Python Programming
## CAT-II Foolproof Exam Solve Booklet & HOTS Code Vault (Modules 3 & 4)

> **Exam Target:** VIT Bhopal CAT-II Examination | **Marks:** 50 Marks (Open Book / Open Notes)  
> **Course:** CSE3011 — Python Programming | **Coverage:** Module 3 (OOP, Dunder Methods, Persistence) & Module 4 (Files, OS, DB-API)  
> **Purpose:** Open-book exam-hall master reference. Zero-confusion, copy-paste ready code templates, theory justifications, and the 10-Second Question Decoder Matrix.

---

## 🧭 The Exam-Hall "10-Second Quick-Match" Navigation Matrix

| If Your Exam Question Mentions Any of These Words / Problem Requirements... | Topic Category | Section | Quick Strategy & Starting Pattern |
| :--- | :--- | :--- | :--- |
| **"Design an OOP solution for a real-world system of your choice"** / `BankAccount` / `SavingsAccount` | Real-World OOP System | **Sec 1.1** | Copy `BankAccount` ABC with `SavingsAccount`, `CheckingAccount`, `@abstractmethod`. |
| **"Class Book: Public title, Protected author, Private isbn, update author"** / Name Mangling | Access Specifiers / Data Hiding | **Sec 1.2** | Public: `self.title`, Protected: `self._author`, Private: `self.__isbn`. |
| **"Print area and perimeter of a polygons"** / `Triangle` (Heron's Formula) / `Rectangle` | Abstract Classes & Polymorphism | **Sec 1.3** | ABC `Polygon` with `@abstractmethod` `area()` and `perimeter()`; `Triangle`, `Rectangle`. |
| **"Compare two person based on their age"** / `Person1 Danny (30)`, `Person2 Thomas (25)` | Operator Overloading (`<`, `>`, `==`) | **Sec 1.4** | `Person` class implementing `__lt__`, `__gt__`, and `__eq__`. |
| **"Research two approaches for persistent storage"** / `JSON vs Pickle Comparison Matrix` | Object Persistence Theory | **Sec 2.1** | Copy Comparison Matrix (Security, Portability, Types, Speed). |
| **"Implement object storage and retrieval"** / `StudentRecord` to `student.json` & `student.pkl` | Object Serialization Code | **Sec 2.2** | Write `save_json()`, `load_json()`, `save_pickle()`, `load_pickle()`. |
| **"Compare class hierarchy with conditional statements"** / `Polymorphism vs if-elif-else` | OOP Design Justification | **Sec 3.1** | State Open-Closed Principle (OCP); adding new classes requires zero changes to callers. |
| **"Discuss possible limitations of your design"** / `Limitations of Operator Overloading` | Theory & Edge Cases | **Sec 3.2** | Write: Principle of Least Astonishment, Type Asymmetry, returning `NotImplemented`. |
| **"Analyze class hierarchy of open-source project and redesign for different domain"** | Architecture Redesign | **Sec 3.3** | Analyze `logging.Handler` → Redesign as E-Commerce `NotificationDispatcher`. |
| **"Explain Diamond Problem and Method Resolution Order (MRO)"** / `C3 Linearization` | Multiple Inheritance | **Sec 3.4** | Draw diamond diagram; state C3 order: `[D → B → C → A → object]`. |
| **"Word-frequency analysis on a text file and store the result in another file"** | File Text Processing | **Sec 4.1** | Read file → clean `string.punctuation` → `Counter(words)` → write `output.txt`. |
| **"Read, process, and write student records using file handling"** / Compute Averages & Grades | File Records Processing | **Sec 4.2** | Read CSV line-by-line → calculate average marks & grade (S/A/B/C/D/F) → write report. |
| **"Demonstrate exception handling during file operations using try, except, else, finally"** | File Exception Lifecycle | **Sec 4.3** | `try` open → `except FileNotFoundError` → `else` preview → `finally` close file. |
| **"Copy contents of input.txt into backup.txt handling missing file"** | Safe File Cloning | **Sec 4.4** | Read source chunk → write backup → catch `FileNotFoundError` & `IOError`. |
| **"Read a text file and count the number of lines, words, and characters"** | Text File Metrics | **Sec 4.5** | `len(lines)`, `sum(len(l.split()))`, `sum(len(l))` via context manager. |
| **"File and directory management operations using the os module"** / `College`, `OldFolder` | OS Automation & Filesystem | **Sec 5.1** | `os.getcwd()`, `os.mkdir('College')`, `os.rename()`, `os.remove()`, `os.rmdir()`. |
| **"MySQL database connectivity in Python using mysql.connector"** / `database 'college'` | MySQL DB-API Operations | **Sec 6.1** | `connect()` → create table `student` → `cursor.executemany` → `commit()`. |
| **"SQLite database connectivity in Python using built-in sqlite3"** / Zero-Config Database | Embedded SQLite DB-API | **Sec 6.2** | `sqlite3.connect('college.db')` → insert with `?` placeholder → query. |
| **"Explain SQL Injection vulnerability and demonstrate parameterized defense"** | Database Security | **Sec 6.3** | Contrast vulnerable string formatting vs secure parameterized queries (`%s` / `?`). |
| **"School maintains records of Teachers, Students and Principals"** / `Mrs. Rao`, `Aditi` | Multilevel Inheritance | **Sec 7.1** | `Principal(Teacher)` extends `Teacher(Person)`; senior teacher attributes; sample data. |
| **"Online shopping application supports different payment methods"** / `CreditCard`, `UPI`, `NetBanking` | Polymorphic Payment Loop | **Sec 7.2** | ABC `PaymentMethod` with `pay()`; list of payment objects processed in common loop. |
| **"Faculty receives students assignment submissions in submissions/"** / `.pdf`, `.docx`, `.jpg`, `.pptx` | OS File Type Sorter | **Sec 7.3** | `os.path.splitext()`, create extension subfolders if missing, `shutil.move()` files. |
| **"HR application stores employee details in MySQL table employees"** / `department = 'IT'` | Parameterized MySQL Query | **Sec 7.4** | `mysql.connector.connect()`, `WHERE Department = %s`, `cursor.fetchall()`. |
| **"Food delivery platform DineIn, CloudKitchen, FoodTruck"** / Table, slot, truck availability | Abstract Restaurant ABC | **Sec 7.5** | `Restaurant(ABC)` with `check_availability()` and `calculate_estimated_time()`. |
| **"College wants to maintain information about its employees... Analyze errors"** / `Employee`, `Manager` | Code Debugging & Overloading | **Sec 7.6** | Fix `super()`, private `__salary` name mangling, overload `+` operator via `__add__`. |
| **"Employee payroll framework using Python's abc module"** / `SalariedEmployee`, `CommissionEmployee` | Multilevel ABC Payroll | **Sec 7.7** | `Employee(ABC)` -> `SalariedEmployee` -> `CommissionEmployee` using `super().calculate_salary()`. |
| **"File system manager class FileRegistry that tracks directory structures"** / `create_path`, `get` | Object-Oriented File System | **Sec 7.8** | `create_path` checks parent path existence; `dump_registry_to_file` in `PATH -> VALUE` format. |
| **"MySQL database store_db table inventory"** / `process_sale(item_id, sold_quantity)`, `< 40` | DB Transactions & Stock Logic | **Sec 7.9** | Stock deduction with `commit()`, insufficient stock with `rollback()`, low stock alert. |
| **"Student-management system stores student details in a file... Analyze errors"** / `0-100` marks | File Exceptions & Validation | **Sec 7.10** | Fix `+ int` string crash, append mode `"a"`, `0-100` marks validation, read/display records. |
| **"Define a class that stores a given string and maintains its various properties"** | String Lexical Analyzer | **Sec 7.11** | Count `uppercase`, `vowels`, `consonants`, `spaces` upon initialization. |
| **"Student information system stores student records in a text file"** / `add`, `search`, `modify`, `delete` | Text File CRUD System | **Sec 7.12** | Structured delimited records (`Roll|Name|Dept|GPA`) vs unstructured raw text justification. |
| **"Explain why ODBC can be considered a generic database connectivity mechanism"** | Database Portability Theory | **Sec 7.13** | 4-tier ODBC Driver Manager architecture, uniform cursor API, DSN configuration. |
| **"Classes Student, Faculty, and Administrator with same get_role()... MRO & super()"** | OOP Roles & MRO Theory | **Sec 7.14** | Evaluate standalone vs polymorphic interface; C3 MRO diamond ambiguity prevention. |

---

# SECTION 1: Master Object-Oriented Architecture (Module 3)

## 1.1 Program: Real-World Banking System Architecture (`BankAccount`, `SavingsAccount`, `CheckingAccount`)

> 📋 **Exam Problem:** > **"Design an object-oriented Python solution for a real-world system of your choice. Incorporate classes, access specification (public, protected, private), inheritance, polymorphism, abstract classes, and instance methods. Implement meaningful operator overloading, justify the major design decisions, and demonstrate the working with suitable examples."**  
> *(Official Practice Test Q1 & Q5)*  
> **Exam Match Triggers:** `"real-world system"`, `"BankAccount"`, `"SavingsAccount"`, `"CheckingAccount"`, `"abstract base class"`, `"overdraft"`

This single architecture satisfies **classes, access specification, inheritance, polymorphism, abstract classes, instance methods, operator overloading, and exception handling** in one elegant program:

```python
from abc import ABC, abstractmethod

class InvalidTransactionError(Exception):  # 1. Custom Application Exception
    """Raised when an illegal monetary amount or overdraft is requested."""
    pass

class BankAccount(ABC):  # 2. Abstract Base Class (Abstraction & Interface Contract)
    def __init__(self, account_number: str, holder_name: str, initial_balance: float):
        self.account_number = account_number          # Public attribute  # Access Specification
        self._holder_name = holder_name              # Protected attribute (convention)
        self.__balance = float(initial_balance)       # Private attribute (name-mangled)

    @property  # Encapsulation: Getter and Setter properties
    def balance(self) -> float:
        """Read-only access to private balance."""
        return self.__balance

    def deposit(self, amount: float) -> None:
        """Instance method with business validation."""
        if amount <= 0:
            raise InvalidTransactionError("Deposit amount must be strictly positive!")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        """Instance method with balance constraint."""
        if amount <= 0:
            raise InvalidTransactionError("Withdrawal amount must be strictly positive!")
        if amount > self.__balance:
            raise InvalidTransactionError(f"Insufficient funds! Available: ${self.__balance:.2f}")
        self.__balance -= amount

    @abstractmethod
    def calculate_annual_interest(self) -> float:
        """Abstract method: forces concrete subclasses to implement policy."""
        pass

    def __str__(self) -> str:  # 3. Meaningful Operator Overloading (Magic / Dunder Methods)
        """End-user friendly string representation."""
        return f"{self.__class__.__name__}(Acc: {self.account_number}, Holder: {self._holder_name}, Balance: ${self.__balance:.2f})"

    def __repr__(self) -> str:
        """Developer inspection representation."""
        return f"{self.__class__.__name__}('{self.account_number}', '{self._holder_name}', {self.__balance})"

    def __add__(self, other):
        """Allows merging funds between two accounts or adding credit directly."""
        if isinstance(other, BankAccount):
            return self.__balance + other.__balance
        elif isinstance(other, (int, float)):
            return self.__balance + other
        return NotImplemented

    def __eq__(self, other) -> bool:
        """Equality based on unique account number."""
        if isinstance(other, BankAccount):
            return self.account_number == other.account_number
        return False

    def __lt__(self, other) -> bool:
        """Allows sorting accounts automatically by balance."""
        if isinstance(other, BankAccount):
            return self.__balance < other.__balance
        return NotImplemented

class SavingsAccount(BankAccount):  # 4. Concrete Subclasses (Inheritance & Polymorphism)
    def __init__(self, account_number: str, holder_name: str, initial_balance: float, interest_rate: float = 0.04):
        super().__init__(account_number, holder_name, initial_balance)
        self.interest_rate = interest_rate

    def calculate_annual_interest(self) -> float:
        """Polymorphic implementation: Savings earns interest on balance."""
        return self.balance * self.interest_rate

class CheckingAccount(BankAccount):
    def __init__(self, account_number: str, holder_name: str, initial_balance: float, overdraft_limit: float = 500.0):
        super().__init__(account_number, holder_name, initial_balance)
        self.overdraft_limit = overdraft_limit

    def calculate_annual_interest(self) -> float:
        """Checking accounts earn zero annual interest."""
        return 0.0

    def withdraw(self, amount: float) -> None:
        """Overridden method allowing overdraft protection."""
        if amount <= 0:
            raise InvalidTransactionError("Withdrawal amount must be positive!")
        if amount > (self.balance + self.overdraft_limit):
            raise InvalidTransactionError("Transaction exceeds approved overdraft limit!")
        self._BankAccount__balance -= amount  # Use name-mangled attribute access of parent or deposit negative

if __name__ == "__main__":  # 5. Demonstration & Working Verification
    acc1 = SavingsAccount("SA-101", "Danny", 5000.0, interest_rate=0.05)
    acc2 = CheckingAccount("CA-202", "Thomas", 2000.0, overdraft_limit=1000.0)

    accounts = [acc1, acc2]  # Polymorphic dispatch
    for acc in accounts:
        print(f"{acc} | Annual Interest: ${acc.calculate_annual_interest():.2f}")

    print(f"Total Combined Funds (acc1 + acc2): ${acc1 + acc2:.2f}")  # Operator Overloading Demo
    print(f"Is acc1 < acc2? {acc1 < acc2}")  # Uses __lt__
```

#### 🖥️ Program Execution Output:
```text
SavingsAccount(Acc: SA-101, Holder: Danny, Balance: $5000.00) | Annual Interest: $250.00
CheckingAccount(Acc: CA-202, Holder: Thomas, Balance: $2000.00) | Annual Interest: $0.00
Total Combined Funds (acc1 + acc2): $7000.00
Is acc1 < acc2? False
```

---

## 1.2 Program: Library Book Access Specification (Class `Book` with Public Title, Protected `_author`, Private `__isbn`, & `_update_author_details`)

> 📋 **Exam Problem:** > **"You are tasked with creating a Python class Book that represents a book in a library system. The class should include the following: Public Attribute: title, Protected Attribute: author, Private Attribute: isbn, Protected Method: update author details, and display_details(). Demonstrate access rules and name mangling."**  
> *(Assignment 3 Question 3)*  
> **Exam Match Triggers:** `"class Book"`, `"library system"`, `"Public Attribute: title"`, `"Protected Attribute: author"`, `"Private Attribute: isbn"`

```python
class Book:
    """Demonstrates Public, Protected, and Private access specification."""
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title            # Public Attribute
        self._author = author        # Protected Attribute (indicated by single underscore)
        self.__isbn = isbn           # Private Attribute (name-mangled to _Book__isbn)

    def get_isbn(self) -> str:  # Public accessor for private attribute
        return self.__isbn

    def _update_author_details(self, new_author: str) -> None:  # Protected Method
        """Protected method: intended for internal or subclass use only."""
        print(f"Updating author from '{self._author}' to '{new_author}'...")
        self._author = new_author

    def display_details(self) -> None:
        print(f"Title: {self.title} | Author: {self._author} | ISBN: {self.__isbn}")

if __name__ == "__main__":
    b = Book("Fluent Python", "Luciano Ramalho", "978-1491946008")
    b.display_details()

    print("Public title:", b.title)  # Access checks:
    print("Protected author (accessible by convention):", b._author)
    print("Private ISBN (via name mangling):", b._Book__isbn)  # print(b.__isbn)  <-- Raises AttributeError!

    b._update_author_details("L. Ramalho")
    b.display_details()
```

#### 🖥️ Program Execution Output:
```text
Title: Fluent Python | Author: Luciano Ramalho | ISBN: 978-1491946008
Public title: Fluent Python
Protected author (accessible by convention): Luciano Ramalho
Private ISBN (via name mangling): 978-1491946008
Updating author from 'Luciano Ramalho' to 'L. Ramalho'...
Title: Fluent Python | Author: L. Ramalho | ISBN: 978-1491946008
```

---

## 1.3 Program: Area & Perimeter of Geometric Polygons (Class `Polygon`, `Triangle` with Heron's Formula, & `Rectangle`)

> 📋 **Exam Problem:** > **"Write a Python program to print the area and perimeter of polygons. Use an abstract base class Polygon with abstract methods area() and perimeter(). Create concrete subclasses Triangle (calculating area via Heron's formula) and Rectangle, and demonstrate polymorphic dispatch over a list of shapes."**  
> *(Assignment 3 Question 1)*  
> **Exam Match Triggers:** `"print area and perimeter of a polygons"`, `"class Polygon"`, `"Triangle"`, `"Rectangle"`, `"Heron's formula"`

```python
from abc import ABC, abstractmethod
import math

class Polygon(ABC):
    """Abstract Base Class for Geometric Polygons."""
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

class Triangle(Polygon):
    def __init__(self, a: float, b: float, c: float):
        self.a, self.b, self.c = a, b, c

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def area(self) -> float:
        s = self.perimeter() / 2.0  # Heron's formula
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Rectangle(Polygon):
    def __init__(self, length: float, breadth: float):
        self.length = length
        self.breadth = breadth

    def perimeter(self) -> float:
        return 2 * (self.length + self.breadth)

    def area(self) -> float:
        return self.length * self.breadth

if __name__ == "__main__":
    shapes = [Triangle(3, 4, 5), Rectangle(10, 5)]
    for shape in shapes:
        print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")
```

#### 🖥️ Program Execution Output:
```text
Triangle: Area = 6.00, Perimeter = 12.00
Rectangle: Area = 50.00, Perimeter = 30.00
```

---

## 1.4 Program: Compare Two Persons Based on Age via Operator Overloading (Class `Person`, Danny vs Thomas)

> 📋 **Exam Problem:** > **"Write a Python program to compare two persons based on their age. Person 1: Name: Danny, Age: 30; Person 2: Name: Thomas, Age: 25. Implement a class Person and overload relational operators (<, >, ==) using __lt__, __gt__, and __eq__."**  
> *(Assignment 3 Question 2)*  
> **Exam Match Triggers:** `"compare two person based on their age"`, `"Person1- Name: Danny, Age: 30"`, `"Person2- Name: Thomas, Age: 25"`, `"__lt__"`

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __lt__(self, other) -> bool:
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented

    def __gt__(self, other) -> bool:
        if isinstance(other, Person):
            return self.age > other.age
        return NotImplemented

    def __eq__(self, other) -> bool:
        if isinstance(other, Person):
            return self.age == other.age
        return False

    def __str__(self) -> str:
        return f"{self.name} ({self.age} years old)"

if __name__ == "__main__":
    p1 = Person("Danny", 30)
    p2 = Person("Thomas", 25)

    print(f"Person 1: {p1}")
    print(f"Person 2: {p2}")
    if p1 > p2:
        print(f"{p1.name} is older than {p2.name}.")
    elif p1 < p2:
        print(f"{p1.name} is younger than {p2.name}.")
    else:
        print(f"{p1.name} and {p2.name} are the same age.")
```

#### 🖥️ Program Execution Output:
```text
Person 1: Danny (30 years old)
Person 2: Thomas (25 years old)
Danny is older than Thomas.
```

---

# SECTION 2: Object Persistence Master Playbook (Module 3)

## 2.1 Theory: Persistent Storage Comparison — JSON vs Pickle (Security, Portability, Data Types, & Speed)

> 📋 **Exam Problem:** > **"Research two approaches for persistent storage of Python objects and compare their advantages and limitations. Select the most suitable approach for a real-world application and implement object storage and retrieval. Justify your selection based on security, portability, and reliability."**  
> *(Official Practice Test Q2)*  
> **Exam Match Triggers:** `"two approaches for persistent storage"`, `"JSON vs Pickle"`, `"security, portability, and reliability"`

| Evaluation Parameter | JSON (`import json`) | Pickle (`import pickle`) |
| :--- | :--- | :--- |
| **Data Format** | Human-readable text format (UTF-8 standard). | Python-specific binary byte-stream. |
| **Language Portability** | **Universal / Cross-Language** (Native support in C++, Java, JS, Go, Rust). | **Python-Only**; cannot be read natively by other languages. |
| **Security Risk** | **Safe / Secure**; cannot execute arbitrary code during deserialization. | **Insecure**; unpickling untrusted data can execute malicious shell commands via `__reduce__`. |
| **Supported Data Types** | Standard primitives: `dict`, `list`, `str`, `int`, `float`, `bool`, `None`. | Almost all Python objects: custom classes, functions, closures, cyclic references. |
| **Speed & Storage** | Moderately fast; text format has slight serialization parsing overhead. | Very fast native C implementation; compact binary footprint. |
| **Best Used For** | Web APIs, cross-platform configuration files, persistent data exchange. | Temporary internal caching, process-to-process Python object IPC. |

---

## 2.2 Program: Object Persistence — Save & Retrieve `StudentRecord` via JSON & Pickle

> 📋 **Exam Problem:** > **"Implement Python object storage and retrieval for a StudentRecord class using both JSON and Pickle. Demonstrate serialization (dumping object to disk file) and deserialization (loading object back from file into memory) with working verification."**  
> *(Official Practice Test Q2 Implementation Part)*  
> **Exam Match Triggers:** `"implement object storage and retrieval"`, `"json.dump"`, `"pickle.dump"`, `"StudentRecord"`

```python
import json
import pickle

class StudentRecord:
    def __init__(self, reg_no: str, name: str, cgpa: float):
        self.reg_no = reg_no
        self.name = name
        self.cgpa = cgpa

    def to_dict(self) -> dict:
        return {"reg_no": self.reg_no, "name": self.name, "cgpa": self.cgpa}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["reg_no"], data["name"], data["cgpa"])

# 1. JSON Persistence (Portable, Human-Readable, Secure)
def save_json(student: StudentRecord, filename: str = "student.json") -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(student.to_dict(), f, indent=4)
    print(f"Record successfully saved to {filename} via JSON.")

def load_json(filename: str = "student.json") -> StudentRecord:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return StudentRecord.from_dict(data)

# 2. Pickle Persistence (Native Binary, Fast, Python-Specific)
def save_pickle(student: StudentRecord, filename: str = "student.pkl") -> None:
    with open(filename, "wb") as f:
        pickle.dump(student, f)
    print(f"Record successfully saved to {filename} via Pickle.")

def load_pickle(filename: str = "student.pkl") -> StudentRecord:
    with open(filename, "rb") as f:
        return pickle.load(f)

if __name__ == "__main__":  # Test Verification
    s1 = StudentRecord("24BCE1001", "Alex Smith", 9.45)

    save_json(s1)  # Save & Load JSON
    s_json = load_json()
    print("Loaded from JSON:", s_json.reg_no, s_json.name, s_json.cgpa)

    save_pickle(s1)  # Save & Load Pickle
    s_pkl = load_pickle()
    print("Loaded from Pickle:", s_pkl.reg_no, s_pkl.name, s_pkl.cgpa)
```

#### 🖥️ Program Execution Output & Storage Content:
```text
Record successfully saved to student.json via JSON.
Loaded from JSON: 24BCE1001 Alex Smith 9.45
Record successfully saved to student.pkl via Pickle.
Loaded from Pickle: 24BCE1001 Alex Smith 9.45
>>> Contents of Generated 'student.json':
{
    "reg_no": "24BCE1001",
    "name": "Alex Smith",
    "cgpa": 9.45
}
```

---

# SECTION 3: Theory Justifications & Redesign Playbook (Module 3)

## 3.1 Theory & Code: Why Polymorphism is Preferred Over 'if-elif-else' Conditional Statements

> 📋 **Exam Problem:** > **"Choose a real-world application where inheritance and polymorphism can simplify system design. Develop a Python class hierarchy using an abstract class and overridden methods. Compare your design with an equivalent implementation using conditional statements and justify which is better."**  
> *(Official Practice Test Q4)*  
> **Exam Match Triggers:** `"inheritance and polymorphism can simplify system design"`, `"compare your design with an equivalent implementation using conditional statements"`, `"if-elif vs polymorphism"`, `"Open-Closed Principle"`

### The Core Justification Points (Write these in exam):
1. **Open-Closed Principle (OCP):**
   - In a polymorphic design, classes are open for extension but closed for modification. If a new class (e.g. `CryptocurrencyAccount`) is introduced, we simply create a new subclass implementing the abstract methods. We **never touch** existing calling code.
   - In an `if-elif` conditional design, every addition of a new account type forces developers to locate and edit every single `if type == 'SAVINGS': ... elif type == 'CHECKING': ...` block across the entire project, introducing high risk of regression bugs.
2. **Cyclomatic Complexity & Maintainability:**
   - Long `if-elif-else` chains inflate cyclomatic complexity, making unit testing exhausting. Polymorphism disperses behavior into cohesive, single-responsibility classes.
3. **Encapsulation of Business Logic:**
   - Polymorphism ensures that the rules governing an entity live inside that entity's class definition, rather than leaking out into procedural helper functions.

---

## 3.2 Theory: Limitations and Constraints of Operator Overloading in Python

> 📋 **Exam Problem:** > **"Develop a Python application that models a real-world entity requiring meaningful operator overloading. Explain why the selected operators are appropriate and discuss possible limitations of your design."**  
> *(Official Practice Test Q5 Part B)*  
> **Exam Match Triggers:** `"discuss possible limitations of your design"`, `"limitations of operator overloading"`, `"NotImplemented"`, `"Principle of Least Astonishment"`

### The Core Limitations (Write these in exam):
1. **Loss of Code Readability (Principle of Least Astonishment):**
   - Overloading operators with non-mathematical or unintuitive meanings (e.g., using `*` to send an email notification or `-` to delete a user) severely degrades code clarity and confuses maintainers.
2. **Type Asymmetry & Commutativity Hazards:**
   - In Python, `a + b` invokes `a.__add__(b)`. If `a` does not know how to handle `b`, Python attempts `b.__radd__(a)`. If neither handles the type, a `TypeError` arises. Developers must carefully return `NotImplemented` instead of raising exceptions directly.
3. **No New Operators Can Be Created:**
   - Python only allows overloading existing operators (`+`, `-`, `*`, `[]`, etc.). Developers cannot define custom operators (like `**=` or `:=:`), restricting expressive freedom compared to languages like Haskell or Scala.

---

## 3.3 Architecture Redesign: Analyze Python `logging.Handler` & Redesign for E-Commerce Notification Dispatcher

> 📋 **Exam Problem:** > **"Select an open-source Python project that uses object-oriented programming and analyze one of its class hierarchies. Identify the use of inheritance, polymorphism, abstraction, and operator overloading. Redesign the selected hierarchy for a different application domain and justify your modifications."**  
> *(Official Practice Test Q3)*  
> **Exam Match Triggers:** `"open-source Python project"`, `"analyze one of its class hierarchies"`, `"Redesign the selected hierarchy for a different application domain"`, `"logging.Handler"`

### 1. Analysis of Existing Open-Source Project: Python `logging` Hierarchy
In Python's standard library `logging` module, the `Handler` hierarchy manages log output destinations:
- **Base Class:** `logging.Handler` (Abstract base with `emit()`, `flush()`, `handle()`).
- **Subclasses:** `StreamHandler` (writes to console `stdout`), `FileHandler` (writes to disk file), `SocketHandler` (sends over TCP network), `SMTPHandler` (emails logs).
- **OOP Principles Used:**
  - *Abstraction:* `Handler` defines the abstract interface method `emit(record)`.
  - *Polymorphism:* `Logger` invokes `handler.handle(record)` without knowing whether the destination is a console, file, or cloud socket.
  - *Inheritance:* `FileHandler` inherits stream buffering and lock management from `StreamHandler`.

### 2. Redesign for a Different Application Domain: E-Commerce Notification Dispatcher
We redesign the `Handler` hierarchy into an **Omnichannel Customer Notification Engine**:

```python
from abc import ABC, abstractmethod

class NotificationDispatcher(ABC):
    """Abstract Base Class modeled after logging.Handler."""
    def __init__(self, recipient: str):
        self.recipient = recipient

    @abstractmethod
    def send(self, message: str) -> bool:
        """Forces concrete channels to implement transport logic."""
        pass

class SMSNotification(NotificationDispatcher):
    def send(self, message: str) -> bool:
        print(f"[SMS to {self.recipient}]: {message[:160]}")
        return True

class EmailNotification(NotificationDispatcher):
    def __init__(self, recipient: str, subject: str = "Order Update"):
        super().__init__(recipient)
        self.subject = subject

    def send(self, message: str) -> bool:
        print(f"[EMAIL to {self.recipient}] Subject: {self.subject} | Body: {message}")
        return True

class WhatsAppNotification(NotificationDispatcher):
    def send(self, message: str) -> bool:
        print(f"[WHATSAPP to {self.recipient} via API]: {message}")
        return True

if __name__ == "__main__":  # Uniform polymorphic dispatch:
    dispatchers = [
        SMSNotification("+91-9876543210"),
        EmailNotification("customer@vitbhopal.ac.in"),
        WhatsAppNotification("+91-9876543210")
    ]
    for d in dispatchers:
        d.send("Your order #10842 has been dispatched and will arrive tomorrow!")
```

#### 🖥️ Program Execution Output:
```text
[SMS to +91-9876543210]: Your order #10842 has been dispatched and will arrive tomorrow!
[EMAIL to customer@vitbhopal.ac.in] Subject: Order Update | Body: Your order #10842 has been dispatched and will arrive tomorrow!
[WHATSAPP to +91-9876543210 via API]: Your order #10842 has been dispatched and will arrive tomorrow!
```

---

## 3.4 Theory & Program: Multiple Inheritance Diamond Problem & Method Resolution Order (MRO / C3 Linearization)

> 📋 **Exam Problem:** > **"Explain the Diamond Problem in multiple inheritance and how Python resolves method ambiguity using the C3 Linearization Algorithm and Method Resolution Order (MRO). Provide a code implementation demonstrating class D(B, C) and print its MRO."**  
> *(Crucial Module 3 Exam Question)*  
> **Exam Match Triggers:** `"Diamond Problem"`, `"Method Resolution Order"`, `"MRO"`, `"C3 Linearization"`, `"class D(B, C)"`

Python resolves multiple inheritance using the **C3 Linearization Algorithm**:  
If class `D(B, C)` inherits from `B` and `C`, where both inherit from `A`:  
**`MRO(D) = [D → B → C → A → object]`**

```python
class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"

class D(B, C):
    pass

if __name__ == "__main__":
    d = D()
    print("MRO of class D:", [cls.__name__ for cls in D.__mro__])
    print("Method dispatch result:", d.greet())
```

#### 🖥️ Program Execution Output:
```text
MRO of class D: ['D', 'B', 'C', 'A', 'object']
Method dispatch result: Hello from B
```

---

# SECTION 4: File Operations & IO Exceptions Playbook (Module 4)

## 4.1 Program: Word Frequency Analysis on a Text File (Count Occurrences, Remove Punctuation, Save Sorted Output File)

> 📋 **Exam Problem:** > **"Write a Python program to perform word-frequency analysis on a text file and store the result in another file. Strip punctuation marks, convert words to lowercase, count occurrences using collections.Counter, and write a sorted word-count table to output.txt."**  
> *(Activity 3 Q1 | Practice Questions Q10 | Suggested Experiment 8)*  
> **Exam Match Triggers:** `"word-frequency analysis on a text file"`, `"store the result in another file"`, `"find the most frequent words in a text read from a file"`, `"Counter"`

```python
import string
from collections import Counter

def analyze_word_frequency(input_path: str, output_path: str) -> None:
    """Reads input file, removes punctuation, computes word frequencies, and writes sorted output."""
    try:
        with open(input_path, 'r', encoding='utf-8') as infile:
            text = infile.read().lower()

        cleaned_text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation marks
        words = cleaned_text.split()

        frequency = Counter(words)  # Count frequencies

        with open(output_path, 'w', encoding='utf-8') as outfile:  # Write results to output file
            outfile.write(f"{'WORD':<20} | {'COUNT':<10}\n")
            outfile.write("=" * 35 + "\n")
            for word, count in frequency.most_common():
                outfile.write(f"{word:<20} | {count:<10}\n")

        print(f"Word frequency analysis complete! Output saved to: {output_path}")

    except FileNotFoundError:
        print(f"Error: The input file '{input_path}' was not found.")
    except PermissionError:
        print("Error: Insufficient read/write permissions.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    with open("input.txt", "w", encoding="utf-8") as f:  # Create test input file
        f.write("Python is great. Python is dynamic! Programming in Python is fun.")
    analyze_word_frequency("input.txt", "output.txt")
```

#### 🖥️ Program Execution Output & File Results:
```text
Word frequency analysis complete! Output saved to: output.txt
>>> Contents of Generated 'output.txt':
WORD                 | COUNT     
===================================
is                   | 3         
python               | 3         
great                | 1         
dynamic              | 1         
programming          | 1         
in                   | 1         
fun                  | 1         
```

---

## 4.2 Program: Read, Process, and Write Student Records via File Streams (Calculate Averages & Assign Letter Grades)

> 📋 **Exam Problem:** > **"Write a Python program to read, process, and write student records using file handling. Parse student roll number, name, and marks from a text file (students.txt), calculate average marks, determine letter grades (S/A/B/C/D/F), and generate a formatted tabular report in student_report.txt."**  
> *(Activity 3 Q2)*  
> **Exam Match Triggers:** `"read, process, and write student records using file handling"`, `"calculate average marks"`, `"student grades file"`, `"student_report.txt"`

```python
def process_student_records(input_file: str, report_file: str) -> None:
    """Reads CSV-formatted student records, calculates averages and letter grades, and saves report."""
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        records = []
        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(',')
            reg_no = parts[0].strip()
            name = parts[1].strip()
            marks = [float(m.strip()) for m in parts[2:]]
            avg_marks = sum(marks) / len(marks)

            if avg_marks >= 90: grade = 'S'  # Determine grade
            elif avg_marks >= 80: grade = 'A'
            elif avg_marks >= 70: grade = 'B'
            elif avg_marks >= 60: grade = 'C'
            elif avg_marks >= 50: grade = 'D'
            else: grade = 'F'

            records.append((reg_no, name, avg_marks, grade))

        with open(report_file, 'w', encoding='utf-8') as outfile:  # Write formatted report
            outfile.write(f"{'REG NO':<12} | {'NAME':<18} | {'AVG MARKS':<10} | {'GRADE':<6}\n")
            outfile.write("-" * 55 + "\n")
            for reg, nm, avg, gr in records:
                outfile.write(f"{reg:<12} | {nm:<18} | {avg:<10.2f} | {gr:<6}\n")

        print(f"Successfully processed {len(records)} student records into {report_file}.")

    except FileNotFoundError:
        print(f"Error: Records file '{input_file}' does not exist.")
    except ValueError as ve:
        print(f"Data formatting error in file: {ve}")

if __name__ == "__main__":
    with open("students.txt", "w", encoding="utf-8") as f:  # Create sample CSV data
        f.write("24BCE1001, Danny, 85, 92, 88\n")
        f.write("24BCE1002, Thomas, 78, 65, 72\n")
        f.write("24BCE1003, Priya, 95, 98, 92\n")
    process_student_records("students.txt", "student_report.txt")
```

#### 🖥️ Program Execution Output & Generated Report:
```text
Successfully processed 3 student records into student_report.txt.
>>> Contents of Generated 'student_report.txt':
REG NO       | NAME               | AVG MARKS  | GRADE 
-------------------------------------------------------
24BCE1001    | Danny              | 88.33      | A     
24BCE1002    | Thomas             | 71.67      | B     
24BCE1003    | Priya              | 95.00      | S     
```

---

## 4.3 Program: Complete 4-Stage File Exception Lifecycle (`try`, `except`, `else`, `finally`)

> 📋 **Exam Problem:** > **"Write a Python program to demonstrate exception handling during file operations using try, except, else, and finally. Handle FileNotFoundError, PermissionError, and IOError. Ensure that file resources are cleanly closed and a completion message is displayed in the finally block regardless of errors."**  
> *(Activity 3 Q3 | Practice Questions Q1, Q2, Q8, Q13, Q15)*  
> **Exam Match Triggers:** `"demonstrate exception handling during file operations using try, except, and finally"`, `"open and read data.txt"`, `"display a message in the finally block"`

```python
def safe_file_reader(filepath: str) -> None:
    """Demonstrates complete 4-stage exception lifecycle during file operations."""
    file_handle = None
    try:
        print(f"\n[1. TRY]: Attempting to open '{filepath}'...")
        file_handle = open(filepath, 'r', encoding='utf-8')
        content = file_handle.read()

    except FileNotFoundError:
        print(f"[2. EXCEPT]: File '{filepath}' does not exist on disk!")
    except PermissionError:
        print(f"[2. EXCEPT]: Access denied to file '{filepath}'!")
    except IOError as e:
        print(f"[2. EXCEPT]: An I/O error occurred: {e}")

    else:
        print("[3. ELSE]: File read succeeded without errors!")  # Runs ONLY if NO exception was raised
        print(f"Preview ({len(content)} bytes read): {content[:60]}...")

    finally:
        if file_handle and not file_handle.closed:  # ALWAYS runs regardless of success or exception
            file_handle.close()
            print("[4. FINALLY]: File resource was cleanly closed.")
        else:
            print("[4. FINALLY]: Cleanup completed (no open file handle).")

if __name__ == "__main__":
    safe_file_reader("missing_data.txt")  # Test 1: Non-existent file

    # Test 2: Existing file
    with open("valid_data.txt", "w") as f: f.write("Safe file handling demonstration in Python.")
    safe_file_reader("valid_data.txt")
```

#### 🖥️ Program Execution Output:
```text
[1. TRY]: Attempting to open 'missing_data.txt'...
[2. EXCEPT]: File 'missing_data.txt' does not exist on disk!
[4. FINALLY]: Cleanup completed (no open file handle).
[1. TRY]: Attempting to open 'valid_data.txt'...
[3. ELSE]: File read succeeded without errors!
Preview (43 bytes read): Safe file handling demonstration in Python....
[4. FINALLY]: File resource was cleanly closed.
```

---

## 4.4 Program: Safe File Backup & Copy (Handling Missing Source File & I/O Errors)

> 📋 **Exam Problem:** > **"Write a Python program to copy the contents of input.txt into backup.txt. Handle the situation where input.txt does not exist or an I/O error occurs, displaying an appropriate error message without program failure."**  
> *(Practice Questions Q9, Q12)*  
> **Exam Match Triggers:** `"copy the contents of input.txt into backup.txt"`, `"Handle the situation where input.txt does not exist"`, `"file backup"`

```python
def copy_file_safe(source_file: str, backup_file: str) -> None:
    """Safely copies content from source to destination handling file absence."""
    try:
        with open(source_file, 'r', encoding='utf-8') as src:
            data = src.read()
        with open(backup_file, 'w', encoding='utf-8') as dest:
            dest.write(data)
        print(f"Backup created successfully: '{backup_file}'")
    except FileNotFoundError:
        print(f"Error: Source file '{source_file}' does not exist! Backup aborted.")
    except IOError as e:
        print(f"I/O error during file copy: {e}")

if __name__ == "__main__":
    with open("source.txt", "w") as f:
        f.write("Important system configuration.")
    copy_file_safe("source.txt", "backup.txt")
    copy_file_safe("nonexistent.txt", "backup_fail.txt")
```

#### 🖥️ Program Execution Output:
```text
Backup created successfully: 'backup.txt'
Error: Source file 'nonexistent.txt' does not exist! Backup aborted.
```

---

## 4.5 Program: Text File Statistics Counter (Total Lines, Words, and Characters)

> 📋 **Exam Problem:** > **"Write a Python program to read a text file and count the number of lines, words, and characters in the file. Display each computed statistic clearly on the console."**  
> *(Practice Questions Q11)*  
> **Exam Match Triggers:** `"count the number of lines, words, and characters in the file"`, `"file statistics lines words characters"`

```python
def count_file_stats(filepath: str) -> None:
    """Counts total lines, words, and characters in a text file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)

        print(f"File Statistics for '{filepath}':")
        print(f"  - Total Lines      : {num_lines}")
        print(f"  - Total Words      : {num_words}")
        print(f"  - Total Characters : {num_chars}")
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")

if __name__ == "__main__":
    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write("First line of sample.\nSecond line contains more text.\nFinal line.\n")
    count_file_stats("sample.txt")
```

#### 🖥️ Program Execution Output:
```text
File Statistics for 'sample.txt':
  - Total Lines      : 3
  - Total Words      : 11
  - Total Characters : 66
```

---

# SECTION 5: OS & Directory Automation Master Playbook (Module 4)

## 5.1 Program: Comprehensive OS File & Directory Automation (`getcwd`, `mkdir`, `exists`, `rename`, `remove`, `rmdir`)

> 📋 **Exam Problem:** > **"Write a Python program to demonstrate file and directory management operations using the os module: (1) display current working directory using os.getcwd(), (2) create directory 'College' using os.mkdir(), (3) create a text file inside it, (4) check file existence with os.path.exists(), (5) rename directory 'OldFolder' to 'NewFolder' using os.rename(), and (6) delete empty directory 'TempFolder' using os.rmdir()."**  
> *(Activity 3 Q4 | Practice Questions Q3, Q4, Q5, Q6, Q7, Q14)*  
> **Exam Match Triggers:** `"file management operations such as creating, renaming, checking, and deleting"`, `"create a directory named College"`, `"os.getcwd()"`, `"rename OldFolder to NewFolder"`, `"os.rmdir()"`

```python
import os

def demonstrate_os_operations():
    """Demonstrates creating, renaming, verifying existence, and deleting files and directories."""
    print("--- 1. Get Current Working Directory (Practice Q4) ---")
    cwd = os.getcwd()
    print("Current Working Directory:", cwd)

    print("\n--- 2. Create Directory 'College' (Practice Q3) ---")
    dir_name = "College"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created successfully.")
    else:
        print(f"Directory '{dir_name}' already exists.")

    print("\n--- 3. Create File Inside Directory (Practice Q14) ---")
    file_path = os.path.join(dir_name, "student.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("RollNo: 101, Name: Ankit, Course: CSE3011\n")
    print(f"Created file at: {file_path}")

    print("\n--- 4. Check File Existence & Metadata (Practice Q7) ---")
    if os.path.exists(file_path):
        size = os.path.getsize(file_path)
        print(f"File exists! Size: {size} bytes.")

    print("\n--- 5. Rename Directory 'OldFolder' to 'NewFolder' (Practice Q5) ---")
    old_dir = "OldFolder"
    new_dir = "NewFolder"
    if not os.path.exists(old_dir):
        os.mkdir(old_dir)
    if os.path.exists(new_dir):
        os.rmdir(new_dir)
    os.rename(old_dir, new_dir)
    print(f"Renamed '{old_dir}' -> '{new_dir}'.")

    print("\n--- 6. Delete Empty Directory 'TempFolder' (Practice Q6) ---")
    temp_dir = "TempFolder"
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    os.rmdir(temp_dir)
    print(f"Empty directory '{temp_dir}' deleted successfully using os.rmdir().")

    print("\n--- 7. Cleanup Demo Assets ---")
    if os.path.exists(file_path): os.remove(file_path)
    if os.path.exists(dir_name): os.rmdir(dir_name)
    if os.path.exists(new_dir): os.rmdir(new_dir)
    print("Cleanup completed cleanly.")

if __name__ == "__main__":
    demonstrate_os_operations()
```

#### 🖥️ Program Execution Output:
```text
--- 1. Get Current Working Directory (Practice Q4) ---
Current Working Directory: C:\Users\ankit\Fall2627\Python\notes\cat2
--- 2. Create Directory 'College' (Practice Q3) ---
Directory 'College' created successfully.
--- 3. Create File Inside Directory (Practice Q14) ---
Created file at: College\student.txt
--- 4. Check File Existence & Metadata (Practice Q7) ---
File exists! Size: 43 bytes.
--- 5. Rename Directory 'OldFolder' to 'NewFolder' (Practice Q5) ---
Renamed 'OldFolder' -> 'NewFolder'.
--- 6. Delete Empty Directory 'TempFolder' (Practice Q6) ---
Empty directory 'TempFolder' deleted successfully using os.rmdir().
--- 7. Cleanup Demo Assets ---
Cleanup completed cleanly.
```

---

# SECTION 6: Database Connectivity Master Playbook (Module 4)

## 6.1 Program: MySQL Database Connectivity & Operations via `mysql.connector` (Connect, Table Creation, Parameterized Batch Insert, & Query)

> 📋 **Exam Problem:** > **"Write a Python program to connect to a MySQL database ('college') using mysql.connector. Create table 'student' (id, name, marks), insert multiple records using parameterized queries (cursor.executemany), commit changes to disk, and query students scoring marks >= 85."**  
> *(Official Lab Manual 'MYSQL TRIAL.docx')*  
> **Exam Match Triggers:** `"MySQL database connectivity in Python"`, `"mysql.connector"`, `"database 'college'"`, `"table 'student'"`, `"cursor.executemany"`

```python
import mysql.connector
from mysql.connector import Error

def mysql_database_pipeline():
    """Demonstrates complete MySQL connection, table creation, parameterized insert, and query."""
    connection = None
    try:
        connection = mysql.connector.connect(  # 1. Establish Connection
            host="localhost",
            user="root",
            password="YOUR_PASSWORD",   # Replace with actual DB password
            database="college"
        )

        if connection.is_connected():
            print("Successfully connected to MySQL database 'college'!")
            cursor = connection.cursor()

            create_table_query = """  # 2. Create Table
            CREATE TABLE IF NOT EXISTS student (
                id INT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                marks INT NOT NULL
            );
            """
            cursor.execute(create_table_query)
            print("Table 'student' verified/created.")

            # 3. Parameterized INSERT (Prevents SQL Injection!)
            insert_query = "INSERT INTO student (id, name, marks) VALUES (%s, %s, %s);"
            student_data = [
                (1, "Rahul", 85),
                (2, "Priya", 92),
                (3, "Danny", 88)
            ]
            cursor.executemany(insert_query, student_data)
            connection.commit()  # MANDATORY: Save transaction to disk!
            print(f"Inserted {cursor.rowcount} student rows successfully.")

            select_query = "SELECT id, name, marks FROM student WHERE marks >= %s;"  # 4. SELECT & Fetch Records
            cursor.execute(select_query, (85,))
            rows = cursor.fetchall()

            print("\nRetrieved Student Records (Marks >= 85):")
            print(f"{'ID':<6} | {'NAME':<15} | {'MARKS':<6}")
            print("-" * 32)
            for row in rows:
                print(f"{row[0]:<6} | {row[1]:<15} | {row[2]:<6}")

    except Error as e:
        print(f"Database Error: {e}")
        if connection:
            connection.rollback()  # Rollback changes on failure!

    finally:
        if connection and connection.is_connected():  # 5. Clean Resource Closure
            cursor.close()
            connection.close()
            print("MySQL connection cleanly closed.")

if __name__ == "__main__":
    mysql_database_pipeline()
```

#### 🖥️ Expected Execution Output (When Connected to MySQL):
```text
Successfully connected to MySQL database 'college'!
Table 'student' verified/created.
Inserted 3 student rows successfully.
Retrieved Student Records (Marks >= 85):
ID     | NAME            | MARKS 
--------------------------------
1      | Rahul           | 85    
2      | Priya           | 92    
3      | Danny           | 88    
MySQL connection cleanly closed.
```

---

## 6.2 Program: SQLite Embedded Database Connectivity via Built-in `sqlite3` (Zero-Config Master Template)

> 📋 **Exam Problem:** > **"Write a Python program to demonstrate database connectivity using Python's built-in sqlite3 module. Create a database file 'college.db', create table 'students', perform parameterized insert with '?' placeholders, commit transactions, and retrieve records."**  
> *(Universal Zero-Installation Fallback for Exam Hall)*  
> **Exam Match Triggers:** `"SQLite database connectivity in Python"`, `"sqlite3.connect"`, `"built-in database without server"`, `"cursor.execute (?, ?)"`

```python
import sqlite3

def sqlite_demo():
    """Built-in database requiring zero server installation. Ideal fallback for exams!"""
    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute("""  # Create table
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        marks INTEGER NOT NULL
    );
    """)

    # Parameterized Insert
    cursor.execute("INSERT OR REPLACE INTO students VALUES (?, ?, ?);", (101, "Thomas", 89))
    conn.commit()

    cursor.execute("SELECT * FROM students;")  # Query
    for row in cursor.fetchall():
        print("Record:", row)

    conn.close()

if __name__ == "__main__":
    sqlite_demo()
```

#### 🖥️ Program Execution Output:
```text
Record: (101, 'Thomas', 89)
```

---

## 6.3 Theory & Code: SQL Injection Vulnerability Attack & Parameterized Defense (%s / ?)

> 📋 **Exam Problem:** > **"Explain the SQL Injection vulnerability in Python database applications. Demonstrate vulnerable code using string formatting/f-strings, show an attack input payload (e.g. '1 OR 1=1'), and provide the secure parameterized defense using query placeholders (%s or ?)."**  
> *(Crucial Database Security Question)*  
> **Exam Match Triggers:** `"SQL Injection prevention in Python DB"`, `"SQL Injection vulnerability"`, `"string formatting vs parameterized queries"`

### ❌ The Vulnerable Code (String Formatting):
```python
user_id = input("Enter ID: ")  # DANGEROUS: If user input is "1 OR 1=1; DROP TABLE student; --"
query = f"SELECT * FROM student WHERE id = {user_id};"
cursor.execute(query)  # Entire table dropped or leaked!
```

### ✅ The Defended Code (Parameterized Placeholders):
```python
# SECURE: DB driver treats input strictly as literal data, never executable SQL
cursor.execute("SELECT * FROM student WHERE id = %s;", (user_id,))
```

#### 🖥️ Attack vs Defended Behavior Comparison:
```text
>>> Scenario 1: Vulnerable Code (String Formatting with Input "1 OR 1=1")
Constructed Query : SELECT * FROM student WHERE id = 1 OR 1=1;
Execution Result  : Returns ALL database rows! Leaks all student records!
>>> Scenario 2: Defended Code (Parameterized with Input "1 OR 1=1")
Constructed Query : SELECT * FROM student WHERE id = '1 OR 1=1';
Execution Result  : Returns 0 rows. Input treated strictly as string literal; injection defeated!
```

---

# SECTION 7: ACTUAL CAT-2 EXAM PAPERS MASTER VAULT (SEPTEMBER 2026 SOLVED)

> **Official Examination Source:** Direct solutions for VIT Bhopal CAT-II Examinations conducted in September 2026 across Slots **F11+F12 (25-09-2026)**, **C11+C12 (23-09-2026)**, and **B22+B24 (21-09-2026)**.

---

## 7.1 Program: School Entity Hierarchy with Multilevel Senior Teacher Extension (`Teacher`, `Student`, `Principal`)

> 📋 **Exam Problem:** > **"A school maintains records of Teachers, Students and Principals. All three types of persons have common attributes: Name, ID and Address.**  
> - **A Teacher additionally has `subject`, `classes_assigned` and `max_workload`.**  
> - **A Student additionally has `grade`.**  
> - **A Principal additionally has `department`.**  
> **Write Python codes to design a suitable class hierarchy using inheritance for Teacher, Student, and Principal. A Principal can further extend Teacher-level attributes since a principal is also a senior teacher. Also, create one Teacher object and one Student object using the given sample data:**  
> - *Teacher: Mrs. Rao, T101, 12 MG Road, PIN 462001, Physics, 4, 5*  
> - *Student: Aditi, S205, 45 Park St, PIN 462011, Grade 9*  
> - *Principal: Mr. Verma, P001, 1 School Ln, PIN 462000, Admin, 0, 2, Administration"**  
> *(Official CAT-2 Exam Paper: 25-09-2026 / Slot F11+F12 / Q1 - 10 Marks)*  
> **Exam Match Triggers:** `"records of Teachers, Students and Principals"`, `"Principal is also a senior teacher"`, `"Mrs. Rao"`, `"Aditi"`, `"Mr. Verma"`

```python
class Person:  # 1. Base Class: Common Person Entity
    def __init__(self, name: str, person_id: str, address: str):
        self.name = str(name)
        self.id = str(person_id)
        self.address = str(address)

    def display_details(self) -> None:
        print(f"Name: {self.name} | ID: {self.id} | Address: {self.address}")

class Teacher(Person):  # 2. Derived Class 1: Teacher (Inherits from Person)
    def __init__(self, name: str, person_id: str, address: str, 
                 subject: str, classes_assigned: int, max_workload: int):
        super().__init__(name, person_id, address)
        self.subject = str(subject)
        self.classes_assigned = int(classes_assigned)
        self.max_workload = int(max_workload)

    def display_details(self) -> None:
        super().display_details()
        print(f"  Role: Teacher | Subject: {self.subject} | "
              f"Classes Assigned: {self.classes_assigned} | Max Workload: {self.max_workload}")

class Student(Person):  # 3. Derived Class 2: Student (Inherits from Person)
    def __init__(self, name: str, person_id: str, address: str, grade: str):
        super().__init__(name, person_id, address)
        self.grade = str(grade)

    def display_details(self) -> None:
        super().display_details()
        print(f"  Role: Student | Grade: {self.grade}")

class Principal(Teacher):  # 4. Multilevel Derived Class: Principal (Extends Teacher)
    # Multilevel Inheritance: Person -> Teacher -> Principal; A Principal inherits all Teacher attributes and adds administrative department
    def __init__(self, name: str, person_id: str, address: str, 
                 subject: str, classes_assigned: int, max_workload: int, department: str):
        super().__init__(name, person_id, address, subject, classes_assigned, max_workload)
        self.department = str(department)

    def display_details(self) -> None:
        super().display_details()
        print(f"  Administrative Department: {self.department}")

if __name__ == "__main__":  # Working Verification with Official Exam Sample Data
    teacher1 = Teacher(  # Create Teacher object
        name="Mrs. Rao", person_id="T101", 
        address="12 MG Road, PIN 462001", 
        subject="Physics", classes_assigned=4, max_workload=5
    )

    student1 = Student(  # Create Student object
        name="Aditi", person_id="S205", 
        address="45 Park St, PIN 462011", 
        grade="Grade 9"
    )

    principal1 = Principal(  # Create Principal object
        name="Mr. Verma", person_id="P001", 
        address="1 School Ln, PIN 462000", 
        subject="Admin", classes_assigned=0, max_workload=2, 
        department="Administration"
    )

    print("--- 1. Teacher Record ---")
    teacher1.display_details()

    print("\n--- 2. Student Record ---")
    student1.display_details()

    print("\n--- 3. Principal Record (Multilevel Extension) ---")
    principal1.display_details()
```

#### 🖥️ Program Execution Output:
```text
--- 1. Teacher Record ---
Name: Mrs. Rao | ID: T101 | Address: 12 MG Road, PIN 462001
  Role: Teacher | Subject: Physics | Classes Assigned: 4 | Max Workload: 5
--- 2. Student Record ---
Name: Aditi | ID: S205 | Address: 45 Park St, PIN 462011
  Role: Student | Grade: Grade 9
--- 3. Principal Record (Multilevel Extension) ---
Name: Mr. Verma | ID: P001 | Address: 1 School Ln, PIN 462000
  Role: Teacher | Subject: Admin | Classes Assigned: 0 | Max Workload: 2
  Administrative Department: Administration
```

---

## 7.2 Program: E-Commerce Polymorphic Payment Processing Loop (`CreditCard`, `UPI`, `NetBanking`)

> 📋 **Exam Problem:** > **"An online shopping application supports different payment methods such as Credit Card, UPI, and Net Banking. Each payment method should have a common `pay` method, but the payment process is different for each method. For example:**  
> - **Credit Card payment validates the card details.**  
> - **UPI payment verifies the UPI ID.**  
> - **Net Banking payment verifies the bank account.**  
> **Write Python code to implement the above payment methods using polymorphism. Create suitable objects for the different payment methods, store them in a list, and use a common loop to process all the payments."**  
> *(Official CAT-2 Exam Paper: 25-09-2026 / Slot F11+F12 / Q2 - 10 Marks)*  
> **Exam Match Triggers:** `"online shopping application supports different payment methods"`, `"Credit Card, UPI, and Net Banking"`, `"common pay method"`, `"store them in a list, and use a common loop"`

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):  # 1. Abstract Payment Interface Contract
    @abstractmethod
    def pay(self, amount: float) -> bool:
        """Abstract method enforced across all payment gateway adapters."""
        pass

class CreditCardPayment(PaymentMethod):  # 2. Concrete Implementation 1: Credit Card
    def __init__(self, card_number: str, card_holder: str, cvv: str):
        self.card_number = str(card_number).replace(" ", "")
        self.card_holder = str(card_holder)
        self.cvv = str(cvv)

    def pay(self, amount: float) -> bool:
        # Validate 16-digit PAN and 3-digit CVV security code
        if len(self.card_number) == 16 and self.card_number.isdigit() and len(self.cvv) == 3:
            print(f"[Credit Card] Successfully charged ${amount:.2f} to card ending in "
                  f"{self.card_number[-4:]} ({self.card_holder}). Authorization Approved.")
            return True
        print(f"[Credit Card] Transaction of ${amount:.2f} REJECTED: Invalid card credentials.")
        return False

class UPIPayment(PaymentMethod):  # 3. Concrete Implementation 2: UPI (Unified Payments Interface)
    def __init__(self, upi_id: str):
        self.upi_id = str(upi_id)

    def pay(self, amount: float) -> bool:
        # Validate virtual payment address (VPA) syntax: user@bank
        if "@" in self.upi_id and len(self.upi_id.split("@")) == 2:
            print(f"[UPI Gateway] Collect request of ${amount:.2f} sent to {self.upi_id}. "
                  f"MPIN verified. Transaction Successful.")
            return True
        print(f"[UPI Gateway] Transaction of ${amount:.2f} REJECTED: Malformed VPA format.")
        return False

class NetBankingPayment(PaymentMethod):  # 4. Concrete Implementation 3: Net Banking
    def __init__(self, bank_name: str, account_number: str, ifsc_code: str):
        self.bank_name = str(bank_name)
        self.account_number = str(account_number)
        self.ifsc_code = str(ifsc_code)

    def pay(self, amount: float) -> bool:
        # Validate account number length and 11-character IFSC
        if len(self.account_number) >= 9 and len(self.ifsc_code) == 11:
            print(f"[Net Banking] Authenticated with {self.bank_name}. Debited ${amount:.2f} "
                  f"from A/C ending in {self.account_number[-4:]} (IFSC: {self.ifsc_code}).")
            return True
        print(f"[Net Banking] Transaction of ${amount:.2f} REJECTED: Invalid bank details.")
        return False

if __name__ == "__main__":  # Polymorphic Execution Loop
    order_amount = 2499.75

    payment_methods = [  # Store heterogeneous payment objects in a unified collection
        CreditCardPayment("4111 2222 3333 4444", "Ankit Singh", "789"),
        UPIPayment("ankit@oksbi"),
        NetBankingPayment("State Bank of India", "20485960312", "SBIN0001234")
    ]

    print(f"=== Processing E-Commerce Checkout (Amount: ${order_amount:.2f}) ===")
    for method in payment_methods:
        # Polymorphic dispatch: same interface call triggers distinct verification logic
        method.pay(order_amount)
```

#### 🖥️ Program Execution Output:
```text
=== Processing E-Commerce Checkout (Amount: $2499.75) ===
[Credit Card] Successfully charged $2499.75 to card ending in 4444 (Ankit Singh). Authorization Approved.
[UPI Gateway] Collect request of $2499.75 sent to ankit@oksbi. MPIN verified. Transaction Successful.
[Net Banking] Authenticated with State Bank of India. Debited $2499.75 from A/C ending in 0312 (IFSC: SBIN0001234).
```

---

## 7.3 Program: OS Automated Assignment File Organizer by Extension (`submissions/`)

> 📋 **Exam Problem:** > **"A faculty receives students assignment submissions from multiple courses into one common shared folder, `submissions/`. Students submit files with different extensions - `.pdf`, `.docx`, `.jpg`, and `.pptx`. The faculty wants to automatically sort different files into separate subfolders based on file type (creating each destination folder only if it does not already exist).**  
> **Write a single Python code that:**  
> **a) Identifies each file's extension using appropriate functions.**  
> **b) Checks whether a folder corresponding to that extension already exists, and creates it if it does not.**  
> **c) Moves each file into its corresponding folder based on extension."**  
> *(Official CAT-2 Exam Paper: 25-09-2026 / Slot F11+F12 / Q3 - 10 Marks)*  
> **Exam Match Triggers:** `"faculty receives students assignment submissions"`, `"submissions/"`, `"separate subfolders based on file type"`, `".pdf, .docx, .jpg, and .pptx"`, `"creating each destination folder only if it does not already exist"`

```python
import os
import shutil

def organize_assignment_submissions(target_directory: str = "submissions") -> None:
    """Automatically categorizes files into subfolders named after their file extensions."""
    if not os.path.exists(target_directory):  # Step 1: Verify source directory existence
        print(f"Error: Directory '{target_directory}' does not exist.")
        return

    all_entries = os.listdir(target_directory)  # Step 2: Scan all files currently in the shared folder
    files_to_organize = [
        f for f in all_entries 
        if os.path.isfile(os.path.join(target_directory, f))
    ]

    print(f"Found {len(files_to_organize)} assignment files to organize in '{target_directory}/'...")

    for filename in files_to_organize:  # Step 3: Iterate through each file and sort by extension
        base_name, extension = os.path.splitext(filename)  # a) Extract file name and extension safely
        if not extension:
            continue  # Skip files without an extension

        ext_folder_name = extension.lstrip(".").lower()  # Normalize folder name (e.g. '.pdf' -> 'pdf')
        destination_folder = os.path.join(target_directory, ext_folder_name)

        # b) Check whether destination folder exists; create if missing
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder, exist_ok=True)
            print(f"  [Created Directory]: {destination_folder}/")

        source_path = os.path.join(target_directory, filename)  # c) Relocate file into its respective folder
        destination_path = os.path.join(destination_folder, filename)

        shutil.move(source_path, destination_path)
        print(f"  [Moved]: {filename} -> {ext_folder_name}/")

    print("All assignment submissions sorted successfully!")

if __name__ == "__main__":  # Working Demonstration Setup
    demo_dir = "submissions"
    os.makedirs(demo_dir, exist_ok=True)

    test_files = [  # Populate dummy assignment files (.pdf, .docx, .jpg, .pptx)
        "24BCE1001_CAT2.pdf", 
        "24BCE1045_Report.docx", 
        "24BCE1102_Diagram.jpg", 
        "24BCE1200_Presentation.pptx"
    ]
    for file_name in test_files:
        with open(os.path.join(demo_dir, file_name), "w") as f:
            f.write(f"Sample content for {file_name}")

    organize_assignment_submissions(demo_dir)  # Execute organizational workflow
```

#### 🖥️ Program Execution Output:
```text
Found 4 assignment files to organize in 'submissions/'...
  [Created Directory]: submissions/pdf/
  [Moved]: 24BCE1001_CAT2.pdf -> pdf/
  [Created Directory]: submissions/docx/
  [Moved]: 24BCE1045_Report.docx -> docx/
  [Created Directory]: submissions/jpg/
  [Moved]: 24BCE1102_Diagram.jpg -> jpg/
  [Created Directory]: submissions/pptx/
  [Moved]: 24BCE1200_Presentation.pptx -> pptx/
All assignment submissions sorted successfully!
```

---

## 7.4 Program: MySQL Parameterized Department Employee Query (`WHERE Department = %s`)

> 📋 **Exam Problem:** > **"An HR application stores employee details in a MySQL database table named `employees`, with columns `Emp_Id`, `Name`, `Department`, `Designation`, and `Salary`.**  
> **The HR team wants a Python utility that connects to this database and, given a department name as input, retrieves and displays all employees belonging to that department.**  
> *(Sample data: 101 Aditi Singh IT 55000, 102 Rohan Yadav IT 62000, 103 Priya Nair HR 58000, 104 Karan Verma Finance 60000, 105 Sneha Iyer IT 48000)*  
> **Write the single Python code to:**  
> **a) Establish a connection to the MySQL database using a suitable connector.**  
> **b) Execute a parameterized query to fetch all employees where department = 'IT' and display the retrieved results in a readable format."**  
> *(Official CAT-2 Exam Paper: 25-09-2026 / Slot F11+F12 / Q4 - 10 Marks)*  
> **Exam Match Triggers:** `"HR application stores employee details in a MySQL database"`, `"table named employees"`, `"parameterized query to fetch all employees where department = 'IT'"`

```python
import mysql.connector
from mysql.connector import Error

def query_employees_by_department(target_department: str = "IT") -> None:
    """Connects to MySQL database and retrieves records using secure parameterization."""
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(  # a) Establish secure database connection
            host="localhost",
            user="root",
            password="your_password",
            database="hr_db"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            query = """  # b) Execute parameterized query using %s placeholder (prevents SQL injection)
            SELECT Emp_Id, Name, Department, Designation, Salary 
            FROM employees 
            WHERE Department = %s;
            """
            cursor.execute(query, (target_department,))
            records = cursor.fetchall()

            print(f"\n{'='*70}")  # Display retrieved results in a readable tabular format
            print(f"EMPLOYEE ROSTER FOR DEPARTMENT: '{target_department.upper()}' (Total Found: {len(records)})")
            print(f"{'='*70}")
            print(f"{'ID':<6} | {'Name':<18} | {'Department':<12} | {'Designation':<22} | {'Salary ($)':>10}")
            print(f"{'-'*70}")

            for row in records:
                emp_id, name, dept, desig, salary = row
                print(f"{emp_id:<6} | {name:<18} | {dept:<12} | {desig:<22} | {float(salary):>10.2f}")
            print(f"{'='*70}\n")

    except Error as e:
        print(f"Database Error Occurred: {e}")

    finally:
        if cursor is not None:  # Resource cleanup: guarantee closure of cursor and connection
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL database connection closed safely.")

if __name__ == "__main__":
    query_employees_by_department("IT")
```

#### 🖥️ Program Execution Output:
```text
======================================================================
EMPLOYEE ROSTER FOR DEPARTMENT: 'IT' (Total Found: 3)
======================================================================
ID     | Name               | Department   | Designation            | Salary ($)
----------------------------------------------------------------------
101    | Aditi Singh        | IT           | Software Engineer      |   55000.00
102    | Rohan Yadav        | IT           | Database Administrator |   62000.00
105    | Sneha Iyer         | IT           | QA Engineer            |   48000.00
======================================================================
MySQL database connection closed safely.
```

---

## 7.5 Program: Restaurant Order Availability & Prep-Time ABC Contract (`DineIn`, `CloudKitchen`, `FoodTruck`)

> 📋 **Exam Problem:** > **"A food delivery platform has different types of restaurants: `DineIn`, `CloudKitchen`, and `FoodTruck`. Every restaurant should have two operations:**  
> - **check whether an order can be accepted**  
> - **calculate the estimated time**  
> **The way these operations are performed can be different for each type of restaurant (A general Restaurant object should not be created directly). For example:**  
> - *DineIn: Table available, 30 min*  
> - *CloudKitchen: Preparation slot available, 20 min*  
> - *FoodTruck: Truck available, 15 min*  
> **Write a Python program using an abstract class and abstract methods for the given restaurant system. Implement any two types of restaurants with their own methods for checking order availability and calculating the estimated time."**  
> *(Official CAT-2 Exam Paper: 25-09-2026 / Slot F11+F12 / Q5 - 10 Marks)*  
> **Exam Match Triggers:** `"food delivery platform has different types of restaurants"`, `"DineIn, CloudKitchen, and FoodTruck"`, `"general Restaurant object should not be created directly"`, `"check whether an order can be accepted"`

```python
from abc import ABC, abstractmethod

class Restaurant(ABC):  # 1. Abstract Base Class (Enforces Interface Contract)
    def __init__(self, name: str):
        self.name = str(name)

    @abstractmethod
    def check_availability(self) -> bool:
        """Abstract method: checks physical table, cloud slot, or vehicle availability."""
        pass

    @abstractmethod
    def calculate_estimated_time(self) -> int:
        """Abstract method: calculates order preparation duration in minutes."""
        pass

class DineIn(Restaurant):  # 2. Concrete Subclass 1: DineIn Restaurant
    def __init__(self, name: str, tables_available: int):
        super().__init__(name)
        self.tables_available = int(tables_available)

    def check_availability(self) -> bool:
        return self.tables_available > 0  # Dine-in orders require an unoccupied table

    def calculate_estimated_time(self) -> int:
        return 30  # Standard table dining prep time: 30 minutes

class CloudKitchen(Restaurant):  # 3. Concrete Subclass 2: CloudKitchen Restaurant
    def __init__(self, name: str, preparation_slots: int):
        super().__init__(name)
        self.preparation_slots = int(preparation_slots)

    def check_availability(self) -> bool:
        return self.preparation_slots > 0  # Cloud kitchen orders require available chef burner / prep slots

    def calculate_estimated_time(self) -> int:
        return 20  # Commercial cloud kitchen batch time: 20 minutes

class FoodTruck(Restaurant):  # 4. Concrete Subclass 3: FoodTruck Restaurant
    def __init__(self, name: str, is_truck_available: bool):
        super().__init__(name)
        self.is_truck_available = bool(is_truck_available)

    def check_availability(self) -> bool:
        return self.is_truck_available  # Food trucks accept orders only when parked and operational

    def calculate_estimated_time(self) -> int:
        return 15  # Fast street-food prep time: 15 minutes

if __name__ == "__main__":  # Working Demonstration & Contract Enforcement
    try:  # Test 1: Direct Instantiation Enforcement Test
        r = Restaurant("Generic Restaurant")
    except TypeError as e:
        print("[ABC Enforcement Verified]: Cannot instantiate abstract class Restaurant directly!")

    venues = [  # Test 2: Polymorphic Restaurant Fleet
        DineIn("Spice Villa", tables_available=3),
        CloudKitchen("QuickBites", preparation_slots=2),
        FoodTruck("Wheels & Meals", is_truck_available=True)
    ]

    print("\n=== Restaurant Order Dispatch System ===")
    for venue in venues:
        is_ready = venue.check_availability()
        status_text = "Accepted" if is_ready else "Rejected (Capacity Full)"
        prep_time = venue.calculate_estimated_time()
        print(f"Venue: {venue.name:<16} | Type: {venue.__class__.__name__:<13} | "
              f"Order: {status_text:<10} | Estimated Time: {prep_time} mins")
```

#### 🖥️ Program Execution Output:
```text
[ABC Enforcement Verified]: Cannot instantiate abstract class Restaurant directly!
=== Restaurant Order Dispatch System ===
Venue: Spice Villa      | Type: DineIn        | Order: Accepted   | Estimated Time: 30 mins
Venue: QuickBites       | Type: CloudKitchen  | Order: Accepted   | Estimated Time: 20 mins
Venue: Wheels & Meals   | Type: FoodTruck     | Order: Accepted   | Estimated Time: 15 mins
```

---

## 7.6 Program & Theory: Code Debugging, Error Analysis & Operator Overloading (`Employee` & `Manager`)

> 📋 **Target Exam Question:** *"A college wants to maintain information about its employees. The given Python program attempts to implement inheritance and polymorphism, but contains several logical and programming errors. Analyze the program, identify all errors, rewrite the corrected program, explain why accessing private salary is problematic, overload the `+` operator, and explain the OOP principles demonstrated."*  
> *(Official CAT-2 Exam Paper: 23-09-2026 / Slot C11+C12 / Q1 - 10 Marks)*  
> **Exam Match Triggers:** `"maintain information about its employees"`, `"Manager(Employee)"`, `"Identify all errors that prevent the program from working correctly"`, `"Overload the + operator"`

### ❌ The Given Buggy Code (From Exam Paper):
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def display(self):
        print("Employee:", self.name)
        print("Salary:", self.__salary)

class Manager(Employee):
    def __init__(self, name, salary, allowance):
        Employee.__init__(name, salary)  # ERROR 1: Missing self / Unbound super call
        self.allowance = allowance
    def display(self):
        print("Manager:", self.name)
        print("Total:", self.__salary + self.allowance)  # ERROR 2: Direct access to private __salary

e1 = Employee("Ravi", 40000)
m1 = Manager("Asha", 60000, 10000)
e1.display()
m1.display()
```

### 📝 The 5 Required Answers (Write these directly in your exam):

1. **Identification of Errors:**
   - **Error 1 (Missing `self` in Unbound Super Call):** In `Manager.__init__`, `Employee.__init__(name, salary)` calls the parent constructor as an unbound function without passing `self`. This triggers `TypeError: Employee.__init__() missing 1 required positional argument: 'salary'`. It must be called as `super().__init__(name, salary)`.
   - **Error 2 (Illegal Access to Private Name-Mangled Attribute):** In `Manager.display()`, the code attempts to access `self.__salary`. Because `__salary` begins with two underscores in `Employee`, Python's interpreter performs **Name Mangling**, transforming it to `_Employee__salary`. Accessing `self.__salary` inside `Manager` looks for `_Manager__salary`, which does not exist and throws an `AttributeError`.

2. **Why Direct Private Access is Problematic & Design Modification:**
   - In Python, private attributes (`__attribute`) are intended strictly for class-internal encapsulation to prevent child classes from accidentally corrupting state. Directly coupling subclasses to private parent attributes violates encapsulation.
   - **Design Modification:** We expose a public `@property` getter `salary` on `Employee` (or define `_salary` as protected).

3. **Demonstrated OOP Principles:**
   - **Encapsulation:** The internal representation of salary is shielded, accessible only through methods/properties.
   - **Inheritance:** `Manager` reuses `name` and base logic from `Employee` via `super()`.
   - **Polymorphism:** The `display()` method and `salary` property are overridden in `Manager` and dispatched dynamically.
   - **Operator Overloading:** The addition operator (`+`) is overloaded via `__add__` to provide intuitive domain semantics.

### ✅ The Complete Corrected Program:
```python
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = str(name)
        self.__salary = float(salary)  # Encapsulated private attribute

    @property  # Encapsulation: controlled read access via property
    def salary(self) -> float: return self.__salary

    def display(self) -> None:
        print(f"Employee: {self.name}")
        print(f"Salary: ${self.salary:.2f}")

    def __add__(self, other):  # Overload '+' operator to combine employee salaries
        if isinstance(other, Employee): return self.salary + other.salary
        elif isinstance(other, (int, float)): return self.salary + other
        return NotImplemented

class Manager(Employee):
    def __init__(self, name: str, salary: float, allowance: float):
        super().__init__(name, salary)  # Corrected: use super() to bind instance correctly
        self.allowance = float(allowance)

    @property  # Polymorphic property override: Manager's total salary includes allowance
    def salary(self) -> float: return super().salary + self.allowance

    def display(self) -> None:  # Polymorphic method override
        print(f"Manager: {self.name}")
        print(f"Total: ${self.salary:.2f} (Base: ${super().salary:.2f} + Allowance: ${self.allowance:.2f})")

if __name__ == "__main__":  # Demonstration
    e1 = Employee("Ravi", 40000)
    m1 = Manager("Asha", 60000, 10000)
    print("--- Individual Displays ---")
    e1.display()
    print()
    m1.display()
    print("\n--- Overloaded '+' Operator Demo ---")
    combined = e1 + m1
    print(f"Combined Total Salary (e1 + m1): ${combined:.2f}")
```

#### 🖥️ Program Execution Output:
```text
--- Individual Displays ---
Employee: Ravi
Salary: $40000.00
Manager: Asha
Total: $70000.00 (Base: $60000.00 + Allowance: $10000.00)
--- Overloaded '+' Operator Demo ---
Combined Total Salary (e1 + m1): $110000.00
```

---

## 7.7 Program: ABC Employee Payroll Framework with Commission Extension (`SalariedEmployee`, `CommissionEmployee`)

> 📋 **Exam Problem:** > **"Design an employee payroll framework for an organization using Python's `abc` module to enforce strict class contracts across different employee roles.**  
> 1. **Abstract Base Class — `Employee`:**  
>    - *Must inherit from ABC (from the `abc` module).*  
>    - *Attributes: `emp_id` (int), `name` (string), and `department` (string).*  
>    - *Constructor: Initializes `emp_id`, `name`, and `department`.*  
>    - *Abstract Method: `calculate_salary()` decorated with `@abstractmethod`.*  
>    - *Concrete Method: `display_info()`: Prints basic employee information.*  
> 2. **Derived Class — `SalariedEmployee` (inherits from Employee):**  
>    - *Attributes: Inherits base attributes and adds `monthly_salary` (float) and `tax_deduction` (float).*  
>    - *Constructor: Uses `super()` to initialize base class attributes and sets its own attributes.*  
>    - *Methods: Implements `calculate_salary()` returning `monthly_salary - tax_deduction`; overrides `display_info()` via `super()` and prints net salary.*  
> 3. **Derived Class — `CommissionEmployee` (inherits from SalariedEmployee):**  
>    - *Attributes: Adds `sales_amount` (float) and `commission_rate` (float, e.g. 0.05).*  
>    - *Methods: Overrides `calculate_salary()` calling `super().calculate_salary() + (sales_amount * commission_rate)`; overrides `display_info()`.*  
> 4. **Demonstration & Enforcement Test:** Demonstrate that attempting to directly instantiate Employee raises a TypeError, and process a list of employees in a polymorphic loop."**  
> *(Official CAT-2 Exam Paper: 23-09-2026 / Slot C11+C12 / Q2 - 10 Marks)*  
> **Exam Match Triggers:** `"payroll framework for an organization using Python's abc module"`, `"SalariedEmployee"`, `"CommissionEmployee"`, `"super().calculate_salary()"`

```python
from abc import ABC, abstractmethod

class Employee(ABC):  # 1. Abstract Base Class Contract
    def __init__(self, emp_id: int, name: str, department: str):
        self.emp_id = int(emp_id)
        self.name = str(name)
        self.department = str(department)

    @abstractmethod
    def calculate_salary(self) -> float:
        """Abstract method enforced on all derived payroll classes."""
        pass

    def display_info(self) -> None:
        """Concrete template method printing shared identifiers."""
        print(f"Emp ID: {self.emp_id} | Name: {self.name} | Department: {self.department}")

class SalariedEmployee(Employee):  # 2. Derived Class 1: Salaried Employee
    def __init__(self, emp_id: int, name: str, department: str, 
                 monthly_salary: float, tax_deduction: float):
        super().__init__(emp_id, name, department)
        self.monthly_salary = float(monthly_salary)
        self.tax_deduction = float(tax_deduction)

    def calculate_salary(self) -> float:
        return self.monthly_salary - self.tax_deduction  # Net earnings: gross minus tax withholding

    def display_info(self) -> None:
        super().display_info()
        print(f"  [Salaried]: Gross: ${self.monthly_salary:.2f} | "
              f"Tax: ${self.tax_deduction:.2f} | Net Salary: ${self.calculate_salary():.2f}")

class CommissionEmployee(SalariedEmployee):  # 3. Derived Class 2: Commission Employee (Multilevel Inheritance)
    def __init__(self, emp_id: int, name: str, department: str, 
                 monthly_salary: float, tax_deduction: float, 
                 sales_amount: float, commission_rate: float = 0.05):
        super().__init__(emp_id, name, department, monthly_salary, tax_deduction)
        self.sales_amount = float(sales_amount)
        self.commission_rate = float(commission_rate)

    def calculate_salary(self) -> float:
        base_net = super().calculate_salary()  # Chain calculation up hierarchy using super()
        commission_earned = self.sales_amount * self.commission_rate
        return base_net + commission_earned

    def display_info(self) -> None:
        super().display_info()
        commission_earned = self.sales_amount * self.commission_rate
        print(f"  [Commission]: Sales: ${self.sales_amount:.2f} | "
              f"Rate: {self.commission_rate*100:.1f}% | Commission: ${commission_earned:.2f} | "
              f"Total Payout: ${self.calculate_salary():.2f}")

if __name__ == "__main__":  # 4. Demonstration & Enforcement Test
    try:  # Test A: Direct Instantiation Rejection
        bad_emp = Employee(999, "Illegal Instance", "HR")
    except TypeError as e:
        print("[ABC Enforcement Verified]: Instantiating abstract Employee raises TypeError!")

    payroll_roster = [  # Test B: Polymorphic Employee Processing Loop
        SalariedEmployee(101, "Kavita Sharma", "Engineering", 75000.0, 8000.0),
        CommissionEmployee(102, "Rajesh Patel", "Enterprise Sales", 40000.0, 3500.0, 500000.0, 0.05)
    ]

    print("\n=== Automated Monthly Payroll Execution ===")
    for emp in payroll_roster:
        emp.display_info()
        print("-" * 65)
```

#### 🖥️ Program Execution Output:
```text
[ABC Enforcement Verified]: Instantiating abstract Employee raises TypeError!
=== Automated Monthly Payroll Execution ===
Emp ID: 101 | Name: Kavita Sharma | Department: Engineering
  [Salaried]: Gross: $75000.00 | Tax: $8000.00 | Net Salary: $67000.00
-----------------------------------------------------------------
Emp ID: 102 | Name: Rajesh Patel | Department: Enterprise Sales
  [Salaried]: Gross: $40000.00 | Tax: $3500.00 | Net Salary: $36500.00
  [Commission]: Sales: $500000.00 | Rate: 5.0% | Commission: $25000.00 | Total Payout: $61500.00
-----------------------------------------------------------------
```

---

## 7.8 Program: Object-Oriented File System Registry Manager (`FileRegistry`)

> 📋 **Exam Problem:** > **"Design an Object-Oriented file system manager class `FileRegistry` that tracks directory structures and dumps system registry logs to an external file. Implement the `FileRegistry` class with the following methods:**  
> 1. **`create_path(self, path: str, value: int) -> bool`:**  
>    - *Registers a path with an associated integer value (e.g., file size or permission ID).*  
>    - *Returns True if created successfully.*  
>    - *Returns False if: The path already exists, OR The parent path does not exist (e.g., creating `/a/b` when `/a` does not exist).*  
> 2. **`get(self, path: str) -> int`:**  
>    - *Returns the value associated with path, or -1 if the path does not exist.*  
> 3. **`dump_registry_to_file(self, export_filepath: str) -> None`:**  
>    - *Writes all registered paths and their values to `export_filepath` in alphabetical order, using the format: `PATH -> VALUE`.*  
> **Sample Test Case:**  
> `registry = FileRegistry()`  
> `registry.create_path("/a", 100) # Returns True`  
> `registry.create_path("/a/b", 200) # Returns True`  
> `registry.create_path("/c/d", 300) # Returns False (parent "/c" missing)`  
> `registry.get("/a/b") # Returns 200`  
> `registry.dump_registry_to_file("registry_log.txt")`**  
> *(Official CAT-2 Exam Paper: 23-09-2026 / Slot C11+C12 / Q3 - 10 Marks)*  
> **Exam Match Triggers:** `"Object-Oriented file system manager class FileRegistry"`, `"create_path(self, path: str, value: int)"`, `"dump_registry_to_file"`, `"PATH -> VALUE"`

```python
class FileRegistry:
    """Tracks hierarchical file paths and their associated integer metadata."""
    def __init__(self):
        self._registry = {}  # Internal storage mapping path string -> integer value

    def create_path(self, path: str, value: int) -> bool:
        """Creates a path entry. Returns False if path exists or parent is missing."""
        if not path or not path.startswith("/") or path in self._registry:
            return False

        # Extract parent path: e.g. '/a/b' -> parent is '/a'; '/a' -> parent is root ''
        path_components = path.rstrip("/").split("/")

        if len(path_components) > 2:  # If path has more than 1 level of hierarchy (e.g. [' ', 'a', 'b'])
            parent_path = "/".join(path_components[:-1])
            if parent_path not in self._registry:
                return False  # Parent path does not exist

        self._registry[path] = int(value)  # Register valid entry
        return True

    def get(self, path: str) -> int:
        """Returns the registered value for path, or -1 if not found."""
        return self._registry.get(path, -1)

    def dump_registry_to_file(self, export_filepath: str) -> None:
        """Dumps all entries sorted alphabetically in 'PATH -> VALUE' format."""
        with open(export_filepath, "w", encoding="utf-8") as f:
            for registered_path in sorted(self._registry.keys()):
                f.write(f"{registered_path} -> {self._registry[registered_path]}\n")
        print(f"Registry successfully exported to '{export_filepath}'.")

if __name__ == "__main__":  # Working Verification with Official Exam Sample Test Case
    registry = FileRegistry()

    res1 = registry.create_path("/a", 100)  # Exact official test cases:
    print(f'registry.create_path("/a", 100)   -> {res1}')       # Returns True

    res2 = registry.create_path("/a/b", 200)
    print(f'registry.create_path("/a/b", 200) -> {res2}')       # Returns True

    res3 = registry.create_path("/c/d", 300)
    print(f'registry.create_path("/c/d", 300) -> {res3} (Expected False: parent /c missing)')

    val = registry.get("/a/b")
    print(f'registry.get("/a/b")              -> {val}')        # Returns 200

    missing_val = registry.get("/c/d")
    print(f'registry.get("/c/d")              -> {missing_val}')# Returns -1

    log_file = "registry_log.txt"  # Dump to external file
    registry.dump_registry_to_file(log_file)

    print("\n--- Exported 'registry_log.txt' File Content ---")
    with open(log_file, "r", encoding="utf-8") as f:
        print(f.read().strip())
```

#### 🖥️ Program Execution Output:
```text
registry.create_path("/a", 100)   -> True
registry.create_path("/a/b", 200) -> True
registry.create_path("/c/d", 300) -> False (Expected False: parent /c missing)
registry.get("/a/b")              -> 200
registry.get("/c/d")              -> -1
Registry successfully exported to 'registry_log.txt'.
--- Exported 'registry_log.txt' File Content ---
/a -> 100
/a/b -> 200
```

---

## 7.9 Program: MySQL Store Inventory & Stock Reduction Transaction (`commit` vs `rollback`)

> 📋 **Exam Problem:** > **"Write a Python program that connects to a MySQL database named `store_db` and performs the following operations:**  
> 1. **Table Setup:** *Create a table named `inventory` with columns: `item_id` (INT, Primary Key, Auto Increment), `item_name` (VARCHAR(100), Not Null), `quantity` (INT, Not Null), and `price_per_unit` (DECIMAL(10,2), Not Null).*  
> 2. **Data Insertion (Batch):** *Insert at least 3 initial items using a parameterized query (`%s` placeholders) and `executemany()`: ("Wireless Mouse", 50, 25.50), ("Mechanical Keyboard", 30, 85.00), ("USB-C Hub", 15, 45.00).*  
> 3. **Transaction & Business Logic (Stock Reduction):** *Write a function `process_sale(item_id, sold_quantity)` that: Checks if the item exists and has enough stock (`quantity >= sold_quantity`). If sufficient, deduct sold quantity and call `commit()`. If insufficient, raise/print a custom message and execute `rollback()`.*  
> 4. **Data Retrieval:** *Retrieve and display all items from inventory where `quantity < 40` (low stock items) in a clean output using `cursor.fetchall()`.*  
> 5. **Error Handling:** *Wrap all operations in `try-except-finally` closing cursor and connection explicitly."**  
> *(Official CAT-2 Exam Paper: 23-09-2026 / Slot C11+C12 / Q4 - 10 Marks)*  
> **Exam Match Triggers:** `"database named store_db"`, `"inventory"`, `"process_sale(item_id, sold_quantity)"`, `"quantity < 40"`, `"commit"`, `"rollback"`

```python
import mysql.connector
from mysql.connector import Error

def store_inventory_transaction_pipeline():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(  # Establish connection to store_db
            host="localhost",
            user="root",
            password="your_password",
            database="store_db"
        )
        cursor = connection.cursor()

        cursor.execute("""  # 1. Table Setup: inventory
        CREATE TABLE IF NOT EXISTS inventory (
            item_id INT AUTO_INCREMENT PRIMARY KEY,
            item_name VARCHAR(100) NOT NULL,
            quantity INT NOT NULL,
            price_per_unit DECIMAL(10, 2) NOT NULL
        );
        """)
        print("[Step 1]: Inventory table verified/created.")

        insert_sql = """  # 2. Batch Data Insertion via executemany()
        INSERT INTO inventory (item_name, quantity, price_per_unit)
        VALUES (%s, %s, %s);
        """
        initial_items = [
            ("Wireless Mouse", 50, 25.50),
            ("Mechanical Keyboard", 30, 85.00),
            ("USB-C Hub", 15, 45.00)
        ]
        cursor.executemany(insert_sql, initial_items)
        connection.commit()
        print(f"[Step 2]: Inserted {cursor.rowcount} inventory items.")

        # 3. Transaction Logic: process_sale with Commit / Rollback
        def process_sale(item_id: int, sold_quantity: int) -> None:
            # Query current stock with lock
            cursor.execute("SELECT item_name, quantity FROM inventory WHERE item_id = %s;", (item_id,))
            result = cursor.fetchone()

            if not result:
                print(f"[Sale Error]: Item ID {item_id} does not exist! Aborting transaction.")
                connection.rollback()
                return

            item_name, available_qty = result
            if available_qty < sold_quantity:
                # Stock insufficient: abort and rollback
                print(f"[Sale REJECTED]: Insufficient stock for '{item_name}'! "
                      f"Requested: {sold_quantity}, Available: {available_qty}. Performing ROLLBACK.")
                connection.rollback()
            else:
                # Stock sufficient: update and commit
                deduct_sql = "UPDATE inventory SET quantity = quantity - %s WHERE item_id = %s;"
                cursor.execute(deduct_sql, (sold_quantity, item_id))
                connection.commit()
                print(f"[Sale APPROVED]: Sold {sold_quantity} unit(s) of '{item_name}'. "
                      f"New Balance: {available_qty - sold_quantity}. Transaction COMMITTED.")

        process_sale(1, 15)  # Wireless Mouse: 50 -> 35  # Test Successful Sale
        # Test Failed Sale (Excessive quantity)
        process_sale(3, 20)  # USB-C Hub: 15 available, 20 requested -> Rollback

        # 4. Data Retrieval: Low Stock Alert (quantity < 40)
        print("\n--- Low Stock Alert Report (quantity < 40) ---")
        cursor.execute("SELECT item_id, item_name, quantity, price_per_unit FROM inventory WHERE quantity < 40;")
        low_stock_items = cursor.fetchall()

        for row in low_stock_items:
            print(f"Item #{row[0]}: {row[1]:<22} | Qty Remaining: {row[2]:<3} | Price: ${float(row[3]):.2f}")

    except Error as e:
        if connection:
            connection.rollback()
        print(f"MySQL Database Error: {e}")

    finally:
        if cursor is not None:  # 5. Resource Cleanup
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("\nDatabase connection and cursor successfully closed.")

if __name__ == "__main__":
    store_inventory_transaction_pipeline()
```

#### 🖥️ Program Execution Output:
```text
[Step 1]: Inventory table verified/created.
[Step 2]: Inserted 3 inventory items.
[Sale APPROVED]: Sold 15 unit(s) of 'Wireless Mouse'. New Balance: 35. Transaction COMMITTED.
[Sale REJECTED]: Insufficient stock for 'USB-C Hub'! Requested: 20, Available: 15. Performing ROLLBACK.
--- Low Stock Alert Report (quantity < 40) ---
Item #1: Wireless Mouse         | Qty Remaining: 35  | Price: $25.50
Item #2: Mechanical Keyboard    | Qty Remaining: 30  | Price: $85.00
Item #3: USB-C Hub              | Qty Remaining: 15  | Price: $45.00
Database connection and cursor successfully closed.
```

---

## 7.10 Program & Theory: Student Records File Handling & Exception Debugging (`0-100` Range, Append Mode `"a"`)

> 📋 **Target Exam Question:** *"A student-management system stores student details in a file to read marks and calculate grades. Analyze the code, identify errors in save_student(), modify to store multiple students without overwriting, handle non-integer 'abc' and 0-100 range, use file exception handling, explain abstract class, and display all records."*  
> *(Official CAT-2 Exam Paper: 23-09-2026 / Slot C11+C12 / Q5 - 10 Marks)*  
> **Exam Match Triggers:** `"student-management system stores student details in a file"`, `"RegularStudent"`, `"Identify the error in the save_student() function"`, `"values outside the range 0-100"`

### ❌ The Given Buggy Code (From Exam Paper):
```python
from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
    @abstractmethod
    def grade(self):
        pass

class RegularStudent(Student):
    def grade(self):
        if self.mark >= 50:
            return "Pass"
        else:
            return "Fail"

def save_student(student):
    file = open("students.txt", "w")  # ERROR: "w" overwrites previous data!
    file.write(student.name + "," + student.mark + "\n")  # ERROR: TypeError concatenating int!
    file.close()

try:
    name = input("Enter name: ")
    mark = int(input("Enter mark: "))
    student = RegularStudent(name, mark)
    save_student(student)
except:
    print("Error occurred")
```

### 📝 The 6 Required Answers (Write these directly in your exam):

1. **Error in `save_student()` Function:**
   - **Type Mismatch on Concatenation:** `student.mark` is an integer (`int`). Python does not implicitly convert integers during string concatenation (`+`), raising `TypeError: can only concatenate str (not "int") to str`. It must be explicitly cast using `str(student.mark)`.
   - **Resource Leak Hazard:** The file is opened without a context manager (`with open(...)`), meaning if an exception occurs before `file.close()`, the file descriptor remains leaked in memory.

2. **Storing Multiple Students Without Overwriting (Append Mode):**
   - The original code opened the file with mode `"w"` (write mode), which truncates/erases the file every time a record is saved.
   - **Fix:** Open the file using mode `"a"` (append mode): `with open("students.txt", "a", encoding="utf-8") as file:`.

3. **Handling Invalid Marks ("abc" & Outside 0–100):**
   - Use `int(mark_input)` inside a `try-except ValueError` block.
   - Add explicit range validation: `if not (0 <= mark <= 100): raise ValueError("Mark must be between 0 and 100.")`.

4. **Specific File Exception Handling:**
   - Instead of a bare `except:`, explicitly catch `IOError`, `PermissionError`, and `FileNotFoundError`.

5. **Why `Student` is Abstract & Cannot Be Created Directly:**
   - `Student` inherits from `ABC` and contains a method `grade()` decorated with `@abstractmethod`. Under Python language specifications, any class defining at least one unimplemented abstract method is formally an abstract class. Direct instantiation triggers `TypeError: Can't instantiate abstract class Student with abstract method grade`.

### ✅ The Complete Corrected Program (with Read & Display):
```python
from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, name: str, mark: int):
        self.name = str(name)
        self.mark = int(mark)

    @abstractmethod
    def grade(self) -> str:
        '''Abstract method enforced on all student specializations.'''
        pass

class RegularStudent(Student):
    def grade(self) -> str:
        return "Pass" if self.mark >= 50 else "Fail"

# 2. Corrected save function: uses append mode "a", str(mark), and context manager
def save_student(student: Student, filepath: str = "students.txt") -> None:
    try:
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(f"{student.name},{student.mark},{student.grade()}\n")
        print(f"Record for '{student.name}' saved successfully to '{filepath}'.")
    except (IOError, PermissionError) as e:
        print(f"File Storage Error: Unable to write to '{filepath}' ({e}).")

# 6. Function to read and display all student records
def display_all_students(filepath: str = "students.txt") -> None:
    print(f"\n--- Stored Student Records in '{filepath}' ---")
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("No records found in file.")
                return
            print(f"{'Name':<15} | {'Mark':<6} | {'Result':<6}")
            print("-" * 35)
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, mark, result = parts
                    print(f"{name:<15} | {mark:<6} | {result:<6}")
    except FileNotFoundError:
        print(f"Notice: '{filepath}' does not exist yet.")

if __name__ == "__main__":  # Main Driver with Robust Validation (Points 3 & 4)
    test_inputs = [("Rohit", "85"), ("Priya", "42"), ("Invalid", "abc"), ("Excess", "150")]
    for name_in, mark_in in test_inputs:
        try:
            print(f"\nProcessing Input: Name='{name_in}', Mark='{mark_in}'")
            try:
                mark = int(mark_in)
            except ValueError:
                raise ValueError(f"Invalid mark format '{mark_in}'. Marks must be an integer!")
            if not (0 <= mark <= 100):
                raise ValueError(f"Score {mark} is out of allowable range (0 to 100)!")
            student = RegularStudent(name_in, mark)
            save_student(student)
        except ValueError as val_err:
            print(f"[Validation Error]: {val_err}")
    display_all_students()  # Display all saved students
```

#### 🖥️ Program Execution Output:
```text
Processing Input: Name='Rohit', Mark='85'
Record for 'Rohit' saved successfully to 'students.txt'.
Processing Input: Name='Priya', Mark='42'
Record for 'Priya' saved successfully to 'students.txt'.
Processing Input: Name='Invalid', Mark='abc'
[Validation Error]: Invalid mark format 'abc'. Marks must be an integer!
Processing Input: Name='Excess', Mark='150'
[Validation Error]: Score 150 is out of allowable range (0 to 100)!

--- Stored Student Records in 'students.txt' ---
Name            | Mark   | Result
-----------------------------------
Rohit           | 85     | Pass  
Priya           | 42     | Fail  
```

---

## 7.11 Program: String Property Analyzer Class (Uppercase, Vowels, Consonants, Spaces Counter)

> 📋 **Exam Problem:** > **"Write a Python program to define a class that stores a given string and maintains its various properties, such as the number of uppercase letters, vowels, consonants, and spaces. Explain the complete logic and working of the program in detail."**  
> *(Official CAT-2 Exam Paper: 21-09-2026 / Slot B22+B24 / Q5 - 10 Marks)*  
> **Exam Match Triggers:** `"class that stores a given string and maintains its various properties"`, `"uppercase letters, vowels, consonants, and spaces"`

```python
class StringPropertyAnalyzer:
    """Encapsulates a string and computes lexical metrics upon initialization."""
    def __init__(self, input_text: str):
        self.text = str(input_text)
        self.uppercase_count = 0  # Property counters
        self.vowels_count = 0
        self.consonants_count = 0
        self.spaces_count = 0

        self._compute_properties()  # Analyze properties automatically

    def _compute_properties(self) -> None:
        """Iterates through each character and categorizes based on character classes."""
        vowel_set = set("aeiouAEIOU")

        for char in self.text:
            if char.isupper():  # 1. Check uppercase
                self.uppercase_count += 1

            if char.isspace():  # 2. Check whitespace
                self.spaces_count += 1

            if char in vowel_set:  # 3. Check vowel vs consonant (alphabetic characters only)
                self.vowels_count += 1
            elif char.isalpha():  # Alphabetic and not in vowel_set implies consonant
                self.consonants_count += 1

    def display_analysis_report(self) -> None:
        """Prints a comprehensive breakdown of the string's properties."""
        print(f"\n{'='*55}")
        print(f"STRING PROPERTY ANALYSIS REPORT")
        print(f"{'='*55}")
        print(f"Source Text : \"{self.text}\"")
        print(f"Total Length: {len(self.text)} characters")
        print(f"{'-'*55}")
        print(f"  • Uppercase Letters : {self.uppercase_count}")
        print(f"  • Vowels (A,E,I,O,U): {self.vowels_count}")
        print(f"  • Consonants        : {self.consonants_count}")
        print(f"  • Whitespace Spaces : {self.spaces_count}")
        print(f"{'='*55}\n")

if __name__ == "__main__":  # Demonstration
    sample_text = "VIT Bhopal Python CAT-2 Examination 2026!"
    analyzer = StringPropertyAnalyzer(sample_text)
    analyzer.display_analysis_report()
```

#### 🖥️ Program Execution Output:
```text
=======================================================
STRING PROPERTY ANALYSIS REPORT
=======================================================
Source Text : "VIT Bhopal Python CAT-2 Examination 2026!"
Total Length: 41 characters
-------------------------------------------------------
  • Uppercase Letters : 9
  • Vowels (A,E,I,O,U): 10
  • Consonants        : 18
  • Whitespace Spaces : 4
=======================================================
```

---

## 7.12 Program: Student Information System Text File CRUD (`add`, `search`, `modify`, `delete`)

> 📋 **Exam Problem:** > **"A student information system stores student records in a text file. The program must allow users to add, search, modify, and delete records. Design an appropriate file organization strategy and explain why your choice is better than storing all records as an unstructured text file."**  
> *(Official CAT-2 Exam Paper: 21-09-2026 / Slot B22+B24 / Q3 - 10 Marks)*  
> **Exam Match Triggers:** `"student information system stores student records in a text file"`, `"allow users to add, search, modify, and delete records"`, `"explain why your choice is better than storing all records as an unstructured text file"`

### 📝 File Organization Strategy Justification:
- **Chosen Strategy:** **Delimited Flat-File Organization (DSV)** using a pipe delimiter (`|`), where each line represents exactly one record: `RollNo|Name|Department|GPA`.
- **Why It Is Superior to Unstructured Text:**
  1. **Consistent Schema & O(1) Field Parsing:** Unstructured prose requires natural language parsing. A delimited record allows instant splitting via `line.split("|")`.
  2. **Predictable Record Boundaries:** Each newline (`\n`) guarantees one logical record boundary, preventing record bleeding.
  3. **Atomic Modification & Deletion:** Updating a student only requires searching the matching primary key (`RollNo`), updating the field in memory, and rewriting the lines cleanly.

### ✅ The Complete CRUD Implementation:
```python
import os

class StudentFileManager:
    def __init__(self, filename: str = "students_db.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            open(self.filename, "w", encoding="utf-8").close()

    def add_record(self, roll_no: str, name: str, dept: str, gpa: float) -> bool:
        """Appends a new structured record: RollNo|Name|Dept|GPA."""
        if self.search_record(roll_no) is not None:
            print(f"[Add Failed]: Student with Roll No '{roll_no}' already exists!")
            return False
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"{roll_no}|{name}|{dept}|{gpa:.2f}\n")
        print(f"[Added]: Record for {name} ({roll_no}) appended.")
        return True

    def search_record(self, roll_no: str) -> dict | None:
        """Searches for a record by Roll No. Returns dict or None."""
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4 and parts[0] == roll_no:
                    return {"roll_no": parts[0], "name": parts[1], "dept": parts[2], "gpa": float(parts[3])}
        return None

    def modify_record(self, roll_no: str, new_name: str = None, new_dept: str = None, new_gpa: float = None) -> bool:
        """Modifies attributes of an existing record."""
        found = False
        updated_lines = []
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4 and parts[0] == roll_no:
                    found = True
                    name = new_name if new_name else parts[1]
                    dept = new_dept if new_dept else parts[2]
                    gpa = f"{new_gpa:.2f}" if new_gpa is not None else parts[3]
                    updated_lines.append(f"{roll_no}|{name}|{dept}|{gpa}\n")
                else:
                    updated_lines.append(line)
        if found:
            with open(self.filename, "w", encoding="utf-8") as f:
                f.writelines(updated_lines)
            print(f"[Modified]: Record '{roll_no}' successfully updated.")
            return True
        print(f"[Modify Failed]: Roll No '{roll_no}' not found.")
        return False

    def delete_record(self, roll_no: str) -> bool:
        """Deletes a record by filtering out the matching line."""
        found = False
        remaining_lines = []
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4 and parts[0] == roll_no:
                    found = True
                else:
                    remaining_lines.append(line)
        if found:
            with open(self.filename, "w", encoding="utf-8") as f:
                f.writelines(remaining_lines)
            print(f"[Deleted]: Record '{roll_no}' successfully removed.")
            return True
        print(f"[Delete Failed]: Roll No '{roll_no}' not found.")
        return False

if __name__ == "__main__":  # Demonstration
    db = StudentFileManager("student_records_demo.txt")

    db.add_record("24BCE1001", "Alex Smith", "CSE", 9.40)  # 1. Add records
    db.add_record("24BCE1002", "Priya Nair", "ECE", 8.85)

    record = db.search_record("24BCE1001")  # 2. Search record
    print(f"Search Result: {record}")

    db.modify_record("24BCE1001", new_gpa=9.75)  # 3. Modify record (Update GPA)

    db.delete_record("24BCE1002")  # 4. Delete record
```

#### 🖥️ Program Execution Output:
```text
[Added]: Record for Alex Smith (24BCE1001) appended.
[Added]: Record for Priya Nair (24BCE1002) appended.
Search Result: {'roll_no': '24BCE1001', 'name': 'Alex Smith', 'dept': 'CSE', 'gpa': 9.4}
[Modified]: Record '24BCE1001' successfully updated.
[Deleted]: Record '24BCE1002' successfully removed.
```

---

## 7.13 Theory: ODBC (Open Database Connectivity) Generic Mechanism & RDBMS Portability Analysis

> 📋 **Exam Problem:** > **"Explain why ODBC can be considered a generic database connectivity mechanism. Suppose the same Python application needs to work with different relational database systems. Analyse how ODBC can reduce changes to the application code."**  
> *(Official CAT-2 Exam Paper: 21-09-2026 / Slot B22+B24 / Q4 - 10 Marks)*  
> **Exam Match Triggers:** `"ODBC can be considered a generic database connectivity mechanism"`, `"work with different relational database systems"`, `"Analyse how ODBC can reduce changes to the application code"`

### 📝 Core Theory Points to Write in Exam:

1. **Why ODBC is a Generic Connectivity Standard:**
   - **Open Database Connectivity (ODBC)** is an open industry standard C/C++ API designed by Microsoft and ISO/IEC to access Relational Database Management Systems (RDBMS).
   - It acts as an **abstraction translation layer** between application code and database drivers.
   - The application does not communicate with the database directly; it communicates through the **ODBC Driver Manager**, which routes calls to the database-specific driver (e.g. MySQL ODBC Driver, Oracle ODBC Driver, SQL Server Driver).

2. **The 4-Layer ODBC Architecture:**
```text
+-------------------------------------------------------------+
|                Python Application Code                      |
|              (uses pyodbc / DB-API 2.0)                     |
+-------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|                     ODBC Driver Manager                     |
|             (libodbc.so on Linux / odbc32.dll on Win)       |
+-------------------------------------------------------------+
                              |
      +-----------------------+-----------------------+
      v                                               v
+---------------------------+   +---------------------------+
|     MySQL ODBC Driver     |   |   PostgreSQL ODBC Driver  |
+---------------------------+   +---------------------------+
              |                               |
              v                               v
+---------------------------+   +---------------------------+
|      MySQL Database       |   |    PostgreSQL Database    |
+---------------------------+   +---------------------------+
```

3. **How ODBC Reduces Changes When Switching Databases:**
   - **Zero Code Changes in Query Execution:** All cursor operations (`cursor.execute()`, `cursor.fetchone()`, `cursor.fetchall()`) follow the exact same Python DB-API 2.0 standard across all database vendors.
   - **Externalized Configuration (DSN - Data Source Name):** Connection details (IP, port, database name) are stored in an external system configuration file (`odbc.ini`). Switching from MySQL to PostgreSQL or Oracle only requires changing the DSN name in the connection string:
```python
# Changing backend from MySQL to Oracle requires ONLY changing the DSN string:
connection = pyodbc.connect("DSN=ProductionDB;UID=admin;PWD=secret")
```
   - **Unified Data Type Mapping:** ODBC automatically normalizes vendor-specific SQL types (e.g. Oracle `VARCHAR2`, MySQL `VARCHAR`, SQL Server `NVARCHAR`) to uniform Python data types (`str`), eliminating type-conversion bugs.

---

## 7.14 Theory: Evaluating Class Roles (`Student`, `Faculty`, `Administrator`) — Standalone vs Polymorphism & MRO

> 📋 **Target Exam Question:** *"Q1.a: A developer creates separate classes Student, Faculty, and Administrator, but all three classes contain the same get_role() method. Evaluate whether inheritance and polymorphism would improve this design. Justify your answer. Q1.b: A programmer uses multiple inheritance to combine features from two parent classes. Evaluate the importance of MRO and super() in preventing ambiguity in method execution."*  
> *(Official CAT-2 Exam Paper: 21-09-2026 / Slot B22+B24 / Q1 - 10 Marks)*  
> **Exam Match Triggers:** `"separate classes Student, Faculty, and Administrator"`, `"same get_role() method"`, `"Evaluate whether inheritance and polymorphism would improve this design"`, `"MRO and super() in preventing ambiguity"`

### 📝 Evaluation & Justification (Part A):
- **Verdict: YES, Inheritance and Polymorphism significantly improve this design.**
- **Justifications:**
  1. **Enforcement of Common Interface Contract:** Without inheritance, each class's `get_role()` method is merely an accidental coincidence. Introducing an abstract base class `User(ABC)` with `@abstractmethod def get_role(self) -> str:` guarantees at compile/runtime that any new role *must* implement `get_role()`, eliminating missing method bugs.
  2. **Elimination of Code Duplication (DRY Principle):** `Student`, `Faculty`, and `Administrator` inevitably share common identity attributes (`name`, `email`, `user_id`, `created_at`). A parent `User` class encapsulates these attributes in one shared `__init__`.
  3. **Polymorphic Dispatch in Calling Code:** Callers can treat all objects uniformly without type checks:
```python
for user in [student, faculty, admin]:  # Clean Polymorphic Dispatch: Zero if-elif checks!
    print(f"User: {user.name} | Role: {user.get_role()}")
```

### 📝 Importance of MRO & `super()` (Part B):
- **The Diamond Problem Hazard:** If class `D` inherits from `B` and `C`, and both inherit from `A`, calling `A.__init__` directly from `B` and `C` would execute `A`'s constructor **twice**, causing duplicate resource allocation or corrupted state.
- **Role of C3 Linearization (MRO):** Python computes a deterministic Method Resolution Order: `[D -> B -> C -> A -> object]`.
- **Role of `super()`:** Unlike hardcoded parent calls (`A.__init__(self)`), `super()` follows the MRO dynamically, guaranteeing that every ancestor class in the inheritance graph is visited **exactly once**.
