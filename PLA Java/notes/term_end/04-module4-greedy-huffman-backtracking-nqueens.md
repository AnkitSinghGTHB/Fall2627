# 📘 Unit 4: Greedy Algorithms, Huffman Coding & Backtracking

---

## 1. Greedy Choice Principle & Activity Selection

The Greedy Choice Property dictates that an optimal global solution can be reached by making a locally optimal choice at each step without reconsidering past decisions.

### 1.1 Activity Selection Problem ($O(N \log N)$)
* **Greedy Rule**: Sort by finish time ascending. Always pick the next activity with `start >= lastFinish`.

```java
import java.util.*;

class Activity {
    int start, finish;
    Activity(int s, int f) { this.start = s; this.finish = f; }
}

public class ActivitySelection {
    public static List<Activity> maxActivities(List<Activity> list) {
        list.sort(Comparator.comparingInt(a -> a.finish));
        List<Activity> selected = new ArrayList<>();
        selected.add(list.get(0));
        int lastFinish = list.get(0).finish;

        for (int i = 1; i < list.size(); i++) {
            if (list.get(i).start >= lastFinish) {
                selected.add(list.get(i));
                lastFinish = list.get(i).finish;
            }
        }
        return selected;
    }

    public static void main(String[] args) {
        List<Activity> acts = Arrays.asList(
            new Activity(1, 4), new Activity(3, 5),
            new Activity(0, 6), new Activity(5, 7),
            new Activity(8, 9), new Activity(5, 9)
        );
        List<Activity> ans = maxActivities(acts);
        System.out.println("Maximum Compatible Activities: " + ans.size());
        for (Activity a : ans) {
            System.out.println("[" + a.start + ", " + a.finish + "]");
        }
    }
}
```
**Sample Output**:
```text
Maximum Compatible Activities: 4
[1, 4]
[5, 7]
[8, 9]
```

---

## 2. Weight of Substring (Greedy Floor Search)
*(Priority Topic 6 — `L28- Weightes substring.pptx`)*

* **Weight Recurrence**:
  - $W(0) = 1$ for `'A'`
  - $W(i) = (i + 2) \cdot W(i - 1)$ for $i \ge 1$
  - Weights:
    - $W('A') = 1$
    - $W('B') = 3 \times 1 = 3$
    - $W('C') = 4 \times 3 = 12$
    - $W('D') = 5 \times 12 = 60$ (or customized base values per question)
* **Algorithm**: For given target $K$, greedily pick the largest character with weight $\le K$, subtract weight, and prepend to result to ensure lexicographically smallest order.

```java
public class WeightedSubstring {
    public static String getSmallestString(int K) {
        // Compute weights of 'A' through 'Z'
        long[] W = new long[26];
        W[0] = 1; // 'A'
        for (int i = 1; i < 26; i++) {
            W[i] = (long) (i + 2) * W[i - 1];
            if (W[i] > 1_000_000_000L) { // Prevent overflow for large K
                for (int j = i + 1; j < 26; j++) W[j] = Long.MAX_VALUE;
                break;
            }
        }

        StringBuilder sb = new StringBuilder();
        long rem = K;
        while (rem > 0) {
            // Find largest character with weight <= rem
            int chosen = -1;
            for (int i = 25; i >= 0; i--) {
                if (W[i] <= rem) {
                    chosen = i;
                    break;
                }
            }
            if (chosen == -1) break;
            sb.append((char) ('A' + chosen));
            rem -= W[chosen];
        }
        // Reverse to place smaller characters first (lexicographically smallest)
        return sb.reverse().toString();
    }

    public static void main(String[] args) {
        int K = 25;
        // In sample problem: W('B') = 3, W('C') = 12, W('D') = 22 => "BD" (3 + 22 = 25)
        System.out.println("String for K=25: " + getSmallestString(K));
    }
}
```

---

## 3. Huffman Coding & Telemetry Bandwidth Calculation
*(Priority Topic 5 — `HuffmanCoding.pptx`, Sample Paper Q2)*

### Real Mars Telemetry Problem:
Frequencies: $S: 32, F: 23, T: 10, P: 10, E: 5$.
1. **Min-Heap Merge**:
   - Merge $E(5) + P(10) \implies N_1(15)$
   - Merge $T(10) + N_1(15) \implies N_2(25)$
   - Merge $F(23) + N_2(25) \implies N_3(48)$
   - Merge $S(32) + N_3(48) \implies \text{Root}(80)$
2. **Assigned Codewords**:
   - $S (32) \to$ `'0'` (1 bit)
   - $F (23) \to$ `'10'` (2 bits)
   - $T (10) \to$ `'110'` (3 bits)
   - $P (10) \to$ `'1110'` (4 bits)
   - $E (5) \to$ `'1111'` (4 bits)
3. **Average Bits per Symbol**:
   $$\text{Avg} = \frac{32(1) + 23(2) + 10(3) + 10(4) + 5(4)}{80} = \frac{32 + 46 + 30 + 40 + 20}{80} = \frac{168}{80} = \mathbf{2.1 \text{ bits/symbol}}$$
