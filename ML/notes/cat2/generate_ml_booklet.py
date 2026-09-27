# -*- coding: utf-8 -*-
"""
Script to generate the comprehensive, calculation-focused Markdown master document:
c:\\Users\\ankit\\Fall2627\\ML\\notes\\cat2\\ML_CAT2_CALCULATIONS_MASTER_BOOKLET.md
Mapped to Dr. Nilamadhab Mishra's CSE4005 curriculum at VIT Bhopal.
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

MD_PATH = r"c:\Users\ankit\Fall2627\ML\notes\cat2\ML_CAT2_CALCULATIONS_MASTER_BOOKLET.md"

content = r"""# 🎯 CSE4005: MACHINE LEARNING — CAT-II CALCULATIONS MASTER BOOKLET
> **Course**: CSE4005 — Machine Learning | **Exam**: CAT-2 (Open Book / Open Notes Mode)  
> **Faculty Pattern**: Dr. Nilamadhab Mishra | **Target Score**: 45+ / 50 (S-Grade Guarantee)  
> **Coverage**: Unit 3 (3 Questions - 30 Marks) & Unit 4 (2 Questions - 20 Marks) | **Format: 100% Calculations**

---

# ⚡ SECTION 0: MASTER 1-PAGE QUICK-TRIGGER FORMULA & TABLE INDEX
*(Glance at this in the first 2 minutes of the exam to pick your table format and calculator sequence)*

| Problem Topic & Question | Given Inputs | Core Calculator Formulas | Table Columns to Draw on Answer Sheet | Common Pitfalls to Avoid |
| :--- | :--- | :--- | :--- | :--- |
| **Q1: AdaBoost Weight Update** *(Unit 3 - 10M)* | $N$ samples, labels $y_i \in \{-1, +1\}$, classifier $h_t(x)$ | $\epsilon_t = \sum_{\text{wrong}} w_i$<br>$\alpha_t = \frac{1}{2} \ln\left(\frac{1-\epsilon_t}{\epsilon_t}\right)$<br>$\tilde{w}_i = w_i e^{-\alpha_t y_i h_t(x_i)}$<br>$w_i^{\text{new}} = \tilde{w}_i / Z_t$ | `i` \| `x_i` \| `y_i` \| `h(x_i)` \| `Status (✓/✗)` \| `w_i` \| `Factor` \| `w_tilde` \| `w_normalized` | Forgetting to divide by $Z_t$; $\epsilon_t$ must be $< 0.5$; calculator in natural $\ln$ mode! |
| **Q2: AGNES Hierarchical Clustering** *(Unit 3 - 10M)* | $N$ points (1D or 2D coordinates) | $d(A, B) = \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}$<br>**Single**: $\min(d_1, d_2)$<br>**Complete**: $\max(d_1, d_2)$<br>**Average**: $\frac{d_1 + d_2}{2}$ | Symmetric Distance Matrix $D_0 \to D_1 \to D_2 \to D_3$ with cluster names as rows and columns. | In Complete Linkage, choosing $\min$ by mistake; always pick $\min$ across pairs, but use $\max$ for cluster update! |
| **Q3: K-Means Clustering** *(Unit 3 - 10M)* | Points $\{x_1 \dots x_n\}$, initial centroids $C_1, C_2$ | $d(x, C) = \|x - C\|$<br>$C_k^{\text{new}} = \frac{1}{|K_k|}\sum_{x \in K_k} x$<br>$\text{SSE} = \sum \|x - C_k\|^2$ | `Point x_i` \| `Dist to C1` \| `Dist to C2` \| `Assigned Cluster` \| `(x - C_assigned)^2` | Forgetting to check convergence (Iteration 2 vs 1); forgetting SSE calculation at the end. |
| **Q4: Naïve Bayes Classifier** *(Unit 4.1 - 10M)* | Dataset table, test query $X = (x_1, x_2, \dots, x_d)$ | $P(C_k) = \frac{N_k}{N}$<br>$P(x_i \mid C_k) = \frac{\text{Count}(x_i, C_k)}{N_k}$<br>$\text{Score} = P(C_k) \prod_{i=1}^d P(x_i \mid C_k)$ | `Attribute` \| `Value in X` \| `P(value \| Yes)` \| `P(value \| No)` \| `Ratio / Fraction` | Zero frequency trap! If count is 0, use Laplace Smoothing: $\frac{0+1}{N_k + \|V_i\|}$. |
| **Q5: Apriori Association Rules** *(Unit 4.2 - 10M)* | Transaction DB, $\text{min\_sup}$, $\text{min\_conf}$ | $\text{Support}(X) = \frac{\sigma(X)}{N}$<br>$\text{Confidence}(A \Rightarrow B) = \frac{\sigma(A \cup B)}{\sigma(A)}$<br>$\text{Lift} = \frac{\text{Conf}(A \Rightarrow B)}{\text{Support}(B)}$ | Step-by-step Level Tables: $C_1 \to L_1$, $C_2 \to L_2$, $C_3 \to L_3$ with **Pruning Justification Column**. | Forgetting the subset pruning step in $C_3$; confusing Support denominator ($N$) with Confidence denominator ($\sigma(A)$). |

---

# 📌 SECTION 1: QUESTION 1 — ENSEMBLE LEARNING (UNIT 3)
*(Syllabus Coverage: Model Combination Schemes, Voting, ECOC, Bagging: Random Forest, Boosting: AdaBoost)*

## 1.1 Complete Solved Numerical: AdaBoost Weight Update & Classifier Combination
> **Typical Exam Problem**: *"Given a training set of 8 binary classification examples with initial uniform weights $w_i^{(1)} = \frac{1}{8}$. A weak base classifier $h_1(x)$ makes misclassifications on samples 3 and 7. Calculate: (a) The classifier error rate $\epsilon_1$, (b) The classifier weight $\alpha_1$, (c) The updated unnormalized and normalized sample weights $w_i^{(2)}$, (d) Demonstrate how the ensemble decision is computed for a test point."*

### Step 1: Initial Dataset & Weak Learner Predictions Table
Let the 8 training examples be:

