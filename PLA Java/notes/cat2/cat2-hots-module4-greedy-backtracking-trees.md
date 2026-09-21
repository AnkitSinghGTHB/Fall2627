# ⚡ CAT-2 HOTS Master Crib — Module 4: Maneuvering, Backtracking & Greedy Algorithms
**Course**: Competitive Coding Practices (PLA1006 / PLA1004) — VIT Bhopal  
**Coverage**: Maneuvering (Cave Grid Paths), N-Queens (Classic & Broken Board), Activity Selection, Huffman Coding, Sorted Unique Permutations, Combinations, Rat in a Maze, Warnsdorff's Knight's Tour  
**Source Alignment**: Official VIT Bhopal / FacePrep Lecture PPTs (L31, L32, L33, L35, L36, L37, L38, HuffmanCoding) & Internal Assessment  
**Exam Mode**: Open Book / Notes Allowed | **Target**: S-Grade (45+ / 50)

---

## 🧱 TIER 0: The "Explain Like I'm 5" Bedrock Basics

### 1. Maneuvering in a Cave: "The Only Right and Down Rule"
You are trapped at the top-left cell $(0, 0)$ of an $m \times n$ cave and must reach the exit at bottom-right $(m-1, n-1)$.
* **Constraint**: You can **only move Right or Down**.
* **Why does recursion work?** To reach cell $(m, n)$, you *must* have arrived either from the cell above $(m-1, n)$ or from the cell to the left $(m, n-1)$:
  $$\text{Paths}(m, n) = \text{Paths}(m-1, n) + \text{Paths}(m, n-1)$$
* **The Instant Combinatorics Shortcut**: Total steps needed $= (m - 1) \text{ Down} + (n - 1) \text{ Right} = m + n - 2$ total steps. You just need to choose which $m - 1$ steps are Down:
  $$\text{Total Paths} = \binom{m + n - 2}{m - 1} = \frac{(m + n - 2)!}{(m - 1)! (n - 1)!}$$

---

### 2. N-Queens: "The Safe Placement Rule"
Place $N$ non-attacking queens on an $N \times N$ chessboard.
* A queen attacks along its row, column, and two diagonals.
* Since each row must have exactly 1 queen, we place row-by-row.
* **Bitmask Supercharger**: An integer bitmask tracks occupied columns and diagonals in $O(1)$ CPU operations.

---

### 3. Activity Selection: "Earliest Finish Time Wins"
Given tasks with $[start, finish)$ times, how do you perform the maximum number of tasks without overlap?
* **Greedy Rule**: **Always pick the activity that finishes first!**
* Finishing earlier frees up the maximum remaining time for subsequent activities.

---

