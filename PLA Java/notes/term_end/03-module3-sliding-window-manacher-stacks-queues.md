# 📘 Unit 3: Linear DSA, Sliding Window & String Algorithms

> **Aligned with VIT Bhopal October 2026 TEE Papers**: Slots A11, B14, F11, E11  
> **Unit Weight in TEE**: Exactly 20 Marks (12M in Section A + 8M in Section B)

---

## 1. Linked List Patterns

### 1.1 Singly Linked List: Basic Operations & Tail Pointer Impact
*(Paper 1 Q4a — 12 Marks)*

* **Operations**: Insertion (beginning, end, given position), deletion by value, traversal.
* **Impact of Maintaining a Tail Pointer**:
  - *Without Tail Pointer*: `insertEnd()` requires traversing all $N$ nodes from `head` to find the last node $\implies \mathbf{O(N)\text{ time}}$.
  - *With Tail Pointer*: Direct access via `tail.next = newNode; tail = newNode;` $\implies \mathbf{O(1)\text{ time}}$.
  - Note: `deleteEnd()` remains $O(N)$ even with a tail pointer in a singly linked list because updating `tail` requires finding the second-to-last node.

```java
class Node {
    int val;
    Node next;
    Node(int v) { this.val = v; }
}

public class SinglyLinkedList {
    Node head = null, tail = null;

    public void insertBegin(int val) {
        Node newNode = new Node(val);
        if (head == null) { head = tail = newNode; }
        else { newNode.next = head; head = newNode; }
    }

    public void insertEnd(int val) {
        Node newNode = new Node(val);
        if (head == null) { head = tail = newNode; }
        else { tail.next = newNode; tail = newNode; }
    }

    public void insertAt(int val, int pos) { // 1-indexed
        if (pos == 1) { insertBegin(val); return; }
        Node curr = head;
        for (int i = 1; i < pos - 1 && curr != null; i++) curr = curr.next;
        if (curr == null) return;
        Node newNode = new Node(val);
        newNode.next = curr.next;
        curr.next = newNode;
        if (newNode.next == null) tail = newNode;
    }

    public void delete(int val) {
        if (head == null) return;
        if (head.val == val) {
            head = head.next;
            if (head == null) tail = null;
            return;
        }
        Node curr = head;
        while (curr.next != null && curr.next.val != val) curr = curr.next;
        if (curr.next != null) {
            if (curr.next == tail) tail = curr;
            curr.next = curr.next.next;
        }
    }

    public void print() {
        Node c = head;
        while (c != null) { System.out.print(c.val + (c.next != null ? " -> " : "")); c = c.next; }
        System.out.println();
    }

    public static void main(String[] args) {
        SinglyLinkedList list = new SinglyLinkedList();
        list.insertBegin(10);           System.out.print("insertBegin(10): "); list.print();
        list.insertEnd(20);             System.out.print("insertEnd(20):   "); list.print();
        list.insertEnd(30);             System.out.print("insertEnd(30):   "); list.print();
        list.insertAt(25, 3);           System.out.print("insertAt(25, 3):  "); list.print();
        list.delete(20);                System.out.print("delete(20):       "); list.print();
    }
}
```
**Execution Trace Output**:
```text
insertBegin(10): 10
insertEnd(20):   10 -> 20
insertEnd(30):   10 -> 20 -> 30
insertAt(25, 3):  10 -> 20 -> 25 -> 30
delete(20):       10 -> 25 -> 30
```

---

### 1.2 In-Place Merge of Two Sorted Singly Linked Lists
*(Paper 2 Q9 & Paper 3 Q9 — 8 Marks)*

Reuses existing node pointers without allocating any new nodes:
```java
public class InPlaceMergeLists {
    public static Node merge(Node l1, Node l2) {
        Node dummy = new Node(0);
        Node curr = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                curr.next = l1; l1 = l1.next;
            } else {
                curr.next = l2; l2 = l2.next;
            }
            curr = curr.next;
        }
        curr.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }
}
// Time Complexity: O(M + N), Space Complexity: O(1)
```

---

### 1.3 Reverse Singly Linked List (Iterative & Recursive)
*(Paper 4 Q4a-i — 6 Marks)*

* **Iterative ($O(1)$ Space)**:
```java
public static Node reverseIterative(Node head) {
    Node prev = null, curr = head;
    while (curr != null) {
        Node next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}
```
* **Recursive ($O(N)$ Space due to Call Stack)**:
```java
public static Node reverseRecursive(Node head) {
    if (head == null || head.next == null) return head;
    Node newHead = reverseRecursive(head.next);
    head.next.next = head;
    head.next = null;
    return newHead;
}
```

---

## 2. Advanced Stack Patterns

