import sys
import numpy
import scipy.special

from utils.math_utils import compute_covariance_matrix, compute_logdensity, mcol, vrow

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
    classes = numpy.unique(LTR)
    tied_sigma = numpy.zeros((DTR.shape[0], DTR.shape[0]))
    
    # 1. Compute pooled within-class covariance
    for c in classes:
        Dc = DTR[:, LTR == c]
        uc = numpy.mean(Dc, axis=1, keepdims=True)
        sigmac = compute_covariance_matrix(Dc, uc)
        tied_sigma += sigmac * Dc.shape[1]
    tied_sigma /= DTR.shape[1]

    # 2. Compute log-densities with the shared covariance matrix
    for c in classes:
        Dc = DTR[:, LTR == c]
        uc = numpy.mean(Dc, axis=1, keepdims=True)
        logS[c] = compute_logdensity(DTE, uc, tied_sigma)
        
    return logS[classes[1]] - logS[classes[0]]

def compute_tied_mvg_parameters(DTR, LTR, DTE):
    """
    Implements the Tied Covariance Multivariate Gaussian classifier.
    Computes a single, shared within-class covariance matrix for all classes.
    
    Parameters:
        DTR: Training data matrix of shape (M, Ntr)
        LTR: Training labels vector of shape (Ntr,)
        DTE: Test/Evaluation data matrix of shape (M, Nte)
        
    Returns:
        logSJoint: Joint log-densities for the test samples (shape: (C, Nte))
        logSMarginal: Marginal log-densities for the test samples (shape: (1, Nte))
        logSPost: Posterior log-probabilities for the test samples (shape: (C, Nte))
    """
    # Initialize a matrix of zeros to accumulate the scaled covariances
    tied_sigma = numpy.zeros((DTR.shape[0], DTR.shape[0]))

    # Dictionary to save the computed means so we don't recalculate them in Phase 2
    class_means = {}

    # Dynamically determine the number of classes and create a uniform prior array
    classes = numpy.unique(LTR)
    num_classes = len(classes)
    Pc = numpy.ones(num_classes) / num_classes

    for c in classes:
        Dc = DTR[:, LTR == c]
        Nc = Dc.shape[1] # Number of samples belonging to class c
        
        uc = numpy.mean(Dc, axis=1, keepdims=True)
        sigmac = compute_covariance_matrix(Dc, uc)

        # Save the class mean for later
        class_means[c] = uc

        # Accumulate the covariance matrix scaled by its class sample size
        tied_sigma += sigmac * Nc
    
    # Divide by the total number of training samples to finalize the tied covariance
    tied_sigma = tied_sigma / DTR.shape[1]

    S = []
    for c in classes:
        S.append(compute_logdensity(DTE, class_means[c], tied_sigma))

    # Convert the list of arrays into a 2D matrix
    S = numpy.vstack(S)

    # --- 3. Log-Domain Probability Combinations ---
    # Compute joint log-densities
    logSJoint = S + mcol(numpy.log(Pc))

    # Compute marginal log-densities
    logSMarginal = vrow(scipy.special.logsumexp(logSJoint, axis=0))

    # Compute class posterior log-probabilities
    logSPost = logSJoint - logSMarginal

    return logSJoint, logSMarginal, logSPost