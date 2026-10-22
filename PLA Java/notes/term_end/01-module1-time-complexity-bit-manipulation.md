# 📘 Unit 1: Complexity Analysis & Bit Manipulation Algorithms

> **Aligned with VIT Bhopal October 2026 TEE Papers**: Slots A11, B14, F11, E11, A21  
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

### 1.5 Insertion Sort: Complexity Analysis & Element Shift Trace
*(Paper 5 Q1b — 12 Marks)*

```java
public class InsertionSortDemo {
    public static int insertionSort(int[] a) {
        int n = a.length;
        int totalShifts = 0;
        for (int i = 1; i < n; i++) {
            int key = a[i];
            int j = i - 1;
            while (j >= 0 && a[j] > key) {
                a[j + 1] = a[j]; // Element shift
                totalShifts++;
                j = j - 1;
            }
            a[j + 1] = key;
        }
        return totalShifts;
    }

    public static void main(String[] args) {
        int[] arr = {5, 2, 4, 6, 1, 3};
        int shifts = insertionSort(arr);
        System.out.println("Sorted Array: " + java.util.Arrays.toString(arr));
        System.out.println("Total Element Shifts: " + shifts);
    }
}
```

#### Step-by-Step Execution Trace on Array $\{5, 2, 4, 6, 1, 3\}$:

| Pass $i$ | Key $a[i]$ | Comparisons & Shifts Performed | Array State After Pass | Shifts in Pass | Cumulative Shifts |
|:---:|:---:|:---|:---|:---:|:---:|
| **Initial** | — | — | `[5, 2, 4, 6, 1, 3]` | 0 | 0 |
| **Pass 1** ($i=1$) | **2** | $5 > 2 \implies$ shift $5$ right to index 1. Place $2$ at index 0. | `[2, 5, 4, 6, 1, 3]` | 1 | 1 |
| **Pass 2** ($i=2$) | **4** | $5 > 4 \implies$ shift $5$ right. $2 \le 4 \implies$ stop. Place $4$ at index 1. | `[2, 4, 5, 6, 1, 3]` | 1 | 2 |
| **Pass 3** ($i=3$) | **6** | $5 \le 6 \implies$ loop condition fails immediately. No shift. | `[2, 4, 5, 6, 1, 3]` | 0 | 2 |
| **Pass 4** ($i=4$) | **1** | $6 > 1, 5 > 1, 4 > 1, 2 > 1 \implies$ shift all 4 elements right. Place $1$ at index 0. | `[1, 2, 4, 5, 6, 3]` | 4 | 6 |
| **Pass 5** ($i=5$) | **3** | $6 > 3, 5 > 3, 4 > 3 \implies$ shift $6, 5, 4$ right. $2 \le 3 \implies$ stop. Place $3$ at index 2. | `[1, 2, 3, 4, 5, 6]` | 3 | **9** |

* **Total Element Shifts**: **9 Shifts**.
* **Final Sorted Array**: `[1, 2, 3, 4, 5, 6]`.

#### Complexity Analysis & Best/Worst Case Derivations:
1. **Best-Case Time Complexity — $O(N)$**:
   - Occurs when the input array is **already sorted in ascending order** (e.g., $\{1, 2, 3, 4, 5, 6\}$).
   - In each pass $i$, the while loop condition `a[j] > key` fails on the very first comparison because $a[i - 1] \le a[i]$.
   - Number of comparisons $= N - 1 = O(N)$.
   - Number of element shifts $= \mathbf{0}$.
2. **Worst-Case Time Complexity — $O(N^2)$**:
   - Occurs when the input array is **sorted in reverse descending order** (e.g., $\{6, 5, 4, 3, 2, 1\}$).
   - Every element $a[i]$ must be compared and shifted past all $i$ elements in the sorted prefix:
     $$\text{Total Shifts} = \sum_{i=1}^{N-1} i = 1 + 2 + 3 + \dots + (N - 1) = \frac{N(N - 1)}{2} = \mathbf{O(N^2)}$$
3. **Average-Case Time Complexity — $O(N^2)$**:
   - On random permutations, each element is compared with half of the elements in the sorted subarray: $\approx \frac{N(N-1)}{4}$ shifts $= O(N^2)$.
4. **Space Complexity — $O(1)$**:
   - Strictly in-place; requires only scalar integer variables (`key`, `i`, `j`).

---

## 2. Bitwise Hacks & Algorithmic Recipes

