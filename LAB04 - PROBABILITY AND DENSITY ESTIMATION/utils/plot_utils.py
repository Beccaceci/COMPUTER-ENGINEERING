import numpy
import matplotlib.pyplot as plt
from models.MVG import log_MVG
from utils.math_utils import vrow

def plot_feature_histogram (x_feature, mu, C, title, filepath, bins=20, hist_color='blue'):
    """
    Plots the normalized histogram of a 1D feature overlaid with its estimated Gaussian PDF.
    Works dynamically for any dataset based on the passed arguments.
    """
    plt.figure()
    plt.hist(x_feature.ravel(), bins=bins, density=True, alpha=0.4, color=hist_color, label='Samples')
    
    x_min, x_max = x_feature.min() - 1, x_feature.max() + 1
    x_plot = numpy.linspace(x_min, x_max, 1000)
    
    # Compute Gaussian PDF (Calculate in log-domain, then exponentiate for plotting)
    y_pdf = numpy.exp(log_MVG(vrow(x_plot), mu, C))
    plt.plot(x_plot, y_pdf, 'r', linewidth=2, label='Gaussian Fit')
    
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.legend()

    filename = title.replace(" - ", "_").replace(" ", "_").lower() + ".png"
    plt.savefig(output_dir / filename)
    plt.close()

def plot_1d_density(X_c_list, X_plot_list, densities_list, class_names, feature_name, filepath):
    """
    Plots the normalized histograms and continuous Gaussian densities.
    
    Args:
        X_c_list: List of 1D arrays containing raw data for each class.
        X_plot_list: List of 1D arrays containing the continuous X-axis points.
        densities_list: List of 1D arrays containing the computed densities.
        class_names: List of string names for the classes.
        feature_name: String name of the feature being plotted.
        filepath: Path object or string indicating where to save the plot.
    """
    plt.figure(figsize=(8, 6))
    
    for X_c, X_plot, densities, class_name in zip(X_c_list, X_plot_list, densities_list, class_names):
        # Plot normalized histogram
        plt.hist(X_c, bins=10, density=True, alpha=0.4, label=f'{class_name} Hist')
        
        # Plot the continuous Gaussian curve over it
        plt.plot(X_plot, densities, linewidth=2, label=f'{class_name} Gaussian')
        
    plt.title(f'Density Estimation: {feature_name}')
    plt.legend()
    plt.tight_layout()
    
    plt.savefig(filepath)
    plt.close()