### 2.1 Max Stack / Min Stack in $O(1)$ Time
*(Paper 1 Q4b, Paper 3 Q4a, Paper 4 Q4a-ii — 12 Marks)*

#### Evaluation of Alternative Designs:
1. **Scanning Stack on Every Query**: $O(1)$ push/pop, but `getMax()` requires traversing all $N$ elements $\implies O(N)$ time. Inefficient for frequent queries.
2. **Storing `(value, currentMax)` Pairs**: Pushing `(x, Math.max(x, currentMax))` gives $O(1)$ for all queries, but doubles memory consumption to $O(N)$ extra space.
3. **Arithmetic Encoding in Single Stack ($O(1)$ Extra Space - RECOMMENDED)**:
   - For **Max Stack**:
     - When pushing $x > \max$: push encoded flag $2x - \max$ to stack; update $\max = x$.
     - When popping: if $\text{top} > \max \implies$ previous maximum was $2\max - \text{top}$.
   - For **Min Stack**:
     - When pushing $x < \min$: push encoded flag $2x - \min$ to stack; update $\min = x$.
     - When popping: if $\text{top} < \min \implies$ previous minimum was $2\min - \text{top}$.

```java
import java.util.Stack;

public class MaxStackConstantSpace {
    private Stack<Long> stack = new Stack<>();
    private long max;

    public void push(int val) {
        long x = val;
        if (stack.isEmpty()) {
            stack.push(x);
            max = x;
        } else if (x > max) {
            stack.push(2 * x - max); // Encoded flag: strictly greater than new max!
            max = x;
        } else {
            stack.push(x);
        }
    }

    public void pop() {
        if (stack.isEmpty()) return;
        long top = stack.pop();
        if (top > max) {
            max = 2 * max - top; // Restore previous max
        }
    }

    public int top() {
        long top = stack.peek();
        return (top > max) ? (int) max : (int) top;
    }

    public int getMax() {
        return (int) max;
    }

    public static void main(String[] args) {
        MaxStackConstantSpace ms = new MaxStackConstantSpace();
        ms.push(3); ms.push(5); ms.push(2); ms.push(9);
        System.out.println("Max: " + ms.getMax()); // 9
        ms.pop(); // pops 9
        System.out.println("Max after pop: " + ms.getMax()); // 5
    }
}
```

---

### 2.2 Next Greater Element (NGE) Using Monotonic Stack
*(Paper 4 Q4b-ii — 6 Marks)*

```java
import java.util.*;

public class NextGreaterElement {
    public static int[] nextGreater(int[] arr) {
        int n = arr.length;
        int[] nge = new int[n];
        Stack<Integer> stack = new Stack<>();

        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() <= arr[i]) {
                stack.pop();
            }
            nge[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(arr[i]);
        }
        return nge;
    }

    public static void main(String[] args) {
        int[] arr = {4, 5, 2, 25};
        System.out.println("NGE: " + Arrays.toString(nextGreater(arr))); // [5, 25, 25, -1]
    }
}
```

---

### 2.3 Balanced Parentheses Check
*(Paper 2 Q5b & Paper 3 Q5b — 6 Marks)*

```java
import java.util.Stack;

public class BalancedParentheses {
    public static boolean isBalanced(String expr) {
        Stack<Character> stack = new Stack<>();
        for (char c : expr.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') stack.push(c);
            else if (c == ')' || c == '}' || c == ']') {
                if (stack.isEmpty()) return false;
                char top = stack.pop();
                if ((c == ')' && top != '(') || (c == '}' && top != '{') || (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
```

---

## 3. Sliding Window & Queue Patterns

### 3.1 Sliding Window Minimum with Deque Contents Trace
*(Paper 1 Q9 — 8 Marks)*

Given array $A = \{4, 2, 12, 3, 8, 1, 7, 9\}$ and window size $K = 3$:
* Maintain a **monotonic increasing deque** storing indices.

#### Execution Trace Table for $\{4, 2, 12, 3, 8, 1, 7, 9\}$ with $K = 3$:

| Index $i$ | Element $A[i]$ | Indices in Deque | Values in Deque | Window Range | Window Min ($A[\text{peekFirst}]$) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 4 | $[0]$ | $[4]$ | — | — |
| 1 | 2 | $[1]$ (0 popped) | $[2]$ | — | — |
| 2 | 12 | $[1, 2]$ | $[2, 12]$ | $[4, 2, 12]$ | **2** |
| 3 | 3 | $[1, 3]$ (2 popped) | $[2, 3]$ | $[2, 12, 3]$ | **2** |
| 4 | 8 | $[3, 4]$ (1 out of window) | $[3, 8]$ | $[12, 3, 8]$ | **3** |
| 5 | 1 | $[5]$ (all popped) | $[1]$ | $[3, 8, 1]$ | **1** |
| 6 | 7 | $[5, 6]$ | $[1, 7]$ | $[8, 1, 7]$ | **1** |
| 7 | 9 | $[5, 6, 7]$ | $[1, 7, 9]$ | $[1, 7, 9]$ | **1** |

