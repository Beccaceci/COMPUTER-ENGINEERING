import numpy
import scipy.optimize

from utils.bayes_utils import compute_min_dcf, compute_normalised_empirical_Bayes_risk_binary

# =========================
# Function for linear SVM =
# =========================

def train_linear_svm(DTR, LTR, C, K=1.0):
    """
    Trains a Linear SVM using the dual formulation with L-BFGS-B.
    
    Parameters:
        DTR: Training data matrix (Features, Samples)
        LTR: Training labels encoded as {-1, 1}
        C: Regularization hyperparameter
        K: Bias extension factor
        
    Returns:
        w_hat_star: The optimized extended weight vector
        J_primal: The primal objective loss
        J_dual: The dual objective loss
        duality_gap: The gap between primal and dual loss
    """
    # 1. Extend the training matrix with the bias term K
    row_tr = numpy.ones((1, DTR.shape[1])) * K
    DTR_ext = numpy.vstack([DTR, row_tr])
    
    # 2. Precompute the H matrix
    G = DTR_ext.T @ DTR_ext
    H = (LTR.reshape(-1, 1) * LTR.reshape(1, -1)) * G

    # 3. Define the dual objective and its gradient
    def L_dual(alpha):
        term1 = 0.5 * (alpha.T @ H @ alpha)
        term2 = alpha.sum()
        
        Ld = term1 - term2
        Ld_grad = (H @ alpha) - numpy.ones(alpha.shape[0])
        
        return Ld, Ld_grad.ravel()

    # 4. Run L-BFGS-B optimizer
    bounds = [(0, C)] * DTR_ext.shape[1]
    alpha_opt, min_Ld, info = scipy.optimize.fmin_l_bfgs_b(
        func=L_dual,
        x0=numpy.zeros(DTR_ext.shape[1]),
        bounds=bounds,
        factr=numpy.nan,  # High precision
        pgtol=1e-5        # High precision
    )

    # 5. Recover primal weights
    w_hat_star = DTR_ext @ (alpha_opt * LTR)

    # 6. Compute primal loss and duality gap
    S = w_hat_star.T @ DTR_ext
    hinge_losses = numpy.maximum(0, 1 - LTR * S)
    J_primal = 0.5 * numpy.linalg.norm(w_hat_star)**2 + C * hinge_losses.sum()
    
    J_dual = -min_Ld
    duality_gap = J_primal - J_dual

    return w_hat_star, J_primal, J_dual, duality_gap

def evaluate_linear_svm(DTE, LTE, w_hat_star, K=1.0, pi=0.5, Cfn=1.0, Cfp=1.0):
    """
    Scores the test set and evaluates the SVM performance.
    """
    # 1. Extend test matrix
    row_te = numpy.ones((1, DTE.shape[1])) * K
    DTE_ext = numpy.vstack([DTE, row_te])
    
    # 2. Compute scores
    scores = w_hat_star.T @ DTE_ext
    
    # 3. Map labels and predictions to {0, 1} for evaluation utilities
    # LTE is currently {-1, 1}, so (LTE > 0) casts them to {0, 1}
    LTE_binary = (LTE > 0).astype(int)
    predictions = (scores > 0).astype(int)  # SVM threshold is 0
    
    # 4. Compute error rate
    error_rate = 1.0 - numpy.mean(predictions == LTE_binary)
    
    # 5. Compute minDCF
    min_dcf = compute_min_dcf(scores, LTE_binary, pi, Cfn, Cfp)
    
    # 6. Compute actDCF 
    # Build a binary confusion matrix (M[predicted, true])
    M = numpy.zeros((2, 2), dtype=int)
    for p, t in zip(predictions, LTE_binary):
        M[p, t] += 1
        
    act_dcf = compute_normalised_empirical_Bayes_risk_binary(M, pi, Cfn, Cfp)
    
    return error_rate, min_dcf, act_dcf
