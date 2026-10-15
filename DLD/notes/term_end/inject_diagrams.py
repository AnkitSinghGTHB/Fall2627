# -*- coding: utf-8 -*-
"""
Inject interactive Mermaid diagrams and images into:
08-dld-faculty-imp-curated-master-solutions.md
"""
import os

target_file = r"c:\Users\ankit\Fall2627\DLD\notes\term_end\08-dld-faculty-imp-curated-master-solutions.md"

with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. RTL Schematic Mermaid
rtl_mermaid = """
```mermaid
graph TD
    subgraph Inputs
        A["Input A (0V / 3.6V)"] -->|RB = 450 Ohms| B1["Base of Q1"]
        B["Input B (0V / 3.6V)"] -->|RB = 450 Ohms| B2["Base of Q2"]
    end
    subgraph Power_Supply
        VCC["Vcc (+3.6V)"] --> RC["Collector Resistor Rc (640 Ohms)"]
    end
    RC --> NodeY["Collector Node (Output Y)"]
    NodeY --> C1["Collector of Q1"]
    NodeY --> C2["Collector of Q2"]
    B1 --> Q1["Transistor Q1 (NPN)"]
    B2 --> Q2["Transistor Q2 (NPN)"]
    C1 --> Q1
    C2 --> Q2
    Q1 --> GND["Ground (0V)"]
    Q2 --> GND
    NodeY --> Y["Output Y = (A + B)' [NOR Gate]"]
```
"""
content = content.replace("#### 1. Circuit Schematic:\n```", "#### 1. Circuit Schematic:\n" + rtl_mermaid + "\n```")

# 2. BCD to Excess-3 Mermaid
bcd_mermaid = """
```mermaid
graph LR
    subgraph BCD_Inputs["BCD Inputs (0000 to 1001)"]
        A["A (MSB)"]
        B["B"]
        C["C"]
        D["D (LSB)"]
    end
    subgraph Logic_Circuitry["Combinational Converter Logic"]
        EqW["W = A + B(C + D)"]
        EqX["X = B ⊕ (C + D)"]
        EqY["Y = (C ⊕ D)'"]
        EqZ["Z = D'"]
    end
    subgraph Excess3_Outputs["Excess-3 Outputs (0011 to 1100)"]
        W["W (MSB)"]
        X["X"]
        Y["Y"]
        Z["Z (LSB)"]
    end
    A --> EqW --> W
    B --> EqW
    C --> EqW
    D --> EqW
    B --> EqX --> X
    C --> EqX
    D --> EqX
    C --> EqY --> Y
    D --> EqY
    D --> EqZ --> Z
```
"""
content = content.replace("#### Step 4: Logic Schematic", "#### Step 4: Logic Schematic\n" + bcd_mermaid)

# 3. Binary to Gray Mermaid
bin_gray_mermaid = """
```mermaid
graph LR
    B3["Binary Input B3 (MSB)"] --> G3["Gray Output G3"]
    B3 --> XOR1["XOR Gate 1"]
    B2["Binary Input B2"] --> XOR1 --> G2["Gray Output G2"]
    B2 --> XOR2["XOR Gate 2"]
    B1["Binary Input B1"] --> XOR2 --> G1["Gray Output G1"]
    B1 --> XOR3["XOR Gate 3"]
    B0["Binary Input B0 (LSB)"] --> XOR3 --> G0["Gray Output G0"]
```
"""
content = content.replace("* **Hardware**: Exactly **3 XOR gates**.", "* **Hardware**: Exactly **3 XOR gates**.\n" + bin_gray_mermaid)

