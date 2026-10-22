# 📘 Unit 2: Number Theory, Prime Sieves, Euler's Totient & Fast Math

> **Aligned with VIT Bhopal October 2026 TEE Papers**: Slots A11, B14, F11, E11, A21  
> **Unit Weight in TEE**: Exactly 20 Marks (12M in Section A + 8M in Section B)

---

## 1. Strobogrammatic Numbers

A Strobogrammatic number looks identical when rotated $180^\circ$.
* **Reversible Digit Pairs**: `("0", "0")`, `("1", "1")`, `("8", "8")`, `("6", "9")`, `("9", "6")`.

### 1.1 Generate All Strobogrammatic Numbers of Length $N$
*(Paper 1 Q1a — 12 Marks)*

#### Evaluation: Building from Middle Outwards vs Checking Every Number:
1. **Checking Every Number**: Testing all $10^N$ numbers requires generating strings and checking digit pairs, taking $O(N \cdot 10^N)$ time. This is prohibitively slow for $N \ge 6$.
2. **Building from Middle Outwards (Recursive Construction)**:
   - We construct numbers recursively from length $N-2$ to length $N$ by placing matching reversible pairs on both ends.
   - For the outermost pair, **digit `'0'` cannot be used** because numbers cannot have leading zeros (e.g., `"080"` is not a valid 3-digit number; its numerical length is 1).
   - Time Complexity reduces to $O(5^{N/2})$, which is exponentially faster and visits only valid strobogrammatic numbers!

```java
import java.util.*;

public class StrobogrammaticGenerator {
    public static List<String> findStrobogrammatic(int n) {
        return helper(n, n);
    }

    private static List<String> helper(int n, int totalLen) {
        if (n == 0) return new ArrayList<>(Arrays.asList(""));
        if (n == 1) return new ArrayList<>(Arrays.asList("0", "1", "8"));

        List<String> subList = helper(n - 2, totalLen);
        List<String> result = new ArrayList<>();

        for (String s : subList) {
            // Digit '0' cannot be placed at the outermost boundary
            if (n != totalLen) {
                result.add("0" + s + "0");
            }
            result.add("1" + s + "1");
            result.add("8" + s + "8");
            result.add("6" + s + "9");
            result.add("9" + s + "6");
        }
        return result;
    }

    public static void main(String[] args) {
        int n = 3;
        List<String> ans = findStrobogrammatic(n);
        System.out.println("Strobogrammatic numbers of length " + n + ": " + ans);
        System.out.println("Total count: " + ans.size());
    }
}
```
**Sample Input**: $N = 3$  
**Output Produced for $N = 3$**:
```text
Strobogrammatic numbers of length 3: [101, 808, 609, 906, 111, 818, 619, 916, 181, 888, 689, 986]
Total count: 12
```
*(Explanation: Middle single-digit base case provides `["0", "1", "8"]`. Outermost pairs added are `(1,1)`, `(8,8)`, `(6,9)`, `(9,6)`. Total $= 3 \times 4 = 12$ numbers).*

---

## 2. Prime Generation: Simple Sieve vs Segmented Sieve

### 2.1 Simple Sieve of Eratosthenes ($O(N \log \log N)$)
*(Paper 3 Q7 — 8 Marks)*

```java
import java.util.*;

public class SimpleSieve {
    public static List<Integer> simpleSieve(int n) {
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;

        for (int p = 2; p * p <= n; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i <= n; i += p) isPrime[i] = false;
            }
        }

        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) primes.add(i);
        }
        return primes;
    }

    public static void main(String[] args) {
        System.out.println("Primes up to 30: " + simpleSieve(30));
    }
}
```
**Sample Output**:
```text
Primes up to 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

---

### 2.2 Segmented Sieve for Arbitrary Ranges $[L, R]$
*(Paper 4 Q6 — 8 Marks; Priority Topic 11)*

#### Why Segmented Sieve is Preferred over Simple Sieve for Large Ranges:
* **Memory Limitation of Simple Sieve**: When $R = 10^9$, allocating a boolean array of size $10^9$ bytes requires $\approx 1\text{ GB}$ of contiguous memory, throwing a fatal `java.lang.OutOfMemoryError`.
* **Segmented Sieve Advantage**: Any composite number $x \le R$ must have at least one prime factor $p \le \sqrt{R}$. Since $\sqrt{10^9} \approx 31,622$, we only generate base primes up to $31,622$. Then, we allocate an array of size $(R - L + 1) \le 10^6$ (takes only $\approx 1\text{ MB}$ memory) and cross multiples of the base primes!

```java
import java.util.*;

