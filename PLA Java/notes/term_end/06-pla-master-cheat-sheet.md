# 📑 PLA1004: Master Algorithms & Formulas Cheat Sheet (1-Page)

> **Exam Date**: Sunday, October 25, 2026 (01:15 PM – 04:15 PM)  
> **Keep this open for rapid syntax, bitwise hacks, recurrences, and complexities right before entering the exam hall!**

---

## 1. Master Bitwise Hacks & Formulas
* **Swap Two Nibbles in a Byte**: `((n & 0x0F) << 4) | ((n & 0xF0) >> 4)` *(e.g., $100_{10} \implies 70_{10}$)*
* **Power of 2 Check**: `n > 0 && (n & (n - 1)) == 0`
* **Count Set Bits (Brian Kernighan)**: `while(n > 0) { n &= (n - 1); count++; }`
* **Lowest Set Bit**: `n & -n`
* **Toggle $k$-th Bit**: `n ^ (1 << k)`
* **Check $k$-th Bit**: `(n & (1 << k)) != 0`
* **Alternating Bits Check**: `int x = n ^ (n >> 1); return (x & (x + 1)) == 0;`
* **Longest 1s After Flipping One 0**: Maintain `prevLen` and `currLen`; update `maxLen = Math.max(maxLen, prevLen + currLen + 1)`

---

## 2. Number Theory & Hardware Arithmetic
* **Euler's Totient $\phi(n)$**: $\phi(n) = n \prod_{p \mid n} (1 - \frac{1}{p})$ in $O(\sqrt{n})$ time, $O(1)$ space. *(e.g., $\phi(360) = 96$)*
* **Euclidean GCD**: $\gcd(a, b) = \gcd(b, a \pmod b)$
* **Extended GCD**: $a x + b y = \gcd(a, b) \implies x = y_1, \, y = x_1 - \lfloor a/b \rfloor y_1$
* **Segmented Sieve**: Precompute primes up to $\sqrt{R}$; offset window indices by $L$ in range $[L, R]$. Memory is $O(R - L + 1)$.
* **Booth's Multiplication**:
  - `Q_0 Q_{-1} = 10` $\implies A = A - M$, then Arithmetic Shift Right (ASR)
  - `Q_0 Q_{-1} = 01` $\implies A = A + M$, then Arithmetic Shift Right (ASR)
  - `00` or `11` $\implies$ ASR directly (Sign bit of $A$ is preserved)
* **Strobogrammatic Pairs**: `(0,0)`, `(1,1)`, `(8,8)`, `(6,9)`, `(9,6)`.

---

## 3. Linear DSA, Stacks, Queues & Strings
* **Min-Stack in $O(1)$ Extra Space**:
  - **Push($x$)**: If $x < \min \implies$ push $2x - \min$ to stack; $\min = x$.
  - **Pop()**: If $\text{top} < \min \implies$ restore previous $\min = 2\min - \text{top}$.
  - **Top()**: If $\text{top} < \min \implies$ return $\min$; else return $\text{top}$.
* **Circular Queue (Array of size $C$)**:
  - Full: `(rear + 1) % C == front`
  - Enqueue: `rear = (rear + 1) % C`
  - Dequeue: `front = (front + 1) % C`
* **Floyd's Cycle Detection**: Slow moves 1 step, Fast moves 2 steps. Meeting confirms loop. Reset slow to `head` and advance both 1 step $\implies$ meet at **loop start**.
* **Sliding Window Maximum**: Monotonic decreasing Deque storing indices. Front contains max element in $O(N)$ total time.
* **In-Place Hyphen Shift**: Read right-to-left, place non-hyphens from the end, prepend hyphens in $O(1)$ space.
* **Equilibrium Index**: `totalSum - leftSum - arr[i] == leftSum` in single $O(N)$ pass.
* **Block Swap Array Rotation**: Swap matching blocks of size $d$ and $n-d$ recursively in $O(N)$ time, $O(1)$ space.
* **Run-Length Encoding**: Contiguous count tracking: `"aaabbc"` $\to$ `"a3b2c1"`.

---

## 4. Greedy Algorithms & Backtracking
* **Activity Selection**: Sort by finish time ascending. Greedily select next activity with $s_i \ge f_{\text{last}}$.
* **Huffman Coding**:
  - Min-Priority Queue repeatedly merges two lowest frequency nodes.
  - Prefix-free variable-length codes.
  - $\text{Average Bits/Symbol} = \sum (f_i \times \text{codeLength}_i) / \sum f_i$.
