# 📘 Unit 4: Greedy Algorithms, Huffman Coding & Backtracking

---

## 1. Greedy Choice Principle & Activity Selection

The Greedy Choice Property dictates that an optimal global solution can be reached by making a locally optimal choice at each step without reconsidering past decisions.

### 1.1 Activity Selection Problem ($O(N \log N)$)
Given $N$ activities with start times $s_i$ and finish times $f_i$, find the maximum number of mutually compatible activities.
* **Greedy Strategy**: Always select the activity with the **earliest finish time** that does not conflict with previously chosen activities.

```java
import java.util.*;

class Activity {
    int start, finish;
    Activity(int s, int f) { this.start = s; this.finish = f; }
}

public class ActivitySelection {
    public static List<Activity> maxActivities(List<Activity> list) {
        // Step 1: Sort activities by finish time ascending
        list.sort(Comparator.comparingInt(a -> a.finish));

        List<Activity> selected = new ArrayList<>();
        selected.add(list.get(0));
        int lastFinish = list.get(0).finish;

        // Step 2: Iterate and greedily pick non-conflicting activities
        for (int i = 1; i < list.size(); i++) {
            if (list.get(i).start >= lastFinish) {
                selected.add(list.get(i));
                lastFinish = list.get(i).finish;
            }
        }
        return selected;
    }
}
```

---

## 2. Huffman Coding (Greedy Compression Tree)

Builds an optimal prefix-free variable-length binary encoding using a **Min-Priority Queue**:
1. Insert all characters and their frequencies as leaf nodes into a Min-Heap.
2. While heap size $> 1$:
   - Extract two nodes with minimum frequencies: $L$ and $R$.
   - Create internal node with frequency $= \text{freq}(L) + \text{freq}(R)$, left child $= L$, right child $= R$.
   - Insert new internal node back into heap.
3. Root node represents the completed Huffman Tree. Left edges represent `'0'`, right edges represent `'1'`.
* **Prefix-Free Property**: No codeword is a prefix of any other codeword, ensuring instantaneous unambiguous decoding.

---

## 3. Backtracking: $N$-Queens with Bitmasking

Standard 2D array placement requires $O(N)$ validation at each queen placement. Bitmasking reduces this check to **$O(1)$ bitwise operations**:

```java
public class NQueensSolver {
    static int solutionCount = 0;

    public static int solve(int n) {
        solutionCount = 0;
        int allDone = (1 << n) - 1; // n bits set to 1
        backtrack(0, 0, 0, allDone);
        return solutionCount;
    }

    private static void backtrack(int cols, int d1, int d2, int allDone) {
        if (cols == allDone) {
            solutionCount++;
            return;
        }
        // Valid positions are bits that are 0 in cols, d1, and d2
        int valid = allDone & ~(cols | d1 | d2);
        while (valid != 0) {
            int bit = valid & -valid; // Pick lowest available 1
            valid -= bit;
            backtrack(cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1, allDone);
        }
    }
}
```

---

## 4. The Josephus Problem (Elimination Trap)

$n$ people stand in a circle numbered $0$ to $n-1$. In each step, the $k$-th person is eliminated until only 1 survivor remains.

### 4.1 Mathematical Recurrence Relation
$$J(n, k) = (J(n-1, k) + k) \pmod n, \quad \text{with base case } J(1, k) = 0$$

```java
public static int josephusSurvivor(int n, int k) {
    int survivor = 0; // J(1, k) = 0 (0-indexed)
    for (int i = 2; i <= n; i++) {
        survivor = (survivor + k) % i;
    }
    return survivor + 1; // Return 1-indexed position
}
// Time Complexity: O(N), Space Complexity: O(1)
```

---

## 5. Model Exam Questions & Answers

### Question 1 (12 Marks)
**Construct the Huffman Tree for characters with frequencies: $A: 5, B: 9, C: 12, D: 13, E: 16, F: 45$. Derive the binary codeword for each character and compute the average bits per character.**

**Solution**:
1. **Min-Heap Merge Steps**:
   - Initial Heap: `[A:5, B:9, C:12, D:13, E:16, F:45]`.
   - Merge $A(5)$ and $B(9) \implies N_1(14)$. Heap: `[C:12, D:13, N1:14, E:16, F:45]`.
   - Merge $C(12)$ and $D(13) \implies N_2(25)$. Heap: `[N1:14, E:16, N2:25, F:45]`.
   - Merge $N_1(14)$ and $E(16) \implies N_3(30)$. Heap: `[N2:25, N3:30, F:45]`.
   - Merge $N_2(25)$ and $N_3(30) \implies N_4(55)$. Heap: `[F:45, N4:55]`.
   - Merge $F(45)$ and $N_4(55) \implies \text{Root}(100)$.
2. **Codewords Assigned**:
   - $F$: `0` (Length $= 1$)
   - $C$: `100` (Length $= 3$)
   - $D$: `101` (Length $= 3$)
   - $E$: `111` (Length $= 3$)
   - $A$: `1100` (Length $= 4$)
   - $B$: `1101` (Length $= 4$)
3. **Average Bits per Character**:
   $$\text{Avg} = \frac{45(1) + 12(3) + 13(3) + 16(3) + 5(4) + 9(4)}{100}$$
   $$= \frac{45 + 36 + 39 + 48 + 20 + 36}{100} = \frac{224}{100} = \mathbf{2.24\text{ bits/char}}$$
   *(Fixed-length encoding would require $\lceil \log_2 6 \rceil = 3$ bits. Huffman achieves $(3 - 2.24)/3 = \mathbf{25.3\%}$ compression!).*

### Question 2 (8 Marks)
**Explain Warnsdorff's Heuristic for solving the Knight's Tour problem. Why is it superior to blind backtracking?**

**Solution**:
1. **Warnsdorff's Rule**: In any current knight position, evaluate all valid unvisited L-shaped moves. Move the knight to the square that has the **minimum number of onward accessible unvisited squares** (lowest out-degree).
2. **Why it Prevents Blind Backtracking**:
   - By prioritizing squares with few exits early, the knight visits difficult-to-reach corner/edge squares before they become stranded and isolated.
   - Reduces the exponential $O(8^{N^2})$ search space of blind backtracking to a nearly linear $O(N^2)$ direct path without getting trapped.
