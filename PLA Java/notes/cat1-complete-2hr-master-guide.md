# ⚡ PLA Java CAT-1: Complete 2-Hour Zero-to-Hero Exam Guide
> **Course**: Competitive Coding Practices (PLA1004 / PLA1006) — VIT Bhopal  
> **Target Audience**: Anyone starting with **0 prior knowledge** who needs to understand and master every single algorithm, assignment question, and previous-year exam question (PYQ) in **under 2 hours**.

---

## ⏱️ The 2-Hour Speed Study Roadmap

```
┌───────────────────────────────────────────────────────────────────────────────┐
│ 00:00 - 00:20  │ Chapter 1: Complexity & Loop Analysis (O(1), O(n), O(n²))    │
│ 00:20 - 00:50  │ Chapter 2: Number Theory (Sieve, CRT, Euler Phi, Karatsuba)  │
│ 00:50 - 01:15  │ Chapter 3: Bit Manipulation (Palindrome, Nibbles, 1s Flip)   │
│ 01:15 - 01:45  │ Chapter 4: Array Mastery (Max Product, Block Swap, Moore's)  │
│ 01:45 - 02:00  │ Chapter 5: Puzzles & 10-Minute Formula Cheat Sheet           │
└───────────────────────────────────────────────────────────────────────────────┘
```

---

# 🔰 Chapter 0: Java & Complexity Foundations (For Absolute Beginners)

### 1. What is Time & Space Complexity? (The Restaurant Analogy)
- **Time Complexity**: How much **longer** a program takes when you give it more data ($n$).
  - $O(1)$ (*Constant*): Instant. Like ordering a glass of tap water. (Takes 5 seconds whether the restaurant has 1 customer or 1,000).
  - $O(\log n)$ (*Logarithmic*): Super fast. Like looking up a name in a sorted phonebook by dividing it in half repeatedly.
  - $O(n)$ (*Linear*): Checking every item once. Like a waiter serving $n$ tables one by one.
  - $O(n \log n)$ (*Log-linear*): Standard efficient sorting (Merge Sort, Quick Sort).
  - $O(n^2)$ (*Quadratic*): Nested loops. Every customer shakes hands with every other customer.
  - $O(2^n)$ (*Exponential*): Dangerously slow (Naive recursive Fibonacci).
- **Space Complexity**: The total memory an algorithm uses.
  $$\text{Total Space} = \text{Fixed Space (code variables)} + \text{Auxiliary Space (extra arrays, call stacks)}$$

### 2. Big-O Cheat Table
| Notation | Name | 10 Elements | 1,000 Elements | 1,000,000 Elements |
|:---:|:---:|:---:|:---:|:---:|
| $O(1)$ | Constant | 1 step | 1 step | 1 step |
| $O(\log n)$ | Logarithmic | ~3 steps | ~10 steps | ~20 steps |
| $O(n)$ | Linear | 10 steps | 1,000 steps | 1,000,000 steps |
| $O(n^2)$ | Quadratic | 100 steps | 1,000,000 steps | $10^{12}$ (Crash!) |

---

# 📘 Chapter 1: Loop Complexity & Basic Logic

## 1.1 Characteristics of a Good Algorithm
*(Slot S-I — Q1 [10 Marks])*

Every good algorithm must satisfy 7 core properties:
1. **Unambiguous / Definiteness**: Every single step is clear and has only one meaning.
2. **Finiteness**: It must stop after a finite number of steps (no infinite loops).
3. **Input**: Takes 0 or more well-defined inputs.
4. **Output**: Produces at least 1 well-defined output matching the requirement.
5. **Feasibility / Effectiveness**: Every instruction must be basic enough to execute on real hardware.
6. **Correctness**: Delivers correct results for all valid inputs and edge cases.
7. **Generality**: Independent of any specific programming language syntax.

---

## 1.2 Loop Complexity Analysis: Nested vs Sequential Loops
*(Slot S-III Q5(a), Slot S-1 Q5(a), Sample Paper Q1)*

### **Case A: Inner Loop Runs Up to Outer Index ($i=1 \dots n, j=1 \dots i$)**
```java
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
        // O(1) statement
    }
}
```
- **Derivation**:
  $$\text{Total Steps} = 1 + 2 + 3 + \dots + n = \frac{n(n + 1)}{2} = \frac{n^2 + n}{2} = \mathcal{O}(n^2)$$

### **Case B: Two Independent Sequential Loops**
```java
for (int i = 1; i <= n; i++) { /* O(1) */ } // Takes n steps
for (int j = 1; j <= n; j++) { /* O(1) */ } // Takes n steps
```
- **Derivation**:
  $$\text{Total Steps} = n + n = 2n = \mathcal{O}(n)$$

---

## 1.3 Prime Numbers in a Range: Naive $O(n^2)$ vs Optimized $O(n\sqrt{n})$
*(Assignment 1 — Q1, Sample Paper — Q2)*

```
[Is 25 Prime?]
Naive:      Test 2, 3, 4, 5, 6, 7, 8, ... up to 24  (23 divisions) 🐢
Optimized:  Test 2, 3, 4, 5  (only up to √25 = 5!)     (4 divisions) ⚡
```