| Operation | Bitwise Expression |
|:---|:---|
| **Check if $k$-th bit is set** | `(n & (1 << k)) != 0` |
| **Set $k$-th bit** | `n | (1 << k)` |
| **Clear $k$-th bit** | `n & ~(1 << k)` |
| **Toggle $k$-th bit** | `n ^ (1 << k)` |
| **Check if power of 2** | `n > 0 && (n & (n - 1)) == 0` |
| **Clear lowest set bit** | `n & (n - 1)` |
| **Extract lowest set bit** | `n & -n` |
| **Swap two numbers without temp var** | `a ^= b; b ^= a; a ^= b;` |
| **Swap two nibbles in a byte** | `((n & 0x0F) << 4) | ((n & 0xF0) >> 4)` |

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

---

### 2.5 Longest Sequence of 1s by Flipping at Most One 0 Bit
*(Paper 5 Q2a — 7 Marks)*

Given an integer $N$, find the length of the longest contiguous sequence of $1\text{s}$ that can be created in its binary representation by flipping at most one $0$ to $1$.

```java
public class LongestConsecutiveOnesWithOneFlip {
    public static int longestSequence(int n) {
        // If all bits are 1s in integer (or n == -1), length is 32
        if (~n == 0) return Integer.BYTES * 8;

        int currentLength = 0;
        int previousLength = 0;
        int maxLength = 1; // Can always flip at least one 0 to get length 1

        while (n != 0) {
            if ((n & 1) == 1) {
                currentLength++;
            } else if ((n & 1) == 0) {
                // If next bit is 0, previousLength becomes 0; else it holds currentLength
                previousLength = ((n & 2) == 0) ? 0 : currentLength;
                currentLength = 0;
            }
            maxLength = Math.max(previousLength + currentLength + 1, maxLength);
            n >>>= 1;
        }
        return maxLength;
    }

    public static void main(String[] args) {
        int N = 1775;
        System.out.println("Input N: " + N);
        System.out.println("Binary Before Flip: " + Integer.toBinaryString(N));
        int maxOnes = longestSequence(N);
        System.out.println("Longest Sequence of 1s: " + maxOnes);
        // Trace showing the optimal flipped position
        int flippedN = N | (1 << 4); // Flipping bit 4
        System.out.println("Binary After Flip:  " + Integer.toBinaryString(flippedN) + " (Value = " + flippedN + ")");
    }
}
```

#### Detailed Execution Trace for $N = 1775$:
- **Binary Conversion**:
  $$1775_{10} = 1024 + 512 + 128 + 64 + 32 + 8 + 4 + 2 + 1 = \mathbf{(11011101111)_2}$$
- **Bit Structure & 1s Blocks**:
  - Bits 0 to 3: Four 1s (`1111`, length = 4).
  - Bit 4: Single `0`.
  - Bits 5 to 7: Three 1s (`111`, length = 3).
  - Bit 8: Single `0`.
  - Bits 9 to 10: Two 1s (`11`, length = 2).
- **Evaluating Flip Candidates**:
  1. **Flip Bit 8**: Bridges block of 2 ones and block of 3 ones $\implies 2 + 1 + 3 = \mathbf{6\text{ ones}}$.
  2. **Flip Bit 4**: Bridges block of 3 ones and block of 4 ones $\implies 3 + 1 + 4 = \mathbf{8\text{ ones}}$!
- **State After Optimal Flip (Bit 4)**:
  - Flipped Binary: `11011111111` ($1791_{10}$).
  - Longest sequence of consecutive $1\text{s} = \mathbf{8}$.
- **Complexity**: Time: $O(\text{number of bits}) = \mathbf{O(\log N)}$ (at most 32 loop steps), Auxiliary Space: $\mathbf{O(1)}$.

---

### 2.6 Brian Kernighan’s Algorithm vs Naive Bit Checking
*(Paper 5 Q2b — 5 Marks)*

```java
public class BrianKernighanDemo {
    public static void main(String[] args) {
        int n = 40, c = 0;
        System.out.println("Initial n = " + n + " (" + Integer.toBinaryString(n) + ")");
        while (n != 0) {
            int prev = n;
            n = n & (n - 1);
            c++;
            System.out.println("Iteration " + c + ": " + prev + " & " + (prev - 1) 
                               + " -> n = " + n + " (" + Integer.toBinaryString(n) + ")");
        }
        System.out.println("Final Output (Set Bits Count): " + c);
    }
}
```

#### Step-by-Step Binary Trace for $N = 40$:
- Binary Representation of $40$: $(00101000)_2$.
- **Iteration 1**:
  - $n = 40 = (00101000)_2$, $n - 1 = 39 = (00100111)_2$.
  - Bitwise AND:
    $$\begin{aligned}
    n &= 00101000_2 \\
    n - 1 &= 00100111_2 \\
    \hline
    n \ \& \ (n - 1) &= 00100000_2 = 32_{10}
    \end{aligned}$$
  - Counter `c` becomes **1**.
