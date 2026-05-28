from pathlib import Path

from utils.data_loaders import *
from models.linearSVM import train_linear_svm, evaluate_linear_svm
from models.kernelSVM import train_kernel_svm, evaluate_kernel_svm


if __name__ == "__main__":
    # --- SETUP & DATA LOADING ---
    ROOT = Path(".")
    dataset_dir = ROOT / "data" / "iris"
    output_dir = ROOT / "results" / "iris"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "iris_logreg_results.txt"

    # Clear the file at the start of the run
    with open(output_path, "w") as f:
        f.write("LAB 08: SUPPORT VECTOR MACHINES EVALUATION\n")
        f.write("=" * 65 + "\n")

    # Helper function to print to console AND write to file
    def emit(text=""):
        print(text)
        with open(output_path, "a") as f:
            f.write(str(text) + "\n")


    # Load dataset and filter Class 0 (Setosa) directly
    D, L = load_dataset(dataset_dir / "iris_dataset.csv", True)
    D = D[:, L != 0]
    L = L[L != 0]

    # Map labels {1, 2} -> {-1, 1}
    Z = 2 * (L - 1) - 1

    # Split dataset
    (DTR, LTR), (DTE, LTE) = split_dataset(D, Z, 2/3)


    # ===========================
    # 1. Linear SVM
    # ===========================
    emit("\n" + "=" * 30)
    emit("LINEAR SVM")
    emit("=" * 30)

    # --- EXPERIMENT CONFIGURATION ---
    K_values = [1.0, 10.0]
    C_values = [0.1, 1.0, 10.0]  # The values requested in the laboratory table
    
    # Update the table header to include K
    emit(f"{'K':<4} | {'C':<5} | {'Primal Loss':<14} | {'Dual Loss':<14} | {'Gap':<12} | {'Error%':<7} | {'minDCF':<7} | {'actDCF':<7}")
    emit("-" * 90)
    
    # --- RUN EVALUATIONS ---
    for K in K_values:
        for C in C_values:
            # Train the model with current K and C
            w_hat, J_primal, J_dual, gap = train_linear_svm(DTR, LTR, C, K)
            
            # Evaluate the model
            error_rate, min_dcf, act_dcf = evaluate_linear_svm(DTE, LTE, w_hat, K)
            
            # Print results formatted similarly to the laboratory table
            emit(f"{K:<4.1f} | {C:<5.1f} | {J_primal:<14.6e} | {J_dual:<14.6e} | {gap:<12.6e} | {error_rate*100:<6.1f}% | {min_dcf:<7.4f} | {act_dcf:<7.4f}")
        emit("-" * 90)

    
    # ===========================
    # 2. Kernel SVM
    # ===========================

    # --- 2.1 Kernel SVM (polynomial) ---
    emit("\n" + "=" * 30)
    emit("POLYNOMIAL KERNEL SVM (d=2)")
    emit("=" * 30)
    
    K_values_kernel = [0.0, 1.0]
    c_values = [0, 1]
    C_fixed = 1.0
    
    emit(f"{'K':<4} | {'c':<4} | {'Primal Loss':<14} | {'Dual Loss':<14} | {'Error%':<7} | {'minDCF':<7} | {'actDCF':<7}")
    emit("-" * 80)
    
    for K in K_values_kernel:
        for c in c_values:
            # Train and evaluate the polynomial kernel SVM
            alpha_opt, J_primal, J_dual, gap = train_kernel_svm(DTR, LTR, C_fixed, K, "poly", d=2, c=c)
            error_rate, min_dcf, act_dcf = evaluate_kernel_svm(DTR, LTR, DTE, LTE, alpha_opt, K, "poly", d=2, c=c)

            emit(f"{K:<4.1f} | {c:<4} | {J_primal:<14.6e} | {J_dual:<14.6e} | {error_rate*100:<6.1f}% | {min_dcf:<7.4f} | {act_dcf:<7.4f}")


    # --- 2.2 Kernel SVM (RBF) ---
    emit("\n" + "=" * 30)
    emit("RBF KERNEL SVM")
    emit("=" * 30)
    
    gamma_values = [1.0, 10.0]
    
    emit(f"{'K':<4} | {'gama':<4} | {'Primal Loss':<14} | {'Dual Loss':<14} | {'Error%':<7} | {'minDCF':<7} | {'actDCF':<7}")
    emit("-" * 80)
    
    for K in K_values_kernel:
        for gamma in gamma_values:
            # Train and evaluate the RBF kernel SVM
            alpha_opt, J_primal, J_dual, gap = train_kernel_svm(DTR, LTR, C_fixed, K, "rbf", gamma=gamma)
            error_rate, min_dcf, act_dcf = evaluate_kernel_svm(DTR, LTR, DTE, LTE, alpha_opt, K, "rbf", gamma=gamma)
            
            emit(f"{K:<4.1f} | {gamma:<4.1f} | {J_primal:<14.6e} | {J_dual:<14.6e} | {error_rate*100:<6.1f}% | {min_dcf:<7.4f} | {act_dcf:<7.4f}")