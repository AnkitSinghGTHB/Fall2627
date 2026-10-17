# 📘 Unit 2: Collections, Functions, Scoping & Regular Expressions

---

## 1. Python Collections Comparative Architecture

| Collection | Mutability | Ordered? | Duplicates Allowed? | Indexing | Internal Implementation |
|:---|:---|:---|:---|:---|:---|
| **List (`[]`)** | **Mutable** | Yes | Yes | Integer indexing (`[0]`) | Dynamic array of pointers |
| **Tuple (`()`)** | **Immutable** | Yes | Yes | Integer indexing (`[0]`) | Fixed-size array (fast, low memory) |
| **Set (`{}`)** | **Mutable** | No | **No** (Unique only) | Non-indexable | Hash table (keys only, $O(1)$ lookup) |
| **Dict (`{k: v}`)** | **Mutable** | Yes (Python 3.7+) | Unique Keys; Duplicate Values | Key indexing (`['key']`) | Sparse hash table ($O(1)$ average) |

### 1.1 List & Dictionary Comprehensions
* **List Comprehension**:
  ```python
  even_squares = [x**2 for x in range(10) if x % 2 == 0]
  print("Even Squares:", even_squares)
  ```
  ##### Sample Output:
  ```text
  Even Squares: [0, 4, 16, 36, 64]
  ```

* **Dictionary Comprehension**:
  ```python
  char_counts = {word: len(word) for word in ["apple", "banana", "cherry"]}
  print("Word Lengths:", char_counts)
  ```
  ##### Sample Output:
  ```text
  Word Lengths: {'apple': 5, 'banana': 6, 'cherry': 6}
  ```

---

## 2. Advanced Function Parameters & Scoping

### 2.1 Variable-Length Arguments (`*args` and `**kwargs`)
* `*args`: Captures arbitrary extra positional arguments as a **tuple**.
* `**kwargs`: Captures arbitrary extra keyword arguments as a **dictionary**.

```python
def flexible_logger(prefix, *args, **kwargs):
    print(f"Prefix: {prefix}")
    print(f"Positional args: {args}")    # Tuple
    print(f"Keyword args: {kwargs}")      # Dict

flexible_logger("WARN", 101, "Timeout", user="Ankit", ip="192.168.1.1")
```

##### Sample Input & Output:
```text
Sample Output:
Prefix: WARN
Positional args: (101, 'Timeout')
Keyword args: {'user': 'Ankit', 'ip': '192.168.1.1'}
```

### 2.2 The LEGB Scoping Rule
Python resolves variable names in strict hierarchical order:
1. **L (Local)**: Defined inside the current function block.
2. **E (Enclosing)**: Defined in the outer scope of any nested function.
3. **G (Global)**: Defined at top-level module file.
4. **B (Built-in)**: Pre-loaded Python symbols (`len`, `range`, `print`).

* Modifying outer variables requires explicit declaration:
  - `global var_name`: Binds identifier to module-level global variable.
  - `nonlocal var_name`: Binds identifier to nearest enclosing outer function variable.

---

## 3. Regular Expressions (`re` Module)

### 3.1 Primary Metacharacters
* `\d`: Any digit `[0-9]`; `\D`: Non-digit.
* `\w`: Any alphanumeric character `[a-zA-Z0-9_]`; `\W`: Non-alphanumeric.
* `\s`: Whitespace; `\S`: Non-whitespace.
* `^`: Anchors at start of string; `$`: Anchors at end of string.
* `+`: 1 or more repetitions; `*`: 0 or more repetitions; `?`: 0 or 1 repetition.

### 3.2 Key Regex Functions
* `re.match(pattern, string)`: Matches **only at the beginning** of string.
* `re.search(pattern, string)`: Scans throughout string for first match.
* `re.findall(pattern, string)`: Returns all non-overlapping matches as a list of strings.
* `re.sub(pattern, replacement, string)`: Replaces occurrences.

```python
import re

email_text = "Contact support@vit.ac.in or admissions@vitbhopal.ac.in for details."
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern, email_text)
print("Extracted Emails:", emails)
```

##### Sample Input & Output:
```text
Sample Output:
Extracted Emails: ['support@vit.ac.in', 'admissions@vitbhopal.ac.in']
```

---

## 4. Model Exam Questions & Answers

### Question 1 (12 Marks)
**(a) Differentiate between shallow copy and deep copy in Python with code examples.**  
**(b) Write a function using regular expressions to validate whether a given string is a valid password meeting the following rules: at least 8 characters, at least one uppercase letter, one lowercase letter, one digit, and one special character (`@#$%^&+=`).**

**Solution**:
1. **Part (a): Shallow Copy vs Deep Copy**:
   - `copy.copy()`: Creates a new compound object, but inserts references to the original nested objects.
   - `copy.deepcopy()`: Creates a new compound object and recursively copies all nested child objects.
   ```python
   import copy
   original = [[1, 2], [3, 4]]
   shallow = copy.copy(original)
   deep = copy.deepcopy(original)

   original[0][0] = 99
   print("Shallow Copy element [0][0]:", shallow[0][0])  # Mutated!
   print("Deep Copy element [0][0]:   ", deep[0][0])     # Independent!
   ```
   ##### Sample Output:
   ```text
   Shallow Copy element [0][0]: 99
   Deep Copy element [0][0]:    1
   ```

2. **Part (b): Password Validation Program**:
```python
import re

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Must contain at least one lowercase letter."
    if not re.search(r"\d", password):
        return False, "Must contain at least one digit."
    if not re.search(r"[@#$%^&+=]", password):
        return False, "Must contain at least one special character (@#$%^&+=)."
    return True, "Valid password!"

# Test passwords
print(validate_password("SecurePass@2026"))
print(validate_password("weakpass"))
```

##### Sample Input & Output:
```text
Sample Output:
(True, 'Valid password!')
(False, 'Must contain at least one uppercase letter.')
```

### Question 2 (8 Marks)
**Explain the LEGB rule of variable scoping in Python. Demonstrate the use of `global` and `nonlocal` keywords.**

**Solution**:
1. **LEGB Rule Hierarchy**: Local $\to$ Enclosing $\to$ Global $\to$ Built-in.
2. **Demonstration Code**:
```python
counter = 0  # Global

def outer():
    x = 10   # Enclosing

    def inner():
        nonlocal x
        global counter
        x += 5
        counter += 1
        print(f"Inside inner: x={x}, counter={counter}")

    inner()
    print(f"Inside outer: x={x}")

outer()
```

##### Sample Input & Output:
```text
Sample Output:
Inside inner: x=15, counter=1
Inside outer: x=15
```
