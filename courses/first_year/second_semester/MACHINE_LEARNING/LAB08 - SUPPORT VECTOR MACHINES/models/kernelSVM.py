import numpy
import scipy.optimize

from utils.bayes_utils import compute_min_dcf, compute_normalised_empirical_Bayes_risk_binary
from utils.math_utils import polynomial_kernel, radial_basis_kernel

# =========================
# Function for kernel SVM =
# =========================

def train_kernel_svm(DTR, LTR, C, K_bias, kernel_type="poly", **kwargs):
    """
    Trains a Kernel SVM. Returns the optimal dual variables (alpha) instead of w.
    Parameters:
        DTR: Training data matrix (Features, Samples)
        LTR: Training labels encoded as {-1, 1}
        C: Regularization hyperparameter
        K_bias: Bias extension factor for kernel SVM
        kernel_type: 'poly' for polynomial kernel, 'rbf' for RBF kernel
        **kwargs: Additional parameters for the kernel function (e.g., degree d for poly, gamma for rbf)
    Returns:
        alpha_opt: Optimal dual variables
        J_primal: Primal loss
        J_dual: Dual loss
        duality_gap: Duality gap
    """
    # 1. Compute kernel matrix and H
    if kernel_type == "poly":
        K_mat = polynomial_kernel(DTR, DTR, d=kwargs.get('d', 2), c=kwargs.get('c', 1)) + K_bias**2
    elif kernel_type == "rbf":
        K_mat = radial_basis_kernel(DTR, DTR, gamma=kwargs.get('gamma', 1.0)) + K_bias**2
    else:
        raise ValueError("Unsupported kernel type. Use 'poly' or 'rbf'.")
    
    # Kernel matrix multiplied by label outer product (label correlation)
    H = (LTR.reshape(-1, 1) * LTR.reshape(1, -1)) * K_mat

    # 2. Define the dual objective
    def L_dual(alpha):
        Ha = H @ alpha # Kernel matrix multiplied by dual variables
        Ld = 0.5 * (alpha @ Ha) - alpha.sum() # Dual loss function
        Ld_grad = Ha - numpy.ones(alpha.shape[0]) # Gradient of the dual loss
        return Ld, Ld_grad.ravel()

    # 3. Optimize
    bounds = [(0, C)] * DTR.shape[1] # Bounds for the dual variables: 0 <= alpha_i <= C
    alpha_opt, min_Ld, info = scipy.optimize.fmin_l_bfgs_b( # L-BFGS-B is a quasi-Newton method for large-scale bound-constrained optimization
        func=L_dual, # Objective function
        x0=numpy.zeros(DTR.shape[1]), # Initial guess for alpha
        bounds=bounds, # Bounds for alpha
        factr=numpy.nan, # High precision
        pgtol=1e-5 # High precision
    )

    # 4. Compute Losses
    J_dual = -min_Ld # Dual loss is the negative of the minimum value found by the optimizer
    
    # Primal loss trick: J_primal = 0.5 * a^T H a + C * sum(max(0, 1 - H_i a))
    Ha = H @ alpha_opt # Kernel matrix multiplied by dual variables
    J_primal = 0.5 * (alpha_opt @ Ha) + C * numpy.maximum(0, 1 - Ha).sum() # Primal loss function
    
    duality_gap = J_primal - J_dual # Duality gap

    return alpha_opt, J_primal, J_dual, duality_gap

def evaluate_kernel_svm(DTR, LTR, DTE, LTE, alpha_opt, K_bias, kernel_type, pi=0.5, Cfn=1.0, Cfp=1.0, **kwargs):
    """
    Scores the test set using the support vectors (alpha) and the kernel function.
    Parameters:
        DTR: Training data matrix (Features, Samples)
        LTR: Training labels encoded as {-1, 1}
        DTE: Test data matrix (Features, Samples)
        LTE: Test labels encoded as {-1, 1}
        alpha_opt: Optimal dual variables from training
        K_bias: Bias extension factor for kernel SVM
        kernel_type: 'poly' or 'rbf'
        pi, Cfn, Cfp: Parameters for DCF evaluation
    Returns:
        error_rate: Classification error rate on the test set
        min_dcf: Minimum DCF computed from scores
        act_dcf: Actual DCF computed from predictions
    """
    # 1. Compute kernel matrix and H
    if kernel_type == "poly":
        K_test = polynomial_kernel(DTR, DTE, d=kwargs.get('d', 2), c=kwargs.get('c', 1)) + K_bias**2
    elif kernel_type == "rbf":
        K_test = radial_basis_kernel(DTR, DTE, gamma=kwargs.get('gamma', 1.0)) + K_bias**2
    else:
        raise ValueError("Unsupported kernel type. Use 'poly' or 'rbf'.")
    
    # 2. Compute scores: s(x_t) = sum(alpha_i * z_i * k(x_i, x_t))
    scores = (alpha_opt * LTR) @ K_test
    
    # 3. Evaluate Metrics
    LTE_binary = (LTE > 0).astype(int)
    predictions = (scores > 0).astype(int)
    
    # Compute error rate
    error_rate = 1.0 - numpy.mean(predictions == LTE_binary)
    
    # Compute minimum DCF
    min_dcf = compute_min_dcf(scores, LTE_binary, pi, Cfn, Cfp)
    
    # Compute actual DCF
    M = numpy.zeros((2, 2), dtype=int)
    for p, t in zip(predictions, LTE_binary):
        M[p, t] += 1
    act_dcf = compute_normalised_empirical_Bayes_risk_binary(M, pi, Cfn, Cfp)
    
    return error_rate, min_dcf, act_dcf