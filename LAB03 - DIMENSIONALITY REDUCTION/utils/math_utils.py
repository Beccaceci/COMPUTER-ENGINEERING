import numpy

def mcol (v):
    """ Function that reshapes the input vector into a column vector """
    return v.reshape((v.size, 1))

def mrow (v):
    """ Function that reshapes the input vector into a row vector """
    return v.reshape((1, v.size))


def compute_covariance_matrix (D):
    """ Function that computes the covriance matrix starting from a given matrix """
    DC = D - mcol(numpy.mean(D, axis=1))
    return ((DC @ numpy.transpose(DC)) / float(D.shape[1]))
