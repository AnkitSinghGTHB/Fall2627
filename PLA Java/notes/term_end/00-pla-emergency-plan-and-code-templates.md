# ⏱️ PLA1004: Emergency Study Plan & Master Code Blueprints

> **Exam Date**: Sunday, October 25, 2026 (01:15 PM – 04:15 PM)  
> 🚨 **Primary Resource**: Complete solutions for all 15 topics in [08-pla-tee-master-study-sheet-and-imp-topics.md](./08-pla-tee-master-study-sheet-and-imp-topics.md).

---

## 📅 3-Day TEE Battle Schedule

| Day | Focus Modules & Priority Topics | Target Goal |
|:---|:---|:---|
| **Day 1 (Thu, Oct 22)** | **Unit 1 & Unit 2**: Complexity, Swap Nibbles, Flip Bit, Segmented Sieve, Euler's Totient, Booth's Multiplier | Master bitwise hacks & hardware arithmetic (40 Marks) |
| **Day 2 (Fri, Oct 23)** | **Unit 3**: MinStack $O(1)$ space, Sliding Window, Floyd Cycle, Circular Queue, Move Hyphens, Equilibrium, Block Swap | Secure linear structures & array rotations (20 Marks) |
| **Day 3 (Sat, Oct 24)** | **Unit 4 & Unit 5**: Huffman Coding, Weighted Substring, $N$-Queens, Josephus, Hamiltonian, Knapsack, LCS, Kruskal, Tree Traversals + 1-Page Cheat Sheet Review | Master backtracking, trees, and DP algorithms (40 Marks) |

---

## 🎯 The 5 Master Java Code Blueprints

### Blueprint 1: Sliding Window Maximum using Monotonic Deque (Unit 3 - 12 Marks)
```java
import java.util.*;

public class SlidingWindowMax {
    public static int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || k <= 0) return new int[0];
        int n = nums.length;
        int[] result = new int[n - k + 1];
        Deque<Integer> deque = new ArrayDeque<>(); // Stores indices

        for (int i = 0; i < n; i++) {
            // Remove elements outside current sliding window [i - k + 1, i]
            while (!deque.isEmpty() && deque.peekFirst() < i - k + 1) {
                deque.pollFirst();
            }
            // Maintain monotonic decreasing order in deque
            while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i]) {
                deque.pollLast();
            }
            deque.offerLast(i);

            // Record maximum once first window of size k is formed
            if (i >= k - 1) {
                result[i - k + 1] = nums[deque.peekFirst()];
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, -1, -3, 5, 3, 6, 7};
        int k = 3;
        System.out.println("Max in each window: " + Arrays.toString(maxSlidingWindow(arr, k)));
    }
}
// Time: O(N), Auxiliary Space: O(K)
```
**Sample Input**: `nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3`  
**Sample Output**:
```text
Max in each window: [3, 3, 5, 5, 6, 7]
```

---

### Blueprint 2: Min Stack with $O(1)$ Extra Space $(2x - \text{min})$ (Unit 3 - 12 Marks)
```java
import java.util.Stack;

public class MinStackDemo {
    private Stack<Long> stack = new Stack<>();
    private long min;

    public void push(int val) {
        long x = val;
        if (stack.isEmpty()) {
            stack.push(x);
            min = x;
        } else if (x < min) {
            stack.push(2 * x - min); // Encode smaller value
            min = x;
        } else {
            stack.push(x);
        }
    }

    public void pop() {
        if (stack.isEmpty()) return;
        long top = stack.pop();
        if (top < min) {
            min = 2 * min - top; // Recover previous minimum
        }
    }

    public int top() {
        long top = stack.peek();
        return top < min ? (int) min : (int) top;
    }

    public int getMin() {
        return (int) min;
    }

    public static void main(String[] args) {
        MinStackDemo ms = new MinStackDemo();
        ms.push(10);
        ms.push(5);
        ms.push(12);
        System.out.println("Min: " + ms.getMin());
        ms.pop();
        ms.pop();
        System.out.println("Min after pops: " + ms.getMin());
    }
}
// Time: O(1) for all operations, Auxiliary Space: O(1)
```
**Sample Output**:
```text
Min: 5
Min after pops: 10
```

