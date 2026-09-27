# -*- coding: utf-8 -*-
"""
Script to generate the ultimate, exhaustive, 100% calculation + full 10-mark theory master booklet
with EXACT slide question wording, SVG visual diagrams, and pen-and-paper drawing guides:
c:\\Users\\ankit\\Fall2627\\ML\\notes\\cat2\\ML_CAT2_CALCULATIONS_MASTER_BOOKLET.md
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

MD_PATH = r"c:\Users\ankit\Fall2627\ML\notes\cat2\ML_CAT2_CALCULATIONS_MASTER_BOOKLET.md"

content = r"""# 🎯 CSE4005: MACHINE LEARNING — CAT-II FOOLPROOF MASTER BOOKLET
> **Course**: CSE4005 — Machine Learning | **Exam**: CAT-2 (Open Book / Open Notes Mode)  
> **Faculty Pattern**: Dr. Nilamadhab Mishra | **Target Score**: 45+ / 50 (S-Grade Guarantee)  
> **Scope**: Unit 3 (3 Questions - 30 Marks) & Unit 4 (2 Questions - 20 Marks)  
> **Structure**: 100% Verified Calculations + Exact Slide Prompts + Visual SVG Diagrams + Full 10-Mark Theory Modules

---

# ⚡ SECTION 0: MASTER 1-PAGE QUICK-TRIGGER FORMULA & TABLE INDEX
*(Open this in the first 2 minutes of the exam. Match the algorithm, draw the table, and punch the formulas!)*

| Problem Topic & Question | What the Question Gives You | Core Calculator Formula (Type This In) | Table Columns to Draw on Answer Sheet | Common Exam Traps & Fixes |
| :--- | :--- | :--- | :--- | :--- |
| **Q1: AdaBoost Weight Update** *(Unit 3 - 10M)* | $N$ samples, labels $y_i \in \{-1, +1\}$, classifier $h_t(x)$ | $\epsilon_t = \frac{\text{Number of Errors}}{N}$<br>$\alpha_t = 0.5 \times \ln\left(\frac{1-\epsilon_t}{\epsilon_t}\right)$<br>$\tilde{w}_{\text{correct}} = w_i \times e^{-\alpha_t}$<br>$\tilde{w}_{\text{wrong}} = w_i \times e^{+\alpha_t}$<br>$w_i^{\text{new}} = \tilde{w}_i / \sum \tilde{w}_i$ | `Sample i` \| `True y_i` \| `Pred h(x_i)` \| `Status (✓/✗)` \| `Old w_i` \| `Factor` \| `Unnormalized w` \| `Final w_new` | **Trap**: Forgetting to divide by $Z_t$.<br>**Fix**: The sum of your final $w_i^{\text{new}}$ column MUST equal $1.000$. |
| **Q2: AGNES Hierarchical Clustering** *(Unit 3 - 10M)* | Points list (1D numbers or 2D coordinates) | **1D Dist**: $\|x_1 - x_2\|$<br>**2D Dist**: $\sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}$<br>**Single Link**: $\min(d_1, d_2)$<br>**Complete Link**: $\max(d_1, d_2)$<br>**Average Link**: $\frac{d_1 + d_2}{2}$ | Symmetric Distance Matrix $D_0 \to D_1 \to D_2 \to D_3$ with active cluster names as row/col headers. | **Trap**: Confusing Single vs Complete.<br>**Fix**: Both always pick the **smallest** cell in the matrix to merge! But to update distances to other clusters: Single takes $\min$, Complete takes $\max$! |
| **Q3: K-Means Clustering** *(Unit 3 - 10M)* | Data points $\{x_1 \dots x_n\}$, initial seeds $C_1, C_2$ | **Dist**: $\|x_i - C_k\|$ (or Euclidean)<br>**New Centroid**: Average of points in that cluster: $\frac{\sum x}{|K|}$<br>**Total SSE**: $\sum (x_i - C_{\text{assigned}})^2$ | `Point x_i` \| `Dist to C1` \| `Dist to C2` \| `[Dist to C3]` \| `Assigned Cluster` \| `Dist^2 for SSE` | **Trap**: Stopping after Iteration 1.<br>**Fix**: You MUST run Iteration 2 to prove assignments don't change (Convergence proof!). |
| **Q4: Naïve Bayes Classifier** *(Unit 4.1 - 10M)* | Training table with columns, test query $X = (x_1, \dots, x_d)$ | $P(\text{Class}) = \frac{\text{Count in Class}}{N}$<br>$P(x_i \mid \text{Class}) = \frac{\text{Count of } x_i \text{ in Class}}{\text{Total in Class}}$<br>$\text{Score} = P(\text{Class}) \times \prod P(x_i \mid \text{Class})$ | `Feature Name` \| `Value in X` \| `Count in Yes` \| `P(val \| Yes)` \| `Count in No` \| `P(val \| No)` | **Trap**: A count is 0 $\implies$ entire score becomes 0!<br>**Fix**: Laplace Smoothing: add $+1$ to numerator, add $+K$ (distinct values) to denominator. |
| **Q5: Apriori Association Rules** *(Unit 4.2 - 10M)* | Transactions list, $\text{min\_sup}$, $\text{min\_conf}$ | $\text{Support}(X) = \frac{\text{Count}(X)}{N}$<br>$\text{Confidence}(A \Rightarrow B) = \frac{\text{Count}(A \cup B)}{\text{Count}(A)}$<br>$\text{Lift}(A \Rightarrow B) = \frac{\text{Conf}(A \Rightarrow B)}{\text{Support}(B)}$ | Level tables: $C_1 \to L_1$, $C_2 \to L_2$, $C_3 \to L_3$ with **Pruning Justification Column**. | **Trap**: Forgetting to prune $C_3$.<br>**Fix**: If candidate is $\{A, B, C\}$, check if $\{A,B\}, \{A,C\}, \{B,C\}$ are in $L_2$. If any is missing, cross it out! |

---

# 📌 SECTION 1: QUESTION 1 — ENSEMBLE LEARNING (UNIT 3)

## 1.1 PART A: CALCULATION ENGINE & UNIVERSAL RECIPES

### Universal Plug-and-Play Recipe: How to Solve for ANY Given Numbers
```text
[STEP 1: Find N and Initial Weights]
  Count total samples in question's table -> N. Initial weight for every sample: w_i = 1 / N.
[STEP 2: Count Misclassifications]
  Count rows where True y_i != Pred h(x_i) -> K errors.
  Error Rate epsilon = K / N. (Verify epsilon < 0.50).
[STEP 3: Calculator Button Sequence for Alpha]
  Type: 0.5 * ln ( ( 1 - epsilon ) / epsilon ) -> alpha (to 4 decimal places).
[STEP 4: Exponential Multipliers]
  Correct Factor: e^(-alpha)  (Calculator: SHIFT -> ln -> (-alpha))
  Wrong Factor:   e^(+alpha)  (Calculator: SHIFT -> ln -> (+alpha))
[STEP 5: Compute Unnormalized Weights (w_tilde)]
  For each sample: w_tilde = Old_w * Factor. Sum all -> Z = sum(w_tilde).
[STEP 6: Compute Final Normalized Weights (w_new)]
  w_new = w_tilde / Z. (Sanity check: Sum of w_new MUST equal 1.000!).
```

### Solved Numerical: AdaBoost Weight Update (8 Samples, 2 Errors)

> 🎯 **EXACT EXAM QUESTION WORDING / PATTERN (Unit 3: AdaBoost)**:  
> *"Given a dataset of 8 training samples with binary labels $y_i \in \{-1, +1\}$ and initial equal weights $w_i^{(1)} = \frac{1}{8} = 0.125$. If base classifier $h_1(x)$ misclassifies samples 3 and 7:  
> (a) Calculate the weighted error rate $\epsilon_1$.  
> (b) Calculate the classifier importance weight $\alpha_1$.  
> (c) Compute the updated normalized sample weights $w_i^{(2)}$ for all 8 samples.  
> (d) Given three sequential classifiers $h_1, h_2, h_3$ with weights $\alpha_1 = 0.55, \alpha_2 = 0.72, \alpha_3 = 0.41$, determine the final combined ensemble prediction for an unknown test point."*

#### Step-by-Step Solution:
1. **Error Rate**: $\epsilon_1 = w_3^{(1)} + w_7^{(1)} = 0.125 + 0.125 = \mathbf{0.250}$.
2. **Classifier Weight**: $\alpha_1 = \frac{1}{2} \ln \left(\frac{1 - 0.25}{0.25}\right) = \frac{1}{2} \ln(3) = \mathbf{0.5493}$.
3. **Multipliers**: $e^{-\alpha_1} = e^{-0.5493} = \mathbf{0.5774}$ (Correct), $e^{+\alpha_1} = e^{+0.5493} = \mathbf{1.7321}$ (Wrong).

| Sample $i$ | True $y_i$ | Pred $h_1(x_i)$ | Status | Old $w_i^{(1)}$ | Multiplier Factor | Unnormalized $\tilde{w}_i$ | Final Normalized $w_i^{(2)} = \frac{\tilde{w}_i}{Z_1}$ |
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

4. **Final Ensemble Decision**:  
   $$H(x) = \text{sign}\left(\sum_{t=1}^3 \alpha_t h_t(x)\right) = \text{sign}(0.55(+1) + 0.72(-1) + 0.41(+1)) = \text{sign}(0.55 - 0.72 + 0.41) = \text{sign}(+0.24) = \mathbf{+1}$$

---

### Solved Numerical: Error-Correcting Output Codes (ECOC)

> 🎯 **EXACT SLIDE QUESTION WORDING / PATTERN (Slide 3.1, Page 17-19)**:  
> *"In a multi-class problem with 4 classes $\{C_1, C_2, C_3, C_4\}$, 7 binary classifiers $\{f_1, \dots, f_7\}$ are trained. The codeword matrix is:  
> $C_1 = [1, 1, 1, 1, 1, 1, 1]$  
> $C_2 = [0, 0, 0, 0, 1, 1, 1]$  
> $C_3 = [0, 0, 1, 1, 0, 0, 1]$  
> $C_4 = [0, 1, 0, 1, 0, 1, 0]$  
> If an unknown test instance produces the output vector $\hat{Y} = [0, 1, 1, 1, 0, 0, 1]$, determine which class the instance belongs to."*

#### Step-by-Step Solution:
Compute Hamming distance $d_H(\hat{Y}, C_k) = \sum_{j=1}^7 |\hat{Y}_j - C_{k,j}|$:
* $d_H(\hat{Y}, C_1) = |0-1| + |1-1| + |1-1| + |1-1| + |0-1| + |0-1| + |1-1| = 1 + 0 + 0 + 0 + 1 + 1 + 0 = \mathbf{3}$
* $d_H(\hat{Y}, C_2) = |0-0| + |1-0| + |1-0| + |1-0| + |0-1| + |0-1| + |1-1| = 0 + 1 + 1 + 1 + 1 + 1 + 0 = \mathbf{5}$
* $d_H(\hat{Y}, C_3) = |0-0| + |1-0| + |1-1| + |1-1| + |0-0| + |0-0| + |1-1| = 0 + 1 + 0 + 0 + 0 + 0 + 0 = \mathbf{1}$  *(MINIMUM!)*
* $d_H(\hat{Y}, C_4) = |0-0| + |1-1| + |1-0| + |1-1| + |0-0| + |0-1| + |1-0| = 0 + 0 + 1 + 0 + 0 + 1 + 1 = \mathbf{3}$
* **Decision**: Minimum Hamming distance is $1 \implies$ Classified as **Class $C_3$**.

---

## 1.2 PART B: 10-MARK THEORY MASTER MODULE — ENSEMBLE LEARNING

### 1. Conceptual Foundation & The Condorcet Jury Theorem
* **Definition**: Ensemble learning combines predictions from multiple base models (weak learners) to construct a single composite model that outperforms any constituent member.
* **Why Ensembles Work**: According to the **Condorcet Jury Theorem**, if each independent base classifier has an individual error rate $\epsilon < 0.50$, the probability that the majority vote is incorrect approaches **zero** as the number of classifiers $M \to \infty$:
  $$P(\text{Majority Error}) = \sum_{k=\lceil M/2 \rceil}^M \binom{M}{k} \epsilon^k (1-\epsilon)^{M-k} \xrightarrow{M \to \infty} 0$$
* **Bias-Variance Perspective**:
  * Total Generalization Error $= \text{Bias}^2 + \text{Variance} + \text{Irreducible Noise}$.
  * **Bagging** reduces **Variance** (kills overfitting).
  * **Boosting** reduces **Bias** (kills underfitting).

### 2. Ensemble Architectural Taxonomy (Must Draw in Exam!)

