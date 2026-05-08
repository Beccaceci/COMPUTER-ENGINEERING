import numpy
import sys
import matplotlib.pyplot as plt
from utils.data_loaders import load
from models.lda import LDA

def plot_lda_scatter(projected_data, L):
    """
    Creates a 2D scatter plot of the data projected onto the first two LDA directions.
    
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
    
    plt.title("(b) LDA (1st and 2nd direction)")
    plt.xlabel("Discriminant Direction 1")
    plt.ylabel("Discriminant Direction 2")
    plt.legend()


def plot_lda_histogram(projected_data_1d, L):
    """
    Creates a 1D histogram of the data projected onto the first LDA direction.
    
    Parameters:
    -----------
    projected_data_1d : numpy.ndarray
        The projected data matrix of shape (1, N).
    L : numpy.ndarray
        The label array of shape (N,).
    """
    plt.figure(figsize=(8, 6))
    class_names = ["Setosa", "Versicolor", "Virginica"]
    
    for i in range(3):
        # select the 1D projected values for the current class
        class_samples = projected_data_1d[0, L == i]
        
        plt.hist(class_samples, 
                 bins=15,          
                 alpha=0.4,         
                 label=class_names[i], 
                 density=True)     

    plt.title("(d) LDA (1st direction)")
    plt.legend(loc='upper left')


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        path = "data/iris_dataset.csv"
    else:
        path = sys.argv[1]

    # load the dataset
    D, L = load(path)

    # compute the projection matrix W (or orthogonal basis U)
    W = LDA(D, L)
    
    # apply the projection to the matrix of samples D
    y = numpy.transpose(W) @ D
    
    # visualize the projected data
    plot_lda_scatter(y, L)

    # the histogram uses only the 1st direction (the first row of our projection)
    plot_lda_histogram(y[0:1, :], L)

    # show the plot only once
    plt.show()