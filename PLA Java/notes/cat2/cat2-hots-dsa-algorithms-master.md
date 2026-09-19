# ⚡ CAT-2 HOTS Master Crib — PLA Java DSA & Algorithms Complete Suite
**Course**: Competitive Coding Practices (PLA1006 / PLA1004) — VIT Bhopal  
**Coverage**: All 18 Official Syllabus Topics across Modules 3 & 4  
**Source Alignment**: Official Faculty PPTs (L28–L38, LinkedList, Stack, CircularQueue, Huffman) & Internal Assessment Hard  
**Exam Mode**: Open Book / Notes Allowed | **Target Score**: 45+ / 50 (S-Grade)

---

## 🏆 Official Sample Papers Solved (Fall 2026–27)

* 📄 **[Official Sample Paper I Complete Solved Guide (50 Marks + Bonus)](./cat2-pla1004-sample-paper-1-solved.md)**:
  - **Q1 [10M]**: In-Place Hyphen Shifting on `"sys-log-v3-err"` under zero-allocation hardware constraints ($O(n)$ time, $O(1)$ space).
  - **Q2 [10M]**: Mars Satellite Huffman Prefix Coding ($S:32, F:23, T:10, P:10, E:5$), 200 telemetry codes bit length (420 bits vs 600 fixed bits, 30.0% savings).
  - **Q3 [10M]**: Microservices Logical Circular Heartbeat Ring Josephus recurrence $J(n, 3)$ derivation & exact survivor table for $n=1..8$ (Surviving Node 6).
  - **Q4 [10M]**: Hardware Min Stack $O(1)$ space via $(2x - \min)$ modified value encoding with execution trace on $[8, 5, 4, 10]$ + Pop.
  - **Q5(a) [5M]**: Autonomous Delivery Drone $3 \times 3$ state-space grid backtracking with hazards.
  - **Q5(b) [5M]**: Singly Linked List: One-Pass Removal of $N$-th Node from End ($N=2$ on `101 -> 102 -> 103 -> 104 -> 105`) using Two-Pointer Fixed-Gap strategy.
  - **Bonus [Image]**: Greedy Activity Selection on `start = [1, 3, 0, 5]` and `finish = [2, 4, 6, 7]` (Selected: $A_0, A_1, A_3 \to 3$ activities).

---

## 🧭 Master Topic Navigation Table (All 18 Topics)

