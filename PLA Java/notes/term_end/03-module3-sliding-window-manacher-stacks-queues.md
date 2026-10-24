# 📘 Unit 3: Strings, Greedy Algorithms & Backtracking

> **Aligned with VIT Bhopal PLA1004 Syllabus & TEE Papers (Slots A11, B14, F11, E11, A21)**  
> **Exam Paper Mapping**:
> - **PART A**: **Question 3** (12 Marks — with internal choice `OR`)
> - **PART B**: **Question 8** (8 Marks — direct implementation)  
> **Total Unit Weight in TEE**: **Exactly 20 Marks**

---

# PART 1: SECTION A QUESTIONS (12 MARKS) [Question 3 Pool]

---

## 1. Josephus Problem & Elimination Recurrence
*(Paper 1 Q3a, Paper 2 Q3a — 6 to 12 Marks)*

### Problem Statement:
There are $n$ people standing in a circle waiting to be eliminated. Counting begins at person 1 and proceeds around the circle. In each step, every $k$-th person is eliminated until only one survivor remains. Display the complete elimination order of all $n$ people and determine the position of the survivor.

### Algorithmic Approaches:
1. **Simulation Approach (Using a List for Full Elimination Order)**:
   - Place all $n$ people (1 to $n$) into a list.
   - Maintain the current elimination index: `index = (index + k - 1) % list.size()`.
   - Remove the person at `index`, record their elimination, and repeat until the list is empty.
   - Time Complexity: $O(n^2)$ due to list removal shifts; Space: $O(n)$.
2. **Recursive Formula (Direct Survivor Calculation)**:
   - Base Case: $J(1, k) = 1$ (if 1 person remains, they are the survivor).
   - Recurrence (1-indexed):
     $$J(n, k) = (J(n - 1, k) + k - 1) \pmod n + 1$$
   - Time Complexity: $O(n)$; Space: $O(n)$ recursion call stack (or $O(1)$ iterative).

```java
import java.util.*;

public class JosephusSolver {
    // 1. Simulation approach: Displays complete elimination order
    public static List<Integer> getEliminationOrder(int n, int k) {
        List<Integer> circle = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            circle.add(i);
        }

        List<Integer> order = new ArrayList<>();
        int index = 0;

        while (!circle.isEmpty()) {
            index = (index + k - 1) % circle.size();
            order.add(circle.remove(index));
        }
        return order;
    }

    // 2. Recursive formula: Returns position of survivor directly
    public static int josephusSurvivor(int n, int k) {
        if (n == 1) return 1;
        return (josephusSurvivor(n - 1, k) + k - 1) % n + 1;
    }

    public static void main(String[] args) {
        // Trace 1: Paper 1 Q3a (n = 8, k = 3)
        int n1 = 8, k1 = 3;
        List<Integer> order1 = getEliminationOrder(n1, k1);
        System.out.println("n = 8, k = 3 Elimination Order: " + order1);
        System.out.println("Survivor: " + order1.get(order1.size() - 1) + " | Recursive Formula: " + josephusSurvivor(n1, k1));

        // Trace 2: Paper 2 Q3a (n = 8, k = 4)
        int n2 = 8, k2 = 4;
        List<Integer> order2 = getEliminationOrder(n2, k2);
        System.out.println("n = 8, k = 4 Elimination Order: " + order2);
        System.out.println("Survivor: " + order2.get(order2.size() - 1) + " | Recursive Formula: " + josephusSurvivor(n2, k2));
    }
}
```

#### Step-by-Step Execution Trace for $n = 8, k = 3$:
1. Circle: `[1, 2, 3, 4, 5, 6, 7, 8]`. Start at index 0. `(0 + 3 - 1) % 8 = 2` $\implies$ Person **3** eliminated.
2. Circle: `[1, 2, 4, 5, 6, 7, 8]`. Start at index 2. `(2 + 3 - 1) % 7 = 4` $\implies$ Person **6** eliminated.
3. Circle: `[1, 2, 4, 5, 7, 8]`. Start at index 4. `(4 + 3 - 1) % 6 = 0` $\implies$ Person **1** eliminated.
4. Circle: `[2, 4, 5, 7, 8]`. Start at index 0. `(0 + 3 - 1) % 5 = 2` $\implies$ Person **5** eliminated.
5. Circle: `[2, 4, 7, 8]`. Start at index 2. `(2 + 3 - 1) % 4 = 0` $\implies$ Person **2** eliminated.
6. Circle: `[4, 7, 8]`. Start at index 0. `(0 + 3 - 1) % 3 = 2` $\implies$ Person **8** eliminated.
7. Circle: `[4, 7]`. Start at index 2. `(2 + 3 - 1) % 2 = 0` $\implies$ Person **4** eliminated.
8. Circle: `[7]`. Last person remaining: Person **7** is the **Survivor**!
* **Elimination Order**: `[3, 6, 1, 5, 2, 8, 4, 7]`.

#### Step-by-Step Execution Trace for $n = 7, k = 3$ (Assignment Q1.4):
* **Simulation Steps**:
  1. Circle: `[1, 2, 3, 4, 5, 6, 7]`. `(0 + 3 - 1) % 7 = 2` $\implies$ Person **3** eliminated.
  2. Circle: `[1, 2, 4, 5, 6, 7]`. `(2 + 3 - 1) % 6 = 4` $\implies$ Person **6** eliminated.
  3. Circle: `[1, 2, 4, 5, 7]`. `(4 + 3 - 1) % 5 = 1` $\implies$ Person **2** eliminated.
  4. Circle: `[1, 4, 5, 7]`. `(1 + 3 - 1) % 4 = 3` $\implies$ Person **7** eliminated.
  5. Circle: `[1, 4, 5]`. `(3 + 3 - 1) % 3 = 2` $\implies$ Person **5** eliminated.
  6. Circle: `[1, 4]`. `(2 + 3 - 1) % 2 = 0` $\implies$ Person **1** eliminated.
  7. Circle: `[4]`. Person **4** is the **Survivor**!
