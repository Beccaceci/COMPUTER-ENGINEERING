import numpy
import matplotlib
from pathlib import Path

# Reuse existing utilities
from utils.data_loaders import load_dataset, split_dataset
from utils.io_utils import write_matrix

# Import the three Gaussian models
from models.MVGclassifier import compute_MVG_parameters
from models.NaiveBayesclassifier import compute_naive_bayes_parameters
from models.TiedMVGclassifier import compute_tied_mvg_parameters

# Headless backend
matplotlib.use("Agg")


def validate_results(computed, expected_path, name):
    """
    Validates a computed matrix against the provided expected solution.
    """
    if Path(expected_path).exists():
        expected = numpy.load(expected_path)
        max_diff = numpy.max(numpy.abs(computed - expected))

        if numpy.allclose(computed, expected, atol=1e-5):
            print(f"  [PASS] {name} matches expected results (Diff: {max_diff:.2e})")
        else:
            print(f"  [FAIL] {name} mismatch! (Diff: {max_diff:.2e})")
    else:
        print(f"  [SKIP] Validation file {expected_path.name} not found.")


def run_iris_evaluation(DTR, LTR, DTE, LTE, val_dir):
    """
    Evaluates the three Gaussian models and validates them
    using the expected filenames from solutions/expected_results.
    """
    results = {}

    # ======================================================
    # 1. Standard MVG
    # ======================================================
    print("\n--- Evaluating Standard MVG ---")

    logSJoint, logMarginal, logPosterior = compute_MVG_parameters(DTR, LTR, DTE)

    validate_results(logSJoint, val_dir / "logSJoint_MVG.npy", "logSJoint MVG")
    validate_results(logMarginal, val_dir / "logMarginal_MVG.npy", "logMarginal MVG")
    validate_results(logPosterior, val_dir / "logPosterior_MVG.npy", "logPosterior MVG")

    SJoint = numpy.exp(logSJoint)
    Posterior = numpy.exp(logPosterior)
    llr = logPosterior[1, :] - logPosterior[0, :]

    validate_results(SJoint, val_dir / "SJoint_MVG.npy", "SJoint MVG")
    validate_results(Posterior, val_dir / "Posterior_MVG.npy", "Posterior MVG")
    validate_results(llr, val_dir / "llr_MVG.npy", "llr MVG")

    pred = numpy.argmax(logPosterior, axis=0)
    results["Standard MVG"] = round(
        (1 - numpy.sum(pred == LTE) / len(LTE)) * 100, 2
    )

    # ======================================================
    # 2. Naive Bayes
    # ======================================================
    print("\n--- Evaluating Naive Bayes ---")

    logSJoint_nb, logMarginal_nb, logPosterior_nb = compute_naive_bayes_parameters(
        DTR, LTR, DTE
    )

    validate_results(
        logSJoint_nb,
        val_dir / "logSJoint_NaiveBayes.npy",
        "logSJoint NaiveBayes",
    )
    validate_results(
        logMarginal_nb,
        val_dir / "logMarginal_NaiveBayes.npy",
        "logMarginal NaiveBayes",
    )
    validate_results(
        logPosterior_nb,
        val_dir / "logPosterior_NaiveBayes.npy",
        "logPosterior NaiveBayes",
    )

    SJoint_nb = numpy.exp(logSJoint_nb)
    Posterior_nb = numpy.exp(logPosterior_nb)

    validate_results(
        SJoint_nb,
        val_dir / "SJoint_NaiveBayes.npy",
        "SJoint NaiveBayes",
    )
    validate_results(
        Posterior_nb,
        val_dir / "Posterior_NaiveBayes.npy",
        "Posterior NaiveBayes",
    )

    pred_nb = numpy.argmax(logPosterior_nb, axis=0)
    results["Naive Bayes"] = round(
        (1 - numpy.sum(pred_nb == LTE) / len(LTE)) * 100, 2
    )

    # ======================================================
    # 3. Tied MVG
    # ======================================================
    print("\n--- Evaluating Tied MVG ---")

    logSJoint_tied, logMarginal_tied, logPosterior_tied = compute_tied_mvg_parameters(
        DTR, LTR, DTE
    )

    validate_results(
        logSJoint_tied,
        val_dir / "logSJoint_TiedMVG.npy",
        "logSJoint TiedMVG",
    )
    validate_results(
        logMarginal_tied,
        val_dir / "logMarginal_TiedMVG.npy",
        "logMarginal TiedMVG",
    )
    validate_results(
        logPosterior_tied,
        val_dir / "logPosterior_TiedMVG.npy",
        "logPosterior TiedMVG",
    )

    SJoint_tied = numpy.exp(logSJoint_tied)
    Posterior_tied = numpy.exp(logPosterior_tied)

    validate_results(
        SJoint_tied,
        val_dir / "SJoint_TiedMVG.npy",
        "SJoint TiedMVG",
    )
    validate_results(
        Posterior_tied,
        val_dir / "Posterior_TiedMVG.npy",
        "Posterior TiedMVG",
    )

    pred_tied = numpy.argmax(logPosterior_tied, axis=0)
    results["Tied MVG"] = round(
        (1 - numpy.sum(pred_tied == LTE) / len(LTE)) * 100, 2
    )

    return results


if __name__ == "__main__":
    ROOT = Path(".")

    # Paths
    results_dir = ROOT / "results" / "iris" / "metrics"
    results_dir.mkdir(parents=True, exist_ok=True)

    val_dir = ROOT / "solutions" / "expected_results"

    # Data loading
    D, L = load_dataset(ROOT / "data" / "iris_dataset.csv")
    (DTR, LTR), (DTE, LTE) = split_dataset(D, L, percTrain=2.0 / 3.0)

    # Run evaluation
    final_errors = run_iris_evaluation(DTR, LTR, DTE, LTE, val_dir)

    # Summary
    print("\n==========================================")
    print("--- IRIS CLASSIFICATION RESULTS ---")
    print("==========================================")

    summary_data = []
    for model, err in final_errors.items():
        print(f"{model}: {err}% Error Rate")
        summary_data.append([model, f"{err}%"])

    # Save CSV
    write_matrix(
        results_dir / "iris_error_rates.csv",
        ["Model", "Error Rate"],
        summary_data
    )