<div class="diagram-grid">
  <div class="diagram-card">
    <svg width="130" height="90" viewBox="0 0 130 90" xmlns="http://www.w3.org/2000/svg">
      <rect x="40" y="5" width="50" height="15" rx="2" fill="#e2e8f0" stroke="#475569"/>
      <text x="65" y="15" font-size="6.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Dataset D</text>
      <line x1="65" y1="20" x2="25" y2="35" stroke="#64748b" stroke-width="1.2"/>
      <line x1="65" y1="20" x2="65" y2="35" stroke="#64748b" stroke-width="1.2"/>
      <line x1="65" y1="20" x2="105" y2="35" stroke="#64748b" stroke-width="1.2"/>
      <rect x="10" y="35" width="30" height="15" rx="2" fill="#eff6ff" stroke="#3b82f6"/>
      <text x="25" y="45" font-size="6" fill="#1e40af" text-anchor="middle">Tree 1</text>
      <rect x="50" y="35" width="30" height="15" rx="2" fill="#eff6ff" stroke="#3b82f6"/>
      <text x="65" y="45" font-size="6" fill="#1e40af" text-anchor="middle">Tree 2</text>
      <rect x="90" y="35" width="30" height="15" rx="2" fill="#eff6ff" stroke="#3b82f6"/>
      <text x="105" y="45" font-size="6" fill="#1e40af" text-anchor="middle">Tree B</text>
      <line x1="25" y1="50" x2="65" y2="65" stroke="#64748b" stroke-width="1.2"/>
      <line x1="65" y1="50" x2="65" y2="65" stroke="#64748b" stroke-width="1.2"/>
      <line x1="105" y1="50" x2="65" y2="65" stroke="#64748b" stroke-width="1.2"/>
      <rect x="35" y="65" width="60" height="18" rx="2" fill="#dcfce7" stroke="#16a34a"/>
      <text x="65" y="77" font-size="6" font-weight="bold" fill="#15803d" text-anchor="middle">Majority Vote</text>
    </svg>
    <div class="diagram-caption">1. Bagging (Parallel)</div>
    <div style="font-size: 5.8pt; color: #475569;">Reduces Variance (Overfitting)</div>
  </div>
  <div class="diagram-card">
    <svg width="130" height="90" viewBox="0 0 130 90" xmlns="http://www.w3.org/2000/svg">
      <rect x="5" y="35" width="32" height="18" rx="2" fill="#eff6ff" stroke="#3b82f6"/>
      <text x="21" y="46" font-size="6" font-weight="bold" fill="#1e40af" text-anchor="middle">Model 1</text>
      <line x1="37" y1="44" x2="49" y2="44" stroke="#dc2626" stroke-width="1.2"/>
      <polygon points="48,41 53,44 48,47" fill="#dc2626"/>
      <rect x="53" y="35" width="32" height="18" rx="2" fill="#eff6ff" stroke="#3b82f6"/>
      <text x="69" y="46" font-size="6" font-weight="bold" fill="#1e40af" text-anchor="middle">Model 2</text>
      <line x1="85" y1="44" x2="97" y2="44" stroke="#dc2626" stroke-width="1.2"/>
      <polygon points="96,41 101,44 96,47" fill="#dc2626"/>
      <rect x="101" y="35" width="26" height="18" rx="2" fill="#eff6ff" stroke="#3b82f6"/>
      <text x="114" y="46" font-size="6" font-weight="bold" fill="#1e40af" text-anchor="middle">...</text>
      <text x="65" y="25" font-size="5.8pt" fill="#dc2626" font-weight="bold" text-anchor="middle">w_i * exp(±α)</text>
      <rect x="30" y="65" width="70" height="18" rx="2" fill="#fef3c7" stroke="#d97706"/>
      <text x="65" y="77" font-size="6" font-weight="bold" fill="#92400e" text-anchor="middle">Weighted Σ α_t h_t(x)</text>
    </svg>
    <div class="diagram-caption">2. Boosting (Sequential)</div>
    <div style="font-size: 5.8pt; color: #475569;">Reduces Bias (Underfitting)</div>
  </div>
  <div class="diagram-card">
    <svg width="130" height="90" viewBox="0 0 130 90" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="30" height="14" rx="2" fill="#eff6ff" stroke="#3b82f6"/>
      <text x="25" y="20" font-size="5.5" fill="#1e40af" text-anchor="middle">SVM</text>
      <rect x="50" y="10" width="30" height="14" rx="2" fill="#eff6ff" stroke="#3b82f6"/>
      <text x="65" y="20" font-size="5.5" fill="#1e40af" text-anchor="middle">KNN</text>
      <rect x="90" y="10" width="30" height="14" rx="2" fill="#eff6ff" stroke="#3b82f6"/>
      <text x="105" y="20" font-size="5.5" fill="#1e40af" text-anchor="middle">Tree</text>
      <text x="65" y="36" font-size="5.8" fill="#475569" text-anchor="middle">Level-0 Base Predictions</text>
      <line x1="25" y1="24" x2="65" y2="48" stroke="#64748b" stroke-width="1.2"/>
      <line x1="65" y1="24" x2="65" y2="48" stroke="#64748b" stroke-width="1.2"/>
      <line x1="105" y1="24" x2="65" y2="48" stroke="#64748b" stroke-width="1.2"/>
      <rect x="25" y="48" width="80" height="18" rx="2" fill="#f3e8ff" stroke="#9333ea"/>
      <text x="65" y="60" font-size="6" font-weight="bold" fill="#6b21a8" text-anchor="middle">Level-1 Meta-Learner</text>
      <text x="65" y="80" font-size="5.8" fill="#15803d" font-weight="bold" text-anchor="middle">Final Prediction</text>
    </svg>
    <div class="diagram-caption">3. Stacking (Hierarchical)</div>
    <div style="font-size: 5.8pt; color: #475569;">Heterogeneous Blending</div>
  </div>
</div>

### 3. Random Forest Architecture & Deep-Dive
* **Algorithm Pipeline**:
  1. For $b = 1$ to $B$ trees:
     a. Draw a bootstrap sample $D_b$ of size $N$ with replacement from dataset $D$ (contains $\approx 63.2\%$ unique samples).
     b. Grow a deep decision tree $T_b$. At each split node, randomly select a subset of $m$ features ($m \approx \sqrt{p}$ for classification, $m \approx p/3$ for regression) and pick the best split among only those $m$ features.
  2. Aggregate: For classification, take the majority vote across all $B$ unpruned trees.
* **Out-of-Bag (OOB) Error**: The remaining $\approx 36.8\%$ unsampled data points serve as an internal validation set, eliminating the need for separate cross-validation.
* **Feature Importance**: Evaluated by measuring the Mean Decrease in Impurity (Gini Importance) or Mean Decrease in Accuracy when feature values are permuted across OOB samples.

### 4. AdaBoost (Adaptive Boosting) Mathematical Derivation
* **Objective**: Minimize the Exponential Loss function:
  $$L(y, f(x)) = \sum_{i=1}^N \exp(-y_i f(x_i)), \quad \text{where } f(x) = \sum_{t=1}^T \alpha_t h_t(x)$$
* **Derivation of $\alpha_t$**:
  At iteration $t$, the loss is:
  $$J(\alpha_t) = \sum_{y_i = h_t(x_i)} w_i^{(t)} e^{-\alpha_t} + \sum_{y_i \neq h_t(x_i)} w_i^{(t)} e^{+\alpha_t} = (1 - \epsilon_t) e^{-\alpha_t} + \epsilon_t e^{+\alpha_t}$$
  Setting derivative to zero $\frac{\partial J}{\partial \alpha_t} = -(1-\epsilon_t)e^{-\alpha_t} + \epsilon_t e^{+\alpha_t} = 0$:
  $$e^{2\alpha_t} = \frac{1 - \epsilon_t}{\epsilon_t} \implies \mathbf{\alpha_t = \frac{1}{2} \ln \left(\frac{1 - \epsilon_t}{\epsilon_t}\right)}$$

### 5. Dr. Mishra's Slide 24 V.V.I CAT-II Question: Student Performance Prediction Architecture

> 🎯 **EXACT SLIDE QUESTION WORDING (Slide 3.1, Page 24 - V.V.I CAT-II EXAM PATTERN)**:  
> *"Time to Explore – A [7] (V.V.I) CAT-II EXAM PATTERN:  
> Problem Case: Student Performance Prediction  
> A college wants to predict whether a student will Pass or Fail based on: Attendance, assignment marks, internal examination marks, and study hours.  
> Three machine learning models are available: Decision Tree; k-NN; Naïve Bayes.  
> Develop a Bagging architecture and model."*

```text
               +-----------------------------------------------------------+
               |     Original Training Dataset (Attendance, Marks, Hours)  |
               +-----------------------------------------------------------+
                       |                        |                       |
               Bootstrap Sample 1       Bootstrap Sample 2      Bootstrap Sample 3
                       |                        |                       |
                       v                        v                       v
               +---------------+        +---------------+       +---------------+
               | Decision Tree |        |     k-NN      |       |  Naïve Bayes  |
               |  (Model 1)    |        |  (Model 2)    |       |  (Model 3)    |
               +---------------+        +---------------+       +---------------+
                       |                        |                       |
                 Vote: Pass               Vote: Pass              Vote: Fail
                       \                        |                      /
                        +-----------------------+---------------------+
                                                |
                                                v
                               +---------------------------------+
                               |    Majority Voting Aggregator   |
                               |    Decision: PASS (2 vs 1)      |
                               +---------------------------------+
```
* **Design Justification**:
  1. **Diversity**: Combines heterogeneous learning biases (Decision Tree: axis-aligned splits; k-NN: local instance geometry; Naïve Bayes: global probabilistic likelihoods).
  2. **Variance Reduction**: Individual noisy sensor/attendance records are smoothed out by majority voting.
  3. **Robustness**: If one model fails due to non-linear feature interaction, the other two compensate.

### 6. Comprehensive Ensemble Comparison Table (Must Draw for 10 Marks)

| Dimension | Bagging (Random Forest) | Boosting (AdaBoost) | Stacking |
| :--- | :--- | :--- | :--- |
| **Model Structure** | Homogeneous, Parallel & Independent | Homogeneous, Sequential & Adaptive | Heterogeneous, Two-Tier Hierarchy |
| **Error Reduction** | Reduces **Variance** (Overfitting) | Reduces **Bias** (Underfitting) | Reduces both Bias and Variance |
| **Base Learners** | High-variance, deep unpruned trees | High-bias weak learners (stumps) | Diverse algorithms (SVM, KNN, Trees) |
| **Data Sampling** | Bootstrap sampling with replacement | Reweighting samples iteratively | $K$-fold cross-validation split |
| **Aggregation** | Equal-weight Majority Voting | Weighted Voting ($\alpha_t$) | Meta-Learner (Logistic Regression/Ridge) |
| **Outlier Handling**| Highly robust | Highly sensitive (weights blow up) | Moderately robust |

---

# 📌 SECTION 2: QUESTION 2 — HIERARCHICAL CLUSTERING: AGNES (UNIT 3)

## 2.1 PART A: CALCULATION ENGINE & UNIVERSAL RECIPES

### Universal Plug-and-Play Recipe for ANY Given Points
```text
[STEP 1: Construct Initial Distance Matrix D_0]
  N points -> N x N symmetric matrix. Diagonal = 0.
  Distance: d(x,y) = |x - y| (1D) or sqrt((x1-x2)^2 + (y1-y2)^2) (2D).
[STEP 2: Find Minimum Off-Diagonal Element]
  Identify min cell d(A, B) -> Merge clusters A and B into (A, B) at height h = min_dist.
[STEP 3: Update Distance Matrix to Form D_1]
  Delete rows/columns A and B. Add new row/column (A, B).
  To compute distance from (A, B) to any other cluster C:
    * Single Linkage:   d((A,B), C) = min( d(A, C), d(B, C) )
    * Complete Linkage: d((A,B), C) = max( d(A, C), d(B, C) )
    * Average Linkage:  d((A,B), C) = (|A|*d(A,C) + |B|*d(B,C)) / (|A| + |B|)
[STEP 4: Repeat Until 1 Monolithic Cluster Remains]
  Matrix reduces by 1 dimension each step: N x N -> (N-1)x(N-1) -> ... -> 2x2 -> 1x1.
```

### Solved 1D Numerical: Slide 3.5 Example (Hierarchical Clustering)

> 🎯 **EXACT SLIDE QUESTION WORDING (Slide 3.5, Page 6)**:  
> *"Consider one dimensional data set $\{7, 10, 20, 28, 35\}$, perform hierarchical clustering and plot the dendrogram to visualize it."*  
> **What the Question Asks You To Do**:  
> 1. Show the step-by-step distance matrices and cluster merges using **Single Linkage** and **Complete Linkage**.  
> 2. State the final clusters for $k=2$.  
> 3. Draw the dendrogram with exact merge heights on the vertical axis.

#### Initial Distance Matrix $D_0$:
$$D_0 = \begin{pmatrix} & 7 & 10 & 20 & 28 & 35 \\ 7 & 0 & 3 & 13 & 21 & 28 \\ 10 & 3 & 0 & 10 & 18 & 25 \\ 20 & 13 & 10 & 0 & 8 & 15 \\ 28 & 21 & 18 & 8 & 0 & 7 \\ 35 & 28 & 25 & 15 & 7 & 0 \end{pmatrix}$$
* Smallest distance is $d(7, 10) = \mathbf{3}$. Merge $\{7, 10\}$ at height $h = 3$.

#### Single Linkage Execution:
1. Merge $(7, 10)$ at $h=3$.
2. Next smallest is $d(28, 35) = \mathbf{7}$. Merge $(28, 35)$ at $h=7$.
3. Distance from 20 to clusters: $d(20, \{7,10\}) = \min(13, 10) = 10$; $d(20, \{28,35\}) = \min(8, 15) = \mathbf{8}$.  
   Merge 20 into $\{28, 35\} \implies \{20, 28, 35\}$ at $h=8$.
4. Merge $\{7, 10\}$ and $\{20, 28, 35\}$ at $h = \min(10, 18, 25, 13, 21, 28) = \mathbf{10}$.
* **Single Linkage Clusters ($k=2$)**: **$\{7, 10\}$ and $\{20, 28, 35\}$**.

#### Single Linkage Dendrogram:
```text
Height (h)
  10 |       +-----------------------+
     |       |                       |
   8 |       |               +-------+
     |       |               |       |
   7 |       |               |   +---+
     |       |               |   |   |
   3 |   +---+               |   |   |
     |   |   |               |   |   |
   0 +---+---+---------------+---+---+
         7   10              20  28  35
```

#### Complete Linkage Execution:
1. Merge $(7, 10)$ at $h=3$.
2. Merge $(28, 35)$ at $h=7$.
3. Complete distance: $d(20, \{7,10\}) = \max(13, 10) = \mathbf{13}$; $d(20, \{28,35\}) = \max(8, 15) = \mathbf{15}$.  
   Since $13 < 15$, merge 20 into $\{7, 10\} \implies \{7, 10, 20\}$ at $h = 13$.
4. Final merge of $\{7, 10, 20\}$ and $\{28, 35\}$ at $h = \max(21, 28, 18, 25, 8, 15) = \mathbf{28}$.
* **Complete Linkage Clusters ($k=2$)**: **$\{7, 10, 20\}$ and $\{28, 35\}$**.

#### Complete Linkage Dendrogram:
```text
Height (h)
  28 |   +---------------------------+
     |   |                           |
  13 |   +---------------+           |
     |   |               |           |
   7 |   |               |       +---+
     |   |               |       |   |
   3 | +-+-+             |       |   |
     | |   |             |       |   |
   0 +-+---+-------------+-------+---+
       7   10            20      28  35
```

---

### Solved 2D Coordinates Problem: Points $A(1,1), B(2,1), C(4,3), D(5,4)$

> 🎯 **EXACT EXAM QUESTION WORDING / PATTERN (2D Hierarchical AGNES)**:  
> *"Consider four 2D data points $A(1,1), B(2,1), C(4,3), D(5,4)$. Perform Agglomerative Hierarchical Clustering (AGNES) using Single Linkage and Euclidean distance. Show the distance matrix at each merging step and identify the final clusters for $k=2$."*