---

### Blueprint 3: Segmented Sieve of Eratosthenes (Unit 2 - 12 Marks)
```java
import java.util.*;

public class SegmentedSieveDemo {
    public static List<Integer> primesInRange(int L, int R) {
        int limit = (int) Math.sqrt(R);
        boolean[] isPrime = new boolean[limit + 1];
        Arrays.fill(isPrime, true);
        List<Integer> basePrimes = new ArrayList<>();
        for (int p = 2; p <= limit; p++) {
            if (isPrime[p]) {
                basePrimes.add(p);
                for (int i = p * p; i <= limit; i += p) isPrime[i] = false;
            }
        }

        boolean[] range = new boolean[R - L + 1];
        Arrays.fill(range, true);
        for (int p : basePrimes) {
            int firstMultiple = Math.max(p * p, ((L + p - 1) / p) * p);
            for (int j = firstMultiple; j <= R; j += p) {
                range[j - L] = false;
            }
        }
        if (L == 1) range[0] = false;

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i <= R - L; i++) {
            if (range[i] && (L + i) > 1) result.add(L + i);
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println("Primes in [10, 50]: " + primesInRange(10, 50));
    }
}
```
**Sample Input**: `L = 10, R = 50`  
**Sample Output**:
```text
Primes in [10, 50]: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

---

### Blueprint 4: Booth's Multiplication Algorithm for Signed Binary (Unit 2 - 12 Marks)
```java
public class BoothsAlgorithm {
    public static int multiply(int m, int r) {
        int A = m;      // Multiplicand
        int Q = r;      // Multiplier
        int Q_1 = 0;    // Auxiliary bit
        int count = 8;  // Assuming 8-bit operands
        int accumulator = 0;

        while (count > 0) {
            int q0 = Q & 1;
            if (q0 == 1 && Q_1 == 0) {
                accumulator -= A; // Subtraction on 10
            } else if (q0 == 0 && Q_1 == 1) {
                accumulator += A; // Addition on 01
            }
            // Arithmetic Shift Right [accumulator, Q, Q_1]
            int combined = (accumulator << 9) | ((Q & 0xFF) << 1) | Q_1;
            combined >>= 1;
            Q_1 = combined & 1;
            Q = (combined >> 1) & 0xFF;
            accumulator = combined >> 9;
            count--;
        }
        return (accumulator << 8) | (Q & 0xFF);
    }

    public static void main(String[] args) {
        int a = 7, b = -5;
        System.out.println(a + " * " + b + " = " + multiply(a, b));
    }
}
```
**Sample Input**: `7, -5`  
**Sample Output**:
```text
7 * -5 = -35
```

---

### Blueprint 5: $N$-Queens with Bitmasking (Unit 4 - 12 Marks)
```java
public class NQueensBitmask {
    static int count = 0;

    public static int totalNQueens(int n) {
        count = 0;
        solve(0, 0, 0, (1 << n) - 1);
        return count;
    }

    private static void solve(int cols, int diag1, int diag2, int mask) {
        if (cols == mask) {
            count++;
            return;
        }
        int valid = mask & ~(cols | diag1 | diag2);
        while (valid != 0) {
            int bit = valid & -valid; // Extract lowest set bit
            valid -= bit;
            solve(cols | bit, (diag1 | bit) << 1, (diag2 | bit) >> 1, mask);
        }
    }

    public static void main(String[] args) {
        int n = 4;
        System.out.println("Distinct solutions for " + n + "-Queens: " + totalNQueens(n));
    }
}
```
**Sample Input**: `4`  
**Sample Output**:
```text
Distinct solutions for 4-Queens: 2
```
