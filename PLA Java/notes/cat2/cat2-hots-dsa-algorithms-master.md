# ⚡ CAT-2 HOTS Master Crib — PLA Java DSA & Algorithms Master Suite
**Course**: Competitive Coding Practices (PLA1006 / PLA1004) — VIT Bhopal  
**Coverage**: Modules 3 & 4 (Sliding Window, Two Pointers, Backtracking, Greedy, Monotonic Stacks, Advanced Queues)  
**Source Alignment**: FacePrep Internal Assessment (LeetCode Hard), VIT CAT-2 Syllabus  
**Exam Mode**: Open Book / Notes Allowed | **Target Score**: 45+ / 50 (S-Grade)

---

## ⚡ Master Navigation

| Module | Core Exam Topics | Direct Link |
| :--- | :--- | :--- |
| **Module 3: Linear DSA, Sliding Window & Advanced Queues** | • **Sliding Window Maximum (LC 239)** with Monotonic Deque ($O(n)$)<br>• **Maximum Weighted Palindromic Substring** with Manacher's ($O(n)$)<br>• **Josephus Elimination Queue** with Order-Statistics BIT ($O(\log n)$)<br>• **Cyclic Linked List Repair** with Floyd's Cycle Removal ($O(1)$ space)<br>• **Minimum Bracket Deletions** with Monotonic Stack ($O(n)$) | [cat2-hots-module3-linear-dsa-sliding-window.md](./cat2-hots-module3-linear-dsa-sliding-window.md) |
| **Module 4: Backtracking, Bitmasking & Greedy Scheduling** | • **Queens on a Broken Board** with Bitmask Pruning ($O(n \cdot 2^n)$)<br>• **Scheduled Merge Cost** (Huffman Merging under Time Windows)<br>• **Activity Selection & Interval Scheduling** ($O(m \log m)$)<br>• **Classic N-Queens Bitmask Solver** with lowest set bit optimization | [cat2-hots-module4-greedy-backtracking-trees.md](./cat2-hots-module4-greedy-backtracking-trees.md) |

---

## 🧭 Rapid Exam Problem Identifier & Formula Cheat Sheet

| If You See This in the Exam Question... | Use This Pattern | Golden Code Snippet / Recurrence |
| :--- | :--- | :--- |
| Max/Min in every sliding subarray of length $k$ | **Monotonic Deque** | `while (!d.isEmpty() && nums[d.peekLast()] <= nums[i]) d.pollLast();` |
| Longest or weighted palindrome in $O(n)$ | **Manacher's Algorithm + Prefix Weights** | `T = "^#" + join('#') + "#$"; P[i] = min(R - i, P[mirror]);` |
| $k$-th person eliminated in circle (large $k$, $n \le 2 \times 10^5$) | **Order Statistics (Fenwick BIT)** | `targetRank = (currentRank + (k - 1) % totalAlive) % totalAlive + 1;` |
| Detect & remove loop in linked list in $O(1)$ space | **Floyd's Tortoise & Hare** | `slow = head; while (slow.next != fast.next) { slow = slow.next; fast = fast.next; } fast.next = null;` |
| Remove minimum brackets to balance string | **Stack Tracking Unmatched Indices** | Push index of `(`, pop on `)`, any unmatched `)` or remaining `(` are deleted |
| $N$-Queens with obstacles / broken cells | **Bitmask Backtracking** | `available = fullMask & ~(cols | d1 | d2 | brokenMask[row]);` |
| Merge piles with non-overlapping time windows | **Activity Selection + Huffman Min-Heap** | Sort slots by `end`; if valid slots $\ge n-1$, merge smallest pairs in `PriorityQueue` |
