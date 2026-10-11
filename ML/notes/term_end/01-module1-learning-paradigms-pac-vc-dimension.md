# 📘 Unit 1: Learning Paradigms, Concept Learning & Computational Learning Theory

---

## 1. Machine Learning Foundations & Paradigms

### 1.1 Formal Definition of Machine Learning (Tom Mitchell)
> "A computer program is said to **learn** from experience $E$ with respect to some class of tasks $T$ and performance measure $P$, if its performance at tasks in $T$, as measured by $P$, improves with experience $E$."

* **Example (Autonomous Vehicle)**:
  - Task $T$: Navigating urban streets without collision.
  - Performance Measure $P$: Average distance traveled without safety intervention.
  - Experience $E$: Database of recorded camera feeds, LiDAR point clouds, and human driver steering corrections.

### 1.2 Learning Paradigms Comparative Table

| Learning Paradigm | Training Data Nature | Primary Objective | Concrete Real-World Example |
|:---|:---|:---|:---|
| **Supervised Learning** | Labeled pairs: $\{(\mathbf{x}_i, y_i)\}$ | Learn a mapping function $f: \mathcal{X} \to \mathcal{Y}$ | Medical image tumor diagnosis, Spam email filter |
| **Unsupervised Learning** | Unlabeled data: $\{\mathbf{x}_i\}$ | Discover intrinsic cluster structure, manifold, or density | Customer market segmentation, Anomaly detection |
| **Semi-Supervised Learning** | Small labeled set + Massive unlabeled set | Leverage data manifold to improve decision boundary | Webpage classification, Speech acoustic modeling |
| **Reinforcement Learning** | States, actions, reward signals $r_t$ | Learn an optimal policy $\pi^*(s)$ maximizing expected discounted return | AlphaGo, Robotic manipulator balance control |

---

## 2. Concept Learning & Version Spaces

### 2.1 Find-S Algorithm (Maximally Specific Hypothesis)
1. Initialize hypothesis $h$ to the most specific constraint in $H$:
   $$h \leftarrow \langle \Phi, \Phi, \Phi, \Phi, \Phi, \Phi \rangle$$
2. For each positive training instance $x$:
   - For each attribute constraint $a_i$ in $h$:
     - If the constraint $a_i$ is satisfied by $x$, do nothing.
     - Else, replace $a_i$ in $h$ by the next more general constraint satisfied by $x$ (use `?` if mismatch occurs).
3. Ignore all negative instances!
4. Output hypothesis $h$.

### 2.2 Candidate Elimination Algorithm & Version Space
* **Version Space ($VS_{H,D}$)**: The subset of hypotheses from $H$ that are consistent with all training examples in $D$.
* Represented compactly by two boundaries:
  - **General Boundary ($G$)**: The set of maximally general members of $H$ consistent with $D$.
  - **Specific Boundary ($S$)**: The set of maximally specific members of $H$ consistent with $D$.
* **Algorithm Steps**:
  - Initialize $G_0 \leftarrow \langle ?, ?, ?, ?, ?, ? \rangle$ and $S_0 \leftarrow \langle \Phi, \Phi, \Phi, \Phi, \Phi, \Phi \rangle$.
  - For positive instance $d$: Generalize $S$ to accommodate $d$; remove hypotheses from $G$ inconsistent with $d$.
  - For negative instance $d$: Specialize $G$ to exclude $d$; remove hypotheses from $S$ inconsistent with $d$.

---

## 3. Computational Learning Theory: PAC Learning & VC Dimension

### 3.1 PAC Learning (Probably Approximately Correct)
A concept class $C$ is **PAC-learnable** if an algorithm $L$ can, with probability at least $(1 - \delta)$, output a hypothesis $h$ with true error $\text{error}(h) \le \epsilon$, using a polynomial number of samples and computation time.
* **Sample Complexity Bound for Finite Hypothesis Spaces ($|H| < \infty$)**:
  $$m \ge \frac{1}{\epsilon} \left( \ln |H| + \ln \frac{1}{\delta} \right)$$
  - Demonstrates that required sample size grows logarithmically with hypothesis space size $|H|$, and inversely with target error $\epsilon$.

