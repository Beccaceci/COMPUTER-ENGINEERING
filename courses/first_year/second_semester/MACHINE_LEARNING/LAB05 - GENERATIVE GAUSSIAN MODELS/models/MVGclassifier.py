import sys
import numpy
import scipy.special

from utils.data_loaders import load_dataset, split_dataset
from utils.math_utils import compute_covariance_matrix, compute_logdensity, mcol, vrow

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
    classes = numpy.unique(LTR)
    for c in classes: # Iterate over the two classes
        Dc = DTR[:, LTR == c] # Select the samples belonging to class c
        uc = numpy.mean(Dc, axis=1, keepdims=True) # Compute the empirical mean
        sigmac = compute_covariance_matrix(Dc, uc) # Compute the empirical covariance matrix
        logS[c] = compute_logdensity(DTE, uc, sigmac) # Compute the log-density
    return logS[classes[1]] - logS[classes[0]] # Return the log-likelihood ratio

def compute_MVG_parameters(DTR, LTR, DTE):
    """
    Implements the standard Multivariate Gaussian (MVG) classifier inference chain.
    
    Parameters:
        DTR: Training data matrix of shape (M, Ntr)
        LTR: Training labels vector of shape (Ntr,)
        DTE: Test/Evaluation data matrix of shape (M, Nte)
        
    Returns:
        logSJoint: Joint log-densities for the test samples (shape: (C, Nte))
        logSMarginal: Marginal log-densities for the test samples (shape: (1, Nte))
        logSPost: Posterior log-probabilities for the test samples (shape: (C, Nte))
    """

    # List to store class-conditional log-densities (log-likelihoods) before stacking
    S = []

    # Dynamically determine the number of classes and create a uniform prior array
    classes = numpy.unique(LTR)
    num_classes = len(classes)
    Pc = numpy.ones(num_classes) / num_classes

    for c in classes:
        # --- 1. Parameter Estimation (Training Phase) ---
        # Isolate the training samples belonging only to class 'c'
        Dc = DTR[:, LTR == c]
        
        # Compute the empirical mean (uc) and covariance matrix (sigmac)
        uc = numpy.mean(Dc, axis=1, keepdims=True)
        sigmac = compute_covariance_matrix(Dc, uc)

        # --- 2. Inference (Evaluation Phase) ---
        # Evaluate ALL test samples against the learned parameters for class 'c'
        log_densities_c = compute_logdensity(DTE, uc, sigmac)
        S.append(log_densities_c)

    # Convert the list of 1D arrays into a 2D matrix (C rows x Nte columns)
    S = numpy.vstack(S)

    # --- 3. Log-Domain Probability Combinations ---
    # Compute joint log-densities: log(Likelihood) + log(Prior)
    logSJoint = S + mcol(numpy.log(Pc))

    # Compute marginal log-densities using the log-sum-exp trick across classes (axis=0)
    logSMarginal = vrow(scipy.special.logsumexp(logSJoint, axis=0))

    # Compute class posterior log-probabilities: log(Joint) - log(Marginal)
    logSPost = logSJoint - logSMarginal

    return logSPost