# ⚡ CAT-2 HOTS Master Crib — Module 3: Linear DSA, Strings, Stacks & Queues
**Course**: Competitive Coding Practices (PLA1006 / PLA1004) — VIT Bhopal  
**Coverage**: Hyphen Shifting, Lexicographically First Palindrome, Weighted Substrings, Manacher's Algorithm, Linked Lists (Reverse, Detect/Remove Loop, Merge), Stacks (Parentheses, Next Greater Element, Min Stack), Queues (Circular Queue, Sliding Window Max, Josephus)  
**Source Alignment**: Official VIT Bhopal / FacePrep Lecture PPTs (L28, L29, L30, L34, LinkedList, Stack, CircularQueue) & Internal Assessment  
**Exam Mode**: Open Book / Notes Allowed | **Target**: S-Grade (45+ / 50)

---

## 🧱 TIER 0: The "Explain Like I'm 5" Bedrock Basics

### 1. The 3 Core Data Structures at a Glance
* **Linked List**: Train cars hooked together by coupling chains (`head.next`). If you break a chain, you lose the rest of the train!
  - *Iterative Reverse*: You flip the coupling chains one by one using 3 fingers (`prev`, `curr`, `next`).
  - *Floyd's Loop Rule*: If the tracks loop in a circle, a fast runner at speed $2$ and a slow runner at speed $1$ **must crash into each other**. Reset one runner to the station (head) and make both run at speed $1$; they will collide **exactly at the loop junction switch**!
* **Stack (LIFO — Last In, First Out)**: A stack of dinner plates in a cafeteria.
  - You can only put a plate on the top (`push`) or remove the top plate (`pop`).
  - Perfect for matching parentheses (open bracket = put plate, close bracket = take matching plate off).
  - *Min Stack*: A stack where a magic label on the side always tells you the smallest plate currently in the stack in $O(1)$ time.
