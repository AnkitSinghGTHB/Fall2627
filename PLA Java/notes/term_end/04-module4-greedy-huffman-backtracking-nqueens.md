# 📘 Unit 4: Greedy Algorithms, Huffman Coding & Backtracking

> **Aligned with VIT Bhopal October 2026 TEE Papers**: Slots A11, B14, F11, E11  
> **Unit Weight in TEE**: Exactly 20 Marks (12M in Section A + 8M in Section B)

---

## 1. Greedy Principles & Scheduling

### 1.1 Activity Selection Problem ($O(N \log N)$)
*(Paper 2 Q3b & Paper 3 Q3b — 6 Marks)*

* **Greedy Choice Property**: Sort activities by **finish time ascending**. Greedily pick the next activity that does not conflict (`start >= lastFinish`).

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
}
```

---

### 1.2 Minimum Meeting Rooms Required (Greedy Interval Scheduling)
*(Paper 1 Q3b — 6 Marks)*

Given meeting intervals: $(0, 30), (5, 10), (8, 12), (15, 20), (25, 35)$. Find the minimum number of conference rooms required.

```java
import java.util.*;

public class MeetingRooms {
    public static int minRooms(int[][] intervals) {
        int n = intervals.length;
        int[] start = new int[n];
        int[] end = new int[n];

        for (int i = 0; i < n; i++) {
            start[i] = intervals[i][0];
            end[i] = intervals[i][1];
        }

        Arrays.sort(start);
        Arrays.sort(end);

        int rooms = 0, maxRooms = 0;
        int s = 0, e = 0;

        while (s < n) {
            if (start[s] < end[e]) {
                rooms++; // Meeting starts before earliest finishes -> Allocate new room
                maxRooms = Math.max(maxRooms, rooms);
                s++;
            } else {
                rooms--; // Meeting finished -> Room freed
                e++;
            }
        }
        return maxRooms;
    }

    public static void main(String[] args) {
        int[][] meetings = {{0, 30}, {5, 10}, {8, 12}, {15, 20}, {25, 35}};
        System.out.println("Minimum Rooms: " + minRooms(meetings));
    }
}
```

#### Chronological Event Trace:
- Sorted Start Times: $[0, 5, 8, 15, 25]$
- Sorted End Times: $[10, 12, 20, 30, 35]$

| Time | Event | Active Meetings | Rooms Needed |
|:---:|:---|:---:|:---:|
| 0 | Meeting $(0, 30)$ starts | 1 | 1 |
| 5 | Meeting $(5, 10)$ starts | 2 | 2 |
| 8 | Meeting $(8, 12)$ starts | 3 | **3 (PEAK)** |
| 10 | Meeting $(5, 10)$ finishes | 2 | 2 |
| 12 | Meeting $(8, 12)$ finishes | 1 | 1 |
| 15 | Meeting $(15, 20)$ starts | 2 | 2 |
| 20 | Meeting $(15, 20)$ finishes | 1 | 1 |
| 25 | Meeting $(25, 35)$ starts | 2 | 2 |
| 30 | Meeting $(0, 30)$ finishes | 1 | 1 |
| 35 | Meeting $(25, 35)$ finishes | 0 | 0 |

* **Final Answer**: **3 Meeting Rooms Required**. Time: $O(N \log N)$, Space: $O(N)$.

---

## 2. Huffman Coding: Construction & Step-by-Step Decoding

### 2.1 Step-by-Step Decoding Working
*(Paper 4 Q3b — 6 Marks)*

* **Codewords**: $A = \text{"0"}$, $B = \text{"10"}$, $C = \text{"110"}$, $D = \text{"1110"}$, $E = \text{"1111"}$
* **Encoded Bit String**: `'11101100101111'`

#### Prefix-Matching Working:
1. `1110` matches $D \implies$ **Symbol D** (Remaining: `'1100101111'`)
2. `110` matches $C \implies$ **Symbol C** (Remaining: `'0101111'`)
3. `0` matches $A \implies$ **Symbol A** (Remaining: `'101111'`)
4. `10` matches $B \implies$ **Symbol B** (Remaining: `'1111'`)
5. `1111` matches $E \implies$ **Symbol E** (Remaining: `''`)
* **Decoded Output**: **`"DCABE"`**.

---

### 2.2 Huffman Construction & Telemetry Bandwidth Calculation
*(Paper 3 Q3a, Sample Paper Q2)*

* Frequencies: $S: 32, F: 23, T: 10, P: 10, E: 5$.
* Merges: $E(5)+P(10) \to 15$; $T(10)+15 \to 25$; $F(23)+25 \to 48$; $S(32)+48 \to \text{Root}(80)$.
* Average bit length $= \mathbf{2.1\text{ bits/char}}$ vs $3\text{ bits}$ fixed. Bandwidth savings $= \mathbf{30.0\%}$.

---

## 3. Weighted Substring Problems

### 3.1 Substring of Length $K$ with Maximum Alphabetical Weight
*(Paper 4 Q3c — 12 Marks)*

Given string $S$, character weight $= \text{alphabet position}$ ($a=1, \dots, z=26$). Find substring of fixed length $K$ having maximum weight.

```java
public class MaxWeightSubstring {
    public static String maxWeightSubstring(String s, int k) {
        int n = s.length();
        if (n < k) return "";

        int currentWeight = 0;
        for (int i = 0; i < k; i++) currentWeight += (s.charAt(i) - 'a' + 1);

        int maxWeight = currentWeight;
        int bestStart = 0;

        for (int i = k; i < n; i++) {
            currentWeight += (s.charAt(i) - 'a' + 1) - (s.charAt(i - k) - 'a' + 1);
            if (currentWeight > maxWeight) {
                maxWeight = currentWeight;
                bestStart = i - k + 1;
            }
        }
        return s.substring(bestStart, bestStart + k);
    }

