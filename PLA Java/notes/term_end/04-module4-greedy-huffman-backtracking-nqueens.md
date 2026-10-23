# 📘 Unit 4: Linear Data Structures, Stacks & Queues

> **Aligned with VIT Bhopal PLA1004 Syllabus & TEE Papers (Slots A11, B14, F11, E11, A21)**  
> **Exam Paper Mapping**:
> - **PART A**: **Question 4** (12 Marks — with internal choice `OR`)
> - **PART B**: **Question 9** (8 Marks — direct implementation)  
> **Total Unit Weight in TEE**: **Exactly 20 Marks**

---

# PART 1: SECTION A QUESTIONS (12 MARKS) [Question 4 Pool]

---

## 1. Singly Linked List: Basic Operations & Tail Pointer Impact
*(Paper 1 Q4a — 12 Marks)*

### Problem Statement:
Implement the basic operations of a singly linked list: insertion at the beginning, at the end, and at a given position; deletion of a node by value; and traversal. Trace the list after each operation and analyse the time complexity of each operation, including the effect of maintaining a tail pointer.

```java
class Node {
    int val;
    Node next;
    Node(int v) { this.val = v; }
}

public class SinglyLinkedListDemo {
    Node head = null, tail = null;

    // 1. Insertion at Beginning - O(1)
    public void insertBegin(int val) {
        Node newNode = new Node(val);
        if (head == null) {
            head = tail = newNode;
        } else {
            newNode.next = head;
            head = newNode;
        }
    }

    // 2. Insertion at End - O(1) with tail pointer, O(N) without
    public void insertEnd(int val) {
        Node newNode = new Node(val);
        if (head == null) {
            head = tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }
    }

    // 3. Insertion at Given Position (1-indexed) - O(N)
    public void insertAt(int val, int pos) {
        if (pos == 1) {
            insertBegin(val);
            return;
        }
        Node curr = head;
        for (int i = 1; i < pos - 1 && curr != null; i++) {
            curr = curr.next;
        }
        if (curr == null) return;

        Node newNode = new Node(val);
        newNode.next = curr.next;
        curr.next = newNode;
        if (newNode.next == null) {
            tail = newNode;
        }
    }

    // 4. Deletion by Value - O(N)
    public void delete(int val) {
        if (head == null) return;

        if (head.val == val) {
            head = head.next;
            if (head == null) tail = null;
            return;
        }

        Node curr = head;
        while (curr.next != null && curr.next.val != val) {
            curr = curr.next;
        }

        if (curr.next != null) {
            if (curr.next == tail) tail = curr;
            curr.next = curr.next.next;
        }
    }

    // 5. Traversal - O(N)
    public void printList() {
        Node curr = head;
        while (curr != null) {
            System.out.print(curr.val + (curr.next != null ? " -> " : ""));
            curr = curr.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        SinglyLinkedListDemo list = new SinglyLinkedListDemo();
        list.insertBegin(10);           System.out.print("insertBegin(10):          "); list.printList();
        list.insertEnd(20);             System.out.print("insertEnd(20):            "); list.printList();
        list.insertEnd(30);             System.out.print("insertEnd(30):            "); list.printList();
        list.insertAt(25, 3);           System.out.print("insertAt(25, pos 3):      "); list.printList();
        list.delete(20);                System.out.print("delete(20):               "); list.printList();
    }
}
```

#### Step-by-Step Execution Trace Output:
```text
insertBegin(10):          10
insertEnd(20):            10 -> 20
insertEnd(30):            10 -> 20 -> 30
insertAt(25, pos 3):      10 -> 20 -> 25 -> 30
delete(20):               10 -> 25 -> 30
```

#### Impact of Maintaining a Tail Pointer:
* **Insertion at End (`insertEnd`)**:
  - *Without Tail Pointer*: Must traverse all $N$ nodes from `head` to find the last node $\implies \mathbf{O(N)\text{ time}}$.
  - *With Tail Pointer*: Direct assignment `tail.next = newNode; tail = newNode;` $\implies \mathbf{O(1)\text{ time}}$.
* **Deletion at End (`deleteEnd`)**:
  - Still requires $\mathbf{O(N)}$ in a singly linked list because updating `tail` requires finding the second-to-last node, which can only be reached by scanning from `head`.

