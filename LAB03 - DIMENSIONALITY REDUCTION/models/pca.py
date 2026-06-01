import numpy
from utils.math_utils import compute_covariance_matrix, mcol

def trainPCA (D, m):
    """
    Performs PCA on the given dataset.
    Parameters:
        ----------
        D : numpy.ndarray
            The data matrix of shape (features, samples), where each column represents a sample.
        m : int
            The number of dimensions to project the data onto.
    Returns
    -------
        P: numpy.ndarray
            The PCA transformation matrix (eigenvectors).
    Notes
    -----
    This function computes the covariance matrix of the data and performs eigenvalue decomposition
    to obtain the PCA components.
    """
    # compute the covariance matrix
    C = compute_covariance_matrix(D)
    # compute the eigenvalues (s) and eigenvectors (U) of the covariance matrix
    s, U = numpy.linalg.eigh(C)
    # the first slice reverses the order of columns in U
    # the second slice selects the first m columns of that reversed matrix
    # as a result, the first m columns are selcted (which corresponds to the eigenvectors associated to the largest eigenvalues)
    P = U[:, ::-1][:, 0:m]
    return P

def applyPCA (P, D):
    """
    Applies PCA to the given dataset.
    Parameters:
        ----------
        P : numpy.ndarray
            The PCA transformation matrix (eigenvectors).
        D : numpy.ndarray
            The data matrix of shape (features, samples), where each column represents a sample.
    Returns
    -------
        y: numpy.ndarray
            The projected data.
    """
    # compute the projected data by applying the projection to the matrix of samples D
    y = numpy.transpose(P) @ D
    return y


def compute_pca (D, m):
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
    # train the PCA model
    P = trainPCA(D, m)
    # apply the PCA model to the data
    y = applyPCA(P, D)
    return y, P