* **Queue (FIFO — First In, First Out)**: A ticket counter queue. First person in line gets served first.
  - *Circular Queue*: When people leave the front, the empty spots are reused by wrapping around (`(rear + 1) % capacity`), eliminating wasted memory!
  - *Monotonic Deque*: An eviction rule queue for sliding windows. If a newcomer is both *younger* and *bigger* than old members, all smaller old members are kicked out from the back!

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If the Exam Question Asks... | Use This Exact Topic & Method | Time & Space Complexity | Key Formula / Code Logic |
| :--- | :--- | :--- | :--- |
| "Move hyphen to beginning" | **String Partition / Counting** | $O(n)$ Time, $O(1)$ Extra Space | Count hyphens, fill front with `'-'`, copy letters |
| "Lexicographically first palindrome" | **Frequency Array + 3-Part Build** | $O(n)$ Time, $O(1)$ Space (26 chars) | At most 1 odd frequency allowed; mirror left half |
| "Shortest string of target weight", $A=1, B=2A+A$ | **Precomputed Weights + Binary Search Floor** | $O(\log 26)$ Time, $O(1)$ Space | `values[i] = (i+1)*prev + prev`, greedy largest character |
| "Longest palindromic substring in O(n)" | **Manacher's Algorithm** | $O(n)$ Time, $O(n)$ Space | Pad with `@#a#b#c#$`, LPS array $L[i]$, mirror $2C - i$ |
| "Reverse a linked list (Iterative & Recursive)" | **3-Pointer / Call Stack Reversal** | $O(n)$ Time, $O(1)$ Iter / $O(n)$ Recur | `next = curr.next; curr.next = prev; prev = curr; curr = next;` |
| "Detect and remove loop in linked list" | **Floyd's Tortoise & Hare** | $O(n)$ Time, $O(1)$ Space | `slow = slow.next; fast = fast.next.next;` break at loop start |
| "Merge two sorted linked lists" | **Dummy Node Splice / Recursive** | $O(n_1 + n_2)$ Time, $O(1)$ Space | Pick smaller `val`, attach to `tail.next`, advance |
| "Check balanced parentheses", `()[]{}` | **Stack Character Matching** | $O(n)$ Time, $O(n)$ Space | Push open; on close, check if stack empty or mismatch |
| "Next Greater Element (NGE)" | **Monotonic Decreasing Stack** | $O(n)$ Time, $O(n)$ Space | Traverse right-to-left, pop $\le curr$, top is NGE |
| "Min Stack in O(1) time" | **Two Stacks OR $2x - min$ Math** | $O(1)$ Ops, $O(1)$ Extra Space | Store $2x - min$ when new min is pushed |
| "Implement Circular Queue" | **Modulo Circular Array** | $O(1)$ Ops, $O(N)$ Space | `front`, `rear`, `(rear + 1) % N == front` (full check) |
| "Maximum in each sliding window of size k" | **Monotonic Deque (LC 239)** | $O(n)$ Time, $O(k)$ Space | Pop smaller from back, pop expired from front |
| "Longest substring without repeating characters" | **Flexible Sliding Window (LC 3)** | $O(n)$ Time, $O(\min(m, n))$ Space | `left = Math.max(left, lastSeen[c] + 1); maxLen = Math.max(...)` |
| "Smallest subarray with sum >= S" | **Dynamic Sliding Window (LC 209)** | $O(n)$ Time, $O(1)$ Space | Expand right; while `sum >= S`: `minLen = min(...)`, shrink left |
| "Longest substring with at most K distinct characters" | **Flexible Frequency Window** | $O(n)$ Time, $O(K)$ Space | Expand right; while `distinct > K`: decrement `left`, shrink |
| "Max consecutive 1s after flipping at most K zeros" | **Flexible Zero-Count Window (LC 1004)** | $O(n)$ Time, $O(1)$ Space | While `zeroCount > K`: if `nums[left] == 0` `zeroCount--`, `left++` |
| "Reverse linked list in K-groups" | **K-Group Iterative Reversal (LC 25)** | $O(n)$ Time, $O(1)$ Space | Verify $K$ nodes exist; reverse $K$ links; connect `prevGroup.next` |
| "Check if linked list is palindrome in O(1) space" | **Fast/Slow + In-Place Reversal** | $O(n)$ Time, $O(1)$ Space | Find middle with fast/slow; reverse 2nd half; compare halves |
| "Intersection point of two linked lists (Y-shape)" | **Two-Pointer Head Swap Trick** | $O(A + B)$ Time, $O(1)$ Space | `pA = (pA == null) ? headB : pA.next` (meet at intersection) |
| "Reorder linked list (L0 -> Ln -> L1 -> Ln-1)" | **Split + Reverse + Interleave** | $O(n)$ Time, $O(1)$ Space | Find mid, reverse 2nd half, alternately weave nodes |
| "Josephus execution circle", $n$ people, step $k$ | **Josephus Recurrence** | $O(n)$ Time, $O(1)$ Space | $J(n, k) = (J(n-1, k) + k - 1) \pmod n + 1$ (1-indexed) |

---

## 🛠️ TIER 2: Master Code Templates (Lecture PPT & Exam Aligned)

### 1. Move Hyphen to Beginning (`L29-Move hyphen to beginning.pptx`)
> **Problem**: Reposition all hyphens in a string to the front.  
> **Example**: `"face-prep"` $\to$ `"-faceprep"`, `"a-b-c-d"` $\to$ `"---abcd"`.

```java
public class MoveHyphen {
    // Approach 1: In-place char array / Two-pointer (Most efficient: O(n) time, O(1) auxiliary space)
    public static String moveHyphenToBeginning(String str) {
        if (str == null || str.length() == 0) return str;
        char[] arr = str.toCharArray();
        int n = arr.length;
        int writeIndex = n - 1;

        // Traverse right to left, copying non-hyphen characters to the end
        for (int i = n - 1; i >= 0; i--) {
            if (arr[i] != '-') {
                arr[writeIndex--] = arr[i];
            }
        }
        // Fill remaining front positions with hyphens
        while (writeIndex >= 0) {
            arr[writeIndex--] = '-';
        }
        return new String(arr);
    }

    // Approach 2: Faculty PPT Method (Using StringBuilder / substring)
    public static String moveSingleHyphen(String string) {
        if (string.contains("-")) {
            int hyphenIndex = string.indexOf("-");
            return "-" + string.substring(0, hyphenIndex) + string.substring(hyphenIndex + 1);
        }
        return string;
    }
}
```