* **Elimination Order**: `[3, 6, 2, 7, 5, 1, 4]`.
* **Verification via Recurrence Formula**:
  - $J(1, 3) = 1$
  - $J(2, 3) = (1 + 2) \pmod 2 + 1 = \mathbf{2}$
  - $J(3, 3) = (2 + 2) \pmod 3 + 1 = \mathbf{2}$
  - $J(4, 3) = (2 + 2) \pmod 4 + 1 = \mathbf{1}$
  - $J(5, 3) = (1 + 2) \pmod 5 + 1 = \mathbf{4}$
  - $J(6, 3) = (4 + 2) \pmod 6 + 1 = \mathbf{1}$
  - $J(7, 3) = (1 + 2) \pmod 7 + 1 = \mathbf{4}$ $\implies$ Exact match!

---

## 2. Minimum Meeting Rooms Required (Greedy Interval Scheduling)
*(Paper 1 Q3b — 6 to 12 Marks)*

### Problem Statement:
Given the start and finish times of $N$ meetings, find the minimum number of meeting rooms required so that no two overlapping meetings share a room, using a greedy approach.

### Algorithmic Logic:
1. Extract all start times into array `start[]` and all end times into array `end[]`.
2. Sort both `start[]` and `end[]` in ascending order independently.
3. Use two pointers: `i` for `start[]` and `j` for `end[]`. Maintain `currentRooms` and `maxRooms`.
4. If `start[i] < end[j]`, a meeting begins before the earliest meeting ends $\implies$ allocate an additional room (`currentRooms++`, `i++`).
5. Otherwise (`start[i] >= end[j]`), a meeting ended $\implies$ free up a room (`currentRooms--`, `j++`).
6. Track `maxRooms = Math.max(maxRooms, currentRooms)`.

```java
import java.util.Arrays;

public class MeetingRoomsGreedy {
    public static int minMeetingRooms(int[][] intervals) {
        int n = intervals.length;
        if (n == 0) return 0;

        int[] start = new int[n];
        int[] end = new int[n];

        for (int i = 0; i < n; i++) {
            start[i] = intervals[i][0];
            end[i] = intervals[i][1];
        }

        Arrays.sort(start);
        Arrays.sort(end);

        int currentRooms = 0;
        int maxRooms = 0;
        int i = 0, j = 0;

        while (i < n && j < n) {
            if (start[i] < end[j]) {
                currentRooms++;
                maxRooms = Math.max(maxRooms, currentRooms);
                i++;
            } else {
                currentRooms--;
                j++;
            }
        }
        return maxRooms;
    }

    public static void main(String[] args) {
        // Paper 1 Q3b Test Case: (0,30), (5,10), (8,12), (15,20), (25,35)
        int[][] meetings = {{0, 30}, {5, 10}, {8, 12}, {15, 20}, {25, 35}};
        int required = minMeetingRooms(meetings);
        System.out.println("Minimum Meeting Rooms Required: " + required);
    }
}
```

#### Step-by-Step Execution Trace:
* Given Meetings: `(0, 30), (5, 10), (8, 12), (15, 20), (25, 35)`.
* Sorted `start[]`: `[0, 5, 8, 15, 25]`.
* Sorted `end[]`: `[10, 12, 20, 30, 35]`.

| Step | `start[i]` | `end[j]` | Comparison | Action Taken | `currentRooms` | `maxRooms` |
|:---:|:---:|:---:|:---|:---|:---:|:---:|
| 1 | 0 | 10 | $0 < 10$ | Meeting starts $\implies$ room allocated (`i=1`) | 1 | 1 |
| 2 | 5 | 10 | $5 < 10$ | Meeting starts $\implies$ room allocated (`i=2`) | 2 | 2 |
| 3 | 8 | 10 | $8 < 10$ | Meeting starts $\implies$ room allocated (`i=3`) | **3** | **3** |
| 4 | 15 | 10 | $15 \ge 10$ | Meeting ends $\implies$ room released (`j=1`) | 2 | 3 |
| 5 | 15 | 12 | $15 \ge 12$ | Meeting ends $\implies$ room released (`j=2`) | 1 | 3 |
| 6 | 15 | 20 | $15 < 20$ | Meeting starts $\implies$ room allocated (`i=4`) | 2 | 3 |
| 7 | 25 | 20 | $25 \ge 20$ | Meeting ends $\implies$ room released (`j=3`) | 1 | 3 |
| 8 | 25 | 30 | $25 < 30$ | Meeting starts $\implies$ room allocated (`i=5`) | 2 | 3 |

* **Final Result**: Peak overlap occurs at time $t = 8$, requiring **3 meeting rooms**.
* **Complexities**: Time: $O(N \log N)$ (sorting), Auxiliary Space: $O(N)$ (start and end arrays).

---

## 3. Activity Selection Problem (Greedy by Finish Time)
*(Paper 2 Q3b, Paper 3 Q3b — 6 Marks)*

### Problem Statement:
Given $n$ activities with their start and finish times, select the maximum number of mutually compatible activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

### Greedy Choice Property:
* Always sort activities in **ascending order of their finish times**.
* Greedily pick the first activity (which finishes earliest, leaving maximum time for remaining tasks).
* For each subsequent activity, select it if and only if its start time is greater than or equal to the finish time of the last selected activity: `start[i] >= lastFinish`.

```java
import java.util.*;

class Activity {
    int id, start, finish;
    Activity(int id, int start, int finish) {
        this.id = id;
        this.start = start;
        this.finish = finish;
    }
}

public class ActivitySelectionGreedy {
    public static List<Activity> selectActivities(int[] start, int[] finish) {
        int n = start.length;
        List<Activity> activities = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            activities.add(new Activity(i, start[i], finish[i]));
        }

        // Sort activities by finish time ascending
        activities.sort(Comparator.comparingInt(a -> a.finish));

        List<Activity> selected = new ArrayList<>();
        // Always select the first activity
        selected.add(activities.get(0));
        int lastFinish = activities.get(0).finish;

        for (int i = 1; i < n; i++) {
            if (activities.get(i).start >= lastFinish) {
                selected.add(activities.get(i));
                lastFinish = activities.get(i).finish;
            }
        }
        return selected;
    }

    public static void main(String[] args) {
        int[] start = {2, 4, 3, 7};
        int[] finish = {5, 6, 8, 9};

        List<Activity> result = selectActivities(start, finish);
        System.out.print("Selected Activities (IDs): ");
        for (Activity a : result) {
            System.out.print(a.id + " ");
        }
        System.out.println("\nTotal Activities Selected: " + result.size());
    }
}
```