# 4. Decoder Full Adder Mermaid
decoder_fa_mermaid = """
```mermaid
graph LR
    subgraph Inputs
        A["Input A"]
        B["Input B"]
        Cin["Input Cin"]
    end
    subgraph Decoder["3:8 Active-Low Decoder (74LS138)"]
        Y1["Y1 (m1')"]
        Y2["Y2 (m2')"]
        Y3["Y3 (m3')"]
        Y4["Y4 (m4')"]
        Y5["Y5 (m5')"]
        Y6["Y6 (m6')"]
        Y7["Y7 (m7')"]
    end
    A --> Decoder
    B --> Decoder
    Cin --> Decoder
    Y1 --> NAND_SUM["4-Input NAND Gate"]
    Y2 --> NAND_SUM
    Y4 --> NAND_SUM
    Y7 --> NAND_SUM
    NAND_SUM --> Sum["Sum S = Σm(1,2,4,7)"]
    Y3 --> NAND_CARRY["4-Input NAND Gate"]
    Y5 --> NAND_CARRY
    Y6 --> NAND_CARRY
    Y7 --> NAND_CARRY
    NAND_CARRY --> Cout["Carry Cout = Σm(3,5,6,7)"]
```
"""
content = content.replace("- Total hardware: **One 3:8 Decoder + Two 4-input NAND gates!**", "- Total hardware: **One 3:8 Decoder + Two 4-input NAND gates!**\n" + decoder_fa_mermaid)

# 5. Decoder Expansion Mermaid
decoder_exp_mermaid = """
```mermaid
graph TD
    A["MSB Input A"] --> Inverter["NOT Gate"]
    Inverter -->|"A' (Active when A=0)"| E1["Enable E of Decoder 1"]
    A -->|"A (Active when A=1)"| E2["Enable E of Decoder 2"]
    BCD["Inputs B, C, D"] --> D1["3:8 Decoder 1"]
    BCD --> D2["3:8 Decoder 2"]
    D1 --> Out0_7["Outputs Y0 - Y7 (Minterms 0 to 7)"]
    D2 --> Out8_15["Outputs Y8 - Y15 (Minterms 8 to 15)"]
```
"""
content = content.replace("#### 2. Construct 5:32 Decoder using four 3:8 Decoders", decoder_exp_mermaid + "\n\n#### 2. Construct 5:32 Decoder using four 3:8 Decoders")

# 6. MUX Implementation Mermaid
mux_mermaid = """
```mermaid
graph LR
    subgraph Select_Lines
        S2["S2 = Input A"]
        S1["S1 = Input B"]
        S0["S0 = Input C"]
    end
    subgraph Data_Inputs
        I0["I0 = D"]
        I1["I1 = D"]
        I2["I2 = D'"]
        I3["I3 = 0 (GND)"]
        I4["I4 = 0 (GND)"]
        I5["I5 = D"]
        I6["I6 = 1 (VCC)"]
        I7["I7 = 1 (VCC)"]
    end
    MUX["8:1 Multiplexer (Data Selector)"]
    S2 --> MUX
    S1 --> MUX
    S0 --> MUX
    I0 --> MUX
    I1 --> MUX
    I2 --> MUX
    I3 --> MUX
    I4 --> MUX
    I5 --> MUX
    I6 --> MUX
    I7 --> MUX
    MUX --> Y["Output F(A,B,C,D)"]
```
"""
content = content.replace("3. **Pin Connections**:", mux_mermaid + "\n\n3. **Pin Connections**:")

# 7. JK Flip-Flop State Diagram Mermaid
jk_state_mermaid = """
```mermaid
stateDiagram-v2
    state "Q = 0" as Q0
    state "Q = 1" as Q1
    Q0 --> Q0: J=0, K=0 (Hold) / J=0, K=1 (Reset)
    Q0 --> Q1: J=1, K=0 (Set) / J=1, K=1 (Toggle)
    Q1 --> Q1: J=0, K=0 (Hold) / J=1, K=0 (Set)
    Q1 --> Q0: J=0, K=1 (Reset) / J=1, K=1 (Toggle)
```
"""
content = content.replace("### Q3.1: Master Flip-Flop Suite (SR, JK, D, T)", "### Q3.1: Master Flip-Flop Suite (SR, JK, D, T)\n\n#### Flip-Flop State Transition Diagram (JK Flip-Flop Model):\n" + jk_state_mermaid)

