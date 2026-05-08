import numpy

def mcol (v):
    """ Function to reshape a vector into a column vector """
    return v.reshape((v.size, 1))


def mrow (v):
    """ Function to reshape a vector into a row vector """
    return v.reshape((1, v.size))


def compute_mean (D):
    """ Function to compute the mean of each feature across all samples """
    
    # By providing axis=1, you tell NumPy to "collapse" the columns. It iterates through each row (each feature) and calculates the average of the 150 samples in that row.
    # When NumPy calculates the mean across an axis, it discards that dimension: The output is a 1D array: [mu1, mu2, mu3, mu4] with shape (4,).
    # You cannot directly subtract a (4,) array from a (4, 150) matrix in a way that subtracts each feature mean from its corresponding row
    # We reshape it to (4, 1) so it becomes a "column vector".
    return mcol(numpy.mean(D, axis=1))


def compute_covariance (D):
    """ Function to compute the covariance matrix of the dataset """

    D_centered = D - compute_mean(D) # Center the data by subtracting the mean from each feature
    return ((D_centered @ D_centered.T) / float(D.shape[1]))


def compute_variance (D):
    """ Function to compute the variance of each feature across all samples """
    return numpy.var(D, axis=1)


def compute_std (D):
    """ Function to compute the standard deviation of each feature across all samples """
    return numpy.std(D, axis=1)