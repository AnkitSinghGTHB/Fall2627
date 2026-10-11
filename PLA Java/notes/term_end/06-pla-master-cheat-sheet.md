# 📑 PLA1004: Master Algorithms & Complexity Cheat Sheet (1-Page)

> Keep this open for rapid syntax, bitwise hacks, recurrences, and complexities before the exam on October 25!

---

## 1. Master Bitwise Hacks
* **Power of 2**: `n > 0 && (n & (n - 1)) == 0`
* **Count Set Bits (Kernighan)**: `while(n > 0) { n &= (n - 1); count++; }`
* **Swap Nibbles (Byte)**: `((n & 0x0F) << 4) | ((n & 0xF0) >> 4)`
* **Lowest Set Bit**: `n & -n`
* **Toggle k-th Bit**: `n ^ (1 << k)`

---

## 2. Number Theory Formulas
* **Euler's Totient**: $\phi(n) = n \prod_{p \mid n} (1 - 1/p)$ in $O(\sqrt{n})$
* **GCD**: $\gcd(a, b) = \gcd(b, a \pmod b)$
* **Josephus Recurrence**: $J(n, k) = (J(n-1, k) + k) \pmod n$ with $J(1, k) = 0$
* **Grid Paths**: $\binom{m + n - 2}{m - 1}$ paths from $(0, 0)$ to $(m-1, n-1)$

---

## 3. Data Structures & Core Idioms
* **Sliding Window Max**: Monotonic decreasing Deque storing indices, $O(N)$ time
* **Min Stack $O(1)$ space**: Push $2x - \min$ when $x < \min$; Pop recovers $\min = 2\min - top$
* **Cycle in Linked List**: Fast $= 2\times$, Slow $= 1\times$. Reset slow to head to find loop entry.
* **In-place Hyphen Shift**: Read right-to-left, write non-hyphens from end, prepend hyphens.

---

## 4. Master Complexity Table

| Algorithm | Best Time | Average Time | Worst Time | Space |
|:---|:---|:---|:---|:---|
| **Sieve of Eratosthenes** | $O(N \log \log N)$ | $O(N \log \log N)$ | $O(N \log \log N)$ | $O(N)$ |
| **Segmented Sieve** | $O((R-L) \log \log R)$ | $O((R-L) \log \log R)$ | $O((R-L) \log \log R)$ | $O(\sqrt{R})$ |
| **Euler's Totient $\phi$** | $O(\sqrt{N})$ | $O(\sqrt{N})$ | $O(\sqrt{N})$ | $O(1)$ |
| **Sliding Window Max** | $O(N)$ | $O(N)$ | $O(N)$ | $O(K)$ |
| **Huffman Coding** | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(N)$ |
| **0/1 Knapsack DP** | $O(N \cdot W)$ | $O(N \cdot W)$ | $O(N \cdot W)$ | $O(W)$ |
| **Longest Common Subsequence** | $O(M \cdot N)$ | $O(M \cdot N)$ | $O(M \cdot N)$ | $O(M \cdot N)$ |
| **Dijkstra Shortest Path** | $O((V + E) \log V)$ | $O((V + E) \log V)$ | $O((V + E) \log V)$ | $O(V)$ |
| **Kruskal's MST (DSU)** | $O(E \log E)$ | $O(E \log E)$ | $O(E \log E)$ | $O(V)$ |
