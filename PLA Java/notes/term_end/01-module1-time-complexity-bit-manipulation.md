# 📘 Unit 1: Complexity Analysis & Bit Manipulation Algorithms

---

## 1. Asymptotic Notations & Complexity Analysis

### 1.1 Asymptotic Definitions
* **Big-$O$ ($O$)**: Asymptotic upper bound ($f(n) \le c \cdot g(n)$ for all $n \ge n_0$). Represents worst-case upper ceiling.
* **Big-$\Omega$ ($\Omega$)**: Asymptotic lower bound ($f(n) \ge c \cdot g(n)$ for all $n \ge n_0$). Represents best-case lower floor.
* **Big-$\Theta$ ($\Theta$)**: Tight bound ($c_1 g(n) \le f(n) \le c_2 g(n)$ for all $n \ge n_0$). Algorithm grows at the exact same rate.

### 1.2 Loop Complexity Comparison: $O(n)$ vs $O(n^2)$
*(Directly tested in Sample Paper 1, Q1)*

```java
public class ComplexityDemo {
    // Linear Time O(n): Single loop running n times
    public static int linearSum(int[] arr) {
        int sum = 0;
        for (int x : arr) { // Runs exactly n iterations
            sum += x;
        }
        return sum;
    }

    // Quadratic Time O(n^2): Nested loops comparing every pair
    public static int countInversions(int[] arr) {
        int n = arr.length;
        int invCount = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) { // Total iterations = n*(n-1)/2
                if (arr[i] > arr[j]) invCount++;
            }
        }
        return invCount;
    }

    public static void main(String[] args) {
        int[] data = {8, 4, 2, 1};
        System.out.println("Linear Sum: " + linearSum(data));
        System.out.println("Inversion Count: " + countInversions(data));
    }
}
```
**Sample Input**: `[8, 4, 2, 1]`  
**Sample Output**:
```text
Linear Sum: 15
Inversion Count: 6
```

---

### 1.3 Master Theorem for Divide-and-Conquer Recurrences
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

### 2.1 Swap Two Nibbles in an 8-bit Byte
*(Guaranteed TEE Question — Sample Paper 1, Q4)*

* **Concept**: An 8-bit byte consists of two 4-bit nibbles: high nibble (bits 4–7) and low nibble (bits 0–3).
* **Bitwise Formula**: `((n & 0x0F) << 4) | ((n & 0xF0) >> 4)`

```java
public class SwapNibbles {
    public static int swapNibbles(int n) {
        return ((n & 0x0F) << 4) | ((n & 0xF0) >> 4);
    }

    public static void main(String[] args) {
        int n = 100;
        int swapped = swapNibbles(n);
        System.out.println("Original: " + n + " (" + Integer.toBinaryString(n) + ")");
        System.out.println("Swapped:  " + swapped + " (" + Integer.toBinaryString(swapped) + ")");
    }
}
```
**Sample Input**: `100`  
**Execution Trace**:
- $100_{10} = 0110 \, 0100_2$
- `n & 0x0F` $= 0000 \, 0100_2 \implies$ shift left 4 bits $= 0100 \, 0000_2 = 64$
- `n & 0xF0` $= 0110 \, 0000_2 \implies$ shift right 4 bits $= 0000 \, 0110_2 = 6$
- OR operation $= 0100 \, 0110_2 = 64 + 6 = \mathbf{70_{10}}$

**Sample Output**:
```text
Original: 100 (1100100)
Swapped:  70 (1000110)
```

---

### 2.2 Brian Kernighan's Algorithm (Count Set Bits)
Iterates in $O(\text{set bits})$ time rather than checking all 32 bits:
```java
public class KernighanBits {
    public static int countSetBits(int n) {
        int count = 0;
        while (n > 0) {
            n &= (n - 1); // Clears the lowest set bit in each step
            count++;
        }
        return count;
    }

    public static void main(String[] args) {
        int n = 29; // Binary: 11101 (4 set bits)
        System.out.println("Set bits in " + n + ": " + countSetBits(n));
    }
}
```
**Sample Input**: `29`  
**Sample Output**:
```text
Set bits in 29: 4
```

