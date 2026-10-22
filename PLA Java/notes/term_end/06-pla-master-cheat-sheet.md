# 📑 PLA1004: Master Algorithms & Formulas Cheat Sheet (1-Page)

> **Exam Date**: Sunday, October 25, 2026 (01:15 PM – 04:15 PM)  
> **Keep this open for rapid syntax, bitwise hacks, recurrences, and complexities right before entering the exam hall!**

---

## 1. Master Bitwise Hacks & Formulas
* **Swap Two Nibbles in a Byte**: `((n & 0x0F) << 4) | ((n & 0xF0) >> 4)` *(e.g., $100_{10} \implies 70_{10}$)*
* **Power of 2 Check**: `n > 0 && (n & (n - 1)) == 0`
* **Count Set Bits (Brian Kernighan)**: `while(n > 0) { n &= (n - 1); count++; }`
  - *Trace for $N=40$ ($00101000_2$)*: $40 \to 32 \to 0$ in **2 iterations** vs 32 naive shifts.
* **Lowest Set Bit**: `n & -n`
* **Toggle $k$-th Bit**: `n ^ (1 << k)`
* **Check $k$-th Bit**: `(n & (1 << k)) != 0`
* **Alternating Bits Check**: `int x = n ^ (n >> 1); return (x & (x + 1)) == 0;`
* **Longest 1s After Flipping One 0**: Maintain `prevLen` and `currLen`; update `maxLen = Math.max(maxLen, prevLen + currLen + 1)`. *(For $N=1775 \implies 8$)*.
* **Max Product Subarray**: Track `maxEndingHere` and `minEndingHere`; swap on negative value. For $\{2, 3, -2, 4, -1\} \implies \text{max}=48$, range $[0, 4]$.
* **Quadratic Discriminant ($D = b^2 - 4ac$)**:
  - $D > 0 \implies$ Real & Distinct: $(-b \pm \sqrt{D}) / (2a)$
  - $D = 0 \implies$ Real & Equal: $-b / (2a)$
  - $D < 0 \implies$ Complex Conjugates: $-b/(2a) \pm i\sqrt{|D|}/(2a)$

---

## 2. Number Theory & Hardware Arithmetic
* **Euler's Totient $\phi(N)$**:
  - Factorisation formula: $\phi(N) = N \prod_{p \mid N} (1 - \frac{1}{p})$ in $O(\sqrt{N})$ time, $O(1)$ space.
  - Comparison: $\phi(36) = 12$. For $N = 10^{12}$, factorisation takes $10^6$ ops ($\approx 2\text{ ms}$) vs brute-force GCD $4 \times 10^{13}$ ops ($\approx 111\text{ hours}$).
* **Euclidean GCD**: $\gcd(a, b) = \gcd(b, a \pmod b)$
* **Extended GCD**: $a x + b y = \gcd(a, b) \implies x = y_1, \, y = x_1 - \lfloor a/b \rfloor y_1$
* **Segmented Sieve**: Precompute primes up to $\sqrt{R}$; offset window indices by $L$ in range $[L, R]$. Memory is $O(R - L + 1)$.
* **Booth's Multiplication**:
  - `Q_0 Q_{-1} = 10` $\implies A = A - M$, then Arithmetic Shift Right (ASR)
  - `Q_0 Q_{-1} = 01` $\implies A = A + M$, then Arithmetic Shift Right (ASR)
  - `00` or `11` $\implies$ ASR directly (Sign bit of $A$ is preserved)
* **Strobogrammatic Pairs**: `(0,0)`, `(1,1)`, `(8,8)`, `(6,9)`, `(9,6)`.
* **Armstrong Check**: Sum of (digit)$^{\text{digits}} == \text{original}$.

---

## 3. Linear DSA, Stacks, Queues & Strings
* **Insertion Sort Shifts**: Best $O(N)$ (0 shifts when sorted); Worst $O(N^2)$ ($N(N-1)/2$ shifts when reverse). For $\{5, 2, 4, 6, 1, 3\} \implies 9$ shifts.
* **Array Right Rotation by $k$ (3 Reversals)**:
  - `k = k % n; reverse(a, 0, n - 1); reverse(a, 0, k - 1); reverse(a, k, n - 1);` in $O(N)$ time, $O(1)$ space.
