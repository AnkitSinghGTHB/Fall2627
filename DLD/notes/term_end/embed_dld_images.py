"""
embed_dld_images.py
Injects high-yield visual SVG/PNG circuit diagrams into 08-dld-faculty-imp-curated-master-solutions.md
"""

import os
import shutil

MD_PATH = r"c:\Users\ankit\Fall2627\DLD\notes\term_end\08-dld-faculty-imp-curated-master-solutions.md"
BACKUP_PATH = r"c:\Users\ankit\Fall2627\DLD\notes\term_end\08-dld-faculty-imp-curated-master-solutions.backup.md"

shutil.copy2(MD_PATH, BACKUP_PATH)

with open(MD_PATH, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    # 1. RTL NOR Gate (Module 1)
    (
        "#### 1. Circuit Schematic:\n\n```mermaid\ngraph TD",
        """#### 1. Circuit Schematic:

![2-Input RTL NOR Gate Circuit Diagram](images/rtl_nor_gate.svg)
*Figure 1.1: Complete Schematic of 2-Input RTL NOR Gate showing Transistors Q1, Q2, Base Resistors RB, Collector Resistor RC, and Output Node Y.*

```mermaid
graph TD"""
    ),

    # 2. Universal Gate Realizations (Module 1)
    (
        "| **XNOR ($A \\odot B$)** | $\\overline{(A \\oplus B) \\cdot (A \\oplus B)}$ (5 gates) | $\\overline{\\overline{A+B} + \\overline{A'+B'}}$ (4 gates) |\n\n---",
        """| **XNOR ($A \\odot B$)** | $\\overline{(A \\oplus B) \\cdot (A \\oplus B)}$ (5 gates) | $\\overline{\\overline{A+B} + \\overline{A'+B'}}$ (4 gates) |

![Universal Logic Realization using NAND and NOR](images/universal_gates_realization.svg)
*Figure 1.2: Complete Visual Blueprint for realizing NOT, AND, OR, XOR using NAND-Only and NOR-Only configurations.*

---"""
    ),

    # 3. BCD to Excess-3 Circuit (Module 2)
    (
        "#### Step 4: Logic Circuit Schematic\n\n```mermaid\ngraph LR",
        """#### Step 4: Logic Circuit Schematic

![BCD to Excess-3 Logic Circuit Diagram](images/bcd_to_excess3_circuit.svg)
*Figure 2.1: Minimized 4-Bit Gate-Level Schematic of BCD to Excess-3 Code Converter (Outputs W, X, Y, Z).*

```mermaid
graph LR"""
    ),

    # 4. Binary to Gray & Gray to Binary (Module 2)
    (
        "#### 2. Gray to Binary Code:\n* **Inverse Equations**:",
        """#### 2. Gray to Binary Code:

![4-Bit Binary to Gray & Gray to Binary Circuits](images/binary_to_gray_circuit.svg)
*Figure 2.2: Side-by-Side Gate Schematics for 4-Bit Binary-to-Gray and Gray-to-Binary Converters with XOR Cascade.*

* **Inverse Equations**:"""
    ),

    # 5. Full Adder with 3:8 Decoder (Module 2)
    (
        "#### 2. Implementation with Active-Low Decoder (74LS138 style):\n- An active-low decoder produces",
        """#### 2. Implementation with Active-Low Decoder (74LS138 style):

![Full Adder Implementation using 3:8 Decoder with Active Low NAND](images/full_adder_decoder.svg)
*Figure 2.3: Hardware Implementation of Full Adder (S, Cout) using a 3:8 Active-Low Decoder and two 4-Input NAND Gates.*

- An active-low decoder produces"""
    ),

    # 6. 4:1 Multiplexer (Module 2)
    (
        "3. **Pin Connections**:\n   $$I_0 = D, \\quad I_1 = D, \\quad I_2 = D', \\quad I_3 = 0, \\quad I_4 = 0, \\quad I_5 = D, \\quad I_6 = 1, \\quad I_7 = 1$$\n\n---",
        """3. **Pin Connections**:
   $$I_0 = D, \\quad I_1 = D, \\quad I_2 = D', \\quad I_3 = 0, \\quad I_4 = 0, \\quad I_5 = D, \\quad I_6 = 1, \\quad I_7 = 1$$

![4:1 Multiplexer Architecture & Implementation](images/mux_4to1_circuit.svg)
*Figure 2.4: 4:1 Multiplexer Internal Gate-Level Architecture and Boolean Function Realization Block Diagram.*

---"""
    ),

    # 7. SR Latches (Module 3)
    (
        "### Q3.1: Master Flip-Flop Suite (SR, JK, D, T)\n\n#### Flip-Flop State Transition Diagram",
        """### Q3.1: Master Flip-Flop Suite (SR, JK, D, T)

![SR Latches using NOR and NAND Cross-Coupled Gates](images/sr_latches.svg)
*Figure 3.1: Circuit Topologies and Truth Tables for NOR Latch (Active-High) and NAND Latch (Active-Low).*

#### Flip-Flop State Transition Diagram"""
    ),

    # 8. Master-Slave JK FF (Module 3)
    (
        "#### 2. The Master-Slave JK Solution:\n\n```mermaid\ngraph LR",
        """#### 2. The Master-Slave JK Solution:

![Master-Slave JK Flip-Flop Schematic](images/master_slave_jk_ff.svg)
*Figure 3.2: Complete Gate-Level Schematic of Master-Slave JK Flip-Flop showing Clock Inverter and Anti-Race Feedback Paths.*

```mermaid
graph LR"""
    ),

    # 9. Assignment 4 Sequential Circuit in Q3.4 (Module 3)
    (
        "### Q3.4: Analysis of Clocked Sequential Circuits\n\n**Methodology**:",
        """### Q3.4: Analysis of Clocked Sequential Circuits

![Sequential Circuit from Assignment 4](images/assignment4_img_1.png)
*Figure 3.3: Clocked Sequential Circuit from Assignment 4 (Flip-Flops with Combinational Logic).*

**Methodology**:"""
    ),

    # 10. Synchronous Decade Counter (Module 4)
    (
        "#### Step 4: Logic Circuit Schematic\n\n```mermaid\ngraph LR\n    CLK[\"Synchronized Clock CLK\"]",
        """#### Step 4: Logic Circuit Schematic

![Synchronous Decade Counter Circuit Diagram](images/sync_decade_counter_circuit.svg)
*Figure 4.1: Complete Synchronous Mod-10 Decade Counter Logic Schematic with 4 JK Flip-Flops and Synchronized Clocking.*

```mermaid
graph LR
    CLK[\"Synchronized Clock CLK\"]"""
    ),

    # 11. Asynchronous Ripple Decade Counter (Module 4)
    (
        "### Q4.4: Asynchronous (Ripple) Decade Counter with NAND Reset\n\n* **Structure**:",
        """### Q4.4: Asynchronous (Ripple) Decade Counter with NAND Reset

![Asynchronous Ripple Decade Counter with NAND Reset](images/async_decade_counter_circuit.svg)
*Figure 4.2: Asynchronous Ripple Decade Counter (0000 to 1001) with 2-Input NAND Gate Clear at State 1010.*

* **Structure**:"""
    ),

    # 12. Ring vs Johnson Counter (Module 4)
    (
        "### Q4.5: Ring Counter vs Johnson Counter\n\n| Parameter | 4-Bit Ring Counter |",
        """### Q4.5: Ring Counter vs Johnson Counter

![Ring Counter vs Johnson Counter Schematics](images/ring_and_johnson_counters.svg)
*Figure 4.3: Comparison of 4-Bit Ring Counter (Straight Feedback) and 4-Bit Johnson Counter (Twisted-Ring Inverted Feedback).*

| Parameter | 4-Bit Ring Counter |"""
    ),

    # 13. Sequence Detector Hardware (Module 4 & Hacks)
    (
        "#### Worked Example: Overlapping '1010' Sequence Detector using D Flip-Flops",
        """![Sequence Detector Hardware Implementation with D Flip-Flops](images/sequence_detector_circuit.svg)
*Figure 4.4: Complete Hardware Implementation of 1011 Overlapping Sequence Detector using 2 D Flip-Flops and Combinational Gates.*

#### Worked Example: Overlapping '1010' Sequence Detector using D Flip-Flops"""
    ),

    # 14. All 4 Shift Registers (Hacks)
    (
        "### ⚡ HACK 1: The Register Clock Pulse Rule (Exam Numerical Guaranteed!)\n**Question**:",
        """### ⚡ HACK 1: The Register Clock Pulse Rule (Exam Numerical Guaranteed!)

![All 4 Shift Registers (SISO, SIPO, PISO, PIPO)](images/shift_registers_all4.svg)
*Figure 4.5: Master Architectural Comparison of All 4 Shift Registers (SISO, SIPO, PISO, PIPO) with Clock Pulse Formulations.*

**Question**:"""
    ),

    # 15. Circuit Activity A & B Paths update in Q5.9 & Q5.10
    (
        "![Group Activity Circuit 2 (XOR-AND-OR Network)](../../resources/circuit_activity_b.png)",
        "![Group Activity Circuit 2 (XOR-AND-OR Network)](images/circuit_activity_b.png)"
    ),
    (
        "### Q5.9: Gate-Level Verilog for Circuit 1 (`circuit_activity_a.png`)\n\n```verilog",
        """### Q5.9: Gate-Level Verilog for Circuit 1 (`circuit_activity_a.png`)

![Group Activity Circuit 1 (NAND-XOR Network)](images/circuit_activity_a.png)
*Figure 5.1: Group Activity Circuit 1 Schematic Diagram.*

```verilog"""
    )
]

modified = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new, 1)
        modified += 1
    else:
        print("MISSING PATTERN:", repr(old[:40]))

with open(MD_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully applied {modified}/{len(replacements)} image embeds!")