---

### 2.3 Longest Sequence of 1s After Flipping Exactly One 0
*(Tested in Sample Paper 1, Q5)*

```java
public class LongestConsecutiveOnes {
    public static int longestSequenceAfterFlip(int n) {
        if (~n == 0) return Integer.BYTES * 8; // All 1s

        int currentLen = 0, prevLen = 0, maxLen = 0;
        while (n != 0) {
            if ((n & 1) == 1) {
                currentLen++;
            } else {
                // If the next bit is also 0, previous sequence cannot bridge
                prevLen = ((n & 2) == 0) ? 0 : currentLen;
                currentLen = 0;
            }
            maxLen = Math.max(maxLen, prevLen + currentLen + 1);
            n >>>= 1;
        }
        return maxLen;
    }

    public static void main(String[] args) {
        int n = 1775; // Binary: 11011101111_2
        System.out.println("Max sequence of 1s for " + n + ": " + longestSequenceAfterFlip(n));
    }
}
```
**Sample Input**: `1775` (Binary: `11011101111`)  
**Sample Output**:
```text
Max sequence of 1s for 1775: 8
```
*(Explanation: Flipping the 0 at bit 4 joins sequences of length 3 and 4, producing $3 + 1 + 4 = 8$ contiguous 1s).*

---

### 2.4 Binary Palindrome Check
*(Tested in Sample Paper 1, Q6)*

Check if the binary representation of a number reads the same forwards and backwards:
```java
public class BinaryPalindrome {
    public static boolean isBinaryPalindrome(int n) {
        int rev = 0;
        int temp = n;
        while (temp > 0) {
            rev = (rev << 1) | (temp & 1);
            temp >>= 1;
        }
        return rev == n;
    }

    public static void main(String[] args) {
        int a = 9;  // 1001_2 -> Palindrome
        int b = 10; // 1010_2 -> Not Palindrome
        System.out.println(a + " is palindrome: " + isBinaryPalindrome(a));
        System.out.println(b + " is palindrome: " + isBinaryPalindrome(b));
    }
}
```
**Sample Input**: `9` and `10`  
**Sample Output**:
```text
9 is palindrome: true
10 is palindrome: false
```

---

### 2.5 Maximum $6 \times 6$ Hourglass Sum
*(Tested in Sample Paper 1, Q3)*

In a $6 \times 6$ matrix, an hourglass is defined by 7 values:
```text
a b c
  d
e f g
```
There are $(6-2) \times (6-2) = 16$ possible hourglasses.

```java
public class HourglassMaxSum {
    public static int maxHourglass(int[][] mat) {
        int maxSum = Integer.MIN_VALUE;
        for (int r = 0; r <= 3; r++) {
            for (int c = 0; c <= 3; c++) {
                int sum = mat[r][c] + mat[r][c+1] + mat[r][c+2]
                                    + mat[r+1][c+1]
                        + mat[r+2][c] + mat[r+2][c+1] + mat[r+2][c+2];
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
        System.out.println("Maximum Hourglass Sum: " + maxHourglass(mat));
    }
}
```
**Sample Input**: The $6 \times 6$ matrix above  
**Sample Output**:
```text
Maximum Hourglass Sum: 19
```
*(The bottom-right hourglass: $2+4+4 + 2 + 1+2+4 = 19$).*

---

## 3. High-Yield Unit 1 Exam Question

### Question: Master Theorem Solution
**Solve the recurrence relation $T(n) = 4 T(n/2) + n^2 \log n$.**

1. Identify parameters: $a = 4, b = 2, f(n) = n^2 \log n$.
2. Compute watershed boundary: $n^{\log_b a} = n^{\log_2 4} = n^2$.
3. Compare $f(n)$ with $n^{\log_b a}$:
   $$f(n) = n^2 \log^1 n = \Theta(n^{\log_b a} \log^k n) \quad \text{with } k = 1$$
4. By Master Theorem Case 2:
   $$T(n) = \Theta(n^{\log_b a} \log^{k+1} n) = \Theta(n^2 \log^{1+1} n) = \mathbf{\Theta(n^2 \log^2 n)}$$