### 4. Huffman Coding: "The Greedy Tree Builder"
Data compression algorithm assigning shorter bit codes to frequent characters.
* Always merge the **two lowest frequency nodes** into a parent node. Repeat using a min-heap (`PriorityQueue`) until 1 tree remains.

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If the Exam Question Asks... | Use This Exact Topic & Method | Time & Space Complexity | Key Formula / Code Logic |
| :--- | :--- | :--- | :--- |
| "Count paths from top-left to bottom-right (Maneuvering)" | **Combinatorics / 2D DP** | $O(\min(m, n))$ Math / $O(m \cdot n)$ DP | $\binom{m+n-2}{m-1}$ or `dp[i][j] = dp[i-1][j] + dp[i][j-1]` |
| "Maneuvering with obstacles / blocked cells" | **Obstacle Grid 1D DP** | $O(m \cdot n)$ Time, $O(n)$ Space | If cell is obstacle, `dp[j] = 0`; else `dp[j] += dp[j-1]` |
| "Maneuvering with diagonal moves allowed" | **Delannoy Recurrence / DP** | $O(m \cdot n)$ Time, $O(n)$ Space | $Paths(m, n) = Paths(m-1, n) + Paths(m, n-1) + Paths(m-1, n-1)$ |
| "Print all maneuvering path strings (D, R)" | **DFS Path Backtracking** | $O(\binom{m+n-2}{m-1})$ Time, $O(m+n)$ Space | Recurse with `path + "D"` and `path + "R"`, collect on exit |
| "Minimum / Maximum path sum in grid" | **Grid Dynamic Programming** | $O(m \cdot n)$ Time, $O(n)$ Space | `dp[j] = grid[i][j] + min(dp[j], dp[j-1])` |
| "Place N non-attacking queens" | **Backtracking / Bitmasking** | $O(N!)$ Time, $O(N)$ Space | `available = fullMask & ~(cols \| d1 \| d2)` |
| "Queens on a broken board (obstacles)" | **Bitmask with Broken Mask** | $O(N \cdot 2^N)$ Time, $O(N)$ Space | `available = fullMask & ~(cols \| d1 \| d2 \| brokenMask[r])` |
| "Super-Queens / Maharaja (Queen + Knight moves)" | **Dual Attack Vector Backtracking** | $O(N!)$ Time, $O(N)$ Space | Queen attack check + 8 knight jump attack checks |
| "Select maximum activities without overlap" | **Activity Selection (Greedy)** | $O(n \log n)$ Time, $O(1)$ Space | Sort by `finish` time; pick if `start >= lastFinish` |
| "Construct Huffman codes / prefix tree" | **Huffman Greedy PriorityQueue** | $O(n \log n)$ Time, $O(n)$ Space | Poll two smallest, combine frequencies, re-insert |
| "Decode / Decompress Huffman bitstream" | **Prefix Tree Traversal** | $O(\text{Bits})$ Time, $O(1)$ Extra Space | Walk left on `'0'`, right on `'1'`; on leaf, append char |
| "Minimum cost to connect all ropes / merge files" | **Greedy Min-Heap (Huffman Cost)** | $O(n \log n)$ Time, $O(n)$ Space | Total Cost $= \sum \text{all internal node values}$ |
| "Distinct sorted permutations (with duplicates)" | **Backtracking with Set Pruning** | $O(n \cdot n!)$ Time, $O(n)$ Space | Sort string first; use `Set<Character>` at each level |
| "Compute combinations nCr" | **Factorial / Multiplicative Formula** | $O(r)$ Time, $O(1)$ Space | $\binom{n}{r} = \frac{n \times (n-1) \dots (n-r+1)}{r \times (r-1) \dots 1}$ |
| "Find path in maze (Rat in a Maze)" | **Matrix Backtracking** | $O(2^{N^2})$ Time, $O(N^2)$ Space | Move (D, R); mark visited, backtrack on dead end |
| "Knight's tour on NxN board" | **Warnsdorff's Algorithm** | $O(N^2)$ Heuristic Time | Greedily move to unvisited neighbor with **minimum degree** |

---

## 🛠️ TIER 2: Master Code Templates (Lecture PPT & Exam Aligned)

### 1. Maneuvering a Cave Problem (`L32-Maneuvering.pptx`)
> **Problem**: Count all possible paths from top-left $(0, 0)$ to bottom-right $(m-1, n-1)$ in an $m \times n$ matrix, moving only Right or Down.  
> **Example**: $m = 2, n = 2 \implies 2$ paths; $m = 3, n = 3 \implies 6$ paths.

```java
public class ManeuveringCave {
    // 1. Recursive Method (Direct from Faculty PPT Slide 3)
    public static int numberOfPathsRecursive(int m, int n) {
        if (m == 1 || n == 1) {
            return 1;
        }
        return numberOfPathsRecursive(m - 1, n) + numberOfPathsRecursive(m, n - 1);
    }

    // 2. Dynamic Programming Method: O(m * n) Time, O(n) Space
    public static int numberOfPathsDP(int m, int n) {
        int[] dp = new int[n];
        java.util.Arrays.fill(dp, 1); // Base row: only 1 path (all Right)
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] = dp[j] + dp[j - 1]; // from top + from left
            }
        }
        return dp[n - 1];
    }

    // 3. Mathematical Formula (Combinatorics): O(min(m, n)) Time, O(1) Space
    // Formula: C(m + n - 2, m - 1)
    public static long numberOfPathsMath(int m, int n) {
        long totalPaths = 1;
        int N = m + n - 2;
        int R = Math.min(m - 1, n - 1);
        for (int i = 1; i <= R; i++) {
            totalPaths = totalPaths * (N - i + 1) / i;
        }
        return totalPaths;
    }

    public static void main(String[] args) {
        System.out.println("Paths for 3x3: " + numberOfPathsRecursive(3, 3)); // Output: 6
        System.out.println("Paths for 3x3 (Math): " + numberOfPathsMath(3, 3)); // Output: 6
    }
}
```

