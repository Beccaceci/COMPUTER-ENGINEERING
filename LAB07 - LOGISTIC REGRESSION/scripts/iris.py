import numpy
import scipy.optimize

from pathlib import Path
from utils.data_loaders import *
from utils.bayes_utils import compute_optimal_bayes_binary, compute_normalised_empirical_Bayes_risk_binary, compute_min_dcf
from utils.math_utils import f_with_gradient, compute_confusion_matrix
from models.logisticRegression import *

def my_math_function(y, z):
    return ((y + 3)**2) + numpy.sin(y) + ((z + 1)**2)

def my_math_gradient(y, z):
    grad_y = 2 * (y + 3) + numpy.cos(y)
    grad_z = 2 * (z + 1)
    return [grad_y, grad_z]


if __name__ == "__main__":
    # Define the starting point
    x0 = numpy.zeros(2)

    ROOT = Path(".")

    # Paths
    results_dir = ROOT / "results" / "iris"
    dataset_dir = ROOT / "data" / "iris"

    # Create the results directory if it doesn't exist
    results_dir.mkdir(parents=True, exist_ok=True)
    output_path = results_dir / "lab07_evaluation.txt"

    # Clear the file at the start of the run
    with open(output_path, "w") as f:
        f.write("LAB 07: LOGISTIC REGRESSION EVALUATION\n")
        f.write("=" * 65 + "\n")

    # Helper function to print to console AND write to file
    def emit(text=""):
        print(text)
        with open(output_path, "a") as f:
            f.write(str(text) + "\n")

    # ======================================================
    # 1. NUMERICAL OPTIMISATION
    # ======================================================

    emit("--- Using Analytical Gradient (Tuple Return) ---")

    f = f_with_gradient(my_math_function, my_math_gradient)

    # Use the L-BFGS-B algorithm to find the minimum of f(y, z) using the provided gradient
    x_opt_exact, f_opt_exact, d_exact = scipy.optimize.fmin_l_bfgs_b(
        func=f, 
        x0=x0, 
        approx_grad=False
    )

    emit(f"Minimum found at: {x_opt_exact}")
    emit(f"Objective value: {f_opt_exact}")
    emit(f"Number of function calls: {d_exact['funcalls']}")


    # ======================================================
    # 2. BINARY LOGISTIC REGRESSION
    # ======================================================

    # Data loading
    D, L = load_dataset(dataset_dir / "iris_dataset.csv", True)
    
    # Reassign virginica to Class 0, versicolor is Class 1
    L[L == 2] = 0 
    (DTR, LTR), (DTE, LTE) = split_dataset(D, L, percTrain=2.0 / 3.0)

    # Calculate empirical prior
    pi_emp = numpy.sum(LTR == 1) / len(LTR)
    empirical_log_odds = numpy.log(pi_emp / (1 - pi_emp))
    
    # Application parameters
    pi_T = 0.5
    Cfn = 1.0
    Cfp = 1.0
    
    lambdas = [1e-3, 1e-1, 1.0]

    emit("\n\n--- Standard Logistic Regression ---")
    emit(f"{'Lambda':<10} | {'J(w*, b*)':<12} | {'Error Rate':<12} | {'minDCF':<10} | {'actDCF':<10}")
    emit("-" * 65)
    
    for l in lambdas:
        # Train the model
        w_opt, b_opt = trainLogReg(DTR, LTR, l)
        
        # 1. Compute objective J(w*, b*) at the minimum
        # Re-pack w and b to pass to our objective function to get the final J
        v_opt = numpy.hstack([w_opt, b_opt])
        J_opt, _ = logreg_obj_standard(v_opt, DTR, LTR, l)
        
        # 2. Compute raw scores on validation set
        S_val = (numpy.dot(w_opt.reshape(1, -1), DTE) + b_opt).ravel()
        
        # 3. Compute error rate (Thresholding raw score at 0)
        predictions_raw = (S_val > 0).astype(int)
        error_rate = numpy.mean(predictions_raw != LTE) * 100
        
        # 4. Convert to Log-Likelihood Ratios (LLR)
        llr_val = S_val - empirical_log_odds
        
        # 5. Compute minDCF and actDCF
        min_DCF = compute_min_dcf(llr_val, LTE, pi_T, Cfn, Cfp)
        
        predictions_opt = compute_optimal_bayes_binary(llr_val, pi_T, Cfn, Cfp)
        M = compute_confusion_matrix(predictions_opt, LTE, num_classes=2)
        act_DCF = compute_normalised_empirical_Bayes_risk_binary(M, pi_T, Cfn, Cfp)
        
        # Print results
        emit(f"{l:<10.0e} | {J_opt:<12.6e} | {error_rate:>5.1f}%       | {min_DCF:<10.4f} | {act_DCF:<10.4f}")


    # ======================================================
    # 3. PRIOR-WEIGHTED BINARY LOGISTIC REGRESSION
    # ======================================================

    pi_T_weighted = 0.8
    target_log_odds = numpy.log(pi_T_weighted / (1 - pi_T_weighted))

    emit(f"\n\n--- Prior-Weighted Logistic Regression (pi_T = {pi_T_weighted}) ---")
    emit(f"{'Lambda':<10} | {'J(w*, b*)':<12} | {'minDCF':<10} | {'actDCF':<10}")
    emit("-" * 50)

    for l in lambdas:
        # Train the weighted model
        w_opt, b_opt = trainLogReg(DTR, LTR, l, pi_T=pi_T_weighted)
        
        # 1. Compute objective J(w*, b*) at the minimum using the weighted objective
        v_opt = numpy.hstack([w_opt, b_opt])
        J_opt, _ = logreg_obj_weighted(v_opt, DTR, LTR, l, pi_T_weighted)
        
        # 2. Compute raw scores on validation set
        S_val = (numpy.dot(w_opt.reshape(1, -1), DTE) + b_opt).ravel()
        
        # 3. Convert to Log-Likelihood Ratios (LLR)
        # CRITICAL: Subtract target prior log-odds for prior-weighted models
        llr_val = S_val - target_log_odds
        
        # 4. Compute minDCF and actDCF
        min_DCF = compute_min_dcf(llr_val, LTE, pi_T_weighted, Cfn, Cfp)
        
        predictions_opt = compute_optimal_bayes_binary(llr_val, pi_T_weighted, Cfn, Cfp)
        M = compute_confusion_matrix(predictions_opt, LTE, num_classes=2)
        act_DCF = compute_normalised_empirical_Bayes_risk_binary(M, pi_T_weighted, Cfn, Cfp)
        
        # Print results
        emit(f"{l:<10.0e} | {J_opt:<12.6e} | {min_DCF:<10.4f} | {act_DCF:<10.4f}")


    # ======================================================
    # 4. MULTICLASS LOGISTIC REGRESSION (FULL DATASET)
    # ======================================================

    emit("\n\n--- Multiclass Logistic Regression (Full 3-Class Iris) ---")
    
    # Reload the full dataset
    D_multi, L_multi = load_dataset(dataset_dir / "iris_dataset.csv")
    (DTR_m, LTR_m), (DTE_m, LTE_m) = split_dataset(D_multi, L_multi, percTrain=2.0 / 3.0)
    
    emit(f"{'Lambda':<10} | {'J(w*, b*)':<12} | {'Error Rate':<12}")
    emit("-" * 40)
    
    for l in lambdas:
        # Train the multiclass model
        W_opt, b_opt = trainLogReg_Multiclass(DTR_m, LTR_m, l)
        
        # 1. Compute Objective J(W*, b*)
        v_opt = numpy.hstack([W_opt.ravel(), b_opt.ravel()])
        J_opt, _ = logreg_obj_multiclass(v_opt, DTR_m, LTR_m, l)
        
        # 2. Compute Scores on Evaluation Set
        S_val = numpy.dot(W_opt.T, DTE_m) + b_opt
        
        # 3. Predict the class (highest score)
        predictions = numpy.argmax(S_val, axis=0)
        
        # 4. Compute Error Rate
        error_rate = numpy.mean(predictions != LTE_m) * 100
        
        emit(f"{l:<10.0e} | {J_opt:<12.6e} | {error_rate:>5.1f}%")