# 8. Master-Slave JK Mermaid
ms_jk_mermaid = """
```mermaid
graph LR
    J["Input J"] --> Master["Master JK Flip-Flop<br>(Active on CLK = 1)"]
    K["Input K"] --> Master
    CLK["Clock Pulse CLK"] --> Master
    CLK --> INV["Inverter (NOT)"] --> Slave["Slave SR Flip-Flop<br>(Active on CLK = 0)"]
    Master -->|"Y (Internal State)"| Slave
    Master -->|"Y' (Complement)"| Slave
    Slave --> Q["Output Q"]
    Slave --> Qbar["Output Q'"]
    Q -.->|"Feedback to Input K"| Master
    Qbar -.->|"Feedback to Input J"| Master
```
"""
content = content.replace("#### 2. The Master-Slave JK Solution:", "#### 2. The Master-Slave JK Solution:\n" + ms_jk_mermaid)

# 9. Synchronous Decade Counter State Transition Mermaid
decade_state_mermaid = """
```mermaid
stateDiagram-v2
    0000 --> 0001: Clock 1
    0001 --> 0010: Clock 2
    0010 --> 0011: Clock 3
    0011 --> 0100: Clock 4
    0100 --> 0101: Clock 5
    0101 --> 0110: Clock 6
    0110 --> 0111: Clock 7
    0111 --> 1000: Clock 8
    1000 --> 1001: Clock 9
    1001 --> 0000: Clock 10 (Rollover)
    state "Unused States (10 to 15)" as Unused
    Unused --> 0000: Self-Starting Recovery
```
"""
content = content.replace("#### Step 1: State Sequence & Number of Flip-Flops", "#### Step 1: State Sequence & State Diagram\n" + decade_state_mermaid)

# 10. Synchronous Decade Counter Hardware Topology Mermaid
decade_hw_mermaid = """
```mermaid
graph LR
    CLK["Synchronized Clock CLK"] --> FFA["JK FF A (LSB)"]
    CLK --> FFB["JK FF B"]
    CLK --> FFC["JK FF C"]
    CLK --> FFD["JK FF D (MSB)"]
    VCC["Logic 1 (+Vcc)"] --> JA["JA = 1, KA = 1"] --> FFA
    FFA -->|"QA"| AND_B["AND Gate: QA · QD'"] --> JB["JB = QA · QD'"] --> FFB
    FFA -->|"QA"| KB["KB = QA"] --> FFB
    FFA -->|"QA"| AND_C["AND Gate: QA · QB"]
    FFB -->|"QB"| AND_C --> JC["JC = KC = QA · QB"] --> FFC
    AND_C -->|"QA · QB"| AND_D["3-Input AND Gate"]
    FFC -->|"QC"| AND_D --> JD["JD = QA · QB · QC"] --> FFD
    FFA -->|"QA"| KD["KD = QA"] --> FFD
    FFD -->|"QD'"| AND_B
```
"""
content = content.replace("#### Step 4: Logic Circuit Schematic", "#### Step 4: Logic Circuit Schematic\n" + decade_hw_mermaid)

# 11. Arbitrary Sequence Counter State Diagram Mermaid
arbitrary_state_mermaid = """
```mermaid
stateDiagram-v2
    000 --> 100: 0 to 4
    100 --> 110: 4 to 6
    110 --> 001: 6 to 1
    001 --> 011: 1 to 3
    011 --> 111: 3 to 7
    111 --> 010: 7 to 2
    010 --> 101: 2 to 5
    101 --> 000: 5 to 0
```
"""
content = content.replace("$$0 \\to 4 \\to 6 \\to 1 \\to 3 \\to 7 \\to 2 \\to 5 \\to 0$$", "$$0 \\to 4 \\to 6 \\to 1 \\to 3 \\to 7 \\to 2 \\to 5 \\to 0$$\n" + arbitrary_state_mermaid)

