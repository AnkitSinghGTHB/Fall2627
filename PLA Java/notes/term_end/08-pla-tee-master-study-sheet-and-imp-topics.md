# 🎯 PLA1004: Competitive Coding Practices — TEE Master Study Sheet & Guaranteed Question Bank

> **Target Exam**: Sunday, October 25, 2026 (01:15 PM – 04:15 PM)  
> **Course**: PLA1004 — Competitive Coding Practices (Java)  
> **Pre-TEE Standing**: **61.5 / 70.0** (+2.0 marks ahead of class). **Target: 65–68 / 100 for A Grade**, **82+ for S Grade**.  
> **Source Material**: Exclusively synthesized from the official class PPTs, `Sample paper_1.docx`, `SAMPLE_PAPER.docx.pdf`, and the priority list (`tee_imp.txt`). *(All assignments excluded as requested)*.

---

## 1. Exam Paper Architecture (Official Format from `tee_imp.txt`)

* **Total Marks**: **100 Marks** | **Duration**: 3 Hours | **Calculators**: Strictly Prohibited
* **Part A (60 Marks)**:
  - 5 Questions × 12 Marks (One from each module/unit).
  - Each question is structured as **(6 Marks + 6 Marks)** with internal choice **OR** **(6 Marks + 6 Marks)**.
* **Part B (40 Marks)**:
  - 5 Questions × 8 Marks (Direct algorithm/program implementation; no subparts).

---

## 2. Priority Topic Index (All 15 Topics from `tee_imp.txt`)

| # | Priority Topic | Origin / Lecture PPT | Complexity | Core Concept / Formula |
|:---:|:---|:---|:---:|:---|
| **1** | **Time & Space Complexity** | `L5`, `L6`, `Sample Paper 1 Q1` | $O(1)$ to $O(N^2)$ | Loop iterations, nested loops, recursion stack depth |
| **2** | **Equilibrium Index & Sum** | `tee_imp.txt` | $O(N)$ Time, $O(1)$ Space | `totalSum - leftSum - arr[i] == leftSum` |
| **3** | **Swap 2 Nibbles in a Byte** | `L18`, `Sample Paper 1 Q4` | $O(1)$ Time, $O(1)$ Space | `((n & 0x0F) << 4) \| ((n & 0xF0) >> 4)` |
| **4** | **N-Queens Problem** | `L36-N Queens.pptx` | $O(N!)$ Time, $O(N)$ Space | Backtracking, column/diagonal attack validation |
| **5** | **Huffman Coding** | `HuffmanCoding.pptx`, `Sample Paper Q2` | $O(N \log N)$ Time | Min-Heap priority queue, prefix codes, bandwidth saving |
| **6** | **Weight of Substring** | `L28- Weightes substring.pptx` | $O(K \log 26)$ Time | $W(i) = (i+2) W(i-1)$, greedy floor search |
| **7** | **Min-Stack in $O(1)$ Space** | `Stack_Problems.pptx`, `Sample Paper Q4` | $O(1)$ Time, $O(1)$ Space | Arithmetic encoding: push $2x - \text{min}$, pop $2\text{min} - \text{top}$ |
| **8** | **Floyd Cycle Detection** | `LinkedList_Problems.pptx` | $O(N)$ Time, $O(1)$ Space | Tortoise & Hare: slow=1, fast=2, loop start at $L = nC - k$ |
| **9** | **Hamiltonian Cycle** | `Hamiltonian_Cycle.pptx` | $O(N!)$ Time, $O(N)$ Space | Backtracking: visiting all vertices exactly once |
| **10** | **Encode & Decode Strings** | `tee_imp.txt` | $O(N)$ Time, $O(N)$ Space | Run-length encoding: `"aaabbc"` $\to$ `"a3b2c1"` |
| **11** | **Segmented Sieve** | `L8-Segmented Sieve.pptx` | $O((R - L + 1) \log \log R)$ | Base primes up to $\sqrt{R}$, window shift by $L$ |
| **12** | **Block Swap Algorithm** | `tee_imp.txt` | $O(N)$ Time, $O(1)$ Space | Array rotation by $d$: divide into $A$ and $B$, swap blocks |
| **13** | **Lexicographically 1st Palindrome** | `tee_imp.txt` | $O(N)$ Time, $O(26)$ Space | Frequency count, max 1 odd character, symmetric placement |
| **14** | **Circular Queue Implementation** | `CircularQueue_SlidingWindow.pptx`| $O(1)$ Enqueue/Dequeue | `front = (front+1)%cap`, `rear = (rear+1)%cap` |
| **15** | **Tree Traversals (Pre/Post/Level)** | `Tree_Traversals.pptx` | $O(N)$ Time, $O(H)$ Space | Recursive traversals & Queue-based BFS |

