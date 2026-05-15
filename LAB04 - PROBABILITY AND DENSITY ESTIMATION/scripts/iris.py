import numpy
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

# Ensure these match your actual import paths
from utils.data_loaders import load_dataset, split_dataset
from utils.math_utils import compute_covariance_matrix, vrow
from models.MVG import log_MVG
from utils.io_utils import *
from utils.plot_utils import plot_feature_histogram

# Set backend to avoid GUI pop-ups during bulk plot generation
matplotlib.use("Agg")


def validate_array(computed_array, expected_path, name, emit):
    """
    Validates a computed array against a saved .npy expected result, using the emit function.
    """
    if Path(expected_path).exists():
        expected_array = numpy.load(expected_path)
        max_diff = numpy.max(numpy.abs(computed_array - expected_array))
        if numpy.allclose(computed_array, expected_array, atol=1e-5):
            emit(f"  [PASS] {name} matches the expected results! (Max diff: {max_diff:.2e})")
        else:
            emit(f"  [FAIL] {name} DIFFERS from expected! Max diff: {max_diff:.2e}")
    else:
        emit(f"  [SKIP] Validation file for {name} not found at {expected_path}")


if __name__ == "__main__":
    ROOT = Path(".")
    
    # Paths for saving outputs and finding validation files
    output_dir = ROOT / "results" / "iris"
    mle_dir = output_dir / "MLE"
    mvg_dir = output_dir / "MVG"
    
    # Assuming your validation .npy files are in a "Solution" or similar folder
    validation_dir = ROOT / "Solution" 
    
    mle_dir.mkdir(parents=True, exist_ok=True)
    mvg_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize the emitter
    report_path = output_dir / "iris_lab04_metrics.txt"
    emit = create_emitter(report_path)

    # Load and split dataset
    D, L = load_dataset(ROOT / "data" / "iris" / "iris_dataset.csv")
    (DTR, LTR), (DVAL, LVAL) = split_dataset(D, L, 2.0 / 3.0)
    
    classes = [0, 1, 2]
    num_classes = len(classes)
    
    emit("1. Training MVG Model (Computing mu and C for each class)...")
    
    # 1. Train the MVG model
    mu_c = []
    C_c = []
    for cls in classes:
        DTR_c = DTR[:, LTR == cls]
        # Keep dimensions for mu so it remains a column vector
        mu = numpy.mean(DTR_c, axis=1, keepdims=True)
        C = compute_covariance_matrix(DTR_c)
        mu_c.append(mu)
        C_c.append(C)

    emit(f"  [INFO] Class Means (mu_c):")
    for i, mu in enumerate(mu_c):
        emit(f"    Class {i}: {mu.flatten()}")
    
    emit(f"\n  [INFO] Class Covariance Matrices (C_c):")
    for i, C in enumerate(C_c):
        emit(f"    Class {i}:\n{C}\n")

    emit("2. Testing MVG Model (Computing Log-Likelihoods)...")
    
    # 2. Test the MVG model
    log_prior = numpy.log(1.0 / num_classes)
    
    # Compute class-conditional log-likelihoods
    S_log = numpy.zeros((num_classes, DVAL.shape[1]))
    for cls in classes:
        S_log[cls, :] = log_MVG(DVAL, mu_c[cls], C_c[cls])

    emit(f"\n  [INFO] Class Conditionals (S_log):")
    for i, row in enumerate(S_log):
        emit(f"    Sample {i}: {row}")

    emit("\n--- VALIDATION: Class Conditionals (S_log) ---")
    # VALIDATION 1: Check S_log matrix against the file provided by the lab
    validate_array(S_log, validation_dir / "llND.npy", "S_log (Class Conditionals)", emit)
    
    # Compute Joint Log-Likelihoods
    log_S_joint = S_log + log_prior
    
    emit("\n--- VALIDATION: Joint Log-Likelihoods (log_S_joint) ---")
    # VALIDATION 2: Check Joint Log-Likelihood matrix against the file provided by the lab
    validate_array(log_S_joint, validation_dir / "llGAU.npy", "log_S_joint (Joint Log-Likelihoods)", emit)
    
    # Predict the class by finding the index (class) with the maximum joint log-probability
    PVAL = numpy.argmax(log_S_joint, axis=0)
    
    # Compute Final Evaluation Metrics
    correct_predictions = numpy.sum(PVAL == LVAL)
    total_samples = len(LVAL)
    accuracy = correct_predictions / total_samples
    error_rate = 1.0 - accuracy
    
    emit("\n" + "=" * 70)
    emit("FINAL CLASSIFICATION METRICS (MVG)")
    emit("=" * 70)
    emit(f"Total Validation Samples : {total_samples}")
    emit(f"Correct Predictions      : {correct_predictions}")
    emit(f"Accuracy                 : {accuracy * 100:.2f}%")
    emit(f"Error Rate               : {error_rate * 100:.2f}%")
    emit("=" * 70)
    
    emit(f"\n[+] Script execution complete. Results saved to: {report_path}")