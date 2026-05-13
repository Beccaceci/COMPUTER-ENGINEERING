import matplotlib
import numpy
from pathlib import Path

# Ensure these match your specific util imports
from utils.data_loaders import load_dataset
from models.pca import compute_pca
from models.lda import compute_lda, compute_within_class_covariance, compute_between_class_covariance 
from utils.math_utils import compute_covariance_matrix, mcol
from utils.plot_utils import plot_scatter_pairs

matplotlib.use("Agg")

ROOT = Path(".")
IRIS_LABEL_NAMES = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}

def create_emitter(file_path):
    """
    Creates an emit function that prints to standard output AND appends to a text file.
    It automatically clears the target file upon initialization.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as f:
        f.write("LAB 03: EXPECTED MATRICES (IRIS DATASET)\n")
        f.write("=" * 65 + "\n")
        
    def emit(text=""):
        print(text)
        with open(file_path, "a") as f:
            f.write(str(text) + "\n")
    return emit

def print_matrix(name, matrix, emit):
    """Helper function to cleanly format and print numpy matrices."""
    emit(f"\n--- {name} ---")
    if matrix.ndim == 1 or matrix.shape[1] == 1:
        # Column vector or 1D array
        for val in matrix.ravel():
            emit(f"{val:>12.6f}")
    else:
        # 2D Matrix
        for row in matrix:
            row_vals = " ".join([f"{val:>12.6f}" for val in row])
            emit(row_vals)

if __name__ == "__main__":
    # Load the dataset
    D, L = load_dataset(ROOT / "data" / "iris" / "iris_dataset.csv")
    
    # 1. Setup Folder Structure
    output_dir = ROOT / "results" / "iris"
    pca_dir = output_dir / "PCA"
    lda_dir = output_dir / "LDA"
    
    pca_dir.mkdir(parents=True, exist_ok=True)
    lda_dir.mkdir(parents=True, exist_ok=True)
    
    # 2. Setup Emitter
    report_path = output_dir / "iris_lab03_matrices.txt"
    emit = create_emitter(report_path)
    
    emit(f"Dataset Shape: {D.shape[1]} samples, {D.shape[0]} features.")
    
    # ==========================================
    # PART 0: Compute and Print Expected Matrices
    # ==========================================
    emit("\n" + "=" * 65)
    emit("MATRICES FOR COMPARISON WITH LAB INSTRUCTIONS")
    emit("=" * 65)
    
    # Compute Dataset Mean (mu)
    mu = mcol(numpy.mean(D, axis=1))
    print_matrix("Dataset Mean (mu)", mu, emit)
    
    # Compute Covariance Matrix (C)
    C = compute_covariance_matrix(D)
    print_matrix("Covariance Matrix (C)", C, emit)
    
    # Compute Between-class Covariance Matrix (SB)
    SB = compute_between_class_covariance(D, L)
    print_matrix("Between-class Covariance Matrix (SB)", SB, emit)
    
    # Compute Within-class Covariance Matrix (SW)
    SW = compute_within_class_covariance(D, L)
    print_matrix("Within-class Covariance Matrix (SW)", SW, emit)
    
    emit("\n" + "=" * 65)
    emit("PROJECTIONS (PCA & LDA)")
    emit("=" * 65)

    # Since we are projecting to 2D for both PCA and LDA
    proj_feature_names = ["Direction 1", "Direction 2"]

    # ==========================================
    # PART 1: PCA Projection (m=2)
    # ==========================================
    # Unpack the tuple: discard eigenvalues (_), keep projection matrix (P_pca)
    _, P_pca = compute_pca(D, m=2)
    DP_pca = P_pca.T @ D
    
    # Generate scatter plot for the 2 PCA directions
    plot_scatter_pairs(DP_pca, L, proj_feature_names, IRIS_LABEL_NAMES, pca_dir, "Iris PCA")
    emit("[+] PCA projections computed and plotted successfully.")
    

    # ==========================================
    # PART 2: LDA Projection (m=2)
    # ==========================================
    # Max dimensions for LDA is C-1 (3 classes - 1 = 2 dimensions)
    _, W_lda = compute_lda(D, L, m=2)
    DP_lda = W_lda.T @ D
    
    # Generate scatter plot for the 2 LDA directions
    plot_scatter_pairs(DP_lda, L, proj_feature_names, IRIS_LABEL_NAMES, lda_dir, "Iris LDA")
    emit("[+] LDA projections computed and plotted successfully.")

    emit(f"\n[+] All outputs successfully generated and saved to: {report_path}")