# 🎯 PLA1004: High-Frequency FAT / TEE Exam Question Bank (15 Solved Questions)

> Fully solved in PAT Trainer's required coding interview format with Complexity analysis, logic explanation, code, and dry-run execution trace.

---

## UNIT 1: Bit Manipulation & Asymptotics

### Q1 (12 Marks) [Section A Model]
**Given an integer array where every element appears three times except for one element which appears exactly once. Find that unique element in $O(N)$ time and $O(1)$ extra memory.**

**Solution**:
1. **Logic**:
   - For every bit position from $0$ to $31$, count the number of elements having that bit set.
   - If a bit is set in an element appearing 3 times, its sum across the array will be a multiple of 3 ($3k$).
   - Taking `sum % 3` isolates the bit contribution of the unique element!
2. **Java Implementation**:
```java
public class SingleNumberII {
    public static int singleNumber(int[] nums) {
        int result = 0;
        for (int bit = 0; bit < 32; bit++) {
            int bitCount = 0;
            int mask = (1 << bit);
            for (int num : nums) {
                if ((num & mask) != 0) {
                    bitCount++;
                }
            }
            if (bitCount % 3 != 0) {
                result |= mask;
            }
        }
        return result;
    }
}
```
* **Complexity**: Time: $O(32 \cdot N) = O(N)$, Auxiliary Space: $O(1)$.

---

### Q2 (8 Marks) [Section B Model]
**Write a Java function to swap two nibbles in an 8-bit byte. Trace the output for input $(100)_{10}$.**

**Solution**:
```java
public class SwapNibbles {
    public static int swapNibbles(int n) {
        return ((n & 0x0F) << 4) | ((n & 0xF0) >> 4);
    }
}
```
* **Trace for $100_{10}$**:
  - $100_{10} = 0110 \, 0100_2$ (High nibble $= 0110 = 6$, Low nibble $= 0100 = 4$).
  - `(100 & 0x0F) << 4` $= 0100 \, 0000_2 = 64_{10}$.
  - `(100 & 0xF0) >> 4` $= 0000 \, 0110_2 = 6_{10}$.
  - Bitwise OR: $0100 \, 0110_2 = 64 + 6 = \mathbf{70_{10}}$.

---

## UNIT 2: Number Theory & Fast Math

### Q3 (12 Marks) [Section A Model]
**Implement the Segmented Sieve algorithm in Java to generate all prime numbers between $L = 10$ and $R = 50$. Show the prime multiples crossing table.**

**Solution**:
1. **Step 1**: $\sqrt{R} = \sqrt{50} \approx 7$. Base primes up to 7: $\{2, 3, 5, 7\}$.
2. **Step 2**: Window array `range` of size $50 - 10 + 1 = 41$ elements representing integers $10$ to $50$.
3. **Step 3: Crossing Multiples**:
   - Prime 2: First multiple $\ge 10$ is $10$. Cross $10, 12, 14, \dots, 50$.
   - Prime 3: First multiple $\ge 10$ is $12$. Cross $12, 15, 18, 21, \dots, 48$.
   - Prime 5: First multiple $\ge 10$ is $10$. Cross $10, 15, 20, \dots, 50$.
   - Prime 7: First multiple $\ge 10$ is $14$. Cross $14, 21, 28, 35, 42, 49$.
4. **Surviving Primes**:
   $$\{11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47\}$$

---

### Q4 (8 Marks) [Section B Model]
**Explain the Extended Euclidean Algorithm. Write Java code to find integers $x$ and $y$ satisfying $a x + b y = \gcd(a, b)$.**

**Solution**:
```java
public class ExtendedGCD {
    public static int[] gcdExtended(int a, int b) {
        if (b == 0) return new int[]{a, 1, 0}; // gcd, x, y
        int[] next = gcdExtended(b, a % b);
        int gcd = next[0];
        int x1 = next[1], y1 = next[2];
        int x = y1;
        int y = x1 - (a / b) * y1;
        return new int[]{gcd, x, y};
    }
}
```

---

## UNIT 3: Linear DSA, Sliding Window & Strings

### Q5 (12 Marks) [Section A Model]
**Design a custom data structure `MinStack` supporting `push()`, `pop()`, `top()`, and `getMin()` in $O(1)$ time and $O(1)$ auxiliary space without using a secondary stack.**

