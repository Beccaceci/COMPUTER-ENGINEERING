import sys
import numpy
import scipy.special

from utils.math_utils import compute_covariance_matrix, compute_logdensity, mcol, vrow


def compute_naive_bayes_parameters(DTR, LTR, DTE):
    """
    Implements the Naive Bayes Gaussian classifier inference chain.
    Assumes feature independence by strictly using the diagonal of the covariance matrix.
    
    Parameters:
        DTR: Training data matrix of shape (M, Ntr)
        LTR: Training labels vector of shape (Ntr,)
        DTE: Test/Evaluation data matrix of shape (M, Nte)
        
    Returns:
        logSJoint: Joint log-densities for the test samples (shape: (C, Nte))
        logSMarginal: Marginal log-densities for the test samples (shape: (1, Nte))
        logSPost: Posterior log-probabilities for the test samples (shape: (C, Nte))
    """
    # List to store class-conditional log-densities before stacking
    S = []

    # Dynamically determine the number of classes and create a uniform prior array
    classes = numpy.unique(LTR)
    num_classes = len(classes)
    Pc = numpy.ones(num_classes) / num_classes

    for c in classes:
        # --- 1. Parameter Estimation (Training Phase) ---
        Dc = DTR[:, LTR == c]
        uc = numpy.mean(Dc, axis=1, keepdims=True)
        
        # Compute the standard covariance matrix, then isolate the diagonal elements
        sigmac = compute_covariance_matrix(Dc, uc) 
        diagonalSigmac = sigmac * numpy.eye(sigmac.shape[0])

        # --- 2. Inference (Evaluation Phase) ---
        # Evaluate using the diagonalized covariance matrix
        S.append(compute_logdensity(DTE, uc, diagonalSigmac))

    # Convert the list of 1D arrays into a 2D matrix (C rows x Nte columns)
    S = numpy.vstack(S)

    # --- 3. Log-Domain Probability Combinations ---
    # Compute joint log-densities: log(Likelihood) + log(Prior)
    logSJoint = S + mcol(numpy.log(Pc))

    # Compute marginal log-densities using the log-sum-exp trick across classes
    logSMarginal = vrow(scipy.special.logsumexp(logSJoint, axis=0))

    # Compute class posterior log-probabilities: log(Joint) - log(Marginal)
    logSPost = logSJoint - logSMarginal

    return logSJoint, logSMarginal, logSPost