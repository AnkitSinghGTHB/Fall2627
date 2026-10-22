# 📘 Unit 2: Number Theory, Prime Sieves, Euler's Totient & Booth's Multiplier

---

## 1. Prime Generation: Sieve of Eratosthenes vs Segmented Sieve

### 1.1 Simple Sieve of Eratosthenes vs Trial Division
*(Tested in Sample Paper 1, Q2)*

| Feature | Trial Division | Sieve of Eratosthenes | Segmented Sieve |
|:---|:---|:---|:---|
| **Time Complexity** | $O(N \sqrt{N})$ for $1 \dots N$ | $O(N \log \log N)$ | $O((R - L + 1) \log \log R)$ |
| **Space Complexity**| $O(1)$ | $O(N)$ boolean array | $O(\sqrt{R} + (R - L + 1))$ |
| **Best Used For** | Checking a single number $N$ | Generating primes up to $10^7$ | Range $[L, R]$ where $R \le 10^{12}$ |

```java
import java.util.*;

public class SimpleSieve {
    public static List<Integer> simpleSieve(int n) {
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;

        for (int p = 2; p * p <= n; p++) {
            if (isPrime[p]) {
                // Mark multiples of p starting from p * p
                for (int i = p * p; i <= n; i += p) {
                    isPrime[i] = false;
                }
            }
        }

        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) primes.add(i);
        }
        return primes;
    }

    public static void main(String[] args) {
        int n = 30;
        System.out.println("Primes up to " + n + ": " + simpleSieve(n));
    }
}
```
**Sample Input**: `30`  
**Sample Output**:
```text
Primes up to 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

---

### 1.2 Segmented Sieve for Arbitrary Ranges $[L, R]$
*(Tested in Priority Topic 11 & PPT L8)*

When $R \le 10^{12}$ and $R - L \le 10^6$, allocating an array of size $R$ throws `OutOfMemoryError`. Segmented Sieve allocates only $O(R - L + 1)$ memory:

```java
import java.util.*;

