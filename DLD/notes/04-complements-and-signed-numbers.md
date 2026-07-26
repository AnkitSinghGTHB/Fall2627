# 🔄 Module 1.4 — Complements & Signed Binary Numbers

> **TL;DR**: Complements are just a trick to do **subtraction using addition**. Computers hate subtraction — they convert it into addition using complements. Learn 2 types (r's and (r-1)'s complement), and you're set.

---

## 🤔 Why Do Complements Exist?

Computers are really good at **adding**. They're terrible at **subtracting**. So engineers thought:

> *"What if we convert subtraction into addition using a trick?"*

That trick = **complements**. That's literally the entire reason they exist.

---

## 📋 Two Types of Complements

For any base-r number system, there are exactly **two** types:

| Complement | Name | How to find it |
|:---:|---|---|
| **(r-1)'s** complement | "Diminished radix" | Subtract each digit from **(r-1)** |
| **r's** complement | "Radix" | (r-1)'s complement **+ 1** |

### For Binary (base 2):
- **1's complement** = flip every bit (0→1, 1→0)
- **2's complement** = 1's complement + 1

### For Decimal (base 10):
- **9's complement** = subtract each digit from 9
- **10's complement** = 9's complement + 1

---

## ✨ Binary Complements (The Ones You'll Use 95% of the Time)

### 1's Complement — Just Flip the Bits

```
Original:        1 0 1 1 0 0
1's complement:  0 1 0 0 1 1     ← every bit flipped

Original:        0 0 1 1 0 1
1's complement:  1 1 0 0 1 0     ← every bit flipped
```

That's it. Literally just swap 0s and 1s.

---

### 2's Complement — Flip + Add 1

```
Step 1: Find 1's complement (flip the bits)
Step 2: Add 1

Example: Find 2's complement of (101100)₂

Original:          1 0 1 1 0 0
1's complement:    0 1 0 0 1 1     ← flip
                              + 1  ← add 1
2's complement:    0 1 0 1 0 0     ✅
```

> 🧠 **Shortcut**: Scan from the RIGHT. Keep all bits **up to and including the first 1** the same. Flip everything else.
>
> Example: `101100` → keep `100` from right, flip the rest → `010100` ✅

---

### Decimal Complements (Rarely Asked But Know It)

```
9's complement of (3456)₁₀:
  9-3=6, 9-4=5, 9-5=4, 9-6=3  →  (6543)₁₀

10's complement = 9's complement + 1:
  6543 + 1 = (6544)₁₀
```

---

## ✍️ Signed Binary Numbers

In real computers, numbers can be **positive or negative**. But binary only has 0s and 1s — no minus sign! So we use the **leftmost bit (MSB)** as the sign:

| MSB | Meaning |
|:---:|---------|
| **0** | Positive number (+) |
| **1** | Negative number (−) |

### Three Ways to Represent Signed Numbers

For an **n-bit** number:

| Method | How negative numbers work | Range |
|--------|--------------------------|-------|
| **Sign-Magnitude** | MSB = sign, rest = magnitude | −(2ⁿ⁻¹ − 1) to +(2ⁿ⁻¹ − 1) |
| **1's Complement** | Negative = flip all bits of positive | −(2ⁿ⁻¹ − 1) to +(2ⁿ⁻¹ − 1) |
| **2's Complement** | Negative = 2's complement of positive | −2ⁿ⁻¹ to +(2ⁿ⁻¹ − 1) |

> 💡 **2's complement is the most used** in real computers because it has only one zero (no +0 and −0 problem).

### Example: Represent −5 in 4-bit signed binary

```
+5 in binary:     0 1 0 1

Sign-Magnitude:   1 1 0 1   (just change MSB to 1)
1's Complement:   1 0 1 0   (flip all bits of 0101)
2's Complement:   1 0 1 1   (flip all bits + add 1)
```

### Range for 4-bit numbers:

| Method | Range |
|--------|-------|
| Sign-Magnitude | −7 to +7 |
| 1's Complement | −7 to +7 |
| **2's Complement** | **−8 to +7** |

---

## ➖ Subtraction Using Complements

This is the whole reason complements exist. Here's how it works:

### Using 2's Complement (The Standard Method)

