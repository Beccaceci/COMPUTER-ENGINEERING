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