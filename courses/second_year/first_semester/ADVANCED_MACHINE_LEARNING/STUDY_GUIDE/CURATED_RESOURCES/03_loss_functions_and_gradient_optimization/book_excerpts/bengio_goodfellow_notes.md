# Deep Inspection: Goodfellow, Bengio & Courville (2016)
## Chapters 4 & 8: Numerical Computation, Optimization Dynamics & Gradient Descent

This document extracts formal mathematical theorems, derivations, and definitions from *Deep Learning* (MIT Press, 2016) by Ian Goodfellow, Yoshua Bengio, and Aaron Courville, anchoring the core content of Lecture 3.

---

### 1. Directional Derivatives & Method of Steepest Descent (Chapter 4)
- **Directional Derivative**:
  The directional derivative of scalar function $f: \mathbb{R}^n \to \mathbb{R}$ in unit direction $\mathbf{u}$ ($\|\mathbf{u}\|_2 = 1$) is:
  \begin{equation}
  D_{\mathbf{u}} f(\mathbf{x}) = \lim_{\alpha \to 0} \frac{f(\mathbf{x} + \alpha \mathbf{u}) - f(\mathbf{x})}{\alpha} = \mathbf{u}^\top \nabla_{\mathbf{x}} f(\mathbf{x}).
  \label{eq:bengio_directional_derivative}
  \end{equation}

- **Steepest Descent Derivation**:
  To minimize $f(\mathbf{x})$, we seek the unit direction $\mathbf{u}$ that minimizes the directional derivative:
  \begin{equation}
  \min_{\mathbf{u}: \|\mathbf{u}\|_2 = 1} \mathbf{u}^\top \nabla_{\mathbf{x}} f(\mathbf{x}) = \min_{\mathbf{u}: \|\mathbf{u}\|_2 = 1} \|\mathbf{u}\|_2 \|\nabla_{\mathbf{x}} f(\mathbf{x})\|_2 \cos \theta = -\|\nabla_{\mathbf{x}} f(\mathbf{x})\|_2,
  \label{eq:bengio_steepest_descent_proof}
  \end{equation}
  which occurs when $\cos \theta = -1 \iff \mathbf{u} = -\frac{\nabla_{\mathbf{x}} f(\mathbf{x})}{\|\nabla_{\mathbf{x}} f(\mathbf{x})\|_2}$.
  Hence, the negative gradient $-\nabla_{\mathbf{x}} f(\mathbf{x})$ points in the direction of steepest local descent.

- **The Steepest Descent Update Rule**:
  \begin{equation}
  \mathbf{x}^{(t+1)} = \mathbf{x}^{(t)} - \epsilon \nabla_{\mathbf{x}} f(\mathbf{x}^{(t)}),
  \label{eq:bengio_gd_update}
  \end{equation}
  where $\epsilon > 0$ is the learning rate (step size).

---

### 2. Second-Order Curvature, Hessian Matrix & Condition Number (Section 4.3)
- **The Hessian Matrix**:
  $\mathbf{H}(f)(\mathbf{x}) \in \mathbb{R}^{n \times n}$ where $H_{i,j} = \frac{\partial^2 f}{\partial x_i \partial x_j}$. By Schwarz's theorem, when partial derivatives are continuous, $\mathbf{H}$ is symmetric ($H_{i,j} = H_{j,i}$).

- **Second-Order Taylor Series Approximation**:
  Expanding $f(\mathbf{x})$ around point $\mathbf{x}^{(0)}$:
  \begin{equation}
  f(\mathbf{x}) \approx f(\mathbf{x}^{(0)}) + (\mathbf{x} - \mathbf{x}^{(0)})^\top \mathbf{g} + \frac{1}{2} (\mathbf{x} - \mathbf{x}^{(0)})^\top \mathbf{H} (\mathbf{x} - \mathbf{x}^{(0)}),
  \label{eq:bengio_second_order_taylor}
  \end{equation}
  where $\mathbf{g} = \nabla_{\mathbf{x}} f(\mathbf{x}^{(0)})$.
  If we take a gradient step $\mathbf{x} = \mathbf{x}^{(0)} - \epsilon \mathbf{g}$, the predicted objective value is:
  \begin{equation}
  f(\mathbf{x}^{(0)} - \epsilon \mathbf{g}) \approx f(\mathbf{x}^{(0)}) - \epsilon \mathbf{g}^\top \mathbf{g} + \frac{1}{2} \epsilon^2 \mathbf{g}^\top \mathbf{H} \mathbf{g}.
  \label{eq:bengio_taylor_step}
  \end{equation}

