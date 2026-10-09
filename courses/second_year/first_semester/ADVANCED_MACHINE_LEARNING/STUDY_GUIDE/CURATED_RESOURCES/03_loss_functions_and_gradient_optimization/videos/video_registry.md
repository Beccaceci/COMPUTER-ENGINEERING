# Curated Video Lectures for Lecture 3: Numerical Optimization & Gradient Descent

This registry stages key video breakdowns from top pedagogical creators that enrich Lecture 3.

---

## 1. 3Blue1Brown (Grant Sanderson)
- **Title**: *Gradient Descent, How Neural Networks Learn* (Chapter 2, Neural Networks)
- **Link**: [https://www.youtube.com/watch?v=IHZwWFHWa-w](https://www.youtube.com/watch?v=IHZwWFHWa-w)
- **Role in AML**: Geometric visualization of gradient vectors in high-dimensional parameter spaces. Explains why the gradient $\nabla C(\mathbf{w})$ points in the direction of steepest increase, and why stepping along $-\nabla C(\mathbf{w})$ ensures local loss minimization.
- **Key Exam Takeaway**:
  - The gradient is a vector of partial derivatives: $\nabla C = \left[\frac{\partial C}{\partial w_1}, \dots, \frac{\partial C}{\partial w_n}\right]^\top$.
  - Magnitude of the gradient indicates slope steepness; direction indicates steepest ascent.

- **Title**: *Multivariable Calculus: The Directional Derivative and the Gradient*
- **Link**: [https://www.youtube.com/watch?v=te963P2sWzQ](https://www.youtube.com/watch?v=te963P2sWzQ)
- **Role in AML**: Rigorous mathematical proof that the dot product $\mathbf{u}^\top \nabla f(\mathbf{x})$ is maximized when unit vector $\mathbf{u}$ is collinear with the gradient vector.

---

## 2. Andrej Karpathy
- **Title**: *CS231n Lecture 3: Loss Functions and Optimization (Stanford University)*
- **Link**: [https://www.youtube.com/watch?v=h7iBpEHGVNc](https://www.youtube.com/watch?v=h7iBpEHGVNc)
- **Role in AML**: Direct source credit for Slide 23 of `03-AMLGradientDescend.pdf`.
- **Key Oral Insights**:
  - Comparison between Multiclass SVM Hinge loss and Softmax Cross-Entropy loss.
  - Step size / learning rate hyperparameter tuning: why too small leads to glacial convergence and too large leads to catastrophic divergence.
  - Mini-batch SGD: computing gradients over small subsets of training data to approximate full-batch gradient cheaply.

---

## 3. Enkk
- **Title**: *Inside the Loss Landscape: Ravines, Saddle Points, and Second-Order Curvature*
- **Link**: [https://www.youtube.com/watch?v=8VzG1M0d7qA](https://www.youtube.com/watch?v=8VzG1M0d7qA)
- **Role in AML**: Visual demonstration of ill-conditioned Hessian ravines and why standard gradient descent bounces from wall to wall.
