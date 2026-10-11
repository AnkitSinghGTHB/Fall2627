# 📘 Unit 3: Object-Oriented Programming, Dunder Methods & Exceptions

---

## 1. Python OOP Architecture & Access Control

### 1.1 Method Types & Decorators
1. **Instance Method**: Receives `self` (the instance) as the first argument; can read and mutate instance state.
2. **Class Method (`@classmethod`)**: Receives `cls` (the class) as the first argument; used for factory constructors.
3. **Static Method (`@staticmethod`)**: Receives neither `self` nor `cls`; acts as a regular utility function bound to the class namespace.

```python
class Employee:
    company = "VIT Bhopal"  # Class variable

    def __init__(self, name, salary):
        self.name = name          # Instance variable
        self.__salary = salary    # Private attribute (Name Mangled)

    @classmethod
    def from_string(cls, emp_str):  # Alternative constructor
        name, salary = emp_str.split("-")
        return cls(name, float(salary))

    @staticmethod
    def is_workday(day_name):
        return day_name.lower() not in ["saturday", "sunday"]
```

### 1.2 Access Specifiers & Name Mangling
Python does not enforce compile-time access restrictions (`public`, `protected`, `private`), but uses established naming conventions and runtime name mangling:

* **Public**: Accessible freely anywhere (`self.title`).
* **Protected (`_`)**: Convention indicating internal use (`self._author`). Subclasses and module internals may access it, but external users should treat it as non-public.
* **Private (`__`)**: Triggers **Name Mangling** (`self.__isbn`). Python automatically rewrites the attribute internally as `_ClassName__attribute` (`_Book__isbn`) to prevent accidental overrides in subclasses.

#### Complete Example: Library System `Book` Class (Assignment 3)
```python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title          # Public Attribute
        self._author = author       # Protected Attribute
        self.__isbn = isbn          # Private Attribute (Name Mangled)

    # Protected Method
    def _update_author_details(self, new_author):
        """Protected method to update author details internally or by subclasses."""
        self._author = new_author
        print(f"Author updated to: {self._author}")

    # Public Getter / Setter for Private Attribute
    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, new_isbn):
        if len(new_isbn) in [10, 13]:
            self.__isbn = new_isbn
        else:
            raise ValueError("Invalid ISBN length!")

    def display_details(self):
        print(f"Title: {self.title} | Author: {self._author} | ISBN: {self.__isbn}")

# Demonstration
b = Book("Automata Theory", "John Hopcroft", "978-0131103627")
print(b.title)                     # Allowed: Automata Theory
print(b._author)                   # Accessible by convention: John Hopcroft
# print(b.__isbn)                  # Raises AttributeError!
print(b._Book__isbn)               # Accessible via name mangling: 978-0131103627
b._update_author_details("J. E. Hopcroft & J. D. Ullman")
```

---

## 2. Inheritance & Method Resolution Order (C3 Linearization)

### 2.1 The Diamond Problem & `super()`
When multiple parent classes share a common base ancestor:

```
         A
       /   \
      B     C
       \   /
         D
```

Python calculates the lookup path using the **C3 Linearization algorithm**:
$$\text{MRO}(D) = D \to B \to C \to A \to \text{object}$$
* Accessed via `D.__mro__` or `D.mro()`.
* `super()` follows this exact linearization path rather than jumping strictly to the parent class.

---

## 3. Operator Overloading & Dunder Methods

Python objects customize operator behaviors by implementing double-underscore ("dunder") methods:

| Operator | Dunder Method | Meaning / Operation |
|:---|:---|:---|
| `+` | `__add__(self, other)` | Addition / Vector sum |
| `-` | `__sub__(self, other)` | Subtraction |
| `*` | `__mul__(self, other)` | Multiplication / Dot product |
| `==` | `__eq__(self, other)` | Equality comparison |
| `<` | `__lt__(self, other)` | Less-than comparison |
| `len()` | `__len__(self)` | Length of container |
| `str()` | `__str__(self)` | Informal string for end-users |
| `repr()` | `__repr__(self)` | Official unambiguous string for debugging |

```python
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
```

#### Complete Example: Comparing Persons by Age via Operator Overloading (Assignment 3)
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Overloading '>' operator
    def __gt__(self, other):
        if isinstance(other, Person):
            return self.age > other.age
        return NotImplemented

    # Overloading '<' operator
    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented

    # Overloading '==' operator
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age
        return NotImplemented

    def __str__(self):
        return f"Person({self.name}, {self.age} years)"

# Given in Assignment 3:
# Person1: Danny, Age: 30
# Person2: Thomas, Age: 25
p1 = Person("Danny", 30)
p2 = Person("Thomas", 25)

print(f"{p1.name} ({p1.age}) vs {p2.name} ({p2.age}):")
if p1 > p2:
    print(f"-> {p1.name} is older than {p2.name}.")
elif p1 < p2:
    print(f"-> {p1.name} is younger than {p2.name}.")
else:
    print(f"-> {p1.name} and {p2.name} are of the same age.")