# 12. Prime Sequence Counter State Diagram Mermaid
prime_state_mermaid = """
```mermaid
stateDiagram-v2
    010 --> 011: Prime 2 to 3
    011 --> 101: Prime 3 to 5
    101 --> 111: Prime 5 to 7
    111 --> 010: Prime 7 to 2
    state "Unused (0, 1, 4, 6)" as Unused
    Unused --> 010: Recovers to Prime 2
```
"""
content = content.replace("$$2 (0010) \\to 3 (0011) \\to 5 (0101) \\to 7 (0111) \\to 2 (0010).$$", "$$2 (0010) \\to 3 (0011) \\to 5 (0101) \\to 7 (0111) \\to 2 (0010).$$\n" + prime_state_mermaid)

# 13. Asynchronous Decade Counter Reset Mermaid
async_dec_mermaid = """
```mermaid
graph LR
    CLK["Input Clock Pulse"] --> FF0["Toggle FF0"]
    FF0 -->|"Q0"| FF1["Toggle FF1"]
    FF1 -->|"Q1"| FF2["Toggle FF2"]
    FF2 -->|"Q2"| FF3["Toggle FF3"]
    FF1 -->|"Q1 (Bit 1)"| NAND["2-Input NAND Gate"]
    FF3 -->|"Q3 (Bit 3)"| NAND
    NAND -->|"Active-Low Clear Pulse"| CLR0["CLR FF0"]
    NAND --> CLR1["CLR FF1"]
    NAND --> CLR2["CLR FF2"]
    NAND --> CLR3["CLR FF3"]
```
"""
content = content.replace("* **Asynchronous Reset**:", "* **Asynchronous Reset**:\n" + async_dec_mermaid)

# 14. Mealy Sequence Detector Mermaid
mealy_mermaid = """
```mermaid
stateDiagram-v2
    [*] --> S0: Reset
    S0 --> S1: 1 / 0
    S0 --> S0: 0 / 0
    S1 --> S1: 1 / 0
    S1 --> S2: 0 / 0
    S2 --> S3: 1 / 0
    S2 --> S0: 0 / 0
    S3 --> S1: 1 / 0
    S3 --> S2: 0 / 1 (Pattern 1010 Detected!)
```
"""
content = content.replace("#### 1. Mealy State Diagram (Overlapping '1010'):", "#### 1. Mealy State Diagram (Overlapping '1010'):\n" + mealy_mermaid)

# 15. Moore Sequence Detector Mermaid
moore_mermaid = """
```mermaid
stateDiagram-v2
    state "S0 [Out = 0]" as S0
    state "S1 [Out = 0]" as S1
    state "S2 [Out = 0]" as S2
    state "S3 [Out = 0]" as S3
    state "S4 [Out = 1]" as S4
    [*] --> S0: Reset
    S0 --> S0: Input 0
    S0 --> S1: Input 1
    S1 --> S1: Input 1
    S1 --> S2: Input 0
    S2 --> S0: Input 0
    S2 --> S3: Input 1
    S3 --> S1: Input 1
    S3 --> S4: Input 0 (Detected!)
    S4 --> S1: Input 1
    S4 --> S0: Input 0
```
"""
content = content.replace("#### 2. Moore State Diagram (Requires 5 States):", "#### 2. Moore State Diagram (Requires 5 States):\n" + moore_mermaid)

# 16. Images for Q5.9 and Q5.10
img_q59 = """
![Group Activity Circuit 1 (NAND-XOR-NOT Network)](../../resources/circuit_activity_a.png)
*Figure 5.1: Group Activity Circuit 1 Schematic Diagram.*
"""
content = content.replace("### Q5.9: Gate-Level Verilog for Circuit 1 (`circuit_activity_a.png`)\n", "### Q5.9: Gate-Level Verilog for Circuit 1 (`circuit_activity_a.png`)\n\n" + img_q59 + "\n")

img_q510 = """
![Group Activity Circuit 2 (XOR-AND-OR Network)](../../resources/circuit_activity_b.png)
*Figure 5.2: Group Activity Circuit 2 Schematic Diagram.*
"""
content = content.replace("### Q5.10: Gate-Level Verilog for Circuit 2 (`circuit_activity_b.png`)\n", "### Q5.10: Gate-Level Verilog for Circuit 2 (`circuit_activity_b.png`)\n\n" + img_q510 + "\n")

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Updated successfully! Written {len(content)} characters to {target_file}")
