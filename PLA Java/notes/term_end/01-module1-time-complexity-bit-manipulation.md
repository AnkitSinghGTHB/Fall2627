# 📘 Unit 1: Programming Foundations, Complexity Analysis & Basic Algorithms

> **Aligned with VIT Bhopal PLA1004 Syllabus & TEE Papers (Slots A11, B14, F11, E11, A21)**  
> **Exam Paper Mapping**:
> - **PART A**: **Question 1** (12 Marks — with internal choice `OR`)
> - **PART B**: **Question 6** (8 Marks — direct implementation)  
> **Total Unit Weight in TEE**: **Exactly 20 Marks**

---

# PART 1: SECTION A QUESTIONS (12 MARKS) [Question 1 Pool]

---

## 1. Asymptotic Notations & Formal Definitions
*(Foundational Theory for Q1)*

* **Big-$O$ ($O$) — Asymptotic Upper Bound**:
  $$f(n) = O(g(n)) \iff \exists \; c > 0, n_0 > 0 \text{ such that } 0 \le f(n) \le c \cdot g(n) \; \forall \; n \ge n_0$$
  Guarantees the algorithm will never take more time than this bound (worst-case ceiling).
* **Big-$\Omega$ ($\Omega$) — Asymptotic Lower Bound**:
  $$f(n) = \Omega(g(n)) \iff \exists \; c > 0, n_0 > 0 \text{ such that } 0 \le c \cdot g(n) \le f(n) \; \forall \; n \ge n_0$$
  Guarantees the minimum time an algorithm requires (best-case floor).
* **Big-$\Theta$ ($\Theta$) — Asymptotically Tight Bound**:
  $$f(n) = \Theta(g(n)) \iff \exists \; c_1, c_2 > 0, n_0 > 0 \text{ such that } c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n) \; \forall \; n \ge n_0$$
  Represents exact growth rate when upper and lower bounds match.

---

## 2. High-Frequency Exam Loop Complexity Traces
*(Paper 4 Q1a-i, Q1a-ii, Q1b-ii — 6 to 12 Marks)*

### 2.1 Geometric Series Inner Bound Loop
```java
for (i = 1; i <= n; i = i * 2) {
    for (j = 1; j <= i; j++) {
        print(j);
    }
}
```
* **Analysis & Proof**:
  - Outer loop variable $i$ takes values $2^0, 2^1, 2^2, \dots, 2^k \le n$ where $k = \lfloor \log_2 n \rfloor$.
  - For each step $i$, inner loop runs exactly $i$ times.
  - Sum of operations is a geometric progression:
    $$\text{Total Steps} = \sum_{p=0}^{\lfloor \log_2 n \rfloor} 2^p = 1 + 2 + 4 + 8 + \dots + 2^k = 2^{k+1} - 1 < 2n = \mathbf{O(n)}$$
* **Complexity**: Time Complexity is **$O(n)$ (Linear Time)**, NOT $O(n^2)$ or $O(n \log n)$! Auxiliary Space: $O(1)$.

### 2.2 Halving Double Loop
```java
int count = 0;
for (int i = 1; i < n; i = i * 2) {
    for (int j = n; j > 0; j = j / 2) {
        count++;
    }
}
```
* **Analysis**:
  - Outer loop doubles: $i \in \{1, 2, 4, \dots, < n\} \implies \lceil \log_2 n \rceil$ iterations.
  - Inner loop halves: $j \in \{n, \lfloor n/2 \rfloor, \lfloor n/4 \rfloor, \dots, 1\} \implies (\lfloor \log_2 n \rfloor + 1)$ iterations.
  - Total Operations: $O(\log n) \times O(\log n) = \mathbf{O(\log^2 n)}$. Space: $\mathbf{O(1)}$.
* **Execution Trace for $N = 16$**:
  - Outer values: $i = 1, 2, 4, 8$ (4 iterations).
  - Inner values: $j = 16, 8, 4, 2, 1$ (5 iterations).
  - Cumulative `count` $= 4 \times 5 = \mathbf{20}$.

