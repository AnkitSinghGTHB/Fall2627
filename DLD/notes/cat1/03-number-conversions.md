# 🔄 Module 1.3 — Number Conversions (The Tricks)

> **TL;DR**: There are really only **3 methods** you need. Master these and you can convert anything to anything. This is guaranteed exam marks — just practice the steps.

---

## 🗺️ The Conversion Roadmap

Don't panic at all the possible conversions. Here's the cheat code:

```
┌──────────────────────────────────────────────────┐
│              CONVERSION ROADMAP                  │
│                                                  │
│   Decimal ←──→ Binary ←──→ Octal                │
│       ↑            ↕           ↕                 │
│       └────────── Hex ←───────┘                  │
│                                                  │
│   METHOD 1: Decimal → Others  (Division method)  │
│   METHOD 2: Others → Decimal  (Multiply & add)   │
│   METHOD 3: Binary ↔ Octal/Hex (Group trick)     │
└──────────────────────────────────────────────────┘
```

> 💡 **Pro tip**: Octal ↔ Hex? Just go through Binary as the middleman. Easy.

---

## 🔧 METHOD 1: Decimal → Any Other Base

### The Algorithm (it's the same for ALL bases)

1. **Divide** the decimal number by the target base
2. **Write down the remainder**
3. **Repeat** with the quotient until it becomes 0
4. **Read remainders BOTTOM → TOP** ← that's your answer!

---

### Example 1: Decimal → Binary — `(24)₁₀ = (?)₂`

```
24 ÷ 2 = 12   remainder = 0  ↑
12 ÷ 2 = 6    remainder = 0  │
 6 ÷ 2 = 3    remainder = 0  │  READ
 3 ÷ 2 = 1    remainder = 1  │  BOTTOM
 1 ÷ 2 = 0    remainder = 1  │  TO TOP
                              ↓

Answer: (11000)₂  ✅
```

> 🔍 **Verify**: 16 + 8 + 0 + 0 + 0 = 24 ✓

---

### Example 2: Decimal → Octal — `(24)₁₀ = (?)₈`

```
24 ÷ 8 = 3    remainder = 0  ↑
 3 ÷ 8 = 0    remainder = 3  │  READ UP

Answer: (30)₈  ✅
```

---

### Example 3: Decimal → Hex — `(24)₁₀ = (?)₁₆`

```
24 ÷ 16 = 1   remainder = 8  ↑
 1 ÷ 16 = 0   remainder = 1  │  READ UP

Answer: (18)₁₆  ✅
```

---

### 🔥 What About Fractional Numbers?

For the part **after the decimal point**, the method FLIPS:

