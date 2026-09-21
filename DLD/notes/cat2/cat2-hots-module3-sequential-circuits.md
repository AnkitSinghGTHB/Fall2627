# ⚡ CAT-2 HOTS Master Crib — Module 3: Flip-Flops, Conversions & Shift Registers
**Course**: ECE2002 — Digital Logic Design  
**Level**: Self-Contained & Fully Visual (Zero-Assumption Bedrock Basics to Circuit Schematics)  
**Exam Mode**: Open Book / Handwritten Notes Allowed | **Target Score**: 45+ / 50

---

## 🧱 TIER 0: The "Explain Like I'm 5" Bedrock Basics
*(Read this first if flip-flops and sequential circuits confuse you)*

### 1. What is a Flip-Flop?
A combinational circuit (like an Adder) has **no memory** — output depends solely on current inputs.
A **sequential circuit** has **memory**: it remembers past states!
* The fundamental 1-bit memory cell is a **Flip-Flop**.
* Flip-flops change their state **only when a Clock edge arrives** (Positive Edge $\uparrow$ or Negative Edge $\downarrow$).

---

### 2. The 4 Fundamental Flip-Flops (Visual Circuit Schematics)

#### A. The SR (Set-Reset) Flip-Flop
* **Concept**: 
  * $S=1, R=0 \implies$ **SET** ($Q=1$).
  * $S=0, R=1 \implies$ **RESET** ($Q=0$).
  * $S=0, R=0 \implies$ **HOLD** (No change, $Q^+=Q$).
  * $S=1, R=1 \implies$ **INVALID / FORBIDDEN!** Both $Q$ and $Q'$ try to become 0 simultaneously, violating the rule that $Q' = \overline{Q}$.

![Clocked SR Flip-Flop Logic Circuit](circuits/circuit_a4_q1_sr_latch.png)
*(Figure 3.1: Clocked SR Flip-Flop using NAND steering gates and cross-coupled latch with S=1, R=1 metastability protection)*

