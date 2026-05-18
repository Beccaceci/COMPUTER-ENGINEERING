import sys
import numpy
from pathlib import Path

from utils.data_loaders import load_dataset, split_dataset
from utils.math_utils import compute_covariance_matrix, mcol, vrow
from utils.plot_utils import plot_histograms
from utils.PCA import PCA
from utils.io_utils import create_emitter

from models.MVGclassifier import compute_MVG_parameters
from models.NaiveBayesclassifier import compute_naive_bayes_parameters
from models.TiedMVGclassifier import compute_tied_mvg_parameters 
from models.lda import compute_lda


# ==========================================
# SETUP & CONFIGURATION
# ==========================================
ROOT = Path(".")
results_dir = ROOT / "results" / "project"
histograms_dir = results_dir / "histograms"
metrics_dir = results_dir / "metrics"

# Create the emitter for the base models
base_report_path = metrics_dir / "project_lab05_results.txt"
emit_base = create_emitter(base_report_path)

def evaluate_base_models(DTR, LTR, DTE, LTE):
    """
    Computes the baseline metrics for the primary classifiers on the full dataset,
    strictly using explicit Log-Likelihood Ratios (LLRs). Logs results via the emitter.
    """
    emit = emit_base  # Use the base emitter for this function
    base_results = {}
    
    emit("\n" + "=" * 60)
    emit("BASE MODELS EVALUATION (Project Dataset)")
    emit("=" * 60)
    emit(f"{'Model':<25} | {'Accuracy':<12} | {'Error Rate'}")
    emit("-" * 60)

    # --- 1. Standard Multivariate Gaussian (MVG) ---
    logSJoint_mvg, _, _ = compute_MVG_parameters(DTR, LTR, DTE)
    llr_mvg = logSJoint_mvg[1, :] - logSJoint_mvg[0, :]
    pred_mvg = (llr_mvg >= 0).astype(int)
    acc_mvg = numpy.sum(pred_mvg == LTE) / len(LTE)
    err_mvg = 1 - acc_mvg
    base_results["Standard MVG"] = {"Accuracy": round(acc_mvg * 100, 2), "Error Rate": round(err_mvg * 100, 1)}
    emit(f"{'Standard MVG':<25} | {acc_mvg * 100:>11.2f}% | {err_mvg * 100:>9.1f}%")

    # --- 2. Naive Bayes Gaussian ---
    logSJoint_nb, _, _ = compute_naive_bayes_parameters(DTR, LTR, DTE)
    llr_nb = logSJoint_nb[1, :] - logSJoint_nb[0, :]
    pred_nb = (llr_nb >= 0).astype(int)
    acc_nb = numpy.sum(pred_nb == LTE) / len(LTE)
    err_nb = 1 - acc_nb
    base_results["Naive Bayes"] = {"Accuracy": round(acc_nb * 100, 2), "Error Rate": round(err_nb * 100, 1)}
    emit(f"{'Naive Bayes':<25} | {acc_nb * 100:>11.2f}% | {err_nb * 100:>9.1f}%")

    # --- 3. Tied Covariance Gaussian ---
    logSJoint_tied, _, _ = compute_tied_mvg_parameters(DTR, LTR, DTE)
    llr_tied = logSJoint_tied[1, :] - logSJoint_tied[0, :]
    pred_tied = (llr_tied >= 0).astype(int)
    acc_tied = numpy.sum(pred_tied == LTE) / len(LTE)
    err_tied = 1 - acc_tied
    base_results["Tied Covariance MVG"] = {"Accuracy": round(acc_tied * 100, 2), "Error Rate": round(err_tied * 100, 1)}
    emit(f"{'Tied Covariance MVG':<25} | {acc_tied * 100:>11.2f}% | {err_tied * 100:>9.1f}%")
    
    # --- 4. Linear Discriminant Analysis (LDA) ---
    _, W_lda = compute_lda(DTR, LTR, m=1)
    DTR_lda = W_lda.T @ DTR
    DTE_lda = W_lda.T @ DTE

    if DTR_lda[0, LTR == 1].mean() < DTR_lda[0, LTR == 0].mean():
        DTR_lda = -DTR_lda
        DTE_lda = -DTE_lda

    threshold_lda = (DTR_lda[0, LTR == 0].mean() + DTR_lda[0, LTR == 1].mean()) / 2.0
    pred_lda = (DTE_lda[0, :] >= threshold_lda).astype(int)
    acc_lda = numpy.sum(pred_lda == LTE) / len(LTE)
    err_lda = 1 - acc_lda
    base_results["LDA"] = {"Accuracy": round(acc_lda * 100, 2), "Error Rate": round(err_lda * 100, 1)}
    emit(f"{'LDA':<25} | {acc_lda * 100:>11.2f}% | {err_lda * 100:>9.1f}%")
    emit("=" * 60)

