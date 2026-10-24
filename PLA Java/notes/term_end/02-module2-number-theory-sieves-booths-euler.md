# 📘 Unit 2: Bit Manipulation, Array Properties & Hardware Mathematics

> **Aligned with VIT Bhopal PLA1004 Syllabus & TEE Papers (Slots A11, B14, F11, E11, A21)**  
> **Exam Paper Mapping**:
> - **PART A**: **Question 2** (12 Marks — with internal choice `OR`)
> - **PART B**: **Question 7** (8 Marks — direct implementation)  
> **Total Unit Weight in TEE**: **Exactly 20 Marks**

---

# PART 1: SECTION A QUESTIONS (12 MARKS) [Question 2 Pool]

---

## 1. Swap Two Nibbles in an 8-bit Byte
*(Paper 2 Q2c, Paper 4 Q2c — 12 Marks)*

A nibble consists of $4$ bits. An $8$-bit byte has an upper nibble (bits 4–7) and a lower nibble (bits 0–3).

```java
public class SwapNibbles {
    public static int swapNibbles(int n) {
        // Step 1: Extract lower 4 bits (0x0F = 0000 1111)
        int lowerNibble = n & 0x0F;

        // Step 2: Extract upper 4 bits (0xF0 = 1111 0000)
        int upperNibble = n & 0xF0;

        // Step 3: Shift lower nibble left by 4 to higher position
        int shiftedLower = lowerNibble << 4;

        // Step 4: Shift upper nibble right by 4 to lower position
        int shiftedUpper = upperNibble >> 4;

        // Step 5: Combine both parts using bitwise OR
        return shiftedLower | shiftedUpper;
    }

    public static void main(String[] args) {
        int n = 100;
        int swapped = swapNibbles(n);
        System.out.println("Before: " + n + " (" + String.format("%8s", Integer.toBinaryString(n)).replace(' ', '0') + ")");
        System.out.println("After:  " + swapped + " (" + String.format("%8s", Integer.toBinaryString(swapped)).replace(' ', '0') + ")");
    }
}
```

#### Step-by-Step Execution Trace for $N = 100$:
- Binary representation of $100_{10}$: $0110 \, 0100_2$.
- **Upper Nibble**: $0110_2 = 6_{10}$.
- **Lower Nibble**: $0100_2 = 4_{10}$.
- Shift Lower Nibble left by 4: $0100_2 \to 0100 \, 0000_2 = 64_{10}$.
- Shift Upper Nibble right by 4: $0110_2 \to 0000 \, 0110_2 = 6_{10}$.
- Bitwise OR: $0100 \, 0000_2 \mid 0000 \, 0110_2 = 0100 \, 0110_2 = 64 + 6 = \mathbf{70_{10}}$.
* **Complexity**: Time: $O(1)$, Space: $O(1)$.

---

## 2. Single Number with XOR vs HashMap Space Comparison
*(Paper 1 Q2b — 5 to 6 Marks)*

Given an array where every element appears twice except one unique element, find that element in $O(N)$ time and $O(1)$ space.

```java
public class SingleNumberXOR {
    public static int findSingle(int[] a) {
        int r = 0;
        for (int x : a) {
            r ^= x;
        }
        return r;
    }

    public static void main(String[] args) {
        int[] a = {4, 1, 2, 1, 2};
        System.out.println("Single Element: " + findSingle(a)); // Output: 4
    }
}
```

#### Properties of XOR that Make the Code Work:
1. **Self-Inverse Property**: $x \oplus x = 0$. Identical pairs cancel each other out to zero.
2. **Identity Element**: $x \oplus 0 = x$. XORing any number with zero preserves the number.
3. **Commutative & Associative**: $a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = b$. Order does not matter.

#### Trace on $\{4, 1, 2, 1, 2\}$:
- Initially: `r = 0`
- $x = 4 \implies r = 0 \oplus 4 = 4$
- $x = 1 \implies r = 4 \oplus 1 = 5$
- $x = 2 \implies r = 5 \oplus 2 = 7$
- $x = 1 \implies r = 7 \oplus 1 = 6$
- $x = 2 \implies r = 6 \oplus 2 = \mathbf{4}$

