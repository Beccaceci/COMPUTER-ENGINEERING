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

def load_dataset (file_path):
    """
    Loads a dataset from a text file, extracting features and labels.
    Parameters:
        file_path (str): Path to the dataset file.
    Returns:
        tuple:
            - D (numpy.ndarray): Feature matrix with shape (num_features, num_samples).
            - L (numpy.ndarray): Array of labels corresponding to each sample.
    Raises:
        FileNotFoundError: If the specified file does not exist.
    Notes:
        Each line in the file is expected to contain 5 comma-separated values:
        the first 4 are features (converted to float), and the 5th is the label.
        Lines not matching this format are skipped.
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

def split_dataset (D, L, percTrain, seed=0):
    """
    Splits the dataset into training and testing sets based on the specified percentage for training.
    Parameters:
        D (numpy.ndarray): Feature matrix with shape (num_features, num_samples).
        L (numpy.ndarray): Array of labels corresponding to each sample.
        percTrain (float): Percentage of the dataset to be used for training (between 0 and 1).
        seed (int, optional): Random seed for reproducibility. Default is 0.
    Returns:
        tuple:
            - DTR (numpy.ndarray): Training feature matrix.
            - LTR (numpy.ndarray): Training labels.
            - DTE (numpy.ndarray): Testing feature matrix.
            - LTE (numpy.ndarray): Testing labels.
    """

    # Calculate the number of training samples based on the percentage
    nTrain = int(D.shape[1] * percTrain)

    # Set the random seed for reproducibility and shuffle the indices of the samples
    numpy.random.seed(seed)
    idx = numpy.random.permutation(D.shape[1])

    # Split the indices into training and testing sets
    idxTrain = idx[:nTrain]
    idxTest = idx[nTrain:]

    # Use the indices to create the training and testing datasets for features and labels
    DTR = D[:, idxTrain]
    DTE = D[:, idxTest]

    LTR = L[idxTrain]
    LTE = L[idxTest]

    return (DTR, LTR), (DTE, LTE)