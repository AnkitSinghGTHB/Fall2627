# ⏱️ CSE4005: ML Emergency Study Plan & Formula Matrix

> **Exam Date**: Saturday, October 17, 2026 (01:15 PM – 04:15 PM)  
> **Your Starting Position**: **62.2 / 70.0 Recorded Subtotal** (+3.3 marks ahead of class!)  
> **Target for A Grade**: **64–68 / 100** (Very relaxed!) | **Target for S Grade**: **88–92 / 100**

---

## 📅 Revision Strategy (Zero-Gap Survival)
Since ML is on Saturday right after DLD on Friday:
* **Friday Night (Oct 16, 5:30 PM – 11:30 PM)**:
  - 5:30 – 7:30 PM: Unit 2 & 3 Numericals (Decision Tree Entropy/Gain, K-Means cluster distance table).
  - 8:00 – 10:00 PM: Unit 4 & 5 Numericals (Naïve Bayes posterior calculation with Laplace smoothing, Apriori Support/Confidence, Confusion Matrix & PCA steps).
  - 10:00 – 11:30 PM: Unit 1 Theory (PAC Learning bounds, VC Dimension, Candidate Elimination).
* **Saturday Morning (Oct 17, 8:00 AM – 11:30 AM)**:
  - 06-Formula Cheat Sheet review + Solve 2 past numerical questions.

---

## 🎯 The 6 Guaranteed Exam Numericals (50+ Marks Locked)

| Numerical Archetype | Module | Core Formula / Algorithm |
|:---|:---:|:---|
| **1. Decision Tree Root Selection** | Unit 2 | $\text{Gain}(S, A) = \text{Entropy}(S) - \sum \frac{\|S_v\|}{\|S\|} \text{Entropy}(S_v)$ |
| **2. Support Vector Machine (Linear Margin)** | Unit 2 | $\text{Margin } M = \frac{2}{\|\mathbf{w}\|}$; Classify using $\text{sign}(\mathbf{w}^T \mathbf{x} + b)$ |
| **3. K-Means Clustering 2-Iteration Trace** | Unit 3 | Reassign points to nearest centroid: $d(\mathbf{x}, \mathbf{\mu}) = \|\mathbf{x} - \mathbf{\mu}\|^2$; Recompute $\mathbf{\mu} = \frac{1}{\|C_k\|} \sum \mathbf{x}$ |
| **4. AdaBoost Classifier Weight Updates** | Unit 3 | $\epsilon_t = \sum_{misclassified} w_i$; $\alpha_t = \frac{1}{2} \ln \left(\frac{1-\epsilon_t}{\epsilon_t}\right)$; $w_{i}^{(t+1)} = \frac{w_i^{(t)} \exp(-\alpha_t y_i h_t(x_i))}{Z_t}$ |
| **5. Naïve Bayes Classification with Laplace** | Unit 4 | $P(C_k \mid X) \propto P(C_k) \prod P(x_i \mid C_k)$; Laplace: $P(x_i \mid C_k) = \frac{N_{ik} + 1}{N_k + \|V\|}$ |
| **6. Apriori Itemset Mining (Min Support/Conf)** | Unit 4 | $\text{Support}(A \cup B) \ge \text{minsup}$; $\text{Confidence}(A \to B) = \frac{\text{Support}(A \cup B)}{\text{Support}(A)} \ge \text{minconf}$ |