#### 1.1 High-Yield Maneuvering Variations for CAT-2

```java
import java.util.*;

public class ManeuveringVariationsMaster {

    // VARIATION A: Maneuvering with Obstacles / Blocked Cells (Unique Paths II)
    // Constraint: 1 represents an obstacle, 0 represents free passage.
    // Complexity: O(m * n) Time, O(n) Space (Optimized 1D DP)
    public static int numberOfPathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid == null || obstacleGrid.length == 0 || obstacleGrid[0][0] == 1) {
            return 0;
        }
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[] dp = new int[n];
        dp[0] = 1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (obstacleGrid[i][j] == 1) {
                    dp[j] = 0; // Impassable cell: zero incoming paths
                } else if (j > 0) {
                    dp[j] += dp[j - 1]; // Paths from top (dp[j]) + paths from left (dp[j-1])
                }
            }
        }
        return dp[n - 1];
    }

    // VARIATION B: Maneuvering with Diagonal Moves Allowed (Delannoy Numbers)
    // Allowed Moves: Down (+1, 0), Right (0, +1), Diagonal (+1, +1)
    // Recurrence: D(m, n) = D(m-1, n) + D(m, n-1) + D(m-1, n-1)
    // Complexity: O(m * n) Time, O(n) Space
    public static int numberOfPathsWithDiagonal(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        for (int i = 1; i < m; i++) {
            int prevDiagonal = 1; // Holds dp[i-1][j-1]
            for (int j = 1; j < n; j++) {
                int temp = dp[j];
                dp[j] = dp[j] + dp[j - 1] + prevDiagonal;
                prevDiagonal = temp; // Save for next column
            }
        }
        return dp[n - 1];
    }

    // VARIATION C: Path Reconstruction (Print All Direction Strings 'D' and 'R')
    // Complexity: O(C(m+n-2, m-1)) Time, O(m + n) Auxiliary Call Stack
    public static List<String> getAllManeuveringPaths(int m, int n) {
        List<String> result = new ArrayList<>();
        backtrackPaths(0, 0, m, n, new StringBuilder(), result);
        return result;
    }

    private static void backtrackPaths(int r, int c, int m, int n, StringBuilder path, List<String> result) {
        if (r == m - 1 && c == n - 1) {
            result.add(path.toString());
            return;
        }
        // Try Down move
        if (r + 1 < m) {
            path.append('D');
            backtrackPaths(r + 1, c, m, n, path, result);
            path.deleteCharAt(path.length() - 1); // Backtrack
        }
        // Try Right move
        if (c + 1 < n) {
            path.append('R');
            backtrackPaths(r, c + 1, m, n, path, result);
            path.deleteCharAt(path.length() - 1); // Backtrack
        }
    }

    // VARIATION D: Minimum Path Sum in Grid
    // Cost to move through grid[i][j]: find path minimizing total accumulated weight.
    // Recurrence: cost[i][j] = grid[i][j] + min(cost[i-1][j], cost[i][j-1])
    public static int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] dp = new int[n];

        dp[0] = grid[0][0];
        for (int j = 1; j < n; j++) dp[j] = dp[j - 1] + grid[0][j];

        for (int i = 1; i < m; i++) {
            dp[0] += grid[i][0];
            for (int j = 1; j < n; j++) {
                dp[j] = grid[i][j] + Math.min(dp[j], dp[j - 1]);
            }
        }
        return dp[n - 1];
    }
}
```

---

