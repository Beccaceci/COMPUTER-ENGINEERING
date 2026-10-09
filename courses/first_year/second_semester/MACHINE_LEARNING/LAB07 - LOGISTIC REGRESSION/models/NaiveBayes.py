import numpy
from utils.math_utils import compute_covariance_matrix, compute_logdensity

def compute_naive_bayes_loglikelihoods(DTR, LTR, DTE):
    """
    Trains the Naive Bayes model and computes the class-conditional log-likelihoods.
    It enforces feature independence by using a diagonal covariance matrix.
    
    Returns:
        S_log: Matrix of shape (C, Nte) containing log f(x_t | c)
    """
    S_log = []
    classes = numpy.unique(LTR)
    
    for c in classes:
        # Isolate class data
        Dc = DTR[:, LTR == c]
        
        # Compute empirical mean and full covariance
        uc = numpy.mean(Dc, axis=1, keepdims=True)
        sigmac_full = compute_covariance_matrix(Dc, uc)
        
        # NAIVE BAYES ASSUMPTION: 
        # Multiply element-wise by the identity matrix to zero out covariances
        sigmac_nb = sigmac_full * numpy.eye(sigmac_full.shape[0])
        
        # Compute log-densities for this class
        log_densities_c = compute_logdensity(DTE, uc, sigmac_nb)
        S_log.append(log_densities_c)

    return numpy.vstack(S_log)