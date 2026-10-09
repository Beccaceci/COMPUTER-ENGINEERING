import sys
from pathlib import Path
import numpy as np
import scipy.special

# Setup Paths
ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))
sys.path.append(str(ROOT.parent / "LAB08 - SUPPORT VECTOR MACHINES"))
sys.path.append(str(ROOT.parent / "LAB09 - GMM"))

from utils.data_loaders import load_dataset, split_dataset
from utils.bayes_utils import compute_minDCF_binary_fast, compute_actDCF_binary_fast

# Import Classifiers from previous labs
import scipy.optimize
def vcol(x): return x.reshape((x.size, 1))
def vrow(x): return x.reshape((1, x.size))

def trainWeightedLogRegBinary(DTR, LTR, l, pT):
    ZTR = LTR * 2.0 - 1.0 
    wTar = pT / (ZTR>0).sum() 
    wNon = (1-pT) / (ZTR<0).sum()
    def logreg_obj_with_grad(v): 
        w = v[:-1]
        b = v[-1]
        s = np.dot(vcol(w).T, DTR).ravel() + b
        loss = np.logaddexp(0, -ZTR * s)
        loss[ZTR>0] *= wTar 
        loss[ZTR<0] *= wNon
        G = -ZTR / (1.0 + np.exp(ZTR * s))
        G[ZTR > 0] *= wTar 
        G[ZTR < 0] *= wNon
        GW = (vrow(G) * DTR).sum(1) + l * w.ravel()
        Gb = G.sum()
        return loss.sum() + l / 2 * np.linalg.norm(w)**2, np.hstack([GW, np.array(Gb)])
    vf = scipy.optimize.fmin_l_bfgs_b(logreg_obj_with_grad, x0 = np.zeros(DTR.shape[0]+1))[0]
    return vf[:-1], vf[-1]

from models.kernelSVM import train_kernel_svm
from utils.math_utils import radial_basis_kernel

from GMMmodel.gmm_lbg import LBG_algorithm_tied
from GMMmodel.gmm_em import EM_algorithm_tied
from GMMmodel.gmm_core import compute_log_joint, apply_eigenvalue_constraint

def train_gmm_lbg(X, n_components, LBG_split_func, EM_func, psi=0.01):
    mu = X.mean(axis=1, keepdims=True)
    C = np.cov(X, bias=True)
    C = apply_eigenvalue_constraint(C, psi)
    gmm = [(1.0, mu, C)]
    gmm = EM_func(X, gmm, psi=psi)
    current_c = 1
    while current_c < n_components:
        gmm = LBG_split_func(gmm, psi=psi)
        gmm = EM_func(X, gmm, psi=psi)
        current_c *= 2
    return gmm