### 2. N-Queens Problem (`L36-N Queens.pptx` & Bitmask Optimization)
> **Problem**: Place $N$ non-attacking queens on an $N \times N$ chessboard.

```java
public class NQueensSolver {
    // Approach 1: Classic Backtracking (Direct from Faculty PPT)
    public static boolean solveNQ(int n) {
        int[][] board = new int[n][n];
        if (!solveNQUtil(board, 0, n)) {
            System.out.println("Solution does not exist");
            return false;
        }
        printSolution(board, n);
        return true;
    }

    private static boolean isSafe(int[][] board, int row, int col, int n) {
        // Check left side of current row
        for (int i = 0; i < col; i++) if (board[row][i] == 1) return false;
        // Check upper left diagonal (\)
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) if (board[i][j] == 1) return false;
        // Check lower left diagonal (/)
        for (int i = row, j = col; j >= 0 && i < n; i++, j--) if (board[i][j] == 1) return false;
        return true;
    }

    private static boolean solveNQUtil(int[][] board, int col, int n) {
        if (col >= n) return true; // All queens placed
        for (int i = 0; i < n; i++) {
            if (isSafe(board, i, col, n)) {
                board[i][col] = 1;
                if (solveNQUtil(board, col + 1, n)) return true;
                board[i][col] = 0; // Backtrack
            }
        }
        return false;
    }

    // Approach 2: Bitmask High-Speed Counter (O(N!) Time, O(N) Space)
    public static int totalNQueensBitmask(int n) {
        int fullMask = (1 << n) - 1;
        return countPlacements(0, 0, 0, fullMask);
    }

    private static int countPlacements(int cols, int d1, int d2, int fullMask) {
        if (cols == fullMask) return 1;
        int available = fullMask & ~(cols | d1 | d2);
        int total = 0;
        while (available != 0) {
            int p = available & -available; // Lowest set bit
            available &= available - 1;     // Clear bit
            total += countPlacements(cols | p, (d1 | p) >> 1, (d2 | p) << 1, fullMask);
        }
        return total;
    }

    private static void printSolution(int[][] board, int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) System.out.print(board[i][j] + " ");
            System.out.println();
        }
    }
}
```

#### 2.1 High-Yield N-Queens Variations for CAT-2