#### Step-by-Step Execution Trace:
- Initial Activities: `A0(2, 5)`, `A1(4, 6)`, `A2(3, 8)`, `A3(7, 9)`.
- Already sorted by finish time: $5 < 6 < 8 < 9$.
1. Pick `A0(2, 5)`. `lastFinish = 5`.
2. Check `A1(4, 6)`: `start = 4 < 5` $\implies$ overlaps, **rejected**.
3. Check `A2(3, 8)`: `start = 3 < 5` $\implies$ overlaps, **rejected**.
4. Check `A3(7, 9)`: `start = 7 >= 5` $\implies$ compatible, **selected**! `lastFinish = 9`.
* Selected activities: `A0` and `A3` (or `{0, 1, 3}` depending on start sets). Maximum activities = 2.
* **Complexities**: Time: $O(N \log N)$ (sorting) $+ O(N)$ (scan) $= O(N \log N)$, Space: $O(N)$.

---

## 4. Lexicographically Largest Palindrome Rearrangement
*(Paper 1 Q3c — 12 Marks)*

### Problem Statement:
Given a string $S$, rearrange its characters to form the **lexicographically largest palindrome** possible. If no palindromic arrangement exists, output `-1`.

### Algorithmic Logic:
1. Count character frequencies in a frequency table of size 26.
2. Count how many characters have an **odd frequency**.
   - If `oddCount > 1`, a palindrome is **impossible** $\implies$ return `"-1"`.
3. Construct the first half of the palindrome by scanning from `'z'` down to `'a'` (to make it lexicographically largest). For each character, append `freq[ch] / 2` occurrences to a `StringBuilder`.
4. If there is a character with an odd frequency, save it as the middle character.
5. Combine: `firstHalf + middleChar + reverse(firstHalf)`.

```java
public class LargestPalindromeRearrangement {
    public static String largestPalindrome(String s) {
        int[] freq = new int[26];
        for (char ch : s.toCharArray()) {
            freq[ch - 'a']++;
        }

        int oddCount = 0;
        char middleChar = 0;

        for (int i = 0; i < 26; i++) {
            if (freq[i] % 2 != 0) {
                oddCount++;
                middleChar = (char) ('a' + i);
            }
        }

        // Palindrome impossible if more than one character has odd frequency
        if (oddCount > 1) {
            return "-1";
        }

        StringBuilder firstHalf = new StringBuilder();
        // Traverse from 'z' down to 'a' for lexicographically largest
        for (int i = 25; i >= 0; i--) {
            int count = freq[i] / 2;
            for (int k = 0; k < count; k++) {
                firstHalf.append((char) ('a' + i));
            }
        }

        StringBuilder secondHalf = new StringBuilder(firstHalf).reverse();
        StringBuilder result = new StringBuilder();
        result.append(firstHalf);
        if (oddCount == 1) {
            result.append(middleChar);
        }
        result.append(secondHalf);

        return result.toString();
    }

    public static void main(String[] args) {
        String s1 = "aabbbcc";
        System.out.println("Input: \"" + s1 + "\" -> Largest Palindrome: \"" + largestPalindrome(s1) + "\"");

        String s2 = "abcd";
        System.out.println("Input: \"" + s2 + "\" -> Largest Palindrome: \"" + largestPalindrome(s2) + "\"");
    }
}
```

#### Step-by-Step Execution Traces:
1. **Trace for $S =$ `"aabbbcc"`**:
   - Frequencies: `a: 2`, `b: 3`, `c: 2`.
   - Odd counts: `b` has count 3 (1 odd count $\le 1 \implies$ valid!).
   - Middle character: `'b'`.
   - Half counts: `c: 1`, `b: 1`, `a: 1`.
   - Traverse descending (`'z'` to `'a'`):
     - `c` (1) $\to$ `"c"`
     - `b` (1) $\to$ `"cb"`
     - `a` (1) $\to$ `"cba"`
   - Combine: `"cba"` + `'b'` + `"abc"` = `"cbababc"` (or `"cbabcbc"` depending on character counts).
2. **Trace for $S =$ `"abcd"`**:
   - Frequencies: `a: 1`, `b: 1`, `c: 1`, `d: 1`.
   - Odd count $= 4 > 1 \implies$ **Output: `-1` (Impossible)**.
* **Complexities**: Time: $O(N)$, Auxiliary Space: $O(1)$ (26-element array).

---

## 5. Huffman Coding: Tree Construction, Prefix Codes & Step-by-Step Decoding
*(Paper 3 Q3a, Paper 4 Q3b — 6 to 12 Marks)*

### Prefix Code Concept:
A prefix code ensures that no code word is a prefix of any other code word. This makes the encoded bitstream uniquely decodable without delimiters.

### Part A: Huffman Tree Construction Algorithm:
1. Create a leaf node for each character with its frequency.
2. Insert all nodes into a min-priority queue (min-heap).
3. While the priority queue has more than 1 node:
   - Extract the two nodes with the lowest frequency: `left = pq.poll()`, `right = pq.poll()`.
   - Create a new internal node with frequency $= \text{left.freq} + \text{right.freq}$.
   - Set its children to `left` and `right`.
   - Reinsert the new node into the priority queue.
4. The remaining node is the root of the Huffman Tree. Assign `'0'` to left edges and `'1'` to right edges.

