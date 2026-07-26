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

## 🧠 Model Trade-offs

- **High Bias**: Underfitting (model too simple).
- **High Variance**: Overfitting (model memorizes training noise).
- **Goal**: Low Bias + Low Variance.
