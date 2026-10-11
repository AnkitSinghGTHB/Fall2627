# 📘 Unit 5: Dynamic Programming & Graph Algorithms

---

## 1. Dynamic Programming Master Paradigms

Dynamic Programming applies to problems exhibiting **Optimal Substructure** (optimal solution to problem contains optimal solutions to subproblems) and **Overlapping Subproblems**.

### 1.1 0/1 Knapsack Problem
Given $N$ items with weights $wt[i]$ and values $val[i]$, and knapsack capacity $W$:
* **Recurrence**:
  $$dp[i][w] = \begin{cases} 
    dp[i-1][w] & \text{if } wt[i-1] > w \\
    \max(dp[i-1][w], \, val[i-1] + dp[i-1][w - wt[i-1]]) & \text{if } wt[i-1] \le w
  \end{cases}$$
* **1D Space-Optimized Array ($O(W)$ Space)**: Must iterate capacity $w$ backwards from $W$ down to $wt[i]$ to prevent reusing the same item:

```java
public static int knapsack(int W, int[] wt, int[] val, int n) {
    int[] dp = new int[W + 1];
    for (int i = 0; i < n; i++) {
        for (int w = W; w >= wt[i]; w--) {
            dp[w] = Math.max(dp[w], val[i] + dp[w - wt[i]]);
        }
    }
    return dp[W];
}
// Time Complexity: O(N * W), Space Complexity: O(W)
```

### 1.2 Longest Common Subsequence (LCS)
* **Recurrence**:
  $$L[i][j] = \begin{cases}
    1 + L[i-1][j-1] & \text{if } s_1[i-1] == s_2[j-1] \\
    \max(L[i-1][j], \, L[i][j-1]) & \text{if } s_1[i-1] \ne s_2[j-1]
  \end{cases}$$

```java
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
```

---

## 2. Graph Algorithms: Dijkstra & Minimum Spanning Trees

### 2.1 Dijkstra's Shortest Path Algorithm (Priority Queue)
Finds single-source shortest path in weighted graphs with **non-negative edges**:

```java
import java.util.*;

public class Dijkstra {
    static class Edge { int to, weight; Edge(int t, int w) { to = t; weight = w; } }

    public static int[] shortestPath(int n, List<List<Edge>> adj, int src) {
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.offer(new int[]{src, 0});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int u = curr[0], d = curr[1];
            if (d > dist[u]) continue;

            for (Edge edge : adj.get(u)) {
                if (dist[u] + edge.weight < dist[edge.to]) {
                    dist[edge.to] = dist[u] + edge.weight;
                    pq.offer(new int[]{edge.to, dist[edge.to]});
                }
            }
        }
        return dist;
    }
}
// Time Complexity: O((V + E) log V), Space Complexity: O(V)
```

### 2.2 Kruskal's Minimum Spanning Tree (Disjoint Set Union)
Sorts all edges by weight ascending. Uses Union-Find with path compression to add edges that do not create cycles until $V - 1$ edges are added.

---

## 3. Model Exam Questions & Answers

### Question 1 (12 Marks)
**Solve the 0/1 Knapsack problem for items with weights $wt = [2, 3, 4, 5]$ and values $val = [3, 4, 5, 6]$ with knapsack capacity $W = 5$. Draw the complete DP table and backtrack to identify the selected items.**

**Solution**:
1. **DP Table Construction ($5 \times 6$ grid)**:
   - Rows: Items $0$ to $4$; Columns: Capacities $0$ to $5$.

| Item ($i$) | Weight ($wt$) | Value ($val$) | $w=0$ | $w=1$ | $w=2$ | $w=3$ | $w=4$ | $w=5$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$0$** (None) | — | — | 0 | 0 | 0 | 0 | 0 | 0 |
| **$1$** | 2 | 3 | 0 | 0 | 3 | 3 | 3 | 3 |
| **$2$** | 3 | 4 | 0 | 0 | 3 | 4 | 4 | **7** |
| **$3$** | 4 | 5 | 0 | 0 | 3 | 4 | 5 | **7** |
| **$4$** | 5 | 6 | 0 | 0 | 3 | 4 | 5 | **7** |

2. **Maximum Profit**: $dp[4][5] = \mathbf{7}$.
3. **Backtracking Selected Items**:
   - At $(4, 5)$: $dp[4][5] = dp[3][5] = 7 \implies$ Item 4 not included.
   - At $(3, 5)$: $dp[3][5] = dp[2][5] = 7 \implies$ Item 3 not included.
   - At $(2, 5)$: $dp[2][5] = 7 \ne dp[1][5] = 3 \implies$ **Item 2 (wt=3, val=4) INCLUDED!**  
     Remaining capacity $= 5 - 3 = 2$.
   - At $(1, 2)$: $dp[1][2] = 3 \ne dp[0][2] = 0 \implies$ **Item 1 (wt=2, val=3) INCLUDED!**  
     Remaining capacity $= 2 - 2 = 0$.
   - **Optimal Items Chosen**: **Item 1 & Item 2** (Total Weight $= 2+3=5$, Total Value $= 3+4=\mathbf{7}$).

### Question 2 (8 Marks)
**Differentiate between Dijkstra's algorithm and Prim's algorithm. Why does Dijkstra fail on graphs with negative weight edges?**

**Solution**:
1. **Dijkstra vs Prim**:
   - *Dijkstra*: Computes shortest paths from a single source to all vertices (minimizes cumulative root distance $dist[u] + weight$).
   - *Prim*: Constructs Minimum Spanning Tree connecting all vertices with minimal total edge weight (minimizes direct connection weight $weight(u, v)$).
2. **Why Dijkstra Fails on Negative Edges**:
   - Dijkstra relies on the greedy assumption that once a vertex is marked visited / extracted from the priority queue, its recorded shortest distance is permanently optimal.
   - A negative edge encountered later in the graph can provide a cheaper route to an already closed vertex, which Dijkstra will never re-evaluate, producing incorrect distance estimates. (Use Bellman-Ford for negative weights).
