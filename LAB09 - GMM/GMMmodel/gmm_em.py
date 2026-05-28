import numpy as np
import scipy.special
from .gmm_core import compute_log_joint, apply_eigenvalue_constraint

def EM_algorithm(X, gmm_init, delta_l=1e-6, max_iter=100, psi=None):
    """
    Perform the EM algorithm to fit a GMM to the data.
        X: (D, N) matrix of samples
        gmm_init: Initial GMM parameters [(w1, mu1, C1), (w2, mu2, C2), ...]
        delta_l: Convergence threshold for log-likelihood improvement
        max_iter: Maximum number of iterations to prevent infinite loops
        psi: Eigenvalue constraint value
    Returns:
        gmm: Fitted GMM parameters after EM convergence
    """
    # 1. Initialize GMM parameters
    N = X.shape[1]
    gmm = gmm_init
    prev_log_likelihood = -np.inf

    for iteration in range(max_iter):
        # 2. E-step
        # Compute log-marginal probabilities
        S = compute_log_joint(X, gmm)
        log_marginal = scipy.special.logsumexp(S, axis=0)

        # Compute responsibilities (gamma) in log-space to avoid underflow
        log_gamma = S - log_marginal  # Shape: (M, N)
        gamma = np.exp(log_gamma)     # Shape: (M, N)

        # 3. M-step: Update parameters
        for g in range(len(gmm)):
            w, mu, C = gmm[g]
            gamma_g = gamma[g, :]  # Shape: (N,)
            sum_gamma_g = np.sum(gamma_g)

            # Update mean
            mu_new = ((X @ gamma_g) / sum_gamma_g).reshape(X.shape[0], 1)
            
            # Update covariance
            X_centered = X - mu_new
            C_new = (X_centered * gamma_g) @ X_centered.T / sum_gamma_g
            
            # Apply the eigenvalue constraint
            C_new = apply_eigenvalue_constraint(C_new, psi)
            
            # Update weight
            w_new = sum_gamma_g / N
            
            gmm[g] = (w_new, mu_new, C_new)

        # 4. Check for convergence
        log_likelihood = np.mean(log_marginal)
        if iteration > 0 and log_likelihood - prev_log_likelihood < delta_l:
            break
        
        prev_log_likelihood = log_likelihood
    
    return gmm

def EM_algorithm_diag(X, gmm_init, delta_l=1e-6, max_iter=100, psi=0.01):
    """EM algorithm for a GMM strictly using Diagonal Covariance matrices."""
    N = X.shape[1]
    gmm = gmm_init.copy()
    prev_log_likelihood = -np.inf

    for iteration in range(max_iter):
        # E-step
        S = compute_log_joint(X, gmm)
        log_marginal = scipy.special.logsumexp(S, axis=0)
        gamma = np.exp(S - log_marginal)

        # M-step
        for g in range(len(gmm)):
            _, _, _ = gmm[g] # Unpack just to iterate, we calculate fresh values
            gamma_g = gamma[g, :]
            sum_gamma_g = np.sum(gamma_g)

            mu_new = ((X @ gamma_g) / sum_gamma_g).reshape(X.shape[0], 1)
            
            X_centered = X - mu_new
            C_new = (X_centered * gamma_g) @ X_centered.T / sum_gamma_g
            
            w_new = sum_gamma_g / N
            
            # --- DIAGONAL SPECIFIC STEP ---
            # Zero out all non-diagonal elements
            C_new = C_new * np.eye(C_new.shape[0])
            
            # Apply eigenvalue constraint
            C_new = apply_eigenvalue_constraint(C_new, psi)
            
            gmm[g] = (w_new, mu_new, C_new)

        # Convergence Check
        log_likelihood = np.mean(log_marginal)
        if iteration > 0 and log_likelihood - prev_log_likelihood < delta_l:
            break
        prev_log_likelihood = log_likelihood
    
    return gmm

def EM_algorithm_tied(X, gmm_init, delta_l=1e-6, max_iter=100, psi=0.01):
    """EM algorithm for a GMM where all components share a Tied Covariance matrix."""
    N = X.shape[1]
    gmm = gmm_init.copy()
    prev_log_likelihood = -np.inf

    for iteration in range(max_iter):
        # E-step
        S = compute_log_joint(X, gmm)
        log_marginal = scipy.special.logsumexp(S, axis=0)
        gamma = np.exp(S - log_marginal)

        # M-step
        new_gmm_temp = []
        tied_C = np.zeros((X.shape[0], X.shape[0]))

        # First pass: calculate means, weights, and accumulate the tied covariance
        for g in range(len(gmm)):
            gamma_g = gamma[g, :]
            sum_gamma_g = np.sum(gamma_g)

            mu_new = ((X @ gamma_g) / sum_gamma_g).reshape(X.shape[0], 1)
            X_centered = X - mu_new
            C_new = (X_centered * gamma_g) @ X_centered.T / sum_gamma_g
            w_new = sum_gamma_g / N
            
            # --- TIED SPECIFIC STEP (Accumulation) ---
            tied_C += w_new * C_new
            
            new_gmm_temp.append((w_new, mu_new))

        # --- TIED SPECIFIC STEP (Application & Constraint) ---
        tied_C = apply_eigenvalue_constraint(tied_C, psi)

        # Second pass: assign the shared covariance to all components
        for g in range(len(new_gmm_temp)):
            w_new, mu_new = new_gmm_temp[g]
            gmm[g] = (w_new, mu_new, tied_C)

        # Convergence Check
        log_likelihood = np.mean(log_marginal)
        if iteration > 0 and log_likelihood - prev_log_likelihood < delta_l:
            break
        prev_log_likelihood = log_likelihood
    
    return gmm