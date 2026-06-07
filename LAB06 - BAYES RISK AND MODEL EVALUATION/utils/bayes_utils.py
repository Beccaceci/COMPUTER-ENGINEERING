import numpy
import scipy.special

from utils.math_utils import compute_covariance_matrix, compute_logdensity, mcol, vrow

def compute_posteriors(S_log, prior_array):
    """
    Computes joint, marginal, and posterior log-probabilities dynamically.
    
    Args:
        S_log: Class-conditional log-likelihoods (C, Nte)
        prior_array: 1D numpy array of class priors (shape: (C,))
    
    Returns:
        logSJoint: Joint log-probabilities (C, Nte)
        logSMarginal: Marginal log-probabilities (1, Nte)
        logSPost: Posterior log-probabilities (C, Nte)
    """
    # 1. log(Likelihood) + log(Prior)
    logSJoint = S_log + mcol(numpy.log(prior_array))
    
    # 2. log-sum-exp trick across classes (axis=0)
    logSMarginal = vrow(scipy.special.logsumexp(logSJoint, axis=0))
    
    # 3. Posterior log-probabilities
    logSPost = logSJoint - logSMarginal
    
    return logSJoint, logSMarginal, logSPost

# ======================================================
# Utils functions for binary problems
# ======================================================

def compute_optimal_bayes_binary(llr, pi1, Cfn, Cfp):
    """
    Computes optimal Bayes decisions for binary tasks based on Log-Likelihood Ratios.
    
    Parameters:
        llr: 1D numpy array of Log-Likelihood Ratios
        pi1: Prior probability of the True class (Class 1)
        Cfn: Cost of a false negative (predicting 0 when actual is 1)
        Cfp: Cost of a false positive (predicting 1 when actual is 0)
        
    Returns:
        predictions: 1D numpy array of predicted labels (0 or 1)
    """
    # Calculate the theoretical optimal threshold
    threshold = -numpy.log((pi1 * Cfn) / ((1 - pi1) * Cfp))
    
    # Generate predictions: 1 if LLR > threshold, else 0
    predictions = (llr > threshold).astype(int)
    
    return predictions

def compute_empirical_Bayes_risk_binary(M, pi1, Cfn, Cfp):
    """
    Computes the un-normalized empirical Bayes risk (DCF_u) from a binary confusion matrix.
    """
    # Calculate False Negative Rate (Pfn) and False Positive Rate (Pfp)
    Pfn = M[0, 1] / (M[0, 1] + M[1, 1])
    Pfp = M[1, 0] / (M[0, 0] + M[1, 0])
    
    # Compute the un-normalized DCF (DCF_u)
    DCF_u = pi1 * Cfn * Pfn + (1 - pi1) * Cfp * Pfp
    return DCF_u

def compute_normalised_empirical_Bayes_risk_binary(M, pi1, Cfn, Cfp):
    """
    Computes the normalized empirical Bayes risk (DCF_n) from a binary confusion matrix.
    """
    # Compute the un-normalized DCF (DCF_u)
    DCF_u = compute_empirical_Bayes_risk_binary(M, pi1, Cfn, Cfp)

    # Compute the normalisation factor
    normalised_factor = normalised_factor = min(pi1 * Cfn, (1 - pi1) * Cfp)

    # Compute the normalized DCF
    DCF_norm = DCF_u / normalised_factor
    return DCF_norm