if __name__ == "__main__":
    data_dir = ROOT / "data" / "project"
    
    D_train, L_train = load_dataset(data_dir / "trainData.txt")
    D_eval, L_eval = load_dataset(data_dir / "evalData.txt")
    
    (DTR, LTR), (DVAL, LVAL) = split_dataset(D_train, L_train, 2/3)
    
    mu_train = DTR.mean(axis=1, keepdims=True)
    DTR_c = DTR - mu_train
    DVAL_c = DVAL - mu_train
    D_eval_c = D_eval - mu_train
    
    # Train Logistic Regression
    w_lr, b_lr = trainWeightedLogRegBinary(DTR_c, LTR, 1e-3, 0.1)
    s_eval_lr = (w_lr.T @ D_eval_c + b_lr).ravel()
    
    # Train SVM
    ZTR = LTR * 2 - 1
    alpha_opt, _, _, _ = train_kernel_svm(DTR_c, ZTR, C=1.0, K_bias=1.0, kernel_type="rbf", gamma=1e-2)
    K_eval = radial_basis_kernel(DTR_c, D_eval_c, gamma=1e-2) + 1.0
    s_eval_svm = ((alpha_opt * ZTR) @ K_eval).ravel()
    
    # Train GMM
    gmm0 = train_gmm_lbg(DTR_c[:, LTR == 0], 8, LBG_algorithm_tied, EM_algorithm_tied)
    gmm1 = train_gmm_lbg(DTR_c[:, LTR == 1], 8, LBG_algorithm_tied, EM_algorithm_tied)
    S0_eval = scipy.special.logsumexp(compute_log_joint(D_eval_c, gmm0), axis=0)
    S1_eval = scipy.special.logsumexp(compute_log_joint(D_eval_c, gmm1), axis=0)
    s_eval_gmm = S1_eval - S0_eval
    
    # Get validation scores for calibration
    s_val_lr = (w_lr.T @ DVAL_c + b_lr).ravel()
    K_val = radial_basis_kernel(DTR_c, DVAL_c, gamma=1e-2) + 1.0
    s_val_svm = ((alpha_opt * ZTR) @ K_val).ravel()
    S0_val = scipy.special.logsumexp(compute_log_joint(DVAL_c, gmm0), axis=0)
    S1_val = scipy.special.logsumexp(compute_log_joint(DVAL_c, gmm1), axis=0)
    s_val_gmm = S1_val - S0_val
    
    raw_val_scores = {"LR": s_val_lr, "SVM": s_val_svm, "GMM": s_val_gmm}
    raw_eval_scores = {"LR": s_eval_lr, "SVM": s_eval_svm, "GMM": s_eval_gmm}
    
    from model.calibration import train_calibration, apply_calibration
    cal_eval_scores = {}
    for name in raw_val_scores:
        alpha_f, beta_f = train_calibration(raw_val_scores[name], LVAL, 0.1)
        c_eval = apply_calibration(raw_eval_scores[name], alpha_f, beta_f, 0.1)
        cal_eval_scores[name] = c_eval
    
    print(f"{'Model':<10} | {'Prior':<5} | {'Raw minD':<8} | {'Raw actD':<8} | {'Cal minD':<8} | {'Cal actD':<8}")
    print("-" * 65)
    for name in raw_eval_scores:
        for pi in [0.1, 0.5, 0.9]:
            r_min = compute_minDCF_binary_fast(raw_eval_scores[name], L_eval, pi, 1.0, 1.0)
            r_act = compute_actDCF_binary_fast(raw_eval_scores[name], L_eval, pi, 1.0, 1.0)
            c_min = compute_minDCF_binary_fast(cal_eval_scores[name], L_eval, pi, 1.0, 1.0)
            c_act = compute_actDCF_binary_fast(cal_eval_scores[name], L_eval, pi, 1.0, 1.0)
            print(f"{name:<10} | {pi:<5.1f} | {r_min:<8.4f} | {r_act:<8.4f} | {c_min:<8.4f} | {c_act:<8.4f}")

    # Fusion
    import numpy as np
    S_val_all = np.vstack([raw_val_scores["LR"], raw_val_scores["SVM"], raw_val_scores["GMM"]])
    S_eval_all = np.vstack([raw_eval_scores["LR"], raw_eval_scores["SVM"], raw_eval_scores["GMM"]])
    
    alpha_fus, beta_fus = train_calibration(S_val_all, LVAL, 0.1)
    fus_eval_scores = apply_calibration(S_eval_all, alpha_fus, beta_fus, 0.1)
    
    print("\n--- FUSION RESULTS ---")
    print(f"{'Model':<10} | {'Prior':<5} | {'Fusion minD':<11} | {'Fusion actD':<11}")
    print("-" * 45)
    for pi in [0.1, 0.5, 0.9]:
        f_min = compute_minDCF_binary_fast(fus_eval_scores, L_eval, pi, 1.0, 1.0)
        f_act = compute_actDCF_binary_fast(fus_eval_scores, L_eval, pi, 1.0, 1.0)
        print(f"{'Fusion':<10} | {pi:<5.1f} | {f_min:<11.4f} | {f_act:<11.4f}")