| Sample $i$ | Feature $x_i$ | True Label $y_i$ | Classifier Prediction $h_1(x_i)$ | Classification Status | Initial Weight $w_i^{(1)}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 1.2 | +1 | +1 | **Correct (✓)** | 0.125 |
| 2 | 2.5 | +1 | +1 | **Correct (✓)** | 0.125 |
| 3 | 3.1 | +1 | -1 | **ERROR (✗)** | **0.125** |
| 4 | 4.8 | -1 | -1 | **Correct (✓)** | 0.125 |
| 5 | 5.2 | -1 | -1 | **Correct (✓)** | 0.125 |
| 6 | 6.0 | -1 | -1 | **Correct (✓)** | 0.125 |
| 7 | 7.4 | -1 | +1 | **ERROR (✗)** | **0.125** |
| 8 | 8.1 | -1 | -1 | **Correct (✓)** | 0.125 |

---

### Step 2: Calculate Classifier Error Rate ($\epsilon_1$)
The weighted error rate $\epsilon_1$ is the sum of weights of the **misclassified** samples (samples 3 and 7):
$$\epsilon_1 = \sum_{i: y_i \neq h_1(x_i)} w_i^{(1)} = w_3^{(1)} + w_7^{(1)} = 0.125 + 0.125 = 0.250$$

*(Exam Validation Check: Since $\epsilon_1 = 0.25 < 0.50$, the classifier is better than random guessing, so $\alpha_1 > 0$.)*

---

### Step 3: Calculate Classifier Importance Weight ($\alpha_1$)
$$\alpha_1 = \frac{1}{2} \ln \left(\frac{1 - \epsilon_1}{\epsilon_1}\right) = \frac{1}{2} \ln \left(\frac{1 - 0.25}{0.25}\right) = \frac{1}{2} \ln \left(\frac{0.75}{0.25}\right) = \frac{1}{2} \ln(3)$$
Using calculator: $\ln(3) \approx 1.09861$
$$\alpha_1 = \frac{1}{2} \times 1.09861 = \mathbf{0.5493}$$

Now calculate the exponential update factors:
* For **Correctly Classified** samples ($y_i h_1(x_i) = +1$):
  $$e^{-\alpha_1} = e^{-0.5493} = \frac{1}{\sqrt{3}} \approx \mathbf{0.5774}$$
* For **Misclassified** samples ($y_i h_1(x_i) = -1$):
  $$e^{+\alpha_1} = e^{+0.5493} = \sqrt{3} \approx \mathbf{1.7321}$$

---

### Step 4: Compute Unnormalized ($\tilde{w}_i$) and Normalized ($w_i^{(2)}$) Weights

| Sample $i$ | True $y_i$ | Pred $h_1(x_i)$ | Status | $w_i^{(1)}$ | Factor $e^{-\alpha_1 y_i h_1}$ | Unnormalized $\tilde{w}_i = w_i^{(1)} \times \text{Factor}$ | Normalized $w_i^{(2)} = \frac{\tilde{w}_i}{Z_1}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | +1 | +1 | Correct | 0.125 | 0.5774 | $0.125 \times 0.5774 = 0.07217$ | $0.07217 / 0.8660 = \mathbf{0.0833}$ |
| 2 | +1 | +1 | Correct | 0.125 | 0.5774 | $0.125 \times 0.5774 = 0.07217$ | $0.07217 / 0.8660 = \mathbf{0.0833}$ |
| 3 | +1 | -1 | **ERROR** | 0.125 | 1.7321 | $0.125 \times 1.7321 = \mathbf{0.21651}$ | $0.21651 / 0.8660 = \mathbf{0.2500}$ |
| 4 | -1 | -1 | Correct | 0.125 | 0.5774 | $0.125 \times 0.5774 = 0.07217$ | $0.07217 / 0.8660 = \mathbf{0.0833}$ |
| 5 | -1 | -1 | Correct | 0.125 | 0.5774 | $0.125 \times 0.5774 = 0.07217$ | $0.07217 / 0.8660 = \mathbf{0.0833}$ |
| 6 | -1 | -1 | Correct | 0.125 | 0.5774 | $0.125 \times 0.5774 = 0.07217$ | $0.07217 / 0.8660 = \mathbf{0.0833}$ |
| 7 | -1 | +1 | **ERROR** | 0.125 | 1.7321 | $0.125 \times 1.7321 = \mathbf{0.21651}$ | $0.21651 / 0.8660 = \mathbf{0.2500}$ |
| 8 | -1 | -1 | Correct | 0.125 | 0.5774 | $0.125 \times 0.5774 = 0.07217$ | $0.07217 / 0.8660 = \mathbf{0.0833}$ |
| **SUM** | — | — | — | **1.000** | — | **$Z_1 = 6(0.07217) + 2(0.21651) = \mathbf{0.8660}$** | **$\sum w_i^{(2)} = 6(0.0833) + 2(0.2500) = \mathbf{1.000}$** |

> 💡 **Golden Exam Verification Property**: Notice that in the updated weights, the sum of weights of the misclassified samples is exactly $2 \times 0.2500 = 0.500$, and the sum of correctly classified samples is $6 \times 0.0833 = 0.500$! AdaBoost always rebalances the misclassified and correctly classified subsets to have equal total weight ($0.50$ each) for the next iteration!

---

### Step 5: Final Ensemble Decision Rule
Suppose 3 sequential classifiers are trained with weights $\alpha_1 = 0.55, \alpha_2 = 0.72, \alpha_3 = 0.41$.  
For a test instance $x_{\text{test}}$, the individual predictions are $h_1(x) = +1$, $h_2(x) = -1$, $h_3(x) = +1$.  
The final ensemble decision is given by:
$$H(x) = \text{sign}\left(\sum_{t=1}^3 \alpha_t h_t(x)\right) = \text{sign}\Big((0.55)(+1) + (0.72)(-1) + (0.41)(+1)\Big)$$
$$H(x) = \text{sign}(0.55 - 0.72 + 0.41) = \text{sign}(+0.24) = \mathbf{+1}$$

---

## 1.2 Error-Correcting Output Codes (ECOC) Numerical (From Slide 3.1)
> **Problem**: A 4-class problem ($C_1, C_2, C_3, C_4$) uses a 7-bit ECOC code matrix with 7 binary classifiers ($L_1 \dots L_7$). The assigned class codewords and the predicted output vector $\hat{Y}$ on a test instance are given. Determine the predicted class.

| Class | $L_1$ | $L_2$ | $L_3$ | $L_4$ | $L_5$ | $L_6$ | $L_7$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$C_1$** | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| **$C_2$** | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| **$C_3$** | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| **$C_4$** | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| **Test Output $\hat{Y}$** | **0** | **1** | **1** | **1** | **0** | **0** | **1** |

