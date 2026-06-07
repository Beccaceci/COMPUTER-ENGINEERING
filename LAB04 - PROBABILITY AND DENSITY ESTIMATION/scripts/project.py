import numpy
from pathlib import Path
import matplotlib
matplotlib.use("Agg") # Prevent GUI popups during plot generation

from utils.data_loaders import load_dataset
from utils.math_utils import compute_covariance_matrix, vrow
from utils.io_utils import create_emitter
from utils.plot_utils import plot_feature_histogram


if __name__ == "__main__":
    # 1. Setup directories and emitter
    ROOT = Path(".")
    dataset_dir = ROOT / "data" / "project"
    output_dir = ROOT / "results" / "project"
    plots_dir = output_dir / "plots"
    plots_dir.mkdir(parents=True, exist_ok=True)
    
    report_path = output_dir / "project_lab04_mle_metrics.txt"
    emit = create_emitter(report_path)

    # 2. Load the PROJECT dataset
    X, y = load_dataset(dataset_dir / "trainData.txt")
    
    emit(f"Dataset Loaded: {X.shape[1]} samples, {X.shape[0]} features.")
    emit("=" * 65)
    
    # 3. Execute core logic
    class_names = {0: "Fake", 1: "Genuine"}
    num_features = X.shape[0]

    for cls_id, cls_name in class_names.items():
        emit(f"\n--- CLASS: {cls_name} (Label {cls_id}) ---")
        emit(f"{'Feature':<12} | {'ML Mean (mu)':<15} | {'ML Variance (C)':<15}")
        emit("-" * 50)
        
        # Select only the samples belonging to the current class
        X_class = X[:, y == cls_id]
        
        # Iterate through each feature
        for f_idx in range(num_features):
            feature_name = f"Feature_{f_idx + 1}"
            
            # Extract 1D feature and reshape to (1, N)
            x_feature = vrow(X_class[f_idx, :])
            
            # Compute MLE parameters for this specific 1D distribution
            mu_ML = numpy.mean(x_feature, axis=1, keepdims=True)
            C_ML = compute_covariance_matrix(x_feature)
            
            # Extract scalars for clean printing
            mu_val = mu_ML[0, 0]
            var_val = C_ML[0, 0]
            
            # Log the metrics
            emit(f"{feature_name:<12} | {mu_val:<15.4f} | {var_val:<15.4f}")
            
            # Plot and save the result 
            title = f"{cls_name} - {feature_name}"
            
            # Just pass the plots_dir, the plot_utils.py will auto-generate the filename!
            plot_feature_histogram(x_feature, mu_ML, C_ML, title, plots_dir)
            
    emit("\n" + "=" * 65)
    print(f"[+] Script execution complete. Metrics saved to: {report_path}")
    print(f"[+] Density plots saved to: {plots_dir}")