### 2.3 Recursive Fibonacci Recurrence
```java
int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
```
* **Analysis**:
  - Recurrence: $T(n) = T(n - 1) + T(n - 2) + O(1)$.
  - The recursion generates a binary call tree of height $n$.
  - Total recursive calls: $2^0 + 2^1 + 2^2 + \dots + 2^n \approx 2^{n+1} - 1 = \mathbf{O(2^n)}$ (Exponential Time).
  - Auxiliary Space: $\mathbf{O(n)}$ due to maximum call stack depth reaching $n$.

---

## 3. Master Theorem for Divide-and-Conquer Recurrences
*(Essential for Recurrence Solving in Q1)*

$$T(n) = a T(n/b) + f(n), \quad \text{where } a \ge 1, b > 1$$

Compare $f(n)$ with watershed boundary $n^{\log_b a}$:
1. **Case 1**: If $f(n) = O(n^{\log_b a - \epsilon})$ for some $\epsilon > 0 \implies \mathbf{T(n) = \Theta(n^{\log_b a})}$.
2. **Case 2**: If $f(n) = \Theta(n^{\log_b a} \log^k n)$ for $k \ge 0 \implies \mathbf{T(n) = \Theta(n^{\log_b a} \log^{k+1} n)}$.
   - Example: $T(n) = 4T(n/2) + n^2 \log n \implies n^{\log_2 4} = n^2 \implies T(n) = \mathbf{\Theta(n^2 \log^2 n)}$.
   - Example: $T(n) = 2T(n/2) + O(n)$ (Merge Sort) $\implies n^{\log_2 2} = n^1 \implies T(n) = \mathbf{\Theta(n \log n)}$.
3. **Case 3**: If $f(n) = \Omega(n^{\log_b a + \epsilon})$ and regularity condition holds ($a f(n/b) \le c f(n)$) $\implies \mathbf{T(n) = \Theta(f(n))}$.

---

## 4. Binary Search: Complexity & Execution Trace
*(Paper 1 Q1b — 12 Marks)*

```java
public class BinarySearchDemo {
    public static int binarySearch(int[] a, int l, int r, int key) {
        while (l <= r) {
            int mid = l + (r - l) / 2; // Prevents integer overflow
            if (a[mid] == key) {
                return mid; // Key found
            } else if (a[mid] < key) {
                l = mid + 1; // Search right half
            } else {
                r = mid - 1; // Search left half
            }
        }
        return -1; // Key not present
    }

    public static void main(String[] args) {
        int[] arr = {2, 5, 8, 12, 16, 23, 38, 45, 56, 72};
        System.out.println("Search 23: Index " + binarySearch(arr, 0, arr.length - 1, 23));
        System.out.println("Search 50: Index " + binarySearch(arr, 0, arr.length - 1, 50));
    }
}
```

#### Step-by-Step Execution Traces on Array $\{2, 5, 8, 12, 16, 23, 38, 45, 56, 72\}$:
1. **Searching for Key = 23**:
   - $l=0, r=9 \implies \text{mid} = 0 + (9-0)/2 = 4$. $a[4] = 16 < 23 \implies l = 5$.
   - $l=5, r=9 \implies \text{mid} = 5 + (9-5)/2 = 7$. $a[7] = 45 > 23 \implies r = 6$.
   - $l=5, r=6 \implies \text{mid} = 5 + (6-5)/2 = 5$. $a[5] = 23 == 23 \implies$ **Found at Index 5!**
2. **Searching for Key = 50**:
   - $l=0, r=9 \implies \text{mid} = 4, a[4] = 16 < 50 \implies l = 5$.
   - $l=5, r=9 \implies \text{mid} = 7, a[7] = 45 < 50 \implies l = 8$.
   - $l=8, r=9 \implies \text{mid} = 8, a[8] = 56 > 50 \implies r = 7$.
   - $l = 8 > r = 7 \implies$ Loop terminates. **Return -1 (Not Found)**.
* **Complexities**:
  - Best-Case Time: $O(1)$ (key matches initial midpoint).
  - Average & Worst-Case Time: $O(\log n)$.
  - Auxiliary Space: Iterative $= O(1)$, Recursive $= O(\log n)$ (call stack).