    public static void main(String[] args) {
        String s = "abcadeaf";
        int k = 3;
        System.out.println("Max weight substring of length 3: " + maxWeightSubstring(s, k));
    }
}
```
**Trace for $S = \text{"abcadeaf"}, K = 3$**:
- Weights: $a=1, b=2, c=3, d=4, e=5, f=6$.
- `"abc"` $= 1+2+3=6$; `"bca"` $= 2+3+1=6$; `"cad"` $= 3+1+4=8$; `"ade"` $= 1+4+5=10$; `"dea"` $= 4+5+1=10$; `"eaf"` $= 5+1+6=\mathbf{12\text{ (MAX)}}$.
- **Result**: **`"eaf"`** with Weight $= 12$. Time: $O(N)$, Space: $O(1)$.

---

### 3.2 Greedy Floor Search for Target Weight $K$
*(Priority Topic 6 — `L28- Weightes substring.pptx`)*

* Weight Recurrence: $W(0) = 1 ('A')$; $W(i) = (i+2) W(i-1)$ for $i \ge 1$.
* Greedily subtract largest character weight $\le K$, reverse result for lexicographical order.

---

## 4. Backtracking: $N$-Queens & State-Space Pruning

### 4.1 Pruning Efficiency Analysis: Backtracking vs $4^4 = 256$ Brute Force
*(Paper 1 Q8 & Paper 4 Q3a — 8 Marks)*

* **Brute Force (No Pruning)**:
  - Placing 4 queens on an $4 \times 4$ board without constraints explores $4 \times 4 \times 4 \times 4 = 4^4 = \mathbf{256\text{ states}}$.
* **Backtracking (Smart Pruning)**:
  - Immediately rejects invalid partial boards (prunes subtrees whenever two queens share a row, column, or diagonal).
  - Only **17 nodes** are visited in the search tree. Over **93.3% of the search space is eliminated**!

```java
public class NQueensSolver {
    static int count = 0;

    public static int solve(int n) {
        count = 0;
        backtrack(0, 0, 0, (1 << n) - 1);
        return count;
    }

    private static void backtrack(int cols, int d1, int d2, int allDone) {
        if (cols == allDone) { count++; return; }
        int valid = allDone & ~(cols | d1 | d2);
        while (valid != 0) {
            int bit = valid & -valid;
            valid -= bit;
            backtrack(cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1, allDone);
        }
    }

    public static void main(String[] args) {
        System.out.println("Distinct solutions for 4-Queens: " + solve(4)); // 2
    }
}
```

---

## 5. Hamiltonian Cycle Backtracking
*(Paper 4 Q5b/c — 12 Marks; Priority Topic 9)*

### Worked Example for 5 Vertices $\{A, B, C, D, E\}$:
* **Edges**: $\{A\text{--}B, B\text{--}C, C\text{--}D, D\text{--}E, E\text{--}A, A\text{--}C, B\text{--}D\}$.
* **Backtracking Process**:
  1. Fix start vertex at $A$. Path: $[A]$.
  2. Visit neighbor $B$ (safe). Path: $[A, B]$.
  3. Neighbors of $B$ are $A$ (visited), $C$, $D$. Try $C$. Path: $[A, B, C]$.
  4. Neighbors of $C$ are $B, A$ (visited), $D$. Try $D$. Path: $[A, B, C, D]$.
  5. Neighbors of $D$ are $C, B$ (visited), $E$. Try $E$. Path: $[A, B, C, D, E]$.
  6. All 5 vertices visited! Check if edge exists between last vertex $E$ and start vertex $A$:
     - Edge $E\text{--}A$ exists in the graph!
* **Hamiltonian Cycle Found**: **`A -> B -> C -> D -> E -> A`**.

---

## 6. Josephus Elimination Recurrence
*(Paper 1 Q3a, Paper 2 Q3a — 6 Marks)*

$$J(n, k) = (J(n-1, k) + k) \pmod n, \quad \text{with } J(1, k) = 0$$

```java
public class Josephus {
    public static int getSurvivor(int n, int k) {
        int s = 0;
        for (int i = 2; i <= n; i++) s = (s + k) % i;
        return s + 1; // 1-indexed
    }

