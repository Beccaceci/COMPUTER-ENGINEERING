import csv
import numpy

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


def print_model_table(model_name, logSJoint, logSMarginal, logSPost, error_rate, emit):
    """
    Prints the three matrices inside a table boundary, and the error rate outside of it.
    """
    # Formatting options for clean matrix printing
    opts = {'max_line_width': 120, 'precision': 4, 'suppress_small': True}
    
    # --- TABLE START ---
    emit("\n" + "=" * 80)
    emit(f"MODEL: {model_name}")
    emit("-" * 80)
    
    emit("--- logSJoint ---")
    emit(numpy.array2string(logSJoint, **opts))
    
    emit("\n--- logMarginal ---")
    emit(numpy.array2string(logSMarginal, **opts))
    
    emit("\n--- logPosterior ---")
    emit(numpy.array2string(logSPost, **opts))
    emit("=" * 80)
    # --- TABLE END ---
    
    # Error rate printed OUTSIDE the table
    emit(f"> ERROR RATE: {error_rate:.2f}%\n")