### **Java Implementation**:
```java
import java.util.Scanner;

public class PrimeRangeComparison {
    // 1. Naive Approach: O(n^2) time complexity
    public static void printPrimesNaive(int start, int end) {
        System.out.print("Naive O(n^2): ");
        for (int i = start; i <= end; i++) {
            if (i <= 1) continue;
            boolean isPrime = true;
            for (int j = 2; j < i; j++) { // Checks every number up to i - 1
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) System.out.print(i + " ");
        }
        System.out.println();
    }

    // 2. Optimized Approach: O(n * sqrt(n))
    public static void printPrimesOptimized(int start, int end) {
        System.out.print("Optimized O(n*sqrt(n)): ");
        for (int i = start; i <= end; i++) {
            if (i <= 1) continue;
            boolean isPrime = true;
            for (int j = 2; j * j <= i; j++) { // Only checks up to sqrt(i)
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) System.out.print(i + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int start = 10, end = 50;
        printPrimesNaive(start, end);
        printPrimesOptimized(start, end);
    }
}
```

---

## 1.4 Fibonacci Series (Recursive vs Iterative)
*(Assignment 1 — Q2)*

- **Recursive Relation**: $F(n) = F(n-1) + F(n-2)$ with base cases $F(0)=0, F(1)=1$.
- **Time Complexity of Recursive**: $\mathcal{O}(2^n)$ (each call splits into 2 calls like a binary tree).
- **Time Complexity of Iterative**: $\mathcal{O}(n)$ with $\mathcal{O}(1)$ space.

```java
public class FibonacciMaster {
    // Recursive: O(2^n) time, O(n) call-stack space
    public static int fibRecursive(int n) {
        if (n <= 0) return 0;
        if (n == 1) return 1;
        return fibRecursive(n - 1) + fibRecursive(n - 2);
    }

    // Iterative: O(n) time, O(1) space
    public static void printFibIterative(int terms) {
        int a = 0, b = 1;
        for (int i = 0; i < terms; i++) {
            System.out.print(a + " ");
            int next = a + b;
            a = b;
            b = next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int n = 10;
        System.out.print("Recursive: ");
        for (int i = 0; i < n; i++) System.out.print(fibRecursive(i) + " ");
        System.out.println();
        System.out.print("Iterative: ");
        printFibIterative(n);
    }
}
```

---

## 1.5 Break vs Continue (Divisible by 3 or 5, but NOT both)
*(Slot S-1 — Q1 [10 Marks])*

- **`break`**: Immediately kills the loop.
- **`continue`**: Skips the rest of the current iteration and jumps to the next turn.

```java
public class DivisibleThreeOrFive {
    public static void main(String[] args) {
        System.out.println("Numbers 1-100 divisible by 3 or 5, but NOT both:");
        for (int i = 1; i <= 100; i++) {
            boolean div3 = (i % 3 == 0);
            boolean div5 = (i % 5 == 0);

            // If divisible by both 3 and 5 (i.e., 15, 30, 45...) -> SKIP IT!
            if (div3 && div5) {
                continue;
            }

            // If divisible by either 3 OR 5
            if (div3 || div5) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }
}
```

---

# 🔢 Chapter 2: Number Theory & Fast Multiplication

## 2.1 Simple Sieve of Eratosthenes
*(Slot S-I Q2, Slot S-1 Q2, CAT 1 Master Q1)*

### **The Concept (ELI5)**:
Instead of testing whether every number is prime, make a list of numbers from $2$ to $N$. Start with the first prime ($2$), and cross off all its multiples ($4, 6, 8, \dots$). Move to the next uncrossed number ($3$) and cross off its multiples ($9, 12, \dots$). What remains uncrossed are prime numbers!

```
[2]  3  [4]  5  [6]  7  [8]  9  [10] 11 [12] 13 [14] 15 [16] 17 [18] 19 [20]
Multiples of 2 crossed out! Next do 3, starting from 3*3 = 9...
```

### **Mathematical Derivation of $\mathcal{O}(N \log \log N)$**:
Marking multiples of $2$ takes $N/2$ steps, multiples of $3$ takes $N/3$ steps, and so on:
$$\text{Total Steps} = N \left( \frac{1}{2} + \frac{1}{3} + \frac{1}{5} + \frac{1}{7} + \dots \right) = N \sum_{p \le N} \frac{1}{p}$$
By **Mertens' Second Theorem**, $\sum_{p \le N} \frac{1}{p} = \ln(\ln N) + M$.  
Therefore, the **Time Complexity is $\mathcal{O}(N \log \log N)$** and **Space Complexity is $\mathcal{O}(N)$**.

### **Java Code for Range $[L, R]$**:
```java
import java.util.Arrays;

public class SimpleSieve {
    public static void sieveRange(int L, int R) {
        boolean[] isPrime = new boolean[R + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        if (R >= 1) isPrime[1] = false;

        // Start crossing off from p * p
        for (int p = 2; p * p <= R; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i <= R; i += p) {
                    isPrime[i] = false;
                }
            }
        }

        System.out.println("Primes between " + L + " and " + R + ":");
        for (int i = Math.max(2, L); i <= R; i++) {
            if (isPrime[i]) System.out.print(i + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Slot S-1 PYQ: Primes between 50 and 120
        sieveRange(50, 120);
        // Output: 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113
    }
}
```