public class SegmentedSieve {
    public static List<Long> segmentedSieve(long L, long R) {
        int limit = (int) Math.sqrt(R);
        // Step 1: Base primes up to sqrt(R)
        boolean[] base = new boolean[limit + 1];
        Arrays.fill(base, true);
        for (int p = 2; p * p <= limit; p++) {
            if (base[p]) {
                for (int i = p * p; i <= limit; i += p) base[i] = false;
            }
        }
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= limit; i++) if (base[i]) primes.add(i);

        // Step 2: Mark non-primes in window [L, R]
        int rangeSize = (int) (R - L + 1);
        boolean[] isPrime = new boolean[rangeSize];
        Arrays.fill(isPrime, true);

        for (int p : primes) {
            long firstMultiple = Math.max((long) p * p, ((L + p - 1) / p) * p);
            for (long j = firstMultiple; j <= R; j += p) {
                isPrime[(int) (j - L)] = false;
            }
        }

        List<Long> result = new ArrayList<>();
        for (long i = L; i <= R; i++) {
            if (i > 1 && isPrime[(int) (i - L)]) result.add(i);
        }
        return result;
    }

    public static void main(String[] args) {
        long L = 10, R = 50;
        System.out.println("Primes in [" + L + ", " + R + "]: " + segmentedSieve(L, R));
    }
}
```
* **Complexity**: Time: $O((R - L + 1) \log \log R + \sqrt{R} \log \log \sqrt{R})$, Auxiliary Space: $O(R - L + 1 + \sqrt{R})$.

---

## 3. Euler's Totient Function $\phi(N)$
*(Paper 3 Q1a & Paper 5 Q1a — 12 Marks)*

Euler's Totient function $\varphi(N)$ counts the number of positive integers $k \in [1, N]$ that are relatively prime (coprime) to $N$, i.e., $\gcd(k, N) = 1$.

---

### 3.1 Comparison of Methods: Prime Factorisation vs Brute-Force Testing

| Criterion | Method A: Brute-Force Testing | Method B: Prime Factorisation |
|:---|:---|:---|
| **Core Idea** | Test $\gcd(k, N) == 1$ for all $k \in [1, N]$ | Express $N = p_1^{a_1} \cdot p_2^{a_2} \dots$ |
| **Formula Used** | Count if Euclidean $\gcd(k, N) == 1$ | $\varphi(N) = N \prod (1 - 1/p)$ |
| **Time Complexity** | $O(N \log N)$ | $O(\sqrt{N})$ |
| **Auxiliary Space** | $O(1)$ | $O(1)$ |
| **Feasibility for $10^{12}$** | **IMPOSSIBLE** ($\approx 4 \times 10^{13}$ operations, $\approx 111$ hours) | **FEASIBLE** ($\approx 10^6$ operations, $< 10\text{ ms}$) |

1. **Method A: Brute-Force GCD Enumeration ($O(N \log N)$)**:
   - Evaluates $\gcd(k, N)$ for every integer $k \in [1, N]$ using the Euclidean algorithm.
   - Euclidean $\gcd$ takes $O(\log(\min(k, N))) = O(\log N)$ steps.
   - Running this over all $N$ candidates yields total time: $\sum_{k=1}^N O(\log N) = \mathbf{O(N \log N)}$.

2. **Method B: Prime Factorisation ($O(\sqrt{N})$)**:
   - Based on Euler’s product formula. If $N = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$:
     $$\varphi(N) = N \prod_{p \mid N} \left(1 - \frac{1}{p}\right) = N \prod_{p \mid N} \frac{p - 1}{p}$$
   - Any composite integer $N$ has at most one prime factor greater than $\sqrt{N}$.
   - We trial-divide $N$ by all candidate primes $p \le \sqrt{N}$. When a prime factor $p$ divides $N$, we remove all occurrences of $p$ (`while (n % p == 0) n /= p`) and multiply our accumulator by $(1 - 1/p)$.
   - After testing all $p \le \sqrt{N}$, if the remaining $N > 1$, it is a prime factor and we apply $(1 - 1/N)$.
   - Time Complexity is bounded strictly by the loop running up to $\sqrt{N} \implies \mathbf{O(\sqrt{N})}$.

---

### 3.2 Computation of $\varphi(36)$ Using Both Methods

#### Method A: Brute-Force GCD Enumeration on $[1, 36]$
Testing $\gcd(k, 36) = 1$ for all integers from $1$ to $36$:
- **Coprime Elements ($\gcd(k, 36) = 1$)**:
  $$\mathbf{\{1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35\}}$$
- **Non-Coprime Elements** (share factors 2 or 3 with 36):
  $$\{2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 26, 27, 28, 30, 32, 33, 34, 36\}$$
- **Total Coprime Count**: **`12`**.

#### Method B: Prime Factorisation Formula
1. Find distinct prime factors of $36$:
   $$36 = 4 \times 9 = 2^2 \times 3^2 \implies \text{Distinct prime factors are } p_1 = 2, \, p_2 = 3$$
2. Substitute into Euler's product formula:
   $$\varphi(36) = 36 \times \left(1 - \frac{1}{2}\right) \times \left(1 - \frac{1}{3}\right) = 36 \times \frac{1}{2} \times \frac{2}{3} = 36 \times \frac{1}{3} = \mathbf{12}$$

Both methods yield identical results: $\mathbf{\varphi(36) = 12}$.

---

### 3.3 Computational Feasibility Proof for $N \le 10^{12}$

Consider evaluating $\varphi(N)$ for $N = 10^{12}$ on standard computer hardware executing $\approx 10^8$ operations per second:

1. **Brute-Force Approach ($O(N \log N)$)**:
   - Number of Operations:
     $$10^{12} \times \log_2(10^{12}) \approx 10^{12} \times 40 = \mathbf{4 \times 10^{13}\text{ operations}}$$
   - Estimated Wall-Clock Execution Time:
     $$T = \frac{4 \times 10^{13}\text{ operations}}{10^8\text{ ops/sec}} = 400,000\text{ seconds} \approx \mathbf{111.1\text{ hours (over 4.6 days!)}}$$
   - **Verdict**: Completely infeasible. Fails timeout limits ($1.0\text{ s}$) exponentially.

2. **Prime Factorisation Approach ($O(\sqrt{N})$)**:
   - Number of Operations:
     $$\sqrt{N} = \sqrt{10^{12}} = \mathbf{10^6\text{ operations}}$$
   - Estimated Wall-Clock Execution Time:
     $$T = \frac{10^6\text{ operations}}{10^8\text{ ops/sec}} = 0.01\text{ seconds} = \mathbf{10\text{ milliseconds!}}$$
   - **Verdict**: Highly efficient and well within the 1.0-second execution envelope.
   - **Conclusion**: Prime factorisation is **mandatory** for large $N \le 10^{12}$.

---

### 3.4 Complete Java Implementation (Both Methods)

```java
import java.util.*;

