# 📘 Unit 3: Ensemble Learning, Clustering & Expectation-Maximization

---

## 1. Ensemble Learning Paradigms

Ensemble methods combine multiple base models ("weak learners") to produce a robust meta-model with superior generalization performance.

```
+-----------------------------------------------------------------------------------------+
| Dimension         | Bagging (Bootstrap Aggregating)   | Boosting (Adaptive Boosting)    |
+-------------------+-----------------------------------+---------------------------------+
| **Execution**     | **Parallel & Independent**        | **Sequential & Dependent**      |
| **Base Learners** | High-variance, deep unpruned trees| High-bias, weak learners (stumps)|
| **Primary Goal**  | **Variance Reduction**            | **Bias Reduction**              |
| **Sample Weight** | Uniform random with replacement   | Adaptive; increases on errors   |
| **Noise Impact**  | Robust against noisy data         | Vulnerable to overfitting noise |
| **Exemplar**      | **Random Forest**                 | **AdaBoost, XGBoost**           |
+-----------------------------------------------------------------------------------------+
```

---

## 2. The AdaBoost Algorithm (Step-by-Step Derivation)

1. Given training set $\{(\mathbf{x}_1, y_1), \dots, (\mathbf{x}_m, y_m)\}$ with labels $y_i \in \{-1, +1\}$.
2. Initialize sample weight distribution uniformly:
   $$w_i^{(1)} = \frac{1}{m}, \quad \forall i = 1, \dots, m$$
3. For iteration $t = 1$ to $T$:
   - Train weak hypothesis $h_t(\mathbf{x})$ using weights $\mathbf{w}^{(t)}$.
   - Calculate weighted training error $\epsilon_t$:
     $$\epsilon_t = \sum_{i: h_t(x_i) \neq y_i} w_i^{(t)}$$
   - Calculate hypothesis voting weight $\alpha_t$:
     $$\alpha_t = \frac{1}{2} \ln \left( \frac{1 - \epsilon_t}{\epsilon_t} \right)$$
   - Update sample weights:
     $$w_i^{(t+1)} = \frac{w_i^{(t)} \exp\left( - \alpha_t y_i h_t(\mathbf{x}_i) \right)}{Z_t}$$
     *(where $Z_t$ is the normalization factor ensuring $\sum w_i^{(t+1)} = 1$).*
4. Output final combined classifier:
   $$H(\mathbf{x}) = \text{sign}\left( \sum_{t=1}^T \alpha_t h_t(\mathbf{x}) \right)$$

---

## 3. Unsupervised Clustering: K-Means Algorithm

### 3.1 Objective & Algorithm Steps
Minimizes the **Within-Cluster Sum of Squares (WCSS)** / Inertia:
$$J = \sum_{k=1}^K \sum_{\mathbf{x} \in C_k} \|\mathbf{x} - \mathbf{\mu}_k\|^2$$

1. **Step 1: Initialization**: Randomly choose $K$ data points as initial centroids $\mathbf{\mu}_1, \dots, \mathbf{\mu}_K$.
2. **Step 2: Assignment**: Assign each point $\mathbf{x}_i$ to the nearest cluster centroid:
   $$c^{(i)} = \arg\min_k \|\mathbf{x}_i - \mathbf{\mu}_k\|^2$$
3. **Step 3: Update**: Recompute each centroid as the geometric mean of assigned points:
   $$\mathbf{\mu}_k = \frac{1}{|C_k|} \sum_{\mathbf{x} \in C_k} \mathbf{x}$$
4. **Step 4: Convergence**: Repeat Steps 2 and 3 until centroid positions stabilize or maximum iterations reached.

---

## 4. Hierarchical Clustering (AGNES vs DIANA)

* **Agglomerative (AGNES)**: Bottom-up approach. Starts with each point as its own cluster; sequentially merges the closest pair of clusters until one single cluster remains.
* **Divisive (DIANA)**: Top-down approach. Starts with all points in one mega-cluster; sequentially splits clusters.
* **Linkage Distance Metrics between Clusters $A$ and $B$**:
  - **Single Linkage**: $d(A, B) = \min_{\mathbf{a} \in A, \mathbf{b} \in B} \|\mathbf{a} - \mathbf{b}\|$ (Prone to "chaining" effect).
  - **Complete Linkage**: $d(A, B) = \max_{\mathbf{a} \in A, \mathbf{b} \in B} \|\mathbf{a} - \mathbf{b}\|$ (Produces tight, compact clusters).
  - **Average Linkage**: $d(A, B) = \frac{1}{|A||B|} \sum_{\mathbf{a} \in A} \sum_{\mathbf{b} \in B} \|\mathbf{a} - \mathbf{b}\|$.