---

## 5. Insertion Sort: Complexity Analysis & Element Shift Trace
*(Paper 5 Q1b — 12 Marks)*

```java
public class InsertionSortDemo {
    public static int insertionSort(int[] a) {
        int n = a.length;
        int totalShifts = 0;

        for (int i = 1; i < n; i++) {
            int key = a[i];
            int j = i - 1;

            // Move elements of a[0..i-1] that are greater than key one position ahead
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

| Pass $i$ | Key $a[i]$ | Action & Shifts | Array State After Pass | Shifts in Pass | Cumulative Shifts |
|:---:|:---:|:---|:---|:---:|:---:|
| **Initial** | — | Array before sorting | `[5, 2, 4, 6, 1, 3]` | 0 | 0 |
| **Pass 1** ($i=1$) | **2** | $5 > 2 \implies$ shift $5$ right to index 1. Place $2$ at index 0. | `[2, 5, 4, 6, 1, 3]` | 1 | 1 |
| **Pass 2** ($i=2$) | **4** | $5 > 4 \implies$ shift $5$ right. $2 \le 4 \implies$ stop. Place $4$ at index 1. | `[2, 4, 5, 6, 1, 3]` | 1 | 2 |
| **Pass 3** ($i=3$) | **6** | $5 \le 6 \implies$ loop condition fails immediately. No shift. | `[2, 4, 5, 6, 1, 3]` | 0 | 2 |
| **Pass 4** ($i=4$) | **1** | $6 > 1, 5 > 1, 4 > 1, 2 > 1 \implies$ shift all 4 elements right. Place $1$ at index 0. | `[1, 2, 4, 5, 6, 3]` | 4 | 6 |
| **Pass 5** ($i=5$) | **3** | $6 > 3, 5 > 3, 4 > 3 \implies$ shift $6, 5, 4$ right. $2 \le 3 \implies$ stop. Place $3$ at index 2. | `[1, 2, 3, 4, 5, 6]` | 3 | **9** |

* **Total Element Shifts**: **9 Shifts**.
* **Complexity & Best/Worst Case Derivations**:
  - **Best-Case Time ($O(n)$)**: Occurs when the array is **already sorted in ascending order**. The condition `a[j] > key` fails on the very first comparison for every $i$. Total comparisons $= n - 1$, element shifts $= \mathbf{0}$.
  - **Worst-Case Time ($O(n^2)$)**: Occurs when the array is **sorted in reverse descending order**. Every element shifts past all preceding elements: $\sum_{i=1}^{n-1} i = \frac{n(n-1)}{2}$ shifts.
  - **Space Complexity ($O(1)$)**: Strictly in-place.

---

## 6. Armstrong Numbers Between $m$ and $n$
*(Paper 4 Q1b-i — 6 Marks)*

An integer is an Armstrong number if the sum of its digits raised to the power of the number of digits equals the number itself (e.g., $153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$).

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

## 7. Move All Hyphens to the Beginning
*(Paper 2 Q1a — 12 Marks)*

### Problem Statement:
Given a string containing characters and hyphens (`'-'`), move all hyphens to the beginning of the string while strictly preserving the relative order of all non-hyphen characters.

---

### Approach 1: Intuitive Two-String / StringBuilder Method (Recommended for Exams)
This is the simplest, most natural, and error-proof way to solve this in an exam:
1. Create two `StringBuilder` instances: `hyphens` (to store all `'-'`) and `letters` (to store all normal characters).
2. Traverse the input string character by character:
   - If the character is `'-'`, append it to `hyphens`.
   - Otherwise, append it to `letters`.
3. Combine and return: `hyphens.append(letters).toString()`.

```java
public class MoveHyphensSimple {
    public static String moveHyphens(String str) {
        StringBuilder hyphens = new StringBuilder();
        StringBuilder letters = new StringBuilder();

        for (char c : str.toCharArray()) {
            if (c == '-') {
                hyphens.append(c);
            } else {
                letters.append(c);
            }
        }

        return hyphens.append(letters).toString();
    }

