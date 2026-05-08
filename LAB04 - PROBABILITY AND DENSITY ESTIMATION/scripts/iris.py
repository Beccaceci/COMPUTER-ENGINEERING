import numpy
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

# Ensure these match your actual import paths
from utils.data_loaders import load_dataset, split_dataset
from utils.math_utils import compute_covariance_matrix, vrow
from models.MVG import log_MVG
from utils.io_utils import write_matrix
from utils.plot_utils import plot_feature_histogram

# Set backend to avoid GUI pop-ups during bulk plot generation
matplotlib.use("Agg")

def validate_array(computed_array, expected_path, name):
    """
    Validates a computed array against a saved .npy expected result.
    """
    if Path(expected_path).exists():
        expected_array = numpy.load(expected_path)
        max_diff = numpy.max(numpy.abs(computed_array - expected_array))
        if numpy.allclose(computed_array, expected_array, atol=1e-5):
            print(f"  [PASS] {name} matches the expected results! (Max diff: {max_diff:.2e})")
        else:
            print(f"  [FAIL] {name} DIFFERS from expected! Max diff: {max_diff:.2e}")
    else:
        print(f"  [SKIP] Validation file for {name} not found at {expected_path}")

def generate_mle_analysis(X, y, output_dir):
    """
    MLE Logic: Computes 1D Gaussian parameters and plots them.
    """
    class_names = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    feature_names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
    num_features = X.shape[0]

    print("\n--- Generating MLE 1D Gaussian fits for Iris ---")
    for cls_id, cls_name in class_names.items():
        X_class = X[:, y == cls_id]
        for f_idx in range(num_features):
            x_feature = vrow(X_class[f_idx, :])
            mu_ML = numpy.mean(x_feature, axis=1, keepdims=True)
            C_ML = compute_covariance_matrix(x_feature)
            
            title = f"{cls_name} - {feature_names[f_idx]}"
            # Call the unified plotting function
            plot_feature_histogram(
                x_feature, mu_ML, C_ML, title, output_dir, bins=15, hist_color='green'
            )

def run_mvg_classification(X, y, output_dir, validation_dir):
    """
    MVG Logic: Splits the dataset, trains a Multivariate Gaussian classifier, 
    evaluates it, and validates matrices against expected results.
    """
    print("\n--- Running standard MVG Classification on Iris ---")
    
    (DTR, LTR), (DVAL, LVAL) = split_dataset(X, y, 2.0/3.0)
    classes = [0, 1, 2]
    num_classes = len(classes)
    
    # 1. Train the MVG model
    mu_c = []
    C_c = []
    for cls in classes:
        DTR_c = DTR[:, LTR == cls]
        mu_c.append(numpy.mean(DTR_c, axis=1, keepdims=True))
        C_c.append(compute_covariance_matrix(DTR_c))
        
    # 2. Test the MVG model
    log_prior = numpy.log(1.0 / num_classes)
    
    # Compute class-conditional log-likelihoods
    S_log = numpy.zeros((num_classes, DVAL.shape[1]))
    for cls in classes:
        S_log[cls, :] = log_MVG(DVAL, mu_c[cls], C_c[cls])
        
    # VALIDATION 1: Check S_log matrix
    # validate_array(S_log, validation_dir / "llND.npy", "S_log (Class Conditionals)")
        
    # Compute Joint Log-Likelihoods
    log_S_joint = S_log + log_prior
    
    # VALIDATION 2: Check Joint Log-Likelihood matrix
    # validate_array(log_S_joint, validation_dir / "llGAU.npy", "log_S_joint (Joint Log-Likelihoods)")
    
    # Predict the class 
    PVAL = numpy.argmax(log_S_joint, axis=0)
    
    # Calculate Error Rate
    error_count = numpy.sum(PVAL != LVAL)
    error_rate = error_count / LVAL.size
    
    metrics = [
        ["Total Validation Samples", LVAL.size],
        ["Misclassified Samples", error_count],
        ["Error Rate (%)", error_rate * 100],
        ["Accuracy (%)", (1 - error_rate) * 100]
    ]
    write_matrix(output_dir / "mvg_classification_metrics.csv", ["Metric", "Value"], metrics)
    print(f"MVG Error Rate: {error_rate * 100:.2f}%")   

if __name__ == "__main__":
    ROOT = Path(".")
    
    # Paths for saving outputs
    mle_dir = ROOT / "results" / "iris" / "MLE"
    mvg_dir = ROOT / "results" / "iris" / "MVG"
    mle_dir.mkdir(parents=True, exist_ok=True)
    mvg_dir.mkdir(parents=True, exist_ok=True)

    # Path to where you store the professor's .npy files for validation
    validation_dir = ROOT / "solutions" / "expected_results" 

    X, y = load_dataset(ROOT / "data" / "iris_dataset.csv")
    
    generate_mle_analysis(X, y, mle_dir)
    run_mvg_classification(X, y, mvg_dir, validation_dir)
    
    print("\nIris analysis and validations completed.")