```

---

## 4. Exception Handling Architecture

### 4.1 The Complete `try-except-else-finally` Lifecycle

```
[ try block ] ──▶ Executes risky code prone to runtime exceptions
       │
       ├─ (If exception raised) ────▶ [ except block ] : Handles error gracefully
       │
       ├─ (If NO exception raised) ─▶ [ else block ]   : Executes code requiring successful try
       │
       └─ (Always executed) ────────▶ [ finally block ]: Releases resources (close files, DB locks)
```

### 4.2 Custom User-Defined Exceptions
```python
class InsufficientBalanceError(Exception):
    """Raised when withdrawal exceeds available account balance."""
    def __init__(self, balance, amount):
        super().__init__(f"Attempted to withdraw ₹{amount}, but balance is only ₹{balance}!")
        self.balance = balance
        self.amount = amount

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)
        self.balance -= amount
        return self.balance
```

---

## 5. Model Exam Questions & Answers

### Question 1 (12 Marks)
**Implement a complete Python class hierarchy demonstrating Multiple Inheritance. Explain how Python resolves method calls in diamond inheritance using Method Resolution Order (MRO). Show code with `super()`.**

**Solution**:
```python
class Device:
    def identify(self):
        print("Device identification")

class Phone(Device):
    def identify(self):
        print("Phone subsystem")
        super().identify()

class Camera(Device):
    def identify(self):
        print("Camera subsystem")
        super().identify()

class SmartPhone(Phone, Camera):
    def identify(self):
        print("SmartPhone initializing:")
        super().identify()

sp = SmartPhone()
sp.identify()
print("MRO Order:", [cls.__name__ for cls in SmartPhone.__mro__])

# Output:
# SmartPhone initializing:
# Phone subsystem
# Camera subsystem
# Device identification
# MRO Order: ['SmartPhone', 'Phone', 'Camera', 'Device', 'object']
```

### Question 2 (8 Marks)
**Explain Abstract Base Classes (ABCs) in Python. Write a program with an abstract class `Shape` having abstract methods `area()` and `perimeter()`, implemented by a derived class `Rectangle`.**

**Solution**:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 4)
print(f"Area: {rect.area()}, Perimeter: {rect.perimeter()}")
# Output: Area: 20, Perimeter: 18
```

---

### Question 3 (12 Marks) [Direct from Assignment 3]
**Write a Python program to calculate the area and perimeter of different polygons using an Object-Oriented hierarchy. Implement classes for Triangle, Rectangle, and Regular Polygon with proper mathematical formulas.**

**Solution**:
```python
import math
from abc import ABC, abstractmethod

class Polygon(ABC):
    """Abstract base class representing an arbitrary geometric polygon."""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def display(self):
        print(f"\n--- {self.name} ---")
        print(f"Perimeter: {self.perimeter():.2f}")
        print(f"Area:      {self.area():.2f}")

class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Heron's Formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

class RegularPolygon(Polygon):
    """Regular n-sided polygon with side length s."""
    def __init__(self, num_sides, side_length):
        super().__init__(f"Regular {num_sides}-gon")
        self.n = num_sides
        self.s = side_length

    def perimeter(self):
        return self.n * self.s

    def area(self):
        # Area = (n * s^2) / (4 * tan(pi / n))
        return (self.n * (self.s ** 2)) / (4 * math.tan(math.pi / self.n))

# Execution & Testing
if __name__ == "__main__":
    t = Triangle(3, 4, 5)
    r = Rectangle(10, 5)
    hex_poly = RegularPolygon(6, 4)  # Regular Hexagon

    for shape in [t, r, hex_poly]:
        shape.display()
```

---

### Question 4 (8 Marks) [Direct from Suggested Experiments 3]
**(a) Write a Python program to find the most frequent words in a text read from a file.**  
**(b) Write a program defining a class, instantiating an object, and calling its method, along with a function with a single string parameter.**

**Solution**:
```python
import re
from collections import Counter

# Part (a): Most Frequent Words in a File
def find_most_frequent_words(filename, top_n=5):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read().lower()
        
        # Tokenize words using regular expression (alphanumeric only)
        words = re.findall(r"\b[a-z0-9]+\b", text)
        
        counts = Counter(words)
        print(f"Top {top_n} Most Frequent Words:")
        for word, freq in counts.most_common(top_n):
            print(f"- '{word}': {freq} times")
        return counts.most_common(top_n)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Part (b): Simple Class Method & Function with Single String Parameter
def greet_student(msg: str):
    """Function with single string parameter."""
    print(f"[Function Call Output]: {msg}")

class Greeter:
    """Class with a simple print method."""
    def __init__(self, greeting_prefix="Hello"):
        self.prefix = greeting_prefix

    def print_message(self, target_name):
        print(f"[Class Method Output]: {self.prefix}, {target_name}!")

# Demonstration
if __name__ == "__main__":
    greet_student("Welcome to Python Programming FAT preparation!")
    obj = Greeter("Good Morning")
    obj.print_message("Ankit")
```