---

### 2. Lexicographically First Palindromic String
> **Problem**: Rearrange characters of string $s$ to form the lexicographically smallest palindrome. If impossible, return `"No Palindromic String"`.  
> **Example**: `"malayalam"` $\to$ `"aallmllaa"` (or `"aalmymlaa"`), `"bba"` $\to$ `"bab"`.

```java
public class LexicographicallyFirstPalindrome {
    public static String findFirstPalindrome(String s) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }

        int oddCount = 0;
        char oddChar = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] % 2 != 0) {
                oddCount++;
                oddChar = (char) (i + 'a');
            }
        }

        // A valid palindrome can have at most one odd-frequency character
        if (oddCount > 1) {
            return "No Palindromic String";
        }

        // Build first half lexicographically (from 'a' to 'z')
        StringBuilder firstHalf = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < freq[i] / 2; j++) {
                firstHalf.append((char) (i + 'a'));
            }
        }

        StringBuilder secondHalf = new StringBuilder(firstHalf).reverse();
        if (oddCount == 1) {
            return firstHalf.toString() + oddChar + secondHalf.toString();
        } else {
            return firstHalf.toString() + secondHalf.toString();
        }
    }
}
```

---

### 3. Weighted Substring (`L28- Weightes substring.pptx`)
> **Problem**: Every English letter has weight:
> $$A = 1, \quad B = 2A + A = 3, \quad C = 3B + B = 12, \quad \dots \quad \text{values}[i] = (i + 1) \cdot \text{prev} + \text{prev}$$
> Given target weight $k$ ($1 \le k \le 10^{16}$), determine the **shortest string** of that weight. If multiple, return the **lexicographically smallest**.  
> **Sample**: $k = 20 \implies$ Output: `AABBC` (or reverse printed greedily).

```java
import java.util.*;

public class WeightedSubstring {
    static long[] values = new long[26];

    // Precompute weights: values[0]=1, values[i] = (i + 1) * prev + prev
    public static void insertValues() {
        values[0] = 1;
        long prev = 1;
        for (int i = 1; i < 26; i++) {
            values[i] = (long) (i + 1) * prev + prev;
            prev = values[i];
        }
    }

    // Binary search to find floor (largest character weight <= k)
    public static int findFloor(long k, int low, int high) {
        int ans = -1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (values[mid] <= k) {
                ans = mid;
                low = mid + 1; // Try to find larger valid character
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }

    // Constructs shortest, lexicographically smallest string
    public static String formedString(long k) {
        insertValues();
        List<Character> list = new ArrayList<>();

        while (k != 0) {
            int ind = findFloor(k, 0, 25);
            list.add((char) (ind + 'A'));
            k = k - values[ind];
        }

        // Print in reverse order to ensure lexicographically smallest
        StringBuilder sb = new StringBuilder();
        for (int i = list.size() - 1; i >= 0; i--) {
            sb.append(list.get(i));
        }
        return sb.toString();
    }
}
```

---

### 4. Manacher's Algorithm (`L30-Manacher_s Algorithm.pptx`)
> **Problem**: Find the longest palindromic substring in $O(n)$ time.  
> **Concept**: Transform string $s$ of length $N$ into $T = @\#s_0\#s_1\# \dots \#\$$ of length $2N + 3$. Exploit palindrome symmetry with center $C$ and right boundary $R$:
> $$\text{mirror} = 2C - i, \quad L[i] = (R > i) \ ? \ \min(R - i, L[\text{mirror}]) : 0$$

