import os
import numpy
import matplotlib.pyplot as plt
from utils.math_utils import compute_covariance_matrix, vrow
from models.MVG import log_MVG

def plot_gaussian_density (x_plot, computed_pdf, solution_pdf):
    """
    Plots both the computed and solution densities for visual verification.
    """
    title = "Gaussian Density Comparison (1D Case)"
    plt.figure(figsize=(8, 6))
    
    # exponentiate log-densities to get actual values 
    plt.plot(x_plot.ravel(), numpy.exp(computed_pdf), label='Computed Density', linewidth=2)
    plt.plot(x_plot.ravel(), numpy.exp(solution_pdf), label='Solution Density', linestyle='--', linewidth=2)
    
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.grid(True, alpha=0.3)

    # define the output folder for saving plots
    output_folder = "plots/MVG" 
    
    # create the directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    filename = title.replace(" - ", "_").replace(" ", "_") + ".png"
    save_path = os.path.join(output_folder, filename)
    
    plt.savefig(save_path)
    plt.close()

def compare_results (computed_pdf, solution_pdf, label):
    """
    Computes and prints the maximum absolute difference between implementation and solution.
    """
    max_diff = numpy.abs(computed_pdf - solution_pdf).max()
    print(f"[{label}] Max Absolute Difference: {max_diff}")


if __name__ == "__main__":
    """
    This function computes the log-density of a Gaussian distribution for both a 1D and a multi-dimensional dataset, compares the results with provided solutions and visualizes the 1D case.
    """

    # --- PART 1: 1D DATASET ---
    # load data and compute the parameters
    X_1D = numpy.linspace(-8, 12, 1000)
    mu_1D = numpy.ones((1, 1)) * 1.0
    C_1D = numpy.ones((1, 1)) * 2.0
    
    # load solution result
    sol_1D = numpy.load("data/llGAU.npy")
    
    # compute MVG density
    MVGdensity_1D = log_MVG(vrow(X_1D), mu_1D, C_1D) # 

    # compare and plot
    compare_results(MVGdensity_1D, sol_1D, "1D Case")
    plot_gaussian_density(X_1D, MVGdensity_1D, sol_1D)

    # --- PART 2: MULTI-DIMENSIONAL DATASET ---
    # load the dataset 
    X_ND = numpy.load("data/XND.npy")
    
    # compute MVG parameters
    mu_ND = numpy.mean(X_ND, axis=1, keepdims=True)
    C_ND = compute_covariance_matrix(X_ND)
    
    # load solution result
    sol_ND = numpy.load("data/llND.npy")
    
    # compute MVG density with the calculated parameters
    MVGdensity_ND = log_MVG(X_ND, mu_ND, C_ND)

    # compare the results for the multi-dimensional case
    compare_results(MVGdensity_ND, sol_ND, "Multi-Dimensional Case")