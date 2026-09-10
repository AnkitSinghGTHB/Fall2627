# ⚡ Machine Learning — Master Cheatsheet

> **Print this. One page. All core formulas and concepts.**

---

## 📊 Evaluation Formulas

| Metric | Formula | Best Used When |
|---|---|---|
| **Accuracy** | $\frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}$ | Balanced classes |
| **Precision** | $\frac{\text{TP}}{\text{TP} + \text{FP}}$ | High cost of False Positives (e.g. Spam) |
| **Recall** | $\frac{\text{TP}}{\text{TP} + \text{FN}}$ | High cost of False Negatives (e.g. Medical) |
| **F1-Score** | $2 \times \frac{P \times R}{P + R}$ | Imbalanced datasets |

---

## 🧹 Scaling Formulas

- **Min-Max**: $X_{\text{norm}} = \frac{X - X_{\text{min}}}{X_{\text{max}} - X_{\text{min}}}$ (Range: $[0, 1]$)
- **Standardization**: $Z = \frac{X - \mu}{\sigma}$ (Mean $= 0$, Std Dev $= 1$)

---

## 🧠 Model Trade-offs (Bias-Variance)

| Error Type | Meaning | Result | Fix |
|---|---|---|---|
| **High Bias** | Model is too simple to learn the data | **Underfitting** | Make model more complex, add features |
| **High Variance** | Model memorizes the training noise | **Overfitting** | Simplify model, get more data, use regularization |

> **Goal**: Low Bias + Low Variance (The Goldilocks Zone).

---

## 🤖 Learning Paradigms

| Paradigm | Data Type | Goal | Example Algorithms |
|---|---|---|---|
| **Supervised** | Labeled (Answers provided) | Predict future answers | Linear Regression, SVM, Random Forest |
| **Unsupervised** | Unlabeled (No answers) | Find hidden patterns/groups | K-Means Clustering, PCA |
| **Reinforcement** | Environment & Rewards | Learn by trial and error | Q-Learning (Chess, Self-driving cars) |

---

## ⚡ Perceptron Update Rule
If the perceptron makes a mistake:
$$ w_{\text{new}} = w_{\text{old}} + (\alpha \times \text{Error} \times X) $$
*Where $\alpha$ is the Learning Rate, and Error = True Label - Predicted Label.*