#### Space Complexity Comparison:
- **XOR Solution**: Auxiliary Space $= \mathbf{O(1)}$. Uses only a single scalar integer variable `r`.
- **HashMap Solution**: Auxiliary Space $= \mathbf{O(N)}$. Must store $N/2 + 1$ keys and their frequencies in memory.

---

## 3. Maximum $6 \times 6$ (or $N \times M$) Hourglass Sum in Matrix
*(Paper 1 Q2c, Paper 2 Q5c, Paper 3 Q5c — 12 Marks)*

An hourglass in a 2D matrix consists of 7 cells:
$$\begin{matrix} (i, j) & (i, j+1) & (i, j+2) \\ & (i+1, j+1) & \\ (i+2, j) & (i+2, j+1) & (i+2, j+2) \end{matrix}$$

```java
public class HourglassSum {
    public static int maxHourglass(int[][] mat) {
        int R = mat.length;
        int C = mat[0].length;
        if (R < 3 || C < 3) return -1;

        int maxSum = Integer.MIN_VALUE;

        for (int i = 0; i < R - 2; i++) {
            for (int j = 0; j < C - 2; j++) {
                int sum = mat[i][j]     + mat[i][j + 1]     + mat[i][j + 2]
                                        + mat[i + 1][j + 1]
                        + mat[i + 2][j] + mat[i + 2][j + 1] + mat[i + 2][j + 2];

                if (sum > maxSum) {
                    maxSum = sum;
                }
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

## 4. Equilibrium Index & Maximum Equilibrium Sum
*(Paper 4 Q2a/b — 12 Marks)*

An index $i$ is an **Equilibrium Index** if the sum of elements before $i$ equals the sum of elements after $i$:
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

#### Step-by-Step Execution Trace on $\{-7, 1, 5, 2, -4, 3, 0\}$:
- Total Sum $= -7 + 1 + 5 + 2 + (-4) + 3 + 0 = \mathbf{0}$.

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
* **Complexity**: Time: $O(N)$ (single pass), Space: $O(1)$.

---

## 5. Longest Sequence of 1s by Flipping At Most One 0 Bit
*(Paper 5 Q2a — 7 Marks)*

Given an integer $N$, find the length of the longest sequence of consecutive $1\text{s}$ in its binary representation obtainable by flipping at most one $0$ to $1$.

```java
public class LongestConsecutiveOnesWithOneFlip {
    public static int longestSequence(int n) {
        String binary = Integer.toBinaryString(n);
        int currentStreak = 0;
        int previousStreak = 0;
        int maxStreak = 1;

        for (int i = 0; i < binary.length(); i++) {
            char bit = binary.charAt(i);

            if (bit == '1') {
                currentStreak++;
            } else { // bit == '0'
                // If two zeros occur in a row, a single flip cannot bridge them
                if (i > 0 && binary.charAt(i - 1) == '0') {
                    previousStreak = 0;
                } else {
                    previousStreak = currentStreak;
                }
                currentStreak = 0;
            }

            // Streak formed by flipping the zero between previous and current block
            int total = previousStreak + currentStreak + 1;
            if (total > maxStreak) {
                maxStreak = total;
            }
        }
        return maxStreak;
    }