1. **Initial Distance Matrix $D_0$**:
   * $d(A,B) = \sqrt{(2-1)^2 + (1-1)^2} = \mathbf{1.000}$ *(MINIMUM!)*
   * $d(C,D) = \sqrt{(5-4)^2 + (4-3)^2} = \sqrt{2} = \mathbf{1.414}$
   * $d(A,C) = \sqrt{9+4} = \sqrt{13} = 3.606$; $d(B,C) = \sqrt{4+4} = \sqrt{8} = 2.828$
   * $d(A,D) = \sqrt{16+9} = 5.000$; $d(B,D) = \sqrt{9+9} = \sqrt{18} = 4.243$
2. **Step 1**: Merge $(A, B)$ at height $h = 1.000$.
   * Single Link: $d((A,B), C) = \min(3.606, 2.828) = 2.828$; $d((A,B), D) = \min(5.000, 4.243) = 4.243$.
3. **Step 2**: Smallest distance in $D_1$ is $d(C,D) = 1.414$. Merge $(C, D)$ at height $h = 1.414$.
4. **Step 3**: Merge $\{A, B\}$ and $\{C, D\}$ at height $h = \min(2.828, 4.243) = \mathbf{2.828}$.
* **Clusters for $k=2$**: **$\{A, B\}$ and $\{C, D\}$**.

---

## 2.2 PART B: 10-MARK THEORY MASTER MODULE — HIERARCHICAL CLUSTERING

### 1. Fundamental Paradigm: Agglomerative vs Divisive

<div class="diagram-box">
  <svg width="450" height="90" viewBox="0 0 450 90" xmlns="http://www.w3.org/2000/svg">
    <!-- Top Monolithic -->
    <rect x="175" y="5" width="100" height="20" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
    <text x="225" y="18" font-size="7.5" font-weight="bold" fill="#92400e" text-anchor="middle">{ a, b, c, d, e }</text>
    
    <!-- Intermediate -->
    <rect x="100" y="35" width="60" height="18" rx="3" fill="#e0f2fe" stroke="#0284c7"/>
    <text x="130" y="47" font-size="7" fill="#0369a1" text-anchor="middle">{ a, b }</text>
    
    <rect x="290" y="35" width="70" height="18" rx="3" fill="#e0f2fe" stroke="#0284c7"/>
    <text x="325" y="47" font-size="7" fill="#0369a1" text-anchor="middle">{ c, d, e }</text>
    
    <!-- Bottom Singletons -->
    <rect x="60" y="65" width="30" height="18" rx="3" fill="#f1f5f9" stroke="#64748b"/>
    <text x="75" y="77" font-size="7" fill="#334155" text-anchor="middle">{ a }</text>
    <rect x="100" y="65" width="30" height="18" rx="3" fill="#f1f5f9" stroke="#64748b"/>
    <text x="115" y="77" font-size="7" fill="#334155" text-anchor="middle">{ b }</text>
    <rect x="250" y="65" width="30" height="18" rx="3" fill="#f1f5f9" stroke="#64748b"/>
    <text x="265" y="77" font-size="7" fill="#334155" text-anchor="middle">{ c }</text>
    <rect x="290" y="65" width="30" height="18" rx="3" fill="#f1f5f9" stroke="#64748b"/>
    <text x="305" y="77" font-size="7" fill="#334155" text-anchor="middle">{ d }</text>
    <rect x="330" y="65" width="30" height="18" rx="3" fill="#f1f5f9" stroke="#64748b"/>
    <text x="345" y="77" font-size="7" fill="#334155" text-anchor="middle">{ e }</text>
    
    <!-- Tree Lines -->
    <line x1="225" y1="25" x2="130" y2="35" stroke="#94a3b8" stroke-width="1.2"/>
    <line x1="225" y1="25" x2="325" y2="35" stroke="#94a3b8" stroke-width="1.2"/>
    <line x1="130" y1="53" x2="75" y2="65" stroke="#94a3b8" stroke-width="1.2"/>
    <line x1="130" y1="53" x2="115" y2="65" stroke="#94a3b8" stroke-width="1.2"/>
    <line x1="325" y1="53" x2="265" y2="65" stroke="#94a3b8" stroke-width="1.2"/>
    <line x1="325" y1="53" x2="305" y2="65" stroke="#94a3b8" stroke-width="1.2"/>
    <line x1="325" y1="53" x2="345" y2="65" stroke="#94a3b8" stroke-width="1.2"/>
    
    <!-- Side Flow Arrows -->
    <line x1="35" y1="75" x2="35" y2="15" stroke="#16a34a" stroke-width="2.5"/>
    <polygon points="30,20 35,10 40,20" fill="#16a34a"/>
    <text x="35" y="85" font-size="6.5" font-weight="bold" fill="#16a34a" text-anchor="middle">AGNES: Merge ↑</text>
    
    <line x1="410" y1="15" x2="410" y2="75" stroke="#ea580c" stroke-width="2.5"/>
    <polygon points="405,70 410,80 415,70" fill="#ea580c"/>
    <text x="410" y="87" font-size="6.5" font-weight="bold" fill="#ea580c" text-anchor="middle">DIANA: Split ↓</text>
  </svg>
  <div class="diagram-caption">AGNES (Bottom-Up Agglomerative) vs DIANA (Top-Down Divisive) (Slide 3.5, p. 3)</div>
</div>

* **Agglomerative (AGNES - Bottom-Up)**: Starts with $N$ individual singleton clusters; at each step merges the two most proximate clusters. Complexity: $O(N^3)$ (naive) or $O(N^2 \log N)$ (with priority queue).
* **Divisive (DIANA - Top-Down)**: Starts with 1 monolithic cluster containing all $N$ objects; recursively bisects until $N$ singletons remain.

---

### 2. Comprehensive Linkage Criteria Analysis (Must Draw These 4 Diagrams!)

<div class="diagram-grid">
  <div class="diagram-card">
    <svg width="115" height="75" viewBox="0 0 115 75" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="28" cy="38" rx="20" ry="28" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <ellipse cx="87" cy="38" rx="20" ry="28" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>
      <circle cx="18" cy="28" r="2" fill="#0369a1"/>
      <circle cx="22" cy="48" r="2" fill="#0369a1"/>
      <circle cx="38" cy="38" r="3" fill="#dc2626"/>
      <circle cx="77" cy="38" r="3" fill="#dc2626"/>
      <circle cx="93" cy="28" r="2" fill="#0369a1"/>
      <circle cx="97" cy="48" r="2" fill="#0369a1"/>
      <line x1="38" y1="38" x2="77" y2="38" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="3,2"/>
      <text x="58" y="32" font-size="6.5" font-weight="bold" fill="#dc2626" text-anchor="middle">min d(x,y)</text>
    </svg>
    <div class="diagram-caption">1. Single Linkage</div>
    <div style="font-size: 5.8pt; color: #475569;">Nearest Neighbor (Chaining)</div>
  </div>
  <div class="diagram-card">
    <svg width="115" height="75" viewBox="0 0 115 75" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="28" cy="38" rx="20" ry="28" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
      <ellipse cx="87" cy="38" rx="20" ry="28" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
      <circle cx="14" cy="38" r="3" fill="#dc2626"/>
      <circle cx="32" cy="28" r="2" fill="#b45309"/>
      <circle cx="35" cy="48" r="2" fill="#b45309"/>
      <circle cx="80" cy="28" r="2" fill="#b45309"/>
      <circle cx="83" cy="48" r="2" fill="#b45309"/>
      <circle cx="101" cy="38" r="3" fill="#dc2626"/>
      <line x1="14" y1="38" x2="101" y2="38" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="3,2"/>
      <text x="58" y="32" font-size="6.5" font-weight="bold" fill="#dc2626" text-anchor="middle">max d(x,y)</text>
    </svg>
    <div class="diagram-caption">2. Complete Linkage</div>
    <div style="font-size: 5.8pt; color: #475569;">Furthest Neighbor (Outliers)</div>
  </div>
  <div class="diagram-card">
    <svg width="115" height="75" viewBox="0 0 115 75" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="28" cy="38" rx="20" ry="28" fill="#f1f5f9" stroke="#64748b" stroke-width="1.2"/>
      <ellipse cx="87" cy="38" rx="20" ry="28" fill="#f1f5f9" stroke="#64748b" stroke-width="1.2"/>
      <circle cx="24" cy="30" r="2" fill="#334155"/>
      <circle cx="32" cy="46" r="2" fill="#334155"/>
      <circle cx="82" cy="30" r="2" fill="#334155"/>
      <circle cx="92" cy="46" r="2" fill="#334155"/>
      <line x1="24" y1="30" x2="82" y2="30" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2,2"/>
      <line x1="24" y1="30" x2="92" y2="46" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2,2"/>
      <line x1="32" y1="46" x2="82" y2="30" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2,2"/>
      <line x1="32" y1="46" x2="92" y2="46" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2,2"/>
      <text x="58" y="24" font-size="6.5" font-weight="bold" fill="#334155" text-anchor="middle">mean d(x,y)</text>
    </svg>
    <div class="diagram-caption">3. Average Linkage</div>
    <div style="font-size: 5.8pt; color: #475569;">All Pairs Mean (Balanced)</div>
  </div>
  <div class="diagram-card">
    <svg width="115" height="75" viewBox="0 0 115 75" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="28" cy="38" rx="20" ry="28" fill="#dcfce7" stroke="#16a34a" stroke-width="1.2"/>
      <ellipse cx="87" cy="38" rx="20" ry="28" fill="#dcfce7" stroke="#16a34a" stroke-width="1.2"/>
      <circle cx="20" cy="30" r="1.8" fill="#15803d"/>
      <circle cx="32" cy="46" r="1.8" fill="#15803d"/>
      <circle cx="82" cy="30" r="1.8" fill="#15803d"/>
      <circle cx="94" cy="46" r="1.8" fill="#15803d"/>
      <line x1="24" y1="38" x2="32" y2="38" stroke="#b91c1c" stroke-width="2"/>
      <line x1="28" y1="34" x2="28" y2="42" stroke="#b91c1c" stroke-width="2"/>
      <line x1="83" y1="38" x2="91" y2="38" stroke="#b91c1c" stroke-width="2"/>
      <line x1="87" y1="34" x2="87" y2="42" stroke="#b91c1c" stroke-width="2"/>
      <line x1="28" y1="38" x2="87" y2="38" stroke="#b91c1c" stroke-width="1.8"/>
      <text x="58" y="32" font-size="6.5" font-weight="bold" fill="#b91c1c" text-anchor="middle">||μ1 - μ2||²</text>
    </svg>
    <div class="diagram-caption">4. Centroid Linkage</div>
    <div style="font-size: 5.8pt; color: #475569;">Mean Distance (Inversion)</div>
  </div>
</div>

1. **Single Linkage**: $d(C_i, C_j) = \min_{x \in C_i, y \in C_j} d(x, y)$. Handles elongated non-elliptical shapes; prone to **Chaining Effect**.
2. **Complete Linkage**: $d(C_i, C_j) = \max_{x \in C_i, y \in C_j} d(x, y)$. Enforces compact spherical clusters; sensitive to outliers.
3. **Average Linkage (UPGMA)**: $d(C_i, C_j) = \frac{1}{|C_i||C_j|} \sum \sum d(x, y)$. Robust trade-off.
4. **Centroid Linkage (UPGMC)**: $d(C_i, C_j) = \|\mu_i - \mu_j\|^2$. Fast, but prone to **Inversion (Non-monotonicity)** where merge height decreases.
5. **Ward's Method**: Merges clusters minimizing increase in total variance: $\Delta \text{ESS} = \frac{|C_i||C_j|}{|C_i| + |C_j|} \|\mu_i - \mu_j\|^2$.

---

### 3. Dendrogram Structure & Cut-Line Heuristic (Must Draw in Exam!)

<div class="diagram-box">
  <svg width="450" height="150" viewBox="0 0 450 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Y Axis -->
    <line x1="45" y1="15" x2="45" y2="125" stroke="#334155" stroke-width="1.5"/>
    <text x="35" y="20" font-size="7" text-anchor="end" fill="#334155">12 -</text>
    <text x="35" y="42" font-size="7" text-anchor="end" fill="#334155">10 -</text>
    <text x="35" y="63" font-size="7" text-anchor="end" fill="#334155">8 -</text>
    <text x="35" y="73" font-size="7" text-anchor="end" fill="#334155">7 -</text>
    <text x="35" y="105" font-size="7" text-anchor="end" fill="#334155">3 -</text>
    <text x="35" y="125" font-size="7" text-anchor="end" fill="#334155">0 -</text>
    <text x="15" y="70" font-size="8" font-weight="bold" fill="#1e3a8a" transform="rotate(-90 15 70)" text-anchor="middle">Dissimilarity Height (h)</text>
    
    <!-- X Axis Baseline -->
    <line x1="45" y1="125" x2="420" y2="125" stroke="#334155" stroke-width="1.5"/>
    <text x="90" y="137" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">x1 (7)</text>
    <text x="140" y="137" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">x2 (10)</text>
    <text x="240" y="137" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">x3 (20)</text>
    <text x="310" y="137" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">x4 (28)</text>
    <text x="370" y="137" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">x5 (35)</text>
    
    <!-- Tree Branches: Single Linkage -->
    <!-- (x1, x2) at h=3 -->
    <line x1="90" y1="125" x2="90" y2="105" stroke="#0284c7" stroke-width="2"/>
    <line x1="140" y1="125" x2="140" y2="105" stroke="#0284c7" stroke-width="2"/>
    <line x1="90" y1="105" x2="140" y2="105" stroke="#0284c7" stroke-width="2"/>
    <text x="115" y="100" font-size="7" fill="#0284c7" text-anchor="middle" font-weight="bold">h = 3</text>
    
    <!-- (x4, x5) at h=7 -->
    <line x1="310" y1="125" x2="310" y2="73" stroke="#0284c7" stroke-width="2"/>
    <line x1="370" y1="125" x2="370" y2="73" stroke="#0284c7" stroke-width="2"/>
    <line x1="310" y1="73" x2="370" y2="73" stroke="#0284c7" stroke-width="2"/>
    <text x="340" y="68" font-size="7" fill="#0284c7" text-anchor="middle" font-weight="bold">h = 7</text>
    
    <!-- x3 into (x4, x5) at h=8 -->
    <line x1="240" y1="125" x2="240" y2="63" stroke="#0284c7" stroke-width="2"/>
    <line x1="340" y1="73" x2="340" y2="63" stroke="#0284c7" stroke-width="2"/>
    <line x1="240" y1="63" x2="340" y2="63" stroke="#0284c7" stroke-width="2"/>
    <text x="290" y="58" font-size="7" fill="#0284c7" text-anchor="middle" font-weight="bold">h = 8</text>
    
    <!-- Final merge at h=10 -->
    <line x1="115" y1="105" x2="115" y2="42" stroke="#0284c7" stroke-width="2"/>
    <line x1="290" y1="63" x2="290" y2="42" stroke="#0284c7" stroke-width="2"/>
    <line x1="115" y1="42" x2="290" y2="42" stroke="#0284c7" stroke-width="2"/>
    <text x="202" y="37" font-size="7" fill="#0284c7" text-anchor="middle" font-weight="bold">h = 10</text>
    
    <!-- Red Dashed Horizontal Cut Line at h=9 -->
    <line x1="45" y1="52" x2="350" y2="52" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="5,3"/>
    <text x="355" y="55" font-size="7.2" fill="#dc2626" font-weight="bold" text-anchor="start">Cut Line H = 9 (k = 2)</text>
    <circle cx="115" cy="52" r="3.5" fill="#dc2626"/>
    <circle cx="290" cy="52" r="3.5" fill="#dc2626"/>
    
    <!-- Cluster Labels -->
    <rect x="75" y="1" width="80" height="15" rx="3" fill="#eff6ff" stroke="#3b82f6"/>
    <text x="115" y="11" font-size="7" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Cluster 1: {x1, x2}</text>
    
    <rect x="235" y="1" width="115" height="15" rx="3" fill="#eff6ff" stroke="#3b82f6"/>
    <text x="292" y="11" font-size="7" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Cluster 2: {x3, x4, x5}</text>
  </svg>
  <div class="diagram-caption">Dendrogram Structure & Cluster Cut-Line Heuristic (Slide 3.5 Example)</div>