```java
import java.util.*;

public class NQueensVariationsMaster {

    // VARIATION A: N-Queens on Broken Board (Obstacles / Forbidden Cells - FacePrep IA Q2)
    // blockedMask[r] has bit c set if (r, c) is a broken/forbidden square.
    // Complexity: O(N * 2^N) with bitmask pruning
    public static int solveNQueensBrokenBoard(int n, int[] blockedMask) {
        int fullMask = (1 << n) - 1;
        return countBrokenPlacements(0, 0, 0, 0, n, fullMask, blockedMask);
    }

    private static int countBrokenPlacements(int row, int cols, int d1, int d2, int n, int fullMask, int[] blockedMask) {
        if (row == n) return 1;
        // Available positions: not attacked by cols/d1/d2 AND not on a broken square
        int available = fullMask & ~(cols | d1 | d2 | blockedMask[row]);
        int count = 0;
        while (available != 0) {
            int p = available & -available; // Lowest set bit
            available &= available - 1;
            count += countBrokenPlacements(row + 1, cols | p, (d1 | p) >> 1, (d2 | p) << 1, n, fullMask, blockedMask);
        }
        return count;
    }

    // VARIATION B: Super-Queens / Maharaja (Queen + Knight Combined Attack Vectors)
    // A piece attacks as BOTH a standard Queen (row, col, diagonals) AND a Knight (8 L-shapes).
    public static int countSuperQueens(int n) {
        int[] queenCols = new int[n]; // queenCols[r] = c
        return solveSuperQueens(0, n, queenCols);
    }

    private static int solveSuperQueens(int row, int n, int[] queenCols) {
        if (row == n) return 1;
        int count = 0;
        for (int col = 0; col < n; col++) {
            if (isSafeSuperQueen(row, col, queenCols)) {
                queenCols[row] = col;
                count += solveSuperQueens(row + 1, n, queenCols);
            }
        }
        return count;
    }

    private static boolean isSafeSuperQueen(int row, int col, int[] queenCols) {
        for (int r = 0; r < row; r++) {
            int c = queenCols[r];
            // 1. Standard Queen Attack Check (Column & Diagonals)
            if (c == col || Math.abs(r - row) == Math.abs(c - col)) return false;
            // 2. Knight Jump Attack Check: (|dr| == 1 && |dc| == 2) || (|dr| == 2 && |dc| == 1)
            int dr = Math.abs(r - row);
            int dc = Math.abs(c - col);
            if ((dr == 1 && dc == 2) || (dr == 2 && dc == 1)) return false;
        }
        return true;
    }

    // VARIATION C: Return All Board String Configurations (LeetCode 51 Format)
    public static List<List<String>> solveNQueensAllBoards(int n) {
        List<List<String>> solutions = new ArrayList<>();
        char[][] board = new char[n][n];
        for (char[] row : board) Arrays.fill(row, '.');
        dfsBoards(0, n, 0, 0, 0, board, solutions);
        return solutions;
    }

    private static void dfsBoards(int row, int n, int cols, int d1, int d2, char[][] board, List<List<String>> res) {
        if (row == n) {
            List<String> current = new ArrayList<>();
            for (char[] r : board) current.add(new String(r));
            res.add(current);
            return;
        }
        int fullMask = (1 << n) - 1;
        int available = fullMask & ~(cols | d1 | d2);
        while (available != 0) {
            int p = available & -available;
            int col = Integer.numberOfTrailingZeros(p);
            available &= available - 1;

            board[row][col] = 'Q';
            dfsBoards(row + 1, n, cols | p, (d1 | p) >> 1, (d2 | p) << 1, board, res);
            board[row][col] = '.'; // Backtrack
        }
    }

    // VARIATION D: Maximum Weighted N-Queens Placement
    // Given score matrix points[n][n], place N non-attacking queens to maximize total score.
    public static int maxWeightedNQueens(int[][] points, int n) {
        int[] maxScore = new int[]{Integer.MIN_VALUE};
        int[] queenCols = new int[n];
        findMaxWeighted(0, n, queenCols, 0, points, maxScore);
        return maxScore[0] == Integer.MIN_VALUE ? 0 : maxScore[0];
    }

    private static void findMaxWeighted(int row, int n, int[] queenCols, int currentScore, int[][] points, int[] maxScore) {
        if (row == n) {
            maxScore[0] = Math.max(maxScore[0], currentScore);
            return;
        }
        for (int col = 0; col < n; col++) {
            boolean safe = true;
            for (int r = 0; r < row; r++) {
                int c = queenCols[r];
                if (c == col || Math.abs(r - row) == Math.abs(c - col)) {
                    safe = false;
                    break;
                }
            }
            if (safe) {
                queenCols[row] = col;
                findMaxWeighted(row + 1, n, queenCols, currentScore + points[row][col], points, maxScore);
            }
        }
    }
}
```

---

### 3. Activity Selection Problem (`L38-Activity Selection.pptx`)
> **Problem**: Given start times `s[]` and finish times `f[]` of $n$ activities, find maximum non-overlapping activities.  
> **Faculty PPT Example 1**: `s = {2, 4, 3, 7}`, `f = {5, 6, 8, 9}` $\to$ Output: `0 1 3` (Activities at index 0, 1, and 3).  
> **Faculty PPT Example 2**: `s = {1, 3, 5, 6, 8}`, `f = {2, 4, 7, 9, 10}` $\to$ Output: `0 1 3 4`.