    public static void main(String[] args) {
        int N = 1775;
        System.out.println("Binary Before Flip: " + Integer.toBinaryString(N));
        int ans = longestSequence(N);
        System.out.println("Longest Sequence of 1s: " + ans);

        // Flipping bit at index 4 (from right)
        int flippedN = N | (1 << 4);
        System.out.println("Binary After Flip:  " + Integer.toBinaryString(flippedN) + " (Value = " + flippedN + ")");
    }
}
```

#### Worked Trace for $N = 1775$:
- **Binary Conversion**: $1775_{10} = \mathbf{(11011101111)_2}$.
- Blocks of 1s:
  - Higher block: $2$ ones (`11`)
  - Middle block: $3$ ones (`111`)
  - Lower block: $4$ ones (`1111`)
- Flipping zero between lower and middle blocks gives: $4 + 1 + 3 = \mathbf{8\text{ consecutive 1s}}$!
- **Binary After Flip**: $\mathbf{(11011111111)_2} = 1791_{10}$.
- Time Complexity: $O(\text{bits}) = O(\log N)$, Space Complexity: $O(1)$.

---

## 6. Brian Kernighan’s Algorithm vs Naive Bit Shifting
*(Paper 5 Q2b — 5 Marks)*

```java
public class BrianKernighanDemo {
    public static void main(String[] args) {
        int n = 40, c = 0;
        while (n != 0) {
            n = n & (n - 1); // Clears the lowest set bit
            c++;
        }
        System.out.println("Set Bits Count: " + c);
    }
}
```

#### Step-by-Step Binary Trace for $N = 40$:
- Binary representation of $40$: $(0010 \, 1000)_2$.
- **Iteration 1**:
  - $n = 40 = (0010 \, 1000)_2$, $n - 1 = 39 = (0010 \, 0111)_2$.
  - $n \ \& \ (n - 1) = (0010 \, 0000)_2 = 32_{10}$.
  - Counter `c` becomes **1**. (Lowest set bit cleared).
- **Iteration 2**:
  - $n = 32 = (0010 \, 0000)_2$, $n - 1 = 31 = (0001 \, 1111)_2$.
  - $n \ \& \ (n - 1) = (0000 \, 0000)_2 = 0_{10}$.
  - Counter `c` becomes **2**.
- Loop exits since $n == 0$. Final Output: **`2`**.
* **Why Faster**: A standard shift loop always tests 32 bits ($O(32)$). Brian Kernighan’s algorithm runs in **$O(K)$** where $K$ is the number of set bits. For $N = 40$, it requires **only 2 iterations** instead of 32!

---

## 7. Maximum Product Subarray with Boundary Indices
*(Paper 5 Q2c — 12 Marks)*

Given an array of integers, find the contiguous subarray that has the largest product, reporting the product and start/end indices.

```java
public class MaxProductSubarray {
    public static void findMaxProduct(int[] arr) {
        int n = arr.length;
        if (n == 0) return;

        // DP state:
        // maxProd: maximum product ending at current index
        // minProd: minimum product ending at current index (tracks negative numbers)
        int maxProd = arr[0];
        int minProd = arr[0];
        int globalMax = arr[0];

        int bestStart = 0;
        int bestEnd = 0;

        for (int i = 1; i < n; i++) {
            int num = arr[i];

            // Calculate the two possible product extensions
            int choice1 = num * maxProd;
            int choice2 = num * minProd;

            // Maximum product ending at i can be:
            // 1. Starting fresh with 'num'
            // 2. Extending previous maximum product
            // 3. Extending previous minimum product (negative * negative = positive)
            maxProd = Math.max(num, Math.max(choice1, choice2));
            minProd = Math.min(num, Math.min(choice1, choice2));

            if (maxProd > globalMax) {
                globalMax = maxProd;
            }
        }

        // Identify the exact start and end indices of the best subarray
        for (int i = 0; i < n; i++) {
            int p = 1;
            for (int j = i; j < n; j++) {
                p *= arr[j];
                if (p == globalMax) {
                    bestStart = i;
                    bestEnd = j;
                    break;
                }
            }
        }

        System.out.println("Maximum Product: " + globalMax);
        System.out.println("Subarray Indices: [" + bestStart + ", " + bestEnd + "]");
    }

    public static void main(String[] args) {
        int[] arr = {2, 3, -2, 4, -1};
        findMaxProduct(arr);
    }
}
```

#### Step-by-Step Trace for $\{2, 3, -2, 4, -1\}$:
- At $i = 0$: `num = 2` $\implies \text{product} = 2$.
- At $i = 1$: `num = 3` $\implies 2 \times 3 = 6$.
- At $i = 2$: `num = -2` $\implies 6 \times (-2) = -12$ (min becomes $-12$).
- At $i = 3$: `num = 4` $\implies -12 \times 4 = -48$.
- At $i = 4$: `num = -1` $\implies -48 \times (-1) = \mathbf{+48}$!
* **Global Maximum Product**: $\mathbf{48}$.
* **Subarray Indices**: Start Index $= \mathbf{0}$, End Index $= \mathbf{4}$ (Entire array: $2 \times 3 \times (-2) \times 4 \times (-1) = 48$). Time: $O(N)$, Space: $O(1)$.

---

## 8. Euler's Totient Function $\varphi(N)$
*(Paper 3 Q1a & Paper 5 Q1a — 12 Marks)*

Euler's Totient function $\varphi(N)$ counts the number of integers $k \in [1, N]$ such that $\gcd(k, N) = 1$.

```java
import java.util.*;

