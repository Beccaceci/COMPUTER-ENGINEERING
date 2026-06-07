import numpy as np
import scipy.special
import numpy.linalg

def apply_eigenvalue_constraint(C, psi):
    """
    Applies a lower bound (psi) to the eigenvalues of covariance matrix C to prevent degenerate solutions.
    """
    if psi is None:
        return C
    
    U, s, _ = np.linalg.svd(C)
    s[s < psi] = psi
    
    # Efficiently compute U @ S_new @ U^T using broadcasting
    return U @ (s[:, np.newaxis] * U.T)

def logpdf_GAU_ND(X, mu, C):
    """
    Computes the log-density of a Multivariate Gaussian.
        X: (D, N) matrix of samples
        mu: (D, 1) column vector of the mean
        C: (D, D) covariance matrix
    Returns:
        log_pdf: (N,) vector of log-densities for each sample
    """
    D, N = X.shape
    
    # Compute log-determinant of C safely
    sign, log_det_C = np.linalg.slogdet(C)
    
    # Center the data
    X_centered = X - mu
    
    # Compute the Mahalanobis distance term: (X-mu)^T * C^-1 * (X-mu)
    # np.linalg.solve(C, X_centered) efficiently computes C^-1 * (X-mu)
    invC_X = np.linalg.solve(C, X_centered)
    
    # We want the diagonal of (X-mu)^T * invC_X. 
    # Element-wise multiplication and summing over axis 0 does exactly this for all N samples.
    mahalanobis_dist = np.sum(X_centered * invC_X, axis=0)
    
    # Final formula
    log_pdf = -0.5 * D * np.log(2 * np.pi) - 0.5 * log_det_C - 0.5 * mahalanobis_dist
    
    return log_pdf

def compute_log_joint(X, gmm):
    """
    Helper function to compute the log-joint matrix S
    Parameters:
        X: (D, N) matrix of samples
        gmm: List of tuples [(w1, mu1, C1), (w2, mu2, C2), ...]
    Returns:
        S: (M, N) matrix of log-joint probabilities for each sample under each Gaussian component
    """
    M = len(gmm) # num of gaussians
    N = X.shape[1] # num of samples
    S = np.zeros((M, N))

    # Compute the log-joint probabilities
    for g in range(M): # loop over gaussians
        w, mu, C = gmm[g] # get weights, means, and covariances
        
        # Calculate log-conditional probability
        log_conditional = logpdf_GAU_ND(X, mu, C)
        
        # Add log-prior (log w) to get log-joint
        S[g, :] = log_conditional + np.log(w)
    
    return S

def logpdf_GMM(X, gmm):
    """
    Compute the log-density of a GMM.
        X: (D, N) matrix of samples
        gmm: List of tuples [(w1, mu1, C1), (w2, mu2, C2), ...]
    Returns:
        log_marginal: (N,) vector of log-densities for each sample under the GMM
    """
    # Compute the log-joint matrix S
    S = compute_log_joint(X, gmm)

    # Compute the log-marginal probabilities using logsumexp along axis 0
    log_marginal = scipy.special.logsumexp(S, axis=0)
    
    return log_marginal