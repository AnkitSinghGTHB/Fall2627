# 📘 Unit 1: Complexity Analysis & Bit Manipulation Algorithms

> **Aligned with VIT Bhopal October 2026 TEE Papers**: Slots A11, B14, F11, E11  
> **Unit Weight in TEE**: Exactly 20 Marks (12M in Section A + 8M in Section B)

---

## 1. Asymptotic Notations & Complexity Analysis

### 1.1 Asymptotic Definitions
* **Big-$O$ ($O$)**: Asymptotic upper bound ($f(n) \le c \cdot g(n)$ for all $n \ge n_0$). Worst-case guarantee.
* **Big-$\Omega$ ($\Omega$)**: Asymptotic lower bound ($f(n) \ge c \cdot g(n)$ for all $n \ge n_0$). Best-case floor.
* **Big-$\Theta$ ($\Theta$)**: Tight bound ($c_1 g(n) \le f(n) \le c_2 g(n)$ for all $n \ge n_0$). Precise growth rate.

---

### 1.2 High-Frequency Exam Loop Complexity Traces

#### Loop Pattern A: Halving Double Loop *(Paper 2 Q8 & Paper 3 Q8 — 8 Marks)*
```java
int count = 0;
for (int i = 1; i < n; i = i * 2) {
    for (int j = n; j > 0; j = j / 2) {
        count++;
    }
}
```
* **Analysis**:
  - Outer loop: $i \in \{1, 2, 4, \dots, < n\} \implies \lceil \log_2 n \rceil$ iterations.
  - Inner loop: $j \in \{n, \lfloor n/2 \rfloor, \lfloor n/4 \rfloor, \dots, 1\} \implies (\lfloor \log_2 n \rfloor + 1)$ iterations.
  - Total Operations: $O(\log n) \times O(\log n) = \mathbf{O(\log^2 n)}$. Space: $\mathbf{O(1)}$.
* **Execution Trace for $N = 16$**:
  - Outer values: $i = 1, 2, 4, 8$ (4 iterations).
  - Inner values: $j = 16, 8, 4, 2, 1$ (5 iterations).
  - Cumulative `count` $= 4 \times 5 = \mathbf{20}$.

#### Loop Pattern B: Geometric Inner Bound *(Paper 4 Q1a-ii — 6 Marks)*
```java
for (i = 1; i <= n; i = i * 2)
    for (j = 1; j <= i; j++)
        print(j);
```
* **Analysis & Proof**:
  - Outer variable $i$ takes values $2^0, 2^1, 2^2, \dots, 2^k \le n$.
  - Inner loop executes $i$ times for each outer step.
  - Sum of operations is a geometric series:
    $$\sum_{p=0}^{\lfloor \log_2 n \rfloor} 2^p = 1 + 2 + 4 + 8 + \dots + 2^k = 2^{k+1} - 1 < 2n = \mathbf{O(n)}$$
  - Time Complexity is **$O(n)$ (Linear Time)**, NOT $O(n^2)$ or $O(n \log n)$! Auxiliary Space: $O(1)$.

#### Loop Pattern C: Recursive Fibonacci *(Paper 4 Q1b-ii — 6 Marks)*
```java
int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
```
* **Analysis**:
  - Recurrence: $T(n) = T(n - 1) + T(n - 2) + O(1)$.
  - The recursion generates a binary tree of height $n$ where the number of nodes roughly doubles at each level.
  - Total recursive calls: $2^0 + 2^1 + 2^2 + \dots + 2^n \approx 2^{n+1} - 1 = \mathbf{O(2^n)}$ (Exponential Time).
  - Auxiliary Space: $\mathbf{O(n)}$ due to maximum call stack depth reaching $n$.

---

### 1.3 Binary Search: Complexity & Execution Trace
*(Paper 1 Q1b — 12 Marks)*

```java
public class BinarySearchDemo {
    public static int binarySearch(int a[], int l, int r, int key) {
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (a[mid] == key) return mid;
            else if (a[mid] < key) l = mid + 1;
            else r = mid - 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {2, 5, 8, 12, 16, 23, 38, 45, 56, 72};
        System.out.println("Search 23: " + binarySearch(arr, 0, arr.length - 1, 23));
        System.out.println("Search 50: " + binarySearch(arr, 0, arr.length - 1, 50));
    }
}
```

#### Step-by-Step Execution Traces on Array $\{2, 5, 8, 12, 16, 23, 38, 45, 56, 72\}$:
1. **Searching for Key = 23**:
   - $l=0, r=9 \implies \text{mid} = 4, a[4] = 16 < 23 \implies l = 5$.
   - $l=5, r=9 \implies \text{mid} = 7, a[7] = 45 > 23 \implies r = 6$.
   - $l=5, r=6 \implies \text{mid} = 5, a[5] = 23 == 23 \implies$ **Found at Index 5!**
2. **Searching for Key = 50**:
   - $l=0, r=9 \implies \text{mid} = 4, a[4] = 16 < 50 \implies l = 5$.
   - $l=5, r=9 \implies \text{mid} = 7, a[7] = 45 < 50 \implies l = 8$.
   - $l=8, r=9 \implies \text{mid} = 8, a[8] = 56 > 50 \implies r = 7$.
   - $l = 8 > r = 7 \implies$ Loop ends. **Return -1 (Not Found)**.
* **Complexities**: Best: $O(1)$, Average/Worst: $O(\log n)$. Iterative Space: $O(1)$, Recursive Space: $O(\log n)$.

---