    public static void main(String[] args) {
        String input1 = "face-prep";
        System.out.println("Input:  \"" + input1 + "\"");
        System.out.println("Output: \"" + moveHyphens(input1) + "\""); // "-faceprep"

        String input2 = "a-b-c-d";
        System.out.println("Input:  \"" + input2 + "\"");
        System.out.println("Output: \"" + moveHyphens(input2) + "\""); // "---abcd"
    }
}
```

#### Step-by-Step Execution Trace on `"face-prep"`:
- Characters read from left to right:
  - `'f'` $\to$ `letters = "f"`
  - `'a'` $\to$ `letters = "fa"`
  - `'c'` $\to$ `letters = "fac"`
  - `'e'` $\to$ `letters = "face"`
  - `'-'` $\to$ `hyphens = "-"`
  - `'p'` $\to$ `letters = "facep"`
  - `'r'` $\to$ `letters = "facepr"`
  - `'e'` $\to$ `letters = "facepre"`
  - `'p'` $\to$ `letters = "faceprep"`
- Combine `hyphens + letters` $\implies$ `"-faceprep"`.
* **Complexities**: Time: $O(N)$ (single pass), Space: $O(N)$ (linear auxiliary space).

---

### Approach 2: In-Place Backward Pointer Method (Only if $O(1)$ Space is Explicitly Requested)
If the question specifically specifies "do not use extra memory / do it in $O(1)$ auxiliary space":
1. Traverse the character array from right to left using a write pointer `writeIndex = n - 1`.
2. When a non-hyphen character is seen, write it to `s[writeIndex]` and decrement `writeIndex`.
3. Fill remaining positions from index $0$ to `writeIndex` with `'-'`.

```java
public class MoveHyphensInPlace {
    public static String moveHyphensInPlace(char[] s) {
        int n = s.length;
        int writeIndex = n - 1;

        for (int i = n - 1; i >= 0; i--) {
            if (s[i] != '-') {
                s[writeIndex--] = s[i];
            }
        }

        while (writeIndex >= 0) {
            s[writeIndex--] = '-';
        }

        return new String(s);
    }
}
```
* **Complexities**: Time: $O(N)$, Auxiliary Space: $O(1)$.

---

## 8. Strobogrammatic Numbers: Generation of Length $N$ & Rotational Check
*(Paper 1 Q1a, Paper 2 Q1b, Paper 3 Q1b — 12 Marks)*

### Definition & Rotational Mappings:
A number is strobogrammatic if it appears identical when rotated $180^\circ$.
* Valid pairs: `(0, 0)`, `(1, 1)`, `(8, 8)`, `(6, 9)`, `(9, 6)`.
* Single middle digits (for odd length): `'0'`, `'1'`, `'8'`.

### Part A: Generate All Strobogrammatic Numbers of Length $N$ (Middle Outwards):
```java
import java.util.*;

public class StrobogrammaticGenerator {
    public static List<String> findStrobogrammatic(int n) {
        return helper(n, n);
    }

    private static List<String> helper(int n, int totalLength) {
        // Base cases
        if (n == 0) return new ArrayList<>(Arrays.asList(""));
        if (n == 1) return new ArrayList<>(Arrays.asList("0", "1", "8"));

        // Recursively build inner sub-numbers of length n - 2
        List<String> subList = helper(n - 2, totalLength);
        List<String> result = new ArrayList<>();

        for (String s : subList) {
            // Digit '0' cannot be placed in the outermost pair of the final number
            if (n != totalLength) {
                result.add("0" + s + "0");
            }
            result.add("1" + s + "1");
            result.add("6" + s + "9");
            result.add("8" + s + "8");
            result.add("9" + s + "6");
        }
        return result;
    }