* **Stock Span Problem**: Monotonic decreasing stack storing indices. $\text{span} = i - \text{stack.peek()}$ in $O(N)$ total time.
* **Min-Stack in $O(1)$ Extra Space**:
  - **Push($x$)**: If $x < \min \implies$ push $2x - \min$ to stack; $\min = x$.
  - **Pop()**: If $\text{top} < \min \implies$ restore previous $\min = 2\min - \text{top}$.
  - **Top()**: If $\text{top} < \min \implies$ return $\min$; else return $\text{top}$.
* **Circular Queue (Array of size $C$)**: Full: `(rear + 1) % C == front`, Enqueue: `rear = (rear + 1) % C`, Dequeue: `front = (front + 1) % C`.
* **Floyd's Loop Detection & Removal**: Slow moves 1, Fast moves 2. When meeting, reset slow to `head`. Move both 1 step until `fast.next == slow.next`, then `fast.next = null` (no node lost).
* **First Negative in Window $K$**: Deque stores negative indices. Poll elements outside $[i - k + 1, i]$; output `a[dq.peekFirst()]` or $0$.
* **Sliding Window Maximum/Minimum**: Monotonic Deque storing indices in $O(N)$ total time.
* **In-Place Hyphen Shift**: Read right-to-left, place non-hyphens from the end, prepend hyphens in $O(1)$ space.
* **Equilibrium Index**: `totalSum - leftSum - arr[i] == leftSum` in single $O(N)$ pass.
* **Block Swap Array Rotation**: Swap matching blocks of size $d$ and $n-d$ recursively in $O(N)$ time, $O(1)$ space.

---

## 4. Greedy Algorithms & Backtracking
* **Fractional Knapsack**: Sort by ratio $v_i / w_i$ descending. Greedily take full or partial fraction. Fails for 0/1 knapsack where fractions are forbidden.
* **Job Sequencing with Deadlines**: Sort by profit descending. Place each job in latest available slot $\le \text{deadline}$. $O(N^2)$ time or $O(N \log N)$ with DSU.
* **Rat in a Maze**: Backtracking with Right $(r, c+1)$ and Down $(r+1, c)$. Mark cell 1 on visit, reset to 0 on dead end.
* **Activity Selection**: Sort by finish time ascending. Greedily select next activity with $s_i \ge f_{\text{last}}$.
* **Huffman Coding**: Min-Priority Queue repeatedly merges two lowest frequency nodes. Prefix-free codes.
* **Weight of Substring ($L28$)**: $W(0) = 1 ('A')$; $W(i) = (i + 2) W(i - 1)$ for $i \ge 1$. Greedily pick largest character $\le K$.
* **Josephus Recurrence**: $J(n, k) = (J(n - 1, k) + k) \pmod n$ with $J(1, k) = 0$ (0-indexed). Add 1 for 1-indexed.
* **$N$-Queens Bitmasking**: Valid bitmask $= \text{allDone} \ \& \ \sim(\text{cols} \mid \text{d1} \mid \text{d2})$. Advance diagonals: `(d1 | bit) << 1`, `(d2 | bit) >> 1`.
* **Hamiltonian Cycle**: Backtracking to visit all $V$ vertices once; check edge from last node back to start node.

---

## 5. Dynamic Programming & Trees/Graphs
* **Validate BST**: Range check $\text{min} < \text{node.val} < \text{max}$ recursively. Checking only parent is insufficient (e.g. left subtree child cannot exceed root).
* **Tree Diameter**:
  - Naive $O(N^2)$: Computes height at every node separately.
  - Optimal $O(N)$: Single-traversal postorder returning height while maintaining $\max(\text{maxDia}, \text{leftH} + \text{rightH})$.
