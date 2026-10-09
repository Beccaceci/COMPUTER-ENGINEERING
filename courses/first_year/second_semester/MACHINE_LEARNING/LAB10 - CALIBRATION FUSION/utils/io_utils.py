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