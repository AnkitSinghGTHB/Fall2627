# 📘 Unit 5: Trees, Graphs & Dynamic Programming

> **Aligned with VIT Bhopal PLA1004 Syllabus & TEE Papers (Slots A11, B14, F11, E11, A21)**  
> **Exam Paper Mapping**:
> - **PART A**: **Question 5** (12 Marks — with internal choice `OR`)
> - **PART B**: **Question 10** (8 Marks — direct implementation)  
> **Total Unit Weight in TEE**: **Exactly 20 Marks**

---

# PART 1: SECTION A QUESTIONS (12 MARKS) [Question 5 Pool]

---

## 1. Connected Components in Undirected Graph: BFS vs Recursive DFS
*(Paper 1 Q5a — 12 Marks)*

### Problem Statement:
Check whether an undirected graph represented by an adjacency list is connected, and if not, display the number of connected components. Trace your solution for the 7-vertex graph with edges $0\text{--}1, 1\text{--}2, 3\text{--}4, 5\text{--}6$. Evaluate BFS against recursive DFS for a graph with $10^5$ vertices and justify your choice.

### Algorithmic Logic:
1. Maintain a boolean array `visited[]` of size $V$, initially all `false`.
2. Iterate through all vertices $0$ to $V - 1$.
3. If vertex $i$ is not visited, it is the start of a new connected component (`components++`).
4. Perform BFS from vertex $i$ using a queue to visit and mark all vertices reachable in that component.
5. If `components == 1`, the graph is fully connected; otherwise, it is disconnected.

```java
import java.util.*;

public class ConnectedComponentsSolver {
    public static int countComponents(int V, List<List<Integer>> adj) {
        boolean[] visited = new boolean[V];
        int components = 0;

        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                components++;
                // Breadth-First Search (Queue allocated on JVM heap)
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
        System.out.println("Graph has " + V + " vertices.");
        System.out.println("Is connected? " + (count == 1));
        System.out.println("Number of connected components: " + count);
    }
}
```

#### Step-by-Step Execution Trace for 7-vertex Graph:
- Vertices $\{0, 1, 2, 3, 4, 5, 6\}$. Edges: $0\text{--}1, 1\text{--}2, 3\text{--}4, 5\text{--}6$.
1. $i = 0$: `visited[0] = false` $\implies$ `components = 1`. BFS explores $0 \to 1 \to 2$. Marks $\{0, 1, 2\}$ as visited.
2. $i = 1, 2$: Already visited.
3. $i = 3$: `visited[3] = false` $\implies$ `components = 2`. BFS explores $3 \to 4$. Marks $\{3, 4\}$ as visited.
4. $i = 4$: Already visited.
5. $i = 5$: `visited[5] = false` $\implies$ `components = 3`. BFS explores $5 \to 6$. Marks $\{5, 6\}$ as visited.
6. $i = 6$: Already visited.
* **Result**: **Disconnected**, with **3 Connected Components**: Component 1: $\{0, 1, 2\}$, Component 2: $\{3, 4\}$, Component 3: $\{5, 6\}$.

#### Evaluation: BFS vs Recursive DFS for $10^5$ Vertices:
* **Recursive DFS Vulnerability**: In the worst-case (a long linear chain graph $0\text{--}1\text{--}2\dots\text{--}10^5$), recursive DFS reaches a call stack depth of $10^5$. In Java, standard thread call stack size is limited ($\approx 1\text{ MB}$), causing a fatal `java.lang.StackOverflowError`.
* **BFS Superiority (Recommended)**: BFS allocates its `Queue` directly in the JVM **heap memory**, which can easily scale to millions of vertices without crashing the call stack.

---

## 2. Binary Tree Level Order Traversal Using Queue (BFS)
*(Paper 1 Q5b — 6 Marks)*

### Problem Statement:
Perform the Level Order Traversal of a binary tree using a queue, printing each level on a new line. Trace the queue contents for root $3$, left child $9$, right child $20$ (children $15$ and $7$).

