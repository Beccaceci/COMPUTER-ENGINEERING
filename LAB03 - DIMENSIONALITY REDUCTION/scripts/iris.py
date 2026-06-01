import matplotlib
import numpy
from pathlib import Path

# Ensure these match your specific util imports
from models.pca import compute_pca
from models.lda import compute_lda, compute_within_class_covariance, compute_between_class_covariance 

from utils.data_loaders import load_dataset, split_dataset
from utils.math_utils import compute_covariance_matrix, mcol
from utils.plot_utils import plot_scatter_pairs
from utils.io_utils import create_emitter, print_matrix


IRIS_LABEL_NAMES = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}

if __name__ == "__main__":
    # 1. Setup Folder Structure
    matplotlib.use("Agg")
    ROOT = Path(".")

    dataset_dir = ROOT / "data" / "iris"
    output_dir = ROOT / "results" / "iris"
    pca_dir = output_dir / "PCA"
    lda_dir = output_dir / "LDA"
    pca_dir.mkdir(parents=True, exist_ok=True)
    lda_dir.mkdir(parents=True, exist_ok=True)

    # Load the dataset
    D, L = load_dataset(dataset_dir / "iris_dataset.csv")
    
    # 2. Setup Emitter
    report_path = output_dir / "iris_results.txt"
    emit = create_emitter(report_path)
    
    emit(f"Dataset Shape: {D.shape[1]} samples, {D.shape[0]} features.")
    
    # ==========================================
    # PART 0: Compute and Print Expected Matrices
    # ==========================================
    emit("\n" + "=" * 65)
    emit("MATRICES FOR COMPARISON WITH LAB INSTRUCTIONS")
    emit("=" * 65)
    
    # Compute Dataset Mean (mu)
    mu = mcol(numpy.mean(D, axis=1))
    print_matrix("Dataset Mean (mu)", mu, emit)
    
    # Compute Covariance Matrix (C)
    C = compute_covariance_matrix(D)
    print_matrix("Covariance Matrix (C)", C, emit)
    
    # Compute Between-class Covariance Matrix (SB)
    SB = compute_between_class_covariance(D, L)
    print_matrix("Between-class Covariance Matrix (SB)", SB, emit)
    
    # Compute Within-class Covariance Matrix (SW)
    SW = compute_within_class_covariance(D, L)
    print_matrix("Within-class Covariance Matrix (SW)", SW, emit)
    
    emit("\n" + "=" * 65)
    emit("PROJECTIONS (PCA & LDA)")
    emit("=" * 65)

    # Since we are projecting to 2D for both PCA and LDA
    proj_feature_names = ["Direction 1", "Direction 2"]

    # ==========================================
    # PART 1: PCA Projection (m=2)
    # ==========================================
    # Unpack the tuple: discard eigenvalues (_), keep projection matrix (P_pca)
    _, P_pca = compute_pca(D, m=2)
    DP_pca = P_pca.T @ D
    
    # Generate scatter plot for the 2 PCA directions
    plot_scatter_pairs(DP_pca, L, proj_feature_names, IRIS_LABEL_NAMES, pca_dir, "Iris PCA")
    emit("[+] PCA projections computed and plotted successfully.")
    

    # ==========================================
    # PART 2: LDA Projection (m=2)
    # ==========================================
    # Max dimensions for LDA is C-1 (3 classes - 1 = 2 dimensions)
    _, W_lda = compute_lda(D, L, m=2)
    DP_lda = W_lda.T @ D
    
    # Generate scatter plot for the 2 LDA directions
    plot_scatter_pairs(DP_lda, L, proj_feature_names, IRIS_LABEL_NAMES, lda_dir, "Iris LDA")
    emit("[+] LDA projections computed and plotted successfully.")

    emit(f"\n[+] All outputs successfully generated and saved to: {report_path}")

    # ==========================================
    # PART 3: BINARY CLASSIFICATION
    # ==========================================
    emit("\n" + "=" * 65)
    emit("BINARY CLASSIFICATION (Versicolor vs Virginica)")
    emit("=" * 65)

    # Filter out Setosa (label 0)
    D_bin = D[:, L != 0]
    L_bin = L[L != 0]

    # Split dataset
    (DTR, LTR), (DVAL, LVAL) = split_dataset(D_bin, L_bin, train_ratio=2.0/3.0)

    # --- 1. LDA Classification ---
    _, W_lda_bin = compute_lda(DTR, LTR, m=1)
    DTR_lda_bin = W_lda_bin.T @ DTR # project the training data onto the LDA direction
    DVAL_lda_bin = W_lda_bin.T @ DVAL # project the validation data onto the LDA direction

    # Orient so mean of Virginica (2) > mean of Versicolor (1)
    mean_1_lda = numpy.mean(DTR_lda_bin[0, LTR == 1]) # mean of the projection of the training data belonging to class 1
    mean_2_lda = numpy.mean(DTR_lda_bin[0, LTR == 2]) # mean of the projection of the training data belonging to class 2
    
    if mean_2_lda < mean_1_lda: # if the mean of Virginica is smaller than the mean of Versicolor, flip the sign of the projection
        DTR_lda_bin = -DTR_lda_bin
        DVAL_lda_bin = -DVAL_lda_bin
        mean_1_lda = numpy.mean(DTR_lda_bin[0, LTR == 1]) # update the mean of the projection of the training data belonging to class 1
        mean_2_lda = numpy.mean(DTR_lda_bin[0, LTR == 2]) # update the mean of the projection of the training data belonging to class 2

    # Set the threshold as the average between the two class means
    threshold_lda = (mean_1_lda + mean_2_lda) / 2.0
    
    PVAL_lda = numpy.zeros(LVAL.shape, dtype=numpy.int32) # initialize the predicted labels array to zeros
    PVAL_lda[DVAL_lda_bin[0] >= threshold_lda] = 2 # set the predicted label to 2 if the projection is greater than or equal to the threshold
    PVAL_lda[DVAL_lda_bin[0] < threshold_lda] = 1 # set the predicted label to 1 if the projection is less than the threshold
    
    errors_lda = numpy.sum(PVAL_lda != LVAL) # compute the number of errors
    error_rate_lda = errors_lda / LVAL.size # compute the error rate
    emit(f"LDA Classification Error Rate: {errors_lda} / {LVAL.size} ({error_rate_lda * 100:.2f}%)")

    # --- 2. PCA Classification (using 1 principal direction) ---
    _, P_pca_bin = compute_pca(DTR, m=1)
    DTR_pca_bin = P_pca_bin.T @ DTR # project the training data onto the PCA direction
    DVAL_pca_bin = P_pca_bin.T @ DVAL # project the validation data onto the PCA direction

    # Orient so mean of Virginica (2) > mean of Versicolor (1)
    mean_1_pca = numpy.mean(DTR_pca_bin[0, LTR == 1]) # mean of the projection of the training data belonging to class 1
    mean_2_pca = numpy.mean(DTR_pca_bin[0, LTR == 2]) # mean of the projection of the training data belonging to class 2
    
    if mean_2_pca < mean_1_pca: # if the mean of Virginica is smaller than the mean of Versicolor, flip the sign of the projection
        DTR_pca_bin = -DTR_pca_bin # flip the sign of the projection
        DVAL_pca_bin = -DVAL_pca_bin # flip the sign of the projection
        mean_1_pca = numpy.mean(DTR_pca_bin[0, LTR == 1]) # update the mean of the projection of the training data belonging to class 1
        mean_2_pca = numpy.mean(DTR_pca_bin[0, LTR == 2]) # update the mean of the projection of the training data belonging to class 2
        
    threshold_pca = (mean_1_pca + mean_2_pca) / 2.0 # Set the threshold as the average between the two class means
    
    PVAL_pca = numpy.zeros(LVAL.shape, dtype=numpy.int32) # initialize the predicted labels array to zeros
    PVAL_pca[DVAL_pca_bin[0] >= threshold_pca] = 2 # set the predicted label to 2 if the projection is greater than or equal to the threshold
    PVAL_pca[DVAL_pca_bin[0] < threshold_pca] = 1 # set the predicted label to 1 if the projection is less than the threshold
    
    errors_pca = numpy.sum(PVAL_pca != LVAL) # compute the number of errors
    error_rate_pca = errors_pca / LVAL.size # compute the error rate
    emit(f"PCA Classification Error Rate (m=1): {errors_pca} / {LVAL.size} ({error_rate_pca * 100:.2f}%)")

    # --- 3. PCA + LDA Classification ---
    emit("\nPCA + LDA Classification:")
    for m in range(1, 5):
        # PCA on Training Set
        _, P_pca_tr = compute_pca(DTR, m=m) # compute PCA on the training set
        DTR_pca = P_pca_tr.T @ DTR # project the training data onto the PCA direction
        DVAL_pca = P_pca_tr.T @ DVAL # project the validation data onto the PCA direction

        # LDA on PCA-Projected Training Set
        _, W_lda_pca = compute_lda(DTR_pca, LTR, m=1) # compute LDA on the PCA-projected training data
        DTR_lda_pca = W_lda_pca.T @ DTR_pca # project the PCA-projected training data onto the LDA direction
        DVAL_lda_pca = W_lda_pca.T @ DVAL_pca # project the PCA-projected validation data onto the LDA direction

        # Orient
        mean_1_lda_pca = numpy.mean(DTR_lda_pca[0, LTR == 1]) # mean of the projection of the training data belonging to class 1
        mean_2_lda_pca = numpy.mean(DTR_lda_pca[0, LTR == 2]) # mean of the projection of the training data belonging to class 2
        
        if mean_2_lda_pca < mean_1_lda_pca: # if the mean of Virginica is smaller than the mean of Versicolor, flip the sign of the projection
            DTR_lda_pca = -DTR_lda_pca # flip the sign of the projection
            DVAL_lda_pca = -DVAL_lda_pca # flip the sign of the projection
            mean_1_lda_pca = numpy.mean(DTR_lda_pca[0, LTR == 1]) # update the mean of the projection of the training data belonging to class 1
            mean_2_lda_pca = numpy.mean(DTR_lda_pca[0, LTR == 2]) # update the mean of the projection of the training data belonging to class 2

        # Threshold and Evaluate
        t_lda_pca = (mean_1_lda_pca + mean_2_lda_pca) / 2.0 # Set the threshold as the average between the two class means
        p_lda_pca = numpy.zeros(LVAL.shape, dtype=numpy.int32) # initialize the predicted labels array to zeros
        p_lda_pca[DVAL_lda_pca[0] >= t_lda_pca] = 2 # set the predicted label to 2 if the projection is greater than or equal to the threshold
        p_lda_pca[DVAL_lda_pca[0] < t_lda_pca] = 1 # set the predicted label to 1 if the projection is less than the threshold
        
        err_lda_pca = numpy.sum(p_lda_pca != LVAL) # compute the number of errors
        error_rate_lda_pca = err_lda_pca / LVAL.size # compute the error rate
        emit(f"  PCA (m={m}) + LDA Error Rate: {err_lda_pca} / {LVAL.size} ({error_rate_lda_pca * 100:.2f}%)")