```java
import java.util.*;

class HuffmanNode {
    char ch;
    int freq;
    HuffmanNode left, right;

    HuffmanNode(char ch, int freq) {
        this.ch = ch;
        this.freq = freq;
    }

    HuffmanNode(int freq, HuffmanNode left, HuffmanNode right) {
        this.ch = '-';
        this.freq = freq;
        this.left = left;
        this.right = right;
    }
}

public class HuffmanCoding {
    public static Map<Character, String> buildCodes(char[] chars, int[] freqs) {
        PriorityQueue<HuffmanNode> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a.freq));
        for (int i = 0; i < chars.length; i++) {
            pq.add(new HuffmanNode(chars[i], freqs[i]));
        }

        while (pq.size() > 1) {
            HuffmanNode left = pq.poll();
            HuffmanNode right = pq.poll();
            HuffmanNode parent = new HuffmanNode(left.freq + right.freq, left, right);
            pq.add(parent);
        }

        HuffmanNode root = pq.poll();
        Map<Character, String> codeMap = new HashMap<>();
        generatePrefixCodes(root, "", codeMap);
        return codeMap;
    }

    private static void generatePrefixCodes(HuffmanNode node, String code, Map<Character, String> map) {
        if (node == null) return;
        if (node.left == null && node.right == null) {
            map.put(node.ch, code);
            return;
        }
        generatePrefixCodes(node.left, code + "0", map);
        generatePrefixCodes(node.right, code + "1", map);
    }

    public static void main(String[] args) {
        char[] chars = {'A', 'B', 'C', 'D', 'E'};
        int[] freqs = {30, 20, 15, 10, 5};

        Map<Character, String> codes = buildCodes(chars, freqs);
        System.out.println("Generated Huffman Codes: " + codes);
    }
}
```

### Part B: Step-by-Step Decoding Worked Trace
*(Paper 4 Q3b — 6 Marks)*

**Given Huffman Codes**:
- $A = 0$
- $B = 10$
- $C = 110$
- $D = 1110$
- $E = 1111$

**Encoded Bit String**: `'11101100101111'`

#### Step-by-Step Trace Table:
| Step | Remaining Bitstring | Bits Matched | Decoded Symbol | Explanation |
|:---:|:---|:---:|:---:|:---|
| 1 | `11101100101111` | `1110` | **D** | `1110` matches $D$ uniquely |
| 2 | `1100101111` | `110` | **C** | `110` matches $C$ uniquely |
| 3 | `0101111` | `0` | **A** | `0` matches $A$ uniquely |
| 4 | `101111` | `10` | **B** | `10` matches $B$ uniquely |
| 5 | `1111` | `1111` | **E** | `1111` matches $E$ uniquely |

* **Final Decoded Sequence**: **`"DCABE"`**.
* **Complexities**: Encoding: $O(N \log N)$, Decoding: $O(M)$ where $M$ is the number of bits.

---

### Part C: Complete Huffman Tree Construction Trace (Assignment Q5.4)
*(Standard Benchmark: $a:5, b:9, c:12, d:13, e:16, f:45$)*

#### Step-by-Step Priority Queue Merging:
1. **Initial Queue**: $\{a(5), b(9), c(12), d(13), e(16), f(45)\}$
2. **Merge 1**: Poll $a(5)$ and $b(9) \implies$ Parent $N_1(14)$.
   Queue: $\{c(12), d(13), N_1(14), e(16), f(45)\}$
3. **Merge 2**: Poll $c(12)$ and $d(13) \implies$ Parent $N_2(25)$.
   Queue: $\{N_1(14), e(16), N_2(25), f(45)\}$
4. **Merge 3**: Poll $N_1(14)$ and $e(16) \implies$ Parent $N_3(30)$.
   Queue: $\{N_2(25), N_3(30), f(45)\}$
5. **Merge 4**: Poll $N_2(25)$ and $N_3(30) \implies$ Parent $N_4(55)$.
   Queue: $\{f(45), N_4(55)\}$
6. **Merge 5**: Poll $f(45)$ and $N_4(55) \implies$ Root $N_5(100)$.

#### Codebook, Lengths & Total Bit Cost:
| Character | Frequency | Huffman Prefix Code | Code Length ($L_i$) | Total Bits ($f_i \times L_i$) |
|:---:|:---:|:---:|:---:|:---:|
| **f** | 45 | `0` | 1 | $45 \times 1 = 45$ |
| **c** | 12 | `100` | 3 | $12 \times 3 = 36$ |
| **d** | 13 | `101` | 3 | $13 \times 3 = 39$ |
| **a** | 5 | `1100` | 4 | $5 \times 4 = 20$ |
| **b** | 9 | `1101` | 4 | $9 \times 4 = 36$ |
| **e** | 16 | `111` | 3 | $16 \times 3 = 48$ |
| **Total** | **100** | — | — | **224 Bits** |

* **Average Code Length**:
  $$\bar{L} = \frac{\sum (f_i \cdot L_i)}{\sum f_i} = \frac{224}{100} = \mathbf{2.24\text{ bits/character}}$$
* **Bandwidth Comparison**: A standard 3-bit fixed-length encoding requires $100 \times 3 = 300\text{ bits}$. Huffman reduces storage to $224\text{ bits}$, achieving a **$25.33\%$ bandwidth reduction**.

---

## 6. Weighted Substring of Fixed Length $K$
*(Paper 4 Q3c — 12 Marks)*

### Problem Statement:
Given a string $S$ of length $N$ consisting of lowercase English letters and an integer $K$, the weight of a character is its position in the alphabet ($a = 1, b = 2, \dots, z = 26$). The weight of a substring is the sum of the weights of its characters. Find the maximum weight among all substrings of length exactly $K$, and report that substring.

### Algorithmic Logic:
1. Convert character weights using `s.charAt(i) - 'a' + 1`.
2. Compute the weight of the initial window of size $K$ (indices $0$ to $K - 1$).
3. Slide the window one character at a time from index $K$ to $N - 1$:
   - Add weight of the incoming character: `+ weight(s[i])`.
   - Subtract weight of the outgoing character: `- weight(s[i - K])`.
4. If the new window weight exceeds `maxWeight`, update `maxWeight` and `bestStartIndex`.