```java
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { this.val = v; }
}

public class LevelOrderLineByLine {
    public static void printLevelOrder(TreeNode root) {
        if (root == null) return;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode curr = queue.poll();
                System.out.print(curr.val + " ");
                if (curr.left != null) queue.offer(curr.left);
                if (curr.right != null) queue.offer(curr.right);
            }
            System.out.println(); // New line after each level completes
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

#### Step-by-Step Queue State Trace:
| Level | Queue at Start of Level | Nodes Polled | Children Enqueued | Level Output |
|:---:|:---|:---|:---|:---|
| **Level 0** | `[3]` | Node 3 | `9, 20` | `3` |
| **Level 1** | `[9, 20]` | Node 9, Node 20 | Node 9: none; Node 20: `15, 7` | `9 20` |
| **Level 2** | `[15, 7]` | Node 15, Node 7 | None | `15 7` |

* **Complexities**: Time: $O(N)$ (every node visited once), Auxiliary Space: $O(W)$ where $W$ is maximum width of the tree ($\le N/2$).

---

## 3. Check If Two Binary Trees are Identical
*(Paper 1 Q5c — 6 Marks)*

### Problem Statement:
Check whether two binary trees are identical (same structure and same node values). Analyse on $T_1 = 1(2, 3), T_2 = 1(2, 3)$ and $T_1 = 1(2, 3), T_3 = 1(3, 2)$.

```java
public class IdenticalTreesCheck {
    public static boolean isIdentical(TreeNode t1, TreeNode t2) {
        // Both null -> Identical
        if (t1 == null && t2 == null) return true;
        // One null and one not null -> Not identical
        if (t1 == null || t2 == null) return false;

        // Check current node value and recurse on left and right subtrees
        return (t1.val == t2.val) &&
               isIdentical(t1.left, t2.left) &&
               isIdentical(t1.right, t2.right);
    }

    public static void main(String[] args) {
        // T1 = 1(2, 3)
        TreeNode t1 = new TreeNode(1); t1.left = new TreeNode(2); t1.right = new TreeNode(3);
        // T2 = 1(2, 3)
        TreeNode t2 = new TreeNode(1); t2.left = new TreeNode(2); t2.right = new TreeNode(3);
        // T3 = 1(3, 2)
        TreeNode t3 = new TreeNode(1); t3.left = new TreeNode(3); t3.right = new TreeNode(2);

        System.out.println("T1 and T2 are identical? " + isIdentical(t1, t2)); // true
        System.out.println("T1 and T3 are identical? " + isIdentical(t1, t3)); // false
    }
}
```

#### Analytical Working:
1. **Comparing $T_1$ and $T_2$**:
   - Roots match: `1 == 1`.
   - Left subtrees match: `isIdentical(t1.left, t2.left)` checks `2 == 2`, both leaves match $\implies$ `true`.
   - Right subtrees match: `isIdentical(t1.right, t2.right)` checks `3 == 3`, both leaves match $\implies$ `true`.
   - Output: **`true`**.
2. **Comparing $T_1$ and $T_3$**:
   - Roots match: `1 == 1`.
   - Left subtrees: `t1.left.val = 2`, but `t3.left.val = 3`. Mismatch `2 != 3` $\implies$ immediately returns **`false`**.
* **Complexities**: Time: $O(\min(N_1, N_2))$, Space: $O(\min(H_1, H_2))$ recursion stack.

---

## 4. Binary Tree Height & Diameter: Naive $O(N^2)$ vs Single-Traversal $O(N)$
*(Paper 2 Q2a, Paper 3 Q2a, Paper 5 Q5a — 12 Marks)*

### Problem Statement:
The diameter of a binary tree is the number of nodes on the longest path between any two nodes. Implement both the naive approach and the optimized single-traversal approach, evaluate their time complexities, and recommend one with justification.

```java
public class BinaryTreeDiameter {
    // 1. Helper function for height
    public static int height(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(height(root.left), height(root.right));
    }

    // Naive O(N^2) Diameter Approach: Computes height separately at every node
    public static int diameterNaive(TreeNode root) {
        if (root == null) return 0;
        int leftH = height(root.left);
        int rightH = height(root.right);
        int diameterThroughRoot = leftH + rightH + 1; // nodes on path

        int leftD = diameterNaive(root.left);
        int rightD = diameterNaive(root.right);

        return Math.max(diameterThroughRoot, Math.max(leftD, rightD));
    }

