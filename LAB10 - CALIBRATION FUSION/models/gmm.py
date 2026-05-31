import numpy as np
import scipy.special

def apply_eigenvalue_constraint(C, psi):
    """
    Applies a lower bound (psi) to the eigenvalues of covariance matrix C to prevent degenerate solutions.
    """
    if psi is None:
        return C
    
    U, s, _ = np.linalg.svd(C)
    s[s < psi] = psi
    
    return U @ (s[:, np.newaxis] * U.T)

def logpdf_GAU_ND(X, mu, C):
    """
    Computes the log-density of a Multivariate Gaussian.
    """
    D, N = X.shape
    sign, log_det_C = np.linalg.slogdet(C)
    X_centered = X - mu
    invC_X = np.linalg.solve(C, X_centered)
    mahalanobis_dist = np.sum(X_centered * invC_X, axis=0)
    log_pdf = -0.5 * D * np.log(2 * np.pi) - 0.5 * log_det_C - 0.5 * mahalanobis_dist
    return log_pdf

def compute_log_joint(X, gmm):
    """
    Helper function to compute the log-joint matrix S
    """
    M = len(gmm)
    N = X.shape[1]
    S = np.zeros((M, N))

    for g in range(M):
        w, mu, C = gmm[g]
        log_conditional = logpdf_GAU_ND(X, mu, C)
        S[g, :] = log_conditional + np.log(w)
    
    return S

def EM_algorithm_tied(X, gmm_init, delta_l=1e-6, max_iter=100, psi=0.01):
    """EM algorithm for a GMM where all components share a Tied Covariance matrix."""
    N = X.shape[1]
    gmm = gmm_init.copy()
    prev_log_likelihood = -np.inf

    for iteration in range(max_iter):
        S = compute_log_joint(X, gmm)
        log_marginal = scipy.special.logsumexp(S, axis=0)
        gamma = np.exp(S - log_marginal)

        new_gmm_temp = []
        tied_C = np.zeros((X.shape[0], X.shape[0]))

        for g in range(len(gmm)):
            gamma_g = gamma[g, :]
            sum_gamma_g = np.sum(gamma_g)

            mu_new = ((X @ gamma_g) / sum_gamma_g).reshape(X.shape[0], 1)
            X_centered = X - mu_new
            C_new = (X_centered * gamma_g) @ X_centered.T / sum_gamma_g
            w_new = sum_gamma_g / N
            
            tied_C += w_new * C_new
            new_gmm_temp.append((w_new, mu_new))

        tied_C = apply_eigenvalue_constraint(tied_C, psi)

        for g in range(len(new_gmm_temp)):
            w_new, mu_new = new_gmm_temp[g]
            gmm[g] = (w_new, mu_new, tied_C)

        log_likelihood = np.mean(log_marginal)
        if iteration > 0 and log_likelihood - prev_log_likelihood < delta_l:
            break
        prev_log_likelihood = log_likelihood
    
    return gmm

def LBG_algorithm_tied(GMM, alpha=0.1, psi=0.01):
    """LBG split for Tied Covariances."""
    new_GMM = []
    
    for w, mu, C in GMM:
        U, s, _ = np.linalg.svd(C)
        epsilon = U[:, 0:1] * s[0]**0.5 * alpha
        
        mu_plus = mu + epsilon
        mu_minus = mu - epsilon
        w_new = w / 2
        
        C_constrained = apply_eigenvalue_constraint(C, psi)
        
        new_GMM.append((w_new, mu_plus, C_constrained))
        new_GMM.append((w_new, mu_minus, C_constrained))
        
    return new_GMM

def train_gmm_lbg(X, n_components, LBG_split_func, EM_func, psi=0.01):
    """
    Trains a Gaussian Mixture Model using the LBG algorithm.
    """
    mu = X.mean(axis=1, keepdims=True)
    C = np.cov(X, bias=True)
    C = apply_eigenvalue_constraint(C, psi)
    gmm = [(1.0, mu, C)]
    
    gmm = EM_func(X, gmm, psi=psi)
    
    current_c = 1
    while current_c < n_components:
        gmm = LBG_split_func(gmm, psi=psi)
        gmm = EM_func(X, gmm, psi=psi)
        current_c *= 2
        
    return gmm


def train_and_eval_project_gmm(DTR_centered, LTR, DVAL_centered, D_eval_centered):
    """
    Trains the Tied GMM model for the project part and evaluates it.
    Returns:
        s_val_gmm: scores on validation set
        s_eval_gmm: scores on evaluation set
    """
    gmm0 = train_gmm_lbg(DTR_centered[:, LTR == 0], 8, LBG_algorithm_tied, EM_algorithm_tied)
    gmm1 = train_gmm_lbg(DTR_centered[:, LTR == 1], 8, LBG_algorithm_tied, EM_algorithm_tied)
    
    S0_val = scipy.special.logsumexp(compute_log_joint(DVAL_centered, gmm0), axis=0)
    S1_val = scipy.special.logsumexp(compute_log_joint(DVAL_centered, gmm1), axis=0)
    s_val_gmm = S1_val - S0_val
    
    S0_eval = scipy.special.logsumexp(compute_log_joint(D_eval_centered, gmm0), axis=0)
    S1_eval = scipy.special.logsumexp(compute_log_joint(D_eval_centered, gmm1), axis=0)
    s_eval_gmm = S1_eval - S0_eval
    
    return s_val_gmm, s_eval_gmm