---

## 5. Model Exam Questions & Answers

### Question 1 (12 Marks)
**Apply the K-Means clustering algorithm for 1D points: $\{2, 4, 10, 12, 3, 20, 30, 11, 25\}$ with $K = 2$. Choose initial centroids $\mu_1 = 2$ and $\mu_2 = 4$. Show step-by-step centroid updates for 2 iterations.**

**Solution**:
1. **Iteration 1**:
   - Initial Centroids: $\mu_1 = 2, \mu_2 = 4$.
   - Compute distances and assign points to nearest centroid:
     - Point 2: $|2-2|=0 \le |2-4|=2 \implies C_1$
     - Point 4: $|4-2|=2 > |4-4|=0 \implies C_2$
     - Point 10: $|10-2|=8 > |10-4|=6 \implies C_2$
     - Point 12: $|12-2|=10 > |12-4|=8 \implies C_2$
     - Point 3: $|3-2|=1 = |3-4|=1 \implies C_1$ (tie break)
     - Point 20, 30, 11, 25: All closer to $\mu_2 = 4 \implies C_2$.
   - Cluster Formations:
     - $C_1 = \{2, 3\}$
     - $C_2 = \{4, 10, 11, 12, 20, 25, 30\}$
   - Recompute Centroids:
     $$\mu_1^{(1)} = \frac{2 + 3}{2} = \mathbf{2.5}$$
     $$\mu_2^{(1)} = \frac{4 + 10 + 11 + 12 + 20 + 25 + 30}{7} = \frac{112}{7} = \mathbf{16.0}$$
2. **Iteration 2**:
   - New Centroids: $\mu_1 = 2.5, \mu_2 = 16.0$. Midpoint threshold $= \frac{2.5 + 16.0}{2} = 9.25$.
   - Reassign points based on threshold $9.25$:
     - Points $\le 9.25$: $\{2, 3, 4\} \implies C_1$
     - Points $> 9.25$: $\{10, 11, 12, 20, 25, 30\} \implies C_2$
   - Recompute Centroids:
     $$\mu_1^{(2)} = \frac{2 + 3 + 4}{3} = \frac{9}{3} = \mathbf{3.0}$$
     $$\mu_2^{(2)} = \frac{10 + 11 + 12 + 20 + 25 + 30}{6} = \frac{108}{6} = \mathbf{18.0}$$
   - *End of Iteration 2: Clusters partitioned into low values $\{2, 3, 4\}$ and high values $\{10, 11, 12, 20, 25, 30\}$.*

### Question 2 (8 Marks)
**Explain the AdaBoost weight update rule. If a weak classifier has training error $\epsilon_t = 0.2$, calculate its voting weight $\alpha_t$ and the weight multiplier for correctly vs incorrectly classified instances.**

**Solution**:
1. **Voting Weight $\alpha_t$**:
   $$\alpha_t = \frac{1}{2} \ln \left( \frac{1 - \epsilon_t}{\epsilon_t} \right) = \frac{1}{2} \ln \left( \frac{1 - 0.2}{0.2} \right) = \frac{1}{2} \ln (4) = \frac{1}{2} (1.3863) = \mathbf{0.6931}$$
2. **Multiplier for Misclassified Instances ($y_i \ne h_t(x_i) \implies y_i h_t(x_i) = -1$)**:
   $$\text{Factor} = \exp(-\alpha_t (-1)) = \exp(\alpha_t) = \exp(0.6931) = \mathbf{2.00}$$
   *(The sample weight doubles!)*
3. **Multiplier for Correctly Classified Instances ($y_i = h_t(x_i) \implies y_i h_t(x_i) = +1$)**:
   $$\text{Factor} = \exp(-\alpha_t (+1)) = \exp(-\alpha_t) = \exp(-0.6931) = \mathbf{0.50}$$
   *(The sample weight is halved!)*
