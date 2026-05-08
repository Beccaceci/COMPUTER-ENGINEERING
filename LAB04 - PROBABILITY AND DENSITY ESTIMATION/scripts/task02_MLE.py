import os
import numpy
import matplotlib.pyplot as plt
from utils.math_utils import compute_covariance_matrix, vrow
from models.MLE import loglikelihood
from models.MVG import log_MVG

def plot_MLE (X1D, mu_ML, C_ML):
    """
    Plots the histogram of 1D samples and the estimated Gaussian density.
    """
    title = "ML Estimate Fit"
    plt.figure()

    # normalized histogram
    plt.hist(X1D.ravel(), bins=50, density=True, alpha=0.6, label="Samples")
    
    # solution curve
    XPlot = numpy.linspace(-8, 12, 1000)

    # compute density for the range
    y_pdf = numpy.exp(log_MVG(vrow(XPlot), mu_ML, C_ML))
    plt.plot(XPlot.ravel(), y_pdf, "r", label="ML Gaussian Fit")
    plt.title(title)
    plt.legend()
    
     # define the output folder for saving plots
    output_folder = "plots/MLE" 
    
    # create the directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    filename = title.replace(" - ", "_").replace(" ", "_") + ".png"
    save_path = os.path.join(output_folder, filename)

    plt.savefig(save_path)
    plt.close()


if __name__ == "__main__":
    """
    This function computes the log-likelihood of a Gaussian distribution for both a 1D and a multi-dimensional dataset, compares the results with provided solutions and visualizes the 1D case.
    """

    # --- PART 1: 1D DATASET ---
    X1D_raw = numpy.load("data/X1D.npy")
    X1D = vrow(X1D_raw)
    
    # compute ML Parameters
    mu_ML_1D = numpy.mean(X1D, axis=1, keepdims=True)
    C_ML_1D = compute_covariance_matrix(X1D)
    
    # compute log-likelihood
    ll_1D = loglikelihood(X1D, mu_ML_1D, C_ML_1D)
    print(f"1D Log-Likelihood (Expected ~-23227.08): {ll_1D}")
    
    # visualize fit
    plot_MLE(X1D, mu_ML_1D, C_ML_1D)

    # --- PART 2: MULTI-DIMENSIONAL DATASET ---
    XND = numpy.load("data/XND.npy")
    
    # compute ML parameters
    mu_ML_ND = numpy.mean(XND, axis=1, keepdims=True)
    C_ML_ND = compute_covariance_matrix(XND)
    
    # compute log-likelihood
    ll_ND = loglikelihood(XND, mu_ML_ND, C_ML_ND)
    print(f"ND Log-Likelihood (Expected ~-270.70): {ll_ND}")