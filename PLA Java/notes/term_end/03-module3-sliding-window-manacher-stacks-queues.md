# 📘 Unit 3: Linear DSA, Sliding Window & String Algorithms

---

## 1. Linked List Patterns

### 1.1 Floyd's Cycle Detection & Cycle Starting Node
*(Priority Topic 8 — `LinkedList_Problems.pptx`)*

* **Detection**: Fast pointer moves 2 steps, slow pointer moves 1 step. If `fast == slow`, cycle exists.
* **Finding Entry Node**:
  - Distance from head to cycle start $= L$.
  - Distance from cycle start to meeting point $= k$.
  - When fast and slow meet, total distance by fast $= 2 \times \text{slow}$.
  - Reset `slow = head`; keep `fast` at meeting point. Move both **1 step at a time**. They meet at the **cycle start node**!

```java
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

public class LinkedListCycle {
    public static ListNode detectCycleStart(ListNode head) {
        if (head == null || head.next == null) return null;
        ListNode slow = head, fast = head;
        boolean hasCycle = false;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                hasCycle = true;
                break;
            }
        }
        if (!hasCycle) return null;

        slow = head;
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }
        return slow; // Loop starting node
    }

    public static void main(String[] args) {
        ListNode n1 = new ListNode(1);
        ListNode n2 = new ListNode(2);
        ListNode n3 = new ListNode(3);
        ListNode n4 = new ListNode(4);
        n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n2; // Loop back to 2

        ListNode cycleStart = detectCycleStart(n1);
        System.out.println("Cycle starts at node: " + (cycleStart != null ? cycleStart.val : "No cycle"));
    }
}
```
**Sample Input**: Linked list `1 -> 2 -> 3 -> 4 -> (points back to 2)`  
**Sample Output**:
```text
Cycle starts at node: 2
```

---

### 1.2 Remove $N$-th Node From End of List (Single Pass)
*(Tested in Sample Paper, Q6 with $N=2$)*

```java
public class RemoveNthEnd {
    public static ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode fast = dummy, slow = dummy;

        // Move fast ahead by n + 1 steps
        for (int i = 0; i <= n; i++) {
            if (fast == null) return head;
            fast = fast.next;
        }

        // Move both until fast reaches the end
        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }
        slow.next = slow.next.next;
        return dummy.next;
    }

    public static void printList(ListNode head) {
        ListNode curr = head;
        while (curr != null) {
            System.out.print(curr.val + (curr.next != null ? " -> " : ""));
            curr = curr.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        System.out.print("Original list: ");
        printList(head);
        head = removeNthFromEnd(head, 2);
        System.out.print("After removing 2nd from end: ");
        printList(head);
    }
}
```
**Sample Input**: `1 -> 2 -> 3 -> 4 -> 5`, $N = 2$  
**Sample Output**:
```text
Original list: 1 -> 2 -> 3 -> 4 -> 5
After removing 2nd from end: 1 -> 2 -> 3 -> 5
```

---

## 2. Advanced Stack & Queue Patterns

### 2.1 Min-Stack with $O(1)$ Extra Space (Arithmetic Encoding)
*(Priority Topic 7 — `Stack_Problems.pptx`, Sample Paper Q4)*

Stores min value along with encoded difference values $(2x - \text{min})$:
* When pushing value $x < \min$: Push $2x - \min$ into stack and update $\min = x$.
  - Note: Since $x < \min$, $2x - \min < x$. The stored value is strictly less than the new $\min$, serving as a recovery flag!
* When popping: If top $< \min$, previous minimum was $2 \cdot \min - \text{top}$.

