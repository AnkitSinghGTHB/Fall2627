# 🤖 ML: Perceptron Learning (The Brain's Building Block)

Welcome to the foundation of Neural Networks! Before ChatGPT was writing your code, there was the humble **Perceptron**, invented all the way back in 1957.

## 1. What is a Perceptron?
**TL;DR:** A Perceptron is the simplest type of artificial neuron. It takes multiple inputs, multiplies them by some "importance" weights, adds them up, and decides to either fire (output 1) or stay quiet (output 0).

* **The Analogy:** Imagine you're deciding whether to go to a party. You have 3 inputs (features):
  1. Is the weather good? (`x1`)
  2. Is your crush going? (`x2`)
  3. Is there free food? (`x3`)

  You assign **weights** (importance) to these inputs.
  - Weather: `w1 = 2` (You don't care that much).
  - Crush: `w2 = 10` (Extremely important!).
  - Food: `w3 = 5` (Pretty good).

  You calculate your total score: `(x1*w1) + (x2*w2) + (x3*w3)`.
  If the total score is above your personal **Threshold** (e.g., 12), you go to the party (Output = 1). If not, you stay home (Output = 0).

## 2. The Math (Exam Format)

Instead of a threshold on the right side of the equation, we move it to the left side and call it the **Bias (`b`)**.

**Formula:** 
`Output = 1` if `(w1*x1 + w2*x2 + ... + b) > 0`
`Output = 0` otherwise.

> [!TIP]
> **Exam Trick:** Think of the Bias (`b`) as how easily this neuron gets excited. A high positive bias means it wants to fire even if the inputs are zero. A negative bias means it's stubborn and needs strong inputs to fire.

## 3. How does it "Learn"? (The Perceptron Rule)

If the perceptron makes a mistake, it adjusts its weights.
* **If it predicted 1, but the true answer was 0:** It was too eager! It decreases the weights for whichever inputs were active.
* **If it predicted 0, but the true answer was 1:** It was too shy! It increases the weights for the active inputs.

**The Update Rule:**
`New Weight = Old Weight + (Learning_Rate * Error * Input)`
*(Where Error = True_Label - Predicted_Label)*

## 4. The Fatal Flaw (The XOR Problem)
> [!WARNING]
> **Exam Trap:** A single Perceptron is a **Linear Classifier**. It can only draw a straight line to separate data points.
> Because of this, a single Perceptron CANNOT solve the `XOR` problem! You can't draw a single straight line to separate `XOR` outputs. This discovery actually killed Neural Network research for a decade (the "AI Winter") until Multi-Layer Perceptrons were invented!

---

## ✅ Quick Self-Check

1. What is the role of a "weight" in a perceptron?
2. What does a high positive bias (`b`) mean?
3. When a perceptron predicts 1, but the true answer is 0, what does it do to its weights?
4. True or False: A single perceptron can easily solve the XOR problem.

<details>
<summary>🔑 Answers</summary>

1. It determines the relative importance of a specific input feature.
2. It means the perceptron is very "eager" to fire, even if the inputs are zero or small.
3. It decreases the weights for the active inputs to make it less likely to fire next time.
4. **False**. A single perceptron is a linear classifier and cannot solve non-linearly separable problems like XOR.

</details>

---

**⏱️ Time spent: ~10 min.**
