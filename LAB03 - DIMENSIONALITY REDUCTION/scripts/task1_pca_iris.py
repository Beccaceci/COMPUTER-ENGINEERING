import numpy
import sys
import matplotlib.pyplot as plt
from utils.data_loaders import load
from utils.math_utils import compute_covariance_matrix
from models.pca import PCA

def plot_pca(projected_data, L):
    """
    Creates a 2D scatter plot of the data projected onto the first two principal components.
    
    Parameters:
    -----------
    projected_data : numpy.ndarray
        The projected data matrix of shape (2, N).
    L : numpy.ndarray
        The label array of shape (N,).
    """
    plt.figure(figsize=(8, 6))
    names = ["Setosa", "Versicolor", "Virginica"]
    for i in range(3):
        # extract samples for each class
        D_class = projected_data[:, L == i]
        plt.scatter(D_class[0, :], D_class[1, :], label=names[i])
    
    plt.title("PCA Projection (m=2)")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.legend()


def plot_pca_histogram(projected_data_1d, L):
    """
    Creates a 1D histogram of the data projected onto the first principal component.
    
    Parameters:
    -----------
    projected_data_1d : numpy.ndarray
        The projected data matrix of shape (1, N).
    L : numpy.ndarray
        The label array of shape (N,).
    """
    plt.figure(figsize=(8, 6))
    
    # define class names and corresponding colors from the manual
    class_names = ["Setosa", "Versicolor", "Virginica"]
    
    for i in range(3):
        # select the 1D projected values for the current class
        class_samples = projected_data_1d[0, L == i]
        
        # Plot the histogram
        plt.hist(class_samples, 
                 bins=15,          # adjust bins to match visual density
                 alpha=0.4,         # transparency to show overlaps
                 label=class_names[i], 
                 density=True)     # normalize to show distribution shape

    plt.title("(c) PCA (1st direction)")
    plt.legend(loc='upper left')


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        path = "data/iris_dataset.csv"
    else:
        path = sys.argv[1]
    
    # load the dataset
    D, L = load(path)

    # compute the number of classes
    m = len(numpy.unique(L)) - 1
    
    # compute the projected data and P
    y, P = PCA(D, m)
    
    # visualize the projected data
    plot_pca(y, L)
    plot_pca_histogram(y[0:1, :], L)
    plt.show()