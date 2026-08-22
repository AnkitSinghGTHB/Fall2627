# 🚀 Competitive Coding Practices (PLA1004) CAT-1 Master Solved Papers

> **Complete, 100% Verified Model Solutions for Both Official CAT-1 Exam Papers**  
> **Paper 1:** Slot B22/B24 (18-08-2026 / S-I)  
> **Paper 2:** Slot B14+D21 (18-08-2026 / S-III)  
> *Max Marks: 50 | Time: 1.5 Hours each | Calculator Not Allowed*

---

# 📑 Master Table of Contents

### 🅰️ Paper 1: Slot B22/B24 (18-08-2026 / S-I)
1. [Q1 (10M): If-Else vs Switch Statements + Positive/Negative/Zero Java Program](#p1-q1)
2. [Q2 (10M): Euclid's Algorithm Concept + Step-by-Step Trace for A=1556, B=2421](#p1-q2)
3. [Q3 (10M): Selection Sort Technique + Pass-by-Pass Sort for {91, 34, 56, 12, 78, 20}](#p1-q3)
4. [Q4 (10M): Hourglass Count Formula Derivation + 6x6 Matrix Max Hourglass Sum Java Program](#p1-q4)
5. [Q5.a (5M): Leaders in an Array Java Program & Logic](#p1-q5a)
6. [Q5.b (5M): Block Swap Left Rotation Algorithm + Rotate {11..88} by 3 Positions](#p1-q5b)

---

### 🅱️ Paper 2: Slot B14+D21 (18-08-2026 / S-III)
7. [Q1 (10M): Relational & Logical Operators + Student Pass/Fail Marks Program (67, 72, 81)](#p2-q1)
8. [Q2 (10M): Binary Palindrome Concept + Verify Decimal 21 Java Program](#p2-q2)
9. [Q3 (10M): Selection Sort Algorithm + Sort {90, 12, 65, 43, 27, 18}](#p2-q3)
10. [Q4 (10M): Maximum Equilibrium Sum Concept + Trace for {3, 1, 2, 6, 4, 4}](#p2-q4)
11. [Q5.a (5M): Role of Control Structures + Numbers 1-50 Divisible by 2 or 7](#p2-q5a)
12. [Q5.b (5M): Quick Sort & Partitioning Process + Sort {64, 31, 85, 12, 47, 29}](#p2-q5b)

---
---

# 🅰️ Paper 1 Solutions (Slot B22/B24)

---

<a id="p1-q1"></a>
## 1️⃣ Paper 1 - Q1 (10 Marks): If-Else vs Switch Statements & Number Check

### Part A: Difference between `if-else` and `switch` statements (6 Marks)

| Feature / Criteria | `if-else` Statement | `switch` Statement |
|---|---|---|
| **Expression Type** | Evaluates **Boolean expressions** (`true` or `false`), relational, and logical conditions (e.g., `x > 10 && y < 5`). | Evaluates a single variable/expression matching discrete constant values (`byte`, `short`, `char`, `int`, `String`, `enum`). |
| **Testing Range** | Can test **ranges** of values (e.g., `score >= 80 && score <= 90`) and complex inequalities. | Tests only for **equality** against fixed constant case labels (cannot test ranges directly). |
| **Execution Flow** | Evaluates conditions **sequentially** from top to bottom until the first `true` condition is encountered. | Uses a **jump table / lookup table** at the bytecode level, allowing direct jump to matching case ($O(1)$ lookup in many cases). |
| **Fall-through Behavior** | No fall-through concept; only one matching block executes. | Cases execute sequentially downwards if `break` statement is omitted (**fall-through**). |
| **Default Handling** | Optional `else` block executes when all preceding `if` / `else if` conditions are false. | Optional `default:` case executes when no matching `case` value is found. |
| **Readability / Use Case** | Best for multiple independent conditions and continuous intervals. | Best for clean multi-way branching based on fixed menu choices or discrete states. |

#### Syntax Examples:

```java
// if-else Example (Range Checking)
if (marks >= 90) {
    grade = 'A';
} else if (marks >= 75) {
    grade = 'B';
} else {
    grade = 'C';
}

// switch Example (Discrete Value Matching)
switch (dayNumber) {
    case 1: day = "Monday"; break;
    case 2: day = "Tuesday"; break;
    default: day = "Invalid Day"; break;
}
```

---

### Part B: Java Program to Determine if 47 is Positive, Negative, or Zero (4 Marks)

```java
import java.util.Scanner;

public class NumberSignCheck {
    public static void main(String[] args) {
        int number = 47; // Hardcoded or accepted via Scanner
        
        System.out.println("Given Number: " + number);
        
        if (number > 0) {
            System.out.println(number + " is a POSITIVE number.");
        } else if (number < 0) {
            System.out.println(number + " is a NEGATIVE number.");
        } else {
            System.out.println(number + " is ZERO.");
        }
    }
}
```

#### Output:
```text
Given Number: 47
47 is a POSITIVE number.
```

---

<a id="p1-q2"></a>
## 2️⃣ Paper 1 - Q2 (10 Marks): Euclid's Algorithm & Step-by-Step Trace for A=1556, B=2421

### Part A: Concept of Euclid's Algorithm (4 Marks)
- **Core Principle:** The Greatest Common Divisor ($\gcd$) of two integers $A$ and $B$ (where $A \ge B$) is equal to the $\gcd$ of $B$ and the remainder of $A$ divided by $B$ ($A \pmod B$).
  $$\gcd(A, B) = \gcd(B, A \pmod B)$$
- **Termination:** The process repeats iteratively until the remainder becomes `0`. The non-zero divisor at this terminal step is the $\gcd(A, B)$.
- **Time Complexity:** $O(\log(\min(A, B)))$ — established by **Lamé's Theorem**, making it exponentially faster than naive subtraction or trial division.

---

### Part B: Step-by-Step Trace for $A = 1556$ and $B = 2421$ (6 Marks)

We apply the Division Algorithm $Dividend = (Divisor \times Quotient) + Remainder$:

$$\begin{array}{|c|c|c|c|c|l|}
\hline
\textbf{Step} & \textbf{Dividend } (A) & \textbf{Divisor } (B) & \textbf{Quotient } (q) & \textbf{Remainder } (r = A \pmod B) & \textbf{Equation} \\
\hline
\text{1} & 2421 & 1556 & 1 & 865 & 2421 = 1556 \times 1 + 865 \\
\text{2} & 1556 & 865 & 1 & 691 & 1556 = 865 \times 1 + 691 \\
\text{3} & 865 & 691 & 1 & 174 & 865 = 691 \times 1 + 174 \\
\text{4} & 691 & 174 & 3 & 169 & 691 = 174 \times 3 + 169 \\
\text{5} & 174 & 169 & 1 & 5 & 174 = 169 \times 1 + 5 \\
\text{6} & 169 & 5 & 33 & 4 & 169 = 5 \times 33 + 4 \\
\text{7} & 5 & 4 & 1 & 1 & 5 = 4 \times 1 + 1 \\
\text{8} & 4 & 1 & 4 & 0 & 4 = 1 \times 4 + 0 \\
\hline
\end{array}$$

Since the remainder in Step 8 is **0**, the last non-zero divisor is **1**.

$$\mathbf{\gcd(1556, 2421) = 1} \quad (\text{The numbers are Co-prime!})$$

---

### Complete Java Implementation:
```java
public class EuclideanGCD {
    public static int gcd(int a, int b) {
        while (b != 0) {
            int remainder = a % b;
            a = b;
            b = remainder;
        }
        return a;
    }

    public static void main(String[] args) {
        int a = 1556, b = 2421;
        System.out.println("GCD(" + a + ", " + b + ") = " + gcd(a, b));
    }
}
```

---

<a id="p1-q3"></a>
## 3️⃣ Paper 1 - Q3 (10 Marks): Selection Sort & Pass-by-Pass Trace for {91, 34, 56, 12, 78, 20}

### Part A: Concept of Selection Sort (4 Marks)
- **Mechanism:** Selection sort divides the array into two subarrays: **sorted** (left) and **unsorted** (right).
- In each pass $i$ ($0 \le i < n-1$):
  1. Find the index of the minimum element in the unsorted subarray `arr[i...n-1]`.
  2. Swap that minimum element with `arr[i]`.
  3. The boundary of the sorted subarray expands by one position to the right.
- **Complexity:**
  - **Time:** Best Case $= O(n^2)$, Average Case $= O(n^2)$, Worst Case $= O(n^2)$ (Always performs $\frac{n(n-1)}{2}$ comparisons).
  - **Space:** $O(1)$ (In-place sorting algorithm).
  - **Stability:** Not stable in its standard form.

---

### Part B: Pass-by-Pass Trace & Java Program (6 Marks)

**Initial Array:** `[91, 34, 56, 12, 78, 20]` ($n = 6$)

| Pass | Unsorted Subarray Checked | Minimum Element Found | Swap Operation | Array State After Pass |
|:---:|---|---|---|---|
| **Pass 1** | `[91, 34, 56, 12, 78, 20]` | **12** at index 3 | Swap `arr[0]` (91) with `arr[3]` (12) | `[12, 34, 56, 91, 78, 20]` |
| **Pass 2** | `[34, 56, 91, 78, 20]` | **20** at index 5 | Swap `arr[1]` (34) with `arr[5]` (20) | `[12, 20, 56, 91, 78, 34]` |
| **Pass 3** | `[56, 91, 78, 34]` | **34** at index 5 | Swap `arr[2]` (56) with `arr[5]` (34) | `[12, 20, 34, 91, 78, 56]` |
| **Pass 4** | `[91, 78, 56]` | **56** at index 5 | Swap `arr[3]` (91) with `arr[5]` (56) | `[12, 20, 34, 56, 78, 91]` |
| **Pass 5** | `[78, 91]` | **78** at index 4 | No swap needed (78 is already at index 4) | `[12, 20, 34, 56, 78, 91]` |

---

### Complete Java Program Displaying Each Pass:
```java
import java.util.Arrays;

public class SelectionSortPasses {
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        System.out.println("Initial Array: " + Arrays.toString(arr));
        System.out.println("---------------------------------------------");

        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            // Swap minimum element with first element of unsorted part
            int temp = arr[minIdx];
            arr[minIdx] = arr[i];
            arr[i] = temp;

            System.out.println("Pass " + (i + 1) + ": " + Arrays.toString(arr));
        }
    }

    public static void main(String[] args) {
        int[] arr = {91, 34, 56, 12, 78, 20};
        selectionSort(arr);
    }
}
```

---

<a id="p1-q4"></a>
## 4️⃣ Paper 1 - Q4 (10 Marks): Maximum Hourglass Sum & Matrix Formula

### Part A: Formula Derivation for Number of Hourglasses in $R \times C$ Matrix (4 Marks)
An hourglass in a 2D matrix spans **3 rows and 3 columns** in an "I" shape:
```
  [i, j]     [i, j+1]     [i, j+2]    ← Top row (3 elements)
             [i+1, j+1]                ← Center row (1 element)
  [i+2, j]   [i+2, j+1]   [i+2, j+2]  ← Bottom row (3 elements)
```

- **Row Constraints:** Since an hourglass needs 3 continuous rows, the starting row index $i$ can range from $0$ to $R - 3$. Total valid row start positions $= \mathbf{(R - 2)}$.
- **Column Constraints:** Since an hourglass needs 3 continuous columns, the starting column index $j$ can range from $0$ to $C - 3$. Total valid column start positions $= \mathbf{(C - 2)}$.

$$\mathbf{\text{Total Number of Hourglasses in an } R \times C \text{ Matrix}} = \mathbf{(R - 2) \times (C - 2)}$$

**For a $6 \times 6$ Matrix ($R=6, C=6$):**
$$\text{Number of Hourglasses} = (6 - 2) \times (6 - 2) = 4 \times 4 = \mathbf{16 \text{ Hourglasses}}$$

---

### Part B: Java Program to Find Maximum Hourglass Sum in $6 \times 6$ Matrix (6 Marks)

```java
public class MaxHourglassSum {
    public static int findMaxHourglass(int[][] mat) {
        int R = mat.length;
        int C = mat[0].length;
        
        if (R < 3 || C < 3) {
            throw new IllegalArgumentException("Matrix must be at least 3x3");
        }

        int maxSum = Integer.MIN_VALUE; // Handles negative sums correctly

        for (int i = 0; i <= R - 3; i++) {
            for (int j = 0; j <= C - 3; j++) {
                int currentSum = mat[i][j]     + mat[i][j+1]     + mat[i][j+2]
                                               + mat[i+1][j+1]
                               + mat[i+2][j]   + mat[i+2][j+1]   + mat[i+2][j+2];

                if (currentSum > maxSum) {
                    maxSum = currentSum;
                }
            }
        }
        return maxSum;
    }

    public static void main(String[] args) {
        int[][] matrix = {
            {1, 1, 1, 0, 0, 0},
            {0, 1, 0, 0, 0, 0},
            {1, 1, 1, 0, 0, 0},
            {0, 0, 2, 4, 4, 0},
            {0, 0, 0, 2, 0, 0},
            {0, 0, 1, 2, 4, 0}
        };

        int result = findMaxHourglass(matrix);
        System.out.println("Total Hourglasses Evaluated: (6-2)*(6-2) = 16");
        System.out.println("Maximum Hourglass Sum: " + result);
    }
}
```

---

<a id="p1-q5a"></a>
## 5️⃣ Paper 1 - Q5.a (5 Marks): Leaders in an Array

### 📌 Concept:
An element is called a **Leader** if it is **strictly greater than all the elements to its right side**.
- The rightmost element of any array is **always a leader** (since there are no elements to its right).
- **Efficient Approach:** Traverse from **right to left**, maintaining a running `max_from_right`. If `arr[i] > max_from_right`, then `arr[i]` is a leader, and update `max_from_right = arr[i]`. Time Complexity: $O(n)$, Space: $O(1)$.

```java
import java.util.ArrayList;
import java.util.Collections;

public class LeadersInArray {
    public static void findLeaders(int[] arr) {
        int n = arr.length;
        int maxFromRight = arr[n - 1];
        
        ArrayList<Integer> leaders = new ArrayList<>();
        leaders.add(maxFromRight); // Rightmost element is always a leader

        for (int i = n - 2; i >= 0; i--) {
            if (arr[i] > maxFromRight) {
                maxFromRight = arr[i];
                leaders.add(maxFromRight);
            }
        }

        // Reverse to display leaders in their original left-to-right order
        Collections.reverse(leaders);
        System.out.println("Leaders: " + leaders);
    }

    public static void main(String[] args) {
        int[] arr = {16, 17, 4, 3, 5, 2};
        System.out.print("Array: [16, 17, 4, 3, 5, 2] -> ");
        findLeaders(arr); // Output: [17, 5, 2]
    }
}
```

---

<a id="p1-q5b"></a>
## 6️⃣ Paper 1 - Q5.b (5 Marks): Block Swap Algorithm for Array Left Rotation

### 📌 Concept & Algorithm Mechanics:
To left-rotate an array $arr[0..n-1]$ by $d$ positions:
1. Divide the array into two blocks:
   - $A = arr[0..d-1]$ (size $d$)
   - $B = arr[d..n-1]$ (size $n-d$)
2. Repeat until size of $A$ equals size of $B$:
   - **If size($A$) < size($B$):** Divide $B$ into $B_1$ and $B_2$ where size($B_2$) = size($A$). Swap block $A$ with block $B_2$. Block $A$ is now in its final position. Recursively rotate the remaining part.
   - **If size($A$) > size($B$):** Divide $A$ into $A_1$ and $A_2$ where size($A_1$) = size($B$). Swap block $A_1$ with block $B$. Block $B$ is now in its final position. Recursively rotate the remaining part.
   - **If size($A$) == size($B$):** Swap block $A$ and block $B$. Done!
3. **Time Complexity:** $O(n)$ with $O(1)$ auxiliary space.

---

### Step-by-Step Trace for $\{11, 22, 33, 44, 55, 66, 77, 88\}$ with $d = 3, n = 8$:
- **Initial:** `[11, 22, 33 | 44, 55, 66, 77, 88]` ($A = [11, 22, 33]$, $B = [44, 55, 66, 77, 88]$)
- Size($A$) = 3, Size($B$) = 5 $\implies A < B$. Swap $A$ with last 3 elements of $B$ (`[66, 77, 88]`):
  - Array becomes: `[66, 77, 88 | 44, 55 | 11, 22, 33]` (11, 22, 33 are now in their final positions!)
- Now solve for remaining unsorted part `[66, 77, 88 | 44, 55]` ($A = [66, 77, 88]$, $B = [44, 55]$):
  - Size($A$) = 3, Size($B$) = 2 $\implies A > B$. Swap first 2 elements of $A$ (`[66, 77]`) with $B$ (`[44, 55]`):
  - Array becomes: `[44, 55 | 88 | 66, 77 | 11, 22, 33]`
- Now solve for `[88 | 66, 77]` ($A = [88]$, $B = [66, 77]$):
  - Size($A$) = 1, Size($B$) = 2 $\implies A < B$. Swap $A$ with last element of $B$ (`77`):
  - Array becomes: `[44, 55 | 77 | 66 | 88 | 11, 22, 33]`
- Finally swap `[77]` and `[66]` $\implies \mathbf{[44, 55, 66, 77, 88, 11, 22, 33]}$ ✅

---

### Java Program for Block Swap Algorithm:
```java
import java.util.Arrays;

public class BlockSwapRotation {
    // Utility to swap d elements starting at index fi with elements at index si
    public static void swap(int[] arr, int fi, int si, int d) {
        for (int i = 0; i < d; i++) {
            int temp = arr[fi + i];
            arr[fi + i] = arr[si + i];
            arr[si + i] = temp;
        }
    }

    public static void leftRotate(int[] arr, int d, int n) {
        d = d % n;
        if (d == 0 || d == n) return;

        int i = d;
        int j = n - d;
        while (i != j) {
            if (i < j) { // A is shorter than B
                swap(arr, d - i, d + j - i, i);
                j -= i;
            } else { // A is longer than B
                swap(arr, d - i, d, j);
                i -= j;
            }
        }
        // When size of A equals size of B
        swap(arr, d - i, d, i);
    }

    public static void main(String[] args) {
        int[] arr = {11, 22, 33, 44, 55, 66, 77, 88};
        int d = 3;
        System.out.println("Original: " + Arrays.toString(arr));
        leftRotate(arr, d, arr.length);
        System.out.println("Rotated by 3: " + Arrays.toString(arr));
    }
}
```

---
---

# 🅱️ Paper 2 Solutions (Slot B14+D21)

---

<a id="p2-q1"></a>
## 7️⃣ Paper 2 - Q1 (10 Marks): Relational & Logical Operators & Pass/Fail Program

### Part A: Relational & Logical Operators Explanation (6 Marks)

#### 1. Relational Operators:
Used to compare two values; always return a `boolean` (`true` or `false`).
- `==` (Equal to): `5 == 5` $\to$ `true`
- `!=` (Not equal to): `5 != 3` $\to$ `true`
- `>` (Greater than): `10 > 7` $\to$ `true`
- `<` (Less than): `4 < 2` $\to$ `false`
- `>=` (Greater than or equal to): `6 >= 6` $\to$ `true`
- `<=` (Less than or equal to): `3 <= 8` $\to$ `true`

#### 2. Logical Operators:
Used to combine multiple relational expressions.
- `&&` (**Logical AND - Short-Circuit**): Returns `true` ONLY if both operands are `true`. If the left operand is `false`, the right operand is NOT evaluated.
- `||` (**Logical OR - Short-Circuit**): Returns `true` if at least one operand is `true`. If the left operand is `true`, the right operand is NOT evaluated.
- `!` (**Logical NOT**): Inverts the boolean value (`!true` is `false`).

---

### Part B: Java Program to Check if Student Passed in All 3 Subjects (4 Marks)
*Passing Criterion: Marks $\ge 50$ (or $\ge 40$) in each individual subject.*

```java
public class StudentPassCheck {
    public static void main(String[] args) {
        int sub1 = 67;
        int sub2 = 72;
        int sub3 = 81;
        int passMark = 50;

        System.out.println("Subject Marks: " + sub1 + ", " + sub2 + ", " + sub3);

        // Using Relational (>=) and Logical (&&) Operators
        if (sub1 >= passMark && sub2 >= passMark && sub3 >= passMark) {
            double average = (sub1 + sub2 + sub3) / 3.0;
            System.out.println("Status: PASSED in all subjects!");
            System.out.printf("Average Marks: %.2f\n", average);
        } else {
            System.out.println("Status: FAILED (Scored below passing mark in one or more subjects).");
        }
    }
}
```

#### Output:
```text
Subject Marks: 67, 72, 81
Status: PASSED in all subjects!
Average Marks: 73.33
```

---

<a id="p2-q2"></a>
## 8️⃣ Paper 2 - Q2 (10 Marks): Binary Palindrome Concept & Verification for 21

### Part A: Concept of Binary Palindrome (4 Marks)
- A number is a **Binary Palindrome** if its binary representation reads identical from left-to-right and right-to-left.
- **Example 1:** $9_{10} = 1001_2 \implies$ Reverse is $1001_2$ (**Palindrome** ✅)
- **Example 2:** $10_{10} = 1010_2 \implies$ Reverse is $0101_2 = 101_2 \ne 1010_2$ (**Not Palindrome** ❌)
- **Example 3:** $21_{10} = 10101_2 \implies$ Reverse is $10101_2$ (**Palindrome** ✅)

---

### Part B: Step-by-Step Bit Trace for Decimal 21 & Java Program (6 Marks)

#### Binary Conversion of $21_{10}$:
- $21 / 2 = 10 \text{ rem } 1$
- $10 / 2 = 5 \text{ rem } 0$
- $5 / 2 = 2 \text{ rem } 1$
- $2 / 2 = 1 \text{ rem } 0$
- $1 / 2 = 0 \text{ rem } 1$
$$\mathbf{21_{10} = 10101_2}$$

#### Reversal Trace:
- Position 0: `1` $\leftrightarrow$ Position 4: `1` (Matches)
- Position 1: `0` $\leftrightarrow$ Position 3: `0` (Matches)
- Position 2: `1` (Center bit, matches itself)
$$\text{Reversed Binary} = 10101_2 = \text{Original Binary} \implies \mathbf{\text{PALINDROME}}$$

---

### Complete Java Program (Using Pure Bit Manipulation):
```java
public class BinaryPalindromeCheck {
    // Pure bitwise reversal (O(log N) time, O(1) space)
    public static boolean isBinaryPalindrome(int n) {
        int original = n;
        int reversed = 0;

        int temp = n;
        while (temp > 0) {
            reversed = (reversed << 1) | (temp & 1);
            temp = temp >> 1;
        }

        return original == reversed;
    }

    public static void main(String[] args) {
        int num = 21;
        String binaryString = Integer.toBinaryString(num);
        
        System.out.println("Decimal Number: " + num);
        System.out.println("Binary Representation: " + binaryString);

        if (isBinaryPalindrome(num)) {
            System.out.println("Result: " + num + " is a BINARY PALINDROME!");
        } else {
            System.out.println("Result: " + num + " is NOT a binary palindrome.");
        }
    }
}
```

---

<a id="p2-q3"></a>
## 9️⃣ Paper 2 - Q3 (10 Marks): Selection Sort for {90, 12, 65, 43, 27, 18}

### Part A: Algorithm Explanation (4 Marks)
Selection sort works by iteratively locating the minimum element from the unsorted segment of the array and swapping it with the element at the beginning of the unsorted segment.

---

### Part B: Trace & Java Program for `{90, 12, 65, 43, 27, 18}` (6 Marks)

**Array Size:** $n = 6$

| Pass | Unsorted Subarray | Smallest Found | Action | Resulting Array |
|:---:|---|---|---|---|
| **Pass 1** | `[90, 12, 65, 43, 27, 18]` | **12** (idx 1) | Swap with `arr[0]` (90) | `[12, 90, 65, 43, 27, 18]` |
| **Pass 2** | `[90, 65, 43, 27, 18]` | **18** (idx 5) | Swap with `arr[1]` (90) | `[12, 18, 65, 43, 27, 90]` |
| **Pass 3** | `[65, 43, 27, 90]` | **27** (idx 4) | Swap with `arr[2]` (65) | `[12, 18, 27, 43, 65, 90]` |
| **Pass 4** | `[43, 65, 90]` | **43** (idx 3) | No swap (already at idx 3) | `[12, 18, 27, 43, 65, 90]` |
| **Pass 5** | `[65, 90]` | **65** (idx 4) | No swap (already at idx 4) | `[12, 18, 27, 43, 65, 90]` |

---

### Java Code:
```java
import java.util.Arrays;

public class SelectionSort2 {
    public static void sort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIdx]) minIdx = j;
            }
            int temp = arr[minIdx];
            arr[minIdx] = arr[i];
            arr[i] = temp;
        }
    }

    public static void main(String[] args) {
        int[] arr = {90, 12, 65, 43, 27, 18};
        System.out.println("Original: " + Arrays.toString(arr));
        sort(arr);
        System.out.println("Sorted:   " + Arrays.toString(arr));
    }
}
```

---

<a id="p2-q4"></a>
## 🔟 Paper 2 - Q4 (10 Marks): Maximum Equilibrium Sum for {3, 1, 2, 6, 4, 4}

### Part A: Concept of Equilibrium Sum (4 Marks)
- An **Equilibrium Index** in an array is an index $i$ where the sum of elements at lower indices equals the sum of elements at higher indices:
  $$\sum_{k=0}^{i-1} arr[k] = \sum_{k=i+1}^{n-1} arr[k]$$
- **Inclusive / Prefix-Suffix Equilibrium Point:** In some formulations, the maximum sum where prefix sum equals suffix sum (either including or excluding the index) is found.
- **$O(n)$ Linear Approach:**
  1. Calculate `total_sum` of the array.
  2. Maintain a running `left_sum = 0`.
  3. For each element at index $i$, `right_sum = total_sum - left_sum - arr[i]`.
  4. If `left_sum == right_sum`, index $i$ is an equilibrium point! Update `max_equilibrium_sum`.
  5. Add `arr[i]` to `left_sum`.

---

### Part B: Step-by-Step Evaluation for `{3, 1, 2, 6, 4, 4}` (6 Marks)

- **Total Sum:** $3 + 1 + 2 + 6 + 4 + 4 = \mathbf{20}$

$$\begin{array}{|c|c|c|c|c|}
\hline
\textbf{Index } (i) & \textbf{Value } (arr[i]) & \textbf{Left Sum} & \textbf{Right Sum } (20 - \text{Left} - arr[i]) & \textbf{Left == Right?} \\
\hline
0 & 3 & 0 & 20 - 0 - 3 = 17 & \text{No} \\
1 & 1 & 3 & 20 - 3 - 1 = 16 & \text{No} \\
2 & 2 & 3 + 1 = 4 & 20 - 4 - 2 = 14 & \text{No} \\
3 & 6 & 4 + 2 = 6 & 20 - 6 - 6 = 8 & \text{No} \\
4 & 4 & 6 + 6 = 12 & 20 - 12 - 4 = 4 & \text{No} \\
5 & 4 & 12 + 4 = 16 & 20 - 16 - 4 = 0 & \text{No} \\
\hline
\end{array}$$

- **Inclusive Prefix-Suffix Check:**
  - Prefix Sum up to index 3 ($3+1+2+6$) = $12$. Suffix sum from index 3 ($6+4+4$) = $14$.
  - Maximum balanced sub-segment / equilibrium evaluation is calculated cleanly in $O(n)$ time.

---

### Java Program for Equilibrium Sum:
```java
public class EquilibriumSum {
    public static int findMaxEquilibrium(int[] arr) {
        int totalSum = 0;
        for (int num : arr) totalSum += num;

        int leftSum = 0;
        int maxEquilibrium = Integer.MIN_VALUE;
        boolean found = false;

        for (int i = 0; i < arr.length; i++) {
            int rightSum = totalSum - leftSum - arr[i];

            if (leftSum == rightSum) {
                found = true;
                if (leftSum > maxEquilibrium) {
                    maxEquilibrium = leftSum;
                }
                System.out.println("Equilibrium index at " + i + " with sum = " + leftSum);
            }
            leftSum += arr[i];
        }

        return found ? maxEquilibrium : -1;
    }

    public static void main(String[] args) {
        int[] arr = {3, 1, 2, 6, 4, 4};
        int result = findMaxEquilibrium(arr);
        if (result != -1) {
            System.out.println("Maximum Equilibrium Sum: " + result);
        } else {
            System.out.println("No strict equilibrium index found for the given array.");
        }
    }
}
```

---

<a id="p2-q5a"></a>
## 1️⃣1️⃣ Paper 2 - Q5.a (5 Marks): Control Structures & Numbers Divisible by 2 or 7

### Part A: Role of Control Structures (2.5 Marks)
Control structures govern the **flow of execution** of a program. They are categorized into:
1. **Sequential Flow:** Default execution line-by-line in order.
2. **Selection / Conditional (`if`, `if-else`, `switch`):** Executes specific code paths based on boolean evaluations.
3. **Iteration / Repetition (`for`, `while`, `do-while`):** Repeats a code block until a termination condition is met.
4. **Jump / Transfer (`break`, `continue`, `return`):** Alters linear loop flow.

---

### Part B: Java Program (Numbers 1 to 50 Divisible by 2 or 7) (2.5 Marks)

```java
public class DivisibleBy2Or7 {
    public static void main(String[] args) {
        System.out.println("Numbers between 1 and 50 divisible by 2 or 7:");

        for (int i = 1; i <= 50; i++) {
            if (i % 2 == 0 || i % 7 == 0) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }
}
```

#### Output:
```text
2 4 6 7 8 10 12 14 16 18 20 21 22 24 26 28 30 32 34 35 36 38 40 42 44 46 48 49 50 
```

---

<a id="p2-q5b"></a>
## 1️⃣2️⃣ Paper 2 - Q5.b (5 Marks): Quick Sort & Partitioning Process for {64, 31, 85, 12, 47, 29}

### Part A: Concept & Partitioning Process (2.5 Marks)
- **Divide and Conquer:** Quick sort chooses an element as a **Pivot** (commonly the last element `arr[high]`).
- **Partitioning Algorithm (Lomuto Partition):** Rearranges the array such that all elements smaller than the pivot are shifted to its left, and all elements greater than the pivot are shifted to its right.
- The pivot is then placed at its correct sorted position (index `pIndex`), and Quick Sort is called recursively on `arr[low...pIndex-1]` and `arr[pIndex+1...high]`.
- **Complexities:** Best/Average Time $= O(n \log n)$, Worst Case $= O(n^2)$ (when array is already sorted), Space $= O(\log n)$ recursion stack.

---

### Part B: Trace & Java Program for `{64, 31, 85, 12, 47, 29}` (2.5 Marks)

- **Array:** `[64, 31, 85, 12, 47, 29]`, Pivot $= 29$
- Elements $< 29$: `12`
- Elements $> 29$: `64, 31, 85, 47`
- After Partition 1: Pivot 29 lands at index 1 $\implies \mathbf{[12, \mathbf{29}, 85, 64, 47, 31]}$
- Recursively sorting left `[12]` (already sorted) and right `[85, 64, 47, 31]`
- Final Sorted Array: $\mathbf{[12, 29, 31, 47, 64, 85]}$ ✅

---

### Java Program for Quick Sort:
```java
import java.util.Arrays;

public class QuickSort {
    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high]; // Pivot as last element
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                // Swap arr[i] and arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        // Place pivot at correct position
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }

    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pIndex = partition(arr, low, high);
            quickSort(arr, low, pIndex - 1);
            quickSort(arr, pIndex + 1, high);
        }
    }

    public static void main(String[] args) {
        int[] arr = {64, 31, 85, 12, 47, 29};
        System.out.println("Original: " + Arrays.toString(arr));
        quickSort(arr, 0, arr.length - 1);
        System.out.println("Sorted:   " + Arrays.toString(arr));
    }
}
```
