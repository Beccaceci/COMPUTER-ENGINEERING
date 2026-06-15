import numpy as np
import scipy.optimize
from utils.math_utils import vcol, vrow

def trainWeightedLogRegBinary(DTR, LTR, l, pT):
    """
    Trains a weighted binary Logistic Regression model.
    Weights are applied to correct for differences between empirical 
    training priors and the target application prior.
    
    Args:
        DTR: Training data (features x samples).
        LTR: Training labels (0 and 1).
        l: Regularization parameter (lambda).
        pT: Target application prior probability.
        
    Returns:
        w: Learned weight vector.
        b: Learned bias term.
    """
    # Map labels to {-1, 1}
    ZTR = LTR * 2.0 - 1.0 
    
    # Calculate weights for target and non-target classes
    wTar = pT / (ZTR > 0).sum() 
    wNon = (1 - pT) / (ZTR < 0).sum()

    def logreg_obj_with_grad(v): 
        w = v[:-1]
        b = v[-1]
        s = np.dot(vcol(w).T, DTR).ravel() + b

        # Compute objective function
        loss = np.logaddexp(0, -ZTR * s)
        loss[ZTR > 0] *= wTar 
        loss[ZTR < 0] *= wNon
        
        # Compute gradient
        G = -ZTR / (1.0 + np.exp(ZTR * s))
        G[ZTR > 0] *= wTar 
        G[ZTR < 0] *= wNon
        
        GW = (vrow(G) * DTR).sum(1) + l * w.ravel()
        Gb = G.sum()
        
        obj = loss.sum() + l / 2 * np.linalg.norm(w)**2
        grad = np.hstack([GW, np.array(Gb)])
        return obj, grad

    # Optimize using L-BFGS-B
    vf = scipy.optimize.fmin_l_bfgs_b(logreg_obj_with_grad, x0=np.zeros(DTR.shape[0] + 1))[0]
    return vf[:-1], vf[-1]

def train_and_eval_project_lr(DTR_centered, LTR, DVAL_centered, D_eval_centered, pi_T):
    """
    Trains the Logistic Regression model for the project part and evaluates it.
    Returns:
        s_val_lr: scores on validation set
        s_eval_lr: scores on evaluation set
    """
    # Train weighted logistic regression model with regularization parameter lambda = 1e-3
    # pi_T is the target application prior probability, used to correct for differences between empirical training priors and the target application prior.
    w_lr, b_lr = trainWeightedLogRegBinary(DTR_centered, LTR, 1e-3, pi_T)
    
    # Apply model to validation and evaluation sets
    s_val_lr = (w_lr.T @ DVAL_centered + b_lr).ravel()
    s_eval_lr = (w_lr.T @ D_eval_centered + b_lr).ravel()
    return s_val_lr, s_eval_lr

def quadratic_feature_expansion(D):
    """
    Expands the feature space to include quadratic terms.
    For each column x, creates phi(x) = [vec(x * x.T), x]
    """
    D_expanded = []
    for i in range(D.shape[1]):
        x = D[:, i:i+1]
        # Compute xxT, flatten it, and concatenate with the original x
        xxT = np.dot(x, x.T).flatten()
        phi_x = np.concatenate([xxT, x.flatten()])
        D_expanded.append(phi_x)
    return np.column_stack(D_expanded)

def train_and_eval_project_quad_lr(DTR_centered, LTR, DVAL_centered, D_eval_centered, pi_T):
    """
    Trains the Quadratic Logistic Regression model for the project part and evaluates it.
    Returns:
        s_val_lr: scores on validation set
        s_eval_lr: scores on evaluation set
    """
    DTR_expanded = quadratic_feature_expansion(DTR_centered)
    DVAL_expanded = quadratic_feature_expansion(DVAL_centered)
    D_eval_expanded = quadratic_feature_expansion(D_eval_centered)
    
    # Train weighted logistic regression model with regularization parameter lambda = 3.16e-2 (optimal from LAB07)
    # pi_T is the target application prior probability
    w_lr, b_lr = trainWeightedLogRegBinary(DTR_expanded, LTR, 3.16e-2, pi_T)
    
    # Apply model to validation and evaluation sets
    s_val_lr = (w_lr.T @ DVAL_expanded + b_lr).ravel()
    s_eval_lr = (w_lr.T @ D_eval_expanded + b_lr).ravel()
    return s_val_lr, s_eval_lr