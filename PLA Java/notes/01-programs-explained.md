# ☕ Lesson 1 — Java Programs Explained (Line by Line)

> **TL;DR**: Here are the actual programs from class, broken down so a 10-year-old could follow along. No jargon, no textbook energy.

---

## Program 1: 🔢 Prime Numbers in a Range

**What it does**: Finds all prime numbers between two values (e.g., 10 to 50).

**What's a prime number?** A number greater than 1 that's only divisible by 1 and itself. (2, 3, 5, 7, 11, 13, ...)

### The Logic (in English first)

```
For each number from 'start' to 'end':
    Skip if it's ≤ 1 (not prime by definition)
    Assume it's prime
    Try dividing by every number from 2 to (number-1)
        If any division has remainder 0 → NOT prime, stop checking
    If it survived all checks → it IS prime, print it
```

### The Code (with annotations)

```java
public class PrimeNumbersNaive {

    // This method finds and prints primes between 'start' and 'end'
    public static void printPrimesInRange(int start, int end) {

        for (int i = start; i <= end; i++) {  // Loop through each number

            if (i <= 1) {           // 0 and 1 are NOT prime
                continue;           // skip to next number
            }

            boolean isPrime = true; // Assume it's prime until proven otherwise

            for (int j = 2; j < i; j++) {   // Try every divisor from 2 to i-1
                if (i % j == 0) {           // If i is divisible by j...
                    isPrime = false;        // ...it's NOT prime
                    break;                  // No need to check more, exit inner loop
                }
            }

            if (isPrime) {                  // If no divisor was found
                System.out.print(i + " "); // Print the prime number
            }
        }
        System.out.println();  // New line at the end
    }

    public static void main(String[] args) {
        int start = 10;
        int end = 50;
        System.out.println("Prime numbers between " + start + " and " + end + ":");
        printPrimesInRange(start, end);
    }
}
```

**Output**: `11 13 17 19 23 29 31 37 41 43 47`

### 🧠 Key Concepts Used

| Concept | How it's used |
|---------|--------------|
| `for` loop | Iterating through numbers |
| `if / continue` | Skipping non-prime candidates |
| `boolean` flag | Tracking whether number is prime |
| `%` (modulo) | Checking divisibility (remainder = 0 means divisible) |
| `break` | Exiting early when we know it's not prime |

### ⚡ How to Optimize (Bonus)
> You only need to check divisors up to √n instead of n-1. Change `j < i` to `j <= Math.sqrt(i)`. Same result, much faster.

---

## Program 2: 🐇 Fibonacci Series (Recursive)

**What it does**: Prints the first N numbers of the Fibonacci sequence.

**What's Fibonacci?** Each number = sum of the two before it: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...`

### The Logic

```
fibonacci(0) = 0          ← base case
fibonacci(1) = 1          ← base case
fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)   ← recursive case

Example: fibonacci(4) = fibonacci(3) + fibonacci(2)
                       = (fibonacci(2) + fibonacci(1)) + (fibonacci(1) + fibonacci(0))
                       = ((1+0) + 1) + (1 + 0)
                       = 3
```

### The Code

```java
public class FibonacciRecursive {

    // Returns the nth Fibonacci number
    public static int calculateFibonacci(int n) {
        if (n <= 1) {           // Base case: fib(0)=0, fib(1)=1
            return n;
        }
        // Recursive case: fib(n) = fib(n-1) + fib(n-2)
        return calculateFibonacci(n - 1) + calculateFibonacci(n - 2);
    }

    public static void main(String[] args) {
        int terms = 10;
        System.out.println("Fibonacci series up to " + terms + " terms:");
        for (int i = 0; i < terms; i++) {
            System.out.print(calculateFibonacci(i) + " ");
        }
        System.out.println();
    }
}
```

**Output**: `0 1 1 2 3 5 8 13 21 34`

### 🧠 Key Concepts

| Concept | How it's used |
|---------|--------------|
| **Recursion** | Function calls itself with a smaller input |
| **Base case** | Stops recursion (n ≤ 1) — WITHOUT THIS, infinite loop! |
| **Return value** | Each call returns a number that gets added up |

### ⚠️ Why This Is "Naive"
> This approach recalculates the same values MANY times. `fib(5)` calls `fib(3)` twice! For large n, it's extremely slow (exponential time). Better approach: use a loop or memoization.

---

