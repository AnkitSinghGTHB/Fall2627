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

---

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

---

**Q3.**
* **(a)** Write the algorithm and Java program to solve the Josephus Problem for $n$ people standing in a circle where every $k$-th person is eliminated, and display the complete elimination order of all $n$ people. Trace your solution for $n = 8$ and $k = 3$ and analyse the time complexity of a list-based simulation. *(6 Marks)*
* **(b)** Given the start and finish times of $N$ meetings, write the algorithm and Java program to find the minimum number of meeting rooms required so that no two overlapping meetings share a room, using a greedy approach. Trace your solution for the meetings $(0,30)$, $(5,10)$, $(8,12)$, $(15,20)$ and $(25,35)$ and analyse the time complexity. *(6 Marks)*

**OR**

* **(c)** Given a string $S$, write the algorithm and Java program to rearrange its characters to form the lexicographically largest palindrome possible. If no palindromic arrangement exists, output $-1$. Trace your solution for $S =$ `"aabbbcc"` and $S =$ `"abcd"`, and analyse the time and space complexity of your approach. *(12 Marks)*

---

**Q4.**
* **(a)** Write a Java program to implement the basic operations of a singly linked list: insertion at the beginning, at the end and at a given position; deletion of a node by value; and traversal. Trace the list after each of the operations `insertBegin(10)`, `insertEnd(20)`, `insertEnd(30)`, `insertAt(25, position 3)` and `delete(20)`, and analyse the time complexity of each operation, including the effect of maintaining a tail pointer. *(12 Marks)*

**OR**

* **(b)** Design a stack that supports `push`, `pop`, `top` and retrieval of the maximum element, all in $O(1)$ time (Max Stack), and write the Java program to implement it. Evaluate your design against (i) scanning the stack for the maximum on every query and (ii) storing (value, current maximum) pairs, in terms of time and space, and justify the design you choose. *(12 Marks)*

---

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
---

# Paper 2: Slot B14+D21 (21-10-2026/S-2)

## PART A – (60 Marks)

**Q1.**
* **(a)** Write a Java program to Move all Hyphens to the Beginning of a given string while preserving the relative character order of the non-hyphen characters. *(12 Marks)*

**OR**

* **(b)** Write the algorithm and Java program to identify whether a given number string is a Strobogrammatic Number (looks the same when rotated $180$ degrees). *(12 Marks)*

---

**Q2.**
* **(a)** Write a Java program to find the Height of a Binary Tree (number of nodes on the longest path from root to leaf), along with its algorithm. *(7 Marks)*
* **(b)** Write a Java program that reads three numbers and uses nested conditional operators / if-else ladders to find the largest number, demonstrating relational and logical operators. *(5 Marks)*

**OR**

* **(c)** Write a Java program to isolate and swap the lower and upper nibbles of an $8$-bit byte variable using bitwise shift and mask operations. *(12 Marks)*

---

**Q3.**
* **(a)** Write the algorithm and Java program to solve the Josephus Problem. Given $n$ people standing in a circle and every $k$-th person eliminated, determine the position of the survivor. Trace your solution for $n = 8$ and $k = 4$. *(6 Marks)*
* **(b)** Write the algorithm and Java program for the Activity Selection Problem using a greedy approach. Select the maximum number of non-overlapping activities based on their start and finish times. *(6 Marks)*

**OR**

* **(c)** Write a formal algorithmic description and a recursive Java program to accurately calculate the Height of a Binary Tree, measuring the maximum edge or node depth extending from the root node down to the deepest leaf node. *(12 Marks)*

---

**Q4.**
* **(a)** Write a Java program to find the maximum element in every contiguous subarray of size $K$ using the Sliding Window Maximum technique with a deque. *(12 Marks)*

**OR**

* **(b)** Write the Quick Sort algorithm and a Java program to sort an array in ascending order. Trace the partitioning process for the input $\{3, 7, 8, 5, 2, 1, 9\}$. *(12 Marks)*

---

**Q5.**
* **(a)** Write a dynamic programming-based Java program equipped with memorization techniques to solve the Maneuvering Problem, accurately calculating the total number of unique paths from the top-left corner to the bottom-right corner of an $M \times N$ grid. *(12 Marks)*

**OR**

* **(b)** Write a Java program using a stack to check whether an expression contains balanced parentheses. Consider `()`, `{}`, and `[]`. *(6 Marks)*
* **(c)** Analyze the following code snippet to determine its time and space complexity. Trace its execution with input matrix of size $3 \times 3$. *(6 Marks)*
```java
int maxSum = Integer.MIN_VALUE;
for(int i=0; i < n - 2; i++) { // Note: loop conditions reconstructed from standard hourglass snippet
    for(int j=0; j < m - 2; j++) {
        int sum = mat[i][j]+mat[i][j+1]+mat[i][j+2]+mat[i+1][j+1]+mat[i+2][j]+mat[i+2][j+1]+mat[i+2][j+2];
        if(sum > maxSum) maxSum = sum;
    }
}
```
*(Exact printed line in paper: `for(int i=0; i for(int j=0; j int sum = mat[i][j]+...`)*

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
---