---

## 2.2 Segmented Sieve of Eratosthenes (For Large $R \le 10^9$)
*(CAT 1 Master — Q1(b) [6 Marks])*

### **Why is Segmented Sieve Needed?**
If $R = 10^9$, allocating `boolean[10^9]` requires **$1 \text{ GB}$ of memory**, crashing Java with an `OutOfMemoryError`.  
**Solution**:
1. Find all primes up to $\sqrt{R} = \sqrt{10^9} \approx 31,622$ using simple sieve.
2. Create a tiny array of size $(R - L + 1)$ for the range $[L, R]$ (e.g., $10^5$ items $= 100 \text{ KB}$).
3. Use the small primes to mark composites in $[L, R]$ by mapping index $j$ to `isPrime[j - L]`.
4. **Space Complexity reduced from $\mathcal{O}(R)$ to $\mathcal{O}(\sqrt{R} + (R - L))$!**

### **Java Implementation**:
```java
import java.util.*;

public class SegmentedSieveMaster {
    public static void segmentedSieve(long L, long R) {
        int limit = (int) Math.sqrt(R);
        // Step 1: Standard sieve up to sqrt(R)
        boolean[] mark = new boolean[limit + 1];
        Arrays.fill(mark, true);
        List<Integer> primes = new ArrayList<>();
        for (int p = 2; p * p <= limit; p++) {
            if (mark[p]) {
                for (int i = p * p; i <= limit; i += p) mark[i] = false;
            }
        }
        for (int p = 2; p <= limit; p++) {
            if (mark[p]) primes.add(p);
        }

        // Step 2: Sieve only the segment [L, R]
        int rangeSize = (int) (R - L + 1);
        boolean[] isPrime = new boolean[rangeSize];
        Arrays.fill(isPrime, true);

        for (int p : primes) {
            long start = (L / p) * p;
            if (start < L) start += p;
            if (start == p) start += p; // Don't cross out the prime itself

            for (long j = start; j <= R; j += p) {
                isPrime[(int) (j - L)] = false;
            }
        }

        System.out.println("Primes in range [" + L + ", " + R + "]:");
        for (long i = L; i <= R; i++) {
            if (i > 1 && isPrime[(int) (i - L)]) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {
        segmentedSieve(100, 120);
        // Output: 101 103 107 109 113
    }
}
```

---

## 2.3 Euclidean & Extended Euclidean Algorithm (GCD & $ax + by = \gcd(a, b)$)
*(CAT 1 Master — Q2(a) [5 Marks])*

- **Euclidean GCD**: $\gcd(a, b) = \gcd(b, a \pmod b)$ until $b = 0$. Time Complexity: $\mathcal{O}(\log(\min(a, b)))$.
- **Extended Euclidean**: Computes integer coefficients $x$ and $y$ such that:
  $$a \cdot x + b \cdot y = \gcd(a, b)$$

```java
public class EuclideanMaster {
    // 1. Basic Euclidean GCD
    public static int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    // 2. Extended Euclidean
    static class Result {
        int gcd, x, y;
        Result(int gcd, int x, int y) { this.gcd = gcd; this.x = x; this.y = y; }
    }

    public static Result extendedGCD(int a, int b) {
        if (b == 0) return new Result(a, 1, 0);
        Result r = extendedGCD(b, a % b);
        int x = r.y;
        int y = r.x - (a / b) * r.y;
        return new Result(r.gcd, x, y);
    }

    public static void main(String[] args) {
        int a = 35, b = 15;
        System.out.println("GCD(35, 15) = " + gcd(a, b)); // 5
        Result res = extendedGCD(35, 15);
        System.out.println("Extended: 35*(" + res.x + ") + 15*(" + res.y + ") = " + res.gcd);
        // 35*(1) + 15*(-2) = 5
    }
}
```

---

## 2.4 Chinese Remainder Theorem (CRT) with Hand Trace
*(CAT 1 Master — Q2(b) [5 Marks])*

### **Problem Statement**:
Find the smallest positive integer $x$ such that:
$$x \equiv 2 \pmod 3, \quad x \equiv 3 \pmod 5, \quad x \equiv 2 \pmod 7$$

### **Step-by-Step Hand Trace**:
1. **List Given Values**:
   - $a_1 = 2, m_1 = 3$
   - $a_2 = 3, m_2 = 5$
   - $a_3 = 2, m_3 = 7$
2. **Compute Total Modulus $M$**:
   $$M = m_1 \times m_2 \times m_3 = 3 \times 5 \times 7 = \mathbf{105}$$
3. **Compute $M_i = M / m_i$**:
   - $M_1 = 105 / 3 = \mathbf{35}$
   - $M_2 = 105 / 5 = \mathbf{21}$
   - $M_3 = 105 / 7 = \mathbf{15}$
4. **Find Modular Inverses $y_i = M_i^{-1} \pmod{m_i}$**:
   - $35 \pmod 3 \equiv 2 \implies 2 \cdot y_1 \equiv 1 \pmod 3 \implies \mathbf{y_1 = 2}$ (since $2 \times 2 = 4 \equiv 1$)
   - $21 \pmod 5 \equiv 1 \implies 1 \cdot y_2 \equiv 1 \pmod 5 \implies \mathbf{y_2 = 1}$
   - $15 \pmod 7 \equiv 1 \implies 1 \cdot y_3 \equiv 1 \pmod 7 \implies \mathbf{y_3 = 1}$
