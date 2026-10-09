# Seminal Papers Digest for Lecture 2: Probability, Decision Theory & Risk

This document extracts formal problem definitions, mathematical frameworks, and exam insights from the landmark research papers underlying Lecture 2.

---

## 1. Cox's Theorem: The Axioms of Plausible Reasoning
- **Seminal Reference**: Cox, R. T. (1946). *Probability, Frequency and Reasonable Expectation*. American Journal of Physics, 14(1), 1-13; Jaynes, E. T. (2003). *Probability Theory: The Logic of Science*. Cambridge University Press.
- **Foundational Motivation (Slide 7–11 of 02.1)**:
  Why must machine learning represent uncertainty using standard probability theory rather than fuzzy logic or ad-hoc scores?
- **The Three Core Desiderata**:
  1. *Degrees of plausibility are represented by real numbers*: Plausibility $p(A \mid B)$ is a continuous scalar.
  2. *Qualitative correspondence with common sense*: If evidence increases the plausibility of $A$, the plausibility of $\neg A$ must decrease.
  3. *Consistency*: If a conclusion can be reasoned in more than one way, every valid path must yield the identical plausibility score.
- **Theorem**:
  Any system satisfying these three consistency desiderata is isomorphic to standard probability calculus (Kolmogorov's axioms).

---

## 2. Information Theory and Relative Entropy
- **Seminal Reference**: Shannon, C. E. (1948). *A Mathematical Theory of Communication*. Bell System Technical Journal, 27(3), 379-423; Kullback, S., & Leibler, R. A. (1951). *On Information and Sufficiency*. Annals of Mathematical Statistics, 22(1), 79-86.
- **Mathematical Formulations**:
  - **Self-information**: $I(x) = -\log p(x)$ (measured in nats when using natural logarithm).
  - **Shannon entropy**: $H(X) = \mathbb{E}_{x \sim P}[-\log P(x)]$.
  - **Kullback-Leibler divergence**:
    \begin{equation}
    D_{\mathrm{KL}}(P \parallel Q) = \sum_{x \in \mathcal{X}} P(x) \log \frac{P(x)}{Q(x)}.
    \label{eq:paper_kl_def}
    \end{equation}
- **Proof of Non-Negativity via Jensen's Inequality**:
  Since $f(t) = -\log t$ is strictly convex:
  \begin{equation}
  D_{\mathrm{KL}}(P \parallel Q) = -\sum_{x} P(x) \log \frac{Q(x)}{P(x)} \ge -\log \left( \sum_{x} P(x) \frac{Q(x)}{P(x)} \right) = -\log(1) = 0.
  \label{eq:jensen_kl_proof}
  \end{equation}
  Equality holds if and only if $\frac{Q(x)}{P(x)} = 1$ for all $x$ where $P(x) > 0$.

---

## 3. Statistical Risk and Empirical Risk Minimization
- **Seminal Reference**: Vapnik, V. (1998). *Statistical Learning Theory*. Wiley; Shalev-Shwartz, S., & Ben-David, S. (2014). *Understanding Machine Learning: From Theory to Algorithms*. Cambridge University Press.
- **Core Formulations (Orabona & Srebro Slides, Lecture 2.2)**:
  - **True Statistical Risk**: $R(h) = \mathbb{E}_{(\mathbf{x}, y) \sim \mathcal{D}}[\ell(h(\mathbf{x}), y)]$.
  - **Bayes Optimal Classifier**:
    \begin{equation}
    h^*(\mathbf{x}) = \argmin_{\hat{y} \in \mathcal{Y}} \mathbb{E}_{y \sim P(y \mid \mathbf{x})}[\ell(\hat{y}, y)].
    \label{eq:paper_bayes_optimal}
    \end{equation}
    Under symmetric 0-1 loss, $h^*(\mathbf{x}) = \argmax_{y \in \mathcal{Y}} P(y \mid \mathbf{x})$.
  - **Bayes Risk**: $R^* = R(h^*)$ is the irreducible error caused by intrinsic class overlap in $P(\mathbf{x}, y)$.
  - **Generalization Gap**: $\mathrm{gen}(h) = R(h) - \hat{R}_N(h)$. Overfitting occurs when $\hat{R}_N(h) \ll R(h)$.
