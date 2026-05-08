import numpy
from pathlib import Path

from utils.data_loaders import load_dataset, split_dataset
from utils.bayes_utils import compute_optimal_bayes_binary, compute_normalised_empirical_Bayes_risk_binary, compute_min_dcf
from utils.math_utils import compute_confusion_matrix
from utils.plot_utils import plot_dcf_vs_lambda
from models.logisticRegression import trainLogReg
from models.MVG import compute_mvg_loglikelihoods
from models.NaiveBayes import compute_naive_bayes_loglikelihoods
from models.TiedMVG import compute_tied_mvg_loglikelihoods

def quadratic_feature_expansion(D):
    """
    Expands the feature space to include quadratic terms.
    For each column x, creates phi(x) = [vec(x * x.T), x]
    """
    D_expanded = []
    for i in range(D.shape[1]):
        x = D[:, i:i+1]
        # Compute xxT, flatten it, and concatenate with the original x
        xxT = numpy.dot(x, x.T).flatten()
        phi_x = numpy.concatenate([xxT, x.flatten()])
        D_expanded.append(phi_x)
    return numpy.column_stack(D_expanded)

if __name__ == "__main__":
    ROOT = Path(".")
    
    # -----------------------------------------------------------------------
    # Setup paths
    # -----------------------------------------------------------------------
    dataset_dir = ROOT / "data" / "project" # Assume project data is here
    results_dir = ROOT / "results" / "project"
    plots_dir = results_dir / "plots"
    results_dir.mkdir(parents=True, exist_ok=True)
    plots_dir.mkdir(parents=True, exist_ok=True)

    # Define the output text file for logging
    output_path = results_dir / "project_evaluation.txt"
    
    # Clear the file at the start of the run
    with open(output_path, "w") as f:
        f.write("LAB 07: PROJECT LOGISTIC REGRESSION EVALUATION\n")
        f.write("=" * 65 + "\n")

    # Helper function to print to console AND write to file
    def emit(text=""):
        print(text)
        with open(output_path, "a") as f:
            f.write(str(text) + "\n")
    
    # Load project data
    D, L = load_dataset(dataset_dir / "trainData.txt") 
    
    # Split dataset 2/3 train, 1/3 validation
    (DTR, LTR), (DVAL, LVAL) = split_dataset(D, L, percTrain=2.0 / 3.0)


    # ======================================================
    # 1. LOGISTIC REGRESSION EVALUATION
    # ======================================================

    # -----------------------------------------------------------------------
    # Setup parameters
    # -----------------------------------------------------------------------
    # Primary application target prior
    pi_T = 0.1
    Cfn = 1.0
    Cfp = 1.0
    
    # Calculate empirical prior from the training set
    pi_emp = numpy.sum(LTR == 1) / len(LTR)
    empirical_log_odds = numpy.log(pi_emp / (1 - pi_emp))
    
    # Log-spaced lambda values from 10^-4 to 10^2
    lambdas = numpy.logspace(-4, 2, 13)
    
    # Lists to store metrics
    act_dcfs = []
    min_dcfs = []

    emit("=========================================================================")
    emit("--- PROJECT: STANDARD LOGISTIC REGRESSION (pi_T = 0.1) ---")
    emit("=========================================================================")
    emit(f"{'Lambda':<12} | {'minDCF':<10} | {'actDCF':<10}")
    emit("-" * 40)
    
    # -----------------------------------------------------------------------
    # Training and evaluation loop
    # -----------------------------------------------------------------------
    for l in lambdas:
        # Train the standard model
        w_opt, b_opt = trainLogReg(DTR, LTR, l)
        
        # Compute raw scores on the validation set
        S_val = (numpy.dot(w_opt.reshape(1, -1), DVAL) + b_opt).ravel()
        
        # Convert to LLR by removing the empirical training prior log-odds
        llr_val = S_val - empirical_log_odds
        
        # Compute minDCF
        min_DCF = compute_min_dcf(llr_val, LVAL, pi_T, Cfn, Cfp)
        min_dcfs.append(min_DCF)
        
        # Compute actDCF
        predictions_opt = compute_optimal_bayes_binary(llr_val, pi_T, Cfn, Cfp)
        M = compute_confusion_matrix(predictions_opt, LVAL, num_classes=2)
        act_DCF = compute_normalised_empirical_Bayes_risk_binary(M, pi_T, Cfn, Cfp)
        act_dcfs.append(act_DCF)
        
        emit(f"{l:<12.4e} | {min_DCF:<10.4f} | {act_DCF:<10.4f}")

    # -----------------------------------------------------------------------
    # Plotting
    # -----------------------------------------------------------------------
    plot_filename = plots_dir / "LR_Standard_DCF_vs_Lambda.png"
    plot_dcf_vs_lambda(lambdas, act_dcfs, min_dcfs, plot_filename)
    print(f"\nPlot saved to: {plot_filename}")


    # ======================================================
    # 2. REDUCED DATASET ANALYSIS (1 out of 50 samples)
    # ======================================================

    emit("\n\n=========================================================================")
    emit("--- PROJECT: STANDARD LOGISTIC REGRESSION (REDUCED DATASET) ---")
    emit("=========================================================================")
    
    # Keep only 1 out of 50 training samples
    DTR_reduced = DTR[:, ::50]
    LTR_reduced = LTR[::50]
    
    # Recalculate empirical prior for the reduced dataset!
    pi_emp_reduced = numpy.sum(LTR_reduced == 1) / len(LTR_reduced)
    empirical_log_odds_reduced = numpy.log(pi_emp_reduced / (1 - pi_emp_reduced))
    
    # Lists to store metrics for the reduced dataset
    act_dcfs_reduced = []
    min_dcfs_reduced = []
    
    emit(f"{'Lambda':<12} | {'minDCF':<10} | {'actDCF':<10}")
    emit("-" * 40)
    
    for l in lambdas:
        # Train the standard model on the REDUCED dataset
        w_opt_red, b_opt_red = trainLogReg(DTR_reduced, LTR_reduced, l)
        
        # Compute raw scores on the FULL validation set
        S_val_red = (numpy.dot(w_opt_red.reshape(1, -1), DVAL) + b_opt_red).ravel()
        
        # Convert to LLR by removing the REDUCED empirical training prior log-odds
        llr_val_red = S_val_red - empirical_log_odds_reduced
        
        # Compute minDCF
        min_DCF_red = compute_min_dcf(llr_val_red, LVAL, pi_T, Cfn, Cfp)
        min_dcfs_reduced.append(min_DCF_red)
        
        # Compute actDCF
        predictions_opt_red = compute_optimal_bayes_binary(llr_val_red, pi_T, Cfn, Cfp)
        M_red = compute_confusion_matrix(predictions_opt_red, LVAL, num_classes=2)
        act_DCF_red = compute_normalised_empirical_Bayes_risk_binary(M_red, pi_T, Cfn, Cfp)
        act_dcfs_reduced.append(act_DCF_red)
        
        emit(f"{l:<12.4e} | {min_DCF_red:<10.4f} | {act_DCF_red:<10.4f}")

    # -----------------------------------------------------------------------
    # Plotting for Reduced Dataset
    # -----------------------------------------------------------------------
    plot_filename_red = plots_dir / "LR_Standard_Reduced_DCF_vs_Lambda.png"
    plot_dcf_vs_lambda(lambdas, act_dcfs_reduced, min_dcfs_reduced, plot_filename_red)
    print(f"\nReduced Dataset Plot saved to: {plot_filename_red}")


    # ======================================================
    # 3. PRIOR-WEIGHTED LOGISTIC REGRESSION (pi_T = 0.1)
    # ======================================================
    emit("\n\n=========================================================================")
    emit("--- PROJECT: PRIOR-WEIGHTED LOGISTIC REGRESSION (pi_T = 0.1) ---")
    emit("=========================================================================")
    
    # Calculate target prior log-odds for calibration
    target_log_odds = numpy.log(pi_T / (1 - pi_T))
    
    # Lists to store metrics for the weighted model
    act_dcfs_weighted = []
    min_dcfs_weighted = []
    
    emit(f"{'Lambda':<12} | {'minDCF':<10} | {'actDCF':<10}")
    emit("-" * 40)
    
    for l in lambdas:
        # Train the weighted model
        w_opt_w, b_opt_w = trainLogReg(DTR, LTR, l, pi_T=pi_T)
        
        # Compute raw scores on the validation set
        S_val_w = (numpy.dot(w_opt_w.reshape(1, -1), DVAL) + b_opt_w).ravel()
        
        # Convert to LLR by removing the TARGET prior log-odds
        llr_val_w = S_val_w - target_log_odds
        
        # Compute minDCF
        min_DCF_w = compute_min_dcf(llr_val_w, LVAL, pi_T, Cfn, Cfp)
        min_dcfs_weighted.append(min_DCF_w)
        
        # Compute actDCF
        predictions_opt_w = compute_optimal_bayes_binary(llr_val_w, pi_T, Cfn, Cfp)
        M_w = compute_confusion_matrix(predictions_opt_w, LVAL, num_classes=2)
        act_DCF_w = compute_normalised_empirical_Bayes_risk_binary(M_w, pi_T, Cfn, Cfp)
        act_dcfs_weighted.append(act_DCF_w)
        
        emit(f"{l:<12.4e} | {min_DCF_w:<10.4f} | {act_DCF_w:<10.4f}")

    # -----------------------------------------------------------------------
    # Plotting for Prior-Weighted Dataset
    # -----------------------------------------------------------------------
    plot_filename_w = plots_dir / "LR_Weighted_DCF_vs_Lambda.png"
    plot_dcf_vs_lambda(lambdas, act_dcfs_weighted, min_dcfs_weighted, plot_filename_w)
    print(f"\nPrior-Weighted Plot saved to: {plot_filename_w}")


    # =======================================================================
    # 4. QUADRATIC LOGISTIC REGRESSION (STANDARD, pi_T = 0.1)
    # =======================================================================
    emit("\n\n=========================================================================")
    emit("--- PROJECT: QUADRATIC LOGISTIC REGRESSION (STANDARD) ---")
    emit("=========================================================================")
    
    # 1. Expand features for both training and validation sets
    DTR_expanded = quadratic_feature_expansion(DTR)
    DVAL_expanded = quadratic_feature_expansion(DVAL)
    
    # Lists to store metrics
    act_dcfs_quad = []
    min_dcfs_quad = []
    
    emit(f"{'Lambda':<12} | {'minDCF':<10} | {'actDCF':<10}")
    emit("-" * 40)
    
    # 2. Train and Evaluate
    for l in lambdas:
        # Train standard model on the EXPANDED dataset
        w_opt_q, b_opt_q = trainLogReg(DTR_expanded, LTR, l)
        
        # Compute raw scores on the EXPANDED validation set
        S_val_q = (numpy.dot(w_opt_q.reshape(1, -1), DVAL_expanded) + b_opt_q).ravel()
        
        # Convert to LLR by removing the standard empirical training prior log-odds
        llr_val_q = S_val_q - empirical_log_odds
        
        # Compute minDCF
        min_DCF_q = compute_min_dcf(llr_val_q, LVAL, pi_T, Cfn, Cfp)
        min_dcfs_quad.append(min_DCF_q)
        
        # Compute actDCF
        predictions_opt_q = compute_optimal_bayes_binary(llr_val_q, pi_T, Cfn, Cfp)
        M_q = compute_confusion_matrix(predictions_opt_q, LVAL, num_classes=2)
        act_DCF_q = compute_normalised_empirical_Bayes_risk_binary(M_q, pi_T, Cfn, Cfp)
        act_dcfs_quad.append(act_DCF_q)
        
        emit(f"{l:<12.4e} | {min_DCF_q:<10.4f} | {act_DCF_q:<10.4f}")

    # -----------------------------------------------------------------------
    # Plotting for Quadratic Dataset
    # -----------------------------------------------------------------------
    plot_filename_q = plots_dir / "LR_Quadratic_DCF_vs_Lambda.png"
    plot_dcf_vs_lambda(lambdas, act_dcfs_quad, min_dcfs_quad, plot_filename_q)
    print(f"\nQuadratic Plot saved to: {plot_filename_q}")


    # =======================================================================
    # 6. FINAL SUMMARY AND MODEL COMPARISON (pi_T = 0.1)
    # =======================================================================

    # -----------------------------------------------------------------------
    # Evaluate Gaussian Generative Models for comparison
    # -----------------------------------------------------------------------

    emit("\n\n=========================================================================")
    emit("--- GAUSSIAN GENERATIVE MODELS ---")
    emit("=========================================================================")
    
    # 1. Multivariate Gaussian (MVG)
    S_log_mvg = compute_mvg_loglikelihoods(DTR, LTR, DVAL)
    llr_mvg = S_log_mvg[1, :] - S_log_mvg[0, :] # LLR = log f(x|c=1) - log f(x|c=0)
    
    minDCF_mvg = compute_min_dcf(llr_mvg, LVAL, pi_T, Cfn, Cfp)
    pred_mvg = compute_optimal_bayes_binary(llr_mvg, pi_T, Cfn, Cfp)
    M_mvg = compute_confusion_matrix(pred_mvg, LVAL, num_classes=2)
    actDCF_mvg = compute_normalised_empirical_Bayes_risk_binary(M_mvg, pi_T, Cfn, Cfp)
    
    # 2. Naive Bayes
    S_log_nb = compute_naive_bayes_loglikelihoods(DTR, LTR, DVAL)
    llr_nb = S_log_nb[1, :] - S_log_nb[0, :]
    
    minDCF_nb = compute_min_dcf(llr_nb, LVAL, pi_T, Cfn, Cfp)
    pred_nb = compute_optimal_bayes_binary(llr_nb, pi_T, Cfn, Cfp)
    M_nb = compute_confusion_matrix(pred_nb, LVAL, num_classes=2)
    actDCF_nb = compute_normalised_empirical_Bayes_risk_binary(M_nb, pi_T, Cfn, Cfp)
    
    # 3. Tied MVG
    S_log_tied = compute_tied_mvg_loglikelihoods(DTR, LTR, DVAL)
    llr_tied = S_log_tied[1, :] - S_log_tied[0, :]
    
    minDCF_tied = compute_min_dcf(llr_tied, LVAL, pi_T, Cfn, Cfp)
    pred_tied = compute_optimal_bayes_binary(llr_tied, pi_T, Cfn, Cfp)
    M_tied = compute_confusion_matrix(pred_tied, LVAL, num_classes=2)
    actDCF_tied = compute_normalised_empirical_Bayes_risk_binary(M_tied, pi_T, Cfn, Cfp)
    
    emit(f"{'Model':<20} | {'minDCF':<10} | {'actDCF':<10}")
    emit("-" * 45)
    emit(f"{'MVG':<20} | {minDCF_mvg:<10.4f} | {actDCF_mvg:<10.4f}")
    emit(f"{'Naive Bayes':<20} | {minDCF_nb:<10.4f} | {actDCF_nb:<10.4f}")
    emit(f"{'Tied MVG':<20} | {minDCF_tied:<10.4f} | {actDCF_tied:<10.4f}")

    # -----------------------------------------------------------------------
    # Final Summary Table Comparing All Models
    # -----------------------------------------------------------------------

    emit("\n\n=========================================================================")
    emit("--- FINAL PROJECT SUMMARY: MODEL COMPARISON (pi_T = 0.1) ---")
    emit("=========================================================================")
    
    # Find the index of the lowest minDCF for each Logistic Regression model
    idx_std = numpy.argmin(min_dcfs)
    idx_red = numpy.argmin(min_dcfs_reduced)
    idx_w = numpy.argmin(min_dcfs_weighted)
    idx_q = numpy.argmin(min_dcfs_quad)
    
    emit(f"{'Model':<35} | {'Opt Lambda':<10} | {'minDCF':<10} | {'actDCF':<10} | {'Calibration Gap'}")
    emit("-" * 90)
    
    # --- Generative Models ---
    emit(f"{'MVG':<35} | {'-':<10} | {minDCF_mvg:<10.4f} | {actDCF_mvg:<10.4f} | {actDCF_mvg - minDCF_mvg:<10.4f}")
    emit(f"{'Naive Bayes':<35} | {'-':<10} | {minDCF_nb:<10.4f} | {actDCF_nb:<10.4f} | {actDCF_nb - minDCF_nb:<10.4f}")
    emit(f"{'Tied MVG':<35} | {'-':<10} | {minDCF_tied:<10.4f} | {actDCF_tied:<10.4f} | {actDCF_tied - minDCF_tied:<10.4f}")
    
    emit("-" * 90)
    
    # --- Logistic Regression Models ---
    gap_std = act_dcfs[idx_std] - min_dcfs[idx_std]
    emit(f"{'Standard LR':<35} | {lambdas[idx_std]:<10.4e} | {min_dcfs[idx_std]:<10.4f} | {act_dcfs[idx_std]:<10.4f} | {gap_std:<10.4f}")
    
    gap_red = act_dcfs_reduced[idx_red] - min_dcfs_reduced[idx_red]
    emit(f"{'Reduced Standard LR (1/50)':<35} | {lambdas[idx_red]:<10.4e} | {min_dcfs_reduced[idx_red]:<10.4f} | {act_dcfs_reduced[idx_red]:<10.4f} | {gap_red:<10.4f}")
    
    gap_w = act_dcfs_weighted[idx_w] - min_dcfs_weighted[idx_w]
    emit(f"{'Prior-Weighted LR':<35} | {lambdas[idx_w]:<10.4e} | {min_dcfs_weighted[idx_w]:<10.4f} | {act_dcfs_weighted[idx_w]:<10.4f} | {gap_w:<10.4f}")
    
    gap_q = act_dcfs_quad[idx_q] - min_dcfs_quad[idx_q]
    emit(f"{'Quadratic LR':<35} | {lambdas[idx_q]:<10.4e} | {min_dcfs_quad[idx_q]:<10.4f} | {act_dcfs_quad[idx_q]:<10.4f} | {gap_q:<10.4f}")
    
    emit("-" * 90)
    print("\nProject evaluation complete.")