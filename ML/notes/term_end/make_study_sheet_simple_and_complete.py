# -*- coding: utf-8 -*-
r"""
make_study_sheet_simple_and_complete.py
Rewrites 09-ml-guaranteed-topics-master-study-sheet.md based directly on the user's feedback:
1. Q1: Plain English PAC explanation, full step-by-step derivation, complete Option B (Version spaces, G and S boundaries, Candidate Elimination algorithm + Find-S trace).
2. Q2: Full buys_computer dataset, ID3 entropy math, AND the complete drawn Decision Tree diagram! Plus complete Option B answer (k-NN, Euclidean/Manhattan, Curse of Dimensionality, SVM Soft-margin slack variables and C).
3. Q3: AdaBoost with easy memory hooks, step trace, AND complete Option B answer (Bagging vs Boosting table, Random Forest in clinical medicine, ECOC matrix & Hamming trace).
4. Q4: Complete Naive Bayes Loan Approval + real-world critique, AND complete Option B answer (Apriori algorithm steps, candidate pruning, 10-transaction execution).
5. Q5: Imbalanced data, Accuracy paradox 1000 patients, SMOTE vector math, ROS vs SMOTE, AND complete Option B answer (500-patient Confusion Matrix calculations + Enterprise RAG architecture).
6. Q6: VC Dimension in simple terms with keywords, 1D interval proof (VC=2) in clean steps, Natarajan dimension in plain English.
7. Q7: SVM explained in student-friendly, standard exam format (Margin width 2/||w|| derivation, Support Vectors, Slack variables, Kernel Trick) removing confusing "Wolfe" jargon.
8. Q8: Hierarchical clustering on {5, 9, 14, 25, 28, 40} with step-by-step distance tables, merge heights, AND complete ASCII Dendrograms for both Single and Complete Linkage!
9. Q9: Standard high-probability Module 4 topic: Apriori Principle (Downward Closure Property, Candidate Generation, Pruning) vs Bayesian Belief Networks (BBN DAG & Chain Rule).
10. Q10: PCA Variance Maximization via Lagrange explained step-by-step in intuitive, plain terms.
"""

import os

output_path = r"c:\Users\ankit\Fall2627\ML\notes\term_end\09-ml-guaranteed-topics-master-study-sheet.md"

