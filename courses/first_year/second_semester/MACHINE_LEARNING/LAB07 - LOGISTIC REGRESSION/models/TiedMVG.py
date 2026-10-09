import numpy
from utils.math_utils import compute_covariance_matrix, compute_logdensity, mcol, vrow

def compute_tied_mvg_loglikelihoods(DTR, LTR, DTE):
    """
    Computes the class-conditional log-likelihoods for a Tied Multivariate Gaussian model.
    
    Parameters:
        DTR: Training data matrix of shape (M, Ntr)
        LTR: Training labels vector of shape (Ntr,)
        DTE: Test/Evaluation data matrix of shape (M, Nte)
        
    Returns:
        S_log: Matrix of shape (C, Nte) containing log f(x_t | c) for each class c and test sample t
    """
    # Initialize a matrix of zeros to accumulate the scaled covariances
    # DTR.shape[0] dynamically gets the number of features (M)
    tied_sigma = numpy.zeros((DTR.shape[0], DTR.shape[0]))

    # Dictionary to save the computed means so we don't recalculate them in Phase 2
    class_means = {}

    # Dynamically determine the number of classes and create a uniform prior array
    classes = numpy.unique(LTR)
    num_classes = len(classes)
    Pc = numpy.ones(num_classes) / num_classes

    # --- PHASE 1: TRAINING (Compute means and tied covariance matrices) ---
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

    # --- PHASE 2: INFERENCE (Compute log-densities) ---
    S = []
    for c in numpy.unique(LTR):
        # Evaluate all test samples using the specific class mean and the SHARED tied_sigma
        S.append(compute_logdensity(DTE, class_means[c], tied_sigma))

    # Convert the list of arrays into a 2D matrix
    return numpy.vstack(S)