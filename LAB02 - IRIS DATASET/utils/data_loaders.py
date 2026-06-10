import numpy
import matplotlib.pyplot as plt
import sys
from utils.math_utils import mcol, compute_mean, compute_covariance, compute_variance, compute_std

# Mapping of class labels to integer values for easier processing
LABELS_MAP = {
    "Iris-setosa": 0,
    "Iris-versicolor": 1,
    "Iris-virginica": 2
}

# Names of the features in the Iris dataset for reference
FEATURE_NAMES = ["Sepal length", "Sepal width", "Petal length", "Petal width"]


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


def visualize_dataset(D, L, title_prefix=""):
    """Generates histograms and scatter plots for feature analysis"""

    # Generate histograms for each feature, separated by class labels
    for i, name in enumerate(FEATURE_NAMES):
        plt.figure()
        plt.title(f"{title_prefix} Histogram: {name}")
        for label_name, label_id in LABELS_MAP.items():
            # Filter data using masks to select only the samples corresponding to the current label and feature
            plt.hist(D[i, L == label_id], bins=10, density=True, alpha=0.4, label=label_name)
        plt.xlabel(name)
        plt.ylabel("Density")
        plt.legend()

    # Generate scatter plots for each pair of features
    for i in range(len(FEATURE_NAMES)):
        for j in range(i + 1, len(FEATURE_NAMES)):
            plt.figure()
            plt.title(f"{title_prefix} Scatter: {FEATURE_NAMES[i]} vs {FEATURE_NAMES[j]}")
            for label_name, label_id in LABELS_MAP.items():
                # Filter data using masks to select only the samples corresponding to the current label and features for the scatter plot
                plt.scatter(D[i, L == label_id], D[j, L == label_id], label=label_name, alpha=0.7)
            plt.xlabel(FEATURE_NAMES[i])
            plt.ylabel(FEATURE_NAMES[j])
            plt.legend()
    plt.show()

    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        path = "../data/iris_dataset.csv"
    else:
        path = sys.argv[1]

    D, L = load_dataset(path)


    # Global stats
    mu_g = compute_mean(D)
    print(f"Global Mean:\n{mu_g}")
    print(f"Global Covariance:\n{compute_covariance(D)}\n")

    # Per-class stats
    for label_name, label_id in LABELS_MAP.items():
        D_class = D[:, L == label_id]
        print(f"--- {label_name} ---")
        print(f"Mean:\n{compute_mean(D_class)}")
        print(f"Std Dev: {compute_std(D_class).flatten()}\n")

    # Visualization
    visualize_dataset(D, L)