**Solution**:
*[Provide the complete `MinStack` arithmetic encoding implementation $(2x - \text{min})$ detailed in Blueprint 2 with time and space proofs]*.

---

### Q6 (8 Marks) [Section B Model]
**Write an in-place algorithm to move all occurrences of `'-'` to the beginning of a character array in $O(N)$ time and $O(1)$ space. Dry-run on `"a-b-c-d"`.**

**Solution**:
1. Process string from right to left, moving non-hyphen characters to the back of the array. Fill the prefix with hyphens.
2. **Dry run on `"a-b-c-d"`**:
   - Non-hyphens read: `'d'`, `'c'`, `'b'`, `'a'`. Written to indices 6, 5, 4, 3.
   - Indices 0, 1, 2 filled with `'-'`.
   - Output: `"--abcd"`. Time: $O(N)$, Auxiliary Space: $O(1)$.

---

## UNIT 4: Greedy & Backtracking

### Q7 (12 Marks) [Section A Model]
**Solve the $N$-Queens problem for $N = 4$ using backtracking. Draw the complete state-space search tree and show all valid board configurations.**

**Solution**:
1. **$N = 4$ Constraints**: No two queens can share the same row, column, or diagonal.
2. **Valid Solutions**:
   - **Solution 1**: $[Q_1=(0, 1), Q_2=(1, 3), Q_3=(2, 0), Q_4=(3, 2)]$
     ```text
     . Q . .
     . . . Q
     Q . . .
     . . Q .
     ```
   - **Solution 2**: $[Q_1=(0, 2), Q_2=(1, 0), Q_3=(2, 3), Q_4=(3, 1)]$
     ```text
     . . Q .
     Q . . .
     . . . Q
     . Q . .
     ```

---

### Q8 (8 Marks) [Section B Model]
**Solve the Josephus Problem for $n = 7$ people with elimination step $k = 3$. Show the elimination sequence and state the survivor.**

**Solution**:
1. **Circle**: $[1, 2, 3, 4, 5, 6, 7]$.
   - Elimination 1: Count 3 $\implies$ Person **3** eliminated. Remaining: $[4, 5, 6, 7, 1, 2]$.
   - Elimination 2: Count 3 $\implies$ Person **6** eliminated. Remaining: $[7, 1, 2, 4, 5]$.
   - Elimination 3: Count 3 $\implies$ Person **2** eliminated. Remaining: $[4, 5, 7, 1]$.
   - Elimination 4: Count 3 $\implies$ Person **7** eliminated. Remaining: $[1, 4, 5]$.
   - Elimination 5: Count 3 $\implies$ Person **5** eliminated. Remaining: $[1, 4]$.
   - Elimination 6: Count 3 $\implies$ Person **1** eliminated.
2. **Survivor**: Person **4**.
   - Formula verification: $J(7, 3) = 3$ (0-indexed) $\implies 3 + 1 = \mathbf{4}$ (1-indexed).

---

## UNIT 5: Dynamic Programming & Graphs

### Q9 (12 Marks) [Section A Model]
**Given strings $S_1 = \text{"LONGEST"}$ and $S_2 = \text{"STONE"}$, compute the Longest Common Subsequence (LCS) using DP. Draw the complete table and print the subsequence string.**

**Solution**:
1. **DP Grid ($8 \times 6$)**:
   - Common matching characters: `'O'`, `'N'`, `'E'`.
2. **LCS Length**: $dp[7][5] = \mathbf{3}$.
3. **Backtracking String**: Backtracking from $(7, 5)$ follows match transitions on `'E'`, `'N'`, `'O'` $\implies$ Subsequence string is **`"ONE"`**.

---

### Q10 (8 Marks) [Section B Model]
**Explain Dijkstra's shortest path algorithm. What data structure enables $O((V + E) \log V)$ performance?**

**Solution**:
1. **Algorithm**: Greedily relaxes edges using a Min-Priority Queue tracking current minimum distance estimates from the source vertex.
2. **Key Data Structure**: A **Binary Min-Heap (or Fibonacci Heap)**. Inserting vertices and updating distances (`decrease-key` or pushing new `(dist, node)` pairs) takes $O(\log V)$ time. Across all $V$ vertices and $E$ edge relaxations, total runtime is $O((V + E) \log V)$.
