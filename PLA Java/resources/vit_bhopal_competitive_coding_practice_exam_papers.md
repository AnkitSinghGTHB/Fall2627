# VIT BHOPAL UNIVERSITY

## TERM END EXAMINATIONS (TEE) – October 2026

* **Programme:** B.Tech., Integrated M.Tech
* **Semester:** Fall Semester 2026-27
* **Course Name:** Competitive Coding Practice - CS
* **Course Code:** PLA1004
* **Time:** 3 Hrs. | **Max. Marks:** 100
* *Note: Calculators of any kind are not allowed. Answer ALL the Questions.*

---

# Paper 1: Slot A11+A12 (15-10-2026/S-2)

## PART A – (60 Marks)

**Q1.**
* **(a)** A Strobogrammatic number looks the same when rotated by $180$ degrees (for example $69$, $88$, $818$). Write the algorithm and Java program to generate all Strobogrammatic numbers of length $N$ and list the numbers produced for $N = 3$. Evaluate your approach (building from the middle outwards) against checking every $N$-digit number, and justify why the digit $0$ may not be used in the outermost pair. *(12 Marks)*

**OR**

* **(b)** Analyse the following Binary Search code. Determine its time complexity in the best, average and worst cases and the space complexity of both the iterative and recursive versions. Trace the execution for the sorted array $\{2, 5, 8, 12, 16, 23, 38, 45, 56, 72\}$ while searching for the key $23$ and then for the key $50$. *(12 Marks)*

```java
int binarySearch(int a[], int l, int r, int key) {
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (a[mid] == key) return mid;
        else if (a[mid] < key) l = mid + 1;
        else r = mid - 1;
    }
    return -1;
}
```

**Q2.**
* **(a)** Write the algorithm and Java program to find the smallest number strictly greater than a given number $N$ whose binary representation is a palindrome. Illustrate your solution for $N = 25$ by showing the binary representation of each number checked, and analyse the time complexity. *(7 Marks)*
* **(b)** Analyse the following code. Trace the value of `r` after each iteration, explain which properties of the XOR operator make the code work, and compare its space complexity with a HashMap-based solution to the same problem. *(5 Marks)*

```java
int[] a = {4, 1, 2, 1, 2};
int r = 0;
for (int x : a) r ^= x;
System.out.println(r);
```

**OR**

* **(c)** Given a 2D matrix, an hourglass is the set of $7$ values at positions $(i, j)$, $(i, j+1)$, $(i, j+2)$, $(i+1, j+1)$, $(i+2, j)$, $(i+2, j+1)$, $(i+2, j+2)$. Write the algorithm and Java program to find the maximum sum among all hourglasses in a matrix, and trace your solution for a $5 \times 5$ matrix of your choice. *(12 Marks)*

**Q3.**
* **(a)** Write the algorithm and Java program to solve the Josephus Problem for $n$ people standing in a circle where every $k$-th person is eliminated, and display the complete elimination order of all $n$ people. Trace your solution for $n = 8$ and $k = 3$ and analyse the time complexity of a list-based simulation. *(6 Marks)*
* **(b)** Given the start and finish times of $N$ meetings, write the algorithm and Java program to find the minimum number of meeting rooms required so that no two overlapping meetings share a room, using a greedy approach. Trace your solution for the meetings $(0,30)$, $(5,10)$, $(8,12)$, $(15,20)$ and $(25,35)$ and analyse the time complexity. *(6 Marks)*

**OR**

* **(c)** Given a string $S$, write the algorithm and Java program to rearrange its characters to form the lexicographically largest palindrome possible. If no palindromic arrangement exists, output $-1$. Trace your solution for $S =$ `"aabbbcc"` and $S =$ `"abcd"`, and analyse the time and space complexity of your approach. *(12 Marks)*

**Q4.**
* **(a)** Write a Java program to implement the basic operations of a singly linked list: insertion at the beginning, at the end and at a given position; deletion of a node by value; and traversal. Trace the list after each of the operations `insertBegin(10)`, `insertEnd(20)`, `insertEnd(30)`, `insertAt(25, position 3)` and `delete(20)`, and analyse the time complexity of each operation, including the effect of maintaining a tail pointer. *(12 Marks)*

