# Curated Notes: Christopher Bishop & Hugh Bishop (2024) - Deep Learning: Foundations and Concepts

## Chapter 8: Error Backpropagation
- **Efficiency of Gradient Computation**:
  - For an objective function with $W$ total parameters, numerical differentiation (finite differences) requires $W + 1$ function evaluations, each taking $O(W)$ steps, leading to an overall computational complexity of $O(W^2)$ per parameter update.
  - Error backpropagation evaluates the exact gradient $\nabla E(\mathbf{w})$ in $O(W)$ operations by caching intermediate activations during the forward pass and propagating errors backward via the vector-chain rule.
  - Forward pass computes activations: $\mathbf{a}^{(l)} = \mathbf{W}^{(l)} \mathbf{z}^{(l-1)} + \mathbf{b}^{(l)}$, $\mathbf{z}^{(l)} = h(\mathbf{a}^{(l)})$.
  - Backward pass computes error signals $\boldsymbol{\delta}^{(l)} \triangleq \frac{\partial E}{\partial \mathbf{a}^{(l)}}$:
    $$\boldsymbol{\delta}^{(l)} = h'(\mathbf{a}^{(l)}) \odot \left( (\mathbf{W}^{(l+1)})^\top \boldsymbol{\delta}^{(l+1)} \right)$$
  - Gradients with respect to weights:
    $$\frac{\partial E}{\partial \mathbf{W}^{(l)}} = \boldsymbol{\delta}^{(l)} (\mathbf{z}^{(l-1)})^\top$$
- **Memory Footprint**: Forward pass activations must be cached in memory (GPU VRAM) until the corresponding backward pass is completed. This creates the primary memory bottleneck in training deep networks.

---

## Chapter 10: Convolutional Networks
- **Cross-Correlation vs. Mathematical Convolution**:
  - In signal processing, continuous convolution is defined with a reflected (flipped) kernel: $(f * g)(t) = \int f(\tau) g(t - \tau) d\tau$.
  - In deep learning libraries (PyTorch, TensorFlow), the kernel is not flipped, which corresponds strictly to **cross-correlation**:
    $$S(i, j) = (I * K)(i, j) = \sum_m \sum_n I(i + m, j + n) K(m, n)$$
  - Because kernel weights are learned directly from data via backpropagation, flipping the kernel before training would simply learn the reflected weights; thus, the lack of flipping has zero impact on representational capacity.
- **Multi-Channel Convolution**:
  - Input tensor: $\mathbf{X} \in \mathbb{R}^{H \times W \times C_{\text{in}}}$.
  - Filter bank: $C_{\text{out}}$ kernels, each of size $F \times F \times C_{\text{in}}$.
  - Crucial rule: **Filters always span the entire depth $C_{\text{in}}$ of the input volume!**
  - Linear combination across all input channels produces one 2D spatial activation map per output filter:
    $$\mathbf{Y}_{:,:,k} = \sum_{c=1}^{C_{\text{in}}} \mathbf{X}_{:,:,c} * \mathbf{K}_{:,:,c,k} + b_k$$
- **Receptive Field Growth**:
  - In layer 1, a $3 \times 3$ filter has a receptive field of $3 \times 3$ on the input image.
  - In layer 2, another $3 \times 3$ filter applied to layer 1 has a receptive field of $5 \times 5$ on the input image!
  - Stacking $L$ layers of $3 \times 3$ convolutions yields an effective receptive field of $(2L + 1) \times (2L + 1)$ with vastly fewer parameters than a single large $(2L + 1) \times (2L + 1)$ filter.
