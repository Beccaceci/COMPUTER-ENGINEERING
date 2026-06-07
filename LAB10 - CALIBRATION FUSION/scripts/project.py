import sys
from pathlib import Path
import numpy as np

# Add the parent directory to the path so we can import modules
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.data_loaders import load_dataset, split_dataset
from utils.bayes_utils import compute_minDCF_binary_fast, compute_actDCF_binary_fast, compute_bayes_error_data
from models.calibration import train_calibration, apply_calibration, kfold_calibrate, kfold_fusion
from utils.plot_utils import plot_bayes_errors_multi
from utils.math_utils import vcol, vrow

# Models
from models.logistic_regression import train_and_eval_project_lr
from models.svm import train_and_eval_project_svm
from models.gmm import train_and_eval_project_gmm
from utils.io_utils import create_emitter

if __name__ == "__main__":
    # Setup Paths
    ROOT = Path(__file__).resolve().parent.parent
    
    # Setup directories
    data_dir = ROOT / "data" / "project"
    results_dir = ROOT / "results" / "project"
    plots_dir = results_dir / "plots"
    logs_dir = results_dir / "logs"
    plots_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = logs_dir / "calibration_fusion_results.txt"
    emit = create_emitter(output_file, title="LAB 10: SCORE CALIBRATION AND FUSION")

    # ==========================================
    # 1. LOAD DATA & GENERATE BASE SCORES
    # ==========================================
    emit("Loading Data and generating base model scores...")
    D, L = load_dataset(data_dir / "trainData.txt")
    
    # Assuming we split train/val and also have a separate eval set. 
    # For project context, we typically split trainData into DTR/DVAL to train the calibrator,
    # and use evalData for the final evaluation. 
    # (Adjust this split exactly to match your data_loaders logic)
    (DTR, LTR), (DVAL, LVAL) = split_dataset(D, L, percTrain=2.0 / 3.0)
    D_eval, L_eval = load_dataset(data_dir / "evalData.txt")

    # Center data using DTR mean
    mu_train = DTR.mean(axis=1, keepdims=True)
    DTR_c = DTR - mu_train
    DVAL_c = DVAL - mu_train
    D_eval_c = D_eval - mu_train

    # Generate scores using optimal hyperparameters from previous labs
    S_val_lr, S_eval_lr = train_and_eval_project_lr(DTR_c, LTR, DVAL_c, D_eval_c, 0.5) # train and eval LR model for target prior 0.5
    S_val_svm, S_eval_svm = train_and_eval_project_svm(DTR_c, LTR, DVAL_c, D_eval_c) # train and eval SVM model for target prior 0.5
    S_val_gmm, S_eval_gmm = train_and_eval_project_gmm(DTR_c, LTR, DVAL_c, D_eval_c) # train and eval GMM model for target prior 0.5
    
    # Prepare array groupings for fusion
    S_val_all = np.vstack([S_val_svm, S_val_gmm]) # fusion of SVM and GMM scores
    S_eval_all = np.vstack([S_eval_svm, S_eval_gmm])

    # Target Applications
    target_priors = [0.1, 0.5, 0.9]

    # ==========================================
    # 2. EVALUATE ACROSS TARGET APPLICATIONS
    # ==========================================
    # Set cost of false negatives (Cfn) and false positives (Cfp)
    Cfn = Cfp = 1.0

    # Loop over target applications (priori probabilities)
    for pi_T in target_priors:
        emit("\n" + "="*80)
        emit(f"EVALUATING APPLICATION: Target Prior (pi_T) = {pi_T}")
        emit("="*80)

        # --- A. BASE MODEL EVALUATION (Uncalibrated) ---
        emit("\n--- Base Models (Uncalibrated Validation) ---")
        for name, s_val in [("LogReg", S_val_lr), ("SVM", S_val_svm), ("GMM", S_val_gmm)]:
            min_dcf = compute_minDCF_binary_fast(s_val, LVAL, pi_T, Cfn, Cfp) # compute min DCF for target prior pi_T
            act_dcf = compute_actDCF_binary_fast(s_val, LVAL, pi_T, Cfn, Cfp) # compute act DCF for target prior pi_T
            emit(f"{name:<10} -> Min DCF: {min_dcf:.3f} | Act DCF: {act_dcf:.3f}")

        # --- B. K-FOLD CALIBRATION EVALUATION ---
        emit("\n--- Calibrated Models (K-Fold Validation) ---")
        
        # FIX: explicitly name pi_T=pi_T and K=5 to prevent positional mismatches
        cal_val_lr, cal_labels_lr = kfold_calibrate(S_val_lr, LVAL, K=5, pi_T=pi_T) # k-fold calibration for target prior pi_T
        lr_cal_min = compute_minDCF_binary_fast(cal_val_lr, cal_labels_lr, pi_T, Cfn, Cfp) # compute min DCF for target prior pi_T
        lr_cal_act = compute_actDCF_binary_fast(cal_val_lr, cal_labels_lr, pi_T, Cfn, Cfp) # compute act DCF for target prior pi_T
        emit(f"LogReg     -> Min DCF: {lr_cal_min:.3f} | Act DCF: {lr_cal_act:.3f}")

        cal_val_svm, cal_labels_svm = kfold_calibrate(S_val_svm, LVAL, K=5, pi_T=pi_T) # k-fold calibration for target prior pi_T
        svm_cal_min = compute_minDCF_binary_fast(cal_val_svm, cal_labels_svm, pi_T, Cfn, Cfp) # compute min DCF for target prior pi_T
        svm_cal_act = compute_actDCF_binary_fast(cal_val_svm, cal_labels_svm, pi_T, Cfn, Cfp) # compute act DCF for target prior pi_T
        emit(f"SVM        -> Min DCF: {svm_cal_min:.3f} | Act DCF: {svm_cal_act:.3f}")

        cal_val_gmm, cal_labels_gmm = kfold_calibrate(S_val_gmm, LVAL, K=5, pi_T=pi_T) # k-fold calibration for target prior pi_T
        gmm_cal_min = compute_minDCF_binary_fast(cal_val_gmm, cal_labels_gmm, pi_T, Cfn, Cfp) # compute min DCF for target prior pi_T
        gmm_cal_act = compute_actDCF_binary_fast(cal_val_gmm, cal_labels_gmm, pi_T, Cfn, Cfp) # compute act DCF for target prior pi_T
        emit(f"GMM        -> Min DCF: {gmm_cal_min:.3f} | Act DCF: {gmm_cal_act:.3f}")

        # --- C. K-FOLD FUSION EVALUATION ---
        emit("\n--- Score-Level Fusion (K-Fold Validation) ---")
        fus_val_scores, fus_l = kfold_fusion(S_val_svm, S_val_gmm, LVAL, K=5, pi_T=pi_T) # k-fold fusion for target prior pi_T
        f_min = compute_minDCF_binary_fast(fus_val_scores, fus_l, pi_T, Cfn, Cfp) # compute min DCF for target prior pi_T
        f_act = compute_actDCF_binary_fast(fus_val_scores, fus_l, pi_T, Cfn, Cfp) # compute act DCF for target prior pi_T
        emit(f"SVM + GMM  -> Min DCF: {f_min:.3f} | Act DCF: {f_act:.3f}")

        # --- D. FINAL EVALUATION ON UNSEEN EVAL DATA (Trained on entire VAL set) ---
        emit("\n--- Final Evaluation Set Performance (Actual Deployable System) ---")
        
        # Train final calibrators/fusion using the ENTIRE validation set
        alpha_svm, beta_svm = train_calibration(S_val_svm, LVAL, pi_T) # train final calibrator for target prior pi_T
        svm_eval_cal = apply_calibration(S_eval_svm, alpha_svm, beta_svm, pi_T) # apply calibration for target prior pi_T
        se_min = compute_minDCF_binary_fast(svm_eval_cal, L_eval, pi_T, Cfn, Cfp) # compute min DCF for target prior pi_T
        se_act = compute_actDCF_binary_fast(svm_eval_cal, L_eval, pi_T, Cfn, Cfp) # compute act DCF for target prior pi_T
        emit(f"Calibrated SVM Evaluation -> Min DCF: {se_min:.3f} | Act DCF: {se_act:.3f}")
        
        alpha_gmm, beta_gmm = train_calibration(S_val_gmm, LVAL, pi_T) # train final calibrator for target prior pi_T
        gmm_eval_cal = apply_calibration(S_eval_gmm, alpha_gmm, beta_gmm, pi_T) # apply calibration for target prior pi_T
        ge_min = compute_minDCF_binary_fast(gmm_eval_cal, L_eval, pi_T, Cfn, Cfp) # compute min DCF for target prior pi_T
        ge_act = compute_actDCF_binary_fast(gmm_eval_cal, L_eval, pi_T, Cfn, Cfp) # compute act DCF for target prior pi_T
        emit(f"Calibrated GMM Evaluation -> Min DCF: {ge_min:.3f} | Act DCF: {ge_act:.3f}")

        alpha_fus, beta_fus = train_calibration(S_val_all, LVAL, pi_T) # train final calibrator for target prior pi_T
        fus_eval_scores = apply_calibration(S_eval_all, alpha_fus, beta_fus, pi_T) # apply calibration for target prior pi_T
        fe_min = compute_minDCF_binary_fast(fus_eval_scores, L_eval, pi_T, Cfn, Cfp) # compute min DCF for target prior pi_T
        fe_act = compute_actDCF_binary_fast(fus_eval_scores, L_eval, pi_T, Cfn, Cfp) # compute act DCF for target prior pi_T
        emit(f"Fused SVM+GMM Evaluation  -> Min DCF: {fe_min:.3f} | Act DCF: {fe_act:.3f}")

    # ==========================================
    # 3. BAYES ERROR PLOTS (Plotted across all pi)
    # ==========================================
    emit("\nGenerating Bayes Error plots for Calibration and Fusion...")
    
    # We use pi_T = 0.5 parameters to train the general calibrator for the plot
    alpha_svm, beta_svm = train_calibration(S_val_svm, LVAL, 0.5) # train final calibrator for target prior pi_T
    svm_eval_cal = apply_calibration(S_eval_svm, alpha_svm, beta_svm, 0.5) # apply calibration for target prior pi_T

    alpha_gmm, beta_gmm = train_calibration(S_val_gmm, LVAL, 0.5) # train final calibrator for target prior pi_T
    gmm_eval_cal = apply_calibration(S_eval_gmm, alpha_gmm, beta_gmm, 0.5) # apply calibration for target prior pi_T

    alpha_fus, beta_fus = train_calibration(S_val_all, LVAL, 0.5) # train final calibrator for target prior pi_T
    fus_eval_scores = apply_calibration(S_eval_all, alpha_fus, beta_fus, 0.5) # apply calibration for target prior pi_T

    # Compute data for plots
    effPriorLogOdds, f_eval_min, f_eval_act = compute_bayes_error_data(fus_eval_scores, L_eval) # compute bayes error data for target prior pi_T
    _, svm_eval_min, svm_eval_act = compute_bayes_error_data(svm_eval_cal, L_eval) # compute bayes error data for target prior pi_T
    _, gmm_eval_min, gmm_eval_act = compute_bayes_error_data(gmm_eval_cal, L_eval) # compute bayes error data for target prior pi_T

    # Plot SVM vs Fusion
    plot_bayes_errors_multi(
        effPriorLogOdds,
        {
            "SVM": {'min_dcf': svm_eval_min, 'act_dcf': svm_eval_act},
            "Fusion": {'min_dcf': f_eval_min, 'act_dcf': f_eval_act}
        },
        "Fusion vs SVM - Bayes Error",
        plots_dir / "Bayes_Error_Fusion_vs_SVM.png"
    )
    
    # Plot GMM vs Fusion
    plot_bayes_errors_multi(
        effPriorLogOdds,
        {
            "GMM": {'min_dcf': gmm_eval_min, 'act_dcf': gmm_eval_act},
            "Fusion": {'min_dcf': f_eval_min, 'act_dcf': f_eval_act}
        },
        "Fusion vs GMM - Bayes Error",
        plots_dir / "Bayes_Error_Fusion_vs_GMM.png"
    )
    print(f"\n[SUCCESS] Script execution complete! Results saved to {output_file.name}")