# 🐍 Python: Strings, Functions & Exam Traps!

Welcome to the Python practice zone. We are covering all the assignment questions for Strings and Functions, plus the classic Exam "Predict the Output" traps that professors love to set.

---

## 1. String Manipulation (Assignment 2)
Strings in Python are **immutable** (they can't be changed after creation). So when you "modify" a string, you're actually creating a new one!

<details>
<summary>💡 Top String Methods to Memorize</summary>

* `s.count(char)` - Frequency of a character.
* `s.split()` - Splits a sentence into a list of words.
* `s.replace(old, new)` - Replaces characters.
* `''.join(list)` - Glues a list of strings back together.
</details>

### 🔥 Quick Solves:
1. **Find frequency of each character:**
   ```python
   # The cheating way (using built-ins)
   from collections import Counter
   freq = Counter("hello")
   
   # using dictionary
   s="hello"
   f={}
   for i in s:
	   if i not in f:
		   f[i]=1
	   else:
		   f[i]+=1
	
	for i,j in f.items():
		print(i, j)
   ```
2. **Remove duplicate characters:**
   ```python
   # Sets automatically remove duplicates, but lose order!
   s = "programming"
   unique_s = "".join(set(s)) 
   ```
3. **Check Anagrams:**
   ```python
   # If sorting them makes them identical, they are anagrams!
   is_anagram = sorted("listen") == sorted("silent") # True
   ```
4. **Reverse Words in a Sentence:**
   ```python
   sentence = "I love python"
   # Split, reverse the list, and join!
   reversed_sentence = " ".join(sentence.split()[::-1]) # "python love I"
   ```
5. **Check Substring:**
   ```python
   is_substring = "th" in "python" # True
   ```

---

## 2. Functions (Activity 1)

Functions in Python are defined using `def`. They can take arguments and `return` values. If a function doesn't have a `return` statement, it returns `None`.

### 🔥 Quick Solves:
```python
# 1. Square of a number
def square(n): return n ** 2

# 2. Largest of three
def largest(a, b, c): return max(a, b, c)

# 3. No parameters, no return
def greet(): 
    print("Welcome to Python")

# 4. No parameters, with return
def get_year(): 
    return 2026
```

---

## 3. Classic Logic Puzzles (Assignment 1)

<details>
<summary>🧩 Fibonacci Series</summary>

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
```
</details>

<details>
<summary>🧩 Factorial & GCD (Math module is your friend)</summary>

```python
import math
print(math.factorial(5)) # 120
print(math.gcd(48, 18))  # 6
print(math.lcm(12, 15))  # 60

#how about wihtout math module

```
</details>

---

## 🎯 Exam Trap: Predict the Output

> [!WARNING]
> **Can you trace these without running the code?** This is exactly how they test your deep understanding!

**Question 1: The String Trap**
```python
s = "Hello"
s[0] = "J"
print(s)
```
* **Answer:** **TypeError!** Strings are immutable in Python. You can't change `s[0]`. You must do `s = "J" + s[1:]`.

**Question 2: The Scope Trap**
```python
x = 10
def change():
    x = 20
change()
print(x)
```
* **Answer:** **10**. The `x` inside the function is a local variable. It doesn't affect the global `x` unless you write `global x`.

**Question 3: The Default Argument Trap (Classic!)**
```python
def append_to(num, target=[]):
    target.append(num)
    return target

print(append_to(1))
print(append_to(2))
```
* **Answer:** `[1]` then `[1, 2]`. Default lists are created *once* when the function is defined, not every time it's called! Always use `target=None` instead.

**Question 4: The Slicing Trick**
```python
s = "PYTHON"
print(s[100:])
```
* **Answer:** `""` (Empty string). Slicing out of bounds doesn't throw an `IndexError`, it just returns an empty string!

**Question 5: List Multiplication**
```python
L = [1, 2]
print(L * 3)
```
* **Answer:** `[1, 2, 1, 2, 1, 2]`. Multiplying a list duplicates its contents, it doesn't do vector math.

**Question 6: Dictionary Key Error?**
```python
d = {"a": 1, "b": 2}
print(d.get("c", 3))
```
* **Answer:** `3`. The `.get()` method safely looks for "c". If it doesn't exist, it returns the default value `3` instead of crashing.

**Question 7: Tuple Mutability Trick**
```python
t = (1, [2, 3])
t[1].append(4)
print(t)
```
* **Answer:** `(1, [2, 3, 4])`. Wait, aren't tuples immutable? Yes! The tuple's reference to the list cannot change, but the list *inside* the tuple can still be modified!

**Question 8: The `is` vs `==` Trap**
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
```
* **Answer:** `True`, then `False`. `==` checks if the *values* are the same. `is` checks if they are the exact same *object in memory*. Since we created two separate lists, `is` is false.

**Question 9: Boolean Math**
```python
print(True + True + False)
```
* **Answer:** `2`. In Python, `True` is mathematically `1` and `False` is `0`. 

**Question 10: Local Variable Shadowing**
```python
x = 5
def func():
    print(x)
    x = 10
func()
```
* **Answer:** **UnboundLocalError!** Because `x = 10` is inside the function, Python treats `x` as a local variable for the *entire* function. When it hits `print(x)` on the line above, the local `x` hasn't been assigned yet, so it crashes.

**Question 11: Set Uniqueness**
```python
my_set = {1, 2, 2, 3, True, 1.0}
print(len(my_set))
```
* **Answer:** `3`. The set will be `{1, 2, 3}`. Duplicates are removed. Notice that `1`, `True`, and `1.0` are considered the EXACT same value in Python sets!

**Question 12: Lambda in a loop**
```python
funcs = [lambda x: x + i for i in range(3)]
print(funcs[0](10))
```
* **Answer:** `12`. This is a famously hard interview question. The lambda doesn't evaluate `i` until it's *called*. By the time you call it, the loop has finished and `i` is `2`. So `10 + 2 = 12`.

**Question 13: Formatting Trap**
```python
print(f"{2 * 3 = }")
```
* **Answer:** `2 * 3 = 6`. Using `=` inside an f-string prints both the expression and the result! Extremely useful for debugging.