---

## 2. Reverse a Singly Linked List: Iterative vs Recursive
*(Paper 4 Q4ai — 6 Marks)*

### Problem Statement:
Reverse a given singly linked list using both the iterative approach ($O(1)$ space) and the recursive approach ($O(N)$ stack space).

```java
public class ReverseLinkedList {
    // 1. Iterative 3-pointer approach: O(N) time, O(1) space
    public static Node reverseIterative(Node head) {
        Node prev = null;
        Node curr = head;
        Node next = null;

        while (curr != null) {
            next = curr.next; // Store next node
            curr.next = prev; // Reverse current node's pointer
            prev = curr;      // Move prev one step ahead
            curr = next;      // Move curr one step ahead
        }
        return prev; // New head
    }

    // 2. Recursive approach: O(N) time, O(N) call stack space
    public static Node reverseRecursive(Node head) {
        if (head == null || head.next == null) {
            return head;
        }

        Node newHead = reverseRecursive(head.next);
        head.next.next = head; // Point next node back to current node
        head.next = null;      // Disconnect current node's original forward link

        return newHead;
    }

    public static void print(Node head) {
        Node c = head;
        while (c != null) {
            System.out.print(c.val + (c.next != null ? " -> " : ""));
            c = c.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // List: 1 -> 2 -> 3 -> 4 -> null
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);

        System.out.print("Original:           "); print(head);
        head = reverseIterative(head);
        System.out.print("Reversed Iterative: "); print(head);
        head = reverseRecursive(head);
        System.out.print("Reversed Back (Rec):"); print(head);
    }
}
```

#### Pointer Trace for Iterative Reversal on $1 \to 2 \to 3 \to \text{null}$:
| Step | `curr` | `next` (`curr.next`) | `curr.next = prev` | `prev` becomes | `curr` becomes |
|:---:|:---:|:---:|:---|:---:|:---:|
| **Init** | Node 1 | — | — | `null` | Node 1 |
| **1** | Node 1 | Node 2 | Node 1 points to `null` | Node 1 | Node 2 |
| **2** | Node 2 | Node 3 | Node 2 points to Node 1 | Node 2 | Node 3 |
| **3** | Node 3 | `null` | Node 3 points to Node 2 | Node 3 | `null` |
* Loop terminates. Return `prev` (Node 3) $\implies 3 \to 2 \to 1 \to \text{null}$.

---

## 3. Floyd's Cycle Detection & Loop Removal without Node Loss
*(Paper 4 Q4bi, Paper 5 Q4a — 12 Marks)*

### Problem Statement:
Detect if a loop exists in a singly linked list using Floyd's Tortoise and Hare algorithm. If a loop exists, remove the loop without losing any nodes. Trace the algorithm on $1 \to 2 \to 3 \to 4 \to 5 \to 6 \to 3$.

```java
public class FloydCycleDetectionAndRemoval {
    public static boolean detectAndRemoveLoop(Node head) {
        if (head == null || head.next == null) return false;

        Node slow = head;
        Node fast = head;

        // Phase 1: Detect if a cycle exists
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                // Cycle detected! Move to Phase 2: Find starting node of loop & remove
                removeLoop(head, slow);
                return true;
            }
        }
        return false;
    }

    private static void removeLoop(Node head, Node meetPoint) {
        Node p1 = head;
        Node p2 = meetPoint;

        // Special case: Loop starts at head node
        if (p1 == p2) {
            while (p2.next != p1) p2 = p2.next;
            p2.next = null; // Break loop
            return;
        }

        // Advance both 1 step at a time until next pointers meet
        while (p1.next != p2.next) {
            p1 = p1.next;
            p2 = p2.next;
        }

        // p2.next is the start of the loop; break the circular link
        p2.next = null;
    }

    public static void main(String[] args) {
        // Build list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 3
        Node head = new Node(1);
        head.next = new Node(2);
        Node loopStart = new Node(3);
        head.next.next = loopStart;
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);
        Node node6 = new Node(6);
        head.next.next.next.next.next = node6;
        node6.next = loopStart; // Loop created

        System.out.println("Loop detected and removed? " + detectAndRemoveLoop(head));

        System.out.print("List after removing loop: ");
        Node curr = head;
        while (curr != null) {
            System.out.print(curr.val + (curr.next != null ? " -> " : ""));
            curr = curr.next;
        }
        System.out.println();
    }
}
```

