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
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as f:
        f.write("LAB 04: 1D GAUSSIAN MLE ESTIMATES (PROJECT DATASET)\n")
        f.write("=" * 65 + "\n")
        
    def emit(text=""):
        print(text)
        with open(file_path, "a") as f:
            f.write(str(text) + "\n")
    return emit