# 📘 Unit 4: Probabilistic Learning, Bayesian Networks & Association Mining

---

## 1. Probabilistic Classification: Naïve Bayes

### 1.1 Bayes Theorem Formulation
$$P(C_k \mid \mathbf{X}) = \frac{P(\mathbf{X} \mid C_k) P(C_k)}{P(\mathbf{X})}$$
* **$P(C_k)$**: Prior probability of class $C_k$.
* **$P(\mathbf{X} \mid C_k)$**: Likelihood of observing feature vector $\mathbf{X}$ given class $C_k$.
* **$P(C_k \mid \mathbf{X})$**: Posterior probability.

### 1.2 The Naïve Conditional Independence Assumption
Assumes all attributes $X_1, \dots, X_d$ are mutually conditionally independent given target class $C_k$:
$$P(\mathbf{X} \mid C_k) = \prod_{i=1}^d P(X_i \mid C_k)$$
Classification decision rule:
$$C_{\text{MAP}} = \arg\max_{C_k} P(C_k) \prod_{i=1}^d P(X_i \mid C_k)$$

### 1.3 Laplace (Lidstone) Smoothing for Zero-Frequencies
If a feature value $x_i$ never appears with class $C_k$ in the training set, $P(x_i \mid C_k) = 0$, reducing the entire product to zero.
* **Laplace Estimator ($+1$ Smoothing)**:
  $$\hat{P}(x_i \mid C_k) = \frac{N_{ik} + 1}{N_k + |V|}$$
  *(where $N_{ik}$ is the count of feature $x_i$ in class $C_k$, $N_k$ is the total count of all feature instances in class $C_k$, and $|V|$ is the vocabulary / distinct attribute value count).*

### 1.4 MAP, ML & The Bayes Optimal Classifier (Dr. Nilamadhab Mishra)
1. **Maximum A Posteriori (MAP) Hypothesis**:
   $$h_{\text{MAP}} = \arg\max_{h \in H} P(h \mid D) = \arg\max_{h \in H} P(D \mid h) P(h)$$
2. **Maximum Likelihood (ML) Hypothesis**:
   When assuming a uniform prior across all hypotheses ($P(h_i) = P(h_j)$):
   $$h_{\text{ML}} = \arg\max_{h \in H} P(D \mid h)$$
3. **Bayes Optimal Classifier (BOC)**:
   * *Problem with MAP*: $h_{\text{MAP}}$ finds the single most likely hypothesis, but what if multiple other hypotheses collectively vote for an alternative class?
   * *BOC Principle*: Combines predictions of **all hypotheses**, weighted by their posterior probabilities:
     $$v_{\text{BOC}} = \arg\max_{v_j \in V} \sum_{h_i \in H} P(v_j \mid h_i) P(h_i \mid D)$$
   * *Theoretical Optimality*: **No other classification method using the same hypothesis space and prior knowledge can outperform the Bayes Optimal Classifier on average!**
   * *Gibbs Classifier*: Practical randomized alternative that draws a single hypothesis $h$ sampled according to $P(h \mid D)$ and uses $h$ to classify. Its expected error is at most twice that of the Bayes Optimal Classifier ($E_{\text{Gibbs}} \le 2 E_{\text{BOC}}$).

---

## 2. Bayesian Belief Networks (BBN)

A **Bayesian Belief Network** represents joint probability distributions over a set of variables without requiring the naive full conditional independence assumption.

```
                              A (Burglary)       B (Earthquake)
                                   \             /
                                    v           v
                                   C (Alarm)
                                   /       \
                                  v         v
                             D (JohnCalls)  E (MaryCalls)
```

1. **DAG Structure**: Nodes represent random variables; directed edges represent direct probabilistic causal influences.
2. **Conditional Probability Tables (CPT)**: Each node $X_i$ maintains a local table quantifying $P(X_i \mid \text{Parents}(X_i))$.
3. **Chain Rule Factorization**:
   $$P(X_1, X_2, \dots, X_n) = \prod_{i=1}^n P(X_i \mid \text{Parents}(X_i))$$

