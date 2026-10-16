"""
apply_final_embeds.py
"""

MD_PATH = r"c:\Users\ankit\Fall2627\DLD\notes\term_end\08-dld-faculty-imp-curated-master-solutions.md"

with open(MD_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Universal gates
old1 = "4 NOR gates |"
insert1 = """4 NOR gates |

![Universal Logic Realization using NAND and NOR](images/universal_gates_realization.svg)
*Figure 1.2: Complete Visual Blueprint for realizing NOT, AND, OR, XOR using NAND-Only and NOR-Only configurations.*"""

if old1 in text and "universal_gates_realization.svg" not in text:
    text = text.replace(old1, insert1, 1)
    print("Embedded universal_gates_realization.svg")

# 2. BCD to Excess-3
old2 = "#### Step 4: Logic Schematic"
insert2 = """#### Step 4: Logic Schematic

![BCD to Excess-3 Logic Circuit Diagram](images/bcd_to_excess3_circuit.svg)
*Figure 2.1: Minimized 4-Bit Gate-Level Schematic of BCD to Excess-3 Code Converter (Outputs W, X, Y, Z).*"""

if old2 in text and "bcd_to_excess3_circuit.svg" not in text:
    text = text.replace(old2, insert2, 1)
    print("Embedded bcd_to_excess3_circuit.svg")

# 3. Circuit Activity A
old3 = "### Q5.9: Gate-Level Verilog for Group Activity Circuit 1 (circuit_activity_a.png)"
insert3 = """### Q5.9: Gate-Level Verilog for Group Activity Circuit 1 (circuit_activity_a.png)

![Group Activity Circuit 1 (NAND-XOR Network)](images/circuit_activity_a.png)
*Figure 5.1: Group Activity Circuit 1 Schematic Diagram.*"""

if old3 in text and "circuit_activity_a.png" not in text:
    text = text.replace(old3, insert3, 1)
    print("Embedded circuit_activity_a.png")

with open(MD_PATH, "w", encoding="utf-8") as f:
    f.write(text)

print("Done final embeds!")
