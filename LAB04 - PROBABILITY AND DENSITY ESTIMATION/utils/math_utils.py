import numpy

def mcol (v):
    """ Function that reshapes the input vector into a column vector (size, 1) """
    return v.reshape((v.size, 1))

def vrow (v):
    """ Function that reshapes the input vector into a row vector (1, size)"""
    return v.reshape((1, v.size))

def compute_covariance_matrix (M):
    """ Function that computes the covriance matrix starting from a given matrix """
    # center the data by subtracting the mean from each column
    MC = M - numpy.mean(M, axis=1, keepdims=True)
    return (MC @ numpy.transpose(MC)) / float(MC.shape[1])


def log_GAU_ND(X, mu, C):
    """ 
    Computes the log-Gaussian PDF for a set of samples.
    Args:
        X (np.ndarray): Input matrix (d, n)
        mu (np.ndarray): Mean vector (d, 1)
        C (np.ndarray): Covariance matrix (d, d)
    Returns:
        np.ndarray: Log-Gaussian PDF (n,)
    """
    d = X.shape[0] # Corrected: d is the number of features (rows)
    
    # First term: -d/2 * log(2pi)
    first_term = -0.5 * d * numpy.log(2 * numpy.pi)
    
    # Second term: -1/2 * log|C|
    sign, det_C = numpy.linalg.slogdet(C)
    second_term = -0.5 * det_C
    
    # Third term: -1/2 * (X-mu)^T * inv(C) * (X-mu)
    X_centered = X - mu
    
    # Efficiently compute inv(C) * (X-mu) without explicitly inverting C
    invC_X = numpy.linalg.solve(C, X_centered)
    
    # Element-wise multiplication and sum along columns gives the diagonal of the dot product
    third_term = -0.5 * numpy.sum(X_centered * invC_X, axis=0)
    
    return first_term + second_term + third_term