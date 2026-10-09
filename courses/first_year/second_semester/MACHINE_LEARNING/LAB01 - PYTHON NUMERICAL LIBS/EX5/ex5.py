import sys

# Check for the correct number of command-line arguments
if len(sys.argv) != 2:
    print("Usage: python ex5.py <filename>")
    sys.exit(1)
filename = sys.argv[1]

try:
    with open(filename, "r") as file:
        lines = file.readlines()
        if not lines: # Check if the file is empty
            sys.exit(0)

        # Read N and initialize the list of lists
        N = int(lines[0].strip())
        room = [[0.0 for _ in range(N)] for _ in range(N)]

        # Process lightspots
        for line in lines[1:]:
            coords = line.strip().split()

            # Skip lines that don't have at least two coordinates
            if len(coords) < 2:
                continue
            
            # Using x for row and y for column based on coordinates
            x, y = int(coords[0]), int(coords[1])

            # Update the room array based on the lightspot's influence
            for i in range(max(0, x-2), min(N, x+3)):
                for j in range(max(0, y-2), min(N, y+3)):
                    room[i][j] += 0.2
                    
            for i in range(max(0, x-1), min(N, x+2)):
                for j in range(max(0, y-1), min(N, y+2)):
                    room[i][j] += 0.3

            # The lightspot itself receives an additional 0.5 to reach +1.0 total
            room[x][y] += 0.5

        # Print the resulting room array
        for row in room:
            print(" ".join(f"{val:.1f}" for val in row))

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)