</div>

* **Determining $k$**: Drawing a horizontal cut-line across the dendrogram at height $H$. The number of vertical tree branches intersected by the cut-line equals the number of natural clusters $k$.
* **Cophenetic Correlation Coefficient (CPCC)**: Measures how faithfully a dendrogram preserves the original pairwise distances:
  $$\text{CPCC} = \frac{\sum_{i<j} (D_{ij} - \bar{D})(C_{ij} - \bar{C})}{\sqrt{\sum_{i<j}(D_{ij} - \bar{D})^2 \sum_{i<j}(C_{ij} - \bar{C})^2}}$$
  where $D_{ij}$ is the original Euclidean distance and $C_{ij}$ is the dendrogram merge height. $\text{CPCC} > 0.80$ indicates a high-fidelity clustering.

---

# 📌 SECTION 3: QUESTION 3 — PARTITIONAL CLUSTERING: K-MEANS & VARIANTS (UNIT 3)

## 3.1 PART A: CALCULATION ENGINE & UNIVERSAL RECIPES

### Universal Plug-and-Play Recipe for ANY Given Points & Seeds
```text
[STEP 1: Centroids & Distance Table]
  Write initial seeds C_1, C_2 (and C_3 if k=3).
  For each point: compute Dist = |x - C| (1D) or sqrt((x-Cx)^2 + (y-Cy)^2) (2D).
  Assign point to whichever centroid has the minimum distance.
[STEP 2: Centroid Update]
  New Centroid C_k = (sum of all coordinates in cluster K) / (number of points in cluster K).
[STEP 3: Iteration 2 (Convergence Proof)]
  Recalculate distances to New Centroids. If assignments don't change -> STOP! CONVERGED!
[STEP 4: SSE Calculation]
  Sum (Dist to assigned centroid)^2 across all points -> Total SSE.
```

### Solved 1D Numerical: Slide 3.6 Problem (K-Means Clustering)

> 🎯 **EXACT SLIDE QUESTION WORDING (Slide 3.6, Page 7-9)**:  
> *"Using K-means clustering, cluster the following data into two clusters and show each step:  
> $\{2, 4, 10, 12, 3, 20, 30, 11, 25\}$.  
> (Method-02: Use initial means $m_1 = 3, m_2 = 4$)."*

#### Step-by-Step Iterations:
* Initial Seeds: $m_1 = 3, m_2 = 4$.
* **Iteration 1**: Midpoint $= \frac{3+4}{2} = 3.5$.  
  $K_1 = \{2, 3\}$ ($m_1^{(1)} = \mathbf{2.5}$), $K_2 = \{4, 10, 11, 12, 20, 25, 30\}$ ($m_2^{(1)} = \mathbf{16.0}$).
* **Iteration 2**: Midpoint $= \frac{2.5+16.0}{2} = 9.25$.  
  $K_1 = \{2, 3, 4\}$ ($m_1^{(2)} = \mathbf{3.0}$), $K_2 = \{10, 11, 12, 20, 25, 30\}$ ($m_2^{(2)} = \mathbf{18.0}$).
* **Iteration 3**: Midpoint $= \frac{3.0+18.0}{2} = 10.5$.  
  $K_1 = \{2, 3, 4, 10\}$ ($m_1^{(3)} = \mathbf{4.75}$), $K_2 = \{11, 12, 20, 25, 30\}$ ($m_2^{(3)} = \mathbf{19.6}$).
* **Iteration 4**: Midpoint $= \frac{4.75+19.6}{2} = 12.18$.  
  $K_1 = \{2, 3, 4, 10, 11, 12\}$ ($m_1^{(4)} = \mathbf{7.0}$), $K_2 = \{20, 25, 30\}$ ($m_2^{(4)} = \mathbf{25.0}$).
* **Iteration 5**: Midpoint $= \frac{7.0+25.0}{2} = 16.0$.  
  $K_1 = \{2, 3, 4, 10, 11, 12\}$ ($m_1=7.0$), $K_2 = \{20, 25, 30\}$ ($m_2=25.0$) $\implies$ **CONVERGED!**
* **Final Centroids**: $C_1 = 7.0, C_2 = 25.0$.
* **Total SSE**: $\text{SSE}_1 + \text{SSE}_2 = 100 + 50 = \mathbf{150}$.

---

### Solved Numerical: K-Medoids (PAM) 2D Swap Cost

> 🎯 **EXACT SLIDE QUESTION WORDING (Slide 3.6, Page 16-20)**:  
> *"Cluster Computation using K-Medoids through a dataset scenario:  
> Initial medoids selected: $k = 2$, with $C_1 = (4, 5)$ and $C_2 = (8, 5)$, yielding total absolute dissimilarity cost $= 20$.  
> Randomly select one non-medoid point $(8, 4)$ to replace $C_2$. Compute the new cost, calculate the swap cost $\Delta S = \text{Cost}_{\text{new}} - \text{Cost}_{\text{previous}}$, and determine whether to accept or reject the swap."*

#### Step-by-Step Solution:
* **Initial State**: Medoids $C_1(4,5)$ and $C_2(8,5) \implies \text{Cost}_{\text{old}} = \mathbf{20}$.
* **Candidate Swap**: Replace $C_2(8,5)$ with $(8,4)$.
* **New Cost**: Reassigning points with Manhattan distances to $C_1(4,5)$ and $(8,4)$ yields:
  $$\text{Cost}_{\text{new}} = (3 + 4 + 4) + (2 + 2 + 1 + 3 + 3) = 11 + 11 = \mathbf{22}$$
* **Swap Cost ($\Delta S$)**:
  $$\Delta S = \text{Cost}_{\text{new}} - \text{Cost}_{\text{old}} = 22 - 20 = \mathbf{+2 > 0}$$
* **Decision**: Since $\Delta S > 0$ (cost increased), **REJECT the swap** and retain original medoids $(4,5)$ and $(8,5)$.

---

## 3.2 PART B: 10-MARK THEORY MASTER MODULE — PARTITIONAL CLUSTERING

### 1. Mathematical Formulation & Alternating Optimization
* **Objective Function**: Minimize Within-Cluster Sum of Squares (WCSS / SSE):
  $$J = \sum_{k=1}^K \sum_{x_i \in S_k} \|x_i - \mu_k\|^2 = \sum_{i=1}^N \sum_{k=1}^K r_{ik} \|x_i - \mu_k\|^2$$
  where $r_{ik} \in \{0, 1\}$ is a binary indicator ($r_{ik}=1$ if $x_i \in S_k$).
* **Two-Step Alternating Minimization Proof**:
  1. **Assignment Step (Optimize $r_{ik}$ holding $\mu_k$ fixed)**:
     $$r_{ik} = \begin{cases} 1 & \text{if } k = \arg\min_j \|x_i - \mu_j\|^2 \\ 0 & \text{otherwise} \end{cases}$$
  2. **Update Step (Optimize $\mu_k$ holding $r_{ik}$ fixed)**:
     Setting $\frac{\partial J}{\partial \mu_k} = 0$:
     $$-2 \sum_{i=1}^N r_{ik}(x_i - \mu_k) = 0 \implies \mathbf{\mu_k = \frac{\sum_{i=1}^N r_{ik} x_i}{\sum_{i=1}^N r_{ik}} = \frac{1}{|S_k|} \sum_{x \in S_k} x}$$
* **Convergence**: Since $J$ decreases monotonically at each step and there are a finite number of partitions ($K^N$), K-Means is guaranteed to terminate in finite iterations (local optimum).

### 2. K-Means vs K-Medoids Outlier Robustness (Must Draw in Exam!)

<div class="diagram-grid">
  <div class="diagram-card">
    <svg width="180" height="90" viewBox="0 0 180 90" xmlns="http://www.w3.org/2000/svg">
      <circle cx="35" cy="40" r="3" fill="#0284c7"/>
      <circle cx="45" cy="30" r="3" fill="#0284c7"/>
      <circle cx="40" cy="50" r="3" fill="#0284c7"/>
      <circle cx="50" cy="45" r="3" fill="#0284c7"/>
      <circle cx="30" cy="45" r="3" fill="#0284c7"/>
      <circle cx="40" cy="42" r="3.5" fill="#16a34a"/>
      <text x="40" y="58" font-size="6" fill="#16a34a" text-anchor="middle">True Center</text>
      <circle cx="155" cy="20" r="4" fill="#dc2626"/>
      <text x="155" y="14" font-size="6" font-weight="bold" fill="#dc2626" text-anchor="middle">Outlier!</text>
      <circle cx="68" cy="37" r="4" fill="#dc2626"/>
      <line x1="40" y1="42" x2="68" y2="37" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="2,2"/>
      <line x1="68" y1="37" x2="155" y2="20" stroke="#dc2626" stroke-width="1" stroke-dasharray="2,2"/>
      <text x="75" y="29" font-size="6.5" font-weight="bold" fill="#dc2626">Mean μ pulled!</text>
    </svg>
    <div class="diagram-caption">K-Means: Distorted by Outlier</div>
    <div style="font-size: 5.8pt; color: #475569;">Artificial center shifts towards extreme values</div>
  </div>
  <div class="diagram-card">
    <svg width="180" height="90" viewBox="0 0 180 90" xmlns="http://www.w3.org/2000/svg">
      <circle cx="35" cy="40" r="3" fill="#0284c7"/>
      <circle cx="45" cy="30" r="3" fill="#0284c7"/>
      <circle cx="40" cy="50" r="3" fill="#0284c7"/>
      <circle cx="50" cy="45" r="3" fill="#0284c7"/>
      <circle cx="30" cy="45" r="3" fill="#0284c7"/>
      <polygon points="40,36 43,44 35,39 45,39 37,44" fill="#f59e0b" stroke="#b45309" stroke-width="0.8"/>
      <text x="40" y="58" font-size="6" font-weight="bold" fill="#b45309" text-anchor="middle">Medoid M (Actual Point)</text>
      <circle cx="155" cy="20" r="4" fill="#dc2626"/>
      <text x="155" y="14" font-size="6" font-weight="bold" fill="#dc2626" text-anchor="middle">Outlier!</text>
      <line x1="40" y1="42" x2="155" y2="20" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2,2"/>
      <text x="95" y="27" font-size="6.5" font-weight="bold" fill="#15803d">Medoid does NOT shift!</text>
    </svg>
    <div class="diagram-caption">K-Medoids (PAM): Outlier Robust</div>
    <div style="font-size: 5.8pt; color: #475569;">Medoid is locked to an actual data object</div>
  </div>
</div>

### 3. Modern Mitigations: K-Means++, K-Medoids (PAM), and K-Modes
* **K-Means++**: Eliminates seed sensitivity by choosing initial centroids with probability proportional to squared distance: $P(x) = \frac{D(x)^2}{\sum D(x)^2}$.
* **K-Medoids (PAM)**: Optimizes absolute error using actual data objects (medoids): $J_{\text{medoid}} = \sum \sum d(x, M_k)$ with Manhattan $L_1$ norm.
* **K-Modes Algorithm**: Handles categorical data by replacing Euclidean distance with Simple Matching Dissimilarity $\delta(x, y)$ and replacing means with **modes**.

### 4. Expectation-Maximization (EM) & Gaussian Mixture Models (GMM)
* **Soft Clustering**: Computes posterior responsibility: $\gamma_{nk} = \frac{\pi_k \mathcal{N}(x_n \mid \mu_k, \Sigma_k)}{\sum_j \pi_j \mathcal{N}(x_n \mid \mu_j, \Sigma_j)}$.
* **Connection**: K-Means is a special limiting case of EM on GMM where all covariances $\Sigma_k = \sigma^2 I$ as $\sigma^2 \to 0$ (hard cluster boundary).

### 5. Determining Optimal $k$: Elbow Method vs Silhouette Analysis (Must Draw in Exam!)