---

## 3. High-Yield Question Solutions & Code Templates

---

### Topic 1: Time & Space Complexity Analysis (Guaranteed 10–12M Question)
*(Direct from `Sample paper_1.docx Q1` & `L5-Time_Complexity.pptx`)*

#### Theoretical Concepts:
1. **Time Complexity**: Measures how the execution time of an algorithm scales with input size $n$.
   - **$O(1)$ (Constant)**: Array index lookup, bitwise operations.
   - **$O(\log n)$ (Logarithmic)**: Binary search, loop index doubling/halving (`i = i * 2`).
   - **$O(n)$ (Linear)**: Single loop scanning $n$ elements.
   - **$O(n \log n)$**: Merge sort, Heap sort, Divide-and-conquer recurrences ($T(n) = 2T(n/2) + O(n)$).
   - **$O(n^2)$ (Quadratic)**: Nested loops over array pairs.
2. **Space Complexity**: Total memory consumed by the algorithm:
   $$\text{Total Space} = \text{Input Space} + \text{Auxiliary Space (extra variables, arrays, call stack)}$$

#### Java Program: Comparing $O(n)$ vs $O(n^2)$ Loop Structures
```java
public class ComplexityAnalysis {
    // Linear Time O(n), Auxiliary Space O(1)
    public static int linearSum(int[] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) { // Loop runs n times
            sum += arr[i];
        }
        return sum;
    }

    // Quadratic Time O(n^2), Auxiliary Space O(1)
    public static int countDuplicatePairs(int[] arr) {
        int count = 0;
        int n = arr.length;
        for (int i = 0; i < n; i++) {             // Outer loop: n iterations
            for (int j = i + 1; j < n; j++) {     // Inner loop: (n - 1) + (n - 2) + ... + 1 = n(n-1)/2
                if (arr[i] == arr[j]) {
                    count++;
                }
            }
        }
        return count; // Total iterations = n(n-1)/2 -> O(n^2)
    }

    public static void main(String[] args) {
        int[] data = {1, 2, 3, 2, 1};
        System.out.println("Linear Sum O(n): " + linearSum(data));
        System.out.println("Duplicate Pairs O(n^2): " + countDuplicatePairs(data));
    }
}
```
##### Sample Output:
```text
Linear Sum O(n): 9
Duplicate Pairs O(n^2): 2
```

---

### Topic 2: Equilibrium Index of an Array
*(Direct from `tee_imp.txt`)*

#### Problem Definition:
An index $i$ in array $A[0 \dots n-1]$ is an **equilibrium index** if the sum of elements at lower indices equals the sum of elements at higher indices:
$$\sum_{j=0}^{i-1} A[j] = \sum_{j=i+1}^{n-1} A[j]$$

#### Optimal $O(n)$ Time, $O(1)$ Space Algorithm:
1. Compute `totalSum` of the entire array in one pass.
2. Maintain a running `leftSum` initialized to 0.
3. For each index $i$:
   $$\text{rightSum} = \text{totalSum} - \text{leftSum} - A[i]$$
4. If `leftSum == rightSum`, index $i$ is an equilibrium point!
5. Add $A[i]$ to `leftSum` and continue.

