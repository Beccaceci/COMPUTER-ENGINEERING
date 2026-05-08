import sys
import numpy
from pathlib import Path

from utils.data_loaders import load_dataset, split_dataset
from utils.math_utils import compute_covariance_matrix, mcol, vrow
from utils.plot_utils import plot_histograms
from utils.PCA import PCA

from models.MVGclassifier import compute_MVG_parameters
from models.NaiveBayesclassifier import compute_naive_bayes_parameters
from models.TiedMVGclassifier import compute_tied_mvg_parameters 

def analyze_correlations(DTR, LTR):
    """
    Analyzes the correlation structure of the features for each class in the training set.
    For each class, it computes the covariance matrix and then derives the correlation matrix.
    The results are printed to the console.
    """
    corr_results = {}
    
    # Dynamically determine the number of classes and create a uniform prior array
    classes = numpy.unique(LTR)

    for c in classes:
        Dc = DTR[:, LTR == c]
        
        # Compute the empirical mean (uc) and covariance matrix (sigmac)
        uc = numpy.mean(Dc, axis=1, keepdims=True)
        sigmac = compute_covariance_matrix(Dc, uc)
        corr = sigmac / ( mcol(sigmac.diagonal()**0.5) * vrow(sigmac.diagonal()**0.5) )

        corr_results[c] = {
            "Covariance Matrix": sigmac,
            "Correlation Matrix": corr
        }
        
    return corr_results

def evaluate_feature_ablation(DTR, LTR, DTE, LTE):
    ablation_results = {}
    
    # Define the subsets: "Display Name": (start_row, end_row)
    # Note: end_row is exclusive in Python slicing
    subsets = {
        "Features 1-4 (Indices 0 to 3)": (0, 4),
        "Features 1-2 (Indices 0 to 1)": (0, 2),
        "Features 3-4 (Indices 2 to 3)": (2, 4),
        "Features 5-6 (Indices 4 to 5)": (4, 6) # Added as requested
    }

    for name, (start, end) in subsets.items():
        # Slice the data dynamically
        DTR_sub = DTR[start:end, :]
        DTE_sub = DTE[start:end, :]
        
        metrics = {}
        
        # --- Standard MVG ---
        logSJoint_mvg, _, _ = compute_MVG_parameters(DTR_sub, LTR, DTE_sub)
        pred_mvg = numpy.argmax(logSJoint_mvg, axis=0)
        metrics["Standard MVG"] = round((1 - (numpy.sum(pred_mvg == LTE) / len(LTE))) * 100, 1)

        # --- Tied MVG ---
        logSJoint_tied, _, _ = compute_tied_mvg_parameters(DTR_sub, LTR, DTE_sub)
        pred_tied = numpy.argmax(logSJoint_tied, axis=0)
        metrics["Tied MVG"] = round((1 - (numpy.sum(pred_tied == LTE) / len(LTE))) * 100, 1)

        # We only strictly need Naive Bayes for the 1-4 ablation, 
        # but printing it for all subsets doesn't hurt!
        logSJoint_nb, _, _ = compute_naive_bayes_parameters(DTR_sub, LTR, DTE_sub)
        pred_nb = numpy.argmax(logSJoint_nb, axis=0)
        metrics["Naive Bayes"] = round((1 - (numpy.sum(pred_nb == LTE) / len(LTE))) * 100, 1)
        
        ablation_results[name] = metrics

    return ablation_results

def evaluate_pca(DTR, LTR, DTE, LTE):
    """
    Evaluates the performance of the classifiers after applying PCA for dimensionality reduction.
    It iterates through dimensions from 1 to the total number of features, applies PCA on the training set, projects the evaluation set, and then computes the error rates for each classifier.
    """
    pca_results = {}
    num_features = DTR.shape[0]

    # Loop through dimensions from 1 up to the total number of features (6)
    for m in range(1, num_features + 1):
        metrics = {}
        
        # 1. Compute PCA on the TRAINING set only
        # DTR_pca is the projected training data, P is the projection matrix
        DTR_pca, P = PCA(DTR, m)
        
        # 2. Project the EVALUATION set using the P matrix learned from training
        DTE_pca = numpy.transpose(P) @ DTE
        
        # --- Standard MVG ---
        logSJoint_mvg, _, _ = compute_MVG_parameters(DTR_pca, LTR, DTE_pca)
        pred_mvg = numpy.argmax(logSJoint_mvg, axis=0)
        metrics["Standard MVG"] = round((1 - (numpy.sum(pred_mvg == LTE) / len(LTE))) * 100, 1)
        
        # --- Naive Bayes ---
        logSJoint_nb, _, _ = compute_naive_bayes_parameters(DTR_pca, LTR, DTE_pca)
        pred_nb = numpy.argmax(logSJoint_nb, axis=0)
        metrics["Naive Bayes"] = round((1 - (numpy.sum(pred_nb == LTE) / len(LTE))) * 100, 1)

        # --- Tied MVG ---
        logSJoint_tied, _, _ = compute_tied_mvg_parameters(DTR_pca, LTR, DTE_pca)
        pred_tied = numpy.argmax(logSJoint_tied, axis=0)
        metrics["Tied MVG"] = round((1 - (numpy.sum(pred_tied == LTE) / len(LTE))) * 100, 1)
        
        pca_results[f"PCA Dimension: m = {m}"] = metrics
        
    return pca_results

