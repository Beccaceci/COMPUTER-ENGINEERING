# Curated Video Lectures for Lecture 1: Foundations & Learning Paradigms

This registry stages the key video breakdowns from our curated creator index that enrich the lecture topics.

---

## 1. 3Blue1Brown (Grant Sanderson)
- **Title**: *Linear Transformations and Matrices* (Essence of Linear Algebra, Chapter 3)
- **Link**: [https://www.youtube.com/watch?v=kYB8IZa5AuE](https://www.youtube.com/watch?v=kYB8IZa5AuE)
- **Role in AML**: Geometric representation of feature space transformations. Shows how linear models rotate, scale, and project high-dimensional feature spaces, connecting directly to Slide 86 (Choosing a Representation) and the Iris projection problem.
- **Key Oral Insights**:
  - A feature representation $\boldsymbol{\phi}(\mathbf{x})$ is a geometric mapping from raw input manifold to latent decision space.
  - Linear separability depends entirely on whether the chosen transformation aligns the underlying classes along orthogonal bases.

- **Title**: *What is a Neural Network?* (Deep Learning, Chapter 1)
- **Link**: [https://www.youtube.com/watch?v=aircAruvnKk](https://www.youtube.com/watch?v=aircAruvnKk)
- **Role in AML**: Connects the transition from manual feature engineering (Slide 86) to automated hierarchical representation learning in Deep Learning (Slide 96).

---

## 2. Andrej Karpathy
- **Title**: *The Spelled-out Intro to Neural Networks and Backpropagation: Building Micrograd*
- **Link**: [https://www.youtube.com/watch?v=VMj-3S1tku0](https://www.youtube.com/watch?v=VMj-3S1tku0)
- **Role in AML**: First-principles breakdown of Tom Mitchell's learning triad $(T, P, E)$. Shows how experience $E$ (data) adjusts continuous parameters $\mathbf{w}$ via gradient descent to minimize empirical risk $\hat{R}_N$.

---

## 3. Nello Cristianini
- **Title**: *On the Foundations of Artificial Intelligence: Computational Rationality and Shortcuts*
- **Link**: [https://www.youtube.com/watch?v=M5K3-Z8gY0g](https://www.youtube.com/watch?v=M5K3-Z8gY0g)
- **Role in AML**: Directly mirrors Prof. Tommasi's discussion on Slide 42 (Computational Rationality) and Slide 100 (Dataset Bias).
- **Key Oral Insights**:
  - Why pure logical rationality fails in high-dimensional real-world environments (computational intractability).
  - How bounded optimality formalizes intelligence under finite CPU/memory constraints.
  - Shortcut learning: how classifiers exploit spurious correlations (e.g. background grass instead of cow anatomy) when data exhibits distribution shift.

---

## 4. Antirez (Salvatore Sanfilippo)
- **Title**: *Machine Learning from Scratch: Why Representations Matter*
- **Link**: [https://www.youtube.com/watch?v=kY7fFz6q9gE](https://www.youtube.com/watch?v=kY7fFz6q9gE)
- **Role in AML**: Deep intuition on how representation design dictates algorithm complexity. Explains the playing cards analogy ("what counts in spades does not count in poker") from an engineering and memory standpoint.

---

## 5. Enkk
- **Title**: *Representation Spaces, Embeddings, and the Task-Driven Nature of Deep Learning*
- **Link**: [https://www.youtube.com/watch?v=7X5zY8b8rWc](https://www.youtube.com/watch?v=7X5zY8b8rWc)
- **Role in AML**: Analyzes the shift from classical hand-crafted computer vision descriptors (SIFT, HOG) to end-to-end task-driven representations in deep neural backbones.

---

## 6. AI Explained
- **Title**: *The Paradigm Shift: From Supervised to Self-Supervised and Foundation Models*
- **Link**: [https://www.youtube.com/watch?v=1F9rTz7pQ2A](https://www.youtube.com/watch?v=1F9rTz7pQ2A)
- **Role in AML**: Comprehensive synthesis of the learning spectrum (Slides 54–64: Supervised, Unsupervised, Reinforcement, Self-Supervised).