```java
public class ManachersAlgorithm {
    public static String longestPalindromicSubstring(String text) {
        if (text == null || text.length() == 0) return "";
        int N = text.length();

        // Transform string: "aba" -> "@#a#b#a#$"
        char[] T = new char[2 * N + 3];
        T[0] = '@';
        T[T.length - 1] = '$';
        int idx = 1;
        for (int i = 0; i < N; i++) {
            T[idx++] = '#';
            T[idx++] = text.charAt(i);
        }
        T[idx] = '#';

        int[] L = new int[T.length]; // Palindrome radius array
        int C = 0, R = 0;
        int maxLen = 0, maxCenter = 0;

        for (int i = 1; i < T.length - 1; i++) {
            int iMirror = 2 * C - i;
            if (R > i) {
                L[i] = Math.min(R - i, L[iMirror]);
            }

            // Expand around center i
            while (T[i + 1 + L[i]] == T[i - 1 - L[i]]) {
                L[i]++;
            }

            // Update center and boundary if expanded beyond R
            if (i + L[i] > R) {
                C = i;
                R = i + L[i];
            }

            // Track longest palindrome
            if (L[i] > maxLen) {
                maxLen = L[i];
                maxCenter = i;
            }
        }

        // Map back to original string indices
        int start = (maxCenter - maxLen) / 2;
        return text.substring(start, start + maxLen);
    }
}
```

---

### 5. Linked List Suite (`LinkedList_Problems.pptx`)
Includes: (a) Reverse LL (Iterative & Recursive), (b) Detect & Remove Loop, (c) Merge Sorted Lists.

```java
public class LinkedListMaster {
    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    // 1a. Reverse Linked List - Iterative (O(n) time, O(1) space)
    public static ListNode reverseIterative(ListNode head) {
        ListNode prev = null, curr = head;
        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }

    // 1b. Reverse Linked List - Recursive (O(n) time, O(n) space)
    public static ListNode reverseRecursive(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode newHead = reverseRecursive(head.next);
        head.next.next = head;
        head.next = null;
        return newHead;
    }

    // 2. Detect & Remove Loop (Floyd's Algorithm: O(n) time, O(1) space)
    public static void detectAndRemoveLoop(ListNode head) {
        if (head == null || head.next == null) return;
        ListNode slow = head, fast = head;

        // Step 1: Detect collision
        boolean hasLoop = false;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                hasLoop = true;
                break;
            }
        }
        if (!hasLoop) return;

        // Step 2: Find start node of the loop
        slow = head;
        if (slow == fast) { // Loop starts at head
            while (fast.next != slow) fast = fast.next;
            fast.next = null;
            return;
        }
        while (slow.next != fast.next) {
            slow = slow.next;
            fast = fast.next;
        }
        // Step 3: Break the loop
        fast.next = null;
    }

    // 3. Merge Two Sorted Lists - Iterative (O(n1 + n2) time, O(1) space)
    public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;

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
        tail.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }

    // 4. Remove N-th Node From End of List - One Pass (O(n) time, O(1) space)
    // Direct solution to Sample Paper 1 Question 5(b)
    public static ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode fast = dummy;
        ListNode slow = dummy;

        // Advance fast by n + 1 steps to create gap
        for (int i = 0; i <= n; i++) {
            if (fast == null) return head;
            fast = fast.next;
        }

        // Move both until fast reaches end
        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }

        // Delete target node
        slow.next = slow.next.next;
        return dummy.next;
    }
}
```

#### 5.1 High-Yield Linked List Variations for CAT-2