**OR**

* **(b)** Design a stack that supports `push`, `pop`, `top` and retrieval of the maximum element, all in $O(1)$ time (Max Stack), and write the Java program to implement it. Evaluate your design against (i) scanning the stack for the maximum on every query and (ii) storing (value, current maximum) pairs, in terms of time and space, and justify the design you choose. *(12 Marks)*

**Q5.**
* **(a)** Write the algorithm and Java program to check whether an undirected graph represented by an adjacency list is connected, and if not, to display the number of connected components. Trace your solution for the $7$-vertex graph with edges $0\text{--}1$, $1\text{--}2$, $3\text{--}4$, $5\text{--}6$. Evaluate BFS against recursive DFS for a graph with $10^5$ vertices and justify your choice. *(12 Marks)*

**OR**

* **(b)** Write the algorithm and Java program to perform the Level Order Traversal of a binary tree using a queue, printing each level on a new line. Trace the queue contents for the tree whose root is $3$, with left child $9$ and right child $20$, where $20$ has children $15$ and $7$, and analyse the time and space complexity. *(6 Marks)*
* **(c)** Write a Java program to check whether two binary trees are identical (same structure and same node values). Analyse the working of your program on the pair $T_1 = 1(2, 3)$, $T_2 = 1(2, 3)$ and on the pair $T_1 = 1(2, 3)$, $T_3 = 1(3, 2)$, where the notation `root(left, right)` is used, and state the time complexity. *(6 Marks)*

## PART B – (40 Marks)

* **Q6.** Write a Java program that reads an integer between $1$ and $7$ and, using switch-case, displays the corresponding day of the week (Monday to Sunday), and uses logical operators to indicate whether the day is a Weekday or a Weekend. Analyse the behaviour of your program if every `break` statement is removed by tracing the output for the input $6$, and state the output for the input $9$. *(8 Marks)*
* **Q7.** Write the algorithm and Java program to sort an array containing only $0\text{s}$, $1\text{s}$ and $2\text{s}$ in a single pass without using a sorting library (Dutch National Flag algorithm). Trace the three pointers for the array $\{2, 0, 2, 1, 1, 0\}$ and analyse the time and space complexity. *(8 Marks)*
* **Q8.** Write the algorithm and Java program to solve the N-Queens problem for $N = 4$ using backtracking and display all solutions. Evaluate the effect of pruning by comparing the number of queen placements your program tries with the $4^4 = 256$ placements of a brute-force approach, and justify your conclusion. *(8 Marks)*
* **Q9.** Write a Java program to find the minimum element in every contiguous window of size $K$ of an array using the Sliding Window Minimum technique with a deque. Apply your program to the array $\{4, 2, 12, 3, 8, 1, 7, 9\}$ with $K = 3$ and show the deque contents for each window. *(8 Marks)*
* **Q10.** Write the algorithm and Java program to find the shortest path (minimum number of edges) between two vertices of an unweighted graph using BFS and display the path. Trace your solution from vertex $0$ to vertex $4$ for the graph with edges $0\text{--}1$, $0\text{--}2$, $1\text{--}3$, $2\text{--}3$, $3\text{--}4$, $2\text{--}5$ (visit neighbours in ascending order), and explain why BFS, and not DFS, guarantees the shortest path. *(8 Marks)*

---

# Paper 2: Slot B14+D21 (21-10-2026/S-2)

## PART A – (60 Marks)

**Q1.**
* **(a)** Write a Java program to Move all Hyphens to the Beginning of a given string while preserving the relative character order of the non-hyphen characters. *(12 Marks)*

**OR**

* **(b)** Write the algorithm and Java program to identify whether a given number string is a Strobogrammatic Number (looks the same when rotated $180$ degrees). *(12 Marks)*

**Q2.**
* **(a)** Write a Java program to find the Height of a Binary Tree (number of nodes on the longest path from root to leaf), along with its algorithm. *(7 Marks)*
* **(b)** Write a Java program that reads three numbers and uses nested conditional operators / if-else ladders to find the largest number, demonstrating relational and logical operators. *(5 Marks)*

