import matplotlib
import matplotlib.pyplot as plt
import numpy
from pathlib import Path

# Make sure these match your imports exactly
from utils.data_loaders import load_dataset, split_dataset
from models.pca import compute_pca
from models.lda import compute_lda
from utils.plot_utils import plot_histograms, plot_scatter_pairs, plot_1d_histograms
from utils.io_utils import write_matrix

matplotlib.use("Agg")

ROOT = Path(".")
PROJECT_LABEL_NAMES = {0: "Fake", 1: "Genuine"}

def run_project_analysis():
    D, L = load_dataset(ROOT / "data" / "project" / "trainData.txt")
    
    # 1. Setup Folder Structure
    output_dir = ROOT / "results" / "project"
    lda_dir = output_dir / "LDA"
    pca_dir = output_dir / "PCA"
    
    pca_hist_dir = pca_dir / "histograms"
    pca_scatter_dir = pca_dir / "scatter"
    lda_hist_dir = lda_dir / "histograms"
    
    # Create the directories
    for d in [pca_hist_dir, pca_scatter_dir, lda_hist_dir]:
        d.mkdir(parents=True, exist_ok=True)
    
    # ==========================================
    # PART A: Exploratory Analysis (Whole Dataset)
    # ==========================================
    
    # --- PCA (m=6) ---
    _, P_pca = compute_pca(D, m=6)
    DP_pca = P_pca.T @ D
    pca_feature_names = [f"PCA Direction {i+1}" for i in range(6)]
    plot_histograms(DP_pca, L, pca_feature_names, PROJECT_LABEL_NAMES, pca_hist_dir, "Project PCA", bins=40)
    plot_scatter_pairs(DP_pca, L, pca_feature_names, PROJECT_LABEL_NAMES, pca_scatter_dir, "Project PCA")
    
    # --- LDA (m=1) ---
    _, W_lda = compute_lda(D, L, m=1)
    DP_lda = W_lda.T @ D
    plot_1d_histograms(DP_lda, L, PROJECT_LABEL_NAMES, lda_hist_dir, "Project Exploratory LDA")


    # ==========================================
    # PART B: Classification Analysis 
    # ==========================================
    
    # Split the dataset
    (DTR, LTR), (DVAL, LVAL) = split_dataset(D, L, train_ratio=2.0/3.0)

    # --- 1. Standard LDA Classification ---
    _, W_lda_tr = compute_lda(DTR, LTR, m=1)
    DTR_lda = W_lda_tr.T @ DTR
    DVAL_lda = W_lda_tr.T @ DVAL

    # Orient the projection so the mean of Genuine (1) > Fake (0)
    if DTR_lda[0, LTR == 1].mean() < DTR_lda[0, LTR == 0].mean():
        DTR_lda = -DTR_lda
        DVAL_lda = -DVAL_lda

    mean_0 = DTR_lda[0, LTR == 0].mean()
    mean_1 = DTR_lda[0, LTR == 1].mean()
    threshold = (mean_0 + mean_1) / 2.0

    # Predictions using the default threshold
    PVAL = numpy.zeros(LVAL.shape, dtype=numpy.int32)
    PVAL[DVAL_lda[0] >= threshold] = 1
    error_rate = numpy.sum(PVAL != LVAL) / LVAL.size

    # Sweep thresholds to find if accuracy can be improved
    thresholds = numpy.linspace(DTR_lda.min(), DTR_lda.max(), 1000)
    error_rates = []
    
    for t in thresholds:
        p = numpy.zeros(LVAL.shape, dtype=numpy.int32)
        p[DVAL_lda[0] >= t] = 1
        error_rates.append(numpy.sum(p != LVAL) / LVAL.size)

    best_idx = numpy.argmin(error_rates)
    best_threshold = thresholds[best_idx]
    best_error_rate = error_rates[best_idx]

    # Plot the threshold sweep
    plt.figure(figsize=(7, 5))
    plt.plot(thresholds, [e * 100 for e in error_rates], label="Validation Error")
    plt.axvline(threshold, color='red', linestyle='--', label=f'Mean Threshold ({error_rate*100:.2f}%)')
    plt.axvline(best_threshold, color='green', linestyle='--', label=f'Best Threshold ({best_error_rate*100:.2f}%)')
    plt.xlabel("Threshold")
    plt.ylabel("Error Rate (%)")
    plt.title("LDA Threshold Sweep")
    plt.legend()
    plt.tight_layout()
    plt.savefig(lda_dir / "lda_threshold_sweep.png", dpi=160)
    plt.close()

    # Save the LDA metrics
    write_matrix(lda_dir / "lda_classification_metrics.csv", ["Metric", "Value"], [
        ["Validation Samples", LVAL.size],
        ["Default Threshold", threshold],
        ["Default Error Rate (%)", error_rate * 100],
        ["Best Sweep Threshold", best_threshold],
        ["Best Error Rate (%)", best_error_rate * 100]
    ])

    # --- 2. PCA + LDA Classification ---
    pca_lda_results = []
    
    for m in range(1, 7):
        # PCA on Training Set
        _, P_pca_tr = compute_pca(DTR, m=m)
        DTR_pca = P_pca_tr.T @ DTR
        DVAL_pca = P_pca_tr.T @ DVAL

        # LDA on PCA-Projected Training Set
        _, W_lda_pca = compute_lda(DTR_pca, LTR, m=1)
        DTR_lda_pca = W_lda_pca.T @ DTR_pca
        DVAL_lda_pca = W_lda_pca.T @ DVAL_pca

        # Orient
        if DTR_lda_pca[0, LTR == 1].mean() < DTR_lda_pca[0, LTR == 0].mean():
            DTR_lda_pca = -DTR_lda_pca
            DVAL_lda_pca = -DVAL_lda_pca

        # Threshold and Evaluate
        t_pca = (DTR_lda_pca[0, LTR == 0].mean() + DTR_lda_pca[0, LTR == 1].mean()) / 2.0
        p_pca = numpy.zeros(LVAL.shape, dtype=numpy.int32)
        p_pca[DVAL_lda_pca[0] >= t_pca] = 1
        err_pca = numpy.sum(p_pca != LVAL) / LVAL.size
        
        pca_lda_results.append([m, err_pca * 100])

    # Save PCA+LDA Metrics
    write_matrix(pca_dir / "pca_lda_classification_metrics.csv", ["PCA Dimensions (m)", "Error Rate (%)"], pca_lda_results)


if __name__ == "__main__":
    run_project_analysis()
    print("Lab 03 Project classification outputs successfully generated in results/project/LDA/ and results/project/PCA/.")