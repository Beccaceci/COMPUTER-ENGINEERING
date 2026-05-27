import numpy
import scipy.special

# ======================================================
# Utils functions for binary problems
# ======================================================

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