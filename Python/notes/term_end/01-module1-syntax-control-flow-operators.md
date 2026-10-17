# 📘 Unit 1: Python Fundamentals, Syntax & Control Flow

---

## 1. Python Architecture & Python 2 vs 3

### 1.1 Core Characteristics
* **Interpreted & Dynamically Typed**: Types are resolved at runtime; variables are references/pointers to memory objects.
* **Automatic Garbage Collection**: Uses reference counting augmented with a cyclic garbage collector.

### 1.2 Python 2 vs Python 3 Comparative Table

| Feature | Python 2 | Python 3 |
|:---|:---|:---|
| **Print Statement** | Keyword: `print "Hello"` | Built-in function: `print("Hello", end="\n")` |
| **Integer Division** | `5 / 2 = 2` (Truncates to integer floor) | `5 / 2 = 2.5` (Float); Floor division uses `5 // 2 = 2` |
| **String Storage** | ASCII by default; Unicode requires `u'text'` | **Unicode (UTF-8)** by default; Raw bytes require `b'data'` |
| **Input Function** | `input()` evaluated code; `raw_input()` returned string | `raw_input()` eliminated; `input()` always returns `str` |
| **Range Function** | `range()` allocated full memory list; `xrange()` was generator | `xrange()` eliminated; `range()` is memory-efficient iterator |

---

## 2. Operators & Precedence

### 2.1 Bitwise Operators
* `a & b`: Bitwise AND (1 if both bits are 1).
* `a | b`: Bitwise OR (1 if either bit is 1).
* `a ^ b`: Bitwise XOR (1 if bits differ).
* `~a`: Bitwise NOT (Inverts bits: $\sim a = -(a + 1)$ in 2's complement).
* `a << n`: Left shift (Multiplies by $2^n$).
* `a >> n`: Right shift (Floor divides by $2^n$).

### 2.2 Identity vs Equality Operators
* `a == b`: Value Equality (checks if the contents/values are equal).
* `a is b`: Identity Equality (checks if both variables reference the **exact same memory address**: `id(a) == id(b)`).
* *Integer Caching*: Python pre-allocates integers from $-5$ to $256$. Thus, `x = 250; y = 250; x is y` is `True`, whereas `x = 300; y = 300; x is y` may be `False`.

---

## 3. Control Flow Structures

### 3.1 Loop `else` Clause
In Python, both `for` and `while` loops support an `else` block:
* The `else` block executes **only if the loop terminates normally** (without hitting a `break` statement).
```python
def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is divisible by {i}")
            break
    else:
        print(f"{n} is prime!")  # Executes only if no divisor found

# Test calls:
check_prime(11)
check_prime(12)
```

##### Sample Input & Output:
```text
Sample Output:
11 is prime!
12 is divisible by 2
```

### 3.2 String Slicing (`[start:stop:step]`)
* `s[::-1]`: Reverses the string in $O(n)$ time.
* `s[1:6:2]`: Elements from index 1 up to (excluding) 6 with step 2.

```python
s = "PYTHON_FAT_2026"
print("Original String: ", s)
print("Reversed (s[::-1]):", s[::-1])
print("Slice (s[0:6]):    ", s[0:6])
print("Step 2 (s[::2]):   ", s[::2])
```

##### Sample Input & Output:
```text
Sample Output:
Original String:  PYTHON_FAT_2026
Reversed (s[::-1]): 6202_TAF_NOHTYP
Slice (s[0:6]):     PYTHON
Step 2 (s[::2]):    PTO_A_06
```

---

## 4. Model Exam Questions & Answers

### Question 1 (12 Marks)
**(a) Explain the differences between Python 2 and Python 3 with suitable code snippets.**  
**(b) Write a Python program to print the first $N$ Fibonacci numbers and check if the sum of all generated numbers is even or odd.**

**Solution**:
1. **Part (a)**: *[Include the 5-point comparative table from Section 1.2]*.
2. **Part (b) Program**:
```python
def fibonacci_series(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    
    a, b = 0, 1
    fib_list = []
    
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
        
    total_sum = sum(fib_list)
    parity = "Even" if total_sum % 2 == 0 else "Odd"
    
    print(f"First {n} Fibonacci numbers: {fib_list}")
    print(f"Sum = {total_sum} | Parity: {parity}")

fibonacci_series(6)
```

##### Sample Input & Output:
```text
Sample Input:
fibonacci_series(6)

Sample Output:
First 6 Fibonacci numbers: [0, 1, 1, 2, 3, 5]
Sum = 12 | Parity: Even
```

### Question 2 (8 Marks)
**Differentiate between `is` and `==` operators in Python. Illustrate with an example involving lists.**

**Solution**:
```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
```

##### Sample Input & Output:
```text
Sample Output:
list1 == list2: True  (Values are identical [1, 2, 3])
list1 is list2: False (Different heap allocations: id(list1) != id(list2))
list1 is list3: True  (Point to the same reference: id(list1) == id(list3))
```
* `==` invokes the `__eq__()` dunder method to compare values.
* `is` compares memory pointers (`id(a) == id(b)`).
