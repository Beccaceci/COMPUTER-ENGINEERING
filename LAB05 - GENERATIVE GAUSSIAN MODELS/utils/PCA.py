import numpy
import sys
from utils.math_utils import compute_covariance_matrix, mcol


def PCA (D, m):
    """
        Performs PCA on the given dataset.
        Parameters
        ----------
        D : numpy.ndarray
            The data matrix of shape (features, samples), where each column represents a sample.
        L : numpy.ndarray
            The label vector of shape (samples,), containing the class labels for each sample.
        Returns
        -------
        projected_data : numpy.ndarray
            The data projected onto the LDA subspace.
        lda_components : numpy.ndarray
            The LDA transformation matrix (eigenvectors).
        Notes
        -----
        This function computes the covariance matrix of the data and performs eigenvalue decomposition
        to obtain the LDA components.
    
    """
    
    # compute the mean of the dataset
    u = numpy.mean(D, axis=1, keepdims=True)
    
    # compute the covariance matrix
    C = compute_covariance_matrix(D, u)

    # compute the eigenvalues (s) and eigenvectors (U) of the covariance matrix
    s, U = numpy.linalg.eigh(C)

    # the first slice reverses the order of columns in U
    # the second slice selects the first m columns of that reversed matrix
    # as a result, the first m columns are selcted (which corresponds to the eigenvectors associated to the largest eigenvalues)
    P = U[:, ::-1][:, 0:m]

    # compute the projected data by applying the projecton to the matrix of samples D
    y = numpy.transpose(P) @ D
    return y, P