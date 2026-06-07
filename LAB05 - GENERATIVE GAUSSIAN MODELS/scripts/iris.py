import numpy
import matplotlib
from pathlib import Path

# Reuse existing utilities
from utils.data_loaders import load_dataset, split_dataset
from utils.io_utils import write_matrix, print_model_table, create_emitter

# Import the three Gaussian models
from models.MVGclassifier import compute_MVG_parameters, compute_binary_mvg
from models.NaiveBayesclassifier import compute_naive_bayes_parameters
from models.TiedMVGclassifier import compute_tied_mvg_parameters, compute_binary_tied_mvg


if __name__ == "__main__":
    # Setup output routing
    ROOT = Path(".")
    input_dir = ROOT / "data" / "iris"
    output_dir = ROOT / "results" / "iris"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    report_path = output_dir / "iris_lab05_metrics.txt"
    emit = create_emitter(report_path)

    # Data loading
    D, L = load_dataset(input_dir / "iris_dataset.csv")
    (DTR, LTR), (DTE, LTE) = split_dataset(D, L, percTrain=2.0 / 3.0)

    # Run evaluation
    results = {}


    # ======================================================
    # 1. Standard MVG
    # ======================================================
    print("\n--- Standard MVG ---")

    # Compute the log-likelihood of the data under the MVG model
    logSJoint_mvg, logSMarginal_mvg, logSPost_mvg = compute_MVG_parameters(DTR, LTR, DTE)

    # Compute the posterior probability and LLR
    llr_mvg = logSPost_mvg[1, :] - logSPost_mvg[0, :]

    # Compute the predict labels
    predicted_labels_mvg = numpy.argmax(logSJoint_mvg, axis=0)

    # Compute the accuracy and error rate
    accuracy_mvg = numpy.sum(predicted_labels_mvg == LTE) / len(LTE)
    error_rate_mvg = round((1 - accuracy_mvg) * 100, 2)
    results["Standard MVG"] = error_rate_mvg

    # Print the results in a table format
    print_model_table("Multivariate Gaussian (MVG)", logSJoint_mvg, logSMarginal_mvg, logSPost_mvg, error_rate_mvg, emit)


    # ======================================================
    # 2. Naive Bayes
    # ======================================================
    print("\n--- Naive Bayes ---")

    # Compute the log-likelihood of the data under the Naive Bayes model
    logSJoint_nb, logSMarginal_nb, logSPost_nb = compute_naive_bayes_parameters(DTR, LTR, DTE)

    # Compute the posterior probability and LLR
    llr_nb = logSPost_nb[1, :] - logSPost_nb[0, :]

    # Compute the predict labels
    predicted_labels_nb = numpy.argmax(logSJoint_nb, axis=0)

    # Compute the accuracy and error rate
    accuracy_nb = numpy.sum(predicted_labels_nb == LTE) / len(LTE)
    error_rate_nb = round((1 - accuracy_nb) * 100, 2)
    results["Naive Bayes"] = error_rate_nb

    # Print the results in a table format
    print_model_table("Naive Bayes Gaussian", logSJoint_nb, logSMarginal_nb, logSPost_nb, error_rate_nb, emit)


    # ======================================================
    # 3. Tied MVG
    # ======================================================
    print("\n--- Tied MVG ---")

    # Compute the log-likelihood of the data under the Tied MVG model
    logSJoint_tied, logSMarginal_tied, logSPost_tied = compute_tied_mvg_parameters(DTR, LTR, DTE)

    # Compute the posterior probability and LLR
    llr_tied = logSPost_tied[1, :] - logSPost_tied[0, :]

    # Compute the predict labels
    predicted_labels_tied = numpy.argmax(logSJoint_tied, axis=0)

    # Compute the accuracy and error rate
    accuracy_tied = numpy.sum(predicted_labels_tied == LTE) / len(LTE)
    error_rate_tied = round((1 - accuracy_tied) * 100, 2)
    results["Tied MVG"] = error_rate_tied

    # Print the results in a table format
    print_model_table("Tied Covariance Gaussian", logSJoint_tied, logSMarginal_tied, logSPost_tied, error_rate_tied, emit)

    # Compute the predict labels
    predicted_labels_tied = numpy.argmax(logSJoint_tied, axis=0)

    # Compute the accuracy and error rate
    accuracy_tied = numpy.sum(predicted_labels_tied == LTE) / len(LTE)
    error_rate_tied = round((1 - accuracy_tied) * 100, 2)
    results["Tied MVG"] = error_rate_tied

    # Print the results in a table format
    print_model_table("Tied Covariance Gaussian", logSJoint_tied, logSMarginal_tied, logSPost_tied, error_rate_tied, emit)


    # ======================================================
    # 4. Binary task
    # ======================================================
    emit("\n" + "=" * 80)
    emit("BINARY CLASSIFICATION TASK (Versicolor vs Virginica)")
    emit("=" * 80)
    
    # Create the binary dataset (drop class 0)
    binary_mask = L != 0
    D_bin = D[:, binary_mask]
    L_bin = L[binary_mask]
    (DTR_bin, LTR_bin), (DTE_bin, LTE_bin) = split_dataset(D_bin, L_bin, percTrain=2.0/3.0)
    
    emit(f"Binary Dataset Split: {DTR_bin.shape[1]} Training, {DTE_bin.shape[1]} Validation.\n")

    # Binary MVG
    llr_mvg = compute_binary_mvg(DTR_bin, LTR_bin, DTE_bin) # Returns the log-likelihood ratio for classes 2 and 1
    pred_mvg = (llr_mvg > 0).astype(int) + 1 # Predict labels based on the log-likelihood ratio
    binary_err_mvg = numpy.sum(pred_mvg != LTE_bin) / len(LTE_bin) # Compute the accuracy and error rate
    emit(f"-> Binary MVG Error Rate:        {binary_err_mvg * 100:.1f}%")

    # Binary Tied MVG
    llr_tied = compute_binary_tied_mvg(DTR_bin, LTR_bin, DTE_bin) # Returns the log-likelihood ratio for classes 2 and 1
    pred_tied = (llr_tied > 0).astype(int) + 1 # Predict labels based on the log-likelihood ratio
    binary_err_tied = numpy.sum(pred_tied != LTE_bin) / len(LTE_bin) # Compute the accuracy and error rate
    emit(f"-> Binary Tied MVG Error Rate:   {binary_err_tied * 100:.1f}%")

    emit(f"\n[+] Script execution complete. Metrics saved to: {report_path}")