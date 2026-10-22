# 📘 Unit 2: Number Theory, Prime Sieves, Euler's Totient & Fast Math

> **Aligned with VIT Bhopal October 2026 TEE Papers**: Slots A11, B14, F11, E11  
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

## 3. Euler's Totient Function $\phi(n)$
*(Paper 3 Q1a — 12 Marks)*

Count of integers $k \in [1, n]$ coprime to $n$ ($\gcd(k, n) = 1$):
$$\phi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)$$

```java
public class EulerTotient {
    public static int eulerPhi(int n) {
        int result = n;
        for (int p = 2; p * p <= n; p++) {
            if (n % p == 0) {
                while (n % p == 0) n /= p; // Remove factor p completely
                result -= result / p;      // Equivalent to: result * (1 - 1/p)
            }
        }
        if (n > 1) { // Remaining prime factor
            result -= result / n;
        }
        return result;
    }

    public static void main(String[] args) {
        int n = 360;
        System.out.println("phi(" + n + ") = " + eulerPhi(n)); // 96
    }
}
```
* **Time Complexity**: $O(\sqrt{n})$, **Auxiliary Space**: $O(1)$.

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
