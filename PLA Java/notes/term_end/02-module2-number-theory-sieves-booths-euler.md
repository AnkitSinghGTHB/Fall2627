# 📘 Unit 2: Number Theory, Prime Sieves, Euler's Totient & Booth's Multiplier

---

## 1. Prime Generation: Sieve of Eratosthenes vs Segmented Sieve

### 1.1 Simple Sieve of Eratosthenes ($O(N \log \log N)$)
* Marks all multiples of prime $p$ starting from $p^2$ as composite:
```java
public static boolean[] simpleSieve(int n) {
    boolean[] prime = new boolean[n + 1];
    Arrays.fill(prime, true);
    prime[0] = prime[1] = false;

    for (int p = 2; p * p <= n; p++) {
        if (prime[p]) {
            for (int i = p * p; i <= n; i += p) prime[i] = false;
        }
    }
    return prime;
}
```

### 1.2 Segmented Sieve for Large Ranges $[L, R]$
When $R \le 10^{12}$ and $R - L \le 10^6$, allocating an array of size $R$ throws `OutOfMemoryError`.
* **Method**:
  1. Generate all primes up to $\sqrt{R}$ using Simple Sieve.
  2. Create a boolean array `isPrime` of size $(R - L + 1)$.
  3. For each prime $p \le \sqrt{R}$, find the smallest multiple in range:
     $$\text{firstMultiple} = \max\left(p^2, \left\lceil \frac{L}{p} \right\rceil \times p\right)$$
  4. Mark multiples of $p$ as false in the window. Space complexity reduces to $O(\sqrt{R} + (R - L))$.

---

## 2. Euler's Totient Function $\phi(n)$

Count of integers $k \in [1, n]$ such that $\gcd(k, n) = 1$:

$$\phi(n) = n \prod_{p \mid n} \left( 1 - \frac{1}{p} \right)$$

```java
public static int eulerPhi(int n) {
    int result = n;
    for (int p = 2; p * p <= n; p++) {
        if (n % p == 0) {
            // Found prime factor p
            while (n % p == 0) n /= p;
            result -= result / p; // Equivalent to result * (1 - 1/p)
        }
    }
    if (n > 1) { // If remaining n is prime
        result -= result / n;
    }
    return result;
}
// Time Complexity: O(sqrt(N)), Auxiliary Space: O(1)
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

---

## 4. Strobogrammatic Numbers & Binary Palindromes

* **Strobogrammatic Numbers**: Numbers that appear identical when rotated $180^\circ$.
  - Reversible digit pairs: `(0, 0)`, `(1, 1)`, `(8, 8)`, `(6, 9)`, `(9, 6)`.
* **Binary Palindrome Check**:
```java
public static boolean isBinaryPalindrome(int n) {
    int reversed = 0, temp = n;
    while (temp > 0) {
        reversed = (reversed << 1) | (temp & 1);
        temp >>= 1;
    }
    return reversed == n;
}
```

---

## 5. Model Exam Questions & Answers

### Question 1 (12 Marks)
**Multiply $(7)_{10}$ by $(-5)_{10}$ using Booth's Multiplication Algorithm in 5-bit 2's complement representation. Show each step and register state table.**

**Solution**:
1. **Operands in 5-bit 2's complement**:
   - Multiplicand $M = +7 = 00111_2$. Two's complement $-M = 11001_2$.
   - Multiplier $Q = -5$. $+5 = 00101_2 \implies -5 = 11011_2$.
   - Initial Registers: $A = 00000_2$, $Q = 11011_2$, $Q_{-1} = 0$, $\text{Count} = 5$.
2. **Execution Steps**:
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
3. **Combined 10-bit Output ($[A, Q]$)**:
   $$[11110 \, 11101]_2$$
   - MSB is 1 (Negative result).
   - Magnitude: Take 2's complement: $00001 \, 00010 + 1 = 00001 \, 00011_2 = \mathbf{35_{10}}$.  
   - $\therefore \text{Result} = \mathbf{-35_{10}}$ (Matches $7 \times (-5) = -35$ exactly!).

### Question 2 (8 Marks)
**Compute $\phi(360)$ using Euler's Totient function product formula. Explain its significance in the RSA cryptosystem.**

**Solution**:
1. **Prime Factorization of 360**:
   $$360 = 2^3 \times 3^2 \times 5^1$$
2. **Apply Euler's Totient Formula**:
   $$\phi(360) = 360 \times \left(1 - \frac{1}{2}\right) \times \left(1 - \frac{1}{3}\right) \times \left(1 - \frac{1}{5}\right)$$
   $$= 360 \times \frac{1}{2} \times \frac{2}{3} \times \frac{4}{5} = 360 \times \frac{8}{30} = 12 \times 8 = \mathbf{96}$$
3. **Role in RSA Cryptosystem**:
   - For modulus $n = p \cdot q$ (product of two distinct large primes), $\phi(n) = (p-1)(q-1)$.
   - The private decryption exponent $d$ is derived as the modular multiplicative inverse of public exponent $e$ modulo $\phi(n)$: $e \cdot d \equiv 1 \pmod{\phi(n)}$. Without knowing $\phi(n)$, computing $d$ from public key $(e, n)$ requires factoring $n$, which is computationally intractable.