public class EulerTotientComparison {
    // Method A: Brute-Force O(N log N)
    public static int gcd(int a, int b) {
        while (b != 0) {
            int t = b;
            b = a % b;
            a = t;
        }
        return a;
    }

    public static int eulerPhiBruteForce(int n, List<Integer> coprimes) {
        int count = 0;
        for (int k = 1; k <= n; k++) {
            if (gcd(k, n) == 1) {
                count++;
                if (coprimes != null) coprimes.add(k);
            }
        }
        return count;
    }

    // Method B: Prime Factorisation O(sqrt(N))
    public static long eulerPhiFactorisation(long n) {
        long result = n;
        for (long p = 2; p * p <= n; p++) {
            if (n % p == 0) {
                while (n % p == 0) n /= p; // Remove all multiples of prime factor p
                result -= result / p;      // Multiply result by (1 - 1/p)
            }
        }
        if (n > 1) { // Remaining prime factor greater than sqrt(N)
            result -= result / n;
        }
        return result;
    }

    public static void main(String[] args) {
        int n = 36;
        List<Integer> coprimes = new ArrayList<>();
        int ansBrute = eulerPhiBruteForce(n, coprimes);
        long ansFactor = eulerPhiFactorisation(n);

        System.out.println("=== Euler's Totient for N = " + n + " ===");
        System.out.println("Method A (Brute-Force): " + ansBrute);
        System.out.println("Coprime Set: " + coprimes);
        System.out.println("Method B (Factorisation): " + ansFactor);

        // Verification for large N = 10^12
        long largeN = 1000000000000L;
        long startTime = System.nanoTime();
        long ansLarge = eulerPhiFactorisation(largeN);
        long duration = (System.nanoTime() - startTime) / 1000000;
        System.out.println("\n=== Large N = 10^12 Test ===");
        System.out.println("phi(10^12) = " + ansLarge + " (Computed in " + duration + " ms)");
    }
}
```

**Sample Output**:
```text
=== Euler's Totient for N = 36 ===
Method A (Brute-Force): 12
Coprime Set: [1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35]
Method B (Factorisation): 12