5. **Apply Formula $x = \left(\sum a_i \times M_i \times y_i\right) \pmod M$**:
   $$x = (2 \times 35 \times 2) + (3 \times 21 \times 1) + (2 \times 15 \times 1) \pmod{105}$$
   $$x = (140 + 63 + 30) \pmod{105} = 233 \pmod{105} = \mathbf{23}$$

**Verification**:
- $23 \pmod 3 = 2$ ✅
- $23 \pmod 5 = 3$ ✅
- $23 \pmod 7 = 2$ ✅

---

## 2.5 Euler's Totient Function $\phi(n)$ (Computation for $\phi(84)$ & $\phi(24)$)
*(Slot S-III — Q2 [10 Marks])*

### **What is $\phi(n)$?**
$\phi(n)$ counts how many integers from $1$ to $n$ have $\gcd(x, n) = 1$ (coprime to $n$).

### **Formula**:
$$\phi(n) = n \times \prod_{p | n} \left(1 - \frac{1}{p}\right)$$

### **Hand Calculations**:
1. **For $n = 84$**:
   - Prime factors: $84 = 2^2 \times 3^1 \times 7^1 \implies p \in \{2, 3, 7\}$
   $$\phi(84) = 84 \times \left(1 - \frac{1}{2}\right) \times \left(1 - \frac{1}{3}\right) \times \left(1 - \frac{1}{7}\right) = 84 \times \frac{1}{2} \times \frac{2}{3} \times \frac{6}{7} = \mathbf{24}$$
2. **For $n = 24$**:
   - Prime factors: $24 = 2^3 \times 3^1 \implies p \in \{2, 3\}$
   $$\phi(24) = 24 \times \left(1 - \frac{1}{2}\right) \times \left(1 - \frac{1}{3}\right) = 24 \times \frac{1}{2} \times \frac{2}{3} = \mathbf{8}$$

```java
public class EulerTotientMaster {
    public static int phi(int n) {
        int result = n;
        for (int p = 2; p * p <= n; p++) {
            if (n % p == 0) {
                while (n % p == 0) n /= p; // Remove all multiples of p
                result -= result / p;      // result = result * (1 - 1/p)
            }
        }
        if (n > 1) { // If remaining n is prime
            result -= result / n;
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println("phi(84) = " + phi(84)); // Output: 24
        System.out.println("phi(24) = " + phi(24)); // Output: 8
    }
}
```

---

## 2.6 Karatsuba Fast Multiplication Algorithm (Recurrence & Trace of $1234 \times 5678$)
*(CAT 1 Master — Q5 [10 Marks])*

### **1. Divide & Conquer Recurrence Relation**:
Standard multiplication takes 4 products: $T(n) = 4T(n/2) + \mathcal{O}(n) = \mathcal{O}(n^2)$.  
Karatsuba reduces it to **3 multiplications**:
$$T(n) = 3T(n/2) + \mathcal{O}(n)$$
By Master Theorem ($a = 3, b = 2$):
$$\text{Time Complexity} = \mathcal{O}\left(n^{\log_2 3}\right) \approx \mathbf{\mathcal{O}(n^{1.585})}$$

---

### **2. Hand Trace: Multiply $1234 \times 5678$**:
- Split numbers at $m = 2$:
  - $X = 1234 \implies a = 12, b = 34$
  - $Y = 5678 \implies c = 56, d = 78$
- **Step 1 ($z_2$)**: $a \times c = 12 \times 56 = \mathbf{672}$
- **Step 2 ($z_0$)**: $b \times d = 34 \times 78 = \mathbf{2652}$
- **Step 3**: $(a + b) \times (c + d) = (12 + 34) \times (56 + 78) = 46 \times 134 = \mathbf{6164}$
- **Step 4 ($z_1$)**: $z_1 = 6164 - z_2 - z_0 = 6164 - 672 - 2652 = \mathbf{2840}$
- **Step 5 (Combine)**:
  $$\text{Product} = z_2 \times 10^4 + z_1 \times 10^2 + z_0$$
  $$\text{Product} = 672 \times 10000 + 2840 \times 100 + 2652 = 6,720,000 + 284,000 + 2652 = \mathbf{7,006,652}$$

---

## 2.7 Booth's Multiplication Algorithm
*(L14 Syllabus)*

Multiplies two signed binary numbers using 2's complement.
- Inspect current bit $Q_0$ and previous bit $Q_{-1}$:
  - `00` or `11`: No arithmetic, just **Arithmetic Shift Right (ASR)**.
  - `01`: $A = A + M$, then **ASR**.
  - `10`: $A = A - M$, then **ASR**.