---

## 3. Association Rule Mining: Apriori vs FP-Growth

### 3.1 Market Basket Terminology
For a transaction database $T = \{t_1, \dots, t_N\}$ and rule $X \to Y$ (where $X \cap Y = \emptyset$):
* **Support**: Percentage of transactions containing both $X$ and $Y$:
  $$\text{Support}(X \to Y) = \frac{\sigma(X \cup Y)}{N}$$
* **Confidence**: Percentage of transactions containing $X$ that also contain $Y$:
  $$\text{Confidence}(X \to Y) = \frac{\sigma(X \cup Y)}{\sigma(X)} = \frac{\text{Support}(X \cup Y)}{\text{Support}(X)}$$
* **Lift**: Ratio of observed joint support to expected support if independent:
  $$\text{Lift}(X \to Y) = \frac{\text{Confidence}(X \to Y)}{\text{Support}(Y)}$$
  *(Lift $> 1 \implies$ Positive correlation; Lift $= 1 \implies$ Independence; Lift $< 1 \implies$ Negative substitution).*

### 3.2 The Apriori Property (Downward Closure of Support)
> "Any subset of a frequent itemset must also be frequent."  
> Contrapositive: "If an itemset is infrequent, all of its supersets are guaranteed to be infrequent and can be pruned immediately."

### 3.3 FP-Growth (Frequent Pattern Growth) Algorithm
Eliminates Apriori’s expensive candidate generation and multiple database passes:
1. **Pass 1**: Scan database once; calculate support for each 1-itemset. Filter by $\text{minsup}$ and sort frequent items in **descending frequency order**.
2. **Pass 2**: Scan database again; insert transactions into a prefix tree (**FP-Tree**) sharing common prefixes.
3. **Mining**: Construct a **Conditional Pattern Base** for each suffix item, build a **Conditional FP-Tree**, and recursively extract frequent itemsets.

### 3.4 High Utility Itemset Mining (HUIM) vs Frequent Pattern Mining (Dr. Nilamadhab Mishra)
1. **Why Frequent Pattern Mining Fails in Business**:
   * Apriori and FP-Growth assume each item occurrence has equal value (frequency count $= 1$).
   * A high-frequency item (e.g., bread sold 500 times at ₹2 profit = ₹1,000) generates far less business value than an infrequent high-utility item (e.g., laptop sold 10 times at ₹5,000 profit = ₹50,000).
2. **Core Utility Definitions**:
   * **External Utility $p(i)$**: Unit profit / significance of item $i$ (external profit table).
   * **Internal Utility $q(i, t)$**: Quantity of item $i$ purchased in transaction $t$.
   * **Utility of Item in Transaction**: $u(i, t) = p(i) \times q(i, t)$.
   * **Utility of Itemset $X$ in Transaction**: $u(X, t) = \sum_{i \in X} u(i, t)$ (if $X \subseteq t$, else $0$).
   * **Utility of Itemset $X$ in Database $D$**: $u(X) = \sum_{t \in D, X \subseteq t} u(X, t)$.
   * An itemset $X$ is a **High Utility Itemset (HUI)** if $u(X) \ge \text{min\_util}$.
3. **The Anti-Monotonicity Challenge & TWU Solution**:
   * **Utility does NOT satisfy Downward Closure**: An itemset $\{A\}$ might have utility ₹20, while its superset $\{A, B\}$ has utility ₹120 ($> \text{min\_util}$). Thus, Apriori pruning cannot be directly applied!
   * **Transaction-Weighted Utilization (TWU)**:
     $$\text{TWU}(X) = \sum_{t \in D, X \subseteq t} TU(t) \quad \text{where } TU(t) = \sum_{i \in t} u(i, t)$$
   * **TWU Downward Closure Property**: If $\text{TWU}(X) < \text{min\_util}$, then neither $X$ nor any of its supersets can be a high-utility itemset. This restores the pruning power!

