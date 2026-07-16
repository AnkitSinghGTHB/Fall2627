# 🔢 Module 1.5 — BCD (Binary Coded Decimal)

> **TL;DR**: BCD is NOT regular binary. Each **decimal digit** gets its own 4-bit binary code. It's less efficient than binary but easier for humans to read. The only tricky part is **BCD addition** — if a group exceeds 9, add 6.

---

## 🤔 What is BCD?

BCD = **Binary Coded Decimal**

Instead of converting the whole number to binary, you convert **each decimal digit separately** into 4 bits.

```
Normal Binary:     (25)₁₀ = (11001)₂      ← one single binary number

BCD:               (25)₁₀ = 0010 0101     ← digit 2 = 0010, digit 5 = 0101
                             ──── ────
                              2    5
```

### BCD Encoding Table

| Decimal | BCD (4 bits) |
|:---:|:---:|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |
| ~~10~~ | ~~1010~~ ❌ INVALID |
| ~~11~~ | ~~1011~~ ❌ INVALID |
| ~~12~~ | ~~1100~~ ❌ INVALID |
| ~~13~~ | ~~1101~~ ❌ INVALID |
| ~~14~~ | ~~1110~~ ❌ INVALID |
| ~~15~~ | ~~1111~~ ❌ INVALID |

> ⚠️ **The 6 invalid codes** (1010 through 1111) don't exist in BCD! Only 0000–1001 are valid. This is important for addition.

---

## 👍 Pros and Cons

| ✅ Advantages | ❌ Disadvantages |
|---|---|
| Very similar to decimal — easy to understand | Uses more bits than regular binary |
| Only need to remember 0–9 in binary | Addition/subtraction rules are different |
| Great for display systems (calculators, clocks) | Less efficient for computation |

---

## ➕ BCD Addition — The Important Part

BCD addition works group by group (4 bits at a time). The rules are:

### The Algorithm

```
1. Add the two 4-bit BCD groups using normal binary addition
2. Check the result of each group:
   ├── If result ≤ 9 (and no carry) → it's valid BCD ✅ done
   └── If result > 9 OR there's a carry → ADD 6 (0110) to that group
3. Any carry from adding 6 goes to the next group
```

### Why add 6?

Because BCD skips 6 codes (1010–1111). When you overflow past 9, you need to **jump over those 6 invalid codes** to land on the correct BCD value. Adding 6 does exactly that.

---

### Example 1: BCD Addition of 5 + 6

```
  5 → 0101
+ 6 → 0110
  ────────
       1011    ← This is 11 in binary, which is > 9 ❌

Add 6: 1011
     + 0110
     ──────
     1 0001    ← Carry = 1, group = 0001

Result: 0001 0001 = 11 in BCD  ✅  (5 + 6 = 11 ✓)
```

---

### Example 2: BCD Addition of 184 + 576

Work **right to left**, one digit-pair at a time:

```
         0001    1000    0100       (184 in BCD)
      +  0101    0111    0110       (576 in BCD)
      ────────────────────────
Ones place:   0100 + 0110 = 1010  → > 9! Add 6: 1010 + 0110 = 1 0000
                                                  carry ↑    result: 0000

Tens place:   1000 + 0111 + 1(carry) = 1 0000  → carry out! Add 6: 0000 + 0110 = 0110
                                                  carry ↑    result: 0110

Hundreds:     0001 + 0101 + 1(carry) = 0111     → ≤ 9 ✅  result: 0111

Final BCD:    0111    0110    0000  = 760  ✅
```

> 🔍 **Verify**: 184 + 576 = 760 ✓

---

### Example 3: BCD Addition of 184 + 976

```
         0001    1000    0100       (184 in BCD)
      +  1001    0111    0110       (976 in BCD)
      ────────────────────────
Ones:     0100 + 0110 = 1010 → > 9! +6 = 1 0000   (carry 1, digit 0)
Tens:     1000 + 0111 + 1 = 1 0000 → carry! +6 = 0110   (carry 1, digit 6)
Hundreds: 0001 + 1001 + 1 = 1011 → > 9! +6 = 1 0001   (carry 1, digit 1)
Thousands: carry = 0001

Final BCD: 0001  0001  0110  0000 = 1160  ✅
```

> 🔍 **Verify**: 184 + 976 = 1160 ✓

---

## 🎯 BCD Addition Decision Flowchart

```
         Add two 4-bit BCD groups
                    │
                    ▼
        ┌───────────────────────┐
        │ Is sum > 9 or carry?  │
        └───────────┬───────────┘
               ╱         ╲
             YES          NO
              │            │
              ▼            ▼
         Add 0110      Keep result
         to the sum     as-is ✅
              │
              ▼
         New carry goes
         to next group ✅
```

---

## 📝 Quick Reference

| Situation | Action |
|-----------|--------|
| Sum of a BCD group ≤ 9, no carry | ✅ Valid — keep it |
| Sum of a BCD group > 9 | ❌ Add `0110` (6) |
| Sum of a BCD group has carry-out | ❌ Add `0110` (6) |
| 1010 through 1111 in a group | ❌ INVALID BCD — always add 6 |

---

## 🏋️ Practice Problems

1. Convert `(349)₁₀` to BCD
2. Convert BCD `0100 0111 0010` to decimal
3. Perform BCD addition: `27 + 35`
4. Perform BCD addition: `456 + 789`
5. Is `1100 0101` valid BCD? Why or why not?

<details>
<summary>🔑 Answers</summary>

1. `0011 0100 1001`
2. `472`
3. `0010 0111 + 0011 0101`: Ones: 0111+0101=1100 >9, +6=1 0010. Tens: 0010+0011+1=0110. Answer: `0110 0010` = **62** ✅
4. Ones: 0110+1001=1111 >9, +6=1 0101. Tens: 0101+1000+1=1110 >9, +6=1 0100. Hundreds: 0100+0111+1=1100 >9, +6=1 0010. Thousands: 0001. Answer: `0001 0010 0100 0101` = **1245** ✅
5. **No!** First nibble `1100` = 12, which is > 9 and invalid in BCD. Second nibble `0101` = 5, which is valid. But since the first group is invalid, the whole thing is invalid BCD.

</details>

---

## ✅ Quick Self-Check (30 seconds)

1. How many bits per decimal digit in BCD?
2. What's the BCD for `(83)₁₀`?
3. When do you add 6 during BCD addition?
4. Why are codes 1010–1111 invalid in BCD?

<details>
<summary>🔑 Answers</summary>

1. **4 bits** per digit
2. `1000 0011`
3. When the 4-bit sum > 9 or when there's a carry out from the group
4. Because BCD only represents digits 0–9, and those codes would represent 10–15 which aren't single decimal digits

</details>

---

**⏱️ Time spent: ~15 minutes. Day 2 material done! 🎉**

---

*BCD addition looks scary but it's literally just: add normally → check if > 9 → add 6 if needed. That's it. Practice 3-4 problems and you'll nail it.*
