import numpy
import scipy.special
from utils.math_utils import compute_covariance_matrix, compute_logdensity, mcol, vrow

def compute_mvg_loglikelihoods(DTR, LTR, DTE):
    """
    Trains the MVG model and computes the class-conditional log-likelihoods.
    
    Returns:
        S_log: Matrix of shape (C, Nte) containing log f(x_t | c)
    """
    S_log = []
    classes = numpy.unique(LTR)
    
    for c in classes:
        # --- 1. Parameter Estimation (Training Phase) ---
        # Isolate the training samples belonging only to class 'c'
        Dc = DTR[:, LTR == c]

        # Compute the empirical mean (uc) and covariance matrix (sigmac)
        uc = numpy.mean(Dc, axis=1, keepdims=True)
        sigmac = compute_covariance_matrix(Dc, uc)
        
         # --- 2. Inference (Evaluation Phase) ---
        # Evaluate ALL test samples against the learned parameters for class 'c'
        # log_densities_c is log f(x_t | c)
        log_densities_c = compute_logdensity(DTE, uc, sigmac)
        S_log.append(log_densities_c)

    # Convert the list of 1D arrays into a 2D matrix (C rows x Nte columns)
    return numpy.vstack(S_log)