def compute_min_dcf(llr, true_labels, pi1, Cfn, Cfp):
    """
    Computes the minimum normalized empirical Bayes risk (min DCF) by sweeping over all possible theoretical thresholds.
    Parameters:
        llr: 1D numpy array of Log-Likelihood Ratios
        true_labels: 1D numpy array of true binary labels (0 or 1)
        pi1: Prior probability of the True class (Class 1)
        Cfn: Cost of a false negative (predicting 0 when actual is 1)
        Cfp: Cost of a false positive (predicting 1 when actual is 0)
    Returns:
        min_dcf_norm: The minimum normalized DCF across all thresholds
    """
    # Create the sorted list of all possible thresholds (-inf, sorted scores, +inf)
    thresholds = numpy.concatenate([numpy.array([-numpy.inf]), numpy.sort(llr), numpy.array([numpy.inf])])
    
    min_dcf_u = numpy.inf
    
    # Precompute total actual positives and negatives to speed up the loop
    total_actual_1 = numpy.sum(true_labels == 1)
    total_actual_0 = numpy.sum(true_labels == 0)
    
    for t in thresholds:
        # Vectorized prediction: 1 if LLR > t, else 0
        predictions = (llr > t).astype(int)
        
        # Fast vectorized calculation of False Negatives
        FN = numpy.sum((predictions == 0) & (true_labels == 1))
        FP = numpy.sum((predictions == 1) & (true_labels == 0))
        
        # Compute False Negative Rate (Pfn) and False Positive Rate (Pfp)
        Pfn = FN / total_actual_1
        Pfp = FP / total_actual_0
        
        # Compute un-normalized DCF for this threshold
        DCF_u = pi1 * Cfn * Pfn + (1 - pi1) * Cfp * Pfp
        
        # Track the minimum value
        if DCF_u < min_dcf_u:
            min_dcf_u = DCF_u

           
    # Compute the normalisation factor
    normalised_factor = min(pi1 * Cfn, (1 - pi1) * Cfp)
    
    # Return the normalized minimum DCF
    min_dcf_norm = min_dcf_u / normalised_factor
    return min_dcf_norm

def compute_roc_coordinates(llr, true_labels):
    """
    Computes the FPR and TPR arrays for all possible thresholds.
    """
    # Create the sorted list of all possible thresholds (-inf, sorted scores, +inf)
    thresholds = numpy.concatenate([numpy.array([-numpy.inf]), numpy.sort(llr), numpy.array([numpy.inf])])
    
    FPR = []
    TPR = []
    
    total_actual_1 = numpy.sum(true_labels == 1)
    total_actual_0 = numpy.sum(true_labels == 0)
    
    for t in thresholds:
        # Vectorized prediction: 1 if LLR > t, else 0
        predictions = (llr > t).astype(int)
        
        # Fast vectorized calculation of False Negatives and False Positives
        FN = numpy.sum((predictions == 0) & (true_labels == 1))
        FP = numpy.sum((predictions == 1) & (true_labels == 0))
        
        # Compute False Negative Rate (Pfn) and False Positive Rate (Pfp)
        Pfn = FN / total_actual_1
        Pfp = FP / total_actual_0
        Ptp = 1 - Pfn
        
        FPR.append(Pfp)
        TPR.append(Ptp)
        
    return FPR, TPR


# ======================================================
# Utils functions for multiclass problems
# ======================================================

def compute_optimal_bayes_multiclass(logSPost, Cost):
    """
    Computes optimal Bayes decisions for multiclass tasks.
    (Suggestion 1: bC = C * bP, optimal class = argmin over axis 0)
    """
    P = numpy.exp(logSPost)
    expected_costs = numpy.dot(Cost, P)
    predictions = numpy.argmin(expected_costs, axis=0)
    return predictions

def compute_empirical_Bayes_risk_multiclass(M, prior_array, Cost):
    """
    Computes the un-normalized empirical Bayes risk (DCF_u) from a multiclass confusion matrix.
    (Suggestion 3: R = M / sum(M), DCF_u = sum(prior * sum(R * Cost)))
    """
    # Prevent division by zero warnings if a true class is entirely missing
    col_sums = numpy.sum(M, axis=0)
    col_sums[col_sums == 0] = 1
    
    # Compute mis-classification ratios R
    R = M / col_sums
    
    DCF_u = 0
    num_classes = M.shape[0]
    for j in range(num_classes):
        for i in range(num_classes):
            DCF_u += prior_array[j] * R[i, j] * Cost[i, j]
            
    return DCF_u

def compute_normalised_empirical_Bayes_risk_multiclass(M, prior_array, Cost):
    """
    Computes the normalized empirical Bayes risk (DCF_n) for multiclass problems.
    (Suggestion 2: Dummy system cost = min(Cost * vPrior))
    """
    DCF_u = compute_empirical_Bayes_risk_multiclass(M, prior_array, Cost)
    
    # Convert prior to a column vector for the dummy system calculation
    vPrior = prior_array.reshape(-1, 1)
    
    # Compute the cost of a "dummy" system that relies strictly on priors
    dummy_cost = numpy.min(numpy.dot(Cost, vPrior))
    
    DCF_norm = DCF_u / dummy_cost
    return DCF_norm