## Program 3: 🔄 Collatz Conjecture (3n+1 Problem)

**What it does**: Takes a number and applies a simple rule until you reach 1.

**The Rule**:
- If number is **even** → divide by 2
- If number is **odd** → multiply by 3, add 1

> 🤯 **Fun fact**: Nobody has ever proven that this always reaches 1. It's an unsolved math problem! But it works for every number ever tested.

### The Code

```java
import java.util.*;

// HackerRank - Number Transformation Challenge
public class Solution1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);  // Read input from user
        int n = sc.nextInt();                 // Get the starting number
        System.out.print(n);                  // Print starting number

        while (n != 1) {                      // Keep going until we reach 1
            if (n % 2 == 0) {                 // If even...
                n /= 2;                       // ...divide by 2
            } else {                          // If odd...
                n = (n * 3) + 1;              // ...multiply by 3 and add 1
            }
            System.out.print(" " + n);        // Print each step
        }
        sc.close();
    }
}
```

**Example** (n=6): `6 3 10 5 16 8 4 2 1`

### 🧠 Key Concepts

| Concept | How it's used |
|---------|--------------|
| `Scanner` | Reading user input |
| `while` loop | Keeps running until condition is false |
| `n % 2 == 0` | Checking even/odd |
| `n /= 2` | Shorthand for `n = n / 2` |

---

## Program 4: 💰 Maximum Product Decomposition

**What it does**: Breaks a number into a sum of 2s and 3s to maximize the product.

**Why 3s?** Mathematically, breaking into 3s gives the maximum product. If remainder is 1, use one fewer 3 and add a 4 (= 2+2 = 2×2) instead, because 3×1 < 2×2.

### The Code

```java
import java.util.*;

public class Solution2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int a = n / 3;     // How many 3s can we use?
        int b = n % 3;     // What's the remainder?

        if (b == 1) {       // Remainder 1: 3×1=3, but 2×2=4 is better!
            a--;            // Use one fewer 3
            b = 2;          // Replace 3+1 with 2+2 (two 2s)
        } else if (b == 2) {
            b = 1;          // Remainder 2: just use one 2
        }
        // b == 0 means perfect split into 3s, no 2s needed

        int sum = 1;
        for (int i = 0; i < a; i++) {
            sum *= 3;       // Multiply all the 3s
        }
        for (int i = 0; i < b; i++) {
            sum *= 2;       // Multiply all the 2s
        }
        System.out.println(sum);
        sc.close();
    }
}
```

**Example**: n=10 → 3+3+2+2 → 3×3×2×2 = **36**

### 🧠 Key Concepts

| Concept | How it's used |
|---------|--------------|
| **Greedy algorithm** | Use as many 3s as possible for max product |
| **Edge case handling** | Remainder 1 is worse than 2+2 |
| **Integer division** | `n/3` gives how many 3s, `n%3` gives leftover |

---

## 📝 Java Patterns to Recognize

> These patterns repeat in almost every exam question. Know the template, fill in the specific logic.

| Pattern | Template |
|---------|----------|
| **Check all numbers in range** | `for (int i = start; i <= end; i++) { ... }` |
| **Check divisibility** | `if (n % d == 0)` |
| **Even/Odd check** | `if (n % 2 == 0)` |
| **Read user input** | `Scanner sc = new Scanner(System.in); int n = sc.nextInt();` |
| **Loop until condition** | `while (condition) { ... }` |
| **Recursion** | Base case + recursive call that reduces the problem |
| **Flag variable** | `boolean found = false; ... if (condition) found = true;` |
| **Accumulate a result** | `int sum = 0; for (...) sum += value;` |

---

## ✅ Mini Challenges (2 min each)

1. Modify the prime program to only print primes that are also **odd** (skip 2)
2. What happens if you call `calculateFibonacci(50)`? Why?
3. Trace the Collatz sequence for n = 7 by hand
4. In the product decomposition, why is remainder=1 special?

<details>
<summary>🔑 Answers</summary>

1. Add `if (i == 2) continue;` after the `i <= 1` check, OR start the range from 3
2. It takes FOREVER — exponential time complexity. Each call branches into 2 more calls. ~2⁵⁰ operations!
3. 7 → 22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
4. Because 3×1 = 3, but 2×2 = 4. So it's better to "trade" a 3+1 for 2+2

</details>

---

**⏱️ Time spent: ~15 min. You now understand all 4 programs!**
