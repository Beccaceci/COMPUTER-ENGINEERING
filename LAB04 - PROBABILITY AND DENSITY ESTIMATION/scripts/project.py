import numpy
from pathlib import Path

from utils.data_loaders import load_dataset
from utils.math_utils import compute_covariance_matrix, vrow
from utils.plot_utils import plot_feature_histogram


def generate_1d_gaussian_plots(X, y, output_dir):
    """
    Core mathematical logic: Iterates over classes and features, computes MLE parameters and triggers the plotting function.
    """
    class_names = {0: "Fake", 1: "Genuine"}
    num_features = X.shape[0]
    feature_names = [f"Feature {i+1}" for i in range(num_features)]

    for cls_id, cls_name in class_names.items():
        # Select only the samples belonging to the current class
        X_class = X[:, y == cls_id]
        
        # Iterate through each feature
        for f_idx in range(num_features):
            # Extract 1D feature and reshape to (1, N)
            x_feature = vrow(X_class[f_idx, :])
            
            # Compute MLE parameters for this specific 1D distribution
            mu_ML = numpy.mean(x_feature, axis=1, keepdims=True)
            C_ML = compute_covariance_matrix(x_feature)
            
            # Plot and save the result 
            title = f"{cls_name} - {feature_names[f_idx]}"
            plot_feature_histogram(x_feature, mu_ML, C_ML, title, output_dir)    


if __name__ == "__main__":
    ROOT = Path(".")
    
    # 1. Setup output directory
    output_dir = ROOT / "results" / "project"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 2. Load the PROJECT dataset
    X, y = load_dataset(ROOT / "data" / "project" / "trainData.txt")
    
    # 3. Execute core logic
    print("Generating 1D Gaussian fits...")
    generate_1d_gaussian_plots(X, y, output_dir)
    print(f"Successfully generated 12 Gaussian plots in {output_dir}")