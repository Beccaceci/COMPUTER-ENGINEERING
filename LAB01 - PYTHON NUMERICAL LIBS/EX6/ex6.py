import numpy as np
import sys

# Check for the correct number of command-line arguments
if len(sys.argv) != 2:
    print("Usage: python ex6.py <filename>")
    sys.exit(1)
filename = sys.argv[1]

try:
    with open(filename, "r") as file:
        lines = file.readlines()
        if not lines: # Check if the file is empty
            sys.exit(0)

        # Read N and initialize the NumPy array
        N = int(lines[0].strip())
        room = np.zeros((N, N), dtype=np.float64)

        # Process lightspots
        for line in lines[1:]:
            coords = line.strip().split()

            # Skip lines that don't have at least two coordinates
            if len(coords) < 2:
                continue
            
            # Using x for row and y for column based on coordinates
            x, y = int(coords[0]), int(coords[1])

            # Update the room array based on the lightspot's influence
            room[max(0, x-2):min(N, x+3), max(0, y-2):min(N, y+3)] += 0.2
            room[max(0, x-1):min(N, x+2), max(0, y-1):min(N, y+2)] += 0.3

            # The lightspot itself is fully lit
            room[x, y] += 0.5

        # Print the resulting room array
        for row in room:
            print(" ".join(f"{val:.1f}" for val in row))

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)
