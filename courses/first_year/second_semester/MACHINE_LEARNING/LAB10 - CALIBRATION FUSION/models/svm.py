import numpy as np
import scipy.optimize
from utils.math_utils import radial_basis_kernel

def train_kernel_svm(DTR, LTR, C, K_bias, kernel_type="rbf", **kwargs):
    """
    Trains a Kernel SVM. Returns the optimal dual variables (alpha) instead of w.
    Parameters:
        DTR: Training data matrix (Features, Samples)
        LTR: Training labels encoded as {-1, 1}
        C: Regularization hyperparameter
        K_bias: Bias extension factor for kernel SVM
        kernel_type: 'rbf' for RBF kernel
        **kwargs: Additional parameters for the kernel function (e.g., gamma for rbf)
    Returns:
        alpha_opt: Optimal dual variables
        J_primal: Primal loss
        J_dual: Dual loss
        duality_gap: Duality gap
    """
    if kernel_type == "rbf":
        K_mat = radial_basis_kernel(DTR, DTR, gamma=kwargs.get('gamma', 1.0)) + K_bias**2
    else:
        raise ValueError("Unsupported kernel type. Use 'rbf' for the project.")
    
    H = (LTR.reshape(-1, 1) * LTR.reshape(1, -1)) * K_mat

    def L_dual(alpha):
        Ha = H @ alpha
        Ld = 0.5 * (alpha @ Ha) - alpha.sum()
        Ld_grad = Ha - np.ones(alpha.shape[0])
        return Ld, Ld_grad.ravel()

    bounds = [(0, C)] * DTR.shape[1]
    alpha_opt, min_Ld, info = scipy.optimize.fmin_l_bfgs_b(
        func=L_dual,
        x0=np.zeros(DTR.shape[1]),
        bounds=bounds,
        factr=np.nan,
        pgtol=1e-5
    )

    J_dual = -min_Ld
    Ha = H @ alpha_opt
    J_primal = 0.5 * (alpha_opt @ Ha) + C * np.maximum(0, 1 - Ha).sum()
    duality_gap = J_primal - J_dual

    return alpha_opt, J_primal, J_dual, duality_gap


def train_and_eval_project_svm(DTR_centered, LTR, DVAL_centered, D_eval_centered):
    """
    Trains the Kernel SVM model for the project part and evaluates it.
    Returns:
        s_val_svm: scores on validation set
        s_eval_svm: scores on evaluation set
    """
    ZTR = LTR * 2 - 1

    # Train Kernel SVM model with RBF kernel for the project part and evaluate it.
    # Returns scores on validation and evaluation sets
    alpha_opt, _, _, _ = train_kernel_svm(DTR_centered, ZTR, C=1.0, K_bias=1.0, kernel_type="rbf", gamma=1e-2)
    
    # Apply model to validation and evaluation sets
    K_val = radial_basis_kernel(DTR_centered, DVAL_centered, gamma=1e-2) + 1.0
    s_val_svm = ((alpha_opt * ZTR) @ K_val).ravel()
    
    # Apply model to evaluation set
    K_eval = radial_basis_kernel(DTR_centered, D_eval_centered, gamma=1e-2) + 1.0
    s_eval_svm = ((alpha_opt * ZTR) @ K_eval).ravel()
    
    return s_val_svm, s_eval_svm
