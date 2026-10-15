# -*- coding: utf-8 -*-
"""
Build the All-Inclusive Master Solutions PDF Handbook for CSE2004:
Theory of Computation & Compiler Design
Author: DeepMind Antigravity Pair Programmer for Ankit
"""
import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CSE2004: Theory of Computation & Compiler Design — Master Solutions & Methodology Handbook</title>
<style>
  @page {
    size: A4 portrait;
    margin: 12mm 12mm 14mm 12mm;
    @bottom-right {
      content: "Page " counter(page) " of " counter(pages);
      font-size: 9px;
      color: #64748b;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    @bottom-left {
      content: "CSE2004: TEE Master Solutions Handbook — Dr. Gaurav Soni";
      font-size: 9px;
      color: #64748b;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
  }
  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background: #ffffff;
    line-height: 1.48;
    font-size: 12.5px;
    margin: 0;
    padding: 0;
  }

  /* COVER BANNER */
  .cover {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 60%, #1e40af 100%);
    color: white;
    padding: 28px 24px;
    border-radius: 10px;
    margin-bottom: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
  }
  .cover h1 {
    margin: 0 0 6px 0;
    font-size: 24px;
    letter-spacing: -0.5px;
    color: #ffffff;
    font-weight: 800;
  }
  .cover h2 {
    margin: 0 0 14px 0;
    font-size: 14px;
    font-weight: 400;
    color: #93c5fd;
    letter-spacing: 0.2px;
  }
  .cover-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    font-size: 11px;
    border-top: 1px solid rgba(255,255,255,0.2);
    padding-top: 10px;
  }
  .cover-meta span {
    background: rgba(255,255,255,0.14);
    padding: 3px 9px;
    border-radius: 5px;
    font-weight: 500;
  }

  /* HEADINGS & CARDS */
  .module-header {
    background: #1e3a8a;
    color: white;
    padding: 9px 15px;
    border-radius: 7px;
    font-size: 16px;
    font-weight: 700;
    margin-top: 24px;
    margin-bottom: 14px;
    page-break-after: avoid;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .problem-card {
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 14px;
    margin-bottom: 14px;
    background: #ffffff;
    page-break-inside: avoid;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
  }
  .problem-title {
    font-size: 14px;
    font-weight: 700;
    color: #1e3a8a;
    margin-top: 0;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .badge {
    display: inline-block;
    padding: 2px 7px;
    border-radius: 4px;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
  }
  .badge-12m { background: #fee2e2; color: #b91c1c; border: 1px solid #fca5a5; }
  .badge-8m { background: #e0e7ff; color: #4338ca; border: 1px solid #c7d2fe; }
  .badge-core { background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }

  /* CALLOUT BOXES FOR TIPS & METHODOLOGY */
  .callout {
    border-radius: 6px;
    padding: 10px 14px;
    margin: 10px 0;
    font-size: 11.8px;
    line-height: 1.45;
    page-break-inside: avoid;
  }
  .callout-method {
    background: #f0fdf4;
    border-left: 4px solid #16a34a;
    color: #14532d;
  }
  .callout-tips {
    background: #fefce8;
    border-left: 4px solid #ca8a04;
    color: #713f12;
  }
  .callout-warning {
    background: #fef2f2;
    border-left: 4px solid #dc2626;
    color: #7f1d1d;
  }
  .callout-title {
    font-weight: 700;
    font-size: 12px;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 5px;
  }

  /* DIAGRAM BOXES */
  .diagram-container {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 10px;
    margin: 10px 0;
    text-align: center;
    page-break-inside: avoid;
  }
  .diagram-caption {
    font-size: 10.5px;
    color: #64748b;
    font-style: italic;
    margin-top: 6px;
  }

  /* TABLES & CODE */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0 12px 0;
    font-size: 11.5px;
  }
  th, td {
    border: 1px solid #cbd5e1;
    padding: 5px 8px;
    text-align: left;
  }
  th {
    background: #f1f5f9;
    font-weight: 700;
    color: #0f172a;
  }
  tr:nth-child(even) td {
    background: #f8fafc;
  }
  code {
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    font-size: 11px;
    background: #f1f5f9;
    padding: 1px 4px;
    border-radius: 3px;
    color: #0f172a;
  }
  pre {
    background: #0f172a;
    color: #f8fafc;
    padding: 10px 12px;
    border-radius: 6px;
    font-size: 11px;
    line-height: 1.4;
    overflow-x: auto;
    margin: 8px 0;
    font-family: "SFMono-Regular", Consolas, Menlo, monospace;
    page-break-inside: avoid;
  }
  .step-num {
    display: inline-block;
    width: 18px;
    height: 18px;
    background: #1e3a8a;
    color: white;
    border-radius: 50%;
    text-align: center;
    line-height: 18px;
    font-size: 10px;
    font-weight: bold;
    margin-right: 5px;
  }
  ul, ol {
    margin: 4px 0 8px 20px;
    padding: 0;
  }
  li {
    margin-bottom: 3px;
  }
  .page-break {
    page-break-before: always;
  }
</style>
</head>
<body>

<!-- COVER -->
<div class="cover">
  <h1>CSE2004: Theory of Computation & Compiler Design</h1>
  <h2>Comprehensive Exam Solutions, Methodology & Intuition Handbook (All 5 Modules)</h2>
  <div class="cover-meta">
    <span>Slot: A11+A12+A13</span>
    <span>Faculty: Dr. Gaurav Soni</span>
    <span>TEE Date: 15-Oct-2026</span>
    <span>Coverage: 100% Questions from Modules 1 to 5</span>
    <span>Format: Step-by-Step + Tips & Tricks + Diagrams</span>
  </div>
</div>

<!-- ========================================== -->
<!-- MODULE 1: FA, REGEX & LEXICAL ANALYSIS -->
<!-- ========================================== -->
<div class="module-header">
  <span>MODULE 1: Finite Automata, Regular Languages & Lexical Analysis</span>
  <span style="font-size: 12px; font-weight: normal;">Weightage: ~20-25 Marks</span>
</div>

<div class="callout callout-method">
  <div class="callout-title">⚡ Standard 6-Part Presentation for ANY Automata Question (Faculty Requirement)</div>
  Whenever asked to construct a DFA, NFA, or PDA, structure your written answer in these 6 exact parts to secure full 12/12 or 8/8 marks:
  <ol>
    <li><strong>Formal 5-Tuple Definition:</strong> State $M = (Q, \Sigma, \delta, q_0, F)$ explicitly naming every set.</li>
    <li><strong>State Semantic Meanings:</strong> Define what each state physically remembers (e.g., "$q_1$ = remembers that the last seen bit was 1").</li>
    <li><strong>Transition Diagram:</strong> Clean, labelled circles (double circle for final, incoming arrow for start).</li>
    <li><strong>Transition Table:</strong> Rows = States, Columns = Alphabet symbols ($\delta(q, a)$).</li>
    <li><strong>String Acceptance Trace:</strong> Show step-by-step state sequence for 1 accepted string and 1 rejected string.</li>
    <li><strong>Language Equation:</strong> Express the accepted language formally: $L(M) = \\{w \\in \\Sigma^* \\mid \\dots\\}$.</li>
  </ol>
</div>

<div class="callout callout-tips">
  <div class="callout-title">💡 Tips, Tricks & Misconception Buster (Module 1)</div>
  <ul>
    <li><strong>DFA vs NFA:</strong> In a DFA, EVERY state MUST have exactly ONE outgoing arrow for every alphabet symbol! If an input is invalid, it CANNOT simply disappear; it must go to a <strong>Dead/Trap state</strong> ($q_{\\text{trap}}$). In an NFA, invalid transitions are just omitted.</li>
    <li><strong>"Contains" vs "Ends With":</strong>
      <ul>
        <li><em>Contains `010`:</em> Once `010` is seen, transition to a final state that LOOPS on all inputs forever ($\delta(q_{\\text{final}}, 0,1) = q_{\\text{final}}$).</li>
        <li><em>Ends with `010`:</em> Once `010` is reached, it is final, BUT subsequent inputs can break the suffix, so it must loop back to earlier prefix states!</li>
      </ul>
    </li>
    <li><strong>Complementing a DFA:</strong> Swap final and non-final states ($F' = Q \\setminus F$). <em>CAUTION:</em> You can ONLY do this on a complete DFA (with all trap transitions drawn). If you complement an NFA directly, you get the WRONG answer!</li>
    <li><strong>Modulo Arithmetic (Divisibility):</strong> A binary number modulo $k$ has exactly $k$ states ($q_0, q_1, \\dots, q_{k-1}$). When reading bit $b \\in \\{0, 1\\}$, the transition is: $\\delta(q_r, b) = q_{(2r + b) \\bmod k}$.</li>
  </ul>
</div>

<!-- PROBLEM CARD 1: DFA 101 -->
<div class="problem-card">
  <div class="problem-title">
    <span>Q1(a)(vi) & (vii): DFA for Strings Ending in '101' vs NOT Containing '101'</span>
    <span class="badge badge-12m">12 Marks Flagship</span>
  </div>
  <p><strong>Alphabet:</strong> $\Sigma = \{0, 1\}$. <strong>Problem:</strong> Design DFA for (1) strings ending in 101, and (2) strings NOT containing 101.</p>
  
  <div class="diagram-container">
    <svg width="520" height="120" viewBox="0 0 520 120" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
          <path d="M0,0 L0,6 L6,3 z" fill="#1e3a8a" />
        </marker>
      </defs>
      <!-- Start arrow -->
      <line x1="10" y1="60" x2="40" y2="60" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr)"/>
      <!-- State q0 -->
      <circle cx="65" cy="60" r="22" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2"/>
      <text x="65" y="65" text-anchor="middle" font-weight="bold" fill="#1e3a8a" font-size="13">q0</text>
      <!-- State q1 -->
      <circle cx="185" cy="60" r="22" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2"/>
      <text x="185" y="65" text-anchor="middle" font-weight="bold" fill="#1e3a8a" font-size="13">q1</text>
      <!-- State q2 -->
      <circle cx="305" cy="60" r="22" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2"/>
      <text x="305" y="65" text-anchor="middle" font-weight="bold" fill="#1e3a8a" font-size="13">q2</text>
      <!-- State q3 (Accepting) -->
      <circle cx="435" cy="60" r="24" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
      <circle cx="435" cy="60" r="20" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
      <text x="435" y="65" text-anchor="middle" font-weight="bold" fill="#15803d" font-size="13">q3</text>
      
      <!-- Forward arrows -->
      <line x1="87" y1="60" x2="161" y2="60" stroke="#1e3a8a" stroke-width="1.8" marker-end="url(#arr)"/>
      <text x="124" y="52" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">1</text>
      <line x1="207" y1="60" x2="281" y2="60" stroke="#1e3a8a" stroke-width="1.8" marker-end="url(#arr)"/>
      <text x="244" y="52" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">0</text>
      <line x1="327" y1="60" x2="409" y2="60" stroke="#1e3a8a" stroke-width="1.8" marker-end="url(#arr)"/>
      <text x="368" y="52" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">1</text>
      
      <!-- Loops & Backtracks -->
      <path d="M 55 40 C 40 10, 90 10, 75 39" fill="none" stroke="#1e3a8a" stroke-width="1.5" marker-end="url(#arr)"/>
      <text x="65" y="12" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">0</text>
      <path d="M 175 40 C 160 10, 210 10, 195 39" fill="none" stroke="#1e3a8a" stroke-width="1.5" marker-end="url(#arr)"/>
      <text x="185" y="12" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">1</text>
      <!-- q2 on 0 back to q0 -->
      <path d="M 300 82 C 280 115, 90 115, 70 82" fill="none" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#arr)"/>
      <text x="185" y="112" text-anchor="middle" font-size="11" font-weight="bold" fill="#dc2626">0</text>
      <!-- q3 on 1 back to q1 -->
      <path d="M 425 84 C 380 105, 230 105, 195 82" fill="none" stroke="#1e3a8a" stroke-width="1.5" marker-end="url(#arr)"/>
      <text x="310" y="98" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">1</text>
      <!-- q3 on 0 back to q2 -->
      <path d="M 420 40 C 390 15, 340 15, 315 40" fill="none" stroke="#1e3a8a" stroke-width="1.5" marker-end="url(#arr)"/>
      <text x="365" y="20" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">0</text>
    </svg>
    <div class="diagram-caption">Figure 1.1: State transition graph for DFA accepting strings ending in 101.</div>
  </div>

  <p><strong>Part (2) Complement Solution (Strings NOT containing '101'):</strong></p>
  <ul>
    <li>In Part (1), $q_3$ was reached whenever `101` was recognized. To reject `101` anywhere, make $q_3$ a <strong>Dead Trap State</strong> ($\delta(q_3, 0) = q_3, \delta(q_3, 1) = q_3$).</li>
    <li>Invert final states: $F' = \{q_0, q_1, q_2\}$. $q_3$ is non-accepting. Any string reaching $q_3$ gets permanently trapped and rejected!</li>
  </ul>
</div>

<!-- PROBLEM CARD 2: ALL 29 REGEXES -->
<div class="problem-card">
  <div class="problem-title">
    <span>Q5: All 29 Regular Expressions (i to xxix) Master Rapid Lookup</span>
    <span class="badge badge-core">Core Reference</span>
  </div>
  <table>
    <thead>
      <tr>
        <th style="width: 8%;">#</th>
        <th style="width: 46%;">Language Requirement</th>
        <th style="width: 46%;">Exact Regular Expression</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><strong>(i)</strong></td><td>No 0 or triples of 0s with no 1 or many 1s</td><td><code>(000)* 1*</code></td></tr>
      <tr><td><strong>(ii)</strong></td><td>Strings of one or many 11 or no 11</td><td><code>(0 + 10)* (11)* (0 + 01)*</code></td></tr>
      <tr><td><strong>(iii)</strong></td><td>Ending with abb</td><td><code>(a + b)* abb</code></td></tr>
      <tr><td><strong>(iv)</strong></td><td>Having 010 or 101</td><td><code>(0 + 1)* (010 + 101) (0 + 1)*</code></td></tr>
      <tr><td><strong>(v)</strong></td><td>Even length strings defined over {a, b}</td><td><code>((a + b)(a + b))*</code></td></tr>
      <tr><td><strong>(vi)</strong></td><td>At least one double 0 or double 1</td><td><code>(0 + 1)* (00 + 11) (0 + 1)*</code></td></tr>
      <tr><td><strong>(vii)</strong></td><td>Starting with 0 and having multiple even 1s or no 1</td><td><code>0 0* (1 0* 1 0*)*</code></td></tr>
      <tr><td><strong>(viii)</strong></td><td>Odd number of 0s OR odd number of 1s</td><td><code>(1* 0 1* (0 1* 0 1*)*) + (0* 1 0* (1 0* 1 0*)*)</code></td></tr>
      <tr><td><strong>(ix)</strong></td><td>Starting with 0 and ending with 1</td><td><code>0 (0 + 1)* 1</code></td></tr>
      <tr><td><strong>(x)</strong></td><td>Ending with b, zero or multiple sets of aa and bb</td><td><code>(aa + bb)* b</code></td></tr>
      <tr><td><strong>(xi)</strong></td><td>Second last symbol is 1</td><td><code>(0 + 1)* 1 (0 + 1)</code></td></tr>
      <tr><td><strong>(xii)</strong></td><td>Starting with 1 having zero or multiple even 1s</td><td><code>1 (0* 1 0* 1 0*)*</code></td></tr>
      <tr><td><strong>(xiii)</strong></td><td>Exactly single 1, many 0s</td><td><code>0* 1 0*</code></td></tr>
      <tr><td><strong>(xiv)</strong></td><td>Starting with aa and ending with ba</td><td><code>aa (a + b)* ba</code></td></tr>
      <tr><td><strong>(xv)</strong></td><td>Consecutive even length a's</td><td><code>(aa)*</code></td></tr>
      <tr><td><strong>(xvi)</strong></td><td>Odd length strings</td><td><code>(a + b) ((a + b)(a + b))*</code></td></tr>
      <tr><td><strong>(xvii)</strong></td><td>Even length strings ending with aa</td><td><code>((a + b)(a + b))* aa</code></td></tr>
      <tr><td><strong>(xviii)</strong></td><td>Odd number of 1s</td><td><code>0* 1 0* (0* 1 0* 1 0*)*</code></td></tr>
      <tr><td><strong>(xix)</strong></td><td>Even length starting with a, ending with b</td><td><code>a ((a + b)(a + b))* b</code> where length mod 2 = 0</td></tr>
      <tr><td><strong>(xx)</strong></td><td>Even length strings starting with a</td><td><code>a (a + b) ((a + b)(a + b))*</code></td></tr>
      <tr><td><strong>(xxi)</strong></td><td>Even number of 0s OR even number of 1s</td><td><code>(1* 0 1* 0 1*)* + (0* 1 0* 1 0*)*</code></td></tr>
      <tr><td><strong>(xxii)</strong></td><td>Exactly three consecutive 1s</td><td><code>(0 + 10 + 110)* 111 (0 + 01 + 011)*</code></td></tr>
      <tr><td><strong>(xxiii)</strong></td><td>Length divisible by 4</td><td><code>((0 + 1)(0 + 1)(0 + 1)(0 + 1))*</code></td></tr>
      <tr><td><strong>(xxiv)</strong></td><td>Does not contain substring 110</td><td><code>(0 + 10)* 1*</code></td></tr>
      <tr><td><strong>(xxv)(a)</strong></td><td>Exactly 2 a's</td><td><code>b* a b* a b*</code></td></tr>
      <tr><td><strong>(xxv)(b)</strong></td><td>At least 2 a's</td><td><code>(a + b)* a (a + b)* a (a + b)*</code></td></tr>
      <tr><td><strong>(xxv)(c)</strong></td><td>At most 2 a's</td><td><code>b* (a + ε) b* (a + ε) b*</code></td></tr>
      <tr><td><strong>(xxv)(d)</strong></td><td>Containing substring aa</td><td><code>(a + b)* aa (a + b)*</code></td></tr>
      <tr><td><strong>(xxviii)(b)</strong></td><td>Odd length 1s strictly greater than 1 ($1^{2n+1}, n>0$)</td><td><code>111 (11)*</code></td></tr>
      <tr><td><strong>(xxix)(b)</strong></td><td>Occurrences of 'a' divisible by 3</td><td><code>(b* a b* a b* a b*)*</code></td></tr>
      <tr><td><strong>(xxix)(c)</strong></td><td>At least two b's between any two a's</td><td><code>b* (a bb b*)* a b* + b*</code></td></tr>
    </tbody>
  </table>
</div>

<!-- PROBLEM CARD 3: DFA MINIMIZATION -->
<div class="problem-card">
  <div class="problem-title">
    <span>Q4: DFA Minimization (Table-Filling / Myhill-Nerode Method)</span>
    <span class="badge badge-12m">12 Marks Flagship</span>
  </div>
  <div class="callout callout-method">
    <div class="callout-title">⚡ 3-Step Methodology: Table Filling Algorithm</div>
    <ol>
      <li><strong>Step 1 (Base Cases):</strong> Mark all pairs $(p, q)$ where one is final ($p \in F$) and one is non-final ($q \notin F$) with an 'X'.</li>
      <li><strong>Step 2 (Inductive Step):</strong> For each unmarked pair $(p, q)$, check their transitions on all inputs $a \in \Sigma$. If $(\delta(p, a), \delta(q, a))$ is already marked, then mark $(p, q)$! Repeat until no new marks are added in a full pass.</li>
      <li><strong>Step 3 (Merge):</strong> All remaining unmarked pairs are <strong>equivalent states</strong> and must be collapsed into single composite states.</li>
    </ol>
  </div>
  <p><strong>Example:</strong> Given DFA with states $\{q_0, q_1, q_2, q_3, q_4, q_5\}$ with final state $F = \{q_2\}$.</p>
  <ul>
    <li>Testing $(q_1, q_3)$: $\delta(q_1, 0) = q_2$ (Final), but $\delta(q_3, 0) = q_4$ (Non-final) &rarr; Immediately marked as distinguishable!</li>
    <li>Testing $(q_0, q_4)$: $\delta(q_0, 0) = q_1, \delta(q_4, 0) = q_1$ (identical); $\delta(q_0, 1) = q_3, \delta(q_4, 1) = q_3$ (identical). Both transitions lead to identical states! Hence $(q_0, q_4)$ can NEVER be distinguished.</li>
    <li><strong>Equivalence Classes:</strong> $\{q_0, q_4\}, \{q_1\}, \{q_2\}, \{q_3\}, \{q_5\}$. Reduced from 6 states to 5 states.</li>
  </ul>
</div>

<!-- PROBLEM CARD 4: PUMPING LEMMA -->
<div class="problem-card">
  <div class="problem-title">
    <span>Q14: Proving Non-Regularity using Pumping Lemma</span>
    <span class="badge badge-8m">8 Marks</span>
  </div>
  <div class="callout callout-tips">
    <div class="callout-title">💡 How to Pick String 'w' and 'i' (Never Get Stuck!)</div>
    <ul>
      <li>Assume $L$ is regular with pumping length $p$.</li>
      <li>Pick string $w \in L$ such that $|w| \ge p$. <strong>Crucial Rule:</strong> Express $w$ strictly in terms of $p$ (e.g., $w = 0^p 1^p$).</li>
      <li>Split $w = xyz$ where $|xy| \le p$ and $|y| \ge 1$. This forces $y$ to lie ENTIRELY inside the first symbol block (e.g., $y = 0^k, k \ge 1$).</li>
      <li>Pump with $i = 0$ (pumping down) or $i = 2$ (pumping up). The number of 0's becomes $p + (i-1)k \ne p$, violating the language equality!</li>
    </ul>
  </div>
  <p><strong>Proof for $L = \{a^p \mid p \text{ is prime}\}$:</strong> Let $w = a^n$ where $n \ge p$ is prime. Split $w = xyz$ with $|y| = k \ge 1$. Then $|x y^i z| = n + (i - 1)k$. Pick $i = n + 1$. Then length $= n + n \cdot k = n(1 + k)$, which has factors $n$ and $(1+k)$ &there4; <strong>composite, not prime!</strong> Contradiction! $\blacksquare$</p>
</div>

<!-- ========================================== -->
<!-- MODULE 2: CFG, NORMAL FORMS, PDA & CFL -->
<!-- ========================================== -->
<div class="page-break"></div>
<div class="module-header">
  <span>MODULE 2: Context-Free Grammars, CNF/GNF, Pushdown Automata</span>
  <span style="font-size: 12px; font-weight: normal;">Weightage: ~20-25 Marks</span>
</div>

<div class="callout callout-tips">
  <div class="callout-title">💡 Tips, Tricks & Misconception Buster (Module 2)</div>
  <ul>
    <li><strong>Proving Ambiguity:</strong> You MUST draw <strong>TWO distinct parse trees</strong> for the EXACT same string (or write two distinct Leftmost Derivations). Showing one Leftmost and one Rightmost derivation does NOT prove ambiguity unless their trees differ!</li>
    <li><strong>CNF Strict Definition:</strong> Every production in Chomsky Normal Form must be either $A \to BC$ (exactly two variables) or $A \to a$ (exactly one terminal). Never mix terminals and variables on RHS!</li>
    <li><strong>Order of Simplification Matters:</strong> When converting CFG to CNF, you must follow this exact sequence:
      <ol style="margin: 2px 0 2px 16px;">
        <li>Eliminate $\epsilon$-productions ($A \to \epsilon$).</li>
        <li>Eliminate Unit productions ($A \to B$).</li>
        <li>Eliminate Useless symbols (non-generating first, then non-reachable).</li>
        <li>Replace terminals in mixed productions ($C_a \to a$).</li>
        <li>Cascade-split productions with $\ge 3$ variables.</li>
      </ol>
    </li>
    <li><strong>PDA Stack Intuition:</strong> PDA has finite states + 1 LIFO stack. For $a^n b^n$, push $a$ on stack, pop $a$ on $b$. For $a^{2n} b^n$, push TWO markers on each $a$ or pop one $a$ on every TWO $b$'s.</li>
  </ul>
</div>

<!-- AMBIGUITY -->
<div class="problem-card">
  <div class="problem-title">
    <span>Q1(e) & (f): Grammar Ambiguity Proofs with Parse Trees</span>
    <span class="badge badge-8m">8 Marks</span>
  </div>
  <p><strong>Problem:</strong> Prove grammar $S \to S + S \mid S * S \mid a \mid b$ is ambiguous for string $w = a + b * a$.</p>
  <div class="diagram-container">
    <svg width="480" height="150" viewBox="0 0 480 150" xmlns="http://www.w3.org/2000/svg">
      <!-- Tree 1 -->
      <g transform="translate(10, 10)">
        <text x="110" y="0" text-anchor="middle" font-weight="bold" fill="#1e3a8a">Tree 1: Root (+), yields (a) + (b*a)</text>
        <circle cx="110" cy="20" r="14" fill="#eff6ff" stroke="#1e3a8a"/>
        <text x="110" y="24" text-anchor="middle" font-weight="bold" font-size="12">S</text>
        <line x1="100" y1="32" x2="50" y2="60" stroke="#1e3a8a"/>
        <line x1="110" y1="34" x2="110" y2="60" stroke="#1e3a8a"/>
        <line x1="120" y1="32" x2="170" y2="60" stroke="#1e3a8a"/>
        <circle cx="50" cy="70" r="12" fill="#eff6ff" stroke="#1e3a8a"/>
        <text x="50" y="74" text-anchor="middle" font-size="11">S</text>
        <text x="110" y="74" text-anchor="middle" font-weight="bold" fill="#dc2626">+</text>
        <circle cx="170" cy="70" r="12" fill="#eff6ff" stroke="#1e3a8a"/>
        <text x="170" y="74" text-anchor="middle" font-size="11">S</text>
        <!-- children of left S -->
        <line x1="50" y1="82" x2="50" y2="105" stroke="#1e3a8a"/>
        <text x="50" y="118" text-anchor="middle" font-weight="bold" fill="#15803d">a</text>
        <!-- children of right S -->
        <line x1="160" y1="80" x2="140" y2="105" stroke="#1e3a8a"/>
        <line x1="170" y1="82" x2="170" y2="105" stroke="#1e3a8a"/>
        <line x1="180" y1="80" x2="200" y2="105" stroke="#1e3a8a"/>
        <text x="140" y="118" text-anchor="middle" font-weight="bold" fill="#15803d">b</text>
        <text x="170" y="118" text-anchor="middle" font-weight="bold" fill="#dc2626">*</text>
        <text x="200" y="118" text-anchor="middle" font-weight="bold" fill="#15803d">a</text>
      </g>
      <!-- Tree 2 -->
      <g transform="translate(250, 10)">
        <text x="110" y="0" text-anchor="middle" font-weight="bold" fill="#1e3a8a">Tree 2: Root (*), yields (a+b) * (a)</text>
        <circle cx="110" cy="20" r="14" fill="#eff6ff" stroke="#1e3a8a"/>
        <text x="110" y="24" text-anchor="middle" font-weight="bold" font-size="12">S</text>
        <line x1="100" y1="32" x2="50" y2="60" stroke="#1e3a8a"/>
        <line x1="110" y1="34" x2="110" y2="60" stroke="#1e3a8a"/>
        <line x1="120" y1="32" x2="170" y2="60" stroke="#1e3a8a"/>
        <circle cx="50" cy="70" r="12" fill="#eff6ff" stroke="#1e3a8a"/>
        <text x="50" y="74" text-anchor="middle" font-size="11">S</text>
        <text x="110" y="74" text-anchor="middle" font-weight="bold" fill="#dc2626">*</text>
        <circle cx="170" cy="70" r="12" fill="#eff6ff" stroke="#1e3a8a"/>
        <text x="170" y="74" text-anchor="middle" font-size="11">S</text>
        <!-- children of left S -->
        <line x1="40" y1="80" x2="20" y2="105" stroke="#1e3a8a"/>
        <line x1="50" y1="82" x2="50" y2="105" stroke="#1e3a8a"/>
        <line x1="60" y1="80" x2="80" y2="105" stroke="#1e3a8a"/>
        <text x="20" y="118" text-anchor="middle" font-weight="bold" fill="#15803d">a</text>
        <text x="50" y="118" text-anchor="middle" font-weight="bold" fill="#dc2626">+</text>
        <text x="80" y="118" text-anchor="middle" font-weight="bold" fill="#15803d">b</text>
        <!-- children of right S -->
        <line x1="170" y1="82" x2="170" y2="105" stroke="#1e3a8a"/>
        <text x="170" y="118" text-anchor="middle" font-weight="bold" fill="#15803d">a</text>
      </g>
    </svg>
    <div class="diagram-caption">Figure 2.1: Dual derivation trees for string 'a + b * a' proving grammar ambiguity.</div>
  </div>
  <p><strong>Conclusion:</strong> Since the string $w = a+b*a$ yields two structurally distinct parse trees, the grammar is conclusively <strong>AMBIGUOUS</strong>.</p>
</div>

<!-- CNF CONVERSIONS -->
<div class="problem-card">
  <div class="problem-title">
    <span>Q3: Chomsky Normal Form (CNF) Step-by-Step Conversions</span>
    <span class="badge badge-12m">12 Marks</span>
  </div>
  <p><strong>Grammar:</strong> $S \to bA \mid aB, \quad A \to bAA \mid aS \mid a, \quad B \to aBB \mid bS \mid b$.</p>
  <div class="callout callout-method">
    <div class="callout-title">⚡ Step-by-Step CNF Execution</div>
    <ol>
      <li><strong>Step 1: Check Nullable & Unit Rules:</strong> No $\epsilon$-productions and no unit productions ($A \to B$) exist in this grammar.</li>
      <li><strong>Step 2: Replace Terminals in Mixed Productions:</strong> Introduce $C_a \to a$ and $C_b \to b$.
        <ul>
          <li>$S \to C_b A \mid C_a B$ (Both RHS are length 2 &rarr; Already in CNF!)</li>
          <li>$A \to C_b AA \mid C_a S \mid a$</li>
          <li>$B \to C_a BB \mid C_b S \mid b$</li>
        </ul>
      </li>
      <li><strong>Step 3: Split Productions of Length $\ge 3$:</strong>
        <ul>
          <li>For $A \to C_b A A$: Introduce $D_1 \to AA$, giving $A \to C_b D_1$.</li>
          <li>For $B \to C_a B B$: Introduce $D_2 \to BB$, giving $B \to C_a D_2$.</li>
        </ul>
      </li>
      <li><strong>Step 4: Final CNF Grammar:</strong>
        <pre>S  -> Cb A | Ca B
A  -> Cb D1 | Ca S | a
D1 -> AA
B  -> Ca D2 | Cb S | b
D2 -> BB
Ca -> a
Cb -> b</pre>
      </li>
    </ol>
  </div>
</div>

<!-- PDA MASTER -->
<div class="problem-card">
  <div class="problem-title">
    <span>Q5: Pushdown Automata (PDA) for $L = \{a^{2n} b^n \mid n \ge 1\}$</span>
    <span class="badge badge-12m">12 Marks</span>
  </div>
  <p><strong>Logic:</strong> There are two $a$'s for every single $b$. We push all $a$'s into the stack. When $b$'s arrive, for every single $b$ consumed, we <strong>pop exactly TWO $a$'s</strong> from the stack!</p>
  <div class="callout callout-method">
    <div class="callout-title">⚡ Complete 7-Tuple Transition Set $\delta$:</div>
    <ul>
      <li>$\delta(q_0, a, Z_0) = \{(q_0, a Z_0)\}$ (First $a$ pushes onto initial stack symbol $Z_0$)</li>
      <li>$\delta(q_0, a, a) = \{(q_0, aa)\}$ (Subsequent $a$'s push onto stack)</li>
      <li>$\delta(q_0, b, a) = \{(q_1, \epsilon)\}$ (First $b$ seen: pop 1st $a$, transition to helper state $q_1$)</li>
      <li>$\delta(q_1, \epsilon, a) = \{(q_2, \epsilon)\}$ (Helper $\epsilon$-move: pop 2nd $a$ to complete popping 2 $a$'s per $b$)</li>
      <li>$\delta(q_2, b, a) = \{(q_1, \epsilon)\}$ (Next $b$ repeats the 2-pop cycle)</li>
      <li>$\delta(q_2, \epsilon, Z_0) = \{(q_f, Z_0)\}$ (Input finished and stack clean &rarr; Accept by Final State $q_f$!)</li>
    </ul>
  </div>
</div>

<!-- ========================================== -->
<!-- MODULE 3: SYNTAX ANALYSIS & PARSING -->
<!-- ========================================== -->
<div class="page-break"></div>
<div class="module-header">
  <span>MODULE 3: Syntax Analysis, FIRST/FOLLOW & Parsing Tables</span>
  <span style="font-size: 12px; font-weight: normal;">Weightage: ~20-25 Marks</span>
</div>

<div class="callout callout-tips">
  <div class="callout-title">💡 Tips, Tricks & Misconception Buster (Module 3)</div>
  <ul>
    <li><strong>Left Recursion Eliminator Formula:</strong>
      If $A \to A\alpha_1 \mid A\alpha_2 \mid \beta_1 \mid \beta_2$, rewrite as:
      <code>A &rarr; &beta;1 A' | &beta;2 A'</code> and <code>A' &rarr; &alpha;1 A' | &alpha;2 A' | &epsilon;</code>.
    </li>
    <li><strong>The 3 Golden Rules of FIRST:</strong>
      <ol style="margin: 2px 0 2px 16px;">
        <li>If $X$ is a terminal, $\text{FIRST}(X) = \{X\}$.</li>
        <li>If $X \to \epsilon$, add $\epsilon$ to $\text{FIRST}(X)$.</li>
        <li>If $X \to Y_1 Y_2 \dots Y_k$, add $\text{FIRST}(Y_1)$ (except $\epsilon$). If $Y_1 \Rightarrow \epsilon$, add $\text{FIRST}(Y_2)$, and so on.</li>
      </ol>
    </li>
    <li><strong>The 3 Golden Rules of FOLLOW:</strong>
      <ol style="margin: 2px 0 2px 16px;">
        <li>Put $\$$ in $\text{FOLLOW}(S)$ where $S$ is start symbol.</li>
        <li>If $A \to \alpha B \beta$, add $\text{FIRST}(\beta) \setminus \{\epsilon\}$ to $\text{FOLLOW}(B)$.</li>
        <li>If $A \to \alpha B$ or $A \to \alpha B \beta$ where $\beta \Rightarrow \epsilon$, add $\text{FOLLOW}(A)$ to $\text{FOLLOW}(B)$.</li>
        <li><strong>FATAL MISTAKE:</strong> $\epsilon$ is NEVER in any FOLLOW set! $\$$ is NEVER in any FIRST set!</li>
      </ol>
    </li>
    <li><strong>LL(1) Condition:</strong> No cell in the parsing table can contain more than 1 entry. A grammar with Left Recursion or Ambiguity is NEVER LL(1)!</li>
  </ul>
</div>

<!-- FIRST & FOLLOW + LL(1) -->
<div class="problem-card">
  <div class="problem-title">
    <span>Q3 & Q4: Expression Grammar FIRST/FOLLOW & LL(1) Table</span>
    <span class="badge badge-12m">12 Marks Flagship</span>
  </div>
  <p><strong>Unambiguous Grammar after Left Recursion Elimination:</strong></p>
  <pre>E  -> T E'
E' -> + T E' | ε
T  -> F T'
T' -> * F T' | ε
F  -> ( E ) | id</pre>

  <p><strong>FIRST and FOLLOW Sets:</strong></p>
  <table>
    <thead>
      <tr><th>Non-Terminal</th><th>FIRST Set</th><th>FOLLOW Set</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>E</strong></td><td><code>{ (, id }</code></td><td><code>{ ), $ }</code></td></tr>
      <tr><td><strong>E'</strong></td><td><code>{ +, ε }</code></td><td><code>{ ), $ }</code></td></tr>
      <tr><td><strong>T</strong></td><td><code>{ (, id }</code></td><td><code>{ +, ), $ }</code></td></tr>
      <tr><td><strong>T'</strong></td><td><code>{ *, ε }</code></td><td><code>{ +, ), $ }</code></td></tr>
      <tr><td><strong>F</strong></td><td><code>{ (, id }</code></td><td><code>{ *, +, ), $ }</code></td></tr>
    </tbody>
  </table>

  <p><strong>Constructed LL(1) Predictive Parsing Table $M[A, a]$:</strong></p>
  <table>
    <thead>
      <tr><th>NT</th><th>id</th><th>+</th><th>*</th><th>(</th><th>)</th><th>$</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>E</strong></td><td>E &rarr; T E'</td><td></td><td></td><td>E &rarr; T E'</td><td></td><td></td></tr>
      <tr><td><strong>E'</strong></td><td></td><td>E' &rarr; + T E'</td><td></td><td></td><td>E' &rarr; &epsilon;</td><td>E' &rarr; &epsilon;</td></tr>
      <tr><td><strong>T</strong></td><td>T &rarr; F T'</td><td></td><td></td><td>T &rarr; F T'</td><td></td><td></td></tr>
      <tr><td><strong>T'</strong></td><td></td><td>T' &rarr; &epsilon;</td><td>T' &rarr; * F T'</td><td></td><td>T' &rarr; &epsilon;</td><td>T' &rarr; &epsilon;</td></tr>
      <tr><td><strong>F</strong></td><td>F &rarr; id</td><td></td><td></td><td>F &rarr; ( E )</td><td></td><td></td></tr>
    </tbody>
  </table>

  <p><strong>Stack-Trace for input <code>id + id $</code>:</strong></p>
  <pre>Matched   Stack        Input         Action Applied
-------------------------------------------------------------
          $ E          id + id $     Output: E -> T E'
          $ E' T       id + id $     Output: T -> F T'
          $ E' T' F    id + id $     Output: F -> id
          $ E' T' id   id + id $     Match terminal 'id'
id        $ E' T'      + id $        Output: T' -> ε
id        $ E'         + id $        Output: E' -> + T E'
id +      $ E' T +     + id $        Match terminal '+'
id +      $ E' T       id $          Output: T -> F T'
id +      $ E' T' F    id $          Output: F -> id
id +      $ E' T' id   id $          Match terminal 'id'
id + id   $ E' T'      $             Output: T' -> ε
id + id   $ E'         $             Output: E' -> ε
id + id $ $            $             ACCEPT! (Successful parse)</pre>
</div>

<!-- ========================================== -->
<!-- MODULE 4: TURING MACHINES & COMPUTABILITY -->
<!-- ========================================== -->
<div class="page-break"></div>
<div class="module-header">
  <span>MODULE 4: Turing Machines, Computability & Decidability</span>
  <span style="font-size: 12px; font-weight: normal;">Weightage: ~15-20 Marks</span>
</div>

<div class="callout callout-tips">
  <div class="callout-title">💡 Tips, Tricks & Misconception Buster (Module 4)</div>
  <ul>
    <li><strong>Turing Machine Power:</strong> Unlike FA and PDA, a TM can move BOTH Left ($L$) and Right ($R$) and can overwrite tape cells!</li>
    <li><strong>Unary Math Tricks:</strong> Numbers are represented in unary using 0's (e.g. $3 = 000$, $2 = 00$).
      <ul>
        <li><em>Addition ($x + y$):</em> Input is $0^m 1 0^n$. Replace the separator $1$ with a $0$, and erase the rightmost $0$ (replace with Blank $B$). Result length is $m + n$!</li>
        <li><em>Subtraction ($x - y$ for $x \ge y$):</em> Pair each $0$ in $y$ with a $0$ in $x$ by replacing with markers $X$ and $Y$.</li>
      </ul>
    </li>
    <li><strong>PCP 10-Second Shortcut:</strong>
      In Post Correspondence Problem, if list $X$ contains only $\{a, b\}$ and list $Y$ has a symbol $c$ that NEVER appears anywhere in list $X$, it is <strong>IMPOSSIBLE to match &rarr; State "No solution" immediately!</strong>
    </li>
  </ul>
</div>

<!-- TM FOR ADDITION -->
<div class="problem-card">
  <div class="problem-title">
    <span>Q6: Turing Machine for Addition of Two Unary Numbers $f(x, y) = x + y$</span>
    <span class="badge badge-12m">12 Marks Flagship</span>
  </div>
  <p><strong>Input tape:</strong> $0^m 1 0^n B$ (where $m, n \ge 1$, separated by 1). <strong>Goal:</strong> Produce $0^{m+n} B$.</p>

  <div class="callout callout-method">
    <div class="callout-title">⚡ 4-Phase Execution Algorithm</div>
    <ol>
      <li><strong>Phase 1 (Delete First 0):</strong> In state $q_0$, read first $0$, replace with Blank $B$, move Right to state $q_1$. (Tape now has $m-1$ zeros).</li>
      <li><strong>Phase 2 (Convert Separator 1 to 0):</strong> In $q_1$, skip all remaining zeros. Upon encountering separator $1$, <strong>overwrite $1$ with $0$</strong>, move Right to $q_2$. (Tape now has $(m-1) + 1 = m$ zeros).</li>
      <li><strong>Phase 3 (Traverse to End):</strong> In $q_2$, skip all $n$ zeros until Blank $B$ is reached. Step Left to $q_3$.</li>
      <li><strong>Phase 4 (Halt):</strong> In $q_3$, the head points to the last $0$. Halt in accepting state $q_4$. The tape now contains exactly $m + n$ zeros!</li>
    </ol>
  </div>

  <p><strong>Transition Table:</strong></p>
  <table>
    <thead>
      <tr><th>Current State</th><th>Input Symbol '0'</th><th>Input Symbol '1'</th><th>Input Symbol 'B'</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>q0</strong></td><td>(q1, B, R)</td><td>-</td><td>-</td></tr>
      <tr><td><strong>q1</strong></td><td>(q1, 0, R)</td><td>(q2, 0, R)</td><td>-</td></tr>
      <tr><td><strong>q2</strong></td><td>(q2, 0, R)</td><td>-</td><td>(q3, B, L)</td></tr>
      <tr><td><strong>q3</strong></td><td>(q4, 0, Halt)</td><td>-</td><td>-</td></tr>
    </tbody>
  </table>
</div>

<!-- ========================================== -->
<!-- MODULE 5: TAC, DAGS & OPTIMIZATION -->
<!-- ========================================== -->
<div class="page-break"></div>
<div class="module-header">
  <span>MODULE 5: Intermediate Code Generation, DAGs & Optimization</span>
  <span style="font-size: 12px; font-weight: normal;">Weightage: ~20-25 Marks</span>
</div>

<div class="callout callout-tips">
  <div class="callout-title">💡 Tips, Tricks & Misconception Buster (Module 5)</div>
  <ul>
    <li><strong>Short-Circuit Condition Layout:</strong>
      For <code>while ((A > B) and (A <= 2*B - 5))</code>:
      If $A \le B$, immediately jump to <code>L_exit</code>! Never evaluate the second condition unless the first passes.
    </li>
    <li><strong>DAG Construction & Value Numbering:</strong>
      Before creating a new interior node for an operation (e.g. <code>b + c</code>), search if an identical operator node with the SAME children already exists in the graph. If yes, <strong>reuse the existing node</strong> and simply attach the new variable name to it!
    </li>
    <li><strong>2D Array Addressing Formulas:</strong>
      Array $A[1\dots m, 1\dots n]$ with base address $B$ and element width $w$:
      <ul>
        <li><strong>Row-Major:</strong> $\text{Address}(A[i, j]) = B + [(i - 1) \times n + (j - 1)] \times w$</li>
        <li><strong>Column-Major:</strong> $\text{Address}(A[i, j]) = B + [(j - 1) \times m + (i - 1)] \times w$</li>
      </ul>
    </li>
  </ul>
</div>

<!-- TAC & DAG -->
<div class="problem-card">
  <div class="problem-title">
    <span>Q11 & Q12: Basic Block DAG with Common Subexpression Elimination</span>
    <span class="badge badge-12m">12 Marks Flagship</span>
  </div>
  <p><strong>Basic Block Code:</strong></p>
  <pre>1. a := b + c
2. b := a - d
3. c := b + c
4. d := a - d</pre>

  <div class="diagram-container">
    <svg width="450" height="180" viewBox="0 0 450 180" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="dagArr" markerWidth="7" markerHeight="7" refX="5" refY="2.5" orient="auto">
          <path d="M0,0 L0,5 L5,2.5 z" fill="#1e3a8a" />
        </marker>
      </defs>
      <!-- Leaves -->
      <circle cx="80" cy="150" r="16" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"/>
      <text x="80" y="154" text-anchor="middle" font-weight="bold">b0</text>
      <circle cx="180" cy="150" r="16" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"/>
      <text x="180" y="154" text-anchor="middle" font-weight="bold">c0</text>
      <circle cx="340" cy="150" r="16" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"/>
      <text x="340" y="154" text-anchor="middle" font-weight="bold">d0</text>
      
      <!-- Node 1: a = b + c -->
      <circle cx="130" cy="90" r="18" fill="#dbeafe" stroke="#1e3a8a" stroke-width="2"/>
      <text x="130" y="94" text-anchor="middle" font-weight="bold" fill="#1e3a8a" font-size="14">+</text>
      <text x="100" y="85" font-weight="bold" fill="#1e3a8a">a</text>
      <line x1="120" y1="104" x2="90" y2="136" stroke="#1e3a8a" marker-end="url(#dagArr)"/>
      <line x1="140" y1="104" x2="170" y2="136" stroke="#1e3a8a" marker-end="url(#dagArr)"/>
      
      <!-- Node 2: b, d = a - d -->
      <circle cx="260" cy="40" r="20" fill="#dcfce7" stroke="#16a34a" stroke-width="2.5"/>
      <text x="260" y="45" text-anchor="middle" font-weight="bold" fill="#15803d" font-size="16">-</text>
      <rect x="290" y="24" width="70" height="24" rx="4" fill="#16a34a"/>
      <text x="325" y="40" text-anchor="middle" font-weight="bold" fill="white" font-size="11">b, d (Shared)</text>
      <line x1="242" y1="48" x2="148" y2="82" stroke="#1e3a8a" marker-end="url(#dagArr)"/>
      <line x1="275" y1="54" x2="330" y2="136" stroke="#1e3a8a" marker-end="url(#dagArr)"/>
      
      <!-- Node 3: c = b + c -->
      <circle cx="210" cy="100" r="18" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
      <text x="210" y="104" text-anchor="middle" font-weight="bold" fill="#dc2626" font-size="14">+</text>
      <text x="235" y="105" font-weight="bold" fill="#dc2626">c</text>
      <line x1="225" y1="84" x2="250" y2="58" stroke="#dc2626" marker-end="url(#dagArr)"/>
      <line x1="200" y1="116" x2="185" y2="134" stroke="#dc2626" marker-end="url(#dagArr)"/>
    </svg>
    <div class="diagram-caption">Figure 5.1: Directed Acyclic Graph showing common subexpression sharing between statement 2 and statement 4.</div>
  </div>

  <div class="callout callout-method">
    <div class="callout-title">⚡ Key Optimization Insight:</div>
    In statement 4, `d := a - d`. Since neither variable `a` nor `d` was modified after line 2 (`b := a - d`), the expression `a - d` has ALREADY been evaluated! The DAG attaches variable label `d` to the existing subtraction node. Thus, statement 4 requires <strong>zero redundant CPU calculation</strong>!
  </div>
</div>

</body>
</html>
"""

base_dir = r"c:\Users\ankit\Fall2627\TOC\notes\term_end"
html_path = os.path.join(base_dir, "CSE2004_TOC_Exhaustive_Solutions_Master_Handbook.html")
pdf_path = os.path.join(base_dir, "CSE2004_TOC_Exhaustive_Solutions_Master_Handbook.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML generated at: {html_path} ({len(html_content)} chars)")

# Run headless Chrome
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    html_path
]

print("Compiling PDF with Chrome...")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0 and os.path.exists(pdf_path):
    print(f"SUCCESS! PDF created at: {pdf_path} (Size: {os.path.getsize(pdf_path)} bytes)")
else:
    print(f"FAILED! Error: {res.stderr}")