```java
import java.util.*;

public class ActivitySelectionMaster {
    static class ActivityItem {
        int id, start, finish;
        ActivityItem(int id, int start, int finish) {
            this.id = id;
            this.start = start;
            this.finish = finish;
        }
    }

    // Greedy Activity Selection: O(n log n) Time, O(n) Space
    public static List<Integer> selectMaxActivities(int[] s, int[] f) {
        int n = s.length;
        ActivityItem[] activities = new ActivityItem[n];
        for (int i = 0; i < n; i++) {
            activities[i] = new ActivityItem(i, s[i], f[i]);
        }

        // Step 1: Sort activities by finish time ascending
        Arrays.sort(activities, (a, b) -> Integer.compare(a.finish, b.finish));

        List<Integer> selected = new ArrayList<>();
        // Step 2: First activity always selected
        selected.add(activities[0].id);
        int lastFinishTime = activities[0].finish;

        // Step 3: Iterate through sorted activities
        for (int i = 1; i < n; i++) {
            if (activities[i].start >= lastFinishTime) {
                selected.add(activities[i].id);
                lastFinishTime = activities[i].finish;
            }
        }
        return selected;
    }

    public static void main(String[] args) {
        // Slide Example 1
        int[] s1 = {2, 4, 3, 7};
        int[] f1 = {5, 6, 8, 9};
        System.out.println("Selected Activities (Ex 1): " + selectMaxActivities(s1, f1)); // Output: [0, 1, 3]

        // Slide Example 2
        int[] s2 = {1, 3, 5, 6, 8};
        int[] f2 = {2, 4, 7, 9, 10};
        System.out.println("Selected Activities (Ex 2): " + selectMaxActivities(s2, f2)); // Output: [0, 1, 3, 4]
    }
}
```

---

### 4. Huffman Coding (`HuffmanCoding.pptx`)
> **Problem**: Build optimal variable-length prefix codes based on character frequencies.  
> **Worked Example from Slide 4**: `'ABRACADABRA'` ($A=5, B=2, R=2, C=1, D=1$).

```java
import java.util.*;

public class HuffmanCodingMaster {
    static class HuffmanNode implements Comparable<HuffmanNode> {
        char data;
        int freq;
        HuffmanNode left, right;

        HuffmanNode(char data, int freq) {
            this.data = data;
            this.freq = freq;
        }

        @Override
        public int compareTo(HuffmanNode o) {
            return Integer.compare(this.freq, o.freq);
        }
    }

    // Build Huffman Tree and generate binary codes
    public static Map<Character, String> buildHuffmanCodes(String text) {
        // 1. Calculate frequencies
        Map<Character, Integer> freqMap = new HashMap<>();
        for (char c : text.toCharArray()) freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);

        // 2. Insert into Min-Heap PriorityQueue
        PriorityQueue<HuffmanNode> pq = new PriorityQueue<>();
        for (var entry : freqMap.entrySet()) {
            pq.offer(new HuffmanNode(entry.getKey(), entry.getValue()));
        }

        // 3. Build tree by repeatedly combining 2 smallest nodes
        while (pq.size() > 1) {
            HuffmanNode left = pq.poll();
            HuffmanNode right = pq.poll();
            HuffmanNode parent = new HuffmanNode('-', left.freq + right.freq);
            parent.left = left;
            parent.right = right;
            pq.offer(parent);
        }

        HuffmanNode root = pq.peek();
        Map<Character, String> huffmanCodes = new HashMap<>();
        generateCodes(root, "", huffmanCodes);
        return huffmanCodes;
    }

    private static void generateCodes(HuffmanNode node, String code, Map<Character, String> map) {
        if (node == null) return;
        if (node.left == null && node.right == null) {
            map.put(node.data, code);
            return;
        }
        generateCodes(node.left, code + "0", map);
        generateCodes(node.right, code + "1", map);
    }

    public static void main(String[] args) {
        String text = "ABRACADABRA";
        Map<Character, String> codes = buildHuffmanCodes(text);
        System.out.println("Huffman Codes for ABRACADABRA:");
        codes.forEach((k, v) -> System.out.println(k + " : " + v));
    }
}
```

#### 4.1 High-Yield Huffman Variations for CAT-2

