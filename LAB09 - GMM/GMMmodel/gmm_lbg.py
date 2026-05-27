import numpy as np
from .gmm_core import apply_eigenvalue_constraint

def LBG_algorithm (GMM, alpha=0.1, psi=None):
    """
    Perform the Linde-Buzo-Gray (LBG) algorithm to split each Gaussian component in the GMM.
        GMM: List of tuples [(w1, mu1, C1), (w2, mu2, C2), ...]
    Returns:
        new_GMM: List of tuples with doubled number of components after splitting
    """
    new_GMM = []
    for w, mu, C in GMM:
        # Create two new components by perturbing the mean
        U, s, Vh = np.linalg.svd(C)
        epsilon = U[:, 0:1] * s[0]**0.5 * alpha
        mu_minus = mu - epsilon
        mu_plus = mu + epsilon
        
        # Each new component gets half the weight of the original
        w_new = w / 2

        # Apply the eigenvalue constraint before returning!
        C_constrained = apply_eigenvalue_constraint(C, psi)
        
        # Add the two new components to the new GMM list
        new_GMM.append((w_new, mu_plus, C_constrained))
        new_GMM.append((w_new, mu_minus, C_constrained))
    
    return new_GMM

def LBG_algorithm_diag(GMM, alpha=0.1, psi=0.01):
    """LBG split enforcing Diagonal Covariance constraints."""
    new_GMM = []
    
    for w, mu, C in GMM:
        U, s, _ = np.linalg.svd(C)
        epsilon = U[:, 0:1] * s[0]**0.5 * alpha
        
        mu_plus = mu + epsilon
        mu_minus = mu - epsilon
        w_new = w / 2
        
        # Enforce Diagonal
        C_diag = C * np.eye(C.shape[0])
        C_constrained = apply_eigenvalue_constraint(C_diag, psi)
        
        new_GMM.append((w_new, mu_plus, C_constrained))
        new_GMM.append((w_new, mu_minus, C_constrained))
        
    return new_GMM

def LBG_algorithm_tied(GMM, alpha=0.1, psi=0.01):
    """LBG split for Tied Covariances. (Covariance is identical for all components)."""
    new_GMM = []
    
    # Since it's a tied GMM, all C's are exactly the same.
    # We calculate the displacement vector based on this shared covariance.
    
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