public class EulerTotientComparison {
    // Method A: Brute-Force Testing O(N log N)
    public static int gcd(int a, int b) {
        while (b != 0) {
            int t = b; b = a % b; a = t;
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
                while (n % p == 0) n /= p; // Remove factor p
                result -= result / p;      // result = result * (1 - 1/p)
            }
        }
        if (n > 1) {
            result -= result / n;
        }
        return result;
    }

    public static void main(String[] args) {
        int n = 36;
        List<Integer> coprimes = new ArrayList<>();
        System.out.println("phi(36) via Brute Force: " + eulerPhiBruteForce(n, coprimes));
        System.out.println("Coprimes to 36: " + coprimes);
        System.out.println("phi(36) via Factorisation: " + eulerPhiFactorisation(n));
    }
}
```

#### Hand Calculations by Prime Factorisation (Assignment Q1.3):
1. **$\varphi(36)$**:
   - Prime factorisation: $36 = 2^2 \times 3^2$. Distinct prime factors: $p \in \{2, 3\}$.
   - Formula: $\varphi(36) = 36 \times (1 - \frac{1}{2}) \times (1 - \frac{1}{3}) = 36 \times \frac{1}{2} \times \frac{2}{3} = \mathbf{12}$.
   - Coprime set: $\{1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35\}$ (Count = 12).
2. **$\varphi(100)$**:
   - Prime factorisation: $100 = 2^2 \times 5^2$. Distinct prime factors: $p \in \{2, 5\}$.
   - Formula: $\varphi(100) = 100 \times (1 - \frac{1}{2}) \times (1 - \frac{1}{5}) = 100 \times \frac{1}{2} \times \frac{4}{5} = \mathbf{40}$.
3. **$\varphi(97)$**:
   - Prime factorisation: $97$ is a **prime number**.
   - Formula for any prime $p$: $\varphi(p) = p - 1 \implies \varphi(97) = 97 - 1 = \mathbf{96}$.

#### Feasibility Comparison for $N \le 10^{12}$:
- **Brute-Force ($O(N \log N)$)**: Testing $\gcd(i, 10^{12}) = 1$ for all $1 \le i \le 10^{12}$ requires $10^{12} \times 40 \approx 4 \times 10^{13}$ operations ($\approx 111\text{ hours}$ of CPU time $\implies$ **completely infeasible**).
- **Prime Factorisation ($O(\sqrt{N})$)**: Loops up to $\sqrt{10^{12}} = 10^6$ operations ($\approx 2\text{ milliseconds} \implies$ **highly feasible and optimal**).

---

## 9. Strobogrammatic Number Generation
*(Paper 1 Q1a, Paper 2 Q1b, Paper 3 Q1b — 12 Marks)*

A Strobogrammatic number looks identical when rotated $180^\circ$.
* Reversible digit pairs: `(0, 0)`, `(1, 1)`, `(8, 8)`, `(6, 9)`, `(9, 6)`.

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
            // '0' cannot be placed at the outermost ends
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
        System.out.println("Total Count: " + ans.size());
    }
}
```
**Sample Output for $N = 3$**:
```text
Strobogrammatic numbers of length 3: [101, 808, 609, 906, 111, 818, 619, 916, 181, 888, 689, 986]
Total Count: 12
```

---

## 10. Booth's Multiplication Algorithm for Signed Binary
*(Syllabus Model — 12 Marks)*

Multiplies two signed binary integers using registers $[A, Q, Q_{-1}]$ and Arithmetic Shift Right (ASR):
* `Q_0 Q_{-1} = 10` $\implies A = A - M$, then ASR.
* `Q_0 Q_{-1} = 01` $\implies A = A + M$, then ASR.
* `00` or `11` $\implies$ ASR directly (Sign bit of $A$ is preserved).
* Fully worked trace for $(7)_{10} \times (-5)_{10}$ yields $[11110 \, 11101]_2 = \mathbf{-35_{10}}$.

---

## 11. Toggle the Switch Problem & Perfect Squares Mathematical Proof
*(Assignment Q2.4 & PPT L13 — 12 Marks)*