```java
import java.util.*;

public class HuffmanVariationsMaster {

    // VARIATION A: Huffman Decoding / Bitstream Decompression
    // Given the root of the Huffman Tree and a binary bitstream string (e.g., "110011110"),
    // reconstruct the original uncompressed message string.
    // Complexity: O(Bits) Time, O(1) Auxiliary Memory
    public static String decodeHuffmanStream(HuffmanCodingMaster.HuffmanNode root, String binaryStream) {
        if (root == null || binaryStream == null || binaryStream.length() == 0) return "";
        StringBuilder decoded = new StringBuilder();
        HuffmanCodingMaster.HuffmanNode curr = root;

        for (int i = 0; i < binaryStream.length(); i++) {
            char bit = binaryStream.charAt(i);
            curr = (bit == '0') ? curr.left : curr.right;

            // Check if current node is a leaf (contains original character)
            if (curr.left == null && curr.right == null) {
                decoded.append(curr.data);
                curr = root; // Reset traversal to root for next character
            }
        }
        return decoded.toString();
    }

    // VARIATION B: Minimum Cost to Connect Ropes / Merge Files (Greedy Internal Node Sum)
    // Connecting two ropes of length A and B costs (A + B).
    // Theorem: Minimum total cost equals the sum of all non-leaf (internal) nodes in Huffman tree!
    // Complexity: O(n log n) Time, O(n) Space
    public static long minCostToConnectRopes(int[] ropeLengths) {
        if (ropeLengths == null || ropeLengths.length <= 1) return 0;
        PriorityQueue<Long> pq = new PriorityQueue<>();
        for (int len : ropeLengths) pq.offer((long) len);

        long totalMergeCost = 0;
        while (pq.size() > 1) {
            long first = pq.poll();
            long second = pq.poll();
            long mergedCost = first + second;
            totalMergeCost += mergedCost;
            pq.offer(mergedCost); // Re-insert internal node
        }
        return totalMergeCost;
    }

    // VARIATION C: Ternary Huffman Coding (K = 3 Children per Internal Node)
    // Critical Exam Condition: A full K-ary tree requires (N - 1) % (K - 1) == 0.
    // If (N - 1) % (K - 1) != 0, we must append dummy symbols with frequency 0!
    public static long minCostTernaryHuffman(int[] frequencies) {
        int n = frequencies.length;
        int K = 3;
        PriorityQueue<Long> pq = new PriorityQueue<>();
        for (int f : frequencies) pq.offer((long) f);

        // Add dummy nodes with frequency 0 until (size - 1) % (K - 1) == 0
        while ((pq.size() - 1) % (K - 1) != 0) {
            pq.offer(0L);
        }

        long totalCost = 0;
        while (pq.size() > 1) {
            long groupSum = 0;
            for (int i = 0; i < K && !pq.isEmpty(); i++) {
                groupSum += pq.poll();
            }
            totalCost += groupSum;
            pq.offer(groupSum);
        }
        return totalCost;
    }
}
```

##### 📊 Master Huffman Compression & Bandwidth Formula Reference
* **Average Bit Length per Symbol**:
  $$L_{\text{avg}} = \frac{\sum_{i=1}^n f_i \cdot L_i}{\sum_{i=1}^n f_i} \quad \text{(bits/symbol)}$$
* **Standard Fixed-Length Encoding Comparison**:
  $$\text{Bits}_{\text{fixed}} = \lceil \log_2(\text{Unique Symbols}) \rceil$$
* **Exact Bandwidth Percentage Saved**:
  $$\text{Bandwidth Saved} = \frac{\text{Fixed Bits} - \text{Huffman Bits}}{\text{Fixed Bits}} \times 100\%$$
* **Theoretical Minimum Limit (Shannon Entropy)**:
  $$H(X) = -\sum_{i=1}^n P_i \log_2(P_i) \le L_{\text{avg}} < H(X) + 1$$

---

### 5. Sorted Unique Permutations (`L31-Sorted Unique Permutation.pptx`)
> **Problem**: Print all distinct permutations of a string in sorted order, where input may contain duplicate characters.  
> **Example**: `"AAB"` $\to$ `"AAB"`, `"ABA"`, `"BAA"`.

