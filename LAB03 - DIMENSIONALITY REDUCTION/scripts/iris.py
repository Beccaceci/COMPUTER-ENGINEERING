import matplotlib
import numpy
from pathlib import Path

# Ensure these match your specific util imports
from utils.data_loaders import load_dataset 
from utils.math_utils import compute_pca, compute_lda
from utils.plot_utils import plot_scatter_pairs

matplotlib.use("Agg")

ROOT = Path(".")
IRIS_LABEL_NAMES = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}

def run_iris_dim_reduction():
    # Load the dataset
    D, L = load_dataset(ROOT / "data" /"iris.csv")
    
    # 1. Setup Folder Structure
    output_dir = ROOT / "results" / "iris"
    pca_dir = output_dir / "PCA"
    lda_dir = output_dir / "LDA"
    
    pca_dir.mkdir(parents=True, exist_ok=True)
    lda_dir.mkdir(parents=True, exist_ok=True)
    
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
    

    # ==========================================
    # PART 2: LDA Projection (m=2)
    # ==========================================
    # Max dimensions for LDA is C-1 (3 classes - 1 = 2 dimensions)
    _, W_lda = compute_lda(D, L, m=2)
    DP_lda = W_lda.T @ D
    
    # Generate scatter plot for the 2 LDA directions
    plot_scatter_pairs(DP_lda, L, proj_feature_names, IRIS_LABEL_NAMES, lda_dir, "Iris LDA")


if __name__ == "__main__":
    run_iris_dim_reduction()
    print("Lab 03 Iris dimensional reduction outputs successfully generated in results/iris/PCA/ and results/iris/LDA/.")