<div class="diagram-grid">
  <div class="diagram-card">
    <svg width="180" height="95" viewBox="0 0 180 95" xmlns="http://www.w3.org/2000/svg">
      <line x1="30" y1="10" x2="30" y2="75" stroke="#334155" stroke-width="1.2"/>
      <line x1="30" y1="75" x2="170" y2="75" stroke="#334155" stroke-width="1.2"/>
      <text x="25" y="15" font-size="6" text-anchor="end" fill="#334155">WCSS</text>
      <text x="165" y="86" font-size="6" text-anchor="end" fill="#334155">k</text>
      <text x="50" y="84" font-size="6" fill="#334155" text-anchor="middle">1</text>
      <text x="75" y="84" font-size="6" fill="#334155" text-anchor="middle">2</text>
      <text x="100" y="84" font-size="6" fill="#dc2626" font-weight="bold">3</text>
      <text x="125" y="84" font-size="6" fill="#334155" text-anchor="middle">4</text>
      <text x="150" y="84" font-size="6" fill="#334155" text-anchor="middle">5</text>
      <path d="M 50 18 Q 80 45 100 58 T 150 68" fill="none" stroke="#0284c7" stroke-width="2"/>
      <circle cx="50" cy="18" r="2.5" fill="#0284c7"/>
      <circle cx="75" cy="42" r="2.5" fill="#0284c7"/>
      <circle cx="100" cy="58" r="4" fill="#dc2626"/>
      <circle cx="125" cy="64" r="2.5" fill="#0284c7"/>
      <circle cx="150" cy="68" r="2.5" fill="#0284c7"/>
      <line x1="100" y1="58" x2="125" y2="30" stroke="#dc2626" stroke-width="1"/>
      <text x="128" y="28" font-size="6" font-weight="bold" fill="#dc2626">Elbow Point (k=3)</text>
      <text x="128" y="36" font-size="5.5" fill="#475569">Optimal Clusters</text>
    </svg>
    <div class="diagram-caption">1. The Elbow Method</div>
  </div>
  <div class="diagram-card">
    <svg width="180" height="95" viewBox="0 0 180 95" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="45" cy="48" rx="28" ry="32" fill="#eff6ff" stroke="#3b82f6" stroke-dasharray="2,2"/>
      <text x="35" y="24" font-size="6" font-weight="bold" fill="#1d4ed8">Cluster A</text>
      <circle cx="45" cy="48" r="3.5" fill="#dc2626"/>
      <text x="45" y="42" font-size="6" font-weight="bold" fill="#dc2626" text-anchor="middle">Point i</text>
      <circle cx="30" cy="58" r="2.2" fill="#3b82f6"/>
      <circle cx="58" cy="62" r="2.2" fill="#3b82f6"/>
      <circle cx="52" cy="34" r="2.2" fill="#3b82f6"/>
      <line x1="45" y1="48" x2="30" y2="58" stroke="#3b82f6" stroke-width="1"/>
      <text x="42" y="68" font-size="5.8" fill="#1d4ed8" text-anchor="middle">a(i) = Cohesion</text>
      <ellipse cx="138" cy="48" rx="26" ry="32" fill="#f0fdf4" stroke="#16a34a" stroke-dasharray="2,2"/>
      <text x="138" y="24" font-size="6" font-weight="bold" fill="#15803d">Nearest Cluster B</text>
      <circle cx="125" cy="45" r="2.2" fill="#16a34a"/>
      <circle cx="145" cy="58" r="2.2" fill="#16a34a"/>
      <line x1="45" y1="48" x2="125" y2="45" stroke="#dc2626" stroke-width="1.5"/>
      <text x="85" y="42" font-size="6" font-weight="bold" fill="#dc2626" text-anchor="middle">b(i) = Separation</text>
      <text x="90" y="88" font-size="6" font-weight="bold" fill="#0f172a" text-anchor="middle">s(i) = (b - a) / max(a, b)</text>
    </svg>
    <div class="diagram-caption">2. Silhouette Analysis Anatomy</div>
  </div>
</div>

---

# 📌 SECTION 4: QUESTION 4 — PROBABILISTIC LEARNING: NAÏVE BAYES & BBN (UNIT 4.1)

## 4.1 PART A: CALCULATION ENGINE & UNIVERSAL RECIPES

### Universal Plug-and-Play Recipe for ANY Classification Table
```text
[STEP 1: Prior Probabilities]
  P(Yes) = N_yes / N,   P(No) = N_no / N.
[STEP 2: Likelihood Grid for Query X = (x1, x2, ...)]
  For each feature:
    P(x_i | Yes) = Count(x_i in Yes) / N_yes
    P(x_i | No)  = Count(x_i in No)  / N_no
  *If count is 0, use Laplace Smoothing: (0 + 1) / (N_class + K_distinct_options).
[STEP 3: Multiply Likelihoods & Multiply by Priors]
  Score(Yes) = P(Yes) * P(x1|Yes) * P(x2|Yes) * ...
  Score(No)  = P(No)  * P(x1|No)  * P(x2|No)  * ...
[STEP 4: Decision]
  Whichever score is larger wins! Normalized % = Score / (Score_Yes + Score_No).
```

### Solved Numerical: 14-Row `buys_computer` Problem (Slide 4.1)

> 🎯 **EXACT SLIDE QUESTION WORDING (Slide 4.1, Page 20-21)**:  
> *"Given the 14-record AllElectronics customer training database with attributes: Age ($\le 30, 31..40, >40$), Income (high, medium, low), Student (no, yes), Credit_rating (fair, excellent), and Class: buys_computer (yes, no).  
> Data to be classified:  
> $X = (\text{age} \le 30, \text{income} = \text{medium}, \text{student} = \text{yes}, \text{credit\_rating} = \text{fair})$.  
> Task: Classify $X$ using Bayesian classifier ????"*

#### Step-by-Step Solution:
1. **Priors**: $P(\text{yes}) = 9/14 = 0.643$, $P(\text{no}) = 5/14 = 0.357$.
2. **Likelihoods**:
   * $P(\text{age} \le 30 \mid \text{yes}) = 2/9 = 0.222$; $P(\text{age} \le 30 \mid \text{no}) = 3/5 = 0.600$
   * $P(\text{income} = \text{med} \mid \text{yes}) = 4/9 = 0.444$; $P(\text{income} = \text{med} \mid \text{no}) = 2/5 = 0.400$
   * $P(\text{student} = \text{yes} \mid \text{yes}) = 6/9 = 0.667$; $P(\text{student} = \text{yes} \mid \text{no}) = 1/5 = 0.200$
   * $P(\text{credit} = \text{fair} \mid \text{yes}) = 6/9 = 0.667$; $P(\text{credit} = \text{fair} \mid \text{no}) = 2/5 = 0.400$
3. **Likelihood Products**:  
   * $P(X \mid \text{yes}) = 0.222 \times 0.444 \times 0.667 \times 0.667 = \mathbf{0.0438}$
   * $P(X \mid \text{no}) = 0.600 \times 0.400 \times 0.200 \times 0.400 = \mathbf{0.0192}$
4. **Posteriors (Unnormalized Scores)**:  
   * $\text{Score}(\text{yes}) = 0.0438 \times 0.643 = \mathbf{0.0282}$
   * $\text{Score}(\text{no}) = 0.0192 \times 0.357 = \mathbf{0.0069}$
5. **Decision**: $\text{Score}(\text{yes}) > \text{Score}(\text{no}) \implies$ **buys_computer = YES (80.3% confidence)**.

---

### Solved Numerical: Continuous Gaussian Naïve Bayes

> 🎯 **EXACT EXAM QUESTION WORDING / PATTERN (Continuous Naïve Bayes)**:  
> *"In a continuous Naïve Bayes classification problem, attribute $X$ follows a Gaussian distribution with class mean $\mu = 80$ and variance $\sigma^2 = 25$ ($\sigma = 5$). Compute the class-conditional probability density $P(X = 85 \mid C)$."*

$$P(x = 85 \mid C) = \frac{1}{\sqrt{2\pi(25)}} \exp\left(-\frac{(85-80)^2}{2(25)}\right) = \frac{1}{12.533} e^{-0.50} = \frac{0.6065}{12.533} \approx \mathbf{0.0484}$$

---

## 4.2 PART B: 10-MARK THEORY MASTER MODULE — PROBABILISTIC LEARNING & BBN

### 1. Bayes Theorem & Maximum A Posteriori (MAP) Derivation
* **Bayes Theorem**:
  $$P(C_k \mid X) = \frac{P(X \mid C_k) P(C_k)}{P(X)} = \frac{P(X \mid C_k) P(C_k)}{\sum_j P(X \mid C_j) P(C_j)}$$
  * $P(C_k)$ = Class Prior; $P(X \mid C_k)$ = Likelihood; $P(X)$ = Marginal Evidence; $P(C_k \mid X)$ = Posterior.
* **MAP vs Maximum Likelihood (ML)**:
  * **MAP Classifier**: Picks class maximizing posterior: $\hat{y}_{\text{MAP}} = \arg\max_{C_k} P(X \mid C_k) P(C_k)$.
  * **ML Classifier**: Assumes uniform priors ($P(C_k) = 1/K$): $\hat{y}_{\text{ML}} = \arg\max_{C_k} P(X \mid C_k)$.
* **Bayes Optimal Classifier**: Averages predictions over all hypotheses weighted by posterior: $P(y \mid X) = \sum_{h \in \mathcal{H}} P(y \mid h, X) P(h \mid D)$. Theoretical gold standard minimum error.

### 2. The Naïve Bayes Assumption & Parameter Reduction Proof
* **The "Naïve" Conditional Independence Assumption**:
  Given class label $C$, all features $x_1, \dots, x_d$ are mutually conditionally independent:
  $$P(X \mid C) = P(x_1, x_2, \dots, x_d \mid C) = \prod_{i=1}^d P(x_i \mid C)$$
* **Parameter Reduction**: Reduces full joint complexity from $O(2^d)$ exponential parameters to $O(d)$ linear parameters.

### 3. Handling Zero-Frequency: Laplace Smoothing Derivation
* **Problem**: If feature value $x_i$ never appears with class $C_k$, $P(x_i \mid C_k) = 0$, collapsing the entire product to zero.
* **Laplace (Add-One) Correction**: $\hat{P}(x_i \mid C_k) = \frac{\text{Count}(x_i, C_k) + 1}{N_k + |V_i|}$.  
  Proof of total probability preservation: $\sum_v \hat{P} = \frac{\sum \text{Count} + |V_i|}{N_k + |V_i|} = \frac{N_k + |V_i|}{N_k + |V_i|} = 1.000$.

### 4. Bayesian Belief Networks (BBN) & D-Separation Topologies (Must Draw in Exam!)

<div class="diagram-grid">
  <div class="diagram-card">
    <svg width="125" height="70" viewBox="0 0 125 70" xmlns="http://www.w3.org/2000/svg">
      <circle cx="20" cy="35" r="12" fill="#eff6ff" stroke="#1e40af" stroke-width="1.2"/>
      <text x="20" y="38" font-size="7.5" font-weight="bold" fill="#1e40af" text-anchor="middle">A</text>
      <line x1="32" y1="35" x2="48" y2="35" stroke="#334155" stroke-width="1.5"/>
      <polygon points="48,32 54,35 48,38" fill="#334155"/>
      <circle cx="65" cy="35" r="12" fill="#cbd5e1" stroke="#334155" stroke-width="1.5"/>
      <text x="65" y="38" font-size="7.5" font-weight="bold" fill="#0f172a" text-anchor="middle">B</text>
      <line x1="77" y1="35" x2="93" y2="35" stroke="#334155" stroke-width="1.5"/>
      <polygon points="93,32 99,35 93,38" fill="#334155"/>
      <circle cx="108" cy="35" r="12" fill="#eff6ff" stroke="#1e40af" stroke-width="1.2"/>
      <text x="108" y="38" font-size="7.5" font-weight="bold" fill="#1e40af" text-anchor="middle">C</text>
      <text x="62" y="60" font-size="6" font-weight="bold" fill="#15803d" text-anchor="middle">A ⊥ C | B (Blocked)</text>
    </svg>
    <div class="diagram-caption">1. Serial Connection</div>
  </div>
  <div class="diagram-card">
    <svg width="125" height="70" viewBox="0 0 125 70" xmlns="http://www.w3.org/2000/svg">
      <circle cx="62" cy="18" r="12" fill="#cbd5e1" stroke="#334155" stroke-width="1.5"/>
      <text x="62" y="21" font-size="7.5" font-weight="bold" fill="#0f172a" text-anchor="middle">B</text>
      <line x1="53" y1="26" x2="33" y2="44" stroke="#334155" stroke-width="1.5"/>
      <polygon points="32,40 28,48 37,45" fill="#334155"/>
      <circle cx="20" cy="52" r="12" fill="#eff6ff" stroke="#1e40af" stroke-width="1.2"/>
      <text x="20" y="55" font-size="7.5" font-weight="bold" fill="#1e40af" text-anchor="middle">A</text>
      <line x1="71" y1="26" x2="91" y2="44" stroke="#334155" stroke-width="1.5"/>
      <polygon points="87,45 96,48 92,40" fill="#334155"/>
      <circle cx="104" cy="52" r="12" fill="#eff6ff" stroke="#1e40af" stroke-width="1.2"/>
      <text x="104" y="55" font-size="7.5" font-weight="bold" fill="#1e40af" text-anchor="middle">C</text>
      <text x="62" y="66" font-size="6" font-weight="bold" fill="#15803d" text-anchor="middle">A ⊥ C | B (Common Cause)</text>
    </svg>
    <div class="diagram-caption">2. Diverging Connection</div>
  </div>
  <div class="diagram-card">
    <svg width="125" height="70" viewBox="0 0 125 70" xmlns="http://www.w3.org/2000/svg">
      <circle cx="20" cy="22" r="12" fill="#eff6ff" stroke="#1e40af" stroke-width="1.2"/>
      <text x="20" y="25" font-size="7.5" font-weight="bold" fill="#1e40af" text-anchor="middle">A</text>
      <circle cx="104" cy="22" r="12" fill="#eff6ff" stroke="#1e40af" stroke-width="1.2"/>
      <text x="104" y="25" font-size="7.5" font-weight="bold" fill="#1e40af" text-anchor="middle">C</text>
      <line x1="30" y1="29" x2="52" y2="43" stroke="#dc2626" stroke-width="1.5"/>
      <polygon points="50,39 57,46 47,44" fill="#dc2626"/>
      <line x1="94" y1="29" x2="72" y2="43" stroke="#dc2626" stroke-width="1.5"/>
      <polygon points="77,44 67,46 74,39" fill="#dc2626"/>
      <circle cx="62" cy="52" r="12" fill="#fecaca" stroke="#b91c1c" stroke-width="1.5"/>
      <text x="62" y="55" font-size="7.5" font-weight="bold" fill="#991b1b" text-anchor="middle">B</text>
      <text x="62" y="67" font-size="5.5" font-weight="bold" fill="#dc2626" text-anchor="middle">B observed => Active!</text>
    </svg>
    <div class="diagram-caption">3. V-Structure / Collider</div>
  </div>
  <div class="diagram-card">
    <svg width="125" height="70" viewBox="0 0 125 70" xmlns="http://www.w3.org/2000/svg">
      <rect x="15" y="4" width="95" height="62" rx="8" fill="#ecfdf5" stroke="#059669" stroke-width="1.2" stroke-dasharray="3,2"/>
      <circle cx="45" cy="18" r="9" fill="#eff6ff" stroke="#1e40af" stroke-width="1"/>
      <text x="45" y="21" font-size="6" font-weight="bold" fill="#1e40af" text-anchor="middle">Parent</text>
      <line x1="45" y1="27" x2="45" y2="33" stroke="#334155" stroke-width="1.2"/>
      <polygon points="42,32 45,36 48,32" fill="#334155"/>
      <circle cx="45" cy="42" r="9" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
      <text x="45" y="45" font-size="7" font-weight="bold" fill="#854d0e" text-anchor="middle">Target X</text>
      <line x1="45" y1="51" x2="45" y2="54" stroke="#334155" stroke-width="1.2"/>
      <polygon points="42,53 45,57 48,53" fill="#334155"/>
      <circle cx="45" cy="58" r="6.5" fill="#eff6ff" stroke="#1e40af" stroke-width="1"/>
      <text x="45" y="60.5" font-size="5" font-weight="bold" fill="#1e40af" text-anchor="middle">Child</text>
      <circle cx="85" cy="42" r="7.5" fill="#eff6ff" stroke="#1e40af" stroke-width="1"/>
      <text x="85" y="44.5" font-size="4.8" font-weight="bold" fill="#1e40af" text-anchor="middle">Co-Parent</text>
      <line x1="77" y1="46" x2="52" y2="56" stroke="#334155" stroke-width="1.2"/>
      <polygon points="53,53 49,57 55,58" fill="#334155"/>
      <text x="96" y="16" font-size="5" font-weight="bold" fill="#059669">MB(X)</text>
    </svg>
    <div class="diagram-caption">4. Markov Blanket of X</div>
  </div>
