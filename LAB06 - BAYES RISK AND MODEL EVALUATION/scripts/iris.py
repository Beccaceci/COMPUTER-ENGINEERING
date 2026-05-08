import numpy
import matplotlib.pyplot as plt
from pathlib import Path

from models.MVG import compute_mvg_loglikelihoods
from models.TiedMVG import compute_tied_mvg_loglikelihoods

from utils.bayes_utils import *
from utils.data_loaders import *
from utils.plot_utils import *
from utils.math_utils import compute_confusion_matrix, mcol, vrow

# ======================================================
# HELPER FUNCTIONS
# ======================================================
def evaluate_binary_applications(llr, LTE, applications, model_name):
    """
    Evaluates a set of specific applications for a given binary classifier and prints a formatted table.
    """
    print(f"\n--- Application Metrics for {model_name} ---")
    print(f"{'(pi1, Cfn, Cfp)':^18} | {'DCF_u':^10} | {'DCF_n':^10} | {'min_DCF':^10}")
    print("-" * 59)
    
    for pi1, Cfn, Cfp in applications:
        # Get optimal predictions and confusion matrix
        pred = compute_optimal_bayes_binary(llr, pi1, Cfn, Cfp)
        M = compute_confusion_matrix(pred, LTE, num_classes=2)
        
        # Compute metrics
        DCF_u = compute_empirical_Bayes_risk_binary(M, pi1, Cfn, Cfp)
        DCF_n = compute_normalised_empirical_Bayes_risk_binary(M, pi1, Cfn, Cfp)
        min_DCF = compute_min_dcf(llr, LTE, pi1, Cfn, Cfp)
        
        # Print row
        triplet_str = f"({pi1}, {Cfn}, {Cfp})"
        print(f"{triplet_str:>18} | {DCF_u:>10.3f} | {DCF_n:>10.3f} | {min_DCF:>10.3f}")

def sweep_bayes_error(llr, LTE, pi_array, Cfn=1, Cfp=1):
    """
    Sweeps across an array of effective priors and returns the DCF and min DCF arrays.
    """
    # Initialize lists to hold DCF values
    dcf_values = []
    min_dcf_values = []
    
    # Sweep across the array of effective priors
    for pi_tilde in pi_array:
        # Get optimal predictions and confusion matrix for the current prior
        pred = compute_optimal_bayes_binary(llr, pi_tilde, Cfn, Cfp)
        M = compute_confusion_matrix(pred, LTE, num_classes=2)
        
        # Compute and store DCF and min DCF for the current prior
        dcf_values.append(compute_normalised_empirical_Bayes_risk_binary(M, pi_tilde, Cfn, Cfp))
        min_dcf_values.append(compute_min_dcf(llr, LTE, pi_tilde, Cfn, Cfp))
        
    return dcf_values, min_dcf_values


