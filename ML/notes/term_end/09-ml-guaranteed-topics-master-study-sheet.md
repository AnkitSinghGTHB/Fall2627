# 🏆 CSE4005: Machine Learning — Ultimate TEE FAT Master Sheet (Student-Friendly Edition)
### *Written in Plain English with Bold Scoring Keywords for Dr. Nilamadhab Mishra's Exam*

> **Course Code**: CSE4005 — Machine Learning | **Faculty**: Dr. Nilamadhab Mishra  
> **Slot**: A21+A23 | **Duration**: 3 Hours (Closed Book) | **Maximum Marks**: 100  
> **Structure**: 5 Modules | Section A: 5 × 12M (with internal OR) | Section B: 5 × 8M (direct)  

---

## 📋 OFFICIAL TEE PAPER ARCHITECTURE (TEE.txt)
* **Section A (60 Marks)**: 5 Questions $\times$ 12 Marks (Questions 1 to 5). One question per module. Compulsory internal choice **"OR" format** (Both Option A and Option B fully solved below).
* **Section B (40 Marks)**: 5 Questions $\times$ 8 Marks (Questions 6 to 10). One question per module. Direct question **without subparts**.
* **Total**: 100 Marks (Exactly 20 Marks per Module: 12M in Section A + 8M in Section B).
* **Faculty Grading Strategy**: Dr. Mishra asks students to write **in their own words what they understand**, but looks for **specific bold keywords** to award marks quickly.

---

## 📑 QUICK EXAM NAVIGATION MATRIX

