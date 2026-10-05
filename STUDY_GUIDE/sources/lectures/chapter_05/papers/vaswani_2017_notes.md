# Seminal Paper Notes: Attention Is All You Need (Vaswani et al., 2017)

## 1. Citation
- **Authors**: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin
- **Venue**: Advances in Neural Information Processing Systems (NeurIPS 2017)
- **arXiv**: 1706.03762

## 2. Core Contributions
1. **Dispensing with Recurrence and Convolutions**:
   - The Transformer relies entirely on an attention mechanism to draw global dependencies between input and output sequences.
   - Reduces maximum path length between any two tokens from $\mathcal{O}(L)$ (RNN) or $\mathcal{O}(\log_k L)$ (CNN) to $\mathcal{O}(1)$.
2. **Scaled Dot-Product Attention**:
   $$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}}\right)\mathbf{V}$$
   - Scaling factor $\frac{1}{\sqrt{d_k}}$ prevents vanishing gradients during softmax backward pass when $d_k$ is large.
3. **Multi-Head Attention (MHA)**:
   $$\text{MultiHead}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{Concat}(\text{head}_1, \dots, \text{head}_h)\mathbf{W}^O$$
   $$\text{head}_i = \text{Attention}(\mathbf{Q}\mathbf{W}_i^Q, \mathbf{K}\mathbf{W}_i^K, \mathbf{V}\mathbf{W}_i^V)$$
   - Allows the model to jointly attend to information from different representation subspaces at different positions.
4. **Sinusoidal Positional Encoding**:
   $$\text{PE}_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)$$
   $$\text{PE}_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)$$
   - Wavelengths form a geometric progression from $2\pi$ to $10000 \cdot 2\pi$.
   - Allows the model to easily learn to attend by relative positions, since for any fixed offset $k$, $\text{PE}_{pos+k}$ is a linear function of $\text{PE}_{pos}$.
5. **Computational Complexity per Layer**:
   - Self-Attention: $\mathcal{O}(L^2 \cdot d)$ total complexity, $\mathcal{O}(1)$ sequential operations, $\mathcal{O}(1)$ maximum path length.
   - Recurrent: $\mathcal{O}(L \cdot d^2)$ total complexity, $\mathcal{O}(L)$ sequential operations, $\mathcal{O}(L)$ maximum path length.
   - Convolutional: $\mathcal{O}(k \cdot L \cdot d^2)$ total complexity, $\mathcal{O}(1)$ sequential operations, $\mathcal{O}(\log_k L)$ maximum path length.
