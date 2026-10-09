import sys

# Check if the filename is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python ex1.py <filename>")
    sys.exit(1)
filename = sys.argv[1]

try:
    with open(filename, "r") as file:
        # Initialize an empty list to store the athletes' information
        athlets = []
        for line in file:
            # .strip() removes leading and trailing whitespace characters, including the newline character ('\n')
            # .split() splits the line into a list of strings based on whitespace (by default)
            fields = line.strip().split()

            # Check if the line has at least 8 fields
            if len(fields) < 8:
                continue

            # Extract the athlete's name, surname, nationality, and evaluations from the fields
            name = fields[0]
            surname = fields[1]
            nationality = fields[2]
            evaluations = sorted([float(e) for e in fields[3:]])  # Convert evaluations to floats and sort them

            # Calculate the final score by summing the three middle evaluations (after sorting, these are the evaluations at indices 1, 2, and 3)
            finalScore = sum(evaluations[1:4])

            # Create a list for the athlete's information and append it to the list of athletes
            athlete = [name, surname, nationality, finalScore]
            athlets.append(athlete)

        # Check if any valid athlete records were found
        if not athlets:
            print("No valid athlete records found.")
            sys.exit(0)

        # Print the first three athletes with the best scores
        print("Final ranking:")
        athlets.sort(key=lambda x: x[3], reverse=True)
        for i, athlete in enumerate(athlets[:3]):
            print(f"{i+1}. {athlete[0]} {athlete[1]} - Score: {athlete[3]}")
        print("\n")

        # Compute the total score for each nation
        nationalScore = {}
        for athlete in athlets:
            nation = athlete[2]
            score = athlete[3]

            # Update the total score for the nation by adding the athlete's score to the existing total (or initializing it if the nation is not yet in the dictionary)
            nationalScore[nation] = nationalScore.get(nation, 0) + score

        # Select the nation that obtained the best score considering the sum of all the competitors of this country
        bestCountry = max(nationalScore, key=nationalScore.get)

        # Print the best country and its total score
        print("Best country:")
        print(f"{bestCountry} - Total score {nationalScore[bestCountry]} \n")       

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)           