**OR**

* **(c)** Write a Java program to isolate and swap the lower and upper nibbles of an $8$-bit byte variable using bitwise shift and mask operations. *(12 Marks)*

**Q3.**
* **(a)** Write the algorithm and Java program to solve the Josephus Problem. Given $n$ people standing in a circle and every $k$-th person eliminated, determine the position of the survivor. Trace your solution for $n = 8$ and $k = 4$. *(6 Marks)*
* **(b)** Write the algorithm and Java program for the Activity Selection Problem using a greedy approach. Select the maximum number of non-overlapping activities based on their start and finish times. *(6 Marks)*

**OR**

* **(c)** Write a formal algorithmic description and a recursive Java program to accurately calculate the Height of a Binary Tree, measuring the maximum edge or node depth extending from the root node down to the deepest leaf node. *(12 Marks)*

**Q4.**
* **(a)** Write a Java program to find the maximum element in every contiguous subarray of size $K$ using the Sliding Window Maximum technique with a deque. *(12 Marks)*

**OR**

* **(b)** Write the Quick Sort algorithm and a Java program to sort an array in ascending order. Trace the partitioning process for the input $\{3, 7, 8, 5, 2, 1, 9\}$. *(12 Marks)*

**Q5.**
* **(a)** Write a dynamic programming-based Java program equipped with memorization techniques to solve the Maneuvering Problem, accurately calculating the total number of unique paths from the top-left corner to the bottom-right corner of an $M \times N$ grid. *(12 Marks)*

**OR**

* **(b)** Write a Java program using a stack to check whether an expression contains balanced parentheses. Consider `()`, `{}`, and `[]`. *(6 Marks)*
* **(c)** Analyze the following code snippet to determine its time and space complexity. Trace its execution with input matrix of size $3 \times 3$. *(6 Marks)*

```java
int maxSum = Integer.MIN_VALUE;
for(int i=0; i < n - 2; i++) {
    for(int j=0; j < m - 2; j++) {
        int sum = mat[i][j]+mat[i][j+1]+mat[i][j+2]+mat[i+1][j+1]+mat[i+2][j]+mat[i+2][j+1]+mat[i+2][j+2];
        if(sum > maxSum) maxSum = sum;
    }
}
```

## PART B – (40 Marks)

* **Q6.** Write the algorithm and Java program to check whether a given integer (and its binary form) is a **Binary Palindrome**. *(8 Marks)*
* **Q7.** Write a Java program to swap the two nibbles of a given byte using bitwise operators. Display the binary representation before and after swapping. *(8 Marks)*
* **Q8.** Analyze the following code snippet and determine its time and space complexity. Trace the execution for $N=16$. *(8 Marks)*

```java
int count = 0;
for (int i = 1; i < n; i = i * 2) {
    for (int j = n; j > 0; j = j / 2) {
        count++;
    }
}
```

* **Q9.** Write a Java program to merge two sorted singly linked lists into one sorted linked list. Do not create a third list; reuse the existing nodes. *(8 Marks)*
* **Q10.** Write the Breadth First Search (BFS) algorithm and a Java program to traverse a graph starting from a given source vertex using a queue. *(8 Marks)*

---

# Paper 3: Slot F11+F12 (18-10-2026/S-2)

## PART A – (60 Marks)

**Q1.**
* **(a)** Write the algorithm and Java program to compute the Euler's Phi ($\phi$) Algorithm value for a given integer $n$. *(12 Marks)*

**OR**

* **(b)** Write the algorithm and Java program to identify whether a given number string is a Strobogrammatic Number (looks the same when rotated $180$ degrees). *(12 Marks)*

**Q2.**
* **(a)** Write a Java program to find the Diameter of a Binary Tree (the length of the longest path between any two nodes), along with its algorithm. *(7 Marks)*
* **(b)** Write a Java program that reads an operator character and two operands to implement a basic calculator using a switch-case control structure, demonstrating control flow and branching. *(5 Marks)*

**OR**

* **(c)** Write a Java program to find the Maximum Product Subarray in a given integer array using an optimized linear scan. *(12 Marks)*