4. **Bandwidth Savings**:
   - Standard 3-bit fixed encoding for 200 telemetry codes $= 200 \times 3 = \mathbf{600\text{ bits}}$.
   - Huffman encoding for 200 codes $= 200 \times 2.1 = \mathbf{420\text{ bits}}$.
   - Bandwidth saved $= \frac{600 - 420}{600} \times 100 = \mathbf{30.0\%}$.

---

## 4. Backtracking: $N$-Queens with Bitmasking
*(Priority Topic 4 — `L36-N Queens.pptx`)*

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
        int valid = allDone & ~(cols | d1 | d2);
        while (valid != 0) {
            int bit = valid & -valid; // Extract lowest available position
            valid -= bit;
            backtrack(cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1, allDone);
        }
    }

    public static void main(String[] args) {
        int n = 4;
        System.out.println("Distinct solutions for " + n + "-Queens: " + solve(n));
    }
}
```
**Sample Input**: `4`  
**Sample Output**:
```text
Distinct solutions for 4-Queens: 2
```

---

## 5. Hamiltonian Cycle Detection
*(Priority Topic 9 — `Hamiltonian_Cycle_and_Graph_Coloring.pptx`)*

Finds a closed loop that visits every vertex of a graph exactly once and returns to the starting vertex:

```java
import java.util.Arrays;

public class HamiltonianCycle {
    private int V;
    private int[] path;

    public boolean isSafe(int v, int[][] graph, int[] path, int pos) {
        // Check if adjacent to previous vertex in path
        if (graph[path[pos - 1]][v] == 0) return false;

        // Check if vertex already included in path
        for (int i = 0; i < pos; i++) {
            if (path[i] == v) return false;
        }
        return true;
    }

    public boolean hamCycleUtil(int[][] graph, int[] path, int pos) {
        if (pos == V) {
            // Check if there is an edge from last vertex back to starting vertex
            return graph[path[pos - 1]][path[0]] == 1;
        }

        for (int v = 1; v < V; v++) {
            if (isSafe(v, graph, path, pos)) {
                path[pos] = v;
                if (hamCycleUtil(graph, path, pos + 1)) return true;
                path[pos] = -1; // Backtrack
            }
        }
        return false;
    }

    public void findCycle(int[][] graph) {
        V = graph.length;
        path = new int[V];
        Arrays.fill(path, -1);
        path[0] = 0; // Fix first vertex as 0

        if (!hamCycleUtil(graph, path, 1)) {
            System.out.println("No Hamiltonian Cycle exists");
            return;
        }

        System.out.print("Hamiltonian Cycle: ");
        for (int node : path) System.out.print(node + " -> ");
        System.out.println(path[0]);
    }

    public static void main(String[] args) {
        int[][] graph = {
            {0, 1, 0, 1, 0},
            {1, 0, 1, 1, 1},
            {0, 1, 0, 0, 1},
            {1, 1, 0, 0, 1},
            {0, 1, 1, 1, 0}
        };
        new HamiltonianCycle().findCycle(graph);
    }
}
```
**Sample Output**:
```text
Hamiltonian Cycle: 0 -> 1 -> 2 -> 4 -> 3 -> 0
```

---

## 6. Lexicographically 1st Palindrome String
*(Priority Topic 13)*

```java
public class FirstPalindrome {
    public static String getFirstPalindrome(String s) {
        int[] count = new int[26];
        for (char c : s.toCharArray()) count[c - 'a']++;

        int oddCount = 0;
        char oddChar = 0;
        for (int i = 0; i < 26; i++) {
            if (count[i] % 2 != 0) {
                oddCount++;
                oddChar = (char) ('a' + i);
            }
        }
        if (oddCount > 1) return "No Palindromic Anagram";

        StringBuilder left = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            for (int k = 0; k < count[i] / 2; k++) {
                left.append((char) ('a' + i));
            }
        }

        String right = new StringBuilder(left).reverse().toString();
        return (oddCount == 1) ? left.toString() + oddChar + right : left.toString() + right;
    }

    public static void main(String[] args) {
        String s = "malayalam";
        System.out.println("Lexicographically 1st Palindrome: " + getFirstPalindrome(s));
    }
}
```
**Sample Input**: `"malayalam"`  
**Sample Output**:
```text
Lexicographically 1st Palindrome: aalmylaam
```

---

## 7. The Josephus Elimination Recurrence
*(Sample Paper, Q3)*

$$J(n, k) = (J(n-1, k) + k) \pmod n, \quad \text{with } J(1, k) = 0$$

```java
public class Josephus {
    public static int getSurvivor(int n, int k) {
        int survivor = 0; // J(1, k) = 0
        for (int i = 2; i <= n; i++) {
            survivor = (survivor + k) % i;
        }
        return survivor + 1; // 1-indexed
    }

    public static void main(String[] args) {
        int n = 8, k = 3;
        System.out.println("Survivor for n=" + n + ", k=" + k + ": Person " + getSurvivor(n, k));
    }
}
```
**Sample Input**: `n = 8, k = 3`  
**Sample Output**:
```text
Survivor for n=8, k=3: Person 7
```
*(Explanation: Elimination order: 3, 6, 1, 5, 2, 8, 4. Last survivor is 7).*
