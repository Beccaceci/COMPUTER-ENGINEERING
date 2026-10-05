# Notes on Transformers & Attention: Jurafsky & Martin (Chapter 10) & D2L (Chapter 11)

## 1. Encoder-Decoder Architectural Rationale
- Recurrent sequence-to-sequence models bottleneck input sequences into a single fixed-size vector $\mathbf{h}_T$. For sequences exceeding a few dozen tokens, this induces catastrophic forgetting of early contextual dependencies.
- The Transformer replaces recurrence with unconstrained attention routing: the encoder outputs an uncompressed sequence of contextual representations $\mathbf{H} = [\mathbf{h}_1, \dots, \mathbf{h}_L]$, allowing the decoder to attend dynamically to any source position at any generation step.

## 2. Attention Mechanics
- **Queries, Keys, and Values**:
  - Attention generalizes associative dictionary lookup to dense, continuous metric spaces.
  - Queries represent probing vectors ("What information is needed?").
  - Keys represent indexing tags ("What information is available here?").
  - Values represent the informational content transmitted if matched.
- **Scaled Dot-Product**:
  - The dot product $\mathbf{q}^\top \mathbf{k}$ measures vector alignment.
  - As dimension $d_k$ increases, the variance of $\mathbf{q}^\top \mathbf{k}$ scales linearly with $d_k$. Without scaling by $\frac{1}{\sqrt{d_k}}$, large values push the softmax function into its saturation regions where gradients vanish to zero.
- **Multi-Head Attention (MHA)**:
  - Projecting queries, keys, and values $h$ times with learned parameter matrices allows the model to jointly attend to information from different representation subspaces at different positions.
  - Total computation cost matches single-head attention of full dimension when $d_k = d_v = d_{\text{model}} / h$.

## 3. Sublayer Design: Residuals and Normalization
- Deep stacking of multi-head attention and feed-forward sublayers is stabilized by:
  - Residual connections: $\mathbf{x} + \text{Sublayer}(\mathbf{x})$, providing identity gradient highways.
  - Layer Normalization: Normalizing across features for each token independently: $\text{LN}(\mathbf{x}) = \frac{\mathbf{x} - \mu}{\sigma} \odot \boldsymbol{\gamma} + \boldsymbol{\beta}$.
