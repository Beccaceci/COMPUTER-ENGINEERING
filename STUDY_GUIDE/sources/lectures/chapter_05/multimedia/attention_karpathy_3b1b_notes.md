# Notes on Attention Masterclasses: 3Blue1Brown & Andrej Karpathy

## 1. 3Blue1Brown: Visualizing Attention and Transformers (2024)
- **Vector Space Shifting**: Word embeddings are static points in high-dimensional space. Attention allows these vectors to "shift" their position dynamically in context.
- **The Information Transfer Mechanism**:
  - A query vector $\mathbf{q}_i = \mathbf{x}_i \mathbf{W}_Q$ is a prompt asking: *"I am a pronoun; what noun am I referring to?"* or *"I am a verb; what is my direct object?"*.
  - A key vector $\mathbf{k}_j = \mathbf{x}_j \mathbf{W}_K$ is a tag responding: *"I am a masculine singular noun preceding you"*.
  - The dot product $\mathbf{q}_i^\top \mathbf{k}_j$ measures the geometric alignment of the question and the tag.
  - The value vector $\mathbf{v}_j = \mathbf{x}_j \mathbf{W}_V$ is the payload of contextual information that is blended into the representation of token $i$.
- **Attention Matrix as Heatmap**:
  - Normalizing by row-wise softmax guarantees that the attention weights form a probability distribution summing to 1.0 for each query.

## 2. Andrej Karpathy: Let's build GPT from scratch (2023)
- **Variance Proof of Scaled Dot-Product**:
  - Karpathy demonstrates in Python:
    ```python
    q = torch.randn(B, T, 16)
    k = torch.randn(B, T, 16)
    wei = q @ k.transpose(-2, -1)  # variance of wei is 16!
    # With large variance, softmax(wei) becomes an extreme one-hot distribution:
    # torch.softmax(wei, dim=-1) produces weights like [0.0001, 0.9998, 0.0001]
    # Scaling by 16**-0.5 brings variance back to 1.0!
```
- **Causal Masking Trick**:
  - Lower triangular matrix `torch.tril(torch.ones(T, T))` has 1s on and below the diagonal, and 0s above.
  - Masking future positions:
    ```python
    wei = wei.masked_fill(tril == 0, float('-inf'))
    wei = F.softmax(wei, dim=-1)
```
  - This sets future attention weights to strictly zero because $\exp(-\infty) = 0$.
- **Parallelization Advantage**:
  - Recurrent models must loop $T$ times. Attention computes all $T \times T$ interactions simultaneously via matrix multiplication on GPU tensor cores.