content = r"""# 🏆 CSE4005: Machine Learning — Ultimate TEE FAT Model Exam Paper & Complete Answer Script
### *Fully Solved Model Exam Paper in Exact VIT Bhopal TEE Format (TEE.txt)*

> **Course Code**: CSE4005 — Machine Learning | **Faculty**: Dr. Nilamadhab Mishra  
> **Slot**: A21+A23 | **Duration**: 3 Hours (Closed Book) | **Maximum Marks**: 100  
> **Pre-TEE Internal Standing**: **62.20 / 70.0** vs Class Mean **61.90 / 70.0** *(+0.30 ahead)*  
> **A Grade Target ($\ge \mu + 0.5\sigma$)**: **70–74 / 100** *(Must score ~10–12 marks above TEE class average)*  
> **S Grade Target (Total $\ge 90.0$)**: **93+ / 100** *(Strict VIT rule)*  
> **B-Grade Danger Zone**: **48–69 / 100** *(B Grade is an absolute NO-GO for CGPA)*  

---

## 📋 OFFICIAL TEE PAPER SPECIFICATION (FROM TEE.txt)
* **Section A (60 Marks)**: 5 Questions $\times$ 12 Marks (Questions 1 to 5). Exactly one question per module. Compulsory internal choice **"OR" format** (Both Option A and Option B fully solved below).
* **Section B (40 Marks)**: 5 Questions $\times$ 8 Marks (Questions 6 to 10). Exactly one question per module. Direct question **without subparts**.
* **Module Distribution**: Every single Module (1 to 5) carries **exactly 20 Marks** (12M in Section A + 8M in Section B).
* **Dataset Rule**: Every question provides the **entire, complete dataset table** directly in the question prompt. No abbreviations or missing rows.

---

## 📑 TEE QUESTION PAPER NAVIGATION MATRIX

| Section | Q# | Module | Core Exam Topic | Marks | Format |
|:---:|:---:|:---:|:---|:---:|:---:|
| **SEC A** | **Q1** | **Module 1** | [PAC Learnability & Sample Complexity Bound **OR** Version Spaces & Find-S Trace](#question-1-module-1--12-marks) | 12M | 12M OR 6M+6M |
| **SEC A** | **Q2** | **Module 2** | [ID3 Decision Tree (`buys_computer` + Drawn Tree) **OR** k-NN & SVM Slack](#question-2-module-2--12-marks) | 12M | 12M OR 6M+6M |
| **SEC A** | **Q3** | **Module 3** | [AdaBoost 5-Sample Weight Update Trace **OR** Bagging vs Boosting & ECOC](#question-3-module-3--12-marks) | 12M | 12M OR 6M+6M |
| **SEC A** | **Q4** | **Module 4** | [Naïve Bayes Loan Approval (12 Applicants) **OR** Apriori Mining (10 Transactions)](#question-4-module-4--12-marks) | 12M | 12M OR 6M+6M |
| **SEC A** | **Q5** | **Module 5** | [Imbalanced Data & SMOTE Math **OR** 500-Patient Confusion Matrix & RAG](#question-5-module-5--12-marks) | 12M | 12M OR 6M+6M |
| **SEC B** | **Q6** | **Module 1** | [VC Dimension ($VC=2$ Proof) & Natarajan Multiclass Dimension](#question-6-module-1--8-marks) | 8M | Direct 8M |
| **SEC B** | **Q7** | **Module 2** | [SVM Maximum Margin Width $2/\|\mathbf{w}\|$ & Support Vectors & Kernels](#question-7-module-2--8-marks) | 8M | Direct 8M |
| **SEC B** | **Q8** | **Module 3** | [Hierarchical AGNES Clustering on $\{5, 9, 14, 25, 28, 40\}$ with Full Dendrograms](#question-8-module-3--8-marks) | 8M | Direct 8M |
| **SEC B** | **Q9** | **Module 4** | [Apriori Principle (Downward Closure) & Bayesian Belief Networks (BBN)](#question-9-module-4--8-marks) | 8M | Direct 8M |
| **SEC B** | **Q10**| **Module 5** | [PCA Projected Variance Maximization Derivation via Lagrange Multipliers](#question-10-module-5--8-marks) | 8M | Direct 8M |

---
---

# ══════════════════════════════════════════════════
# SECTION A: 5 QUESTIONS $\times$ 12 MARKS = 60 MARKS
### *(Answer One Full Question from each Module — Internal Choice "OR" Format)*
# ══════════════════════════════════════════════════

---

# QUESTION 1 [Module 1 — 12 Marks]

### OPTION A:
*(a) Explain the Probably Approximately Correct (PAC) learning framework in simple terms. Define the error parameter $\epsilon$ and the confidence parameter $\delta$.* **[4 Marks]**  
*(b) For a finite hypothesis space $H$, derive the general PAC sample complexity bound:*  
$$m \ge \frac{1}{\epsilon} \left( \ln |H| + \ln \frac{1}{\delta} \right)$$  
*Explain what this formula tells us about how many training examples we need.* **[8 Marks]**

### OR

### OPTION B:
*(a) Explain Version Space learning. Define the General Boundary ($G$) and Specific Boundary ($S$), and write the Candidate Elimination algorithm update rules.* **[6 Marks]**  
*(b) The following complete 4-sample training dataset for the target concept `EnjoySport` is given:*  

| Example | Sky | AirTemp | Humidity | Wind | Water | Forecast | EnjoySport (Class) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Sunny | Warm | Normal | Strong | Warm | Same | **Yes** |
| 2 | Sunny | Warm | High | Strong | Warm | Same | **Yes** |
| 3 | Rainy | Cold | High | Strong | Warm | Change | **No** |
| 4 | Sunny | Warm | High | Strong | Cool | Change | **Yes** |

*Trace the step-by-step execution of the Find-S algorithm starting from the maximally specific hypothesis $h_0$. Show the updated hypothesis after observing each training instance and state the final hypothesis $h_4$.* **[6 Marks]**

---

### MODEL EXAM ANSWER FOR QUESTION 1 (OPTION A):

#### 1. What is PAC Learning? (Simple Explanation & Keywords)
* **Goal of PAC**: In real life, machine learning can almost never guarantee $100\%$ accuracy on unseen data. Instead, PAC learning demands that the model is **"Probably Approximately Correct"**:
  1. **Approximately Correct**: The true error of our learned hypothesis $h$ on future data is at most $\epsilon$ (Error tolerance, e.g. $\epsilon = 0.05 \implies \le 5\%$ error).
  2. **Probably**: The algorithm outputs such a good hypothesis with high confidence of at least $1 - \delta$ (e.g. if failure probability $\delta = 0.05 \implies 95\%$ confidence).
* **Formal PAC Condition**:
  $$P(\text{error}(h) \le \epsilon) \ge 1 - \delta$$
* **PAC Learnability**: A concept class is PAC-learnable if a learning algorithm can achieve this guarantee using a number of training examples $m$ that grows reasonably (polynomially) with $1/\epsilon, 1/\delta,$ and the problem size.

---

#### 2. Derivation of PAC Sample Complexity Bound ($m$)

Let $H$ be a finite hypothesis space. We consider a "consistent learner" (an algorithm that outputs a hypothesis $h$ that makes zero errors on the $m$ training examples).

#### Step 1: Probability that ONE "Bad" Hypothesis Survives One Example
* A hypothesis $h_{\text{bad}}$ is "bad" if its true error $> \epsilon$.
* For a single randomly drawn example, the probability that $h_{\text{bad}}$ happens to make a correct prediction is:
  $$P(\text{correct on 1 example}) = 1 - \text{error} < 1 - \epsilon$$

#### Step 2: Probability that ONE "Bad" Hypothesis Survives ALL $m$ Examples
* Since the $m$ training examples are drawn independently (i.i.d.):
  $$P(h_{\text{bad}} \text{ survives all } m \text{ examples}) < (1 - \epsilon)^m$$
* Using the standard mathematical inequality $(1 - x) \le e^{-x}$:
  $$(1 - \epsilon)^m \le e^{-m\epsilon}$$

#### Step 3: Probability that ANY Bad Hypothesis Survives (Union Bound)
* There are at most $|H|$ hypotheses in the hypothesis space.
* The probability that *at least one* bad hypothesis survives and tricks our learner is bounded by the sum of individual probabilities (Boole's Union Bound):
  $$P(\text{Learner Fails}) \le |H| \cdot (1 - \epsilon)^m \le |H| e^{-m\epsilon}$$

#### Step 4: Enforce the Failure Limit $\delta$
* We want the probability of failure to be at most $\delta$:
  $$|H| e^{-m\epsilon} \le \delta$$
* Divide both sides by $|H|$:
  $$e^{-m\epsilon} \le \frac{\delta}{|H|}$$
* Take the natural logarithm ($\ln$) on both sides:
  $$-m\epsilon \le \ln\left( \frac{\delta}{|H|} \right) = - \ln\left( \frac{|H|}{\delta} \right)$$
* Multiply by $-1$ (this flips the inequality sign $\le$ to $\ge$):
  $$m\epsilon \ge \ln\left( \frac{|H|}{\delta} \right) = \ln |H| + \ln\left(\frac{1}{\delta}\right)$$
* Divide by $\epsilon$:
  $$m \ge \frac{1}{\epsilon} \left( \ln |H| + \ln \frac{1}{\delta} \right)$$

$$\mathbf{\text{Final Boxed Result: } m \ge \frac{1}{\epsilon} \left( \ln |H| + \ln \frac{1}{\delta} \right)}$$

* **What this formula means**:
  1. If you want higher accuracy (smaller $\epsilon$), sample size $m$ must increase linearly ($1/\epsilon$).
  2. If you want higher confidence (smaller $\delta$), sample size $m$ only needs to increase slowly (logarithmically $\ln(1/\delta)$).
  3. If your hypothesis space $|H|$ is larger, you need more examples ($\ln |H|$).

---

### MODEL EXAM ANSWER FOR QUESTION 1 (OPTION B):

#### 1. Version Space Learning & Candidate Elimination

* **Version Space ($VS_{H, D}$)**: The subset of all hypotheses in $H$ that are completely consistent with all training examples in dataset $D$.
* **Boundary Representations**:
  - **General Boundary ($G$)**: The set of most general hypotheses consistent with $D$.
  - **Specific Boundary ($S$)**: The set of most specific hypotheses consistent with $D$.
* **Candidate Elimination Algorithm**:
  - Initialize $G = \{\langle ?, ?, ?, ?, ?, ? \rangle\}$ (accepts everything).
  - Initialize $S = \{\langle \Phi, \Phi, \Phi, \Phi, \Phi, \Phi \rangle\}$ (rejects everything).
  - **For a Positive Example**: Generalize $S$ just enough to cover the example. Remove from $G$ any hypothesis that does not cover it.
  - **For a Negative Example**: Specialize $G$ just enough to exclude the example. Remove from $S$ any hypothesis that covers it.

---

#### 2. Find-S Algorithm Step-by-Step Trace on `EnjoySport`

> 💡 **EXAM NOTE: Find-S Rules**  
> 1. Start with $h_0 = \langle \Phi, \Phi, \Phi, \Phi, \Phi, \Phi \rangle$.  
> 2. **Completely ignore negative examples** (Find-S only learns from positive examples).  
> 3. For positive examples: if the attribute matches, keep it. If it differs, replace with `?`.

* **Step 0 (Initialization)**:  
  $$h_0 = \langle \Phi, \; \Phi, \; \Phi, \; \Phi, \; \Phi, \; \Phi \rangle$$
* **Step 1: Observe Example 1 (Positive)**:  
  $\langle \text{Sunny, Warm, Normal, Strong, Warm, Same} \rangle \to \text{Yes}$  
  Replace all $\Phi$ with the exact values:  
  $$h_1 = \langle \text{Sunny, Warm, Normal, Strong, Warm, Same} \rangle$$
* **Step 2: Observe Example 2 (Positive)**:  
  $\langle \text{Sunny, Warm, High, Strong, Warm, Same} \rangle \to \text{Yes}$  
  Attribute `Humidity` changes from `Normal` to `High` $\implies$ generalize to `?`:  
  $$h_2 = \langle \text{Sunny, Warm, ?, Strong, Warm, Same} \rangle$$
* **Step 3: Observe Example 3 (Negative)**:  
  $\langle \text{Rainy, Cold, High, Strong, Warm, Change} \rangle \to \text{No}$  
  Negative example $\implies$ **IGNORED** by Find-S:  
  $$h_3 = h_2 = \langle \text{Sunny, Warm, ?, Strong, Warm, Same} \rangle$$
* **Step 4: Observe Example 4 (Positive)**:  
  $\langle \text{Sunny, Warm, High, Strong, Cool, Change} \rangle \to \text{Yes}$  
  `Water` changes from `Warm` to `Cool` $\implies$ generalize to `?`.  
  `Forecast` changes from `Same` to `Change` $\implies$ generalize to `?`:  
  $$h_4 = \langle \text{Sunny, Warm, ?, Strong, ?, ?} \rangle$$

$$\mathbf{\text{Final Output Hypothesis: } h_4 = \langle \text{Sunny, Warm, ?, Strong, ?, ?} \rangle}$$

---

# QUESTION 2 [Module 2 — 12 Marks]

### OPTION A:
*(a) Explain the fundamental concepts of Decision Tree induction using the ID3 algorithm. Define Entropy, Information Gain, Gain Ratio, and Gini Impurity.* **[4 Marks]**  
*(b) The following complete 14-sample training dataset `buys_computer` is given:*  

| RID | Age | Income | Student | Credit_Rating | Buys_Computer (Class) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | <=30 | High | No | Fair | **No** |
| 2 | <=30 | High | No | Excellent | **No** |
| 3 | 31..40 | High | No | Fair | **Yes** |
| 4 | >40 | Medium | No | Fair | **Yes** |
| 5 | >40 | Low | Yes | Fair | **Yes** |
| 6 | >40 | Low | Yes | Excellent | **No** |
| 7 | 31..40 | Low | Yes | Excellent | **Yes** |
| 8 | <=30 | Medium | No | Fair | **No** |
| 9 | <=30 | Low | Yes | Fair | **Yes** |
| 10 | >40 | Medium | Yes | Fair | **Yes** |
| 11 | <=30 | Medium | Yes | Excellent | **Yes** |
| 12 | 31..40 | Medium | No | Excellent | **Yes** |
| 13 | 31..40 | High | Yes | Fair | **Yes** |
| 14 | >40 | Medium | No | Excellent | **No** |

*Using the ID3 algorithm, evaluate candidate attributes `Age` and `Credit_Rating`. Compute the Target Entropy $H(S)$, the conditional entropies, and the Information Gain for each attribute. Determine which attribute must be selected as the Root Node, and draw the complete final Decision Tree.* **[8 Marks]**

### OR

### OPTION B:
*(a) Explain the k-Nearest Neighbor (k-NN) classification algorithm, distance metrics (Euclidean, Manhattan), and the curse of dimensionality.* **[6 Marks]**  
*(b) Explain Support Vector Machine (SVM) soft-margin classification, slack variables $\xi_i$, and the regularization parameter $C$.* **[6 Marks]**

---

### MODEL EXAM ANSWER FOR QUESTION 2 (OPTION A):

#### 1. Theoretical Formulations
* **Entropy $H(S)$**: Measures the impurity or randomness of set $S$:
  $$H(S) = - \sum_{i=1}^c p_i \log_2(p_i)$$
  *(Pure set: $H=0$. 50/50 split: $H=1.0$).*
* **Information Gain $\text{Gain}(S, A)$**: The reduction in entropy achieved by splitting on attribute $A$:
  $$\text{Gain}(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$$
* **Gain Ratio (C4.5)**: Normalizes Gain to avoid favoring attributes with many distinct values:
  $$\text{GainRatio}(S, A) = \frac{\text{Gain}(S, A)}{\text{SplitInfo}(S, A)}, \quad \text{SplitInfo} = - \sum \frac{|S_v|}{|S|} \log_2 \frac{|S_v|}{|S|}$$
* **Gini Impurity (CART)**:
  $$\text{Gini}(S) = 1 - \sum p_i^2$$

![Decision Tree Entropy and Information Gain](images/decision_tree_entropy_split.svg)

---

#### 2. Numerical Calculations on `buys_computer`

#### Step 1: Overall Target Entropy $H(S)$
Total instances $N = 14$: $9$ Yes, $5$ No.
$$p_+ = \frac{9}{14} \approx 0.6429, \quad p_- = \frac{5}{14} \approx 0.3571$$
$$H(S) = - \left[ \frac{9}{14}\log_2\frac{9}{14} + \frac{5}{14}\log_2\frac{5}{14} \right] = \mathbf{0.9403 \text{ bits}}$$

#### Step 2: Information Gain for Attribute `Age`
`Age` has 3 branches: `<=30` (5), `31..40` (4), `>40` (5).
1. **`Age <= 30`** (2 Yes, 3 No):
   $$H(S_{<=30}) = - \left[ \frac{2}{5}\log_2\frac{2}{5} + \frac{3}{5}\log_2\frac{3}{5} \right] = \mathbf{0.9710}$$
2. **`Age 31..40`** (4 Yes, 0 No) $\implies$ **Pure node!**
   $$H(S_{31..40}) = \mathbf{0.0000}$$
3. **`Age > 40`** (3 Yes, 2 No):
   $$H(S_{>40}) = - \left[ \frac{3}{5}\log_2\frac{3}{5} + \frac{2}{5}\log_2\frac{2}{5} \right] = \mathbf{0.9710}$$
* **Weighted Conditional Entropy $E(S, \text{Age})$**:
  $$E(S, \text{Age}) = \frac{5}{14}(0.9710) + \frac{4}{14}(0.0000) + \frac{5}{14}(0.9710) = \mathbf{0.6936 \text{ bits}}$$
* **Information Gain**:
  $$\text{Gain}(S, \text{Age}) = 0.9403 - 0.6936 = \mathbf{0.2467 \text{ bits}}$$

#### Step 3: Information Gain for Attribute `Credit_Rating`
Values: `Fair` (8: 6 Yes, 2 No), `Excellent` (6: 3 Yes, 3 No).
1. **`Fair`**:
   $$H(S_{\text{Fair}}) = - [0.75 \log_2 0.75 + 0.25 \log_2 0.25] = \mathbf{0.8113}$$
2. **`Excellent`**:
   $$H(S_{\text{Exc}}) = - [0.5 \log_2 0.5 + 0.5 \log_2 0.5] = \mathbf{1.0000}$$
* **Weighted Conditional Entropy**:
  $$E(S, \text{Credit}) = \frac{8}{14}(0.8113) + \frac{6}{14}(1.0000) = \mathbf{0.8922 \text{ bits}}$$
* **Information Gain**:
  $$\text{Gain}(S, \text{Credit}) = 0.9403 - 0.8922 = \mathbf{0.0481 \text{ bits}}$$

#### Step 4: Root Selection
$$\text{Gain}(S, \text{Age}) = 0.2467 > \text{Gain}(S, \text{Credit}) = 0.0481$$
$$\mathbf{\text{Root Node Selected: Attribute `Age`}}$$

---

#### 3. Complete Final Decision Tree Diagram

```text
                       ┌─────────────────┐
                       │    ROOT NODE    │
                       │     [ Age? ]    │
                       └────────┬────────┘
                                │
         ┌──────────────────────┼──────────────────────┐
         │ <= 30                │ 31..40               │ > 40
         ▼                      ▼                      ▼
  ┌──────────────┐         ┌───────────┐         ┌──────────────┐
  │  [Student?]  │         │   [YES]   │         │ [Credit_R.?] │
  └───┬──────┬───┘         │  (Pure!)  │         └───┬──────┬───┘
      │      │             └───────────┘             │      │
   No │      │ Yes                              Fair │      │ Excellent
      ▼      ▼                                       ▼      ▼
   ┌────┐  ┌─────┐                                ┌─────┐ ┌────┐
   │ NO │  │ YES │                                │ YES │ │ NO │
   └────┘  └─────┘                                └─────┘ └────┘
```

* **Classification Rules Extracted**:
  1. $\text{IF } \text{Age} = 31..40 \implies \text{Buys\_Computer} = \mathbf{YES}$.
  2. $\text{IF } \text{Age} \le 30 \text{ AND } \text{Student} = \text{No} \implies \text{Buys\_Computer} = \mathbf{NO}$.
  3. $\text{IF } \text{Age} \le 30 \text{ AND } \text{Student} = \text{Yes} \implies \text{Buys\_Computer} = \mathbf{YES}$.
  4. $\text{IF } \text{Age} > 40 \text{ AND } \text{Credit\_Rating} = \text{Fair} \implies \text{Buys\_Computer} = \mathbf{YES}$.
  5. $\text{IF } \text{Age} > 40 \text{ AND } \text{Credit\_Rating} = \text{Excellent} \implies \text{Buys\_Computer} = \mathbf{NO}$.

---

### MODEL EXAM ANSWER FOR QUESTION 2 (OPTION B):

#### 1. k-Nearest Neighbor (k-NN) Algorithm
* **Concept**: An instance-based, lazy-learning algorithm that makes no parametric assumptions.
* **Working Steps**:
  1. Store all training tuples $(\mathbf{x}_i, y_i)$.
  2. When query instance $\mathbf{x}_q$ arrives, compute distance to all stored instances.
  3. Identify the $k$ nearest training instances.
  4. Output the majority class label among the $k$ neighbors.
* **Distance Metrics**:
  - **Euclidean Distance ($L_2$)**: $d(\mathbf{x}, \mathbf{z}) = \sqrt{\sum_{i=1}^n (x_i - z_i)^2}$
  - **Manhattan Distance ($L_1$)**: $d(\mathbf{x}, \mathbf{z}) = \sum_{i=1}^n |x_i - z_i|$
* **Curse of Dimensionality**: As the number of features $n$ grows, volume expands exponentially. Data points become sparse and equidistant ($d_{\max} \approx d_{\min}$), causing distance metrics to lose discriminative power.

#### 2. SVM Soft-Margin & Slack Variables
* When data is not strictly linearly separable, strict hard-margin fails.
* **Slack Variables ($\xi_i \ge 0$)**: Allow individual data points to violate the margin:
  $$y_i (\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i$$
  - If $\xi_i = 0$: Point lies safely on or outside the margin.
  - If $0 < \xi_i \le 1$: Point is inside the margin, but correctly classified.
  - If $\xi_i > 1$: Point is misclassified across the hyperplane.
* **Objective Function**:
  $$\min_{\mathbf{w}, b, \mathbf{\xi}} \frac{1}{2} \|\mathbf{w}\|^2 + C \sum_{i=1}^m \xi_i$$
* **Role of Regularization Parameter $C$**:
  - **Large $C$**: Heavy penalty for mistakes $\implies$ narrow margin, risks overfitting.
  - **Small $C$**: Tolerates more margin violations $\implies$ wider margin, avoids overfitting.

---

# QUESTION 3 [Module 3 — 12 Marks]

### OPTION A:
*(a) Explain the sequential boosting paradigm of AdaBoost. State how sample weights are updated and combined.* **[4 Marks]**  
*(b) Consider a training dataset of $N=5$ instances with initial uniform weights $w_i^{(1)} = 0.20$. The performance of base classifier $h_1$ is given in the table below:*  

| Sample Index ($i$) | Feature Vector ($x_i$) | Ground Truth Label ($y_i$) | Base Classifier Prediction ($h_1(x_i)$) | Initial Weight ($w_i^{(1)}$) |
|:---:|:---:|:---:|:---:|:---:|
| 1 | $x_1$ | $+1$ | $+1$ | 0.20 |
| 2 | $x_2$ | $+1$ | $-1$ | 0.20 |
| 3 | $x_3$ | $-1$ | $-1$ | 0.20 |
| 4 | $x_4$ | $-1$ | $+1$ | 0.20 |
| 5 | $x_5$ | $+1$ | $+1$ | 0.20 |

*Compute the weighted error rate $\epsilon_1$, the classifier importance weight $\alpha_1$, the unnormalized weights, the normalization factor $Z_1$, and the updated normalized sample distribution $w_i^{(2)}$.* **[8 Marks]**

### OR

### OPTION B:
*(a) Compare Bagging and Boosting ensemble paradigms across 5 distinct dimensions. Discuss the Random Forest algorithm and its application in clinical medicine.* **[6 Marks]**  
*(b) Given the following 7-bit Error-Correcting Output Code (ECOC) matrix for 4 target classes:*  

| Class | $C_1$ | $C_2$ | $C_3$ | $C_4$ | $C_5$ | $C_6$ | $C_7$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $y_1$ | 1 | 1 | 0 | 0 | 1 | 0 | 1 |
| $y_2$ | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
| $y_3$ | 1 | 0 | 1 | 1 | 0 | 0 | 1 |
| $y_4$ | 0 | 0 | 0 | 1 | 1 | 1 | 0 |

*If an unknown instance produces prediction vector $\mathbf{v} = [1, 1, 1, 0, 1, 0, 1]$, compute the Hamming distance to all 4 classes and determine its predicted class.* **[6 Marks]**

---

### MODEL EXAM ANSWER FOR QUESTION 3 (OPTION A):

#### 1. AdaBoost Working Principle
* Unlike bagging (which trains trees independently in parallel), AdaBoost trains weak learners **sequentially**.
* Each iteration raises the weights of misclassified instances, forcing the next learner to focus on the hardest examples.
* **Final Ensemble Formula**:
  $$H(\mathbf{x}) = \text{sign}\left( \sum_{t=1}^T \alpha_t h_t(\mathbf{x}) \right)$$

![AdaBoost Sequential Ensemble Architecture](images/adaboost_sequential_architecture.svg)

---

> 💡 **EXAM NOTE: AdaBoost 3-Step Memory Hook**  
> 1. $\epsilon = \text{sum of weights of WRONG instances}$.  
> 2. $\alpha = \frac{1}{2} \ln \left( \frac{1-\epsilon}{\epsilon} \right)$ *(Importance of classifier: log of good over bad, halved)*.  
> 3. Multiplier: Correct $\times e^{-\alpha}$ (shrink); Incorrect $\times e^{+\alpha}$ (boost).  
> 4. Normalize by dividing by sum $Z$. Check: sum of new weights must equal $1.0000$.

#### 2. Step-by-Step Numerical Trace ($N=5$)

#### Step 1: Weighted Error Rate $\epsilon_1$
Samples 2 and 4 are misclassified:
$$\epsilon_1 = w_2^{(1)} + w_4^{(1)} = 0.20 + 0.20 = \mathbf{0.40}$$

#### Step 2: Classifier Weight $\alpha_1$
$$\alpha_1 = \frac{1}{2} \ln \left( \frac{1 - 0.40}{0.40} \right) = \frac{1}{2} \ln(1.5) = \frac{0.4055}{2} = \mathbf{0.2027}$$

#### Step 3: Multiplier Factors
* For correct samples: $e^{-\alpha_1} = e^{-0.2027} = \mathbf{0.8165}$
* For incorrect samples: $e^{+\alpha_1} = e^{+0.2027} = \mathbf{1.2247}$

#### Step 4: Unnormalized Weights $\tilde{w}_i$
* Correct ($i=1, 3, 5$): $\tilde{w}_i = 0.20 \times 0.8165 = \mathbf{0.1633}$
* Incorrect ($i=2, 4$): $\tilde{w}_i = 0.20 \times 1.2247 = \mathbf{0.2449}$

#### Step 5: Normalization Factor $Z_1$
$$Z_1 = 3(0.1633) + 2(0.2449) = 0.4899 + 0.4898 = \mathbf{0.9797}$$

#### Step 6: Normalized Weights $w_i^{(2)} = \frac{\tilde{w}_i}{Z_1}$
* Correct: $w_1 = w_3 = w_5 = \frac{0.1633}{0.9797} = \mathbf{0.1667}$
* Incorrect: $w_2 = w_4 = \frac{0.2449}{0.9797} = \mathbf{0.2500}$

#### Summary Table:
| Sample $i$ | True $y_i$ | Pred $h_1(x_i)$ | Status | Initial $w_i^{(1)}$ | Multiplier | Unnorm $\tilde{w}_i$ | Normalized $w_i^{(2)}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $+1$ | $+1$ | Correct | 0.20 | 0.8165 | 0.1633 | **0.1667** |
| 2 | $+1$ | $-1$ | **Error** | 0.20 | 1.2247 | 0.2449 | **0.2500** |
| 3 | $-1$ | $-1$ | Correct | 0.20 | 0.8165 | 0.1633 | **0.1667** |
| 4 | $-1$ | $+1$ | **Error** | 0.20 | 1.2247 | 0.2449 | **0.2500** |
| 5 | $+1$ | $+1$ | Correct | 0.20 | 0.8165 | 0.1633 | **0.1667** |
| **Sum** | — | — | — | **1.00** | — | **$Z_1=0.9797$** | **1.0000** |

$$\mathbf{\text{Final Boxed Result: } w_{\text{correct}}^{(2)} = 0.1667, \quad w_{\text{error}}^{(2)} = 0.2500}$$

---

### MODEL EXAM ANSWER FOR QUESTION 3 (OPTION B):

#### 1. Bagging vs Boosting Comparison

| Parameter | Bagging (Bootstrap Aggregation) | Boosting (e.g. AdaBoost) |
|:---|:---|:---|
| **Training Paradigm** | **Parallel**: Base learners trained independently. | **Sequential**: Base learners trained in series. |
| **Instance Weights** | Equal uniform weights for all instances. | Adaptive: Weights increase for misclassified points. |
| **Primary Goal** | **Reduces Variance** (prevents overfitting). | **Reduces Bias** (converts weak learners to strong). |
| **Voting Method** | Simple majority voting or average. | Weighted voting based on model accuracy $\alpha_t$. |
| **Susceptibility to Noise**| Robust against noise and outliers. | Vulnerable (can overfit to noisy outliers). |

* **Random Forest in Clinical Medicine**:
  - Combines bootstrap aggregation with random feature selection at each node split.
  - In healthcare (e.g. sepsis prediction, cardiovascular risk): Handles high-dimensional patient data, provides **Feature Importance** rankings (e.g. identifying troponin levels as key predictor), and does not overfit even with small patient sample sizes.

#### 2. ECOC (Error-Correcting Output Codes) Hamming Distance Trace
* Query prediction vector: $\mathbf{v} = [1, 1, 1, 0, 1, 0, 1]$.
* **Hamming Distance $d_H$**: Count the number of bit positions that differ.
1. **To Class $y_1 = [1, 1, 0, 0, 1, 0, 1]$**:
   Differs only at bit 3 ($1$ vs $0$) $\implies \mathbf{d_H = 1}$.
2. **To Class $y_2 = [0, 1, 1, 0, 0, 1, 1]$**:
   Differs at bits 1, 5, 6 $\implies \mathbf{d_H = 3}$.
3. **To Class $y_3 = [1, 0, 1, 1, 0, 0, 1]$**:
   Differs at bits 2, 4, 5 $\implies \mathbf{d_H = 3}$.
4. **To Class $y_4 = [0, 0, 0, 1, 1, 1, 0]$**:
   Differs at bits 1, 2, 3, 4, 6, 7 $\implies \mathbf{d_H = 6}$.

$$\mathbf{\text{Final Classification: Minimum Hamming distance is } d_H = 1 \implies \text{Class } y_1}$$

---

# QUESTION 4 [Module 4 — 12 Marks]

### OPTION A:
*(a) State Bayes' Theorem and explain the conditional independence assumption of the Naïve Bayes classifier. Formulate the Laplace smoothing equation.* **[4 Marks]**  
*(b) The following complete 12-applicant Loan Approval training dataset is given:*  

| Applicant_ID | Income | Credit_History | Employment | Existing_Loan | Loan_Decision (Class) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| A1 | High | Good | Stable | No | **Approved** |
| A2 | High | Good | Unstable | No | **Approved** |
| A3 | Medium | Good | Stable | No | **Approved** |
| A4 | High | Poor | Stable | Yes | **Rejected** |
| A5 | Low | Good | Stable | Yes | **Rejected** |
| A6 | Medium | Poor | Unstable | Yes | **Rejected** |
| A7 | Low | Poor | Unstable | Yes | **Rejected** |
| A8 | Medium | Good | Stable | No | **Approved** |
| A9 | High | Good | Stable | Yes | **Approved** |
| A10 | Low | Good | Unstable | No | **Rejected** |
| A11 | Medium | Poor | Stable | Yes | **Rejected** |
| A12 | High | Poor | Unstable | No | **Rejected** |

*Predict the loan decision for a new applicant with query feature vector:*  
$$X = (\text{Income}=\text{Medium}, \; \text{Credit\_History}=\text{Good}, \; \text{Employment}=\text{Stable}, \; \text{Existing\_Loan}=\text{No})$$  
*(c) Critique whether the conditional independence assumption holds in real-world credit evaluation.* **[8 Marks]**

### OR

### OPTION B:
*(a) State the Apriori algorithm for Frequent Itemset Mining. Describe candidate generation $L_{k-1} \bowtie L_{k-1}$ and subset pruning.* **[6 Marks]**  
*(b) Given the following complete 10-transaction market basket dataset with $\text{min\_sup} = 2$ ($20\%$):*  

| TID | Items Purchased |
|:---:|:---|
| T1 | {A, B, E} |
| T2 | {B, D} |
| T3 | {B, C} |
| T4 | {A, B, D} |
| T5 | {A, C} |
| T6 | {B, C} |
| T7 | {A, C} |
| T8 | {A, B, C, E} |
| T9 | {A, B, C} |
| T10 | {A, C, E} |

*Execute candidate generation $C_1 \to L_1 \to C_2 \to L_2 \to C_3 \to L_3$ and compute the confidence of rule $\{B, C\} \to \{E\}$.* **[6 Marks]**

---

### MODEL EXAM ANSWER FOR QUESTION 4 (OPTION A):

#### 1. Naïve Bayes Formulation
* **Bayes' Theorem**:
  $$P(Y \mid X) = \frac{P(X \mid Y) P(Y)}{P(X)}$$
* **Conditional Independence Assumption**:
  $$P(X_1, X_2, \dots, X_n \mid Y) = \prod_{i=1}^n P(X_i \mid Y)$$
* **Laplace Smoothing** (prevents zero probability):
  $$P(X_i = v \mid Y = c) = \frac{\text{Count}(X_i = v, Y = c) + 1}{\text{Count}(Y = c) + |V_i|}$$

![Probabilistic Learning: Naive Bayes vs BBN](images/bayes_naive_and_bbn.svg)

---

#### 2. Loan Approval Step-by-Step Calculation

#### Step 1: Class Priors ($N = 12$)
* Approved: A1, A2, A3, A8, A9 $\implies 5$
* Rejected: A4, A5, A6, A7, A10, A11, A12 $\implies 7$
$$P(\text{Approved}) = \frac{5}{12} \approx 0.4167, \qquad P(\text{Rejected}) = \frac{7}{12} \approx 0.5833$$

#### Step 2: Likelihoods for Class = Approved ($N_{\text{App}} = 5$)
* $P(\text{Income=Medium} \mid \text{App}) = \frac{2}{5} = \mathbf{0.40}$ *(A3, A8)*
* $P(\text{Credit=Good} \mid \text{App}) = \frac{5}{5} = \mathbf{1.00}$ *(All 5)*
* $P(\text{Employment=Stable} \mid \text{App}) = \frac{4}{5} = \mathbf{0.80}$ *(A1, A3, A8, A9)*
* $P(\text{Existing=No} \mid \text{App}) = \frac{4}{5} = \mathbf{0.80}$ *(A1, A2, A3, A8)*
$$\text{Likelihood Product } P(X \mid \text{App}) = 0.40 \times 1.00 \times 0.80 \times 0.80 = \mathbf{0.2560}$$
$$\text{Score}(\text{App}) = \frac{5}{12} \times 0.2560 = \mathbf{0.1067}$$

#### Step 3: Likelihoods for Class = Rejected ($N_{\text{Rej}} = 7$)
* $P(\text{Income=Medium} \mid \text{Rej}) = \frac{2}{7} \approx \mathbf{0.2857}$ *(A6, A11)*
* $P(\text{Credit=Good} \mid \text{Rej}) = \frac{2}{7} \approx \mathbf{0.2857}$ *(A5, A10)*
* $P(\text{Employment=Stable} \mid \text{Rej}) = \frac{3}{7} \approx \mathbf{0.4286}$ *(A4, A5, A11)*
* $P(\text{Existing=No} \mid \text{Rej}) = \frac{3}{7} \approx \mathbf{0.4286}$ *(A7, A10, A12)*
$$\text{Likelihood Product } P(X \mid \text{Rej}) = \frac{2}{7} \times \frac{2}{7} \times \frac{3}{7} \times \frac{3}{7} = \frac{36}{2401} \approx \mathbf{0.0150}$$
$$\text{Score}(\text{Rej}) = \frac{7}{12} \times \frac{36}{2401} = \frac{3}{343} \approx \mathbf{0.00875}$$

#### Step 4: Normalization & Decision
$$\text{Total Evidence} = 0.1067 + 0.00875 = 0.11545$$
$$P(\text{Approved} \mid X) = \frac{0.1067}{0.11545} = \mathbf{92.42\%}, \qquad P(\text{Rejected} \mid X) = \mathbf{7.58\%}$$

$$\mathbf{\text{Final Decision: Loan application is APPROVED (92.42\% probability)}}$$

#### 3. Real-World Independence Critique
* **Are features truly independent?** **NO.**
* In banking:
  1. `Employment Stability` directly influences `Income` (stable jobs produce higher/consistent income).
  2. `Existing Loans` directly impact `Credit History` (defaulting on loans destroys credit score).
* **Why Naïve Bayes still works**: It only needs the correct **relative ranking** ($0.1067 \gg 0.00875$), not exact probabilities.

---

### MODEL EXAM ANSWER FOR QUESTION 4 (OPTION B):

#### 1. Apriori Execution on 10 Transactions ($\text{min\_sup} = 2$)
* **Candidate 1-itemsets ($C_1 \to L_1$)**:
  - $A: 8, \; B: 7, \; C: 6, \; D: 2, \; E: 4$ (All $\ge 2 \implies$ All kept in $L_1$).
* **Candidate 2-itemsets ($C_2 \to L_2$)**:
  - $\{A, B\}: 4, \; \{A, C\}: 5, \; \{A, D\}: 1 \text{ (Pruned)}, \; \{A, E\}: 3$
  - $\{B, C\}: 4, \; \{B, D\}: 2, \; \{B, E\}: 2$
  - $\{C, E\}: 2$
* **Candidate 3-itemsets ($C_3 \to L_3$)**:
  - Generated: $\{A, B, C\}, \{A, B, E\}, \{A, C, E\}$.
  - Support of $\{A, B, C\} = 2 \implies L_3$.
  - Support of $\{A, B, E\} = 2 \implies L_3$.
  - Support of $\{A, C, E\} = 2 \implies L_3$.
* **Confidence of Rule $\{B, C\} \to \{E\}$**:
  $$\text{Confidence} = \frac{\text{Support}(\{B, C, E\})}{\text{Support}(\{B, C\})} = \frac{1}{4} = \mathbf{25.0\%}$$

---

# QUESTION 5 [Module 5 — 12 Marks]

### OPTION A:
*(a) Explain the concept of imbalanced datasets. Discuss why accuracy is deceptive when dealing with imbalanced data, illustrating with a numerical proof on a 1,000-patient clinical cohort.* **[6 Marks]**  
*(b) Detail the working mechanism of SMOTE. Given seed minority instance $\mathbf{x}_i = [2.0, 4.0]$, neighbor $\mathbf{x}_{zi} = [6.0, 10.0]$, and random interpolation parameter $\lambda = 0.5$, compute the synthetic sample coordinates. Compare Random Oversampling (ROS) vs SMOTE.* **[6 Marks]**

### OR

### OPTION B:
*(a) A clinical diagnostic model for detecting a rare cardiac disease is tested on a cohort of 500 patients. The complete evaluation results are given in the confusion matrix below:*  

| | Actual Positive (Disease) | Actual Negative (Healthy) |
|:---|:---:|:---:|
| **Predicted Positive** | 45 ($TP$) | 15 ($FP$) |
| **Predicted Negative** | 5 ($FN$) | 435 ($TN$) |

*Calculate the model's Accuracy, Precision, Recall (Sensitivity), Specificity, and F1-Score.* **[6 Marks]**  
*(b) Detail Enterprise RAG (Retrieval-Augmented Generation) architecture, vector databases, and semantic search as modern machine learning technology trends impacting industry.* **[6 Marks]**

---

### MODEL EXAM ANSWER FOR QUESTION 5 (OPTION A):

#### 1. Concept of Imbalanced Datasets & Accuracy Paradox
* **Definition**: A dataset is imbalanced when one class significantly outnumbers another (e.g. $99:1$). Common in fraud detection, disease diagnosis, and cyber intrusions.
* **The Accuracy Paradox (1,000-Patient Proof)**:
  - Cohort: $990$ Healthy, $10$ Cancer patients.
  - A dumb classifier predicting **"Healthy" for everyone** gets:
    - $TP = 0, \quad FP = 0, \quad TN = 990, \quad FN = 10$.
  - Performance:
    $$\text{Accuracy} = \frac{TP + TN}{N} = \frac{0 + 990}{1000} = \mathbf{99.0\%}$$
    $$\text{Recall} = \frac{TP}{TP + FN} = \frac{0}{0 + 10} = \mathbf{0.0\%}$$
  - **Conclusion**: Despite $99\%$ accuracy, the model fails to detect all 10 cancer patients! Accuracy is therefore a misleading metric for imbalanced data. Evaluators must use Precision, Recall, and F1-Score.

![Classification Metrics and Confusion Matrix](images/confusion_matrix_and_metrics.svg)

---

#### 2. SMOTE Working Mechanism & Coordinate Interpolation
* **How SMOTE Works**:
  1. For each minority point $\mathbf{x}_i$, find its $k$-nearest minority neighbors (default $k=5$).
  2. Pick a random neighbor $\mathbf{x}_{zi}$.
  3. Draw a line segment between them and pick a random point on that line:
     $$\mathbf{x}_{\text{new}} = \mathbf{x}_i + \lambda \cdot (\mathbf{x}_{zi} - \mathbf{x}_i), \quad \lambda \in [0, 1]$$

![SMOTE Synthetic Sample Interpolation](images/smote_synthetic_interpolation.svg)

* **Coordinate Numerical**:
  - $\mathbf{x}_i = [2.0, 4.0], \quad \mathbf{x}_{zi} = [6.0, 10.0], \quad \lambda = 0.5$
  - Difference: $[6.0 - 2.0, \; 10.0 - 4.0] = [4.0, 6.0]$
  - Scale: $0.5 \times [4.0, 6.0] = [2.0, 3.0]$
  - New Point:
    $$\mathbf{x}_{\text{new}} = [2.0, 4.0] + [2.0, 3.0] = \mathbf{[4.0, \; 7.0]}$$

#### 3. Random Oversampling (ROS) vs SMOTE

| Dimension | Random Oversampling (ROS) | SMOTE |
|:---|:---|:---|
| **Method** | Clones/duplicates existing minority points. | Generates brand-new synthetic points along lines. |
| **Overfitting** | **High**: Memorizes exact duplicate points. | **Low**: Broadens minority decision region. |
| **Speed** | Instantaneous ($O(N)$). | Slower ($O(N^2)$ due to $k$-NN distance matrix). |

$$\mathbf{\text{Final Coordinate Result: } [4.0, \; 7.0]}$$

---

### MODEL EXAM ANSWER FOR QUESTION 5 (OPTION B):

#### 1. 500-Patient Confusion Matrix Evaluation
Given: $TP = 45, \quad FP = 15, \quad FN = 5, \quad TN = 435 \quad (N = 500)$.
1. **Accuracy**:
   $$\text{Accuracy} = \frac{TP + TN}{N} = \frac{45 + 435}{500} = \frac{480}{500} = \mathbf{96.00\%}$$
2. **Precision**:
   $$\text{Precision} = \frac{TP}{TP + FP} = \frac{45}{45 + 15} = \frac{45}{60} = \mathbf{75.00\%}$$
3. **Recall (Sensitivity)**:
   $$\text{Recall} = \frac{TP}{TP + FN} = \frac{45}{45 + 5} = \frac{45}{50} = \mathbf{90.00\%}$$
4. **Specificity**:
   $$\text{Specificity} = \frac{TN}{TN + FP} = \frac{435}{435 + 15} = \frac{435}{450} = \mathbf{96.67\%}$$
5. **F1-Score**:
   $$\text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = 2 \times \frac{0.75 \times 0.90}{0.75 + 0.90} = \frac{1.35}{1.65} = \mathbf{81.82\%}$$

#### 2. Enterprise RAG Architecture
* Combines static LLMs with live external databases.
* **Flow**: User Query $\to$ Embedding Model $\to$ Vector DB similarity search $\to$ Retrieve top-k factual chunks $\to$ Augmented Prompt $\to$ Accurate response without hallucinations.

---
---

# ══════════════════════════════════════════════════
# SECTION B: 5 QUESTIONS $\times$ 8 MARKS = 40 MARKS
### *(Compulsory Direct Questions Without Subparts — 1 from Each Module)*
# ══════════════════════════════════════════════════

---

# QUESTION 6 [Module 1 — 8 Marks]

### Question:
*Define Vapnik-Chervonenkis (VC) Dimension. Prove that the VC dimension of 1D closed intervals $H = \{[a, b] \mid a, b \in \mathbb{R}\}$ is 2. Define the Natarajan Dimension and explain its significance in multiclass PAC learnability.* **[8 Marks]**

---

### MODEL EXAM ANSWER:

#### 1. What is VC Dimension? (Simple Terms & Keywords)
* **Shattering**: A hypothesis set $H$ "shatters" a set of data points if it can assign **every possible combination of positive and negative labels** ($2^N$ combinations) to those points.
* **VC Dimension ($VC(H)$)**: The **maximum number of points** that $H$ can shatter.
* If a model can shatter $N$ points, its $VC \ge N$. If it cannot shatter ANY set of $N+1$ points, then $VC = N$.

---

#### 2. Proof that $VC(\text{1D Closed Intervals}) = 2$

A 1D closed interval hypothesis labels points inside $[a, b]$ as $+1$, and points outside as $-1$.

#### Step 1: Can 1D intervals shatter 2 points? (YES)
Let points be $x_1 = 1, x_2 = 3$. There are $2^2 = 4$ possible labelings:
* $(-1, -1) \implies \text{Interval } [5, 6]$ (both outside)
* $(+1, -1) \implies \text{Interval } [0, 2]$ (only $x_1$ inside)
* $(-1, +1) \implies \text{Interval } [2, 4]$ (only $x_2$ inside)
* $(+1, +1) \implies \text{Interval } [0, 4]$ (both inside)  
All 4 labelings are successfully formed $\implies VC \ge 2$.

#### Step 2: Can 1D intervals shatter 3 points? (NO)
* Take any 3 collinear points ordered on the real line: $x_1 < x_2 < x_3$.
* There are $2^3 = 8$ labelings. Test the labeling **$(+1, -1, +1)$**:
  - To label $x_1$ as $+1$, the interval must start at or before $x_1$ ($a \le x_1$).
  - To label $x_3$ as $+1$, the interval must end at or after $x_3$ ($x_3 \le b$).
  - Therefore, $a \le x_1 < x_2 < x_3 \le b$.
  - This forces $x_2$ to be INSIDE $[a, b]$, meaning $x_2$ MUST be labeled $+1$.
  - It is mathematically impossible to label $x_2$ as $-1$ while labeling $x_1$ and $x_3$ as $+1$!
* Contradiction: No 3 points can be shattered.

$$\mathbf{\text{Conclusion: } VC(\text{1D Closed Intervals}) = 2}$$

---

#### 3. Natarajan Dimension (Multiclass PAC Learnability)
* **Limitation of VC Dimension**: VC dimension is defined strictly for **binary classification** ($2$ classes).
* **Natarajan Dimension**: Generalizes VC dimension to **multiclass classification** ($K \ge 3$ classes).
* **Significance**: A multiclass hypothesis class $H$ is PAC-learnable if and only if its Natarajan dimension is finite:
  $$\mathbf{N_{\dim}(H) < \infty}$$

---

# QUESTION 7 [Module 2 — 8 Marks]

### Question:
*Explain the geometric formulation of Support Vector Machines (SVM). Derive the margin width $M = \frac{2}{\|\mathbf{w}\|}$ from canonical hyperplanes. Explain the role of Support Vectors, Slack Variables, and the Kernel Trick.* **[8 Marks]**

---

### MODEL EXAM ANSWER:

#### 1. Geometric Margin Derivation ($M = \frac{2}{\|\mathbf{w}\|}$)

Let linearly separable data be labeled $y_i \in \{-1, +1\}$.
* **Separating Hyperplane**:
  $$\mathbf{w}^T \mathbf{x} + b = 0$$
* **Canonical Margin Boundaries** (where the closest positive and negative points lie):
  $$\text{Positive Boundary: } \mathbf{w}^T \mathbf{x}_+ + b = +1$$
  $$\text{Negative Boundary: } \mathbf{w}^T \mathbf{x}_- + b = -1$$
* **Subtract the two equations**:
  $$\mathbf{w}^T (\mathbf{x}_+ - \mathbf{x}_-) = 2$$
* **Project along the unit normal vector $\frac{\mathbf{w}}{\|\mathbf{w}\|}$**:
  $$M = (\mathbf{x}_+ - \mathbf{x}_-) \cdot \frac{\mathbf{w}}{\|\mathbf{w}\|} = \frac{\mathbf{w}^T (\mathbf{x}_+ - \mathbf{x}_-)}{\|\mathbf{w}\|} = \mathbf{\frac{2}{\|\mathbf{w}\|}}$$

$$\mathbf{\text{Final Boxed Margin: } M = \frac{2}{\|\mathbf{w}\|}}$$

* **Optimization Goal**: To maximize the margin $M = \frac{2}{\|\mathbf{w}\|}$, we minimize $\frac{1}{2}\|\mathbf{w}\|^2$ subject to $y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1$.

![Support Vector Machine Hyperplane and Maximum Margin](images/svm_hyperplane_margin.svg)

---

#### 2. Key SVM Concepts (Exam Standard)
* **Support Vectors**: The training points that lie directly ON the margin boundaries ($\mathbf{w}^T \mathbf{x}_i + b = \pm 1$). If you delete any non-support vector, the decision boundary does not change at all! The optimal hyperplane depends solely on the support vectors.
* **Slack Variables ($\xi_i$)**: Introduced for non-separable data (Soft Margin). Points with $\xi_i > 0$ are allowed to cross into the margin or get misclassified, controlled by penalty parameter $C$.
* **The Kernel Trick**: When data cannot be separated by a flat line/plane, map points to a higher dimension $\phi(\mathbf{x})$. A kernel function $K(\mathbf{x}_i, \mathbf{x}_j) = \phi(\mathbf{x}_i)^T \phi(\mathbf{x}_j)$ computes dot products directly in higher dimensions without explicitly calculating the high-dimensional coordinates (e.g. Linear, Polynomial, Gaussian RBF).

---

# QUESTION 8 [Module 3 — 8 Marks]

### Question:
*The following complete 1D dataset of 6 numbers is given:*  
$$D = \{5, \; 9, \; 14, \; 25, \; 28, \; 40\}$$  
*Perform agglomerative hierarchical clustering (AGNES) using Single Linkage and Complete Linkage. Show the complete merge sequences, draw both dendrograms with heights, and explain why Single Linkage causes the chaining effect.* **[8 Marks]**

---

### MODEL EXAM ANSWER:

#### 1. Initial Distance Setup
Dataset: $x_1 = 5, \; x_2 = 9, \; x_3 = 14, \; x_4 = 25, \; x_5 = 28, \; x_6 = 40$.  
Adjacent pairwise distances:
$$d(5, 9) = 4, \quad d(9, 14) = 5, \quad d(14, 25) = 11, \quad d(25, 28) = \mathbf{3}, \quad d(28, 40) = 12$$

---

#### 2. Single Linkage Execution ($d_{\min}$)
*Rule: Distance between two clusters is the MINIMUM distance between any pair of points.*

* **Merge 1**: Global minimum distance is $d(25, 28) = \mathbf{3} \implies$ **Merge $\{25, 28\}$ at height $h = 3$**.
* **Merge 2**: Next minimum is $d(5, 9) = \mathbf{4} \implies$ **Merge $\{5, 9\}$ at height $h = 4$**.
* **Merge 3**: Distance $d(\{5, 9\}, 14) = \min(|5-14|, |9-14|) = \min(9, 5) = \mathbf{5} \implies$ **Merge $\{5, 9, 14\}$ at height $h = 5$**.
* **Merge 4**: Distance $d(\{5, 9, 14\}, \{25, 28\}) = \min|14-25| = \mathbf{11} \implies$ **Merge $\{5, 9, 14, 25, 28\}$ at height $h = 11$**.
* **Merge 5**: Distance to $\{40\} = \min|28-40| = \mathbf{12} \implies$ **Merge all at height $h = 12$**.

#### Single Linkage Dendrogram:
```text
Height
  12 |                         ┌─────── 40
  11 |             ┌───────────┴─────── (25, 28)
   5 |     ┌───────┴─────── 14
   4 |  ┌──┴── 9
   3 |  │               ┌─── 28
   0 └──┴───────────────┴───────────────
        5      9   14   25   28    40
```

---

#### 3. Complete Linkage Execution ($d_{\max}$)
*Rule: Distance between two clusters is the MAXIMUM distance between any pair of points.*

* **Merge 1**: Merge $\{25, 28\}$ at height $h = 3$.
* **Merge 2**: Merge $\{5, 9\}$ at height $h = 4$.
* **Merge 3**: Distance $d(\{5, 9\}, 14) = \max(|5-14|, |9-14|) = \max(9, 5) = \mathbf{9} \implies$ **Merge $\{5, 9, 14\}$ at height $h = 9$**.
* **Merge 4**: Compare candidates:
  - $d(\{5, 9, 14\}, \{25, 28\}) = \max|5-28| = 23$.
  - $d(\{25, 28\}, 40) = \max(|25-40|, |28-40|) = \mathbf{15}$.
  - Minimum candidate is $15 \implies$ **Merge $\{25, 28\}$ with $\{40\}$ into $\{25, 28, 40\}$ at height $h = 15$**!
* **Merge 5**: Final merge of $\{5, 9, 14\}$ and $\{25, 28, 40\}$ at height $\max|5-40| = \mathbf{35}$.

#### Complete Linkage Dendrogram:
```text
Height
  35 |             ┌──────────────────────┐
     |             │                      │
  15 |             │              ┌───────┴─────── 40
     |             │              │       ┌─────── 28
   9 |     ┌───────┴─────── 14    └───┬───┘
   4 |  ┌──┴── 9                      │
   3 |  │                             └─── 25
   0 └──┴─────────────────────────────────────────
        5      9   14             25      28      40
```

---

#### 4. The Chaining Effect
* **Single Linkage**: Forms long, straggly chains because individual points act as bridges between separate clusters (e.g. 14 bridges to 25).
* **Complete Linkage**: Avoids chaining by grouping $\{25, 28\}$ with 40 first, creating compact, balanced clusters.

---

# QUESTION 9 [Module 4 — 8 Marks]

### Question:
*(a) Explain the Apriori Principle and the Downward Closure Property in Association Rule Mining. How does candidate pruning reduce computational search space?* **[4 Marks]**  
*(b) Define Bayesian Belief Networks (BBN). Explain how Directed Acyclic Graphs (DAGs) and Conditional Probability Tables (CPTs) represent joint probability distributions.* **[4 Marks]**

---

### MODEL EXAM ANSWER:

#### 1. The Apriori Principle & Downward Closure Property
* **Association Mining Goal**: Find itemsets that frequently appear together in transaction databases (Support $\ge \text{min\_sup}$).
* **The Apriori Principle**:
  $$\text{All non-empty subsets of a frequent itemset must also be frequent.}$$
* **Downward Closure (Anti-Monotonicity)**:
  - If itemset $X$ is frequent, any subset $Y \subset X$ is guaranteed to be frequent.
  - **Pruning Rule**: If an itemset $A$ is **infrequent** ($\text{Support}(A) < \text{min\_sup}$), then **any superset containing $A$ is immediately pruned without scanning the database**!
  - *Example*: If $\{D\}$ is infrequent, then $\{A, D\}, \{B, D\}, \{A, B, D\}$ are never generated or checked. This drastically cuts down search complexity from $O(2^d)$ to a manageable subset.

---

#### 2. Bayesian Belief Networks (BBN)
* **Motivation**: Standard Naïve Bayes assumes ALL features are strictly independent. In reality, features often have selective dependencies. BBN models these relationships realistically.
* **Two Core Components**:
  1. **Directed Acyclic Graph (DAG)**:
     - **Nodes**: Represent random variables (discrete or continuous).
     - **Directed Edges**: Represent direct causal influence or dependency (arrow from Parent $\to$ Child).
     - **Absence of Edge**: Represents conditional independence.
  2. **Conditional Probability Tables (CPTs)**:
     - Each node $X_i$ has a CPT specifying $P(X_i \mid \text{Parents}(X_i))$.
* **Joint Probability Chain Rule**:
  $$P(X_1, X_2, \dots, X_n) = \prod_{i=1}^n P(X_i \mid \text{Parents}(X_i))$$
  *(Allows computing any joint probability using only local parent-child conditional tables).*

---

# QUESTION 10 [Module 5 — 8 Marks]

### Question:
*Derive the first principal component projection vector in Principal Component Analysis (PCA) by maximizing the projected variance using the method of Lagrange Multipliers. Prove that the optimal projection vector is the eigenvector corresponding to the maximum eigenvalue of the sample covariance matrix.* **[8 Marks]**

---

### MODEL EXAM ANSWER:

#### 1. PCA Goal in Plain English
* We have high-dimensional centered data (mean $\mathbf{\bar{x}} = \mathbf{0}$).
* We want to find a 1D direction vector $\mathbf{u}_1$ such that when we project our data onto $\mathbf{u}_1$, the **spread (variance) of the points is maximized**.
* Constraint: $\mathbf{u}_1$ must be a unit vector ($\mathbf{u}_1^T \mathbf{u}_1 = 1$) so it only represents a direction.

---

#### 2. Derivation via Lagrange Multipliers (Step-by-Step)

#### Step 1: Centered Data & Covariance Matrix
Let $\mathbf{X}_c \in \mathbb{R}^{m \times n}$ be the centered data matrix. The sample covariance matrix is:
$$\mathbf{\Sigma} = \frac{1}{m} \mathbf{X}_c^T \mathbf{X}_c$$

#### Step 2: Formulate the Projected Variance
The projection of a data point $\mathbf{x}_i$ onto unit vector $\mathbf{u}_1$ is $z_i = \mathbf{x}_i^T \mathbf{u}_1$.  
The projected sample variance $\sigma_z^2$ is:
$$\sigma_z^2 = \frac{1}{m} \sum_{i=1}^m z_i^2 = \frac{1}{m} \sum_{i=1}^m (\mathbf{u}_1^T \mathbf{x}_i)(\mathbf{x}_i^T \mathbf{u}_1) = \mathbf{u}_1^T \left( \frac{1}{m} \mathbf{X}_c^T \mathbf{X}_c \right) \mathbf{u}_1$$
$$\sigma_z^2 = \mathbf{u}_1^T \mathbf{\Sigma} \mathbf{u}_1$$

#### Step 3: Constrained Optimization Setup
We want to maximize projected variance subject to the unit length constraint:
$$\max_{\mathbf{u}_1} \mathbf{u}_1^T \mathbf{\Sigma} \mathbf{u}_1 \quad \text{subject to } \mathbf{u}_1^T \mathbf{u}_1 = 1$$

#### Step 4: The Lagrangian Function
Introduce Lagrange multiplier $\lambda$:
$$\mathcal{L}(\mathbf{u}_1, \lambda) = \mathbf{u}_1^T \mathbf{\Sigma} \mathbf{u}_1 - \lambda (\mathbf{u}_1^T \mathbf{u}_1 - 1)$$

#### Step 5: Differentiate and Equate to Zero
Take the vector derivative of $\mathcal{L}$ with respect to $\mathbf{u}_1$:
$$\frac{\partial \mathcal{L}}{\partial \mathbf{u}_1} = 2 \mathbf{\Sigma} \mathbf{u}_1 - 2 \lambda \mathbf{u}_1 = \mathbf{0}$$
Divide by 2:
$$\mathbf{\Sigma} \mathbf{u}_1 - \lambda \mathbf{u}_1 = \mathbf{0} \implies \mathbf{\mathbf{\Sigma} \mathbf{u}_1 = \lambda \mathbf{u}_1}$$

#### Step 6: Conclusion (Eigenvector with Maximum Eigenvalue)
1. The equation $\mathbf{\Sigma} \mathbf{u}_1 = \lambda \mathbf{u}_1$ is the fundamental definition of an **Eigenvector** and **Eigenvalue**! Therefore, $\mathbf{u}_1$ must be an eigenvector of covariance matrix $\mathbf{\Sigma}$.
2. Pre-multiply both sides by $\mathbf{u}_1^T$:
   $$\mathbf{u}_1^T \mathbf{\Sigma} \mathbf{u}_1 = \lambda (\mathbf{u}_1^T \mathbf{u}_1)$$
   Since $\mathbf{u}_1^T \mathbf{u}_1 = 1$:
   $$\sigma_z^2 = \mathbf{\lambda}$$
3. The projected variance is directly equal to the eigenvalue $\lambda$.
4. Therefore, to achieve the **maximum possible variance**, $\mathbf{u}_1$ must be the eigenvector corresponding to the **largest eigenvalue $\lambda_{\max}$**.

$$\mathbf{\text{Q.E.D. The optimal projection vector is the eigenvector for } \lambda_{\max}.}$$

![PCA Variance Maximization and Orthogonal Axes](images/pca_variance_maximization.svg)
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print(f"Successfully generated simple, complete, and exam-ready {output_path}!")