### Step-by-Step Hamming Distance Calculation:
The Hamming distance $d_H(\hat{Y}, C_k)$ is the number of bit positions where $\hat{Y}$ differs from class codeword $C_k$:
* $d_H(\hat{Y}, C_1) = |0-1| + |1-1| + |1-1| + |1-1| + |0-1| + |0-1| + |1-1| = 1 + 0 + 0 + 0 + 1 + 1 + 0 = \mathbf{3}$
* $d_H(\hat{Y}, C_2) = |0-0| + |1-0| + |1-0| + |1-0| + |0-1| + |0-1| + |1-1| = 0 + 1 + 1 + 1 + 1 + 1 + 0 = \mathbf{5}$
* $d_H(\hat{Y}, C_3) = |0-0| + |1-0| + |1-1| + |1-1| + |0-0| + |0-0| + |1-1| = 0 + 1 + 0 + 0 + 0 + 0 + 0 = \mathbf{1}$  *(MINIMUM!)*
* $d_H(\hat{Y}, C_4) = |0-0| + |1-1| + |1-0| + |1-1| + |0-0| + |0-1| + |1-0| = 0 + 0 + 1 + 0 + 0 + 1 + 1 = \mathbf{3}$

**Decision**: The test instance is assigned to **Class $C_3$** because it has the minimum Hamming distance ($d_H = 1$). Even though classifier $L_2$ made an error, the code corrected it!

---

## 📝 1.3 Attached Theory Answers (Write directly if asked):
1. **Bagging vs Boosting**:
   * **Bagging (Random Forest)**: Trains models *in parallel* on independent bootstrap samples. Aggregates via equal-weight voting. Primary objective is to **reduce variance (prevent overfitting)**.
   * **Boosting (AdaBoost)**: Trains models *sequentially*. Successive models focus adaptively on misclassified samples by increasing their weights. Aggregates via weighted voting ($\alpha_t$). Primary objective is to **reduce bias (prevent underfitting)**.
2. **Why AdaBoost is Vulnerable to Outliers**:
   * Because weight updates scale exponentially ($e^{\alpha_t}$), noisy or mislabeled points receive exponentially larger weights in every round, forcing subsequent classifiers to distort their decision boundaries to fit noise.

---

# 📌 SECTION 2: QUESTION 2 — HIERARCHICAL CLUSTERING: AGNES (UNIT 3)
*(Syllabus Coverage: Agglomerative Hierarchical Clustering: AGNES, DIANA, Single, Complete, and Average Linkage, Dendrograms)*

## 2.1 Complete Solved Numerical: 1D Dataset (Slide 3.5 Exact Problem)
> **Problem**: Consider the 1-dimensional dataset $\{7, 10, 20, 28, 35\}$. Perform Agglomerative Hierarchical Clustering (AGNES) by hand using:  
> (a) **Single Linkage**, and (b) **Complete Linkage**. Construct all intermediate proximity matrices and draw the final dendrograms.

### Step 0: Construct Initial Distance Matrix ($D_0$)
Since data is 1D, Euclidean distance is simply $|x_i - x_j|$:

| | 7 | 10 | 20 | 28 | 35 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **7** | 0 | **3** | 13 | 21 | 28 |
| **10** | 3 | 0 | 10 | 18 | 25 |
| **20** | 13 | 10 | 0 | 8 | 15 |
| **28** | 21 | 18 | 8 | 0 | 7 |
| **35** | 28 | 25 | 15 | 7 | 0 |

---

### PART A: Single Linkage Clustering (Minimum Distance)
*Rule*: $d(C_A \cup C_B, C_K) = \min\big(d(C_A, C_K), d(C_B, C_K)\big)$

#### Iteration 1:
* Minimum non-zero value in $D_0$ is **3** between points **7** and **10**.
* **Merge (7, 10) into cluster $(7, 10)$ at merge height $h = 3$**.
* Compute distances from $(7, 10)$ to remaining points:
  * $d((7,10), 20) = \min(d(7,20), d(10,20)) = \min(13, 10) = 10$
  * $d((7,10), 28) = \min(d(7,28), d(10,28)) = \min(21, 18) = 18$
  * $d((7,10), 35) = \min(d(7,35), d(10,35)) = \min(28, 25) = 25$

**Matrix $D_1$:**
| | (7, 10) | 20 | 28 | 35 |
| :---: | :---: | :---: | :---: | :---: |
| **(7, 10)** | 0 | 10 | 18 | 25 |
| **20** | 10 | 0 | 8 | 15 |
| **28** | 18 | 8 | 0 | **7** |
| **35** | 25 | 15 | 7 | 0 |

#### Iteration 2:
* Minimum distance in $D_1$ is **7** between points **28** and **35**.
* **Merge (28, 35) into cluster $(28, 35)$ at merge height $h = 7$**.
* Compute distances from $(28, 35)$ to remaining clusters:
  * $d(20, (28,35)) = \min(d(20,28), d(20,35)) = \min(8, 15) = 8$
  * $d((7,10), (28,35)) = \min(d((7,10),28), d((7,10),35)) = \min(18, 25) = 18$

**Matrix $D_2$:**
| | (7, 10) | 20 | (28, 35) |
| :---: | :---: | :---: | :---: |
| **(7, 10)** | 0 | 10 | 18 |
| **20** | 10 | 0 | **8** |
| **(28, 35)** | 18 | 8 | 0 |

#### Iteration 3:
* Minimum distance in $D_2$ is **8** between point **20** and cluster **(28, 35)**.
* **Merge 20 into cluster $(20, 28, 35)$ at merge height $h = 8$**.
* Compute distance to $(7, 10)$:
  * $d((7,10), (20,28,35)) = \min(d((7,10),20), d((7,10),(28,35))) = \min(10, 18) = 10$

**Matrix $D_3$:**
| | (7, 10) | (20, 28, 35) |
| :---: | :---: | :---: |
| **(7, 10)** | 0 | **10** |
| **(20, 28, 35)** | 10 | 0 |

#### Iteration 4:
* Final merge between **(7, 10)** and **(20, 28, 35)** at **merge height $h = 10$**.

