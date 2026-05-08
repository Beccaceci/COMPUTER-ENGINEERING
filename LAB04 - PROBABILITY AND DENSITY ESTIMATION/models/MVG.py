import numpy
from utils.math_utils import mcol


def log_MVG(X, mu, C):
    """
    Computes the log-density for a set of N samples
    X: matrix of shape (M, N)
    mu: mean vector of shape (M, 1)
    C: covariance matrix of shape (M, M)
    """
    M = X.shape[0]
    N = X.shape[1]
    
    # pre-compute constants for the N samples
    firstTerm = - (M / 2) * numpy.log(2 * numpy.pi)

    # compute the log-determinant of the covariance matrix
    log_det = numpy.linalg.slogdet(C)[1]
    secondTerm = - 0.5 * log_det
    
    # compute the inverse of the covariance matrix
    C_inv = numpy.linalg.inv(C)
    
    Y = []
    for i in range(N):
        # select the i-th sample as a column vector
        x = X[:, i:i+1]

        # compute the centered sample
        centered_x = x - mu

        # compute the third term of the log-density for the i-th sample
        thirdTerm = - 0.5 * (numpy.transpose(centered_x) @ C_inv @ centered_x)

        # sum the three terms to get the log-density for the i-th sample and append it to the list Y
        Y.append(firstTerm + secondTerm + thirdTerm.item())

    return numpy.array(Y)

