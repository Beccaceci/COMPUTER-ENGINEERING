import numpy as np
from GMMmodel.gmm_core import apply_eigenvalue_constraint

def train_gmm_lbg(X, n_components, LBG_split_func, EM_func, psi=0.01):
    """
    Trains a Gaussian Mixture Model using the LBG (Linde-Buzo-Gray) algorithm.
    It progressively splits the components until the target number is reached.
    
    Args:
        X: Dataset to train on (features x samples).
        n_components: Target number of GMM components.
        LBG_split_func: Function to split GMM components.
        EM_func: Expectation-Maximization function for GMM fitting.
        psi: Eigenvalue constraint for covariance matrices.
        
    Returns:
        Trained GMM model parameters.
    """
    # Initialize with a single component (global mean and covariance)
    mu = X.mean(axis=1, keepdims=True)
    C = np.cov(X, bias=True)
    C = apply_eigenvalue_constraint(C, psi)
    gmm = [(1.0, mu, C)]
    
    # Initial EM iteration with 1 component
    gmm = EM_func(X, gmm, psi=psi)
    
    current_c = 1
    while current_c < n_components:
        # Split components and re-estimate parameters
        gmm = LBG_split_func(gmm, psi=psi)
        gmm = EM_func(X, gmm, psi=psi)
        current_c *= 2
        
    return gmm