</div>

* **Chain Rule of BBNs**: $P(X_1, \dots, X_n) = \prod P(X_i \mid \text{Parents}(X_i))$.
* **Markov Blanket**: Consists of Parents + Children + Co-parents. Conditioning on the Markov Blanket completely insulates node $X$ from the rest of the network.

---

# 📌 SECTION 5: QUESTION 5 — ASSOCIATION RULE MINING: APRIORI & FP-GROWTH (UNIT 4.2)

## 5.1 PART A: CALCULATION ENGINE & UNIVERSAL RECIPES

### Universal Plug-and-Play Recipe for Apriori
```text
[STEP 1: Support Threshold]
  If min_sup given as %, min_count = ceil(% * Total_Transactions).
[STEP 2: Level-wise Generation C_1 -> L_1, C_2 -> L_2]
  Count frequency of individual items in DB -> L_1.
  Pair up items from L_1 -> scan DB for counts -> keep pairs >= min_count -> L_2.
[STEP 3: C_3 Candidate Generation & The Apriori Pruning Step]
  Join L_2 pairs sharing first item: {A,B} + {A,C} -> {A,B,C}.
  *PRUNING RULE*: Check if all 2-item subsets {A,B}, {A,C}, {B,C} are in L_2.
  If ANY subset is missing from L_2 -> PRUNE IT! Do not scan DB!
  Scan DB for remaining candidates -> L_3.
[STEP 4: Confidence & Rule Extraction]
  Confidence(X => Y) = Support_Count(X U Y) / Support_Count(X) * 100%.
  If Confidence >= min_conf -> Rule is STRONG!
  Lift(X => Y) = Confidence(X => Y) / Support(Y). (Lift > 1 = Positive correlation).
```

### Solved Numerical: 9-Transaction Apriori Problem (Slide 4.2, Exercise 1)

> 🎯 **EXACT SLIDE QUESTION WORDING (Slide 4.2, Page 17 — Exercise 1)**:  
> *"• Exercise 1: Find the frequent Itemset where the minimum support count = 2.  
> Given 9 transactions:  
> $T_{100}: \{I_1, I_2, I_5\}$  
> $T_{200}: \{I_2, I_4\}$  
> $T_{300}: \{I_2, I_3\}$  
> $T_{400}: \{I_1, I_2, I_4\}$  
> $T_{500}: \{I_1, I_3\}$  
> $T_{600}: \{I_2, I_3\}$  
> $T_{700}: \{I_1, I_3\}$  
> $T_{800}: \{I_1, I_2, I_3, I_5\}$  
> $T_{900}: \{I_1, I_2, I_3\}$  
> Show candidate generation and pruning for $C_1 \to L_1 \to C_2 \to L_2 \to C_3 \to L_3$ and generate strong association rules for minimum confidence $= 70\%$."*

#### Step-by-Step Level-wise Generation:
* $N = 9$, $\text{minsup\_count} = 2$, $\text{min\_conf} = 70\%$.
* **1-Itemsets ($L_1$)**:
  * $\{I_1\}: 6$, $\{I_2\}: 7$, $\{I_3\}: 6$, $\{I_4\}: 2$, $\{I_5\}: 2$. (All $\ge 2 \implies L_1$).
* **2-Itemsets ($L_2$)**:
  * $\{I_1, I_2\}: 4$, $\{I_1, I_3\}: 4$, $\{I_1, I_4\}: 1$ *(Pruned)*, $\{I_1, I_5\}: 2$, $\{I_2, I_3\}: 4$, $\{I_2, I_4\}: 2$, $\{I_2, I_5\}: 2$, $\{I_3, I_4\}: 0$ *(Pruned)*, $\{I_3, I_5\}: 1$ *(Pruned)*, $\{I_4, I_5\}: 0$ *(Pruned)*.
  * $L_2 = \{\{I_1, I_2\}, \{I_1, I_3\}, \{I_1, I_5\}, \{I_2, I_3\}, \{I_2, I_4\}, \{I_2, I_5\}\}$.
* **3-Itemset Candidate Generation & Pruning ($C_3$)**:
  * Join $\{I_1, I_2\} \Join \{I_1, I_3\} \implies \{I_1, I_2, I_3\}$. Subsets: $\{I_1,I_2\}, \{I_1,I_3\}, \{I_2,I_3\} \in L_2 \implies$ **Retained**.
  * Join $\{I_1, I_2\} \Join \{I_1, I_5\} \implies \{I_1, I_2, I_5\}$. Subsets: $\{I_1,I_2\}, \{I_1,I_5\}, \{I_2,I_5\} \in L_2 \implies$ **Retained**.
  * Join $\{I_2, I_3\} \Join \{I_2, I_4\} \implies \{I_2, I_3, I_4\}$. Subset $\{I_3, I_4\} \notin L_2 \implies$ **PRUNED!**
  * Database Scan for retained candidates: Count($\{I_1, I_2, I_3\}$) $= 2$, Count($\{I_1, I_2, I_5\}$) $= 2$.
  * $L_3 = \{\{I_1, I_2, I_3\}, \{I_1, I_2, I_5\}\}$.
* **Rule Generation from $\{I_1, I_2, I_5\}$ (Count $= 2$)**:
  * $I_1 \wedge I_5 \Rightarrow I_2$: $\text{Conf} = \frac{\sigma(I_1, I_2, I_5)}{\sigma(I_1, I_5)} = \frac{2}{2} = \mathbf{100\%}$ (**STRONG**)
  * $I_2 \wedge I_5 \Rightarrow I_1$: $\text{Conf} = \frac{\sigma(I_1, I_2, I_5)}{\sigma(I_2, I_5)} = \frac{2}{2} = \mathbf{100\%}$ (**STRONG**)
  * $I_5 \Rightarrow I_1 \wedge I_2$: $\text{Conf} = \frac{\sigma(I_1, I_2, I_5)}{\sigma(I_5)} = \frac{2}{2} = \mathbf{100\%}$ (**STRONG**)
  * $I_1 \wedge I_2 \Rightarrow I_5$: $\text{Conf} = \frac{\sigma(I_1, I_2, I_5)}{\sigma(I_1, I_2)} = \frac{2}{4} = 50\%$ (Weak, rejected).

---

## 5.2 PART B: 10-MARK THEORY MASTER MODULE — ASSOCIATION RULE MINING

### 1. Market Basket Problem Formulation & Mathematical Metrics
* **Itemset Lattice**: For $I = \{i_1, \dots, i_d\}$, there are $2^d$ possible itemsets.
* **Association Rule**: Implication $X \Rightarrow Y$ where $X, Y \subset I$ and $X \cap Y = \emptyset$.
* **Metrics (Must Define All 4 for 10 Marks)**:
  1. **Support**: $\text{Support}(X \Rightarrow Y) = \frac{\sigma(X \cup Y)}{N}$
  2. **Confidence**: $\text{Confidence}(X \Rightarrow Y) = \frac{\sigma(X \cup Y)}{\sigma(X)}$
  3. **Lift**: $\text{Lift}(X \Rightarrow Y) = \frac{P(X \cup Y)}{P(X)P(Y)} = \frac{\text{Confidence}(X \Rightarrow Y)}{\text{Support}(Y)}$ ($>1$ complementary, $=1$ independent, $<1$ substitute).
  4. **Conviction**: $\text{Conviction}(X \Rightarrow Y) = \frac{1 - \text{Support}(Y)}{1 - \text{Confidence}(X \Rightarrow Y)}$.

### 2. The Apriori Property (Anti-Monotonicity Principle) & Proof
* **Theorem**: *"All non-empty subsets of a frequent itemset must also be frequent."*
* **Contrapositive (Pruning Rule)**: *"If an itemset is infrequent, all of its supersets are guaranteed to be infrequent."*
* **Mathematical Proof**:
  Let $A \subset B$. Every transaction that contains $B$ must also contain $A$: $\{T \mid B \subseteq T\} \subseteq \{T \mid A \subseteq T\} \implies \sigma(B) \le \sigma(A)$.  
  If $\sigma(A) < \text{minsup}$, then $\sigma(B) \le \sigma(A) < \text{minsup}$, proving $B$ is strictly infrequent. $\blacksquare$

<div class="diagram-box">
  <svg width="450" height="85" viewBox="0 0 450 85" xmlns="http://www.w3.org/2000/svg">
    <!-- Level 1 -->
    <rect x="30" y="8" width="45" height="16" rx="2" fill="#eff6ff" stroke="#2563eb"/>
    <text x="52" y="19" font-size="6.5" font-weight="bold" fill="#1e40af" text-anchor="middle">{ A }</text>
    <rect x="90" y="8" width="45" height="16" rx="2" fill="#eff6ff" stroke="#2563eb"/>
    <text x="112" y="19" font-size="6.5" font-weight="bold" fill="#1e40af" text-anchor="middle">{ B }</text>
    <rect x="150" y="8" width="45" height="16" rx="2" fill="#eff6ff" stroke="#2563eb"/>
    <text x="172" y="19" font-size="6.5" font-weight="bold" fill="#1e40af" text-anchor="middle">{ C }</text>
    <rect x="210" y="8" width="45" height="16" rx="2" fill="#eff6ff" stroke="#2563eb"/>
    <text x="232" y="19" font-size="6.5" font-weight="bold" fill="#1e40af" text-anchor="middle">{ D }</text>
    <text x="360" y="19" font-size="6.5" fill="#475569" text-anchor="start">Level 1: Frequent 1-itemsets (L1)</text>

    <!-- Level 2 -->
    <rect x="25" y="34" width="70" height="18" rx="2" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
    <text x="60" y="46" font-size="6.5" font-weight="bold" fill="#b91c1c" text-anchor="middle">{ A, B } (Infrequent! ✗)</text>
    
    <rect x="105" y="34" width="45" height="18" rx="2" fill="#eff6ff" stroke="#2563eb"/>
    <text x="127" y="46" font-size="6.5" font-weight="bold" fill="#1e40af" text-anchor="middle">{ A, C } (✓)</text>
    <rect x="160" y="34" width="45" height="18" rx="2" fill="#eff6ff" stroke="#2563eb"/>
    <text x="182" y="46" font-size="6.5" font-weight="bold" fill="#1e40af" text-anchor="middle">{ B, C } (✓)</text>
    <text x="360" y="46" font-size="6.5" fill="#475569" text-anchor="start">Level 2: {A,B} &lt; minsup (Infrequent)</text>

    <!-- Pruning branches to Level 3 -->
    <line x1="60" y1="52" x2="60" y2="62" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3,2"/>
    <polygon points="57,60 60,64 63,60" fill="#dc2626"/>
    
    <rect x="15" y="64" width="90" height="16" rx="2" fill="#f8fafc" stroke="#dc2626" stroke-width="1" stroke-dasharray="3,2"/>
    <text x="60" y="75" font-size="6" font-weight="bold" fill="#dc2626" text-anchor="middle">{ A, B, C } PRUNED (✗)</text>

    <line x1="75" y1="52" x2="120" y2="62" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3,2"/>
    <polygon points="117,59 121,64 123,59" fill="#dc2626"/>
    
    <rect x="115" y="64" width="90" height="16" rx="2" fill="#f8fafc" stroke="#dc2626" stroke-width="1" stroke-dasharray="3,2"/>
    <text x="160" y="75" font-size="6" font-weight="bold" fill="#dc2626" text-anchor="middle">{ A, B, D } PRUNED (✗)</text>

    <rect x="220" y="64" width="220" height="16" rx="2" fill="#fef2f2" stroke="#ef4444"/>
    <text x="330" y="75" font-size="6.2" font-weight="bold" fill="#b91c1c" text-anchor="middle">APRIORI PROPERTY: All supersets of {A,B} pruned without DB scan!</text>
  </svg>
  <div class="diagram-caption">Apriori Anti-Monotone Property & Downward Closure Pruning Lattice (Slide 4.2, p. 10)</div>
</div>

### 3. FP-Growth (Frequent Pattern Growth) Architecture (Must Draw in Exam!)