### 3.2 VC Dimension (Vapnik-Chervonenkis Dimension)
* **Shattering**: A set of instances $S$ is **shattered** by a hypothesis space $H$ if and only if for every possible binary labeling of $S$, there exists some hypothesis in $H$ consistent with that labeling ($2^{|S|}$ possible labelings).
* **VC Dimension ($VC(H)$)**: The maximum number of points that can be shattered by $H$.
* **Key Values for Exam**:
  - Linear separator in 2D plane: **$VC = 3$** (Can shatter any 3 non-collinear points; cannot shatter 4 points due to XOR placement).
  - Linear separator in $d$-dimensional space: **$VC = d + 1$**.
  - 1D Intervals on real line: **$VC = 2$**.
  - Convex polygons in 2D plane: **$VC = \infty$** (An $n$-gon can shatter any set of $n$ points placed on a circle).
* **Sample Complexity Bound for Infinite $H$ using VC Dimension**:
  $$m \ge \frac{1}{\epsilon} \left( 4 \log_2 \frac{2}{\delta} + 8 \, VC(H) \log_2 \frac{13}{\epsilon} \right)$$

---

## 4. Model Exam Questions & Answers

### Question 1 (12 Marks)
**Explain the Candidate Elimination Algorithm with a complete trace for a concept with attributes: `Sky` (Sunny, Rainy), `AirTemp` (Warm, Cold), `Wind` (Strong, Weak). Show the evolution of $S$ and $G$ boundaries for:**  
**1. `(Sunny, Warm, Strong)` : Yes**  
**2. `(Sunny, Warm, Weak)` : Yes**  
**3. `(Rainy, Cold, Strong)` : No**

**Solution**:
1. **Initialization**:
   $$S_0 = \langle \Phi, \Phi, \Phi \rangle$$
   $$G_0 = \langle ?, ?, ? \rangle$$
2. **Instance 1 (Positive)**: `(Sunny, Warm, Strong) [+]`:
   $$S_1 = \langle \text{Sunny, Warm, Strong} \rangle$$
   $$G_1 = \langle ?, ?, ? \rangle$$
3. **Instance 2 (Positive)**: `(Sunny, Warm, Weak) [+]`:
   - Attributes `Sky` and `AirTemp` match; `Wind` differs (`Strong` vs `Weak`) $\implies$ Generalize `Wind` to `?`.
   $$S_2 = \langle \text{Sunny, Warm, ?} \rangle$$
   $$G_2 = \langle ?, ?, ? \rangle$$
4. **Instance 3 (Negative)**: `(Rainy, Cold, Strong) [-]`:
   - Specialize $G$ to exclude this negative instance while remaining consistent with $S_2$:
   - `Sky = Sunny` excludes `Rainy`.
   - `AirTemp = Warm` excludes `Cold`.
   $$G_3 = \{ \langle \text{Sunny, ?, ?} \rangle, \langle \text{?, Warm, ?} \rangle \}$$
   $$S_3 = \langle \text{Sunny, Warm, ?} \rangle$$
5. **Final Version Space**: Contains hypotheses consistent between $S_3$ and $G_3$.

### Question 2 (8 Marks)
**Define VC Dimension and Shattering. Prove that the VC dimension of a linear decision boundary in 2-dimensional space is 3.**

**Solution**:
1. **Definitions**:
   - *Shattering*: An inductive bias can realize all $2^N$ dichotomies on $N$ points.
   - *VC Dimension*: Cardinality of the largest subset of points shattered.
2. **Proof that $VC(\text{Linear 2D}) \ge 3$**:
   - Take 3 non-collinear points in 2D forming a triangle.
   - There are $2^3 = 8$ possible labelings: all positive, all negative, and combinations of 1 vs 2 points.
   - Any point can be separated from the other two by a straight line. Thus, 3 points can be shattered $\implies VC \ge 3$.
3. **Proof that $VC(\text{Linear 2D}) < 4$**:
   - For any 4 points in a 2D plane:
     - Case A: 3 points form a triangle enclosing the 4th point. If the 3 outer points are labeled $+1$ and the interior point is $-1$, no straight line can separate them without cutting the triangle.
     - Case B: 4 points form a convex quadrilateral. If diagonal pairs are assigned alternating labels (XOR configuration: $P_1, P_3 = +1$ and $P_2, P_4 = -1$), no single line can separate them.
   - Since no set of 4 points can be shattered, $VC = \mathbf{3}$.