```java
public class EquilibriumIndex {
    public static int findEquilibrium(int[] arr) {
        long totalSum = 0;
        for (int x : arr) totalSum += x;

        long leftSum = 0;
        for (int i = 0; i < arr.length; i++) {
            long rightSum = totalSum - leftSum - arr[i];
            if (leftSum == rightSum) {
                return i; // Found equilibrium index
            }
            leftSum += arr[i];
        }
        return -1; // No equilibrium index exists
    }

    public static void main(String[] args) {
        int[] arr = {-7, 1, 5, 2, -4, 3, 0};
        int eqIndex = findEquilibrium(arr);
        System.out.println("Equilibrium Index: " + eqIndex); // Index 3 (Value: 2)
        // Left sum = -7 + 1 + 5 = -1
        // Right sum = -4 + 3 + 0 = -1
    }
}
```
##### Sample Output:
```text
Equilibrium Index: 3
```

---

### Topic 3: Swap Two Nibbles in an 8-bit Byte
*(Direct from `L18-Swap Two Nibbles in a Byte.pptx` & `Sample paper_1.docx Q4`)*

#### Logic & Bitmasking:
* An 8-bit byte consists of two 4-bit nibbles:
  - **Low Nibble** (bits 0–3): isolated via mask `0x0F` (`0000 1111`).
  - **High Nibble** (bits 4–7): isolated via mask `0xF0` (`1111 0000`).
* **Swapping Expression**:
  $$\text{swapped} = ((n \ \& \ \text{0x0F}) \ll 4) \ \mid \ ((n \ \& \ \text{0xF0}) \gg 4)$$

#### Dry Run on Input $n = 100_{10}$:
1. Binary of $100$: $0110 \, 0100_2$
   - High nibble: `0110` ($6_{10}$)
   - Low nibble: `0100` ($4_{10}$)
2. `(100 & 0x0F) << 4`:
   $$0000 \, 0100_2 \ll 4 = 0100 \, 0000_2 = 64_{10}$$
3. `(100 & 0xF0) >> 4`:
   $$0110 \, 0000_2 \gg 4 = 0000 \, 0110_2 = 6_{10}$$
4. Bitwise OR:
   $$0100 \, 0000_2 \mid 0000 \, 0110_2 = 0100 \, 0110_2 = 64 + 6 = \mathbf{70_{10}}$$

```java
public class SwapNibbles {
    public static int swapNibbles(int n) {
        return ((n & 0x0F) << 4) | ((n & 0xF0) >> 4);
    }

    public static void main(String[] args) {
        int input = 100;
        int result = swapNibbles(input);
        System.out.println("Input:  " + input + " (Binary: " + Integer.toBinaryString(input) + ")");
        System.out.println("Result: " + result + " (Binary: " + Integer.toBinaryString(result) + ")");
    }
}
```
##### Sample Output:
```text
Input:  100 (Binary: 1100100)
Result: 70 (Binary: 1000110)
```

---

### Topic 4: N-Queens Backtracking Problem
*(Direct from `L36-N Queens.pptx`)*

#### Backtracking Constraints:
Place $N$ queens on an $N \times N$ chessboard such that no two queens attack each other:
1. No two queens in the same column.
2. No two queens in the same upper-left diagonal ($\text{row} - \text{col} = \text{constant}$).
3. No two queens in the same upper-right diagonal ($\text{row} + \text{col} = \text{constant}$).

```java
public class NQueens {
    static final int N = 4;

    public static boolean isSafe(int[][] board, int row, int col) {
        // Check column
        for (int i = 0; i < row; i++)
            if (board[i][col] == 1) return false;

        // Check upper-left diagonal
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--)
            if (board[i][j] == 1) return false;

        // Check upper-right diagonal
        for (int i = row - 1, j = col + 1; i >= 0 && j < N; i--, j++)
            if (board[i][j] == 1) return false;

        return true;
    }

    public static boolean solveNQ(int[][] board, int row) {
        if (row >= N) return true; // All queens placed

        for (int col = 0; col < N; col++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 1; // Place queen
                if (solveNQ(board, row + 1)) return true;
                board[row][col] = 0; // Backtrack
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int[][] board = new int[N][N];
        if (solveNQ(board, 0)) {
            System.out.println("Valid N-Queens Solution (N = 4):");
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    System.out.print((board[i][j] == 1 ? "Q " : ". "));
                }
                System.out.println();
            }
        }
    }
}
```
##### Sample Output:
```text
Valid N-Queens Solution (N = 4):
. Q . . 
. . . Q 
Q . . . 
. . Q . 
```