def evaluate_base_models(DTR, LTR, DTE, LTE):
    """
    Computes the baseline metrics for the three primary classifiers on the full dataset.
    """
    base_results = {}
    
    # --- 1. Standard Multivariate Gaussian (MVG) ---
    # Execute the core MVG math to get the joint log-probabilities
    logSJoint_mvg, _, _ = compute_MVG_parameters(DTR, LTR, DTE)
    pred_mvg = numpy.argmax(logSJoint_mvg, axis=0)
    acc_mvg = numpy.sum(pred_mvg == LTE) / len(LTE)
    base_results["Standard MVG"] = {"Accuracy": round(acc_mvg * 100, 2), "Error Rate": round((1 - acc_mvg) * 100, 1)}

    # --- 2. Naive Bayes Gaussian ---
    # Execute the Naive Bayes logic (using diagonal covariance matrices)
    logSJoint_nb, _, _ = compute_naive_bayes_parameters(DTR, LTR, DTE)
    pred_nb = numpy.argmax(logSJoint_nb, axis=0)
    acc_nb = numpy.sum(pred_nb == LTE) / len(LTE)
    base_results["Naive Bayes"] = {"Accuracy": round(acc_nb * 100, 2), "Error Rate": round((1 - acc_nb) * 100, 1)}

    # --- 3. Tied Covariance Gaussian ---
    # Execute the Tied MVG logic (using a single shared covariance matrix)
    logSJoint_tied, _, _ = compute_tied_mvg_parameters(DTR, LTR, DTE)
    pred_tied = numpy.argmax(logSJoint_tied, axis=0)
    acc_tied = numpy.sum(pred_tied == LTE) / len(LTE)
    base_results["Tied Covariance MVG"] = {"Accuracy": round(acc_tied * 100, 2), "Error Rate": round((1 - acc_tied) * 100, 1)}
    
    return base_results

def display_and_save_results(base_res, corr_res, ablation_res, pca_res, output_dir):
    """
    Apposite function in charge of visualising the output and saving error rates to a file.
    """
    output_lines = []
    
    def emit(text):
        print(text)
        output_lines.append(text)

    emit("\n==========================================")
    emit("--- PROJECT DATASET EVALUATION ---")
    emit("==========================================")
    for model, metrics in base_res.items():
        emit(f"\n--- {model} ---")
        emit(f"Accuracy: {metrics['Accuracy']}%")
        emit(f"Error Rate: {metrics['Error Rate']}%")

    emit("\n==========================================")
    emit("--- CORRELATION ANALYSIS ---")
    emit("==========================================")
    for cls, matrices in corr_res.items():
        emit(f"\n--- Class {cls} ---")
        emit("Covariance Matrix:")
        emit(str(matrices["Covariance Matrix"]))
        emit("Correlation Matrix:")
        emit(str(matrices["Correlation Matrix"]))

    emit("\n==========================================")
    emit("--- FEATURE ABLATION ---")
    emit("==========================================")
    for subset, metrics in ablation_res.items():
        emit(f"\n--- {subset} ---")
        for model, err in metrics.items():
            emit(f"{model} Error Rate: {err}%")

    emit("\n==========================================")
    emit("--- PCA PRE-PROCESSING ANALYSIS ---")
    emit("==========================================")
    for dim, metrics in pca_res.items():
        emit(f"\n--- {dim} ---")
        for model, err in metrics.items():
            emit(f"{model} Error Rate: {err}%")
    emit("\n==========================================\n")

    # Save to file in results/project/metrics
    results_file = output_dir / "project_evaluation_metrics.txt"
    with open(results_file, "w") as f:
        f.write("\n".join(output_lines))
    print(f"Metrics successfully saved to: {results_file}")

if __name__ == "__main__":
    # ==========================================
    # SETUP & CONFIGURATION
    # ==========================================
    ROOT = Path(".")
    results_dir = ROOT / "results" / "project"
    histograms_dir = results_dir / "histograms"
    metrics_dir = results_dir / "metrics"
    
    # Create required folders
    results_dir.mkdir(parents=True, exist_ok=True)
    histograms_dir.mkdir(parents=True, exist_ok=True)
    metrics_dir.mkdir(parents=True, exist_ok=True)

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = ROOT / "data" / "project" / "trainData.txt"
        
    # ==========================================
    # DATA PIPELINE
    # ==========================================
    D, L = load_dataset(file_path)
    ((DTR, LTR), (DTE, LTE)) = split_dataset(D, L, 2/3)
    
    # ==========================================
    # MODEL EXECUTION & EVALUATION
    # ==========================================
    
    # Gather all metrics without printing
    base_metrics = evaluate_base_models(DTR, LTR, DTE, LTE)
    corr_metrics = analyze_correlations(DTR, LTR)
    ablation_metrics = evaluate_feature_ablation(DTR, LTR, DTE, LTE)
    pca_metrics = evaluate_pca(DTR, LTR, DTE, LTE)
    
    # Note: Assuming plot_histograms is updated to accept an output directory parameter. 
    # If not, you may need to update plot_utils.py to utilize 'histograms_dir' internally.
    plot_histograms(DTR, LTR, output_dir=histograms_dir) 

    # ==========================================
    # VISUALIZATION & SAVING
    # ==========================================
    # Route text outputs specifically to the metrics folder
    display_and_save_results(base_metrics, corr_metrics, ablation_metrics, pca_metrics, metrics_dir)