if __name__ == "__main__":
    ROOT = Path(".")

    # Paths
    results_dir = ROOT / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    dataset_dir = ROOT / "data" / "iris"

    # Data loading
    D, L = load_dataset(dataset_dir / "iris_dataset.csv")
    (DTR, LTR), (DTE, LTE) = split_dataset(D, L, percTrain=2.0 / 3.0)

    num_classes = len(numpy.unique(LTR))
    class_names = ["Setosa", "Versicolor", "Virginica"]
    prior_uniform = numpy.ones(num_classes) / num_classes


    # ======================================================
    # 1. STANDARD MVG EVALUATION
    # ======================================================
    print("\nEvaluating Standard MVG...")
    S_log_mvg = compute_mvg_loglikelihoods(DTR, LTR, DTE)
    _, _, logSPost_mvg = compute_posteriors(S_log_mvg, prior_uniform)
    pred_mvg = numpy.argmax(logSPost_mvg, axis=0)
    M_mvg = compute_confusion_matrix(pred_mvg, LTE, num_classes)
    
    print("Standard MVG Confusion Matrix:")
    print_confusion_matrix(M_mvg)


    # ======================================================
    # 2. TIED MVG EVALUATION
    # ======================================================
    print("\nEvaluating Tied MVG...")
    S_log_tied = compute_tied_mvg_loglikelihoods(DTR, LTR, DTE)
    _, _, logSPost_tied = compute_posteriors(S_log_tied, prior_uniform)
    pred_tied = numpy.argmax(logSPost_tied, axis=0)
    M_tied = compute_confusion_matrix(pred_tied, LTE, num_classes)
    
    print("Tied MVG Confusion Matrix:")
    print_confusion_matrix(M_tied)


    # ======================================================
    # 3. PROVIDED MULTICLASS DATASET EVALUATION
    # ======================================================
    print("\nEvaluating provided multiclass dataset...")
    S_log_provided = numpy.load(ROOT / "data" / "iris" / "evalset_ll.npy")
    LTE_multi = numpy.load(ROOT / "data" / "iris" / "evalset_labels.npy")

    num_classes_prov = S_log_provided.shape[0]
    prior_uniform_prov = numpy.ones(num_classes_prov) / num_classes_prov
    _, _, logSPost_provided = compute_posteriors(S_log_provided, prior_uniform_prov)
    pred_provided = numpy.argmax(logSPost_provided, axis=0)
    M_provided = compute_confusion_matrix(pred_provided, LTE_multi, num_classes_prov)
    
    print("Provided dataset Confusion Matrix:")
    print_confusion_matrix(M_provided)


    # ======================================================
    # 4. BINARY EVALUATION (TABULAR METRICS)
    # ======================================================
    print("\nEvaluating binary decisions with Bayes risk...")

    # Load binary datasets
    llr1 = numpy.load(ROOT / "data" / "iris" / "evalset_llr_binary.npy")
    llr2 = numpy.load(ROOT / "data" / "iris" / "evalset_llr_binary_2.npy")
    LTE_bin = numpy.load(ROOT / "data" / "iris" / "evalset_labels_binary.npy")
    
    applications = [
        (0.5, 1, 1),
        (0.8, 1, 1),
        (0.5, 10, 1),
        (0.8, 1, 10)
    ]
    
    # Process both classifiers cleanly
    evaluate_binary_applications(llr1, LTE_bin, applications, "Classifier 1")
    evaluate_binary_applications(llr2, LTE_bin, applications, "Classifier 2")


    # ======================================================
    # 5. ROC CURVE
    # ======================================================
    print("\nComputing and plotting ROC curve for Classifier 1...")
    FPR, TPR = compute_roc_coordinates(llr1, LTE_bin)
    
    roc_output_path = results_dir / "iris" / "ROC_binary_evaluation.png"
    plot_roc_curve(FPR, TPR, roc_output_path)
    print(f"ROC curve successfully saved to {roc_output_path}")


    # ======================================================
    # 6. BAYES ERROR PLOTS
    # ======================================================
    print("\nComputing and plotting Bayes Error Plots...")

    effPriorLogOdds = numpy.linspace(-3, 3, 21)
    pi_array = 1 / (1 + numpy.exp(-effPriorLogOdds))

    # Sweep for Classifier 1
    dcf_1, min_dcf_1 = sweep_bayes_error(llr1, LTE_bin, pi_array)
    
    # Sweep for Classifier 2
    dcf_2, min_dcf_2 = sweep_bayes_error(llr2, LTE_bin, pi_array)

    # Plot single Bayes Error
    bayes_single_path = results_dir / "iris" / "Bayes_Error_binary_evaluation_classifier1.png"
    plot_bayes_error(effPriorLogOdds, dcf_1, min_dcf_1, bayes_single_path)
    plot_bayes_error(effPriorLogOdds, dcf_2, min_dcf_2, results_dir / "iris" / "Bayes_Error_binary_evaluation_classifier2.png")
    
    # Plot comparative Bayes Error (Classifier 1 vs Classifier 2)
    bayes_comp_path = results_dir / "iris" / "Bayes_Error_Comparison.png"
    plot_bayes_error_comparison(
        effPriorLogOdds, 
        dcf_1, min_dcf_1, 
        dcf_2, min_dcf_2, 
        bayes_comp_path
    )
    
    print(f"Bayes Error plots successfully saved to {results_dir / 'iris'}")


    # ======================================================
    # 7. MULTICLASS EVALUATION WITH BAYES RISK
    # ======================================================
    print("\nComputing multiclass evaluation with Bayes risk...")

    # Load multiclass datasets
    ll_multi_1 = numpy.load(ROOT / "data" / "iris" / "evalset_ll.npy")
    ll_multi_2 = numpy.load(ROOT / "data" / "iris" / "evalset_ll_2.npy")
    LTE_multi = numpy.load(ROOT / "data" / "iris" / "evalset_labels.npy")

    # ------------------------------------------------------
    # PART A: Custom priors and costs
    # ------------------------------------------------------

    # Define Cost matrix and Priors from the laboratory
    Cost_multi = numpy.array([
        [0, 1, 2],
        [1, 0, 1],
        [2, 1, 0]
    ])
    prior_multi = numpy.array([0.3, 0.4, 0.3])
    num_classes_multi = 3

    # --- Evaluate Classifier 1 ---
    print("\n--- Classifier 1 (evalset_ll.npy) ---")
    
    _, _, logSPost_multi_1 = compute_posteriors(ll_multi_1, prior_multi)
    pred_multi_1 = compute_optimal_bayes_multiclass(logSPost_multi_1, Cost_multi)
    M_multi_1 = compute_confusion_matrix(pred_multi_1, LTE_multi, num_classes_multi)
    
    print_confusion_matrix(M_multi_1)
    DCF_u_1 = compute_empirical_Bayes_risk_multiclass(M_multi_1, prior_multi, Cost_multi)
    DCF_n_1 = compute_normalised_empirical_Bayes_risk_multiclass(M_multi_1, prior_multi, Cost_multi)
    
    print(f"\nDCF_u = {DCF_u_1:.3f}")
    print(f"DCF_n = {DCF_n_1:.3f}")

    # --- Evaluate Classifier 2 ---
    print("\n--- Classifier 2 (evalset_ll_2.npy) ---")
    
    _, _, logSPost_multi_2 = compute_posteriors(ll_multi_2, prior_multi)
    pred_multi_2 = compute_optimal_bayes_multiclass(logSPost_multi_2, Cost_multi)
    M_multi_2 = compute_confusion_matrix(pred_multi_2, LTE_multi, num_classes_multi)
    
    print_confusion_matrix(M_multi_2)
    DCF_u_2 = compute_empirical_Bayes_risk_multiclass(M_multi_2, prior_multi, Cost_multi)
    DCF_n_2 = compute_normalised_empirical_Bayes_risk_multiclass(M_multi_2, prior_multi, Cost_multi)
    
    print(f"\nDCF_u = {DCF_u_2:.3f}")
    print(f"DCF_n = {DCF_n_2:.3f}")

    # ------------------------------------------------------
    # PART B: Uniform priors and costs
    # ------------------------------------------------------
    Cost_uniform = numpy.ones((num_classes_multi, num_classes_multi)) - numpy.eye(num_classes_multi)
    prior_uniform = numpy.ones(num_classes_multi) / num_classes_multi

    # Classifier 1
    _, _, logSPost_uni_1 = compute_posteriors(ll_multi_1, prior_uniform)
    pred_uni_1 = compute_optimal_bayes_multiclass(logSPost_uni_1, Cost_uniform)
    M_uni_1 = compute_confusion_matrix(pred_uni_1, LTE_multi, num_classes_multi)
    DCF_u_uni_1 = compute_empirical_Bayes_risk_multiclass(M_uni_1, prior_uniform, Cost_uniform)
    DCF_n_uni_1 = compute_normalised_empirical_Bayes_risk_multiclass(M_uni_1, prior_uniform, Cost_uniform)

    # Classifier 2
    _, _, logSPost_uni_2 = compute_posteriors(ll_multi_2, prior_uniform)
    pred_uni_2 = compute_optimal_bayes_multiclass(logSPost_uni_2, Cost_uniform)
    M_uni_2 = compute_confusion_matrix(pred_uni_2, LTE_multi, num_classes_multi)
    DCF_u_uni_2 = compute_empirical_Bayes_risk_multiclass(M_uni_2, prior_uniform, Cost_uniform)
    DCF_n_uni_2 = compute_normalised_empirical_Bayes_risk_multiclass(M_uni_2, prior_uniform, Cost_uniform)

    # Print the requested comparative table
    print("\n--- Multiclass Evaluation (Uniform Priors and Costs) ---")
    print("-" * 37)
    print(f"{'':<15} | {'DCF_u':^7} | {'DCF':^7}")
    print("-" * 37)
    print(f"{'Classifier 1':<15} | {DCF_u_uni_1:^7.3f} | {DCF_n_uni_1:^7.3f}")
    print(f"{'Classifier 2':<15} | {DCF_u_uni_2:^7.3f} | {DCF_n_uni_2:^7.3f}")
    print("-" * 37)