# 🚀 PLA Java CAT-1 Master Algorithm Cheat Sheet

Welcome to the **Ultimate CAT-1 Survival Guide**. We've got a lot of algorithms to cover. If you learn the core logic for each, writing the Java code is just translating English to syntax.

Let's dive into the TL;DRs, the Memory Tricks, and the Exam Traps!

---

## 1. Number Theory & Primes

### 🧠 Sieve of Eratosthenes (Simple & Segmented & Incremental)
**TL;DR:** The fastest way to find all prime numbers up to `N`. Instead of checking if each number is prime, you cross out the multiples of every prime you find.
* **Simple Sieve:** Create a boolean array up to `N`. Cross out multiples starting from `p*p`.
* **Segmented Sieve:** Used when `N` is huge (like 10^9) but the range is small (like 10^5). Find primes up to `sqrt(N)`, then use them to cross out multiples only in your specific segment `[L, R]`.
* **Incremental Sieve:** Generates primes infinitely on the fly using a priority queue.

<details>
<summary>💡 The Simple Sieve Code</summary>

```java
import java.util.Arrays;

public class Sieve {
    public static void sieveOfEratosthenes(int n) {
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = false; isPrime[1] = false;
        
        for (int p = 2; p * p <= n; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i <= n; i += p) {
                    isPrime[i] = false;
                }
            }
        }
    }
}
```
</details>

> [!WARNING]
> **Exam Trap:** Don't loop `i` starting from `p + p`. Start from `p * p`! (Because all smaller multiples like `p*2` or `p*3` were already crossed out by 2 or 3).

### 🔢 Euclid's Algorithm (GCD)
**TL;DR:** Find the Greatest Common Divisor using the magic of remainders. `GCD(a, b) = GCD(b, a % b)`. Keep going until `b` is 0.

<details>
<summary>💡 The Code</summary>

```java
public static int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
```
</details>

### 👑 Euler's Totient Function (Phi)
**TL;DR:** Counts how many numbers up to `N` are *coprime* to `N` (i.e., their GCD with `N` is 1).
* **Formula:** `Phi(N) = N * (1 - 1/p1) * (1 - 1/p2)...` where `p` are the prime factors.

<details>
<summary>💡 The Code</summary>

```java
public static int phi(int n) {
    int result = n;
    for (int p = 2; p * p <= n; p++) {
        if (n % p == 0) {
            while (n % p == 0) n /= p;
            result -= result / p;
        }
    }
    if (n > 1) result -= result / n;
    return result;
}
```
</details>

### 🧮 Chinese Remainder Theorem (CRT)
**TL;DR:** Used to find a number `X` that leaves specific remainders when divided by specific (coprime) divisors. 
* "Find `X` such that `X % 3 = 2` and `X % 5 = 3` and `X % 7 = 2`."

---

## 2. Bit Manipulation Wizards 🧙‍♂️

### 🔄 Swap Two Nibbles in a Byte
**TL;DR:** A byte has 8 bits (e.g., `0110 1001`). A nibble is 4 bits. We want to swap the left half with the right half.
* **Trick:** Push the right side to the left `(x << 4)`, pull the left side to the right `(x >> 4)`, and combine them with OR `|`.

<details>
<summary>💡 The Code</summary>

```java
public class SwapNibbles {
    public static int swapNibbles(int x) {
        // 0x0F is 00001111 (gets right nibble)
        // 0xF0 is 11110000 (gets left nibble)
        return ((x & 0x0F) << 4 | (x & 0xF0) >> 4);
    }
}
```
</details>

### 🎭 Binary Palindrome
**TL;DR:** Check if the binary representation of a number reads the same forwards and backwards.
* **Exam Trap:** Reverse bits using bitwise operators, not strings! `(reversed = (reversed << 1) | (n & 1))`

