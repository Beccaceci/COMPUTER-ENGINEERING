import numpy
from models.MVG import log_MVG

def loglikelihood(X, mu, C):
    """
    Computes the total log-likelihood as the sum of log-densities.
    """
    log_densities = log_MVG(X, mu, C)
    return log_densities.sum()