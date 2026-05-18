from pathlib import Path

from utils.data_loaders import *
from models.linearSVM import *
from models.kernelSVM import *
from utils.plot_utils import *


# Helper to run the sweep over C
def run_linear_experiment(D_train, L_train, D_test, L_test, C_array, K_bias, pi_t=0.1):
    min_dcfs = []
    act_dcfs = []
    for C in C_array:
        w_hat, J_primal, J_dual, gap = train_linear_svm(D_train, L_train, C, K_bias)
        error_rate, min_dcf, act_dcf = evaluate_linear_svm(D_test, L_test, w_hat, K_bias, pi=pi_t)
        
        min_dcfs.append(min_dcf)
        act_dcfs.append(act_dcf)
        
        emit(f"{K_bias:<4.1f} | {C:<7.1e} | {J_primal:<14.6e} | {J_dual:<14.6e} | {gap:<12.6e} | {error_rate*100:<6.1f}% | {min_dcf:<7.4f} | {act_dcf:<7.4f}")
    return min_dcfs, act_dcfs

if __name__ == "__main__":
    # --- SETUP & DATA LOADING ---
    ROOT = Path(".")
    dataset_dir = ROOT / "data" / "project"
    output_dir = ROOT / "results" / "project"
    plots_dir = output_dir / "plots"

    plots_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "project_logreg_results.txt"

    # Clear the file at the start of the run
    with open(output_path, "w") as f:
        f.write("LAB 08: SUPPORT VECTOR MACHINES EVALUATION\n")
        f.write("=" * 65 + "\n")

    # Helper function to print to console AND write to file
    def emit(text=""):
        print(text)
        with open(output_path, "a") as f:
            f.write(str(text) + "\n")


    # Load dataset
    D, L = load_dataset(dataset_dir / "trainData.txt")

    # Map labels {1, 2} -> {-1, 1}
    Z = 2 * L - 1

    # Split dataset
    (DTR, LTR), (DTE, LTE) = split_dataset(D, Z, 2/3)


    # ===========================
    # 1. Linear SVM
    # ===========================

    # --- EXPERIMENT CONFIGURATION ---
    K = 1.0
    C_values = numpy.logspace(-5, 0, 11).tolist()  # The values requested in the laboratory table

    min_dcfs = []
    act_dcfs = []
    
    # Update the table header to include K
    emit(f"{'K':<4} | {'C':<5} | {'Primal Loss':<14} | {'Dual Loss':<14} | {'Gap':<12} | {'Error%':<7} | {'minDCF':<7} | {'actDCF':<7}")
    emit("-" * 90)
    
    # --- RUN EVALUATIONS ---
    min_dcfs, act_dcfs = run_linear_experiment(DTR, LTR, DTE, LTE, C_values, K, pi_t=0.1)

    plot_dcf_vs_c(C_values, min_dcfs, act_dcfs,
                  "Linear SVM (Raw Data): DCF vs C", 
                  plots_dir / "Linear_SVM_Raw_DCF_vs_C.png")
    
    # --- CENTER THE DATA ---
    # Compute the mean of the training set only
    mu_train = DTR.mean(axis=1, keepdims=True)
    
    # Subtract training mean from both training and test sets
    DTR_centered = DTR - mu_train
    DTE_centered = DTE - mu_train

    min_centered_dcfs = []
    act_centered_dcfs = []

    # Update the table header to include K
    emit(f"{'K':<4} | {'C':<5} | {'Primal Loss':<14} | {'Dual Loss':<14} | {'Gap':<12} | {'Error%':<7} | {'minDCF':<7} | {'actDCF':<7}")
    emit("-" * 90)
    
    # --- RUN EVALUATIONS ---
    min_centered_dcfs, act_centered_dcfs = run_linear_experiment(DTR_centered, LTR, DTE_centered, LTE, C_values, K, pi_t=0.1)

    plot_dcf_vs_c(C_values, min_centered_dcfs, act_centered_dcfs, 
                  "Linear SVM (Centered Data): DCF vs C", 
                  plots_dir / "Linear_SVM_Centered_DCF_vs_C.png")
    
    # ===========================
    # 2. Kernel SVM
    # ===========================

    # --- 2.1 Kernel SVM (polynomial) ---
    emit("\n" + "=" * 50)
    emit("POLYNOMIAL KERNEL SVM (d=2, c=1, K=0)")
    emit("=" * 50)
    
    emit(f"{'K':<4} | {'C':<7} | {'Primal Loss':<14} | {'Dual Loss':<14} | {'Gap':<12} | {'Error%':<7} | {'minDCF':<7} | {'actDCF':<7}")
    emit("-" * 90)
    
    min_poly_dcfs = []
    act_poly_dcfs = []
    
    # Iterate over the same logarithmic space used for the linear SVM
    for C in C_values:
        # K_bias is 0 because the kernel handles the bias intrinsically (xi=0)
        alpha_opt, J_primal, J_dual, gap = train_kernel_svm(DTR, LTR, C, 0.0, "poly", d=2, c=1)
        
        error_rate, min_dcf, act_dcf = evaluate_kernel_svm(DTR, LTR, DTE, LTE, alpha_opt, 0.0, "poly", pi=0.1, d=2, c=1)
        
        min_poly_dcfs.append(min_dcf)
        act_poly_dcfs.append(act_dcf)
        
        emit(f"{0.0:<4.1f} | {C:<7.1e} | {J_primal:<14.6e} | {J_dual:<14.6e} | {gap:<12.6e} | {error_rate*100:<6.1f}% | {min_dcf:<7.4f} | {act_dcf:<7.4f}")

    # Plot the results
    plot_dcf_vs_c(C_values, min_poly_dcfs, act_poly_dcfs,
                  "Polynomial Kernel SVM: DCF vs C", 
                  plots_dir / "Poly_Kernel_SVM_DCF_vs_C.png")
    
    # --- 2.2 Kernel SVM (RBF) ---
    emit("\n" + "=" * 50)
    emit("RBF KERNEL SVM (Grid Search)")
    emit("=" * 50)
    
    gamma_values = [1e-4, 1e-3, 1e-2, 1e-1]
    C_values_rbf = numpy.logspace(-3, 2, 11).tolist()
    K_rbf = 1.0 # Set K=1.0 since xi=1 for RBF
    
    emit(f"{'K':<4} | {'gamma':<7} | {'C':<7} | {'Primal Loss':<14} | {'Dual Loss':<14} | {'Gap':<12} | {'Error%':<7} | {'minDCF':<7} | {'actDCF':<7}")
    emit("-" * 105)
    
    # Dictionaries to store results for plotting
    min_rbf_dcfs = {gamma: [] for gamma in gamma_values}
    act_rbf_dcfs = {gamma: [] for gamma in gamma_values}
    
    for gamma in gamma_values:
        for C in C_values_rbf:
            # Train the RBF model
            alpha_opt, J_primal, J_dual, gap = train_kernel_svm(DTR, LTR, C, K_rbf, "rbf", gamma=gamma)
            
            # Evaluate using pi_t = 0.1
            error_rate, min_dcf, act_dcf = evaluate_kernel_svm(DTR, LTR, DTE, LTE, alpha_opt, K_rbf, "rbf", pi=0.1, gamma=gamma)
            
            # Track metrics
            min_rbf_dcfs[gamma].append(min_dcf)
            act_rbf_dcfs[gamma].append(act_dcf)
            
            emit(f"{K_rbf:<4.1f} | {gamma:<7.1e} | {C:<7.1e} | {J_primal:<14.6e} | {J_dual:<14.6e} | {gap:<12.6e} | {error_rate*100:<6.1f}% | {min_dcf:<7.4f} | {act_dcf:<7.4f}")
        
        emit("-" * 105)

    # Plot the RBF Grid Search Results
    plot_rbf_dcfs_vs_c(C_values_rbf, min_rbf_dcfs, act_rbf_dcfs,
                       r"RBF Kernel SVM: DCF vs C for different $\gamma$", 
                       plots_dir / "RBF_Kernel_SVM_DCF_vs_C.png")
    
    # ===========================
    # 3. Optional: Polynomial Kernel (d=4)
    # ===========================
    emit("\n" + "=" * 50)
    emit("OPTIONAL: POLYNOMIAL KERNEL SVM (d=4, c=1, K=0)")
    emit("=" * 50)
    
    emit(f"{'K':<4} | {'C':<7} | {'Primal Loss':<14} | {'Dual Loss':<14} | {'Gap':<12} | {'Error%':<7} | {'minDCF':<7} | {'actDCF':<7}")
    emit("-" * 90)
    
    min_poly4_dcfs = []
    act_poly4_dcfs = []
    
    # Iterate over the same logarithmic space used for the linear SVM
    for C in C_values: # C_values is numpy.logspace(-5, 0, 11)
        # K_bias is 0.0 because the kernel handles the bias intrinsically (xi=0)
        alpha_opt, J_primal, J_dual, gap = train_kernel_svm(DTR, LTR, C, 0.0, "poly", d=4, c=1)
        
        # Evaluate with pi_t = 0.1
        error_rate, min_dcf, act_dcf = evaluate_kernel_svm(DTR, LTR, DTE, LTE, alpha_opt, 0.0, "poly", pi=0.1, d=4, c=1)
        
        min_poly4_dcfs.append(min_dcf)
        act_poly4_dcfs.append(act_dcf)
        
        emit(f"{0.0:<4.1f} | {C:<7.1e} | {J_primal:<14.6e} | {J_dual:<14.6e} | {gap:<12.6e} | {error_rate*100:<6.1f}% | {min_dcf:<7.4f} | {act_dcf:<7.4f}")

    # Plot the results
    plot_dcf_vs_c(C_values, min_poly4_dcfs, act_poly4_dcfs,
                  "Optional Polynomial Kernel SVM (d=4): DCF vs C", 
                  plots_dir / "Poly_Kernel_SVM_d4_DCF_vs_C.png")