    public static void main(String[] args) {
        int n = 3;
        List<String> res = findStrobogrammatic(n);
        System.out.println("Strobogrammatic numbers of length " + n + ": " + res);
        System.out.println("Total Count: " + res.size());
    }
}
```

#### Analytical Evaluations Required in Exam:
1. **Numbers Produced for $N = 3$**:
   - For $n = 1$, base sub-numbers: `["0", "1", "8"]`.
   - Wrapping outer pairs (excluding `"0"` on outside since $n = totalLength = 3$):
     - Wrapped with `"1...1"`: `"101"`, `"111"`, `"181"`.
     - Wrapped with `"6...9"`: `"609"`, `"619"`, `"689"`.
     - Wrapped with `"8...8"`: `"808"`, `"818"`, `"888"`.
     - Wrapped with `"9...6"`: `"906"`, `"916"`, `"986"`.
   - **Complete List for $N = 3$ (12 numbers)**:
     `["101", "609", "808", "906", "111", "619", "818", "916", "181", "689", "888", "986"]`.
2. **Evaluation (Middle-Outwards vs Brute-Force Checking)**:
   - *Brute-Force*: Checking every $N$-digit number requires inspecting $9 \times 10^{N-1}$ integers. For $N = 8$, that is $90,000,000$ checks!
   - *Building from Middle*: Generates only valid strobogrammatic numbers directly in $O(5^{N/2})$ time, avoiding $99.99\%$ wasted checks.
3. **Justification of why digit `0` cannot be in the outermost pair**:
   - If `'0'` is placed at the outermost boundary, the resulting number has a leading zero (e.g., `"010"`), which mathematically reduces it to a 2-digit number ($10$), violating the length $N$ constraint.

---

## 9. Student Grade Evaluation & Decision Making
*(Paper 4 Q1a-i — 6 Marks)*

```java
import java.util.Scanner;

public class StudentGradeCalculator {
    public static void evaluateGrade(int m1, int m2, int m3) {
        // Individual subject passing criteria: minimum 40 in each subject
        if (m1 < 40 || m2 < 40 || m3 < 40) {
            System.out.println("Result: Failed (Individual subject score below passing threshold 40)");
            System.out.println("Grade:  F");
            return;
        }

        double average = (m1 + m2 + m3) / 3.0;
        char grade;

        if (average >= 90) {
            grade = 'O';
        } else if (average >= 80) {
            grade = 'A';
        } else if (average >= 70) {
            grade = 'B';
        } else if (average >= 60) {
            grade = 'C';
        } else if (average >= 50) {
            grade = 'D';
        } else {
            grade = 'P';
        }

        System.out.printf("Average Marks: %.2f | Result: Passed | Grade: %c\n", average, grade);
    }

    public static void main(String[] args) {
        evaluateGrade(92, 88, 95); // High scorer
        evaluateGrade(75, 68, 80); // First class
        evaluateGrade(85, 35, 90); // Failed in one subject
    }
}
```

---
---

# PART 2: SECTION B QUESTIONS (8 MARKS) [Question 6 Pool]

---

## 7. Day of the Week Display using Switch-Case & Fall-Through Analysis
*(Paper 1 Q6 — 8 Marks)*

```java
import java.util.Scanner;

public class DayOfWeek {
    public static void displayDay(int day) {
        // Normal version with break statements
        System.out.print("Standard Output for day " + day + ": ");
        switch (day) {
            case 1: System.out.println("Monday - Weekday"); break;
            case 2: System.out.println("Tuesday - Weekday"); break;
            case 3: System.out.println("Wednesday - Weekday"); break;
            case 4: System.out.println("Thursday - Weekday"); break;
            case 5: System.out.println("Friday - Weekday"); break;
            case 6: System.out.println("Saturday - Weekend"); break;
            case 7: System.out.println("Sunday - Weekend"); break;
            default: System.out.println("Invalid day entered!");
        }
    }

    public static void traceFallThrough(int day) {
        System.out.println("Output without 'break' statements for input " + day + ":");
        switch (day) {
            case 1: System.out.println("Monday");
            case 2: System.out.println("Tuesday");
            case 3: System.out.println("Wednesday");
            case 4: System.out.println("Thursday");
            case 5: System.out.println("Friday");
            case 6: System.out.println("Saturday");
            case 7: System.out.println("Sunday");
            default: System.out.println("Invalid / Fallthrough End");
        }
    }