* **Characteristic Equation**: $\mathbf{Q^+ = S + R' Q}$ (with constraint $S \cdot R = 0$).
* **Excitation Table (How to force transitions)**:
  $$\begin{array}{|c|c|c|c|} \hline Q & Q^+ & S & R \\ \hline 0 & 0 & 0 & X \\ 0 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 \\ 1 & 1 & X & 0 \\ \hline \end{array}$$

---

#### B. The JK Flip-Flop (Fixing the SR Flaw)
* **The Breakthrough**: In SR, $S=1, R=1$ caused a crash. In JK, we feed $Q$ and $Q'$ back to the inputs!
* When $J=1, K=1$, the output **TOGGLES** (inverts: $0 \to 1$ and $1 \to 0$)! No invalid state exists!

![Clocked JK Flip-Flop Logic Circuit](circuits/circuit_m3_jk_ff.png)
*(Figure 3.2: Clocked JK Flip-Flop with cross-coupled feedback loops from $Q$ and $\overline{Q}$ to steering gates, solving the forbidden state through toggle mode $Q^+ = \overline{Q}$)*

* **Characteristic Equation**: $\mathbf{Q^+ = J Q' + K' Q}$
* **JK Truth Table & Modes**:
  $$\begin{array}{|c|c|c|l|} \hline J & K & Q^+ & \textbf{Operating Mode} \\ \hline 0 & 0 & Q & \text{No Change (Hold)} \\ 0 & 1 & 0 & \text{Reset} \\ 1 & 0 & 1 & \text{Set} \\ 1 & 1 & Q' & \textbf{Toggle (Invert)} \\ \hline \end{array}$$
* **JK Excitation Table (CRITICAL FOR COUNTER DESIGN!)**:
  $$\begin{array}{|c|c|c|c|} \hline Q & Q^+ & J & K \\ \hline 0 & 0 & 0 & X \\ 0 & 1 & 1 & X \\ 1 & 0 & X & 1 \\ 1 & 1 & X & 0 \\ \hline \end{array}$$

---

#### C. The D (Data / Delay) Flip-Flop
* **Concept**: Takes whatever single bit is on input $D$ and transfers it to output $Q$ on the next clock edge.
* **Circuit**: Made from an SR or JK flip-flop by connecting an **inverter (NOT gate)** between inputs ($K = \overline{J}$).

![D and T Flip-Flop Derivations from JK Core](circuits/circuit_m3_d_and_t_ff.png)
*(Figure 3.3: D Flip-Flop built from JK core with inverter $K = \overline{D}$, ensuring $Q^+ = D$; and T Flip-Flop built by tying inputs $J = K = T$ for toggle operation $Q^+ = T \oplus Q$)*

* **Characteristic Equation**: $\mathbf{Q^+ = D}$
* **Excitation Table**: $D = Q^+$ (Whatever next state you want, set $D$ to that value!).

---

#### D. The T (Toggle) Flip-Flop
* **Concept**: Has 1 control input $T$.
  * If $T = 0 \implies$ Hold state ($Q^+ = Q$).
  * If $T = 1 \implies$ Toggle state ($Q^+ = Q'$).
* **Circuit**: Made from JK by **tying inputs J and K together** ($J = K = T$) (see Figure 3.3 right panel).

* **Characteristic Equation**: $\mathbf{Q^+ = T \oplus Q = T Q' + T' Q}$
* **Excitation Table**: $\mathbf{T = Q \oplus Q^+}$
  $$\begin{array}{|c|c|c|} \hline Q & Q^+ & T \\ \hline 0 & 0 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \\ \hline \end{array}$$

---

### 3. Master-Slave JK Flip-Flop (Solving the Race-Around Condition)

#### What is the "Race-Around Condition"?
* When $J=1$ and $K=1$ in a level-triggered flip-flop, the output toggles.
* If the clock pulse width ($t_p$) is **longer than the propagation delay of the flip-flop ($t_{pd}$)**:
  $$t_p > t_{pd}$$
* The output toggles repeatedly, oscillating wildly between $0$ and $1$ multiple times during a single clock pulse! At the end of the pulse, the final state is **unpredictable**!

#### How Master-Slave Eliminates Race-Around:
* Uses **two separate stages**:
  1. **Master Stage**: Clocked directly by $\text{CLK}$. Accepts inputs while $\text{CLK}=1$; Slave is inactive.
  2. **Slave Stage**: Clocked by inverted clock ($\overline{\text{CLK}}$). When $\text{CLK}$ drops to $0$, Master shuts off, and Slave copies Master's output to $Q$!
* Because Master and Slave are **never active at the same instant**, feedback during a single clock pulse is physically impossible!

![Master-Slave JK Flip-Flop Architecture](circuits/circuit_m3_master_slave_jk.png)
*(Figure 3.4: Master-Slave JK Flip-Flop architecture eliminating the race-around condition via dual-stage inverted clocking $\text{CLK}$ and $\overline{\text{CLK}}$)*

---

### 4. Universal Flip-Flop Conversion Blueprint

To convert an **Available Flip-Flop** (e.g. JK) into a **Target Flip-Flop** (e.g. D or T):
1. Draw the **Target FF Truth Table** (Inputs + Present state $Q \to$ Next state $Q^+$).
2. Append the **Available FF Excitation Columns** required to produce that transition.
3. Solve K-Maps for Available FF inputs in terms of Target inputs and $Q$.
4. Draw the combinational steering circuit!

![Universal Flip-Flop Conversion Blueprint](circuits/circuit_m3_ff_conversion.png)
*(Figure 3.5: Universal Flip-Flop Conversion Architecture — Target inputs and present state $Q$ enter combinational steering gates derived from K-Maps to drive the available flip-flop)*

#### Solved Conversion: Convert JK to D Flip-Flop
$$\begin{array}{|c|c|c|c|c|} \hline \textbf{Target Input } D & Q & Q^+ & \textbf{Required } J & \textbf{Required } K \\ \hline 0 & 0 & 0 & 0 & X \\ 0 & 1 & 0 & X & 1 \\ 1 & 0 & 1 & 1 & X \\ 1 & 1 & 1 & X & 0 \\ \hline \end{array}$$
* K-Map for $J$: $J = D \cdot Q' + D \cdot Q = \mathbf{D}$
* K-Map for $K$: $K = D' \cdot Q + D' \cdot Q' = \mathbf{D'}$
* **Circuit**: Connect $D$ directly to $J$, and connect $\overline{D}$ (via NOT gate) to $K$!

---

### 5. Shift Register Architectures (Full Visual Schematics)

#### A. 4-Bit Serial-In Serial-Out (SISO):
Data enters serially at FF3, shifts right on each clock edge, and leaves serially at FF0.
* **Clock pulses to load 4 bits**: $N = 4$.
* **Clock pulses to unload 4 bits**: $N - 1 = 3$.
* **Total pulses**: $2N - 1 = \mathbf{7\text{ pulses}}$.

![4-Bit SISO Shift Register Circuit](circuits/circuit_a5_q3_siso_shift_register.png)
*(Figure 3.6: 4-Bit Serial-In Serial-Out (SISO) Shift Register — Serial data cascades across 4 D flip-flops; total latency = $2N - 1 = 7$ clock pulses)*

---

#### B. 4-Bit Serial-In Parallel-Out (SIPO):
Data enters serially, but all flip-flop outputs ($Q_3, Q_2, Q_1, Q_0$) are available simultaneously.
* **Clock pulses to load & read**: Exactly $\mathbf{N = 4\text{ pulses}}$ (0 pulses to read).

![4-Bit SIPO Shift Register Circuit](circuits/circuit_m3_sipo_register.png)
*(Figure 3.7: 4-Bit Serial-In Parallel-Out (SIPO) Shift Register — 4 pulses to load serially, 0 pulses to read all 4 bits in parallel simultaneously)*

---

#### C. 4-Bit Parallel-In Serial-Out (PISO):
Requires a **$\text{Shift} / \overline{\text{Load}}$** control line to select between parallel loading ($X_3 \dots X_0$) and serial shifting.
* When $\text{Shift} / \overline{\text{Load}} = 0$: Parallel data $X_i$ loads into flip-flops.
* When $\text{Shift} / \overline{\text{Load}} = 1$: Data shifts right towards the serial output.
* **Steering Logic per Stage**: $D_i = (\text{Shift} \cdot Q_{i+1}) + (\overline{\text{Shift}} \cdot X_i)$

![4-Bit PISO Shift Register Circuit](circuits/circuit_m3_piso_register.png)
*(Figure 3.8: 4-Bit Parallel-In Serial-Out (PISO) Shift Register with 2:1 multiplexers steered by $\text{Shift}/\overline{\text{Load}}$ control line)*

---

#### D. 4-Bit Parallel-In Parallel-Out (PIPO):
Highest throughput: Loads all bits in parallel on 1 clock pulse, and reads them all in parallel on 1 clock pulse.
* **Total clock pulses**: **1 pulse**!

![4-Bit PIPO Shift Register Circuit](circuits/circuit_m3_pipo_register.png)
*(Figure 3.9: 4-Bit Parallel-In Parallel-Out (PIPO) Register — Instant 1-clock load ($N=1$) and 0-clock parallel read for maximum data throughput)*

---

#### E. Ring Counter vs. Johnson Counter Feedback Loops

![Ring Counter vs Johnson Counter Feedback Topologies](circuits/circuit_m3_ring_johnson_counters.png)
*(Figure 3.10: Shift Register Counter Topologies — 4-bit Ring Counter ($Q_0 \to D_3$, $\text{MOD}=N=4$) vs 4-bit Johnson Twisted-Ring Counter ($\overline{Q_0} \to D_3$, $\text{MOD}=2N=8$))*

* **Ring Counter**:
  * Modulus: $\text{MOD} = N = 4$ states: $\text{1000} \to \text{0100} \to \text{0010} \to \text{0001} \to \text{1000}$.
  * Needs pre-loading a '1' on startup.
* **Johnson Counter (Twisted-Ring)**:
  * Modulus: $\text{MOD} = 2N = 8$ states.
  * Self-starts from `0000`. Each state decoded by a single 2-input AND gate!

---

#### F. 4-Bit Universal Shift Register (IC 74LS194 Architecture):
The most versatile register architecture. It can hold data, shift right, shift left, or load parallel data based on two mode select lines ($S_1, S_0$):
* Uses **one 4:1 Multiplexer per Flip-Flop stage**:

| $S_1$ | $S_0$ | **Operating Mode** | **Action at each stage $i$** |
| :---: | :---: | :--- | :--- |
| **0** | **0** | **Hold (No Change)** | $D_i = Q_i$ (Connects flip-flop output back to its own input) |
| **0** | **1** | **Shift Right** | $D_i = Q_{i+1}$ (Takes output from stage to the left; Stage 3 takes Serial In $SR$) |
| **1** | **0** | **Shift Left** | $D_i = Q_{i-1}$ (Takes output from stage to the right; Stage 0 takes Serial In $SL$) |
| **1** | **1** | **Parallel Load** | $D_i = I_i$ (Loads independent parallel inputs $I_3, I_2, I_1, I_0$) |

![Universal Shift Register IC 74LS194 Single Stage](circuits/circuit_m3_usr_stage.png)
*(Figure 3.11: Single stage $i$ of 4-Bit Universal Shift Register (IC 74LS194) steered by 4:1 multiplexer with mode lines $S_1, S_0$ for Hold, Shift Right, Shift Left, and Parallel Load)*

---

### 6. State Reduction & State Assignment (FSM Optimization)

#### A. State Reduction (Implication Table / Partitioning Method)
Why reduce states? **Fewer states = Fewer flip-flops and cheaper combinational logic!**
* Two states $S_a$ and $S_b$ are **equivalent ($S_a \equiv S_b$)** $\iff$ For every possible input $x$:
  1. They produce the **exact same output** ($Y_a = Y_b$).
  2. Their next states are either identical, or themselves equivalent!

#### The Implication Table Method (Step-by-Step):
1. Construct a triangular grid with all pairs of states $(S_i, S_j)$.
2. If outputs for any input differ $\implies$ Immediately **cross out with an 'X'** (non-equivalent).
3. If outputs are identical $\implies$ Write down the **required next-state pairs** that must be equivalent.
4. Pass through the table: If a required pair is crossed out, cross out this cell too!
5. Any squares remaining without an 'X' are **equivalent states** and can be merged into a single state!

---

#### B. State Assignment Rules (Encoding States into Binary)
For $m$ states, the number of flip-flops $n$ required satisfies:
$$2^{n-1} < m \le 2^n \implies n = \lceil \log_2 m \rceil$$

* **Binary / Gray Encoding**: Uses minimum number of flip-flops ($n$). Assign adjacent states bit patterns that differ by only 1 bit to minimize K-Map groupings.
* **One-Hot Encoding**: Uses **1 flip-flop per state** ($n = m$ flip-flops, e.g. State 0 = `0001`, State 1 = `0010`, State 2 = `0100`, State 3 = `1000`).
  * *Advantage*: Zero decoding logic needed! State is read directly from flip-flop outputs. Ideal for high-speed FPGAs.
  * *Disadvantage*: Requires more flip-flops.

---

## 🧭 TIER 1: The Problem Symptom & Keyword Decoder

| If Question Shows / Asks... | It Means This Exact Topic | What You Do (In 5 Seconds) |
| :--- | :--- | :--- |
| "Convert Flip-Flop A to Flip-Flop B" | **Universal FF Conversion** | Write Target truth table $\to$ add Excitation columns for Available FF $\to$ solve K-Maps for inputs. |
| "Explain Race-Around condition & solution" | **Master-Slave JK Flip-Flop** | State condition $t_p > t_{pd}$ with $J=K=1$. Draw Master-Slave block diagram with clock inverter. |
| "Load 1111 into 4-bit SISO/SIPO", clock trace | **Shift Register Timing Table** | Table: Clock $1 \dots 7$. Trace shift of bits stage by stage. SISO takes 7 pulses, SIPO takes 4. |
| "Universal Shift Register (IC 74LS194)" | **Bidirectional Shift Register** | Mode select $S_1 S_0$: $00$ Hold, $01$ Shift Right, $10$ Shift Left, $11$ Parallel Load. Draw 4:1 MUX stage. |
| "Reduce states using implication chart" | **State Reduction** | Triangular table $\to$ cross out pairs with different outputs $\to$ test remaining pairs for next-state equivalence. |
| "Analysis of sequential circuit given logic diagram" | **Sequential Circuit Analysis** | Write input equations $\to$ substitute into characteristic equation for $Q^+ \to$ build State Table $\to$ draw State Diagram. |

---

## 📝 TIER 4: Solved Classroom & Exam Archetypes

### Classroom Problem 1: 4-Bit SISO Shift Register Trace (Loading & Unloading `1111`)
*(From Class Notes Module 3 Page 1)*  
**Question**: A 4-bit Serial-In Serial-Out (SISO) register initially holds `0000`. Trace the loading of `1111` and complete unloading to zero.

$$\begin{array}{|c|c|c|c|c|c|c|}
\hline
\textbf{Clock Pulse} & \textbf{Serial In } (D_3) & Q_3 & Q_2 & Q_1 & Q_0 & \textbf{Serial Out } (Q_0) \\ \hline
\text{Initial} & - & 0 & 0 & 0 & 0 & 0 \\
\text{CP 1} & 1 & 1 & 0 & 0 & 0 & 0 \\
\text{CP 2} & 1 & 1 & 1 & 0 & 0 & 0 \\
\text{CP 3} & 1 & 1 & 1 & 1 & 0 & 0 \\
\text{CP 4} & 1 & \mathbf{1} & \mathbf{1} & \mathbf{1} & \mathbf{1} & \mathbf{1} \text{ (Fully Loaded!)} \\ \hline
\text{CP 5} & 0 & 0 & 1 & 1 & 1 & \mathbf{1} \\
\text{CP 6} & 0 & 0 & 0 & 1 & 1 & \mathbf{1} \\
\text{CP 7} & 0 & 0 & 0 & 0 & 1 & \mathbf{1} \text{ (Fully Unloaded!)} \\ \hline
\end{array}$$

---

### Classroom Problem 2: 4-Bit Johnson Counter Decoding Table
*(From Class Notes Module 3 Page 2)*  
A 4-bit Johnson counter uses inverted feedback ($D_3 = Q_0'$). Every state is decoded using a single 2-input AND gate:

$$\begin{array}{|c|c|c|c|c|c|}
\hline
\textbf{Clock Pulse} & Q_3 & Q_2 & Q_1 & Q_0 & \textbf{Decoded State AND Equation} \\ \hline
0 & 0 & 0 & 0 & 0 & Q_3' Q_0' \\
1 & 1 & 0 & 0 & 0 & Q_3 Q_2' \\
2 & 1 & 1 & 0 & 0 & Q_2 Q_1' \\
3 & 1 & 1 & 1 & 0 & Q_1 Q_0' \\
4 & 1 & 1 & 1 & 1 & Q_3 Q_0 \\
5 & 0 & 1 & 1 & 1 & Q_3' Q_2 \\
6 & 0 & 0 & 1 & 1 & Q_2' Q_1 \\
7 & 0 & 0 & 0 & 1 & Q_1' Q_0 \\ \hline
\end{array}$$

---

### Classroom Problem 3: Convert SR Flip-Flop to JK Flip-Flop
**Goal**: Build a JK flip-flop using an SR flip-flop and combinational gates.

#### Step 1: Combined Conversion Table
$$\begin{array}{|c|c|c|c|c|c|}
\hline
J & K & Q & Q^+ & \textbf{Required } S & \textbf{Required } R \\ \hline
0 & 0 & 0 & 0 & 0 & X \\
0 & 0 & 1 & 1 & X & 0 \\
0 & 1 & 0 & 0 & 0 & X \\
0 & 1 & 1 & 0 & 0 & 1 \\
1 & 0 & 0 & 1 & 1 & 0 \\
1 & 0 & 1 & 1 & X & 0 \\
1 & 1 & 0 & 1 & 1 & 0 \\
1 & 1 & 1 & 0 & 0 & 1 \\ \hline
\end{array}$$

#### Step 2: K-Map Simplification
* **For S**: Grouping 1s and Xs gives:
  $$\mathbf{S = J \cdot Q'}$$
* **For R**: Grouping 1s and Xs gives:
  $$\mathbf{R = K \cdot Q}$$

#### Step 3: Hardware Schematic
Connect a 2-input AND gate feeding into $S$ with inputs $J$ and $Q'$. Connect a 2-input AND gate feeding into $R$ with inputs $K$ and $Q$!

---

### Classroom Problem 4: Assignment 4 Q1 — SR Flip-Flop Input Pulses & Invalid State Analysis
*(From Assignment-4 Problem 1)*  
**Question**: An SR flip-flop is initially in RESET state ($Q_0 = 0$). The following inputs are applied for 5 consecutive clock pulses:
* CP 1: $S=1, R=0$
* CP 2: $S=0, R=0$
* CP 3: $S=0, R=1$
* CP 4: $S=1, R=1$ (Forbidden input!)
* CP 5: $S=0, R=0$

#### Step-by-Step State Trace:
$$\begin{array}{|c|c|c|c|c|l|}
\hline
\textbf{Clock Pulse} & S & R & Q_{prev} & Q_{next} & \textbf{Action / Physical Explanation} \\ \hline
\text{Initial} & - & - & - & 0 & \text{Reset State} \\
\text{CP 1} & 1 & 0 & 0 & \mathbf{1} & \text{SET operation: Output transitions to 1} \\
\text{CP 2} & 0 & 0 & 1 & \mathbf{1} & \text{HOLD operation: Output retains previous value (1)} \\
\text{CP 3} & 0 & 1 & 1 & \mathbf{0} & \text{RESET operation: Output transitions to 0} \\
\text{CP 4} & 1 & 1 & 0 & \mathbf{0^*} & \textbf{INVALID STATE: In NOR latch, both } Q=0 \text{ and } Q'=0! \\
\text{CP 5} & 0 & 0 & 0^* & \mathbf{?} & \textbf{METASTABLE RACE: Unpredictable final state!} \\ \hline
\end{array}$$

#### Physical Analysis of the Invalid Condition ($S=1, R=1$):
1. In a NOR-gate latch, when $S=1$ and $R=1$, both outputs are physically forced to **$Q = 0$ and $Q' = 0$**. This violates the complementary property ($Q' = \overline{Q}$).
2. When the inputs switch simultaneously from $11 \to 00$ (CP 5), both NOR gates try to switch to 1 at the same time. Whichever gate has a fractionally shorter propagation delay will win the race.
3. The latch enters **metastability** (unpredictable oscillation or random latching to 0 or 1). That is why $S=1, R=1$ is strictly forbidden!

---

### Classroom Problem 5: Assignment 4 Q2 — Positive Edge-Triggered T Flip-Flop Using NAND Gates Only
*(From Assignment-4 Problem 2)*  
**Goal**: Draw the logic diagram using ONLY NAND gates and trace the output waveform $Q(t)$ when initially HIGH ($Q_0 = 1$).

#### 1. Logic Diagram using NAND Gates:
A positive edge-triggered T flip-flop consists of a steering pulse stage followed by cross-coupled NAND latch with feedback:
* Cross-couple outputs $Q$ and $Q'$ back to input NAND gates.
* When $T=1$, the clock pulse passes through the input gate connected to the opposite state, causing the output to toggle on every rising edge ($\uparrow$).

![Positive Edge-Triggered T Flip-Flop NAND Logic](circuits/circuit_a4_q2_nand_t_ff.png)
*(Figure 3.12: Positive Edge-Triggered T Flip-Flop implemented strictly with 2-input and 3-input NAND gates)*

![T Flip-Flop 6-Clock Cycle Waveform Timing](circuits/circuit_a4_q2_waveform.png)
*(Figure 3.13: Ideal timing diagram showing 6-clock-edge transition trace with initial state $Q_0 = 1$)*

#### 2. 6-Clock Pulse Transition Trace (Initially $Q_0 = 1$):
Assume $T = [1, 0, 1, 1, 0, 1]$ applied across 6 positive clock edges:
$$\begin{array}{|c|c|c|c|l|}
\hline
\textbf{Clock Edge } (\uparrow) & T & Q_{prev} & Q_{next} & \textbf{Behavior} \\ \hline
\text{Initial} & - & - & \mathbf{1} & \text{Given initially HIGH} \\
1\uparrow & 1 & 1 & \mathbf{0} & T=1 \implies \text{Toggle: } 1 \to 0 \\
2\uparrow & 0 & 0 & \mathbf{0} & T=0 \implies \text{Hold: remains } 0 \\
3\uparrow & 1 & 0 & \mathbf{1} & T=1 \implies \text{Toggle: } 0 \to 1 \\
4\uparrow & 1 & 1 & \mathbf{0} & T=1 \implies \text{Toggle: } 1 \to 0 \\
5\uparrow & 0 & 0 & \mathbf{0} & T=0 \implies \text{Hold: remains } 0 \\
6\uparrow & 1 & 0 & \mathbf{1} & T=1 \implies \text{Toggle: } 0 \to 1 \\ \hline
\end{array}$$
* **Waveform Description**: Output $Q(t)$ stays constant during the clock low/high periods, and transitions **only at the instant of the positive clock edge** if $T=1$. Frequency of $Q(t)$ is half of the clock frequency when $T$ is held continuously at 1 (Divide-by-2 frequency divider!).