```java
public class BoothsAlgorithm {
    public static int multiply(int m, int q) {
        int a = 0, q_minus_1 = 0;
        int count = 8; // 8-bit integers

        for (int i = 0; i < count; i++) {
            int q0 = q & 1;
            if (q0 == 0 && q_minus_1 == 1) a += m;
            else if (q0 == 1 && q_minus_1 == 0) a -= m;

            // Arithmetic Shift Right [A, Q, Q-1]
            q_minus_1 = q0;
            q = (q >>> 1) | ((a & 1) << (count - 1));
            a = a >> 1;
        }
        return (a << count) | q;
    }

    public static void main(String[] args) {
        System.out.println("-7 * 3 = " + multiply(-7, 3)); // -21
    }
}
```

---

# ⚡ Chapter 3: Bit Manipulation Masterclass

## 3.1 Binary Palindrome Check (Without String Conversion)
*(Assignment 2 — Q1, Sample Paper — Q5(b))*

```java
public class BinaryPalindrome {
    public static boolean isPalindrome(int n) {
        int original = n;
        int reversed = 0;

        // Reverse bits mathematically
        while (n > 0) {
            reversed = (reversed << 1) | (n & 1);
            n = n >> 1;
        }
        return original == reversed;
    }

    public static void main(String[] args) {
        int n = 9; // Binary: 1001 (reads same forwards and backwards)
        System.out.println("9 is binary palindrome: " + isPalindrome(n)); // true
    }
}
```

---

## 3.2 Longest Sequence of 1s After Flipping Exactly One Bit
*(Assignment 2 — Q2, Sample Paper — Q5(a))*

```
Example: 11011101111
Streak before 0: length 3
Streak after 0:  length 4
Flipping the 0 links both streaks: 3 + 4 + 1 = 8 consecutive 1s!
```

```java
public class LongestOnesFlip {
    public static int longestConsecutiveOnes(int n) {
        if (~n == 0) return Integer.BYTES * 8; // All 1s

        int currentLen = 0, previousLen = 0, maxLen = 0;

        while (n != 0) {
            if ((n & 1) == 1) {
                currentLen++;
            } else {
                // If next bit is 0, reset previousLen to 0
                previousLen = ((n & 2) == 0) ? 0 : currentLen;
                currentLen = 0;
            }
            maxLen = Math.max(maxLen, previousLen + currentLen + 1);
            n >>>= 1;
        }
        return maxLen;
    }

    public static void main(String[] args) {
        int n = 0b11011101111;
        System.out.println("Max 1s after 1 flip: " + longestConsecutiveOnes(n)); // Output: 8
    }
}
```

---

## 3.3 Swap Two Nibbles in an 8-bit Byte (Masking, Shifting & Trace for 100)
*(Assignment 2 — Q3, Sample Paper — Q4 [10 Marks])*

### **1. Logic**:
- A byte has 8 bits. A **nibble** is 4 bits: `[Upper Nibble (4 bits) | Lower Nibble (4 bits)]`.
- Mask with `0x0F` (`0000 1111`) to isolate the lower nibble and shift left by 4 (`<< 4`).
- Mask with `0xF0` (`1111 0000`) to isolate the upper nibble and shift right by 4 (`>> 4`).
- Combine with bitwise OR (`|`).

---

### **2. Hand Trace for Input $100$**:
1. Decimal $100$ in binary: `0110 0100` ($64 + 32 + 4 = 100$).
2. **Extract Lower Nibble**: `0110 0100 & 0000 1111 = 0000 0100` (value 4).
3. **Shift Left by 4**: `0000 0100 << 4 = 0100 0000` (value 64).
4. **Extract Upper Nibble**: `0110 0100 & 1111 0000 = 0110 0000` (value 96).
5. **Shift Right by 4**: `0110 0000 >> 4 = 0000 0110` (value 6).
6. **Combine via Bitwise OR**:
   $$0100\ 0000 \mid 0000\ 0110 = \mathbf{0100\ 0110_2} = 64 + 4 + 2 = \mathbf{70_{10}}$$

```java
public class SwapNibblesMaster {
    public static int swapNibbles(int b) {
        return ((b & 0x0F) << 4) | ((b & 0xF0) >> 4);
    }

    public static void main(String[] args) {
        int input = 100;
        System.out.println("Swapped 100 = " + swapNibbles(input)); // Output: 70
    }
}
```

---

## 3.4 Reverse All Bits & 3.5 Count Set Bits
*(Assignment 2 — Q4, Q5)*

```java
public class BitTricksMaster {
    // Reverse all 32 bits
    public static int reverseBits(int n) {
        int rev = 0;
        for (int i = 0; i < 32; i++) {
            rev = (rev << 1) | (n & 1);
            n >>>= 1;
        }
        return rev;
    }

    // Brian Kernighan's Algorithm: O(number of 1s)
    // n & (n - 1) wipes out the lowest set bit in 1 operation!
    public static int countSetBits(int n) {
        int count = 0;
        while (n != 0) {
            n = n & (n - 1);
            count++;
        }
        return count;
    }

    public static void main(String[] args) {
        int n = 13; // Binary: 1101 (3 set bits)
        System.out.println("Set bits in 13: " + countSetBits(n)); // 3
    }
}
```

---

## 3.6 Strobogrammatic Number (Two-Pointer Technique)
*(Slot S-I — Q5(a) [5 Marks])*

A number is **strobogrammatic** if it looks identical upside down ($180^\circ$ rotation).
- Valid pairs: `(0,0), (1,1), (8,8), (6,9), (9,6)`.