    // 2. Optimized O(N) Single-Traversal Approach (RECOMMENDED)
    static int maxDiameterNodes = 0;

    public static int calculateHeightAndUpdateDiameter(TreeNode root) {
        if (root == null) return 0;

        int leftH = calculateHeightAndUpdateDiameter(root.left);
        int rightH = calculateHeightAndUpdateDiameter(root.right);

        // Update global diameter (number of nodes on longest path = leftH + rightH + 1)
        maxDiameterNodes = Math.max(maxDiameterNodes, leftH + rightH + 1);

        return 1 + Math.max(leftH, rightH);
    }

    public static int diameterOptimized(TreeNode root) {
        maxDiameterNodes = 0;
        calculateHeightAndUpdateDiameter(root);
        return maxDiameterNodes;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        System.out.println("Tree Height:             " + height(root)); // 3
        System.out.println("Diameter (Naive O(N^2)): " + diameterNaive(root)); // 4 nodes (4-2-1-3 or 5-2-1-3)
        System.out.println("Diameter (Optimized O(N)): " + diameterOptimized(root)); // 4 nodes
    }
}
```

#### Evaluation & Recommendation:
* **Naive Approach ($O(N^2)$)**: At each node, computing height traverses all descendants. For a skewed tree of $N$ nodes, height calls take $\sum_{i=1}^N i = O(N^2)$ operations.
* **Optimized Approach ($O(N)$ — RECOMMENDED)**: Using a bottom-up post-order traversal, each node calculates its height from its children's returned heights in $O(1)$ and simultaneously updates the diameter. Every node is visited exactly once $\implies \mathbf{O(N)\text{ time}}$, Auxiliary Space: $O(H)$.

---

## 5. Maneuvering Problem (Grid Unique Paths with DP)
*(Paper 2 Q5a, Paper 3 Q5a — 12 Marks)*

### Problem Statement:
Count all unique paths from the top-left cell `(0, 0)` to the bottom-right cell `(M-1, N-1)` of an $M \times N$ matrix moving only Right or Down, using dynamic programming with memoization.

### Recurrence & Closed Form:
* Recurrence: $dp[i][j] = dp[i-1][j] + dp[i][j-1]$.
* Base Cases: $dp[0][j] = 1$ and $dp[i][0] = 1$.
* Combinatorial Formula: $\binom{(M-1) + (N-1)}{M-1} = \frac{(M+N-2)!}{(M-1)! \, (N-1)!}$.

```java
public class ManeuveringDP {
    public static int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];

        // Base cases: 1 path along the first row and first column
        for (int i = 0; i < m; i++) dp[i][0] = 1;
        for (int j = 0; j < n; j++) dp[0][j] = 1;

        // Fill DP table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[m - 1][n - 1];
    }

    public static void main(String[] args) {
        int m = 3, n = 3;
        System.out.println("Unique paths in 3x3 grid: " + uniquePaths(m, n)); // 6
    }
}
```

#### Trace for $3 \times 3$ Grid:
```text
Row 0: [1, 1, 1]
Row 1: [1, 2, 3]  (dp[1][1]=1+1=2, dp[1][2]=2+1=3)
Row 2: [1, 3, 6]  (dp[2][1]=1+2=3, dp[2][2]=3+3=6)
```
* **Output**: **$6$ Unique Paths**. Combinatorially: $\binom{4}{2} = \frac{4 \times 3}{2} = 6$. Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.

---

## 6. Balanced Parentheses Using Stack
*(Paper 2 Q5b, Paper 3 Q5b — 6 Marks)*

### Problem Statement:
Check whether an expression contains balanced parentheses considering `()`, `{}`, and `[]`.

```java
import java.util.Stack;

