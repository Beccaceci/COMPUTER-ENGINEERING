import numpy
import sys
import matplotlib.pyplot as plt
from utils.data_loaders import load, split_dataset
from utils.math_utils import mcol
from models.pca import PCA
from models.lda import LDA


def plot_training_vs_validation(DTR_lda, LTR, DVAL_lda, LVAL):
    """
    Generates side-by-side histograms using colors from the lab manual.
    """
    plt.figure(figsize=(12, 5))
    
    # Define colors to match the attached image
    color_map = {1: 'orange', 2: 'green'}
    name_map = {1: 'Versicolor', 2: 'Virginica'}
    
    # (a) Model training set (DTR, LTR)
    plt.subplot(1, 2, 1)
    for cls in [1, 2]:
        plt.hist(DTR_lda[0, LTR == cls], 
                 bins=5, 
                 alpha=0.4, 
                 color=color_map[cls], 
                 label=name_map[cls], 
                 density=True)
    plt.title("(a) Model training set (DTR, LTR)")
    plt.legend()
    
    # (b) Validation set (DVAL, LVAL)
    plt.subplot(1, 2, 2)
    for cls in [1, 2]:
        plt.hist(DVAL_lda[0, LVAL == cls], 
                 bins=5, 
                 alpha=0.4, 
                 color=color_map[cls], 
                 label=name_map[cls], 
                 density=True)
    plt.title("(b) Validation set (DVAL, LVAL)")
    plt.legend()
    
    plt.tight_layout()
    plt.show()


def evaluate_classifier(DTR_proj, LTR, DVAL_proj, LVAL, method_name):
    """
    Standardizes the orientation, computes threshold, and evaluates error.
    """
    # Fix orientation: Virginica (2) mean should be > Versicolor (1) mean
    if DTR_proj[0, LTR==2].mean() < DTR_proj[0, LTR==1].mean():
        DTR_proj = -DTR_proj
        DVAL_proj = -DVAL_proj

    # Threshold: average of the projected training class means
    threshold = (DTR_proj[0, LTR==1].mean() + DTR_proj[0, LTR==2].mean()) / 2.0

    # Prediction 
    PVAL = numpy.zeros(LVAL.shape, dtype=numpy.int32)
    PVAL[DVAL_proj[0] >= threshold] = 2
    PVAL[DVAL_proj[0] < threshold] = 1

    # Error calculation
    errors = numpy.sum(PVAL != LVAL)
    print(f"{method_name} - Validation Errors: {errors}/{LVAL.size} ({(errors/LVAL.size)*100:.2f}%)")


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        path = "data/iris_dataset.csv"
    else:
        path = sys.argv[1]
    
    # load the dataset and filter for binary tasks
    DIris, LIris = load(path)
    D_binary = DIris[:, LIris != 0]
    L_binary = LIris[LIris != 0]
    (DTR, LTR), (DVAL, LVAL) = split_dataset(D_binary, L_binary, train_ratio=0.66)

    # estimate LDA strictly on DTR
    W = LDA(DTR, LTR)
    DTR_lda = W.T @ DTR
    DVAL_lda = W.T @ DVAL

    # ensure Virginica mean > Versicolor mean 
    if DTR_lda[0, LTR==2].mean() < DTR_lda[0, LTR==1].mean():
        DTR_lda = -DTR_lda
        DVAL_lda = -DVAL_lda

    # calculate threshold and error
    t = (DTR_lda[0, LTR==1].mean() + DTR_lda[0, LTR==2].mean()) / 2.0
    PVAL = numpy.zeros(LVAL.shape, dtype=numpy.int32)
    PVAL[DVAL_lda[0] >= t] = 2
    PVAL[DVAL_lda[0] < t] = 1
    
    errors = numpy.sum(PVAL != LVAL)
    plot_training_vs_validation(DTR_lda, LTR, DVAL_lda, LVAL)