    public static void main(String[] args) {
        System.out.println("Survivor for n=8, k=3: Person " + getSurvivor(8, 3)); // Person 7
        System.out.println("Survivor for n=8, k=4: Person " + getSurvivor(8, 4)); // Person 6
    }
}
```
* For $n = 8, k = 3 \implies$ **Survivor is Person 7**.
* For $n = 8, k = 4 \implies$ **Survivor is Person 6**. Time: $O(N)$, Space: $O(1)$.

---

## 7. Fractional Knapsack vs 0/1 Knapsack: Greedy Choice Justification
*(Paper 5 Q3b — 6 Marks)*

* **Items**: $I_1(\text{wt}=10, \text{val}=60, \text{ratio}=6.0), I_2(\text{wt}=20, \text{val}=100, \text{ratio}=5.0), I_3(\text{wt}=30, \text{val}=120, \text{ratio}=4.0)$. Capacity $W = 50$.
* **Fractional Knapsack Execution**:
  1. Take all of $I_1$ (wt 10, val 60). Remaining capacity $= 40$.
  2. Take all of $I_2$ (wt 20, val 100). Remaining capacity $= 20$.
  3. Take $\frac{20}{30} = \frac{2}{3}$ fraction of $I_3$ (wt 20, val $\frac{2}{3} \times 120 = 80$).
  * **Total Optimal Value**: $60 + 100 + 80 = \mathbf{240}$.
* **Why Ordering by Ratio Fails for 0/1 Knapsack**:
  - In $0/1$ knapsack, items cannot be broken. Picking $I_1$ (ratio 6.0) leaves only room for $I_2$ for a total value of $160$ (wasting 20 capacity).
  - But picking $I_2$ and $I_3$ yields weight $20+30=50$ and total value $100+120 = \mathbf{220} > 160$!
  - Therefore, the greedy choice property **fails for 0/1 Knapsack** because empty space cannot be filled with partial items (requires Dynamic Programming).

---

## 8. Job Sequencing with Deadlines (Greedy)
*(Paper 5 Q8 — 8 Marks)*

Given jobs: $J_1(d=2, p=100), J_2(d=1, p=19), J_3(d=2, p=27), J_4(d=1, p=25), J_5(d=3, p=15)$. Each job takes 1 unit of time.

* **Greedy Strategy**:
  1. Sort jobs by **profit descending**: $J_1(100), J_3(27), J_4(25), J_2(19), J_5(15)$.
  2. Maximum deadline is $3 \implies$ 3 time slots available: Slot 1 ($0-1$), Slot 2 ($1-2$), Slot 3 ($2-3$).
  3. Schedule each job at the **latest available slot $\le$ deadline**:
     - $J_1$ (deadline 2) $\to$ Slot 2.
     - $J_3$ (deadline 2) $\to$ Slot 1 (latest free slot $\le 2$).
     - $J_4$ (deadline 1) $\to$ Slot 1 is already taken. Cannot schedule!
     - $J_2$ (deadline 1) $\to$ Slot 1 is already taken. Cannot schedule!
     - $J_5$ (deadline 3) $\to$ Slot 3.
* **Scheduled Sequence**: $[J_3, J_1, J_5]$. **Total Profit**: $27 + 100 + 15 = \mathbf{142}$.
* **Why Ordering by Profit is Optimal**: Greedily securing high profits and pushing their execution as late as possible preserves earlier slots for more urgent tasks.

---

## 9. Rat in a Maze Backtracking ($4 \times 4$ Maze)
*(Paper 5 Q3a — 6 Marks)*

Maze:
```
1 1 0 0
0 1 1 0
0 1 0 0
0 1 1 1
```
* Movements allowed: **Right** and **Down** only.
* **Trace of Dead Ends & Backtracking**:
  1. $(0,0) \to (0,1)$
  2. From $(0,1)$, Right $(0,2)$ is blocked ($0$). Go Down $\to (1,1)$.
  3. From $(1,1)$, Right $\to (1,2)$. But from $(1,2)$, Right $(1,3)$ and Down $(2,2)$ are blocked ($0$). **Dead end! Backtrack to $(1,1)$!**
  4. From $(1,1)$, try Down $\to (2,1)$.
  5. From $(2,1)$, Right $(2,2)$ is blocked ($0$). Try Down $\to (3,1)$.
  6. From $(3,1)$, Right $\to (3,2) \to (3,3)$ (**Destination reached!**).
* **Final Solution Path**: **`(0,0) -> (0,1) -> (1,1) -> (2,1) -> (3,1) -> (3,2) -> (3,3)`**.