public class BalancedParentheses {
    public static boolean isBalanced(String s) {
        Stack<Character> stack = new Stack<>();

        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            } else if (ch == ')' || ch == '}' || ch == ']') {
                if (stack.isEmpty()) return false;
                char top = stack.pop();
                if ((ch == ')' && top != '(') ||
                    (ch == '}' && top != '{') ||
                    (ch == ']' && top != '[')) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        System.out.println("\"({[]})\" is balanced? " + isBalanced("({[]})")); // true
        System.out.println("\"([)]\"   is balanced? " + isBalanced("([)]"));   // false
        System.out.println("\"(()\"    is balanced? " + isBalanced("(()"));    // false
    }
}
```

* **Complexities**: Time: $O(N)$, Auxiliary Space: $O(N)$.

---

## 7. 2D Matrix Hourglass Maximum Sum Code Complexity Analysis
*(Paper 2 Q5c, Paper 3 Q5c — 6 Marks)*

### Given Code Snippet:
```java
int maxSum = Integer.MIN_VALUE;
for (int i = 0; i < n - 2; i++) {
    for (int j = 0; j < m - 2; j++) {
        int sum = mat[i][j] + mat[i][j+1] + mat[i][j+2]
                            + mat[i+1][j+1]
                + mat[i+2][j] + mat[i+2][j+1] + mat[i+2][j+2];
        if (sum > maxSum) maxSum = sum;
    }
}
```

#### Detailed Complexity & Execution Analysis:
1. **Outer Loop**: Runs from $i = 0$ to $n - 3 \implies (n - 2)$ iterations.
2. **Inner Loop**: Runs from $j = 0$ to $m - 3 \implies (m - 2)$ iterations.
3. **Inner Work**: Inside the nested loops, exactly 7 additions and 1 comparison are performed $\implies O(1)$ constant work per hourglass.
4. **Total Operations**:
   $$\text{Total Additions} = 7 \cdot (n - 2)(m - 2) = \mathbf{O(n \cdot m)}$$
* **Time Complexity**: **$\mathbf{O(n \cdot m)}$** (Linear in total matrix elements).
* **Space Complexity**: **$\mathbf{O(1)}$** (Uses only scalar variables `maxSum`, `sum`, `i`, `j`).
* **Trace on $3 \times 3$ Matrix**:
  - $n = 3, m = 3 \implies (3 - 2) \times (3 - 2) = 1 \times 1 = \mathbf{1\text{ hourglass}}$.
  - The loop executes exactly once for $(i=0, j=0)$ summing all 7 values of the unique hourglass.

---

## 8. Kruskal's Algorithm for Minimum Spanning Tree (MST) Using Union-Find
*(Paper 4 Q5a — 12 Marks)*

### Problem Statement:
Explain Kruskal's algorithm for finding the Minimum Spanning Tree of a graph and implement it using the Disjoint Set Union (DSU / Union-Find) data structure with path compression and union by rank.

```java
import java.util.*;

class Edge implements Comparable<Edge> {
    int src, dest, weight;
    Edge(int s, int d, int w) { this.src = s; this.dest = d; this.weight = w; }
    public int compareTo(Edge other) { return this.weight - other.weight; }
}

public class KruskalMST {
    static class DSU {
        int[] parent, rank;
        DSU(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }

        int find(int i) {
            if (parent[i] == i) return i;
            return parent[i] = find(parent[i]); // Path compression
        }

        boolean union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX == rootY) return false; // Cycle detected