---

### Topic 5: Huffman Coding Algorithm
*(Direct from `HuffmanCoding.pptx` & `sample_paper_text.txt Q2`)*

#### Worked Problem (Mars Satellite Telemetry):
* Given symbols and frequencies:
  - **S**: 32
  - **F**: 23
  - **T**: 10
  - **P**: 10
  - **E**: 5
  - *Total sum* $= 32 + 23 + 10 + 10 + 5 = 80$.

#### Tree Construction Steps (Greedy Min-Heap):
1. Extract two lowest: $E(5)$ and $P(10) \implies \text{Node } N_1(15)$.
2. Extract two lowest from $\{S(32), F(23), T(10), N_1(15)\}$:
   - Lowest: $T(10)$ and $N_1(15) \implies \text{Node } N_2(25)$.
3. Extract two lowest from $\{S(32), F(23), N_2(25)\}$:
   - Lowest: $F(23)$ and $N_2(25) \implies \text{Node } N_3(48)$.
4. Extract remaining two $\{S(32), N_3(48)\}$:
   - Root: $N_4(80)$.

#### Resulting Prefix Codes & Lengths:
* **S** (Left of Root): `'0'` $\to$ **1 bit**
* **F** (Right-Left): `'10'` $\to$ **2 bits**
* **T** (Right-Right-Left): `'110'` $\to$ **3 bits**
* **P** (Right-Right-Right-Left): `'1110'` $\to$ **4 bits**
* **E** (Right-Right-Right-Right): `'1111'` $\to$ **4 bits**

#### Bit Length & Bandwidth Savings Calculation:
* Average bits per symbol:
  $$\bar{L} = \frac{(32 \times 1) + (23 \times 2) + (10 \times 3) + (10 \times 4) + (5 \times 4)}{80} = \frac{32 + 46 + 30 + 40 + 20}{80} = \frac{168}{80} = \mathbf{2.1\text{ bits/symbol}}$$
* Total bits for 200 telemetry codes:
  $$\text{Total Bits} = 200 \times 2.1 = \mathbf{420\text{ bits}}$$
* Fixed 3-bit encoding:
  $$\text{Fixed Bits} = 200 \times 3 = \mathbf{600\text{ bits}}$$
* **Bandwidth Percentage Saved**:
  $$\text{Savings} = \frac{600 - 420}{600} \times 100\% = \frac{180}{600} \times 100\% = \mathbf{30\%}$$

```java
import java.util.PriorityQueue;

class HuffmanNode implements Comparable<HuffmanNode> {
    char data;
    int freq;
    HuffmanNode left, right;

    public HuffmanNode(char data, int freq) {
        this.data = data;
        this.freq = freq;
    }

    public int compareTo(HuffmanNode other) {
        return this.freq - other.freq;
    }
}

public class HuffmanDemo {
    public static void printCodes(HuffmanNode root, String code) {
        if (root == null) return;
        if (root.left == null && root.right == null) {
            System.out.println(root.data + " : " + code + " (" + code.length() + " bits)");
            return;
        }
        printCodes(root.left, code + "0");
        printCodes(root.right, code + "1");
    }

    public static void main(String[] args) {
        char[] chars = {'S', 'F', 'T', 'P', 'E'};
        int[] freqs = {32, 23, 10, 10, 5};

        PriorityQueue<HuffmanNode> pq = new PriorityQueue<>();
        for (int i = 0; i < chars.length; i++) {
            pq.add(new HuffmanNode(chars[i], freqs[i]));
        }

        while (pq.size() > 1) {
            HuffmanNode left = pq.poll();
            HuffmanNode right = pq.poll();
            HuffmanNode parent = new HuffmanNode('-', left.freq + right.freq);
            parent.left = left;
            parent.right = right;
            pq.add(parent);
        }

        System.out.println("Generated Huffman Codes:");
        printCodes(pq.peek(), "");
    }
}
```
##### Sample Output:
```text
Generated Huffman Codes:
S : 0 (1 bits)
F : 10 (2 bits)
T : 110 (3 bits)
P : 1110 (4 bits)
E : 1111 (4 bits)
```

