import numpy as np
from pathlib import Path

from utils.data_loaders import load_dataset
from utils.math_utils import vrow, log_GAU_ND, mcol
from utils.plot_utils import plot_1d_density

if __name__ == "__main__":
    # Setup paths
    ROOT = Path(".")
    
    # Dataset path
    dataset_dir = ROOT / "data" / "iris"
    output_dir = ROOT / "results" / "iris"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load dataset
    D, L = load_dataset(dataset_dir / "iris_dataset.csv")
    class_names_dict = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
    feature_names = {0: 'Sepal length', 1: 'Sepal width', 2: 'Petal length', 3: 'Petal width'}
    
    # Loop over each of the 4 features
    for idx_feat in range(4):
        # Data collectors for the plotting function
        X_c_list = []
        X_plot_list = []
        densities_list = []
        class_names = []
        
        # Loop over each of the 3 classes
        for idx_class in range(3):
            # Extract 1D array of data for this specific feature and class
            X_c = D[idx_feat, L == idx_class]
            
            # 1. Compute ML estimates (Mean and Variance)
            mu_ML = np.mean(X_c)
            C_ML = np.var(X_c) # 1D Variance
            
            # 2. Reshape into matrices to feed into log_GAU_ND (1x1 matrices)
            mu_ML_2d = mcol(np.array([mu_ML]))
            C_ML_2d = np.array([[C_ML]])
            
            # 3. Create a continuous X-axis for the plot curve
            X_plot = np.linspace(np.min(X_c) - 1, np.max(X_c) + 1, 1000)
            X_plot_2d = vrow(X_plot) # shape (1, 1000)
            
            # 4. Compute Log-Density and Exponentiate to get normal Density
            log_densities = log_GAU_ND(X_plot_2d, mu_ML_2d, C_ML_2d)
            densities = np.exp(log_densities)
            
            # Append computed data to lists
            X_c_list.append(X_c)
            X_plot_list.append(X_plot)
            densities_list.append(densities)
            class_names.append(class_names_dict[idx_class])
            
        # 5. Pass all computed math to the plotting function
        filepath = output_dir / f'{feature_names[idx_feat].replace(" ", "_")}_gaussian_density.png'
        plot_1d_density(
            X_c_list=X_c_list,
            X_plot_list=X_plot_list,
            densities_list=densities_list,
            class_names=class_names,
            feature_name=feature_names[idx_feat],
            filepath=filepath
        )

        print(f"Saved plot -> {filepath}")