* **Final Output Array**: **$[2, 2, 3, 1, 1, 1]$**. Time: $O(N)$, Auxiliary Space: $O(K)$.

---

### 3.2 Circular Queue Implementation Using Array
*(Paper 4 Q9 — 8 Marks; Priority Topic 14)*

* **Overflow Condition**: `(rear + 1) % capacity == front`
* **Underflow Condition**: `front == -1`
* **Enqueue**: `rear = (rear + 1) % capacity; arr[rear] = val;`
* **Dequeue**: If `front == rear` $\implies$ reset `front = rear = -1`; else `front = (front + 1) % capacity`.

```java
public class CircularQueue {
    private int[] arr;
    private int front, rear, capacity;

    public CircularQueue(int k) {
        capacity = k;
        arr = new int[k];
        front = rear = -1;
    }

    public boolean enqueue(int val) {
        if ((rear + 1) % capacity == front) {
            System.out.println("Overflow! Queue is full");
            return false;
        }
        if (front == -1) front = 0;
        rear = (rear + 1) % capacity;
        arr[rear] = val;
        return true;
    }

    public int dequeue() {
        if (front == -1) {
            System.out.println("Underflow! Queue is empty");
            return -1;
        }
        int val = arr[front];
        if (front == rear) front = rear = -1;
        else front = (front + 1) % capacity;
        return val;
    }
}
```

---

## 4. String Algorithms

### 4.1 Move Hyphens to Beginning in $O(1)$ Space
*(Paper 2 Q1a — 12 Marks)*

```java
public class MoveHyphens {
    public static String moveHyphens(char[] s) {
        int n = s.length;
        int writeIdx = n - 1;
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] != '-') s[writeIdx--] = s[i];
        }
        while (writeIdx >= 0) s[writeIdx--] = '-';
        return new String(s);
    }

    public static void main(String[] args) {
        char[] str = "Face-Prep-Java".toCharArray();
        System.out.println("Result: " + moveHyphens(str)); // --FacePrepJava
    }
}
```

---

### 4.2 Lexicographically Largest / Smallest Palindrome Rearrangement
*(Paper 1 Q3c & Paper 4 Q8 — 8 to 12 Marks)*

Rearrange string characters to form the lexicographically largest or smallest palindrome. If impossible (more than 1 odd frequency), return `-1`.

```java
public class PalindromeRearrangement {
    public static String largestPalindrome(String s) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) freq[c - 'a']++;

        int oddCount = 0;
        char oddChar = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] % 2 != 0) {
                oddCount++;
                oddChar = (char) ('a' + i);
            }
        }
        if (oddCount > 1) return "-1"; // Not possible

        // For largest palindrome: iterate from 'z' down to 'a'
        StringBuilder half = new StringBuilder();
        for (int i = 25; i >= 0; i--) {
            for (int k = 0; k < freq[i] / 2; k++) {
                half.append((char) ('a' + i));
            }
        }

        String rightHalf = new StringBuilder(half).reverse().toString();
        return (oddCount == 1) ? half.toString() + oddChar + rightHalf : half.toString() + rightHalf;
    }

    public static void main(String[] args) {
        System.out.println("aabbbcc: " + largestPalindrome("aabbbcc")); // cbababc
        System.out.println("abcd:    " + largestPalindrome("abcd"));    // -1
    }
}
```
**Sample Output**:
```text
aabbbcc: cbababc
abcd:    -1
```

---

### 4.3 Block Swap Algorithm for Array Left Rotation by $d$
*(Paper 4 Q7 — 8 Marks; Priority Topic 12)*

```java
public class BlockSwapRotation {
    public static void rotate(int[] arr, int d, int n) {
        d = d % n;
        if (d == 0) return;
        rotateRec(arr, 0, d, n);
    }

    private static void rotateRec(int[] arr, int i, int d, int n) {
        if (d == 0 || d == n) return;
        if (n - d == d) { swap(arr, i, i + d, d); return; }
        if (d < n - d) {
            swap(arr, i, i + n - d, d);
            rotateRec(arr, i, d, n - d);
        } else {
            swap(arr, i, i + d, n - d);
            rotateRec(arr, i + n - d, 2 * d - n, d);
        }
    }

    private static void swap(int[] arr, int fi, int si, int d) {
        for (int k = 0; k < d; k++) {
            int t = arr[fi + k]; arr[fi + k] = arr[si + k]; arr[si + k] = t;
        }
    }
}
// Time Complexity: O(N), Space Complexity: O(1)
```
