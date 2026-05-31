import numpy
import numpy as np
import scipy.optimize

from utils.bayes_utils import vcol, vrow

# ==========================================
# PRIOR-WEIGHTED LOGISTIC REGRESSION FOR CALIBRATION
# ==========================================

def train_calibration(scores, labels, pi_T):
    """
    Train a prior-weighted logistic regression model (non-regularized) for calibration and fusion.
    Args:
        scores: 1D array of scores (or 2D array for fusion: m x N)
        labels: 1D array of labels
        pi_T: target application prior
    Return:
        alpha (np.ndarray): weights
        beta (float): bias
    """
    # 1. DATA PREPARATION & PRE-PROCESSING
    if scores.ndim == 1:
        scores = vrow(scores)
    
    ZTR = labels * 2.0 - 1.0 # Maps 1/0 to 1/-1
    
    # 2. WEIGHT CALCULATION
    wTar = pi_T / (ZTR > 0).sum() # Compute the weight for the target class (class 1) by dividing the target prior by the number of target samples
    wNon = (1 - pi_T) / (ZTR < 0).sum() # Compute the weight for the non-target class (class -1) by dividing the non-target prior by the number of non-target samples

    # 3. LOSS FUNCTION & GRADIENT (using L-BFGS-B)
    def logreg_obj_with_grad(v):
        w = v[:-1]
        b = v[-1]
        s = numpy.dot(vcol(w).T, scores).ravel() + b # Compute the linear score by taking the dot product of the weights and the scores, and adding the bias

        loss = numpy.logaddexp(0, -ZTR * s) # Compute the loss by taking the logarithm of 1 + exp(-ZTR * s)
        loss[ZTR > 0] *= wTar # Apply the weight for the target class (class 1)
        loss[ZTR < 0] *= wNon # Apply the weight for the non-target class (class -1)

        G = -ZTR / (1.0 + numpy.exp(ZTR * s)) # Compute the gradient of the loss with respect to the scores
        G[ZTR > 0] *= wTar # Apply the weight for the target class (class 1)
        G[ZTR < 0] *= wNon # Apply the weight for the non-target class (class -1)

        GW = (vrow(G) * scores).sum(1) # Compute the gradient of the loss with respect to the weights
        Gb = G.sum() # Compute the gradient of the loss with respect to the bias
        return loss.sum(), numpy.hstack([GW, numpy.array(Gb)])

    # 4. OPTIMIZATION (L-BFGS-B)
    # Use L-BFGS-B optimization algorithm to find the optimal weights and bias that minimize the loss function
    vf = scipy.optimize.fmin_l_bfgs_b(logreg_obj_with_grad, x0=numpy.zeros(scores.shape[0] + 1))[0]
    alpha = vf[:-1]
    beta = vf[-1]
    
    return alpha, beta

def apply_calibration(scores, alpha, beta, pi_T):
    """
    Applies the estimated calibration parameters to scores to produce LLRs.
    Args:
        scores: 1D array of scores (or 2D array for fusion: m x N)
        alpha (np.ndarray): weights
        beta (float): bias
        pi_T: target application prior
    Return:
        calibrated_scores (np.ndarray): calibrated scores
    """
    if scores.ndim == 1:
        scores = vrow(scores)

    # gamma is the offset to apply to the calibrated scores, that makes the probability of the first class equal to pi_T
    gamma = beta - numpy.log(pi_T / (1 - pi_T))
    calibrated_scores = (numpy.transpose(vcol(alpha)) @ scores).ravel() + gamma
    return calibrated_scores


# ==========================================
# K-fold Calibration
# ==========================================

def kfold_calibrate(scores_arr, labels_arr, K, pi_T=0.5):
    calibrated_folds = []
    labels_folds = []
    for i in range(K): # Iterate over folds 
        # Split data into training and validation sets
        val_idx = numpy.arange(i, len(scores_arr), K)
        train_idx = numpy.delete(numpy.arange(len(scores_arr)), val_idx)
        
        # Train and calibrate on the training set
        s_train = scores_arr[train_idx]
        l_train = labels_arr[train_idx]
        s_val = scores_arr[val_idx]
        l_val = labels_arr[val_idx]
        
        alpha, beta = train_calibration(s_train, l_train, pi_T)
        cal_val = apply_calibration(s_val, alpha, beta, pi_T)
        
        calibrated_folds.append(cal_val)
        labels_folds.append(l_val)
        
    return numpy.hstack(calibrated_folds), numpy.hstack(labels_folds)


# ==========================================
# K-fold Fusion
# ==========================================

def kfold_fusion(s1, s2, labels_arr, K, pi_T=0.5):
    cal_folds = []
    l_folds = []

    # for each fold
    for i in range(K):
        # Split data into training and validation sets
        val_idx = numpy.arange(i, len(s1), K)
        train_idx = numpy.delete(numpy.arange(len(s1)), val_idx)
        
        # concatenate the scores of the two models in the training and validation sets
        train_fus = numpy.vstack([s1[train_idx], s2[train_idx]])
        val_fus = numpy.vstack([s1[val_idx], s2[val_idx]])
        
        l_train = labels_arr[train_idx]
        l_val = labels_arr[val_idx]
        
        # train and apply calibration 
        alpha, beta = train_calibration(train_fus, l_train, pi_T)
        cal_val = apply_calibration(val_fus, alpha, beta, pi_T)
        
        cal_folds.append(cal_val)
        l_folds.append(l_val)
        
    return numpy.hstack(cal_folds), numpy.hstack(l_folds)