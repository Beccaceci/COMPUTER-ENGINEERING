import numpy
import scipy.linalg
from utils.math_utils import compute_covariance_matrix, mcol

def compute_within_class_covariance(D, L):
    """
    Computes the within-class covariance matrix Sw.
    Sw = (1/N) * sum(nc * Sw_c)
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
    """
     
    u = mcol(numpy.mean(D, axis=1)) # compute the dataset mean
    n_features = D.shape[0] # number of features (4)
    n_samples = D.shape[1]  # number of samples (150)
    Sb = numpy.zeros((n_features, n_features)) # final between covariance matrix (4x4)

    for c in numpy.unique(L):
        D_c = D[:, L==c] # select all the samples belonging to the class c
        n_c = D_c.shape[1] # number of samples belonging to the class c
        u_c = mcol(numpy.mean(D_c, axis=1)) # compute the mean considering all the samples belonging to class c
        diff = u_c - u
        Sb += (n_c * (diff @ numpy.transpose(diff)))

    return (Sb / n_samples)


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
    SW = compute_within_class_covariance(D, L)
    SB = compute_between_class_covariance (D, L)

    s, U = scipy.linalg.eigh(SB, SW)
    W = U[:, ::-1][:, 0:m]

    # UW, _, _ = numpy.linalg.svd(W)
    # U = UW[:, 0:m]
    # return U
    return s[::-1], W