def analyze_correlations(DTR, LTR):
    """
    Analyzes the correlation structure of the features for each class in the training set.
    Logs the neatly formatted Covariance and Correlation matrices using the emitter.
    """
    emit = emit_base  # Use the provided emitter for logging
    corr_results = {}
    classes = numpy.unique(LTR)
    class_names = {0: "Fake", 1: "Genuine"}
    
    emit("\n" + "=" * 80)
    emit("FEATURE CORRELATION ANALYSIS (Project Dataset)")
    emit("=" * 80)

    # Formatting options to ensure the 6x6 matrices print cleanly without wrapping
    opts = {'max_line_width': 120, 'precision': 4, 'suppress_small': True}

    for c in classes:
        c_name = class_names.get(c, str(c))
        emit(f"\n--- CLASS {c}: {c_name} ---")
        
        Dc = DTR[:, LTR == c]
        
        # Compute the empirical mean (uc) and covariance matrix (sigmac)
        uc = numpy.mean(Dc, axis=1, keepdims=True)
        sigmac = compute_covariance_matrix(Dc, uc)
        
        # Compute Pearson correlation matrix
        corr = sigmac / ( mcol(sigmac.diagonal()**0.5) * vrow(sigmac.diagonal()**0.5) )

        emit("\nCovariance Matrix:")
        emit(numpy.array2string(sigmac, **opts))
        
        emit("\nCorrelation Matrix:")
        emit(numpy.array2string(corr, **opts))

        corr_results[c] = {
            "Covariance Matrix": sigmac,
            "Correlation Matrix": corr
        }
        
    emit("\n" + "=" * 80)

def evaluate_feature_ablation(DTR, LTR, DTE, LTE):
    """
    Evaluates the performance of the classifiers on specific subsets of features.
    Logs the error rates using the emitter.
    """
    emit = emit_base  # Use the provided emitter for logging
    ablation_results = {}
    
    emit("\n" + "=" * 80)
    emit("FEATURE ABLATION ANALYSIS (Project Dataset)")
    emit("=" * 80)
    emit(f"{'Feature Subset':<30} | {'Standard MVG':<14} | {'Naive Bayes':<14} | {'Tied MVG'}")
    emit("-" * 80)

    # Define the subsets: "Display Name": (start_row, end_row)
    subsets = {
        "Features 1-4 (Indices 0 to 3)": (0, 4),
        "Features 1-2 (Indices 0 to 1)": (0, 2),
        "Features 3-4 (Indices 2 to 3)": (2, 4),
        "Features 5-6 (Indices 4 to 5)": (4, 6) 
    }

    for name, (start, end) in subsets.items():
        # Slice the data dynamically
        DTR_sub = DTR[start:end, :]
        DTE_sub = DTE[start:end, :]
        
        metrics = {}
        
        # --- Standard MVG ---
        logSJoint_mvg, _, _ = compute_MVG_parameters(DTR_sub, LTR, DTE_sub)
        llr_mvg = logSJoint_mvg[1, :] - logSJoint_mvg[0, :]
        pred_mvg = (llr_mvg >= 0).astype(int)
        err_mvg = 1 - (numpy.sum(pred_mvg == LTE) / len(LTE))
        metrics["Standard MVG"] = round(err_mvg * 100, 1)

        # --- Naive Bayes ---
        logSJoint_nb, _, _ = compute_naive_bayes_parameters(DTR_sub, LTR, DTE_sub)
        llr_nb = logSJoint_nb[1, :] - logSJoint_nb[0, :]
        pred_nb = (llr_nb >= 0).astype(int)
        err_nb = 1 - (numpy.sum(pred_nb == LTE) / len(LTE))
        metrics["Naive Bayes"] = round(err_nb * 100, 1)

        # --- Tied MVG ---
        logSJoint_tied, _, _ = compute_tied_mvg_parameters(DTR_sub, LTR, DTE_sub)
        llr_tied = logSJoint_tied[1, :] - logSJoint_tied[0, :]
        pred_tied = (llr_tied >= 0).astype(int)
        err_tied = 1 - (numpy.sum(pred_tied == LTE) / len(LTE))
        metrics["Tied MVG"] = round(err_tied * 100, 1)
        
        emit(f"{name:<30} | {metrics['Standard MVG']:>13.1f}% | {metrics['Naive Bayes']:>13.1f}% | {metrics['Tied MVG']:>9.1f}%")
        ablation_results[name] = metrics

    emit("=" * 80)