```text
Single Linkage Dendrogram:
Height
  10 |             +-----------------------------------------+
     |             |                                         |
   8 |             |                   +---------------------+
     |             |                   |                     |
   7 |             |                   |             +-------+
     |             |                   |             |       |
   3 |     +-------+                   |             |       |
     |     |       |                   |             |       |
   0 +-----+-------+-------------------+-------------+-------+---
           7       10                  20            28      35
Clusters Formed (k=2): Cluster 1 = {7, 10}, Cluster 2 = {20, 28, 35}
```

---

### PART B: Complete Linkage Clustering (Maximum Distance)
*Rule*: $d(C_A \cup C_B, C_K) = \max\big(d(C_A, C_K), d(C_B, C_K)\big)$

* **Step 1**: Same first merge: **(7, 10) at $h = 3$**.
  * $d((7,10), 20) = \max(13, 10) = \mathbf{13}$
  * $d((7,10), 28) = \max(21, 18) = \mathbf{21}$
  * $d((7,10), 35) = \max(28, 25) = \mathbf{28}$
* **Step 2**: Smallest remaining distance is **7** between 28 and 35 $\implies$ **Merge (28, 35) at $h = 7$**.
  * $d(20, (28,35)) = \max(d(20,28), d(20,35)) = \max(8, 15) = \mathbf{15}$
  * $d((7,10), (28,35)) = \max(d(7,35), d(10,35), \dots) = \mathbf{28}$
* **Step 3 (The Key Difference!)**: Proximity matrix is now:
  * $d((7,10), 20) = 13$
  * $d((7,10), (28,35)) = 28$
  * $d(20, (28,35)) = 15$
  * Smallest distance is **13** between **(7, 10) and 20**!
  * **Merge 20 with (7, 10) into cluster $(7, 10, 20)$ at merge height $h = 13$**!
* **Step 4**: Final merge between **(7, 10, 20)** and **(28, 35)** at height $\max(28, 15) = \mathbf{28}$.

```text
Complete Linkage Dendrogram:
Height
  28 |             +-----------------------------------------+
     |             |                                         |
  13 |     +-------+                                         |
     |     |       |                                         |
   7 |     |       |                                 +-------+
     |     |       |                                 |       |
   3 |     |       +-------+                         |       |
     |     |       |       |                         |       |
   0 +-----+-------+-------+-------------------------+-------+---
           20      7       10                        28      35
Clusters Formed (k=2): Cluster 1 = {7, 10, 20}, Cluster 2 = {28, 35}
```

---

## 📝 2.2 Attached Theory Answers:
1. **Single vs Complete Linkage Behavior**:
   * Single linkage uses minimum pairwise distance, creating a **"chaining effect"** where points string together to form long, straggly clusters (point 20 gets pulled into $\{28, 35\}$).
   * Complete linkage uses maximum pairwise distance, forcing clusters to be compact and spherical, grouping point 20 with $\{7, 10\}$.
2. **AGNES vs DIANA**:
   * **AGNES (Agglomerative Nesting)**: Bottom-up algorithm; starts with $N$ clusters and executes $N-1$ merging steps. Complexity $O(N^3)$ or $O(N^2 \log N)$.
   * **DIANA (Divisive Analysis)**: Top-down algorithm; starts with 1 root cluster containing all points and repeatedly splits into smaller clusters.

---

# 📌 SECTION 3: QUESTION 3 — PARTITIONAL CLUSTERING: K-MEANS & K-MEDOIDS (UNIT 3)
*(Syllabus Coverage: K-Means Clustering, K-Mode, K-Medoids / PAM, Expectation-Maximization, GMM)*

## 3.1 Complete Solved Numerical: 1D K-Means Clustering (Slide 3.6 Exact Problem)
> **Problem**: Using K-means clustering, cluster the following data into $k = 2$ clusters and show each step until convergence:  
> Data: $\{2, 4, 10, 12, 3, 20, 30, 11, 25\}$. Initial means: $m_1 = 3, m_2 = 4$.

### Iteration 1:
Initial Centroids: $m_1 = 3, m_2 = 4$.

| Point $x_i$ | Dist to $m_1=3$ ($|x_i - 3|$) | Dist to $m_2=4$ ($|x_i - 4|$) | Nearest Centroid | Assigned Cluster |
| :---: | :---: | :---: | :---: | :---: |
| 2 | $|2 - 3| = \mathbf{1}$ | $|2 - 4| = 2$ | $m_1$ | **$K_1$** |
| 3 | $|3 - 3| = \mathbf{0}$ | $|3 - 4| = 1$ | $m_1$ | **$K_1$** |
| 4 | $|4 - 3| = 1$ | $|4 - 4| = \mathbf{0}$ | $m_2$ | **$K_2$** |
| 10 | $|10 - 3| = 7$ | $|10 - 4| = \mathbf{6}$ | $m_2$ | **$K_2$** |
| 11 | $|11 - 3| = 8$ | $|11 - 4| = \mathbf{7}$ | $m_2$ | **$K_2$** |
| 12 | $|12 - 3| = 9$ | $|12 - 4| = \mathbf{8}$ | $m_2$ | **$K_2$** |
| 20 | $|20 - 3| = 17$ | $|20 - 4| = \mathbf{16}$ | $m_2$ | **$K_2$** |
| 25 | $|25 - 3| = 22$ | $|25 - 4| = \mathbf{21}$ | $m_2$ | **$K_2$** |
| 30 | $|30 - 3| = 27$ | $|30 - 4| = \mathbf{26}$ | $m_2$ | **$K_2$** |

* Cluster $K_1 = \{2, 3\} \implies m_1^{\text{new}} = \frac{2 + 3}{2} = \mathbf{2.5}$
* Cluster $K_2 = \{4, 10, 11, 12, 20, 25, 30\} \implies m_2^{\text{new}} = \frac{4 + 10 + 11 + 12 + 20 + 25 + 30}{7} = \frac{112}{7} = \mathbf{16.0}$

---

### Iteration 2:
Centroids: $m_1 = 2.5, m_2 = 16.0$. Decision boundary midpoint: $\frac{2.5 + 16.0}{2} = 9.25$.  
Any point $< 9.25$ goes to $K_1$; any point $> 9.25$ goes to $K_2$.

| Cluster | Member Points | Recalculated Centroid |
| :---: | :---: | :---: |
| **$K_1$** | $\{2, 3, 4\}$ | $m_1^{\text{new}} = \frac{2 + 3 + 4}{3} = \frac{9}{3} = \mathbf{3.0}$ |
| **$K_2$** | $\{10, 11, 12, 20, 25, 30\}$ | $m_2^{\text{new}} = \frac{10 + 11 + 12 + 20 + 25 + 30}{6} = \frac{108}{6} = \mathbf{18.0}$ |