# Paper 3: Slot F11+F12 (18-10-2026/S-2)

## PART A – (60 Marks)

**Q1.**
* **(a)** Write the algorithm and Java program to compute the Euler's Phi ($\phi$) Algorithm value for a given integer $n$. *(12 Marks)*

**OR**

* **(b)** Write the algorithm and Java program to identify whether a given number string is a Strobogrammatic Number (looks the same when rotated $180$ degrees). *(12 Marks)*

---

**Q2.**
* **(a)** Write a Java program to find the Diameter of a Binary Tree (the length of the longest path between any two nodes), along with its algorithm. *(7 Marks)*
* **(b)** Write a Java program that reads an operator character and two operands to implement a basic calculator using a switch-case control structure, demonstrating control flow and branching. *(5 Marks)*

**OR**

* **(c)** Write a Java program to find the Maximum Product Subarray in a given integer array using an optimized linear scan. *(12 Marks)*

---

**Q3.**
* **(a)** Write the algorithm and Java program to implement Huffman Coding to generate prefix codes for a set of characters based on their frequencies. Trace your solution for a small frequency set. *(6 Marks)*
* **(b)** Write the algorithm and Java program for the Activity Selection Problem using a greedy approach. Select the maximum number of non-overlapping activities based on their start and finish times. *(6 Marks)*

**OR**

* **(c)** Write the Selection Sort algorithm and a Java program to sort an array in ascending order. Trace the selection and swapping process for the input $\{64, 25, 12, 22, 11\}$. *(12 Marks)*

---

**Q4.**
* **(a)** Write a Java program to implement a Min Stack supporting `push`, `pop`, `top`, and retrieving the minimum element in $O(1)$ time. *(12 Marks)*

**OR**

* **(b)** Write a Java program to find the Longest Sequence of $1\text{s}$ after flipping a single $0$ to a $1$ in a given binary array or bit string. *(12 Marks)*

---

**Q5.**
* **(a)** Write a dynamic programming-based Java program equipped with memorization techniques to solve the Maneuvering Problem, accurately calculating the total number of unique paths from the top-left corner to the bottom-right corner of an $M \times N$ grid. *(12 Marks)*

**OR**

* **(b)** Write a Java program using a stack to check whether an expression contains balanced parentheses. Consider `()`, `{}`, and `[]`. *(6 Marks)*
* **(c)** Analyze the following code snippet to determine its time and space complexity. Trace its execution with input matrix of size $3 \times 3$. *(6 Marks)*
```java
int maxSum = Integer.MIN_VALUE;
for(int i=0; i for(int j=0; j int sum = 
mat[i][j]+mat[i][j+1]+mat[i][j+2]+mat[i+1][j+1]+mat[i+2][j]+mat[i+2][j+1]+mat[i+2][j+2];
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

---

**Q2.**
* **(a)** Given an array of integers, an Equilibrium Index $i$ is one where the sum of elements at indices less than $i$ equals the sum of elements at indices greater than $i$. Write an efficient (non-brute-force) algorithm and code to find the maximum equilibrium sum among all equilibrium indices. *(7 Marks)*
* **(b)** Trace your solution for the array $\{-7, 1, 5, 2, -4, 3, 0\}$ and analyse the time and space complexity of your approach. *(5 Marks)*

**OR**

* **(c)** Write the algorithm and code to swap the two nibbles (the upper $4$ bits and the lower $4$ bits) of a given byte ($8$-bit number) using bitwise operators. *(12 Marks)*

---

**Q3.**
* **(a)** Explain the N-Queens problem and describe how backtracking is used to solve it. Illustrate your explanation with a worked example for $N = 4$, and write the code to print all possible solutions. *(6 Marks)*
* **(b)** The Huffman codes assigned to five symbols are: $A = 0$, $B = 10$, $C = 110$, $D = 1110$, $E = 1111$. Given the encoded bit string `'11101100101111'`, explain step by step how you would use the Huffman codes to decode the original sequence of symbols. (Only explain the decoding algorithm/steps clearly with the working — code is not required.) *(6 Marks)*

**OR**

* **(c)** Given a string $S$ of length $N$ consisting of lowercase English letters and an integer $K$, the weight of a character is its position in the alphabet ($a = 1, b = 2, \dots, z = 26$), and the weight of a substring is the sum of the weights of its characters. Write an efficient algorithm and code, to find the maximum weight among all substrings of $S$ having length exactly $K$, and report that substring. Trace your solution step by step for $S =$ `"abcadeaf"` and $K = 3$, and analyse the time and space complexity of your approach. *(12 Marks)*

---

**Q4.**
* **(a)** 
  * **(i)** Write the algorithm and code to reverse a given singly linked list, using both the iterative and the recursive approach.
  * **(ii)** Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element, all in $O(1)$ time complexity. Explain your approach and write the code to implement this Min Stack. *(12 Marks)*

**OR**

* **(b)** 
  * **(i)** Write the algorithm and code to detect the presence of a cycle in a singly linked list using Floyd's Cycle Detection (Tortoise and Hare) algorithm.
  * **(ii)** Write the algorithm and code to find the Next Greater Element for every element of a given array using a stack. *(12 Marks)*

---

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