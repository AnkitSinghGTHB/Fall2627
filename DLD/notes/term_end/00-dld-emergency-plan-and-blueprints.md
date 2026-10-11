# ⏱️ ECE2002: DLD Emergency Plan & The 5 Master Blueprints

> **Exam Date**: Friday, October 16, 2026 (01:15 PM – 04:15 PM)  
> **Critical Trap**: DLD is the very next day after TOC (Exam on Oct 15). **You have ZERO gap days!**  
> **Solution**: Execute the 3-Hour Pre-load on Oct 11, so Thursday night (Oct 15) is purely 2 hours of rapid circuit review.

---

## 🎯 The 5 Master Blueprints (Guaranteed 60+ Marks)

### Blueprint 1: The Universal Flip-Flop Conversion Recipe (10–12 Marks)
Whenever asked to convert **Available Flip-Flop (e.g., JK)** into **Target Flip-Flop (e.g., D or T)**:
1. Identify **Inputs of Target Flip-Flop** and **Present State $Q_n$**.
2. Write the **Next State $Q_{n+1}$** using the target FF's characteristic behavior.
3. Fill in the **Excitation Inputs of the Available FF** needed to drive $Q_n \to Q_{n+1}$.
4. Draw K-Maps for each Available FF input in terms of (Target Inputs + $Q_n$).
5. Write the simplified equations and draw the combined logic diagram.

---

### Blueprint 2: Synchronous Counter Design Recipe (12 Marks)
Designing an arbitrary sequence counter (e.g., $0 \to 4 \to 6 \to 1 \to 3 \to 7 \to 2 \to 5 \to 0$ or Modulo-$N$):
1. **Determine Flip-Flop Count**: $2^n \ge N$.
2. **State Transition Table**:
   - Column 1: Present State $(Q_A, Q_B, Q_C)_n$
   - Column 2: Next State $(Q_A, Q_B, Q_C)_{n+1}$
   - Column 3: Excitation inputs for chosen FFs (D, JK, or T).
3. **K-Map Simplification**: One K-map per flip-flop input. Unused states are marked as **Don't Care ($X$)**.
4. **Self-Starting Check**: Verify where unused states transition. If they transition back into the valid cycle, the counter is self-correcting; otherwise, add lockout logic.
5. **Logic Schematic**: Draw flip-flops with a shared global clock.

---

### Blueprint 3: Implication Chart State Reduction (10–12 Marks)
1. Construct the lower triangular Implication Table comparing every state pair $(S_i, S_j)$.
2. Cross out $(\times)$ any pair with different outputs for the same input.
3. For pairs with identical outputs, enter the implied next-state pairs.
4. Pass through the table iteratively: cross out any square whose implied pair has been crossed out.
5. Combine remaining uncrossed pairs into equivalent state classes; draw the reduced state diagram.

---

### Blueprint 4: Sequence Detector FSM Design (10–12 Marks)
Detecting a binary sequence (e.g., `1010` or `1101`), overlapping vs non-overlapping:
* **Overlapping**: The suffix of a detected sequence can serve as the prefix of the next sequence.
* **Non-Overlapping**: The machine resets to initial state $S_0$ immediately after detection.
* **Number of States**:
  - **Mealy Machine**: $N$ states for an $N$-bit sequence (output on transition edge).
  - **Moore Machine**: $N + 1$ states for an $N$-bit sequence (output associated with state).

---

### Blueprint 5: Verilog HDL Module & Testbench Template (10–12 Marks)
Standard 4-to-1 Multiplexer in Behavioral Verilog:

```verilog
module mux4to1 (
    input [3:0] in,
    input [1:0] sel,
    output reg y
);
    always @(*) begin
        case (sel)
            2'b00: y = in[0];
            2'b01: y = in[1];
            2'b10: y = in[2];
            2'b11: y = in[3];
            default: y = 1'b0;
        endcase
    end
endmodule
```