#### Step-by-Step Execution Trace on $1 \to 2 \to 3 \to 4 \to 5 \to 6 \to 3$:
1. **Phase 1 (Meeting Point)**:
   - Step 0: `slow = 1`, `fast = 1`
   - Step 1: `slow = 2`, `fast = 3`
   - Step 2: `slow = 3`, `fast = 5`
   - Step 3: `slow = 4`, `fast = 3` (from $5 \to 6 \to 3$)
   - Step 4: `slow = 5`, `fast = 5` (from $3 \to 4 \to 5$) $\implies$ **Collision at Node 5!**
2. **Phase 2 (Find Loop Start & Remove)**:
   - Reset `p1 = head = 1`, keep `p2 = meetPoint = 5`.
   - Check `p1.next (2) == p2.next (6)` $\implies$ No. Move `p1 = 2`, `p2 = 6`.
   - Check `p1.next (3) == p2.next (3)` $\implies$ **Match!** Both point to Node 3 (loop start).
   - Set `p2.next = null` (Node 6 `next` set to `null`).
   - Clean List Restored: $1 \to 2 \to 3 \to 4 \to 5 \to 6 \to \text{null}$.
* **Why Fast and Slow Must Meet**: Relative speed is $2 - 1 = 1$ node per step. The distance between them inside a cycle of length $C$ decreases by exactly 1 every iteration, guaranteeing a collision within at most $C$ steps.

---

## 4. Min Stack / Max Stack in $O(1)$ Time
*(Paper 1 Q4b, Paper 3 Q4a, Paper 4 Q4aii — 12 Marks)*

### Problem Statement:
Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum (or maximum) element, all in $O(1)$ time complexity.

### Design Approaches:
1. **Standard Two-Stack Design (Exam Recommended)**:
   - `mainStack` stores actual pushed values.
   - `auxStack` stores the current running min (or max).
   - When pushing $x$: push $x$ to `mainStack`, and push $\min(x, \text{auxStack.peek()})$ to `auxStack`.
   - When popping: pop from both stacks. `getMin()` returns `auxStack.peek()` in $O(1)$ time.
2. **Space-Optimized Single-Stack Design ($O(1)$ Extra Space)**:
   - Uses mathematical encoding: store $2x - \text{min}$ when a new minimum is pushed.

```java
import java.util.Stack;

public class MinStackTwoStack {
    private Stack<Integer> mainStack;
    private Stack<Integer> minStack;

    public MinStackTwoStack() {
        mainStack = new Stack<>();
        minStack = new Stack<>();
    }

    public void push(int val) {
        mainStack.push(val);
        if (minStack.isEmpty() || val <= minStack.peek()) {
            minStack.push(val);
        } else {
            minStack.push(minStack.peek());
        }
    }

    public void pop() {
        if (!mainStack.isEmpty()) {
            mainStack.pop();
            minStack.pop();
        }
    }

    public int top() {
        return mainStack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }

    public static void main(String[] args) {
        MinStackTwoStack s = new MinStackTwoStack();
        s.push(18);
        s.push(19);
        s.push(29);
        s.push(15);
        s.push(16);

        System.out.println("Top: " + s.top() + " | Min: " + s.getMin()); // Top: 16, Min: 15
        s.pop(); // Pop 16
        s.pop(); // Pop 15
        System.out.println("After 2 pops -> Top: " + s.top() + " | Min: " + s.getMin()); // Top: 29, Min: 18
    }
}
```

#### Evaluation Table for Design Choices:
| Approach | `push` Time | `pop` Time | `getMin` Time | Extra Space | Pros & Cons |
|:---|:---:|:---:|:---:|:---:|:---|
| **(i) Naive Stack Scanning** | $O(1)$ | $O(1)$ | $\mathbf{O(N)}$ | $\mathbf{O(1)}$ | Unacceptable: scanning $N$ elements on every `getMin()` |
| **(ii) Value-Min Pairs** | $O(1)$ | $O(1)$ | $\mathbf{O(1)}$ | $O(N)$ | Simple, but doubles object allocation memory |
| **(iii) Dual Stacks (Selected)** | $\mathbf{O(1)}$ | $\mathbf{O(1)}$ | $\mathbf{O(1)}$ | $O(N)$ | Standard, robust against integer overflow, clean code |
| **(iv) Arithmetic Encoding** | $\mathbf{O(1)}$ | $\mathbf{O(1)}$ | $\mathbf{O(1)}$ | $\mathbf{O(1)}$ | Zero extra space, but risks integer overflow on extreme values |

