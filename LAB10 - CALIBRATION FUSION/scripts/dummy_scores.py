import sys
import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# Add the parent directory to the path so we can import modules
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.bayes_utils import compute_minDCF_binary_fast, compute_actDCF_binary_fast, compute_bayes_error_data
from utils.plot_utils import plot_bayes_errors_multi
from model.calibration import train_calibration, apply_calibration, kfold_calibrate, kfold_fusion

if __name__ == "__main__":
    # Setup directories
    ROOT = Path(__file__).resolve().parent.parent
    data_dir = ROOT / "data" / "iris"
    results_dir = ROOT / "results" / "dummy_scores"
    plots_dir = results_dir / "plots"
    logs_dir = results_dir / "logs"
    plots_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)
    
    # Load raw scores
    scores_1 = np.load(data_dir / "scores_1.npy")
    scores_2 = np.load(data_dir / "scores_2.npy")
    labels = np.load(data_dir / "labels.npy")
    
    eval_scores_1 = np.load(data_dir / "eval_scores_1.npy")
    eval_scores_2 = np.load(data_dir / "eval_scores_2.npy")
    eval_labels = np.load(data_dir / "eval_labels.npy")
    
    # Setup logger
    log_file = logs_dir / "dummy_scores_log.txt"
    with open(log_file, "w") as f:
        f.write("LAB 10: CALIBRATION AND FUSION (Dummy Data)\n")
        f.write("=" * 60 + "\n\n")
        
    def emit(text=""):
        print(text)
        with open(log_file, "a") as f:
            f.write(str(text) + "\n")

    pi_T = 0.2
    
    # ==========================================
    # 1. Raw Scores
    # ==========================================
    emit("--- 1. Raw Scores (Full Dataset) ---")
    min_1 = compute_minDCF_binary_fast(scores_1, labels, pi_T, 1.0, 1.0)
    act_1 = compute_actDCF_binary_fast(scores_1, labels, pi_T, 1.0, 1.0)
    min_2 = compute_minDCF_binary_fast(scores_2, labels, pi_T, 1.0, 1.0)
    act_2 = compute_actDCF_binary_fast(scores_2, labels, pi_T, 1.0, 1.0)
    
    emit(f"System 1 - minDCF: {min_1:.3f}, actDCF: {act_1:.3f}")
    emit(f"System 2 - minDCF: {min_2:.3f}, actDCF: {act_2:.3f}")
    
    x, min_1_list, act_1_list = compute_bayes_error_data(scores_1, labels)
    _, min_2_list, act_2_list = compute_bayes_error_data(scores_2, labels)
    
    plot_bayes_errors_multi(x, {
        'System 1': {'min_dcf': min_1_list, 'act_dcf': act_1_list},
        'System 2': {'min_dcf': min_2_list, 'act_dcf': act_2_list}
    }, "Single fold - actual and minimum DCF of original raw scores - full dataset", plots_dir / "raw_scores_bayes.png")
    
    # ==========================================
    # 2. Single-fold Calibration
    # ==========================================
    emit("\n--- 2. Single-fold Calibration ---")
    
    # Split
    s_train_1 = scores_1[::3]
    s_val_1 = np.hstack([scores_1[1::3], scores_1[2::3]])
    
    s_train_2 = scores_2[::3]
    s_val_2 = np.hstack([scores_2[1::3], scores_2[2::3]])
    
    l_train = labels[::3]
    l_val = np.hstack([labels[1::3], labels[2::3]])
    
    # Raw scores on validation split
    emit("Validation Dataset (Raw):")
    min_1_val = compute_minDCF_binary_fast(s_val_1, l_val, pi_T, 1.0, 1.0)
    act_1_val = compute_actDCF_binary_fast(s_val_1, l_val, pi_T, 1.0, 1.0)
    min_2_val = compute_minDCF_binary_fast(s_val_2, l_val, pi_T, 1.0, 1.0)
    act_2_val = compute_actDCF_binary_fast(s_val_2, l_val, pi_T, 1.0, 1.0)
    emit(f"System 1 - minDCF: {min_1_val:.3f}, actDCF: {act_1_val:.3f}")
    emit(f"System 2 - minDCF: {min_2_val:.3f}, actDCF: {act_2_val:.3f}")
    
    # Train and calibrate
    alpha_1, beta_1 = train_calibration(s_train_1, l_train, pi_T)
    cal_val_1 = apply_calibration(s_val_1, alpha_1, beta_1, pi_T)
    
    alpha_2, beta_2 = train_calibration(s_train_2, l_train, pi_T)
    cal_val_2 = apply_calibration(s_val_2, alpha_2, beta_2, pi_T)
    
    # Calibrated scores on validation set
    emit("Validation Dataset (Calibrated):")
    cmin_1_val = compute_minDCF_binary_fast(cal_val_1, l_val, pi_T, 1.0, 1.0)
    cact_1_val = compute_actDCF_binary_fast(cal_val_1, l_val, pi_T, 1.0, 1.0)
    cmin_2_val = compute_minDCF_binary_fast(cal_val_2, l_val, pi_T, 1.0, 1.0)
    cact_2_val = compute_actDCF_binary_fast(cal_val_2, l_val, pi_T, 1.0, 1.0)
    emit(f"System 1 - minDCF: {cmin_1_val:.3f}, actDCF: {cact_1_val:.3f}")
    emit(f"System 2 - minDCF: {cmin_2_val:.3f}, actDCF: {cact_2_val:.3f}")
    
    # Plots for System 1 & 2 (calibrated vs raw on validation)
    _, rmin_1_v, ract_1_v = compute_bayes_error_data(s_val_1, l_val)
    _, cmin_1_v, cact_1_v = compute_bayes_error_data(cal_val_1, l_val)
    plot_bayes_errors_multi(x, {
        'pre-cal.': {'min_dcf': rmin_1_v, 'act_dcf': ract_1_v, 'style': ':'},
        'cal.': {'min_dcf': None, 'act_dcf': cact_1_v, 'style': '-'}
    }, "System 1 - Validation (Single-fold)", plots_dir / "sys1_singlefold_val.png")
    
    _, rmin_2_v, ract_2_v = compute_bayes_error_data(s_val_2, l_val)
    _, cmin_2_v, cact_2_v = compute_bayes_error_data(cal_val_2, l_val)
    plot_bayes_errors_multi(x, {
        'pre-cal.': {'min_dcf': rmin_2_v, 'act_dcf': ract_2_v, 'style': ':'},
        'cal.': {'min_dcf': None, 'act_dcf': cact_2_v, 'style': '-'}
    }, "System 2 - Validation (Single-fold)", plots_dir / "sys2_singlefold_val.png")
    
    # Evaluate on Evaluation set
    emit("\nEvaluation Dataset (Raw):")
    emin_1 = compute_minDCF_binary_fast(eval_scores_1, eval_labels, pi_T, 1.0, 1.0)
    eact_1 = compute_actDCF_binary_fast(eval_scores_1, eval_labels, pi_T, 1.0, 1.0)
    emin_2 = compute_minDCF_binary_fast(eval_scores_2, eval_labels, pi_T, 1.0, 1.0)
    eact_2 = compute_actDCF_binary_fast(eval_scores_2, eval_labels, pi_T, 1.0, 1.0)
    emit(f"System 1 - minDCF: {emin_1:.3f}, actDCF: {eact_1:.3f}")
    emit(f"System 2 - minDCF: {emin_2:.3f}, actDCF: {eact_2:.3f}")
    
    cal_eval_1 = apply_calibration(eval_scores_1, alpha_1, beta_1, pi_T)
    cal_eval_2 = apply_calibration(eval_scores_2, alpha_2, beta_2, pi_T)
    
    emit("Evaluation Dataset (Calibrated - Single Fold Model):")
    ce_min_1 = compute_minDCF_binary_fast(cal_eval_1, eval_labels, pi_T, 1.0, 1.0)
    ce_act_1 = compute_actDCF_binary_fast(cal_eval_1, eval_labels, pi_T, 1.0, 1.0)
    ce_min_2 = compute_minDCF_binary_fast(cal_eval_2, eval_labels, pi_T, 1.0, 1.0)
    ce_act_2 = compute_actDCF_binary_fast(cal_eval_2, eval_labels, pi_T, 1.0, 1.0)
    emit(f"System 1 - minDCF: {ce_min_1:.3f}, actDCF: {ce_act_1:.3f}")
    emit(f"System 2 - minDCF: {ce_min_2:.3f}, actDCF: {ce_act_2:.3f}")
    
    _, remin_1, react_1 = compute_bayes_error_data(eval_scores_1, eval_labels)
    _, cemin_1, ceact_1 = compute_bayes_error_data(cal_eval_1, eval_labels)
    plot_bayes_errors_multi(x, {
        'pre-cal.': {'min_dcf': remin_1, 'act_dcf': react_1, 'style': ':'},
        'cal.': {'min_dcf': None, 'act_dcf': ceact_1, 'style': '-'}
    }, "System 1 - Evaluation (Single-fold)", plots_dir / "sys1_singlefold_eval.png")
    
    _, remin_2, react_2 = compute_bayes_error_data(eval_scores_2, eval_labels)
    _, cemin_2, ceact_2 = compute_bayes_error_data(cal_eval_2, eval_labels)
    plot_bayes_errors_multi(x, {
        'pre-cal.': {'min_dcf': remin_2, 'act_dcf': react_2, 'style': ':'},
        'cal.': {'min_dcf': None, 'act_dcf': ceact_2, 'style': '-'}
    }, "System 2 - Evaluation (Single-fold)", plots_dir / "sys2_singlefold_eval.png")

    # ==========================================
    # 3. K-Fold Calibration
    # ==========================================
    emit("\n--- 3. K-Fold Calibration (K=5) ---")
    K = 5
    
    # K-fold calibration for a given system
    kf_cal_1, kf_labels = kfold_calibrate(scores_1, labels, K=K, pi_T=pi_T)
    kf_cal_2, _ = kfold_calibrate(scores_2, labels, K=K, pi_T=pi_T)
    
    # Original scores aligned with K-fold pooled labels
    aligned_scores_1 = []
    aligned_scores_2 = []
    for i in range(K):
        val_idx = np.arange(i, len(scores_1), K)
        aligned_scores_1.append(scores_1[val_idx])
        aligned_scores_2.append(scores_2[val_idx])
    aligned_scores_1 = np.hstack(aligned_scores_1)
    aligned_scores_2 = np.hstack(aligned_scores_2)

    emit("Validation Dataset (K-fold Calibrated):")
    kmin_1 = compute_minDCF_binary_fast(kf_cal_1, kf_labels, pi_T, 1.0, 1.0)
    kact_1 = compute_actDCF_binary_fast(kf_cal_1, kf_labels, pi_T, 1.0, 1.0)
    kmin_2 = compute_minDCF_binary_fast(kf_cal_2, kf_labels, pi_T, 1.0, 1.0)
    kact_2 = compute_actDCF_binary_fast(kf_cal_2, kf_labels, pi_T, 1.0, 1.0)
    emit(f"System 1 - minDCF: {kmin_1:.3f}, actDCF: {kact_1:.3f}")
    emit(f"System 2 - minDCF: {kmin_2:.3f}, actDCF: {kact_2:.3f}")
    
    # Train final models on ALL scores
    alpha_1_f, beta_1_f = train_calibration(scores_1, labels, pi_T)
    alpha_2_f, beta_2_f = train_calibration(scores_2, labels, pi_T)
    
    # Apply final models to evaluation set
    kf_eval_1 = apply_calibration(eval_scores_1, alpha_1_f, beta_1_f, pi_T)
    kf_eval_2 = apply_calibration(eval_scores_2, alpha_2_f, beta_2_f, pi_T)
    
    emit("Evaluation Dataset (Calibrated - K-Fold Final Model):")
    kfe_min_1 = compute_minDCF_binary_fast(kf_eval_1, eval_labels, pi_T, 1.0, 1.0)
    kfe_act_1 = compute_actDCF_binary_fast(kf_eval_1, eval_labels, pi_T, 1.0, 1.0)
    kfe_min_2 = compute_minDCF_binary_fast(kf_eval_2, eval_labels, pi_T, 1.0, 1.0)
    kfe_act_2 = compute_actDCF_binary_fast(kf_eval_2, eval_labels, pi_T, 1.0, 1.0)
    emit(f"System 1 - minDCF: {kfe_min_1:.3f}, actDCF: {kfe_act_1:.3f}")
    emit(f"System 2 - minDCF: {kfe_min_2:.3f}, actDCF: {kfe_act_2:.3f}")
    
    _, kremin_1, kreact_1 = compute_bayes_error_data(aligned_scores_1, kf_labels)
    _, kcmin_1, kcact_1 = compute_bayes_error_data(kf_cal_1, kf_labels)
    plot_bayes_errors_multi(x, {
        'pre-cal.': {'min_dcf': kremin_1, 'act_dcf': kreact_1, 'style': ':'},
        'cal.': {'min_dcf': None, 'act_dcf': kcact_1, 'style': '-'}
    }, "System 1 - Validation (K-fold)", plots_dir / "sys1_kfold_val.png")

    # ==========================================
    # 4. Score-Level Fusion
    # ==========================================
    emit("\n--- 4. Score-Level Fusion ---")
    
    # 4.1 Single-Fold Fusion
    fusion_train = np.vstack([s_train_1, s_train_2])
    fusion_val = np.vstack([s_val_1, s_val_2])
    
    # Train and calibrate fusion model
    alpha_fus, beta_fus = train_calibration(fusion_train, l_train, pi_T)
    cal_val_fus = apply_calibration(fusion_val, alpha_fus, beta_fus, pi_T)
    
    # Evaluate fusion model on validation set
    emit("Validation Dataset (Single-Fold Fusion):")
    sf_min_fus = compute_minDCF_binary_fast(cal_val_fus, l_val, pi_T, 1.0, 1.0)
    sf_act_fus = compute_actDCF_binary_fast(cal_val_fus, l_val, pi_T, 1.0, 1.0)
    emit(f"Fusion - minDCF: {sf_min_fus:.3f}, actDCF: {sf_act_fus:.3f}")
    
    fusion_eval = np.vstack([eval_scores_1, eval_scores_2])
    cal_eval_fus = apply_calibration(fusion_eval, alpha_fus, beta_fus, pi_T)
    
    emit("Evaluation Dataset (Single-Fold Fusion):")
    ef_min_fus = compute_minDCF_binary_fast(cal_eval_fus, eval_labels, pi_T, 1.0, 1.0)
    ef_act_fus = compute_actDCF_binary_fast(cal_eval_fus, eval_labels, pi_T, 1.0, 1.0)
    emit(f"Fusion - minDCF: {ef_min_fus:.3f}, actDCF: {ef_act_fus:.3f}")
    
    
    kf_cal_fus, kf_labels_fus = kfold_fusion(scores_1, scores_2, labels)
    
    emit("\nValidation Dataset (K-Fold Fusion):")
    kf_min_fus = compute_minDCF_binary_fast(kf_cal_fus, kf_labels_fus, pi_T, 1.0, 1.0)
    kf_act_fus = compute_actDCF_binary_fast(kf_cal_fus, kf_labels_fus, pi_T, 1.0, 1.0)
    emit(f"Fusion - minDCF: {kf_min_fus:.3f}, actDCF: {kf_act_fus:.3f}")
    
    # Final model for Evaluation
    alpha_fus_f, beta_fus_f = train_calibration(np.vstack([scores_1, scores_2]), labels, pi_T)
    kfe_cal_fus = apply_calibration(fusion_eval, alpha_fus_f, beta_fus_f, pi_T)
    
    emit("Evaluation Dataset (K-Fold Final Model Fusion):")
    kfe_min_fus = compute_minDCF_binary_fast(kfe_cal_fus, eval_labels, pi_T, 1.0, 1.0)
    kfe_act_fus = compute_actDCF_binary_fast(kfe_cal_fus, eval_labels, pi_T, 1.0, 1.0)
    emit(f"Fusion - minDCF: {kfe_min_fus:.3f}, actDCF: {kfe_act_fus:.3f}")

    # Plot Single-Fold Fusion
    _, s1_min, s1_act = compute_bayes_error_data(cal_val_1, l_val)
    _, s2_min, s2_act = compute_bayes_error_data(cal_val_2, l_val)
    _, fus_min, fus_act = compute_bayes_error_data(cal_val_fus, l_val)
    plot_bayes_errors_multi(x, {
        'S1 - actDCF': {'min_dcf': s1_min, 'act_dcf': s1_act},
        'S2 - actDCF': {'min_dcf': s2_min, 'act_dcf': s2_act},
        'Fusion - actDCF': {'min_dcf': fus_min, 'act_dcf': fus_act}
    }, "Single fold - score-level fusion (Validation)", results_dir / "singlefold_fusion_val.png")

    # Plot K-Fold Fusion
    _, ks1_min, ks1_act = compute_bayes_error_data(kf_cal_1, kf_labels)
    _, ks2_min, ks2_act = compute_bayes_error_data(kf_cal_2, kf_labels)
    _, kfus_min, kfus_act = compute_bayes_error_data(kf_cal_fus, kf_labels_fus)
    plot_bayes_errors_multi(x, {
        'S1 - actDCF': {'min_dcf': ks1_min, 'act_dcf': ks1_act},
        'S2 - actDCF': {'min_dcf': ks2_min, 'act_dcf': ks2_act},
        'Fusion - actDCF': {'min_dcf': kfus_min, 'act_dcf': kfus_act}
    }, "K-fold - score-level fusion (Validation)", results_dir / "kfold_fusion_val.png")