```java
import java.util.*;

public class StrobogrammaticMaster {
    public static boolean isStrobogrammatic(String num) {
        Map<Character, Character> map = new HashMap<>();
        map.put('0', '0'); map.put('1', '1'); map.put('8', '8');
        map.put('6', '9'); map.put('9', '6');

        int l = 0, r = num.length() - 1;
        while (l <= r) {
            char leftChar = num.charAt(l);
            char rightChar = num.charAt(r);

            if (!map.containsKey(leftChar) || map.get(leftChar) != rightChar) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println("69 is strobogrammatic: " + isStrobogrammatic("69"));   // true
        System.out.println("88 is strobogrammatic: " + isStrobogrammatic("88"));   // true
        System.out.println("818 is strobogrammatic: " + isStrobogrammatic("818")); // true
        System.out.println("962 is strobogrammatic: " + isStrobogrammatic("962")); // false
    }
}
```

---

# 📊 Chapter 4: Array & Matrix Algorithms

## 4.1 Maximum Product Subarray (Algorithm & Step-by-Step Trace Tables)
*(Slot S-I Q3, Slot S-III Q1, Slot S-1 Q4, CAT 1 Master Q4(c))*

### **Why Kadane's Algorithm needs a tweak**:
A negative number multiplied by a negative number becomes a **huge positive number**. Therefore, we must track **both** `maxSoFar` and `minSoFar` at every step!

```java
public class MaxProductSubarrayMaster {
    public static int maxProduct(int[] nums) {
        int maxSoFar = nums[0];
        int minSoFar = nums[0];
        int result = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int curr = nums[i];
            int tempMax = Math.max(curr, Math.max(maxSoFar * curr, minSoFar * curr));
            minSoFar = Math.min(curr, Math.min(maxSoFar * curr, minSoFar * curr));
            maxSoFar = tempMax;

            result = Math.max(result, maxSoFar);
        }
        return result;
    }
}
```

---

### **Execution Trace Table for `arr = [2, -5, -2, -4, 3]` (Slot S-I Exam Question)**

| Step ($i$) | Element (`curr`) | Calculation for `maxSoFar` | `maxSoFar` | Calculation for `minSoFar` | `minSoFar` | Final `result` |
|:---:|:---:|:---|:---:|:---|:---:|:---:|
| **Init ($i=0$)** | $2$ | Initialized to $2$ | **2** | Initialized to $2$ | **2** | **2** |
| **$i = 1$** | $-5$ | $\max(-5, 2\times(-5), 2\times(-5))$ | **-5** | $\min(-5, 2\times(-5), 2\times(-5))$ | **-10** | $\max(2, -5) = \mathbf{2}$ |
| **$i = 2$** | $-2$ | $\max(-2, -5\times(-2), -10\times(-2))$ | **20** | $\min(-2, -5\times(-2), -10\times(-2))$ | **-2** | $\max(2, 20) = \mathbf{20}$ |
| **$i = 3$** | $-4$ | $\max(-4, 20\times(-4), -2\times(-4))$ | **8** | $\min(-4, 20\times(-4), -2\times(-4))$ | **-80** | $\max(20, 8) = \mathbf{20}$ |
| **$i = 4$** | $3$ | $\max(3, 8\times 3, -80\times 3)$ | **24** | $\min(3, 8\times 3, -80\times 3)$ | **-240** | $\max(20, 24) = \mathbf{24}$ |

**Final Maximum Product**: **$24$** (Subarray: `[-2, -4, 3]`).

---

## 4.2 Block Swap Algorithm for Array Left Rotation ($\mathcal{O}(n)$ Time, $\mathcal{O}(1)$ Space)
*(Slot S-I Q4, Slot S-III Q5(b), Slot S-1 Q5(b) [10 Marks])*

### **The Logic**:
To rotate array $arr$ of size $n$ left by $d$ positions:
Divide $arr$ into $A = arr[0 \dots d-1]$ and $B = arr[d \dots n-1]$.
1. If $|A| == |B|$: Swap $A$ and $B$. Done!
2. If $|A| < |B|$: Divide $B$ into $B_l$ (size $|A|$) and $B_r$. Swap $A$ with $B_r$, then recurse.
3. If $|A| > |B|$: Divide $A$ into $A_l$ and $A_r$ (size $|B|$). Swap $A_l$ with $B$, then recurse.

