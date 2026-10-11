# 📘 Unit 1: Complexity Analysis & Bit Manipulation Algorithms

---

## 1. Asymptotic Notations & Master Theorem

### 1.1 Asymptotic Notations
* **Big-$O$ ($O$)**: Asymptotic upper bound ($f(n) \le c \cdot g(n)$ for all $n \ge n_0$).
* **Big-$\Omega$ ($\Omega$)**: Asymptotic lower bound ($f(n) \ge c \cdot g(n)$ for all $n \ge n_0$).
* **Big-$\Theta$ ($\Theta$)**: Tight bound ($c_1 g(n) \le f(n) \le c_2 g(n)$ for all $n \ge n_0$).

### 1.2 Master Theorem for Divide-and-Conquer Recurrences
$$T(n) = a T(n/b) + f(n), \quad \text{where } a \ge 1, b > 1$$

Compare $f(n)$ with the watershed threshold $n^{\log_b a}$:
1. **Case 1**: If $f(n) = O(n^{\log_b a - \epsilon})$ for some $\epsilon > 0$:
   $$T(n) = \Theta(n^{\log_b a})$$
   *(Example: Strassen's Matrix Multiplication $T(n) = 7 T(n/2) + O(n^2) \implies \log_2 7 \approx 2.81 > 2 \implies T(n) = \Theta(n^{2.81})$).*
2. **Case 2**: If $f(n) = \Theta(n^{\log_b a} \log^k n)$ for $k \ge 0$:
   $$T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$$
   *(Example: Merge Sort $T(n) = 2 T(n/2) + \Theta(n) \implies \log_2 2 = 1 \implies T(n) = \Theta(n \log n)$).*
3. **Case 3**: If $f(n) = \Omega(n^{\log_b a + \epsilon})$ for $\epsilon > 0$ and $a f(n/b) \le c f(n)$ for $c < 1$:
   $$T(n) = \Theta(f(n))$$

---

## 2. Bitwise Hacks & Algorithmic Recipes

```
+-----------------------------------------------------------------------------------------+
| Operation                              | Bitwise Expression                             |
+----------------------------------------+------------------------------------------------+
| Check if k-th bit is set               | `(n & (1 << k)) != 0`                          |
| Set k-th bit                           | `n | (1 << k)`                                 |
| Clear k-th bit                         | `n & ~(1 << k)`                                |
| Toggle k-th bit                        | `n ^ (1 << k)`                                 |
| Check if power of 2                    | `n > 0 && (n & (n - 1)) == 0`                  |
| Clear lowest set bit                   | `n & (n - 1)`                                  |
| Extract lowest set bit                 | `n & -n`                                       |
| Swap two numbers without temp var      | `a ^= b; b ^= a; a ^= b;`                      |
| Swap two nibbles in a byte             | `((n & 0x0F) << 4) | ((n & 0xF0) >> 4)`        |
+-----------------------------------------------------------------------------------------+
```

### 2.1 Brian Kernighan's Algorithm (Count Set Bits)
Iterates in $O(\text{number of set bits})$ time rather than checking all 32 bits:
```java
public static int countSetBits(int n) {
    int count = 0;
    while (n > 0) {
        n &= (n - 1); // Clears the lowest set bit in each iteration
        count++;
    }
    return count;
}
```

### 2.2 Longest Consecutive 1s After Flipping Exactly One 0
Given a binary integer, find the maximum length of contiguous 1s achievable by flipping at most one 0:
```java
public static int longestSequenceAfterFlip(int n) {
    if (~n == 0) return Integer.BYTES * 8; // All 1s

    int currentLen = 0, prevLen = 0, maxLen = 0;
    while (n != 0) {
        if ((n & 1) == 1) {
            currentLen++;
        } else {
            // Next bit is 0: check if subsequent bit is also 0
            prevLen = ((n & 2) == 0) ? 0 : currentLen;
            currentLen = 0;
        }
        maxLen = Math.max(maxLen, prevLen + currentLen + 1);
        n >>>= 1;
    }
    return maxLen;
}
```

---

## 3. Model Exam Questions & Answers

### Question 1 (12 Marks)
**Solve the recurrence relation $T(n) = 4 T(n/2) + n^2 \log n$ using the Master Theorem. Prove the correctness of the swap nibbles bitwise formula.**

**Solution**:
1. **Recurrence Solution**:
   - $a = 4, b = 2, f(n) = n^2 \log n$.
   - Compute watershed threshold: $n^{\log_b a} = n^{\log_2 4} = n^2$.
   - Comparing $f(n) = n^2 \log^1 n$ with $n^2$:
   - This matches **Master Theorem Case 2** with $k = 1$ ($f(n) = \Theta(n^{\log_b a} \log^k n)$).
   - Solution: $T(n) = \Theta(n^{\log_b a} \log^{k+1} n) = \Theta(n^2 \log^{1+1} n) = \mathbf{\Theta(n^2 \log^2 n)}$.
2. **Proof of Swap Nibbles in an 8-bit Byte**:
   - Let 8-bit byte be represented by two 4-bit nibbles: $N = [H_3 H_2 H_1 H_0 \, L_3 L_2 L_1 L_0]$.
   - Masking with `0x0F` (`0000 1111`) isolates low nibble: $N \ \& \ 0x0F = [0000 \, L_3 L_2 L_1 L_0]$. Left shifting by 4 bits moves it to high nibble: $[L_3 L_2 L_1 L_0 \, 0000]$.
   - Masking with `0xF0` (`1111 0000`) isolates high nibble: $N \ \& \ 0xF0 = [H_3 H_2 H_1 H_0 \, 0000]$. Right shifting by 4 bits moves it to low nibble: $[0000 \, H_3 H_2 H_1 H_0]$.
   - Bitwise OR combines the shifted values:
     $$[L_3 L_2 L_1 L_0 \, 0000] \mid [0000 \, H_3 H_2 H_1 H_0] = [L_3 L_2 L_1 L_0 \, H_3 H_2 H_1 H_0]$$
   - High and low nibbles are successfully swapped.

### Question 2 (8 Marks)
**Write a Java method to check whether an integer has alternating bits (e.g., $5 = 101_2$ is alternating, $7 = 111_2$ is not). Analyze its time and space complexity.**

**Solution**:
```java
public class AlternatingBits {
    public static boolean hasAlternatingBits(int n) {
        // Step 1: XOR n with itself shifted right by 1
        int x = n ^ (n >> 1);
        // If n had alternating bits, x will be of the form 111...1
        // Step 2: Check if x + 1 is a power of 2
        return (x & (x + 1)) == 0;
    }
}
```
* **Complexity**: Time $= O(1)$ (constant CPU bitwise cycles), Auxiliary Space $= O(1)$.