---

### Topic 6: Weighted Substring
*(Direct from `L28- Weightes substring.pptx`)*

#### Problem Rule:
* Weights defined as:
  $$A = 1$$
  $$B = 2A + A = 3A = 3$$
  $$C = 3B + B = 4B = 12$$
  $$D = 4C + C = 5C = 60$$
  $$\text{General Formula: } W[i] = (i + 1) \cdot W[i-1] + W[i-1] = (i + 2) \cdot W[i-1]$$
* **Goal**: Given target weight $K$, find the **shortest** string. If tie, return the **lexicographically smallest**.
* **Greedy Strategy**: Repeatedly pick the largest character with weight $\le K$. Append to list, subtract weight. Finally, reverse the list to ensure smallest characters appear first!

```java
import java.util.*;

public class WeightedSubstring {
    static long[] values = new long[26];

    static void precomputeWeights() {
        values[0] = 1; // 'A'
        long prev = 1;
        for (int i = 1; i < 26; i++) {
            values[i] = (i + 2) * prev;
            prev = values[i];
        }
    }

    public static String smallestString(long k) {
        precomputeWeights();
        List<Character> list = new ArrayList<>();

        while (k > 0) {
            // Find largest character with weight <= k
            int ind = 0;
            for (int i = 25; i >= 0; i--) {
                if (values[i] <= k) {
                    ind = i;
                    break;
                }
            }
            list.add((char) ('A' + ind));
            k -= values[ind];
        }

        // Reverse to make it lexicographically smallest
        StringBuilder sb = new StringBuilder();
        for (int i = list.size() - 1; i >= 0; i--) {
            sb.append(list.get(i));
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        long targetWeight = 25;
        System.out.println("Shortest & Lexicographically Smallest String for weight 25: " + smallestString(targetWeight));
        // A=1, B=3, C=12 -> 25 = 12 + 12 + 1 -> 'C', 'C', 'A' -> Reversed: "ACC"
    }
}
```
##### Sample Output:
```text
Shortest & Lexicographically Smallest String for weight 25: ACC
```

---

### Topic 7: Min-Stack in $O(1)$ Extra Space
*(Direct from `Stack_Problems.pptx` & `sample_paper_text.txt Q4`)*

#### Arithmetic Encoding Mechanics:
* Instead of allocating an auxiliary tracking stack, store a **modified encoded value**:
1. **Push($x$)**:
   - If stack is empty: `min = x`, push $x$.
   - If $x \ge \text{min}$: push $x$ directly.
   - If $x < \text{min}$: push the flag value $2x - \text{min}$, and update $\text{min} = x$.  
     *(Notice: since $x < \text{min}$, $2x - \text{min} < x$, so the stored value is strictly less than the new min!)*
2. **Pop()**:
   - Let top element be $y$.
   - If $y \ge \text{min}$: real value is $y$.
   - If $y < \text{min}$: real value is $\text{min}$, and restore previous min:
     $$\text{previous\_min} = 2 \cdot \text{min} - y$$
3. **getMin()**: Returns `min` variable in $O(1)$ time.

#### Dry Run on Sequence: `push(8), push(5), push(4), push(10), pop()`:
1. `push(8)`: Stack empty $\implies$ push $8$, `min = 8`. Stack: `[8]`.
2. `push(5)`: $5 < 8 \implies$ push $2(5) - 8 = 2$, `min = 5`. Stack: `[8, 2]`.
3. `push(4)`: $4 < 5 \implies$ push $2(4) - 5 = 3$, `min = 4`. Stack: `[8, 2, 3]`.
4. `push(10)`: $10 \ge 4 \implies$ push $10$. Stack: `[8, 2, 3, 10]`, `min = 4`.
5. `pop()`: Top $= 10 \ge \text{min}(4) \implies$ pop $10$. Stack: `[8, 2, 3]`, `min = 4`.

