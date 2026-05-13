import matplotlib
import numpy
from pathlib import Path

from utils.data_loaders import load_dataset 
from utils.math_utils import compute_covariance, compute_mean, compute_std, compute_variance
from utils.plot_utils import plot_histograms, plot_scatter_pairs

matplotlib.use("Agg")

# Constants derived from the lab instructions
ROOT = Path(".")
PROJECT_LABEL_NAMES = {0: "Fake", 1: "Genuine"}
PROJECT_FEATURE_NAMES = [f"Feature_{i+1}" for i in range(6)]

def create_emitter(file_path):
    """
    Creates an emit function that prints to standard output AND appends to a text file.
    It automatically clears the target file upon initialization.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as f:
        f.write("PROJECT DATASET: STATISTICAL ANALYSIS REPORT\n")
        f.write("=" * 75 + "\n")
        
    def emit(text=""):
        print(text)
        with open(file_path, "a") as f:
            f.write(str(text) + "\n")
    return emit

def analyze_and_report(D, L, emit):
    """
    Computes all mathematical statistics (means, variances, overlaps, covariances)
    and formats them into a single comprehensive report using the emit function.
    """
    
    # ==========================================
    # 1. CLASS-CONDITIONAL STATISTICS
    # ==========================================
    emit("\n" + "=" * 75)
    emit("1. CLASS-CONDITIONAL STATISTICS")
    emit("   Metrics explained:")
    emit("   - Mean: The central tendency or average value of the feature.")
    emit("   - Variance: The spread of the feature values around the mean.")
    emit("   - Std Dev: Standard deviation, expressing spread in the original units.")
    emit("=" * 75)
    emit(f"{'Class':<10} | {'Feature':<12} | {'Mean':<10} | {'Variance':<10} | {'Std Dev':<10}")
    emit("-" * 75)
    
    covariances = {}
    
    for label_id, label_name in PROJECT_LABEL_NAMES.items():
        # Filter data for the specific class using a boolean mask
        Dc = D[:, L == label_id] 
        
        # Compute basic statistics (flattened to 1D arrays for easy indexing)
        means = compute_mean(Dc).ravel()
        variances = compute_variance(Dc).ravel()
        stds = compute_std(Dc).ravel()
        
        # Print row-by-row statistics
        for idx, feature in enumerate(PROJECT_FEATURE_NAMES):
            emit(f"{label_name:<10} | {feature:<12} | {means[idx]:<10.4f} | {variances[idx]:<10.4f} | {stds[idx]:<10.4f}")
            
        # Compute and store the covariance matrix for later use
        covariances[label_id] = compute_covariance(Dc)

    # ==========================================
    # 2. FEATURE OVERLAP RANGES
    # ==========================================
    emit("\n" + "=" * 75)
    emit("2. FEATURE OVERLAP RANGES")
    emit("   Metrics explained:")
    emit("   - Overlap Width: The size of the intersecting interval between the Fake")
    emit("     and Genuine classes for a given feature. A smaller overlap generally")
    emit("     indicates that the feature has higher discriminative power.")
    emit("=" * 75)
    emit(f"{'Feature':<12} | {'Min (Overlap)':<15} | {'Max (Overlap)':<15} | {'Overlap Width':<15}")
    emit("-" * 75)
    
    for idx, feature in enumerate(PROJECT_FEATURE_NAMES):
        # Isolate the current feature's data for both classes
        values0 = D[idx, L == 0]
        values1 = D[idx, L == 1]
        
        # Calculate the intersection boundaries
        lo = max(values0.min(), values1.min())
        hi = min(values0.max(), values1.max())
        
        # Ensure we report 0 if the ranges are completely disjoint (hi < lo)
        overlap_width = max(0.0, hi - lo)
        emit(f"{feature:<12} | {lo:<15.4f} | {hi:<15.4f} | {overlap_width:<15.4f}")

    # ==========================================
    # 3. COVARIANCE MATRICES
    # ==========================================
    emit("\n" + "=" * 75)
    emit("3. COVARIANCE MATRICES")
    emit("   Metrics explained:")
    emit("   - Covariance Matrix: Measures the joint variability of feature pairs.")
    emit("   - Diagonal fields: Represent the individual feature variances.")
    emit("   - Off-diagonal fields: Represent linear dependence between two features.")
    emit("=" * 75)
    
    # Create the top header row displaying feature names
    col_headers = " ".join([f"{f:>10}" for f in PROJECT_FEATURE_NAMES])
    
    for label_id, label_name in PROJECT_LABEL_NAMES.items():
        emit(f"\n--- Covariance Matrix for Class: {label_name} (Label: {label_id}) ---")
        emit(f"{'':<12} {col_headers}")
        emit("-" * 75)
        
        cov_matrix = covariances[label_id]
        
        # Print each row with its corresponding feature name on the left
        for i, row in enumerate(cov_matrix):
            row_vals = " ".join([f"{val:>10.4f}" for val in row])
            emit(f"{PROJECT_FEATURE_NAMES[i]:<12} {row_vals}")
    

if __name__ == "__main__":
    # Load the dataset
    D, L = load_dataset(ROOT / "data" / "project" / "trainData.txt")

    # Define output paths
    output_dir = ROOT / "results" / "project"
    report_path = output_dir / "project_statistics_summary.txt"
    
    # Initialize our logger/emitter
    emit = create_emitter(report_path)
    emit(f"Dataset Shape: {D.shape[1]} samples, {D.shape[0]} features.")

    # 1. Run mathematical analysis and write the single unified report
    analyze_and_report(D, L, emit)
    
    print(f"\n[+] Statistical report successfully saved to: {report_path}")

    # 2. Plot normalized density histograms (density=True normalizes area to 1)
    print("[*] Generating histograms...")
    plot_histograms(
        D, L, PROJECT_FEATURE_NAMES, PROJECT_LABEL_NAMES, 
        output_dir / "histograms", "Project", bins=40
    )
    
    # 3. Plot scatter plots for every unique pair of features
    print("[*] Generating scatter plots...")
    plot_scatter_pairs(
        D, L, PROJECT_FEATURE_NAMES, PROJECT_LABEL_NAMES, 
        output_dir / "scatter", "Project"
    )
    print("[+] All plots successfully generated.")