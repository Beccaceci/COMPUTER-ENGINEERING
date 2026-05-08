import matplotlib
import numpy
from pathlib import Path

from utils.data_loaders import load_dataset
from utils.math_utils import compute_covariance, compute_mean, compute_std, compute_variance
from utils.io_utils import write_matrix
from utils.plot_utils import plot_histograms, plot_scatter_pairs

matplotlib.use("Agg")

ROOT = Path(".")
IRIS_LABEL_NAMES = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
IRIS_FEATURE_NAMES = ["Sepal length", "Sepal width", "Petal length", "Petal width"]

def compute_statistics(D, L):
    stats_rows = []
    covariances = {}

    # Global
    global_means = compute_mean(D).ravel()
    global_variances = compute_variance(D).ravel()
    global_stds = compute_std(D).ravel()
    covariances["Global"] = compute_covariance(D)

    for idx, feature in enumerate(IRIS_FEATURE_NAMES):
        stats_rows.append(["All", "Global", feature, global_means[idx], global_variances[idx], global_stds[idx]])

    # Per-Class
    for label_id, label_name in IRIS_LABEL_NAMES.items():
        Dc = D[:, L == label_id] 
        means = compute_mean(Dc).ravel()
        variances = compute_variance(Dc).ravel()
        stds = compute_std(Dc).ravel()
        covariances[label_id] = compute_covariance(Dc)
        
        for idx, feature in enumerate(IRIS_FEATURE_NAMES):
            stats_rows.append([label_id, label_name, feature, means[idx], variances[idx], stds[idx]])

    return stats_rows, covariances

def save_iris_outputs(D, L):
    tables_dir = ROOT / "results" / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)

    # Math
    stats_rows, covariances = compute_statistics(D, L)
    
    # I/O
    write_matrix(tables_dir / "lab02_iris_statistics.csv", ["label", "class", "feature", "mean", "variance", "std"], stats_rows)
    for label_id, cov_matrix in covariances.items():
        name = "global" if label_id == "Global" else f"class_{label_id}"
        numpy.savetxt(tables_dir / f"lab02_iris_covariance_{name}.csv", cov_matrix, delimiter=",")

    # Plots
    plot_histograms(D, L, IRIS_FEATURE_NAMES, IRIS_LABEL_NAMES, ROOT / "results" / "iris" / "histograms", "Iris", bins=15)
    plot_scatter_pairs(D, L, IRIS_FEATURE_NAMES, IRIS_LABEL_NAMES, ROOT / "results" / "iris" / "scatter", "Iris")

if __name__ == "__main__":
    D, L = load_dataset(ROOT / "data" / "iris" / "iris.csv")
    print(f"Iris data shape: {D.shape}, labels: {L.shape}")
    save_iris_outputs(D, L)