<div class="diagram-box">
  <svg width="450" height="115" viewBox="0 0 450 115" xmlns="http://www.w3.org/2000/svg">
    <!-- Header Table -->
    <rect x="15" y="10" width="105" height="95" fill="#f8fafc" stroke="#334155" stroke-width="1.2" rx="3"/>
    <rect x="15" y="10" width="105" height="18" fill="#e2e8f0" stroke="#334155"/>
    <text x="25" y="22" font-size="6.5" font-weight="bold" fill="#0f172a">Item</text>
    <text x="55" y="22" font-size="6.5" font-weight="bold" fill="#0f172a">Count</text>
    <text x="92" y="22" font-size="6.5" font-weight="bold" fill="#0f172a">Link</text>
    
    <text x="28" y="37" font-size="6.5">I2</text><text x="60" y="37" font-size="6.5">7</text><circle cx="98" cy="35" r="2.5" fill="#dc2626"/>
    <text x="28" y="52" font-size="6.5">I1</text><text x="60" y="52" font-size="6.5">6</text><circle cx="98" cy="50" r="2.5" fill="#dc2626"/>
    <text x="28" y="67" font-size="6.5">I3</text><text x="60" y="67" font-size="6.5">6</text><circle cx="98" cy="65" r="2.5" fill="#dc2626"/>
    <text x="28" y="82" font-size="6.5">I4</text><text x="60" y="82" font-size="6.5">2</text><circle cx="98" cy="80" r="2.5" fill="#dc2626"/>
    <text x="28" y="97" font-size="6.5">I5</text><text x="60" y="97" font-size="6.5">2</text><circle cx="98" cy="95" r="2.5" fill="#dc2626"/>
    
    <!-- Tree Root -->
    <rect x="250" y="10" width="55" height="18" rx="3" fill="#cbd5e1" stroke="#334155"/>
    <text x="277" y="22" font-size="7" font-weight="bold" fill="#0f172a" text-anchor="middle">null (root)</text>
    
    <!-- Level 1 Nodes -->
    <rect x="180" y="40" width="45" height="18" rx="3" fill="#eff6ff" stroke="#2563eb"/>
    <text x="202" y="52" font-size="7" font-weight="bold" fill="#1e40af" text-anchor="middle">I2 : 7</text>
    
    <rect x="330" y="40" width="45" height="18" rx="3" fill="#eff6ff" stroke="#2563eb"/>
    <text x="352" y="52" font-size="7" font-weight="bold" fill="#1e40af" text-anchor="middle">I1 : 2</text>
    
    <line x1="260" y1="28" x2="202" y2="40" stroke="#334155" stroke-width="1.2"/>
    <line x1="290" y1="28" x2="352" y2="40" stroke="#334155" stroke-width="1.2"/>
    
    <!-- Level 2 Nodes -->
    <rect x="145" y="70" width="45" height="18" rx="3" fill="#eff6ff" stroke="#2563eb"/>
    <text x="167" y="82" font-size="7" font-weight="bold" fill="#1e40af" text-anchor="middle">I1 : 4</text>
    
    <rect x="205" y="70" width="45" height="18" rx="3" fill="#eff6ff" stroke="#2563eb"/>
    <text x="227" y="82" font-size="7" font-weight="bold" fill="#1e40af" text-anchor="middle">I4 : 2</text>
    
    <line x1="190" y1="58" x2="167" y2="70" stroke="#334155" stroke-width="1.2"/>
    <line x1="215" y1="58" x2="227" y2="70" stroke="#334155" stroke-width="1.2"/>
    
    <rect x="330" y="70" width="45" height="18" rx="3" fill="#eff6ff" stroke="#2563eb"/>
    <text x="352" y="82" font-size="7" font-weight="bold" fill="#1e40af" text-anchor="middle">I3 : 2</text>
    <line x1="352" y1="58" x2="352" y2="70" stroke="#334155" stroke-width="1.2"/>
    
    <!-- Horizontal Links (Dotted Red) -->
    <path d="M 98 35 H 175" stroke="#dc2626" stroke-width="1.2" stroke-dasharray="2,2"/>
    <path d="M 98 50 C 120 50, 130 79, 145 79" stroke="#dc2626" stroke-width="1.2" stroke-dasharray="2,2" fill="none"/>
    <path d="M 190 79 C 230 79, 280 50, 330 50" stroke="#dc2626" stroke-width="1.2" stroke-dasharray="2,2" fill="none"/>
  </svg>
  <div class="diagram-caption">FP-Tree Architecture: Header Table & Prefix Tree with Horizontal Node-Links (Slide 4.2)</div>
</div>

* **2-Pass Algorithmic Pipeline**:
  1. **Pass 1**: Scan DB $\to$ individual item support counts $\to$ filter by minsup $\to$ sort into descending frequency list (F-List).
  2. **Pass 2**: Construct the **FP-Tree** by inserting each transaction as a common prefix branch; create Header Table with linked list pointers connecting identical items across branches.
  3. **Mining Patterns**: Extract Conditional Pattern Base $\to$ build Conditional FP-Tree $\to$ recursively generate patterns (Zero candidate generation!).

### 4. Comprehensive Comparison: Apriori vs FP-Growth (Must Draw for 10 Marks)

| Feature | Apriori Algorithm | FP-Growth Algorithm |
| :--- | :--- | :--- |
| **Database Scans** | Multiple scans ($k$ scans for $k$-itemsets) | **Exactly 2 database scans** |
| **Candidate Generation** | Generates millions of candidate sets ($L_k \Join L_k$) | **Zero candidate generation** |
| **Memory Footprint** | Low initial memory, but explodes during joins | High initial memory to hold FP-Tree in RAM |
| **Data Structure** | Array / Hash-Tree of candidates | Compact, highly compressed **Prefix Tree (FP-Tree)** |
| **Runtime Speed** | Slow, bounded by disk I/O and candidate joins | Fast (typically 10x to 100x faster than Apriori) |
| **Scalability** | Poor on dense datasets with long patterns | Highly scalable on dense and large datasets |

---

# 🏆 SECTION 6: THE PROFESSOR'S EXACT MODULE ACTIVITIES (FULLY SOLVED)

## 6.1 Task A9 (Slide 3.5, p.25): Hierarchical AGNES on $\{8, 11, 21, 29, 36\}$

> 🎯 **EXACT SLIDE QUESTION WORDING [Task A9] (Slide 3.5, Page 25)**:  
> *"TASK FOR YOU [A9]:  
> Consider one-dimensional data set $\{8, 11, 21, 29, 36\}$, perform hierarchical clustering to decide the clusters using single linkage and complete linkage analysis and plot the respective dendrogram to visualize it.  
> Give some key inferences to distinguish between those two analysis."*

### Step 1: Initial Distance Matrix $D_0$:
$$D_0 = \begin{pmatrix} & 8 & 11 & 21 & 29 & 36 \\ 8 & 0 & 3 & 13 & 21 & 28 \\ 11 & 3 & 0 & 10 & 18 & 25 \\ 21 & 13 & 10 & 0 & 8 & 15 \\ 29 & 21 & 18 & 8 & 0 & 7 \\ 36 & 28 & 25 & 15 & 7 & 0 \end{pmatrix}$$
* Smallest distance is $d(8, 11) = \mathbf{3}$. Merge $\{8, 11\}$ at height $h = 3$.

### Step 2: Distance Matrix $D_1$:
* Smallest remaining distance is $d(29, 36) = \mathbf{7}$. Merge $\{29, 36\}$ at height $h = 7$.

### Step 3: Distance Matrix $D_2$ (Deciding Point 21):
* Distance to point 21:
  * Single Linkage: $d(\{8,11\}, 21) = \min(13, 10) = 10$; $d(\{29,36\}, 21) = \min(8, 15) = \mathbf{8}$.  
    **Single Link Choice**: Merge 21 into $\{29, 36\} \implies \{21, 29, 36\}$ at $h = 8$.
  * Complete Linkage: $d(\{8,11\}, 21) = \max(13, 10) = \mathbf{13}$; $d(\{29,36\}, 21) = \max(8, 15) = 15$.  
    **Complete Link Choice**: Merge 21 into $\{8, 11\} \implies \{8, 11, 21\}$ at $h = 13$.

### Step 4: Final Merges & Cluster Output:
* **Single Linkage**: Final merge at $h = \min(13, 21, 28, 10, 18, 25) = \mathbf{10}$.  
  **Clusters ($k=2$)**: **$\{8, 11\}$ and $\{21, 29, 36\}$**.
* **Complete Linkage**: Final merge at $h = \max(21, 28, 18, 25, 8, 15) = \mathbf{28}$.  
  **Clusters ($k=2$)**: **$\{8, 11, 21\}$ and $\{29, 36\}$**.

#### Task A9 Single Linkage Dendrogram:
```text
Height (h)
  10 |       +-----------------------+
     |       |                       |
   8 |       |               +-------+
     |       |               |       |
   7 |       |               |   +---+
     |       |               |   |   |
   3 |   +---+               |   |   |
     |   |   |               |   |   |
   0 +---+---+---------------+---+---+
         8   11              21  29  36
```

#### Task A9 Complete Linkage Dendrogram:
```text
Height (h)
  28 |   +---------------------------+
     |   |                           |
  13 |   +---------------+           |
     |   |               |           |
   7 |   |               |       +---+
     |   |               |       |   |
   3 | +-+-+             |       |   |
     | |   |             |       |   |
   0 +-+---+-------------+-------+---+
       8   11            21      29  36
```

<div class="diagram-grid">
  <div class="diagram-card" style="flex: 1;">
    <svg width="230" height="110" viewBox="0 0 240 110" xmlns="http://www.w3.org/2000/svg">
      <!-- Y Axis -->
      <line x1="28" y1="12" x2="28" y2="95" stroke="#334155" stroke-width="1.2"/>
      <text x="22" y="16" font-size="5.5" text-anchor="end" fill="#334155">10 -</text>
      <text x="22" y="32" font-size="5.5" text-anchor="end" fill="#334155">8 -</text>
      <text x="22" y="40" font-size="5.5" text-anchor="end" fill="#334155">7 -</text>
      <text x="22" y="72" font-size="5.5" text-anchor="end" fill="#334155">3 -</text>
      <text x="22" y="95" font-size="5.5" text-anchor="end" fill="#334155">0 -</text>
      <text x="10" y="55" font-size="6" font-weight="bold" fill="#1e3a8a" transform="rotate(-90 10 55)" text-anchor="middle">Height (h)</text>

      <!-- Baseline -->
      <line x1="28" y1="95" x2="230" y2="95" stroke="#334155" stroke-width="1.2"/>
      <text x="45" y="104" font-size="6.5" font-weight="bold" fill="#0f172a" text-anchor="middle">8</text>
      <text x="75" y="104" font-size="6.5" font-weight="bold" fill="#0f172a" text-anchor="middle">11</text>
      <text x="115" y="104" font-size="6.5" font-weight="bold" fill="#0f172a" text-anchor="middle">21</text>
      <text x="150" y="104" font-size="6.5" font-weight="bold" fill="#0f172a" text-anchor="middle">29</text>
      <text x="185" y="104" font-size="6.5" font-weight="bold" fill="#0f172a" text-anchor="middle">36</text>

      <!-- Single Linkage Tree -->
      <line x1="45" y1="95" x2="45" y2="72" stroke="#0284c7" stroke-width="1.5"/>
      <line x1="75" y1="95" x2="75" y2="72" stroke="#0284c7" stroke-width="1.5"/>
      <line x1="45" y1="72" x2="75" y2="72" stroke="#0284c7" stroke-width="1.5"/>
      <text x="60" y="68" font-size="5.5" fill="#0284c7" font-weight="bold" text-anchor="middle">h=3</text>

      <line x1="150" y1="95" x2="150" y2="40" stroke="#0284c7" stroke-width="1.5"/>
      <line x1="185" y1="95" x2="185" y2="40" stroke="#0284c7" stroke-width="1.5"/>
      <line x1="150" y1="40" x2="185" y2="40" stroke="#0284c7" stroke-width="1.5"/>
      <text x="167" y="37" font-size="5.5" fill="#0284c7" font-weight="bold" text-anchor="middle">h=7</text>

      <line x1="115" y1="95" x2="115" y2="32" stroke="#0284c7" stroke-width="1.5"/>
      <line x1="167" y1="40" x2="167" y2="32" stroke="#0284c7" stroke-width="1.5"/>
      <line x1="115" y1="32" x2="167" y2="32" stroke="#0284c7" stroke-width="1.5"/>
      <text x="141" y="29" font-size="5.5" fill="#0284c7" font-weight="bold" text-anchor="middle">h=8</text>

      <line x1="60" y1="72" x2="60" y2="16" stroke="#0284c7" stroke-width="1.5"/>
      <line x1="141" y1="32" x2="141" y2="16" stroke="#0284c7" stroke-width="1.5"/>
      <line x1="60" y1="16" x2="141" y2="16" stroke="#0284c7" stroke-width="1.5"/>
      <text x="100" y="13" font-size="5.5" fill="#0284c7" font-weight="bold" text-anchor="middle">h=10</text>

      <!-- Cut Line H=9 -->
      <line x1="28" y1="24" x2="160" y2="24" stroke="#dc2626" stroke-width="1.2" stroke-dasharray="3,2"/>
      <text x="165" y="26" font-size="5.5" fill="#dc2626" font-weight="bold" text-anchor="start">Cut H=9 (k=2)</text>
    </svg>
    <div class="diagram-caption">Task A9: Single Linkage Dendrogram</div>
    <div style="font-size: 5.8pt; color: #16a34a; font-weight: bold;">Final Clusters: {8, 11} and {21, 29, 36}</div>
  </div>

  <div class="diagram-card" style="flex: 1;">
    <svg width="230" height="110" viewBox="0 0 240 110" xmlns="http://www.w3.org/2000/svg">
      <!-- Y Axis -->
      <line x1="28" y1="12" x2="28" y2="95" stroke="#334155" stroke-width="1.2"/>
      <text x="22" y="16" font-size="5.5" text-anchor="end" fill="#334155">28 -</text>
      <text x="22" y="44" font-size="5.5" text-anchor="end" fill="#334155">13 -</text>
      <text x="22" y="62" font-size="5.5" text-anchor="end" fill="#334155">7 -</text>
      <text x="22" y="78" font-size="5.5" text-anchor="end" fill="#334155">3 -</text>
      <text x="22" y="95" font-size="5.5" text-anchor="end" fill="#334155">0 -</text>
      <text x="10" y="55" font-size="6" font-weight="bold" fill="#1e3a8a" transform="rotate(-90 10 55)" text-anchor="middle">Height (h)</text>

      <!-- Baseline -->
      <line x1="28" y1="95" x2="230" y2="95" stroke="#334155" stroke-width="1.2"/>
      <text x="45" y="104" font-size="6.5" font-weight="bold" fill="#0f172a" text-anchor="middle">8</text>
      <text x="75" y="104" font-size="6.5" font-weight="bold" fill="#0f172a" text-anchor="middle">11</text>
      <text x="115" y="104" font-size="6.5" font-weight="bold" fill="#0f172a" text-anchor="middle">21</text>
      <text x="150" y="104" font-size="6.5" font-weight="bold" fill="#0f172a" text-anchor="middle">29</text>
      <text x="185" y="104" font-size="6.5" font-weight="bold" fill="#0f172a" text-anchor="middle">36</text>

      <!-- Complete Linkage Tree -->
      <line x1="45" y1="95" x2="45" y2="78" stroke="#7c3aed" stroke-width="1.5"/>
      <line x1="75" y1="95" x2="75" y2="78" stroke="#7c3aed" stroke-width="1.5"/>
      <line x1="45" y1="78" x2="75" y2="78" stroke="#7c3aed" stroke-width="1.5"/>
      <text x="60" y="74" font-size="5.5" fill="#7c3aed" font-weight="bold" text-anchor="middle">h=3</text>

      <line x1="150" y1="95" x2="150" y2="62" stroke="#7c3aed" stroke-width="1.5"/>
      <line x1="185" y1="95" x2="185" y2="62" stroke="#7c3aed" stroke-width="1.5"/>
      <line x1="150" y1="62" x2="185" y2="62" stroke="#7c3aed" stroke-width="1.5"/>
      <text x="167" y="58" font-size="5.5" fill="#7c3aed" font-weight="bold" text-anchor="middle">h=7</text>

      <line x1="60" y1="78" x2="60" y2="44" stroke="#7c3aed" stroke-width="1.5"/>
      <line x1="115" y1="95" x2="115" y2="44" stroke="#7c3aed" stroke-width="1.5"/>
      <line x1="60" y1="44" x2="115" y2="44" stroke="#7c3aed" stroke-width="1.5"/>
      <text x="87" y="40" font-size="5.5" fill="#7c3aed" font-weight="bold" text-anchor="middle">h=13</text>

      <line x1="87" y1="44" x2="87" y2="16" stroke="#7c3aed" stroke-width="1.5"/>
      <line x1="167" y1="62" x2="167" y2="16" stroke="#7c3aed" stroke-width="1.5"/>
      <line x1="87" y1="16" x2="167" y2="16" stroke="#7c3aed" stroke-width="1.5"/>
      <text x="127" y="13" font-size="5.5" fill="#7c3aed" font-weight="bold" text-anchor="middle">h=28</text>

      <!-- Cut Line H=20 -->
      <line x1="28" y1="30" x2="155" y2="30" stroke="#dc2626" stroke-width="1.2" stroke-dasharray="3,2"/>
      <text x="160" y="32" font-size="5.5" fill="#dc2626" font-weight="bold" text-anchor="start">Cut H=20 (k=2)</text>
    </svg>
    <div class="diagram-caption">Task A9: Complete Linkage Dendrogram</div>
    <div style="font-size: 5.8pt; color: #16a34a; font-weight: bold;">Final Clusters: {8, 11, 21} and {29, 36}</div>
  </div>