### 1.4 Master Theorem for Divide-and-Conquer Recurrences
$$T(n) = a T(n/b) + f(n), \quad \text{where } a \ge 1, b > 1$$

Compare $f(n)$ with watershed boundary $n^{\log_b a}$:
1. **Case 1**: If $f(n) = O(n^{\log_b a - \epsilon}) \implies T(n) = \Theta(n^{\log_b a})$.
2. **Case 2**: If $f(n) = \Theta(n^{\log_b a} \log^k n) \implies T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$.
   - Example: $T(n) = 4T(n/2) + n^2 \log n \implies n^{\log_2 4} = n^2 \implies T(n) = \mathbf{\Theta(n^2 \log^2 n)}$.
3. **Case 3**: If $f(n) = \Omega(n^{\log_b a + \epsilon}) \implies T(n) = \Theta(f(n))$.

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
*(Guaranteed TEE Question — Appeared in Paper 2 Q2c, Paper 2 Q7, Paper 3 Q7, Paper 4 Q2c)*

```java
public class SwapNibbles {
    public static int swapNibbles(int n) {
        return ((n & 0x0F) << 4) | ((n & 0xF0) >> 4);
    }

    public static void main(String[] args) {
        int n = 100;
        int swapped = swapNibbles(n);
        System.out.println("Before: " + n + " (" + String.format("%8s", Integer.toBinaryString(n)).replace(' ', '0') + ")");
        System.out.println("After:  " + swapped + " (" + String.format("%8s", Integer.toBinaryString(swapped)).replace(' ', '0') + ")");
    }
}
```
**Sample Input**: `100`  
**Execution Trace**:
- $100_{10} = 0110 \, 0100_2$
- `n & 0x0F` isolates low nibble: $0000 \, 0100_2$. Shift left 4 bits: $0100 \, 0000_2 = 64$.
- `n & 0xF0` isolates high nibble: $0110 \, 0000_2$. Shift right 4 bits: $0000 \, 0110_2 = 6$.
- Bitwise OR: $0100 \, 0110_2 = 64 + 6 = \mathbf{70_{10}}$.
**Sample Output**:
```text
Before: 100 (01100100)
After:  70 (01000110)
```

---

### 2.2 Dutch National Flag ($0, 1, 2$ Single-Pass Sort)
*(Paper 1 Q7 — 8 Marks)*

Sort an array of $0\text{s}, 1\text{s}, 2\text{s}$ in $O(N)$ time and $O(1)$ space using 3 pointers:
```java
import java.util.Arrays;

public class DutchFlag {
    public static void sort012(int[] arr) {
        int low = 0, mid = 0, high = arr.length - 1;
        while (mid <= high) {
            if (arr[mid] == 0) {
                swap(arr, low++, mid++);
            } else if (arr[mid] == 1) {
                mid++;
            } else { // arr[mid] == 2
                swap(arr, mid, high--);
            }
        }
    }

    private static void swap(int[] a, int i, int j) {
        int t = a[i]; a[i] = a[j]; a[j] = t;
    }

    public static void main(String[] args) {
        int[] arr = {2, 0, 2, 1, 1, 0};
        sort012(arr);
        System.out.println("Sorted: " + Arrays.toString(arr));
    }
}
```
**Sample Input**: `[2, 0, 2, 1, 1, 0]`  
**Sample Output**:
```text
Sorted: [0, 0, 1, 1, 2, 2]
```

---

### 2.3 Single Number with XOR vs HashMap Space Comparison
*(Paper 1 Q2b — 5 Marks)*

```java
int[] a = {4, 1, 2, 1, 2};
int r = 0;
for (int x : a) r ^= x;
System.out.println(r); // Output: 4
```
* **Properties of XOR that make it work**:
  1. **Self-inverse**: $x \oplus x = 0$. (Pairs cancel out).
  2. **Identity element**: $x \oplus 0 = x$.
  3. **Commutative & Associative**: Order of operations does not affect the final result.
* **Space Comparison**:
  - **XOR Approach**: Auxiliary Space $= \mathbf{O(1)}$ (uses only a single integer variable `r`).
  - **HashMap Approach**: Auxiliary Space $= \mathbf{O(N)}$ (must store $N/2 + 1$ distinct keys and their frequencies in memory).

---

### 2.4 Maximum $6 \times 6$ (or $N \times M$) Hourglass Sum
*(Paper 1 Q2c, Paper 2 Q5c, Paper 3 Q5c — 6 to 12 Marks)*

```java
public class HourglassSum {
    public static int maxHourglass(int[][] mat) {
        int R = mat.length, C = mat[0].length;
        if (R < 3 || C < 3) return -1;
        int maxSum = Integer.MIN_VALUE;

        for (int i = 0; i < R - 2; i++) {
            for (int j = 0; j < C - 2; j++) {
                int sum = mat[i][j]   + mat[i][j+1]   + mat[i][j+2]
                                      + mat[i+1][j+1]
                        + mat[i+2][j] + mat[i+2][j+1] + mat[i+2][j+2];
                if (sum > maxSum) maxSum = sum;
            }
        }
        return maxSum;
    }

    public static void main(String[] args) {
        int[][] mat = {
            {1, 1, 1, 0, 0},
            {0, 1, 0, 0, 0},
            {1, 1, 1, 0, 0},
            {0, 0, 2, 4, 4},
            {0, 0, 0, 2, 0}
        };
        System.out.println("Maximum Hourglass Sum: " + maxHourglass(mat));
    }
}
```
* **Complexity**: Time: $O((R-2)(C-2)) = \mathbf{O(R \cdot C)}$, Auxiliary Space: $\mathbf{O(1)}$.
