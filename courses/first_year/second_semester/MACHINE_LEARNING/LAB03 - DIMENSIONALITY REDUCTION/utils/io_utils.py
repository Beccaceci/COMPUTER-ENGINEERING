import csv

def write_matrix(filepath, header, rows):
    """
    Helper function to write a list of rows to a CSV file with a header.
    """
    with open(filepath, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

def create_emitter(file_path):
    """
    Creates an emit function that prints to standard output AND appends to a text file.
    It automatically clears the target file upon initialization.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as f:
        f.write("LAB 03: EXPECTED MATRICES (IRIS DATASET)\n")
        f.write("=" * 65 + "\n")
        
    def emit(text=""):
        print(text)
        with open(file_path, "a") as f:
            f.write(str(text) + "\n")
    return emit

def print_matrix(name, matrix, emit):
    """Helper function to cleanly format and print numpy matrices."""
    emit(f"\n--- {name} ---")
    if matrix.ndim == 1 or matrix.shape[1] == 1:
        # Column vector or 1D array
        for val in matrix.ravel():
            emit(f"{val:>12.6f}")
    else:
        # 2D Matrix
        for row in matrix:
            row_vals = " ".join([f"{val:>12.6f}" for val in row])
            emit(row_vals)