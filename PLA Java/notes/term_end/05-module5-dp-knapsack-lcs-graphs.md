# 📘 Unit 5: Dynamic Programming & Graph Algorithms

---

## 1. Dynamic Programming Master Paradigms

### 1.1 0/1 Knapsack Problem (1D Space Optimized)
* **Recurrence**:
  $$dp[w] = \max(dp[w], val[i] + dp[w - wt[i]])$$
  *(Iterate backwards from $W$ down to $wt[i]$ to prevent reusing the same item)*

```java
public class KnapsackDP {
    public static int knapsack(int W, int[] wt, int[] val, int n) {
        int[] dp = new int[W + 1];
        for (int i = 0; i < n; i++) {
            for (int w = W; w >= wt[i]; w--) {
                dp[w] = Math.max(dp[w], val[i] + dp[w - wt[i]]);
            }
        }
        return dp[W];
    }

    public static void main(String[] args) {
        int W = 5;
        int[] wt = {2, 3, 4, 5};
        int[] val = {3, 4, 5, 6};
        System.out.println("Maximum Knapsack Value: " + knapsack(W, wt, val, wt.length));
    }
}
// Time Complexity: O(N * W), Space Complexity: O(W)
```
**Sample Input**: $W = 5, wt = [2, 3, 4, 5], val = [3, 4, 5, 6]$  
**Sample Output**:
```text
Maximum Knapsack Value: 7
```

---

### 1.2 Longest Common Subsequence (LCS)
* **Recurrence**:
  $$L[i][j] = \begin{cases}
    1 + L[i-1][j-1] & \text{if } s_1[i-1] == s_2[j-1] \\
    \max(L[i-1][j], \, L[i][j-1]) & \text{if } s_1[i-1] \ne s_2[j-1]
  \end{cases}$$

```java
public class LCSDemo {
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

    public static void main(String[] args) {
        String s1 = "LONGEST", s2 = "STONE";
        System.out.println("LCS of " + s1 + " and " + s2 + ": " + lcs(s1, s2));
    }
}
```
**Sample Input**: `"LONGEST"`, `"STONE"`  
**Sample Output**:
```text
LCS of LONGEST and STONE: 3
```
*(Common subsequence: `"ONE"`).*

---

## 2. Tree Traversals (DFS & BFS Level Order)
*(Priority Topic 15 — `Tree_Traversals.pptx`)*

```java
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { this.val = v; }
}

public class TreeTraversals {
    public static void preorder(TreeNode root) {
        if (root == null) return;
        System.out.print(root.val + " ");
        preorder(root.left);
        preorder(root.right);
    }

    public static void inorder(TreeNode root) {
        if (root == null) return;
        inorder(root.left);
        System.out.print(root.val + " ");
        inorder(root.right);
    }

    public static void postorder(TreeNode root) {
        if (root == null) return;
        postorder(root.left);
        postorder(root.right);
        System.out.print(root.val + " ");
    }

    public static void levelOrder(TreeNode root) {
        if (root == null) return;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            TreeNode curr = queue.poll();
            System.out.print(curr.val + " ");
            if (curr.left != null) queue.offer(curr.left);
            if (curr.right != null) queue.offer(curr.right);
        }
    }

    public static void main(String[] args) {
        /* Construct Tree:
                 1
               /   \
              2     3
             / \
            4   5
        */
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        System.out.print("Preorder:   "); preorder(root); System.out.println();
        System.out.print("Inorder:    "); inorder(root); System.out.println();
        System.out.print("Postorder:  "); postorder(root); System.out.println();
        System.out.print("Level Order: "); levelOrder(root); System.out.println();
    }
}
```
**Sample Output**:
```text
Preorder:   1 2 4 5 3 
Inorder:    4 2 5 1 3 
Postorder:  4 5 2 3 1 
Level Order: 1 2 3 4 5 
```

---

## 3. Graph Algorithms: Dijkstra & Kruskal's MST

### 3.1 Dijkstra's Shortest Path Algorithm
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

    public static void main(String[] args) {
        int n = 4;
        List<List<Edge>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        adj.get(0).add(new Edge(1, 4));
        adj.get(0).add(new Edge(2, 1));
        adj.get(2).add(new Edge(1, 2));
        adj.get(1).add(new Edge(3, 1));
        adj.get(2).add(new Edge(3, 5));

        int[] dist = shortestPath(n, adj, 0);
        System.out.println("Distances from node 0: " + Arrays.toString(dist));
    }
}
// Time Complexity: O((V + E) log V), Auxiliary Space: O(V)
```
**Sample Output**:
```text
Distances from node 0: [0, 3, 1, 4]
```

---

### 3.2 Kruskal's Algorithm with Disjoint Set Union (DSU)
*(From `Kruskal_Algorithm.pptx`)*

```java
import java.util.*;

class Edge implements Comparable<Edge> {
    int src, dest, weight;
    Edge(int s, int d, int w) { src = s; dest = d; weight = w; }
    public int compareTo(Edge o) { return Integer.compare(this.weight, o.weight); }
}

public class KruskalMST {
    static int find(int[] parent, int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent, parent[i]); // Path compression
    }

    static void union(int[] parent, int[] rank, int x, int y) {
        int rootX = find(parent, x);
        int rootY = find(parent, y);
        if (rootX != rootY) {
            if (rank[rootX] < rank[rootY]) parent[rootX] = rootY;
            else if (rank[rootX] > rank[rootY]) parent[rootY] = rootX;
            else { parent[rootY] = rootX; rank[rootX]++; }
        }
    }

    public static int getMSTWeight(int V, List<Edge> edges) {
        Collections.sort(edges);
        int[] parent = new int[V];
        int[] rank = new int[V];
        for (int i = 0; i < V; i++) parent[i] = i;

        int totalWeight = 0;
        int edgesCount = 0;
        for (Edge e : edges) {
            int rootSrc = find(parent, e.src);
            int rootDest = find(parent, e.dest);
            if (rootSrc != rootDest) {
                totalWeight += e.weight;
                union(parent, rank, rootSrc, rootDest);
                edgesCount++;
                if (edgesCount == V - 1) break;
            }
        }
        return totalWeight;
    }

    public static void main(String[] args) {
        int V = 4;
        List<Edge> edges = Arrays.asList(
            new Edge(0, 1, 10),
            new Edge(0, 2, 6),
            new Edge(0, 3, 5),
            new Edge(1, 3, 15),
            new Edge(2, 3, 4)
        );
        System.out.println("Total MST Weight: " + getMSTWeight(V, edges));
    }
}
// Time: O(E log E), Space: O(V)
```
**Sample Output**:
```text
Total MST Weight: 19
```
