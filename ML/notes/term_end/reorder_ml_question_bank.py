"""
reorder_ml_question_bank.py
Reorders 07-ml-fat-high-frequency-exam-question-bank.md into a strictly priority-ranked guide:
- TIER 1: Official Assignment Questions (Assignment 13 & 14)
- TIER 2: Guaranteed 6 Exam Numericals (ID3, AdaBoost, Naive Bayes, Apriori, K-Means, AGNES)
- TIER 3: Core Mathematical Derivations & Dr. Mishra PPT Special Topics (PCA, SVM Dual, Bayes Optimal, HUIM)
- TIER 4: Foundational Learning Theory & Comparisons (Regression, PAC Learning, VC Dimension, FP-Growth, Find-S)
"""

OUT_PATH = r"c:\Users\ankit\Fall2627\ML\notes\term_end\07-ml-fat-high-frequency-exam-question-bank.md"

content = """# 🏆 CSE4005: Machine Learning — Master FAT Exam Question Bank (Priority-Ranked)

> **Course**: CSE4005 — Machine Learning  
> **Faculty**: Dr. Nilamadhab Mishra | **Slot**: A21+A23  
> **Target**: FAT / TEE Exam — Saturday, 17-Oct-2026 (01:15 PM – 04:15 PM)  
> **Pre-TEE Standing**: **62.2 / 70.0** (+3.3 marks ahead of class!) | **Target for A Grade**: **64–68 / 100** | **Target for S Grade**: **88–92 / 100**  
> **Study Priority Architecture**:
> 1. **TIER 1**: Official Assignment 13 & 14 Questions (Faculty High-Probability Repeats)
> 2. **TIER 2**: The 6 Guaranteed Exam Numericals (50+ Direct Marks)
> 3. **TIER 3**: Core Mathematical Derivations & Faculty PPT Direct Prompts (PCA, SVM, BOC, HUIM)
> 4. **TIER 4**: Learning Theory & Architectural Comparisons (Regression, PAC, VC Dimension, FP-Growth)

---

## 📑 PRIORITY TABLE OF CONTENTS

| Priority Tier | Q# | Topic & Question Focus | Marks | Embedded Technical Schematic |
|:---|:---:|:---|:---:|:---|
| **TIER 1: ASSIGNMENTS** | **Q1** | **Assignment 13 Q1**: Imbalanced Datasets & Accuracy Paradox Proof | 12M | [`confusion_matrix_and_metrics.svg`](images/confusion_matrix_and_metrics.svg) |
| | **Q2** | **Assignment 13 Q2**: SMOTE Complete Mechanism & Interpolation Math | 12M | [`smote_synthetic_interpolation.svg`](images/smote_synthetic_interpolation.svg) |
| | **Q3** | **Assignment 13 Q3**: Random Oversampling vs SMOTE Comparison | 8M | — |
| | **Q4** | **Assignment 14**: Modern ML Technology Trend (Enterprise RAG) | 8M | — |
| **TIER 2: NUMERICALS** | **Q5** | **ID3 Decision Tree**: Entropy & Information Gain Root Selection | 12M | [`decision_tree_entropy_split.svg`](images/decision_tree_entropy_split.svg) |
| | **Q6** | **AdaBoost Ensemble**: 5-Sample Weight & Error Update Trace | 12M | [`adaboost_sequential_architecture.svg`](images/adaboost_sequential_architecture.svg) |
| | **Q7** | **Naïve Bayes**: "Play Tennis" Probability with Laplace Smoothing | 12M | [`bayes_naive_and_bbn.svg`](images/bayes_naive_and_bbn.svg) |
| | **Q8** | **Apriori Algorithm**: Full Itemset Mining & Association Rules | 12M | — |
| | **Q9** | **K-Means Clustering**: Lloyd's Iterative Algorithm & K-Means++ | 8M | [`kmeans_clustering_iterations.svg`](images/kmeans_clustering_iterations.svg) |
| | **Q10** | **Hierarchical Clustering**: AGNES Distance Matrix & Dendrogram | 10M | — |
| **TIER 3: DERIVATIONS** | **Q11** | **PCA Derivation**: Lagrange Multiplier & Covariance Eigenvalues | 12M | [`pca_variance_maximization.svg`](images/pca_variance_maximization.svg) |
| | **Q12** | **SVM Dual Formulation**: Margin Width $M = 2/||w||$ & Mercer's Rule | 12M | [`svm_hyperplane_margin.svg`](images/svm_hyperplane_margin.svg) |
| | **Q13** | **Bayes Optimal Classifier**: Optimality Proof & MAP Counterexample | 12M | — |
| | **Q14** | **HUIM & TWU**: High Utility Mining & Downward Closure Fix | 10M | — |
| **TIER 4: THEORY & PROOFS** | **Q15** | **Regression Comparison**: Linear vs Logistic Regression Analysis | 8M | — |
| | **Q16** | **PAC Learning**: Sample Complexity Derivation $m \\ge \\frac{1}{\\epsilon}(\\ln\|H\| + \\ln\\frac{1}{\\delta})$ | 12M | — |
| | **Q17** | **VC Dimension**: Shattering Definition & 1D Intervals Proof ($VC=2$) | 8M | — |
| | **Q18** | **FP-Growth vs Apriori**: FP-Tree Compression & Scalability | 8M | — |

---

# 🔴 TIER 1: OFFICIAL ASSIGNMENT QUESTIONS (STUDY FIRST!)
*(Direct from Dr. Nilamadhab Mishra's Official Assignments 13 and 14)*

---

### Q1 (12 Marks) [Direct from Assignment 13 Q1]
**Explain the concept of imbalanced datasets in machine learning. Discuss the causes, characteristics, challenges, and impact of class imbalance on classification algorithms. Why can classification accuracy be misleading when dealing with imbalanced data? Illustrate with a suitable numerical example.**

**Solution**:

![Classification Metrics and Confusion Matrix](images/confusion_matrix_and_metrics.svg)
*Figure 1.1: Master Classification Performance Framework: Confusion Matrix, Precision, Recall, Specificity, F1-Score, and ROC space.*

#### 1. Concept & Causes:
* **Definition**: A dataset is imbalanced when the distribution of target classes is significantly skewed (e.g., $95:5$ or $99.9:0.1$).
* **Real-World Causes**:
  - Inherent rarity of target events: Credit card fraud occurs in $<0.1\%$ of transactions.
  - Rare disease diagnosis: Cancer or rare genetic mutations appear in $<1\%$ of screened patients.
  - Fault detection & cybersecurity: Malicious intrusion packets are rare anomalies among petabytes of benign traffic.

#### 2. Characteristics & Algorithmic Challenges:
1. **Majority Class Bias**: Standard loss functions (e.g., Mean Squared Error, Cross-Entropy) assume equal misclassification costs. The optimizer pushes the decision boundary toward the minority class to minimize aggregate loss.
2. **Treating Minority as Noise**: Algorithms like Decision Trees or SVMs with soft margins often treat isolated minority samples as outliers or noise and prune them away.
3. **Small Sample Size Problem**: The absolute number of minority instances is often too small for the algorithm to extract generalizable patterns, causing extreme variance.

#### 3. The Accuracy Paradox (Numerical Proof):
Consider a cancer screening dataset with $1,000$ patient test samples:
* **Actual Distribution**: $990$ Benign (Negative) and $10$ Malignant (Positive).
* **The Dummy Classifier**: A degenerate model that always predicts **Negative (Benign)** for every patient without looking at feature inputs.
* **Confusion Matrix**:
  - $TP = 0, \quad FN = 10, \quad FP = 0, \quad TN = 990$
* **Performance Calculation**:
  $$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} = \frac{0 + 990}{1000} = \mathbf{99.0\%}$$
  $$\text{Recall (Sensitivity)} = \frac{TP}{TP + FN} = \frac{0}{0 + 10} = \mathbf{0.0\%}$$
  $$\text{Precision} = \frac{TP}{TP + FP} = \frac{0}{0 + 0} = \mathbf{\text{Undefined (or 0)}}$$
* **Why Accuracy is Catastrophically Deceptive**:
  - Despite achieving an apparently stellar **99% accuracy**, this classifier sends **all 10 cancer patients home undiagnosed**, resulting in medical fatalities!
  - **Verdict**: In imbalanced problems, accuracy is meaningless. Performance **must** be evaluated using **Recall**, **Precision**, **F1-Score**, and **PR-AUC (Precision-Recall Area Under Curve)**.

---

### Q2 (12 Marks) [Direct from Assignment 13 Q2]
**Explain the complete working mechanism of SMOTE (Synthetic Minority Over-sampling Technique) with an example. How are minority-class samples selected, nearest neighbors identified, and synthetic samples generated? Discuss the role of interpolation in creating new minority observations.**

**Solution**:

![SMOTE Synthetic Sample Interpolation](images/smote_synthetic_interpolation.svg)
*Figure 1.2: SMOTE geometric synthesis mechanism along the line segment connecting seed point x_i to neighbor x_zi.*

#### 1. Step-by-Step SMOTE Algorithm:
* **Step 1: Minority Selection**: Let $S_{\text{min}}$ be the set of all minority class instances. Iterate through each sample $\mathbf{x}_i \in S_{\text{min}}$.
* **Step 2: $k$-Nearest Neighbors Search**:
  - Compute Euclidean distances from $\mathbf{x}_i$ to all other points $\mathbf{x}_j \in S_{\text{min}}$:
    $$d(\mathbf{x}_i, \mathbf{x}_j) = \sqrt{\sum_{m=1}^D (x_{im} - x_{jm})^2}$$
  - Identify the $k$ closest minority neighbors (standard default is $k = 5$).
* **Step 3: Random Neighbor Selection**:
  - Randomly select one neighbor $\mathbf{x}_{zi}$ from the identified $k$-nearest neighbors.
* **Step 4: Linear Feature Space Interpolation**:
  - Compute the difference vector: $\mathbf{\Delta} = \mathbf{x}_{zi} - \mathbf{x}_i$.
  - Multiply by a random uniform scalar $\lambda \sim \mathcal{U}(0, 1)$.
  - The new synthetic sample is synthesized as:
    $$\mathbf{x}_{\text{new}} = \mathbf{x}_i + \lambda \cdot (\mathbf{x}_{zi} - \mathbf{x}_i)$$

#### 2. Concrete Coordinate Example:
* Given minority seed sample: $\mathbf{x}_i = [2.0, 4.0]$.
* Identified $k$-NN neighbor: $\mathbf{x}_{zi} = [6.0, 10.0]$.
* Randomly drawn interpolation factor: $\lambda = 0.5$ (exact midpoint).
* **Synthetic Instance Calculation**:
  $$\begin{aligned}
  \mathbf{x}_{\text{new}} &= [2.0, 4.0] + 0.5 \cdot ([6.0, 10.0] - [2.0, 4.0]) \\
                          &= [2.0, 4.0] + 0.5 \cdot [4.0, 6.0] \\
                          &= [2.0, 4.0] + [2.0, 3.0] = \mathbf{[4.0, 7.0]}
  \end{aligned}$$
* The new point $[4.0, 7.0]$ is assigned to the minority class and added to the training set.

#### 3. Role of Interpolation in Generalization:
* **Convex Combination**: Rather than replicating identical coordinate duplicates, interpolation generates new samples strictly within the convex hull of existing minority observations.
* **Decision Boundary Expansion**: It forces the classifier to establish a continuous, broadened decision region around the minority class rather than isolated, memorized data points.

---

### Q3 (8 Marks) [Direct from Assignment 13 Q3]
**Compare Random Oversampling and SMOTE for handling class imbalance. Detail how both methods increase minority representation, their differences, and their advantages and disadvantages.**

**Solution**:

| Comparison Dimension | Random Oversampling (ROS) | SMOTE (Synthetic Minority Over-sampling) |
|:---|:---|:---|
| **Underlying Mechanism** | Duplicates existing minority instances at random with replacement. | Generates novel, synthetic instances via feature-space linear interpolation. |
| **Feature Space Impact** | Increases point density at identical existing coordinates; creates zero new volume. | Fills the feature space along line segments between neighbors; expands minority volume. |
| **Risk of Overfitting** | **Extremely High**: Classifiers (especially decision trees) memorize exact points and create tight, overfitted rules. | **Low**: Introduces realistic feature variability that acts as an implicit regularizer. |
| **Susceptibility to Noise** | High: Replicates noisy outliers, amplifying their negative influence. | Moderate: If a minority outlier is chosen, synthetic points can bridge into majority regions (mitigated by Borderline-SMOTE). |
| **Computational Complexity** | $O(N)$ (Instantaneous random selection). | $O(N^2 \cdot D)$ (Requires all-pairs Euclidean distance calculations for $k$-NN). |
| **Suitability** | Fast baseline on small datasets. | Production standard for tabular machine learning with continuous features. |

---

### Q4 (8 Marks) [Direct from Assignment 14]
**Investigate a modern machine learning technology trend that has a significant impact on modern business innovations.**

**Solution**:

#### Technology Trend: Enterprise Retrieval-Augmented Generation (RAG) with Vector Databases
1. **Core Problem in Modern Business**:
   - Modern enterprises possess massive volumes of unstructured proprietary knowledge (internal PDFs, compliance manuals, financial audits, code repositories).
   - Standard foundation LLMs cannot access private enterprise data and are prone to hallucinations when answering domain-specific queries.
2. **The RAG Architecture & Mechanism**:
   - **Chunking & Embedding**: Proprietary corporate documents are split into semantic chunks and mapped into dense vector embeddings using models like `text-embedding-3`.
   - **Vector Storage**: Stored in high-throughput vector databases (Pinecone, Milvus, Qdrant) using HNSW (Hierarchical Navigable Small World) indexing.
   - **Hybrid Retrieval**: When a query arrives, the system computes cosine similarity to retrieve top-$k$ relevant factual context chunks.
   - **Grounded Generation**: The retrieved context is passed alongside the user query to an LLM, constraining the response strictly to verified corporate data.
3. **Business Innovations & ROI**:
   - **Legal & Contract Auditing**: Reduces NDA and contract review time from 3 weeks to under 30 seconds with cited source clauses.
   - **Autonomous Support**: Replaces static rule-based chatbots with agents capable of resolving complex technical issues with 99.5% factual accuracy.
   - **Elimination of Fine-Tuning Costs**: Avoids multi-million-dollar model pretraining while keeping private knowledge real-time and up-to-date.

---

# ⚡ TIER 2: GUARANTEED EXAM NUMERICALS (50+ MARKS)
*(Master these step-by-step arithmetic traces tonight!)*

---

### Q5 (12 Marks) [Guaranteed Unit 2 Numerical: ID3 Decision Tree Root Selection]
**Given the following 14-sample training dataset for predicting whether to play tennis (`Play = Yes/No`), compute the Entropy $H(S)$ of the target class and determine whether `Outlook` or `Wind` should be selected as the root attribute using Information Gain.**

| Day | Outlook | Temperature | Humidity | Wind | Play Tennis |
|:---:|:---:|:---:|:---:|:---:|:---:|
| D1 | Sunny | Hot | High | Weak | No |
| D2 | Sunny | Hot | High | Strong | No |
| D3 | Overcast | Hot | High | Weak | Yes |
| D4 | Rain | Mild | High | Weak | Yes |
| D5 | Rain | Cool | Normal | Weak | Yes |
| D6 | Rain | Cool | Normal | Strong | No |
| D7 | Overcast | Cool | Normal | Strong | Yes |
| D8 | Sunny | Mild | High | Weak | No |
| D9 | Sunny | Cool | Normal | Weak | Yes |
| D10 | Rain | Mild | Normal | Weak | Yes |
| D11 | Sunny | Mild | Normal | Strong | Yes |
| D12 | Overcast | Mild | High | Strong | Yes |
| D13 | Overcast | Hot | Normal | Weak | Yes |
| D14 | Rain | Mild | High | Strong | No |

**Solution**:

![Decision Tree Entropy and Information Gain](images/decision_tree_entropy_split.svg)
*Figure 2.1: Entropy curve H(p) and attribute split Information Gain derivation.*

#### Step 1: Overall Entropy of Target Class $S$
Total instances $N = 14$: Positive ($p = 9$, `Yes`), Negative ($n = 5$, `No`).
$$\begin{aligned}
H(S) &= - p_+ \log_2(p_+) - p_- \log_2(p_-) \\
     &= - \left(\frac{9}{14}\right) \log_2\left(\frac{9}{14}\right) - \left(\frac{5}{14}\right) \log_2\left(\frac{5}{14}\right) \\
     &= - (0.6429)(-0.6374) - (0.3571)(-1.4854) \\
     &= 0.4098 + 0.5305 = \mathbf{0.9403 \text{ bits}}
\end{aligned}$$

#### Step 2: Information Gain for Attribute `Wind`
`Wind` has two values: `Weak` (8 instances) and `Strong` (6 instances).
- **For `Wind = Weak`** (8 instances: 6 Yes, 2 No):
  $$H(S_{\text{Weak}}) = - \frac{6}{8} \log_2\left(\frac{6}{8}\right) - \frac{2}{8} \log_2\left(\frac{2}{8}\right) = - 0.75(-0.4150) - 0.25(-2.000) = 0.3113 + 0.5000 = \mathbf{0.8113}$$
- **For `Wind = Strong`** (6 instances: 3 Yes, 3 No):
  $$H(S_{\text{Strong}}) = - \frac{3}{6} \log_2\left(\frac{3}{6}\right) - \frac{3}{6} \log_2\left(\frac{3}{6}\right) = - 0.5(-1) - 0.5(-1) = \mathbf{1.0000}$$
- **Expected Entropy**:
  $$E(S, \text{Wind}) = \frac{8}{14} H(S_{\text{Weak}}) + \frac{6}{14} H(S_{\text{Strong}}) = \frac{8}{14}(0.8113) + \frac{6}{14}(1.0000) = 0.4636 + 0.4286 = \mathbf{0.8922}$$
- **Information Gain**:
  $$\text{Gain}(S, \text{Wind}) = H(S) - E(S, \text{Wind}) = 0.9403 - 0.8922 = \mathbf{0.0481 \text{ bits}}$$

#### Step 3: Information Gain for Attribute `Outlook`
`Outlook` has three values: `Sunny` (5), `Overcast` (4), `Rain` (5).
- **`Outlook = Sunny`** (5 instances: 2 Yes, 3 No):
  $$H(S_{\text{Sunny}}) = - \frac{2}{5} \log_2(0.4) - \frac{3}{5} \log_2(0.6) = - 0.4(-1.3219) - 0.6(-0.7370) = 0.5288 + 0.4422 = \mathbf{0.9710}$$
- **`Outlook = Overcast`** (4 instances: 4 Yes, 0 No) $\implies$ Completely pure!
  $$H(S_{\text{Overcast}}) = \mathbf{0.0000}$$
- **`Outlook = Rain`** (5 instances: 3 Yes, 2 No):
  $$H(S_{\text{Rain}}) = - \frac{3}{5} \log_2(0.6) - \frac{2}{5} \log_2(0.4) = \mathbf{0.9710}$$
- **Expected Entropy**:
  $$E(S, \text{Outlook}) = \frac{5}{14}(0.9710) + \frac{4}{14}(0) + \frac{5}{14}(0.9710) = \frac{10}{14}(0.9710) = \mathbf{0.6936}$$
- **Information Gain**:
  $$\text{Gain}(S, \text{Outlook}) = H(S) - E(S, \text{Outlook}) = 0.9403 - 0.6936 = \mathbf{0.2467 \text{ bits}}$$

#### Step 4: Root Node Selection Decision
Comparing the Information Gains:
$$\text{Gain}(S, \text{Outlook}) = 0.2467 > \text{Gain}(S, \text{Wind}) = 0.0481$$
$\therefore$ **`Outlook` is selected as the Root Attribute** because it produces the highest reduction in impurity!

---

### Q6 (12 Marks) [Guaranteed Unit 3 Numerical: AdaBoost Classifier Weight Updates]
**Apply AdaBoost to a dataset with 5 samples. Initial weights are $w_i = 0.20$. In round 1, classifier $h_1$ misclassifies sample 2 and sample 4. Calculate error $\epsilon_1$, voting weight $\alpha_1$, and the updated normalized weights $w_i^{(2)}$.**

**Solution**:

![AdaBoost Sequential Ensemble Architecture](images/adaboost_sequential_architecture.svg)
*Figure 2.2: AdaBoost sequential ensemble reweighting mechanism: misclassified samples grow in weight while correctly classified samples shrink.*

#### 1. Weighted Error $\epsilon_1$:
$$\epsilon_1 = \sum_{h_1(x_i) \ne y_i} w_i = w_2 + w_4 = 0.20 + 0.20 = \mathbf{0.40}$$

#### 2. Classifier Voting Weight $\alpha_1$:
$$\alpha_1 = \frac{1}{2} \ln \left( \frac{1 - \epsilon_1}{\epsilon_1} \right) = \frac{1}{2} \ln \left( \frac{0.60}{0.40} \right) = \frac{1}{2} \ln(1.50) = \frac{1}{2} (0.4055) = \mathbf{0.2027}$$

#### 3. Weight Multipliers:
* For misclassified samples ($i = 2, 4$):
  $$\text{Multiplier} = \exp(+\alpha_1) = \exp(0.2027) = \mathbf{1.2247}$$
* For correctly classified samples ($i = 1, 3, 5$):
  $$\text{Multiplier} = \exp(-\alpha_1) = \exp(-0.2027) = \mathbf{0.8165}$$

#### 4. Unnormalized Weights $w_i'$:
* $w_1' = 0.20 \times 0.8165 = 0.1633$
* $w_2' = 0.20 \times 1.2247 = 0.2449$
* $w_3' = 0.20 \times 0.8165 = 0.1633$
* $w_4' = 0.20 \times 1.2247 = 0.2449$
* $w_5' = 0.20 \times 0.8165 = 0.1633$
* **Normalization Factor $Z_1$**:
  $$Z_1 = 3(0.1633) + 2(0.2449) = 0.4899 + 0.4898 = \mathbf{0.9797}$$

#### 5. Normalized Weights $w_i^{(2)} = w_i' / Z_1$:
* $w_1^{(2)} = w_3^{(2)} = w_5^{(2)} = \frac{0.1633}{0.9797} = \mathbf{0.1667}$
* $w_2^{(2)} = w_4^{(2)} = \frac{0.2449}{0.9797} = \mathbf{0.2500}$
* *(Check: $3 \times 0.1667 + 2 \times 0.2500 = 0.5001 + 0.5000 = 1.00$. Exact!).*

---

### Q7 (12 Marks) [Guaranteed Unit 4 Numerical: Naïve Bayes Classification]
**Classify a new sample $X = (\text{Outlook=Rainy, Humidity=High})$ using Naïve Bayes on the dataset:**  
* `Play=Yes` (9 instances): `Outlook=Rainy` (3/9), `Humidity=High` (3/9).  
* `Play=No` (5 instances): `Outlook=Rainy` (2/5), `Humidity=High` (4/5).  
**Show all prior, likelihood, and posterior probability calculations.**

**Solution**:

![Probabilistic Learning: Naive Bayes vs BBN](images/bayes_naive_and_bbn.svg)
*Figure 2.3: Naive Bayes conditional independence structure vs Bayesian Belief Network (DAG with conditional probability distributions).*

#### 1. Prior Probabilities:
* $P(\text{Play=Yes}) = \frac{9}{14} \approx 0.6429$
* $P(\text{Play=No}) = \frac{5}{14} \approx 0.3571$

#### 2. Class-Conditional Likelihoods:
* **For `Play=Yes`**:
  $$P(\text{Rainy} \mid \text{Yes}) = \frac{3}{9} = \frac{1}{3} \approx 0.3333$$
  $$P(\text{High} \mid \text{Yes}) = \frac{3}{9} = \frac{1}{3} \approx 0.3333$$
  $$\text{Joint Likelihood } P(X \mid \text{Yes}) = 0.3333 \times 0.3333 = \mathbf{0.1111}$$
* **For `Play=No`**:
  $$P(\text{Rainy} \mid \text{No}) = \frac{2}{5} = 0.4000$$
  $$P(\text{High} \mid \text{No}) = \frac{4}{5} = 0.8000$$
  $$\text{Joint Likelihood } P(X \mid \text{No}) = 0.4000 \times 0.8000 = \mathbf{0.3200}$$

#### 3. Posterior Numerators ($P(C) \times P(X \mid C)$):
* $\text{Score}(\text{Yes}) = 0.6429 \times 0.1111 = \mathbf{0.0714}$
* $\text{Score}(\text{No}) = 0.3571 \times 0.3200 = \mathbf{0.1143}$

#### 4. Normalized Posteriors:
* Evidence $P(X) = 0.0714 + 0.1143 = 0.1857$.
* $P(\text{Yes} \mid X) = \frac{0.0714}{0.1857} = \mathbf{38.45\%}$
* $P(\text{No} \mid X) = \frac{0.1143}{0.1857} = \mathbf{61.55\%}$

#### 5. Classification Decision:
Since $P(\text{No} \mid X) > P(\text{Yes} \mid X)$, the predicted class is **`Play = No`**.

---

### Q8 (12 Marks) [Guaranteed Unit 4 Numerical: Apriori Frequent Itemset Mining]
**A transaction database contains the following 5 transactions. Set minimum support count $\text{min\_sup} = 2$ ($40\%$) and minimum confidence $\text{min\_conf} = 70\%$. Find all frequent itemsets using the Apriori algorithm and generate all valid association rules.**

| TID | Items Purchased |
|:---:|:---|
| T100 | {Bread, Milk} |
| T200 | {Bread, Diaper, Beer, Eggs} |
| T300 | {Milk, Diaper, Beer, Coke} |
| T400 | {Bread, Milk, Diaper, Beer} |
| T500 | {Bread, Milk, Diaper, Coke} |

**Solution**:

#### Step 1: Frequent 1-Itemsets ($L_1$)
* Count support of all single items:
  - {Bread}: 4 $\ge 2$
  - {Milk}: 4 $\ge 2$
  - {Diaper}: 4 $\ge 2$
  - {Beer}: 3 $\ge 2$
  - {Coke}: 2 $\ge 2$
  - {Eggs}: 1 $< 2$ $\implies$ **Pruned!**
* **$L_1$**: `{Bread: 4}, {Milk: 4}, {Diaper: 4}, {Beer: 3}, {Coke: 2}`

#### Step 2: Frequent 2-Itemsets ($L_2$)
Generate candidate pairs from $L_1$ and scan database:
* {Bread, Milk}: T100, T400, T500 $\implies$ Count = **3** (Frequent)
* {Bread, Diaper}: T200, T400, T500 $\implies$ Count = **3** (Frequent)
* {Bread, Beer}: T200, T400 $\implies$ Count = **2** (Frequent)
* {Bread, Coke}: T500 $\implies$ Count = 1 ($<2$, Pruned)
* {Milk, Diaper}: T300, T400, T500 $\implies$ Count = **3** (Frequent)
* {Milk, Beer}: T300, T400 $\implies$ Count = **2** (Frequent)
* {Milk, Coke}: T300, T500 $\implies$ Count = **2** (Frequent)
* {Diaper, Beer}: T200, T300, T400 $\implies$ Count = **3** (Frequent)
* {Diaper, Coke}: T300, T500 $\implies$ Count = **2** (Frequent)
* {Beer, Coke}: T300 $\implies$ Count = 1 ($<2$, Pruned)
* **$L_2$**: `{Bread, Milk: 3}, {Bread, Diaper: 3}, {Bread, Beer: 2}, {Milk, Diaper: 3}, {Milk, Beer: 2}, {Milk, Coke: 2}, {Diaper, Beer: 3}, {Diaper, Coke: 2}`

#### Step 3: Frequent 3-Itemsets ($L_3$)
Join $L_2$ pairs and prune non-frequent subsets:
* `{Bread, Diaper, Beer}`: Count in DB (T200, T400) = **2** $\ge 2$.
* `{Bread, Milk, Diaper}`: Count in DB (T400, T500) = **2** $\ge 2$.
* `{Milk, Diaper, Beer}`: Count in DB (T300, T400) = **2** $\ge 2$.
* `{Milk, Diaper, Coke}`: Count in DB (T300, T500) = **2** $\ge 2$.
* **$L_3$**: `{Bread, Diaper, Beer: 2}, {Bread, Milk, Diaper: 2}, {Milk, Diaper, Beer: 2}, {Milk, Diaper, Coke: 2}`

#### Step 4: Association Rule Generation ($\text{min\_conf} \ge 70\%$):
1. From `{Beer, Diaper}` (Beer count = 3, joint count = 3):
   $$\text{Conf}(\text{Beer} \to \text{Diaper}) = \frac{3}{3} = \mathbf{100\%} \quad (\mathbf{VALID!})$$
2. From `{Coke, Diaper}` (Coke count = 2, joint count = 2):
   $$\text{Conf}(\text{Coke} \to \text{Diaper}) = \frac{2}{2} = \mathbf{100\%} \quad (\mathbf{VALID!})$$
3. From `{Coke, Milk}` (Coke count = 2, joint count = 2):
   $$\text{Conf}(\text{Coke} \to \text{Milk}) = \frac{2}{2} = \mathbf{100\%} \quad (\mathbf{VALID!})$$

---

### Q9 (8 Marks) [Guaranteed Unit 3: K-Means Algorithm & K-Means++]
**Explain the K-Means clustering algorithm. What is K-Means++ and how does it prevent poor local minima?**

**Solution**:

![K-Means Clustering Iterative Convergence](images/kmeans_clustering_iterations.svg)
*Figure 2.4: K-Means iterative convergence (Lloyd's algorithm): Centroid initialization, Voronoi partitioning, and mean shifting.*

#### 1. K-Means Algorithm (Lloyd's Alternating Optimization):
* **Objective Function**: Minimize Within-Cluster Sum of Squares (WCSS):
  $$J = \sum_{k=1}^K \sum_{\mathbf{x}_i \in C_k} \|\mathbf{x}_i - \mathbf{\mu}_k\|^2$$
* **Alternating Steps**:
  1. **Assignment Step**: Assign each data point $\mathbf{x}_i$ to its nearest centroid:
     $$C^{(t)}(i) = \arg\min_k \|\mathbf{x}_i - \mathbf{\mu}_k^{(t)}\|^2$$
  2. **Update Step**: Recompute the centroid as the center of gravity of all assigned points:
     $$\mathbf{\mu}_k^{(t+1)} = \frac{1}{|C_k|} \sum_{\mathbf{x} \in C_k} \mathbf{x}$$
  3. **Convergence**: Repeat until centroids do not shift ($\mathbf{\mu}^{(t+1)} = \mathbf{\mu}^{(t)}$).

#### 2. K-Means++ Initialization:
* **The Problem**: Standard K-Means picks initial centroids uniformly at random, which frequently places multiple centroids inside the same natural cluster, resulting in poor sub-optimal local minima.
* **The K-Means++ Fix**:
  1. Select the 1st centroid $\mathbf{\mu}_1$ uniformly at random from the dataset.
  2. For each remaining data point $\mathbf{x}$, compute $D(\mathbf{x})$, the distance to the closest already chosen centroid.
  3. Choose the next centroid $\mathbf{\mu}_k$ with probability proportional to $D(\mathbf{x})^2$:
     $$P(\mathbf{x}) = \frac{D(\mathbf{x})^2}{\sum_{\mathbf{x}'} D(\mathbf{x}')^2}$$
  4. Repeat until $K$ centroids are chosen.
* **Benefit**: Ensures initial centroids are well-dispersed across the feature space, guaranteeing $O(\log K)$-competitive approximations to optimal clustering.

---

### Q10 (10 Marks) [Guaranteed Unit 3: Agglomerative Hierarchical Clustering (AGNES)]
**Given five 1D data points $P_1 = 2, P_2 = 5, P_3 = 9, P_4 = 15, P_5 = 25$, trace the Agglomerative Hierarchical Clustering (AGNES) procedure using Single Linkage. Construct the distance matrix at each step and draw the resulting dendrogram.**

**Solution**:

#### Step 1: Initial Distance Matrix $D_0$ ($5 \times 5$)
Using Euclidean distance $d(x_i, x_j) = |x_i - x_j|$:

| | $P_1(2)$ | $P_2(5)$ | $P_3(9)$ | $P_4(15)$ | $P_5(25)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$P_1(2)$** | 0 | 3 | 7 | 13 | 23 |
| **$P_2(5)$** | 3 | 0 | 4 | 10 | 20 |
| **$P_3(9)$** | 7 | 4 | 0 | 6 | 16 |
| **$P_4(15)$** | 13 | 10 | 6 | 0 | 10 |
| **$P_5(25)$** | 23 | 20 | 16 | 10 | 0 |

* **Minimum Distance**: $d(P_1, P_2) = \mathbf{3}$.
* **Action**: Merge $P_1$ and $P_2$ into cluster **$(P_1 P_2)$** at distance $h = 3$.

#### Step 2: Distance Matrix $D_1$ ($4 \times 4$)
Under Single Linkage, $d(A, B) = \min_{a \in A, b \in B} d(a, b)$:
- $d((P_1 P_2), P_3) = \min(7, 4) = \mathbf{4}$.
- $d((P_1 P_2), P_4) = \min(13, 10) = \mathbf{10}$.
- $d((P_1 P_2), P_5) = \min(23, 20) = \mathbf{20}$.

| | $(P_1 P_2)$ | $P_3$ | $P_4$ | $P_5$ |
|:---:|:---:|:---:|:---:|:---:|
| **$(P_1 P_2)$** | 0 | **4** | 10 | 20 |
| **$P_3$** | 4 | 0 | 6 | 16 |
| **$P_4$** | 10 | 6 | 0 | 10 |
| **$P_5$** | 20 | 16 | 10 | 0 |

* **Minimum Distance**: $d((P_1 P_2), P_3) = \mathbf{4}$.
* **Action**: Merge $(P_1 P_2)$ and $P_3$ into cluster **$(P_1 P_2 P_3)$** at distance $h = 4$.

#### Step 3: Distance Matrix $D_2$ ($3 \times 3$)
- $d((P_1 P_2 P_3), P_4) = \min(13, 10, 6) = \mathbf{6}$.
- $d((P_1 P_2 P_3), P_5) = \min(23, 20, 16) = \mathbf{16}$.
- $d(P_4, P_5) = |15 - 25| = \mathbf{10}$.

| | $(P_1 P_2 P_3)$ | $P_4$ | $P_5$ |
|:---:|:---:|:---:|:---:|
| **$(P_1 P_2 P_3)$** | 0 | **6** | 16 |
| **$P_4$** | 6 | 0 | 10 |
| **$P_5$** | 16 | 10 | 0 |

* **Minimum Distance**: $d((P_1 P_2 P_3), P_4) = \mathbf{6}$.
* **Action**: Merge $(P_1 P_2 P_3)$ and $P_4$ into cluster **$(P_1 P_2 P_3 P_4)$** at distance $h = 6$.

#### Step 4: Final Merge Matrix $D_3$ ($2 \times 2$)
- $d((P_1 P_2 P_3 P_4), P_5) = \min(23, 20, 16, 10) = \mathbf{10}$.
* **Action**: Merge into single root cluster **$(P_1 P_2 P_3 P_4 P_5)$** at height $h = 10$.

#### Step 5: Dendrogram Representation
```text
Height (h)
  12 |
  10 |                         ┌─────────────── P5 (25)
   8 |                         │
   6 |                 ┌───────┴─────── P4 (15)
   4 |         ┌───────┴─────── P3 (9)
   3 |     ┌───┴─── P2 (5)
   0 |──── P1 (2)
```

---

# 📐 TIER 3: CORE MATHEMATICAL DERIVATIONS & PPT TOPICS
*(Proof questions frequently selected by Dr. Nilamadhab Mishra)*

---

### Q11 (12 Marks) [Guaranteed Derivation: Principal Component Analysis (PCA)]
**Derive the first principal component in Principal Component Analysis (PCA) by maximizing variance of projected data using Lagrange Multipliers.**

**Solution**:

![PCA Variance Maximization and Orthogonal Axes](images/pca_variance_maximization.svg)
*Figure 3.1: Principal Component Analysis (PCA): Projection onto orthogonal axes maximizing projected variance along the major ellipse axis.*

#### 1. Setup:
* Given zero-mean centered dataset $\mathbf{X}_c$ of size $m \times n$.
* Covariance matrix:
  $$\mathbf{\Sigma} = \frac{1}{m} \mathbf{X}_c^T \mathbf{X}_c \quad (n \times n)$$
* Let $\mathbf{u}_1$ be a unit direction vector on which data is projected:
  $$\mathbf{u}_1^T \mathbf{u}_1 = 1$$

#### 2. Projected Data Variance:
* For data point $\mathbf{x}_i$, its scalar projection onto $\mathbf{u}_1$ is $z_i = \mathbf{x}_i^T \mathbf{u}_1$.
* The sample variance of projected points is:
  $$\sigma_z^2 = \frac{1}{m} \sum_{i=1}^m (\mathbf{x}_i^T \mathbf{u}_1)^2 = \frac{1}{m} \mathbf{u}_1^T \left( \sum_{i=1}^m \mathbf{x}_i \mathbf{x}_i^T \right) \mathbf{u}_1 = \mathbf{u}_1^T \mathbf{\Sigma} \mathbf{u}_1$$

#### 3. Constrained Optimization (Lagrangian):
$$\max_{\mathbf{u}_1} \mathbf{u}_1^T \mathbf{\Sigma} \mathbf{u}_1 \quad \text{subject to } \mathbf{u}_1^T \mathbf{u}_1 = 1$$
Formulate the Lagrangian using multiplier $\lambda$:
$$\mathcal{L}(\mathbf{u}_1, \lambda) = \mathbf{u}_1^T \mathbf{\Sigma} \mathbf{u}_1 - \lambda (\mathbf{u}_1^T \mathbf{u}_1 - 1)$$

#### 4. Setting Gradient to Zero:
$$\frac{\partial \mathcal{L}}{\partial \mathbf{u}_1} = 2 \mathbf{\Sigma} \mathbf{u}_1 - 2 \lambda \mathbf{u}_1 = 0$$
$$\mathbf{\Sigma} \mathbf{u}_1 = \lambda \mathbf{u}_1$$

#### 5. Conclusion:
* $\mathbf{u}_1$ must be an **eigenvector** of the covariance matrix $\mathbf{\Sigma}$, and $\lambda$ is its corresponding **eigenvalue**.
* The projected variance is:
  $$\sigma_z^2 = \mathbf{u}_1^T \mathbf{\Sigma} \mathbf{u}_1 = \mathbf{u}_1^T (\lambda \mathbf{u}_1) = \lambda (\mathbf{u}_1^T \mathbf{u}_1) = \lambda$$
* To maximize variance, $\mathbf{u}_1$ must be the eigenvector corresponding to the **largest eigenvalue $\lambda_{\max}$**.

---

### Q12 (12 Marks) [Guaranteed Derivation: Support Vector Machines (SVM)]
**Explain the mathematical principle of Support Vector Machines (SVM). Formulate the dual optimization problem and explain the Mercer condition for valid kernel functions.**

**Solution**:

![Support Vector Machine Hyperplane and Maximum Margin](images/svm_hyperplane_margin.svg)
*Figure 3.2: Support Vector Machine maximum margin hyperplane w^T x + b = 0, support vectors on margin boundaries w^T x + b = ±1, and margin width M = 2 / ||w||.*

#### 1. Primal Formulation:
* Linearly separable training data: $\{(\mathbf{x}_i, y_i)\}_{i=1}^m, y_i \in \{-1, +1\}$.
* Separating hyperplane: $\mathbf{w}^T \mathbf{x} + b = 0$.
* Margin boundary constraints:
  $$\mathbf{w}^T \mathbf{x}_i + b \ge +1 \quad \text{if } y_i = +1$$
  $$\mathbf{w}^T \mathbf{x}_i + b \le -1 \quad \text{if } y_i = -1$$
  Combined: $y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1, \forall i$.
* Geometric margin width: $M = \frac{2}{\|\mathbf{w}\|}$.
* Maximizing $M$ is equivalent to minimizing $\frac{1}{2} \|\mathbf{w}\|^2$:
  $$\min_{\mathbf{w}, b} \frac{1}{2} \|\mathbf{w}\|^2 \quad \text{subject to } y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1, \forall i$$

#### 2. Dual Formulation via Lagrange Multipliers:
* Construct Lagrangian with multipliers $\alpha_i \ge 0$:
  $$\mathcal{L}(\mathbf{w}, b, \mathbf{\alpha}) = \frac{1}{2} \|\mathbf{w}\|^2 - \sum_{i=1}^m \alpha_i [y_i(\mathbf{w}^T \mathbf{x}_i + b) - 1]$$
* Set partial derivatives to zero:
  $$\frac{\partial \mathcal{L}}{\partial \mathbf{w}} = \mathbf{w} - \sum_{i=1}^m \alpha_i y_i \mathbf{x}_i = 0 \implies \mathbf{w} = \sum_{i=1}^m \alpha_i y_i \mathbf{x}_i$$
  $$\frac{\partial \mathcal{L}}{\partial b} = - \sum_{i=1}^m \alpha_i y_i = 0 \implies \sum_{i=1}^m \alpha_i y_i = 0$$
* Substitute $\mathbf{w}$ and $b$ back into $\mathcal{L}$ to obtain the **Wolfe Dual**:
  $$\max_{\mathbf{\alpha}} \sum_{i=1}^m \alpha_i - \frac{1}{2} \sum_{i=1}^m \sum_{j=1}^m \alpha_i \alpha_j y_i y_j (\mathbf{x}_i^T \mathbf{x}_j)$$
  $$\text{subject to } \alpha_i \ge 0, \quad \sum_{i=1}^m \alpha_i y_i = 0$$

#### 3. Mercer's Condition for Kernel Functions:
* Non-linear mapping $\phi(\mathbf{x})$ into high-dimensional Hilbert space allows inner product computation via kernel: $K(\mathbf{x}_i, \mathbf{x}_j) = \phi(\mathbf{x}_i)^T \phi(\mathbf{x}_j)$.
* **Mercer's Theorem**: A kernel function $K(\mathbf{x}, \mathbf{z})$ is valid if and only if its Gram Matrix $K_{ij} = K(\mathbf{x}_i, \mathbf{x}_j)$ is **symmetric positive semi-definite** (all eigenvalues $\lambda_i \ge 0$) for any finite set of points.

---

### Q13 (12 Marks) [Direct from Dr. Nilamadhab Mishra Unit 4 PPT]
**(a) Formulate the Bayes Optimal Classifier. Explain why no other classification method using the same hypothesis space and prior knowledge can outperform it on average.**  
**(b) Give a concrete numeric example where the classification assigned by the Bayes Optimal Classifier differs from the Maximum A Posteriori (MAP) hypothesis.**

**Solution**:

#### 1. Formulation:
Given training data $D$ and hypothesis space $H$, the Bayes Optimal Classifier combines the predictions of all hypotheses weighted by their posterior probabilities:
$$v_{\text{BOC}} = \arg\max_{v_j \in V} \sum_{h_i \in H} P(v_j \mid h_i) P(h_i \mid D)$$

#### 2. Proof of Optimality:
* The probability of making a classification error on instance $x$ given data $D$ is $1 - P(v(x) \mid D)$.
* To minimize error, one must maximize $P(v(x) \mid D) = \sum_{h \in H} P(v(x) \mid h) P(h \mid D)$.
* The Bayes Optimal Classifier selects the class value that directly maximizes this exact posterior sum. Therefore, no other classifier can achieve lower expected error!

#### 3. Numeric Counterexample (BOC vs MAP):
* Let $H = \{h_1, h_2, h_3\}$ with posteriors:
  $$P(h_1 \mid D) = 0.40, \quad P(h_2 \mid D) = 0.30, \quad P(h_3 \mid D) = 0.30$$
* Predictions for a query instance $x$:
  $$h_1(x) = +, \quad h_2(x) = -, \quad h_3(x) = -$$
* **MAP Prediction**:
  $$h_{\text{MAP}} = \arg\max \{0.40, 0.30, 0.30\} = h_1 \implies \mathbf{+}$$
* **Bayes Optimal Prediction**:
  $$P(+ \mid D) = P(+ \mid h_1) P(h_1 \mid D) = 1.0 \times 0.40 = \mathbf{0.40}$$
  $$P(- \mid D) = P(- \mid h_2) P(h_2 \mid D) + P(- \mid h_3) P(h_3 \mid D) = 1.0(0.30) + 1.0(0.30) = \mathbf{0.60}$$
  $$\arg\max \{0.40, 0.60\} = \mathbf{-}$$
* **Result**: MAP predicts $+$ with only $40\%$ posterior probability, whereas Bayes Optimal correctly outputs $-$ with $60\%$ majority confidence!

---

### Q14 (10 Marks) [Direct from Dr. Nilamadhab Mishra Unit 4 PPT]
**(a) What is High Utility Itemset Mining (HUIM)? How does it overcome the limitations of standard Frequent Itemset Mining?**  
**(b) Explain why the Apriori downward closure property fails for itemset utility and how Transaction-Weighted Utilization (TWU) restores pruning efficiency.**

**Solution**:

#### 1. Limitations of Frequent Itemset Mining:
* Standard Apriori/FP-Growth treat all items equally: a high-margin item (e.g., diamond ring) that sells rarely is discarded as "infrequent," while low-margin items (e.g., matchboxes) dominate the output.
* HUIM incorporates **external utility** $p(i)$ (unit profit) and **internal utility** $q(i, t)$ (quantity purchased in basket $t$). An itemset is high-utility if total profit $u(X) \ge \text{min\_util}$.

#### 2. Downward Closure Failure in Utility:
* In frequency mining: $X \subseteq Y \implies \text{Support}(X) \ge \text{Support}(Y)$ (anti-monotonic).
* In utility mining: Adding an item $Y$ to $X$ adds positive profit: $u(X \cup Y, t) = u(X, t) + u(Y, t) \ge u(X, t)$. Thus, a low-utility item can combine with others to become high utility! Direct subset pruning fails.

#### 3. Transaction-Weighted Utilization (TWU) Solution:
* Let Transaction Utility $TU(t) = \sum_{i \in t} u(i, t)$ (total spend of entire basket $t$).
* Define $\text{TWU}(X) = \sum_{t \supseteq X} TU(t)$ (sum of total basket values for all baskets containing $X$).
* **TWU Monotonicity**: Any superset $X \cup Y$ appears in a subset of transactions where $X$ appears:
  $$\text{TWU}(X \cup Y) \le \text{TWU}(X)$$
* If $\text{TWU}(X) < \text{min\_util}$, no superset of $X$ can ever be high utility. Candidates are safely pruned!

---

# 📊 TIER 4: LEARNING THEORY & CONCEPTUAL COMPARISONS

---

### Q15 (8 Marks) [Section B Model]
**Compare Linear Regression and Logistic Regression with respect to hypothesis, output range, cost function, and decision boundary.**

**Solution**:

| Dimension | Linear Regression | Logistic Regression |
|:---|:---|:---|
| **Target Output** | Continuous real values ($y \in \mathbb{R}$) | Discrete binary classification ($y \in \{0, 1\}$) |
| **Hypothesis Function** | $h_\theta(x) = \mathbf{\theta}^T \mathbf{x}$ | $h_\theta(x) = \sigma(\mathbf{\theta}^T \mathbf{x}) = \frac{1}{1 + e^{-\mathbf{\theta}^T \mathbf{x}}}$ |
| **Output Range** | $(-\infty, +\infty)$ | $[0, 1]$ (Interpreted as probability $P(y=1 \mid x)$) |
| **Cost Function** | Mean Squared Error (MSE, Convex):<br>$J(\theta) = \frac{1}{2m} \sum (h_\theta(x^{(i)}) - y^{(i)})^2$ | Binary Cross-Entropy Loss (Convex):<br>$J(\theta) = - \frac{1}{m} \sum [y \ln h + (1-y) \ln(1-h)]$ |
| **Decision Rule** | Predict continuous scalar output | Threshold at $h_\theta(x) \ge 0.5 \iff \mathbf{\theta}^T \mathbf{x} \ge 0$ |

---

### Q16 (12 Marks) [Section A Model]
**(a) Trace the Find-S algorithm on the following dataset to find the most specific hypothesis for `EnjoySport`:**  
1. `(Sunny, Warm, Normal, Strong, Warm, Same)` $\implies$ **Yes**  
2. `(Sunny, Warm, High, Strong, Warm, Same)` $\implies$ **Yes**  
3. `(Rainy, Cold, High, Strong, Warm, Change)` $\implies$ **No**  
4. `(Sunny, Warm, High, Strong, Cool, Change)` $\implies$ **Yes**  
**(b) Define PAC Learnability. What is sample complexity?**

**Solution**:
1. **Find-S Trace**:
   - Initial hypothesis: $h_0 = \langle \Phi, \Phi, \Phi, \Phi, \Phi, \Phi \rangle$.
   - Example 1 (+): $h_1 = \langle \text{Sunny, Warm, Normal, Strong, Warm, Same} \rangle$.
   - Example 2 (+): $h_2 = \langle \text{Sunny, Warm, ?, Strong, Warm, Same} \rangle$ (`Humidity` generalized).
   - Example 3 (-): Negative example $\implies$ Ignored by Find-S! $h_3 = h_2$.
   - Example 4 (+): `(Sunny, Warm, High, Strong, Cool, Change)`.
     - `Water`: `Warm` vs `Cool` $\implies$ Generalize to `?`.
     - `Forecast`: `Same` vs `Change` $\implies$ Generalize to `?`.
     - $h_4 = \langle \mathbf{\text{Sunny, Warm, ?, Strong, ?, ?}} \rangle$.
   - **Final Hypothesis**: $\mathbf{h = \langle \text{Sunny, Warm, ?, Strong, ?, ?} \rangle}$.
2. **PAC Learnability**:
   - A concept class $C$ is Probably Approximately Correct (PAC) learnable if learner outputs hypothesis $h$ with error $\le \epsilon$ with probability $\ge 1 - \delta$ in polynomial time.
   - **Sample Complexity** formula:
     $$m \ge \frac{1}{\epsilon} \left( \ln |H| + \ln \frac{1}{\delta} \right)$$

---

### Q17 (8 Marks) [Section B Model]
**Explain the concept of VC Dimension. What is the VC dimension of a set of 1D intervals? Prove your answer.**

**Solution**:
1. **Definition**: The Vapnik-Chervonenkis (VC) dimension of hypothesis class $H$ is the cardinality of the largest set of points that can be **shattered** (every possible $2^N$ binary labeling realized) by $H$.
2. **VC Dimension of 1D Intervals $[a, b]$ on the Real Line**:
   - **Can shatter 2 points**: For two points $x_1 < x_2$, all 4 dichotomies $(--, -+, +-, ++)$ can be captured by an interval.
   - **Cannot shatter 3 points**: For points $x_1 < x_2 < x_3$, consider the labeling where $x_1 = +, x_2 = -, x_3 = +$. Any single continuous interval $[a, b]$ that encloses both $x_1$ and $x_3$ must also enclose the intermediate point $x_2$, forcing $x_2$ to be positive. Thus, the labeling $(+, -, +)$ is impossible to realize.
   - $\therefore \mathbf{VC(\text{1D Intervals}) = 2}$.

---

### Q18 (8 Marks) [Section B Model]
**Explain the FP-Growth algorithm. Why is FP-Growth faster than the Apriori algorithm?**

**Solution**:
1. **Core Mechanism**:
   - Compresses the transaction database into a compact **FP-Tree (Frequent Pattern Tree)** with linked header tables.
   - Mines frequent patterns recursively using **Conditional Pattern Bases** and **Conditional FP-Trees** in a divide-and-conquer manner.
2. **Key Advantages over Apriori**:
   - **Database Scans**: Apriori requires $k$ full database passes for itemsets of length $k$. FP-Growth scans the physical database **only twice** regardless of pattern length.
   - **No Candidate Generation**: Apriori generates up to $2^N$ candidate sets through expensive joins and subset tests. FP-Growth completely eliminates candidate generation.
   - **Memory Efficiency**: Shared prefixes compress duplicate transactions into common tree branches.
"""

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully reordered {OUT_PATH} into priority-ranked format!")
