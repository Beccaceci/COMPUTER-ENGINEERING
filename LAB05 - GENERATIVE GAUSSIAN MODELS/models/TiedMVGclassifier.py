import sys
import numpy
import scipy.special

from utils.data_loaders import load_dataset, split_dataset
from utils.math_utils import compute_covariance_matrix, compute_logdensity, mcol, vrow


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
    S = numpy.vstack(S)

    # --- 3. Log-Domain Probability Combinations ---
    # Compute joint log-densities
    logSJoint = S + mcol(numpy.log(Pc))

    # Compute marginal log-densities
    logSMarginal = vrow(scipy.special.logsumexp(logSJoint, axis=0))

    # Compute class posterior log-probabilities
    logSPost = logSJoint - logSMarginal

    return logSJoint, logSMarginal, logSPost


if __name__ == "__main__":
    
    # ==========================================
    # SETUP & CONFIGURATION
    # ==========================================
    if len(sys.argv) > 1: # Fixed: sys[1] changed to sys.argv[1]
        file_path = sys.argv[1]
    else:
        file_path = "data/iris_dataset.csv"

    # Pre-load instructor solutions for sanity checks
    try:
        expected_logSJoint = numpy.load("SOLUTIONS/logSJoint_TiedMVG.npy")
        expected_logSMarginal = numpy.load("SOLUTIONS/logMarginal_TiedMVG.npy")
        expected_logSPost = numpy.load("SOLUTIONS/logPosterior_TiedMVG.npy")
    except FileNotFoundError:
        print("Warning: Could not find the .npy solution files. Check the folder path.")
        
    # ==========================================
    # DATA PIPELINE
    # ==========================================
    D, L = load_dataset(file_path)
    ((DTR, LTR), (DTE, LTE)) = split_dataset(D, L, 2/3)

    # ==========================================
    # MODEL EXECUTION & PREDICTION
    # ==========================================
    logSJoint, logSMarginal, logSPost = compute_tied_mvg_parameters(DTR, LTR, DTE)

    # Predict labels using argmax
    predicted_labels = numpy.argmax(logSJoint, axis=0)

    # ==========================================
    # EVALUATION & METRICS
    # ==========================================
    accuracy = numpy.sum(predicted_labels == LTE) / len(LTE)
    error_rate = round((1 - accuracy) * 100, 1)
    
    print(f"Accuracy: {accuracy * 100:.1f}%")
    print(f"Error Rate: {error_rate}%")

    print("\n--- Running laboratory checks ---")
    print(f"logSJoint matches perfectly: {numpy.allclose(logSJoint, expected_logSJoint)}")
    print(f"logSMarginal matches perfectly: {numpy.allclose(logSMarginal, expected_logSMarginal)}")
    print(f"logSPost matches perfectly: {numpy.allclose(logSPost, expected_logSPost)}")
    print(f"Error Rate match: {numpy.isclose(error_rate, 2.0)}")