* **Number of Islands**: Grid DFS/BFS sink visited land cells (`grid[r][c] = '0'`) in $O(R \cdot C)$ time and space.
* **0/1 Knapsack (1D Array)**: $dp[w] = \max(dp[w], val[i] + dp[w - wt[i]])$ traversed backwards from $W$ down to $wt[i]$.
* **Longest Common Subsequence (LCS)**: If $s_1[i-1] == s_2[j-1] \implies 1 + dp[i-1][j-1]$; else $\max(dp[i-1][j], dp[i][j-1])$.
* **Tree Traversals**: Preorder ($DLR$), Inorder ($LDR$), Postorder ($LRD$), Level Order (Queue BFS).
* **Dijkstra's Algorithm**: Min-Heap priority queue in $O((V + E) \log V)$ time. Fails on negative edge weights.
* **Kruskal's MST**: Sort edges by weight; Disjoint Set Union (DSU) with path compression and rank in $O(E \log E)$.

---

## 6. Master Complexity Reference Table

| Algorithm | Best Time | Average Time | Worst Time | Auxiliary Space |
|:---|:---|:---|:---|:---|
| **Insertion Sort** | $O(N)$ (0 shifts) | $O(N^2)$ | $O(N^2)$ ($N(N-1)/2$ shifts) | $O(1)$ |
| **Sieve of Eratosthenes** | $O(N \log \log N)$ | $O(N \log \log N)$ | $O(N \log \log N)$ | $O(N)$ |
| **Segmented Sieve** | $O((R-L+1) \log \log R)$ | $O((R-L+1) \log \log R)$ | $O((R-L+1) \log \log R)$ | $O(\sqrt{R} + (R-L+1))$ |
| **Euler's Totient $\phi(N)$** | $O(\sqrt{N})$ | $O(\sqrt{N})$ | $O(\sqrt{N})$ | $O(1)$ |
| **Array Right Rotation (Reversal)** | $O(N)$ | $O(N)$ | $O(N)$ | $O(1)$ |
| **Stock Span (Stack)** | $O(N)$ | $O(N)$ | $O(N)$ | $O(N)$ |
| **Sliding Window Max/Min** | $O(N)$ | $O(N)$ | $O(N)$ | $O(K)$ |
| **First Negative in Window** | $O(N)$ | $O(N)$ | $O(N)$ | $O(K)$ |
| **Min-Stack (Constant Space)** | $O(1)$ | $O(1)$ | $O(1)$ | $O(1)$ |
| **Floyd Cycle Detection & Removal** | $O(N)$ | $O(N)$ | $O(N)$ | $O(1)$ |
| **Fractional Knapsack** | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(1)$ |
| **Job Sequencing with Deadlines** | $O(N \log N)$ | $O(N^2)$ | $O(N^2)$ | $O(\max(D))$ |
| **Huffman Coding** | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(N)$ |
| **Rat in a Maze** | $O(2^{N^2})$ | $O(2^{N^2})$ | $O(2^{N^2})$ | $O(N^2)$ |
| **$N$-Queens Backtracking** | $O(N!)$ | $O(N!)$ | $O(N!)$ | $O(N)$ |
| **Hamiltonian Cycle** | $O(N!)$ | $O(N!)$ | $O(N!)$ | $O(N)$ |
| **0/1 Knapsack DP** | $O(N \cdot W)$ | $O(N \cdot W)$ | $O(N \cdot W)$ | $O(W)$ |
| **Longest Common Subsequence**| $O(M \cdot N)$ | $O(M \cdot N)$ | $O(M \cdot N)$ | $O(M \cdot N)$ |
| **Validate BST (Range Check)**| $O(N)$ | $O(N)$ | $O(N)$ | $O(H)$ |
| **Tree Diameter (Single-Traversal)** | $O(N)$ | $O(N)$ | $O(N)$ | $O(H)$ |
| **Number of Islands (DFS/BFS)** | $O(R \cdot C)$ | $O(R \cdot C)$ | $O(R \cdot C)$ | $O(R \cdot C)$ |
| **Dijkstra Shortest Path** | $O((V + E) \log V)$ | $O((V + E) \log V)$ | $O((V + E) \log V)$ | $O(V)$ |
| **Kruskal's MST (DSU)** | $O(E \log E)$ | $O(E \log E)$ | $O(E \log E)$ | $O(V)$ |
| **Tree Level Order (BFS)** | $O(N)$ | $O(N)$ | $O(N)$ | $O(W_{\text{tree}})$ |
