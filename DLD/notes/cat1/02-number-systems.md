# 🔢 Module 1.2 — Number Systems

> **TL;DR**: There are 4 number systems. You already know Decimal. Binary = base 2, Octal = base 8, Hex = base 16. Learn the table below and you're 80% done.

---

## 🎯 The Big Picture

Computers don't speak human. They speak in **0s and 1s** (binary). But writing long binary numbers is painful, so we use **octal** and **hexadecimal** as shortcuts.

```
You:      "Two hundred fifty five"    → Decimal:     255
Computer: "one one one one one..."    → Binary:      11111111
Shortcut: "three seven seven"         → Octal:       377
Shortcut: "F F"                       → Hexadecimal: FF

ALL of these = the same number. Just different languages.
```

---

## 📋 The 4 Number Systems — One Table to Rule Them All

| System | Base (Radix) | Digits Used | Used By |
|--------|:---:|-------------|---------|
| **Binary** | 2 | 0, 1 | Computers internally |
| **Octal** | 8 | 0–7 | Old computers, some Linux stuff |
| **Decimal** | 10 | 0–9 | Humans (that's you!) |
| **Hexadecimal** | 16 | 0–9, A–F | Programmers, memory addresses, colors |

> 💡 **Key Rule**: A base-r system uses digits from **0 to (r−1)**
> - Base 2 → digits 0 to 1
> - Base 8 → digits 0 to 7
> - Base 16 → digits 0 to 15 (but 10=A, 11=B, 12=C, 13=D, 14=E, 15=F)

---

## 1️⃣ Binary Number System (Base 2)

The language of computers. Only two digits: **0** and **1**.

### Key Vocabulary

| Term | Meaning | Example |
|------|---------|---------|
| **Bit** | A single binary digit | `1` |
| **Nibble** | 4 bits | `1010` |
| **Byte** | 8 bits | `10110011` |
| **Word** | 16 bits | `1011001110100101` |

### How to Read Binary (Positional Value)

Each position = a power of 2, starting from the right:

```
Binary:    1    0    1    1    0
Position:  2⁴   2³   2²   2¹   2⁰
Value:     16   8    4    2    1

So: (10110)₂ = 16 + 0 + 4 + 2 + 0 = 22 in decimal
```

> 🧠 **Memory trick**: Just remember the powers of 2 → **1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024**. You'll use these constantly.

---

## 🔟 Decimal Number System (Base 10)

This is what you use every day. Nothing new here.

```
(2541)₁₀ = (2 × 10³) + (5 × 10²) + (4 × 10¹) + (1 × 10⁰)
         = 2000 + 500 + 40 + 1
         = 2541
```

The point? **Every number system works the same way** — multiply each digit by its position's power of the base.

---

## 8️⃣ Octal Number System (Base 8)

Uses digits **0 through 7** only. No 8, no 9!

### Why does it exist?
Each octal digit = exactly **3 binary bits**. So it's a compact way to write binary.

### Octal ↔ Binary Cheatsheet

| Octal | Binary |
|:---:|:---:|
| 0 | 000 |
| 1 | 001 |
| 2 | 010 |
| 3 | 011 |
| 4 | 100 |
| 5 | 101 |
| 6 | 110 |
| 7 | 111 |

> ⚡ **Shortcut**: To convert octal → binary, just replace each octal digit with its 3-bit binary equivalent. Done.
>
> Example: `(273)₈` → `2=010`, `7=111`, `3=011` → `(010111011)₂`

---

## 🔤 Hexadecimal Number System (Base 16)

Uses **0–9** and then **A–F** for values 10–15.

### Why does it exist?
Each hex digit = exactly **4 binary bits**. Even more compact than octal!

### Hex ↔ Binary Cheatsheet

| Hex | Decimal | Binary |
|:---:|:---:|:---:|
| 0 | 0 | 0000 |
| 1 | 1 | 0001 |
| 2 | 2 | 0010 |
| 3 | 3 | 0011 |
| 4 | 4 | 0100 |
| 5 | 5 | 0101 |
| 6 | 6 | 0110 |
| 7 | 7 | 0111 |
| 8 | 8 | 1000 |
| 9 | 9 | 1001 |
| A | 10 | 1010 |
| B | 11 | 1011 |
| C | 12 | 1100 |
| D | 13 | 1101 |
| E | 14 | 1110 |
| F | 15 | 1111 |

> ⚡ **Shortcut**: To convert hex → binary, replace each hex digit with its 4-bit binary. Done.
>
> Example: `(FAC2)₁₆` → `F=1111`, `A=1010`, `C=1100`, `2=0010` → `(1111101011000010)₂`

---

## 🧩 The Relationship Between Them

```
                    ┌─────────┐
                    │ BINARY  │ ← The universal language
                    │ (base 2)│
                    └────┬────┘
                         │
              ┌──────────┼──────────┐
              │          │          │
         ┌────▼───┐ ┌────▼───┐ ┌───▼────┐
         │ OCTAL  │ │DECIMAL │ │  HEX   │
         │(base 8)│ │(base10)│ │(base16)│
         └────────┘ └────────┘ └────────┘
          3 bits      math      4 bits
         per digit   we know   per digit
```

**Everything converts through binary.** That's the golden rule.

---

## ✅ Quick Self-Check (1 minute)

1. How many digits does hexadecimal use?
2. What letter represents the value 15 in hex?
3. Convert `(101)₂` to decimal in your head
4. How many bits is a nibble?
5. What's `(7)₈` in binary?

<details>
<summary>🔑 Answers</summary>

1. 16 (0-9 and A-F)
2. F
3. 4 + 0 + 1 = **5**
4. 4 bits
5. `111`

</details>

---

**⏱️ Time spent: ~10 minutes. Now the fun part →** [03 - Number Conversions](./03-number-conversions.md)