public class SegmentedSieve {
    // Helper: Standard sieve up to sqrt(R)
    public static List<Integer> getBasePrimes(int limit) {
        boolean[] isPrime = new boolean[limit + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;
        for (int p = 2; p * p <= limit; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i <= limit; i += p) isPrime[i] = false;
            }
        }
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= limit; i++) {
            if (isPrime[i]) primes.add(i);
        }
        return primes;
    }

    // Segmented Sieve in range [L, R]
    public static List<Long> segmentedSieve(long L, long R) {
        int limit = (int) Math.sqrt(R);
        List<Integer> basePrimes = getBasePrimes(limit);

        int rangeSize = (int) (R - L + 1);
        boolean[] isPrime = new boolean[rangeSize];
        Arrays.fill(isPrime, true);

        for (int p : basePrimes) {
            // Find lowest multiple of p that is >= L
            long firstMultiple = Math.max((long) p * p, ((L + p - 1) / p) * p);
            for (long j = firstMultiple; j <= R; j += p) {
                isPrime[(int) (j - L)] = false;
            }
        }

        List<Long> result = new ArrayList<>();
        for (long i = L; i <= R; i++) {
            if (i > 1 && isPrime[(int) (i - L)]) {
                result.add(i);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        long L = 10, R = 50;
        System.out.println("Primes in [" + L + ", " + R + "]: " + segmentedSieve(L, R));
    }
}
```
**Sample Input**: `L = 10, R = 50`  
**Sample Output**:
```text
Primes in [10, 50]: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

---

## 2. Euler's Totient Function $\phi(n)$

Count of integers $k \in [1, n]$ such that $\gcd(k, n) = 1$:

$$\phi(n) = n \prod_{p \mid n} \left( 1 - \frac{1}{p} \right)$$

```java
public class EulerTotient {
    public static int eulerPhi(int n) {
        int result = n;
        for (int p = 2; p * p <= n; p++) {
            if (n % p == 0) {
                while (n % p == 0) n /= p; // Remove all factors of prime p
                result -= result / p;      // Equivalent to: result * (1 - 1/p)
            }
        }
        if (n > 1) { // Remaining n is a prime factor
            result -= result / n;
        }
        return result;
    }

    public static void main(String[] args) {
        int n = 360;
        System.out.println("phi(" + n + ") = " + eulerPhi(n));
    }
}
// Time Complexity: O(sqrt(n)), Auxiliary Space: O(1)
```
**Sample Input**: `360`  
**Sample Output**:
```text
phi(360) = 96
```

---

## 3. Booth's Multiplication Algorithm for Signed Binary

Multiplies two signed 2's complement integers using hardware registers:
* **Accumulator ($A$)**, **Multiplier ($Q$)**, **Auxiliary bit ($Q_{-1}$)**, **Multiplicand ($M$)**.

```
+-----------------------------------------------------------------------------------------+
| Bits [Q_0, Q_{-1}] | Operation                                                         |
+--------------------+-------------------------------------------------------------------+
| **`10`**           | $A \leftarrow A - M$, then Arithmetic Shift Right (ASR)           |
| **`01`**           | $A \leftarrow A + M$, then Arithmetic Shift Right (ASR)           |
| **`00`** or **`11`**| No arithmetic; Perform Arithmetic Shift Right (ASR) directly     |
+-----------------------------------------------------------------------------------------+
```
* **Arithmetic Shift Right (ASR)**: Preserves sign bit of $A$ during the right shift ($A_{n-1} \to A_{n-1}$, $A_i \to A_{i-1}$, $A_0 \to Q_{n-1}$, $Q_0 \to Q_{-1}$).

### Fully Worked Example: $(7)_{10} \times (-5)_{10}$ in 5-bit
1. **Representations**:
   - Multiplicand $M = +7 = 00111_2$. Two's complement $-M = 11001_2$.
   - Multiplier $Q = -5 = 11011_2$.
   - Initial Registers: $A = 00000_2$, $Q = 11011_2$, $Q_{-1} = 0$, $\text{Count} = 5$.
2. **Cycle Trace Table**:
   - **Step 1 ($Q_0 Q_{-1} = 10$)**:
     - $A = A - M \implies 00000 + 11001 = 11001$.
     - ASR: $A = 11100, Q = 11101, Q_{-1} = 1$. Count $= 4$.
   - **Step 2 ($Q_0 Q_{-1} = 11$)**:
     - No arithmetic.
     - ASR: $A = 11110, Q = 01110, Q_{-1} = 1$. Count $= 3$.
   - **Step 3 ($Q_0 Q_{-1} = 01$)**:
     - $A = A + M \implies 11110 + 00111 = 00101$.
     - ASR: $A = 00010, Q = 10111, Q_{-1} = 0$. Count $= 2$.
   - **Step 4 ($Q_0 Q_{-1} = 10$)**:
     - $A = A - M \implies 00010 + 11001 = 11011$.
     - ASR: $A = 11101, Q = 11011, Q_{-1} = 1$. Count $= 1$.
   - **Step 5 ($Q_0 Q_{-1} = 11$)**:
     - No arithmetic.
     - ASR: $A = 11110, Q = 11101, Q_{-1} = 1$. Count $= 0$.
3. **Result Register $[A, Q]$**:
   $$[11110 \, 11101]_2$$
   - Since MSB is 1, take 2's complement to get magnitude: $00001 \, 00010 + 1 = 00001 \, 00011_2 = \mathbf{35_{10}}$.
   - $\therefore \text{Final Product} = \mathbf{-35_{10}}$ (Matches $7 \times (-5) = -35$).

---

## 4. Strobogrammatic Numbers

A Strobogrammatic number looks identical when rotated $180^\circ$.
* Valid pairs: `('0','0')`, `('1','1')`, `('8','8')`, `('6','9')`, `('9','6')`.

```java
import java.util.*;

public class Strobogrammatic {
    public static boolean isStrobogrammatic(String num) {
        Map<Character, Character> map = new HashMap<>();
        map.put('0', '0');
        map.put('1', '1');
        map.put('8', '8');
        map.put('6', '9');
        map.put('9', '6');

        int left = 0, right = num.length() - 1;
        while (left <= right) {
            char l = num.charAt(left);
            char r = num.charAt(right);
            if (!map.containsKey(l) || map.get(l) != r) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static void main(String[] args) {
        String[] testCases = {"69", "88", "818", "962"};
        for (String s : testCases) {
            System.out.println(s + " is strobogrammatic: " + isStrobogrammatic(s));
        }
    }
}
```
**Sample Input**: `"69", "88", "818", "962"`  
**Sample Output**:
```text
69 is strobogrammatic: true
88 is strobogrammatic: true
818 is strobogrammatic: true
962 is strobogrammatic: false
```
