import numpy
import matplotlib.pyplot as plt
from pathlib import Path

from models.MVG import compute_mvg_loglikelihoods
from models.TiedMVG import compute_tied_mvg_loglikelihoods

from utils.bayes_utils import *
from utils.data_loaders import *
from utils.plot_utils import *
from utils.io_utils import *
from utils.math_utils import compute_confusion_matrix

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
    results_dir = ROOT / "results" / "iris"
    results_dir.mkdir(parents=True, exist_ok=True)
    dataset_dir = ROOT / "data" / "iris"

    emit = create_emitter(results_dir / "iris_results.txt")

    # Data loading
    D, L = load_dataset(dataset_dir / "iris_dataset.csv")
    (DTR, LTR), (DTE, LTE) = split_dataset(D, L, percTrain=2.0 / 3.0)

    num_classes = len(numpy.unique(LTR))
    class_names = ["Setosa", "Versicolor", "Virginica"]
    prior_uniform = numpy.ones(num_classes) / num_classes

    emit("1. CONFUSION MATRICES\n")

    # ======================================================
    # 1. STANDARD MVG EVALUATION
    # ======================================================
    S_log_mvg = compute_mvg_loglikelihoods(DTR, LTR, DTE) # compute the log-likelihoods of the test set given the model
    _, _, logSPost_mvg = compute_posteriors(S_log_mvg, prior_uniform) # compute the posterior probabilities of the test set given the model using the priors
    pred_mvg = numpy.argmax(logSPost_mvg, axis=0) # compute the optimal predictions
    M_mvg = compute_confusion_matrix(pred_mvg, LTE, num_classes) # compute the confusion matrix
    
    emit("Standard MVG confusion matrix:")
    print_confusion_matrix(M_mvg, emit)


    # ======================================================
    # 2. TIED MVG EVALUATION
    # ======================================================
    S_log_tied = compute_tied_mvg_loglikelihoods(DTR, LTR, DTE) # compute the log-likelihoods of the test set given the model
    _, _, logSPost_tied = compute_posteriors(S_log_tied, prior_uniform) # compute the posterior probabilities of the test set given the model using the priors
    pred_tied = numpy.argmax(logSPost_tied, axis=0) # compute the optimal predictions based on maximum a posteriori (MAP)
    M_tied = compute_confusion_matrix(pred_tied, LTE, num_classes) # compute the confusion matrix
    
    emit("\nTied MVG confusion matrix:")
    print_confusion_matrix(M_tied, emit)


    # ======================================================
    # 3. PROVIDED MULTICLASS DATASET EVALUATION
    # ======================================================
    S_log_provided = numpy.load(dataset_dir / "evalset_ll.npy")
    LTE_multi = numpy.load(dataset_dir / "evalset_labels.npy")

    num_classes_prov = S_log_provided.shape[0] # compute the number of classes
    prior_uniform_prov = numpy.ones(num_classes_prov) / num_classes_prov # compute the uniform prior for each class
    _, _, logSPost_provided = compute_posteriors(S_log_provided, prior_uniform_prov) # compute the posterior probabilities of the test set given the model using the priors
    pred_provided = numpy.argmax(logSPost_provided, axis=0) # compute the optimal predictions based on maximum a posteriori (MAP)
    M_provided = compute_confusion_matrix(pred_provided, LTE_multi, num_classes_prov) # compute the confusion matrix
    
    emit("\nProvided dataset confusion matrix:")
    print_confusion_matrix(M_provided, emit)


    emit("\n\n2. OPTIMAL BAYES DECISIONS\n")
    # ======================================================
    # 4. BINARY EVALUATION (TABULAR METRICS)
    # ======================================================
    # Load binary datasets
    llr1 = numpy.load(dataset_dir / "evalset_llr_binary.npy") # load log-likelihood ratios from the first dataset
    llr2 = numpy.load(dataset_dir / "evalset_llr_binary_2.npy") # load log-likelihood ratios from the second dataset
    LTE_bin = numpy.load(dataset_dir / "evalset_labels_binary.npy") # load true labels from the binary dataset
    
    applications = [
        (0.5, 1, 1),
        (0.8, 1, 1),
        (0.5, 10, 1),
        (0.8, 1, 10)
    ]
    
    # Process both classifiers cleanly
    for pi1, Cfn, Cfp, llr, model_name in zip(applications, [llr1, llr2], ["Standard MVG", "Tied MVG"]):
        emit(f"\n--- Application Metrics {model_name} ---")
        emit(f"{' (pi1, Cfn, Cfp)':^18} | {'DCF_u':^10} | {'DCF_n':^10} | {'min_DCF':^10}")
        emit("-" * 59)
        
        # Get optimal predictions and confusion matrix
        pred = compute_optimal_bayes_binary(llr, pi1, Cfn, Cfp) # get optimal predictions based on the  Bayes risk for each application
        M = compute_confusion_matrix(pred, LTE, num_classes=2) # compute the confusion matrix
        
        # Compute metrics
        DCF_u = compute_empirical_Bayes_risk_binary(M, pi1, Cfn, Cfp) # compute the empirical Bayes risk for each application
        DCF_n = compute_normalised_empirical_Bayes_risk_binary(M, pi1, Cfn, Cfp) # compute the normalized empirical Bayes risk for each application
        min_DCF = compute_min_dcf(llr, LTE, pi1, Cfn, Cfp) # compute the minimum Bayes risk for each application
        
        # Print row
        triplet_str = f"({pi1}, {Cfn}, {Cfp})"
        emit(f"{triplet_str:>18} | {DCF_u:>10.3f} | {DCF_n:>10.3f} | {min_DCF:>10.3f}")

    # ======================================================
    # 5. ROC CURVE
    # ======================================================
    FPR, TPR = compute_roc_coordinates(llr1, LTE_bin) # compute the ROC curve for the first dataset
    
    roc_output_path = results_dir / "ROC_binary_evaluation.png"
    plot_roc_curve(FPR, TPR, roc_output_path) # plot the ROC curve for the first dataset


    # ======================================================
    # 6. BAYES ERROR PLOTS
    # ======================================================
    effPriorLogOdds = numpy.linspace(-3, 3, 21) # compute the effective prior log-odds
    pi_array = 1 / (1 + numpy.exp(-effPriorLogOdds)) # compute the effective priors

    # Sweep for Classifier 1
    dcf_1, min_dcf_1 = sweep_bayes_error(llr1, LTE_bin, pi_array) # compute the DCF and min DCF for the first dataset
    
    # Sweep for Classifier 2
    dcf_2, min_dcf_2 = sweep_bayes_error(llr2, LTE_bin, pi_array) # compute the DCF and min DCF for the second dataset

    # Plot single Bayes Error
    bayes_single_path = results_dir / "Bayes_Error_binary_evaluation_classifier1.png"
    plot_bayes_error(effPriorLogOdds, dcf_1, min_dcf_1, bayes_single_path) # plot the Bayes error for the first dataset
    plot_bayes_error(effPriorLogOdds, dcf_2, min_dcf_2, results_dir / "Bayes_Error_binary_evaluation_classifier2.png") # plot the Bayes error for the second dataset
    
    # Plot comparative Bayes Error (Classifier 1 vs Classifier 2)
    bayes_comp_path = results_dir / "Bayes_Error_Comparison.png" # create the path for the comparative Bayes error plot
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
    emit("\n\n3. MULTICLASS EVALUATION")

    # Load multiclass datasets
    ll_multi_1 = numpy.load(dataset_dir / "evalset_ll.npy")
    ll_multi_2 = numpy.load(dataset_dir / "evalset_ll_2.npy")
    LTE_multi = numpy.load(dataset_dir / "evalset_labels.npy")

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
    emit("\n--- Confusion matrix of classifier 1 (evalset_ll.npy) ---")
    
    _, _, logSPost_multi_1 = compute_posteriors(ll_multi_1, prior_multi) # compute the posterior probabilities of the test set given the model using the priors
    pred_multi_1 = compute_optimal_bayes_multiclass(logSPost_multi_1, Cost_multi) # compute the optimal predictions based on maximum a posteriori (MAP)
    M_multi_1 = compute_confusion_matrix(pred_multi_1, LTE_multi, num_classes_multi) # compute the confusion matrix
    
    print_confusion_matrix(M_multi_1, emit)
    DCF_u_1 = compute_empirical_Bayes_risk_multiclass(M_multi_1, prior_multi, Cost_multi) # compute the empirical Bayes risk for each application
    DCF_n_1 = compute_normalised_empirical_Bayes_risk_multiclass(M_multi_1, prior_multi, Cost_multi) # compute the normalized empirical Bayes risk for each application

    # --- Evaluate Classifier 2 ---
    emit("\n--- Confusion matrix of classifier 2 (evalset_ll_2.npy) ---")
    
    _, _, logSPost_multi_2 = compute_posteriors(ll_multi_2, prior_multi) # compute the posterior probabilities of the test set given the model using the priors
    pred_multi_2 = compute_optimal_bayes_multiclass(logSPost_multi_2, Cost_multi) # compute the optimal predictions based on maximum a posteriori (MAP)
    M_multi_2 = compute_confusion_matrix(pred_multi_2, LTE_multi, num_classes_multi) # compute the confusion matrix
    
    print_confusion_matrix(M_multi_2, emit)
    DCF_u_2 = compute_empirical_Bayes_risk_multiclass(M_multi_2, prior_multi, Cost_multi) # compute the empirical Bayes risk for each application
    DCF_n_2 = compute_normalised_empirical_Bayes_risk_multiclass(M_multi_2, prior_multi, Cost_multi) # compute the normalized empirical Bayes risk for each application

    # ------------------------------------------------------
    # PART B: Uniform priors and costs
    # ------------------------------------------------------
    Cost_uniform = numpy.ones((num_classes_multi, num_classes_multi)) - numpy.eye(num_classes_multi) # compute the uniform cost matrix
    prior_uniform = numpy.ones(num_classes_multi) / num_classes_multi # compute the uniform prior

    # Classifier 1
    _, _, logSPost_uni_1 = compute_posteriors(ll_multi_1, prior_uniform) # compute the posterior probabilities of the test set given the model using the priors
    pred_uni_1 = compute_optimal_bayes_multiclass(logSPost_uni_1, Cost_uniform) # compute the optimal predictions based on maximum a posteriori (MAP)
    M_uni_1 = compute_confusion_matrix(pred_uni_1, LTE_multi, num_classes_multi) # compute the confusion matrix
    DCF_u_uni_1 = compute_empirical_Bayes_risk_multiclass(M_uni_1, prior_uniform, Cost_uniform) # compute the empirical Bayes risk for each application
    DCF_n_uni_1 = compute_normalised_empirical_Bayes_risk_multiclass(M_uni_1, prior_uniform, Cost_uniform) # compute the normalized empirical Bayes risk for each application

    # Classifier 2
    _, _, logSPost_uni_2 = compute_posteriors(ll_multi_2, prior_uniform) # compute the posterior probabilities of the test set given the model using the priors
    pred_uni_2 = compute_optimal_bayes_multiclass(logSPost_uni_2, Cost_uniform) # compute the optimal predictions based on maximum a posteriori (MAP)
    M_uni_2 = compute_confusion_matrix(pred_uni_2, LTE_multi, num_classes_multi) # compute the confusion matrix
    DCF_u_uni_2 = compute_empirical_Bayes_risk_multiclass(M_uni_2, prior_uniform, Cost_uniform) # compute the empirical Bayes risk for each application
    DCF_n_uni_2 = compute_normalised_empirical_Bayes_risk_multiclass(M_uni_2, prior_uniform, Cost_uniform) # compute the normalized empirical Bayes risk for each application

    # Print the requested comparative table
    emit("\n--- Multiclass evaluation (Uniform priors and costs) ---")
    emit("-" * 37)
    emit(f"{'':<15} | {'DCF_u':^7} | {'DCF':^7}")
    emit("-" * 37)
    emit(f"{'Classifier 1':<15} | {DCF_u_uni_1:^7.3f} | {DCF_n_uni_1:^7.3f}")
    emit(f"{'Classifier 2':<15} | {DCF_u_uni_2:^7.3f} | {DCF_n_uni_2:^7.3f}")
    emit("-" * 37)