```java
public class WeightedSubstringSolver {
    public static void findMaxWeightSubstring(String s, int k) {
        int n = s.length();
        if (n < k) {
            System.out.println("String length is less than window size K");
            return;
        }

        // Step 1: Compute weight of the first window
        int currentWeight = 0;
        for (int i = 0; i < k; i++) {
            currentWeight += (s.charAt(i) - 'a' + 1);
        }

        int maxWeight = currentWeight;
        int bestStartIndex = 0;

        // Step 2: Slide the window across the string
        for (int i = k; i < n; i++) {
            int incoming = s.charAt(i) - 'a' + 1;
            int outgoing = s.charAt(i - k) - 'a' + 1;
            currentWeight = currentWeight + incoming - outgoing;

            if (currentWeight > maxWeight) {
                maxWeight = currentWeight;
                bestStartIndex = i - k + 1;
            }
        }

        String bestSubstring = s.substring(bestStartIndex, bestStartIndex + k);
        System.out.printf("Best Substring: \"%s\" (Start Index: %d) | Maximum Weight: %d\n", bestSubstring, bestStartIndex, maxWeight);
    }

    public static void main(String[] args) {
        // Paper 4 Q3c: S = "abcadeaf", K = 3
        String s = "abcadeaf";
        int k = 3;
        findMaxWeightSubstring(s, k);
    }
}
```

#### Step-by-Step Execution Trace for $S =$ `"abcadeaf"`, $K = 3$:
- Character Weights: $a = 1, b = 2, c = 3, d = 4, e = 5, f = 6$.

| Window Index Range | Substring | Characters & Individual Weights | Window Weight Calculation | Max Weight So Far |
|:---:|:---:|:---|:---:|:---:|
| `[0..2]` | `"abc"` | $a(1) + b(2) + c(3)$ | $1 + 2 + 3 = \mathbf{6}$ | 6 (`"abc"`) |
| `[1..3]` | `"bca"` | $b(2) + c(3) + a(1)$ | $6 + 1(a) - 1(a) = \mathbf{6}$ | 6 |
| `[2..4]` | `"cad"` | $c(3) + a(1) + d(4)$ | $6 + 4(d) - 2(b) = \mathbf{8}$ | 8 (`"cad"`) |
| `[3..5]` | `"ade"` | $a(1) + d(4) + e(5)$ | $8 + 5(e) - 3(c) = \mathbf{10}$ | **10 (`"ade"`)** |
| `[4..6]` | `"dea"` | $d(4) + e(5) + a(1)$ | $10 + 1(a) - 1(a) = \mathbf{10}$ | 10 |
| `[5..7]` | `"eaf"` | $e(5) + a(1) + f(6)$ | $10 + 6(f) - 4(d) = \mathbf{12}$ | **12 (`"eaf"`)** |

* **Final Output**: Substring **`"eaf"`** with Maximum Weight **$12$**.
* **Complexities**: Time: $O(N)$ (each character added and removed once), Auxiliary Space: $O(1)$.

---

## 7. Rat in a Maze Backtracking ($4 \times 4$ Maze)
*(Paper 5 Q3a — 6 Marks)*

### Problem Statement:
A rat is placed at `(0, 0)` in an $N \times N$ maze and must reach destination `(N-1, N-1)`. The rat can only move **Right** `(r, c+1)` or **Down** `(r+1, c)`. Cells with value `1` are open, and cells with value `0` are blocked. Write the backtracking algorithm and display the path matrix.

```java
public class RatInMaze {
    private static final int N = 4;

    public static boolean solveMaze(int[][] maze) {
        int[][] sol = new int[N][N];
        if (!solveMazeUtil(maze, 0, 0, sol)) {
            System.out.println("No path exists!");
            return false;
        }
        printSolution(sol);
        return true;
    }

    private static boolean solveMazeUtil(int[][] maze, int r, int c, int[][] sol) {
        // Base case: Reached destination
        if (r == N - 1 && c == N - 1 && maze[r][c] == 1) {
            sol[r][c] = 1;
            return true;
        }

        // Check if (r, c) is a valid move
        if (r >= 0 && r < N && c >= 0 && c < N && maze[r][c] == 1) {
            sol[r][c] = 1; // Mark cell as part of solution path

            // Move 1: Down
            if (solveMazeUtil(maze, r + 1, c, sol)) return true;

            // Move 2: Right
            if (solveMazeUtil(maze, r, c + 1, sol)) return true;

            // Backtrack: Unmark cell if neither move leads to destination
            sol[r][c] = 0;
            return false;
        }
        return false;
    }

    private static void printSolution(int[][] sol) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(sol[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] maze = {
            {1, 1, 0, 0},
            {0, 1, 1, 0},
            {0, 1, 0, 0},
            {0, 1, 1, 1}
        };

        System.out.println("Path Matrix (1 = Path taken):");
        solveMaze(maze);
    }
}
```

#### Step-by-Step Execution Trace on $4 \times 4$ Maze:
- Initial Maze:
  ```text
  (0,0)=1  (0,1)=1  (0,2)=0  (0,3)=0
  (1,0)=0  (1,1)=1  (1,2)=1  (1,3)=0
  (2,0)=0  (2,1)=1  (2,2)=0  (2,3)=0
  (3,0)=0  (3,1)=1  (3,2)=1  (3,3)=1
  ```
1. Start at `(0, 0)` $\implies$ Down is `(1, 0) = 0` (Blocked). Move Right to `(0, 1)`.
2. At `(0, 1)`: Down is `(1, 1) = 1` $\implies$ Move Down to `(1, 1)`.
3. At `(1, 1)`: Down is `(2, 1) = 1` $\implies$ Move Down to `(2, 1)`.
4. At `(2, 1)`: Down is `(3, 1) = 1` $\implies$ Move Down to `(3, 1)`.
5. At `(3, 1)`: Down is out of bounds. Move Right to `(3, 2)`.
6. At `(3, 2)`: Down is out of bounds. Move Right to `(3, 3)` $\implies$ **Destination Reached!**
* **Output Path Matrix**:
  ```text
  1 1 0 0 
  0 1 0 0 
  0 1 0 0 
  0 1 1 1 
  ```