---

## 5. Next Greater Element (NGE) Using Monotonic Stack
*(Paper 4 Q4bii — 6 Marks)*

### Problem Statement:
Given an array, find the Next Greater Element (NGE) for every element. The Next Greater Element for an element $x$ is the first greater element on the right side in the array. If no greater element exists, output `-1`.

### Algorithmic Logic:
1. Traverse the array from **right to left** (index $N - 1$ down to $0$).
2. Maintain a **monotonic decreasing stack** of elements.
3. While stack is not empty and `stack.peek() <= arr[i]`, pop from stack (smaller elements can never be the next greater element for elements further left).
4. If stack is empty, `nge[i] = -1`; otherwise, `nge[i] = stack.peek()`.
5. Push current element `arr[i]` onto stack.

```java
import java.util.Stack;

public class NextGreaterElement {
    public static int[] findNGE(int[] arr) {
        int n = arr.length;
        int[] nge = new int[n];
        Stack<Integer> stack = new Stack<>();

        for (int i = n - 1; i >= 0; i--) {
            // Pop smaller or equal elements
            while (!stack.isEmpty() && stack.peek() <= arr[i]) {
                stack.pop();
            }

            // Stack top is the next greater element
            nge[i] = stack.isEmpty() ? -1 : stack.peek();

            // Push current element
            stack.push(arr[i]);
        }
        return nge;
    }

    public static void main(String[] args) {
        int[] arr = {4, 5, 2, 25};
        int[] result = findNGE(arr);
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i] + " -> " + result[i]);
        }
    }
}
```

#### Step-by-Step Execution Trace on $\{4, 5, 2, 25\}$:
| Index $i$ | `arr[i]` | Stack Before Pop | Popped Elements | `nge[i]` (Stack Top) | Stack After Push |
|:---:|:---:|:---|:---|:---:|:---|
| 3 | **25** | `[]` | None | **-1** | `[25]` |
| 2 | **2** | `[25]` | None ($25 > 2$) | **25** | `[25, 2]` |
| 1 | **5** | `[25, 2]` | `2` ($2 \le 5$) | **25** | `[25, 5]` |
| 0 | **4** | `[25, 5]` | None ($5 > 4$) | **5** | `[25, 5, 4]` |

* **Final Output**: `4 -> 5`, `5 -> 25`, `2 -> 25`, `25 -> -1`.
* **Complexities**: Time: $O(N)$ (each element pushed and popped at most once), Auxiliary Space: $O(N)$.

---

## 6. Stock Span Problem Using Monotonic Stack
*(Paper 5 Q4b — 12 Marks)*

### Problem Statement:
The span $S_i$ of the stock’s price on a given day $i$ is defined as the maximum number of consecutive days just before the given day, for which the price of the stock was less than or equal to its price on the current day. Compute the span for all days in $O(N)$ time.

```java
import java.util.Arrays;
import java.util.Stack;

public class StockSpanSolver {
    public static int[] calculateSpan(int[] price) {
        int n = price.length;
        int[] span = new int[n];
        Stack<Integer> stack = new Stack<>(); // Stores indices

        for (int i = 0; i < n; i++) {
            // Pop elements from stack while price is less than or equal to current price
            while (!stack.isEmpty() && price[stack.peek()] <= price[i]) {
                stack.pop();
            }

            // If stack is empty, price is greater than all previous elements
            span[i] = stack.isEmpty() ? (i + 1) : (i - stack.peek());

            // Push this day's index onto stack
            stack.push(i);
        }
        return span;
    }

    public static void main(String[] args) {
        // Paper 5 Q4b Test Case: {100, 80, 60, 70, 60, 75, 85}
        int[] prices = {100, 80, 60, 70, 60, 75, 85};
        int[] span = calculateSpan(prices);
        System.out.println("Prices: " + Arrays.toString(prices));
        System.out.println("Spans:  " + Arrays.toString(span));
    }
}
```

