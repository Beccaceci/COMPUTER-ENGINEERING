# Seminal Papers Digest for Lecture 3: Numerical Optimization & Gradient Descent

This document extracts formal problem definitions, mathematical frameworks, and exam insights from the landmark research papers underlying Lecture 3.

---

## 1. The Method of Steepest Descent
- **Seminal Reference**: Cauchy, A. (1847). *Méthode générale pour la résolution des systèmes d'équations simultanées*. Comp. Rend. Sci. Paris, 25, 536-538.
- **Historical Formulation**:
  Augustin-Louis Cauchy proposed that to minimize an unconstrained real-valued function $f(\mathbf{w})$, one should take incremental steps along the direction where the directional derivative decreases most rapidly.
- **First-Order Vector Form**:
  \begin{equation}
  \mathbf{w}^{(t+1)} = \mathbf{w}^{(t)} - \eta_t \nabla f(\mathbf{w}^{(t)}),
  \label{eq:cauchy_gd}
  \end{equation}
  where $\nabla f(\mathbf{w}) = \left[ \frac{\partial f}{\partial w_1}, \dots, \frac{\partial f}{\partial w_d} \right]^\top \in \mathbb{R}^d$.

---

## 2. Stochastic Approximation & SGD Foundations
- **Seminal Reference**: Robbins, H., & Monro, S. (1951). *A Stochastic Approximation Method*. The Annals of Mathematical Statistics, 22(3), 400-407; Bottou, L., Curtis, F. E., & Nocedal, J. (2018). *Optimization Methods for Large-Scale Machine Learning*. SIAM Review, 60(2), 223-311.
- **Mathematical Problem Formulation**:
  When dataset size $N$ is massive ($N \sim 10^6 - 10^9$), computing the exact gradient of the empirical risk $\nabla \hat{R}_N(\mathbf{w}) = \frac{1}{N} \sum_{i=1}^N \nabla \ell(h(\mathbf{x}_i; \mathbf{w}), y_i)$ requires passing through all $N$ examples per step ($\mathcal{O}(N)$ compute).
- **The Mini-Batch Unbiased Estimator**:
  Sample a uniform mini-batch $\mathcal{B} \subset \{1, \dots, N\}$ of size $B = |\mathcal{B}| \ll N$. The stochastic gradient is:
  \begin{equation}
  \mathbf{g}_t(\mathbf{w}) = \frac{1}{B} \sum_{i \in \mathcal{B}} \nabla \ell(h(\mathbf{x}_i; \mathbf{w}), y_i).
  \label{eq:stochastic_gradient_estimator}
  \end{equation}
  - **Unbiasedness**: $\mathbb{E}_{\mathcal{B}}[\mathbf{g}_t(\mathbf{w})] = \nabla \hat{R}_N(\mathbf{w})$.
  - **Variance**: $\mathrm{Var}(\mathbf{g}_t(\mathbf{w})) = \frac{\sigma^2}{B} \left( \frac{N - B}{N - 1} \right) \approx \frac{\sigma^2}{B}$.
- **Robbins-Monro Convergence Conditions**:
  Stochastic gradient descent converges almost surely to a stationary point if the learning rate sequence $\{\eta_t\}_{t=1}^\infty$ satisfies:
  \begin{equation}
  \sum_{t=1}^\infty \eta_t = \infty \quad \text{and} \quad \sum_{t=1}^\infty \eta_t^2 < \infty.
  \label{eq:robbins_monro_conditions}
  \end{equation}

---

## 3. High-Dimensional Saddle Points & Non-Convex Curvature
- **Seminal Reference**: Dauphin, Y. N., Pascanu, R., Gulcehre, C., Cho, K., Ganguli, S., & Bengio, Y. (2014). *Identifying and attacking the saddle point problem in high-dimensional non-convex optimization*. Advances in Neural Information Processing Systems (NeurIPS 2014), pp. 2933-2941.
- **The Core Breakthrough**:
  Historically, researchers believed local minima were the primary obstacle preventing gradient descent from training deep models. Dauphin, Bengio et al. proved that in high dimensions:
  1. Local minima with high cost are exponentially rare. Almost all local minima sit near the global minimum value.
  2. **The proliferation of saddle points**: At a critical point $\nabla f = \mathbf{0}$, the eigenvalues of the Hessian matrix $\mathbf{H}$ follow a random matrix distribution (Wigner semicircle law).
  3. The fraction of critical points that are true local minima is $(1/2)^d$, which vanishes to zero for $d \ge 100$. Almost all critical points are **saddle points** with both positive and negative eigenvalues.
  4. First-order gradient descent slows down dramatically near saddle points where $\|\nabla f\| \approx 0$, requiring momentum or stochastic noise to escape along directions of negative curvature.