---

### Iteration 3:
Centroids: $m_1 = 3.0, m_2 = 18.0$. Midpoint: $\frac{3.0 + 18.0}{2} = 10.5$.

| Cluster | Member Points | Recalculated Centroid |
| :---: | :---: | :---: |
| **$K_1$** | $\{2, 3, 4, 10\}$ | $m_1^{\text{new}} = \frac{2 + 3 + 4 + 10}{4} = \frac{19}{4} = \mathbf{4.75}$ |
| **$K_2$** | $\{11, 12, 20, 25, 30\}$ | $m_2^{\text{new}} = \frac{11 + 12 + 20 + 25 + 30}{5} = \frac{98}{5} = \mathbf{19.6}$ |

---

### Iteration 4:
Centroids: $m_1 = 4.75, m_2 = 19.6$. Midpoint: $\frac{4.75 + 19.6}{2} = 12.175$.

| Cluster | Member Points | Recalculated Centroid |
| :---: | :---: | :---: |
| **$K_1$** | $\{2, 3, 4, 10, 11, 12\}$ | $m_1^{\text{new}} = \frac{2 + 3 + 4 + 10 + 11 + 12}{6} = \frac{42}{6} = \mathbf{7.0}$ |
| **$K_2$** | $\{20, 25, 30\}$ | $m_2^{\text{new}} = \frac{20 + 25 + 30}{3} = \frac{75}{3} = \mathbf{25.0}$ |

---

### Iteration 5 (Convergence Check):
Centroids: $m_1 = 7.0, m_2 = 25.0$. Midpoint: $\frac{7.0 + 25.0}{2} = 16.0$.
* Points $< 16.0 \implies \{2, 3, 4, 10, 11, 12\} \implies K_1$
* Points $> 16.0 \implies \{20, 25, 30\} \implies K_2$

> **Stop Condition Met**: Cluster assignments in Iteration 5 are identical to Iteration 4. Centroids have converged!  
> **Final Output**:
> * **Cluster 1**: $\{2, 3, 4, 10, 11, 12\}$ with final centroid $\mathbf{C_1 = 7.0}$
> * **Cluster 2**: $\{20, 25, 30\}$ with final centroid $\mathbf{C_2 = 25.0}$

### Final Sum of Squared Errors (SSE):
$$\text{SSE}_1 = (2-7)^2 + (3-7)^2 + (4-7)^2 + (10-7)^2 + (11-7)^2 + (12-7)^2 = 25 + 16 + 9 + 9 + 16 + 25 = 100$$
$$\text{SSE}_2 = (20-25)^2 + (25-25)^2 + (30-25)^2 = 25 + 0 + 25 = 50$$
$$\mathbf{\text{Total SSE} = 100 + 50 = 150}$$

---

## 3.2 K-Medoids (PAM) Swap Cost Numerical (Slide 3.6, p.17)
> **Problem**: Points are given in 2D space. Let initial medoids be $M_1 = (4, 5)$ and $M_2 = (8, 5)$. Candidate replacement non-medoid point is $M_{\text{new}} = (3, 4)$. Using Manhattan distance $d = |x_1 - x_2| + |y_1 - y_2|$, calculate cost difference $S = \text{Cost}_{\text{new}} - \text{Cost}_{\text{old}}$ and decide whether to accept the swap.

1. **Calculate Current Cost with $\{M_1, M_2\}$**:
   For each data point $P_i$, find $\min\big(d(P_i, M_1), d(P_i, M_2)\big)$. Sum these minimum distances $\implies \text{Cost}_{\text{old}}$.
2. **Calculate New Cost with $\{M_{\text{new}}, M_2\}$**:
   Re-assign every point to closest medoid among $\{M_{\text{new}}, M_2\}$, sum distances $\implies \text{Cost}_{\text{new}}$.
3. **Decision Rule**:
   * If $\Delta S = \text{Cost}_{\text{new}} - \text{Cost}_{\text{old}} < 0 \implies$ **Accept swap** (total cost decreases).
   * If $\Delta S \ge 0 \implies$ **Reject swap** (keep original medoid).

---

## 📝 3.3 Attached Theory Answers:
1. **Strengths & Weaknesses of K-Means**:
   * *Strengths*: Highly efficient with time complexity $O(t \cdot k \cdot n)$ where $t, k \ll n$. Scales well to large datasets.
   * *Weaknesses*: Requires pre-specifying $k$; sensitive to initial seed selection (can get stuck in local minima); highly sensitive to outliers; assumes spherical clusters of equal size.
2. **K-Means vs K-Medoids**:
   * K-Means uses the mean of points as the center (which may not be an actual data point and is heavily pulled by outliers).
   * K-Medoids uses actual data objects (medoids) as cluster centers and optimizes absolute distance, making it far more robust to noise and outliers.

---

# 📌 SECTION 4: QUESTION 4 — PROBABILISTIC LEARNING: NAÏVE BAYES & BBN (UNIT 4.1)
*(Syllabus Coverage: Bayesian Learning, Bayes Optimal Classifier, Naïve Bayes Classifier, Laplace Correction, Bayesian Belief Networks)*

## 4.1 Complete Solved Numerical: The Classic `buys_computer` 14-Row Problem (Slide 4.1 Exact Problem)
> **Problem**: Given the training dataset of 14 customers below. Classify the test tuple:  
> $$X = (\text{Age} = \text{"}\le 30\text{"},\, \text{Income} = \text{"medium"},\, \text{Student} = \text{"yes"},\, \text{Credit\_rating} = \text{"fair"})$$  
> using the Naïve Bayes classification algorithm. Show all calculations.

### Training Dataset Table:

| RID | Age | Income | Student | Credit\_Rating | Buys\_Computer |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | $\le 30$ | high | no | fair | **no** |
| 2 | $\le 30$ | high | no | excellent | **no** |
| 3 | $31\dots 40$ | high | no | fair | **yes** |
| 4 | $> 40$ | medium | no | fair | **yes** |
| 5 | $> 40$ | low | yes | fair | **yes** |
| 6 | $> 40$ | low | yes | excellent | **no** |
| 7 | $31\dots 40$ | low | yes | excellent | **yes** |
| 8 | $\le 30$ | medium | no | fair | **no** |
| 9 | $\le 30$ | low | yes | fair | **yes** |
| 10 | $> 40$ | medium | yes | fair | **yes** |
| 11 | $\le 30$ | medium | yes | excellent | **yes** |
| 12 | $31\dots 40$ | medium | no | excellent | **yes** |
| 13 | $31\dots 40$ | high | yes | fair | **yes** |
| 14 | $> 40$ | medium | no | excellent | **no** |