#### Step-by-Step Execution Trace on $\{100, 80, 60, 70, 60, 75, 85\}$:
| Day $i$ | Price | Stack Indices Before Pop | Action & Popped | Stack Top After Pop | Span ($i - \text{top}$) | Stack After Push |
|:---:|:---:|:---|:---|:---:|:---:|:---|
| 0 | **100** | `[]` | None | Empty | $0 + 1 = \mathbf{1}$ | `[0]` |
| 1 | **80** | `[0]` ($100$) | None | 0 | $1 - 0 = \mathbf{1}$ | `[0, 1]` |
| 2 | **60** | `[0, 1]` ($80$) | None | 1 | $2 - 1 = \mathbf{1}$ | `[0, 1, 2]` |
| 3 | **70** | `[0, 1, 2]` | Pop index 2 ($60 \le 70$) | 1 ($80$) | $3 - 1 = \mathbf{2}$ | `[0, 1, 3]` |
| 4 | **60** | `[0, 1, 3]` ($70$) | None | 3 | $4 - 3 = \mathbf{1}$ | `[0, 1, 3, 4]` |
| 5 | **75** | `[0, 1, 3, 4]` | Pop index 4 ($60$), Pop index 3 ($70$) | 1 ($80$) | $5 - 1 = \mathbf{4}$ | `[0, 1, 5]` |
| 6 | **85** | `[0, 1, 5]` | Pop index 5 ($75$), Pop index 1 ($80$) | 0 ($100$) | $6 - 0 = \mathbf{6}$ | `[0, 6]` |

* **Output Spans**: `[1, 1, 1, 2, 1, 4, 6]`.
* **Justification of $O(N)$ Time vs $O(N^2)$ Brute-Force**:
  - Brute-force checks leftwards for every day $i$, requiring $\sum_{i=1}^N i = O(N^2)$ worst-case comparisons.
  - With the stack, each element index is pushed exactly once and popped at most once across the entire algorithm, making total push/pop operations $\le 2N \implies \mathbf{O(N)\text{ amortized time}}$.

---

## 7. Quick Sort Algorithm & Partitioning Trace
*(Paper 2 Q4b — 12 Marks)*

### Problem Statement:
Write the Quick Sort algorithm and trace the partitioning process for the input array $\{3, 7, 8, 5, 2, 1, 9\}$.

```java
import java.util.Arrays;

public class QuickSortDemo {
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high]; // Last element as pivot
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return i + 1;
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;
    }

    public static void main(String[] args) {
        int[] arr = {3, 7, 8, 5, 2, 1, 9};
        System.out.println("Original: " + Arrays.toString(arr));
        quickSort(arr, 0, arr.length - 1);
        System.out.println("Sorted:   " + Arrays.toString(arr));
    }
}
```

* **Complexities**: Best/Average Time: $O(N \log N)$, Worst-Case Time: $O(N^2)$ (when array is already sorted and extreme pivot is chosen). Auxiliary Space: $O(\log N)$ recursion call stack.

---
---

# PART 2: SECTION B QUESTIONS (8 MARKS) [Question 9 Pool]

---

## 8. Sliding Window Minimum Using Monotonic Deque
*(Paper 1 Q9 — 8 Marks)*

### Problem Statement:
Find the minimum element in every contiguous window of size $K$ using a deque. Apply to $\{4, 2, 12, 3, 8, 1, 7, 9\}$ with $K = 3$ and show the deque contents for each window.

```java
import java.util.*;

public class SlidingWindowMinDeque {
    public static List<Integer> minSlidingWindow(int[] a, int k) {
        List<Integer> result = new ArrayList<>();
        Deque<Integer> dq = new LinkedList<>(); // Stores indices in increasing order of values

        for (int i = 0; i < a.length; i++) {
            // 1. Remove expired indices outside the current window
            while (!dq.isEmpty() && dq.peekFirst() <= i - k) {
                dq.pollFirst();
            }

            // 2. Remove elements from rear that are >= incoming element
            while (!dq.isEmpty() && a[dq.peekLast()] >= a[i]) {
                dq.pollLast();
            }

            dq.offerLast(i);

            // 3. Front of deque is the minimum for the current window
            if (i >= k - 1) {
                result.add(a[dq.peekFirst()]);
                System.out.printf("Window [%d..%d] -> Deque Indices: %s -> Min: %d\n",
                    i - k + 1, i, dq.toString(), a[dq.peekFirst()]);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int[] arr = {4, 2, 12, 3, 8, 1, 7, 9};
        int k = 3;
        List<Integer> mins = minSlidingWindow(arr, k);
        System.out.println("Final Sliding Window Minimums: " + mins);
    }
}
```

