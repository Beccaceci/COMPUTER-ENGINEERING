# Curated Notes: Goodfellow, Bengio & Courville (2016) - Deep Learning

## Chapter 6: Deep Feedforward Networks
- **Core Motivation**: Linear models are fundamentally limited: they cannot represent interactions between features and cannot compute non-linear functions like XOR. Designing hand-crafted feature transformations $\boldsymbol{\phi}(\mathbf{x})$ requires domain expertise and does not scale. Deep feedforward networks learn representations by composing non-linear functions $\mathbf{h}^{(l)} = \sigma(\mathbf{W}^{(l)} \mathbf{h}^{(l-1)} + \mathbf{b}^{(l)})$.
- **Resolving the XOR Dilemma**:
  - The XOR function: $f([0, 0]) = 0, f([1, 1]) = 0, f([0, 1]) = 1, f([1, 0]) = 1$.
  - A linear model $f(\mathbf{x}) = \mathbf{w}^\top \mathbf{x} + b$ fails because the four points cannot be separated by any single hyperplane.
  - A two-layer network with 2 hidden units and ReLU non-linearities maps the input space into a feature space $\mathbf{h} \in \mathbb{R}^2$ where $[0, 0] \mapsto [0, 0]$, $[1, 1] \mapsto [0, 0]$, $[1, 0] \mapsto [1, 0]$, and $[0, 1] \mapsto [0, 1]$.
  - In this transformed space, the positive and negative classes are collapsed and linearly separable!
- **Activation Functions**:
  - *Sigmoid & Tanh*: Saturated at extremes where $\sigma'(z) \to 0$. As depth increases, gradients diminish exponentially (vanishing gradient problem), stalling training.
  - *ReLU (Glorot et al., 2011)*: $\max(0, z)$. Piecewise linear, preserves gradient magnitude ($1$ for $z > 0$), computationally trivial, induces sparse representation.
- **Universal Approximation Theorem (Hornik, 1991; Cybenko, 1989)**:
  - Any continuous function on a compact subset of $\mathbb{R}^d$ can be approximated to arbitrary accuracy by a feedforward network with a single hidden layer and non-linear activation.
  - *Critical Oral Exam Pitfall*: Universal approximation is an **existence / representation theorem**, NOT a constructive or learning guarantee! It does NOT guarantee that gradient descent will find the optimal weights, nor that the required number of hidden units will be polynomial (it can be exponential $O(2^d)$). Deep networks achieve exponential statistical efficiency by reusing compositional features across depth.
- **Computational Graphs & Backpropagation**:
  - Forward pass computes intermediate activations; backward pass propagates adjoint error signals $\boldsymbol{\delta}$.
  - Reverse-mode automatic differentiation computes the full gradient vector $\nabla_{\mathbf{W}} \mathcal{L}$ in a single backward pass ($O(W)$ operations), whereas forward-mode or numerical finite differences would require $O(W \cdot \text{ops})$ or $O(W^2)$ operations.

---

## Chapter 9: Convolutional Networks
- **Core Motivation**: Three fundamental architectural principles:
  1. **Sparse Interactions (Sparse Connectivity)**: Kernel size $k \ll n$. Rather than connecting every output unit to every input unit ($m \times n$ operations), each output unit connects only to $k$ inputs ($m \times k$ operations). Receptive fields grow hierarchically with depth.
  2. **Parameter Sharing (Tied Weights)**: The same kernel weights are reused across every spatial location. This decouples parameter count from image resolution and enforces translational symmetry.
  3. **Translation Equivariance**: A function $f$ is equivariant to transformation $g$ if $f(g(\mathbf{x})) = g(f(\mathbf{x}))$. Convolution commutes with spatial translation: translating the input translates the feature map identically.
- **Pooling**:
  - Replaces detector outputs with a summary statistic (e.g., max-pooling).
  - Induces **approximate translation invariance**: small perturbations/shifts do not alter the pooled feature.
  - Downsamples spatial resolution and expands the effective receptive field of deeper layers.
- **Convolution and Pooling as an Infinitely Strong Prior**:
  - A prior belief that weights for neighboring units are identical (shifted in space) and that weights outside the kernel support are strictly zero.
  - Matches the physical statistics of natural images (locality, stationarity, scale hierarchy).
- **Why Put Fully Connected Layers (FCN) After Convolutional Layers**:
  - Convolutional layers preserve spatial coordinate topology and extract translation-equivariant local features.
  - Classification requires a **global, translation-invariant decision**: aggregating evidence across the entire spatial domain to predict a single categorical distribution.
  - The FCN acts as the global synthesizer: flattening/pooling the spatial feature maps and computing unconstrained dense linear combinations to produce class logits.
