# 📘 Unit 3: Linear DSA, Sliding Window & String Algorithms

---

## 1. Linked List Patterns

### 1.1 Floyd's Cycle Detection & Cycle Starting Node
* **Detection**: Fast pointer moves 2 steps, slow pointer moves 1 step. If `fast == slow`, cycle exists.
* **Finding Entry Node**:
  - Distance from head to cycle start $= L$.
  - Distance from cycle start to meeting point $= k$.
  - When fast and slow meet, total distance by fast $= 2 \times \text{slow}$.
  - Reset `slow = head`; keep `fast` at meeting point. Move both **1 step at a time**. They meet at the **cycle start node**!

```java
public static ListNode detectCycleStart(ListNode head) {
    if (head == null || head.next == null) return null;
    ListNode slow = head, fast = head;
    boolean hasCycle = false;

    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) { hasCycle = true; break; }
    }
    if (!hasCycle) return null;

    slow = head;
    while (slow != fast) {
        slow = slow.next;
        fast = fast.next;
    }
    return slow; // Cycle start node
}
```

### 1.2 Remove $N$-th Node From End in One Pass
```java
public static ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode fast = dummy, slow = dummy;

    // Advance fast pointer by n + 1 steps
    for (int i = 0; i <= n; i++) fast = fast.next;

    // Move both until fast reaches end
    while (fast != null) {
        slow = slow.next;
        fast = fast.next;
    }
    // Delete target node
    slow.next = slow.next.next;
    return dummy.next;
}
```

---

## 2. Advanced Stack Patterns: Min Stack $O(1)$ Space

Stores min value along with encoded difference values $(2x - \text{min})$:
* When pushing value $x < \min$: Push $2x - \min$ into stack and update $\min = x$.
  - Note: Since $x < \min$, $2x - \min < x$. The stored value is strictly less than the new $\min$, serving as a flag!
* When popping: If top $< \min$, previous minimum was $2 \cdot \min - \text{top}$.

---

## 3. String Algorithms: In-Place Hyphen Shifting

Move all hyphens `'-'` to the beginning of the string in $O(N)$ time and $O(1)$ auxiliary space:
```java
public static String moveHyphensToBeginning(char[] str) {
    int n = str.length;
    int writeIdx = n - 1;

    // Process from right to left
    for (int i = n - 1; i >= 0; i--) {
        if (str[i] != '-') {
            str[writeIdx--] = str[i];
        }
    }
    // Fill remaining prefix with hyphens
    while (writeIdx >= 0) {
        str[writeIdx--] = '-';
    }
    return new String(str);
}
// Input: "Face-Prep-Java" -> Output "--FacePrepJava"
```

---

## 4. Manacher's Algorithm for Longest Palindromic Substring ($O(N)$)

Transforms string with boundary delimiters (e.g., `"aba"` $\to$ `"^#a#b#a#$"`) to handle even and odd palindromes uniformly.
* Maintains center $C$ and rightmost boundary $R$ of the current palindrome.
* For index $i < R$, uses mirror index $i' = 2C - i$:
  $$P[i] = \min(R - i, P[i'])$$
* Expands beyond $R$ only when necessary, yielding guaranteed linear $O(N)$ runtime.

---

## 5. Model Exam Questions & Answers

### Question 1 (12 Marks)
**Explain the Sliding Window Maximum problem. Write the optimal Java code using a Monotonic Deque and dry-run it for array $[1, 3, -1, -3, 5, 3, 6, 7]$ with $k = 3$.**

**Solution**:
1. **Algorithm Logic**:
   - Maintain a deque of indices such that elements corresponding to these indices are in strictly descending order.
   - For each element $A[i]$: Remove indices smaller than $i - k + 1$ (out of window); pop smaller elements from the back of the deque; push index $i$. The front of the deque always contains the window maximum.
2. **Dry-Run Trace Table**:

| Index $i$ | Element $A[i]$ | Deque Content (Indices) | Window Range | Window Max ($A[\text{peekFirst}]$) |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | $[0]$ | — | — |
| 1 | 3 | $[1]$ (1 popped) | — | — |
| 2 | -1 | $[1, 2]$ | $[1, 3, -1]$ | **3** |
| 3 | -3 | $[1, 2, 3]$ | $[3, -1, -3]$ | **3** |
| 4 | 5 | $[4]$ (all popped) | $[-1, -3, 5]$ | **5** |
| 5 | 3 | $[4, 5]$ | $[-3, 5, 3]$ | **5** |
| 6 | 6 | $[6]$ (all popped) | $[5, 3, 6]$ | **6** |
| 7 | 7 | $[7]$ (all popped) | $[3, 6, 7]$ | **7** |

* Final Result Array: **$[3, 3, 5, 5, 6, 7]$**. Time: $O(N)$, Space: $O(K)$.

### Question 2 (8 Marks)
**Prove why Floyd's Cycle-Finding Algorithm guarantees detection of a loop in a Linked List. What is the time complexity?**

**Solution**:
1. **Proof**:
   - Let the loop have length $C$. Once both fast and slow pointers enter the loop, fast is behind slow by some distance $d < C$.
   - In every clock step, fast moves 2 nodes and slow moves 1 node. The relative distance decreases by $2 - 1 = 1$ node per step.
   - Since the relative distance decreases by exactly 1 in each step, the distance must eventually reach $0$. Fast and slow are guaranteed to collide in at most $C$ iterations after slow enters the loop.
2. **Complexity**: Time $= O(N)$ (where $N$ is total nodes), Auxiliary Space $= O(1)$ (only two pointers).
