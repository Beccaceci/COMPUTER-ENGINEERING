import numpy
import matplotlib
from pathlib import Path

# Reuse existing utilities
from utils.data_loaders import load_dataset, split_dataset
from utils.io_utils import write_matrix, print_model_table

# Import the three Gaussian models
from models.MVGclassifier import compute_MVG_parameters
from models.NaiveBayesclassifier import compute_naive_bayes_parameters
from models.TiedMVGclassifier import compute_tied_mvg_parameters
from models.binaryClassificationTask import compute_binary_mvg, compute_binary_tied_mvg


def create_emitter(file_path):
    """
    Creates an emit function that prints to standard output AND appends to a text file.
    It automatically clears the target file upon initialization.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as f:
        f.write("LAB 05: GENERATIVE GAUSSIAN MODELS (IRIS DATASET)\n")
        f.write("=" * 60 + "\n")
        
    def emit(text=""):
        print(text)
        with open(file_path, "a") as f:
            f.write(str(text) + "\n")
    return emit


if __name__ == "__main__":
    ROOT = Path(".")

    # Setup output routing
    input_dir = ROOT / "data" / "iris"
    output_dir = ROOT / "results" / "iris"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    report_path = output_dir / "iris_lab05_metrics.txt"
    emit = create_emitter(report_path)

    # val_dir = ROOT / "solutions" / "expected_results"

    # Data loading
    D, L = load_dataset(input_dir / "iris_dataset.csv")
    (DTR, LTR), (DTE, LTE) = split_dataset(D, L, percTrain=2.0 / 3.0)

    # Run evaluation
    results = {}


    # ======================================================
    # 1. Standard MVG
    # ======================================================
    print("\n--- Standard MVG ---")

    logSJoint_mvg, logSMarginal_mvg, logSPost_mvg = compute_MVG_parameters(DTR, LTR, DTE)

    # validate_results(logSJoint, val_dir / "logSJoint_MVG.npy", "logSJoint MVG")
    # validate_results(logMarginal, val_dir / "logMarginal_MVG.npy", "logMarginal MVG")
    # validate_results(logPosterior, val_dir / "logPosterior_MVG.npy", "logPosterior MVG")

    SJoint = numpy.exp(logSJoint_mvg)
    Posterior = numpy.exp(logSPost_mvg)
    llr = logSPost_mvg[1, :] - logSPost_mvg[0, :]

    # validate_results(SJoint, val_dir / "SJoint_MVG.npy", "SJoint MVG")
    # validate_results(Posterior, val_dir / "Posterior_MVG.npy", "Posterior MVG")
    # validate_results(llr, val_dir / "llr_MVG.npy", "llr MVG")

    # Compute the predict labels
    predicted_labels = numpy.argmax(logSJoint_mvg, axis=0)

    # Compute the accuracy and error rate
    accuracy = numpy.sum(predicted_labels == LTE) / len(LTE)
    error_rate_mvg = round((1 - accuracy) * 100, 2)
    results["Standard MVG"] = error_rate_mvg

    # Print the results in a table format
    print_model_table("Multivariate Gaussian (MVG)", logSJoint_mvg, logSMarginal_mvg, logSPost_mvg, error_rate_mvg, emit)


    # ======================================================
    # 2. Naive Bayes
    # ======================================================
    print("\n--- Naive Bayes ---")

    logSJoint_nb, logSMarginal_nb, logSPost_nb = compute_naive_bayes_parameters(DTR, LTR, DTE)

    # validate_results(logSJoint_nb, val_dir / "logSJoint_NaiveBayes.npy", "logSJoint NaiveBayes")
    # validate_results(logMarginal_nb, val_dir / "logMarginal_NaiveBayes.npy", "logMarginal NaiveBayes")
    # validate_results(logPosterior_nb, val_dir / "logPosterior_NaiveBayes.npy", "logPosterior NaiveBayes")

    SJoint_nb = numpy.exp(logSJoint_nb)
    Posterior_nb = numpy.exp(logSPost_nb)

    # validate_results(SJoint_nb, val_dir / "SJoint_NaiveBayes.npy", "SJoint NaiveBayes")
    # validate_results(Posterior_nb, val_dir / "Posterior_NaiveBayes.npy", "Posterior NaiveBayes")

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

    logSJoint_tied, logSMarginal_tied, logSPost_tied = compute_tied_mvg_parameters(
        DTR, LTR, DTE
    )

    # validate_results(logSJoint_tied, val_dir / "logSJoint_TiedMVG.npy", "logSJoint TiedMVG")
    #validate_results(logMarginal_tied, val_dir / "logMarginal_TiedMVG.npy", "logMarginal TiedMVG")
    # validate_results(logPosterior_tied, val_dir / "logPosterior_TiedMVG.npy", "logPosterior TiedMVG")

    SJoint_tied = numpy.exp(logSJoint_tied)
    Posterior_tied = numpy.exp(logSPost_tied)

    # validate_results(SJoint_tied, val_dir / "SJoint_TiedMVG.npy", "SJoint TiedMVG")
    # validate_results(Posterior_tied, val_dir / "Posterior_TiedMVG.npy", "Posterior TiedMVG")

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
    llr_mvg = compute_binary_mvg(DTR_bin, LTR_bin, DTE_bin)
    pred_mvg = (llr_mvg > 0).astype(int) + 1
    binary_err_mvg = numpy.sum(pred_mvg != LTE_bin) / len(LTE_bin)
    emit(f"-> Binary MVG Error Rate:        {binary_err_mvg * 100:.1f}%")

    # Binary Tied MVG
    llr_tied = compute_binary_tied_mvg(DTR_bin, LTR_bin, DTE_bin)
    pred_tied = (llr_tied > 0).astype(int) + 1
    binary_err_tied = numpy.sum(pred_tied != LTE_bin) / len(LTE_bin)
    emit(f"-> Binary Tied MVG Error Rate:   {binary_err_tied * 100:.1f}%")

    emit(f"\n[+] Script execution complete. Metrics saved to: {report_path}")