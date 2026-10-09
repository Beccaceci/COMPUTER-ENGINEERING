import numpy
import sys
from utils.math_utils import mcol

LABELS_MAP = {
    "Fake": 0,
    "Genuine": 1,
    "Iris-setosa": 0,
    "Iris-versicolor": 1,
    "Iris-virginica": 2
}

def load_dataset(file_path):
    """
    Loads a dataset from a text file, extracting features and labels dynamically.
    """
    try:
        with open(file_path, "r") as file:
            data_list = []
            label_list = []

            # Read each line in the file, split by comma, and process features and labels
            for line in file:
                # Some datasets might have spaces around the commas, so we strip them
                fields = [f.strip() for f in line.strip().split(",")]

                # Skip empty lines
                if len(fields) < 2:
                    continue

                # DYNAMIC FEATURES: Take everything EXCEPT the last column
                features = mcol(numpy.array(fields[:-1], dtype=float))

                # DYNAMIC LABEL: Take the last column
                label_str = fields[-1]

                # Try to parse it as an integer directly (Project dataset)
                try:
                    label = int(label_str)
                # If it's a string, use the dictionary map (Iris dataset)
                except ValueError:
                    label = int(LABELS_MAP.get(label_str))

                # append the features and label to their respective lists
                data_list.append(features)
                label_list.append(label)

            # horizontally stack the list of feature column vectors to create the feature matrix D
            D = numpy.hstack(data_list)

            # convert the list of labels to a numpy array
            L = numpy.array(label_list)

            return D, L

    except FileNotFoundError:
        print(f"Error while loading dataset: '{file_path}'")
        sys.exit(1)


def split_dataset(D, L, train_ratio=0.66, seed=0):
    """
    Splits the dataset into training and validation sets based on a ratio.
    
    Parameters:
    -----------
    D : numpy.ndarray
        The feature matrix (samples as columns).
    L : numpy.ndarray
        The label array.
    train_ratio : float
        The fraction of data to assign to the training set (e.g., 0.66 for 2/3).
    seed : int
        Random seed for reproducibility.
    """
    # calculate exact number of training samples based on the provided ratio
    nTrain = int(D.shape[1] * train_ratio)
    
    # set seed to ensure the random permutation is the same across different runs
    numpy.random.seed(seed)
    
    # randomly shuffle the indices of the samples
    idx = numpy.random.permutation(D.shape[1])
    
    # partition indices into training and test sets
    idxTrain = idx[0:nTrain]
    idxTest = idx[nTrain:]
    
    # extract the corresponding samples and labels
    DTR, LTR = D[:, idxTrain], L[idxTrain]
    DVAL, LVAL = D[:, idxTest], L[idxTest]

    return (DTR, LTR), (DVAL, LVAL)