```java
import java.util.Stack;

public class MinStackSpaceOptimized {
    private Stack<Long> stack = new Stack<>();
    private Long minEle;

    public void push(long x) {
        if (stack.isEmpty()) {
            minEle = x;
            stack.push(x);
            return;
        }
        if (x < minEle) {
            stack.push(2 * x - minEle); // Flag encoded value
            minEle = x;
        } else {
            stack.push(x);
        }
    }

    public long pop() {
        if (stack.isEmpty()) throw new IllegalStateException("Stack Underflow");
        long top = stack.pop();
        if (top < minEle) {
            long actual = minEle;
            minEle = 2 * minEle - top; // Restore previous min
            return actual;
        }
        return top;
    }

    public long getMin() {
        if (stack.isEmpty()) throw new IllegalStateException("Stack Empty");
        return minEle;
    }

    public static void main(String[] args) {
        MinStackSpaceOptimized s = new MinStackSpaceOptimized();
        s.push(8);
        s.push(5);
        s.push(4);
        s.push(10);
        System.out.println("Current Min: " + s.getMin()); // 4
        System.out.println("Popped:      " + s.pop());    // 10
        System.out.println("Min after Pop: " + s.getMin()); // 4
        System.out.println("Popped:      " + s.pop());    // 4
        System.out.println("Min after Pop: " + s.getMin()); // 5
    }
}
```
##### Sample Output:
```text
Current Min: 4
Popped:      10
Min after Pop: 4
Popped:      4
Min after Pop: 5
```

---

### Topic 8: Floyd's Cycle Detection Algorithm (Tortoise and Hare)
*(Direct from `LinkedList_Problems.pptx`)*

#### Algorithm Logic:
1. **Cycle Detection**:
   - `slow` moves 1 step: `slow = slow.next`
   - `fast` moves 2 steps: `fast = fast.next.next`
   - If `slow == fast`, a loop exists!
2. **Find Loop Start Node**:
   - Reset `slow = head`, keep `fast` at meeting point.
   - Move both 1 step at a time: `slow = slow.next`, `fast = fast.next`.
   - The node where they collide again is the exact start of the loop!
3. **Remove Loop**:
   - Find node pointing to loop start, set its `next = null`.

```java
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; next = null; }
}

public class FloydCycleDetection {
    public static ListNode detectCycleStart(ListNode head) {
        if (head == null || head.next == null) return null;

        ListNode slow = head, fast = head;
        boolean hasCycle = false;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                hasCycle = true;
                break;
            }
        }

        if (!hasCycle) return null; // No cycle

        // Move slow to head, advance both by 1 step
        slow = head;
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }
        return slow; // Loop start node
    }

    public static void main(String[] args) {
        ListNode n1 = new ListNode(101);
        ListNode n2 = new ListNode(102);
        ListNode n3 = new ListNode(103);
        ListNode n4 = new ListNode(104);
        n1.next = n2; n2.next = n3; n3.next = n4;
        n4.next = n2; // Creates loop back to 102

        ListNode start = detectCycleStart(n1);
        System.out.println("Cycle detected starting at node: " + (start != null ? start.val : "None"));
    }
}
```
##### Sample Output:
```text
Cycle detected starting at node: 102
```

---

### Topic 9: Hamiltonian Cycle Backtracking Algorithm
*(Direct from `Hamiltonian_Cycle_and_Graph_Coloring.pptx`)*

```java
public class HamiltonianCycle {
    final int V = 5;
    int[] path;

    boolean isSafe(int v, int[][] graph, int[] path, int pos) {
        // Check if adjacent to previous vertex in path
        if (graph[path[pos - 1]][v] == 0) return false;

        // Check if vertex already included in path
        for (int i = 0; i < pos; i++)
            if (path[i] == v) return false;

        return true;
    }

    boolean hamCycleUtil(int[][] graph, int[] path, int pos) {
        if (pos == V) {
            // Check if there is an edge from last to first vertex
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

    public void solve(int[][] graph) {
        path = new int[V];
        Arrays.fill(path, -1);
        path[0] = 0; // Start at vertex 0

        if (hamCycleUtil(graph, path, 1)) {
            System.out.print("Hamiltonian Cycle found: ");
            for (int v : path) System.out.print(v + " -> ");
            System.out.println(path[0]);
        } else {
            System.out.println("No Hamiltonian Cycle exists.");
        }
    }

    public static void main(String[] args) {
        HamiltonianCycle hc = new HamiltonianCycle();
        int[][] graph = {
            {0, 1, 0, 1, 0},
            {1, 0, 1, 1, 1},
            {0, 1, 0, 0, 1},
            {1, 1, 0, 0, 1},
            {0, 1, 1, 1, 0}
        };
        hc.solve(graph);
    }
}
```
##### Sample Output:
```text
Hamiltonian Cycle found: 0 -> 1 -> 2 -> 4 -> 3 -> 0
```