def evaluate_pca(DTR, LTR, DTE, LTE):
    """
    Evaluates the performance of the classifiers after applying PCA for dimensionality reduction.
    Logs the error rates for each dimension 'm' using the emitter.
    """
    emit = emit_base  # Use the provided emitter for logging
    num_features = DTR.shape[0]

    emit("\n" + "=" * 80)
    emit("PCA PRE-PROCESSING ANALYSIS (Project Dataset)")
    emit("=" * 80)
    emit(f"{'PCA Dimension (m)':<20} | {'Standard MVG':<14} | {'Naive Bayes':<14} | {'Tied MVG'}")
    emit("-" * 80)

    # Loop through dimensions from 1 up to the total number of features (6)
    for m in range(1, num_features + 1):
        metrics = {}
        
        # 1. Compute PCA on the TRAINING set only
        DTR_pca, P = PCA(DTR, m)
        
        # 2. Project the EVALUATION set using the P matrix learned from training
        DTE_pca = numpy.transpose(P) @ DTE
        
        # --- Standard MVG ---
        logSJoint_mvg, _, _ = compute_MVG_parameters(DTR_pca, LTR, DTE_pca)
        llr_mvg = logSJoint_mvg[1, :] - logSJoint_mvg[0, :]
        pred_mvg = (llr_mvg >= 0).astype(int)
        metrics["Standard MVG"] = round((1 - (numpy.sum(pred_mvg == LTE) / len(LTE))) * 100, 1)
        
        # --- Naive Bayes ---
        logSJoint_nb, _, _ = compute_naive_bayes_parameters(DTR_pca, LTR, DTE_pca)
        llr_nb = logSJoint_nb[1, :] - logSJoint_nb[0, :]
        pred_nb = (llr_nb >= 0).astype(int)
        metrics["Naive Bayes"] = round((1 - (numpy.sum(pred_nb == LTE) / len(LTE))) * 100, 1)

        # --- Tied MVG ---
        logSJoint_tied, _, _ = compute_tied_mvg_parameters(DTR_pca, LTR, DTE_pca)
        llr_tied = logSJoint_tied[1, :] - logSJoint_tied[0, :]
        pred_tied = (llr_tied >= 0).astype(int)
        metrics["Tied MVG"] = round((1 - (numpy.sum(pred_tied == LTE) / len(LTE))) * 100, 1)
        
        emit(f"m = {m:<16} | {metrics['Standard MVG']:>13.1f}% | {metrics['Naive Bayes']:>13.1f}% | {metrics['Tied MVG']:>9.1f}%")

if __name__ == "__main__":
    # Create required folders
    results_dir.mkdir(parents=True, exist_ok=True)
    histograms_dir.mkdir(parents=True, exist_ok=True)
    metrics_dir.mkdir(parents=True, exist_ok=True)

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
    evaluate_base_models(DTR, LTR, DTE, LTE)
    analyze_correlations(DTR, LTR)
    evaluate_feature_ablation(DTR, LTR, DTE, LTE)
    pca_metrics = evaluate_pca(DTR, LTR, DTE, LTE)
    
    plot_histograms(DTR, LTR, output_dir=histograms_dir)