            // Union by rank
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
            return true;
        }
    }

    public static void kruskalMST(int V, List<Edge> edges) {
        Collections.sort(edges); // Sort edges by weight ascending
        DSU dsu = new DSU(V);

        List<Edge> mst = new ArrayList<>();
        int mstWeight = 0;

        for (Edge edge : edges) {
            if (dsu.union(edge.src, edge.dest)) {
                mst.add(edge);
                mstWeight += edge.weight;
                if (mst.size() == V - 1) break; // MST complete
            }
        }

        System.out.println("Edges in Minimum Spanning Tree (MST):");
        for (Edge e : mst) {
            System.out.println(e.src + " -- " + e.dest + " == " + e.weight);
        }
        System.out.println("Total MST Weight: " + mstWeight);
    }

    public static void main(String[] args) {
        int V = 4;
        List<Edge> edges = new ArrayList<>();
        edges.add(new Edge(0, 1, 10));
        edges.add(new Edge(0, 2, 6));
        edges.add(new Edge(0, 3, 5));
        edges.add(new Edge(1, 3, 15));
        edges.add(new Edge(2, 3, 4));

        kruskalMST(V, edges);
    }
}
```

#### Step-by-Step Edge Selection Trace (Assignment Q10.4):
Given graph with vertices $\{A, B, C, D, E\}$ ($V = 5$, requires $V - 1 = 4$ edges):
Edges: $(A-B, 4), (A-C, 2), (B-C, 1), (B-D, 5), (C-D, 8), (C-E, 10), (D-E, 2)$.

| Step | Edge Picked | Weight | Sets / Cycle Check | Action | Disjoint Sets After Step |
|:---:|:---:|:---:|:---|:---:|:---|
| 1 | **(B, C)** | **1** | $B$ and $C$ belong to different sets | **ACCEPTED** | $\{A\}, \{B, C\}, \{D\}, \{E\}$ |
| 2 | **(A, C)** | **2** | $A$ and $C$ belong to different sets | **ACCEPTED** | $\{A, B, C\}, \{D\}, \{E\}$ |
| 3 | **(D, E)** | **2** | $D$ and $E$ belong to different sets | **ACCEPTED** | $\{A, B, C\}, \{D, E\}$ |
| 4 | **(A, B)** | **4** | Both $A$ and $B$ are already in $\{A, B, C\}$ (Forms cycle $A-C-B-A$) | **REJECTED** | $\{A, B, C\}, \{D, E\}$ |
| 5 | **(B, D)** | **5** | $B \in \{A, B, C\}$ and $D \in \{D, E\}$ | **ACCEPTED** | $\{A, B, C, D, E\}$ (All connected) |

* **Total MST Weight**: $1 + 2 + 2 + 5 = \mathbf{10}$.
* Total edges accepted: $4 = V - 1$. Algorithm terminates successfully.
* **Complexities**: Time: $O(E \log E)$ for sorting $+ O(E \cdot \alpha(V))$ for DSU operations $\implies \mathbf{O(E \log E)}$, Space: $O(V + E)$.

---

## 9. Hamiltonian Cycle Backtracking on Graph
*(Paper 4 Q5b, Q5c — 12 Marks)*

### Problem Statement:
Determine whether a Hamiltonian Cycle (a closed loop that visits every vertex exactly once and returns to the starting vertex) exists in a given graph. Trace the backtracking process for the 5-vertex graph $\{A, B, C, D, E\}$ with edges $\{A\text{--}B, B\text{--}C, C\text{--}D, D\text{--}E, E\text{--}A, A\text{--}C, B\text{--}D\}$.

```java
import java.util.Arrays;

public class HamiltonianCycleSolver {
    private int V;
    private int[] path;

    public HamiltonianCycleSolver(int v) {
        this.V = v;
        this.path = new int[v];
        Arrays.fill(path, -1);
    }

    private boolean isSafe(int v, int[][] graph, int pos) {
        // Check if this vertex is an adjacent neighbor of the previous vertex
        if (graph[path[pos - 1]][v] == 0) return false;

        // Check if vertex has already been included in path
        for (int i = 0; i < pos; i++) {
            if (path[i] == v) return false;
        }
        return true;
    }

    private boolean hamCycleUtil(int[][] graph, int pos) {
        // Base case: All vertices are in the path
        if (pos == V) {
            // Check if there is an edge from the last vertex to the first vertex
            return graph[path[pos - 1]][path[0]] == 1;
        }

        // Try different vertices as candidates
        for (int v = 1; v < V; v++) {
            if (isSafe(v, graph, pos)) {
                path[pos] = v;
                if (hamCycleUtil(graph, pos + 1)) return true;
                path[pos] = -1; // Backtrack
            }
        }
        return false;
    }

    public void solve(int[][] graph) {
        path[0] = 0; // Start at vertex 0 (A)
        if (!hamCycleUtil(graph, 1)) {
            System.out.println("No Hamiltonian Cycle exists!");
            return;
        }

        char[] names = {'A', 'B', 'C', 'D', 'E'};
        System.out.print("Hamiltonian Cycle: ");
        for (int i = 0; i < V; i++) {
            System.out.print(names[path[i]] + " -> ");
        }
        System.out.println(names[path[0]]);
    }