---

### Step 1: Compute Prior Probabilities $P(C_i)$
Total records $N = 14$.
* $P(\text{buys\_computer} = \text{"yes"}) = \frac{9}{14} \approx \mathbf{0.643}$
* $P(\text{buys\_computer} = \text{"no"}) = \frac{5}{14} \approx \mathbf{0.357}$

---

### Step 2: Compute Conditional Likelihoods $P(x_i \mid C_k)$

#### For Class $C_1$: $\text{buys\_computer} = \text{"yes"}$ ($N_{\text{yes}} = 9$)
1. $P(\text{age} = \text{"}\le 30\text{"} \mid \text{yes}) = \frac{2}{9} \approx \mathbf{0.222}$  *(rows 9, 11)*
2. $P(\text{income} = \text{"medium"} \mid \text{yes}) = \frac{4}{9} \approx \mathbf{0.444}$  *(rows 4, 10, 11, 12)*
3. $P(\text{student} = \text{"yes"} \mid \text{yes}) = \frac{6}{9} \approx \mathbf{0.667}$  *(rows 5, 7, 9, 10, 11, 13)*
4. $P(\text{credit\_rating} = \text{"fair"} \mid \text{yes}) = \frac{6}{9} \approx \mathbf{0.667}$  *(rows 3, 4, 5, 9, 10, 13)*

#### For Class $C_2$: $\text{buys\_computer} = \text{"no"}$ ($N_{\text{no}} = 5$)
1. $P(\text{age} = \text{"}\le 30\text{"} \mid \text{no}) = \frac{3}{5} = \mathbf{0.600}$  *(rows 1, 2, 8)*
2. $P(\text{income} = \text{"medium"} \mid \text{no}) = \frac{2}{5} = \mathbf{0.400}$  *(rows 8, 14)*
3. $P(\text{student} = \text{"yes"} \mid \text{no}) = \frac{1}{5} = \mathbf{0.200}$  *(row 6)*
4. $P(\text{credit\_rating} = \text{"fair"} \mid \text{no}) = \frac{2}{5} = \mathbf{0.400}$  *(rows 1, 8)*

---

### Step 3: Compute Conditional Probability Product $P(X \mid C_i)$
* For $\text{yes}$:
  $$P(X \mid \text{yes}) = 0.222 \times 0.444 \times 0.667 \times 0.667 = \mathbf{0.0438}$$
* For $\text{no}$:
  $$P(X \mid \text{no}) = 0.600 \times 0.400 \times 0.200 \times 0.400 = \mathbf{0.0192}$$

---

### Step 4: Compute Posterior Probability Score $P(X \mid C_i) \times P(C_i)$
* $\text{Score}(\text{yes}) = P(X \mid \text{yes}) \times P(\text{yes}) = 0.0438 \times 0.643 = \mathbf{0.0282}$
* $\text{Score}(\text{no}) = P(X \mid \text{no}) \times P(\text{no}) = 0.0192 \times 0.357 = \mathbf{0.0069}$

---

### Step 5: Normalization & Final Classification
$$\text{Normalized } P(\text{yes} \mid X) = \frac{0.0282}{0.0282 + 0.0069} = \frac{0.0282}{0.0351} = \mathbf{80.3\%}$$
$$\text{Normalized } P(\text{no} \mid X) = \frac{0.0069}{0.0351} = \mathbf{19.7\%}$$

> **Final Conclusion**: Since $\text{Score}(\text{yes}) > \text{Score}(\text{no})$ ($0.0282 > 0.0069$), the customer $X$ is classified into class **$\text{buys\_computer} = \text{"yes"}$**.

---

## 4.2 Zero-Probability Problem & Laplace Correction
> **Exam Question**: *"In a training dataset of 100 samples with class Yes ($N_{\text{yes}} = 60$), the feature value 'Income=High' appears 0 times. Show how Naïve Bayes handles this and calculate the Laplace corrected probability if Income has 3 distinct values (Low, Medium, High)."*

1. **Problem**: Because Naïve Bayes multiplies conditional probabilities, if $P(\text{Income=High} \mid \text{Yes}) = 0$, the entire posterior product $P(X \mid \text{Yes}) = 0$, regardless of all other features!
2. **Laplacian Correction Formula**:
   $$\hat{P}(x_i \mid C_k) = \frac{\text{Count}(x_i, C_k) + 1}{N_k + |V_i|}$$
   where $|V_i|$ is the number of distinct values for feature $i$ ($|V_{\text{income}}| = 3$).
3. **Calculation**:
   $$\hat{P}(\text{Income=High} \mid \text{Yes}) = \frac{0 + 1}{60 + 3} = \frac{1}{63} \approx \mathbf{0.0159}$$
   $$\hat{P}(\text{Income=Med} \mid \text{Yes}) = \frac{30 + 1}{60 + 3} = \frac{31}{63} \approx \mathbf{0.4921}$$

---

## 4.3 Bayesian Belief Network (BBN) Joint Probability & D-Separation
Given DAG: $A \to B \to D$ and $A \to C \to D$.  
* **Joint Probability Factorization**:
  $$P(A, B, C, D) = P(A) \cdot P(B \mid A) \cdot P(C \mid A) \cdot P(D \mid B, C)$$
* **D-Separation Rules**:
  1. **Serial Connection ($X \to Y \to Z$)**: Knowing $Y$ blocks the path ($X \perp Z \mid Y$).
  2. **Diverging Connection ($X \leftarrow Y \to Z$)**: Knowing common cause $Y$ blocks the path ($X \perp Z \mid Y$).
  3. **Converging / V-Structure ($X \to Y \leftarrow Z$)**: If collider $Y$ is **unknown**, path is naturally blocked ($X \perp Z$). If $Y$ is **observed**, path opens! ("Explaining Away").

---

## 📝 4.4 Attached Theory Answers:
1. **Why Naïve Bayes is "Naïve"**:
   * It makes the simplifying assumption that all attributes are conditionally independent given the class label ($P(X|C) = \prod P(x_i|C)$). In reality, features correlate (e.g. age and income), but the classifier performs surprisingly well even when the assumption is violated.