### Problem Statement:
There are $N$ switches numbered $1$ to $N$, all initially **OFF**.
- In round 1, you toggle every 1st switch (switches 1, 2, 3, 4, ... are toggled).
- In round 2, you toggle every 2nd switch (switches 2, 4, 6, 8, ... are toggled).
- In round $i$, you toggle every $i$-th switch (switches $i, 2i, 3i, \dots$).
Find which switches are **ON** after $N$ rounds and justify your answer mathematically.

### Mathematical Proof:
1. A switch at position $k$ is toggled in round $i$ if and only if $i$ is a divisor of $k$.
2. Therefore, the total number of times switch $k$ is toggled is equal to the **total number of divisors** of $k$.
3. Since the switch starts in the OFF position:
   - An **even number of toggles** leaves the switch **OFF** ($\text{OFF} \to \text{ON} \to \text{OFF}$).
   - An **odd number of toggles** leaves the switch **ON** ($\text{OFF} \to \text{ON}$).
4. Divisors of any positive integer naturally occur in distinct pairs: $(d, \frac{k}{d})$. For example:
   - Divisors of $12$: $(1, 12), (2, 6), (3, 4) \implies 6\text{ divisors (even)} \implies$ Switch 12 ends **OFF**.
5. The only integers that have an **odd number of divisors** are **perfect squares** ($k = d^2$), because the divisor $d = \sqrt{k}$ is paired with itself and counted only once!
   - Divisors of $16$: $(1, 16), (2, 8), (4, 4) \implies 5\text{ divisors (odd)} \implies$ Switch 16 ends **ON**.
6. **Conclusion**: Exactly those switches whose numbers are **perfect squares** ($1, 4, 9, 16, 25, \dots \le N$) will remain **ON**.
   The total count of ON switches is $\mathbf{\lfloor \sqrt{N} \rfloor}$.

```java
import java.util.*;

public class ToggleTheSwitch {
    public static List<Integer> getSwitchesON(int n) {
        List<Integer> onSwitches = new ArrayList<>();
        // Only perfect squares remain ON
        for (int i = 1; i * i <= n; i++) {
            onSwitches.add(i * i);
        }
        return onSwitches;
    }

    public static void main(String[] args) {
        int n = 50;
        List<Integer> result = getSwitchesON(n);
        System.out.println("Switches ON after " + n + " rounds: " + result);
        System.out.println("Total count: " + result.size() + " (= floor(sqrt(" + n + ")))");
    }
}
```
**Sample Output for $N = 50$**:
```text
Switches ON after 50 rounds: [1, 4, 9, 16, 25, 36, 49]
Total count: 7 (= floor(sqrt(50)))
```
* **Complexities**: Time: $O(\sqrt{N})$, Auxiliary Space: $O(1)$.

---
---

# PART 2: SECTION B QUESTIONS (8 MARKS) [Question 7 Pool]

---

## 11. Dutch National Flag Algorithm ($0, 1, 2$ Single-Pass Sort)
*(Paper 1 Q7 — 8 Marks)*

Sort an array containing only $0\text{s}$, $1\text{s}$, and $2\text{s}$ in a single pass without using any library sort.

```java
import java.util.Arrays;

public class DutchNationalFlag {
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

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;
    }

    public static void main(String[] args) {
        int[] arr = {2, 0, 2, 1, 1, 0};
        sort012(arr);
        System.out.println("Sorted Array: " + Arrays.toString(arr));
    }
}
```

#### Step-by-Step Pointer Trace for $\{2, 0, 2, 1, 1, 0\}$:
- Initially: `low = 0, mid = 0, high = 5`.
1. `arr[mid=0] == 2`: Swap `arr[0]` and `arr[5]`. Array: $\{0, 0, 2, 1, 1, 2\}$. `high = 4`.
2. `arr[mid=0] == 0`: Swap `arr[0]` and `arr[0]`. `low = 1, mid = 1`. Array: $\{0, 0, 2, 1, 1, 2\}$.
3. `arr[mid=1] == 0`: Swap `arr[1]` and `arr[1]`. `low = 2, mid = 2`. Array: $\{0, 0, 2, 1, 1, 2\}$.
4. `arr[mid=2] == 2`: Swap `arr[2]` and `arr[4]`. Array: $\{0, 0, 1, 1, 2, 2\}$. `high = 3`.
5. `arr[mid=2] == 1`: `mid = 3`.
6. `arr[mid=3] == 1`: `mid = 4`.
- Now `mid = 4 > high = 3` $\implies$ Loop terminates!
* **Final Sorted Array**: $\{0, 0, 1, 1, 2, 2\}$. Time: $O(N)$, Space: $O(1)$.

