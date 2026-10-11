# 📑 CSE4005: ML Master Formula & Derivation Cheat Sheet

> Keep this 1-page summary open for instant numerical formula lookup during revision!

---

## 1. Decision Tree Metrics
* **Entropy**: $H(S) = - \sum p_i \log_2 p_i \quad (0 \le H \le 1)$
* **Information Gain**: $\text{Gain}(S, A) = H(S) - \sum \frac{|S_v|}{|S|} H(S_v)$
* **Split Info**: $\text{SplitInfo}(S, A) = - \sum \frac{|S_v|}{|S|} \log_2 \left(\frac{|S_v|}{|S|}\right)$
* **Gain Ratio**: $\text{GainRatio} = \frac{\text{Gain}}{\text{SplitInfo}}$
* **Gini Impurity**: $\text{Gini}(S) = 1 - \sum p_i^2$

---

## 2. Regression & Optimization
* **MSE Cost Function**: $J(\theta) = \frac{1}{2m} \sum (h_\theta(x^{(i)}) - y^{(i)})^2$
* **Gradient Descent**: $\theta_j := \theta_j - \alpha \frac{1}{m} \sum (h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)}$
* **Normal Equation**: $\mathbf{\theta} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$
* **Sigmoid Function**: $g(z) = \frac{1}{1 + e^{-z}}$

---

## 3. Support Vector Machines
* **Geometric Margin**: $M = \frac{2}{\|\mathbf{w}\|}$
* **Optimization**: $\min \frac{1}{2} \|\mathbf{w}\|^2 \quad \text{s.t. } y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1$
* **Gaussian RBF Kernel**: $K(\mathbf{x}, \mathbf{z}) = \exp(-\gamma \|\mathbf{x} - \mathbf{z}\|^2)$

---

## 4. Ensemble & Clustering
* **AdaBoost Error**: $\epsilon_t = \sum_{h_t(x_i) \ne y_i} w_i^{(t)}$
* **Hypothesis Weight**: $\alpha_t = \frac{1}{2} \ln \left(\frac{1 - \epsilon_t}{\epsilon_t}\right)$
* **Weight Update**: $w_i^{(t+1)} = \frac{w_i^{(t)} \exp(-\alpha_t y_i h_t(x_i))}{Z_t}$
* **K-Means Objective (WCSS)**: $J = \sum_{k=1}^K \sum_{\mathbf{x} \in C_k} \|\mathbf{x} - \mathbf{\mu}_k\|^2$

---

## 5. Bayesian & Association Mining
* **Naïve Bayes MAP**: $C_{\text{MAP}} = \arg\max_{C_k} P(C_k) \prod P(x_i \mid C_k)$
* **Laplace Smoothing**: $\hat{P}(x_i \mid C_k) = \frac{N_{ik} + 1}{N_k + |V|}$
* **Support**: $\text{Supp}(X \to Y) = \frac{\sigma(X \cup Y)}{N}$
* **Confidence**: $\text{Conf}(X \to Y) = \frac{\sigma(X \cup Y)}{\sigma(X)}$
* **Lift**: $\text{Lift}(X \to Y) = \frac{\text{Conf}(X \to Y)}{\text{Supp}(Y)}$

---

## 6. Evaluation Metrics
* **Accuracy**: $\frac{TP + TN}{TP + TN + FP + FN}$
* **Precision**: $\frac{TP}{TP + FP}$
* **Recall (Sensitivity)**: $\frac{TP}{TP + FN}$
* **Specificity**: $\frac{TN}{TN + FP}$
* **F1-Score**: $\frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2 TP}{2 TP + FP + FN}$
* **PCA Covariance**: $\mathbf{\Sigma} = \frac{1}{m} \mathbf{X}_c^T \mathbf{X}_c \implies \mathbf{\Sigma} \mathbf{v}_i = \lambda_i \mathbf{v}_i$
