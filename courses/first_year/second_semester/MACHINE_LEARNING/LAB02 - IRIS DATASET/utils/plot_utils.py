import matplotlib.pyplot as plt

def plot_histograms(D, L, feature_names, label_names, output_dir, title_prefix, bins=15):
    """Generates and saves normalized density histograms for each feature."""
    output_dir.mkdir(parents=True, exist_ok=True)

    for idx, feature in enumerate(feature_names):
        plt.figure(figsize=(7, 5))
        for label_id, label_name in label_names.items():
            plt.hist(D[idx, L == label_id], bins=bins, density=True, alpha=0.45, label=label_name)
        
        plt.xlabel(feature)
        plt.ylabel("Density")
        plt.title(f"{title_prefix} {feature} distribution")
        plt.legend()
        plt.tight_layout()
        plt.savefig(output_dir / f"feature_{idx + 1}_histogram.png", dpi=160)
        plt.close()

def plot_scatter_pairs(D, L, feature_names, label_names, output_dir, title_prefix):
    """Generates and saves scatter plots for every unique pair of features."""
    output_dir.mkdir(parents=True, exist_ok=True)
    num_features = D.shape[0]

    for i in range(num_features):
        for j in range(i + 1, num_features):
            plt.figure(figsize=(7, 5))
            for label_id, label_name in label_names.items():
                plt.scatter(D[i, L == label_id], D[j, L == label_id], s=10, alpha=0.5, label=label_name)
            
            plt.xlabel(feature_names[i])
            plt.ylabel(feature_names[j])
            plt.title(f"{title_prefix} {feature_names[i]} vs {feature_names[j]}")
            plt.legend(markerscale=2)
            plt.tight_layout()
            plt.savefig(output_dir / f"features_{i + 1}_{j + 1}_scatter.png", dpi=160)
            plt.close()