=== Large N = 10^12 Test ===
phi(10^12) = 400000000000 (Computed in 2 ms)
```

---

## 4. Binary Palindromes & Next Binary Palindrome

### 4.1 Smallest Binary Palindrome Strictly Greater than $N$
*(Paper 1 Q2a — 7 Marks)*

```java
public class NextBinaryPalindrome {
    public static boolean isBinaryPalindrome(int n) {
        int rev = 0, temp = n;
        while (temp > 0) {
            rev = (rev << 1) | (temp & 1);
            temp >>= 1;
        }
        return rev == n;
    }

    public static int findNext(int n) {
        int candidate = n + 1;
        while (!isBinaryPalindrome(candidate)) {
            candidate++;
        }
        return candidate;
    }

    public static void main(String[] args) {
        int n = 25;
        System.out.println("Next binary palindrome after " + n + ": " + findNext(n));
    }
}
```
**Sample Input**: $N = 25$  
**Execution Trace**:
- $25_{10} = 11001_2$ (Reverse $= 10011_2 \ne 11001_2 \implies$ Not palindrome).
- $26_{10} = 11010_2$ (Reverse $= 01011_2 \implies$ Not palindrome).
- $27_{10} = 11011_2$ (Reverse $= 11011_2 \implies$ **Binary Palindrome!**).  
**Sample Output**:
```text
Next binary palindrome after 25: 27
```

---

## 5. Equilibrium Index & Maximum Equilibrium Sum
*(Paper 4 Q2a/b — 12 Marks; Priority Topic 2)*

An index $i$ is an **Equilibrium Index** if:
$$\sum_{j=0}^{i-1} A[j] = \sum_{j=i+1}^{n-1} A[j]$$

```java
public class EquilibriumIndex {
    public static int findMaxEquilibriumSum(int[] arr) {
        int totalSum = 0;
        for (int x : arr) totalSum += x;

        int leftSum = 0;
        int maxEquilibriumSum = Integer.MIN_VALUE;
        int bestIndex = -1;

        for (int i = 0; i < arr.length; i++) {
            int rightSum = totalSum - leftSum - arr[i];
            if (leftSum == rightSum) {
                if (leftSum > maxEquilibriumSum) {
                    maxEquilibriumSum = leftSum;
                    bestIndex = i;
                }
            }
            leftSum += arr[i];
        }

        System.out.println("Best Equilibrium Index: " + bestIndex);
        return maxEquilibriumSum;
    }

