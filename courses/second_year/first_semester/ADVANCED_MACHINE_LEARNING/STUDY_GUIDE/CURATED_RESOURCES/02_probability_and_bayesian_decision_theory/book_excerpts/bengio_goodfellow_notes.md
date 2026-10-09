# Deep Inspection: Goodfellow, Bengio & Courville (2016)
## Chapters 3 & 5: Probability, Information Theory & Statistical Learning Foundations

This document extracts formal mathematical theorems, derivations, and definitions from *Deep Learning* (MIT Press, 2016) by Ian Goodfellow, Yoshua Bengio, and Aaron Courville, anchoring the core content of Lecture 2.

---

### 1. The Foundations of Probability & Plausible Reasoning (Chapter 3)
- **Frequentist vs. Bayesian Interpretation**:
  Machine learning models uncertainty in two forms:
  1. *Aleatoric uncertainty* (inherent physical stochasticity in the data-generating process).
  2. *Epistemic uncertainty* (lack of knowledge or finite sample limitations).
  Probability serves as an extension of formal logic to handle plausible reasoning (Cox's Theorem, Jaynes 2003).

- **Conditioning, Sum Rule, and Product Rule**:
  For random variables $\mathbf{x} \in \mathcal{X}$ and $\mathbf{y} \in \mathcal{Y}$:
  \begin{align}
  \text{Sum Rule (Marginalization):} \quad & p(\mathbf{x}) = \int_{\mathcal{Y}} p(\mathbf{x}, \mathbf{y}) \, d\mathbf{y}, \label{eq:bengio_sum_rule} \\
  \text{Product Rule:} \quad & p(\mathbf{x}, \mathbf{y}) = p(\mathbf{y} \mid \mathbf{x}) p(\mathbf{x}). \label{eq:bengio_product_rule}
  \end{align}

- **Independence vs. Uncorrelatedness (Section 3.8)**:
  - Random variables $\mathbf{x}$ and $\mathbf{y}$ are **independent** ($\mathbf{x} \perp \mathbf{y}$) if and only if:
    \begin{equation}
    p(\mathbf{x}, \mathbf{y}) = p(\mathbf{x}) p(\mathbf{y}) \quad \forall \mathbf{x}, \mathbf{y}.
    \label{eq:bengio_independence}
    \end{equation}
  - Covariance measures linear association:
    \begin{equation}
    \mathrm{Cov}(f(\mathbf{x}), g(\mathbf{y})) = \mathbb{E}\left[ (f(\mathbf{x}) - \mathbb{E}[f(\mathbf{x})]) (g(\mathbf{y}) - \mathbb{E}[g(\mathbf{y})]) \right].
    \label{eq:bengio_covariance}
    \end{equation}
  - **Key Oral Exam Pitfall highlighted by Bengio**: Independence implies zero covariance ($\mathbf{x} \perp \mathbf{y} \implies \mathrm{Cov}(\mathbf{x}, \mathbf{y}) = 0$). However, \textbf{zero covariance does NOT imply independence}! For example, if $x \sim \mathcal{U}(-1, 1)$ and $y = x^2$, $\mathrm{Cov}(x, y) = 0$ yet $y$ is completely determined by $x$.

---

### 2. Information Theory and Divergence Measures (Section 3.13)
- **Shannon Entropy**:
  Quantifies the fundamental lower bound on the expected number of bits/nats required to encode symbols drawn from distribution $P$:
  \begin{equation}
  H(P) = -\mathbb{E}_{\mathbf{x} \sim P}[\log P(\mathbf{x})] = -\sum_{\mathbf{x}} P(\mathbf{x}) \log P(\mathbf{x}).
  \label{eq:bengio_shannon_entropy}
  \end{equation}

- **Kullback-Leibler (KL) Divergence (Relative Entropy)**:
  Measures the inefficiency of encoding samples from true distribution $P$ using an optimal code designed for distribution $Q$:
  \begin{equation}
  D_{\mathrm{KL}}(P \parallel Q) = \mathbb{E}_{\mathbf{x} \sim P} \left[ \log \frac{P(\mathbf{x})}{Q(\mathbf{x})} \right] = \mathbb{E}_{\mathbf{x} \sim P}[\log P(\mathbf{x}) - \log Q(\mathbf{x})].
  \label{eq:bengio_kl_divergence}
  \end{equation}
  - Non-negativity (Gibbs' inequality): $D_{\mathrm{KL}}(P \parallel Q) \ge 0$, with equality if and only if $P = Q$ almost everywhere.
  - Asymmetry: $D_{\mathrm{KL}}(P \parallel Q) \ne D_{\mathrm{KL}}(Q \parallel P)$. Hence, KL divergence is \textbf{not a metric} (violates symmetry and triangle inequality).

- **Cross-Entropy**:
  \begin{equation}
  H(P, Q) = H(P) + D_{\mathrm{KL}}(P \parallel Q) = -\mathbb{E}_{\mathbf{x} \sim P}[\log Q(\mathbf{x})].
  \label{eq:bengio_cross_entropy}
  \end{equation}
  In machine learning, minimizing cross-entropy with respect to model parameters $\boldsymbol{\theta}$ ($Q = p_{\boldsymbol{\theta}}$) is mathematically equivalent to minimizing the KL divergence $D_{\mathrm{KL}}(P \parallel p_{\boldsymbol{\theta}})$, because $H(P)$ is invariant to $\boldsymbol{\theta}$.

---

### 3. Statistical Risk, Bayes Error & Maximum Likelihood (Chapter 5)
- **True Risk vs. Empirical Risk**:
  - True risk: $R(h) = \mathbb{E}_{(\mathbf{x}, y) \sim p_{\mathrm{data}}}[\ell(h(\mathbf{x}), y)]$.
  - Empirical risk: $\hat{R}_N(h) = \frac{1}{N} \sum_{i=1}^N \ell(h(\mathbf{x}_i), y_i)$.
- **Bayes Error**:
  The minimum achievable generalization error by any classifier:
  \begin{equation}
  R^* = \mathbb{E}_{\mathbf{x}} \left[ 1 - \max_{y} P(y \mid \mathbf{x}) \right].
  \label{eq:bengio_bayes_error}
  \end{equation}
  Even an oracle knowing the exact data-generating distribution $p(\mathbf{x}, y)$ cannot achieve zero error if the classes overlap ($P(y \mid \mathbf{x}) < 1$).
- **Maximum Likelihood as KL Divergence Minimization**:
  \begin{equation}
  \boldsymbol{\theta}_{\mathrm{ML}} = \argmax_{\boldsymbol{\theta}} \sum_{i=1}^N \log p_{\mathrm{model}}(\mathbf{x}_i; \boldsymbol{\theta}) \iff \argmin_{\boldsymbol{\theta}} D_{\mathrm{KL}}(\hat{p}_{\mathrm{data}} \parallel p_{\mathrm{model}}(\cdot; \boldsymbol{\theta})).
  \label{eq:bengio_mle_kl}
  \end{equation}
