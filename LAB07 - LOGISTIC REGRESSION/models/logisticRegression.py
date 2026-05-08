import numpy
import scipy.optimize

from utils.math_utils import mcol, vrow

# =======================================================
# BINARY LOGISTIC REGRESSION
# =======================================================

# Logistic Regression objective functions (standard and prior-weighted) and their gradients

def logreg_obj_standard(v, DTR, LTR, l):
    """
    Computes the Logistic Regression objective function and its analytical gradient.
    Parameters:
        v: A 1D array containing the parameters (w and b) concatenated.
        DTR: Training data matrix (D, N)
        LTR: Training labels array (N,)
        l: Regularization parameter (lambda)
    Returns:
        J: The value of the objective function at the given parameters.
        grad: A 1D array containing the gradient of the objective function with respect to the
    """
    # Unpack w and b
    w, b = v[:-1], v[-1]
    
    # Compute scores S
    S = (numpy.dot(mcol(w).T, DTR) + b).ravel()
    
    # Compute zi (ZTR)
    ZTR = 2 * LTR - 1
    
    # ==========================================
    # COMPUTE OBJECTIVE J(w, b)
    # ==========================================
    # Calculate the cross-entropy loss safely using logaddexp.mean() automatically sums the array and divides by n
    cross_entropy = numpy.logaddexp(0, -ZTR * S).mean()

    # J(w, b) = (lambda / 2) * ||w||^2 + cross_entropy
    J = (l / 2) * numpy.linalg.norm(w)**2 + cross_entropy
    
    # ==========================================
    # COMPUTE GRADIENTS
    # ==========================================
    # Compute the shared G_i term
    # G_i = -z_i / (1 + e^(z_i * S_i))
    G = -ZTR / (1.0 + numpy.exp(ZTR * S))
    
    # Gradient with respect to w
    # vrow(G) * DTR broadcasts G across the features of DTR.
    # .mean(axis=1) sums across all samples and divides by n.
    grad_w = l * w + (vrow(G) * DTR).mean(axis=1)
    
    # Gradient with respect to b
    grad_b = G.mean()
    
    # Pack gradients back into a single 1D array
    grad = numpy.hstack([grad_w, grad_b])
    
    return J, grad

def logreg_obj_weighted(v, DTR, LTR, l, pi_T):
    """
    Objective function for Prior-Weighted Logistic Regression.
    Explicitly computes and applies xi weights based on target prior pi_T.
    """
    # Unpack w and b
    w, b = v[:-1], v[-1]
    
    # Compute scores S
    S = (numpy.dot(mcol(w).T, DTR) + b).ravel()

    # Compute zi (ZTR)
    ZTR = 2 * LTR - 1
    
    # ==========================================
    # COMPUTE OBJECTIVE J(w, b)
    # ==========================================
    # Compute xi array
    nT = (LTR == 1).sum()
    nF = (LTR == 0).sum()
    xi = numpy.where(LTR == 1, pi_T / nT, (1 - pi_T) / nF)
    
    # Calculate the cross-entropy loss safely using logaddexp.mean() automatically sums the array and divides by n
    cross_entropy = (numpy.logaddexp(0, -ZTR * S) * xi).sum()

    # J(w, b) = (lambda / 2) * ||w||^2 + cross_entropy
    J = (l / 2) * numpy.linalg.norm(w)**2 + cross_entropy
    
    # ==========================================
    # COMPUTE GRADIENTS
    # ==========================================
    # Compute the shared G_i term
    # G_i = -z_i / (1 + e^(z_i * S_i))
    G = -ZTR / (1.0 + numpy.exp(ZTR * S))
    
    # Gradient with respect to w
    grad_w = l * w + (vrow(G * xi) * DTR).sum(axis=1)

    # Gradient with respect to b
    grad_b = (G * xi).sum()
    
    grad = numpy.hstack([grad_w, grad_b])
    return J, grad

# Logistic Regression training function using L-BFGS optimization

def trainLogReg(DTR, LTR, l, pi_T=None):
    """
    Trains a Logistic Regression model using L-BFGS.
    
    Parameters:
        DTR: Training data matrix (D, N)
        LTR: Training labels array (N,)
        l: Regularization parameter (lambda)
        
    Returns:
        w, b: The optimized weight vector and bias.
    """

    # Define the starting point for the optimizer
    x0 = numpy.zeros(DTR.shape[0] + 1)

    # Route to the appropriate objective function based on pi_T
    if pi_T is None:
        obj_func = logreg_obj_standard
        args_tuple = (DTR, LTR, l)
    else:
        obj_func = logreg_obj_weighted
        args_tuple = (DTR, LTR, l, pi_T)

    # Call the L-BFGS optimizer to minimize the objective function
    x_opt, f_opt, d = scipy.optimize.fmin_l_bfgs_b(
        func=obj_func,
        x0=x0, 
        args=args_tuple,
        approx_grad=False
    )

    # Extract the optimized parameters
    w_opt, b_opt = x_opt[:-1], x_opt[-1]
    
    return w_opt, b_opt


# =======================================================
# MULTICLASS LOGISTIC REGRESSION
# =======================================================

# Multiclass Logistic Regression objective function and gradient using the softmax formulation

def logreg_obj_multiclass(v, DTR, LTR, l):
    """
    Objective function for Multiclass Logistic Regression.
    """
    n = DTR.shape[1]
    D = DTR.shape[0]
    K = numpy.max(LTR) + 1 # Number of classes
    
    # Unpack W and b from the flat array v
    W = v[:D*K].reshape((D, K))
    b = v[D*K:].reshape((K, 1))
    
    # 1. Compute the matrix of scores S (K x n)
    S = numpy.dot(W.T, DTR) + b
    
    # 2. Compute Y_log using the log-sum-exp trick
    logsumexp_S = scipy.special.logsumexp(S, axis=0)
    Y_log = S - logsumexp_S 
    
    # 3. 1-of-K (One-Hot) encoding of the labels
    T = numpy.zeros((K, n))
    T[LTR, numpy.arange(n)] = 1
    
    # 4. Compute Objective Function J(W, b)
    # Element-wise multiplication of T and Y_log, summed over all elements, divided by n
    cross_entropy = - (T * Y_log).sum() / n
    
    # Squared norm of W is (W * W).sum()
    J = (l / 2) * (W * W).sum() + cross_entropy
    
    # 5. Compute the gradients with respect to W and b
    Y = numpy.exp(Y_log) # Matrix of posterior probabilities
    
    grad_W = l * W + numpy.dot(DTR, (Y - T).T) / n
    grad_b = (Y - T).sum(axis=1) / n
    
    # Pack gradients back into a 1D array
    grad = numpy.hstack([grad_W.ravel(), grad_b.ravel()])
    
    return J, grad

# Multiclass Logistic Regression training function using L-BFGS optimization

def trainLogReg_Multiclass(DTR, LTR, l):
    """
    Trains a Multiclass Logistic Regression model using L-BFGS.
    """
    D = DTR.shape[0]
    K = numpy.max(LTR) + 1
    
    # Starting point: all zeros for W and b
    x0 = numpy.zeros(D * K + K)
    
    x_opt, f_opt, d = scipy.optimize.fmin_l_bfgs_b(
        func=logreg_obj_multiclass,
        x0=x0, 
        args=(DTR, LTR, l),
        approx_grad=False # Using our exact gradient!
    )
    
    # Unpack the optimal parameters
    W_opt = x_opt[:D*K].reshape((D, K))
    b_opt = x_opt[D*K:].reshape((K, 1))
    
    return W_opt, b_opt