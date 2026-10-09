# Sources Dossier: Chapter 05 (The Transformer Architecture)

This directory houses all required primary and external reference materials for Chapter 05, organized prior to chapter authoring to ensure zero omission, rigorous pedagogical grounding, and adherence to the *Linear Causal Progression* and *Curated Purposeful Integration* principles.

## 1. Definitive Graduate Textbooks
- [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) (Dan Jurafsky & James H. Martin — 3rd ed. draft, 2024)
  - **Chapter 10**: Transformers and Large Language Models
  - **Why it matters**: The standard NLP graduate textbook reference for the complete Transformer pipeline.
  - **What it covers**: High-level Encoder-Decoder architecture, Scaled Dot-Product Attention, Query-Key-Value vector roles, Multi-Head Attention equations, causal masking, residual connections, Layer Normalization, and decoding algorithms.
- [Dive into Deep Learning (D2L.ai)](https://d2l.ai/) (Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola — Cambridge University Press, 2023)
  - **Chapter 11**: Attention Mechanisms and Transformers
  - **Why it matters**: Bridges mathematical derivations with complete, working PyTorch/NumPy implementations from scratch (without high-level `nn.Transformer` abstractions).
  - **What it covers**: Attention pooling, Nadaraya-Watson kernel regression, Scaled Dot-Product Attention, Multi-Head Attention, Self-Attention vs. Cross-Attention, Transformer blocks, and relative positional representations.
- [Understanding Deep Learning](https://udlbook.github.io/udlbook/) (Simon J.D. Prince — MIT Press, 2023)
  - **Chapter 12**: Transformers
  - **Why it matters**: Excellent geometric and matrix visual breakdowns of dot-product similarity routing and self-attention operations.
  - **What it covers**: Self-attention as graph message passing, keys/queries/values as linear projections, multi-head subspaces, and positional encoding mechanisms.

## 2. Intuitive Masterclasses & Visual Walkthroughs
- 3Blue1Brown (Grant Sanderson): ["Attention in transformers, visually explained | Chapter 6, Deep Learning" (2024)](https://www.youtube.com/watch?v=eMlx5fFNoYc)
  - **Why it matters**: The undisputed gold standard visual intuition for the Query, Key, Value attention mechanism.
  - **Key insights**: Visualizes how word vectors move in high-dimensional embedding space through attention.
  - **Iconic Pedagogical Example ("Fluffy Blue Creature")**: In the phrase *"A fluffy blue creature roamed the verdant forest"*, the token *"creature"* emits a **Query** vector asking: *"What adjectives precede me?"*. The tokens *"fluffy"* and *"blue"* advertise **Key** vectors responding: *"I am an adjective at position $j$."* High dot-product compatibility scores yield large attention weights that blend the **Value** vectors of *"fluffy"* and *"blue"* into a context offset $\Delta \mathbf{e}_{\text{creature}}$, moving the embedding of *"creature"* towards a specialized semantic region (a fluffy blue animal).
- Andrej Karpathy: ["Let's build GPT: from scratch, in code, spelled out" (2023)](https://www.youtube.com/watch?v=kCc8FmEb1nY)
  - **Why it matters**: Complete, line-by-line PyTorch implementation of the Transformer block from raw tensor operations.
  - **Key insights**: Derives Scaled Dot-Product Attention step-by-step; explains why the variance of $\mathbf{q}^\top \mathbf{k}$ scales as $d_k$ and why $\frac{1}{\sqrt{d_k}}$ preserves unit variance; demonstrates causal masking with `tril`; builds Multi-Head Attention via parallel linear heads; adds residual skip connections and LayerNorm; demonstrates autoregressive generation with temperature scaling and top-$k$ filtering.
  - **Companion code**: [`nanoGPT` repository](https://github.com/karpathy/nanoGPT) (clean, minimal GPT training and inference codebase).
- Jay Alammar: ["The Illustrated Transformer" (2018)](https://jalammar.github.io/illustrated-transformer/)
  - **Why it matters**: The seminal visual guide breaking down the Transformer Encoder-Decoder mechanics.
  - **Key insights**: Clear block-by-block flowcharts of vectors passing through self-attention, feed-forward sublayers, residual addition, and layer normalization.

## 3. Landmark Seminal Papers (Primary Ground Truth)
- **The Core Architecture & Attention Foundations**:
  - Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, {\L}., & Polosukhin, I. (2017): [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (NeurIPS 2017):
    - Scaled Dot-Product Attention:
      $$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}} + \mathbf{M}\right)\mathbf{V}$$
    - Multi-Head Attention:
      $$\text{MultiHead}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \left[ \text{head}_1 \parallel \dots \parallel \text{head}_h \right] \mathbf{W}^O, \quad \text{head}_i = \text{Attention}(\mathbf{Q}\mathbf{W}_i^Q, \mathbf{K}\mathbf{W}_i^K, \mathbf{V}\mathbf{W}_i^V)$$
    - Sinusoidal Positional Encoding:
      $$\text{PE}_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right), \quad \text{PE}_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)$$
- **Relative Positional Representations**:
  - Shaw, P., Uszkoreit, J., & Vaswani, A. (2018): [Self-Attention with Relative Position Representations](https://arxiv.org/abs/1803.02155) (NAACL-HLT 2018):
    - Replaces absolute positional embeddings with pairwise relative offsets $S_{\text{rel}} \in \mathbb{R}^{L \times L}$:
      $$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left( \frac{\mathbf{Q}\mathbf{K}^\top + \mathbf{S}_{\text{rel}}}{\sqrt{d_k}} \right)\mathbf{V}$$
    - Proves that relative distance matters most in self-attention, whereas cross-attention lacks a natural relative coordinate frame between disjoint source and target sequences.
- **Deep Normalization & Residual Highways**:
  - He, K., Zhang, X., Ren, S., & Sun, J. (2016): [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) (CVPR 2016) — Formulates identity shortcut connections $\mathbf{y} = \mathcal{F}(\mathbf{x}) + \mathbf{x}$, providing an unobstructed gradient superhighway $\frac{\partial \mathcal{L}}{\partial \mathbf{x}} = \frac{\partial \mathcal{L}}{\partial \mathbf{y}} (\mathbf{I} + \frac{\partial \mathcal{F}}{\partial \mathbf{x}})$.
  - Ba, J. L., Kiros, J. R., & Hinton, G. E. (2016): [Layer Normalization](https://arxiv.org/abs/1607.06450) — Normalizes activations across features for each individual token independently of batch statistics:
    $$\text{LN}(\mathbf{x}) = \frac{\mathbf{x} - \mu}{\sqrt{\sigma^2 + \epsilon}} \odot \boldsymbol{\gamma} + \boldsymbol{\beta}, \quad \mu = \frac{1}{d}\sum_{j=1}^d x_j, \quad \sigma^2 = \frac{1}{d}\sum_{j=1}^d (x_j - \mu)^2$$
- **Unified Text-to-Text Transfer Framework**:
  - Raffel, C., et al. (2020): [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683) (JMLR 2020) — Formulates T5, casting all NLP tasks into an encoder-decoder text generation framing with task-conditioning string prefixes.
- **Bidirectional Representation Learning (Encoder-Only)**:
  - Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019): [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) (NAACL-HLT 2019):
    - Input representation: Token + Segment + Positional embeddings. Special tokens: `[CLS]` (sentence representation) and `[SEP]` (sentence separator).
    - Pre-training tasks:
      1. Masked Language Model (MLM): 15% tokens corrupted (80% `[MASK]`, 10% random token, 10% unchanged).
      2. Next Sentence Prediction (NSP): 50% contiguous pair (IsNext), 50% randomly sampled pair (NotNext).
- **Autoregressive Generative Pre-training (Decoder-Only)**:
  - Radford, A., Narasimhan, K., Salimans, T., & Sutskever, I. (2018): [Improving Language Understanding by Generative Pre-Training](https://openai.com/research/language-unsupervised) (GPT-1).
  - Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019): [Language Models are Unsupervised Multitask Learners](https://openai.com/index/better-language-models/) (GPT-2).
  - Brown, T., et al. (2020): [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) (GPT-3).
- **Decoding & Sampling Dynamics**:
  - Holtzman, A., Buys, J., Du, L., Forbes, M., & Choi, Y. (2020): [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751) (ICLR 2020):
    - Proves the degeneration and repetition traps of greedy decoding and beam search in open-ended generation.
    - Formulates Nucleus (Top-$p$) Sampling, dynamically truncating to the smallest candidate set $V^{(p)}$ such that $\sum_{w \in V^{(p)}} P(w) \ge p$.
  - Fan, A., Lewis, M., & Dauphin, Y. (2018): [Hierarchical Neural Story Generation](https://arxiv.org/abs/1805.04833) (ACL 2018):
    - Introduces Top-$k$ filtering to eliminate unreliable tail distribution noise.

## 4. Top University Video Lectures
- **Stanford CS224n (Natural Language Processing with Deep Learning)**:
  - Lecture 8: *Attention and Transformers* (Christopher Manning & John Hewitt). Focuses on attention mechanisms, dot-product vs. additive attention, Scaled Dot-Product variance stabilization, and Multi-Head projection.
  - Lecture 9: *Transformers and Pretraining*. Focuses on the Transformer block anatomy, residual connections, and positional representations.
  - Lecture 10: *Natural Language Generation*. Explores decoding algorithms (Greedy, Beam Search, Temperature, Top-$k$, Top-$p$).
- **Stanford CS231n (Deep Learning for Computer Vision)**:
  - Lecture 11: *Transformers and Attention* (Justin Johnson / Fei-Fei Li). Visualizes attention matrices as dynamic graph weights connecting spatial/temporal tokens.
- **MIT 6.S191 (Introduction to Deep Learning)**:
  - Lecture 2: *Recurrent Neural Networks and Transformers* (Alexander Amini). Visual animations of information flow, comparing the sequential recurrent bottleneck with constant-path attention.

## 5. In This Workspace
- Target Chapter File: [`STUDY_GUIDE/lectures/chapters/part1_foundations/05_transformer_architecture.tex`](../../lectures/chapters/part1_foundations/05_transformer_architecture.tex).
- Lecture Slides: [`slides/05-Transformers.pdf`](slides/05-Transformers.pdf) (symlinked to `SLIDES/05-Transformers.pdf`).
  - Slides 1–10: The RNN bottleneck and parallelization imperative.
  - Slides 11–40: Positional Encodings (sinusoidal formulation, linear transformation property, similarity decay with distance).
  - Slides 41–66: Attention definition, fuzzy dictionary lookup, Q/K/V linear projections, Scaled Dot-Product Attention, and the exact step-by-step numerical worked example ($T=3, d=2$).
  - Slides 67–71: The Triad of Attention (Encoder Self-Attention, Decoder Masked Self-Attention, Encoder-Decoder Cross-Attention).
  - Slides 72–73: Multi-Head Attention mechanics and concatenation.
  - Slides 74–77: Transformer sublayers: Residual skip connections and Layer Normalization.
  - Slides 78–79: Relative Positional Embeddings ($S_{\text{rel}}$ bias in attention logits).
  - Slide 80: Advantages of Transformers: $\mathcal{O}(1)$ path length and GPU parallelization.
  - Slides 81–85: High-level Encoder-Decoder framework and T5 (Text-to-Text Transfer Transformer).
  - Slides 86–92: Encoder-only architectures & BERT (Masked LM 80/10/10, Next Sentence Prediction, Token/Segment/Position embeddings, attention map analysis).
  - Slides 93–96: Decoder-only architectures & GPT (Causal autoregressive loop, GPT-2 unicorn generation example).
  - Slides 97–112: Next-token selection & sampling strategies: Greedy decoding, Beam Search, Random sampling, Top-$k$ filtering, Top-$p$ (Nucleus) sampling, and Temperature scaling ($T < 1.0$ sharpening vs. $T > 1.0$ flattening) evaluated on the Sherlock Holmes prompt.
- Lecture Transcriptions:
  - [`transcriptions/05-Transformers-I.md`](transcriptions/05-Transformers-I.md) (symlinked to `TRANSCRIPTIONS/LECTURES/05-Transformers-I.md`).
  - [`transcriptions/05-Transformers-II.md`](transcriptions/05-Transformers-II.md) (symlinked to `TRANSCRIPTIONS/LECTURES/05-Transformers-II.md`).
- Figures:
  - Original Architecture: `STUDY_GUIDE/lectures/figures/part1/transformer_architecture_vaswani2017.png`
  - 3Blue1Brown Attention Masterclass: `STUDY_GUIDE/lectures/figures/part1/3b1b_query_key.jpg`, `3b1b_attention_score_grid.jpg`, `3b1b_value_update.jpg`, `3b1b_richer_context.jpg`
  - Slide Visuals: `slide67_attention_types.png`, `slide75_residual_connections.png`, `slide76_layer_normalization.png`, `slide81_encoder_decoder.png`, `slide82_t5_architecture.png`, `slide86_encoder_only_bert.png`, `slide88_bert_input_encoding.png`, `slide89_bert_masked_lm.png`, `slide90_bert_nsp.png`, `slide93_decoder_only_gpt.png`, `slide95_gpt2_generation.png`, `slide101_beam_search.png`, `slide106_top_p_sampling.png`, `slide108_temperature_sampling.png`