**Q3.**
* **(a)** Write the algorithm and Java program to implement Huffman Coding to generate prefix codes for a set of characters based on their frequencies. Trace your solution for a small frequency set. *(6 Marks)*
* **(b)** Write the algorithm and Java program for the Activity Selection Problem using a greedy approach. Select the maximum number of non-overlapping activities based on their start and finish times. *(6 Marks)*

**OR**

* **(c)** Write the Selection Sort algorithm and a Java program to sort an array in ascending order. Trace the selection and swapping process for the input $\{64, 25, 12, 22, 11\}$. *(12 Marks)*

**Q4.**
* **(a)** Write a Java program to implement a Min Stack supporting `push`, `pop`, `top`, and retrieving the minimum element in $O(1)$ time. *(12 Marks)*

**OR**

* **(b)** Write a Java program to find the Longest Sequence of $1\text{s}$ after flipping a single $0$ to a $1$ in a given binary array or bit string. *(12 Marks)*

**Q5.**
* **(a)** Write a dynamic programming-based Java program equipped with memorization techniques to solve the Maneuvering Problem, accurately calculating the total number of unique paths from the top-left corner to the bottom-right corner of an $M \times N$ grid. *(12 Marks)*

**OR**

* **(b)** Write a Java program using a stack to check whether an expression contains balanced parentheses. Consider `()`, `{}`, and `[]`. *(6 Marks)*
* **(c)** Analyze the following code snippet to determine its time and space complexity. Trace its execution with input matrix of size $3 \times 3$. *(6 Marks)*

```java
int maxSum = Integer.MIN_VALUE;
for(int i=0; i < n - 2; i++) {
    for(int j=0; j < m - 2; j++) {
        int sum = mat[i][j]+mat[i][j+1]+mat[i][j+2]+mat[i+1][j+1]+mat[i+2][j]+mat[i+2][j+1]+mat[i+2][j+2];
        if(sum > maxSum) maxSum = sum;
    }
}
```

## PART B – (40 Marks)

* **Q6.** Write a Java program to implement Manacher's Algorithm to find the longest palindromic substring within a given text in linear time. *(8 Marks)*
* **Q7.** Write a Java program using the Simple Sieve of Eratosthenes algorithm to generate and display all prime numbers up to a given integer $N$. *(8 Marks)*
* **Q8.** Analyze the following code snippet and determine its time and space complexity. Trace the execution for $N=16$. *(8 Marks)*

```java
int count = 0;
for (int i = 1; i < n; i = i * 2) {
    for (int j = n; j > 0; j = j / 2) {
        count++;
    }
}
```

* **Q9.** Write a Java program to merge two sorted singly linked lists into one sorted linked list. Do not create a third list; reuse the existing nodes. *(8 Marks)*
* **Q10.** Write the algorithm and Java program to solve the Hamiltonian Cycle problem using backtracking to determine if a graph contains a cycle that visits every vertex exactly once. *(8 Marks)*

---

# Paper 4: Slot E11+E12 (14-10-2026/S-2)

## PART A – (60 Marks)

**Q1.**
* **(a)**
  * **(i)** Write a program that reads a student's marks in three subjects and, using suitable decision-making and control statements (if-else / switch-case), determines the grade (O, A+, A, B+, B, or F) and prints whether the student has Passed or Failed.
  * **(ii)** Explain the different asymptotic notations ($\text{Big-}O$, $\text{Big-}\Omega$, $\text{Big-}\Theta$) used to analyse the running time of an algorithm. For the code snippet given below, determine its time complexity using $\text{Big-}O$ notation and justify your answer: *(12 Marks)*

```java
for (i = 1; i <= n; i = i * 2)
    for (j = 1; j <= i; j++)
        print(j);
```

**OR**

* **(b)**
  * **(i)** Write a program using suitable control structures (loops and if-else) to print all the Armstrong numbers lying between two given integers $m$ and $n$.
  * **(ii)** Analyse the time and space complexity of the following recursive function used to compute the $n$-th Fibonacci number, and justify your answer: *(12 Marks)*

```java
int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
```

