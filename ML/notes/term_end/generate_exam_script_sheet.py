# -*- coding: utf-8 -*-
"""
Script to generate the exam-script formatted Master Study Sheet:
- No meta-conversational text
- Written exactly like a top-rank student's model answer sheet
- Even gaps, structured headers, clear diagrams
- "💡 EXAM NOTE: Numerical Solving Strategy" only before numericals
"""

import os

content = r"""# 🏆 CSE4005: Machine Learning — FAT TEE Model Exam Answer Script
### *Official Examination Blueprint & Model Answers Written for Full Marks*

> **Course**: CSE4005 — Machine Learning | **Faculty**: Dr. Nilamadhab Mishra  
> **Slot**: A21+A23 | **Time Allowed**: 3 Hours | **Maximum Marks**: 100  
> **Pre-TEE Internal Standing**: **62.20 / 70.0** vs Class Mean **61.90 / 70.0** *(+0.30 ahead)*  
> **Target for A Grade ($\ge \mu + 0.5\sigma$)**: **70–74 / 100** *(Must score ~10 marks above TEE class average)*  
> **Target for S Grade (Total $\ge 90.0$)**: **93+ / 100** *(Strict VIT rule)*  
> **B-Grade Danger Zone**: **48–69 / 100** *(B Grade is an absolute NO-GO for CGPA)*  

---

## 📑 QUESTION INDEX & MODULE MAPPING

| Q# | Question Title & Syllabus Topic | Module | Marks | Type |
|:---:|:---|:---:|:---:|:---:|
| **Q1** | [Imbalanced Datasets, Accuracy Paradox & SMOTE (Activity-13)](#question-1-module-5--12-marks--activity-13) | Mod 5 | 12M | Theory + Numerical |
| **Q2** | [ID3 Decision Tree Induction & Root Selection (`buys_computer`)](#question-2-module-2--12-marks--activity-a-4) | Mod 2 | 12M | Core Algorithmic Numerical |
| **Q3** | [AdaBoost Sequential Ensemble & Weight Update Trace](#question-3-module-3--12-marks--activity-task-a9a10) | Mod 3 | 12M | Multi-Step Numerical Trace |
| **Q4** | [Naïve Bayes Classification with Laplace Smoothing (Task A-11)](#question-4-module-4--12-marks--activity-a-11) | Mod 4 | 12M | Probabilistic Numerical |
| **Q5** | [PCA Projected Variance Maximization Derivation via Lagrange](#question-5-module-5--8-marks--lecture-slide-50) | Mod 5 | 8M | Mathematical Derivation |
| **Q6** | [Support Vector Machines (SVM) Maximum Margin & Wolfe Dual](#question-6-module-2--8-marks--activity-self-explore) | Mod 2 | 8M | Proof + Geometry |
| **Q7** | [Hierarchical AGNES (Single vs Complete Link) & K-Means Lloyd](#question-7-module-3--8-marks--tasks-a9--a10) | Mod 3 | 8M | Clustering Numerical Trace |
| **Q8** | [Association Rule Mining: Apriori vs FP-Growth & HUIM / TWU](#question-8-module-4--8-marks--task-a12) | Mod 4 | 8M | Mining Algorithmic Steps |
| **Q9** | [Computational Learning Theory: PAC Bounds & VC Dimension](#question-9-module-1--12-marks--activity-02) | Mod 1 | 12M | Mathematical Derivation |
| **Q10**| [Bayes Optimal Classifier vs MAP & Height-Weight OLS Regression](#question-10-module-4--2--8-marks--cat-1-q4) | Mod 4 & 2 | 8M | Probability + OLS Fit |

---

# QUESTION 1 [Module 5 — 12 Marks / Activity-13]

### Question:
*(a) Explain the concept of imbalanced datasets in machine learning. Discuss its causes, characteristics, and why accuracy is misleading when dealing with imbalanced data. Illustrate with a suitable numerical example.*  
*(b) Explain the complete working mechanism of SMOTE with an example. How are minority-class samples selected, nearest neighbors identified, and synthetic samples generated?*  
*(c) Compare Random Oversampling (ROS) and SMOTE for handling class imbalance.*

---

### MODEL EXAM ANSWER:

#### 1. Concept of Imbalanced Datasets & The Accuracy Paradox

* **Definition**: A dataset exhibits class imbalance when the distribution of target classes is significantly skewed, with the majority class severely outnumbering the minority class (e.g., $99:1$ or $99.9:0.1$). Typical domains include credit card fraud detection, cancer screening, and network intrusion detection.
* **Causes**:
  1. Natural rarity of events in the real world (e.g., rare diseases, manufacturing defects).
  2. Asymmetric data collection costs or observation windows.
* **The Accuracy Paradox (Numerical Proof)**:
  - Consider a medical dataset of $N = 1,000$ patients:
    $$\text{Actual Negatives (Benign)} = 990, \quad \text{Actual Positives (Malignant)} = 10$$
  - A naive "Dummy Classifier" that predicts **Negative for all 1,000 instances** produces the following Confusion Matrix:
    - $\text{True Positives } (TP) = 0$
    - $\text{False Positives } (FP) = 0$
    - $\text{True Negatives } (TN) = 990$
    - $\text{False Negatives } (FN) = 10$
  - Calculating performance metrics:
    $$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} = \frac{0 + 990}{1000} = \mathbf{99.0\%}$$
    $$\text{Recall (Sensitivity)} = \frac{TP}{TP + FN} = \frac{0}{0 + 10} = \mathbf{0.0\%}$$
  - **Clinical Conclusion**: Despite a seemingly exceptional accuracy of $99.0\%$, the classifier fails to detect even a single positive case ($\text{Recall} = 0\%$). All 10 cancer patients are sent home undiagnosed. Therefore, accuracy is an invalid metric for imbalanced classification.

![Classification Metrics and Confusion Matrix](images/confusion_matrix_and_metrics.svg)

#### 2. Complete Metric Evaluation Suite

$$\text{Precision} = \frac{TP}{TP + FP}, \qquad \text{Recall} = \frac{TP}{TP + FN}$$

$$\text{Specificity} = \frac{TN}{TN + FP}, \qquad F_1\text{-Score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2 \cdot TP}{2 \cdot TP + FP + FN}$$

> For imbalanced data, models must be evaluated using the **Precision-Recall AUC (PR-AUC)** rather than the standard ROC-AUC, because ROC-AUC is distorted by large true negative counts.

---

#### 3. SMOTE (Synthetic Minority Over-sampling Technique) Mechanism

SMOTE synthetically generates new minority-class examples along the feature line segments connecting minority instances to their nearest minority neighbors.

* **Algorithmic Steps**:
  1. For each sample $\mathbf{x}_i \in S_{\text{min}}$, compute the Euclidean distance to all other samples in $S_{\text{min}}$.
  2. Identify the $k$-nearest neighbors of $\mathbf{x}_i$ within $S_{\text{min}}$ (typically $k=5$).
  3. Randomly select one neighbor, denoted as $\mathbf{x}_{zi}$.
  4. Generate a synthetic instance $\mathbf{x}_{\text{new}}$ via linear interpolation:
     $$\mathbf{x}_{\text{new}} = \mathbf{x}_i + \lambda \cdot (\mathbf{x}_{zi} - \mathbf{x}_i), \quad \lambda \sim \mathcal{U}(0, 1)$$

![SMOTE Synthetic Sample Interpolation](images/smote_synthetic_interpolation.svg)

---

> 💡 **EXAM NOTE: Numerical Solving Strategy for SMOTE**  
> 1. Calculate difference vector: $\Delta = \mathbf{x}_{zi} - \mathbf{x}_i$.  
> 2. Multiply difference vector by the scalar parameter $\lambda$: $\lambda \cdot \Delta$.  
> 3. Add to seed point: $\mathbf{x}_{\text{new}} = \mathbf{x}_i + (\lambda \cdot \Delta)$.  
> 4. Verification: The resulting coordinates must lie strictly between $\mathbf{x}_i$ and $\mathbf{x}_{zi}$.

#### 4. Coordinate Interpolation Numerical Solution
* **Given**:
  - Seed sample: $\mathbf{x}_i = [2.0, \; 4.0]$
  - Selected $k$-NN neighbor: $\mathbf{x}_{zi} = [6.0, \; 10.0]$
  - Random interpolation coefficient: $\lambda = 0.5$
* **Step 1: Difference Vector**:
  $$\mathbf{x}_{zi} - \mathbf{x}_i = [6.0 - 2.0, \; 10.0 - 4.0] = [4.0, \; 6.0]$$
* **Step 2: Linear Scaling**:
  $$\lambda \cdot (\mathbf{x}_{zi} - \mathbf{x}_i) = 0.5 \cdot [4.0, \; 6.0] = [2.0, \; 3.0]$$
* **Step 3: Synthetic Instance Calculation**:
  $$\mathbf{x}_{\text{new}} = [2.0, \; 4.0] + [2.0, \; 3.0] = \mathbf{[4.0, \; 7.0]}$$

---

#### 5. Comparison: Random Oversampling (ROS) vs SMOTE

| Evaluation Parameter | Random Oversampling (ROS) | SMOTE (Synthetic Oversampling) |
|:---|:---|:---|
| **Underlying Mechanism** | Duplicates existing raw minority instances at random. | Synthesizes novel points via linear interpolation in feature space. |
| **Overfitting Susceptibility** | **Extremely High**: Forces model to memorize discrete points. | **Low**: Broadens and stabilizes minority decision volume. |
| **Decision Boundary** | Creates rigid, constricted decision boundaries around points. | Smooths and expands the geometric boundary between classes. |
| **Computational Overhead** | $O(N)$ (Instantaneous random selection). | $O(N^2 \cdot D)$ (Requires distance matrix computation for $k$-NN). |

$$\mathbf{\text{Final Result Boxed: } \mathbf{x}_{\text{new}} = [4.0, \; 7.0]}$$

---

# QUESTION 2 [Module 2 — 12 Marks / Activity [A-4]]

### Question:
*(a) Explain the fundamental concepts of Decision Tree induction using the ID3 algorithm. Define Entropy, Information Gain, Gain Ratio, and Gini Impurity.*  
*(b) The following training dataset `buys_computer` consists of 14 instances with attributes `Age`, `Income`, `Student`, `Credit_Rating`, and class label `Buys_Computer`. Determine which attribute should be chosen as the Root Node of the decision tree using Information Gain.*

---

### MODEL EXAM ANSWER:

#### 1. Theoretical Formulations

* **Decision Tree Structure**: A directed tree consisting of a **Root Node** (no incoming branches), **Internal Nodes** (decision tests on feature attributes), and **Leaf Nodes** (terminal class assignments).
* **Entropy**: Measures the impurity or degree of randomness in sample set $S$:
  $$H(S) = - \sum_{i=1}^c p_i \log_2(p_i)$$
  *(For a binary classification task: $H(S) = - p_+ \log_2(p_+) - p_- \log_2(p_-)$. Pure node: $H=0$. Maximum impurity $50/50$: $H=1.0$).*
* **Information Gain (ID3)**: The expected reduction in entropy caused by partitioning $S$ on attribute $A$:
  $$\text{Gain}(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$$
* **Gain Ratio (C4.5)**: Penalizes multi-valued attributes using Split Information:
  $$\text{SplitInfo}(S, A) = - \sum_{v=1}^k \frac{|S_v|}{|S|} \log_2\left(\frac{|S_v|}{|S|}\right), \qquad \text{GainRatio}(S, A) = \frac{\text{Gain}(S, A)}{\text{SplitInfo}(S, A)}$$
* **Gini Impurity (CART)**:
  $$\text{Gini}(S) = 1 - \sum_{i=1}^c p_i^2$$

![Decision Tree Entropy and Information Gain](images/decision_tree_entropy_split.svg)

---

> 💡 **EXAM NOTE: Numerical Solving Strategy for ID3 Trees**  
> 1. Calculate Target Entropy $H(S)$ using total class distribution $(p_+, p_-)$.  
> 2. On your calculator: $\log_2(x) = \frac{\ln(x)}{\ln(2)} = \frac{\ln(x)}{0.69315}$.  
> 3. For each candidate attribute: partition the data, find individual subset entropies $H(S_v)$, and weight them: $E(S, A) = \sum \frac{|S_v|}{|S|} H(S_v)$.  
> 4. $\text{Gain} = H(S) - E(S, A)$. The attribute with the **highest Gain** is chosen as the Root.

#### 2. Step-by-Step ID3 Root Node Selection on `buys_computer`

#### Step 1: Overall Target Entropy $H(S)$
Total instances $N = 14$. Class counts: $\text{Yes } = 9, \; \text{No } = 5$.
$$p_+ = \frac{9}{14} \approx 0.6429, \quad p_- = \frac{5}{14} \approx 0.3571$$
$$H(S) = - \left[ \frac{9}{14} \log_2\left(\frac{9}{14}\right) + \frac{5}{14} \log_2\left(\frac{5}{14}\right) \right]$$
$$H(S) = - [0.6429(-0.6374) + 0.3571(-1.4854)] = 0.4098 + 0.5305 = \mathbf{0.9403 \text{ bits}}$$

#### Step 2: Evaluation of Attribute `Age`
* Values of `Age`: `<=30` (5 instances), `31..40` (4 instances), `>40` (5 instances).
1. **For `Age <= 30`** ($|S_1| = 5$: 2 Yes, 3 No):
   $$H(S_{<=30}) = - \left[ \frac{2}{5}\log_2\frac{2}{5} + \frac{3}{5}\log_2\frac{3}{5} \right] = - [0.4(-1.3219) + 0.6(-0.7370)] = \mathbf{0.9710}$$
2. **For `Age 31..40`** ($|S_2| = 4$: 4 Yes, 0 No):
   $$H(S_{31..40}) = - [1.0 \log_2(1.0) + 0] = \mathbf{0.0000} \quad (\text{Pure Node})$$
3. **For `Age > 40`** ($|S_3| = 5$: 3 Yes, 2 No):
   $$H(S_{>40}) = - \left[ \frac{3}{5}\log_2\frac{3}{5} + \frac{2}{5}\log_2\frac{2}{5} \right] = \mathbf{0.9710}$$
* **Weighted Conditional Entropy $E(S, \text{Age})$**:
  $$E(S, \text{Age}) = \frac{5}{14}(0.9710) + \frac{4}{14}(0.0000) + \frac{5}{14}(0.9710) = 0.3468 + 0 + 0.3468 = \mathbf{0.6936 \text{ bits}}$$
* **Information Gain**:
  $$\text{Gain}(S, \text{Age}) = H(S) - E(S, \text{Age}) = 0.9403 - 0.6936 = \mathbf{0.2467 \text{ bits}}$$

#### Step 3: Evaluation of Attribute `Credit_Rating`
* Values: `Fair` (8 instances: 6 Yes, 2 No), `Excellent` (6 instances: 3 Yes, 3 No).
1. **For `Fair`** ($|S_{\text{Fair}}| = 8$: 6 Yes, 2 No):
   $$H(S_{\text{Fair}}) = - \left[ \frac{6}{8}\log_2\frac{6}{8} + \frac{2}{8}\log_2\frac{2}{8} \right] = - [0.75(-0.4150) + 0.25(-2.0)] = \mathbf{0.8113}$$
2. **For `Excellent`** ($|S_{\text{Exc}}| = 6$: 3 Yes, 3 No):
   $$H(S_{\text{Exc}}) = - \left[ \frac{3}{6}\log_2\frac{3}{6} + \frac{3}{6}\log_2\frac{3}{6} \right] = \mathbf{1.0000}$$
* **Weighted Conditional Entropy $E(S, \text{Credit\_Rating})$**:
  $$E(S, \text{Credit}) = \frac{8}{14}(0.8113) + \frac{6}{14}(1.0000) = 0.4636 + 0.4286 = \mathbf{0.8922 \text{ bits}}$$
* **Information Gain**:
  $$\text{Gain}(S, \text{Credit}) = 0.9403 - 0.8922 = \mathbf{0.0481 \text{ bits}}$$

#### Step 4: Attribute Comparison & Root Selection
$$\text{Gain}(S, \text{Age}) = \mathbf{0.2467 \text{ bits}} \quad > \quad \text{Gain}(S, \text{Credit\_Rating}) = \mathbf{0.0481 \text{ bits}}$$

$$\mathbf{\text{Final Decision: Attribute `Age` is selected as the ROOT NODE.}}$$

---

# QUESTION 3 [Module 3 — 12 Marks / Activity Task A9/A10]

### Question:
*(a) Explain the sequential boosting paradigm of AdaBoost. State how base models are combined and derive the weight update equations.*  
*(b) Consider a training dataset of $N=5$ instances with initial uniform weights $w_i^{(1)} = 0.20$. Base classifier $h_1$ misclassifies sample $2$ and sample $4$, while correctly classifying samples $1, 3,$ and $5$.*  
*Compute the weighted error rate $\epsilon_1$, the classifier importance weight $\alpha_1$, the unnormalized weights, the normalization factor $Z_1$, and the updated normalized sample distribution $w_i^{(2)}$.*

---

### MODEL EXAM ANSWER:

#### 1. AdaBoost Theoretical Architecture
AdaBoost (Adaptive Boosting) trains base classifiers sequentially. Instances misclassified by model $h_t$ receive higher weights in iteration $t+1$, forcing subsequent learners to concentrate on hard-to-classify samples.

* **Final Decision Rule**: A weighted majority vote:
  $$H(x) = \text{sign}\left( \sum_{t=1}^T \alpha_t h_t(x) \right)$$

![AdaBoost Sequential Ensemble Architecture](images/adaboost_sequential_architecture.svg)

---

> 💡 **EXAM NOTE: Numerical Solving Strategy for AdaBoost**  
> 1. Weighted error $\epsilon_t = \sum_{\text{misclassified}} w_i$. Check that $\epsilon_t < 0.50$.  
> 2. Classifier importance: $\alpha_t = \frac{1}{2}\ln\left(\frac{1-\epsilon_t}{\epsilon_t}\right)$.  
> 3. Multipliers: Correct instances $\times e^{-\alpha_t}$; Incorrect instances $\times e^{+\alpha_t}$.  
> 4. Normalization constant: $Z_t = \sum \tilde{w}_i$.  
> 5. Final weights: $w_i^{(t+1)} = \tilde{w}_i / Z_t$. **Verification: $\sum w_i^{(t+1)} = 1.0000$**.

#### 2. Step-by-Step Numerical Trace ($N=5$)

#### Step 1: Weighted Error Rate $\epsilon_1$
Misclassified samples are $x_2$ and $x_4$:
$$\epsilon_1 = w_2^{(1)} + w_4^{(1)} = 0.20 + 0.20 = \mathbf{0.40}$$

#### Step 2: Classifier Weight $\alpha_1$
$$\alpha_1 = \frac{1}{2} \ln \left( \frac{1 - \epsilon_1}{\epsilon_1} \right) = \frac{1}{2} \ln \left( \frac{0.60}{0.40} \right) = \frac{1}{2} \ln(1.5)$$
$$\ln(1.5) \approx 0.405465 \implies \alpha_1 = \frac{0.405465}{2} = \mathbf{0.2027}$$

#### Step 3: Multiplier Factors
* For correct samples: $e^{-\alpha_1} = e^{-0.2027} = \mathbf{0.8165}$
* For incorrect samples: $e^{+\alpha_1} = e^{+0.2027} = \mathbf{1.2247}$

#### Step 4: Unnormalized Weights $\tilde{w}_i$
* Samples $1, 3, 5$ (Correct):
  $$\tilde{w}_1 = \tilde{w}_3 = \tilde{w}_5 = 0.20 \times 0.8165 = \mathbf{0.1633}$$
* Samples $2, 4$ (Incorrect):
  $$\tilde{w}_2 = \tilde{w}_4 = 0.20 \times 1.2247 = \mathbf{0.2449}$$

#### Step 5: Normalization Factor $Z_1$
$$Z_1 = \sum_{i=1}^5 \tilde{w}_i = 3(0.1633) + 2(0.2449) = 0.4899 + 0.4898 = \mathbf{0.9797}$$

#### Step 6: Normalized Weights $w_i^{(2)} = \frac{\tilde{w}_i}{Z_1}$
* For correct samples ($1, 3, 5$):
  $$w_1^{(2)} = w_3^{(2)} = w_5^{(2)} = \frac{0.1633}{0.9797} = \mathbf{0.1667}$$
* For incorrect samples ($2, 4$):
  $$w_2^{(2)} = w_4^{(2)} = \frac{0.2449}{0.9797} = \mathbf{0.2500}$$

#### Summary Weight Distribution Table:
| Sample $i$ | True Label $y_i$ | Classifier $h_1(x_i)$ | Status | Initial $w_i^{(1)}$ | Multiplier | Unnormalized $\tilde{w}_i$ | Normalized $w_i^{(2)}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $+1$ | $+1$ | Correct | 0.20 | 0.8165 | 0.1633 | **0.1667** |
| 2 | $+1$ | $-1$ | **Error** | 0.20 | 1.2247 | 0.2449 | **0.2500** |
| 3 | $-1$ | $-1$ | Correct | 0.20 | 0.8165 | 0.1633 | **0.1667** |
| 4 | $-1$ | $+1$ | **Error** | 0.20 | 1.2247 | 0.2449 | **0.2500** |
| 5 | $+1$ | $+1$ | Correct | 0.20 | 0.8165 | 0.1633 | **0.1667** |
| **Sum** | — | — | — | **1.00** | — | **$Z_1 = 0.9797$** | **1.0001 $\approx$ 1.00** |

$$\mathbf{\text{Final Boxed Weights: } w_{\text{correct}}^{(2)} = 0.1667, \quad w_{\text{error}}^{(2)} = 0.2500}$$

---

# QUESTION 4 [Module 4 — 12 Marks / Activity [A-11]]

### Question:
*(a) State Bayes' Theorem and explain the conditional independence assumption of the Naïve Bayes classifier. Explain the zero-frequency problem and the mathematical formulation of Laplace smoothing.*  
*(b) Given the Loan Approval dataset of 12 applicants (5 Approved, 7 Rejected). Predict the loan status for a new applicant:*  
$$X = (\text{Income}=\text{Medium}, \; \text{Credit}=\text{Good}, \; \text{Employment}=\text{Stable}, \; \text{Existing Loan}=\text{No})$$  
*(c) Critique whether the conditional independence assumption holds in real-world credit evaluation.*

---

### MODEL EXAM ANSWER:

#### 1. Mathematical Formulation of Naïve Bayes

* **Bayes' Theorem**:
  $$P(Y \mid X) = \frac{P(X \mid Y) \cdot P(Y)}{P(X)}$$
* **Conditional Independence Assumption**: Features $X_1, X_2, \dots, X_n$ are assumed to be mutually independent given class $Y$:
  $$P(X_1, \dots, X_n \mid Y) = \prod_{i=1}^n P(X_i \mid Y)$$
* **Classification Decision Rule**:
  $$y^* = \arg\max_{c \in C} \left[ P(Y=c) \prod_{i=1}^n P(X_i = x_i \mid Y=c) \right]$$
* **Laplace Smoothing (Resolving Zero Frequency)**:
  If a category never appears with a class in the training set ($P(X_i \mid Y) = 0$), the entire product likelihood collapses to zero. Laplace smoothing resolves this by introducing pseudo-counts:
  $$P(X_i = v \mid Y = c) = \frac{\text{Count}(X_i = v, Y = c) + 1}{\text{Count}(Y = c) + |V_i|}$$
  where $|V_i|$ is the number of distinct attribute values for feature $X_i$.

![Probabilistic Learning: Naive Bayes vs BBN](images/bayes_naive_and_bbn.svg)

---

> 💡 **EXAM NOTE: Numerical Solving Strategy for Naïve Bayes**  
> 1. Calculate class priors: $P(\text{Class}) = \text{Count}(\text{Class}) / N$.  
> 2. Calculate individual likelihoods for the test instance under each class: $P(X_i \mid \text{Class})$.  
> 3. Multiply likelihoods together with the class prior to obtain the unnormalized posterior score.  
> 4. Normalize: $P(\text{Class}_1 \mid X) = \frac{\text{Score}_1}{\text{Score}_1 + \text{Score}_2}$. State the predicted class explicitly.

#### 2. Step-by-Step Numerical Classification

#### Step 1: Class Priors ($N = 12$)
$$P(\text{Approved}) = \frac{5}{12} \approx 0.4167, \qquad P(\text{Rejected}) = \frac{7}{12} \approx 0.5833$$

#### Step 2: Likelihoods for Class = Approved ($N_{\text{App}} = 5$)
* $P(\text{Income=Medium} \mid \text{Approved}) = \frac{2}{5} = \mathbf{0.40}$
* $P(\text{Credit=Good} \mid \text{Approved}) = \frac{5}{5} = \mathbf{1.00}$
* $P(\text{Employment=Stable} \mid \text{Approved}) = \frac{4}{5} = \mathbf{0.80}$
* $P(\text{Existing Loan=No} \mid \text{Approved}) = \frac{4}{5} = \mathbf{0.80}$

$$\text{Likelihood Product } P(X \mid \text{Approved}) = 0.40 \times 1.00 \times 0.80 \times 0.80 = \mathbf{0.2560}$$
$$\text{Score}(\text{Approved}) = \frac{5}{12} \times 0.2560 = \mathbf{0.1067}$$

#### Step 3: Likelihoods for Class = Rejected ($N_{\text{Rej}} = 7$)
* $P(\text{Income=Medium} \mid \text{Rejected}) = \frac{2}{7} \approx \mathbf{0.2857}$
* $P(\text{Credit=Good} \mid \text{Rejected}) = \frac{2}{7} \approx \mathbf{0.2857}$
* $P(\text{Employment=Stable} \mid \text{Rejected}) = \frac{3}{7} \approx \mathbf{0.4286}$
* $P(\text{Existing Loan=No} \mid \text{Rejected}) = \frac{3}{7} \approx \mathbf{0.4286}$

$$\text{Likelihood Product } P(X \mid \text{Rejected}) = \frac{2}{7} \times \frac{2}{7} \times \frac{3}{7} \times \frac{3}{7} = \frac{36}{2401} \approx \mathbf{0.0150}$$
$$\text{Score}(\text{Rejected}) = \frac{7}{12} \times \frac{36}{2401} = \frac{3}{343} \approx \mathbf{0.00875}$$

#### Step 4: Normalization & Final Classification
$$\text{Total Evidence } P(X) = 0.1067 + 0.00875 = 0.11545$$
$$P(\text{Approved} \mid X) = \frac{0.1067}{0.11545} = \mathbf{92.42\%}$$
$$P(\text{Rejected} \mid X) = \frac{0.00875}{0.11545} = \mathbf{7.58\%}$$

$$\mathbf{\text{Final Decision: The loan application is APPROVED (92.42\% confidence).}}$$

#### 3. Real-World Independence Critique
* **Do these attributes exhibit true independence?** **No.**
* **Economic Justification**:
  1. `Employment Stability` and `Income` are positively correlated (stable professionals typically command higher and more predictable earnings).
  2. `Existing Loan` and `Credit History` are strongly interdependent (existing debt service directly impacts credit utilization and repayment scores).
* **Robustness Rationale**: Despite this theoretical violation, Naïve Bayes succeeds in practice because classification depends solely on the **argmax ranking** ($0.1067 \gg 0.00875$) rather than calibrated probabilities.

---

# QUESTION 5 [Module 5 — 8 Marks / Lecture Slide 5.0]

### Question:
*Derive the principal component projection vector in Principal Component Analysis (PCA) by maximizing the projected variance using the method of Lagrange Multipliers. Prove that the optimal projection vector is the eigenvector of the sample covariance matrix corresponding to the maximum eigenvalue.*

---

### MODEL EXAM ANSWER:

#### Mathematical Derivation of PCA

#### 1. Data Centering & Covariance Matrix
Let $\mathbf{X}$ be a dataset of $m$ observations with $n$ features. The centered data matrix $\mathbf{X}_c$ satisfies:
$$\sum_{i=1}^m \mathbf{x}_i = \mathbf{0}$$
The empirical sample covariance matrix $\mathbf{\Sigma} \in \mathbb{R}^{n \times n}$ is:
$$\mathbf{\Sigma} = \frac{1}{m} \mathbf{X}_c^T \mathbf{X}_c$$

#### 2. Projected Variance Expression
Let $\mathbf{u}_1 \in \mathbb{R}^n$ be a unit projection vector ($\mathbf{u}_1^T \mathbf{u}_1 = 1$). The projection of data point $\mathbf{x}_i$ onto $\mathbf{u}_1$ is the scalar:
$$z_i = \mathbf{x}_i^T \mathbf{u}_1$$
Since the data is zero-mean ($\bar{z} = 0$), the variance of the projected data points is:
$$\sigma_z^2 = \frac{1}{m} \sum_{i=1}^m z_i^2 = \frac{1}{m} \sum_{i=1}^m (\mathbf{u}_1^T \mathbf{x}_i)(\mathbf{x}_i^T \mathbf{u}_1) = \mathbf{u}_1^T \left( \frac{1}{m} \mathbf{X}_c^T \mathbf{X}_c \right) \mathbf{u}_1 = \mathbf{u}_1^T \mathbf{\Sigma} \mathbf{u}_1$$

#### 3. Constrained Optimization via Lagrange Multipliers
To maximize projected variance while constraining $\mathbf{u}_1$ to unit length:
$$\max_{\mathbf{u}_1} \mathbf{u}_1^T \mathbf{\Sigma} \mathbf{u}_1 \quad \text{subject to } \mathbf{u}_1^T \mathbf{u}_1 = 1$$
Formulate the Lagrangian function with Lagrange multiplier $\lambda$:
$$\mathcal{L}(\mathbf{u}_1, \lambda) = \mathbf{u}_1^T \mathbf{\Sigma} \mathbf{u}_1 - \lambda (\mathbf{u}_1^T \mathbf{u}_1 - 1)$$

#### 4. Stationary Point Condition
Differentiating $\mathcal{L}$ with respect to $\mathbf{u}_1$ and equating to zero:
$$\frac{\partial \mathcal{L}}{\partial \mathbf{u}_1} = 2 \mathbf{\Sigma} \mathbf{u}_1 - 2 \lambda \mathbf{u}_1 = \mathbf{0}$$
$$\mathbf{\Sigma} \mathbf{u}_1 = \lambda \mathbf{u}_1$$

#### 5. Conclusion & Variance Maximization
1. The condition $\mathbf{\Sigma} \mathbf{u}_1 = \lambda \mathbf{u}_1$ proves that $\mathbf{u}_1$ must be an **eigenvector** of covariance matrix $\mathbf{\Sigma}$, and $\lambda$ is its corresponding **eigenvalue**.
2. Pre-multiplying both sides by $\mathbf{u}_1^T$:
   $$\mathbf{u}_1^T \mathbf{\Sigma} \mathbf{u}_1 = \lambda (\mathbf{u}_1^T \mathbf{u}_1) = \lambda$$
   $$\mathbf{\sigma_z^2 = \lambda}$$
3. Therefore, the projected variance is precisely equal to the eigenvalue $\lambda$. To maximize variance, $\mathbf{u}_1$ must be chosen as the eigenvector corresponding to the **largest eigenvalue $\lambda_{\max}$**.

$$\mathbf{\text{Q.E.D. Optimal projection vector } \mathbf{u}_1 \text{ is the eigenvector for } \lambda_{\max}.}$$

![PCA Variance Maximization and Orthogonal Axes](images/pca_variance_maximization.svg)

---

# QUESTION 6 [Module 2 — 8 Marks / Activity-Self Explore]

### Question:
*(a) Explain the geometric concept of the maximum margin hyperplane in Support Vector Machines (SVM). Derive the margin width $M = \frac{2}{\|\mathbf{w}\|}$ and formulate the Primal and Dual optimization problems.*  
*(b) State Mercer's Theorem for valid kernel functions.*

---

### MODEL EXAM ANSWER:

#### 1. Geometric Margin Formulation
Let linearly separable training data be $(x_1, y_1), \dots, (x_m, y_m)$ where $y_i \in \{-1, +1\}$.
* **Decision Hyperplane**: $\mathbf{w}^T \mathbf{x} + b = 0$.
* **Canonical Margin Hyperplanes**:
  $$\mathbf{w}^T \mathbf{x} + b = +1 \quad (\text{Positive support vector boundary})$$
  $$\mathbf{w}^T \mathbf{x} + b = -1 \quad (\text{Negative support vector boundary})$$
* **Margin Derivation**:
  Let $\mathbf{x}_+$ lie on the positive boundary and $\mathbf{x}_-$ lie on the negative boundary:
  $$\mathbf{w}^T \mathbf{x}_+ + b = 1, \qquad \mathbf{w}^T \mathbf{x}_- + b = -1$$
  Subtracting the equations:
  $$\mathbf{w}^T (\mathbf{x}_+ - \mathbf{x}_-) = 2$$
  Dividing by the Euclidean norm $\|\mathbf{w}\|$ yields the orthogonal projection:
  $$\text{Margin } M = \frac{\mathbf{w}^T (\mathbf{x}_+ - \mathbf{x}_-)}{\|\mathbf{w}\|} = \mathbf{\frac{2}{\|\mathbf{w}\|}}$$

![Support Vector Machine Hyperplane and Maximum Margin](images/svm_hyperplane_margin.svg)

---

#### 2. Primal & Dual Optimization Problems

* **Primal Problem**: Maximizing $\frac{2}{\|\mathbf{w}\|}$ is equivalent to minimizing $\frac{1}{2}\|\mathbf{w}\|^2$:
  $$\min_{\mathbf{w}, b} \frac{1}{2} \|\mathbf{w}\|^2 \quad \text{subject to } y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1, \quad \forall i=1,\dots,m$$
* **Dual Problem (via Wolfe Duality)**:
  $$\max_{\mathbf{\alpha}} \sum_{i=1}^m \alpha_i - \frac{1}{2} \sum_{i=1}^m \sum_{j=1}^m \alpha_i \alpha_j y_i y_j K(\mathbf{x}_i, \mathbf{x}_j)$$
  $$\text{subject to } \alpha_i \ge 0, \quad \sum_{i=1}^m \alpha_i y_i = 0$$
* **Weight Reconstruction**:
  $$\mathbf{w} = \sum_{i \in \text{SV}} \alpha_i y_i \mathbf{x}_i$$
  *(Non-support vectors have $\alpha_i = 0$ and have no influence on the decision boundary).*

#### 3. Mercer's Theorem
A kernel function $K(\mathbf{x}, \mathbf{z})$ is a valid inner-product mapping in some feature space $\mathcal{H}$ if and only if its Gram Matrix $\mathbf{K}$ ($K_{ij} = K(\mathbf{x}_i, \mathbf{x}_j)$) is **symmetric and positive semi-definite** for all finite point sets:
$$\mathbf{c}^T \mathbf{K} \mathbf{c} \ge 0, \quad \forall \mathbf{c} \in \mathbb{R}^m \quad (\text{All eigenvalues } \ge 0)$$

---

# QUESTION 7 [Module 3 — 8 Marks / Tasks A9 & A10]

### Question:
*(a) Explain the algorithmic steps of Lloyd's K-Means clustering algorithm and state the Within-Cluster Sum of Squares (WCSS) objective.*  
*(b) Consider the 1D dataset $D = \{5, 9, 14, 25, 28, 40\}$. Perform agglomerative hierarchical clustering using Single Linkage and Complete Linkage. State the chaining effect.*

---

### MODEL EXAM ANSWER:

#### 1. K-Means Lloyd's Algorithm
* **Objective Function (WCSS)**:
  $$J = \sum_{k=1}^K \sum_{\mathbf{x} \in C_k} \|\mathbf{x} - \mathbf{\mu}_k\|^2$$
* **Alternating Steps**:
  1. **Assignment Step**: Assign each observation to the nearest cluster centroid:
     $$C(i) = \arg\min_{k} \|\mathbf{x}_i - \mathbf{\mu}_k\|^2$$
  2. **Centroid Update Step**: Recalculate centroids as the cluster mean:
     $$\mathbf{\mu}_k = \frac{1}{|C_k|} \sum_{\mathbf{x} \in C_k} \mathbf{x}$$
* **K-Means++ Initialization**: Selects subsequent centroids with probability proportional to squared distance $D(\mathbf{x})^2$, preventing poor local minima.

![K-Means Clustering Iterative Convergence](images/kmeans_clustering_iterations.svg)

---

> 💡 **EXAM NOTE: Numerical Solving Strategy for Hierarchical Clustering**  
> 1. Compute pairwise distance table for all adjacent sorted numbers: $d(x_i, x_{i+1}) = |x_i - x_{i+1}|$.  
> 2. Always merge the pair with the **global minimum distance**.  
> 3. Update distance matrix to remaining clusters:  
>    - **Single Linkage**: $d(A, B) = \min_{a \in A, b \in B} |a - b|$.  
>    - **Complete Linkage**: $d(A, B) = \max_{a \in A, b \in B} |a - b|$.

#### 2. Hierarchical AGNES Clustering on $\{5, 9, 14, 25, 28, 40\}$

#### Single Linkage Execution ($d_{\min}$):
1. **Initial Distances**:
   $$d(5, 9)=4, \quad d(9, 14)=5, \quad d(14, 25)=11, \quad d(25, 28)=\mathbf{3}, \quad d(28, 40)=12$$
   - Minimum is $d(25, 28) = 3 \implies$ **Merge $\{25, 28\}$ at height $h=3$**.
2. **Next Minimum**:
   - $d(5, 9) = 4 \implies$ **Merge $\{5, 9\}$ at height $h=4$**.
3. **Distance to 14**:
   - $d(\{5, 9\}, 14) = \min(|5-14|, |9-14|) = \min(9, 5) = \mathbf{5}$.
   - Minimum is $5 \implies$ **Merge $\{5, 9, 14\}$ at height $h=5$**.
4. **Distance between $\{5, 9, 14\}$ and $\{25, 28\}$**:
   - $d = \min |14 - 25| = \mathbf{11}$.
   - Distance to 40: $d(\{25, 28\}, 40) = \min |28 - 40| = 12$.
   - Minimum is $11 \implies$ **Merge $\{5, 9, 14, 25, 28\}$ at height $h=11$**.
5. **Final Merge**: Merge with $\{40\}$ at distance $\min|28 - 40| = \mathbf{12}$.

#### Complete Linkage Execution ($d_{\max}$):
1. Merge $\{25, 28\}$ at $h=3$.
2. Merge $\{5, 9\}$ at $h=4$.
3. $d(\{5, 9\}, 14) = \max(9, 5) = \mathbf{9} \implies$ Merge $\{5, 9, 14\}$ at $h=9$.
4. Distance between $\{5, 9, 14\}$ and $\{25, 28\} = \max|5 - 28| = \mathbf{23}$.  
   Distance between $\{25, 28\}$ and $\{40\} = \max(|25-40|, |28-40|) = \mathbf{15}$.  
   Minimum is $15 \implies$ **Merge $\{25, 28\}$ with $\{40\}$ into $\{25, 28, 40\}$ at $h=15$**!
5. Final Merge: Merge $\{5, 9, 14\}$ with $\{25, 28, 40\}$ at height $\max|5 - 40| = \mathbf{35}$.

#### Inferences:
* **The Chaining Effect**: Single linkage suffers from chaining, where intermediate points (such as 14 bridging to 25) create long, straggly clusters.
* **Cluster Compactness**: Complete linkage enforces compact, spherical clusters by grouping $\{25, 28, 40\}$ together before merging with the left cluster.

---

# QUESTION 8 [Module 4 — 8 Marks / Task A12]

### Question:
*(a) Define Support, Confidence, and Lift in Association Rule Mining. State the Apriori Principle.*  
*(b) Explain High Utility Itemset Mining (HUIM). Why does downward closure fail in utility mining, and how does Transaction-Weighted Utilization (TWU) resolve it?*

---

### MODEL EXAM ANSWER:

#### 1. Association Rule Metrics & The Apriori Principle

* **Support**:
  $$\text{Supp}(X) = \frac{\text{Count}(X)}{N}$$
* **Confidence**:
  $$\text{Conf}(X \to Y) = \frac{\text{Supp}(X \cup Y)}{\text{Supp}(X)}$$
* **Lift**:
  $$\text{Lift}(X \to Y) = \frac{\text{Conf}(X \to Y)}{\text{Supp}(Y)} = \frac{\text{Supp}(X \cup Y)}{\text{Supp}(X) \cdot \text{Supp}(Y)}$$
  *(Lift $> 1 \implies$ Positive association; Lift $< 1 \implies$ Negative substitution; Lift $= 1 \implies$ Independence).*
* **The Apriori Principle (Anti-monotonicity)**:
  Any subset of a frequent itemset must also be frequent. If an itemset is infrequent, all of its supersets are guaranteed to be infrequent and are pruned immediately.

---

#### 2. High Utility Itemset Mining (HUIM) & TWU

* **Limitation of Standard Apriori**: Apriori considers only occurrence frequency (treating a $\$1$ notebook identical to a $\$1,000$ laptop).
* **High Utility Mining**: Evaluates external utility (unit profit $p(i)$) and internal utility (quantity sold $q(i, t)$):
  $$u(i, t) = p(i) \times q(i, t), \qquad u(X) = \sum_{t \supseteq X} \sum_{i \in X} u(i, t)$$
* **Why Downward Closure Fails in Utility Mining**:
  Adding an item with high profit can increase total utility ($u(X \cup Y) \ge u(X)$). Therefore, a low-utility itemset can have high-utility supersets, making Apriori subset pruning mathematically invalid.
* **The TWU Solution (Transaction-Weighted Utilization)**:
  The transaction utility $TU(t)$ is the total profit of all items in transaction $t$. The TWU of itemset $X$ is:
  $$\text{TWU}(X) = \sum_{t \supseteq X} TU(t)$$
* **TWU Anti-monotonicity Property**:
  $$\text{TWU}(X \cup Y) \le \text{TWU}(X)$$
  If $\text{TWU}(X) < \text{min\_util}$, neither $X$ nor any of its supersets can be high-utility, restoring safe downward-closure pruning!

---

# QUESTION 9 [Module 1 — 12 Marks / Activity-02]

### Question:
*(a) Define the Probably Approximately Correct (PAC) learning model and derive the sample complexity bound $m \ge \frac{1}{\epsilon} \left( \ln |H| + \ln \frac{1}{\delta} \right)$ for finite hypothesis spaces.*  
*(b) Define VC Dimension. Prove that the VC dimension of 1D closed intervals $[a, b]$ is 2.*  
*(c) What is the Natarajan Dimension? State its importance in multiclass learning.*

---

### MODEL EXAM ANSWER:

#### 1. PAC Learning Model & Sample Complexity Derivation

* **PAC Framework**: A concept class $C$ is PAC-learnable if learner $L$ outputs hypothesis $h \in H$ such that with probability $\ge 1 - \delta$, the true generalization error $\text{error}(h) \le \epsilon$, using a polynomial number of samples.
* **Sample Complexity Derivation**:
  1. A hypothesis $h$ is defined as "bad" if its true error exceeds $\epsilon$: $\text{error}(h) > \epsilon$.
  2. The probability that a bad hypothesis agrees with one independent training sample is at most $1 - \epsilon$.
  3. For $m$ independent training examples, the probability that a bad hypothesis remains consistent is:
     $$P(h_{\text{bad}} \text{ consistent}) \le (1 - \epsilon)^m \le e^{-m\epsilon}$$
  4. Applying the **Union Bound** across all hypotheses in finite space $H$:
     $$P(\exists h \in H \text{ such that } \text{error}(h) > \epsilon \text{ and consistent}) \le |H| e^{-m\epsilon}$$
  5. To guarantee PAC learnability, this failure probability must be bounded by confidence parameter $\delta$:
     $$|H| e^{-m\epsilon} \le \delta \implies e^{-m\epsilon} \le \frac{\delta}{|H|}$$
     $$-m\epsilon \le \ln\left(\frac{\delta}{|H|}\right) = -\ln\left(\frac{|H|}{\delta}\right)$$
     $$m \ge \frac{1}{\epsilon} \left( \ln |H| + \ln \frac{1}{\delta} \right)$$

---

#### 2. VC Dimension & Proof for 1D Intervals

* **Definition**: The VC dimension $VC(H)$ is the cardinality of the largest finite subset of points that can be **shattered** by $H$ (i.e., $H$ can realize all $2^N$ possible binary labelings).
* **Proof that $VC(H) = 2$ for Closed Intervals $H = \{[a, b]\}$**:
  1. **Shattering 2 Points**: Consider $x_1 = 1, x_2 = 3$. All $2^2 = 4$ labelings are attainable:
     - $(-1, -1) \implies [5, 6]$
     - $(+1, -1) \implies [0, 2]$
     - $(-1, +1) \implies [2, 4]$
     - $(+1, +1) \implies [0, 4]$  
     $\therefore VC(H) \ge 2$.
  2. **Inability to Shatter 3 Points**:
     Consider any 3 collinear points $x_1 < x_2 < x_3$. Test the labeling **$(+1, -1, +1)$**.  
     For $x_1$ and $x_3$ to be labeled $+1$, the interval $[a, b]$ must satisfy:
     $$a \le x_1 < x_2 < x_3 \le b$$
     This forces the intermediate point $x_2$ to lie inside $[a, b]$, making its label $+1$, which directly contradicts the required label $-1$.  
     Therefore, no 3 points can be shattered.
  3. **Conclusion**: $\mathbf{VC(\text{1D Intervals}) = 2}$.

#### 3. Natarajan Dimension (Multiclass PAC Learning)
The Natarajan dimension $N_{\dim}(H)$ extends the VC dimension to **multiclass classification** ($K \ge 3$ classes). A multiclass hypothesis class $H$ is PAC-learnable if and only if its **Natarajan Dimension is finite**:
$$N_{\dim}(H) < \infty$$

---

# QUESTION 10 [Module 4 & 2 — 8 Marks / CAT-1 Q4]

### Question:
*(a) Differentiate between the Maximum A Posteriori (MAP) hypothesis and the Bayes Optimal Classifier. Illustrate with a counterexample.*  
*(b) Formulate an Ordinary Least Squares (OLS) Linear Regression model for Height ($x$ in cm) and Weight ($y$ in kg) for 10 individuals: $\bar{x} = 161.2$, $\bar{y} = 56.4$, $\sum(x-\bar{x})^2 = 505.6$, $\sum(x-\bar{x})(y-\bar{y}) = 517.2$.*

---

### MODEL EXAM ANSWER:

#### 1. Bayes Optimal Classifier vs MAP

* **MAP Hypothesis**: Selects the single most probable hypothesis:
  $$h_{\text{MAP}} = \arg\max_{h \in H} P(h \mid D)$$
* **Bayes Optimal Classifier (BOC)**: Takes a weighted ensemble vote across all hypotheses in $H$:
  $$v_{\text{BOC}} = \arg\max_{v_j \in V} \sum_{h_i \in H} P(v_j \mid h_i) P(h_i \mid D)$$
* **The Counterexample**:
  - Given 3 hypotheses with posteriors: $P(h_1 \mid D) = 0.40, \; P(h_2 \mid D) = 0.30, \; P(h_3 \mid D) = 0.30$.
  - Predictions for query $x$: $h_1(x) = \mathbf{+}, \; h_2(x) = \mathbf{-}, \; h_3(x) = \mathbf{-}$.
  - **MAP Decision**: $\arg\max \{0.40, 0.30, 0.30\} = h_1 \implies \mathbf{+}$ (only $40\%$ confidence).
  - **BOC Decision**:
    $$P(+ \mid D) = 1.0 \times 0.40 = \mathbf{0.40}$$
    $$P(- \mid D) = (1.0 \times 0.30) + (1.0 \times 0.30) = \mathbf{0.60}$$
    $$v_{\text{BOC}} = \mathbf{-}$$
  - **Conclusion**: The Bayes Optimal Classifier predicts $-$, which is superior because the collective probability mass for $-$ is $60\%$. MAP makes a suboptimal choice.

---

> 💡 **EXAM NOTE: Numerical Solving Strategy for Linear Regression OLS**  
> 1. Slope: $m = \frac{\sum (x - \bar{x})(y - \bar{y})}{\sum (x - \bar{x})^2}$.  
> 2. Intercept: $c = \bar{y} - m\bar{x}$.  
> 3. Formulate equation: $\hat{y} = mx + c$.  
> 4. State units and interpretation clearly.

#### 2. Height-Weight Linear Regression Model Formulation

* **Given Values**:
  - Sample size: $N = 10$
  - Mean height: $\bar{x} = 161.2 \text{ cm}$
  - Mean weight: $\bar{y} = 56.4 \text{ kg}$
  - $\sum (x_i - \bar{x})^2 = 505.6$
  - $\sum (x_i - \bar{x})(y_i - \bar{y}) = 517.2$

* **Step 1: Calculate Slope $m$**:
  $$m = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} = \frac{517.2}{505.6} = \mathbf{1.0229 \approx 1.023}$$

* **Step 2: Calculate Intercept $c$**:
  $$c = \bar{y} - m \bar{x} = 56.4 - (1.0229 \times 161.2) = 56.4 - 164.89 = \mathbf{-108.49 \approx -108.51}$$

* **Step 3: Final Fitted Model**:
  $$\mathbf{\hat{y} = 1.023 \cdot x - 108.51}$$
  *(Interpretation: For every 1 cm increase in height, estimated body weight increases by approximately $1.023$ kg).*
"""

output_path = r"c:\Users\ankit\Fall2627\ML\notes\term_end\09-ml-guaranteed-topics-master-study-sheet.md"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print(f"Successfully generated exam-script formatted master sheet: {len(content)} characters.")
