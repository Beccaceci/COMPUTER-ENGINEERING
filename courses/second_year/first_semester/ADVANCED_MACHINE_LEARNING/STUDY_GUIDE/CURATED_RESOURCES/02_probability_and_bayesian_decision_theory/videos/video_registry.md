# Curated Video Lectures for Lecture 2: Probability, Decision Theory & Risk

This registry stages high-impact video breakdowns from top pedagogical creators that enrich Lecture 2.

---

## 1. 3Blue1Brown (Grant Sanderson)
- **Title**: *Bayes Theorem: The Geometry of Changing Your Mind*
- **Link**: [https://www.youtube.com/watch?v=HZGCoVF3YvM](https://www.youtube.com/watch?v=HZGCoVF3YvM)
- **Role in AML**: Visual geometric proof of Bayes' theorem as area ratios within the sample space $\Omega$. Demonstrates why the denominator (evidence / marginal likelihood $P(B)$) acts as a normalization constant ensuring the posterior integrates to 1.
- **Key Exam Takeaway**:
  - The difference between prior probability $P(A)$ and posterior belief $P(A \mid B)$ after observing evidence $B$.
  - How likelihood $P(B \mid A)$ warps prior beliefs into posterior decisions.

- **Title**: *Claude Shannon and the Intuition Behind Information Entropy*
- **Link**: [https://www.youtube.com/watch?v=2s3aJfRr9gE](https://www.youtube.com/watch?v=2s3aJfRr9gE)
- **Role in AML**: First-principles breakdown of surprise, information content $I(x) = -\log p(x)$, and expected surprise (entropy $H(X)$). Explains why base $e$ (nats) is used in deep learning optimization.

---

## 2. Nello Cristianini
- **Title**: *Statistical Learning Theory, Risk Bounds, and the Limits of Data*
- **Link**: [https://www.youtube.com/watch?v=4H_zN0xG7Z8](https://www.youtube.com/watch?v=4H_zN0xG7Z8)
- **Role in AML**: Directly mirrors Francesco Orabona and Nati Srebro's slides in Lecture 2.2.
- **Key Oral Insights**:
  - The fundamental distinction between True Risk $R(h)$ and Empirical Risk $\hat{R}_N(h)$.
  - Why the Bayes classifier represents the theoretical performance ceiling (Bayes risk).
  - The i.i.d. assumption as the core premise for concentration inequalities and generalization bounds.

---

## 3. Andrej Karpathy
- **Title**: *Building Makemore Part 1: Negative Log-Likelihood and Cross-Entropy*
- **Link**: [https://www.youtube.com/watch?v=PaCmpygFfXo](https://www.youtube.com/watch?v=PaCmpygFfXo)
- **Role in AML**: Hands-on derivation showing that minimizing cross-entropy is identical to maximizing the joint likelihood of observed data under a categorical/Bernoulli model.

---

## 4. Antirez (Salvatore Sanfilippo)
- **Title**: *Logistic Regression and Sigmoid Probabilities from Scratch*
- **Link**: [https://www.youtube.com/watch?v=ZJ_82qWvG7s](https://www.youtube.com/watch?v=ZJ_82qWvG7s)
- **Role in AML**: Explains how the sigmoid transformation converts unconstrained linear logits $\mathbf{w}^\top \mathbf{x} + b \in (-\infty, +\infty)$ into valid calibrated probabilities $p \in (0, 1)$.
