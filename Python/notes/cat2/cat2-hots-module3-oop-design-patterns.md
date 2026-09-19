# ⚡ CAT-2 HOTS Master Crib — Module 3: Advanced OOP, Operator Overloading & Persistence
**Course**: CSE3011 — Python Programming  
**Coverage**: Object-Oriented Design, Operator Overloading & Object Persistence | **Exam Mode**: Open Book / Notes Allowed  
**Target Score**: 45+ / 50 (S-Grade Boundary)

---

## 🧱 TIER 0: The "Explain Like I'm 5" Bedrock Basics
*(Read this first if OOP concepts or design patterns feel abstract)*

### 1. Visualizing Class Inheritance & Polymorphism
* An **Abstract Base Class (ABC)** is a strict contract: It says *"Any child class MUST implement `withdraw()` and `deposit()`, or Python will refuse to create it!"*
* Both `SavingsAccount` and `CurrentAccount` inherit common properties from `BankAccount`, but have different fee/interest behaviors.

```mermaid
graph TD
    subgraph OOP_Hierarchy ["BankAccount Polymorphism Hierarchy"]
    ABC["<< Abstract >> BankAccount<br>(Defines: deposit, withdraw, get_balance)"]
    ABC --> SA["SavingsAccount<br>(Adds: interest_rate, min_balance)"]
    ABC --> CA["CurrentAccount<br>(Adds: overdraft_limit)"]
    end
```

---

### 2. The Diamond Problem & Method Resolution Order (MRO)
* In multiple inheritance, if class `D` inherits from both `B` and `C`, and both inherit from `A`: which `speak()` method runs?
* Python uses the **C3 Linearization algorithm** to produce a deterministic search list (`D.__mro__`):
  $$\text{MRO}(D) = [D \to B \to C \to A \to \text{object}]$$

```mermaid
graph BT
    subgraph Diamond_Problem ["Python C3 Linearization (MRO)"]
    D["Class D (Child)"] --> B["Class B"]
    D --> C["Class C"]
    B --> A["Class A (Grandparent)"]
    C --> A
    A --> OBJ["object"]
    end
```

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If Question Mentions / Shows... | It Means This Exact Topic | Your Immediate Formula / Action |
| :--- | :--- | :--- |
| "Design an OOP system for real-world application", ABC | **Complete OOP Architecture** | Abstract base class (`ABC`), `@abstractmethod`, `super()`, encapsulation (`__private`), polymorphism. |
| "Implement operator overloading", `__add__`, `__eq__` | **Dunder / Magic Methods** | Implement `__str__`, `__repr__`, `__add__`, `__sub__`, `__eq__`, `__lt__`. Always validate operand type! |
| "Pickle vs JSON", "Object persistent storage" | **Object Serialization** | Compare JSON (Human-readable, portable, secure) vs Pickle (Python-specific, binary, security risk). |
| "Compare polymorphism vs conditional `if-elif` statements" | **Design Justification** | Polymorphism obeys Open-Closed Principle (OCP); adding new types requires zero modification of existing code. |
| Name mangling, access specification | **Encapsulation in Python** | Public: `self.name`; Protected: `self._author` (convention); Private: `self.__isbn` (`_Class__isbn`). |

---

## 🛠️ TIER 2: The Master Exam-Ready OOP Template (Copy Directly!)

This master blueprint solves **Questions 1, 3, 4, and 5 of the Open-Book Practice Exam** in one clean, unified architecture:

