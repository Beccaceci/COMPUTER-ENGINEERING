# Sources Dossier: Chapter 05 (The Transformer Architecture)

This directory houses all required primary and external reference materials for Chapter 05, organized prior to chapter authoring to ensure zero omission and rigorous pedagogical grounding.

## 1. Definitive Graduate Textbooks
- [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) (Dan Jurafsky & James H. Martin — 3rd ed. draft, 2024)
  - **Chapter 10**: Transformers and Large Language Models
  - **Why it matters**: The standard NLP graduate textbook reference for the complete Transformer pipeline.
  - **What it covers**: High-level Encoder-Decoder architecture, Scaled Dot-Product Attention, Query-Key-Value vector roles, Multi-Head Attention equations, causal masking, residual connections, and Layer Normalization.
- [Dive into Deep Learning (D2L.ai)](https://d2l.ai/) (Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola — Cambridge University Press, 2023)
  - **Chapter 11**: Attention Mechanisms and Transformers
  - **Why it matters**: Bridges mathematical derivations with complete, working PyTorch/NumPy implementations from scratch (without high-level `nn.Transformer` abstractions).
  - **What it covers**: Attention pooling, Nadaraya-Watson kernel regression, Scaled Dot-Product Attention, Multi-Head Attention, Self-Attention vs. Cross-Attention, and Transformer blocks.
- [Understanding Deep Learning](https://udlbook.github.io/udlbook/) (Simon J.D. Prince — MIT Press, 2023)
  - **Chapter 12**: Transformers
  - **Why it matters**: Excellent geometric and matrix visual breakdowns of dot-product similarity routing and self-attention operations.
  - **What it covers**: Self-attention as graph message passing, keys/queries/values as linear projections, multi-head subspaces, and positional encoding mechanisms.

## 2. Intuitive Masterclasses & Visual Walkthroughs
- 3Blue1Brown (Grant Sanderson): ["Attention in transformers, visually explained | Chapter 6, Deep Learning" (2024)](https://www.youtube.com/watch?v=eMlx5fFNoYc)
  - **Why it matters**: The undisputed gold standard visual intuition for the Query, Key, Value attention mechanism.
  - **Key insights**: Visualizes how word vectors move in high-dimensional embedding space through attention; explains Queries as questions ("What adjectives precede me?"), Keys as answers ("I am an adjective"), and Values as information payloads shifted into the target representation.
- Andrej Karpathy: ["Let's build GPT: from scratch, in code, spelled out" (2023)](https://www.youtube.com/watch?v=kCc8FmEb1nY)
  - **Why it matters**: Complete, line-by-line PyTorch implementation of the Transformer block from raw tensor operations.
  - **Key insights**: Derives Scaled Dot-Product Attention step-by-step; explains why the variance of $\mathbf{q}^\top \mathbf{k}$ scales as $d_k$ and why $\frac{1}{\sqrt{d_k}}$ preserves unit variance; demonstrates causal masking with `tril`; builds Multi-Head Attention via parallel linear heads; adds residual skip connections and LayerNorm.
  - **Companion code**: [`nanoGPT` repository](https://github.com/karpathy/nanoGPT) (clean, minimal GPT training and inference codebase).
- Jay Alammar: ["The Illustrated Transformer" (2018)](https://jalammar.github.io/illustrated-transformer/)
  - **Why it matters**: The seminal visual guide breaking down the Transformer Encoder-Decoder mechanics.
  - **Key insights**: Clear block-by-block flowcharts of vectors passing through self-attention, feed-forward sublayers, residual addition, and layer normalization.

## 3. Landmark Seminal Papers (Primary Ground Truth)
- **The Core Architecture**:
  - Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, {\L}., & Polosukhin, I. (2017): [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (NeurIPS 2017):
    - Scaled Dot-Product Attention:
      $$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}} + \mathbf{M}\right)\mathbf{V}$$
    - Multi-Head Attention:
      $$\text{MultiHead}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \left[ \text{head}_1 \parallel \dots \parallel \text{head}_h \right] \mathbf{W}^O, \quad \text{head}_i = \text{Attention}(\mathbf{Q}\mathbf{W}_i^Q, \mathbf{K}\mathbf{W}_i^K, \mathbf{V}\mathbf{W}_i^V)$$
    - Sinusoidal Positional Encoding:
      $$\text{PE}_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right), \quad \text{PE}_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)$$
- **Deep Normalization & Residual Highways**:
  - He, K., Zhang, X., Ren, S., & Sun, J. (2016): [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) (CVPR 2016) — Formulates identity shortcut connections $\mathbf{y} = \mathcal{F}(\mathbf{x}) + \mathbf{x}$, preventing gradient vanishing across deep multi-layer stacks.
  - Ba, J. L., Kiros, J. R., & Hinton, G. E. (2016): [Layer Normalization](https://arxiv.org/abs/1607.06450) — Normalizes activations across features for each individual token independently of batch statistics:
    $$\text{LN}(\mathbf{x}) = \frac{\mathbf{x} - \mu}{\sqrt{\sigma^2 + \epsilon}} \odot \boldsymbol{\gamma} + \boldsymbol{\beta}, \quad \mu = \frac{1}{d}\sum_{j=1}^d x_j, \quad \sigma^2 = \frac{1}{d}\sum_{j=1}^d (x_j - \mu)^2$$
- **Unified Text-to-Text Transfer Framework**:
  - Raffel, C., et al. (2020): [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683) (JMLR 2020) — Formulates T5, casting all NLP tasks into an encoder-decoder text generation framing.

## 4. Top University Video Lectures
- **Stanford CS224n (Natural Language Processing with Deep Learning)**:
  - Lecture 8: *Attention and Transformers* (Christopher Manning & John Hewitt). Focuses on attention mechanisms, dot-product vs. additive attention, Scaled Dot-Product variance stabilization, and Multi-Head projection.
  - Lecture 9: *Transformers and Pretraining*. Focuses on the Transformer block anatomy, residual connections, and positional representations.
- **Stanford CS231n (Deep Learning for Computer Vision)**:
  - Lecture 11: *Transformers and Attention* (Justin Johnson / Fei-Fei Li). Visualizes attention matrices as dynamic graph weights connecting spatial/temporal tokens.
- **MIT 6.S191 (Introduction to Deep Learning)**:
  - Lecture 2: *Recurrent Neural Networks and Transformers* (Alexander Amini). Visual animations of information flow, comparing the sequential recurrent bottleneck with constant-path attention.

## 5. In This Workspace
- Target Chapter File: [`STUDY_GUIDE/lectures/chapters/part1_foundations/05_transformer_architecture.tex`](../../lectures/chapters/part1_foundations/05_transformer_architecture.tex).
- Lecture Slides: [`slides/05-Transformers.pdf`](slides/05-Transformers.pdf) (symlinked to `SLIDES/05-Transformers.pdf`).
  - Slides 1–10: The RNN bottleneck and parallelization imperative.
  - Slides 41–66: Attention definition, fuzzy dictionary lookup, Q/K/V linear projections, Scaled Dot-Product Attention, and the exact step-by-step numerical worked example ($T=3, d=2$).
  - Slides 67–71: The Triad of Attention (Encoder Self-Attention, Decoder Masked Self-Attention, Encoder-Decoder Cross-Attention).
  - Slides 72–73: Multi-Head Attention mechanics and concatenation.
  - Slides 74–77: Transformer sublayers: Residual skip connections and Layer Normalization.
  - Slides 80: Advantages of Transformers: $\mathcal{O}(1)$ path length and GPU parallelization.
  - Slides 81–85: High-level Encoder-Decoder framework and T5 overview.
- Lecture Transcription: [`transcriptions/05-Transformers-I.md`](transcriptions/05-Transformers-I.md) (symlinked to `TRANSCRIPTIONS/LECTURES/05-Transformers-I.md`).
- **Empirical Slide Examples**:
  - **Slide 57–66 Numeric Matrix Calculation**: Exact worked numerical walkthrough with 3 input tokens ($d=2$), weight matrices $\mathbf{W}_Q, \mathbf{W}_K, \mathbf{W}_V$, scaled dot products, row-wise softmax, and weighted value aggregation producing exact output tokens:
    $\mathbf{o}_1 = [0.91, 1.02]$, $\mathbf{o}_2 = [0.85, 0.95]$, $\mathbf{o}_3 = [1.29, 1.44]$.
