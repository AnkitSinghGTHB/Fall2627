"""
update_ml_guide.py
Updates 07-ml-fat-high-frequency-exam-question-bank.md:
1. Embeds all 8 SVG diagrams at the exact relevant questions.
2. Adds Q16 (ID3 Entropy/Gain Numerical), Q17 (Apriori Itemset Mining Trace), Q18 (Hierarchical Clustering AGNES Trace).
"""

import os
import shutil

QB_PATH = r"c:\Users\ankit\Fall2627\ML\notes\term_end\07-ml-fat-high-frequency-exam-question-bank.md"
BACKUP_PATH = r"c:\Users\ankit\Fall2627\ML\notes\term_end\07-ml-fat-high-frequency-exam-question-bank.backup.md"

shutil.copy2(QB_PATH, BACKUP_PATH)

with open(QB_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Embed SVM image in Q3
old_q3 = "**Solution**:\n1. **Primal Formulation**:"
new_q3 = """**Solution**:

![Support Vector Machine Hyperplane and Maximum Margin](images/svm_hyperplane_margin.svg)
*Figure 2.1: Support Vector Machine maximum margin hyperplane w^T x + b = 0, support vectors on margin boundaries w^T x + b = ±1, and margin width M = 2 / ||w||.*

1. **Primal Formulation**:"""
if old_q3 in text:
    text = text.replace(old_q3, new_q3, 1)

# 2. Embed AdaBoost image in Q5
old_q5 = "**Solution**:\n1. **Weighted Error $\\epsilon_1$**:"
new_q5 = """**Solution**:

![AdaBoost Sequential Ensemble Architecture](images/adaboost_sequential_architecture.svg)
*Figure 3.1: AdaBoost sequential ensemble reweighting mechanism: misclassified samples grow in weight while correctly classified samples shrink.*

1. **Weighted Error $\\epsilon_1$**:"""
if old_q5 in text:
    text = text.replace(old_q5, new_q5, 1)

# 3. Embed K-Means image in Q6
old_q6 = "**Solution**:\n1. **K-Means Algorithm**:"
new_q6 = """**Solution**:

![K-Means Clustering Iterative Convergence](images/kmeans_clustering_iterations.svg)
*Figure 3.2: K-Means iterative convergence (Lloyd's algorithm): Centroid initialization, Voronoi partitioning, and mean shifting.*

1. **K-Means Algorithm**:"""
if old_q6 in text:
    text = text.replace(old_q6, new_q6, 1)

# 4. Embed Naive Bayes / BBN image in Q7
old_q7 = "**Solution**:\n1. **Prior Probabilities**:"
new_q7 = """**Solution**:

![Probabilistic Learning: Naive Bayes vs BBN](images/bayes_naive_and_bbn.svg)
*Figure 4.1: Naive Bayes conditional independence structure vs Bayesian Belief Network (DAG with conditional probability distributions).*

1. **Prior Probabilities**:"""
if old_q7 in text:
    text = text.replace(old_q7, new_q7, 1)

# 5. Embed PCA image in Q9
old_q9 = "**Solution**:\n1. **Setup**:"
new_q9 = """**Solution**:

![PCA Variance Maximization and Orthogonal Axes](images/pca_variance_maximization.svg)
*Figure 5.1: Principal Component Analysis (PCA): Projection onto orthogonal axes maximizing projected variance along the major ellipse axis.*

1. **Setup**:"""
if old_q9 in text:
    text = text.replace(old_q9, new_q9, 1)

# 6. Embed Confusion Matrix image in Q13
old_q13 = "3. **The Accuracy Paradox (Numerical Proof)**:"
new_q13 = """![Classification Metrics and Confusion Matrix](images/confusion_matrix_and_metrics.svg)
*Figure 5.2: Master Classification Performance Framework: Confusion Matrix, Precision, Recall, Specificity, F1-Score, and ROC space.*

3. **The Accuracy Paradox (Numerical Proof)**:"""
if old_q13 in text:
    text = text.replace(old_q13, new_q13, 1)

# 7. Embed SMOTE image in Q14
old_q14 = "2. **Concrete Coordinate Example**:"
new_q14 = """![SMOTE Synthetic Sample Interpolation](images/smote_synthetic_interpolation.svg)
*Figure 5.3: SMOTE geometric synthesis mechanism along the line segment connecting seed point x_i to neighbor x_zi.*

2. **Concrete Coordinate Example**:"""
if old_q14 in text:
    text = text.replace(old_q14, new_q14, 1)

# 8. Append Q16, Q17, Q18 to the document
additional_content = """---

## ADDITIONAL HIGH-YIELD GUARANTEED NUMERICALS

---

### Q16 (12 Marks) [Guaranteed Unit 2 Numerical: ID3 Decision Tree Root Selection]
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
*Figure 2.2: Entropy curve H(p) and attribute split Information Gain derivation.*

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

### Q17 (12 Marks) [Guaranteed Unit 4 Numerical: Apriori Frequent Itemset Mining]
**A transaction database contains the following 5 transactions. Set minimum support count $\text{min\_sup} = 2$ ($40\%$) and minimum confidence $\text{min\_conf} = 70\%$. Find all frequent itemsets using the Apriori algorithm and generate all valid association rules.**

| TID | Items Purchased |
|:---:|:---|
| T100 | {Bread, Milk} |
| T200 | {Bread, Diaper, Beer, Eggs} |
| T300 | {Milk, Diaper, Beer, Coke} |
| T400 | {Bread, Milk, Diaper, Beer} |
| T500 | {Bread, Milk, Diaper, Coke} |

**Solution**:

#### Step 1: Candidate 1-Itemsets ($C_1$) & Frequent 1-Itemsets ($L_1$)
- Scan database to count support of each single item:
  - {Bread}: 4 $\ge 2$
  - {Milk}: 4 $\ge 2$
  - {Diaper}: 4 $\ge 2$
  - {Beer}: 3 $\ge 2$
  - {Coke}: 2 $\ge 2$
  - {Eggs}: 1 $< 2$ $\implies$ **Pruned!**
- **$L_1$**: `{Bread: 4}, {Milk: 4}, {Diaper: 4}, {Beer: 3}, {Coke: 2}`

#### Step 2: Candidate 2-Itemsets ($C_2 = L_1 \bowtie L_1$) & Frequent 2-Itemsets ($L_2$)
Generate all pairs and count occurrences:
- {Bread, Milk}: T100, T400, T500 $\implies$ count = **3** (Frequent)
- {Bread, Diaper}: T200, T400, T500 $\implies$ count = **3** (Frequent)
- {Bread, Beer}: T200, T400 $\implies$ count = **2** (Frequent)
- {Bread, Coke}: T500 $\implies$ count = 1 ($<2$, Pruned)
- {Milk, Diaper}: T300, T400, T500 $\implies$ count = **3** (Frequent)
- {Milk, Beer}: T300, T400 $\implies$ count = **2** (Frequent)
- {Milk, Coke}: T300, T500 $\implies$ count = **2** (Frequent)
- {Diaper, Beer}: T200, T300, T400 $\implies$ count = **3** (Frequent)
- {Diaper, Coke}: T300, T500 $\implies$ count = **2** (Frequent)
- {Beer, Coke}: T300 $\implies$ count = 1 ($<2$, Pruned)
- **$L_2$**: `{Bread, Milk: 3}, {Bread, Diaper: 3}, {Bread, Beer: 2}, {Milk, Diaper: 3}, {Milk, Beer: 2}, {Milk, Coke: 2}, {Diaper, Beer: 3}, {Diaper, Coke: 2}`

#### Step 3: Candidate 3-Itemsets ($C_3 = L_2 \bowtie L_2$) & Frequent 3-Itemsets ($L_3$)
Join pairs sharing first element and prune any candidate whose 2-subsets are not in $L_2$:
- Candidate `{Bread, Diaper, Beer}`: Subsets are {Bread, Diaper}, {Bread, Beer}, {Diaper, Beer} $\to$ All in $L_2$! Count in DB: T200, T400 $\implies$ **Count = 2** $\ge 2$.
- Candidate `{Bread, Milk, Diaper}`: Subsets are {Bread, Milk}, {Bread, Diaper}, {Milk, Diaper} $\to$ All in $L_2$! Count in DB: T400, T500 $\implies$ **Count = 2** $\ge 2$.
- Candidate `{Milk, Diaper, Beer}`: Subsets are {Milk, Diaper}, {Milk, Beer}, {Diaper, Beer} $\to$ All in $L_2$! Count in DB: T300, T400 $\implies$ **Count = 2** $\ge 2$.
- Candidate `{Milk, Diaper, Coke}`: Subsets are {Milk, Diaper}, {Milk, Coke}, {Diaper, Coke} $\to$ All in $L_2$! Count in DB: T300, T500 $\implies$ **Count = 2** $\ge 2$.
- **$L_3$**: `{Bread, Diaper, Beer: 2}, {Bread, Milk, Diaper: 2}, {Milk, Diaper, Beer: 2}, {Milk, Diaper, Coke: 2}`

#### Step 4: Rule Generation & Confidence Verification ($\text{min\_conf} \ge 70\%$)
For frequent itemset `{Bread, Milk, Diaper}` (Support = 2):
1. **Rule: $\{\text{Bread, Milk}\} \to \{\text{Diaper}\}$**:
   $$\text{Confidence} = \frac{\sigma(\text{Bread, Milk, Diaper})}{\sigma(\text{Bread, Milk})} = \frac{2}{3} = \mathbf{66.7\%} \quad (\text{Rejected} < 70\%)$$
2. **Rule: $\{\text{Bread, Diaper}\} \to \{\text{Milk}\}$**:
   $$\text{Confidence} = \frac{\sigma(\text{Bread, Milk, Diaper})}{\sigma(\text{Bread, Diaper})} = \frac{2}{3} = \mathbf{66.7\%} \quad (\text{Rejected})$$
3. **Rule: $\{\text{Milk, Diaper}\} \to \{\text{Bread}\}$**:
   $$\text{Confidence} = \frac{\sigma(\text{Bread, Milk, Diaper})}{\sigma(\text{Milk, Diaper})} = \frac{2}{3} = \mathbf{66.7\%} \quad (\text{Rejected})$$
4. **Rule: $\{\text{Beer}\} \to \{\text{Diaper}\}$** (from itemset `{Diaper, Beer}` where count=3, Beer count=3):
   $$\text{Confidence} = \frac{\sigma(\text{Beer, Diaper})}{\sigma(\text{Beer})} = \frac{3}{3} = \mathbf{100\%} \quad (\mathbf{VALID!})$$
5. **Rule: $\{\text{Coke}\} \to \{\text{Diaper}\}$** (from `{Diaper, Coke}` where count=2, Coke count=2):
   $$\text{Confidence} = \frac{\sigma(\text{Diaper, Coke})}{\sigma(\text{Coke})} = \frac{2}{2} = \mathbf{100\%} \quad (\mathbf{VALID!})$$
6. **Rule: $\{\text{Coke}\} \to \{\text{Milk}\}$** (from `{Milk, Coke}` count=2, Coke count=2):
   $$\text{Confidence} = \frac{2}{2} = \mathbf{100\%} \quad (\mathbf{VALID!})$$

---

### Q18 (10 Marks) [Guaranteed Unit 3 Numerical: Agglomerative Hierarchical Clustering (AGNES)]
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
Under Single Linkage, distance between cluster $A$ and point $B$ is $\min d(a, b)$:
- $d((P_1 P_2), P_3) = \min(d(P_1, P_3), d(P_2, P_3)) = \min(7, 4) = \mathbf{4}$.
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
- $d((P_1 P_2 P_3), P_4) = \min(d(P_1, P_4), d(P_2, P_4), d(P_3, P_4)) = \min(13, 10, 6) = \mathbf{6}$.
- $d((P_1 P_2 P_3), P_5) = \min(23, 20, 16) = \mathbf{16}$.
- $d(P_4, P_5) = |15 - 25| = \mathbf{10}$.

| | $(P_1 P_2 P_3)$ | $P_4$ | $P_5$ |
|:---:|:---:|:---:|
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
- Cluster hierarchy: $[[[P_1, P_2], P_3], P_4], P_5]$.
"""

text += additional_content

with open(QB_PATH, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated 07-ml-fat-high-frequency-exam-question-bank.md successfully!")