```java
import java.util.*;

public class LinkedListVariationsMaster {
    public static class ListNode {
        public int val;
        public ListNode next;
        public ListNode(int val) { this.val = val; }
    }

    // VARIATION A: Reverse Nodes in k-Group (LeetCode 25)
    // Reverses nodes in chunks of k. Leaves remaining < k nodes untouched.
    // Complexity: O(n) Time, O(1) Auxiliary Space
    public static ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k <= 1) return head;

        // Step 1: Check if there are at least k nodes remaining
        ListNode curr = head;
        int count = 0;
        while (curr != null && count < k) {
            curr = curr.next;
            count++;
        }
        if (count < k) return head; // Base case: fewer than k nodes remain

        // Step 2: Reverse first k nodes
        ListNode prev = null;
        curr = head;
        for (int i = 0; i < k; i++) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        // Step 3: head is now the tail of this reversed group; connect to next group
        head.next = reverseKGroup(curr, k);
        return prev; // prev is the new head of this reversed k-group
    }

    // VARIATION B: Check If Linked List is a Palindrome in O(1) Space
    // Complexity: O(n) Time, O(1) Space
    public static boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;

        // Step 1: Find middle using Slow and Fast pointers
        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Step 2: Reverse second half starting from slow.next
        ListNode secondHalfHead = reverseList(slow.next);

        // Step 3: Compare first half and reversed second half
        ListNode p1 = head, p2 = secondHalfHead;
        boolean palindrome = true;
        while (p2 != null) {
            if (p1.val != p2.val) {
                palindrome = false;
                break;
            }
            p1 = p1.next;
            p2 = p2.next;
        }

        // Step 4: Restore original list structure
        slow.next = reverseList(secondHalfHead);
        return palindrome;
    }

    private static ListNode reverseList(ListNode node) {
        ListNode prev = null, curr = node;
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    // VARIATION C: Intersection Point of Two Linked Lists (Y-Shaped List)
    // Elegant Two-Pointer Trick: Pointer A traverses A then B; Pointer B traverses B then A.
    // Both travel exactly Length(A) + Length(B) steps, meeting at intersection or null!
    // Complexity: O(m + n) Time, O(1) Space
    public static ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;
        ListNode pA = headA, pB = headB;

        while (pA != pB) {
            pA = (pA == null) ? headB : pA.next;
            pB = (pB == null) ? headA : pB.next;
        }
        return pA; // Either points to intersection node or null (no intersection)
    }

    // VARIATION D: Reorder List (Fold List: L0 -> Ln -> L1 -> Ln-1 -> L2 ...)
    // Complexity: O(n) Time, O(1) Space
    public static void reorderList(ListNode head) {
        if (head == null || head.next == null) return;

        // 1. Split list into two halves
        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode second = slow.next;
        slow.next = null; // Sever connection

        // 2. Reverse second half
        second = reverseList(second);

        // 3. Merge alternately
        ListNode first = head;
        while (second != null) {
            ListNode temp1 = first.next;
            ListNode temp2 = second.next;
            first.next = second;
            second.next = temp1;
            first = temp1;
            second = temp2;
        }
    }

    // VARIATION E: Merge K Sorted Linked Lists
    // Complexity: O(N log k) Time where N is total nodes, O(k) Space for Min-Heap
    public static ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> Integer.compare(a.val, b.val));

        for (ListNode node : lists) {
            if (node != null) pq.offer(node);
        }

        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (!pq.isEmpty()) {
            ListNode smallest = pq.poll();
            tail.next = smallest;
            tail = tail.next;
            if (smallest.next != null) {
                pq.offer(smallest.next);
            }
        }
        return dummy.next;
    }
}
```

---

### 6. Stack Problems Suite (`Stack_Problems.pptx`)
Includes: (a) Balanced Parentheses, (b) Next Greater Element, (c) Min Stack (Both Approaches).