```java
import java.util.*;

public class SortedUniquePermutations {
    public static void distinctPermutations(String input) {
        char[] chars = input.toCharArray();
        Arrays.sort(chars); // Sort initially
        permute(chars, 0);
    }

    private static void permute(char[] chars, int index) {
        if (index == chars.length - 1) {
            System.out.println(String.valueOf(chars));
            return;
        }

        Set<Character> used = new HashSet<>(); // Avoid duplicate swaps at current level
        for (int i = index; i < chars.length; i++) {
            if (used.contains(chars[i])) continue;
            used.add(chars[i]);

            swap(chars, index, i);
            permute(chars, index + 1);
            swap(chars, index, i); // Backtrack
        }
    }

    private static void swap(char[] chars, int i, int j) {
        char temp = chars[i];
        chars[i] = chars[j];
        chars[j] = temp;
    }
}
```

---

### 6. Rat in a Maze (`L35-Maze Solving.pptx`)
> **Problem**: Find a path from $(0, 0)$ to $(N-1, N-1)$ in an $N \times N$ maze. $1 =$ open path, $0 =$ wall / dead end.

```java
public class RatInAMaze {
    public static boolean solveMaze(int[][] maze, int N) {
        int[][] sol = new int[N][N];
        if (!solveMazeUtil(maze, 0, 0, sol, N)) {
            System.out.println("No Path Exists");
            return false;
        }
        printSolution(sol, N);
        return true;
    }

    private static boolean solveMazeUtil(int[][] maze, int x, int y, int[][] sol, int N) {
        if (x == N - 1 && y == N - 1 && maze[x][y] == 1) {
            sol[x][y] = 1;
            return true;
        }

        if (x >= 0 && x < N && y >= 0 && y < N && maze[x][y] == 1) {
            if (sol[x][y] == 1) return false; // Already visited

            sol[x][y] = 1;
            // Try moving Down
            if (solveMazeUtil(maze, x + 1, y, sol, N)) return true;
            // Try moving Right
            if (solveMazeUtil(maze, x, y + 1, sol, N)) return true;

            sol[x][y] = 0; // Backtrack
            return false;
        }
        return false;
    }

    private static void printSolution(int[][] sol, int N) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) System.out.print(sol[i][j] + " ");
            System.out.println();
        }
    }
}
```

---

### 7. Warnsdorff’s Algorithm for Knight's Tour (`L37-Warnsdorff’s Algorithm.pptx`)
> **Problem**: Visit every square of an $N \times N$ chessboard exactly once with a knight.  
> **Warnsdorff’s Heuristic**: Always move the knight to an adjacent unvisited cell that has the **minimum degree** (minimum number of onward unvisited moves).

```java
public class WarnsdorffKnightTour {
    public static final int N = 8;
    // 8 possible L-shaped moves of a knight
    public static final int[] cx = {1, 1, 2, 2, -1, -1, -2, -2};
    public static final int[] cy = {2, -2, 1, -1, 2, -2, 1, -1};

    static boolean isSafe(int x, int y, int[] board) {
        return (x >= 0 && y >= 0 && x < N && y < N && board[y * N + x] < 0);
    }

    // Count available unvisited neighbors (degree)
    static int getDegree(int[] board, int x, int y) {
        int count = 0;
        for (int i = 0; i < 8; i++) {
            if (isSafe(x + cx[i], y + cy[i], board)) count++;
        }
        return count;
    }

    public static boolean knightTour() {
        int[] board = new int[N * N];
        java.util.Arrays.fill(board, -1);

        int sx = 0, sy = 0; // Start at (0, 0)
        board[sy * N + sx] = 1;

        for (int step = 2; step <= N * N; step++) {
            int minDeg = 9, minIdx = -1;
            int nx = -1, ny = -1;

            for (int i = 0; i < 8; i++) {
                int tx = sx + cx[i];
                int ty = sy + cy[i];
                if (isSafe(tx, ty, board)) {
                    int deg = getDegree(board, tx, ty);
                    if (deg < minDeg) {
                        minDeg = deg;
                        minIdx = i;
                        nx = tx;
                        ny = ty;
                    }
                }
            }

            if (minIdx == -1) return false; // Dead end
            board[ny * N + nx] = step;
            sx = nx;
            sy = ny;
        }
        return true;
    }
}
```