* **Complexities**: Time: $O(2^{N^2})$, Auxiliary Space: $O(N^2)$ recursion stack.

---

## 8. Fractional Knapsack (Greedy) vs 0/1 Knapsack
*(Paper 5 Q3b — 6 Marks)*

### Problem Statement:
Given weights and values of $N$ items, put these items in a knapsack of capacity $W$ to get the maximum total value. In the **Fractional Knapsack Problem**, we can break items for maximizing total value.

### Greedy Choice Property:
* Calculate the ratio $\text{Value} / \text{Weight}$ for each item.
* Sort items in descending order of this ratio.
* Add items to the knapsack: if the item fits completely, take all of it; otherwise, take the fractional fraction $\frac{\text{remaining capacity}}{\text{item weight}} \times \text{value}$.

```java
import java.util.Arrays;

class Item {
    int weight, value;
    Item(int w, int v) { this.weight = w; this.value = v; }
}

public class FractionalKnapsack {
    public static double getMaxValue(Item[] items, int capacity) {
        // Sort items by value/weight ratio descending
        Arrays.sort(items, (a, b) -> Double.compare((double) b.value / b.weight, (double) a.value / a.weight));

        double totalValue = 0.0;
        int currentCapacity = capacity;

        for (Item item : items) {
            if (item.weight <= currentCapacity) {
                // Take whole item
                currentCapacity -= item.weight;
                totalValue += item.value;
            } else {
                // Take fraction
                totalValue += ((double) item.value / item.weight) * currentCapacity;
                break; // Knapsack full
            }
        }
        return totalValue;
    }

    public static void main(String[] args) {
        // Paper 5 Q3b Test Case: weights {10, 20, 30}, values {60, 100, 120}, capacity 50
        Item[] items = { new Item(10, 60), new Item(20, 100), new Item(30, 120) };
        int capacity = 50;

        double maxValue = getMaxValue(items, capacity);
        System.out.printf("Maximum Value in Fractional Knapsack: %.2f\n", maxValue);
    }
}
```

#### Step-by-Step Execution Trace ($W = 50$):
* Item 1: Weight 10, Value 60 $\implies$ Ratio $= 60 / 10 = \mathbf{6.0}$.
* Item 2: Weight 20, Value 100 $\implies$ Ratio $= 100 / 20 = \mathbf{5.0}$.
* Item 3: Weight 30, Value 120 $\implies$ Ratio $= 120 / 30 = \mathbf{4.0}$.
1. Take Item 1 completely: Weight taken $= 10$, Value $= 60$, Remaining capacity $= 40$.
2. Take Item 2 completely: Weight taken $= 20$, Value $= 100$, Remaining capacity $= 20$.
3. Capacity remaining $= 20 < 30$. Take fraction $\frac{20}{30}$ of Item 3: Value $= \frac{2}{3} \times 120 = \mathbf{80}$.
* **Total Maximum Value**: $60 + 100 + 80 = \mathbf{240.00}$.

#### Why Greedy Fails for 0/1 Knapsack:
* In 0/1 Knapsack, items cannot be divided. An item with high value-to-weight ratio might leave significant empty capacity that cannot be filled, yielding a sub-optimal result. 0/1 Knapsack exhibits the **optimal substructure** property requiring **Dynamic Programming**.

---

## 9. Manacher's Algorithm for Longest Palindromic Substring ($O(N)$)
*(Paper 5 Q3c, Paper 3 Q6 — 8 to 12 Marks)*

### Problem Statement:
Find the longest palindromic substring within a given text in strictly linear $O(N)$ time.

### Algorithmic Logic:
1. **Odd Transformation**: Insert delimiter `'#'` between all characters and surround with sentinels: `"^#b#a#b#c#b#a#b#c#b#a#c#c#b#a#$"`.
2. Maintain array `P[i]` representing the palindrome radius centered at $i$.
3. Keep track of the current center $C$ and right boundary $R = C + P[C]$.
4. For each position $i$:
   - If $i < R$, initialize $P[i] = \min(R - i, P[2C - i])$ using the mirror property $i' = 2C - i$.
   - Expand outwards around $i$ while characters match.
   - If $i + P[i] > R$, update $C = i$ and $R = i + P[i]$.
5. Time Complexity is strictly $O(N)$ because the right pointer $R$ increases monotonically.

```java
public class ManachersAlgorithm {
    public static String longestPalindrome(String s) {
        if (s == null || s.length() == 0) return "";

        // Transform: "aba" -> "^#a#b#a#$"
        StringBuilder t = new StringBuilder("^");
        for (char c : s.toCharArray()) {
            t.append('#').append(c);
        }
        t.append("#$");

        char[] chars = t.toString().toCharArray();
        int n = chars.length;
        int[] p = new int[n];
        int center = 0, right = 0;
        int maxLen = 0, centerIndex = 0;

        for (int i = 1; i < n - 1; i++) {
            int mirror = 2 * center - i;

            if (i < right) {
                p[i] = Math.min(right - i, p[mirror]);
            }

            // Attempt expansion around i
            while (chars[i + (1 + p[i])] == chars[i - (1 + p[i])]) {
                p[i]++;
            }

            // Update center and right boundary
            if (i + p[i] > right) {
                center = i;
                right = i + p[i];
            }

            if (p[i] > maxLen) {
                maxLen = p[i];
                centerIndex = i;
            }
        }

        int start = (centerIndex - maxLen) / 2;
        return s.substring(start, start + maxLen);
    }

    public static void main(String[] args) {
        String s = "babcbabcbaccba";
        String lps = longestPalindrome(s);
        System.out.println("Input String: \"" + s + "\"");
        System.out.println("Longest Palindromic Substring: \"" + lps + "\" | Length: " + lps.length());
    }
}
```

* **Complexity**: Time: $O(N)$, Auxiliary Space: $O(N)$ (for delimiter transformation array).

---

## 10. Selection Sort Algorithm & Swapping Trace
*(Paper 3 Q3c — 12 Marks)*

