# Machine Learning (`01URWOV` / `01URWYG`)

[![Politecnico di Torino](https://img.shields.io/badge/University-Politecnico%20di%20Torino-002D62.svg?style=flat&logo=buffer&logoColor=white)](https://www.polito.it/)
[![Course](https://img.shields.io/badge/Course-Machine%20Learning-blue.svg?style=flat)](https://didattica.polito.it/)
[![Degree](https://img.shields.io/badge/Master's%20Degree-Computer%20Engineering%20(LM--32)-FF8C00?style=flat)](https://didattica.polito.it/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Practical laboratory implementations, algorithms developed from scratch in Python, and comprehensive technical laboratory reports for the Master's degree course in **Machine Learning** at **Politecnico di Torino** (A.Y. 2025/2026).

---

## ⚡ Direct 1-Click PDF Downloads

Download each laboratory report and official problem statement directly with one click:

| Laboratory | Topic / Content | Direct PDF Report | Problem Statement |
| :--- | :--- | :---: | :---: |
| **LAB 01** | Python Numerical Libraries (NumPy, SciPy, Matplotlib) | — *(Practical onboarding)* | [📄 lab01_text.pdf](LAB01%20-%20PYTHON%20NUMERICAL%20LIBS/lab01_text-PythonNumericalLibraries.pdf) |
| **LAB 02** | Iris Dataset (Exploration & Fisher Features) | [📊 lab02_report.pdf](LAB02%20-%20IRIS%20DATASET/report/lab02_report.pdf) | [📄 lab02_text.pdf](LAB02%20-%20IRIS%20DATASET/lab02_text-IrisDataset.pdf) |
| **LAB 03** | Dimensionality Reduction (PCA & LDA from Scratch) | [📊 lab03_report.pdf](LAB03%20-%20DIMENSIONALITY%20REDUCTION/report/lab03_report-DimensionalityReduction.pdf) | [📄 lab03_text.pdf](LAB03%20-%20DIMENSIONALITY%20REDUCTION/lab03_text-DimensionalityReduction.pdf) |
| **LAB 04** | Probability & Density Estimation (Multivariate Gaussian) | [📊 lab04_report.pdf](LAB04%20-%20PROBABILITY%20AND%20DENSITY%20ESTIMATION/report/lab04_report-DensityEstimation.pdf) | [📄 lab04_text.pdf](LAB04%20-%20PROBABILITY%20AND%20DENSITY%20ESTIMATION/lab04_text-ProbabilityAndDensityEstimation.pdf) |
| **LAB 05** | Generative Gaussian Classifiers (MVG, Naive Bayes, Tied) | [📊 lab05_report.pdf](LAB05%20-%20GENERATIVE%20GAUSSIAN%20MODELS/report/lab05_report.pdf) | [📄 lab05_text.pdf](LAB05%20-%20GENERATIVE%20GAUSSIAN%20MODELS/lab05_text-GenerativeGaussianModels.pdf) |
| **LAB 06** | Bayes Risk, Detection Cost Function (DCF) & Model Evaluation | [📊 lab06_report.pdf](LAB06%20-%20BAYES%20RISK%20AND%20MODEL%20EVALUATION/report/lab_06-report.pdf) | [📄 lab06_text.pdf](LAB06%20-%20BAYES%20RISK%20AND%20MODEL%20EVALUATION/lab06_text-BayesRiskAndModelEvaluation.pdf) |
| **LAB 07** | Logistic Regression (Binary, Multiclass, Regularization) | [📊 lab07_report.pdf](LAB07%20-%20LOGISTIC%20REGRESSION/report/lab_07-report.pdf) | [📄 lab07_text.pdf](LAB07%20-%20LOGISTIC%20REGRESSION/lab07_text-LogisticRegression.pdf) |
| **LAB 08** | Support Vector Machines (Linear, Polynomial & RBF Kernels) | [📊 lab08_report.pdf](LAB08%20-%20SUPPORT%20VECTOR%20MACHINES/report/lab08_report-SVM.pdf) | [📄 lab08_text.pdf](LAB08%20-%20SUPPORT%20VECTOR%20MACHINES/lab08_text-SVM.pdf) |
| **LAB 09** | Gaussian Mixture Models (EM & LBG Algorithms) | [📊 lab09_report.pdf](LAB09%20-%20GMM/report/lab09_report-GMM.pdf) | [📄 lab09_text.pdf](LAB09%20-%20GMM/lab09_text-GMM.pdf) |
| **LAB 10** | Score Calibration & Multi-System Fusion | [📊 lab10_report.pdf](LAB10%20-%20CALIBRATION%20FUSION/report/lab10_report-Calibration_Fusion.pdf) | [📄 lab10_text.pdf](LAB10%20-%20CALIBRATION%20FUSION/lab10_text-Calibration_fusion.pdf) |
| **Benchmark** | Full Model Evaluation Benchmark ($\pi = 0.1$) | [📈 model_evaluation_pi_0_1.pdf](model_evaluation_pi_0_1.pdf) | — |

---

# Repository Structure

```text
MACHINE_LEARNING/
│
├── LAB01 - PYTHON NUMERICAL LIBS
├── LAB02 - IRIS DATASET
│   └── report/
├── LAB03 - DIMENSIONALITY REDUCTION
│   └── report/
├── LAB04 - PROBABILITY AND DENSITY ESTIMATION
│   └── report/
├── LAB05 - GENERATIVE GAUSSIAN MODELS
│   └── report/
├── LAB06 - BAYES RISK AND MODEL EVALUATION
│   └── report/
├── LAB07 - LOGISTIC REGRESSION
│   └── report/
├── LAB08 - SUPPORT VECTOR MACHINES
│   └── report/
├── LAB09 - GMM
│   └── report/
├── LAB10 - CALIBRATION FUSION
│   └── report/
│
├── model_evaluation_pi_0_1.pdf
├── publish_labs.sh
└── README.md
```

---

# Labs Overview

## LAB01 — Python Numerical Libraries
Introduction to the Python scientific computing ecosystem:
- NumPy vectorized routines and broadcasting
- SciPy linear algebra
- Matplotlib plotting standards
- Matrix operations and numerical precision

---

## LAB02 — Iris Dataset
Exploration, statistical analysis, and visualization of the classic Iris benchmark:
- Dataset normalization and preprocessing
- Statistical feature variance and covariance
- Pairwise feature scatter plots and distributions
- Basic distance-based classification concepts

---

## LAB03 — Dimensionality Reduction
Mathematical derivations and pure Python implementations:
- **Principal Component Analysis (PCA)**: Spectral decomposition, covariance calculation, and variance preservation
- **Linear Discriminant Analysis (LDA)**: Between-class ($S_B$) and within-class ($S_W$) scatter optimization
- Lower-dimensional manifold projection and separation quality

---

## LAB04 — Probability and Density Estimation
Statistical modeling and maximum likelihood estimation:
- Multivariate Gaussian probability density function (PDF)
- Maximum Likelihood Estimation (MLE) of $\mu$ and $\Sigma$
- Log-likelihood optimization and log-sum-exp numerical stabilization

---

## LAB05 — Generative Gaussian Models
Complete implementations of generative classification frameworks:
- **Full Multivariate Gaussian (MVG)**: Class-specific covariance matrices
- **Naive Bayes Gaussian**: Diagonal covariance constraints
- **Tied Covariance Models**: Shared covariance structure across classes
- Log-domain posterior probabilities calculation

---

## LAB06 — Bayes Risk and Model Evaluation
Decision theory and performance metrics under asymmetric costs:
- Minimum Bayes Risk decisions and optimal thresholding
- Empirical and normalized **Detection Cost Function (DCF)**
- ROC / DET curves and confusion matrices
- Minimum DCF vs. Actual DCF analysis

---

## LAB07 — Logistic Regression
Discriminative linear models solved via numerical optimization:
- Binary Logistic Regression with $L_2$ regularization
- Multiclass Logistic Regression
- Numerical optimization with `scipy.optimize.fmin_l_bfgs_b`
- Score calibration and decision boundary visualization

---

## LAB08 — Support Vector Machines
Constrained quadratic programming formulation and dual representation:
- Dual formulation optimization with box constraints
- Linear SVM
- Kernel Trick: Polynomial and Radial Basis Function (RBF) kernels
- Hyperparameter tuning ($C$ and $\gamma$) and support vectors geometry

---

## LAB09 — Gaussian Mixture Models (GMM)
Non-parametric probabilistic clustering and density estimation:
- Expectation-Maximization (EM) algorithm implementation
- Linde-Buzo-Gray (LBG) hierarchical component-splitting algorithm
- Diagonal and tied covariance adaptations for Gaussian components

---

## LAB10 — Calibration Fusion
Score-level fusion and post-processing:
- Score calibration via unweighted and weighted logistic regression
- Multi-system fusion combining scores from generative and discriminative models
- System validation across operating conditions

---

# Requirements & Environment

Developed and tested using Python 3:

```bash
python >= 3.10
```

Required packages:

```bash
pip install numpy scipy matplotlib scikit-learn
```

---

# Author

**Nicola Beccaceci**  
MSc Computer Engineering — Politecnico di Torino