    public static void main(String[] args) {
        displayDay(6);
        displayDay(9);
        System.out.println("-------------------------------------------");
        traceFallThrough(6);
    }
}
```

#### Analytical Answers Required in Exam:
1. **Output for Input $9$**: `"Invalid day entered!"` (matches `default` case).
2. **Behavior when all `break` statements are removed**:
   - In Java, `switch-case` exhibits **fall-through**: execution continues into subsequent cases regardless of their case values until the switch block ends.
   - For **Input $6$**, execution jumps to `case 6` and executes all remaining lines:
     ```text
     Saturday
     Sunday
     Invalid / Fallthrough End
     ```

---

## 8. Quadratic Equation Roots Solver & Decision Flow
*(Paper 5 Q6 — 8 Marks)*

```java
public class QuadraticRootsSolver {
    public static void solveQuadratic(double a, double b, double c) {
        if (a == 0) {
            System.out.println("Not a quadratic equation (a cannot be 0).");
            return;
        }

        // Calculate discriminant D = b^2 - 4ac
        double discriminant = (b * b) - (4 * a * c);

        System.out.printf("Equation: (%.0f)x^2 + (%.0f)x + (%.0f) = 0 | D = %.2f\n", a, b, c, discriminant);

        if (discriminant > 0) {
            // Branch 1: Real and Distinct Roots
            double root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
            double root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
            System.out.printf("Branch Executed: Real and Distinct | Roots: x1 = %.2f, x2 = %.2f\n", root1, root2);
        } else if (discriminant == 0) {
            // Branch 2: Real and Equal Roots
            double root = -b / (2 * a);
            System.out.printf("Branch Executed: Real and Equal | Roots: x1 = x2 = %.2f\n", root);
        } else {
            // Branch 3: Imaginary (Complex Conjugates)
            double realPart = -b / (2 * a);
            double imagPart = Math.sqrt(-discriminant) / (2 * a);
            System.out.printf("Branch Executed: Imaginary (Complex) | Roots: %.2f ± %.2fi\n", realPart, imagPart);
        }
        System.out.println("---------------------------------------------------------------");
    }

    public static void main(String[] args) {
        solveQuadratic(1, -5, 6);
        solveQuadratic(1, 2, 1);
        solveQuadratic(1, 2, 5);
    }
}
```

#### Decision Flow & Test Case Analysis:

| Coefficients $(a, b, c)$ | Discriminant Calculation $D = b^2 - 4ac$ | Sign of $D$ | Decision Branch Executed | Roots Computed |
|:---|:---|:---:|:---|:---|
| **Case 1**: $(1, -5, 6)$ | $(-5)^2 - 4(1)(6) = 25 - 24 = \mathbf{1}$ | $D > 0$ | **Branch 1 (Real & Distinct)** | $x_1 = \frac{5 + 1}{2} = \mathbf{3.0}$, $x_2 = \frac{5 - 1}{2} = \mathbf{2.0}$ |
| **Case 2**: $(1, 2, 1)$ | $(2)^2 - 4(1)(1) = 4 - 4 = \mathbf{0}$ | $D == 0$ | **Branch 2 (Real & Equal)** | $x_1 = x_2 = \frac{-2}{2} = \mathbf{-1.0}$ |
| **Case 3**: $(1, 2, 5)$ | $(2)^2 - 4(1)(5) = 4 - 20 = \mathbf{-16}$ | $D < 0$ | **Branch 3 (Imaginary / Complex)** | $\text{Real} = -1.0, \text{Imag} = \frac{\sqrt{16}}{2} = 2.0 \implies \mathbf{-1.0 \pm 2.0i}$ |

* **Complexity**: Time: $O(1)$, Space: $O(1)$.

---

## 9. Prime Sieves: Simple Sieve & Segmented Sieve
*(Paper 3 Q6 & Paper 4 Q6 — 8 Marks)*

### 9.1 Simple Sieve of Eratosthenes ($O(N \log \log N)$)
```java
import java.util.*;