**Q2.**
* **(a)** Given an array of integers, an Equilibrium Index $i$ is one where the sum of elements at indices less than $i$ equals the sum of elements at indices greater than $i$. Write an efficient (non-brute-force) algorithm and code to find the maximum equilibrium sum among all equilibrium indices. *(7 Marks)*
* **(b)** Trace your solution for the array $\{-7, 1, 5, 2, -4, 3, 0\}$ and analyse the time and space complexity of your approach. *(5 Marks)*

**OR**

* **(c)** Write the algorithm and code to swap the two nibbles (the upper $4$ bits and the lower $4$ bits) of a given byte ($8$-bit number) using bitwise operators. *(12 Marks)*

**Q3.**
* **(a)** Explain the N-Queens problem and describe how backtracking is used to solve it. Illustrate your explanation with a worked example for $N = 4$, and write the code to print all possible solutions. *(6 Marks)*
* **(b)** The Huffman codes assigned to five symbols are: $A = 0$, $B = 10$, $C = 110$, $D = 1110$, $E = 1111$. Given the encoded bit string `'11101100101111'`, explain step by step how you would use the Huffman codes to decode the original sequence of symbols. (Only explain the decoding algorithm/steps clearly with the working — code is not required.) *(6 Marks)*

**OR**

* **(c)** Given a string $S$ of length $N$ consisting of lowercase English letters and an integer $K$, the weight of a character is its position in the alphabet ($a = 1, b = 2, \dots, z = 26$), and the weight of a substring is the sum of the weights of its characters. Write an efficient algorithm and code, to find the maximum weight among all substrings of $S$ having length exactly $K$, and report that substring. Trace your solution step by step for $S =$ `"abcadeaf"` and $K = 3$, and analyse the time and space complexity of your approach. *(12 Marks)*

**Q4.**
* **(a)**
  * **(i)** Write the algorithm and code to reverse a given singly linked list, using both the iterative and the recursive approach.
  * **(ii)** Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element, all in $O(1)$ time complexity. Explain your approach and write the code to implement this Min Stack. *(12 Marks)*

**OR**

* **(b)**
  * **(i)** Write the algorithm and code to detect the presence of a cycle in a singly linked list using Floyd's Cycle Detection (Tortoise and Hare) algorithm.
  * **(ii)** Write the algorithm and code to find the Next Greater Element for every element of a given array using a stack. *(12 Marks)*

**Q5.**
* **(a)** Explain Kruskal's Algorithm for finding the Minimum Spanning Tree (MST) of a graph. Write the algorithm and code to implement it using the Union-Find (Disjoint Set) data structure. *(12 Marks)*

**OR**

* **(b)** Write the algorithm and code to determine whether a Hamiltonian Cycle exists in a given graph using backtracking. *(6 Marks)*
* **(c)** Consider a graph with $5$ vertices $\{A, B, C, D, E\}$ and edges $\{A\text{--}B, B\text{--}C, C\text{--}D, D\text{--}E, E\text{--}A, A\text{--}C, B\text{--}D\}$. Solve step by step to find a Hamiltonian Cycle (if one exists), showing the backtracking process. *(6 Marks)*

## PART B – (40 Marks)

* **Q6.** Explain the Segmented Sieve algorithm and discuss why it is preferred over the Simple Sieve of Eratosthenes for finding primes in a large range. Write the code to find all prime numbers in a given range $[L, R]$, where $1 \le L \le R \le 10^9$ and $R - L \le 10^6$. *(8 Marks)*
* **Q7.** Explain the Block Swap Algorithm used to rotate an array of size $n$ to the left by $d$ positions. Write the code to implement it and analyse its time and space complexity. *(8 Marks)*
* **Q8.** Given a string $S$, write the algorithm and code to rearrange its characters to form the lexicographically smallest palindrome possible. If no palindromic arrangement exists, the program should output `'-1'`. *(8 Marks)*
* **Q9.** Explain the working of a Circular Queue. Write the algorithm and code to implement its `enqueue` and `dequeue` operations, handling the overflow and underflow conditions correctly. *(8 Marks)*
* **Q10.** Write the code along with the algorithm to perform: (a) Postorder traversal, and (b) Level order traversal, of a given binary tree. *(8 Marks)*