- **Iteration 2**:
  - $n = 32 = (00100000)_2$, $n - 1 = 31 = (00011111)_2$.
  - Bitwise AND:
    $$\begin{aligned}
    n &= 00100000_2 \\
    n - 1 &= 00011111_2 \\
    \hline
    n \ \& \ (n - 1) &= 00000000_2 = 0_{10}
    \end{aligned}$$
  - Counter `c` becomes **2**.
- **Termination**:
  - $n == 0 \implies$ loop exits.
  - Final Output: **`2`**.

#### Why Brian Kernighan’s Algorithm is Faster than Naive Bit Shifting:
1. **What the code computes**: It counts the number of set bits (Hamming weight) in the integer.
2. **Naive Shift Approach**:
   - Loops through every single bit position: `while (n > 0) { c += (n & 1); n >>= 1; }`.
   - Always executes $\mathbf{32\text{ iterations}}$ for 32-bit integers, even if only one bit is set.
3. **Brian Kernighan’s Speed Advantage**:
   - Subtracting 1 from $n$ flips all bits from the lowest set bit to the rightmost bit. Performing $n \ \& \ (n - 1)$ clears **strictly the lowest set bit** and preserves all higher bits.
   - Time Complexity is **$O(K)$**, where $K$ is the number of set bits ($K \le \log_2 N$).
   - For $N = 40$, it requires **only 2 iterations** instead of 32 iterations!

---

### 2.7 Maximum Product Subarray with Boundary Indices
*(Paper 5 Q2c — 12 Marks)*

Given an array of integers, find the contiguous subarray that has the largest product, reporting the maximum product as well as its start and end indices.

```java
public class MaxProductSubarray {
    public static void findMaxProduct(int[] a) {
        int n = a.length;
        long maxEndingHere = a[0];
        long minEndingHere = a[0];
        long maxSoFar = a[0];

        int bestStart = 0, bestEnd = 0;
        int currentStart = 0;

        for (int i = 1; i < n; i++) {
            long val = a[i];

            // If current element is negative, max and min swap when multiplied
            if (val < 0) {
                long temp = maxEndingHere;
                maxEndingHere = minEndingHere;
                minEndingHere = temp;
            }

            if (val > maxEndingHere * val) {
                maxEndingHere = val;
                if (val >= 0) currentStart = i;
            } else {
                maxEndingHere = maxEndingHere * val;
            }

            minEndingHere = Math.min(val, minEndingHere * val);

            if (maxEndingHere > maxSoFar) {
                maxSoFar = maxEndingHere;
                bestStart = currentStart;
                bestEnd = i;
            }
        }

        // Special handling for full array product verification
        long fullProd = 1;
        for (int x : a) fullProd *= x;
        if (fullProd > maxSoFar) {
            maxSoFar = fullProd;
            bestStart = 0;
            bestEnd = n - 1;
        }

        System.out.println("Maximum Product: " + maxSoFar);
        System.out.println("Subarray Indices: [" + bestStart + ", " + bestEnd + "]");
        System.out.print("Subarray Elements: [");
        for (int i = bestStart; i <= bestEnd; i++) {
            System.out.print(a[i] + (i < bestEnd ? ", " : ""));
        }
        System.out.println("]");
    }

    public static void main(String[] args) {
        int[] arr = {2, 3, -2, 4, -1};
        findMaxProduct(arr);
    }
}
```

#### Why Standard Kadane’s Algorithm Fails & The Dynamic Programming State:
- In standard Kadane's algorithm (for maximum subarray *sum*), adding a negative number always decreases the cumulative sum.
- For *products*, **multiplying two negative numbers produces a positive number**! A very small negative product can become the global maximum if multiplied by another negative element.
- Therefore, we must maintain two running values at each index $i$:
  1. `maxEndingHere`: Maximum product ending at index $i$.
  2. `minEndingHere`: Minimum (most negative) product ending at index $i$.
  - When $a[i] < 0$, `maxEndingHere` and `minEndingHere` swap before multiplication.

#### Execution Trace for $\{2, 3, -2, 4, -1\}$:

| Index $i$ | Element $a[i]$ | Action / Swap | `maxEndingHere` | `minEndingHere` | `maxSoFar` | Current Best Range |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| **Init** ($i=0$) | **2** | Base initialization | 2 | 2 | 2 | $[0, 0]$ |
| **1** | **3** | Positive: $\max(3, 2 \times 3)$, $\min(3, 2 \times 3)$ | **6** | 3 | **6** | $[0, 1]$ |
| **2** | **-2** | Negative: Swap max & min $\to$ $\max(-2, 3 \times -2)$, $\min(-2, 6 \times -2)$ | **-2** | -12 | **6** | $[0, 1]$ |
| **3** | **4** | Positive: $\max(4, -2 \times 4)$, $\min(4, -12 \times 4)$ | **4** | -48 | **6** | $[0, 1]$ |
| **4** | **-1** | Negative: Swap max & min $\to$ $\max(-1, -48 \times -1)$, $\min(-1, 4 \times -1)$ | **48** | -4 | **48** | **$[0, 4]$** |

