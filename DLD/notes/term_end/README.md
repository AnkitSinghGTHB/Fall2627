# 🎯 ECE2002: Digital Logic Design — Term End (TEE / FAT) Master Guide

> **Course Code**: ECE2002 | **Slot**: A14+D11+D12 | **Faculty**: Dr. Kanimozhi M  
> **Exam Date**: Friday, October 16, 2026 (01:15 PM – 04:15 PM)  
> **Pre-TEE Recorded Standing**: 49.4 / 65.0 (Estimated 70-scale: ~53.5 / 70)  
> **TEE Target for A Grade**: **70–74 / 100** (Weighted: 21.0–22.2 / 30)

---

## 📋 TEE Exam Paper Architecture (Official Format)
* **Duration**: 3 Hours (Closed Book) | **Total Marks**: 100 Marks (Scaled to 30% Weightage)
* **Section A (60 Marks)**: 5 Questions × 12 Marks (1 from each Unit; internal choice `OR` format, either 12M or 6+6M)
* **Section B (40 Marks)**: 5 Questions × 8 Marks (1 from each Unit; direct numerical/design question without subparts)
* **Weight Distribution**: Every Unit carries **exactly 20 Marks** (12M in Sec A + 8M in Sec B).

| Unit | Title | Core Focus | Weight in TEE |
|:---:|:---|:---|:---:|
| **Unit 1** | **Number Systems & Boolean Algebra** | Base Conversions, Signed 2's Complement Arithmetic, Boolean Theorems, Standard Canonical Forms, Logic Families (TTL, ECL, CMOS) | **20 Marks** |
| **Unit 2** | **Combinational Logic Circuits** | 4-Variable & 5-Variable K-Maps, Don't Cares, Quine-McCluskey, Adders/Subtractors, BCD Adder, MUX/DEMUX, Priority Encoders | **20 Marks** |
| **Unit 3** | **Sequential Logic Circuits** | SR, JK, D, T Flip-Flops, Race-Around Condition & Master-Slave JK, Universal FF Conversion Recipe, Implication Table State Reduction | **20 Marks** |
| **Unit 4** | **Registers, Counters & FSMs** | Synchronous MOD Counter Design Recipe (D & T FFs), Ripple Mod-N Clear, Shift Registers (SISO/SIPO/PIPO/PISO), Mealy/Moore Sequence Detectors | **20 Marks** |
| **Unit 5** | **Verilog HDL Modeling** | Gate-Level, Dataflow (`assign`), Behavioral (`always`, blocking `=` vs non-blocking `<=`), Testbench Construction, Verilog Full Adder & D-FF | **20 Marks** |

---

## 🏆 Dr. Kanimozhi's Scoring Rubric (How to Guarantee 16+/20 per Question)
Digital design evaluators grade circuits on strict structural completeness. Every design question must follow this **5-Step Standardized Pipeline**:

```
[Design Prompt] ──▶ 1. State Table / Excitation Table (Clear Present State Qn, Next State Qn+1, Inputs)
                ──▶ 2. Truth Table / Transition Matrix
                ──▶ 3. Minimal K-Maps (Explicit Grouping & Essential Prime Implicants)
                ──▶ 4. Simplified Boolean Equations (Clearly labeled outputs)
                ──▶ 5. Clean Logic Circuit Diagram (Standard logic gate symbols, clock lines)
```

---

## 📂 Term End Study Suite Navigation

| File | Description |
|:---|:---|
| [00-dld-emergency-plan-and-blueprints.md](./00-dld-emergency-plan-and-blueprints.md) | Emergency execution plan, Pre-load checklist, and design templates |
| [01-module1-number-systems-boolean-logic-families.md](./01-module1-number-systems-boolean-logic-families.md) | Unit 1: Base arithmetic, 2's complement, Boolean theorems, Logic families |
| [02-module2-combinational-circuits-kmaps-arithmetic.md](./02-module2-combinational-circuits-kmaps-arithmetic.md) | Unit 2: K-maps, Adders, BCD Adder, MUX/DEMUX, Encoders/Decoders |
| [03-module3-sequential-logic-flipflops-state-reduction.md](./03-module3-sequential-logic-flipflops-state-reduction.md) | Unit 3: Latches, Flip-flops, Universal conversion, Implication state reduction |
| [04-module4-registers-counters-fsm-detectors.md](./04-module4-registers-counters-fsm-detectors.md) | Unit 4: Shift registers, Synchronous/Asynchronous counters, Mealy/Moore sequence detectors |
| [05-module5-verilog-hdl-modeling-testbenches.md](./05-module5-verilog-hdl-modeling-testbenches.md) | Unit 5: Verilog lexical rules, Gate/Dataflow/Behavioral modeling, Testbenches |
| [06-dld-master-formula-excitation-cheat-sheet.md](./06-dld-master-formula-excitation-cheat-sheet.md) | 1-Page Master Cheat Sheet: Excitation tables, characteristic equations, conversions |
| [07-dld-fat-high-frequency-exam-question-bank.md](./07-dld-fat-high-frequency-exam-question-bank.md) | 15 Fully Solved Past TEE Exam Questions with complete circuit diagrams |