#### Step-by-Step Deque State Table on $\{4, 2, 12, 3, 8, 1, 7, 9\}$ with $K = 3$:
| Window Range | Incoming $a[i]$ | Deque Indices (Values) | Expired Removed | Window Minimum (`a[dq.front]`) |
|:---:|:---:|:---|:---:|:---:|
| `[0..2]` | $a[2] = 12$ | `[1, 2]` (`[2, 12]`) | — | **2** |
| `[1..3]` | $a[3] = 3$ | `[1, 3]` (`[2, 3]`) | $12 \ge 3$ popped from back | **2** |
| `[2..4]` | $a[4] = 8$ | `[3, 4]` (`[3, 8]`) | Index 1 expired (removed from front) | **3** |
| `[3..5]` | $a[5] = 1$ | `[5]` (`[1]`) | $8, 3 \ge 1$ popped from back | **1** |
| `[4..6]` | $a[6] = 7$ | `[5, 6]` (`[1, 7]`) | — | **1** |
| `[5..7]` | $a[7] = 9$ | `[5, 6, 7]` (`[1, 7, 9]`) | — | **1** |

* **Final Result**: `[2, 2, 3, 1, 1, 1]`.
* **Complexities**: Time: $O(N)$ (each index enters and leaves deque at most once), Auxiliary Space: $O(K)$.

---

## 9. Sliding Window Maximum Using Monotonic Deque
*(Paper 2 Q4a — 12M / Q9 — 8 Marks)*

```java
import java.util.*;

public class SlidingWindowMaxDeque {
    public static int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.length == 0 || k <= 0) return new int[0];
        int n = nums.length;
        int[] result = new int[n - k + 1];
        Deque<Integer> dq = new LinkedList<>(); // Stores indices in decreasing order of values

        for (int i = 0; i < n; i++) {
            // Remove indices out of current window
            while (!dq.isEmpty() && dq.peekFirst() <= i - k) {
                dq.pollFirst();
            }

            // Remove elements from back that are smaller than current element
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) {
                dq.pollLast();
            }

            dq.offerLast(i);

            // Front contains maximum of current window
            if (i >= k - 1) {
                result[i - k + 1] = nums[dq.peekFirst()];
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, -1, -3, 5, 3, 6, 7};
        int k = 3;
        System.out.println("Sliding Window Maximums: " + Arrays.toString(maxSlidingWindow(arr, k)));
    }
}
```

* **Complexities**: Time: $O(N)$, Auxiliary Space: $O(K)$.

---

## 10. In-Place Merge of Two Sorted Singly Linked Lists
*(Paper 2 Q9, Paper 3 Q9 — 8 Marks)*

### Problem Statement:
Merge two sorted singly linked lists into one sorted list in-place without creating a third list (reuse the existing nodes).

```java
public class InPlaceMergeLists {
    public static Node merge(Node l1, Node l2) {
        Node dummy = new Node(0); // Temporary anchor node
        Node tail = dummy;

        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                tail.next = l1;
                l1 = l1.next;
            } else {
                tail.next = l2;
                l2 = l2.next;
            }
            tail = tail.next;
        }

        // Attach remaining nodes directly
        tail.next = (l1 != null) ? l1 : l2;

        return dummy.next;
    }

    public static void main(String[] args) {
        // List 1: 1 -> 3 -> 5
        Node l1 = new Node(1); l1.next = new Node(3); l1.next.next = new Node(5);
        // List 2: 2 -> 4 -> 6
        Node l2 = new Node(2); l2.next = new Node(4); l2.next.next = new Node(6);

        Node merged = merge(l1, l2);
        System.out.print("Merged List: ");
        while (merged != null) {
            System.out.print(merged.val + (merged.next != null ? " -> " : ""));
            merged = merged.next;
        }
        System.out.println();
    }
}
```