```java
import java.util.*;

public class StackMaster {
    // 1. Balanced Parentheses: O(n) time, O(n) space
    public static boolean isValidParentheses(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) return false;
                char top = stack.pop();
                if (c == ')' && top != '(') return false;
                if (c == '}' && top != '{') return false;
                if (c == ']' && top != '[') return false;
            }
        }
        return stack.isEmpty();
    }

    // 2. Next Greater Element (NGE): O(n) time, O(n) space
    public static int[] nextGreaterElement(int[] arr) {
        int n = arr.length;
        int[] nge = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();

        // Traverse right to left
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() <= arr[i]) {
                stack.pop();
            }
            nge[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(arr[i]);
        }
        return nge;
    }

    // 3a. Min Stack - Approach 1: Two Stacks (Simple & robust)
    static class MinStackTwoStacks {
        private Deque<Integer> stack = new ArrayDeque<>();
        private Deque<Integer> minStack = new ArrayDeque<>();

        public void push(int val) {
            stack.push(val);
            if (minStack.isEmpty() || val <= minStack.peek()) {
                minStack.push(val);
            }
        }

        public void pop() {
            int popped = stack.pop();
            if (popped == minStack.peek()) {
                minStack.pop();
            }
        }

        public int top() { return stack.peek(); }
        public int getMin() { return minStack.peek(); }
    }

    // 3b. Min Stack - Approach 2: Optimal Space (Single Stack with 2x - min math)
    static class MinStackOptimal {
        private Deque<Long> stack = new ArrayDeque<>();
        private long min;

        public void push(int x) {
            if (stack.isEmpty()) {
                stack.push((long) x);
                min = x;
            } else if (x >= min) {
                stack.push((long) x);
            } else {
                stack.push(2L * x - min); // Store encoded value
                min = x;
            }
        }

        public void pop() {
            long popped = stack.pop();
            if (popped < min) {
                min = 2 * min - popped; // Restore previous min
            }
        }

        public int top() {
            long topVal = stack.peek();
            return (int) (topVal < min ? min : topVal);
        }

        public int getMin() { return (int) min; }
    }
}
```

---

### 7. Circular Queue & Sliding Window Max (`CircularQueue_SlidingWindow.pptx`)

```java
import java.util.*;

public class QueueAndSlidingWindow {
    // 1. Circular Queue Complete Implementation (Modulo Arithmetic)
    static class CircularQueue {
        private int[] data;
        private int front, rear, size, capacity;

        public CircularQueue(int k) {
            this.capacity = k;
            this.data = new int[k];
            this.front = -1;
            this.rear = -1;
            this.size = 0;
        }

        public boolean enQueue(int value) {
            if (isFull()) return false;
            if (isEmpty()) front = 0;
            rear = (rear + 1) % capacity;
            data[rear] = value;
            size++;
            return true;
        }

        public boolean deQueue() {
            if (isEmpty()) return false;
            if (front == rear) { // Reset on empty
                front = -1;
                rear = -1;
            } else {
                front = (front + 1) % capacity;
            }
            size--;
            return true;
        }

        public int Front() { return isEmpty() ? -1 : data[front]; }
        public int Rear() { return isEmpty() ? -1 : data[rear]; }
        public boolean isEmpty() { return size == 0; }
        public boolean isFull() { return size == capacity; }
    }

    // 2. Sliding Window Maximum using Monotonic Deque: O(n) time, O(k) space
    public static int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || k <= 0) return new int[0];
        int n = nums.length;
        int[] res = new int[n - k + 1];
        int ri = 0;
        Deque<Integer> dq = new ArrayDeque<>(); // Stores indices

        for (int i = 0; i < n; i++) {
            // Remove out-of-window indices
            while (!dq.isEmpty() && dq.peekFirst() < i - k + 1) dq.pollFirst();
            // Evict smaller elements from back
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();

            dq.offerLast(i);
            if (i >= k - 1) res[ri++] = nums[dq.peekFirst()];
        }
        return res;
    }
}
```

#### 7.1 High-Yield Flexible (Variable-Size) Sliding Window Suite for CAT-2

> **Fixed vs. Flexible Window**: While fixed sliding window (like LC 239) has a constant size $K$, **Flexible Sliding Window** expands dynamically with a `right` pointer and conditionally shrinks with a `left` pointer to find the longest/shortest subarray satisfying a constraint.