1. **Multiply** the fraction by the target base
2. **Write down the integer part** (that's your digit)
3. **Repeat** with the remaining fraction
4. **Read TOP → BOTTOM** ← opposite of the division method!

### Example: `(0.25)₁₀ = (?)₂`

```
0.25 × 2 = 0.50  → integer part = 0  ↓
0.50 × 2 = 1.00  → integer part = 1  │  READ
0.00 → STOP (fraction = 0)           ↓  TOP DOWN

Answer: (0.01)₂  ✅
```

### Example: `(24.25)₁₀ = (?)₂`

Just combine both methods:
- Integer part: `(24)₁₀ = (11000)₂` (from earlier)
- Fractional part: `(0.25)₁₀ = (0.01)₂`
- **Answer: `(11000.01)₂`** ✅

---

## 🔧 METHOD 2: Any Base → Decimal

### The Algorithm

**Multiply each digit by (base)^position, then add everything up.**

Position counting:
- Start from **rightmost digit** = position 0
- Go **left** = position 1, 2, 3...
- For fractions: first digit after point = position −1, then −2, etc.

---

### Example 1: Binary → Decimal — `(10110)₂ = (?)₁₀`

```
Position:    4    3    2    1    0
Digits:      1    0    1    1    0
Calculation: 1×2⁴ + 0×2³ + 1×2² + 1×2¹ + 0×2⁰
           = 16   + 0    + 4    + 2    + 0
           = 22

Answer: (22)₁₀  ✅
```

---

### Example 2: Octal → Decimal — `(273)₈ = (?)₁₀`

```
Position:    2    1    0
Digits:      2    7    3
Calculation: 2×8² + 7×8¹ + 3×8⁰
           = 128  + 56   + 3
           = 187

Answer: (187)₁₀  ✅
```

---

### Example 3: Hex → Decimal — `(1A3)₁₆ = (?)₁₀`

```
Position:    2    1    0
Digits:      1    A    3     (remember A = 10)
Calculation: 1×16² + 10×16¹ + 3×16⁰
           = 256   + 160    + 3
           = 419

Answer: (419)₁₀  ✅
```

---

## 🔧 METHOD 3: Binary ↔ Octal ↔ Hex (The Group Trick)

This is the **fastest** method and the one you'll use the most. No math needed — just pattern matching!

### Binary → Octal: **Group by 3** (from the right)

```
Binary:   0 1 0 │ 1 1 1 │ 0 1 1
              ↓       ↓       ↓
Octal:        2       7       3

Answer: (010111011)₂ = (273)₈  ✅
```

> Pad with leading zeros if the leftmost group isn't complete!

### Binary → Hex: **Group by 4** (from the right)

```
Binary:   1 1 1 1 │ 1 0 1 0 │ 1 1 0 0 │ 0 0 1 0
              ↓         ↓         ↓         ↓
Hex:          F         A         C         2

Answer: (1111101011000010)₂ = (FAC2)₁₆  ✅
```

### Octal → Binary: Replace each digit with 3 bits
### Hex → Binary: Replace each digit with 4 bits

> These are just the reverse of the above! Use the tables from Module 2.

---

### What About Octal ↔ Hex?

**Go through binary as the middleman!**

```
Octal → Binary → Hex
 (273)₈ → (010 111 011)₂ → (0000 1011 1011)₂ → pad → (0BB)₁₆

Hex → Binary → Octal
 (FAC2)₁₆ → (1111 1010 1100 0010)₂ → (001 111 101 011 000 010)₂ → (175302)₈
```

---

## 📝 The Master Cheatsheet

| From → To | Method | Direction |
|-----------|--------|-----------|
| Decimal → Binary | Divide by 2, read remainders **bottom-up** | ↑ |
| Decimal → Octal | Divide by 8, read remainders **bottom-up** | ↑ |
| Decimal → Hex | Divide by 16, read remainders **bottom-up** | ↑ |
| Fraction → Binary | Multiply by 2, read integers **top-down** | ↓ |
| Binary → Decimal | Multiply digits × 2ⁿ, add all up | ← |
| Octal → Decimal | Multiply digits × 8ⁿ, add all up | ← |
| Hex → Decimal | Multiply digits × 16ⁿ, add all up | ← |
| Binary → Octal | Group by **3** from right | → |
| Binary → Hex | Group by **4** from right | → |
| Octal → Binary | Each digit → **3 bits** | → |
| Hex → Binary | Each digit → **4 bits** | → |
| Octal ↔ Hex | Go through **Binary** | → ← |

---

## 🏋️ Practice Problems (Do These — They WILL Appear on the Exam)

### Set 1: Decimal → Others
1. `(45)₁₀` → Binary, Octal, Hex
2. `(100)₁₀` → Binary, Octal, Hex
3. `(255)₁₀` → Binary, Octal, Hex
4. `(13.375)₁₀` → Binary

### Set 2: Others → Decimal
5. `(110101)₂` → Decimal
6. `(752)₈` → Decimal
7. `(2F3)₁₆` → Decimal

### Set 3: Group Trick
8. `(10110111)₂` → Octal, Hex
9. `(ABC)₁₆` → Binary → Octal
10. `(657)₈` → Binary → Hex

<details>
<summary>🔑 Answers</summary>

1. `(101101)₂`, `(55)₈`, `(2D)₁₆`
2. `(1100100)₂`, `(144)₈`, `(64)₁₆`
3. `(11111111)₂`, `(377)₈`, `(FF)₁₆`
4. `(1101.011)₂`
5. `53`
6. `490`
7. `755`
8. Octal: `(267)₈`, Hex: `(B7)₁₆`
9. Binary: `(101010111100)₂`, Octal: `(5274)₈`
10. Binary: `(110101111)₂`, Hex: `(1AF)₁₆`

</details>

---

## 🎯 Exam Pattern Recognition

> In the exam, number conversion questions are **free marks**. They follow the exact same steps every time. The only way to mess up is by rushing. Take 30 extra seconds to verify.

### Common question formats:
- "Convert (X)₁₀ to binary/octal/hex" → **METHOD 1**
- "Find the decimal equivalent of..." → **METHOD 2**
- "Convert (X)₈ to hexadecimal" → **METHOD 3** (go through binary)
- "Convert (X.Y)₁₀ to binary" → **METHOD 1** (both integer + fraction)

---

**⏱️ Time spent: ~20 minutes + practice. Module 1 complete! 🎉**

> Next up: Boolean Algebra & Logic Gates (coming when your class covers it)

---

*Remember: DLD isn't hard. It's just a lot of small, repeatable procedures. Learn the procedure → follow the steps → get the marks. You've got this.*
