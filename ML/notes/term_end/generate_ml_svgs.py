"""
generate_ml_svgs.py
Generates 8 high-definition, 100% XML-valid SVG diagrams for CSE4005 (Machine Learning):
1. svm_hyperplane_margin.svg
2. confusion_matrix_and_metrics.svg
3. smote_synthetic_interpolation.svg
4. kmeans_clustering_iterations.svg
5. adaboost_sequential_architecture.svg
6. pca_variance_maximization.svg
7. decision_tree_entropy_split.svg
8. bayes_naive_and_bbn.svg
"""

import os
import xml.etree.ElementTree as ET

OUT_DIR = r"c:\Users\ankit\Fall2627\ML\notes\term_end\images"
os.makedirs(OUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. SVM Hyperplane & Maximum Margin
# -------------------------------------------------------------
def gen_svm_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 500" width="950" height="500">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .box { fill: #1e293b; stroke: #334155; stroke-width: 2; rx: 8; }
      .axis { stroke: #64748b; stroke-width: 1.5; stroke-dasharray: 4,3; }
      .hyperplane { stroke: #38bdf8; stroke-width: 3; }
      .margin-line { stroke: #fbbf24; stroke-width: 2; stroke-dasharray: 6,4; }
      .margin-band { fill: rgba(56, 189, 248, 0.08); }
      .pos-pt { fill: #38bdf8; stroke: #ffffff; stroke-width: 1.5; }
      .neg-pt { fill: #f43f5e; stroke: #ffffff; stroke-width: 1.5; }
      .sv-circle { fill: none; stroke: #fbbf24; stroke-width: 2.5; stroke-dasharray: 3,2; }
      .title { fill: #38bdf8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; font-weight: bold; }
      .subtitle { fill: #94a3b8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; }
      .lbl { fill: #e2e8f0; font-family: 'Consolas', monospace; font-size: 12px; font-weight: bold; }
      .formula { fill: #34d399; font-family: 'Consolas', monospace; font-size: 12px; }
      .note { fill: #94a3b8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; }
      .arr { stroke: #fbbf24; stroke-width: 2; fill: none; marker-end: url(#arrow); }
    </style>
    <marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L0,6 L6,3 z" fill="#fbbf24" />
    </marker>
  </defs>

  <rect width="100%" height="100%" class="bg" />
  <rect x="20" y="15" width="910" height="470" class="box" />
  <text x="475" y="38" text-anchor="middle" class="title">SUPPORT VECTOR MACHINE (SVM) — MAXIMUM MARGIN HYPERPLANE</text>
  <text x="475" y="56" text-anchor="middle" class="subtitle">Primal: min (1/2)||w||² s.t. y_i(w^T x_i + b) &gt;= 1 | Geometric Margin M = 2 / ||w||</text>

  <!-- MARGIN BAND (Shaded Area between +1 and -1 hyperplanes) -->
  <polygon points="120,40 180,40 460,420 400,420" class="margin-band" />

  <!-- HYPERPLANES -->
  <!-- Positive Margin Line: w^T x + b = +1 -->
  <line x1="120" y1="40" x2="400" y2="420" class="margin-line" />
  <text x="75" y="60" class="lbl" fill="#fbbf24">w^T x + b = +1</text>

  <!-- Decision Boundary: w^T x + b = 0 -->
  <line x1="150" y1="40" x2="430" y2="420" class="hyperplane" />
  <text x="175" y="35" class="lbl" fill="#38bdf8">w^T x + b = 0 (Separating Hyperplane)</text>

  <!-- Negative Margin Line: w^T x + b = -1 -->
  <line x1="180" y1="40" x2="460" y2="420" class="margin-line" />
  <text x="470" y="425" class="lbl" fill="#fbbf24">w^T x + b = -1</text>

  <!-- NORMAL VECTOR w -->
  <line x1="290" y1="230" x2="350" y2="185" stroke="#a855f7" stroke-width="2.5" marker-end="url(#arrow)" />
  <text x="360" y="180" class="lbl" fill="#c084fc">Normal Vector w (⊥ Hyperplane)</text>

  <!-- MARGIN WIDTH ARROW -->
  <line x1="220" y1="175" x2="260" y2="145" stroke="#fbbf24" stroke-width="2" />
  <text x="210" y="140" class="lbl" fill="#fbbf24">Margin M = 2 / ||w||</text>

  <!-- POSITIVE CLASS DATA POINTS (+1) -->
  <circle cx="150" cy="120" r="6" class="pos-pt" />
  <circle cx="180" cy="190" r="6" class="pos-pt" />
  <circle cx="100" cy="200" r="6" class="pos-pt" />
  <circle cx="140" cy="280" r="6" class="pos-pt" />
  <circle cx="210" cy="260" r="6" class="pos-pt" />
  <!-- SUPPORT VECTORS (+1) -->
  <circle cx="210" cy="160" r="6" class="pos-pt" />
  <circle cx="210" cy="160" r="12" class="sv-circle" />
  <circle cx="280" cy="255" r="6" class="pos-pt" />
  <circle cx="280" cy="255" r="12" class="sv-circle" />

  <!-- NEGATIVE CLASS DATA POINTS (-1) -->
  <circle cx="390" cy="150" r="6" class="neg-pt" />
  <circle cx="430" cy="220" r="6" class="neg-pt" />
  <circle cx="470" cy="190" r="6" class="neg-pt" />
  <circle cx="410" cy="310" r="6" class="neg-pt" />
  <circle cx="480" cy="350" r="6" class="neg-pt" />
  <!-- SUPPORT VECTORS (-1) -->
  <circle cx="350" cy="270" r="6" class="neg-pt" />
  <circle cx="350" cy="270" r="12" class="sv-circle" />

  <!-- RIGHT PANEL: MATHEMATICAL DERIVATION & KEY PRINCIPLES -->
  <g transform="translate(560, 80)">
    <rect width="345" height="380" rx="6" style="fill:#111827; stroke:#475569; stroke-width:1.5;" />
    <text x="172" y="28" text-anchor="middle" class="lbl" fill="#38bdf8">SVM EXAM FORMULAS &amp; CONCEPTS</text>

    <text x="15" y="60" class="lbl" fill="#fbbf24">1. Dual Optimization Problem:</text>
    <text x="15" y="80" class="formula">max_α Σ α_i - 1/2 ΣΣ α_i α_j y_i y_j K(x_i, x_j)</text>
    <text x="15" y="100" class="note">subject to: 0 &lt;= α_i &lt;= C and Σ α_i y_i = 0</text>

    <text x="15" y="130" class="lbl" fill="#fbbf24">2. Weight Vector Reconstruction:</text>
    <text x="15" y="150" class="formula">w = Σ α_i y_i x_i (Only Support Vectors α_i &gt; 0)</text>

    <text x="15" y="180" class="lbl" fill="#fbbf24">3. Decision Function:</text>
    <text x="15" y="200" class="formula">f(x) = sign( Σ α_i y_i K(x_i, x) + b )</text>

    <text x="15" y="235" class="lbl" fill="#fbbf24">4. Popular Kernel Functions:</text>
    <text x="15" y="255" class="note">• Linear: K(x, z) = x^T z</text>
    <text x="15" y="275" class="note">• Polynomial: K(x, z) = (x^T z + c)^d</text>
    <text x="15" y="295" class="note">• RBF / Gaussian: K(x, z) = exp(-γ ||x - z||²)</text>

    <text x="15" y="330" class="lbl" fill="#f43f5e">5. Mercer&apos;s Condition:</text>
    <text x="15" y="350" class="note">Gram matrix K_ij must be symmetric</text>
    <text x="15" y="365" class="note">and positive semi-definite (all λ_i &gt;= 0).</text>
  </g>
</svg>'''
    with open(os.path.join(OUT_DIR, "svm_hyperplane_margin.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# 2. Confusion Matrix & Evaluation Metrics
# -------------------------------------------------------------
def gen_confusion_matrix_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 510" width="950" height="510">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .box { fill: #1e293b; stroke: #334155; stroke-width: 2; rx: 8; }
      .tp-box { fill: #064e3b; stroke: #34d399; stroke-width: 2; rx: 6; }
      .fn-box { fill: #4c0519; stroke: #f43f5e; stroke-width: 2; rx: 6; }
      .fp-box { fill: #451a03; stroke: #f59e0b; stroke-width: 2; rx: 6; }
      .tn-box { fill: #1e3a8a; stroke: #60a5fa; stroke-width: 2; rx: 6; }
      .title { fill: #38bdf8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; font-weight: bold; }
      .subtitle { fill: #94a3b8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; }
      .cell-title { fill: #ffffff; font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; font-weight: bold; text-anchor: middle; }
      .cell-desc { fill: #cbd5e1; font-family: 'Consolas', monospace; font-size: 11px; text-anchor: middle; }
      .lbl { fill: #e2e8f0; font-family: 'Consolas', monospace; font-size: 13px; font-weight: bold; }
      .hdr { fill: #38bdf8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; font-weight: bold; text-anchor: middle; }
      .formula { fill: #34d399; font-family: 'Consolas', monospace; font-size: 12px; font-weight: bold; }
      .note { fill: #94a3b8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; }
    </style>
  </defs>

  <rect width="100%" height="100%" class="bg" />
  <rect x="20" y="15" width="910" height="480" class="box" />
  <text x="475" y="38" text-anchor="middle" class="title">CLASSIFICATION PERFORMANCE METRICS &amp; CONFUSION MATRIX</text>
  <text x="475" y="56" text-anchor="middle" class="subtitle">Complete Diagnostic Framework: Accuracy, Precision, Recall, Specificity, F1-Score &amp; ROC-AUC</text>

  <!-- 2x2 CONFUSION MATRIX GRID -->
  <g transform="translate(60, 90)">
    <!-- Column Headers: Predicted Class -->
    <text x="210" y="0" class="hdr" font-size="14">PREDICTED CLASS</text>
    <text x="135" y="25" class="hdr" fill="#34d399">Predicted Positive (1)</text>
    <text x="285" y="25" class="hdr" fill="#f43f5e">Predicted Negative (0)</text>

    <!-- Row Headers: Actual Class -->
    <text x="-25" y="115" class="hdr" font-size="14" transform="rotate(-90, -25, 115)">ACTUAL CLASS</text>
    <text x="45" y="85" class="lbl" fill="#34d399" text-anchor="end">Actual Positive (1)</text>
    <text x="45" y="195" class="lbl" fill="#f43f5e" text-anchor="end">Actual Negative (0)</text>

    <!-- QUADRANT 1: TRUE POSITIVE (TP) -->
    <rect x="60" y="40" width="150" height="100" class="tp-box" />
    <text x="135" y="75" class="cell-title">TRUE POSITIVE (TP)</text>
    <text x="135" y="98" class="cell-desc">Actual = 1, Pred = 1</text>
    <text x="135" y="118" class="cell-desc" fill="#a7f3d0">Hits / Correct Alarm</text>

    <!-- QUADRANT 2: FALSE NEGATIVE (FN) -->
    <rect x="220" y="40" width="150" height="100" class="fn-box" />
    <text x="295" y="75" class="cell-title">FALSE NEGATIVE (FN)</text>
    <text x="295" y="98" class="cell-desc">Actual = 1, Pred = 0</text>
    <text x="295" y="118" class="cell-desc" fill="#fecdd3">Type II Error (Miss)</text>

    <!-- QUADRANT 3: FALSE POSITIVE (FP) -->
    <rect x="60" y="150" width="150" height="100" class="fp-box" />
    <text x="135" y="185" class="cell-title">FALSE POSITIVE (FP)</text>
    <text x="135" y="208" class="cell-desc">Actual = 0, Pred = 1</text>
    <text x="135" y="228" class="cell-desc" fill="#fed7aa">Type I Error (False Alarm)</text>

    <!-- QUADRANT 4: TRUE NEGATIVE (TN) -->
    <rect x="220" y="150" width="150" height="100" class="tn-box" />
    <text x="295" y="185" class="cell-title">TRUE NEGATIVE (TN)</text>
    <text x="295" y="208" class="cell-desc">Actual = 0, Pred = 0</text>
    <text x="295" y="228" class="cell-desc" fill="#bfdbfe">Correct Rejection</text>

    <!-- Horizontal Arrow for Precision -->
    <path d="M 60 265 L 210 265" stroke="#34d399" stroke-width="2" />
    <text x="135" y="285" text-anchor="middle" class="formula">Precision = TP / (TP + FP)</text>

    <!-- Vertical Arrow for Recall -->
    <path d="M 385 40 L 385 140" stroke="#38bdf8" stroke-width="2" />
    <text x="400" y="95" class="formula" fill="#38bdf8">Recall = TP / (TP + FN)</text>
  </g>

  <!-- RIGHT PANEL: MATHEMATICAL METRICS & FORMULA ROSTER -->
  <g transform="translate(560, 75)">
    <rect width="345" height="395" rx="6" style="fill:#111827; stroke:#475569; stroke-width:1.5;" />
    <text x="172" y="26" text-anchor="middle" class="lbl" fill="#38bdf8">MASTER EVALUATION FORMULAS</text>

    <text x="15" y="55" class="lbl" fill="#fbbf24">1. Accuracy:</text>
    <text x="15" y="75" class="formula">Accuracy = (TP + TN) / (TP + TN + FP + FN)</text>
    <text x="15" y="92" class="note">Warning: Misleading in imbalanced data!</text>

    <text x="15" y="118" class="lbl" fill="#fbbf24">2. Precision (Positive Predictive Value):</text>
    <text x="15" y="138" class="formula">Precision = TP / (TP + FP)</text>
    <text x="15" y="154" class="note">Critical when False Positives are costly (Spam filter).</text>

    <text x="15" y="180" class="lbl" fill="#fbbf24">3. Recall / Sensitivity (True Positive Rate):</text>
    <text x="15" y="200" class="formula">Recall (TPR) = TP / (TP + FN)</text>
    <text x="15" y="216" class="note">Critical when False Negatives are fatal (Cancer diagnosis).</text>

    <text x="15" y="242" class="lbl" fill="#fbbf24">4. Specificity (True Negative Rate):</text>
    <text x="15" y="262" class="formula">Specificity (TNR) = TN / (TN + FP)</text>
    <text x="15" y="278" class="note">FPR = 1 - Specificity = FP / (TN + FP)</text>

    <text x="15" y="304" class="lbl" fill="#fbbf24">5. F1-Score (Harmonic Mean):</text>
    <text x="15" y="324" class="formula">F1 = 2·(Prec · Recall) / (Prec + Recall)</text>
    <text x="15" y="342" class="formula">F1 = 2TP / (2TP + FP + FN)</text>

    <text x="15" y="368" class="lbl" fill="#fbbf24">6. ROC-AUC:</text>
    <text x="15" y="385" class="note">Plot TPR (Recall) vs FPR. Ideal AUC = 1.0; Random = 0.5.</text>
  </g>
</svg>'''
    with open(os.path.join(OUT_DIR, "confusion_matrix_and_metrics.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# 3. SMOTE Synthetic Interpolation Diagram
# -------------------------------------------------------------
def gen_smote_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 490" width="950" height="490">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .box { fill: #1e293b; stroke: #334155; stroke-width: 2; rx: 8; }
      .maj-pt { fill: #475569; stroke: #64748b; stroke-width: 1.5; }
      .min-pt { fill: #f43f5e; stroke: #ffffff; stroke-width: 2; }
      .synth-pt { fill: #34d399; stroke: #ffffff; stroke-width: 2.5; }
      .line-interp { stroke: #fbbf24; stroke-width: 2.5; stroke-dasharray: 6,4; }
      .title { fill: #38bdf8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; font-weight: bold; }
      .subtitle { fill: #94a3b8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; }
      .lbl { fill: #e2e8f0; font-family: 'Consolas', monospace; font-size: 13px; font-weight: bold; }
      .formula { fill: #34d399; font-family: 'Consolas', monospace; font-size: 12px; }
      .note { fill: #cbd5e1; font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; }
    </style>
  </defs>

  <rect width="100%" height="100%" class="bg" />
  <rect x="20" y="15" width="910" height="460" class="box" />
  <text x="475" y="38" text-anchor="middle" class="title">SMOTE: SYNTHETIC MINORITY OVER-SAMPLING TECHNIQUE</text>
  <text x="475" y="56" text-anchor="middle" class="subtitle">Feature Space Interpolation: x_new = x_i + λ · (x_zi - x_i),  where λ ~ U(0, 1)</text>

  <!-- LEFT: ORIGINAL IMBALANCED DATASET -->
  <g transform="translate(40, 80)">
    <rect width="380" height="370" rx="6" style="fill:#111827; stroke:#475569; stroke-width:1.5;" />
    <text x="190" y="28" text-anchor="middle" class="lbl" fill="#f43f5e">ORIGINAL IMBALANCED DISTRIBUTION (99:1)</text>

    <!-- Majority Points (Blue-Gray Dots) -->
    <circle cx="60" cy="80" r="5" class="maj-pt" /><circle cx="100" cy="65" r="5" class="maj-pt" />
    <circle cx="140" cy="90" r="5" class="maj-pt" /><circle cx="80" cy="120" r="5" class="maj-pt" />
    <circle cx="120" cy="140" r="5" class="maj-pt" /><circle cx="160" cy="110" r="5" class="maj-pt" />
    <circle cx="200" cy="75" r="5" class="maj-pt" /><circle cx="230" cy="130" r="5" class="maj-pt" />
    <circle cx="70" cy="170" r="5" class="maj-pt" /><circle cx="110" cy="190" r="5" class="maj-pt" />
    <circle cx="150" cy="210" r="5" class="maj-pt" /><circle cx="190" cy="180" r="5" class="maj-pt" />
    <circle cx="250" cy="90" r="5" class="maj-pt" /><circle cx="280" cy="140" r="5" class="maj-pt" />
    <circle cx="220" cy="230" r="5" class="maj-pt" /><circle cx="260" cy="200" r="5" class="maj-pt" />
    <circle cx="300" cy="180" r="5" class="maj-pt" /><circle cx="330" cy="120" r="5" class="maj-pt" />

    <!-- Minority Points (Red Stars / Dots) -->
    <circle cx="290" cy="270" r="7" class="min-pt" />
    <circle cx="330" cy="310" r="7" class="min-pt" />
    <circle cx="270" cy="330" r="7" class="min-pt" />
    <text x="190" y="350" text-anchor="middle" class="note">Minority class is severely sparse &amp; isolated!</text>
  </g>

  <!-- RIGHT: SMOTE GENERATION DETAIL -->
  <g transform="translate(460, 80)">
    <rect width="450" height="370" rx="6" style="fill:#111827; stroke:#475569; stroke-width:1.5;" />
    <text x="225" y="28" text-anchor="middle" class="lbl" fill="#34d399">SMOTE LINEAR INTERPOLATION MECHANISM</text>

    <!-- Seed Point x_i -->
    <circle cx="90" cy="200" r="9" class="min-pt" />
    <text x="40" y="195" class="lbl" fill="#f43f5e">x_i (2, 4)</text>
    <text x="30" y="215" class="note">Seed Instance</text>

    <!-- Line Segment to Neighbor x_zi -->
    <line x1="90" y1="200" x2="310" y2="100" class="line-interp" />

    <!-- Neighbor Point x_zi -->
    <circle cx="310" cy="100" r="9" class="min-pt" />
    <text x="325" y="95" class="lbl" fill="#f43f5e">x_zi (6, 10)</text>
    <text x="325" y="115" class="note">k-NN Neighbor</text>

    <!-- Synthetic Point x_new on line (λ = 0.5) -->
    <circle cx="200" cy="150" r="9" class="synth-pt" />
    <circle cx="200" cy="150" r="16" fill="none" stroke="#34d399" stroke-width="2" stroke-dasharray="3,2" />
    <text x="145" y="135" class="lbl" fill="#34d399">x_new = (4, 7)</text>
    <text x="135" y="175" class="formula">λ = 0.5 (Midpoint)</text>

    <!-- Another Synthetic Point (λ = 0.25) -->
    <circle cx="145" cy="175" r="7" class="synth-pt" style="fill:#10b981;" />
    <text x="145" y="195" class="formula">λ = 0.25</text>

    <!-- Callout Box on Benefits -->
    <rect x="25" y="240" width="400" height="110" rx="6" style="fill:#1e293b; stroke:#334155;" />
    <text x="35" y="265" class="lbl" fill="#fbbf24">Why SMOTE Outperforms Random Oversampling:</text>
    <text x="35" y="288" class="note">1. Random Oversampling duplicates exact coordinates $\to$ Overfitting.</text>
    <text x="35" y="308" class="note">2. SMOTE creates new convex combinations along line segments.</text>
    <text x="35" y="328" class="note">3. Expands minority decision boundary without memorizing points.</text>
  </g>
</svg>'''
    with open(os.path.join(OUT_DIR, "smote_synthetic_interpolation.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# 4. K-Means Clustering Iterations
# -------------------------------------------------------------
def gen_kmeans_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 490" width="950" height="490">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .box { fill: #1e293b; stroke: #334155; stroke-width: 2; rx: 8; }
      .panel { fill: #111827; stroke: #475569; stroke-width: 1.5; rx: 6; }
      .c1-pt { fill: #38bdf8; stroke: #ffffff; stroke-width: 1.5; }
      .c2-pt { fill: #f43f5e; stroke: #ffffff; stroke-width: 1.5; }
      .c1-centroid { fill: #0284c7; stroke: #38bdf8; stroke-width: 2.5; }
      .c2-centroid { fill: #e11d48; stroke: #f43f5e; stroke-width: 2.5; }
      .boundary { stroke: #fbbf24; stroke-width: 2; stroke-dasharray: 5,4; }
      .title { fill: #38bdf8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; font-weight: bold; }
      .subtitle { fill: #94a3b8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; }
      .lbl { fill: #e2e8f0; font-family: 'Consolas', monospace; font-size: 12px; font-weight: bold; }
      .step-hdr { fill: #fbbf24; font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; font-weight: bold; text-anchor: middle; }
      .formula { fill: #34d399; font-family: 'Consolas', monospace; font-size: 12px; }
    </style>
  </defs>

  <rect width="100%" height="100%" class="bg" />
  <rect x="20" y="15" width="910" height="460" class="box" />
  <text x="475" y="38" text-anchor="middle" class="title">K-MEANS CLUSTERING: LLOYD&apos;S ALGORITHM &amp; CONVERGENCE</text>
  <text x="475" y="56" text-anchor="middle" class="subtitle">Minimizing WCSS: J = Σ Σ ||x - μ_k||² via Alternating Assignment &amp; Centroid Update Steps</text>

  <!-- STEP 1: INITIALIZATION & INITIAL ASSIGNMENT -->
  <g transform="translate(40, 80)">
    <rect width="270" height="360" class="panel" />
    <text x="135" y="28" class="step-hdr">1. INITIALIZATION (K=2)</text>

    <!-- Cluster 1 points -->
    <circle cx="60" cy="110" r="5" class="c1-pt" /><circle cx="90" cy="90" r="5" class="c1-pt" />
    <circle cx="70" cy="140" r="5" class="c1-pt" /><circle cx="100" cy="130" r="5" class="c1-pt" />

    <!-- Cluster 2 points -->
    <circle cx="170" cy="220" r="5" class="c2-pt" /><circle cx="210" cy="200" r="5" class="c2-pt" />
    <circle cx="180" cy="250" r="5" class="c2-pt" /><circle cx="220" cy="240" r="5" class="c2-pt" />

    <!-- Initial Random Centroids (Cross / Diamond) -->
    <rect x="75" y="80" width="12" height="12" transform="rotate(45, 81, 86)" class="c1-centroid" />
    <text x="95" y="75" class="lbl" fill="#38bdf8">μ1 (init)</text>

    <rect x="185" y="170" width="12" height="12" transform="rotate(45, 191, 176)" class="c2-centroid" />
    <text x="205" y="175" class="lbl" fill="#f43f5e">μ2 (init)</text>

    <line x1="20" y1="210" x2="250" y2="80" class="boundary" />
    <text x="135" y="325" text-anchor="middle" class="lbl">Assign each point to</text>
    <text x="135" y="342" text-anchor="middle" class="formula">nearest centroid</text>
  </g>

  <!-- STEP 2: RECOMPUTE CENTROIDS (SHIFT) -->
  <g transform="translate(340, 80)">
    <rect width="270" height="360" class="panel" />
    <text x="135" y="28" class="step-hdr">2. RECOMPUTE CENTROIDS</text>

    <!-- Points with lines to new centroid -->
    <circle cx="60" cy="110" r="5" class="c1-pt" /><circle cx="90" cy="90" r="5" class="c1-pt" />
    <circle cx="70" cy="140" r="5" class="c1-pt" /><circle cx="100" cy="130" r="5" class="c1-pt" />

    <!-- New Center of Gravity μ1* = mean(x in C1) -->
    <rect x="74" y="112" width="14" height="14" transform="rotate(45, 81, 119)" class="c1-centroid" />
    <text x="95" y="125" class="lbl" fill="#38bdf8">μ1 (mean)</text>

    <circle cx="170" cy="220" r="5" class="c2-pt" /><circle cx="210" cy="200" r="5" class="c2-pt" />
    <circle cx="180" cy="250" r="5" class="c2-pt" /><circle cx="220" cy="240" r="5" class="c2-pt" />

    <!-- New Center of Gravity μ2* = mean(x in C2) -->
    <rect x="188" y="221" width="14" height="14" transform="rotate(45, 195, 228)" class="c2-centroid" />
    <text x="145" y="265" class="lbl" fill="#f43f5e">μ2 (mean)</text>

    <text x="135" y="325" text-anchor="middle" class="lbl">Centroids shift to</text>
    <text x="135" y="342" text-anchor="middle" class="formula">μ_k = (1/|C_k|) Σ x_i</text>
  </g>

  <!-- STEP 3: CONVERGENCE -->
  <g transform="translate(640, 80)">
    <rect width="270" height="360" class="panel" />
    <text x="135" y="28" class="step-hdr" fill="#34d399">3. FINAL CONVERGENCE</text>

    <circle cx="60" cy="110" r="5" class="c1-pt" /><circle cx="90" cy="90" r="5" class="c1-pt" />
    <circle cx="70" cy="140" r="5" class="c1-pt" /><circle cx="100" cy="130" r="5" class="c1-pt" />
    <rect x="74" y="112" width="14" height="14" transform="rotate(45, 81, 119)" class="c1-centroid" />

    <circle cx="170" cy="220" r="5" class="c2-pt" /><circle cx="210" cy="200" r="5" class="c2-pt" />
    <circle cx="180" cy="250" r="5" class="c2-pt" /><circle cx="220" cy="240" r="5" class="c2-pt" />
    <rect x="188" y="221" width="14" height="14" transform="rotate(45, 195, 228)" class="c2-centroid" />

    <!-- Final Voronoi Decision Boundary -->
    <line x1="20" y1="240" x2="250" y2="100" class="boundary" stroke="#34d399" />

    <text x="135" y="325" text-anchor="middle" class="lbl" fill="#34d399">Centroids stop moving</text>
    <text x="135" y="342" text-anchor="middle" class="formula">WCSS minimum reached!</text>
  </g>
</svg>'''
    with open(os.path.join(OUT_DIR, "kmeans_clustering_iterations.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# 5. AdaBoost Sequential Architecture
# -------------------------------------------------------------
def gen_adaboost_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 490" width="950" height="490">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .box { fill: #1e293b; stroke: #334155; stroke-width: 2; rx: 8; }
      .round-box { fill: #111827; stroke: #818cf8; stroke-width: 2; rx: 6; }
      .weak-box { fill: #1e1b4b; stroke: #6366f1; stroke-width: 1.5; rx: 4; }
      .title { fill: #38bdf8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; font-weight: bold; }
      .subtitle { fill: #94a3b8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; }
      .lbl { fill: #e2e8f0; font-family: 'Consolas', monospace; font-size: 12px; font-weight: bold; }
      .formula { fill: #34d399; font-family: 'Consolas', monospace; font-size: 12px; }
      .note { fill: #94a3b8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; }
      .arr { stroke: #38bdf8; stroke-width: 2; fill: none; marker-end: url(#bluearr); }
    </style>
    <marker id="bluearr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L0,6 L6,3 z" fill="#38bdf8" />
    </marker>
  </defs>

  <rect width="100%" height="100%" class="bg" />
  <rect x="20" y="15" width="910" height="460" class="box" />
  <text x="475" y="38" text-anchor="middle" class="title">ADABOOST: SEQUENTIAL ENSEMBLE ARCHITECTURE &amp; WEIGHT REBALANCING</text>
  <text x="475" y="56" text-anchor="middle" class="subtitle">Final Prediction: H(x) = sign( Σ α_t h_t(x) ) | α_t = 0.5 · ln((1 - ε_t) / ε_t)</text>

  <!-- ROUND 1 -->
  <g transform="translate(40, 85)">
    <rect width="250" height="320" class="round-box" />
    <text x="125" y="28" text-anchor="middle" class="lbl" fill="#38bdf8">ROUND 1 (t = 1)</text>

    <text x="15" y="60" class="note">Equal Weights: w_i = 1/N = 0.20</text>
    <!-- Sample dots -->
    <circle cx="50" cy="95" r="6" fill="#38bdf8" /><text x="65" y="99" class="note">x1 (correct)</text>
    <circle cx="50" cy="130" r="9" fill="#f43f5e" /><text x="65" y="134" class="note" fill="#f43f5e">x2 (WRONG!)</text>
    <circle cx="50" cy="165" r="6" fill="#38bdf8" /><text x="65" y="169" class="note">x3 (correct)</text>
    <circle cx="50" cy="200" r="9" fill="#f43f5e" /><text x="65" y="204" class="note" fill="#f43f5e">x4 (WRONG!)</text>
    <circle cx="50" cy="235" r="6" fill="#38bdf8" /><text x="65" y="239" class="note">x5 (correct)</text>

    <!-- Metrics -->
    <text x="15" y="275" class="formula">ε_1 = 0.2 + 0.2 = 0.40</text>
    <text x="15" y="295" class="formula">α_1 = 0.5 ln(1.5) = 0.2027</text>
  </g>

  <!-- ARROW TO ROUND 2 -->
  <line x1="290" y1="240" x2="335" y2="240" class="arr" />

  <!-- ROUND 2 -->
  <g transform="translate(340, 85)">
    <rect width="250" height="320" class="round-box" />
    <text x="125" y="28" text-anchor="middle" class="lbl" fill="#fbbf24">ROUND 2 (t = 2)</text>

    <text x="15" y="60" class="note">Reweighted Distribution:</text>
    <!-- Samples with modified size -->
    <circle cx="50" cy="95" r="4.5" fill="#38bdf8" /><text x="65" y="99" class="note">w1 shrinks (0.17)</text>
    <circle cx="50" cy="130" r="14" fill="#f43f5e" /><text x="75" y="134" class="lbl" fill="#f43f5e">w2 GROWS (0.25)</text>
    <circle cx="50" cy="165" r="4.5" fill="#38bdf8" /><text x="65" y="169" class="note">w3 shrinks (0.17)</text>
    <circle cx="50" cy="200" r="14" fill="#f43f5e" /><text x="75" y="204" class="lbl" fill="#f43f5e">w4 GROWS (0.25)</text>
    <circle cx="50" cy="235" r="4.5" fill="#38bdf8" /><text x="65" y="239" class="note">w5 shrinks (0.17)</text>

    <text x="15" y="275" class="formula">Classifier h_2 focuses</text>
    <text x="15" y="295" class="formula">on misclassified x2, x4!</text>
  </g>

  <!-- ARROW TO FINAL COMBINATION -->
  <line x1="590" y1="240" x2="635" y2="240" class="arr" />

  <!-- FINAL ENSEMBLE -->
  <g transform="translate(640, 85)">
    <rect width="270" height="320" class="round-box" style="stroke:#34d399;" />
    <text x="135" y="28" text-anchor="middle" class="lbl" fill="#34d399">FINAL STRONG CLASSIFIER</text>

    <rect x="25" y="60" width="220" height="40" class="weak-box" />
    <text x="135" y="85" text-anchor="middle" class="lbl">α1 · h1(x) [Weight: 0.20]</text>

    <text x="135" y="125" text-anchor="middle" class="lbl" fill="#38bdf8">+</text>

    <rect x="25" y="140" width="220" height="40" class="weak-box" />
    <text x="135" y="165" text-anchor="middle" class="lbl">α2 · h2(x) [Weight: α2]</text>

    <text x="135" y="205" text-anchor="middle" class="lbl" fill="#38bdf8">+</text>

    <rect x="25" y="220" width="220" height="40" class="weak-box" />
    <text x="135" y="245" text-anchor="middle" class="lbl">α3 · h3(x) [Weight: α3]</text>

    <!-- Final Output -->
    <path d="M 135 260 L 135 285" class="arr" />
    <text x="135" y="305" text-anchor="middle" class="formula">H(x) = sign( Σ α_t h_t(x) )</text>
  </g>

  <!-- BOTTOM CALLOUT -->
  <rect x="40" y="420" width="870" height="30" rx="4" style="fill:#111827; stroke:#334155;" />
  <text x="475" y="440" text-anchor="middle" class="formula">Exam Key: Misclassified weight multiplier = exp(α); Correctly classified multiplier = exp(-α). Normalize with Z_t.</text>
</svg>'''
    with open(os.path.join(OUT_DIR, "adaboost_sequential_architecture.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# 6. PCA Variance Maximization
# -------------------------------------------------------------
def gen_pca_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 490" width="950" height="490">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .box { fill: #1e293b; stroke: #334155; stroke-width: 2; rx: 8; }
      .axis { stroke: #64748b; stroke-width: 1.5; stroke-dasharray: 4,3; }
      .pc1-axis { stroke: #34d399; stroke-width: 3; }
      .pc2-axis { stroke: #f43f5e; stroke-width: 2.5; }
      .data-pt { fill: #38bdf8; stroke: #ffffff; stroke-width: 1.5; }
      .proj-line { stroke: #fbbf24; stroke-width: 1.2; stroke-dasharray: 3,2; }
      .title { fill: #38bdf8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; font-weight: bold; }
      .subtitle { fill: #94a3b8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; }
      .lbl { fill: #e2e8f0; font-family: 'Consolas', monospace; font-size: 13px; font-weight: bold; }
      .formula { fill: #34d399; font-family: 'Consolas', monospace; font-size: 12px; }
      .note { fill: #cbd5e1; font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; }
    </style>
  </defs>

  <rect width="100%" height="100%" class="bg" />
  <rect x="20" y="15" width="910" height="460" class="box" />
  <text x="475" y="38" text-anchor="middle" class="title">PRINCIPAL COMPONENT ANALYSIS (PCA): VARIANCE MAXIMIZATION</text>
  <text x="475" y="56" text-anchor="middle" class="subtitle">Eigen-Decomposition of Covariance Matrix Σ u_1 = λ_1 u_1 | Maximum Projected Variance</text>

  <!-- LEFT: 2D PROJECTION & EIGENVECTOR AXES -->
  <g transform="translate(60, 80)">
    <rect width="440" height="370" rx="6" style="fill:#111827; stroke:#475569; stroke-width:1.5;" />

    <!-- Original Axes X1, X2 centered at (220, 185) -->
    <line x1="30" y1="185" x2="410" y2="185" class="axis" />
    <text x="415" y="190" class="lbl" fill="#64748b">x1</text>
    <line x1="220" y1="30" x2="220" y2="340" class="axis" />
    <text x="215" y="25" class="lbl" fill="#64748b">x2</text>

    <!-- Data Distribution Ellipse (Angled) -->
    <ellipse cx="220" cy="185" rx="140" ry="50" transform="rotate(-35, 220, 185)" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="6,4" />

    <!-- Data points scattered along ellipse -->
    <circle cx="120" cy="250" r="5" class="data-pt" /><circle cx="150" cy="225" r="5" class="data-pt" />
    <circle cx="180" cy="220" r="5" class="data-pt" /><circle cx="210" cy="190" r="5" class="data-pt" />
    <circle cx="240" cy="170" r="5" class="data-pt" /><circle cx="260" cy="160" r="5" class="data-pt" />
    <circle cx="290" cy="130" r="5" class="data-pt" /><circle cx="320" cy="115" r="5" class="data-pt" />
    <circle cx="170" cy="170" r="5" class="data-pt" /><circle cx="250" cy="210" r="5" class="data-pt" />

    <!-- PC1 Axis (Major Axis): Maximum Variance -->
    <line x1="70" y1="290" x2="370" y2="80" class="pc1-axis" />
    <text x="365" y="70" class="lbl" fill="#34d399">PC 1 (u1, λ1 max)</text>
    <text x="260" y="90" class="formula">Max Variance Direction</text>

    <!-- PC2 Axis (Minor Axis): Orthogonal to PC1 -->
    <line x1="160" y1="100" x2="280" y2="270" class="pc2-axis" />
    <text x="285" y="280" class="lbl" fill="#f43f5e">PC 2 (u2, λ2)</text>

    <!-- Orthogonal angle indicator -->
    <path d="M 235 175 L 245 190 L 230 200" fill="none" stroke="#fbbf24" stroke-width="1.5" />
    <text x="245" y="200" class="note" fill="#fbbf24">90°</text>
  </g>

  <!-- RIGHT: MATHEMATICAL DERIVATION STEPS -->
  <g transform="translate(530, 80)">
    <rect width="380" height="370" rx="6" style="fill:#111827; stroke:#475569; stroke-width:1.5;" />
    <text x="190" y="28" text-anchor="middle" class="lbl" fill="#38bdf8">DERIVATION OF 1ST PRINCIPAL COMPONENT</text>

    <text x="20" y="60" class="lbl" fill="#fbbf24">Step 1: Center Data (Zero-Mean):</text>
    <text x="20" y="80" class="formula">X_c = X - μ_X</text>

    <text x="20" y="110" class="lbl" fill="#fbbf24">Step 2: Sample Covariance Matrix Σ:</text>
    <text x="20" y="130" class="formula">Σ = (1/m) X_c^T X_c  (Size: n × n)</text>

    <text x="20" y="160" class="lbl" fill="#fbbf24">Step 3: Projected Variance Objective:</text>
    <text x="20" y="180" class="formula">Var(z) = u_1^T Σ u_1   s.t.  u_1^T u_1 = 1</text>

    <text x="20" y="210" class="lbl" fill="#fbbf24">Step 4: Lagrange Multiplier Formulation:</text>
    <text x="20" y="230" class="formula">L(u_1, λ) = u_1^T Σ u_1 - λ(u_1^T u_1 - 1)</text>

    <text x="20" y="260" class="lbl" fill="#fbbf24">Step 5: Set Partial Derivative to Zero:</text>
    <text x="20" y="280" class="formula">∂L/∂u_1 = 2Σ u_1 - 2λ u_1 = 0</text>
    <text x="20" y="305" class="formula" font-size="14" fill="#38bdf8">⟹  Σ u_1 = λ u_1  (Eigenvalue Problem!)</text>

    <text x="20" y="340" class="note">Conclusion: Projected variance = λ_1. Maximized when</text>
    <text x="20" y="358" class="note">u_1 is the eigenvector for LARGEST eigenvalue λ_max.</text>
  </g>
</svg>'''
    with open(os.path.join(OUT_DIR, "pca_variance_maximization.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# 7. Decision Tree Entropy & Information Gain Split
# -------------------------------------------------------------
def gen_decision_tree_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 490" width="950" height="490">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .box { fill: #1e293b; stroke: #334155; stroke-width: 2; rx: 8; }
      .node-root { fill: #1e1b4b; stroke: #818cf8; stroke-width: 2.5; rx: 6; }
      .node-child { fill: #064e3b; stroke: #34d399; stroke-width: 2; rx: 6; }
      .title { fill: #38bdf8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; font-weight: bold; }
      .subtitle { fill: #94a3b8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; }
      .lbl { fill: #e2e8f0; font-family: 'Consolas', monospace; font-size: 12px; font-weight: bold; }
      .formula { fill: #34d399; font-family: 'Consolas', monospace; font-size: 12px; }
      .note { fill: #cbd5e1; font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; }
      .branch { stroke: #38bdf8; stroke-width: 2; fill: none; }
    </style>
  </defs>

  <rect width="100%" height="100%" class="bg" />
  <rect x="20" y="15" width="910" height="460" class="box" />
  <text x="475" y="38" text-anchor="middle" class="title">DECISION TREES: ENTROPY, GINI IMPURITY &amp; INFORMATION GAIN</text>
  <text x="475" y="56" text-anchor="middle" class="subtitle">ID3 (Entropy/Gain) vs CART (Gini Index) Attribute Selection Framework</text>

  <!-- LEFT: ENTROPY FUNCTION CURVE -->
  <g transform="translate(40, 80)">
    <rect width="360" height="370" rx="6" style="fill:#111827; stroke:#475569; stroke-width:1.5;" />
    <text x="180" y="28" text-anchor="middle" class="lbl" fill="#38bdf8">BINARY ENTROPY FUNCTION: H(p)</text>

    <!-- Axes -->
    <line x1="50" y1="280" x2="310" y2="280" stroke="#64748b" stroke-width="2" />
    <text x="315" y="285" class="lbl">p+</text>
    <line x1="50" y1="280" x2="50" y2="70" stroke="#64748b" stroke-width="2" />
    <text x="40" y="65" class="lbl">H(p)</text>

    <!-- Ticks -->
    <text x="45" y="295" class="note">0.0</text>
    <text x="170" y="295" class="note">0.5</text>
    <text x="300" y="295" class="note">1.0</text>
    <text x="25" y="105" class="note">1.0</text>

    <!-- Parabolic Entropy Curve: H(p) = -p log2 p - (1-p) log2 (1-p) -->
    <path d="M 50 280 Q 180 80 310 280" fill="none" stroke="#34d399" stroke-width="3" />

    <!-- Peak Indicator at p = 0.5 -->
    <line x1="180" y1="280" x2="180" y2="130" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="4,3" />
    <circle cx="180" cy="130" r="5" fill="#fbbf24" />
    <text x="190" y="125" class="lbl" fill="#fbbf24">Max Impurity H = 1.0 (50/50)</text>

    <!-- Pure Nodes at p = 0 and p = 1 -->
    <circle cx="50" cy="280" r="5" fill="#38bdf8" />
    <circle cx="310" cy="280" r="5" fill="#38bdf8" />
    <text x="30" y="260" class="note" fill="#38bdf8">Pure: H = 0</text>
    <text x="250" y="260" class="note" fill="#38bdf8">Pure: H = 0</text>

    <text x="30" y="335" class="formula">H(S) = - Σ p_i · log2(p_i)</text>
    <text x="30" y="355" class="formula">Gini(S) = 1 - Σ (p_i)²</text>
  </g>

  <!-- RIGHT: ATTRIBUTE SPLIT & INFORMATION GAIN -->
  <g transform="translate(430, 80)">
    <rect width="480" height="370" rx="6" style="fill:#111827; stroke:#475569; stroke-width:1.5;" />
    <text x="240" y="28" text-anchor="middle" class="lbl" fill="#fbbf24">ID3 INFORMATION GAIN ON ATTRIBUTE SPLIT</text>

    <!-- Root Node S -->
    <rect x="160" y="55" width="160" height="60" class="node-root" />
    <text x="240" y="78" text-anchor="middle" class="lbl">Parent Node S (14)</text>
    <text x="240" y="98" text-anchor="middle" class="formula">9 Yes, 5 No ⟹ H(S) = 0.940</text>

    <!-- Branches for Attribute "Wind" (Weak vs Strong) -->
    <path d="M 210 115 L 110 170" class="branch" />
    <text x="120" y="145" class="lbl" fill="#38bdf8">Weak (8)</text>

    <path d="M 270 115 L 370 170" class="branch" />
    <text x="330" y="145" class="lbl" fill="#38bdf8">Strong (6)</text>

    <!-- Child Node 1: Weak -->
    <rect x="30" y="170" width="160" height="55" class="node-child" />
    <text x="110" y="192" text-anchor="middle" class="lbl">S_Weak (6+, 2-)</text>
    <text x="110" y="212" text-anchor="middle" class="formula">H(S_Weak) = 0.811</text>

    <!-- Child Node 2: Strong -->
    <rect x="290" y="170" width="160" height="55" class="node-child" />
    <text x="370" y="192" text-anchor="middle" class="lbl">S_Strong (3+, 3-)</text>
    <text x="370" y="212" text-anchor="middle" class="formula">H(S_Strong) = 1.000</text>

    <!-- Information Gain Calculation Box -->
    <rect x="30" y="245" width="420" height="105" rx="6" style="fill:#1e293b; stroke:#334155;" />
    <text x="45" y="270" class="lbl" fill="#fbbf24">Information Gain Calculation:</text>
    <text x="45" y="292" class="formula">Gain(S, Wind) = H(S) - [ (8/14)·H(Weak) + (6/14)·H(Strong) ]</text>
    <text x="45" y="314" class="formula">Gain(S, Wind) = 0.940 - [ (8/14)·0.811 + (6/14)·1.000 ]</text>
    <text x="45" y="336" class="formula" fill="#34d399">Gain(S, Wind) = 0.940 - 0.892 = 0.048 bits</text>
  </g>
</svg>'''
    with open(os.path.join(OUT_DIR, "decision_tree_entropy_split.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# 8. Naive Bayes & Bayesian Belief Network (BBN)
# -------------------------------------------------------------
def gen_bayes_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 490" width="950" height="490">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .box { fill: #1e293b; stroke: #334155; stroke-width: 2; rx: 8; }
      .class-node { fill: #1e1b4b; stroke: #818cf8; stroke-width: 2.5; }
      .feat-node { fill: #064e3b; stroke: #34d399; stroke-width: 2; }
      .bbn-node { fill: #451a03; stroke: #f59e0b; stroke-width: 2; }
      .title { fill: #38bdf8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; font-weight: bold; }
      .subtitle { fill: #94a3b8; font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; }
      .lbl { fill: #e2e8f0; font-family: 'Consolas', monospace; font-size: 12px; font-weight: bold; }
      .formula { fill: #34d399; font-family: 'Consolas', monospace; font-size: 12px; }
      .note { fill: #cbd5e1; font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; }
      .wire { stroke: #38bdf8; stroke-width: 2; fill: none; marker-end: url(#parr); }
    </style>
    <marker id="parr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L0,6 L6,3 z" fill="#38bdf8" />
    </marker>
  </defs>

  <rect width="100%" height="100%" class="bg" />
  <rect x="20" y="15" width="910" height="460" class="box" />
  <text x="475" y="38" text-anchor="middle" class="title">PROBABILISTIC LEARNING: NAÏVE BAYES vs BAYESIAN BELIEF NETWORKS (BBN)</text>
  <text x="475" y="56" text-anchor="middle" class="subtitle">Conditional Independence Assumption | Joint Probability via Chain Rule: P(X_1...X_n) = Π P(X_i | Parents(X_i))</text>

  <!-- LEFT: NAIVE BAYES GRAPHICAL MODEL -->
  <g transform="translate(40, 80)">
    <rect width="400" height="370" rx="6" style="fill:#111827; stroke:#475569; stroke-width:1.5;" />
    <text x="200" y="28" text-anchor="middle" class="lbl" fill="#38bdf8">1. NAÏVE BAYES CLASSIFIER</text>

    <!-- Target Class Node Y (Center Top) -->
    <circle cx="200" cy="80" r="30" class="class-node" />
    <text x="200" y="85" text-anchor="middle" class="lbl" fill="#c7d2fe">Class Y</text>

    <!-- Directed arrows from Y to all features X_i -->
    <path d="M 180 105 L 80 190" class="wire" />
    <path d="M 190 110 L 160 190" class="wire" />
    <path d="M 210 110 L 240 190" class="wire" />
    <path d="M 220 105 L 320 190" class="wire" />

    <!-- Feature Nodes (Conditionally Independent given Y) -->
    <circle cx="70" cy="210" r="24" class="feat-node" /><text x="70" y="214" text-anchor="middle" class="lbl">X1</text>
    <circle cx="155" cy="210" r="24" class="feat-node" /><text x="155" y="214" text-anchor="middle" class="lbl">X2</text>
    <circle cx="245" cy="210" r="24" class="feat-node" /><text x="245" y="214" text-anchor="middle" class="lbl">X3</text>
    <circle cx="330" cy="210" r="24" class="feat-node" /><text x="330" y="214" text-anchor="middle" class="lbl">Xn</text>

    <!-- Formulas -->
    <rect x="20" y="255" width="360" height="95" rx="6" style="fill:#1e293b; stroke:#334155;" />
    <text x="30" y="278" class="lbl" fill="#fbbf24">Independence Assumption:</text>
    <text x="30" y="300" class="formula">P(X1, ..., Xn | Y) = Π P(Xi | Y)</text>
    <text x="30" y="322" class="formula">C_MAP = argmax P(Y) · Π P(Xi | Y)</text>
    <text x="30" y="340" class="note">Laplace smoothing prevents zero probabilities.</text>
  </g>

  <!-- RIGHT: BAYESIAN BELIEF NETWORK (DAG) -->
  <g transform="translate(480, 80)">
    <rect width="430" height="370" rx="6" style="fill:#111827; stroke:#475569; stroke-width:1.5;" />
    <text x="215" y="28" text-anchor="middle" class="lbl" fill="#f59e0b">2. BAYESIAN BELIEF NETWORK (BBN)</text>

    <!-- Classic Burglary/Earthquake DAG -->
    <circle cx="110" cy="80" r="26" class="bbn-node" /><text x="110" y="84" text-anchor="middle" class="lbl">Burglar</text>
    <circle cx="310" cy="80" r="26" class="bbn-node" /><text x="310" y="84" text-anchor="middle" class="lbl">Quake</text>

    <!-- Connections to Alarm -->
    <path d="M 125 102 L 190 155" class="wire" />
    <path d="M 295 102 L 230 155" class="wire" />

    <circle cx="210" cy="170" r="26" class="bbn-node" /><text x="210" y="174" text-anchor="middle" class="lbl">Alarm</text>

    <!-- Connections to Calls -->
    <path d="M 195 192 L 130 240" class="wire" />
    <path d="M 225 192 L 290 240" class="wire" />

    <circle cx="115" cy="255" r="24" class="bbn-node" /><text x="115" y="259" text-anchor="middle" class="lbl">JohnCalls</text>
    <circle cx="305" cy="255" r="24" class="bbn-node" /><text x="305" y="259" text-anchor="middle" class="lbl">MaryCalls</text>

    <!-- Formulas -->
    <rect x="20" y="295" width="390" height="60" rx="6" style="fill:#1e293b; stroke:#334155;" />
    <text x="30" y="318" class="lbl" fill="#fbbf24">BBN Chain Rule Representation:</text>
    <text x="30" y="338" class="formula">P(B, E, A, J, M) = P(B)P(E)P(A|B,E)P(J|A)P(M|A)</text>
  </g>
</svg>'''
    with open(os.path.join(OUT_DIR, "bayes_naive_and_bbn.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    gen_svm_svg()
    gen_confusion_matrix_svg()
    gen_smote_svg()
    gen_kmeans_svg()
    gen_adaboost_svg()
    gen_pca_svg()
    gen_decision_tree_svg()
    gen_bayes_svg()

    # Validate XML on all generated files
    files = [
        "svm_hyperplane_margin.svg", "confusion_matrix_and_metrics.svg",
        "smote_synthetic_interpolation.svg", "kmeans_clustering_iterations.svg",
        "adaboost_sequential_architecture.svg", "pca_variance_maximization.svg",
        "decision_tree_entropy_split.svg", "bayes_naive_and_bbn.svg"
    ]
    for f in files:
        p = os.path.join(OUT_DIR, f)
        ET.parse(p)
        print(f"[PASS 100% VALID XML] {f}")