public class SimpleSieve {
    public static List<Integer> simpleSieve(int n) {
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;

        for (int p = 2; p * p <= n; p++) {
            if (isPrime[p]) {
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
        System.out.println("Primes up to 30: " + simpleSieve(30));
    }
}
```
**Sample Output**: `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`

### 9.2 Segmented Sieve for Large Ranges $[L, R]$ ($R \le 10^9, R - L \le 10^6$)
#### Why Segmented Sieve is Preferred for Large Ranges:
* **Memory Limitation of Simple Sieve**: When $R = 10^9$, allocating a boolean array of size $10^9$ takes $\approx 1\text{ GB}$ contiguous memory, causing a fatal `OutOfMemoryError`.
* **Segmented Sieve Advantage**: Any composite number $x \le R$ has at least one prime factor $p \le \sqrt{R}$. Since $\sqrt{10^9} \approx 31,622$, we only generate base primes up to $31,622$. Then we allocate an array of size $(R - L + 1) \le 10^6$ (takes only $\approx 1\text{ MB}$ memory) and cross multiples of the base primes!

```java
import java.util.*;

public class SegmentedSieve {
    public static List<Long> segmentedSieve(long L, long R) {
        int limit = (int) Math.sqrt(R);

        // Step 1: Base primes up to sqrt(R) using simple sieve
        boolean[] base = new boolean[limit + 1];
        Arrays.fill(base, true);
        for (int p = 2; p * p <= limit; p++) {
            if (base[p]) {
                for (int i = p * p; i <= limit; i += p) base[i] = false;
            }
        }
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= limit; i++) if (base[i]) primes.add(i);

        // Step 2: Mark non-primes in range [L, R]
        int rangeSize = (int) (R - L + 1);
        boolean[] isPrime = new boolean[rangeSize];
        Arrays.fill(isPrime, true);

        for (int p : primes) {
            // Find first multiple of p >= L
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

## 13. Binary Palindrome Verification
*(Paper 2 Q6 — 8 Marks)*

### Problem Statement:
Write an algorithm and Java program to check whether a given integer's binary representation is a palindrome.

### Algorithmic Logic:
1. Extract the binary representation of the given integer $N$ by collecting bits from right to left using bitwise operations (`n & 1` and `n >>= 1`), or convert to binary string / reverse bits.
2. Compare the reversed bit sequence with the original bit sequence.
3. If the bits match reading forwards and backwards, output that it is a Binary Palindrome; otherwise, it is not.

```java
public class BinaryPalindromeCheck {
    public static boolean isBinaryPalindrome(int n) {
        String bin = Integer.toBinaryString(n);
        int l = 0, r = bin.length() - 1;

        while (l < r) {
            if (bin.charAt(l) != bin.charAt(r)) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    public static void checkAndDisplay(int n) {
        String bin = Integer.toBinaryString(n);
        boolean result = isBinaryPalindrome(n);
        System.out.printf("Number: %d | Binary: %s | Is Binary Palindrome? %s\n", n, bin, result ? "YES" : "NO");
    }

    public static void main(String[] args) {
        checkAndDisplay(9);   // 1001_2 -> Palindrome
        checkAndDisplay(27);  // 11011_2 -> Palindrome
        checkAndDisplay(10);  // 1010_2 -> Not palindrome
        checkAndDisplay(25);  // 11001_2 -> Not palindrome
    }
}
```

#### Step-by-Step Execution Trace:
| Integer $N$ | Binary Form | Reversed Binary | Comparison ($L \dots R$) | Result |
|:---:|:---:|:---:|:---|:---:|
| **9** | `1001` | `1001` | `1==1`, `0==0` | **YES (Palindrome)** |
| **27** | `11011` | `11011` | `1==1`, `1==1`, `0==0` | **YES (Palindrome)** |
| **10** | `1010` | `0101` | `1 != 0` (mismatch at index 0) | **NO** |
| **25** | `11001` | `10011` | `1==1`, `1 != 0` (mismatch at index 1) | **NO** |

* **Complexities**: Time: $O(\log N)$ (proportional to number of bits), Auxiliary Space: $O(1)$.

