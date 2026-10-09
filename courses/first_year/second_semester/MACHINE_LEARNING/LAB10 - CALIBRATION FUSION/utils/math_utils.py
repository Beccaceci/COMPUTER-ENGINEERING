import numpy

def mcol (v):
    """ Function that reshapes the input vector into a column vector (size, 1) """
    return v.reshape((v.size, 1))

def vcol(v):
    """ Alias for mcol """
    return mcol(v)

def vrow (v):
    """ Function that reshapes the input vector into a row vector (1, size) """
    return v.reshape((1, v.size))

def polynomial_kernel (x1, x2, d=2, c=1):
    """ Computes the polynomial kernel between two vectors x1 and x2 with degree d """
    return (numpy.transpose(x1) @ x2 + c) ** d

def radial_basis_kernel (x1, x2, gamma=1):
    """ Computes the RBF kernel between two vectors x1 and x2 with parameter gamma """
    # Computes ||x1||^2 for each column, reshapes to (N1, 1)
    sq_norm_x1 = numpy.sum(x1**2, axis=0).reshape(-1, 1)
    
    # Computes ||x2||^2 for each column, reshapes to (1, N2)
    sq_norm_x2 = numpy.sum(x2**2, axis=0).reshape(1, -1)
    
    # ||x1 - x2||^2 = ||x1||^2 + ||x2||^2 - 2*x1^T*x2
    sq_dist = sq_norm_x1 + sq_norm_x2 - 2 * (numpy.transpose(x1) @ x2)

    return numpy.exp(-gamma * sq_dist)