* **Weight of Substring ($L28$)**:
  - $W(0) = 1 ('A')$; $W(i) = (i + 2) W(i - 1)$ for $i \ge 1$.
  - Greedily pick largest character $\le K$, subtract weight, and reverse string for lexicographical order.
* **Josephus Recurrence**:
  - $J(n, k) = (J(n - 1, k) + k) \pmod n$ with $J(1, k) = 0$ (0-indexed).
  - Add 1 for 1-indexed survivor!
* **$N$-Queens Bitmasking**: Valid bitmask $= \text{allDone} \ \& \ \sim(\text{cols} \mid \text{d1} \mid \text{d2})$. Advance diagonals: `(d1 | bit) << 1`, `(d2 | bit) >> 1`.
* **Hamiltonian Cycle**: Backtracking to visit all $V$ vertices once; check edge from last node back to start node.

---

## 5. Dynamic Programming & Trees/Graphs
* **0/1 Knapsack (1D Array)**:
  - $dp[w] = \max(dp[w], val[i] + dp[w - wt[i]])$
  - Traverse $w$ **backwards** from $W$ down to $wt[i]$.
* **Longest Common Subsequence (LCS)**:
  - If $s_1[i-1] == s_2[j-1] \implies 1 + dp[i-1][j-1]$; else $\max(dp[i-1][j], dp[i][j-1])$.
* **Tree Traversals**:
  - **Preorder**: Root $\to$ Left $\to$ Right ($DLR$)
  - **Inorder**: Left $\to$ Root $\to$ Right ($LDR$)
  - **Postorder**: Left $\to$ Right $\to$ Root ($LRD$)
  - **Level Order**: BFS using `Queue<TreeNode>`
* **Dijkstra's Algorithm**: Min-Heap priority queue; relaxes edges in $O((V + E) \log V)$ time. Fails on negative edge weights.
* **Kruskal's MST**: Sort edges by weight; Disjoint Set Union (DSU) with path compression and rank in $O(E \log E)$.

---

## 6. Master Complexity Reference Table

| Algorithm | Best Time | Average Time | Worst Time | Auxiliary Space |
|:---|:---|:---|:---|:---|
| **Sieve of Eratosthenes** | $O(N \log \log N)$ | $O(N \log \log N)$ | $O(N \log \log N)$ | $O(N)$ |
| **Segmented Sieve** | $O((R-L+1) \log \log R)$ | $O((R-L+1) \log \log R)$ | $O((R-L+1) \log \log R)$ | $O(\sqrt{R} + (R-L+1))$ |
| **Euler's Totient $\phi(n)$** | $O(\sqrt{N})$ | $O(\sqrt{N})$ | $O(\sqrt{N})$ | $O(1)$ |
| **Sliding Window Maximum** | $O(N)$ | $O(N)$ | $O(N)$ | $O(K)$ |
| **Min-Stack (Constant Space)** | $O(1)$ | $O(1)$ | $O(1)$ | $O(1)$ |
| **Floyd Cycle Detection** | $O(N)$ | $O(N)$ | $O(N)$ | $O(1)$ |
| **Huffman Coding** | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(N)$ |
| **$N$-Queens Backtracking** | $O(N!)$ | $O(N!)$ | $O(N!)$ | $O(N)$ |
| **Hamiltonian Cycle** | $O(N!)$ | $O(N!)$ | $O(N!)$ | $O(N)$ |
| **0/1 Knapsack DP** | $O(N \cdot W)$ | $O(N \cdot W)$ | $O(N \cdot W)$ | $O(W)$ |
| **Longest Common Subsequence**| $O(M \cdot N)$ | $O(M \cdot N)$ | $O(M \cdot N)$ | $O(M \cdot N)$ |
| **Dijkstra Shortest Path** | $O((V + E) \log V)$ | $O((V + E) \log V)$ | $O((V + E) \log V)$ | $O(V)$ |
| **Kruskal's MST (DSU)** | $O(E \log E)$ | $O(E \log E)$ | $O(E \log E)$ | $O(V)$ |
| **Tree Level Order (BFS)** | $O(N)$ | $O(N)$ | $O(N)$ | $O(W_{\text{tree}})$ |
