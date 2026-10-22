# 📘 Unit 5: Dynamic Programming, Trees & Graph Algorithms

> **Aligned with VIT Bhopal October 2026 TEE Papers**: Slots A11, B14, F11, E11  
> **Unit Weight in TEE**: Exactly 20 Marks (12M in Section A + 8M in Section B)

---

## 1. Dynamic Programming Paradigms

### 1.1 Maneuvering Problem (Grid Unique Paths with DP)
*(Paper 2 Q5a & Paper 3 Q5a — 12 Marks)*

Count total number of unique paths from top-left $(0, 0)$ to bottom-right $(M-1, N-1)$ of an $M \times N$ grid moving only Right or Down.

#### Recurrence Relation & Base Cases:
$$dp[i][j] = dp[i-1][j] + dp[i][j-1]$$
- Base Cases: $dp[0][j] = 1$ for all $0 \le j < N$; $dp[i][0] = 1$ for all $0 \le i < M$.
- Combinatorial Solution: Total moves $= (M - 1) + (N - 1)$. We must choose $(M - 1)$ down moves:
  $$\text{Paths} = \binom{(M-1) + (N-1)}{M-1} = \frac{(M + N - 2)!}{(M - 1)! \, (N - 1)!}$$

```java
public class GridPathsDP {
    public static int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        java.util.Arrays.fill(dp, 1); // Row 0 base case

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] = dp[j] + dp[j - 1]; // dp[j] from top cell, dp[j-1] from left cell
            }
        }
        return dp[n - 1];
    }

    public static void main(String[] args) {
        int m = 3, n = 3;
        System.out.println("Unique paths in 3x3 grid: " + uniquePaths(m, n)); // 6
    }
}
```
* **Trace for $3 \times 3$ Grid**:
  - Row 0: $[1, 1, 1]$
  - Row 1: $[1, 1+1=2, 2+1=3]$
  - Row 2: $[1, 1+2=3, 3+3=\mathbf{6}]$
  - Total Unique Paths $= \mathbf{6}$. Combinatorics: $\binom{4}{2} = 6$. Time: $O(M \cdot N)$, Auxiliary Space: $O(N)$.

---

### 1.2 0/1 Knapsack Problem (1D Space Optimized)
* Recurrence: $dp[w] = \max(dp[w], val[i] + dp[w - wt[i]])$ traversing backwards from $W$ down to $wt[i]$. Time: $O(N \cdot W)$, Space: $O(W)$.

### 1.3 Longest Common Subsequence (LCS)
* Recurrence: $dp[i][j] = 1 + dp[i-1][j-1]$ on character match; $\max(dp[i-1][j], dp[i][j-1])$ otherwise.

---

## 2. Binary Tree Algorithms & Traversals

### 2.1 Height & Diameter of Binary Tree
*(Paper 2 Q2a & Paper 3 Q2a — 12 Marks)*

* **Height**: Length of longest path from root to deepest leaf node.
* **Diameter**: Length of longest path between *any two nodes* in a tree.

```java
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { this.val = v; }
}

public class TreeMetrics {
    static int maxDiameter = 0;

    public static int height(TreeNode root) {
        if (root == null) return 0;
        int leftH = height(root.left);
        int rightH = height(root.right);
        maxDiameter = Math.max(maxDiameter, leftH + rightH); // Diameter at this node
        return 1 + Math.max(leftH, rightH);
    }

    public static int getDiameter(TreeNode root) {
        maxDiameter = 0;
        height(root);
        return maxDiameter;
    }
}
```

---

### 2.2 Check if Two Binary Trees are Identical
*(Paper 1 Q5c — 6 Marks)*

```java
public class IdenticalTrees {
    public static boolean isIdentical(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) return true;
        if (t1 == null || t2 == null) return false;
        return (t1.val == t2.val) &&
               isIdentical(t1.left, t2.left) &&
               isIdentical(t1.right, t2.right);
    }

    public static void main(String[] args) {
        // T1 = 1(2, 3), T2 = 1(2, 3)
        TreeNode t1 = new TreeNode(1); t1.left = new TreeNode(2); t1.right = new TreeNode(3);
        TreeNode t2 = new TreeNode(1); t2.left = new TreeNode(2); t2.right = new TreeNode(3);
        // T3 = 1(3, 2)
        TreeNode t3 = new TreeNode(1); t3.left = new TreeNode(3); t3.right = new TreeNode(2);

        System.out.println("T1 and T2 identical? " + isIdentical(t1, t2)); // true
        System.out.println("T1 and T3 identical? " + isIdentical(t1, t3)); // false
    }
}
```
* **Complexity**: Time: $O(\min(N_1, N_2))$, Space: $O(H)$.