- **Optimal Analytical Step Size for Quadratic Forms**:
  Differentiating \cref{eq:bengio_taylor_step} with respect to $\epsilon$ and setting to zero:
  \begin{equation}
  -\mathbf{g}^\top \mathbf{g} + \epsilon \mathbf{g}^\top \mathbf{H} \mathbf{g} = 0 \implies \epsilon^* = \frac{\mathbf{g}^\top \mathbf{g}}{\mathbf{g}^\top \mathbf{H} \mathbf{g}}.
  \label{eq:bengio_optimal_step}
  \end{equation}
  - If $\mathbf{g}^\top \mathbf{H} \mathbf{g} \le 0$, the function is concave along the gradient direction; increasing $\epsilon$ decreases $f$ indefinitely.
  - When $\mathbf{g}^\top \mathbf{H} \mathbf{g} > 0$, curvature limits the step size. If $\epsilon > \frac{2 \mathbf{g}^\top \mathbf{g}}{\mathbf{g}^\top \mathbf{H} \mathbf{g}}$, the update overshoots and diverges!

- **Ill-Conditioned Ravines & The Condition Number**:
  The condition number of the Hessian is the ratio of its largest to smallest eigenvalue:
  \begin{equation}
  \kappa = \frac{\lambda_{\max}(\mathbf{H})}{\lambda_{\min}(\mathbf{H})}.
  \label{eq:bengio_condition_number}
  \end{equation}
  When $\kappa \gg 1$, curvature is wildly asymmetric: gradient descent oscillates violently across the steep canyon walls while making negligible progress along the slow, gently sloping valley floor (Figure 4.5).

- **Saddle Points in High Dimensions (Figure 4.4 & Section 8.2)**:
  At a stationary point $\nabla f(\mathbf{x}) = \mathbf{0}$:
  - Local minimum: all eigenvalues $\lambda_i(\mathbf{H}) > 0$ (positive definite).
  - Local maximum: all eigenvalues $\lambda_i(\mathbf{H}) < 0$ (negative definite).
  - **Saddle point**: mixed eigenvalues ($\exists \lambda_i > 0, \lambda_j < 0$). In high-dimensional deep networks ($n \sim 10^7$), saddle points are exponentially more frequent than local minima because the probability that all $n$ random eigenvalues share the same positive sign is $2^{-n} \approx 0$.

---

### 3. Optimization vs. Learning & Surrogate Losses (Chapter 8)
- **Surrogate Loss Functions**:
  We evaluate machine learning performance using 0-1 classification error $\ell_{0\text{-}1}(\hat{y}, y) = \mathbb{I}\{\hat{y} \ne y\}$. However, the 0-1 loss is piecewise constant: its gradient is zero almost everywhere and undefined at the threshold!
  Gradient descent requires a smooth, continuous **surrogate loss function** (e.g. cross-entropy or negative log-likelihood) whose negative gradient acts as a reliable downhill guide.

- **Batch vs. Stochastic Gradient Descent (SGD)**:
  - Standard error of the sample mean scales as $\frac{\sigma}{\sqrt{B}}$ where $B$ is the mini-batch size. Moving from $B = 100$ to $B = 10,000$ increases computational cost by $100\times$ but only reduces estimator standard error by $10\times$.
  - Mini-batch SGD with $B \in [32, 256]$ provides an optimal Pareto frontier: fast matrix parallelization on GPUs/Apple Silicon while introducing stochastic gradient noise that helps escape saddle points.
