import csv

def write_matrix(filepath, header, rows):
    """
    Helper function to write a list of rows to a CSV file with a header.
    """
    with open(filepath, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)