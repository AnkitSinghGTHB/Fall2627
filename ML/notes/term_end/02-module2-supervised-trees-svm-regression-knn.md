# 📘 Unit 2: Supervised Learning — Trees, Regression, Neural Nets, SVM & KNN

---

## 1. Decision Trees (ID3, C4.5, CART)

### 1.1 Mathematical Metrics
* **Entropy ($H(S)$)**: Measures information uncertainty/impurity:
  $$H(S) = - \sum_{i=1}^c p_i \log_2 p_i$$
  *(For binary target: $H(S) = -p_+ \log_2 p_+ - p_- \log_2 p_-$. Note: $0 \log_2 0 = 0$; Maximum entropy $= 1.0$ when $p_+ = p_- = 0.5$).*

* **Information Gain ($\text{Gain}(S, A)$) [Used in ID3]**: Expected reduction in entropy caused by partitioning on attribute $A$:
  $$\text{Gain}(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$$
  *Limitation*: Biased toward attributes with many distinct values (e.g., `Date` or `Customer_ID`).

* **Gain Ratio [Used in C4.5]**: Normalizes Information Gain by the attribute's **Split Information**:
  $$\text{SplitInfo}(S, A) = - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} \log_2 \left( \frac{|S_v|}{|S|} \right)$$
  $$\text{GainRatio}(S, A) = \frac{\text{Gain}(S, A)}{\text{SplitInfo}(S, A)}$$

* **Gini Impurity [Used in CART]**:
  $$\text{Gini}(S) = 1 - \sum_{i=1}^c p_i^2$$
  *(For binary pure node: $\text{Gini} = 0$; Maximum impurity $= 0.5$).*

---

## 2. Linear & Logistic Regression

### 2.1 Linear Regression
* **Hypothesis**: $h_\theta(x) = \theta_0 + \theta_1 x_1 + \dots + \theta_n x_n = \mathbf{\theta}^T \mathbf{x}$.
* **Cost Function (Mean Squared Error)**:
  $$J(\mathbf{\theta}) = \frac{1}{2m} \sum_{i=1}^m \left( h_\theta(x^{(i)}) - y^{(i)} \right)^2$$
* **Batch Gradient Descent Update Rule**:
  $$\theta_j := \theta_j - \alpha \frac{1}{m} \sum_{i=1}^m \left( h_\theta(x^{(i)}) - y^{(i)} \right) x_j^{(i)}$$
* **Closed-Form Normal Equation**:
  $$\mathbf{\theta} = \left( \mathbf{X}^T \mathbf{X} \right)^{-1} \mathbf{X}^T \mathbf{y}$$

### 2.2 Logistic Regression (Classification)
* **Hypothesis (Sigmoid Function)**:
  $$h_\theta(x) = g(\mathbf{\theta}^T \mathbf{x}) = \frac{1}{1 + e^{-\mathbf{\theta}^T \mathbf{x}}}$$
* Output represents estimated probability $P(y = 1 \mid x; \theta)$. Decision threshold: Predict $y=1$ if $\mathbf{\theta}^T \mathbf{x} \ge 0 \implies h_\theta(x) \ge 0.5$.
* **Binary Cross-Entropy Loss Function**:
  $$J(\mathbf{\theta}) = - \frac{1}{m} \sum_{i=1}^m \left[ y^{(i)} \ln \left( h_\theta(x^{(i)}) \right) + (1 - y^{(i)}) \ln \left( 1 - h_\theta(x^{(i)}) \right) \right]$$

---

## 3. Support Vector Machines (SVM)

### 3.1 Maximum Margin Hyperplane
* Linear decision boundary: $\mathbf{w}^T \mathbf{x} + b = 0$.
* Distance from any point $\mathbf{x}_i$ to the hyperplane: $\gamma_i = \frac{y_i (\mathbf{w}^T \mathbf{x}_i + b)}{\|\mathbf{w}\|}$.
* Geometric Margin:
  $$\text{Margin } M = \frac{2}{\|\mathbf{w}\|}$$
* **Primal Optimization Problem**:
  $$\min_{\mathbf{w}, b} \frac{1}{2} \|\mathbf{w}\|^2 \quad \text{subject to } y_i (\mathbf{w}^T \mathbf{x}_i + b) \ge 1, \quad \forall i$$