* **Complexities**: Time: $O(N_1 + N_2)$, Auxiliary Space: $O(1)$ (strictly in-place link re-wiring).

---

## 11. Circular Queue Array Implementation
*(Paper 4 Q9 — 8 Marks)*

### Problem Statement:
Explain the working of a Circular Queue. Implement its `enqueue` and `dequeue` operations handling overflow and underflow correctly.

```java
public class CircularQueue {
    private int[] data;
    private int front, rear, size, capacity;

    public CircularQueue(int k) {
        this.capacity = k;
        this.data = new int[k];
        this.front = 0;
        this.rear = -1;
        this.size = 0;
    }

    public boolean enqueue(int value) {
        if (isFull()) {
            System.out.println("Overflow: Cannot enqueue " + value + ", queue is full!");
            return false;
        }
        rear = (rear + 1) % capacity;
        data[rear] = value;
        size++;
        return true;
    }

    public int dequeue() {
        if (isEmpty()) {
            System.out.println("Underflow: Cannot dequeue, queue is empty!");
            return -1;
        }
        int removed = data[front];
        front = (front + 1) % capacity;
        size--;
        return removed;
    }

    public boolean isEmpty() { return size == 0; }
    public boolean isFull() { return size == capacity; }

    public static void main(String[] args) {
        CircularQueue cq = new CircularQueue(3);
        cq.enqueue(10);
        cq.enqueue(20);
        cq.enqueue(30);
        cq.enqueue(40); // Demonstrates overflow

        System.out.println("Dequeued: " + cq.dequeue()); // 10
        cq.enqueue(40); // Wraps around circularly
        System.out.println("Dequeued: " + cq.dequeue()); // 20
    }
}
```

* **Complexities**: Time: $O(1)$ for both `enqueue` and `dequeue`; Space: $O(K)$.

---

## 12. First Negative Integer in Every Contiguous Window of Size $K$
*(Paper 5 Q9 — 8 Marks)*

### Problem Statement:
Find the first negative integer in every contiguous window of size $K$ of an array using a deque. Display $0$ if a window contains no negative integer.

```java
import java.util.*;

public class FirstNegativeInWindow {
    public static List<Integer> firstNegative(int[] arr, int k) {
        List<Integer> result = new ArrayList<>();
        Deque<Integer> dq = new LinkedList<>(); // Stores indices of negative integers

        for (int i = 0; i < arr.length; i++) {
            // Remove expired indices outside the current window
            while (!dq.isEmpty() && dq.peekFirst() <= i - k) {
                dq.pollFirst();
            }

            // Add index of incoming element if negative
            if (arr[i] < 0) {
                dq.offerLast(i);
            }

            // Record answer once the first window is formed
            if (i >= k - 1) {
                if (!dq.isEmpty()) {
                    result.add(arr[dq.peekFirst()]);
                } else {
                    result.add(0); // No negative integer in current window
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        // Paper 5 Q9: {12, -1, -7, 8, -15, 30, 16, 28}, K = 3
        int[] arr = {12, -1, -7, 8, -15, 30, 16, 28};
        int k = 3;
        List<Integer> ans = firstNegative(arr, k);
        System.out.println("First Negative in every window of size " + k + ": " + ans);
    }
}
```

#### Step-by-Step Deque State Table on $\{12, -1, -7, 8, -15, 30, 16, 28\}$ with $K = 3$:
| Window Range | Window Elements | Deque Indices (Values) | First Negative Output |
|:---:|:---|:---|:---:|
| `[0..2]` | `[12, -1, -7]` | `[1, 2]` (`[-1, -7]`) | **-1** |
| `[1..3]` | `[-1, -7, 8]` | `[1, 2]` (`[-1, -7]`) | **-1** |
| `[2..4]` | `[-7, 8, -15]` | `[2, 4]` (`[-7, -15]`) | **-7** |
| `[3..5]` | `[8, -15, 30]` | `[4]` (`[-15]`) | **-15** |
| `[4..6]` | `[-15, 30, 16]` | `[4]` (`[-15]`) | **-15** |
| `[5..7]` | `[30, 16, 28]` | `[]` (empty) | **0** |

* **Final Result**: `[-1, -1, -7, -15, -15, 0]`.
* **Complexities**: Time: $O(N)$, Auxiliary Space: $O(K)$.
