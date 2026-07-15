# ⚡ Day 1 Cheatsheet — Signals + Number Systems + Conversions

> **Print this. Stick it on your wall. Read it 5 min before the exam.**

---

## Signals
- **Analog** = continuous, smooth wave
- **Digital** = only 0 and 1, HIGH (+5V) and LOW (0V)
- Digital wins because: noise-proof, fast, cheap, programmable

---

## Number Systems at a Glance

| System | Base | Digits | 1 digit = ? bits |
|--------|:---:|--------|:-:|
| Binary | 2 | 0, 1 | 1 |
| Octal | 8 | 0–7 | 3 |
| Decimal | 10 | 0–9 | — |
| Hex | 16 | 0–F | 4 |

**Bit** = 1 digit &nbsp;|&nbsp; **Nibble** = 4 bits &nbsp;|&nbsp; **Byte** = 8 bits &nbsp;|&nbsp; **Word** = 16 bits

---

## Powers of 2 (memorize this row)

| 2⁰ | 2¹ | 2² | 2³ | 2⁴ | 2⁵ | 2⁶ | 2⁷ | 2⁸ | 2⁹ | 2¹⁰ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | 1024 |

---

## Hex Alphabet

| A=10 | B=11 | C=12 | D=13 | E=14 | F=15 |
|:----:|:----:|:----:|:----:|:----:|:----:|

---

## 3 Conversion Methods

### ① Decimal → Others: **DIVIDE, read remainders ↑ (bottom-up)**
```
Decimal → Binary:  ÷2
Decimal → Octal:   ÷8
Decimal → Hex:     ÷16
Fractions:         ×base, read integer parts ↓ (top-down)
```

### ② Others → Decimal: **digit × base^position, add all**
```
(1011)₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8+0+2+1 = 11
```

### ③ Binary ↔ Octal/Hex: **GROUP trick**
```
Binary → Octal:  group by 3 from right
Binary → Hex:    group by 4 from right
Octal ↔ Hex:     go through Binary!
```

---

## Common Conversions (just know these)

| Decimal | Binary | Octal | Hex |
|:---:|:---:|:---:|:---:|
| 0 | 0000 | 0 | 0 |
| 5 | 0101 | 5 | 5 |
| 10 | 1010 | 12 | A |
| 15 | 1111 | 17 | F |
| 16 | 10000 | 20 | 10 |
| 255 | 11111111 | 377 | FF |

---

*That's it. One page. All of Day 1.*