### ⚡ Longest Sequence of 1s after flipping ONE bit
**TL;DR:** You have a binary string like `110111011`. If you can flip exactly *one* `0` to a `1`, what's the longest continuous streak of `1`s you can get?
* **Trick:** Keep track of the length of the *previous* streak of 1s and the *current* streak of 1s. When you hit a `0`, `prev = current`.

### 🔄 Block Swap Algorithm (Array Rotation)
**TL;DR:** Rotate an array by `d` elements. 
* **Trick:** Instead of moving one by one, swap blocks of elements until the array is fully rotated. Or use the "Reversal Algorithm" (Reverse first `d`, reverse remaining, reverse all).

### ✖️ Booth's Algorithm
**TL;DR:** A clever bit-level algorithm for multiplying two signed binary numbers. 
* **Trick:** It looks at pairs of bits (`01` means add, `10` means subtract, `00` or `11` means do nothing) and shifts.

---

## 3. Arrays & Special Numbers 📊

### 🏆 Leaders in an Array
**TL;DR:** A number is a "Leader" if it is STRICTLY GREATER than everything to its right.
* **Trick:** Start from the *right* side of the array and move left, keeping track of the `max_so_far`. If the current number is `> max_so_far`, it's a leader!

### 👑 Majority Element (Moore's Voting Algorithm)
**TL;DR:** Find the element that appears more than `N/2` times.
* **Analogy:** It's a battle royale! A candidate gets +1 health if they see their own clone, and -1 health if they see a different number. If health drops to 0, they are eliminated and the next number becomes candidate.

### 📈 Max Subarray Sum (Kadane's Algorithm)
**TL;DR:** Find the contiguous part of an array that has the largest sum.
* **Trick:** Keep a running sum. If the running sum ever drops below 0, throw it away (reset to 0) because a negative number will only drag down future numbers. Keep track of the `max_ever_seen`.

<details>
<summary>💡 The Code</summary>

```java
public int maxSubArray(int[] nums) {
    int maxSum = Integer.MIN_VALUE;
    int currentSum = 0;
    
    for (int num : nums) {
        currentSum += num;
        if (currentSum > maxSum) maxSum = currentSum;
        if (currentSum < 0) currentSum = 0; // The Kadane Reset!
    }
    return maxSum;
}
```
</details>

### ⚖️ Max Equilibrium Sum
**TL;DR:** Find the maximum sum of elements where the sum of elements on its left equals the sum of elements on its right.
* **Trick:** Calculate the total sum first. Then iterate, updating `left_sum` and `right_sum = total - left_sum - current`. If `left_sum == right_sum`, record the max.

### ⏳ Max Sum of Hour Glass (2D Array)
**TL;DR:** In a 2D matrix, an hourglass looks like an "I" shape (3 elements top, 1 middle, 3 bottom). Find the hourglass with the max sum.
* **Trick:** Loop through `i` (0 to rows-2) and `j` (0 to cols-2). Sum = `mat[i][j] + mat[i][j+1] + mat[i][j+2] + mat[i+1][j+1] + mat[i+2][j] + mat[i+2][j+1] + mat[i+2][j+2]`.

### 🙃 Strobogrammatic Numbers
**TL;DR:** A number that looks exactly the same when rotated 180 degrees (upside down).
* **Valid Digits:** 0, 1, 8 (stay same). 6 and 9 (flip into each other). All other digits make it invalid.
* **Trick:** Use two pointers (start and end). Check if `pairs(start, end)` is valid `(0,0), (1,1), (8,8), (6,9), (9,6)`.

### 🔠 Natural Sort Order
**TL;DR:** Sorting strings that contain numbers so that "file2.txt" comes before "file10.txt".
* **Standard Sort:** "file10" < "file2" (because '1' < '2').
* **Natural Sort:** "file2" < "file10" (extracts the number and compares as integers).

---

> [!TIP]
> **Exam Strategy:** If they ask for **Space and Time Complexity**, almost all the bit manipulation problems are `O(1)` space and `O(log N)` or `O(1)` time. Arrays are usually `O(N)` time and `O(1)` space (unless sorting is involved, then `O(N log N)` time).