```java
import java.util.Arrays;

public class BlockSwapMaster {
    public static void swap(int[] arr, int fi, int si, int d) {
        for (int i = 0; i < d; i++) {
            int temp = arr[fi + i];
            arr[fi + i] = arr[si + i];
            arr[si + i] = temp;
        }
    }

    public static void leftRotate(int[] arr, int d, int n) {
        leftRotateRec(arr, 0, d, n);
    }

    private static void leftRotateRec(int[] arr, int i, int d, int n) {
        if (d == 0 || d == n) return;
        if (n - d == d) {
            swap(arr, i, n - d + i, d);
            return;
        }
        if (d < n - d) {
            swap(arr, i, n - d + i, d);
            leftRotateRec(arr, i, d, n - d);
        } else {
            swap(arr, i, d + i, n - d);
            leftRotateRec(arr, n - d + i, 2 * d - n, d);
        }
    }

    public static void main(String[] args) {
        // Slot S-III PYQ: {10, 20, 30, 40, 50, 60, 70, 80} left rotate by 4
        int[] arr1 = {10, 20, 30, 40, 50, 60, 70, 80};
        leftRotate(arr1, 4, arr1.length);
        System.out.println("Rotated by 4: " + Arrays.toString(arr1));
        // Output: [50, 60, 70, 80, 10, 20, 30, 40]

        // Slot S-1 PYQ: {11, 22, 33, 44, 55, 66, 77, 88} left rotate by 3
        int[] arr2 = {11, 22, 33, 44, 55, 66, 77, 88};
        leftRotate(arr2, 3, arr2.length);
        System.out.println("Rotated by 3: " + Arrays.toString(arr2));
        // Output: [44, 55, 66, 77, 88, 11, 22, 33]
    }
}
```

---

## 4.3 Leaders in an Array ($\mathcal{O}(n)$ Time)
*(CAT 1 Master — Q4(a))*

An element is a **Leader** if it is strictly greater than all elements to its right.
- **Trick**: Scan from right to left, keeping track of `maxFromRight`.

```java
import java.util.*;

public class LeadersMaster {
    public static List<Integer> findLeaders(int[] arr) {
        List<Integer> leaders = new ArrayList<>();
        int n = arr.length;
        int maxFromRight = arr[n - 1];
        leaders.add(maxFromRight); // Rightmost element is always a leader

        for (int i = n - 2; i >= 0; i--) {
            if (arr[i] > maxFromRight) {
                maxFromRight = arr[i];
                leaders.add(maxFromRight);
            }
        }
        Collections.reverse(leaders);
        return leaders;
    }

    public static void main(String[] args) {
        int[] arr = {16, 17, 4, 3, 5, 2};
        System.out.println("Leaders: " + findLeaders(arr)); // [17, 5, 2]
    }
}
```

---

## 4.4 Majority Element (Moore's Voting Algorithm & Proof)
*(CAT 1 Master — Q4(b))*

Find the element that appears $> \lfloor n/2 \rfloor$ times in $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ space.
- **Intuition**: Different elements cancel each other out in pairs. Since the majority element appears more than half the time, its count will never be completely eliminated.

```java
public class MajorityElementMaster {
    public static int findMajority(int[] nums) {
        int candidate = nums[0], count = 1;

        // Phase 1: Candidate Election
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == candidate) count++;
            else {
                count--;
                if (count == 0) {
                    candidate = nums[i];
                    count = 1;
                }
            }
        }

        // Phase 2: Verification
        int freq = 0;
        for (int num : nums) {
            if (num == candidate) freq++;
        }
        return (freq > nums.length / 2) ? candidate : -1;
    }

    public static void main(String[] args) {
        int[] arr = {2, 2, 1, 1, 1, 2, 2};
        System.out.println("Majority Element: " + findMajority(arr)); // 2
    }
}
```

---

## 4.5 Equilibrium Index
*(Slot S-III — Q4)*

Index where $\text{Sum}(\text{Left elements}) = \text{Sum}(\text{Right elements})$.

```java
public class EquilibriumMaster {
    public static int findEquilibrium(int[] arr) {
        int totalSum = 0;
        for (int x : arr) totalSum += x;

        int leftSum = 0;
        for (int i = 0; i < arr.length; i++) {
            int rightSum = totalSum - leftSum - arr[i];
            if (leftSum == rightSum) return i;
            leftSum += arr[i];
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {-7, 1, 5, 2, -4, 3, 0};
        System.out.println("Equilibrium Index: " + findEquilibrium(arr)); // Index 3 (value 2)
    }
}
```

---

## 4.6 Maximum Hourglass Sum in 2D Matrix ($6 \times 6$)
*(Slot S-III Q3, Sample Paper Q3)*

An hourglass has shape:
```
A B C
  D
E F G
```

```java
public class HourglassMaster {
    public static int maxHourglass(int[][] mat) {
        int maxSum = Integer.MIN_VALUE;
        for (int i = 0; i <= mat.length - 3; i++) {
            for (int j = 0; j <= mat[0].length - 3; j++) {
                int sum = mat[i][j]   + mat[i][j+1]   + mat[i][j+2]
                                      + mat[i+1][j+1]
                        + mat[i+2][j] + mat[i+2][j+1] + mat[i+2][j+2];
                maxSum = Math.max(maxSum, sum);
            }
        }
        return maxSum;
    }

    public static void main(String[] args) {
        int[][] mat = {
            {1, 1, 1, 0, 0, 0},
            {0, 1, 0, 0, 0, 0},
            {1, 1, 1, 0, 0, 0},
            {0, 0, 2, 4, 4, 0},
            {0, 0, 0, 2, 0, 0},
            {0, 0, 1, 2, 4, 0}
        };
        System.out.println("Max Hourglass Sum: " + maxHourglass(mat)); // Output: 19
    }
}
```

---

## 4.7 Quick Sort (Partition Algorithm & Pivot Selection Analysis)
*(Slot S-I Q5(b), Slot S-1 Q3)*

