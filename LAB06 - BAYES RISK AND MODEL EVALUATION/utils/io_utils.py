def create_emitter(file_path, title="LAB 06: BAYES DECISIONS AND MODEL EVALUATION"):
    """
    Creates an emit function that prints to standard output AND appends to a text file.
    It automatically clears the target file upon initialization.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as f:
        f.write(f"{title}\n")
        f.write("=" * 80 + "\n")
        
    def emit(text=""):
        print(text)
        with open(file_path, "a") as f:
            f.write(str(text) + "\n")
    return emit

def print_confusion_matrix(M, emit=print):
    """
    Prints the confusion matrix to the console mimicking the Lab 6 PDF format, with a strict vertical alignment and an underscore divider row.
    """
    num_classes = M.shape[0]
    
    # Print the top header fields
    emit("          Class")
    
    # Print the class labels (0, 1, 2...) dynamically aligned to 5 characters each
    class_labels = "".join([f"{i:>5}" for i in range(num_classes)])
    emit(f"       {class_labels}")
    
    # Draw the underscore divider line matching the matrix width dynamically
    # 9 spaces accounts for the 'Pred X | ' header length
    divider_width = 9 + (5 * num_classes)
    emit("_" * divider_width)
    
    # Print each row of the matrix values
    for i in range(num_classes):
        # Format each matrix value to take exactly 5 characters, right-aligned
        row_vals = "".join([f"{int(M[i, j]):>5}" for j in range(num_classes)])
        
        # Combine the row prefix with the perfectly spaced values
        emit(f"Pred i {i} |{row_vals}")