---

### 2.3 Level-Order Traversal (BFS Queue) Printing Each Level on New Line
*(Paper 1 Q5b & Paper 4 Q10 — 6 to 8 Marks)*

```java
import java.util.*;

public class LevelOrderLineByLine {
    public static void printLevelOrder(TreeNode root) {
        if (root == null) return;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);

        while (!q.isEmpty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode curr = q.poll();
                System.out.print(curr.val + " ");
                if (curr.left != null) q.offer(curr.left);
                if (curr.right != null) q.offer(curr.right);
            }
            System.out.println(); // New line after each level
        }
    }

    public static void main(String[] args) {
        // Tree: 3(9, 20(15, 7))
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        System.out.println("Level Order Traversal:");
        printLevelOrder(root);
    }
}
```
**Queue Contents Trace Output**:
```text
Level Order Traversal:
3 
9 20 
15 7 
```

---

## 3. Graph Algorithms

### 3.1 Connected Components in Undirected Graph: BFS vs Recursive DFS
*(Paper 1 Q5a — 12 Marks)*

#### BFS vs Recursive DFS Evaluation for $10^5$ Vertices:
* **Recursive DFS Vulnerability**: In the worst-case (a degenerate "skewed" graph structured as a straight chain $0\text{--}1\text{--}2\dots\text{--}10^5$), recursive DFS reaches a call stack depth of $10^5$. In standard JVM environments, call stack memory is limited ($\approx 1\text{ MB}$), causing an immediate, fatal `java.lang.StackOverflowError`.
* **BFS Superiority (RECOMMENDED)**: BFS allocates its `Queue` on the JVM **heap memory** (typically hundreds of megabytes or gigabytes). It easily processes $10^5$ or even $10^7$ vertices without call stack overflow risks.

```java
import java.util.*;

public class ConnectedComponents {
    public static int countComponents(int V, List<List<Integer>> adj) {
        boolean[] visited = new boolean[V];
        int components = 0;

        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                components++;
                // BFS Traversal using heap-allocated queue
                Queue<Integer> q = new LinkedList<>();
                visited[i] = true;
                q.offer(i);
                while (!q.isEmpty()) {
                    int curr = q.poll();
                    for (int neighbor : adj.get(curr)) {
                        if (!visited[neighbor]) {
                            visited[neighbor] = true;
                            q.offer(neighbor);
                        }
                    }
                }
            }
        }
        return components;
    }

    public static void main(String[] args) {
        int V = 7;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        // Edges: 0--1, 1--2, 3--4, 5--6
        adj.get(0).add(1); adj.get(1).add(0);
        adj.get(1).add(2); adj.get(2).add(1);
        adj.get(3).add(4); adj.get(4).add(3);
        adj.get(5).add(6); adj.get(6).add(5);

        int count = countComponents(V, adj);
        System.out.println("Is connected? " + (count == 1));
        System.out.println("Number of connected components: " + count);
    }
}
```
**Sample Output for Edges $\{0\text{--}1, 1\text{--}2, 3\text{--}4, 5\text{--}6\}$**:
```text
Is connected? false
Number of connected components: 3
```
*(Component 1: $\{0, 1, 2\}$, Component 2: $\{3, 4\}$, Component 3: $\{5, 6\}$).*

---

### 3.2 Unweighted Graph Shortest Path via BFS
*(Paper 1 Q10 — 8 Marks)*

Find and display the shortest path from vertex $0$ to vertex $4$ for edges: $0\text{--}1, 0\text{--}2, 1\text{--}3, 2\text{--}3, 3\text{--}4, 2\text{--}5$.

```java
import java.util.*;

public class BFSShortestPath {
    public static List<Integer> findShortestPath(int V, List<List<Integer>> adj, int src, int dest) {
        boolean[] visited = new boolean[V];
        int[] parent = new int[V];
        Arrays.fill(parent, -1);
        Queue<Integer> q = new LinkedList<>();

        visited[src] = true;
        q.offer(src);

        while (!q.isEmpty()) {
            int curr = q.poll();
            if (curr == dest) break;

            for (int neighbor : adj.get(curr)) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    parent[neighbor] = curr;
                    q.offer(neighbor);
                }
            }
        }

        List<Integer> path = new ArrayList<>();
        for (int at = dest; at != -1; at = parent[at]) path.add(at);
        Collections.reverse(path);
        return path;
    }

    public static void main(String[] args) {
        int V = 6;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        adj.get(0).addAll(Arrays.asList(1, 2));
        adj.get(1).addAll(Arrays.asList(0, 3));
        adj.get(2).addAll(Arrays.asList(0, 3, 5));
        adj.get(3).addAll(Arrays.asList(1, 2, 4));
        adj.get(4).add(3);
        adj.get(5).add(2);

        System.out.println("Shortest Path from 0 to 4: " + findShortestPath(V, adj, 0, 4));
    }
}
```
* **Step-by-Step Parent Trace**:
  - $0$ enqueues $1, 2$ (`parent[1]=0, parent[2]=0`).
  - $1$ enqueues $3$ (`parent[3]=1`).
  - $2$ enqueues $5$ (`parent[5]=2`).
  - $3$ enqueues $4$ (`parent[4]=3`). Destination reached!
  - Backtracking: $4 \leftarrow 3 \leftarrow 1 \leftarrow 0$.