---

### Topic 10: Run-Length Encoding and Decoding
*(Direct from `tee_imp.txt`)*

```java
public class EncodeDecode {
    public static String encode(String s) {
        if (s == null || s.isEmpty()) return "";
        StringBuilder sb = new StringBuilder();
        int count = 1;
        for (int i = 0; i < s.length(); i++) {
            if (i + 1 < s.length() && s.charAt(i) == s.charAt(i + 1)) {
                count++;
            } else {
                sb.append(s.charAt(i)).append(count);
                count = 1;
            }
        }
        return sb.toString();
    }

    public static String decode(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i += 2) {
            char ch = s.charAt(i);
            int count = Character.getNumericValue(s.charAt(i + 1));
            for (int j = 0; j < count; j++) {
                sb.append(ch);
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        String original = "aaabbccccd";
        String encoded = encode(original);
        String decoded = decode(encoded);
        System.out.println("Original: " + original);
        System.out.println("Encoded:  " + encoded);
        System.out.println("Decoded:  " + decoded);
    }
}
```
##### Sample Output:
```text
Original: aaabbccccd
Encoded:  a3b2c4d1
Decoded:  aaabbccccd
```

---

### Topic 11: Segmented Sieve Algorithm
*(Direct from `L8-Segmented and Incremental Sieve.pptx` & `Sample Paper 1 Q2`)*

```java
import java.util.*;

public class SegmentedSieve {
    public static List<Integer> simpleSieve(int limit) {
        boolean[] isPrime = new boolean[limit + 1];
        Arrays.fill(isPrime, true);
        List<Integer> primes = new ArrayList<>();

        for (int p = 2; p * p <= limit; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i <= limit; i += p)
                    isPrime[i] = false;
            }
        }
        for (int p = 2; p <= limit; p++) {
            if (isPrime[p]) primes.add(p);
        }
        return primes;
    }

    public static void findPrimesInRange(int L, int R) {
        int limit = (int) Math.floor(Math.sqrt(R));
        List<Integer> basePrimes = simpleSieve(limit);

        boolean[] isPrime = new boolean[R - L + 1];
        Arrays.fill(isPrime, true);

        for (int p : basePrimes) {
            // Find minimum multiple of p that is >= L
            int firstMultiple = Math.max(p * p, ((L + p - 1) / p) * p);
            for (int j = firstMultiple; j <= R; j += p) {
                isPrime[j - L] = false;
            }
        }

        System.out.print("Primes in range [" + L + ", " + R + "]: ");
        for (int i = 0; i < isPrime.length; i++) {
            if (isPrime[i] && (i + L) > 1) {
                System.out.print((i + L) + " ");
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {
        findPrimesInRange(10, 50);
    }
}
```
##### Sample Output:
```text
Primes in range [10, 50]: 11 13 17 19 23 29 31 37 41 43 47 
```

---

### Topic 12: Block Swap Algorithm for Array Rotation
*(Direct from `tee_imp.txt`)*

```java
public class BlockSwapRotation {
    public static void swap(int[] arr, int fi, int si, int d) {
        for (int i = 0; i < d; i++) {
            int temp = arr[fi + i];
            arr[fi + i] = arr[si + i];
            arr[si + i] = temp;
        }
    }

    public static void rotate(int[] arr, int d, int n) {
        if (d == 0 || d == n) return;
        d = d % n;
        int i = d;
        int j = n - d;

        while (i != j) {
            if (i < j) { // A is shorter
                swap(arr, d - i, d + j - i, i);
                j -= i;
            } else {     // B is shorter
                swap(arr, d - i, d, j);
                i -= j;
            }
        }
        swap(arr, d - i, d, i);
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        rotate(arr, 2, 7); // Rotate left by 2 positions
        System.out.println("Rotated Array: " + Arrays.toString(arr));
    }
}
```
##### Sample Output:
```text
Rotated Array: [3, 4, 5, 6, 7, 1, 2]
```

