import sys
import scipy.special
import numpy
from utils.data_loaders import *
from utils.math_utils import *


def compute_logdensity_difference (DTR, LTR, DTE):
    """
    This function implements the MVG classifier for a multi-class classification problem.
    Parameters:
        DTR: training data matrix of shape (M, Ntr)
        LTR: training labels vector of shape (Ntr,)
        DTE: test data matrix of shape (M, Nte)
    Returns:
        logSJoint: joint log-densities for the test samples (shape: (C, Nte))
        logSMarginal: marginal log-densities for the test samples (shape: (1, Nte))
        logSPost: posterior log-probabilities for the test samples (shape: (C, Nte))
        predicted_labels: predicted labels for the test samples (shape: (Nte,))
    """

    # define an empty score matrix
    logS = {}

    for c in numpy.unique([1, 2]):
        Dc = DTR[:, LTR == c]
        uc = numpy.mean(Dc, axis=1, keepdims=True)
        sigmac = compute_covariance_matrix(Dc, uc)
        logS[c] = (compute_logdensity(DTE, uc, sigmac))

    return (logS[2] - logS[1])


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        file_path = sys.argv[1]
    else:
        file_path = "data/iris_dataset.csv"

    D, L = load_dataset(file_path, True) # throw away all the samples belonging to class 0
    ((DTR, LTR), (DTE, LTE)) = split_dataset(D, L, 2/3)

    deltaLogS = compute_logdensity_difference(DTR, LTR, DTE)
    
    predicted_labels = (deltaLogS > 0).astype(int) + 1

    # Compute accuracy
    accuracy = numpy.sum(predicted_labels == LTE) / len(LTE)
    error_rate = round((1 - accuracy) * 100, 1)
    print(f"Accuracy: {(accuracy) * 100:.1f}%")
    print(f"Error Rate: {error_rate}%")

    print("\n--- Running laboratory checks ---")
    print(f"Error Rate match: {numpy.isclose(error_rate, 8.8)}")