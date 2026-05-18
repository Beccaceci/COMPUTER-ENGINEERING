import numpy

from utils.data_loaders import *
from utils.math_utils import *

def compute_binary_mvg (DTR, LTR, DTE):
    """
    Computes the Log-Likelihood Ratio for classes 2 and 1 using Standard MVG
    Parameters:
        DTR: training data matrix of shape (M, Ntr)
        LTR: training labels vector of shape (Ntr,)
        DTE: test data matrix of shape (M, Nte)
    Returns:
        logS: log-likelihood ratio for classes 2 and 1 of shape (Nte,)
    """
    logS = {}
    for c in [1, 2]:
        Dc = DTR[:, LTR == c]
        uc = numpy.mean(Dc, axis=1, keepdims=True)
        sigmac = compute_covariance_matrix(Dc, uc)
        logS[c] = compute_logdensity(DTE, uc, sigmac)
    return logS[2] - logS[1]

def compute_binary_tied_mvg(DTR, LTR, DTE):
    """
    Computes the Log-Likelihood Ratio for classes 2 and 1 using Tied MVG.
    Parameters:
        DTR: training data matrix of shape (M, Ntr)
        LTR: training labels vector of shape (Ntr,)
        DTE: test data matrix of shape (M, Nte)
    Returns:
        logS: log-likelihood ratio for classes 2 and 1 of shape (Nte,)
    """
    logS = {}
    tied_sigma = numpy.zeros((DTR.shape[0], DTR.shape[0]))
    
    # 1. Compute pooled within-class covariance
    for c in [1, 2]:
        Dc = DTR[:, LTR == c]
        uc = numpy.mean(Dc, axis=1, keepdims=True)
        sigmac = compute_covariance_matrix(Dc, uc)
        tied_sigma += sigmac * Dc.shape[1]
    tied_sigma /= DTR.shape[1]

    # 2. Compute log-densities with the shared covariance matrix
    for c in [1, 2]:
        Dc = DTR[:, LTR == c]
        uc = numpy.mean(Dc, axis=1, keepdims=True)
        logS[c] = compute_logdensity(DTE, uc, tied_sigma)
        
    return logS[2] - logS[1]