* **Shortest Path**: **`[0, 1, 3, 4]`** (Length $= 3$ edges).
* **Why BFS Guarantees Shortest Path**: In unweighted graphs, BFS visits all vertices at distance $d$ before any vertex at distance $d + 1$. Thus, the first time the destination node is dequeued, it is guaranteed to have been reached along a path of minimum edge length.

---

### 3.3 Kruskal's Algorithm for Minimum Spanning Tree (MST)
*(Paper 4 Q5a — 12 Marks)*

Uses **Disjoint Set Union (DSU)** with path compression and rank to greedily pick the smallest non-cycle edges:
* Time Complexity: $O(E \log E)$, Auxiliary Space: $O(V)$.

---

### 3.4 Number of Islands (Grid Connected Components via DFS/BFS)
*(Paper 5 Q10 — 8 Marks)*

Given a 2D binary matrix where `1` represents land and `0` represents water, count the number of islands.

```java
public class NumberOfIslands {
    public static int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        int count = 0;
        int R = grid.length, C = grid[0].length;

        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (grid[r][c] == '1') {
                    count++;
                    dfsSink(grid, r, c); // Sink the entire island
                }
            }
        }
        return count;
    }

    private static void dfsSink(char[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] != '1') return;
        grid[r][c] = '0'; // Mark visited
        dfsSink(grid, r + 1, c);
        dfsSink(grid, r - 1, c);
        dfsSink(grid, r, c + 1);
        dfsSink(grid, r, c - 1);
    }

    public static void main(String[] args) {
        char[][] grid = {
            {'1', '1', '0', '0', '0'},
            {'0', '1', '0', '0', '1'},
            {'1', '0', '0', '1', '1'},
            {'0', '0', '0', '0', '0'}
        };
        System.out.println("Total Islands: " + numIslands(grid)); // 2
    }
}
```
* **Complexity**: Time: $O(R \cdot C)$, Auxiliary Space: $O(R \cdot C)$ due to recursion stack.

---

## 4. Tree Validation & Optimization Analysis

### 4.1 Validate Binary Search Tree: Min-Max Range Approach
*(Paper 5 Q5c — 6 Marks)*

Tree: Root $10$, left child $5$ (having children $2$ and $12$), right child $15$.

* **Why Comparing Each Node Only with its Parent Fails**:
  - $2 < 5$ is locally valid.
  - $12 > 5$ is locally valid.
  - $5 < 10$ and $15 > 10$ are locally valid.
  - **However, node 12 lies in the left subtree of node 10**, meaning **every node in that entire subtree must be strictly $< 10$**. Since $12 > 10$, the BST property is violated!
  - Local parent checks fail to catch global ancestor bounds.
* **Algorithm**: Pass allowable range `(min, max)` down during traversal:
```java
public static boolean isValidBST(TreeNode root, long min, long max) {
    if (root == null) return true;
    if (root.val <= min || root.val >= max) return false;
    return isValidBST(root.left, min, root.val) && isValidBST(root.right, root.val, max);
}
```

---

### 4.2 Diameter of Binary Tree: Naive $O(N^2)$ vs Single-Traversal $O(N)$
*(Paper 5 Q5a — 12 Marks)*

* **Naive Approach ($O(N^2)$ Time)**:
  - For each node, separately call `height(node.left)` and `height(node.right)` ($O(N)$ work per node).
  - Across all $N$ nodes, total runtime is $O(N^2)$.
* **Optimised Approach ($O(N)$ Time — RECOMMENDED)**:
  - In a single bottom-up post-order DFS traversal, compute height of each subtree while simultaneously updating a global `maxDiameter = Math.max(maxDiameter, leftH + rightH)`.
  - Every node is visited exactly once $\implies \mathbf{O(N)\text{ Linear Time}}$, Space: $O(H)$.
