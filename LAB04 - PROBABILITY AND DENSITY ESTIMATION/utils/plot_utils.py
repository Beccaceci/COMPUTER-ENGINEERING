import numpy
import matplotlib.pyplot as plt
from models.MVG import log_MVG
from utils.math_utils import vrow

def plot_feature_histogram (x_feature, mu, C, title, output_dir, bins=20, hist_color='blue'):
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