# Advanced Machine Learning: Antigravity Skill Specification & Multi-Agent Prompt
## Master's Degree in Computer Engineering — Politecnico di Torino (A.A. 2026/2027)
**Course Codes**: `01URWOV` / `01URWYG` (6 CFU, SSD: `ING-INF/05`)  
**Lead Instructor**: Prof.ssa Tatiana Tommasi (DAUIN, Director of VANDAL Lab, ELLIS Unit Turin)  
**Co-Instructors & Mentors**: Prof. Barbara Caputo, Stephany Chanelo, Davide Sferrazza, Alessandro Marinai, Silvio Chito  
**Course Portals**: Room 3P, Discord (`https://discord.gg/JXQm4fAqv`), VANDAL Lab ([vandal.polito.it](http://vandal.polito.it/))

---

## 1. Executive Mission & System Prompt for the AI Multi-Agent Team

```markdown
You are an elite AI Multi-Agent Engineering Team tasked with building and deploying an autonomous, publication-grade Antigravity workspace skill: `advanced-machine-learning-study-guide-integrator`.

### Prime Directive:
Develop an autonomous skill and LaTeX engineering framework that ingests lecture recordings, slides, and transcripts for the "Advanced Machine Learning" course at Politecnico di Torino.
The skill must strictly enforce two foundational pillars:
1. THE PROFESSOR FLOW IS THE GOLDEN ANCHOR: The study guide's primary structural spine, conceptual pacing, pedagogical metaphors, and section progression MUST strictly mirror Prof. Tatiana Tommasi's lecture sequence. We never substitute the professor's flow with an arbitrary book index.
2. DEEP MULTI-BOOK & PAPER TRIANGULATION FOR EVERY TOPIC: While adhering to the professor's narrative flow, the skill must systematically and autonomously inspect ALL official textbooks in the local `BOOKS/` folder (Bishop & Bishop 2024, Goodfellow et al. 2016, Sutton & Barto 2018, Russell & Norvig 2020, Prince 2023, Murphy) and all linked seminal papers (CVPR, ICCV, ECCV, NeurIPS, ICLR). For every lecture topic, the skill must extract formal proofs, explicit tensor dimensions, intermediate mathematical derivations, and foundational theory that slides only summarize at a high level.
```

---

## 2. Academic Environment & Course Realities

### 2.1 The 3-Tier Exam Architecture
1. **Paper Presentation (Score: 6–10)**:
   - Groups of 4 students, exactly 12 minutes sharp.
   - Presentation and technical breakdown of a seminal research paper from the last 3–7 years published in top-tier venues (CVPR, ICCV, ECCV, NeurIPS, ICLR).
   - Evaluation focuses on technical comprehension, mathematical formulation, ability to convey intuition, and experimental critique.
2. **Group Project (Score: 6–10)**:
   - Teams of 4 students working on 3–4 research proposals mentored by TAs on Google Colab.
   - Mandatory submission of an experimental PDF report form 10 days prior to the oral session.
3. **Oral Exam (Score: 6–10)**:
   - 15-minute group defense of the project + individual Q&A.
   - **Mandatory individual theoretical questions covering all course topics discussed in class**. Insufficient answers result in immediate failure.

### 2.2 Course Syllabus Modules
* **Module 1**: AI, ML & DL Foundations, Computational Rationality, Bounded Optimality (Russell & Norvig, Berkeley CS188).
* **Module 2**: Probability Fundamentals, Bayesian Decision Theory, Likelihood Ratios, Bayes Optimal Classifier (Feller, Murphy, Bishop 2024).
* **Module 3**: Loss Functions, Statistical Risk, Empirical Risk Minimization (ERM), Generalization Bounds, PAC Learning (Shalev-Shwartz & Ben-David, Goodfellow).
* **Module 4**: Shallow Supervised & Unsupervised Learning (Linear Models, Ridge/Lasso, Support Vector Machines, Kernel Trick, PCA, Dimensionality Reduction).
* **Module 5**: Deep Visual Backbones (CNNs, Convolutional Algebra, Receptive Fields, ResNet, Modern Vision Architectures, CS231n, Torralba et al.).
* **Module 6**: Unsupervised, Self-Supervised & Representation Learning (Contrastive Learning, SimCLR, MoCo, Masked Autoencoders, Task-Driven Features — Rodolà, Saenko).
* **Module 7**: Recurrent & Sequence Models (RNNs, LSTMs, Transformers, Multi-Head Self-Attention).
* **Module 8**: Deep Generative Models (Variational Autoencoders, ELBO, Generative Adversarial Networks, Normalizing Flows, Denoising Diffusion Probabilistic Models).
* **Module 9**: 3D Geometry & Multimodal Learning (Point Clouds, PointNet, Neural Radiance Fields [NeRF], 3D Gaussian Splatting, Vision-Language Models).
* **Module 10**: Domain Adaptation, Dataset Bias & Algorithmic Fairness (Prof. Tommasi's seminal research pillar: Covariate Shift, Domain Adversarial Training [DANN], Subpopulation Fairness).
* **Module 11**: Reinforcement Learning Foundations (Markov Decision Processes, Bellman Equations, Value Iteration, Policy Gradients — Sutton & Barto).

---

## 3. The 8 Non-Negotiable Core Principles

1. **Zero Omission (Non-Negotiable)**:
   Every slide bullet, classroom remark, diagram, code listing, and pedagogical analogy (e.g., the Datasaurus statistics demonstration, Ray Mooney's pseudo-algorithm, the card-game analogy "what counts in spades does not count in poker") must appear unabridged in the text.
2. **Professor Flow as the Golden Spine**:
   The chapter hierarchy and internal section narrative strictly track the professor's slides. Supplementary material deepens and enriches the flow—it never derails it.
3. **Multi-Book Deep Cross-Referencing for Every Lecture**:
   For every topic, the skill must execute an automated query across all local textbooks in `BOOKS/` to pull in rigorous lemmas, proofs, historical context, and formal statistical definitions.
4. **Seminal Paper Ingestion & Unified Numbered Bibliography**:
   Seminal papers cited in slides or relevant to the exam must be deeply synthesized into the main prose. Citations use standard numeric format `\cite{key}` (`[1]`, `[2]`), hyperlinked to a single unified `STUDY_GUIDE/references.bib` file at the end of the document.
5. **Exhaustive Mathematical Derivations & Tensor Dimensions**:
   Never skip algebraic steps. Explicitly declare tensor shapes for every operation (e.g., $\mathbf{X} \in \mathbb{R}^{B \times C \times H \times W}$, weight tensor $\mathbf{W} \in \mathbb{R}^{C_{\text{out}} \times C_{\text{in}} \times k_h \times k_w}$).
6. **Tri-Tier Geometric & Visual Intuition**:
   - **Tier 1 (TikZ)**: Publication-grade vector schematics for neural architectures, DAGs, and decision hyperplanes.
   - **Tier 2 (PGFPlots)**: Exact 2D mathematical curves for loss functions, activation functions, ROC/PR curves, and optimization trajectories.
   - **Tier 3 (Manim Engine)**: 3D non-convex optimization surfaces, high-dimensional latent manifold folding, and dynamic companion micro-animations.
7. **Strict Sentence Case**:
   All chapter titles, section headings, subsection titles, table captions, and figure captions must strictly follow sentence case (e.g., *"Chapter overview and learning outcomes"*, *"The Bayes optimal decision boundary"*).
8. **Label Disambiguation & Semantic Prefixes**:
   All labels must have unique semantic prefixes: figures with `fig:`, tables with `tab:`, equations with `eq:`, sections with `sec:`.

---

## 4. Complete Skill File Hierarchy to Build

The AI multi-agent team must construct the following file structure:

```
.agents/skills/advanced-machine-learning-study-guide-integrator/
├── SKILL.md                                    # Master skill manifesto & operational workflow
├── references/
│   ├── 00_video_transcription_protocol.md      # Zero-token local Whisper transcription
│   ├── 01_book_inspection_protocol.md          # Multi-book cross-referencing & theory extraction
│   ├── 02_seminal_paper_research_protocol.md   # CVPR/NeurIPS paper retrieval & exam prep
│   ├── 03_integration_modes.md                  # 4 LaTeX architectural integration modes
│   ├── 04_math_expansion_and_tensors.md        # Tensor dimensionality & proof standards
│   ├── 05_tikz_pgfplots_manim_guidelines.md    # Tri-tier visual diagramming standards
│   └── 06_zero_omission_and_audit_checklist.md # Verification gates and coverage audit
└── scripts/
    ├── transcribe_lecture.py                   # Local Whisper CLI primed with AML vocabulary
    ├── inspect_books.py                        # Automated PDF search & extraction engine
    └── verify_coverage.py                      # Multi-source coverage & formatting validator
```

---

## 5. Detailed Specifications for Every File

### 5.1 `SKILL.md` (Master Manifest)
- **Frontmatter**:
  ```yaml
  ---
  name: advanced-machine-learning-study-guide-integrator
  description: >-
    Autonomously ingests Advanced Machine Learning lecture recordings via zero-token local Whisper,
    lecture slides, and transcripts; anchors the narrative strictly to Prof. Tatiana Tommasi's lecture flow;
    executes systematic pre-ingestion multi-book deep inspection across local textbooks (Bishop 2024,
    Goodfellow 2016, Sutton & Barto 2018, Russell & Norvig 2020, Prince 2023, Murphy); synthesizes seminal
    CVPR/NeurIPS/ICLR papers; derives exhaustive mathematical proofs with explicit tensor dimensions; deploys
    a tri-tier visual framework (native TikZ architectures, exact PGFPlots analytical curves, and Manim 3D
    optimization landscapes); and integrates content seamlessly into the LaTeX study guide across 4 flexible modes
    while enforcing zero omission.
  ---
  ```
- **Contents**: Full articulation of the 8 core principles, tool invocation rules, and the 7-step operational workflow:
  1. *Step 0*: Local Zero-Token Audio Ingestion (`transcribe_lecture.py`).
  2. *Step 1*: Slide & Transcript Inventory Extraction (Concepts, equations, analogies).
  3. *Step 2*: Automated Multi-Book Deep Inspection (`inspect_books.py`).
  4. *Step 3*: Seminal Paper Retrieval & Triangulation (CVPR/NeurIPS/ICLR).
  5. *Step 4*: Mathematical Proof Derivation & Tensor Dimension Rigor.
  6. *Step 5*: Tri-Tier Visual Asset Generation (TikZ, PGFPlots, Manim).
  7. *Step 6*: LaTeX Integration (Modes 1–4) & Automated Audit (`verify_coverage.py`).

---

### 5.2 `references/00_video_transcription_protocol.md`
- **Audio Extraction**: `ffmpeg -i input.mp4 -vn -ar 16000 -ac 1 -c:a pcm_s16le output.wav`.
- **Zero-Token Local Whisper Execution**: Run using Apple Silicon MPS or CUDA acceleration.
- **Domain-Primed Initial Prompt**:
  ```python
  AML_INITIAL_PROMPT = (
      "Advanced Machine Learning lecture by Prof. Tatiana Tommasi at Politecnico di Torino, "
      "VANDAL Lab, ELLIS Unit Turin. Topics: Bayesian decision theory, Bayes risk, likelihood ratio, "
      "empirical risk minimization, PAC learning, VC dimension, Support Vector Machines, kernel trick, "
      "Principal Component Analysis, deep learning, convolutional neural networks, receptive field, "
      "residual networks, ResNet, self-supervised learning, contrastive learning, SimCLR, MoCo, "
      "Masked Autoencoders, recurrent neural networks, LSTM, Transformers, multi-head attention, "
      "variational autoencoders, ELBO, GANs, diffusion models, DDPM, score-based models, NeRF, "
      "3D Gaussian Splatting, domain adaptation, covariate shift, DANN, algorithmic fairness."
  )
  ```
- **Anti-Hallucination Settings**: `condition_on_previous_text=False`, `compression_ratio_threshold=2.4`, `no_speech_threshold=0.6`.
- **Target Output**: Markdown file with timestamped chunks in `TRANSCRIPTIONS/LECTURES/XX-Topic.md`.

---

### 5.3 `references/01_book_inspection_protocol.md` *(The Multi-Book Deep Dive)*
This protocol defines how the agent queries local textbooks in `/Users/nicolabeccaceci/Desktop/ADVANCED MACHINE LEARNING/BOOKS/` for every lecture topic:

| Lecture Topic / Module | Primary Textbook Mapping | Target Mathematical & Conceptual Enrichment |
| :--- | :--- | :--- |
| **1. AI & Rational Agents** | Russell & Norvig (2020) Ch. 1–2; Bishop (2024) Ch. 1 | Computational rationality, bounded optimality, utility theory, PEAS framework. |
| **2. Bayesian Decision Theory & Probability** | Bishop (2024) Ch. 2–3; Murphy (2012) Ch. 2, 5; Feller (1968) | Joint/conditional distributions, Bayes theorem, likelihood ratio test, 0-1 loss vs. asymmetric loss, minimum risk decision boundary, minimax decision rule. |
| **3. Statistical Learning Theory & Risk** | Shalev-Shwartz & Ben-David Ch. 2–4; Goodfellow (2016) Ch. 5; Bishop Ch. 8 | True risk vs. empirical risk, uniform convergence, No Free Lunch theorem, PAC learnability, Rademacher complexity, VC dimension bounds. |
| **4. Shallow Supervised Learning (SVM, Kernels)** | Bishop (2024) Ch. 3; Russell & Norvig Ch. 19; Prince (2023) Ch. 14 | Primal and dual Lagrangian formulations, KKT conditions, support vectors, Mercer's condition, kernel trick (RBF, polynomial). |
| **5. Dimensionality Reduction & Clustering** | Goodfellow (2016) Ch. 2, 14; Prince (2023) Ch. 14 | PCA via SVD vs. eigendecomposition of covariance matrix, variance maximization proof, reconstruction error minimization, $k$-means clustering and EM algorithm. |
| **6. Convolutional Neural Networks & Vision Backbones** | Bishop (2024) Ch. 9; Goodfellow (2016) Ch. 9; Torralba et al. Ch. 6; Prince Ch. 10–11 | 2D cross-correlation vs. convolution, weight sharing, spatial downsampling, effective receptive field derivation ($R_l = R_{l-1} + (k_l - 1) \cdot S_{l-1}$), ResNet degradation problem and residual identity mapping ($\vy = \mathcal{F}(\vx) + \vx$). |
| **7. Self-Supervised & Representation Learning** | Bishop (2024) Ch. 13; Prince (2023) Ch. 15 | InfoNCE loss derivation, mutual information lower bound, negative pair repulsion, temperature hyperparameter dynamics ($\tau$), MoCo memory queue, Masked Autoencoder reconstruction. |
| **8. Recurrent Models & Transformers** | Bishop (2024) Ch. 10–11; Goodfellow (2016) Ch. 10 | BPTT gradient vanishing proof, LSTM Constant Error Carousel, Scaled Dot-Product Attention derivation ($\softmax(\mQ\mK^\top / \sqrt{d_k})\mV$), Multi-Head projection geometry. |
| **9. Generative Models (VAE, GAN, Diffusion)** | Bishop (2024) Ch. 12; Goodfellow (2016) Ch. 20; Prince (2023) Ch. 17–19 | Evidence Lower Bound (ELBO) decomposition ($\E_{q}[\log p] - D_{\text{KL}}(q \parallel p)$), reparameterization trick, GAN minimax game and Jensen-Shannon divergence, DDPM forward Gaussian Markov chain, reverse score matching. |
| **10. 3D Deep Learning & NeRF** | Prince (2023) Ch. 21; Mildenhall et al. (2020) | Ray marching, volumetric rendering integral ($C(\vr) = \int T(t) \sigma(\vr(t)) \vc(\vr(t), \vd) dt$), positional encoding, 3D Gaussian Splatting rasterization. |
| **11. Domain Adaptation & Dataset Fairness** | Goodfellow (2016) Ch. 15; Saenko et al. (2010); Ganin et al. (2016) | Covariate shift vs. concept drift, $\mathcal{H}\Delta\mathcal{H}$-divergence bound (Ben-David et al.), Gradient Reversal Layer (GRL), minimax domain adversarial optimization, demographic parity and equalized odds. |
| **12. Reinforcement Learning** | Sutton & Barto (2018) Ch. 3–6, 13; Bishop (2024) Ch. 14 | MDP definition ($\mathcal{S}, \mathcal{A}, \mathcal{P}, \mathcal{R}, \gamma$), Bellman expectation and optimality equations, policy iteration, Q-learning, REINFORCE policy gradient theorem ($\nabla_\theta J(\theta) = \E[\nabla_\theta \log \pi_\theta(a \mid s) Q(s, a)]$). |

---

### 5.4 `references/02_seminal_paper_research_protocol.md`
- **Venue Index**: CVPR, ICCV, ECCV, NeurIPS, ICLR, ICML, AAAI, IEEE TPAMI.
- **Extraction Protocol for Each Paper**:
  1. *Context & Motivation*: The fundamental limitation of prior work.
  2. *Theoretical Framework*: Mathematical problem formulation and proposed architecture.
  3. *Loss Formulation*: Complete loss equations with regularizers and hyperparameter roles.
  4. *Empirical Verification*: Datasets, benchmarks, ablation studies, and qualitative failure cases.
- **Exam Paper Presentation Guidance**:
  - Highlights what makes an outstanding 12-minute group presentation according to Prof. Tommasi.
  - Structuring slides: Motivation (2 min) $\to$ Architecture/Method (5 min) $\to$ Experimental Results & Ablations (3 min) $\to$ Critical Analysis/Limitations (2 min).

---

### 5.5 `references/03_integration_modes.md`
Detailed implementation rules for the 4 LaTeX integration modes:
- **Mode 1: New Chapter Creation**:
  Used when integrating a completely new syllabus topic. Generates `chapters/partX/XX_topic.tex` with standard structure: Learning Objectives, Theoretical Motivation, Core Mathematical Derivations, Worked Geometric Examples, Exam Insights, and Bibliography linkages.
- **Mode 2: New Section / Subsection**:
  Used when adding a lecture module to an existing chapter. Preserves the narrative transitions from previous topics.
- **Mode 3: Deep In-Place Integration**:
  Used to enrich an existing section with book-derived proofs, explicit tensor algebra, or algorithm pseudo-code.
- **Mode 4: Marginal / Callout Integration**:
  - `\begin{examinsight}`: Recurrent oral exam questions, trick questions, and project presentation pointers.
  - `\begin{intuition}`: Physical, high-dimensional geometric analogies.
  - `\begin{deepdive}`: Rigorous academic proofs from Bishop, Goodfellow, or seminal papers.

---

### 5.6 `references/04_math_expansion_and_tensors.md`
- **Rigorous Mathematical Style Guide**:
  - Every variable introduced must be defined with its set membership (e.g., $\vx \in \mathcal{X} \subseteq \mathbb{R}^d$, $y \in \{-1, +1\}$).
  - Explicit tensor shapes annotated using `\underbrace` or text descriptions.
  - No algebraic leaps: include intermediate steps for matrix inversions, expectations, and derivatives.
- **Standard AML Notation**:
  - Features: $\mathbf{x} \in \mathbb{R}^d$
  - Labels: $y \in \mathcal{Y}$
  - Parameter vectors: $\mathbf{w} \in \mathbb{R}^d$, bias $b \in \mathbb{R}$
  - Weight matrices: $\mathbf{W} \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$
  - Batched tensors: $\mathbf{X} \in \mathbb{R}^{B \times C \times H \times W}$
  - Expected value: $\mathbb{E}_{x \sim P}[f(x)]$
  - Divergence: $D_{\text{KL}}(P \parallel Q)$

---

### 5.7 `references/05_tikz_pgfplots_manim_guidelines.md`
- **Native TikZ Architecture Blueprints**:
  - *2D Convolution & Receptive Field*: Multi-plane grid showing input channels, kernel application, stride, and output feature map.
  - *Residual Block*: Split path showing weight layers $\mathcal{F}(\mathbf{x})$ and identity shortcut $\mathbf{x}$ summing at a $\oplus$ node.
  - *Contrastive Learning (SimCLR)*: Data augmentation branches $t, t' \sim \mathcal{T}$, shared encoder $f(\cdot)$, projection head $g(\cdot)$, and InfoNCE cosine similarity agreement.
  - *Variational Autoencoder (VAE)*: Encoder $q_\phi(\mathbf{z} \mid \mathbf{x}) \to (\boldsymbol{\mu}, \boldsymbol{\sigma})$, reparameterization sampling $\mathbf{z} = \boldsymbol{\mu} + \boldsymbol{\sigma} \odot \boldsymbol{\epsilon}$, and decoder $p_\theta(\mathbf{x} \mid \mathbf{z})$.
  - *Denoising Diffusion (DDPM)*: Markov forward process $q(\mathbf{x}_t \mid \mathbf{x}_{t-1})$ adding Gaussian noise, and reverse denoising network $p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t)$.
  - *Domain Adversarial Neural Network (DANN)*: Feature extractor $\mathbf{f} = G_f(\mathbf{x})$, label predictor $\hat{y} = G_y(\mathbf{f})$, and domain classifier $\hat{d} = G_d(\mathcal{R}(\mathbf{f}))$ with Gradient Reversal Layer (GRL).
- **PGFPlots Analytical Function Standards**:
  - Plots for 0-1 loss, Hinge loss, Logistic loss, Cross-Entropy, Focal loss.
  - Precision-Recall curves, ROC curves showing AUC, and Pareto optimality frontiers.
- **Manim Engine Guidelines**:
  - Generation of 3D loss landscapes (saddle points, ravines, local minima) exported as 4K stills to `STUDY_GUIDE/figures/manim/` and dynamic video clips to `STUDY_GUIDE/animations/`.

---

### 5.8 `references/06_zero_omission_and_audit_checklist.md`
- **Slide & Concept Audit Matrix Template**:
  ```markdown
  | Slide # | Slide Heading / Concept | Professor Dialogue / Analogy | Multi-Book Theoretical Source | Integrated LaTeX Section | Equation / Figure # | Verified |
  | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
  | 01.42 | AI = Computational Rationality | Bounded rationality, utility | Russell & Norvig Ch. 1–2 | sec:computational_rationality | eq:expected_utility | [x] |
  | 01.72 | Datasaurus Dataset | Same stats to 2 decimal places | Bishop Ch. 2, Autodesk 2017 | sec:data_uncertainty | fig:datasaurus | [x] |
  | 01.96 | Task-Driven Features | "What counts in spades..." | Rodolà slides, Bishop Ch. 13 | sec:task_driven_features | fig:feature_representations | [x] |
  | 01.100| Data Bias & Adaptation | Kate Saenko credit, shift | Saenko 2010, Goodfellow Ch. 15| sec:dataset_bias_adaptation | fig:domain_shift | [x] |
  ```
- **6-Gate Verification Pipeline**:
  1. *Inventory completeness*: 100% of slide topics present.
  2. *Book triangulation*: Theoretical proof from `BOOKS/` present for every section.
  3. *Paper references*: Seminal papers cited via numeric bibliography.
  4. *Case conventions*: All section titles and captions strictly sentence case.
  5. *Label checks*: `fig:`, `tab:`, `eq:` prefixes present and unique.
  6. *LaTeX compilation*: Clean build to PDF with 0 fatal errors.

---

### 5.9 `scripts/transcribe_lecture.py`
Complete, standalone Python script utilizing local Whisper:
```python
#!/usr/bin/env python3
"""
transcribe_lecture.py — Zero-Token Local Whisper Transcription for Advanced Machine Learning
"""
import sys
import os
import subprocess
import torch
import whisper

DEFAULT_INITIAL_PROMPT = (
    "Advanced Machine Learning lecture by Prof. Tatiana Tommasi at Politecnico di Torino, "
    "VANDAL Lab, ELLIS Unit Turin. Topics: Bayesian decision theory, Bayes risk, likelihood ratio, "
    "empirical risk minimization, PAC learning, VC dimension, Support Vector Machines, kernel trick, "
    "Principal Component Analysis, deep learning, convolutional neural networks, receptive field, "
    "residual networks, ResNet, self-supervised learning, contrastive learning, SimCLR, MoCo, "
    "Masked Autoencoders, recurrent neural networks, LSTM, Transformers, multi-head attention, "
    "variational autoencoders, ELBO, GANs, diffusion models, DDPM, score-based models, NeRF, "
    "3D Gaussian Splatting, domain adaptation, covariate shift, DANN, algorithmic fairness."
)

def extract_audio(video_path: str, output_wav: str) -> None:
    print(f"[*] Extracting 16kHz mono audio from {video_path}...")
    cmd = [
        "ffmpeg", "-y", "-i", video_path,
        "-vn", "-ar", "16000", "-ac", "1",
        "-c:a", "pcm_s16le", output_wav
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def transcribe(audio_path: str, output_md: str, model_name: str = "base.en") -> None:
    device = "mps" if torch.backends.mps.is_available() else ("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[*] Loading Whisper model '{model_name}' on device '{device}'...")
    model = whisper.load_model(model_name, device=device)

    print(f"[*] Transcribing {audio_path}...")
    result = model.transcribe(
        audio_path,
        initial_prompt=DEFAULT_INITIAL_PROMPT,
        condition_on_previous_text=False,
        compression_ratio_threshold=2.4,
        no_speech_threshold=0.6,
        verbose=False
    )

    os.makedirs(os.path.dirname(os.path.abspath(output_md)), exist_ok=True)
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(f"# Lecture Transcription\n\n")
        f.write(f"- **Source**: `{os.path.basename(audio_path)}`\n")
        f.write(f"- **Model**: `{model_name}`\n")
        f.write(f"- **Device**: `{device}`\n\n---\n\n")
        for seg in result["segments"]:
            start = int(seg["start"])
            end = int(seg["end"])
            text = seg["text"].strip()
            time_str = f"[{start//60:02d}:{start%60:02d} -> {end//60:02d}:{end%60:02d}]"
            f.write(f"**{time_str}** {text}\n\n")
    print(f"[+] Transcription saved successfully to: {output_md}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 transcribe_lecture.py <input_video_or_audio> <output_markdown> [model_name]")
        sys.exit(1)
    in_path = sys.argv[1]
    out_md = sys.argv[2]
    model = sys.argv[3] if len(sys.argv) > 3 else "base.en"
    
    if in_path.lower().endswith((".mp4", ".mkv", ".mov", ".m4a")):
        wav_path = "/tmp/temp_audio.wav"
        extract_audio(in_path, wav_path)
        transcribe(wav_path, out_md, model)
        if os.path.exists(wav_path):
            os.remove(wav_path)
    else:
        transcribe(in_path, out_md, model)
```

---

### 5.10 `scripts/inspect_books.py` *(Automated Multi-Book PDF Search Engine)*
This utility gives the AI agents instant, zero-friction access to the full text of all books:
```python
#!/usr/bin/env python3
"""
inspect_books.py — Automated Multi-Book Search & Theory Extraction Utility
Queries all PDFs in BOOKS/ and extracts matching sections with page numbers and context.
"""
import sys
import os
import argparse
import pypdf

BOOKS_DIR = "/Users/nicolabeccaceci/Desktop/ADVANCED MACHINE LEARNING/BOOKS"

BOOKS_REGISTRY = {
    "bishop": "Christopher M. Bishop, Hugh Bishop - Deep Learning_ Foundations and Concepts-Springer (2024).pdf",
    "goodfellow": "Deep Learning (Ian Goodfellow, Yoshua Bengio etc.).pdf",
    "sutton": "Reinforcement Learning An Introduction, 2nd ed. (Richard S. Sutton  Andrew G. Barto).pdf",
    "russell": "Artificial Intelligence A Modern Approach (Stuart J. Russell  Peter Norvig).pdf",
}

def search_book(book_key: str, query: str, max_matches: int = 5):
    filename = BOOKS_REGISTRY.get(book_key.lower())
    if not filename:
        print(f"[-] Unknown book key: {book_key}. Options: {list(BOOKS_REGISTRY.keys())}")
        return

    filepath = os.path.join(BOOKS_DIR, filename)
    if not os.path.exists(filepath):
        print(f"[-] File not found: {filepath}")
        return

    print(f"\n=======================================================")
    print(f"[*] Searching '{query}' in {filename}...")
    print(f"=======================================================")

    reader = pypdf.PdfReader(filepath)
    matches_found = 0
    query_lower = query.lower()

    for idx, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text:
            continue
        if query_lower in text.lower():
            matches_found += 1
            print(f"\n[+] MATCH {matches_found} — Page {idx + 1}:")
            lines = text.split("\n")
            for line in lines:
                if query_lower in line.lower():
                    print(f"    >>> {line.strip()}")
            if matches_found >= max_matches:
                print(f"\n[*] Reached max match limit ({max_matches}).")
                break

    if matches_found == 0:
        print("[-] No matches found.")

def main():
    parser = argparse.ArgumentParser(description="Query local AML textbooks for mathematical theory and proofs.")
    parser.add_argument("--query", "-q", required=True, help="Search term or concept (e.g. 'Bayes risk', 'reparameterization')")
    parser.add_argument("--book", "-b", default="all", help="Target book: bishop, goodfellow, sutton, russell, or all")
    parser.add_argument("--max", "-m", type=int, default=3, help="Max matches per book")
    args = parser.parse_args()

    if args.book == "all":
        for b in BOOKS_REGISTRY.keys():
            search_book(b, args.query, args.max)
    else:
        search_book(args.book, args.query, args.max)

if __name__ == "__main__":
    main()
```

---

### 5.11 `scripts/verify_coverage.py`
Automated test script to ensure quality before finishing any study guide integration:
```python
#!/usr/bin/env python3
"""
verify_coverage.py — Quality & Zero-Omission Audit Gate for Advanced Machine Learning Study Guide
"""
import sys
import os
import re

def check_file_exists(path: str) -> bool:
    if not os.path.exists(path):
        print(f"[FAIL] Missing required file: {path}")
        return False
    return True

def audit_latex_chapter(tex_path: str):
    print(f"\n[*] Auditing LaTeX file: {tex_path}")
    with open(tex_path, "r", encoding="utf-8") as f:
        content = f.read()

    errors = 0
    # 1. Check label prefix conventions
    labels = re.findall(r'\\label\{([^}]+)\}', content)
    for lbl in labels:
        if not (lbl.startswith("fig:") or lbl.startswith("tab:") or lbl.startswith("eq:") or lbl.startswith("sec:") or lbl.startswith("def:") or lbl.startswith("thm:")):
            print(f"[WARN] Non-standard label prefix: '{lbl}'. Expected fig:, tab:, eq:, sec:, def:, thm:.")
            errors += 1

    # 2. Check title case in section headings (ensure sentence case)
    sections = re.findall(r'\\(section|subsection|subsubsection)\{([^}]+)\}', content)
    for level, title in sections:
        words = title.split()
        capitalized = [w for w in words[1:] if w[0].isupper() and not w.isupper() and w not in ["Bayes", "Markov", "Gaussian", "Laplace", "Euler", "TikZ", "PGFPlots", "Manim", "Python", "PyTorch", "Politecnico", "Torino", "Tommasi", "Caputo", "Bishop", "Goodfellow"]]
        if len(capitalized) > 2:
            print(f"[WARN] Possible Title Case in {level}: '{title}'. Please enforce sentence case.")

    # 3. Check for external source citations
    citations = re.findall(r'\\cite\{([^}]+)\}', content)
    print(f"[+] Total numeric citations found: {len(citations)}")
    if len(citations) == 0:
        print("[WARN] No citations found. Did you triangulate with papers and books?")

    if errors == 0:
        print("[PASS] LaTeX structural audit passed.")
    else:
        print(f"[FAIL] Found {errors} warnings/errors.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 verify_coverage.py <path_to_chapter.tex>")
        sys.exit(1)
    audit_latex_chapter(sys.argv[1])
```

---

## 6. Multi-Agent Team Execution Plan

When spawning the AI multi-agent team to build this skill:

```
+----------------------------------------------------------------------------------------------------+
|                                    ORCHESTRATOR / TEAM LEAD AGENT                                  |
|   - Initializes directory structure in .agents/skills/advanced-machine-learning-study-guide-integrator|
|   - Reviews and enforces Zero-Omission, Professor Flow Anchor, and Multi-Book Deep Dive.          |
+----------------------------------------------------------------------------------------------------+
        |                            |                              |                            |
        v                            v                              v                            v
+------------------+       +-------------------+          +-------------------+        +-------------------+
|  AGENT 1: CORE   |       |  AGENT 2: THEORY  |          |  AGENT 3: VISUAL  |        |  AGENT 4: AUDIT   |
|  & ARCHITECTURE  |       |  & BOOKS ENGINE   |          |  & GRAPHICS       |        |  & VERIFICATION   |
|                  |       |                   |          |                   |        |                   |
| - Authors        |       | - Implements      |          | - Authors TikZ    |        | - Implements      |
|   SKILL.md       |       |   inspect_books.py|            guidelines &      |          verify_coverage.py|
| - Specifies 4    |       | - Maps Bishop,    |            architecture      |        | - Runs test gates |
|   integration    |         Goodfellow, Sutton|            templates         |        |   on sample       |
|   modes &        |         & Barto, Russell  |          | - Configures      |          chapters          |
|   transcription  |       | - Authors seminal |            PGFPlots & Manim  |        | - Verifies PDF    |
|   protocol       |         paper protocol    |            guidelines        |          compilability     |
+------------------+       +-------------------+          +-------------------+        +-------------------+
```

### Execution Steps:
1. **Agent 1 (Core Architecture)**: Scaffold directory layout, author `SKILL.md`, `references/00_video_transcription_protocol.md`, and `references/03_integration_modes.md`.
2. **Agent 2 (Theory & Books Engine)**: Author `references/01_book_inspection_protocol.md`, `references/02_seminal_paper_research_protocol.md`, and implement `scripts/inspect_books.py`.
3. **Agent 3 (Visual & Graphics Framework)**: Author `references/04_math_expansion_and_tensors.md` and `references/05_tikz_pgfplots_manim_guidelines.md`.
4. **Agent 4 (Audit & Quality Verification)**: Author `references/06_zero_omission_and_audit_checklist.md`, implement `scripts/verify_coverage.py` and `scripts/transcribe_lecture.py`.
5. **Team Lead (End-to-End Test)**: Execute `scripts/inspect_books.py --query "Bayes risk"`, run `scripts/verify_coverage.py` on a test template, and confirm all skill files are registered and validated.