```java
import java.util.*;

public class FlexibleSlidingWindowMaster {

    // ARCHETYPE 1: Longest Substring Without Repeating Characters (LeetCode 3)
    // Dynamic window: expand right; if duplicate seen, jump left past its previous position.
    // Complexity: O(n) Time, O(1) Space (ASCII 128 array)
    public static int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) return 0;
        int[] lastSeen = new int[128];
        Arrays.fill(lastSeen, -1);

        int maxLen = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (lastSeen[c] >= left) {
                // Duplicate found within current window: jump left past previous occurrence
                left = lastSeen[c] + 1;
            }
            lastSeen[c] = right;
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }

    // ARCHETYPE 2: Minimum Size Subarray Sum >= S (LeetCode 209)
    // Dynamic window: expand right until sum >= target, then shrink left to find MINIMUM length.
    // Complexity: O(n) Time, O(1) Space
    public static int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int minLen = Integer.MAX_VALUE;
        int currentSum = 0;
        int left = 0;

        for (int right = 0; right < n; right++) {
            currentSum += nums[right];

            // Contract window as much as possible while sum >= target
            while (currentSum >= target) {
                minLen = Math.min(minLen, right - left + 1);
                currentSum -= nums[left++];
            }
        }
        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }

    // ARCHETYPE 3: Longest Substring with At Most K Distinct Characters
    // Dynamic window: expand right, tracking character frequency counts.
    // Shrink left whenever unique character count exceeds K.
    // Complexity: O(n) Time, O(K) Auxiliary Map Space
    public static int lengthOfLongestSubstringKDistinct(String s, int k) {
        if (s == null || s.length() == 0 || k <= 0) return 0;
        Map<Character, Integer> freq = new HashMap<>();
        int maxLen = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char in = s.charAt(right);
            freq.put(in, freq.getOrDefault(in, 0) + 1);

            // Constraint violated: more than K distinct characters in window
            while (freq.size() > k) {
                char out = s.charAt(left);
                freq.put(out, freq.get(out) - 1);
                if (freq.get(out) == 0) {
                    freq.remove(out);
                }
                left++;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }

    // ARCHETYPE 4: Max Consecutive Ones III / At Most K Zero Flips (LeetCode 1004)
    // Dynamic window: expand right; count zeroes; shrink left if zero count > K.
    // Complexity: O(n) Time, O(1) Space
    public static int longestOnes(int[] nums, int k) {
        int left = 0;
        int maxLen = 0;
        int zeroCount = 0;

        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) zeroCount++;

            // Shrink window from left until zeroes <= k
            while (zeroCount > k) {
                if (nums[left] == 0) zeroCount--;
                left++;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }

    // ARCHETYPE 5: Count Subarrays with Product Less Than K (LeetCode 713)
    // Key Insight: Every valid window [left, right] contributes exactly (right - left + 1) subarrays!
    // Complexity: O(n) Time, O(1) Space
    public static int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1) return 0;
        int product = 1;
        int count = 0;
        int left = 0;

        for (int right = 0; right < nums.length; right++) {
            product *= nums[right];
            while (product >= k && left <= right) {
                product /= nums[left++];
            }
            count += (right - left + 1);
        }
        return count;
    }
}
```

---

### 8. Josephus Problem (`L34-Josephus trap.pptx`)
> **Problem**: $n$ people in a circle, every $k$-th eliminated. Find the survivor.  
> **Faculty PPT Recurrence (1-Indexed)**:
> $$\text{josephus}(n, k) = (\text{josephus}(n - 1, k) + k - 1) \pmod n + 1, \quad \text{josephus}(1, k) = 1$$

```java
public class JosephusTrap {
    // 1. Recursive method as presented in Faculty PPT (1-indexed)
    public static int josephus(int n, int k) {
        if (n == 1) return 1;
        return (josephus(n - 1, k) + k - 1) % n + 1;
    }

    // 2. Iterative loop (O(n) time, O(1) space, no stack overflow)
    public static int josephusIterative(int n, int k) {
        int survivor = 0; // 0-indexed base: J(1, k) = 0
        for (int i = 2; i <= n; i++) {
            survivor = (survivor + k) % i;
        }
        return survivor + 1; // Convert to 1-indexed
    }

    public static void main(String[] args) {
        // Sample from Slide 4: n = 14, k = 2 => Output: 13
        System.out.println("The chosen place is: " + josephus(14, 2)); // Output: 13
    }
}
```
