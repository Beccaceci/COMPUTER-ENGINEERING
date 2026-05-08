import sys
import numpy
import scipy.special

from utils.data_loaders import load_dataset, split_dataset
from utils.math_utils import compute_covariance_matrix, compute_logdensity, mcol, vrow


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
    
    # SPost = numpy.exp(logSPost)

    return logSJoint, logSMarginal, logSPost


if __name__ == "__main__":
    # ==========================================
    # SETUP & CONFIGURATION
    # ==========================================
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "data/iris_dataset.csv"

    # Pre-load instructor solutions for sanity checks
    try:
        expected_logSJoint = numpy.load("SOLUTIONS/logSJoint_MVG.npy")
        expected_logSMarginal = numpy.load("SOLUTIONS/logMarginal_MVG.npy")
        expected_logSPost = numpy.load("SOLUTIONS/logPosterior_MVG.npy")
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
    # Execute the core MVG math to get the log-probabilities
    logSJoint, logSMarginal, logSPost = compute_MVG_parameters(DTR, LTR, DTE)

    # Predict labels by finding the class (row index) with the highest joint probability
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
    print(f"Error Rate match: {numpy.isclose(error_rate, 4.0)}")