---

## 4. Model Exam Questions & Answers

### Question 1 (12 Marks)
**Given a transaction database with 5 transactions:**  
$T_1 = \{A, C, D\}$, $T_2 = \{B, C, E\}$, $T_3 = \{A, B, C, E\}$, $T_4 = \{B, E\}$, $T_5 = \{A, B, C, E\}$.  
**Using the Apriori algorithm with $\text{minsup} = 40\%$ (2 transactions) and $\text{minconf} = 70\%$, find all frequent itemsets and generate strong association rules.**

**Solution**:
1. **$C_1$ Candidate Itemsets & $L_1$ Frequent 1-Itemsets**:
   - Counts: $A: 3, B: 4, C: 4, D: 1, E: 4$. Total transactions $N = 5$.
   - $\text{minsup} = 2$. Item $D$ count is $1 < 2 \implies$ Prune $D$.
   - $L_1 = \{ \{A\}: 3, \{B\}: 4, \{C\}: 4, \{E\}: 4 \}$.
2. **$C_2$ Candidate 2-Itemsets & $L_2$**:
   - Pairs from $L_1$: $\{A,B\}, \{A,C\}, \{A,E\}, \{B,C\}, \{B,E\}, \{C,E\}$.
   - Counts:
     - $\{A, B\}: 2$ ($T_3, T_5$)
     - $\{A, C\}: 3$ ($T_1, T_3, T_5$)
     - $\{A, E\}: 2$ ($T_3, T_5$)
     - $\{B, C\}: 3$ ($T_2, T_3, T_5$)
     - $\{B, E\}: 4$ ($T_2, T_3, T_4, T_5$)
     - $\{C, E\}: 3$ ($T_2, T_3, T_5$)
   - All pairs have count $\ge 2 \implies$ All 6 pairs in $L_2$.
3. **$C_3$ Candidate 3-Itemsets & $L_3$**:
   - Triplet candidates: $\{A, B, C\}, \{A, B, E\}, \{A, C, E\}, \{B, C, E\}$.
   - Counts:
     - $\{A, B, C\}: 2$ ($T_3, T_5$)
     - $\{A, B, E\}: 2$ ($T_3, T_5$)
     - $\{A, C, E\}: 2$ ($T_3, T_5$)
     - $\{B, C, E\}: 3$ ($T_2, T_3, T_5$)
   - All 4 triplets in $L_3$.
4. **$C_4$ Candidate 4-Itemset & $L_4$**:
   - $\{A, B, C, E\}$: Appears in $T_3, T_5 \implies \text{Count} = 2 \ge 2 \implies L_4 = \{ \{A, B, C, E\} \}$.
5. **Rule Generation for $\{B, E\} \to C$**:
   - Support count of $\{B, C, E\} = 3$. Support count of $\{B, E\} = 4$.
   - $\text{Confidence}(\{B, E\} \to C) = \frac{3}{4} = \mathbf{75\%} \ge 70\% \implies$ **Strong Rule Generated!**

### Question 2 (8 Marks)
**Explain the conditional independence assumption in Naïve Bayes. Why does Naïve Bayes perform remarkably well in practice despite this unrealistic assumption?**

**Solution**:
1. **Assumption Statement**: Assumes features are completely independent given the target class ($P(x_1, x_2 \mid c) = P(x_1 \mid c) P(x_2 \mid c)$).
2. **Why it Works in Practice**:
   - *Classification vs Probability Estimation*: For classification, we only care whether $P(C_1 \mid X) > P(C_2 \mid X)$ (the correct ranking/argmax), not the exact calibrated probability values. Correlated features may inflate posterior estimates, but rarely alter the winning class sign.
   - *Low Variance*: Eliminating covariance parameter estimation prevents overfitting, especially on high-dimensional text datasets with small sample sizes.

