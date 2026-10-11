# ⏱️ PLA1004: Emergency Study Plan & Master Code Blueprints

> **Exam Date**: Sunday, October 25, 2026 (01:15 PM – 04:15 PM)  
> **Pre-TEE Position**: +2.0 marks ahead of class! Needs only **65–68 / 100** in TEE for A Grade.  
> **Study Window**: Thursday, Oct 22 to Saturday, Oct 24 (3 Full Gap Days!)

---

## 🎯 The 5 Master Java Code Blueprints (Guaranteed 60+ Marks)

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
}
// Time: O(N), Space: O(K)
```

---

### Blueprint 2: Min Stack with $O(1)$ Extra Space $(2x - \text{min})$ (Unit 3 - 12 Marks)
```java
import java.util.Stack;

class MinStack {
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
}
// Time: O(1) for all operations, Auxiliary Space: O(1)
```

---

### Blueprint 3: Segmented Sieve of Eratosthenes (Unit 2 - 12 Marks)
```java
import java.util.*;

public class SegmentedSieve {
    public static List<Integer> primesInRange(int L, int R) {
        int limit = (int) Math.sqrt(R);
        // Step 1: Find all primes up to sqrt(R) using simple sieve
        boolean[] isPrime = new boolean[limit + 1];
        Arrays.fill(isPrime, true);
        List<Integer> primes = new ArrayList<>();
        for (int p = 2; p <= limit; p++) {
            if (isPrime[p]) {
                primes.add(p);
                for (int i = p * p; i <= limit; i += p) isPrime[i] = false;
            }
        }

        // Step 2: Mark non-primes in range [L, R]
        boolean[] range = new boolean[R - L + 1];
        Arrays.fill(range, true);
        for (int p : primes) {
            int firstMultiple = Math.max(p * p, ((L + p - 1) / p) * p);
            for (int j = firstMultiple; j <= R; j += p) {
                range[j - L] = false;
            }
        }
        if (L == 1) range[0] = false;

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i <= R - L; i++) {
            if (range[i]) result.add(L + i);
        }
        return result;
    }
}
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
}
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
        // Valid positions are bits that are 0 in all 3 masks
        int valid = mask & ~(cols | diag1 | diag2);
        while (valid != 0) {
            int bit = valid & -valid; // Extract lowest set bit
            valid -= bit;
            solve(cols | bit, (diag1 | bit) << 1, (diag2 | bit) >> 1, mask);
        }
    }
}
// Massive speedup over standard 2D array backtracking!
```