### Problem Statement:
Write the Selection Sort algorithm and trace the selection and swapping process for the input array $\{64, 25, 12, 22, 11\}$.

```java
import java.util.Arrays;

public class SelectionSortDemo {
    public static void selectionSort(int[] a) {
        int n = a.length;
        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < n; j++) {
                if (a[j] < a[minIdx]) {
                    minIdx = j;
                }
            }
            // Swap minimum with first element of unsorted subarray
            int temp = a[minIdx];
            a[minIdx] = a[i];
            a[i] = temp;

            System.out.println("Pass " + (i + 1) + " (min=" + temp + "): " + Arrays.toString(a));
        }
    }

    public static void main(String[] args) {
        int[] arr = {64, 25, 12, 22, 11};
        System.out.println("Initial Array: " + Arrays.toString(arr));
        selectionSort(arr);
    }
}
```

#### Step-by-Step Swapping Trace on $\{64, 25, 12, 22, 11\}$:
1. **Pass 1 ($i=0$)**: Search in `[64, 25, 12, 22, 11]`. Minimum is $11$ at index 4. Swap $64$ and $11$.
   - Array: `[11, 25, 12, 22, 64]`.
2. **Pass 2 ($i=1$)**: Search in `[25, 12, 22, 64]`. Minimum is $12$ at index 2. Swap $25$ and $12$.
   - Array: `[11, 12, 25, 22, 64]`.
3. **Pass 3 ($i=2$)**: Search in `[25, 22, 64]`. Minimum is $22$ at index 3. Swap $25$ and $22$.
   - Array: `[11, 12, 22, 25, 64]`.
4. **Pass 4 ($i=3$)**: Search in `[25, 64]`. Minimum is $25$ at index 3. No swap needed.
   - Array: `[11, 12, 22, 25, 64]`.
* **Complexities**: Best, Average & Worst Case Time: $O(N^2)$ comparisons, strictly $O(N)$ swaps. Space: $O(1)$.

---
---

# PART 2: SECTION B QUESTIONS (8 MARKS) [Question 8 Pool]

---

## 11. $N$-Queens Backtracking for $N = 4$ & Pruning Evaluation
*(Paper 1 Q8, Paper 4 Q3a — 8 Marks)*

### Problem Statement:
Place 4 queens on a $4 \times 4$ chessboard such that no two queens attack each other (no two queens share the same row, column, or diagonal). Display all solutions and compare the number of placements tried against the brute-force $4^4 = 256$ approach.

```java
public class NQueensSolver {
    private static final int N = 4;
    private static int solutionCount = 0;
    private static int placementsTried = 0;

    public static void solveNQueens() {
        int[][] board = new int[N][N];
        placeQueens(board, 0);
        System.out.println("Total Solutions Found: " + solutionCount);
        System.out.println("Total Valid Placements Tried with Pruning: " + placementsTried);
    }

    private static void placeQueens(int[][] board, int row) {
        if (row == N) {
            solutionCount++;
            printBoard(board);
            return;
        }

        for (int col = 0; col < N; col++) {
            placementsTried++;
            if (isSafe(board, row, col)) {
                board[row][col] = 1;
                placeQueens(board, row + 1);
                board[row][col] = 0; // Backtrack
            }
        }
    }

    private static boolean isSafe(int[][] board, int row, int col) {
        // Check column
        for (int i = 0; i < row; i++) if (board[i][col] == 1) return false;
        // Check upper-left diagonal
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) if (board[i][j] == 1) return false;
        // Check upper-right diagonal
        for (int i = row - 1, j = col + 1; i >= 0 && j < N; i--, j++) if (board[i][j] == 1) return false;
        return true;
    }

    private static void printBoard(int[][] board) {
        System.out.println("Solution " + solutionCount + ":");
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(board[i][j] == 1 ? "Q " : ". ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void main(String[] args) {
        solveNQueens();
    }
}
```

#### Pruning Evaluation vs Brute-Force:
1. **Brute-Force Complexity**: Trying all combinations of 4 queens across 4 columns results in $4^4 = \mathbf{256}$ configurations.
2. **Backtracking Pruning**: As soon as a queen placement conflicts with an existing queen, the entire sub-tree is pruned. Backtracking tests only **17 placements** total before finding both valid solutions, pruning over **93%** of search space!
* **Two Valid Solutions for $N = 4$**:
  - Solution 1: Row indices `[1, 3, 0, 2]` $\implies$ `(0,1), (1,3), (2,0), (3,2)`
  - Solution 2: Row indices `[2, 0, 3, 1]` $\implies$ `(0,2), (1,0), (2,3), (3,1)`

---

## 12. Double Loop Complexity Trace for $N = 16$ ($O(\log^2 n)$)
*(Paper 2 Q8, Paper 3 Q8 — 8 Marks)*

```java
public class DoubleLoopComplexity {
    public static int countOperations(int n) {
        int count = 0;
        for (int i = 1; i < n; i = i * 2) {
            for (int j = n; j > 0; j = j / 2) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int n = 16;
        int total = countOperations(n);
        System.out.println("Total Operations for N = " + n + ": " + total);
    }
}
```

#### Mathematical Proof & Execution Trace for $N = 16$:
- **Outer Loop**: Starts at $i = 1$, doubles each step while $i < 16$.
  - Iterations: $i = 1, 2, 4, 8$ (Stops when $i = 16 \not< 16$).
  - Outer iteration count $= \log_2(16) = \mathbf{4\text{ iterations}}$.
- **Inner Loop**: Starts at $j = 16$, halves each step while $j > 0$.
  - Values of $j$: $16, 8, 4, 2, 1$ (Stops when $j = 0$).
  - Inner iteration count $= \log_2(16) + 1 = \mathbf{5\text{ iterations}}$.
- **Total `count`**:
  $$\text{Total} = 4 \times 5 = \mathbf{20\text{ operations}}$$
* **Time Complexity**: $O(\log n) \times O(\log n) = \mathbf{O(\log^2 n)}$. Space: $O(1)$.

---