---

### Question 3 (12 Marks) [Direct from Dr. Nilamadhab Mishra Slides 4.1 & 4.2]
**(a) Differentiate between the Maximum A Posteriori (MAP) hypothesis and the Bayes Optimal Classifier. Explain why the Bayes Optimal Classifier is theoretically optimal, and provide a numeric example where its prediction differs from the MAP hypothesis.**  
**(b) Explain High Utility Itemset Mining (HUIM). Why does the Apriori downward closure property fail for itemset utility, and how does Transaction-Weighted Utilization (TWU) solve this?**

**Solution**:
1. **Part (a): MAP vs Bayes Optimal Classifier**:
   * *MAP*: Predicts the class favored by the single hypothesis with highest posterior: $h_{\text{MAP}} = \arg\max_h P(h \mid D)$.
   * *Bayes Optimal Classifier (BOC)*: Combines predictions across the **entire hypothesis space**, weighted by posterior probabilities:
     $$v_{\text{BOC}} = \arg\max_{v_j \in V} \sum_{h_i \in H} P(v_j \mid h_i) P(h_i \mid D)$$
   * *Numeric Counterexample*:
     - Suppose hypothesis space $H = \{h_1, h_2, h_3\}$ with posteriors: $P(h_1 \mid D) = 0.4$, $P(h_2 \mid D) = 0.3$, $P(h_3 \mid D) = 0.3$.
     - Hypotheses classify a new instance $x$ as: $h_1(x) = \oplus$, $h_2(x) = \ominus$, $h_3(x) = \ominus$.
     - **MAP Prediction**: $h_{\text{MAP}} = h_1$ (since $0.4 > 0.3$). Thus MAP outputs **$\oplus$**!
     - **BOC Prediction**:
       - $P(\oplus \mid D) = P(\oplus \mid h_1) P(h_1 \mid D) = 1.0 \times 0.4 = \mathbf{0.4}$
       - $P(\ominus \mid D) = P(\ominus \mid h_2) P(h_2 \mid D) + P(\ominus \mid h_3) P(h_3 \mid D) = 0.3 + 0.3 = \mathbf{0.6}$
       - BOC chooses $\arg\max \{0.4, 0.6\} = \mathbf{\ominus}$!
     - *Result*: The MAP hypothesis output ($\oplus$) is actually less likely than the collective consensus ($\ominus$) of the other hypotheses! BOC guarantees the lowest error rate.

2. **Part (b): High Utility Itemset Mining & TWU**:
   * *Frequent Pattern Limitation*: Treats high-value and low-value items identically based solely on transaction frequency.
   * *Utility Downward Closure Failure*: In Apriori, if $\{A\}$ is infrequent, $\{A, B\}$ must be infrequent. But for utility:
     - Suppose unit profit: $p(A) = 1$, $p(B) = 100$.
     - In transaction $T_1 = \{A, B\}$ with quantity 1 each: $u(A) = 1$, $u(\{A, B\}) = 101$.
     - If $\text{min\_util} = 50$, $\{A\}$ has $u(A) = 1 < 50$ (unpromising), yet its superset $\{A, B\}$ has utility $101 \ge 50$ (high utility)! Pruning $\{A\}$ would incorrectly eliminate $\{A, B\}$.
   * *TWU Solution*:
     - $\text{TWU}(X)$ is the sum of total transaction utilities of all transactions containing $X$.
     - Because every item in transaction $t$ contributes to $TU(t)$, $\text{TWU}(X)$ is monotonic: any superset $X \cup \{Y\}$ can appear at most in the same transactions as $X$, so $\text{TWU}(X \cup \{Y\}) \le \text{TWU}(X)$.
     - Therefore, if $\text{TWU}(X) < \text{min\_util}$, no superset of $X$ can ever exceed $\text{min\_util}$, safely pruning the search tree without missing any high-utility itemsets.