---

## 12. Block Swap Algorithm for Array Left Rotation
*(Paper 4 Q7 — 8 Marks)*

To rotate an array of size $n$ to the left by $d$ positions in $O(n)$ time and $O(1)$ space:
Divide array into $A = arr[0..d-1]$ and $B = arr[d..n-1]$. Recursively swap blocks until sizes match.

```java
import java.util.Arrays;

public class BlockSwapRotation {
    public static void leftRotate(int[] arr, int d, int n) {
        d = d % n;
        if (d == 0) return;
        rotateRecursive(arr, 0, d, n);
    }

    private static void rotateRecursive(int[] arr, int i, int d, int n) {
        if (d == 0 || d == n) return;

        if (n - d == d) {
            swap(arr, i, n - d + i, d);
            return;
        }

        if (d < n - d) {
            swap(arr, i, n - d + i, d);
            rotateRecursive(arr, i, d, n - d);
        } else {
            swap(arr, i, d + i, n - d);
            rotateRecursive(arr, n - d + i, 2 * d - n, d);
        }
    }

    private static void swap(int[] arr, int fi, int si, int d) {
        for (int k = 0; k < d; k++) {
            int temp = arr[fi + k];
            arr[fi + k] = arr[si + k];
            arr[si + k] = temp;
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        leftRotate(arr, 2, arr.length);
        System.out.println("Rotated Left by 2: " + Arrays.toString(arr)); // [3, 4, 5, 6, 7, 1, 2]
    }
}
```

---

## 13. Array Right Rotation by $K$ Positions via 3 Reversals
*(Paper 5 Q7 — 8 Marks)*

Rotate an array of size $n$ to the right by $k$ positions in $O(n)$ time and $O(1)$ extra space using the reversal algorithm.

```java
import java.util.Arrays;

public class ArrayRightRotation {
    public static void reverse(int[] a, int start, int end) {
        while (start < end) {
            int temp = a[start];
            a[start] = a[end];
            a[end] = temp;
            start++;
            end--;
        }
    }

    public static void rotateRight(int[] a, int k) {
        int n = a.length;
        k = k % n; // Handle k >= n

        // Step 1: Reverse the entire array
        reverse(a, 0, n - 1);
        // Step 2: Reverse the first k elements
        reverse(a, 0, k - 1);
        // Step 3: Reverse the remaining n - k elements
        reverse(a, k, n - 1);
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        int k = 3;
        System.out.println("Original: " + Arrays.toString(arr));
        rotateRight(arr, k);
        System.out.println("Right Rotated by " + k + ": " + Arrays.toString(arr));
    }
}
```

#### Step-by-Step Trace for $\{1, 2, 3, 4, 5, 6, 7\}$ with $k = 3$:
- **Initial Array**: `[1, 2, 3, 4, 5, 6, 7]`
- **Step 1 (Reverse all 7 elements)**:
  `[7, 6, 5, 4, 3, 2, 1]`
- **Step 2 (Reverse first $k=3$ elements)**:
  `[5, 6, 7, 4, 3, 2, 1]`
- **Step 3 (Reverse remaining $n-k=4$ elements from index 3 to 6)**:
  `[5, 6, 7, 1, 2, 3, 4]`
* **Final Rotated Array**: `[5, 6, 7, 1, 2, 3, 4]`.
* **Complexity**: Time: $O(N)$, Auxiliary Space: $O(1)$.

---

## 14. Binary Palindromes & Next Binary Palindrome
*(Paper 1 Q2a, Paper 2 Q6 — 7 to 8 Marks)*

Find the smallest integer strictly greater than $N$ whose binary representation is a palindrome.

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

#### Execution Trace for $N = 25$:
- $25_{10} = 11001_2$ (Reverse $= 10011_2 \ne 11001_2 \implies$ Not palindrome).
- $26_{10} = 11010_2$ (Reverse $= 01011_2 \implies$ Not palindrome).
- $27_{10} = 11011_2$ (Reverse $= 11011_2 \implies$ **Binary Palindrome!**).  
* **Sample Output**: `27` ($11011_2$).