| Section | Q# | Module | Core Exam Topic | Marks | Format | Origin |
|:---:|:---:|:---:|:---|:---:|:---:|:---|
| **SEC A** | **Q1** | **Module 1** | [ML Lifecycle Framework (CAT-1 Q1) **OR** PAC Learning Bound Derivation](#question-1-module-1--12-marks) | 12M | 12M OR 12M | **CAT-1 Q1** / Slide Act-02 |
| **SEC A** | **Q2** | **Module 2** | [Linear Regression OLS Numerical (CAT-1 Q4) **OR** Logistic Regression vs k-NN & SVM](#question-2-module-2--12-marks) | 12M | 12M OR 12M | **CAT-1 Q4** / **CAT-1 Q3 & Q5** |
| **SEC A** | **Q3** | **Module 3** | [AdaBoost 5-Sample Weight Trace **OR** Hospital RF vs AdaBoost & K-Means](#question-3-module-3--12-marks) | 12M | 12M OR 6M+6M | Slide Act / **CAT-2 Q1 & Q3** |
| **SEC A** | **Q4** | **Module 4** | [Naïve Bayes Loan Approval (CAT-2 Q4) **OR** Apriori Grocery Mining (CAT-2 Q5)](#question-4-module-4--12-marks) | 12M | 12M OR 12M | **CAT-2 Q4** / **CAT-2 Q5** |
| **SEC A** | **Q5** | **Module 5** | [Imbalanced Data & SMOTE Math (A13) **OR** 500-Patient Confusion Matrix & RAG (A14)](#question-5-module-5--12-marks) | 12M | 12M OR 6M+6M | **Assignment 13 & 14** |
| **SEC B** | **Q6** | **Module 1** | [VC Dimension ($VC=2$ Proof) & Natarajan Multiclass Dimension](#question-6-module-1--8-marks) | 8M | Direct 8M | **CAT-1 Q2** |
| **SEC B** | **Q7** | **Module 2** | [SVM Margin Width $2/\|\mathbf{w}\|$ & Support Vectors & Kernels](#question-7-module-2--8-marks) | 8M | Direct 8M | **CAT-1 Q5** |
| **SEC B** | **Q8** | **Module 3** | [Hierarchical AGNES Clustering on $\{5, 9, 14, 25, 28, 40\}$ with Full Dendrograms](#question-8-module-3--8-marks) | 8M | Direct 8M | **CAT-2 Q2** |
| **SEC B** | **Q9** | **Module 4** | [Apriori Principle (Downward Closure) & Bayesian Belief Networks (BBN)](#question-9-module-4--8-marks) | 8M | Direct 8M | Core Syllabus / Slide Act |
| **SEC B** | **Q10**| **Module 5** | [PCA Projected Variance Maximization Derivation via Lagrange Multipliers](#question-10-module-5--8-marks) | 8M | Direct 8M | Slide 5.0 Core Derivation |

---
---

# ══════════════════════════════════════════════════
# SECTION A: 5 QUESTIONS $\times$ 12 MARKS = 60 MARKS
### *(Answer One Full Question from each Module — Internal Choice "OR" Format)*
# ══════════════════════════════════════════════════

---

# QUESTION 1 [Module 1 — 12 Marks]

### OPTION A (CAT-1 QUESTION 1 REPEAT — EASIEST TO WRITE IN YOUR OWN WORDS):
*Explain the Machine Learning Lifecycle Framework for application development in detail. Discuss all major stages from problem definition to deployment and continuous monitoring.* **[12 Marks]**

### OR

### OPTION B (MATHEMATICAL DERIVATION — SLIDE ACTIVITY-02):
*(a) What do you mean by the Probably Approximately Correct (PAC) learning framework? Define error parameter $\epsilon$ and confidence parameter $\delta$.* **[4 Marks]**  
*(b) For a finite hypothesis space $H$, derive the general PAC sample complexity bound:*  
$$m \ge \frac{1}{\epsilon} \left( \ln |H| + \ln \frac{1}{\delta} \right)$$  
*Explain in plain words what this formula means.* **[8 Marks]**

---

### MODEL EXAM ANSWER FOR QUESTION 1 (OPTION A — ML LIFECYCLE):

```text
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ 1. Problem      │ ───► │ 2. Data         │ ───► │ 3. Data         │
│    Definition   │      │    Collection   │      │    Preprocessing│
└─────────────────┘      └─────────────────┘      └────────┬────────┘
                                                           │
┌─────────────────┐      ┌─────────────────┐               │
│ 6. Deployment   │ ◄─── │ 5. Model        │ ◄─────────────┘
│    & Monitoring │      │    Evaluation   │      ┌─────────────────┐
└─────────────────┘      └─────────────────┘ ◄─── │ 4. Model        │
                                                  │    Training     │
                                                  └─────────────────┘
```

#### Explanation in Plain Words with Scoring Keywords:

1. **Stage 1: Problem Definition (Understanding the Goal)**
   - **What we do**: Before writing any code, we understand what business problem we are trying to solve (e.g. predicting whether a patient has a disease or whether a customer will churn).
   - **Key Decision**: Decide what type of ML task it is:
     - **Supervised Learning**: We have labels (e.g. Spam / Not Spam).
     - **Unsupervised Learning**: No labels, finding patterns/groups (e.g. customer segmentation).
     - **Reinforcement Learning**: Agent learns by reward and punishment (e.g. robotics, games).
   - **Keywords**: **Business Objective**, **KPIs**, **Problem Formulation**.

2. **Stage 2: Data Acquisition & Collection**
   - **What we do**: Gather data from various sources like SQL databases, sensors, web scraping, API calls, or CSV logs.
   - **Key Rule**: "Garbage in, garbage out" — the model is only as good as the data collected.
   - **Keywords**: **Data Sources**, **Data Volume**, **Data Quality**.

3. **Stage 3: Data Preprocessing & Feature Engineering**
   - **What we do**: Clean up the messy real-world data:
     - **Handling Missing Values**: Filling missing numbers using mean/median or dropping bad rows.
     - **Removing Outliers & Noise**: Filtering corrupted sensor readings.
     - **Encoding Categorical Data**: Converting words like `[Low, Medium, High]` into numbers using **One-Hot Encoding** or **Label Encoding**.
     - **Feature Scaling**: Normalizing features so large numbers don't dominate ($z = \frac{x - \mu}{\sigma}$).
   - **Keywords**: **Data Cleaning**, **Imputation**, **Normalization**, **Feature Selection**.

4. **Stage 4: Model Selection & Training**
   - **What we do**: 
     - Split data into **Training Set (70–80%)** and **Testing Set (20–30%)**.
     - Pick candidate algorithms (Decision Trees, SVM, Random Forest, Naïve Bayes).
     - Feed training data into the algorithm to let it learn mathematical patterns/weights.
     - Tune **Hyperparameters** using **K-Fold Cross Validation** to find the best settings.
   - **Keywords**: **Train/Test Split**, **Cross-Validation**, **Hyperparameter Tuning**.

5. **Stage 5: Model Evaluation & Testing**
   - **What we do**: Test the trained model on unseen test data to see if it actually works.
   - **Evaluation Metrics**:
     - Do NOT rely on accuracy alone for imbalanced data.
     - Use **Confusion Matrix**, **Precision**, **Recall**, and **F1-Score**.
   - **Check for Overfitting**: Ensure the model hasn't simply memorized the training data.
   - **Keywords**: **Confusion Matrix**, **Precision**, **Recall**, **F1-Score**, **Generalization**.

6. **Stage 6: Deployment & Continuous Monitoring**
   - **What we do**: Put the model into production as a live cloud API or Docker container so apps can use it.
   - **Ongoing Monitoring**: Watch for:
     - **Data Drift**: Incoming user data changes over time (e.g. new shopping trends).
     - **Concept Drift**: The underlying real-world relationship changes.
     - When drift happens, **retrain the model** with fresh data.
   - **Keywords**: **API Deployment**, **Data Drift**, **Concept Drift**, **Model Retraining**.

---

### MODEL EXAM ANSWER FOR QUESTION 1 (OPTION B — PAC LEARNING):

#### 1. What is PAC Learning in Plain Words?
* In real life, machine learning can almost never guarantee $100\%$ accuracy on data it has never seen before.
* Leslie Valiant created the **PAC (Probably Approximately Correct)** framework:
  1. **Approximately Correct ($\epsilon$)**: The true error of our hypothesis on future data is very small ($\le \epsilon$, e.g. $\epsilon = 5\%$).
  2. **Probably ($\delta$)**: The algorithm succeeds in finding such a good model with high confidence of at least $1 - \delta$ (e.g. $95\%$ confidence if failure rate $\delta = 5\%$).
* **Formal PAC Condition**:
  $$\mathbf{P(\text{error}(h) \le \epsilon) \ge 1 - \delta}$$
* **Keywords**: **Error Parameter $\epsilon$**, **Confidence Parameter $1-\delta$**, **Consistent Learner**.

#### 2. Derivation of Sample Complexity $m$ in 4 Simple Steps:
We want to know: **How many training examples ($m$) do we need so bad models don't fool us?**

* **Step 1: Probability ONE bad hypothesis fools us on 1 example**:
  - A hypothesis is "bad" if its true error is $> \epsilon$.
  - The chance that it happens to get 1 random example right is $< (1 - \epsilon)$.
* **Step 2: Probability ONE bad hypothesis fools us on ALL $m$ examples**:
  - Since examples are independent: $< (1 - \epsilon)^m$.
  - Using the standard math rule $(1 - x) \le e^{-x}$, this is bounded by $\le e^{-m\epsilon}$.
* **Step 3: Probability that ANY bad hypothesis in the whole hypothesis space $|H|$ fools us**:
  - By Boole's Union Bound (adding up chances for all $|H|$ hypotheses):
    $$\mathbf{P(\text{Failure}) \le |H| \cdot e^{-m\epsilon}}$$
* **Step 4: Force this failure chance to be at most $\delta$**:
  $$|H| e^{-m\epsilon} \le \delta \implies e^{-m\epsilon} \le \frac{\delta}{|H|}$$
  Take natural log ($\ln$) on both sides:
  $$-m\epsilon \le \ln\left(\frac{\delta}{|H|}\right) = -\ln\left(\frac{|H|}{\delta}\right)$$
  Multiply by $-1$ (this flips the sign from $\le$ to $\ge$):
  $$m\epsilon \ge \ln |H| + \ln\left(\frac{1}{\delta}\right) \implies \mathbf{m \ge \frac{1}{\epsilon} \left( \ln |H| + \ln \frac{1}{\delta} \right)}$$

$$\mathbf{\text{Final Boxed Result: } m \ge \frac{1}{\epsilon} \left( \ln |H| + \ln \frac{1}{\delta} \right)}$$

* **What this formula tells us**:
  1. If you want higher accuracy (smaller $\epsilon$), you need more data ($1/\epsilon$).
  2. If you want higher confidence (smaller $\delta$), you need slightly more data ($\ln(1/\delta)$).
  3. A more complex hypothesis space ($|H|$) requires more data ($\ln |H|$).

---

# QUESTION 2 [Module 2 — 12 Marks]

### OPTION A (CAT-1 QUESTION 4 REPEAT — LINEAR REGRESSION OLS NUMERICAL):
*Consider the dataset of Height ($x$ in cm) and Weight ($y$ in kg) for 10 persons below:*  

| Person | Height ($x$ in cm) | Weight ($y$ in kg) |
|:---:|:---:|:---:|
| 1 | 150 | 45 |
| 2 | 152 | 48 |
| 3 | 155 | 50 |
| 4 | 158 | 53 |
| 5 | 160 | 55 |
| 6 | 162 | 57 |
| 7 | 165 | 60 |
| 8 | 168 | 63 |
| 9 | 170 | 65 |
| 10 | 172 | 68 |

*Formulate a linear regression model $\hat{y} = mx + c$ based on the above dataset using the Ordinary Least Squares (OLS) method. Estimate the weight of a person with height 175 cm.* **[12 Marks]**

### OR

### OPTION B (SLIDE ACTIVITY A-06 & CAT-1 Q3/Q5):
*(a) Explain Logistic Regression. How does it differ from Linear Regression? Discuss the Sigmoid activation function and why Ordinary Least Squares cannot be used for classification.* **[6 Marks]**  
*(b) Explain the k-Nearest Neighbors (k-NN) classification algorithm and discuss the motivation behind Support Vector Machines (SVM).* **[6 Marks]**

---

### MODEL EXAM ANSWER FOR QUESTION 2 (OPTION A — LINEAR REGRESSION NUMERICAL):

#### 1. Formula & Summary Statistics ($N = 10$)
* **Model Equation**: $\hat{y} = mx + c$
* **Slope formula**:
  $$m = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}$$
* **Intercept formula**:
  $$c = \bar{y} - m\bar{x}$$
* **Means**:
  - $\sum x = 150 + 152 + 155 + 158 + 160 + 162 + 165 + 168 + 170 + 172 = \mathbf{1612} \implies \bar{x} = \frac{1612}{10} = \mathbf{161.2\text{ cm}}$
  - $\sum y = 45 + 48 + 50 + 53 + 55 + 57 + 60 + 63 + 65 + 68 = \mathbf{564} \implies \bar{y} = \frac{564}{10} = \mathbf{56.4\text{ kg}}$

#### 2. Computation Table
| Person ($i$) | Height $x_i$ | Weight $y_i$ | $(x_i - \bar{x})$ | $(y_i - \bar{y})$ | $(x_i - \bar{x})^2$ | $(x_i - \bar{x})(y_i - \bar{y})$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 150 | 45 | $-11.2$ | $-11.4$ | $125.44$ | $127.68$ |
| 2 | 152 | 48 | $-9.2$ | $-8.4$ | $84.64$ | $77.28$ |
| 3 | 155 | 50 | $-6.2$ | $-6.4$ | $38.44$ | $39.68$ |
| 4 | 158 | 53 | $-3.2$ | $-3.4$ | $10.24$ | $10.88$ |
| 5 | 160 | 55 | $-1.2$ | $-1.4$ | $1.44$ | $1.68$ |
| 6 | 162 | 57 | $+0.8$ | $+0.6$ | $0.64$ | $0.48$ |
| 7 | 165 | 60 | $+3.8$ | $+3.6$ | $14.44$ | $13.68$ |
| 8 | 168 | 63 | $+6.8$ | $+6.6$ | $46.24$ | $44.88$ |
| 9 | 170 | 65 | $+8.8$ | $+8.6$ | $77.44$ | $75.68$ |
| 10 | 172 | 68 | $+10.8$ | $+11.6$ | $116.64$ | $125.28$ |
| **Sum ($\sum$)** | **1612** | **564** | **0** | **0** | **505.60** | **517.20** |

#### 3. Slope ($m$) and Intercept ($c$) Calculations
* **Slope $m$**:
  $$m = \frac{517.20}{505.60} \approx \mathbf{1.023}$$
* **Intercept $c$**:
  $$c = 56.4 - (1.023 \times 161.2) = 56.4 - 164.91 = \mathbf{-108.51}$$
* **Fitted Model**:
  $$\mathbf{\hat{y} = 1.023 \cdot x - 108.51}$$
  *(Meaning: For every 1 cm increase in height, weight increases by $\approx 1.023$ kg).*

#### 4. Estimation for Height = 175 cm
$$\hat{y} = 1.023(175) - 108.51 = 179.025 - 108.51 = \mathbf{70.515\text{ kg}}$$

$$\mathbf{\text{Final Answer: Estimated Weight is } 70.52\text{ kg}}$$

---

### MODEL EXAM ANSWER FOR QUESTION 2 (OPTION B — LOGISTIC REGRESSION & k-NN):

#### 1. Logistic Regression vs Linear Regression (Slide 2.2 Activity A-06)
* **The Core Difference**:
  - **Linear Regression**: Predicts a continuous numerical value (e.g. house price, weight). Output is an unbounded straight line: $\hat{y} = \mathbf{w}^T \mathbf{x} + b \in (-\infty, +\infty)$.
  - **Logistic Regression**: Solves **binary classification** (e.g. Pass/Fail, Spam/Not Spam). It predicts the **probability** that an instance belongs to Class 1 ($P(Y=1 \mid X) \in [0, 1]$).
* **The Sigmoid Function**:
  To squash any real number into a valid probability between $0$ and $1$, we pass the linear equation through the **Sigmoid (Logistic) Function**:
  $$\mathbf{g(z) = \frac{1}{1 + e^{-z}}}, \quad \text{where } z = \mathbf{w}^T \mathbf{x} + b$$
  - When $z \to +\infty \implies g(z) \to 1$.
  - When $z \to -\infty \implies g(z) \to 0$.
  - When $z = 0 \implies g(z) = 0.5$ (Default Decision Boundary).
* **Why OLS Fails for Classification**:
  - Linear regression with OLS minimizes squared error. For classification, squared error produces a non-convex cost surface full of local minima.
  - Linear regression can output values $< 0$ or $> 1$ (impossible probabilities).
  - Outliers pull the linear boundary heavily, breaking classification. Logistic regression uses **Binary Cross-Entropy Loss** instead.
* **Keywords**: **Sigmoid Function**, **Probability Squashing**, **Decision Boundary ($0.5$)**, **Cross-Entropy Loss**.

#### 2. k-NN and SVM Motivation (CAT-1 Q3 & Q5)
* **k-NN (Instance-Based Learning)**:
  - "Tell me who your neighbors are, and I will tell you who you are."
  - **Steps**: (1) Store training points, (2) For a query point, calculate distance (Euclidean $L_2$ or Manhattan $L_1$) to all points, (3) Pick $k$ closest neighbors, (4) Assign the **majority class label**.
  - **Keywords**: **Lazy Learner**, **Distance Metrics**, **Majority Voting**.
* **SVM Motivation (Maximum Margin Hyperplane)**:
  - Standard perceptrons find *any* arbitrary line separating classes. A line that passes too close to points easily misclassifies new test data.
  - **Motivation of SVM**: Find the **Optimal Hyperplane** that maximizes the **Margin** (the empty buffer distance to the closest points of both classes). This guarantees the best generalization and robustness against noise.
  - **Keywords**: **Margin Maximization**, **Support Vectors**, **Optimal Separating Hyperplane**.

---

# QUESTION 3 [Module 3 — 12 Marks]

### OPTION A (RECOMMENDED NUMERICAL — ADABOOST):
*(a) Explain the sequential boosting paradigm of AdaBoost in simple words. How do sample weights change?* **[4 Marks]**  
*(b) Consider a training dataset of $N=5$ instances with initial uniform weights $w_i^{(1)} = 0.20$. Base classifier $h_1$ makes errors on sample 2 and sample 4, but correctly classifies samples 1, 3, and 5:*  

| Sample Index ($i$) | Feature Vector ($x_i$) | Ground Truth Label ($y_i$) | Base Classifier Prediction ($h_1(x_i)$) | Initial Weight ($w_i^{(1)}$) |
|:---:|:---:|:---:|:---:|:---:|
| 1 | $x_1$ | $+1$ | $+1$ | 0.20 |
| 2 | $x_2$ | $+1$ | $-1$ | 0.20 |
| 3 | $x_3$ | $-1$ | $-1$ | 0.20 |
| 4 | $x_4$ | $-1$ | $+1$ | 0.20 |
| 5 | $x_5$ | $+1$ | $+1$ | 0.20 |

*Compute the weighted error rate $\epsilon_1$, the classifier importance weight $\alpha_1$, the unnormalized weights, the normalization factor $Z_1$, and the updated normalized sample distribution $w_i^{(2)}$.* **[8 Marks]**

### OR

### OPTION B (CAT-2 Q1 & Q3 COMBINED):
*(a) A hospital wants to predict whether a patient is at high or low risk of a disease using clinical attributes. Design and explain the implementation of Random Forest and AdaBoost for this problem. Compare their training process, prediction mechanism, computational requirements, and expected performance. Recommend one algorithm with justification.* **[6 Marks]**  
*(b) Using K-means clustering ($k=2$), cluster dataset $D = \{3, 5, 11, 12, 19, 21, 29, 32, 45, 48\}$. Show iteration step 1 with initial centroids $m_1 = 3, m_2 = 48$.* **[6 Marks]**

---

### MODEL EXAM ANSWER FOR QUESTION 3 (OPTION A — ADABOOST):

#### 1. AdaBoost in Plain Words & Simple Memory Hook
* **What is AdaBoost?** Instead of training models independently, AdaBoost trains simple models (weak learners/stumps) **one after another in a sequence**.
* **The Weight Rule**:
  - If a model gets an example **WRONG**, AdaBoost **increases that example's weight** so the next model is forced to focus on it.
  - If a model gets an example **RIGHT**, its weight is **decreased**.
* **Final Prediction**: All models vote, but accurate models have higher voting power ($\alpha_t$):
  $$H(\mathbf{x}) = \text{sign}\left(\sum_{t=1}^T \alpha_t h_t(\mathbf{x})\right)$$

> 💡 **AdaBoost 3-Step Calculator Hook**:  
> 1. $\epsilon = \text{sum of weights of wrong examples}$.  
> 2. $\alpha = \frac{1}{2} \ln\left(\frac{1 - \epsilon}{\epsilon}\right)$ *(Think: "Log of right over wrong, halved")*.  
> 3. Multiplier: Correct $\times e^{-\alpha}$ (shrink); Wrong $\times e^{+\alpha}$ (boost). Divide all by sum $Z$.

#### 2. Step-by-Step Calculation ($N=5$)
* Misclassified samples: $x_2$ and $x_4$.
1. **Weighted Error Rate $\epsilon_1$**:
   $$\epsilon_1 = w_2^{(1)} + w_4^{(1)} = 0.20 + 0.20 = \mathbf{0.40}$$
2. **Classifier Weight $\alpha_1$**:
   $$\alpha_1 = \frac{1}{2}\ln\left(\frac{1 - 0.40}{0.40}\right) = \frac{1}{2}\ln(1.5) = \frac{0.4055}{2} = \mathbf{0.2027}$$
3. **Multiplier Factors**:
   - For correct samples: $e^{-\alpha_1} = e^{-0.2027} = \mathbf{0.8165}$
   - For incorrect samples: $e^{+\alpha_1} = e^{+0.2027} = \mathbf{1.2247}$
4. **Unnormalized Weights $\tilde{w}_i$**:
   - Correct ($1, 3, 5$): $0.20 \times 0.8165 = \mathbf{0.1633}$
   - Incorrect ($2, 4$): $0.20 \times 1.2247 = \mathbf{0.2449}$
5. **Normalization Factor $Z_1$**:
   $$Z_1 = 3(0.1633) + 2(0.2449) = 0.4899 + 0.4898 = \mathbf{0.9797}$$
6. **Final Normalized Weights $w_i^{(2)} = \frac{\tilde{w}_i}{Z_1}$**:
   - Correct ($1, 3, 5$): $\frac{0.1633}{0.9797} = \mathbf{0.1667}$
   - Incorrect ($2, 4$): $\frac{0.2449}{0.9797} = \mathbf{0.2500}$

$$\mathbf{\text{Final Boxed Weights: } w_{\text{correct}}^{(2)} = 0.1667, \quad w_{\text{error}}^{(2)} = 0.2500}$$

---

### MODEL EXAM ANSWER FOR QUESTION 3 (OPTION B — CAT-2 Q1 & Q3):

#### 1. Hospital Disease Risk: Random Forest vs AdaBoost (CAT-2 Q1)

| Feature | Random Forest (Bagging) | AdaBoost (Boosting) |
|:---|:---|:---|
| **Training Process** | **Parallel**: Builds many full decision trees independently on random subsets of data and features. | **Sequential**: Builds simple trees one by one, focusing on patients misclassified in the previous round. |
| **Prediction Method** | Simple majority vote across all trees. | Weighted vote where more accurate trees have higher influence ($\alpha_t$). |
| **Computational Needs** | High RAM (stores many deep trees), but fast to train across multiple CPU cores. | Low RAM (stores small stumps), but slow to train (must run sequentially). |
| **Robustness to Noise**| Very robust against noisy patient data and outliers. | Prone to overfitting on noisy lab readings or corrupted records. |

* **Final Recommendation**: **Random Forest is recommended**. Patient health data contains missing values, lab measurement noise, and outliers. Random Forest reduces variance, resists noise, and provides **Feature Importance** rankings so doctors can see *why* a patient is flagged as high risk.

#### 2. K-Means Trace on $D = \{3, 5, 11, 12, 19, 21, 29, 32, 45, 48\}$ (CAT-2 Q3)
* Initial centroids: $m_1 = 3, \quad m_2 = 48$.
* Midpoint boundary: $\frac{3 + 48}{2} = 25.5$.
  - Points $< 25.5 \to$ Cluster 1: $\{3, 5, 11, 12, 19, 21\}$
  - Points $> 25.5 \to$ Cluster 2: $\{29, 32, 45, 48\}$
* **New Centroids**:
  $$m_1 = \frac{3 + 5 + 11 + 12 + 19 + 21}{6} = \frac{71}{6} \approx \mathbf{11.83}$$
  $$m_2 = \frac{29 + 32 + 45 + 48}{4} = \frac{154}{4} = \mathbf{38.50}$$

---

# QUESTION 4 [Module 4 — 12 Marks / CAT-2 Q4 & Q5]

### OPTION A (CAT-2 QUESTION 4 — NAÏVE BAYES LOAN APPROVAL):
*(a) State Bayes' Theorem and explain the Naïve Bayes classification model in plain words. What is the conditional independence assumption?* **[4 Marks]**  
*(b) The loan approval dataset is given for 12 applicants:*  

| Applicant | Income | Credit History | Employment | Existing Loan | Class |
|:---:|:---:|:---:|:---:|:---:|:---:|
| A1 | High | Good | Stable | No | **Approved** |
| A2 | High | Good | Unstable | No | **Approved** |
| A3 | Medium | Good | Stable | No | **Approved** |
| A4 | High | Poor | Stable | Yes | **Rejected** |
| A5 | Low | Good | Stable | Yes | **Rejected** |
| A6 | Medium | Poor | Unstable | Yes | **Rejected** |
| A7 | Low | Poor | Unstable | Yes | **Rejected** |
| A8 | Medium | Good | Stable | No | **Approved** |
| A9 | High | Good | Stable | Yes | **Approved** |
| A10 | Low | Good | Unstable | No | **Rejected** |
| A11 | Medium | Poor | Stable | Yes | **Rejected** |
| A12 | High | Poor | Unstable | No | **Rejected** |

*Predict whether loan should be Approved or Rejected for new applicant:*  
$$X = (\text{Income} = \text{Medium}, \, \text{Credit} = \text{Good}, \, \text{Employment} = \text{Stable}, \, \text{Loan} = \text{No})$$  
*(c) Do you think attributes such as income, employment stability, and existing loans are truly independent?* **[8 Marks]**

### OR

### OPTION B (CAT-2 QUESTION 5 — APRIORI ALGORITHM):
*The market basket transaction dataset of 10 customers is given to you:*  

| Transaction ID | Items Purchased |
|:---:|:---|
| T1 | Bread, Milk, Butter |
| T2 | Bread, Milk, Eggs |
| T3 | Bread, Butter, Eggs |
| T4 | Milk, Butter, Eggs |
| T5 | Bread, Milk, Butter, Eggs |
| T6 | Bread, Milk |
| T7 | Bread, Butter |
| T8 | Milk, Butter |
| T9 | Bread, Milk, Eggs |
| T10 | Bread, Butter, Milk |

*Use the computational steps of the Apriori algorithm with minimum support count = 2 to find all frequent itemsets ($L_1, L_2, L_3$).* **[12 Marks]**

---

### MODEL EXAM ANSWER FOR QUESTION 4 (OPTION A — CAT-2 Q4):

#### 1. Part (a): Bayes' Theorem & Naïve Bayes Explained Simply
* **Bayes' Theorem Formula**:
  $$\mathbf{P(Y \mid X) = \frac{P(X \mid Y) \cdot P(Y)}{P(X)}}$$
* **What Each Term Means**:
  - **$P(Y \mid X)$ (Posterior Probability)**: The probability that applicant belongs to Class $Y$ (e.g. Approved) given their features $X$. This is what we want to calculate!
  - **$P(X \mid Y)$ (Likelihood)**: How likely we see these features $X$ among people who were already Approved.
  - **$P(Y)$ (Prior Probability)**: The overall baseline chance of getting Approved before looking at any applicant features.
  - **$P(X)$ (Evidence)**: The total probability of observing feature combination $X$. (Since $P(X)$ is identical for both Approved and Rejected, we can ignore it during comparison and normalize at the end!).
* **The "Naïve" Conditional Independence Assumption**:
  - Calculating the full joint probability $P(X_1, X_2, \dots, X_n \mid Y)$ requires huge data tables.
  - Naïve Bayes makes a simplifying ("naïve") assumption: **all features are completely independent of each other given the class label**:
    $$\mathbf{P(X_1, X_2, \dots, X_n \mid Y) = P(X_1 \mid Y) \times P(X_2 \mid Y) \times \dots \times P(X_n \mid Y)}$$
  - This allows us to simply multiply individual probabilities together!

---

#### 2. Part (b): Step-by-Step Loan Approval Numerical

#### Step 1: Prior Probabilities ($N = 12$)
* Approved applicants: A1, A2, A3, A8, A9 $\implies \mathbf{5}$
* Rejected applicants: A4, A5, A6, A7, A10, A11, A12 $\implies \mathbf{7}$
$$P(\text{Approved}) = \frac{5}{12} \approx 0.4167, \qquad P(\text{Rejected}) = \frac{7}{12} \approx 0.5833$$

#### Step 2: Likelihoods for Class = Approved ($N_{\text{App}} = 5$)
* $P(\text{Income=Medium} \mid \text{App}) = \frac{2}{5} = \mathbf{0.40}$ *(A3, A8)*
* $P(\text{Credit=Good} \mid \text{App}) = \frac{5}{5} = \mathbf{1.00}$ *(All 5)*
* $P(\text{Employment=Stable} \mid \text{App}) = \frac{4}{5} = \mathbf{0.80}$ *(A1, A3, A8, A9)*
* $P(\text{Existing Loan=No} \mid \text{App}) = \frac{4}{5} = \mathbf{0.80}$ *(A1, A2, A3, A8)*
$$\text{Likelihood Product } P(X \mid \text{App}) = 0.40 \times 1.00 \times 0.80 \times 0.80 = \mathbf{0.2560}$$
$$\text{Unnormalized Score}(\text{App}) = P(\text{App}) \times 0.2560 = \frac{5}{12} \times 0.2560 = \mathbf{0.1067}$$

#### Step 3: Likelihoods for Class = Rejected ($N_{\text{Rej}} = 7$)
* $P(\text{Income=Medium} \mid \text{Rej}) = \frac{2}{7} \approx \mathbf{0.2857}$ *(A6, A11)*
* $P(\text{Credit=Good} \mid \text{Rej}) = \frac{2}{7} \approx \mathbf{0.2857}$ *(A5, A10)*
* $P(\text{Employment=Stable} \mid \text{Rej}) = \frac{3}{7} \approx \mathbf{0.4286}$ *(A4, A5, A11)*
* $P(\text{Existing Loan=No} \mid \text{Rej}) = \frac{3}{7} \approx \mathbf{0.4286}$ *(A7, A10, A12)*
$$\text{Likelihood Product } P(X \mid \text{Rej}) = \frac{2}{7} \times \frac{2}{7} \times \frac{3}{7} \times \frac{3}{7} = \frac{36}{2401} \approx \mathbf{0.0150}$$
$$\text{Unnormalized Score}(\text{Rej}) = \frac{7}{12} \times \frac{36}{2401} = \frac{3}{343} \approx \mathbf{0.00875}$$

#### Step 4: Normalization & Classification
$$\text{Total Evidence } P(X) = 0.1067 + 0.00875 = 0.11545$$
$$P(\text{Approved} \mid X) = \frac{0.1067}{0.11545} = \mathbf{92.42\%}$$
$$P(\text{Rejected} \mid X) = \frac{0.00875}{0.11545} = \mathbf{7.58\%}$$

$$\mathbf{\text{Final Decision: The loan application is APPROVED (92.42\% probability)}}$$

#### 3. Part (c): Critical Independence Analysis
* **Are these attributes truly independent?** **NO.**
* In the real financial world:
  1. `Employment Stability` and `Income` are correlated: stable jobs provide higher and reliable income.
  2. `Existing Loans` and `Credit History` are correlated: people with multiple outstanding loans often struggle with repayments, hurting their credit rating.
* **Why Naïve Bayes still works**: Naïve Bayes does not need perfectly calibrated probabilities. It only needs to know **which score is bigger** ($0.1067 \gg 0.00875$). As long as the ranking is preserved, classification is correct!

---

### MODEL EXAM ANSWER FOR QUESTION 4 (OPTION B — CAT-2 Q5 APRIORI):

*Given: Minimum Support Count $\text{min\_sup} = 2$. Total Transactions $N = 10$.*

#### Step 1: Candidate 1-Itemsets ($C_1 \to L_1$)
Count how many transactions contain each individual item:
* $\{\text{Bread}\}: 8 \ge 2 \implies \text{Keep}$
* $\{\text{Milk}\}: 8 \ge 2 \implies \text{Keep}$
* $\{\text{Butter}\}: 7 \ge 2 \implies \text{Keep}$
* $\{\text{Eggs}\}: 5 \ge 2 \implies \text{Keep}$
$$\mathbf{L_1 = \{\{\text{Bread}\}, \{\text{Milk}\}, \{\text{Butter}\}, \{\text{Eggs}\}\}}$$

#### Step 2: Candidate 2-Itemsets ($C_2 \to L_2$)
Pair up items from $L_1$ and count occurrences:
* $\{\text{Bread}, \text{Milk}\}$: T1, T2, T5, T6, T9, T10 $\implies \mathbf{6} \ge 2$
* $\{\text{Bread}, \text{Butter}\}$: T1, T3, T5, T7, T10 $\implies \mathbf{5} \ge 2$
* $\{\text{Bread}, \text{Eggs}\}$: T2, T3, T5, T9 $\implies \mathbf{4} \ge 2$
* $\{\text{Milk}, \text{Butter}\}$: T1, T4, T5, T8, T10 $\implies \mathbf{5} \ge 2$
* $\{\text{Milk}, \text{Eggs}\}$: T2, T4, T5, T9 $\implies \mathbf{4} \ge 2$
* $\{\text{Butter}, \text{Eggs}\}$: T3, T4, T5 $\implies \mathbf{3} \ge 2$
* All 6 pairs meet $\text{min\_sup} \ge 2 \implies \mathbf{\text{All 6 survive in } L_2}$.

#### Step 3: Candidate 3-Itemsets ($C_3 \to L_3$)
Combine pairs into triplets and count occurrences:
* $\{\text{Bread}, \text{Milk}, \text{Butter}\}$: T1, T5, T10 $\implies \mathbf{3} \ge 2$
* $\{\text{Bread}, \text{Milk}, \text{Eggs}\}$: T2, T5, T9 $\implies \mathbf{3} \ge 2$
* $\{\text{Bread}, \text{Butter}, \text{Eggs}\}$: T3, T5 $\implies \mathbf{2} \ge 2$
* $\{\text{Milk}, \text{Butter}, \text{Eggs}\}$: T4, T5 $\implies \mathbf{2} \ge 2$
* All 4 triplets meet $\text{min\_sup} \ge 2 \implies \mathbf{\text{All 4 survive in } L_3}$.

#### Step 4: Candidate 4-Itemsets ($C_4 \to L_4$)
* Candidate: $\{\text{Bread}, \text{Milk}, \text{Butter}, \text{Eggs}\}$.
* Appears only in T5 $\implies \text{Count} = 1 < 2$. **Pruned (Below minimum support)!**
* **Algorithm Terminates.**

---

# QUESTION 5 [Module 5 — 12 Marks / Assignments 13 & 14]

### OPTION A (RECOMMENDED — ASSIGNMENT 13):
*(a) Explain the concept of imbalanced datasets. Discuss causes, characteristics, and why accuracy can be misleading, illustrating with a numerical proof on a 1,000-patient clinical cohort.* **[6 Marks]**  
*(b) Detail the complete working mechanism of SMOTE. Given seed minority instance $\mathbf{x}_i = [2.0, 4.0]$, neighbor $\mathbf{x}_{zi} = [6.0, 10.0]$, and random interpolation parameter $\lambda = 0.5$, compute the synthetic coordinates. Compare Random Oversampling (ROS) vs SMOTE.* **[6 Marks]**

### OR

### OPTION B (CONFUSION MATRIX & ASSIGNMENT 14 RAG):
*(a) A clinical diagnostic model for detecting a rare cardiac disease is tested on 500 patients: $TP=45, FP=15, FN=5, TN=435$. Calculate Accuracy, Precision, Recall, Specificity, and F1-Score.* **[6 Marks]**  
*(b) Investigate Enterprise RAG (Retrieval-Augmented Generation) as a modern machine learning technology trend impacting modern business innovations.* **[6 Marks]**

---

### MODEL EXAM ANSWER FOR QUESTION 5 (OPTION A — ASSIGNMENT 13):

#### 1. Imbalanced Datasets & The Accuracy Paradox (Plain Words)
* **What is an Imbalanced Dataset?** It is a dataset where one class (majority) heavily outnumbers the other class (minority), such as $99:1$ or $99.9:0.1$. Real examples: credit card fraud, cancer screening, factory defects.
* **The Accuracy Paradox (1,000-Patient Proof)**:
  - Suppose a hospital tests $1,000$ patients: **$990$ are Healthy (Negative)** and **$10$ have Cancer (Positive)**.
  - A lazy model that predicts **"Healthy" for every single person** produces:
    - $TP = 0, \quad FP = 0, \quad TN = 990, \quad FN = 10$.
  - Let us calculate the metrics:
    $$\mathbf{\text{Accuracy} = \frac{TP + TN}{N} = \frac{0 + 990}{1000} = 99.0\%}$$
    $$\mathbf{\text{Recall (Sensitivity)} = \frac{TP}{TP + FN} = \frac{0}{0 + 10} = 0.0\%}$$
  - **The Clinical Disaster**: The model looks amazing on paper ($99.0\%$ accuracy), but it has **$0\%$ recall**! All 10 cancer patients are sent home undiagnosed and will die.
  - **Conclusion**: **Accuracy is deceptive and useless for imbalanced data**. We must use **Precision**, **Recall**, and **F1-Score**.

![Classification Metrics and Confusion Matrix](images/confusion_matrix_and_metrics.svg)

---

#### 2. SMOTE Working Mechanism & Coordinate Math
* **What SMOTE does (Synthetic Minority Over-sampling Technique)**:
  Instead of just copying existing minority points, SMOTE **creates brand-new synthetic points** between neighboring minority points.
* **3-Step Mechanism**:
  1. For a minority point $\mathbf{x}_i$, find its $k$-nearest neighbors from the minority class (usually $k=5$).
  2. Pick one random neighbor $\mathbf{x}_{zi}$.
  3. Draw an imaginary line between $\mathbf{x}_i$ and $\mathbf{x}_{zi}$, and pick a random point on that line using random number $\lambda \in [0, 1]$:
     $$\mathbf{x}_{\text{new}} = \mathbf{x}_i + \lambda \cdot (\mathbf{x}_{zi} - \mathbf{x}_i)$$

![SMOTE Synthetic Sample Interpolation](images/smote_synthetic_interpolation.svg)

* **Coordinate Numerical**:
  - Seed: $\mathbf{x}_i = [2.0, 4.0]$, Neighbor: $\mathbf{x}_{zi} = [6.0, 10.0]$, $\lambda = 0.5$.
  - Step 1 (Difference vector): $[6.0 - 2.0, \; 10.0 - 4.0] = [4.0, 6.0]$
  - Step 2 (Scale by $\lambda$): $0.5 \times [4.0, 6.0] = [2.0, 3.0]$
  - Step 3 (Add to seed): $[2.0, 4.0] + [2.0, 3.0] = \mathbf{[4.0, \; 7.0]}$

$$\mathbf{\text{Final Boxed Result: } \mathbf{x}_{\text{new}} = [4.0, \; 7.0]}$$

#### 3. Random Oversampling (ROS) vs SMOTE
| Feature | Random Oversampling (ROS) | SMOTE (Synthetic Oversampling) |
|:---|:---|:---|
| **How it Works** | Simply makes duplicate clones of existing minority rows. | Generates brand-new synthetic data points along lines. |
| **Risk of Overfitting** | **High**: Model memorizes the exact copied data points. | **Low**: Broadens the minority decision region. |
| **Speed** | Extremely fast ($O(N)$). | Slower ($O(N^2)$ because of finding $k$-nearest neighbors). |

---

# ══════════════════════════════════════════════════
# SECTION B: 5 QUESTIONS $\times$ 8 MARKS = 40 MARKS
### *(Compulsory Direct Questions Without Subparts — 1 from Each Module)*
# ══════════════════════════════════════════════════

---

# QUESTION 6 [Module 1 — 8 Marks / CAT-1 Q2]

### Question:
*What do you mean by Version space learning? Define Vapnik-Chervonenkis (VC) Dimension. Prove that the VC dimension of 1D closed intervals is 2. Define the Natarajan Dimension and explain its role in multiclass PAC learnability.* **[8 Marks]**

---

### MODEL EXAM ANSWER:

#### 1. Version Space Learning in Plain Words
* **Version Space ($VS_{H, D}$)**: The collection of all hypotheses in our hypothesis space $H$ that get **$100\%$ of the training examples right** in dataset $D$:
  $$VS_{H, D} = \{h \in H \mid \forall (x, y) \in D, h(x) = y\}$$
* Rather than listing thousands of hypotheses, we bound the Version Space between two limits:
  - **General Boundary ($G$)**: The most general hypotheses consistent with the data.
  - **Specific Boundary ($S$)**: The most specific hypotheses consistent with the data.

#### 2. VC Dimension & Proof ($VC = 2$) in Plain Words
* **Shattering**: A model "shatters" a set of data points if it can assign **every possible $+/-$ combination of labels** ($2^N$ combinations) to those points without making mistakes.
* **VC Dimension**: The **maximum number of points** that the model is able to shatter.
* **Proof that $VC(\text{1D Closed Intervals}) = 2$**:
  - An interval $[a, b]$ labels numbers inside as $+1$, and numbers outside as $-1$.
  - **Can it shatter 2 points ($x_1=1, x_2=3$)?** **YES.**  
    There are $2^2 = 4$ combinations: $(--), (+-), (-+), (++)$. We can slide or stretch the interval $[a, b]$ to easily create all 4 combinations $\implies VC \ge 2$.
  - **Can it shatter 3 points ($x_1 < x_2 < x_3$)?** **NO.**  
    Consider the combination **$(+1, -1, +1)$** (endpoints are $+1$, middle point is $-1$).  
    To enclose $x_1$ and $x_3$, the interval MUST start before $x_1$ and end after $x_3$ ($a \le x_1$ and $x_3 \le b$).  
    Because $x_2$ is in the middle ($x_1 < x_2 < x_3$), $x_2$ is **physically trapped inside the interval**, forcing its label to be $+1$. It is impossible to label $x_2$ as $-1$!  
    Therefore, no 3 points can be shattered.

$$\mathbf{\text{Conclusion: } VC(\text{1D Closed Intervals}) = 2}$$

#### 3. Natarajan Dimension (Multiclass Version)
* **Limitation of VC Dimension**: VC dimension was designed strictly for **binary classification** ($2$ classes).
* **Natarajan Dimension**: The mathematical extension of VC dimension to **multiclass problems** ($3+$ classes).
* **Key Significance**: A multiclass hypothesis space is PAC-learnable if and only if its Natarajan dimension is finite: $\mathbf{N_{\dim}(H) < \infty}$.

---

# QUESTION 7 [Module 2 — 8 Marks / CAT-1 Q5]

### Question:
*What is the motivation for the Support Vector Machine (SVM) algorithm towards modeling classification problems? Derive the margin width $M = \frac{2}{\|\mathbf{w}\|}$ from canonical hyperplanes. Explain the role of Support Vectors, Slack Variables, and the Kernel Trick.* **[8 Marks]**

---

### MODEL EXAM ANSWER:

#### 1. Motivation of SVM
Standard algorithms (like Perceptrons) find *any* arbitrary line that separates classes. If the line passes too close to training points, even tiny noise in new test data causes misclassifications.  
**SVM Motivation**: Find the unique **Optimal Hyperplane** that maximizes the empty buffer zone (called the **Margin**) between classes, giving maximum robustness and best generalization on unseen data.

#### 2. Margin Width Derivation ($M = \frac{2}{\|\mathbf{w}\|}$)
* Separating Hyperplane equation: $\mathbf{w}^T \mathbf{x} + b = 0$.
* The closest points lie on the two parallel margin boundary lines:
  $$\text{Positive Boundary: } \mathbf{w}^T \mathbf{x}_+ + b = +1$$
  $$\text{Negative Boundary: } \mathbf{w}^T \mathbf{x}_- + b = -1$$
* Subtract the two equations:
  $$\mathbf{w}^T (\mathbf{x}_+ - \mathbf{x}_-) = 2$$
* To get the physical width $M$, project the vector $(\mathbf{x}_+ - \mathbf{x}_-)$ onto the unit normal vector $\frac{\mathbf{w}}{\|\mathbf{w}\|}$:
  $$M = (\mathbf{x}_+ - \mathbf{x}_-) \cdot \frac{\mathbf{w}}{\|\mathbf{w}\|} = \frac{\mathbf{w}^T (\mathbf{x}_+ - \mathbf{x}_-)}{\|\mathbf{w}\|} = \mathbf{\frac{2}{\|\mathbf{w}\|}}$$
* **Core Takeaway**: To maximize the margin $\frac{2}{\|\mathbf{w}\|}$, we minimize $\frac{1}{2}\|\mathbf{w}\|^2$.

![Support Vector Machine Hyperplane and Maximum Margin](images/svm_hyperplane_margin.svg)

#### 3. Support Vectors, Slack Variables & Kernel Trick
* **Support Vectors**: The critical training points that lie directly ON the margin boundaries. The entire boundary is calculated **only from these points**! If you delete all other non-support vector points, the hyperplane does not move at all.
* **Slack Variables ($\xi_i \ge 0$)**: In the real world, data is not perfectly separable. We add slack variables $\xi_i$ to allow points to slightly violate the margin (Soft Margin SVM). Parameter $C$ controls the penalty: large $C$ strictly forbids errors (risks overfitting); small $C$ allows minor errors to keep the margin wide.
* **The Kernel Trick**: When data cannot be separated by a flat line, we map points to a higher dimension $\phi(\mathbf{x})$. Instead of doing expensive high-dimensional math, a **Kernel function** $K(\mathbf{x}_i, \mathbf{x}_j) = \phi(\mathbf{x}_i)^T \phi(\mathbf{x}_j)$ computes the result directly in the original space (e.g. Polynomial, Gaussian RBF).

---

# QUESTION 8 [Module 3 — 8 Marks / CAT-2 Q2]

### Question:
*Consider a one-dimensional dataset $D = \{5, 9, 14, 25, 28, 40\}$. Perform hierarchical clustering to determine clusters using single-linkage and complete-linkage analysis, plot the respective dendrograms to visualize results, and suggest key inferences to distinguish between them.* **[8 Marks]**

---

### MODEL EXAM ANSWER:

#### 1. Initial Distance Setup
Points: $5, 9, 14, 25, 28, 40$.  
Adjacent pairwise distances:
$$d(5, 9)=4, \quad d(9, 14)=5, \quad d(14, 25)=11, \quad d(25, 28)=\mathbf{3}, \quad d(28, 40)=12$$

---

#### 2. Single Linkage Execution ($d_{\min} = \text{Minimum Distance}$)
* **Merge 1**: Global minimum distance is $d(25, 28) = \mathbf{3} \implies$ **Merge $\{25, 28\}$ at height $h = 3$**.
* **Merge 2**: Next minimum is $d(5, 9) = \mathbf{4} \implies$ **Merge $\{5, 9\}$ at height $h = 4$**.
* **Merge 3**: Distance $d(\{5, 9\}, 14) = \min(|5-14|, |9-14|) = \min(9, 5) = \mathbf{5} \implies$ **Merge $\{5, 9, 14\}$ at height $h = 5$**.
* **Merge 4**: Distance $d(\{5, 9, 14\}, \{25, 28\}) = \min|14-25| = \mathbf{11} \implies$ **Merge $\{5, 9, 14, 25, 28\}$ at height $h = 11$**.
* **Merge 5**: Connect to $\{40\}$ at distance $\min|28-40| = \mathbf{12} \implies$ **Merge all at height $h = 12$**.

```text
Single Linkage Dendrogram:
Height
  12 |                         ┌─────── 40
  11 |             ┌───────────┴─────── (25, 28)
   5 |     ┌───────┴─────── 14
   4 |  ┌──┴── 9
   3 |  │               ┌─── 28
   0 └──┴───────────────┴───────────────
        5      9   14   25   28    40
```

---

#### 3. Complete Linkage Execution ($d_{\max} = \text{Maximum Distance}$)
* **Merge 1**: Merge $\{25, 28\}$ at height $h = 3$.
* **Merge 2**: Merge $\{5, 9\}$ at height $h = 4$.
* **Merge 3**: Distance $d(\{5, 9\}, 14) = \max(|5-14|, |9-14|) = \max(9, 5) = \mathbf{9} \implies$ **Merge $\{5, 9, 14\}$ at height $h = 9$**.
* **Merge 4**: Compare candidates:
  - $d(\{5, 9, 14\}, \{25, 28\}) = \max|5-28| = 23$.
  - $d(\{25, 28\}, 40) = \max(|25-40|, |28-40|) = \mathbf{15}$.
  - The smaller distance is $15 \implies$ **Merge $\{25, 28\}$ with $\{40\}$ into $\{25, 28, 40\}$ at height $h = 15$!**
* **Merge 5**: Final merge at height $\max|5-40| = \mathbf{35}$.

```text
Complete Linkage Dendrogram:
Height
  35 |             ┌──────────────────────┐
     |             │                      │
  15 |             │              ┌───────┴─────── 40
     |             │              │       ┌─────── 28
   9 |     ┌───────┴─────── 14    └───┬───┘
   4 |  ┌──┴── 9                      │
   3 |  │                             └─── 25
   0 └──┴─────────────────────────────────────────
        5      9   14             25      28      40
```

#### 4. Key Inferences:
* **The Chaining Effect**: Single linkage causes long, straggly "chains" of clusters because single intermediate points (like 14) act as bridges between distant clusters.
* **Compactness**: Complete linkage forms tight, spherical clusters because it groups $\{25, 28\}$ with 40 first, avoiding chaining.

---

# QUESTION 9 [Module 4 — 8 Marks]

### Question:
*(a) Explain the Apriori Principle and the Downward Closure Property in Association Rule Mining. How does candidate pruning reduce computational search space?* **[4 Marks]**  
*(b) Define Bayesian Belief Networks (BBN). Explain how Directed Acyclic Graphs (DAGs) and Conditional Probability Tables (CPTs) represent joint probability distributions.* **[4 Marks]**

---

### MODEL EXAM ANSWER:

#### 1. Apriori Principle & Downward Closure (Plain Words)
* **What is Association Rule Mining?** Finding items that customers frequently buy together (e.g. Milk and Bread).
* **The Apriori Principle**:
  $$\mathbf{\text{All non-empty subsets of a frequent itemset must also be frequent.}}$$
* **Downward Closure (The Pruning Rule)**:
  - If a small itemset is **infrequent**, then **any bigger itemset containing it CANNOT be frequent**.
  - **Pruning in Action**: If $\{D\}$ is purchased only once (infrequent), we **immediately prune and throw away** $\{A, D\}, \{B, D\}, \{A, B, D\}$ without ever wasting time searching the database!
  - This reduces the computational search space from millions of combinations to just a tiny handful.
* **Keywords**: **Support Threshold**, **Downward Closure**, **Anti-Monotonicity**, **Search Space Pruning**.

#### 2. Bayesian Belief Networks (BBN) (Plain Words)
* **Why BBN?** Standard Naïve Bayes makes the unrealistic assumption that *every* feature is completely independent. In real life, features have selective causal links (e.g. Smoking causes Lung Cancer). BBN captures these real relationships.
* **Two Core Parts**:
  1. **Directed Acyclic Graph (DAG)**:
     - Nodes represent variables.
     - Directed arrows represent direct cause-and-effect (Parent $\to$ Child).
     - Missing arrows mean conditional independence.
  2. **Conditional Probability Tables (CPTs)**:
     - Every node stores a small table listing probabilities given its direct parents: $P(X_i \mid \text{Parents}(X_i))$.
* **Chain Rule**: The full joint probability is simply the product of each node conditioned on its parents:
  $$\mathbf{P(X_1, X_2, \dots, X_n) = \prod_{i=1}^n P(X_i \mid \text{Parents}(X_i))}$$
* **Keywords**: **DAG**, **Causal Relationship**, **Conditional Probability Tables (CPTs)**, **Chain Rule**.

---

# QUESTION 10 [Module 5 — 8 Marks / Slide 5.0 Core Derivation]

### Question:
*Derive the first principal component projection vector in Principal Component Analysis (PCA) by maximizing projected variance using Lagrange Multipliers. Prove that the optimal projection vector is the eigenvector corresponding to the maximum eigenvalue of the covariance matrix.* **[8 Marks]**

---

### MODEL EXAM ANSWER:

#### 1. What is PCA Trying to Do? (Plain Words)
* We have centered data (mean $\mathbf{\bar{x}} = \mathbf{0}$) with sample covariance matrix $\mathbf{\Sigma} = \frac{1}{m} \mathbf{X}_c^T \mathbf{X}_c$.
* We want to find a 1D direction vector $\mathbf{u}_1$ such that when we project our data onto it, **the spread (variance) of the points is as large as possible**.
* To prevent $\mathbf{u}_1$ from growing infinitely large, we enforce the constraint that $\mathbf{u}_1$ is a unit vector: $\mathbf{u}_1^T \mathbf{u}_1 = 1$.

#### 2. Derivation in 5 Clean Steps:

* **Step 1: Formula for Projected Variance**:
  The projection of point $\mathbf{x}_i$ onto unit vector $\mathbf{u}_1$ is $z_i = \mathbf{x}_i^T \mathbf{u}_1$.  
  The variance $\sigma_z^2$ of these projected points is:
  $$\sigma_z^2 = \frac{1}{m} \sum z_i^2 = \mathbf{u}_1^T \left( \frac{1}{m}\mathbf{X}_c^T \mathbf{X}_c \right) \mathbf{u}_1 = \mathbf{u}_1^T \mathbf{\Sigma} \mathbf{u}_1$$

* **Step 2: Set up Constrained Optimization**:
  $$\max_{\mathbf{u}_1} \mathbf{u}_1^T \mathbf{\Sigma} \mathbf{u}_1 \quad \text{subject to } \mathbf{u}_1^T \mathbf{u}_1 = 1$$

* **Step 3: Combine using Lagrange Multiplier $\lambda$**:
  $$\mathcal{L}(\mathbf{u}_1, \lambda) = \mathbf{u}_1^T \mathbf{\Sigma} \mathbf{u}_1 - \lambda (\mathbf{u}_1^T \mathbf{u}_1 - 1)$$

* **Step 4: Take Derivative and Set to Zero**:
  Differentiate $\mathcal{L}$ with respect to $\mathbf{u}_1$:
  $$\frac{\partial \mathcal{L}}{\partial \mathbf{u}_1} = 2 \mathbf{\Sigma} \mathbf{u}_1 - 2 \lambda \mathbf{u}_1 = \mathbf{0} \implies \mathbf{\mathbf{\Sigma} \mathbf{u}_1 = \lambda \mathbf{u}_1}$$

* **Step 5: Conclusion & Proof**:
  1. The condition $\mathbf{\Sigma} \mathbf{u}_1 = \lambda \mathbf{u}_1$ is the textbook definition of an **Eigenvector** and **Eigenvalue**! Therefore, $\mathbf{u}_1$ must be an eigenvector of covariance matrix $\mathbf{\Sigma}$.
  2. Pre-multiply both sides by $\mathbf{u}_1^T$:
     $$\mathbf{u}_1^T \mathbf{\Sigma} \mathbf{u}_1 = \lambda (\mathbf{u}_1^T \mathbf{u}_1) = \mathbf{\lambda}$$
  3. The projected variance is directly equal to the eigenvalue $\lambda$.
  4. To achieve **maximum projected variance**, $\mathbf{u}_1$ must be chosen as the eigenvector corresponding to the **largest eigenvalue $\lambda_{\max}$**.

$$\mathbf{\text{Q.E.D. The optimal projection vector is the eigenvector for } \lambda_{\max}.}$$

![PCA Variance Maximization and Orthogonal Axes](images/pca_variance_maximization.svg)