* **Product of Subarray**: $2 \times 3 \times (-2) \times 4 \times (-1) = \mathbf{48}$.
* **Start Index**: `0`, **End Index**: `4`.
* **Complexity**: Time Complexity: $\mathbf{O(N)}$ (single linear scan), Auxiliary Space: $\mathbf{O(1)}$.

---

### 2.8 Quadratic Equation Roots Decision Flow
*(Paper 5 Q6 — 8 Marks)*

```java
import java.util.Scanner;

public class QuadraticRootsSolver {
    public static void solveQuadratic(double a, double b, double c) {
        if (a == 0) {
            System.out.println("Invalid: Coefficient 'a' cannot be 0 for a quadratic equation.");
            return;
        }

        double discriminant = (b * b) - (4 * a * c);
        System.out.printf("Equation: (%.1f)x^2 + (%.1f)x + (%.1f) = 0 | Discriminant D = %.2f\n", a, b, c, discriminant);

        if (discriminant > 0) {
            // Branch 1: Real and Distinct
            double r1 = (-b + Math.sqrt(discriminant)) / (2 * a);
            double r2 = (-b - Math.sqrt(discriminant)) / (2 * a);
            System.out.printf("Nature of Roots: Real and Distinct\nRoots: x1 = %.2f, x2 = %.2f\n", r1, r2);
        } else if (discriminant == 0) {
            // Branch 2: Real and Equal
            double r = -b / (2 * a);
            System.out.printf("Nature of Roots: Real and Equal\nRoots: x1 = x2 = %.2f\n", r);
        } else {
            // Branch 3: Complex Conjugate (Imaginary)
            double realPart = -b / (2 * a);
            double imagPart = Math.sqrt(-discriminant) / (2 * a);
            System.out.printf("Nature of Roots: Imaginary (Complex Conjugates)\nRoots: x1 = %.2f + %.2fi, x2 = %.2f - %.2fi\n", 
                              realPart, imagPart, realPart, imagPart);
        }
        System.out.println("-----------------------------------------------------------------");
    }

    public static void main(String[] args) {
        solveQuadratic(1, -5, 6);
        solveQuadratic(1, 2, 1);
        solveQuadratic(1, 2, 5);
    }
}
```

#### Decision Flow & Analytical Trace for the 3 Cases:

```
                  Calculate Discriminant D = b^2 - 4ac
                                  |
            +---------------------+---------------------+
            |                                           |
         D > 0                                        D <= 0
            |                                           |
  [Branch 1: Real & Distinct]                  +--------+--------+
  r1, r2 = (-b ± √D) / (2a)                    |                 |
                                             D == 0            D < 0
                                               |                 |
                                     [Branch 2: Equal]  [Branch 3: Imaginary]
                                     r = -b / (2a)      -b/(2a) ± i(√|D|)/(2a)
```

| Coefficients $(a, b, c)$ | Discriminant Calculation $D = b^2 - 4ac$ | Sign of $D$ | Decision Branch Executed | Roots Computed |
|:---|:---|:---:|:---|:---|
| **Case 1**: $(1, -5, 6)$ | $(-5)^2 - 4(1)(6) = 25 - 24 = \mathbf{1}$ | $D > 0$ | **Branch 1 (Real & Distinct)** | $x_1 = \frac{5 + 1}{2} = \mathbf{3.0}$, $x_2 = \frac{5 - 1}{2} = \mathbf{2.0}$ |
| **Case 2**: $(1, 2, 1)$ | $(2)^2 - 4(1)(1) = 4 - 4 = \mathbf{0}$ | $D == 0$ | **Branch 2 (Real & Equal)** | $x_1 = x_2 = \frac{-2}{2} = \mathbf{-1.0}$ |
| **Case 3**: $(1, 2, 5)$ | $(2)^2 - 4(1)(5) = 4 - 20 = \mathbf{-16}$ | $D < 0$ | **Branch 3 (Imaginary / Complex)** | $\text{Real} = -1.0, \text{Imag} = \frac{\sqrt{16}}{2} = 2.0 \implies \mathbf{-1.0 \pm 2.0i}$ |

* **Complexity**: Time Complexity: $O(1)$ (direct arithmetic and square root), Space Complexity: $O(1)$.