```java
import java.util.Stack;

public class MinStackConstantSpace {
    private Stack<Long> stack = new Stack<>();
    private long min;

    public void push(int val) {
        long x = val;
        if (stack.isEmpty()) {
            stack.push(x);
            min = x;
        } else if (x < min) {
            stack.push(2 * x - min);
            min = x;
        } else {
            stack.push(x);
        }
    }

    public void pop() {
        if (stack.isEmpty()) return;
        long top = stack.pop();
        if (top < min) {
            min = 2 * min - top; // Restore previous min
        }
    }

    public int top() {
        long top = stack.peek();
        return (top < min) ? (int) min : (int) top;
    }

    public int getMin() {
        return (int) min;
    }

    public static void main(String[] args) {
        MinStackConstantSpace ms = new MinStackConstantSpace();
        ms.push(5);
        ms.push(3);
        ms.push(7);
        ms.push(2);
        System.out.println("Current Min: " + ms.getMin()); // 2
        ms.pop();
        System.out.println("Min after popping 2: " + ms.getMin()); // 3
        System.out.println("Top element: " + ms.top()); // 7
    }
}
```
**Sample Output**:
```text
Current Min: 2
Min after popping 2: 3
Top element: 7
```

---

### 2.2 Circular Queue Implementation Using Array
*(Priority Topic 14 — `CircularQueue_SlidingWindow.pptx`)*

Wrap-around arithmetic using modulo `% capacity`:
- Full condition: `(rear + 1) % capacity == front`
- Empty condition: `front == -1`

```java
public class CircularQueue {
    private int[] arr;
    private int front, rear, size, capacity;

    public CircularQueue(int k) {
        capacity = k;
        arr = new int[k];
        front = -1;
        rear = -1;
        size = 0;
    }

    public boolean enQueue(int value) {
        if (isFull()) return false;
        if (isEmpty()) front = 0;
        rear = (rear + 1) % capacity;
        arr[rear] = value;
        size++;
        return true;
    }

    public boolean deQueue() {
        if (isEmpty()) return false;
        if (front == rear) {
            front = -1;
            rear = -1;
        } else {
            front = (front + 1) % capacity;
        }
        size--;
        return true;
    }

    public int Front() { return isEmpty() ? -1 : arr[front]; }
    public int Rear() { return isEmpty() ? -1 : arr[rear]; }
    public boolean isEmpty() { return size == 0; }
    public boolean isFull() { return size == capacity; }

    public static void main(String[] args) {
        CircularQueue q = new CircularQueue(3);
        q.enQueue(10);
        q.enQueue(20);
        q.enQueue(30);
        System.out.println("Enqueued 10, 20, 30. Is full? " + q.isFull());
        q.deQueue();
        q.enQueue(40);
        System.out.println("Front: " + q.Front() + ", Rear: " + q.Rear());
    }
}
```
**Sample Output**:
```text
Enqueued 10, 20, 30. Is full? true
Front: 20, Rear: 40
```

---

### 2.3 Sliding Window Maximum using Monotonic Deque
*(Tested in Unit 3 Question — `CircularQueue_SlidingWindow.pptx`)*

```java
import java.util.*;

public class SlidingWindowMax {
    public static int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || k <= 0) return new int[0];
        int n = nums.length;
        int[] result = new int[n - k + 1];
        Deque<Integer> deque = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            while (!deque.isEmpty() && deque.peekFirst() < i - k + 1) {
                deque.pollFirst();
            }
            while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i]) {
                deque.pollLast();
            }
            deque.offerLast(i);

            if (i >= k - 1) {
                result[i - k + 1] = nums[deque.peekFirst()];
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, -1, -3, 5, 3, 6, 7};
        int k = 3;
        System.out.println("Sliding Window Max: " + Arrays.toString(maxSlidingWindow(arr, k)));
    }
}
```
**Sample Input**: `nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3`  
**Sample Output**:
```text
Sliding Window Max: [3, 3, 5, 5, 6, 7]
```

---

## 3. String & Array Algorithms

### 3.1 Move Hyphens to Beginning in $O(1)$ Space
*(Sample Paper, Q1)*

```java
public class MoveHyphens {
    public static String moveHyphensToBeginning(char[] str) {
        int n = str.length;
        int writeIdx = n - 1;

        // Process from right to left
        for (int i = n - 1; i >= 0; i--) {
            if (str[i] != '-') {
                str[writeIdx--] = str[i];
            }
        }
        // Fill front with hyphens
        while (writeIdx >= 0) {
            str[writeIdx--] = '-';
        }
        return new String(str);
    }

    public static void main(String[] args) {
        char[] s = "Face-Prep-Java".toCharArray();
        System.out.println("Result: " + moveHyphensToBeginning(s));
    }
}
```
**Sample Input**: `"Face-Prep-Java"`  
**Sample Output**:
```text
Result: --FacePrepJava
```