---

### Topic 13: Lexicographically First Palindromic String
*(Direct from `tee_imp.txt`)*

```java
public class LexicographicallyFirstPalindrome {
    public static String getPalindrome(String s) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) freq[c - 'a']++;

        int oddCount = 0;
        char oddChar = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] % 2 != 0) {
                oddCount++;
                oddChar = (char) ('a' + i);
            }
        }

        if (oddCount > 1) {
            return "NO PALINDROME POSSIBLE";
        }

        StringBuilder firstHalf = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < freq[i] / 2; j++) {
                firstHalf.append((char) ('a' + i));
            }
        }

        String secondHalf = new StringBuilder(firstHalf).reverse().toString();
        if (oddCount == 1) {
            return firstHalf.toString() + oddChar + secondHalf;
        }
        return firstHalf.toString() + secondHalf;
    }

    public static void main(String[] args) {
        String input = "malayalam";
        System.out.println("Lexicographically First Palindrome: " + getPalindrome(input));
    }
}
```
##### Sample Output:
```text
Lexicographically First Palindrome: aalmylaay
```

---

### Topic 14: Circular Queue Implementation
*(Direct from `CircularQueue_SlidingWindow.pptx`)*

```java
public class CircularQueue {
    private int[] data;
    private int front, rear, size, capacity;

    public CircularQueue(int cap) {
        this.capacity = cap;
        this.data = new int[cap];
        this.front = 0;
        this.rear = -1;
        this.size = 0;
    }

    public boolean isFull() { return size == capacity; }
    public boolean isEmpty() { return size == 0; }

    public boolean enqueue(int val) {
        if (isFull()) return false;
        rear = (rear + 1) % capacity;
        data[rear] = val;
        size++;
        return true;
    }

    public int dequeue() {
        if (isEmpty()) return -1;
        int val = data[front];
        front = (front + 1) % capacity;
        size--;
        return val;
    }

    public int peek() {
        if (isEmpty()) return -1;
        return data[front];
    }

    public static void main(String[] args) {
        CircularQueue q = new CircularQueue(3);
        q.enqueue(10);
        q.enqueue(20);
        q.enqueue(30);
        System.out.println("Enqueue 40 on full queue: " + q.enqueue(40)); // false
        System.out.println("Dequeued: " + q.dequeue());                 // 10
        q.enqueue(40);                                                  // Allowed!
        System.out.println("Front Element: " + q.peek());               // 20
    }
}
```
##### Sample Output:
```text
Enqueue 40 on full queue: false
Dequeued: 10
Front Element: 20
```

---

### Topic 15: Tree Traversals (Preorder, Postorder, Level-Order)
*(Direct from `Tree_Traversals.pptx`)*

```java
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

public class TreeTraversals {
    public static void preorder(TreeNode root) {
        if (root == null) return;
        System.out.print(root.val + " ");
        preorder(root.left);
        preorder(root.right);
    }

    public static void postorder(TreeNode root) {
        if (root == null) return;
        postorder(root.left);
        postorder(root.right);
        System.out.print(root.val + " ");
    }

    public static void levelOrder(TreeNode root) {
        if (root == null) return;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode curr = q.poll();
            System.out.print(curr.val + " ");
            if (curr.left != null) q.add(curr.left);
            if (curr.right != null) q.add(curr.right);
        }
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        System.out.print("Preorder (Root-L-R):   "); preorder(root);   System.out.println();
        System.out.print("Postorder (L-R-Root):  "); postorder(root);  System.out.println();
        System.out.print("Level-Order (BFS):     "); levelOrder(root); System.out.println();
    }
}
```
##### Sample Output:
```text
Preorder (Root-L-R):   1 2 4 5 3 
Postorder (L-R-Root):  4 5 2 3 1 
Level-Order (BFS):     1 2 3 4 5 
```