```java
import java.util.Arrays;

public class QuickSortMaster {
    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high]; // Last element as pivot
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;
            }
        }
        int temp = arr[i + 1]; arr[i + 1] = arr[high]; arr[high] = temp;
        return i + 1;
    }

    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    public static void main(String[] args) {
        // Slot S-1 PYQ Array: {72, 18, 54, 11, 39, 26}
        int[] arr = {72, 18, 54, 11, 39, 26};
        quickSort(arr, 0, arr.length - 1);
        System.out.println("Sorted: " + Arrays.toString(arr));
        // Output: [11, 18, 26, 39, 54, 72]
    }
}
```

---

# 🎲 Chapter 5: Classic Puzzles & Game Algorithms

## 5.1 Toggle the Switch (100 Doors & Monkeys)
*(L13 Syllabus)*

### **The Math Proof**:
- Every door $D$ gets toggled by monkey $M$ if $M$ divides $D$.
- Factors come in pairs (e.g., $12 \rightarrow (1,12), (2,6), (3,4) \implies 6$ toggles $\implies$ **Even $\rightarrow$ CLOSED**).
- Only **perfect square numbers** have an odd number of factors (e.g., $16 \rightarrow (1,16), (2,8), (4,4) \implies 5$ toggles $\implies$ **Odd $\rightarrow$ OPEN**).
- For $N = 100$, the open doors are $1^2, 2^2, 3^2, \dots, 10^2 \implies \mathbf{10 \text{ doors open, } 90 \text{ doors closed}}$.

```java
public class ToggleDoorsMaster {
    public static void main(String[] args) {
        int n = 100;
        boolean[] doors = new boolean[n + 1];

        for (int monkey = 1; monkey <= n; monkey++) {
            for (int door = monkey; door <= n; door += monkey) {
                doors[door] = !doors[door];
            }
        }

        System.out.print("Open Doors: ");
        for (int i = 1; i <= n; i++) {
            if (doors[i]) System.out.print(i + " ");
        }
        System.out.println();
    }
}
```

---

## 5.2 Alice Apple Tree
*(L13 Syllabus)*

- Layer $r$ has $12 \times r^2$ apples.
- Perimeter of square of radius $r$ is $8 \times r$.

```java
import java.util.Scanner;

public class AliceAppleMaster {
    public static void main(String[] args) {
        int targetApples = 1000;
        int radius = 0, totalApples = 0;

        while (totalApples < targetApples) {
            radius++;
            totalApples += 12 * radius * radius;
        }
        System.out.println("Minimum Perimeter: " + (8 * radius));
    }
}
```

---

# 🎯 The 10-Minute Last-Minute Exam Formula Cheat Sheet

| Question Pattern | Formula / Core Line of Code | Time Complexity |
|:---|:---|:---:|
| **Swap Nibbles** | `((x & 0x0F) << 4) \| ((x & 0xF0) >> 4)` | $\mathcal{O}(1)$ |
| **Binary Palindrome** | `rev = (rev << 1) \| (n & 1); n >>= 1;` | $\mathcal{O}(\log n)$ |
| **Brian Kernighan** | `n = n & (n - 1); count++;` | $\mathcal{O}(\text{set bits})$ |
| **Euler's Totient** | `result -= result / p;` | $\mathcal{O}(\sqrt{n})$ |
| **Simple Sieve** | `for (int i = p * p; i <= N; i += p) isPrime[i] = false;` | $\mathcal{O}(N \log \log N)$ |
| **Segmented Sieve** | Small sieve up to $\sqrt{R}$, map to $[L, R]$ with `j - L` | $\mathcal{O}(R \log \log R)$ |
| **Karatsuba Recurrence**| $T(n) = 3T(n/2) + \mathcal{O}(n) \implies \mathcal{O}(n^{\log_2 3})$ | $\mathcal{O}(n^{1.585})$ |
| **Max Product Subarray**| Track `tempMax = max(x, max*x, min*x)` & `min = min(x, max*x, min*x)` | $\mathcal{O}(n)$ |
| **Moore's Voting** | Pair cancellation: `if (arr[i] == cand) count++ else count--` | $\mathcal{O}(n)$ |
| **Equilibrium Sum** | `rightSum = totalSum - leftSum - arr[i]` | $\mathcal{O}(n)$ |
| **100 Doors Puzzle** | Only perfect squares ($1, 4, 9, 16 \dots$) remain open | $\mathcal{O}(\sqrt{N})$ |

---

# ⚠️ Top 5 Exam Traps To Avoid!

1. **Simple Sieve Loop Trap**: In Sieve, the inner loop MUST start at `i = p * p`, NOT `i = p + p`.
2. **Swap Nibbles Mask Trap**: `0x0F` is for lower nibble (shift LEFT), `0xF0` is for upper nibble (shift RIGHT).
3. **Max Product Subarray Negative Number Trap**: You MUST save `maxSoFar` in a temporary variable (`tempMax`) before updating `minSoFar`, otherwise `minSoFar` uses the already-modified maximum!
4. **CRT Modulo Multiplicative Inverse Trap**: Verify that $M_i \times y_i \equiv 1 \pmod{m_i}$ before multiplying into the sum.
5. **Bit Reversal Shift Trap**: Use unsigned right shift `>>>` when dealing with bit manipulations to prevent negative sign extension.
