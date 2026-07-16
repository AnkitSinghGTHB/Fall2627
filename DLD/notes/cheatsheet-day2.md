# ⚡ Day 2 Cheatsheet — Complements, Signed Numbers & BCD

> **One page. All the formulas. Exam-night ready.**

---

## Complements

| Type | Binary (base 2) | How |
|------|:---:|---|
| (r-1)'s | **1's complement** | Flip every bit |
| r's | **2's complement** | Flip every bit + add 1 |

**2's complement shortcut**: From the RIGHT, keep everything up to and including the first `1`. Flip the rest.

---

## Subtraction Using 2's Complement

```
A − B  =  A + (2's complement of B)
```

| End carry? | Meaning |
|:---:|---|
| ✅ Yes | **Discard** carry → answer is **positive** |
| ❌ No | Take 2's complement of result → answer is **negative** |

## Subtraction Using 1's Complement

```
A − B  =  A + (1's complement of B)
```

| End carry? | Meaning |
|:---:|---|
| ✅ Yes | **Add carry back** to result → answer is **positive** |
| ❌ No | Take 1's complement of result → answer is **negative** |

---

## Signed Binary (n bits)

| MSB = 0 → Positive | MSB = 1 → Negative |

| Method | Range (n bits) |
|--------|:-:|
| Sign-Magnitude | −(2ⁿ⁻¹−1) to +(2ⁿ⁻¹−1) |
| 1's Complement | −(2ⁿ⁻¹−1) to +(2ⁿ⁻¹−1) |
| **2's Complement** | **−2ⁿ⁻¹ to +(2ⁿ⁻¹−1)** |

---

## BCD (Binary Coded Decimal)

Each decimal digit → **4 bits** (0000 to 1001 only)

```
(349)₁₀ in BCD = 0011  0100  1001
                   3     4     9
```

### BCD Addition Rule

```
Add groups normally.
If sum > 9 or carry → ADD 0110 (6) to that group.
```

**Invalid BCD codes**: 1010, 1011, 1100, 1101, 1110, 1111

---

*That's Day 2. You're flying through Module 1.*
