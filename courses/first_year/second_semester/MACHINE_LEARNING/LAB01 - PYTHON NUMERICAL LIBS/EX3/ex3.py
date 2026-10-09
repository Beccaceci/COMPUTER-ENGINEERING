import sys

# Check if the filename is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python ex3.py <filename>")
    sys.exit(1)
filename = sys.argv[1]

# Define a dictionary to map month numbers to month names
hMonthNames = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

try:
    with open(filename, "r") as file:
        cities = {}
        months = {}
        total_births = 0
        for line in file:
            fields = line.strip().split()

            # Skip lines that do not have enough fields
            if len(fields) < 4:
                continue

            # Extract the birthplace, and birthdate from the fields
            birthplace = fields[2]
            month = int(fields[3].split("/")[1])

            # Update the number of births per city and per month
            cities[birthplace] = cities.get(birthplace, 0) + 1

            # Update the number of births per month
            months[month] = months.get(month, 0) + 1

            # Update the total number of births
            total_births += 1

        # Print the number of births per city
        print("Births per city:")
        for city in cities:
            print(f" {city}: {cities[city]}")
        print("\n")

        # Print the number of births per month
        print("Births per month:")
        for month in months:
            print(f" {hMonthNames[month]}: {months[month]}")
        print("\n")

        # Print the average number of births per city
        print(f" Average number of births: {float(total_births/len(cities.keys())):.2f}")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)