* **Soft Margin with Slack Variables ($\xi_i \ge 0$)**:
  $$\min_{\mathbf{w}, b, \mathbf{\xi}} \frac{1}{2} \|\mathbf{w}\|^2 + C \sum_{i=1}^m \xi_i \quad \text{subject to } y_i (\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i$$
  *(Parameter $C$ controls trade-off: Large $C \implies$ narrow margin, low training error / high variance; Small $C \implies$ wider margin, higher tolerance for misclassifications).*

### 3.2 The Kernel Trick
Maps non-linearly separable input data into high-dimensional feature space $\Phi(\mathbf{x})$ where data becomes linearly separable, computing inner products via a kernel function $K(\mathbf{x}, \mathbf{z}) = \langle \Phi(\mathbf{x}), \Phi(\mathbf{z}) \rangle$:
* **Linear Kernel**: $K(\mathbf{x}, \mathbf{z}) = \mathbf{x}^T \mathbf{z}$
* **Polynomial Kernel**: $K(\mathbf{x}, \mathbf{z}) = (\mathbf{x}^T \mathbf{z} + c)^d$
* **Gaussian Radial Basis Function (RBF)**:
  $$K(\mathbf{x}, \mathbf{z}) = \exp \left( - \gamma \|\mathbf{x} - \mathbf{z}\|^2 \right)$$

---

## 4. K-Nearest Neighbors (KNN)

* **Algorithm**: Non-parametric, instance-based "lazy learner" (stores training set, defers computation to query time).
* **Distance Metrics**:
  - Euclidean ($L_2$): $d(\mathbf{x}, \mathbf{z}) = \sqrt{\sum (x_i - z_i)^2}$
  - Manhattan ($L_1$): $d(\mathbf{x}, \mathbf{z}) = \sum |x_i - z_i|$
  - Minkowski ($L_p$): $d(\mathbf{x}, \mathbf{z}) = \left( \sum |x_i - z_i|^p \right)^{1/p}$
* **Impact of Parameter $k$**:
  - $k = 1$: Sensitive to noise/outliers $\implies$ Low bias, High variance (Overfitting).
  - Large $k$: Smooth decision boundary, may include samples from distant classes $\implies$ High bias, Low variance (Underfitting).

---

## 5. Model Exam Questions & Answers

### Question 1 (12 Marks)
**A dataset consists of 14 instances with 9 positive and 5 negative examples for target class `PlayTennis`. An attribute `Wind` has values `Weak` (6 positive, 2 negative) and `Strong` (3 positive, 3 negative). Calculate the Information Gain of `Wind`.**

**Solution**:
1. **Total Entropy of Dataset $S$**:
   - Total $= 14$, Positive $= 9$, Negative $= 5$.
   $$H(S) = - \left( \frac{9}{14} \log_2 \frac{9}{14} \right) - \left( \frac{5}{14} \log_2 \frac{5}{14} \right)$$
   $$= - (0.6429 \times (-0.6374)) - (0.3571 \times (-1.4855)) = 0.4098 + 0.5305 = \mathbf{0.9403}$$
2. **Entropy for `Wind = Weak` ($S_{Weak}$)**:
   - Total $= 8$, Positive $= 6$, Negative $= 2$.
   $$H(S_{Weak}) = - \left( \frac{6}{8} \log_2 \frac{6}{8} \right) - \left( \frac{2}{8} \log_2 \frac{2}{8} \right)$$
   $$= - (0.75 \times (-0.4150)) - (0.25 \times (-2.0)) = 0.3113 + 0.5000 = \mathbf{0.8113}$$
3. **Entropy for `Wind = Strong` ($S_{Strong}$)**:
   - Total $= 6$, Positive $= 3$, Negative $= 3$.
   $$H(S_{Strong}) = - \left( \frac{3}{6} \log_2 \frac{3}{6} \right) - \left( \frac{3}{6} \log_2 \frac{3}{6} \right) = - (0.5 \times (-1)) - (0.5 \times (-1)) = \mathbf{1.0000}$$
4. **Information Gain**:
   $$\text{Gain}(S, \text{Wind}) = H(S) - \left( \frac{|S_{Weak}|}{|S|} H(S_{Weak}) + \frac{|S_{Strong}|}{|S|} H(S_{Strong}) \right)$$
   $$= 0.9403 - \left( \frac{8}{14} (0.8113) + \frac{6}{14} (1.0000) \right)$$
   $$= 0.9403 - (0.4636 + 0.4286) = 0.9403 - 0.8922 = \mathbf{0.0481}$$

### Question 2 (8 Marks)
**Derive the mathematical formulation of Maximum Margin Hyperplane in linear SVM. Explain the role of Support Vectors.**

**Solution**:
1. **Geometric Setup**: Hyperplane $\mathbf{w}^T \mathbf{x} + b = 0$.
2. **Canonical Hyperplanes**: Scaled such that for the closest training data points:
   $$\mathbf{w}^T \mathbf{x}_+ + b = +1 \quad (\text{for } y_i = +1)$$
   $$\mathbf{w}^T \mathbf{x}_- + b = -1 \quad (\text{for } y_i = -1)$$
3. **Margin Calculation**: Subtracting equations yields $\mathbf{w}^T (\mathbf{x}_+ - \mathbf{x}_-) = 2$. Projecting the vector $(\mathbf{x}_+ - \mathbf{x}_-)$ onto the unit normal vector $\frac{\mathbf{w}}{\|\mathbf{w}\|}$ gives:
   $$\text{Margin } M = \frac{\mathbf{w}^T (\mathbf{x}_+ - \mathbf{x}_-)}{\|\mathbf{w}\|} = \frac{2}{\|\mathbf{w}\|}$$
4. **Optimization**: Maximizing $\frac{2}{\|\mathbf{w}\|}$ is mathematically equivalent to minimizing $\frac{1}{2} \|\mathbf{w}\|^2$ subject to $y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1, \forall i$.
5. **Support Vectors**: The subset of training data points that lie directly on the canonical hyperplanes ($y_i(\mathbf{w}^T \mathbf{x}_i + b) = 1$). All other points can be completely removed from the training set without altering the final optimal decision boundary.