---

# Paper 5: Slot A21+A22 (17-10-2026/S-2)

## PART A – (60 Marks)

**Q1.**
* **(a)** Write the algorithm and Java program to compute Euler's Totient function $\varphi(N)$ using prime factorisation and display the count of integers from $1$ to $N$ that are co-prime to $N$. Evaluate this approach against the brute-force method of testing $\gcd(i, N) = 1$ for every $i$ by computing $\varphi(36)$ with both methods, and justify which method is suitable for $N$ up to $10^{12}$ by stating its complexity. *(12 Marks)*

**OR**

* **(b)** Analyse the following Insertion Sort code. Determine its time complexity in the best, average and worst cases and its space complexity. Trace the execution for the array $\{5, 2, 4, 6, 1, 3\}$, state the total number of element shifts, and explain why the best case occurs. *(12 Marks)*

```java
for (int i = 1; i < n; i++) {
    int key = a[i];
    int j = i - 1;
    while (j >= 0 && a[j] > key) {
        a[j + 1] = a[j];
        j = j - 1;
    }
    a[j + 1] = key;
}
```

**Q2.**
* **(a)** Write a Java program to find the length of the longest sequence of consecutive $1\text{s}$ in the binary representation of a number that can be obtained by flipping at most one $0$ bit to $1$. Display the binary representation before and after the flip for $N = 1775$ and analyse the time complexity of your solution. *(7 Marks)*
* **(b)** Analyse the following code. Determine the output, trace the binary value of $n$ in every iteration, and explain what the code computes and why it is faster than checking every bit of $n$. *(5 Marks)*

```java
int n = 40, c = 0;
while (n != 0) {
    n = n & (n - 1);
    c++;
}
System.out.println(c);
```

**OR**

* **(c)** Write the algorithm and Java program to find the contiguous subarray (containing at least one number) that has the largest product, using an efficient (non-brute-force) approach. Display the product and the start and end indices of the subarray, and trace your solution for the array $\{2, 3, -2, 4, -1\}$. *(12 Marks)*

**Q3.**
* **(a)** Write the algorithm and Java program to solve the Rat in a Maze problem using backtracking, where the rat can move only Right or Down in an $N \times N$ maze ($1 = \text{open}$, $0 = \text{blocked}$). Trace your solution for the following $4 \times 4$ maze, showing the dead ends and the backtracking steps. *(6 Marks)*

```
1 1 0 0
0 1 1 0
0 1 0 0
0 1 1 1
```

* **(b)** Write the algorithm and Java program to solve the Fractional Knapsack Problem using a greedy approach. Trace your solution for weights $\{10, 20, 30\}$, values $\{60, 100, 120\}$ and capacity $50$, and analyse why ordering the items by value-to-weight ratio is optimal here but not for the $0/1$ knapsack problem. *(6 Marks)*

**OR**

* **(c)** Write the algorithm and Java program to find the longest palindromic substring in a given string using Manacher's Algorithm. Trace your solution for the string `"babcbabcbaccba"` and analyse how the algorithm achieves linear time complexity. *(12 Marks)*

**Q4.**
* **(a)** Write the algorithm and Java program to detect a loop in a singly linked list using Floyd's Cycle Detection (Tortoise and Hare) algorithm and, if a loop exists, remove it without losing any node. Trace your solution for the list $1 \to 2 \to 3 \to 4 \to 5 \to 6$, where node $6$ points back to node $3$, and analyse why the two pointers must meet and the time and space complexity. *(12 Marks)*

**OR**

* **(b)** Write a Java program to solve the Stock Span Problem using a stack, where the span of a day is the number of consecutive days (including the current day) for which the price was less than or equal to the price on that day. Trace your solution for the prices $\{100, 80, 60, 70, 60, 75, 85\}$. Evaluate the stack-based approach against the brute-force approach and justify why its time complexity is $O(n)$. *(12 Marks)*