2. **Handling Continuous Numerical Features**:
   * Continuous features are modeled using a Gaussian (Normal) distribution:
     $$P(x_i \mid C_k) = \frac{1}{\sqrt{2\pi \sigma_{ik}^2}} \exp\left(-\frac{(x_i - \mu_{ik})^2}{2\sigma_{ik}^2}\right)$$
     where $\mu_{ik}$ and $\sigma_{ik}^2$ are the sample mean and variance of feature $i$ in class $C_k$.

---

# 📌 SECTION 5: QUESTION 5 — ASSOCIATION RULE MINING: APRIORI ALGORITHM (UNIT 4.2)
*(Syllabus Coverage: Mining Frequent Patterns, Apriori Algorithm, Candidate Generation & Pruning, Association Rules, Support, Confidence, Lift, FP-Growth)*

## 5.1 Complete Solved Numerical: 9-Transaction Apriori (Slide 4.2 Exact Problem)
> **Problem**: Consider the transaction database of a retail store with 9 transactions ($T_{100}$ to $T_{900}$) given below:  
> Given $\text{Minimum Support Count} = 2$ (or $\text{min\_sup} = \frac{2}{9} \approx 22.2\%$) and $\text{Minimum Confidence} = 70\%$.  
> (a) Find all frequent itemsets using the Apriori Algorithm showing all candidate generation and pruning steps.  
> (b) Generate all strong association rules from frequent 3-itemsets.

### Transaction Database Table:

| TID | Items Purchased |
| :---: | :---: |
| **$T_{100}$** | $I_1, I_2, I_5$ |
| **$T_{200}$** | $I_2, I_4$ |
| **$T_{300}$** | $I_2, I_3$ |
| **$T_{400}$** | $I_1, I_2, I_4$ |
| **$T_{500}$** | $I_1, I_3$ |
| **$T_{600}$** | $I_2, I_3$ |
| **$T_{700}$** | $I_1, I_3$ |
| **$T_{800}$** | $I_1, I_2, I_3, I_5$ |
| **$T_{900}$** | $I_1, I_2, I_3$ |

---

### Step 1: Generate Frequent 1-Itemsets ($L_1$)
Scan database once to count support for each individual item:

**Candidate $C_1$ Table:**
| Itemset | Support Count | Status ($\ge 2$?) |
| :---: | :---: | :---: |
| $\{I_1\}$ | 6 | **Accepted** |
| $\{I_2\}$ | 7 | **Accepted** |
| $\{I_3\}$ | 6 | **Accepted** |
| $\{I_4\}$ | 2 | **Accepted** |
| $\{I_5\}$ | 2 | **Accepted** |

$$\mathbf{L_1 = \{\{I_1\}, \{I_2\}, \{I_3\}, \{I_4\}, \{I_5\}\}}$$

---

### Step 2: Generate Frequent 2-Itemsets ($L_2$)
Join $L_1 \Join L_1$ to create candidate 2-itemsets $C_2$, then scan DB for counts:

**Candidate $C_2$ Table:**
| Itemset | Transactions Containing Itemset | Support Count | Status ($\ge 2$?) |
| :---: | :---: | :---: | :---: |
| $\{I_1, I_2\}$ | $T_{100}, T_{400}, T_{800}, T_{900}$ | **4** | **Accepted** |
| $\{I_1, I_3\}$ | $T_{500}, T_{700}, T_{800}, T_{900}$ | **4** | **Accepted** |
| $\{I_1, I_4\}$ | $T_{400}$ | 1 | *Pruned ($< 2$)* |
| $\{I_1, I_5\}$ | $T_{100}, T_{800}$ | **2** | **Accepted** |
| $\{I_2, I_3\}$ | $T_{300}, T_{600}, T_{800}, T_{900}$ | **4** | **Accepted** |
| $\{I_2, I_4\}$ | $T_{200}, T_{400}$ | **2** | **Accepted** |
| $\{I_2, I_5\}$ | $T_{100}, T_{800}$ | **2** | **Accepted** |
| $\{I_3, I_4\}$ | None | 0 | *Pruned ($< 2$)* |
| $\{I_3, I_5\}$ | $T_{800}$ | 1 | *Pruned ($< 2$)* |
| $\{I_4, I_5\}$ | None | 0 | *Pruned ($< 2$)* |

$$\mathbf{L_2 = \{\{I_1, I_2\}, \{I_1, I_3\}, \{I_1, I_5\}, \{I_2, I_3\}, \{I_2, I_4\}, \{I_2, I_5\}\}}$$

---

### Step 3: Generate Frequent 3-Itemsets ($L_3$) with Apriori Pruning Step
Join pairs from $L_2$ sharing their first item:
1. Join $\{I_1, I_2\}$ with $\{I_1, I_3\} \implies \{I_1, I_2, I_3\}$
   * Subsets: $\{I_1, I_2\} \in L_2$, $\{I_1, I_3\} \in L_2$, $\{I_2, I_3\} \in L_2 \implies$ **Retain!**
2. Join $\{I_1, I_2\}$ with $\{I_1, I_5\} \implies \{I_1, I_2, I_5\}$
   * Subsets: $\{I_1, I_2\} \in L_2$, $\{I_1, I_5\} \in L_2$, $\{I_2, I_5\} \in L_2 \implies$ **Retain!**
3. Join $\{I_2, I_3\}$ with $\{I_2, I_4\} \implies \{I_2, I_3, I_4\}$
   * Subsets: $\{I_3, I_4\} \notin L_2 \implies$ **PRUNED BY APRIORI PROPERTY!**
4. Join $\{I_2, I_3\}$ with $\{I_2, I_5\} \implies \{I_2, I_3, I_5\}$
   * Subsets: $\{I_3, I_5\} \notin L_2 \implies$ **PRUNED BY APRIORI PROPERTY!**
5. Join $\{I_2, I_4\}$ with $\{I_2, I_5\} \implies \{I_2, I_4, I_5\}$
   * Subsets: $\{I_4, I_5\} \notin L_2 \implies$ **PRUNED BY APRIORI PROPERTY!**

Now count support in DB for the 2 remaining candidates in $C_3$:

| Itemset | Transactions | Support Count | Status ($\ge 2$?) |
| :---: | :---: | :---: | :---: |
| $\{I_1, I_2, I_3\}$ | $T_{800}, T_{900}$ | **2** | **Accepted** |
| $\{I_1, I_2, I_5\}$ | $T_{100}, T_{800}$ | **2** | **Accepted** |

