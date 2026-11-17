# 🚀 PLA1004: Last-Minute Exam Hall Survival Guide & 100% Attempt Blueprint

> **Exam Date**: Sunday, October 25, 2026 (01:15 PM – 04:15 PM)  
> **Course**: PLA1004 — Competitive Coding Practices (Java)  
> **Primary Rule**: **DO NOT LEAVE ANY QUESTION BLANK!** Follow the 4-part faculty step-marking blueprint below.

---

## 🛡️ Part 1: The 4-Part Faculty Step-Marking Blueprint

VIT examiners grade strictly via **step-wise marking**. Even if you have not memorized the most complex algorithm or your code has small syntax slips, writing the following **4 clean sections** for each question guarantees **80% to 100% marks**:

```
┌────────────────────────────────────────────────────────────────────────┐
│               THE 4-PART HIGH-SCORING ANSWER STRUCTURE                │
├────────────────────────────────────────────────────────────────────────┤
│ 1. APPROACH / CORE LOGIC (2-3 bullet points)                           │
│    • State the data structure used (e.g. Monotonic Deque, Min-Heap).   │
│    • Explain the decision rule in plain English.                       │
├────────────────────────────────────────────────────────────────────────┤
│ 2. CLEAN & INTUITIVE JAVA CODE                                         │
│    • Keep it simple! Faculty prefers straightforward, readable logic   │
│      (e.g., two StringBuilders, clean while loops) over obscure hacks. │
├────────────────────────────────────────────────────────────────────────┤
│ 3. DRY RUN / TRACE TABLE (HIGH VALUE - 2 to 4 Marks!)                  │
│    • Pick the sample input from question (or a small 3-4 item array).  │
│    • Show step-by-step variable values (iteration, pointers, output).  │
├────────────────────────────────────────────────────────────────────────┤
│ 4. TIME & SPACE COMPLEXITY ANALYSIS                                    │
│    • Clearly write: Time Complexity = O(...)                           │
│    • Clearly write: Auxiliary Space = O(...)                           │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🧠 Part 2: Master Memory Anchors for All 10 Questions

Every single slot of PLA1004 follows an identical blueprint:
- **Section A (12 Marks each)**: Questions 1 to 5 (One from each Unit 1 to 5)
- **Section B (8 Marks each)**: Questions 6 to 10 (One from each Unit 1 to 5)

Here is your rapid-recall memory anchor for every possible question:

---

### 📦 UNIT 1 (Sec A: Q1 [12M] | Sec B: Q6 [8M])
*Complexity Analysis, Elementary Math, Basic Sorting/Searching*

1. **Move Hyphens to Beginning (Intuitive 100% Correct Method)**:
   * **Do NOT overcomplicate with pointers!** Use two `StringBuilder`s:
     ```java
     StringBuilder hyphens = new StringBuilder();
     StringBuilder chars = new StringBuilder();
     for (char c : s.toCharArray()) {
         if (c == '-') hyphens.append(c);
         else chars.append(c);
     }
     return hyphens.append(chars).toString(); // Time O(N), Space O(N)
     ```
2. **Simple Sieve of Eratosthenes**:
   * Boolean array `isPrime[]` of size $n+1$, initialize to `true`.
   * Outer loop $p = 2 \dots \sqrt{n}$. If `isPrime[p]`, mark multiples $p^2, p^2 + p, \dots \le n$ as `false`.
   * **Complexity**: Time: $O(n \log \log n)$, Space: $O(n)$.
3. **Strobogrammatic Number**:
   * Reversible digits upside-down: `(0,0)`, `(1,1)`, `(8,8)`, `(6,9)`, `(9,6)`.
   * Use two pointers (`left = 0, right = s.length() - 1`). If pair is not in the set, return `false`.
4. **Insertion Sort Shift Trace**:
   * For $\{5, 2, 4, 6, 1, 3\}$, dry run pass-by-pass $\implies$ **Total Shifts = 9**.
   * Best case (sorted): $O(N)$ time, 0 shifts. Worst case (reverse): $O(N^2)$ time, $n(n-1)/2$ shifts.
5. **Asymptotic Bounds & Loop Complexity**:
   * $O$ (Big-O) = Upper bound ($f(n) \le c \cdot g(n)$).
   * $\Omega$ (Big-Omega) = Lower bound ($f(n) \ge c \cdot g(n)$).
   * $\Theta$ (Big-Theta) = Tight bound ($c_1 g(n) \le f(n) \le c_2 g(n)$).
   * Outer loop $i = 1 \dots n$, inner loop $j = 1, 2, 4 \dots n$ $\implies O(n \log n)$.

---

### 📦 UNIT 2 (Sec A: Q2 [12M] | Sec B: Q7 [8M])
*Bit Manipulation, Number Theory & Matrix/Array Mechanics*

1. **Swap Two Nibbles in a Byte**:
   * **Bitwise Formula**: `((n & 0x0F) << 4) | ((n & 0xF0) >> 4)`
   * *Dry run on $0x4D$*: $0100\,1101_2 \to 1101\,0100_2 = 0xD4 = \mathbf{212_{10}}$.
2. **Toggle the Switch (1 to $N$)**:
   * **Mathematical Proof**: Switch $k$ is toggled once for every divisor of $k$.
   * Only **perfect squares** ($1, 4, 9, 16, \dots$) have an **odd number of factors** (because $\sqrt{k} \times \sqrt{k} = k$ pairs with itself). All other numbers have an even number of factors and end up OFF.
   * **Final Answer**: Exactly $\lfloor \sqrt{N} \rfloor$ switches remain ON!
3. **Longest 1s with 1 Bit Flip**:
   * For $N = 1775$ ($11011101111_2$): **Answer is 8**.
   * Track `currLen` and `prevLen`. When `0` seen: `max = Math.max(max, prevLen + currLen + 1); prevLen = currLen; currLen = 0;`.
4. **Euler's Totient Function $\varphi(N)$**:
   * Formula: $\varphi(N) = N \prod_{p \mid N} \left(1 - \frac{1}{p}\right)$ in $O(\sqrt{N})$.
   * $\varphi(36) = 36 \times (1 - 1/2) \times (1 - 1/3) = 36 \times \frac{1}{2} \times \frac{2}{3} = \mathbf{12}$.
   * $\varphi(100) = 100 \times (1 - 1/2) \times (1 - 1/5) = 100 \times \frac{1}{2} \times \frac{4}{5} = \mathbf{40}$.
   * $\varphi(97) = 97 - 1 = \mathbf{96}$ (since 97 is prime).
5. **Equilibrium Index & Sum**:
   * Compute `totalSum`. Scan array: if `totalSum - leftSum - arr[i] == leftSum`, return index $i$. Update `leftSum += arr[i]`. Single pass $O(N)$ time, $O(1)$ space.
6. **Array Rotation by 3 Reversals**:
   * Right rotate by $k$: `k = k % n; reverse(0, n-1); reverse(0, k-1); reverse(k, n-1);` ($O(N)$ time, $O(1)$ space).
7. **Dutch National Flag (Sort 0, 1, 2)**:
   * 3 Pointers: `low = 0, mid = 0, high = n - 1`. If `0`: swap(`low`, `mid`), `low++`, `mid++`. If `1`: `mid++`. If `2`: swap(`mid`, `high`), `high--`.

---

### 📦 UNIT 3 (Sec A: Q3 [12M] | Sec B: Q8 [8M])
*Greedy Algorithms, Backtracking, Palindromes & Recurrences*

1. **Josephus Problem**:
   * Recurrence: $J(n, k) = (J(n-1, k) + k) \pmod n$ with $J(1, k) = 0$ (0-indexed). Add 1 for 1-indexed.
   * For $n=7, k=3$: Survivor = index $3 \implies \mathbf{4}$ (1-indexed).
   * For $n=8, k=3$: Survivor = index $6 \implies \mathbf{7}$ (1-indexed).
2. **Activity Selection**:
   * **Greedy Choice**: Sort activities by **finish time ascending**!
   * Pick first activity. For subsequent activities, pick if `start >= finish_of_last_selected`.
3. **Huffman Coding**:
   * Insert frequencies into a Min-Heap.
   * While heap size $> 1$: Extract 2 smallest nodes ($n_1, n_2$), make a parent with $\text{freq} = f_1 + f_2$, re-insert into heap.
   * Left branch = `'0'`, Right branch = `'1'`. Optimal prefix-free compression.
4. **$N$-Queens Backtracking ($N=4$)**:
   * Place queens row by row. Safety condition: no conflict in column, left diagonal (`row - col`), or right diagonal (`row + col`).
   * 2 solutions exist: `[2, 4, 1, 3]` and `[3, 1, 4, 2]`. Backtracking state tree prunes search from 256 naive states.
5. **Lexicographically Smallest Palindrome**:
   * Count character frequencies. If more than 1 character has odd count $\to$ **Impossible**.
   * Put half of each character in alphabetical order on left, middle = odd character (if any), mirror on right.
   * For `"aabbccd"` $\to$ `'d'` is odd $\implies$ `"abcdcba"`.

---

### 📦 UNIT 4 (Sec A: Q4 [12M] | Sec B: Q9 [8M])
*Linked Lists, Stacks, Queues & Sliding Window*

1. **Reverse Singly Linked List**:
   * **Iterative (3 Pointers - O(1) Space)**:
     ```java
     Node prev = null, curr = head, next = null;
     while (curr != null) {
         next = curr.next;
         curr.next = prev;
         prev = curr;
         curr = next;
     }
     return prev;
     ```
   * **Recursive**: Base case `if (head == null || head.next == null) return head;`. Call `newHead = reverse(head.next); head.next.next = head; head.next = null; return newHead;` (Uses $O(N)$ stack space).
2. **Floyd's Loop Detection & Removal (Without Node Loss)**:
   * Tortoise & Hare: `slow = slow.next`, `fast = fast.next.next`. If `slow == fast`, loop detected.
   * **Removal**: Reset `slow = head`. Move both by 1 step (`slow = slow.next`, `fast = fast.next`) until `slow.next == fast.next`. Set `fast.next = null`.
3. **Min Stack**:
   * **Exam Safe Dual-Stack**: Maintain `mainStack` and `minStack`.
   * On `push(x)`: push to `mainStack`. If `minStack.isEmpty() || x <= minStack.peek()`, push to `minStack`.
   * On `pop()`: if `mainStack.pop().equals(minStack.peek())`, `minStack.pop()`.
   * All operations $O(1)$ time.
4. **Next Greater Element (NGE) / Stock Span**:
   * Use a **Monotonic Decreasing Stack** storing indices or values.
   * For each element, pop elements from stack that are smaller. Push current element. $O(N)$ time because each element is pushed and popped at most once.
5. **Circular Queue Array Implementation**:
   * Array of capacity $C$, pointers `front = -1, rear = -1`.
   * **Full condition**: `(rear + 1) % C == front`
   * **Empty condition**: `front == -1`
   * **Enqueue**: `if (front == -1) front = 0; rear = (rear + 1) % C; arr[rear] = val;`
   * **Dequeue**: `val = arr[front]; if (front == rear) { front = rear = -1; } else { front = (front + 1) % C; }`

---

### 📦 UNIT 5 (Sec A: Q5 [12M] | Sec B: Q10 [8M])
*Trees, Graph Traversals, Shortest Paths & MST*

1. **Shortest Path in Unweighted Graph**:
   * **Always use BFS (Breadth-First Search) with a Queue!**
   * *Why BFS and not DFS?* BFS explores vertices in strictly increasing order of distance from source (level-by-level). The first time the destination is dequeued, the path is mathematically guaranteed to be the shortest. DFS explores arbitrary deep branches and may find a much longer path.
2. **Connected Components in Undirected Graph**:
   * Loop $v = 0 \dots V-1$. If `!visited[v]`, call `bfs(v)` and `count++`.
   * *Why BFS over recursive DFS for $V = 10^5$?* A degenerate line graph has depth $10^5$. Recursive DFS will trigger a **StackOverflowError** due to JVM call stack limits. BFS uses a heap-allocated Queue and never overflows the call stack.
3. **Kruskal's Algorithm for MST**:
   * 1. Sort all edges by weight in ascending order.
   * 2. Initialize Disjoint Set Union (DSU) where each vertex is its own parent.
   * 3. Iterate through sorted edges: if `find(u) != find(v)`, include edge in MST and perform `union(u, v)`. If `find(u) == find(v)`, **reject edge** (it forms a cycle).
   * **Complexity**: $O(E \log E)$ time, $O(V)$ auxiliary space.
4. **Binary Tree Height & Diameter in Single Pass $O(N)$**:
   ```java
   int maxDiameter = 0;
   int height(TreeNode root) {
       if (root == null) return 0;
       int lh = height(root.left);
       int rh = height(root.right);
       maxDiameter = Math.max(maxDiameter, lh + rh);
       return 1 + Math.max(lh, rh);
   }
   ```
5. **Tree Traversals**:
   * **Preorder**: $Root \to Left \to Right$ ($DLR$)
   * **Inorder**: $Left \to Root \to Right$ ($LDR$)
   * **Postorder**: $Left \to Right \to Root$ ($LRD$)
   * **Level Order**: Queue BFS

---

## 🆘 Part 3: Emergency "I Forgot the Algorithm" Rescue Protocol

If you open the paper and encounter a question where you don't recall the exact optimal algorithm, **DO NOT SKIP IT!** Follow this rescue protocol:

1. **Write the Brute Force Solution**:
   * Even a simple nested loop (e.g. $O(N^2)$ brute force instead of $O(N)$ monotonic stack or sliding window) will get you **70–80% of the coding marks** if it produces the correct output.
   * Faculty marks code that works; an honest brute force is vastly better than half-remembered broken code.
2. **State the Invariant / Logic in English**:
   * Write: *"The optimal solution can be achieved in $O(N)$ using a Monotonic Stack/Deque to maintain elements in sorted order while sliding the window."*
3. **Draw the Dry Run**:
   * Show manually how the answer is calculated for the sample input. This proves you understand the problem.
4. **State the Complexities**:
   * Write down the brute force complexity vs the optimal target complexity.

---

## ⏱️ Part 4: 3-Hour Exam Hall Pacing & Clock Strategy

| Time Window | Target Section | Marks Target | Focus & Mindset |
| :--- | :--- | :---: | :--- |
| **01:15 PM – 02:45 PM** (90 mins) | **Section A (5 Qs × 12M)** | **60 Marks** | Spend ~18 mins per question. Follow the 4-part structure (Approach $\to$ Code $\to$ Trace $\to$ Complexity). |
| **02:45 PM – 03:55 PM** (70 mins) | **Section B (5 Qs × 8M)** | **40 Marks** | Spend ~14 mins per question. Direct, concise code and dry run. |
| **03:55 PM – 04:15 PM** (20 mins) | **Review & Buffer** | **Audit** | Scan every question: Ensure no question is left blank, check edge cases (null checks, empty arrays). |

---

## 🎯 Final Confidence Booster
* You do **not** need a perfect 100/100 to secure an **A Grade** (only ~65/100 needed!).
* Keep your handwriting clean, underline key headings (`Approach`, `Code`, `Dry Run`, `Complexity`), and write with calm confidence.

**You've got this! Go ace the exam! 🏆**