**Q5.**
* **(a)** The diameter of a binary tree is the number of nodes on the longest path between any two leaf nodes (the path may or may not pass through the root). Write the algorithm and Java program to find the diameter using (i) the naive approach that computes the height at every node and (ii) the optimised single-traversal approach. Evaluate the two approaches in terms of time complexity and recommend one with justification. *(12 Marks)*

**OR**

* **(b)** Write the Depth First Search (DFS) algorithm and a Java program to traverse a graph from a given source vertex using recursion. Trace the traversal and the recursion calls for the undirected graph with edges $0\text{--}1, 0\text{--}2, 1\text{--}3, 2\text{--}4, 3\text{--}4$ starting from vertex $0$ (visit neighbours in ascending order), and analyse the time complexity. *(6 Marks)*
* **(c)** Write a Java program to check whether a binary tree is a Binary Search Tree using the minimum-maximum range approach. Analyse the tree whose root is $10$, with left child $5$ (children $2$ and $12$) and right child $15$, and explain why comparing each node only with its parent is not sufficient. *(6 Marks)*

## PART B – (40 Marks)

* **Q6.** Write a Java program that reads the coefficients $a$, $b$ and $c$ of a quadratic equation $ax^2 + bx + c = 0$ and, using relational and logical operators with suitable decision-making statements, determines the nature of its roots (real and distinct, real and equal, or imaginary) and displays the roots. Analyse the decision flow of your program for $(a, b, c) = (1, -5, 6)$, $(1, 2, 1)$ and $(1, 2, 5)$ and state which branch is executed in each case. *(8 Marks)*
* **Q7.** Write the algorithm and Java program to rotate an array of size $n$ to the right by $k$ positions in $O(n)$ time and $O(1)$ extra space using the reversal algorithm. Trace your solution for the array $\{1, 2, 3, 4, 5, 6, 7\}$ with $k = 3$, explain why three reversals produce the rotation, and state how $k > n$ is handled. *(8 Marks)*
* **Q8.** Write the algorithm and Java program to solve the Job Sequencing with Deadlines problem using a greedy approach, where each job takes one unit of time. Given the jobs $J_1$ (deadline $2$, profit $100$), $J_2$ ($1$, $19$), $J_3$ ($2$, $27$), $J_4$ ($1$, $25$) and $J_5$ ($3$, $15$), trace your solution and evaluate whether ordering by profit is better than ordering by deadline, justifying your answer. *(8 Marks)*
* **Q9.** Write a Java program to find the first negative integer in every contiguous window of size $K$ of an array using a deque (display $0$ for a window with no negative integer). Apply your program to the array $\{12, -1, -7, 8, -15, 30, 16, 28\}$ with $K = 3$ and show the deque contents for each window. *(8 Marks)*
* **Q10.** Given a binary matrix in which $1$ represents land and $0$ represents water, write a Java program to count the number of islands (groups of $1\text{s}$ connected horizontally or vertically) using DFS or BFS. Trace your solution for the following matrix, showing the cells visited from each starting cell, and analyse the time complexity. *(8 Marks)*

```
1 1 0 0 0
0 1 0 0 1
1 0 0 1 1
0 0 0 0 0
```

---

# Paper 6: Slot B21+E24 (23-10-2026/S-2)

## PART A – (60 Marks)

**Q1.**
* **(a)** Explain the **Josephus Problem**. Derive the recursive formulation to find the position of the survivor for $n$ people and elimination step $k$. Solve for $n = 7, k = 3$. *(12 Marks)*

**OR**

* **(b)** Given a set of activities, where each activity has a starting time and a finishing time, write a **Java program to implement the Activity Selection Problem using the greedy approach**. The program should select the **maximum number of non-overlapping activities** by choosing the activity that finishes earliest. For the given input, display the selected activities and the maximum number of activities selected. *(12 Marks)*

```text
Sample Input:
6
1 2
3 4
0 6
5 7
8 9
5 9
```

**Q2.**
* **(a)** Differentiate between **Quick Sort and Selection Sort** in terms of time complexity (best, average, and worst cases), space complexity, and stability. Discuss the role of pivot selection in Quick Sort's performance. *(7 Marks)*
* **(b)** Design a **Min Stack** data structure that supports `push()`, `pop()`, `top()`, and `getMin()` operations, all in $O(1)$ time complexity. Write the pseudo-code and explain the auxiliary memory used. *(5 Marks)*