    public static void main(String[] args) {
        int[] arr = {-7, 1, 5, 2, -4, 3, 0};
        System.out.println("Max Equilibrium Sum: " + findMaxEquilibriumSum(arr));
    }
}
```

#### Step-by-Step Trace for $\{-7, 1, 5, 2, -4, 3, 0\}$:
- Total Sum $= -7 + 1 + 5 + 2 + (-4) + 3 + 0 = \mathbf{-0} = \mathbf{0}$.

| Index $i$ | Element $A[i]$ | Left Sum | Right Sum (`total - left - A[i]`) | Equilibrium? |
|:---:|:---:|:---:|:---:|:---:|
| 0 | -7 | 0 | $0 - 0 - (-7) = 7$ | No |
| 1 | 1 | -7 | $0 - (-7) - 1 = 6$ | No |
| 2 | 5 | -6 | $0 - (-6) - 5 = 1$ | No |
| **3** | **2** | **-1** | **$0 - (-1) - 2 = -1$** | **YES! (Sum = -1)** |
| 4 | -4 | 1 | $0 - 1 - (-4) = 3$ | No |
| 5 | 3 | -3 | $0 - (-3) - 3 = 0$ | No |
| **6** | **0** | **0** | **$0 - 0 - 0 = 0$** | **YES! (Sum = 0)** |

* **Equilibrium Indices**: Index 3 (Sum = -1) and Index 6 (Sum = 0).
* **Maximum Equilibrium Sum**: $\mathbf{0}$ at Index 6.
* **Complexity**: Time: $O(N)$ (single pass), Auxiliary Space: $O(1)$.

---

## 6. Armstrong Numbers Between $m$ and $n$
*(Paper 4 Q1b-i — 6 Marks)*

An $n$-digit integer is an Armstrong number if the sum of its digits raised to the power of the number of digits equals the number itself (e.g., $153 = 1^3 + 5^3 + 3^3$).

```java
import java.util.*;

public class ArmstrongNumbers {
    public static boolean isArmstrong(int num) {
        int original = num;
        int digits = String.valueOf(num).length();
        int sum = 0;

        while (num > 0) {
            int digit = num % 10;
            sum += Math.pow(digit, digits);
            num /= 10;
        }
        return sum == original;
    }

    public static List<Integer> getArmstrongBetween(int m, int n) {
        List<Integer> list = new ArrayList<>();
        for (int i = m; i <= n; i++) {
            if (isArmstrong(i)) list.add(i);
        }
        return list;
    }

    public static void main(String[] args) {
        int m = 100, n = 500;
        System.out.println("Armstrong numbers between " + m + " and " + n + ": " + getArmstrongBetween(m, n));
    }
}
```
**Sample Output**:
```text
Armstrong numbers between 100 and 500: [153, 370, 371, 407]
```

---

## 7. Booth's Multiplication Algorithm for Signed Binary
*(Syllabus Model — 12 Marks)*

Multiplies two signed integers using registers $[A, Q, Q_{-1}]$ and Arithmetic Shift Right (ASR):
* `Q_0 Q_{-1} = 10` $\implies A = A - M$, then ASR.
* `Q_0 Q_{-1} = 01` $\implies A = A + M$, then ASR.
* `00` or `11` $\implies$ ASR directly (Sign bit of $A$ is preserved).
* Fully worked trace for $(7)_{10} \times (-5)_{10}$ yields $[11110 \, 11101]_2 = \mathbf{-35_{10}}$.
