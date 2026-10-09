# Seminal Papers Digest for Lecture 1: Foundations & Learning Paradigms

This document extracts formal problem definitions, mathematical frameworks, and exam insights from the landmark research papers underlying Lecture 1.

---

## 1. Computational Rationality and Bounded Optimality
- **Seminal Reference**: Russell, S. (1997). *Rationality and Intelligence*. Artificial Intelligence, 94(1-2), 57-77. Horvitz, E. (1988). *Reasoning about beliefs and actions under computational resource constraints*.
- **Theoretical Problem Formulation**:
  Classical rationality assumes an agent possesses unlimited computational resources and selects the action that maximizes expected utility:
  \begin{equation}
  a^* = \argmax_{a \in \mathcal{A}} \mathbb{E}[U(s') \mid s, a]
  \label{eq:perfect_rationality}
  \end{equation}
  However, real physical agents are bounded by finite computational time $\tau$ and memory space $\mathcal{M}$.
- **Bounded Optimality Principle**:
  An agent program $p \in \mathcal{P}$ running on machine architecture $M$ is **bounded optimal** if it maximizes expected utility over all feasible programs that can actually execute within the resource budget:
  \begin{equation}
  p^* = \argmax_{p \in \mathcal{P}(M)} \mathbb{E}_{e \sim \mathcal{E}}\left[ U(\mathrm{Run}(p, M, e)) \right]
  \label{eq:bounded_optimality}
  \end{equation}
- **Exam Insight for Polito**: Prof. Tommasi highlights this on Slide 42 to contrast classical logic AI (which is computationally intractable in complex environments) with modern statistical machine learning, which trades exact symbolic deduction for bounded, expected utility maximization under uncertainty.

---

## 2. Statistical Definition of Learning
- **Seminal Reference**: Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill; Valiant, L. G. (1984). *A Theory of the Learnable*. Communications of the ACM, 27(11), 1134-1142.
- **Formal Definition (Slide 45)**:
  "A computer program is said to learn from experience $E$ with respect to some class of tasks $T$ and performance measure $P$, if its performance at tasks in $T$, as measured by $P$, improves with experience $E$."
- **Mathematical Decomposition**:
  - **Task space $\mathcal{T}$**: A functional mapping $f: \mathcal{X} \to \mathcal{Y}$.
  - **Experience $\mathcal{E}$**: An i.i.d. dataset $\mathcal{S} = \{(\mathbf{x}_i, y_i)\}_{i=1}^N \sim \mathcal{D}^N$ drawn from unknown joint data-generating distribution $\mathcal{D}$.
  - **Performance measure $\mathcal{P}$**: The statistical expectation of a loss function $\ell(\hat{y}, y)$, defining the true statistical risk $R(h) = \mathbb{E}_{(\mathbf{x}, y) \sim \mathcal{D}}[\ell(h(\mathbf{x}), y)]$.
  - Learning occurs if $\lim_{N \to \infty} P(R(h_N) - R(h^*) > \epsilon) = 0$ (PAC learnability).

---

## 3. The Datasaurus Dozen: The Fallacy of Summary Statistics
- **Seminal Reference**: Matejka, J., & Fitzmaurice, G. (2017). *Same Stats, Different Graphs: Generating Datasets with Varied Appearance and Identical Summary Statistics through Simulated Annealing*. ACM CHI 2017, pp. 1290-1294.
- **Background & Motivation**:
  Extending Francis Anscombe's famous 1973 quartet, Matejka & Fitzmaurice developed an optimization technique using simulated annealing to construct 13 distinct 2D datasets (including a Tyrannosaurus Rex, a star, circles, and slanted lines) that all share the exact same summary statistics to two decimal places:
  - Mean of $X$: $\bar{x} = 54.26$
  - Mean of $Y$: $\bar{y} = 47.83$
  - Standard Deviation of $X$: $s_x = 16.76$
  - Standard Deviation of $Y$: $s_y = 26.93$
  - Pearson Correlation Coefficient: $r = -0.06$
- **Mathematical Optimization via Simulated Annealing**:
  Given initial dataset $\mathbf{D}_0$ and target shape image $S$, the algorithm iteratively perturbs point coordinates $(x_i, y_i) \to (x_i + \Delta x, y_i + \Delta y)$ subject to hard constraint bounds on statistical error:
  \begin{equation}
  \mathrm{Error}(\mathbf{D}) = \sum_{k \in \{\mu_x, \mu_y, \sigma_x, \sigma_y, r\}} \left| \mathrm{Stat}_k(\mathbf{D}) - \mathrm{Target}_k \right| < \epsilon
  \label{eq:datasaurus_loss}
  \end{equation}
  while minimizing distance to the target raster silhouette.
- **Pedagogical Significance in AML (Slide 71–72)**:
  Before choosing a model family, the machine learner must visualize and understand the high-dimensional data manifold. Relying solely on low-order statistical moments (mean, variance, covariance) blindly obscures non-linear geometric structure.

---

## 4. Dataset Bias and Domain Shift
- **Seminal Reference**: Saenko, K., Kulis, B., Fritz, M., & Darrell, T. (2010). *Adapting Visual Category Models to New Domains*. European Conference on Computer Vision (ECCV 2010), pp. 213-226.
- **Theoretical Problem Formulation**:
  Standard supervised machine learning operates under the foundational **i.i.d. assumption**:
  \begin{equation}
  \mathcal{D}_{\text{train}} = \mathcal{D}_{\text{test}} = \mathcal{D}_{(\mathbf{x}, y)}
  \label{eq:iid_assumption}
  \end{equation}
  In real-world computer vision, datasets collected in one environment (e.g. Amazon product images with clean white backgrounds) fail drastically when deployed in another (e.g. webcam photos in messy office rooms—the Office-31 benchmark introduced by Saenko et al.).
- **Covariate Shift vs. Concept Drift**:
  - **Covariate Shift**: $P_{\text{source}}(\mathbf{x}) \ne P_{\text{target}}(\mathbf{x})$, but conditional label distribution remains invariant $P(y \mid \mathbf{x}) = P_{\text{source}}(y \mid \mathbf{x}) = P_{\text{target}}(y \mid \mathbf{x})$.
  - **Concept Drift**: $P_{\text{source}}(y \mid \mathbf{x}) \ne P_{\text{target}}(y \mid \mathbf{x})$.
- **Pedagogical Significance in AML (Slide 100)**:
  Prof. Tommasi is an internationally recognized leader in domain adaptation and transfer learning. Slide 100 introduces this foundational pillar: representation learning cannot assume distribution stationarity; models must be engineered to align source and target feature distributions (e.g., via domain adversarial training or maximum mean discrepancy).