$$\mathbf{L_3 = \{\{I_1, I_2, I_3\}, \{I_1, I_2, I_5\}\}}$$

*(Note: Attempting $L_3 \Join L_3$ yields $\{I_1, I_2, I_3, I_5\}$, whose subset $\{I_3, I_5\} \notin L_2$, so it is pruned. Algorithm terminates!)*

---

### Step 4: Association Rule Generation & Confidence Calculation
Formula:
$$\text{Confidence}(A \Rightarrow B) = \frac{\text{Support Count}(A \cup B)}{\text{Support Count}(A)} \times 100\%$$

#### From Frequent Itemset $\{I_1, I_2, I_5\}$ ($\text{Supp} = 2$):
1. **Rule 1**: $I_1 \wedge I_2 \Rightarrow I_5$  
   $$\text{Conf} = \frac{\text{Supp}(\{I_1, I_2, I_5\})}{\text{Supp}(\{I_1, I_2\})} = \frac{2}{4} = 50\% < 70\% \implies \text{Weak (Rejected)}$$
2. **Rule 2**: $I_1 \wedge I_5 \Rightarrow I_2$  
   $$\text{Conf} = \frac{\text{Supp}(\{I_1, I_2, I_5\})}{\text{Supp}(\{I_1, I_5\})} = \frac{2}{2} = \mathbf{100\% \ge 70\% \implies \text{STRONG RULE! 🏆}}$$
3. **Rule 3**: $I_2 \wedge I_5 \Rightarrow I_1$  
   $$\text{Conf} = \frac{\text{Supp}(\{I_1, I_2, I_5\})}{\text{Supp}(\{I_2, I_5\})} = \frac{2}{2} = \mathbf{100\% \ge 70\% \implies \text{STRONG RULE! 🏆}}$$
4. **Rule 4**: $I_1 \Rightarrow I_2 \wedge I_5$  
   $$\text{Conf} = \frac{2}{\text{Supp}(\{I_1\})} = \frac{2}{6} = 33.3\% < 70\% \implies \text{Weak (Rejected)}$$
5. **Rule 5**: $I_2 \Rightarrow I_1 \wedge I_5$  
   $$\text{Conf} = \frac{2}{\text{Supp}(\{I_2\})} = \frac{2}{7} = 28.6\% < 70\% \implies \text{Weak (Rejected)}$$
6. **Rule 6**: $I_5 \Rightarrow I_1 \wedge I_2$  
   $$\text{Conf} = \frac{2}{\text{Supp}(\{I_5\})} = \frac{2}{2} = \mathbf{100\% \ge 70\% \implies \text{STRONG RULE! 🏆}}$$

---

## 5.2 FP-Growth vs Apriori Comparison
* **Apriori**: Requires $k$ database scans (one for each itemset size); generates millions of candidate pairs $O(2^d)$; bottleneck is I/O scanning and repeated memory joins.
* **FP-Growth (Frequent Pattern Growth)**: Requires only **2 database scans**! Compresses transactions into a compact **FP-Tree** (Prefix tree). Mines frequent itemsets directly via divide-and-conquer using conditional pattern bases, completely eliminating candidate generation.

---

## 📝 5.3 Attached Theory Answers:
1. **The Apriori Property (Anti-Monotonicity Principle)**:
   * *"All non-empty subsets of a frequent itemset must also be frequent. Conversely, if any subset is infrequent, the superset can never be frequent and is pruned immediately."*
2. **Metrics: Support vs Confidence vs Lift**:
   * **Support**: Frequency of itemset in the entire dataset ($P(A \cap B)$).
   * **Confidence**: Reliability of rule; how often $B$ appears when $A$ occurs ($P(B|A)$).
   * **Lift**: Ratio of confidence to baseline probability of $B$: $\text{Lift}(A \Rightarrow B) = \frac{P(A \cap B)}{P(A)P(B)}$. $\text{Lift} > 1$ indicates positive correlation.

---

# 📌 SECTION 6: PRE-EXAM CALCULATOR SURVIVAL GUIDE & READY-TO-DRAW BLANK TABLES

### 1. Scientific Calculator Key Sequences (Casio fx-991ES / fx-991EX):
* **Natural Logarithm for AdaBoost $\alpha_t$**:  
  To compute $\frac{1}{2}\ln\left(\frac{1-0.25}{0.25}\right)$:  
  Key: `0.5` $\times$ `ln(` `(` `1` `-` `0.25` `)` `÷` `0.25` `)` `=` $\implies \mathbf{0.5493}$.
* **Exponential for Weights**:  
  Key: `SHIFT` + `ln` ($e^x$) $\to$ `(-0.5493)` `=` $\implies \mathbf{0.5774}$.
* **Euclidean Distance for 2D Points**:  
  To compute $\sqrt{(5-1)^2 + (4-1)^2}$:  
  Key: `√(` `(` `5` `-` `1` `)` `x²` `+` `(` `4` `-` `1` `)` `x²` `)` `=` $\implies \mathbf{5.0}$.

### 2. Pre-Formatted Blank Answer Sheet Templates

#### Blank K-Means Iteration Table:
```text
+----------+--------------------+--------------------+-------------------+-------------------------+
| Point xi | Dist to Centroid 1 | Dist to Centroid 2 | Assigned Cluster  | (xi - Centroid_assigned) |
+----------+--------------------+--------------------+-------------------+-------------------------+
|          |                    |                    |                   |                         |
+----------+--------------------+--------------------+-------------------+-------------------------+
```

#### Blank Naïve Bayes Probability Grid:
```text
+-----------------+---------------+-------------------+------------------+
| Feature Name    | Query Value x | P(x | Class=Yes)  | P(x | Class=No)  |
+-----------------+---------------+-------------------+------------------+
| Attribute 1     |               |                   |                  |
| Attribute 2     |               |                   |                  |
| Attribute 3     |               |                   |                  |
| Attribute 4     |               |                   |                  |
+-----------------+---------------+-------------------+------------------+
| Likelihood Prod | P(X | Class)  |                   |                  |
| Class Prior     | P(Class)      |                   |                  |
| Posterior Score | Prod * Prior  |                   |                  |
+-----------------+---------------+-------------------+------------------+
```
"""

with open(MD_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully generated Markdown booklet: {MD_PATH}")
