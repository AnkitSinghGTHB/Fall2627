# 📘 Unit 3: Sequential Logic Circuits, Flip-Flops & State Reduction

---

## 1. Latches vs Flip-Flops & Timing Parameters

* **Latch**: Level-sensitive bistable storage element (output changes continuously as long as the clock/enable is high).
* **Flip-Flop**: Edge-triggered storage element (output changes strictly on the rising $\uparrow$ or falling $\downarrow$ clock transition edge).
* **Setup Time ($t_{su}$)**: The minimum time the data input must remain stable **before** the active clock edge.
* **Hold Time ($t_h$)**: The minimum time the data input must remain stable **after** the active clock edge.
* **Metastability**: An indeterminate output state occurring if setup or hold times are violated.

---

## 2. Flip-Flop Master Characteristics & Excitation Matrix

### 2.1 Characteristic Equations
* **SR Flip-Flop**: $Q_{n+1} = S + R' Q_n$ (Constraint: $S \cdot R = 0$)
* **JK Flip-Flop**: $Q_{n+1} = J Q_n' + K' Q_n$
* **D Flip-Flop**: $Q_{n+1} = D$
* **T Flip-Flop**: $Q_{n+1} = T \oplus Q_n = T Q_n' + T' Q_n$

### 2.2 Master Excitation Table (Used in all Counter & Conversion Designs)

| Present State $Q_n$ | Next State $Q_{n+1}$ | $S$ | $R$ | $J$ | $K$ | $D$ | $T$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$0$** | **$0$** | $0$ | $X$ | $0$ | $X$ | $0$ | $0$ |
| **$0$** | **$1$** | $1$ | $0$ | $1$ | $X$ | $1$ | $1$ |
| **$1$** | **$0$** | $0$ | $1$ | $X$ | $1$ | $0$ | $1$ |
| **$1$** | **$1$** | $X$ | $0$ | $X$ | $0$ | $1$ | $0$ |

---

## 3. The Race-Around Condition & Master-Slave JK

* **Definition**: In a level-triggered JK flip-flop, when $J = 1$ and $K = 1$, the output toggles. If the clock pulse width $t_p$ is greater than the propagation delay $t_{pd}$ of the flip-flop ($t_p > t_{pd}$), the output will toggle multiple times during a single clock pulse, settling into an unpredictable random state when the clock drops low.
* **Three Solutions**:
  1. **Master-Slave JK Architecture**: Uses two cascaded flip-flops. The Master is active when $CLK = 1$; the Slave is active when $CLK = 0$ (via an inverter). Output updates strictly on the trailing edge.
  2. **Edge-Triggered Flip-Flops**: Internal steering circuits restrict the active window to nanosecond transition edges.
  3. **Pulse-Narrowing Circuits**: Differentiator network ensuring $t_p \ll t_{pd}$.

---

## 4. Universal Flip-Flop Conversion Algorithm

To convert **Available Flip-Flop ($A$)** to **Target Flip-Flop ($B$)**:
1. Construct table containing: Target Inputs, Present State $Q_n$, Next State $Q_{n+1}$.
2. Insert excitation columns for the Available Flip-Flop inputs.
3. Solve K-maps for each Available FF input in terms of (Target Inputs + $Q_n$).

```
Example: Convert Available JK Flip-Flop into a T Flip-Flop:
+----------+-------+---------+-------+-------+
| Target T |  Q_n  | Q_{n+1} |   J   |   K   |
+----------+-------+---------+-------+-------+
|    0     |   0   |    0    |   0   |   X   |
|    0     |   1   |    1    |   X   |   0   |
|    1     |   0   |    1    |   1   |   X   |
|    1     |   1   |    0    |   X   |   1   |
+----------+-------+---------+-------+-------+
K-Map for J(T, Q_n): J = T
K-Map for K(T, Q_n): K = T
Result: Tie inputs J and K together and label as input T!
```

---

## 5. State Reduction via Implication Chart Method

Reduces the number of states in a sequential circuit to minimize flip-flops and gate count:
1. Construct the lower-triangular chart comparing each state pair $(S_i, S_j)$.
2. An entry $(S_i, S_j)$ is an immediate mismatch ($\times$) if their outputs differ for any input combination.
3. If outputs match, write the implied next-state pairs into the square.
4. Iterate through the grid: Cross out squares if any of their implied state pairs have been crossed out.
5. Combine remaining uncrossed squares into merged equivalence sets.

---

## 6. Model Exam Questions & Answers

### Question 1 (12 Marks)
**Convert a JK flip-flop into a D flip-flop. Show the conversion table, K-maps, Boolean expressions, and complete logic circuit diagram.**

**Solution**:
1. **Target FF**: D Flip-Flop.  
   **Available FF**: JK Flip-Flop.
2. **Conversion Table**:

| Target Input $D$ | Present State $Q_n$ | Next State $Q_{n+1}$ | Available $J$ | Available $K$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | $X$ |
| 0 | 1 | 0 | $X$ | 1 |
| 1 | 0 | 1 | 1 | $X$ |
| 1 | 1 | 1 | $X$ | 0 |

3. **K-Map Simplifications**:
   - For $J(D, Q_n)$:
     - Cell $(0, 0) = 0$, Cell $(0, 1) = X$, Cell $(1, 0) = 1$, Cell $(1, 1) = X$.  
     - Grouping row $D = 1 \implies \mathbf{J = D}$.
   - For $K(D, Q_n)$:
     - Cell $(0, 0) = X$, Cell $(0, 1) = 1$, Cell $(1, 0) = X$, Cell $(1, 1) = 0$.  
     - Grouping row $D = 0 \implies \mathbf{K = D'}$.
4. **Circuit Diagram**: Connect input $D$ directly to terminal $J$. Connect $D$ through a NOT gate into terminal $K$. Connect common clock to CLK pin.

### Question 2 (8 Marks)
**Explain the Race-Around Condition in JK flip-flops. How does the Master-Slave JK flip-flop eliminate this condition? Draw its circuit diagram and timing waveform.**

**Solution**:
1. **Mechanism**: Occurs when $J=1, K=1$, level-triggered clock pulse width $t_p > t_{pd}$. The output oscillates continuously between 0 and 1 during the clock pulse.
2. **Master-Slave Elimination Principle**:
   - When Clock $= 1$: Master latch is enabled, receiving external $J, K$ inputs and updating intermediate internal states ($Y, Y'$). Slave latch is disabled because inverter provides Clock $= 0$.
   - When Clock drops to $0$: Master latch is disabled, locking its state. Slave latch is enabled, passing Master's state to external outputs ($Q, Q'$).
   - Because Master and Slave are never simultaneously active, closed feedback oscillation is physically impossible.