## 13. Lexicographically Smallest Palindrome Rearrangement
*(Paper 4 Q8 — 8 Marks)*

### Problem Statement:
Given a string $S$, rearrange its characters to form the **lexicographically smallest palindrome** possible. If no palindromic arrangement exists, output `"-1"`.

```java
public class SmallestPalindromeRearrangement {
    public static String smallestPalindrome(String s) {
        int[] freq = new int[26];
        for (char ch : s.toCharArray()) freq[ch - 'a']++;

        int oddCount = 0;
        char mid = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] % 2 != 0) {
                oddCount++;
                mid = (char) ('a' + i);
            }
        }

        if (oddCount > 1) return "-1";

        StringBuilder half = new StringBuilder();
        // Traverse ascending 'a' to 'z' for lexicographically smallest
        for (int i = 0; i < 26; i++) {
            int count = freq[i] / 2;
            for (int k = 0; k < count; k++) {
                half.append((char) ('a' + i));
            }
        }

        StringBuilder result = new StringBuilder(half);
        if (oddCount == 1) result.append(mid);
        result.append(new StringBuilder(half).reverse());

        return result.toString();
    }

    public static void main(String[] args) {
        // Assignment Q3.3 Test Cases:
        System.out.println("Smallest for \"aabbccd\": \"" + smallestPalindrome("aabbccd") + "\""); // "abcdcba"
        System.out.println("Smallest for \"aabbc\":   \"" + smallestPalindrome("aabbc") + "\"");   // "abcba"
        System.out.println("Smallest for \"aabbcc\":  \"" + smallestPalindrome("aabbcc") + "\"");  // "abccba"
        System.out.println("Smallest for \"abc\":     \"" + smallestPalindrome("abc") + "\"");     // "-1"
    }
}
```

#### Step-by-Step Execution Trace (Assignment Q3.3):
1. **$S =$ `"aabbccd"`**:
   - Frequencies: $a:2, b:2, c:2, d:1$. Odd count $= 1$ ($d$). Mid $= 'd'$.
   - Half counts: $a:1, b:1, c:1$. Ascending traversal: `"abc"`.
   - Result: `"abc"` + `'d'` + `"cba"` = **`"abcdcba"`**.
2. **$S =$ `"aabbc"`**:
   - Frequencies: $a:2, b:2, c:1$. Odd count $= 1$ ($c$). Mid $= 'c'$.
   - Half counts: $a:1, b:1$. Ascending traversal: `"ab"`.
   - Result: `"ab"` + `'c'` + `"ba"` = **`"abcba"`**.

* **Complexities**: Time: $O(N)$, Auxiliary Space: $O(1)$.

---

## 14. Job Sequencing with Deadlines (Greedy Profit Ordering)
*(Paper 5 Q8 — 8 Marks)*

### Problem Statement:
Given a set of $N$ jobs where each job takes 1 unit of time and has a deadline and profit, find the maximum profit sequence using a greedy approach.

### Greedy Choice Property:
* Sort jobs in descending order of profit.
* Allocate each job to the latest available empty slot $\le$ its deadline (to leave earlier slots open for jobs with tighter deadlines).

```java
import java.util.*;

class Job {
    String id;
    int deadline, profit;
    Job(String id, int d, int p) { this.id = id; this.deadline = d; this.profit = p; }
}

public class JobSequencingGreedy {
    public static void solveJobSequencing(List<Job> jobs) {
        // Sort jobs by profit descending
        jobs.sort((a, b) -> b.profit - a.profit);

        int maxDeadline = 0;
        for (Job j : jobs) maxDeadline = Math.max(maxDeadline, j.deadline);

        String[] slots = new String[maxDeadline + 1];
        int totalProfit = 0;

        for (Job job : jobs) {
            // Find latest available slot <= deadline
            for (int slot = job.deadline; slot > 0; slot--) {
                if (slots[slot] == null) {
                    slots[slot] = job.id;
                    totalProfit += job.profit;
                    break;
                }
            }
        }

        System.out.print("Scheduled Job Sequence: ");
        for (int i = 1; i <= maxDeadline; i++) {
            if (slots[i] != null) System.out.print(slots[i] + " ");
        }
        System.out.println("\nTotal Profit Earned: " + totalProfit);
    }

    public static void main(String[] args) {
        // Paper 5 Q8: J1(2, 100), J2(1, 19), J3(2, 27), J4(1, 25), J5(3, 15)
        List<Job> jobs = new ArrayList<>();
        jobs.add(new Job("J1", 2, 100));
        jobs.add(new Job("J2", 1, 19));
        jobs.add(new Job("J3", 2, 27));
        jobs.add(new Job("J4", 1, 25));
        jobs.add(new Job("J5", 3, 15));

        solveJobSequencing(jobs);
    }
}
```

#### Step-by-Step Execution Trace:
- Jobs sorted by profit: `J1(2, 100)`, `J3(2, 27)`, `J4(1, 25)`, `J2(1, 19)`, `J5(3, 15)`.
- Max deadline $= 3$. Slots: `[1, 2, 3]`.
1. `J1(deadline=2, profit=100)`: Slot 2 is free $\implies$ place in **Slot 2**.
2. `J3(deadline=2, profit=27)`: Slot 2 full, search backwards $\implies$ Slot 1 is free $\implies$ place in **Slot 1**.
3. `J4(deadline=1, profit=25)`: Slot 1 full $\implies$ cannot be scheduled, **dropped**.
4. `J2(deadline=1, profit=19)`: Slot 1 full $\implies$ **dropped**.
5. `J5(deadline=3, profit=15)`: Slot 3 is free $\implies$ place in **Slot 3**.
* **Scheduled Sequence**: `J3, J1, J5`. **Total Profit**: $27 + 100 + 15 = \mathbf{142}$.
* **Evaluation**: Ordering by profit maximizes revenue within slot constraints. Ordering by deadline blindly picks low-profit jobs and misses high-value deadlines.
* **Complexities**: Time: $O(N \log N + N \cdot D)$ where $D$ is max deadline; Space: $O(D)$.
