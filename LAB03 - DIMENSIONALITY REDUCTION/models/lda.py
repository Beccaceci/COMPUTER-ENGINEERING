import numpy
import scipy.linalg
from utils.math_utils import compute_covariance_matrix, compute_mean_vector

def compute_within_class_covariance(D, L):
    """
    Computes the within-class covariance matrix Sw.
    Sw = (1/N) * sum(nc * Sw_c)

    Args:
        - D: data matrix (n_features x n_samples)
        - L: label vector (n_samples,)
    Returns:
        - SW: within-class covariance matrix (n_features x n_features)
    """

    n_features = D.shape[0] # number of features (4)
    n_samples = D.shape[1]  # number of samples (150)
    SW = numpy.zeros((n_features, n_features)) # final within covariance matrix (4x4)

    for c in numpy.unique(L): # for each class
        D_c = D[:, L==c] # select all the samples belonging to the c class
        n_c = D_c.shape[1] # number of samples belonging to the c class

        SW_c = compute_covariance_matrix(D_c) # compute the covariance matrix associated to the c class
        SW += (n_c * SW_c)

    return (SW / n_samples)


def compute_between_class_covariance (D, L):
    """
    Computes the bewteen-class covariance matrix Sb.

    Args:
        - D: data matrix (n_features x n_samples)
        - L: label vector (n_samples,)
    Returns:
        - Sb: between-class covariance matrix (n_features x n_features)
    """
     
    u = compute_mean_vector(D) # compute the dataset mean
    n_features = D.shape[0] # number of features (4)
    n_samples = D.shape[1]  # number of samples (150)
    Sb = numpy.zeros((n_features, n_features)) # final between covariance matrix (4x4)

    for c in numpy.unique(L): # for each class
        D_c = D[:, L==c] # select all the samples belonging to the class c
        n_c = D_c.shape[1] # number of samples belonging to the class c
        u_c = compute_mean_vector(D_c) # compute the mean considering all the samples belonging to class c
        diff = u_c - u
        Sb += (n_c * (diff @ diff.T)) # compute the between-class covariance matrix

    return (Sb / n_samples)

def trainLda(D, L, m):
    """
    Trains the LDA model.
    
    Args:
        - D: data matrix (n_features x n_samples)
        - L: label vector (n_samples,)
        - m: number of dimensions to project onto (m <= C-1, where C is the number of classes)
    Returns:
        - W: projection matrix (n_features x m)
    """

    # compute the within-class and between-class covariance matrices
    SW = compute_within_class_covariance(D, L)
    SB = compute_between_class_covariance (D, L)

    # compute the eigenvectors and eigenvalues of SW^(-1) @ SB
    s, U = scipy.linalg.eigh(SB, SW)

    # Sort the eigenvalues and eigenvectors in descending order and select the first m dimensions
    W = U[:, ::-1][:, 0:m]

    # Alternative approach using SVD
    # UW, _, _ = numpy.linalg.svd(W)
    # U = UW[:, 0:m]
    # return U
    return W

def applyLda(W, D):
    """
    Applies LDA to the given dataset.
    
    Args:
        - W: projection matrix (n_features x m)
        - D: data matrix (n_features x n_samples)
    Returns:
        - y: projected data (m x n_samples)
    """
    y = numpy.transpose(W) @ D
    return y

def compute_lda (D, L, m):
    """
    Computes the projection matrix W for LDA.
    Parameters:
        - D: data matrix (n_features x n_samples)
        - L: label vector (n_samples,)
        - m: number of dimensions to project onto (m <= C-1, where C is the number of classes)
    Returns:
        - s: eigenvalues sorted in descending order
        - W: projection matrix (n_features x m)
    """
    # train the LDA model
    W = trainLda(D, L, m)
    # apply the LDA model to the data
    y = applyLda(W, D)
    return y, W