```python
from abc import ABC, abstractmethod
import json
import pickle

# =====================================================================
# 1. Custom Exception
# =====================================================================
class InvalidAmountError(Exception):
    """Raised when an operation is attempted with an illegal monetary value."""
    pass

# =====================================================================
# 2. Abstract Base Class (Abstraction & Polymorphism Contract)
# =====================================================================
class BankAccount(ABC):
    def __init__(self, account_number: str, holder_name: str, initial_balance: float):
        self.account_number = account_number          # Public
        self._holder_name = holder_name              # Protected (convention)
        self.__balance = float(initial_balance)       # Private (name-mangled)

    # Encapsulated Getter & Setter for Private Balance
    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive!")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive!")
        if amount > self.__balance:
            raise InvalidAmountError("Insufficient funds!")
        self.__balance -= amount

    @abstractmethod
    def calculate_interest(self) -> float:
        """Forces all subclasses to provide custom interest calculation."""
        pass

    # =================================================================
    # 3. Meaningful Operator Overloading (Magic / Dunder Methods)
    # =================================================================
    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"Account[{self.account_number}] - {self._holder_name}: ${self.__balance:.2f}"

    def __repr__(self) -> str:
        """Unambiguous developer representation."""
        return f"{self.__class__.__name__}('{self.account_number}', '{self._holder_name}', {self.__balance})"

    def __add__(self, other):
        """Allows merging two accounts or adding interest directly: acc1 + acc2."""
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
        """Allows sorting accounts by balance."""
        if isinstance(other, BankAccount):
            return self.__balance < other.__balance
        return NotImplemented

# =====================================================================
# 4. Concrete Subclasses (Inheritance & Polymorphism)
# =====================================================================
class SavingsAccount(BankAccount):
    def __init__(self, account_number: str, holder_name: str, initial_balance: float, interest_rate: float = 0.04):
        super().__init__(account_number, holder_name, initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self) -> float:
        return self.balance * self.interest_rate

class CheckingAccount(BankAccount):
    def __init__(self, account_number: str, holder_name: str, initial_balance: float, overdraft_fee: float = 25.0):
        super().__init__(account_number, holder_name, initial_balance)
        self.overdraft_fee = overdraft_fee

    def calculate_interest(self) -> float:
        return 0.0  # Checking accounts typically earn zero interest
```

---

## 🛠️ TIER 3: Object Persistence Comparison & Code

### Comparison Matrix: JSON vs Pickle
| Criterion | JSON (`import json`) | Pickle (`import pickle`) |
| :--- | :--- | :--- |
| **Data Format** | Human-readable text (UTF-8) | Python-specific binary stream |
| **Portability** | **Universal** (Language agnostic: C++, Java, JS) | Python only (version dependency) |
| **Security** | **Safe** (Cannot execute arbitrary bytecode) | **Unsafe** (Deserializing untrusted data can execute malicious shell commands via `__reduce__`) |
| **Supported Types** | Built-in primitives (dicts, lists, strings, numbers) | Arbitrary complex Python objects (classes, lambdas, functions) |
| **Recommendation** | Ideal for external storage, APIs, and interoperable configs | Ideal only for internal temporary caching in trusted environments |

### Implementation Code for Storage & Retrieval:
```python
# 1. JSON Persistence (Convert to dict -> serialize)
def save_account_json(account: BankAccount, filepath: str):
    data = {
        "account_number": account.account_number,
        "holder_name": account._holder_name,
        "balance": account.balance,
        "type": account.__class__.__name__
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# 2. Pickle Persistence (Direct object serialization)
def save_account_pickle(account: BankAccount, filepath: str):
    with open(filepath, "wb") as f:
        pickle.dump(account, f)

def load_account_pickle(filepath: str) -> BankAccount:
    with open(filepath, "rb") as f:
        return pickle.load(f)
```

---

## 📝 TIER 4: Theory Justifications (Copy into Exam Paper)

### 1. Why Polymorphism is Superior to Conditional (`if-elif`) Statements
* **Open-Closed Principle (OCP)**: With polymorphism, if we add a new account type (`FixedDepositAccount`), we write a new class without touching existing `BankAccount` code. With `if-elif` chains, every new account type requires editing every single dispatch function across the entire codebase.
* **Code Smells & Maintenance**: Nested `if-elif` chains lead to cyclomatic complexity explosion and duplicated branching logic. Polymorphism encapsulates behavior within the object itself.

### 2. Limitations of Operator Overloading
* **Readability / Principle of Least Astonishment**: Overloading operators with non-intuitive meanings (e.g. using `*` to send an email) degrades code maintainability.
* **Type Symmetry**: In `a + b`, if `a` does not know how to add `b`, Python attempts `b.__radd__(a)`. If neither handles the type, a `TypeError` must be raised cleanly by returning `NotImplemented`.

---

## 🎯 TIER 5: Assignment 3 & Lab Experiments Master Solutions (Direct Exam Copy)

