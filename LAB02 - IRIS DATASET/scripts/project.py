import matplotlib
import numpy
from pathlib import Path

# Adjust import based on your specific naming in data_loaders.py
from utils.data_loaders import load_project_dataset 
from utils.math_utils import compute_covariance, compute_mean, compute_std, compute_variance
from utils.io_utils import write_matrix
from utils.plot_utils import plot_histograms, plot_scatter_pairs

matplotlib.use("Agg")

# Constants derived from the lab instructions
ROOT = Path(".")
PROJECT_LABEL_NAMES = {0: "Fake", 1: "Genuine"}
PROJECT_FEATURE_NAMES = [f"Feature_{i+1}" for i in range(6)]

def compute_statistics(D, L):
    """
    Computes mean, variance, standard deviation, and covariance for each class.
    Returns the formatted rows for the stats table and a dictionary of covariance matrices.
    """
    stats_rows = []
    covariances = {}

    for label_id, label_name in PROJECT_LABEL_NAMES.items():
        # Filter data for the specific class using a boolean mask
        Dc = D[:, L == label_id] 
        
        # Compute basic statistics
        means = compute_mean(Dc).ravel()
        variances = compute_variance(Dc).ravel()
        stds = compute_std(Dc).ravel()
        
        # Store basic statistics row by row
        for idx, feature in enumerate(PROJECT_FEATURE_NAMES):
            stats_rows.append([label_id, label_name, feature, means[idx], variances[idx], stds[idx]])
            
        # Compute and store the covariance matrix for the current class
        covariances[label_id] = compute_covariance(Dc)

    return stats_rows, covariances

def compute_overlaps(D, L):
    """
    Calculates the overlapping range for each feature between the two classes.
    """
    overlap_rows = []
    
    for idx, feature in enumerate(PROJECT_FEATURE_NAMES):
        # Isolate the current feature's data for both classes
        values0 = D[idx, L == 0]
        values1 = D[idx, L == 1]
        
        # Calculate the intersection (overlap) boundaries
        lo = max(values0.min(), values1.min())
        hi = min(values0.max(), values1.max())
        
        # If hi < lo, max(0.0, hi - lo) ensures we report 0 overlap instead of a negative number
        overlap_rows.append([feature, lo, hi, max(0.0, hi - lo)])
        
    return overlap_rows

def save_project_outputs(D, L):
    """
    Main orchestrator function that ties together computation, saving, and plotting.
    """
    tables_dir = ROOT / "results" / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)

    # Compute mathematical properties
    stats_rows, covariances = compute_statistics(D, L)
    overlap_rows = compute_overlaps(D, L)
    
    # Execute side-effects (saving files and plotting)

    # Save basic statistics
    write_matrix(
        tables_dir / "lab02_project_statistics.csv", 
        ["label", "class", "feature", "mean", "variance", "std"], 
        stats_rows
    )
    
    # Save overlap ranges
    write_matrix(
        tables_dir / "lab02_project_feature_overlap_ranges.csv", 
        ["feature", "overlap_min", "overlap_max", "overlap_width"], 
        overlap_rows
    )

    # Save covariance matrices
    for label_id, cov_matrix in covariances.items():
        numpy.savetxt(tables_dir / f"lab02_project_covariance_class_{label_id}.csv", cov_matrix, delimiter=",")

    # 1. Plot normalized density histograms for each individual feature
    # density=True normalizes the area under the histogram to 1
    plot_histograms(
        D, L, PROJECT_FEATURE_NAMES, PROJECT_LABEL_NAMES, 
        ROOT / "results" / "project" / "histograms", "Project", bins=40
    )
    
    # 2. Plot scatter plots for every unique pair of features
    plot_scatter_pairs(
        D, L, PROJECT_FEATURE_NAMES, PROJECT_LABEL_NAMES, 
        ROOT / "results" / "project" / "scatter", "Project"
    )

if __name__ == "__main__":
    # Ensure load_project_dataset is correctly imported from utils.data_loaders
    D, L = load_project_dataset(ROOT / "data" / "project" / "trainData.txt")
    print(f"Project data shape: {D.shape}, labels: {L.shape}")
    save_project_outputs(D, L)