    public static void main(String[] args) {
        // Vertices: A=0, B=1, C=2, D=3, E=4
        int V = 5;
        int[][] graph = new int[V][V];
        int[][] edges = {{0,1}, {1,2}, {2,3}, {3,4}, {4,0}, {0,2}, {1,3}};
        for (int[] e : edges) { graph[e[0]][e[1]] = 1; graph[e[1]][e[0]] = 1; }

        HamiltonianCycleSolver solver = new HamiltonianCycleSolver(V);
        solver.solve(graph);
    }
}
```

#### Step-by-Step Worked Trace on $\{A, B, C, D, E\}$:
- Vertices: $A=0, B=1, C=2, D=3, E=4$. Path starts at $A$.
1. At $A$: Try neighbor $B$. $B$ is safe $\implies \text{Path} = [A, B]$.
2. At $B$: Neighbors of $B$ are $A, C, D$. $A$ already visited. Try $C$ $\implies \text{Path} = [A, B, C]$.
3. At $C$: Neighbors of $C$ are $B, D, A$. Try $D$ $\implies \text{Path} = [A, B, C, D]$.
4. At $D$: Neighbors of $D$ are $C, B, E$. Try $E$ $\implies \text{Path} = [A, B, C, D, E]$.
5. Reached length 5. Check if edge exists from $E$ back to $A$: Edge $(E, A)$ is present!
* **Valid Hamiltonian Cycle Found**: **$A \to B \to C \to D \to E \to A$**.

#### Second Trace on Graph with Edges $\{0-1, 0-3, 1-2, 1-3, 1-4, 2-4, 3-4\}$ (Assignment Q6.4):
* Vertices: $\{0, 1, 2, 3, 4\}$ ($V = 5$).
* Starting at vertex 0:
  - $0 \to 1 \to 2 \to 4 \to 3 \to 0$ (Cycle completes since edge $(3, 0)$ exists!).
* **Valid Hamiltonian Cycle**: **$0 \to 1 \to 2 \to 4 \to 3 \to 0$**.
* **Complexities**: Time: $O(N!)$, Auxiliary Space: $O(N)$ path array.

---

## 10. Graph $m$-Coloring Problem Using Backtracking
*(Assignment Q6.3 & PPT: `Hamiltonian_Cycle_and_Graph_Coloring.pptx` — 12 Marks)*

### Problem Statement:
Given an undirected graph and an integer $m$, determine if the graph can be colored with at most $m$ colors such that no two adjacent vertices share the same color. Trace your solution on:
1. A 4-cycle graph ($C_4$) with $m = 2$.
2. A complete graph on 4 vertices ($K_4$) with $m = 3$.

### Algorithmic Logic:
1. Assign colors one by one to different vertices starting from vertex $0$.
2. Before assigning a color to vertex $v$, check if it is **safe** (no adjacent neighbor already has that color).
3. If safe, assign the color and recursively try to color the next vertex $v + 1$.
4. If no color from $1$ to $m$ can be assigned, backtrack (reset color of $v$ to $0$ and return `false`).

```java
public class GraphColoring {
    private int V;
    private int[] color;

    public GraphColoring(int v) {
        this.V = v;
        this.color = new int[v];
    }

    private boolean isSafe(int v, int[][] graph, int c) {
        for (int i = 0; i < V; i++) {
            if (graph[v][i] == 1 && color[i] == c) {
                return false; // Adjacent vertex has same color
            }
        }
        return true;
    }

    private boolean graphColoringUtil(int[][] graph, int m, int v) {
        if (v == V) return true; // All vertices colored successfully

        for (int c = 1; c <= m; c++) {
            if (isSafe(v, graph, c)) {
                color[v] = c;
                if (graphColoringUtil(graph, m, v + 1)) return true;
                color[v] = 0; // Backtrack
            }
        }
        return false;
    }

    public boolean solve(int[][] graph, int m) {
        java.util.Arrays.fill(color, 0);
        if (!graphColoringUtil(graph, m, 0)) {
            System.out.println("No " + m + "-coloring solution exists.");
            return false;
        }

        System.out.print("Valid " + m + "-Coloring: ");
        for (int i = 0; i < V; i++) System.out.print("V" + i + ": Color " + color[i] + " | ");
        System.out.println();
        return true;
    }