| # | Topic | Primary Note File | Source PPT | Key Formula / Core Logic |
|:---:|:--- |:--- |:--- |:--- |
| **1** | **Move hyphen to beginning** | [Module 3 Notes](./cat2-hots-module3-linear-dsa-sliding-window.md#1-move-hyphen-to-beginning-l29-move-hyphen-to-beginningpptx) | `L29-Move hyphen to beginning.pptx` | Two-pointer: copy characters right-to-left, pad hyphens at front |
| **2** | **Lexicographically first palindromic string** | [Module 3 Notes](./cat2-hots-module3-linear-dsa-sliding-window.md#2-lexicographically-first-palindromic-string) | Standard Competitive Coding | Frequency array: at most 1 odd count allowed; left + center + reverse(left) |
| **3** | **Weighted substring** | [Module 3 Notes](./cat2-hots-module3-linear-dsa-sliding-window.md#3-weighted-substring-l28--weightes-substringpptx) | `L28- Weightes substring.pptx` | `values[i] = (i+1)*prev + prev`; binary search floor greedy deduction |
| **4** | **Manacher's Algorithm** | [Module 3 Notes](./cat2-hots-module3-linear-dsa-sliding-window.md#4-manachers-algorithm-l30-manacher_s-algorithmpptx) | `L30-Manacher_s Algorithm.pptx` | Odd transformation with `@#a#b#c#$`, LPS array $L[i]$, mirror $2C - i$ |
| **5** | **Maneuvering** | [Module 4 Notes](./cat2-hots-module4-greedy-backtracking-trees.md#1-maneuvering-a-cave-problem-l32-maneuveringpptx) | `L32-Maneuvering.pptx` | $Paths(m, n) = Paths(m-1, n) + Paths(m, n-1) = \binom{m+n-2}{m-1}$ |
| **6** | **N-Queens** | [Module 4 Notes](./cat2-hots-module4-greedy-backtracking-trees.md#2-n-queens-problem-l36-n-queenspptx--bitmask-optimization) | `L36-N Queens.pptx` | Row-by-row backtracking with bitmask: `available = fullMask & ~(cols \| d1 \| d2)` |
| **7** | **Josephus Problem** | [Module 3 Notes](./cat2-hots-module3-linear-dsa-sliding-window.md#8-josephus-problem-l34-josephus-trappptx) | `L34-Josephus trap.pptx` | PPT Formula: $J(n, k) = (J(n-1, k) + k - 1) \pmod n + 1$ (1-indexed) |
| **8** | **Activity Selection Problem** | [Module 4 Notes](./cat2-hots-module4-greedy-backtracking-trees.md#3-activity-selection-problem-l38-activity-selectionpptx) | `L38-Activity Selection.pptx` | Sort by finish time; pick if `start >= lastFinish` ($O(n \log n)$) |
| **9** | **Huffman Coding** | [Module 4 Notes](./cat2-hots-module4-greedy-backtracking-trees.md#4-huffman-coding-huffmancodingpptx) | `HuffmanCoding.pptx` | Greedy min-heap `PriorityQueue`: fuse two lowest frequencies |
| **10** | **Introductions to data structures** | [Module 3 Notes](./cat2-hots-module3-linear-dsa-sliding-window.md#1-the-3-core-data-structures-at-a-glance) | Core DSA Foundations | Linked list (node pointers), Stack (LIFO), Queue (FIFO) |
| **11** | **Reverse LL (iterative + recursive)** | [Module 3 Notes](./cat2-hots-module3-linear-dsa-sliding-window.md#5-linked-list-suite-linkedlist_problemspptx) | `LinkedList_Problems.pptx` | Iterative: `prev, curr, next` ($O(1)$ space); Recursive: call stack ($O(n)$ space) |
| **12** | **Detect / remove loop** | [Module 3 Notes](./cat2-hots-module3-linear-dsa-sliding-window.md#5-linked-list-suite-linkedlist_problemspptx) | `LinkedList_Problems.pptx` | Floyd's cycle: slow (1x) & fast (2x) collision; reset slow to head to find loop start |
| **13** | **Merge sorted lists** | [Module 3 Notes](./cat2-hots-module3-linear-dsa-sliding-window.md#5-linked-list-suite-linkedlist_problemspptx) | `LinkedList_Problems.pptx` | Iterative dummy node splice ($O(n_1 + n_2)$ time, $O(1)$ space) |
| **14** | **Balanced parentheses** | [Module 3 Notes](./cat2-hots-module3-linear-dsa-sliding-window.md#6-stack-problems-suite-stack_problemspptx) | `Stack_Problems.pptx` | Push open brackets `(`, `[`, `{`; pop and match on closing brackets |
| **15** | **Next greater element** | [Module 3 Notes](./cat2-hots-module3-linear-dsa-sliding-window.md#6-stack-problems-suite-stack_problemspptx) | `Stack_Problems.pptx` | Monotonic decreasing stack: traverse right to left, pop $\le curr$ |
| **16** | **Min stack** | [Module 3 Notes](./cat2-hots-module3-linear-dsa-sliding-window.md#6-stack-problems-suite-stack_problemspptx) | `Stack_Problems.pptx` | Dual stacks OR single stack with $2x - min$ encoding in $O(1)$ |
| **17** | **Circular queue** | [Module 3 Notes](./cat2-hots-module3-linear-dsa-sliding-window.md#7-circular-queue--sliding-window-max-circularqueue_slidingwindowpptx) | `CircularQueue_SlidingWindow.pptx` | Modulo wrap: `(rear + 1) % capacity`, full check `size == capacity` |
| **18** | **Sliding window maximum (deque)** | [Module 3 Notes](./cat2-hots-module3-linear-dsa-sliding-window.md#7-circular-queue--sliding-window-max-circularqueue_slidingwindowpptx) | `CircularQueue_SlidingWindow.pptx` | Monotonic decreasing deque: pop smaller from back, pop expired from front |
| **Bonus** | **Sorted Unique Permutations** | [Module 4 Notes](./cat2-hots-module4-greedy-backtracking-trees.md#5-sorted-unique-permutations-l31-sorted-unique-permutationpptx) | `L31-Sorted Unique Permutation.pptx` | Sort string first; prune duplicates at each level using `Set<Character>` |
| **Bonus** | **Rat in a Maze** | [Module 4 Notes](./cat2-hots-module4-greedy-backtracking-trees.md#6-rat-in-a-maze-l35-maze-solvingpptx) | `L35-Maze Solving.pptx` | Binary matrix backtracking: Down, Right recursive exploration |
| **Bonus** | **Warnsdorff's Knight's Tour** | [Module 4 Notes](./cat2-hots-module4-greedy-backtracking-trees.md#7-warnsdorffs-algorithm-for-knights-tour-l37-warnsdorffs-algorithmpptx) | `L37-Warnsdorff’s Algorithm.pptx` | Greedy choice: always move to the neighbor with **minimum degree** |