### 1. Assignment 3 — Question 1: Polygons Area & Perimeter (OOP Hierarchy)
```python
import math
from abc import ABC, abstractmethod

class Polygon(ABC):
    """Abstract Base Class defining the contract for all 2D shapes."""
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

class Rectangle(Polygon):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive!")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Triangle(Polygon):
    def __init__(self, a: float, b: float, c: float):
        # Triangle inequality check
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle side lengths!")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def area(self) -> float:
        # Heron's Formula
        s = self.perimeter() / 2.0
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# Demonstration
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(f"Rectangle -> Area: {rect.area():.2f}, Perimeter: {rect.perimeter():.2f}")

    tri = Triangle(3, 4, 5)
    print(f"Triangle  -> Area: {tri.area():.2f}, Perimeter: {tri.perimeter():.2f}")
```

---

### 2. Assignment 3 — Question 2: Comparing Persons Based on Age (Operator Overloading)
```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    # Greater than: person1 > person2
    def __gt__(self, other) -> bool:
        if isinstance(other, Person):
            return self.age > other.age
        return NotImplemented

    # Less than: person1 < person2
    def __lt__(self, other) -> bool:
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented

    # Equal to: person1 == person2
    def __eq__(self, other) -> bool:
        if isinstance(other, Person):
            return self.age == other.age
        return False

    def __str__(self) -> str:
        return f"Person(Name='{self.name}', Age={self.age})"

# Demonstration for Danny and Thomas
if __name__ == "__main__":
    p1 = Person("Danny", 30)
    p2 = Person("Thomas", 25)

    print(f"{p1} vs {p2}:")
    if p1 > p2:
        print(f"{p1.name} ({p1.age}) is older than {p2.name} ({p2.age}).")
    elif p1 < p2:
        print(f"{p1.name} ({p1.age}) is younger than {p2.name} ({p2.age}).")
    else:
        print(f"{p1.name} and {p2.name} are the same age.")
```

---

### 3. Assignment 3 — Question 3: Library Book Class (Public, Protected & Private Attributes)
```python
class Book:
    """Demonstrates Public, Protected, and Private access modifiers in Python."""
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title          # Public: Accessible anywhere
        self._author = author        # Protected: Accessible within class & subclasses (convention)
        self.__isbn = isbn          # Private: Name-mangled to _Book__isbn

    # Protected method to update author details
    def _update_author_details(self, new_author: str) -> None:
        """Protected helper to update author."""
        print(f"[LOG] Updating author from '{self._author}' to '{new_author}'")
        self._author = new_author

    # Public getters to demonstrate clean encapsulation
    @property
    def author(self) -> str:
        return self._author

    @property
    def isbn(self) -> str:
        # Mask ISBN for security (shows only last 4 digits)
        return f"***-***-{self.__isbn[-4:]}"

    def update_author(self, new_author: str) -> None:
        """Public API calling protected updater."""
        self._update_author_details(new_author)

    def __str__(self) -> str:
        return f"Book Title: '{self.title}' | Author: '{self._author}' | ISBN: {self.isbn}"

# Demonstration
if __name__ == "__main__":
    book = Book("Python Mastery", "Guido van Rossum", "978-0134076423")
    print(book)

    # Accessing attributes according to their scope:
    print(f"Public Title: {book.title}")          # Allowed
    print(f"Protected Author: {book._author}")     # Works by convention, but discouraged outside
    # print(book.__isbn)                          # Raises AttributeError (Private!)
    print(f"Accessing Private via Mangled Name: {book._Book__isbn}") # Demonstrates name-mangling

    # Updating author via protected method
    book.update_author("Modern Python Community")
    print(book)
```

---

### 4. Suggested Experiments 9 & 10: Basic Class & Function Calling
```python
# Experiment 9: Class definition, object creation, and calling print method
class Greeter:
    def __init__(self, greeting_message: str):
        self.message = greeting_message

    def display(self) -> None:
        """Simple print function defined in class."""
        print(f"Class Print Output: {self.message}")

# Experiment 10: Standalone function with single string parameter
def print_string_parameter(param: str) -> None:
    """Takes a single string parameter and prints it."""
    print(f"Function Parameter Output: {param}")

if __name__ == "__main__":
    # Test Experiment 9
    obj = Greeter("Hello from VIT Bhopal Python Class!")
    obj.display()

    # Test Experiment 10
    print_string_parameter("Testing single string parameter passing.")
```