**OR**

* **(c)** Consider an undirected graph with **6 vertices** and edges $(1,2)$, $(1,3)$, $(2,3)$, $(2,4)$, $(3,4)$, $(3,5)$, $(4,5)$, $(4,6)$, $(5,6)$. Write a **Java program using backtracking** to determine whether the given graph can be colored using at most **3 colors** such that no two adjacent vertices have the same color, and also determine whether the graph contains a **Hamiltonian Cycle**. Display the valid vertex coloring, if one exists, and the Hamiltonian Cycle, if one exists. Also state the **worst-case time complexity** of the backtracking approach. *(12 Marks)*

**Q3.**
* **(a)** Write a Java program that demonstrates the use of decision-making control structures (if-else, switch-case) along with bitwise and assignment operators. Display clear descriptive messages for each branch. *(6 Marks)*
* **(b)** Write a **Java program to check whether a given positive integer is a binary palindrome**. Convert the number into its binary representation and determine whether the binary representation reads the same forward and backward. For the input $37$, display its binary representation and the result. *(6 Marks)*

**OR**

* **(c)** Define a **strobogrammatic number**. Write a **Java program using a HashMap** to determine whether the given number $619$ is strobogrammatic. Display the result and state the time and space complexity of your solution. *(12 Marks)*

**Q4.**
* **(a)** Define an **hourglass** in a 2D matrix. Write a **Java program to find the maximum hourglass sum** in the given matrix. Display the maximum hourglass sum and state the time and space complexity of your solution. *(12 Marks)*

```text
Input:
1 2 3
4 5 6
7 8 9
```

**OR**

* **(b)** Define the **Grid Maneuvering Problem**. Write a **Java program using recursion** to find the number of possible ways to move from the top-left corner to the bottom-right corner of the given grid, where movement is allowed only **right or down**. Identify the data structure used internally during recursion and explain why it is required. Also state the time and space complexity of your solution. *(12 Marks)*

**Q5.**
* **(a)** Write a **Java program to detect whether a loop exists in a singly linked list**. If a loop is present, **find the position (nth node from the beginning) at which the loop starts**, remove the loop, and display the linked list after removing it. Also state the time and space complexity of your solution. *(12 Marks)*

**OR**

* **(b)** Write the algorithm and Java program to solve the **N-Queens Problem using backtracking**. Trace your solution for $N = 4$. Draw Matrix. *(6 Marks)*
* **(c)** Write the algorithm and Java program for **Huffman Coding using a greedy approach** to generate prefix codes for a set of characters with given frequencies. *(6 Marks)*

## PART B – (40 Marks)

* **Q6.** Define Preorder, Inorder, and Postorder traversal of a binary tree. Write the algorithm and Java program to perform all three traversals for the given binary tree. Display the traversal results and state the time and space complexity of your approach. *(8 Marks)*

```text
Input Tree:
    1
   / \
  2   3
 / \   \
4   5   6
```

* **Q7.** Write a Java program that reads an integer between $1$ & $7$ using switch case, display the corresponding day of the week (Mon to Sun), and use logical operators to indicate whether the day is week day or weekend. Analyze the behavior of your program if every `break` statement is removed by tracking the output for the input $6$, state the output for input $9$. *(8 Marks)*
* **Q8.** Define the **diameter of a binary tree**. Explain how a binary tree can be represented using an **array and linked-node representation**. Write a **Java program to find the diameter** of the given binary tree and state the time and space complexity of your approach. *(8 Marks)*
* **Q9.** Write the **Quick Sort algorithm and a Java program** to sort an array in ascending order. Trace the partitioning/selection steps explicitly for the input $\{64, 25, 12, 22, 11\}$. *(8 Marks)*
* **Q10.** Differentiate between a **Stack and a Queue** based on their working principles and operations. Then write a **Java program using a Stack** to check whether a given expression has **balanced parentheses**. For the given input, determine whether the parentheses are balanced and display the result. *(8 Marks)*

```text
Input:
{[()]}
```