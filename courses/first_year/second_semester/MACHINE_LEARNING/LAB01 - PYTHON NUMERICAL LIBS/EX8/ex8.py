import numpy as np
import sys

# Check if filename is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python ex8.py <filename>")
    sys.exit(1)
filename = sys.argv[1]

try:
    with open(filename, "r") as file:
        first_line = file.readline().strip()

        # Check if the first line is empty
        if not first_line:
            sys.exit("File is empty")
        
        num_competitors = int(first_line)
        
        names = []
        raw_scores = np.zeros((num_competitors, 5), dtype=np.float64)

        # Read competitor data
        for i in range(num_competitors):
            line = file.readline().strip().split()
            if not line:
                break
            
            # Check if the line has enough data
            if len(line) < 8:
                raise ValueError(f"Line {i+2} does not contain enough data.")
            
            # Store the competitor's name
            names.append(f"{line[0]} {line[1]}")
            
            # Convert the scores to float and store them in the raw_scores array
            raw_scores[i] = [float(val) for val in line[3:8]]

    # Sort the scores for each competitor and calculate the final scores by summing the middle three scores
    sorted_scores = np.sort(raw_scores, axis=1)
    
    # Calculate the final scores by summing the middle three scores (excluding the lowest and highest)
    final_scores = np.sum(sorted_scores[:, 1:4], axis=1)

    # Get the indices of the top 3 competitors based on their final scores
    top_indices = np.argsort(final_scores)[::-1][:3]

   
    # Print the final ranking of the top 3 competitors
    print("final ranking:")
    for rank, idx in enumerate(top_indices, 1):
        print(f"{rank}: {names[idx]}")
        print(f"Score: {final_scores[idx]:.1f}")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except ValueError as e:
    print(f"Data Error: {e}")