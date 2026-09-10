# 📊 Lesson 3 — Data Preprocessing & Model Evaluation

> **TL;DR**: Before you feed data to an ML model, you have to clean it (remove junk, fill blanks, scale numbers). After the model makes predictions, you check how good it is using metrics. The big 4 metrics for exams: **Accuracy, Precision, Recall, F1-Score**. Learn the confusion matrix and you're golden.

---

## 🧹 Data Preprocessing — "Garbage In = Garbage Out"

Think of it like cooking. You wouldn't dump unwashed, unsorted, half-rotten vegetables into a pan and expect a good dish. Same with ML — you clean the data first.

### Step 1: Handle Missing Values

Your dataset has blank cells? Two options:

| Method | When to use | Example |
|---|---|---|
| **Fill with Mean/Median/Mode** | A few values missing | Age column missing 5 values → fill with average age |
| **Drop the row entirely** | Very few rows affected | Only 2 out of 10,000 rows are broken → just delete them |

### Step 2: Feature Scaling (The Tricky One)

**Problem**: If one feature is "Age" (0-100) and another is "Salary" (0-1,000,000), the model thinks salary is 10,000× more important just because the number is bigger. We fix this by scaling.

| Method | Formula | What it does |
|---|---|---|
| **Min-Max** | $X_{\text{norm}} = \frac{X - X_{\text{min}}}{X_{\text{max}} - X_{\text{min}}}$ | Squishes everything into $[0, 1]$ |
| **Z-Score (Standardization)** | $Z = \frac{X - \mu}{\sigma}$ | Centers around 0, spread = 1 |

> 🧠 **Memory Trick**: Min-Max = you know the range. Z-Score = you know the mean and standard deviation.

### Step 3: Encode Categories

ML models only understand numbers. So "Red", "Blue", "Green" needs to become numbers:

| Method | Example |
|---|---|
| **Label Encoding** | Red=0, Blue=1, Green=2 |
| **One-Hot Encoding** | Red=[1,0,0], Blue=[0,1,0], Green=[0,0,1] |

> 🤦 **Exam Trap**: Label Encoding implies an ordering (2 > 1 > 0), which is wrong for colors. Use One-Hot when categories have NO natural order.

---

## 🎯 Model Evaluation — "How Good Is Your Model?"

### The Confusion Matrix (Name Is Accurate — It Confuses Everyone)

|  | Predicted: YES | Predicted: NO |
|---|:---:|:---:|
| **Actually: YES** | ✅ **TP** (Correct YES) | ❌ **FN** (Missed it — Type II Error) |
| **Actually: NO** | ❌ **FP** (False alarm — Type I Error) | ✅ **TN** (Correct NO) |

> 🧠 **How to remember TP/FP/TN/FN**: First letter = was the model right? (True/False). Second letter = what did the model SAY? (Positive/Negative).

### The 4 Formulas (Memorize These, They're Worth 10+ Marks)

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} \quad \text{(Overall correctness)}$$

$$\text{Precision} = \frac{TP}{TP + FP} \quad \text{(Of all the YES predictions, how many were actually YES?)}$$

$$\text{Recall} = \frac{TP}{TP + FN} \quad \text{(Of all the ACTUAL YES cases, how many did we catch?)}$$

$$\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} \quad \text{(Balance of both)}$$

> 🤦 **THE Classic Exam Question**: "In cancer detection, which is more important — Precision or Recall?"
> **Answer**: **Recall**, because missing a cancer patient (False Negative) could kill them. A false alarm (False Positive) just means an extra test. Always prioritize catching ALL the positives.

---

## 🏋️ Solved Exam Practice Questions

### Question 1 (Confusion Matrix Numerical — 100% Appears on Exam)
**A medical ML model tested 100 patients:**
- 40 actually had disease: Model caught 30 correctly (TP=30), missed 10 (FN=10).
- 60 were healthy: Model correctly cleared 50 (TN=50), but falsely flagged 10 (FP=10).

**Calculate Accuracy, Precision, Recall, and F1-Score.**

<details>
<summary>💡 Step-by-Step Solution</summary>

Given: $TP = 30$, $TN = 50$, $FP = 10$, $FN = 10$.

1. $\text{Accuracy} = \frac{30 + 50}{100} = \frac{80}{100} = \mathbf{0.80}$ (80%)
2. $\text{Precision} = \frac{30}{30 + 10} = \frac{30}{40} = \mathbf{0.75}$ (75%)
3. $\text{Recall} = \frac{30}{30 + 10} = \frac{30}{40} = \mathbf{0.75}$ (75%)
4. $\text{F1} = 2 \times \frac{0.75 \times 0.75}{0.75 + 0.75} = 2 \times \frac{0.5625}{1.5} = \mathbf{0.75}$ (75%) ✅
</details>

---

## ✅ Quick Self-Check (30 seconds)

1. Which scaling method squishes values into [0, 1]?
2. In cancer detection — Precision or Recall? Why?
3. What's the harmonic mean of Precision and Recall called?

<details>
<summary>🔑 Answers</summary>

1. **Min-Max Normalization**.
2. **Recall** — missing a cancer patient (FN) is dangerous; a false alarm (FP) is just an extra test.
3. **F1-Score**.

</details>

---

**⏱️ Time spent: ~10 mins. Cheatsheet →** [ML Cheatsheet](./cheatsheet-ml.md)