**A − B = A + (2's complement of B)**

Then:
- If there's an **end carry** → **discard it** → result is **positive** ✅
- If there's **no end carry** → take 2's complement of result → result is **negative** ❌

### Example 1: 7 − 3 (positive result expected)

```
A = 7 = 0111
B = 3 = 0011

2's complement of B:  1100 + 1 = 1101

  0111    (A)
+ 1101    (2's complement of B)
──────
1 0100    ← end carry exists!
  ↓
Discard carry → 0100 = +4  ✅

7 - 3 = 4  ✅
```

> The end carry tells you: **the answer is positive**. Just drop that carry.

### Example 2: 3 − 7 (negative result expected)

```
A = 3 = 0011
B = 7 = 0111

2's complement of B:  1000 + 1 = 1001

  0011    (A)
+ 1001    (2's complement of B)
──────
  1100    ← NO end carry!
  ↓
Take 2's complement: 0011 + 1 = 0100 = 4
Answer = −4  ✅

3 - 7 = −4  ✅
```

---

### Using 1's Complement

**A − B = A + (1's complement of B)**

Then:
- If there's an **end carry** → **add it back** to the result (called **end-around carry**) → result is **positive**
- If there's **no end carry** → take 1's complement of result → result is **negative**

### Example: 7 − 3 using 1's complement

```
A = 7 = 0111
B = 3 = 0011

1's complement of B: 1100

  0111
+ 1100
──────
1 0011    ← end carry!
     ↓
Add carry back: 0011 + 1 = 0100 = +4  ✅
```

> ⚠️ **Key difference from 2's complement**: In 1's complement, you **add the carry back**. In 2's complement, you **discard** it.

---

## 📝 Quick Comparison: Which Method for Subtraction?

| | 2's Complement | 1's Complement |
|---|---|---|
| End carry? | **Discard it** | **Add it back** |
| No carry? | Take 2's complement, answer is negative | Take 1's complement, answer is negative |
| Used by real computers? | ✅ Yes (standard) | ❌ Rarely |

---

## 🏋️ Solved Exam Practice Questions

### Question 1 (2's Complement Subtraction Numerical)
**Perform $(14)_{10} - (9)_{10}$ using 8-bit 2's complement arithmetic.**

<details>
<summary>💡 Step-by-Step Solution</summary>

**Step 1:** Represent $+14$ and $+9$ in 8-bit binary:
- $14 = (00001110)_2$
- $9 = (00001001)_2$

**Step 2:** Find 2's complement of $9$ (which represents $-9$):
- 1's complement of $9 = 11110110$
- 2's complement of $9 = 11110110 + 1 = 11110111$

**Step 3:** Add $+14$ and $-9$:
$$\begin{array}{r@{\quad}l}
  00001110 & (+14) \\
+ 11110111 & (-9) \\
\hline
1\,00000101 &
\end{array}$$

**Step 4:** Discard the end carry $1$.
- Result $= 00000101_2 = (+5)_{10}$. ✅
</details>

---

### Question 2 (Overflow Detection)
**Add $+70$ and $+80$ in 8-bit signed 2's complement system. Check if overflow occurs.**

<details>
<summary>💡 Step-by-Step Solution</summary>

- $+70 = (01000110)_2$ (MSB $= 0$)
- $+80 = (01010000)_2$ (MSB $= 0$)

$$\begin{array}{r@{\quad}l}
  01000110 & (+70) \\
+ 01010000 & (+80) \\
\hline
  10010110 & (-106 \text{ in 2's comp})
\end{array}$$

**Conclusion:** We added two positive numbers (both MSB $= 0$) and got a negative result (MSB $= 1$). Carry into MSB ($C_{\text{in}}=1$) $\neq$ Carry out of MSB ($C_{\text{out}}=0$). **Overflow detected!** (150 exceeds the 8-bit signed range $-128 \text{ to } +127$). ✅
</details>

---

## ✅ Quick Self-Check (1 minute)

1. What's the 1's complement of `10110`?
2. What's the 2's complement of `10110`?
3. In signed binary, what does MSB = 1 mean?
4. When doing subtraction with 2's complement, what do you do with the end carry?
5. Compute `5 − 2` using 2's complement (4 bits)

<details>
<summary>🔑 Answers</summary>

1. `01001` (flip all bits)
2. `01001 + 1 = 01010`
3. The number is **negative**
4. **Discard** it (throw it away)
5. A=0101, B=0010, 2's comp of B = 1110. 0101+1110 = 1 0011. Discard carry → `0011` = **3** ✅

</details>

---

**⏱️ Time spent: ~15 minutes. Next up →** [05 - BCD Codes](./05-bcd-codes.md)