</div>

#### Key Inferences (Must Write in Exam):
1. **Single Linkage favors nearest neighbors**, pulling point 21 towards the right cluster $\{29, 36\}$ because $|21-29|=8 < |21-11|=10$.
2. **Complete Linkage enforces compact diameter**, pulling point 21 towards the left cluster $\{8, 11\}$ because the maximum span $|21-8|=13$ is smaller than the span $|36-21|=15$.

---

## 6.2 Task A10 (Slide 3.6, p.21): K-Means on $\{3, 5, 10, 13, 4, 21, 31, 12, 26\}$ ($k=2$)

> 🎯 **EXACT SLIDE QUESTION WORDING [Task A10] (Slide 3.6, Page 21)**:  
> *"TASK FOR YOU [A10]:  
> 1. Using K-means clustering, cluster the following data into two clusters and show each step:  
> $\{3, 5, 10, 13, 4, 21, 31, 12, 26\}$.  
> Give your step-by-step computational analysis.  
> 2. Investigate the computational processes of the K-medoid algorithm with a suitable scenario."*

### Step-by-Step Computational Analysis ($m_1=3.0, m_2=5.0$):
* **Iteration 1**: Midpoint $= \frac{3.0 + 5.0}{2} = 4.0$.  
  $K_1 = \{3, 4\} \implies \mathbf{m_1^{(1)} = \frac{3+4}{2} = 3.50}$.  
  $K_2 = \{5, 10, 12, 13, 21, 26, 31\} \implies \mathbf{m_2^{(1)} = \frac{118}{7} = 16.86}$.
* **Iteration 2**: Midpoint $= \frac{3.50 + 16.86}{2} = 10.18$.  
  $K_1 = \{3, 4, 5, 10\} \implies \mathbf{m_1^{(2)} = \frac{22}{4} = 5.50}$.  
  $K_2 = \{12, 13, 21, 26, 31\} \implies \mathbf{m_2^{(2)} = \frac{103}{5} = 20.60}$.
* **Iteration 3**: Midpoint $= \frac{5.50 + 20.60}{2} = 13.05$.  
  $K_1 = \{3, 4, 5, 10, 12, 13\} \implies \mathbf{m_1^{(3)} = \frac{47}{6} = 7.83}$.  
  $K_2 = \{21, 26, 31\} \implies \mathbf{m_2^{(3)} = \frac{78}{3} = 26.00}$.
* **Iteration 4**: Midpoint $= \frac{7.83 + 26.00}{2} = 16.915$.  
  $K_1 = \{3, 4, 5, 10, 12, 13\}$ (Unchanged!).  
  $K_2 = \{21, 26, 31\}$ (Unchanged!) $\implies$ **CONVERGENCE ACHIEVED!**
* **Final Cluster Centroids**: $C_1 = 7.83, C_2 = 26.00$.
* **Total SSE**: $94.84 + 50.00 = \mathbf{144.84}$.

---

## 6.3 Task A11 (Slide 4.1, p.22-23): 20-Row Mammals Naïve Bayes Classification

> 🎯 **EXACT SLIDE QUESTION WORDING [Task A11] (Slide 4.1, Page 22-23)**:  
> *"Task to think in-depth - [A-11]:  
> Given the dataset of 20 animal instances with attributes: Give Birth, Can Fly, Live in Water, Have Legs, and Class (mammals vs non-mammals).  
> Classify the unknown test animal:  
> $X = (\text{Give Birth} = \text{yes}, \text{Can Fly} = \text{no}, \text{Live in Water} = \text{yes}, \text{Have Legs} = \text{no})$  
> using Naïve Bayes Classifier."*

### Step-by-Step Likelihood Calculations:
1. **Give Birth = yes**: $P(\text{Give Birth}=\text{yes} \mid M) = \frac{6}{7} \approx 0.8571$; $P(\text{Give Birth}=\text{yes} \mid NM) = \frac{1}{13} \approx 0.0769$.
2. **Can Fly = no**: $P(\text{Can Fly}=\text{no} \mid M) = \frac{6}{7} \approx 0.8571$; $P(\text{Can Fly}=\text{no} \mid NM) = \frac{10}{13} \approx 0.7692$.
3. **Live in Water = yes**: $P(\text{Live in Water}=\text{yes} \mid M) = \frac{2}{7} \approx 0.2857$; $P(\text{Live in Water}=\text{yes} \mid NM) = \frac{3}{13} \approx 0.2308$.
4. **Has Legs = no**: $P(\text{Has Legs}=\text{no} \mid M) = \frac{2}{7} \approx 0.2857$; $P(\text{Has Legs}=\text{no} \mid NM) = \frac{4}{13} \approx 0.3077$.

### Posterior Scoring:
* **Score(Mammal)**: $0.35 \times \left(\frac{6}{7} \times \frac{6}{7} \times \frac{2}{7} \times \frac{2}{7}\right) = 0.35 \times \frac{144}{2401} = \mathbf{0.02099}$.
* **Score(Non-Mammal)**: $0.65 \times \left(\frac{1}{13} \times \frac{10}{13} \times \frac{3}{13} \times \frac{4}{13}\right) = 0.65 \times \frac{120}{28561} = \mathbf{0.00273}$.
* **Decision**: Normalized $P(M \mid X) = \frac{0.02099}{0.02099 + 0.00273} = \mathbf{88.5\%} \implies$ **MAMMAL**.

---

## 6.4 Activity 8 (Slide 3.4, p.10, 19, 20): Cluster Quality & Similarity Metrics

> 🎯 **EXACT SLIDE QUESTION WORDING [Activity 8] (Slide 3.4, Page 10, 19, 20)**:  
> *"1. Purity in Clusters (p. 19): Assume that we cluster three category of data items (colored red, blue, green) into three clusters: Cluster I (5 red, 1 blue), Cluster II (1 red, 4 blue, 1 green), Cluster III (2 red, 0 blue, 3 green). Calculate purity to measure the quality of each cluster.  
> 2. Cosine Similarity (p. 10): Find the similarity between documents 1 and 2: $d_1 = (5, 0, 3, 0, 2, 0, 0, 2, 0, 0)$ and $d_2 = (3, 0, 2, 0, 1, 1, 0, 1, 0, 1)$.  
> 3. Jaccard Similarity (p. 20): Formulate a real-world scenario to use Jaccard similarity and compute similarity/distance between two object sets."*

### 1. Cluster Purity Calculation:
$$\text{Purity}(\Omega, \mathbb{C}) = \frac{1}{N} \sum_{k} \max_j |\omega_k \cap c_j| = \frac{5 + 4 + 3}{17} = \frac{12}{17} = \mathbf{70.59\%}$$

### 2. Cosine Similarity between Slide Vectors:
* Dot Product: $\mathbf{d_1} \cdot \mathbf{d_2} = (5\times3) + (3\times2) + (2\times1) + (2\times1) = 15 + 6 + 2 + 2 = \mathbf{25}$.
* Magnitudes: $\|\mathbf{d_1}\| = \sqrt{42} \approx 6.481$; $\|\mathbf{d_2}\| = \sqrt{17} \approx 4.123$.
* **Cosine Similarity**: $\cos(\mathbf{d_1}, \mathbf{d_2}) = \frac{25}{6.481 \times 4.123} = \frac{25}{26.721} \approx \mathbf{0.9356} \approx \mathbf{0.94}$.

### 3. Jaccard Similarity and Distance:
* $A = \{\text{Bread}, \text{Milk}, \text{Beer}\}$, $B = \{\text{Bread}, \text{Milk}, \text{Diaper}, \text{Eggs}, \text{Coke}\}$.
* $J(A, B) = \frac{|A \cap B|}{|A \cup B|} = \frac{2}{6} = \mathbf{0.333} \text{ (33.3\%)}$; $d_J(A, B) = 1 - 0.333 = \mathbf{0.667} \text{ (66.7\%)}$.

---

# 📌 SECTION 7: PRE-EXAM CALCULATOR SURVIVAL GUIDE & READY-TO-DRAW BLANK TABLES

### 1. Casio fx-991ES / fx-991EX Key-by-Key Keystrokes:
* **AdaBoost $\alpha$**: `0.5` $\times$ `ln(` `(` `1` `-` `[eps]` `)` `÷` `[eps]` `)` `=`
* **Multiplier $e^{-\alpha}$**: `SHIFT` + `ln` ($e^x$) $\to$ `(-[alpha])` `=`
* **Multiplier $e^{+\alpha}$**: `SHIFT` + `ln` ($e^x$) $\to$ `(+[alpha])` `=`
* **Euclidean Distance 2D**: `√(` `(` `x1` `-` `x2` `)` `x²` `+` `(` `y1` `-` `y2` `)` `x²` `)` `=`
* **Gaussian Density**: `1` `÷` `(` `√(` `2` `×` `π` `×` `[var]` `)` `)` $\times$ `SHIFT` `ln` `(` `-(` `[x]` `-` `[mu]` `)x²` `÷` `(` `2` `×` `[var]` `)` `)`

### 2. Ready-to-Draw Table Templates (Draw These Instantly in the Exam):

#### A. AdaBoost Iteration Table:
```text
+----------+----------+----------+----------+----------+------------+----------------+--------------+
| Sample i | True y_i | Pred h_t |  Status  |  Old w_i | Multiplier | Unnormalized w | Final w_new  |
+----------+----------+----------+----------+----------+------------+----------------+--------------+
| 1        |          |          |          |          |            |                |              |
| 2        |          |          |          |          |            |                |              |
| ...      |          |          |          |          |            |                |              |
+----------+----------+----------+----------+----------+------------+----------------+--------------+
| SUM      |    --    |    --    |    --    |  1.0000  |     --     | Z_t = ...      | 1.0000       |
+----------+----------+----------+----------+----------+------------+----------------+--------------+
```

#### B. K-Means Assignment & SSE Table:
```text
+----------+--------------+--------------+------------------+---------------------+
| Point x  | Dist to C_1  | Dist to C_2  | Assigned Cluster | Dist^2 (for SSE)    |
+----------+--------------+--------------+------------------+---------------------+
| x_1      |              |              |                  |                     |
| x_2      |              |              |                  |                     |
| ...      |              |              |                  |                     |
+----------+--------------+--------------+------------------+---------------------+
| TOTAL    |              |              |                  | Total SSE = ...     |
+----------+--------------+--------------+------------------+---------------------+
```

#### C. Naïve Bayes Feature Likelihood Table:
```text
+-------------------+----------------+--------------------+-------------------+------------------+
| Feature Attribute | Value in Query | Count in Class Yes | P(Feature \| Yes) | Count in Class No|
+-------------------+----------------+--------------------+-------------------+------------------+
| Attribute 1       |                |                    |                   |                  |
| Attribute 2       |                |                    |                   |                  |
| Attribute 3       |                |                    |                   |                  |
| Attribute 4       |                |                    |                   |                  |
+-------------------+----------------+--------------------+-------------------+------------------+
| CLASS PRIORS      |                | N_yes = ...        | P(Yes) = ...      | N_no = ...       |
| PRODUCT SCORE     |                |                    | Score(Yes) = ...  | Score(No) = ...  |
| FINAL DECISION    |                | Normalized %: ...  | WINNER: [ YES / NO ]                 |
+-------------------+----------------+--------------------+-------------------+------------------+
```
"""

import re

def sanitize_svgs(text):
    def clean_svg(match):
        svg_content = match.group(0)
        cleaned_lines = []
        for line in svg_content.splitlines():
            line_str = line.strip()
            if line_str:
                cleaned_lines.append(line_str)
        return '\n'.join(cleaned_lines)
    return re.sub(r'<svg[\s\S]*?</svg>', clean_svg, text)

clean_content = sanitize_svgs(content)

with open(MD_PATH, "w", encoding="utf-8") as f:
    f.write(clean_content)

print(f"Successfully generated master booklet: {MD_PATH}")