    public static void main(String[] args) {
        // Case 1: 4-cycle graph (C4) with m = 2
        int[][] c4 = {
            {0, 1, 0, 1},
            {1, 0, 1, 0},
            {0, 1, 0, 1},
            {1, 0, 1, 0}
        };
        System.out.println("--- Test Case 1: 4-Cycle (C4) with m = 2 ---");
        new GraphColoring(4).solve(c4, 2);

        // Case 2: Complete Graph (K4) with m = 3
        int[][] k4 = {
            {0, 1, 1, 1},
            {1, 0, 1, 1},
            {1, 1, 0, 1},
            {1, 1, 1, 0}
        };
        System.out.println("--- Test Case 2: Complete Graph (K4) with m = 3 ---");
        new GraphColoring(4).solve(k4, 3);
    }
}
```

#### Analytical Answers for Exam (Assignment Q6.3):
1. **Trace on 4-Cycle ($C_4$) with $m = 2$**:
   - $V_0 \to \text{Color } 1$
   - $V_1 \to \text{Color } 2$
   - $V_2 \to \text{Color } 1$
   - $V_3 \to \text{Color } 2$
   - **Result**: **Possible!** Every even cycle is bipartite, meaning its chromatic number $\chi(C_4) = \mathbf{2}$.
2. **Trace on $K_4$ with $m = 3$**:
   - In a complete graph $K_4$, every vertex is connected to all other 3 vertices.
   - By the Pigeonhole Principle, assigning $3$ colors across $4$ mutually adjacent vertices forces at least two adjacent vertices to share a color.
   - The chromatic number of $K_4$ is $\chi(K_4) = \mathbf{4}$.
   - **Result**: **Impossible!** Backtracking exhausts all combinations and returns `false`.
* **Complexities**: Time: $O(m^V)$, Auxiliary Space: $O(V)$ recursion stack.

---

## 10. Validate Binary Search Tree: Min-Max Range Approach
*(Paper 5 Q5c — 6 Marks)*

### Problem Statement:
Check whether a binary tree is a Binary Search Tree (BST) using the min-max range approach. Analyse the tree whose root is $10$, left child $5$ (with children $2$ and $12$), and right child $15$. Explain why comparing each node only with its parent is not sufficient.

```java
public class ValidateBST {
    public static boolean isValidBST(TreeNode root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private static boolean validate(TreeNode node, long min, long max) {
        if (node == null) return true;

        // Current node value must lie strictly between min and max
        if (node.val <= min || node.val >= max) {
            return false;
        }

        // Left subtree must be strictly < node.val, right subtree strictly > node.val
        return validate(node.left, min, node.val) && validate(node.right, node.val, max);
    }

    public static void main(String[] args) {
        // Tree: 10(5(2, 12), 15)
        TreeNode root = new TreeNode(10);
        root.left = new TreeNode(5);
        root.right = new TreeNode(15);
        root.left.left = new TreeNode(2);
        root.left.right = new TreeNode(12);

        System.out.println("Is Valid BST? " + isValidBST(root)); // false
    }
}
```

#### Why Parent-Only Comparison Fails:
* If we check each node only against its parent:
  - Node 2 is compared with parent 5: $2 < 5$ (Valid).
  - Node 12 is compared with parent 5: $12 > 5$ (Valid).
  - Node 5 is compared with parent 10: $5 < 10$ (Valid).
  - Node 15 is compared with parent 10: $15 > 10$ (Valid).
  - **Local parent check falsely concludes the tree is a valid BST!**
* **Why it is INVALID**: Node 12 is in the **left subtree of root 10**. By the fundamental definition of a BST, every node in the left subtree of 10 must be strictly less than 10. Since $12 > 10$, the tree violates the BST property! The min-max range approach enforces `validate(node.left.right, min=5, max=10)`, and since $12 \not< 10$, it correctly flags the violation.

---

## 11. 0/1 Knapsack Problem & Longest Common Subsequence (DP)
*(Syllabus Foundations — 12 Marks)*

### 11.1 0/1 Knapsack Problem (Space Optimized):
```java
public class Knapsack01 {
    public static int knapSack(int W, int[] wt, int[] val) {
        int[] dp = new int[W + 1];
        for (int i = 0; i < wt.length; i++) {
            // Traverse backwards from W down to wt[i] to ensure each item is used at most once
            for (int w = W; w >= wt[i]; w--) {
                dp[w] = Math.max(dp[w], val[i] + dp[w - wt[i]]);
            }
        }
        return dp[W];
    }
}
```
* **Recurrence**: $dp[w] = \max(dp[w], val[i] + dp[w - wt[i]])$. Time: $O(N \cdot W)$, Space: $O(W)$.

### 11.2 Longest Common Subsequence (LCS):
```java
public class LCS {
    public static int lcs(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[m][n];
    }
}
```

---
---

# PART 2: SECTION B QUESTIONS (8 MARKS) [Question 10 Pool]

---

## 12. Shortest Path in Unweighted Graph via BFS
*(Paper 1 Q10 — 8 Marks)*

### Problem Statement:
Find the shortest path (minimum number of edges) between two vertices using BFS and display the path. Trace from vertex $0$ to $4$ on edges $0\text{--}1, 0\text{--}2, 1\text{--}3, 2\text{--}3, 3\text{--}4, 2\text{--}5$. Explain why BFS, and not DFS, guarantees the shortest path.

```java
import java.util.*;

public class ShortestPathBFS {
    public static List<Integer> shortestPath(int V, List<List<Integer>> adj, int src, int dest) {
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
        for (int at = dest; at != -1; at = parent[at]) {
            path.add(at);
        }
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

        System.out.println("Shortest Path from 0 to 4: " + shortestPath(V, adj, 0, 4));
    }
}
```

#### Why BFS Guarantees Shortest Path while DFS Does Not:
* **BFS Guarantee**: BFS explores nodes level by level in order of their distance from the source ($0, 1, 2, \dots$). The first time the destination vertex is encountered, it is reached by the path with the minimum number of edges.
* **DFS Failure**: DFS traverses deep into a branch before backtracking. It may reach the destination through a long meandering path (e.g., length 5) before ever checking a direct 2-edge path.

---

## 13. Binary Tree Traversals: Postorder & Level Order
*(Paper 4 Q10 — 8 Marks)*

```java
public class TreeTraversalsDemo {
    // (a) Postorder: Left -> Right -> Root
    public static void postorder(TreeNode root) {
        if (root == null) return;
        postorder(root.left);
        postorder(root.right);
        System.out.print(root.val + " ");
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        System.out.print("Postorder Traversal: ");
        postorder(root);
        System.out.println();
    }
}
```

* **Traversal Orders**:
  - **Preorder**: Root $\to$ Left $\to$ Right
  - **Inorder**: Left $\to$ Root $\to$ Right (Yields sorted order in a BST!)
  - **Postorder**: Left $\to$ Right $\to$ Root (Used for deleting trees and bottom-up metric calculation).

---

## 14. Number of Islands in Binary 2D Matrix (DFS/BFS)
*(Paper 5 Q10 — 8 Marks)*

### Problem Statement:
Given a 2D binary matrix where `1` represents land and `0` represents water, count the number of islands (groups of `1`s connected horizontally or vertically).

```java
public class NumberOfIslandsSolver {
    public static int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        int count = 0;
        int rows = grid.length, cols = grid[0].length;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    count++;
                    sinkIsland(grid, r, c); // Sink the connected land component
                }
            }
        }
        return count;
    }

    private static void sinkIsland(char[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] != '1') {
            return;
        }
        grid[r][c] = '0'; // Mark visited by sinking

        // Explore all 4 orthogonal directions
        sinkIsland(grid, r + 1, c);
        sinkIsland(grid, r - 1, c);
        sinkIsland(grid, r, c + 1);
        sinkIsland(grid, r, c - 1);
    }

    public static void main(String[] args) {
        // Paper 5 Q10 Matrix:
        char[][] grid = {
            {'1', '1', '0', '0', '0'},
            {'0', '1', '0', '0', '1'},
            {'1', '0', '0', '1', '1'},
            {'0', '0', '0', '0', '0'}
        };
        System.out.println("Total Islands Counted: " + numIslands(grid)); // 2
    }
}
```

* **Complexities**: Time: $O(R \cdot C)$ (each cell visited a constant number of times), Auxiliary Space: $O(R \cdot C)$ recursion stack.