---

### 3.2 Equilibrium Index of an Array
*(Priority Topic 2)*

Index where sum of elements at lower indices equals sum at higher indices:
$$\sum_{j=0}^{i-1} A[j] = \sum_{j=i+1}^{n-1} A[j]$$

```java
public class EquilibriumPoint {
    public static int findEquilibrium(int[] arr) {
        int totalSum = 0;
        for (int x : arr) totalSum += x;

        int leftSum = 0;
        for (int i = 0; i < arr.length; i++) {
            // totalSum - leftSum - arr[i] is the right sum
            if (leftSum == totalSum - leftSum - arr[i]) {
                return i;
            }
            leftSum += arr[i];
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {-7, 1, 5, 2, -4, 3, 0};
        System.out.println("Equilibrium index: " + findEquilibrium(arr));
    }
}
```
**Sample Input**: `[-7, 1, 5, 2, -4, 3, 0]`  
**Sample Output**:
```text
Equilibrium index: 3
```
*(At index 3, element 2: Left sum = -7 + 1 + 5 = -1; Right sum = -4 + 3 + 0 = -1).*

---

### 3.3 Block Swap Algorithm for Array Rotation
*(Priority Topic 12)*

Rotates array `arr` by $d$ positions in $O(N)$ time and $O(1)$ space by recursively swapping blocks of size $d$ and $n-d$:

```java
import java.util.Arrays;

public class BlockSwapRotation {
    public static void rotate(int[] arr, int d, int n) {
        d = d % n;
        if (d == 0) return;
        rotateRec(arr, 0, d, n);
    }

    private static void rotateRec(int[] arr, int i, int d, int n) {
        if (d == 0 || d == n) return;

        // If A and B have equal length
        if (n - d == d) {
            swap(arr, i, i + d, d);
            return;
        }

        // If A is shorter
        if (d < n - d) {
            swap(arr, i, i + n - d, d);
            rotateRec(arr, i, d, n - d);
        } else { // If B is shorter
            swap(arr, i, i + d, n - d);
            rotateRec(arr, i + n - d, 2 * d - n, d);
        }
    }

    private static void swap(int[] arr, int fi, int si, int d) {
        for (int k = 0; k < d; k++) {
            int temp = arr[fi + k];
            arr[fi + k] = arr[si + k];
            arr[si + k] = temp;
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        rotate(arr, 2, arr.length);
        System.out.println("Rotated by 2: " + Arrays.toString(arr));
    }
}
```
**Sample Input**: `[1, 2, 3, 4, 5, 6, 7]`, $d = 2$  
**Sample Output**:
```text
Rotated by 2: [3, 4, 5, 6, 7, 1, 2]
```

---

### 3.4 Run-Length Encoding and Decoding
*(Priority Topic 10)*

```java
public class StringEncodeDecode {
    public static String encode(String s) {
        if (s == null || s.isEmpty()) return "";
        StringBuilder sb = new StringBuilder();
        int count = 1;
        for (int i = 1; i <= s.length(); i++) {
            if (i < s.length() && s.charAt(i) == s.charAt(i - 1)) {
                count++;
            } else {
                sb.append(s.charAt(i - 1)).append(count);
                count = 1;
            }
        }
        return sb.toString();
    }

    public static String decode(String s) {
        StringBuilder sb = new StringBuilder();
        int i = 0;
        while (i < s.length()) {
            char ch = s.charAt(i++);
            int num = 0;
            while (i < s.length() && Character.isDigit(s.charAt(i))) {
                num = num * 10 + (s.charAt(i++) - '0');
            }
            for (int k = 0; k < num; k++) sb.append(ch);
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        String original = "aaabbccccd";
        String encoded = encode(original);
        String decoded = decode(encoded);
        System.out.println("Encoded: " + encoded);
        System.out.println("Decoded: " + decoded);
    }
}
```
**Sample Input**: `"aaabbccccd"`  
**Sample Output**:
```text
Encoded: a3b2c4d1
Decoded: aaabbccccd
```
