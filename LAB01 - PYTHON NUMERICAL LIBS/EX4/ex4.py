import sys

# Check if the filename is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python ex4.py <filename>")
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
        numCopiesAvailable = {}
        numCopiesSoldPerMonth = {}
        prices_queue = {}
        gain = {}

        for line in file:
            fields = line.strip().split()

            # Skip lines that do not have enough fields
            if len(fields) < 5:
                continue

            # Extract the relevant information from each line
            ISBN = fields[0]
            operation = fields[1]
            date = fields[2]
            numCopies = int(fields[3])
            pricePerCopy = float(fields[4])

            if operation == "B": # Operation "B" indicates a book purchase
                # Update the number of copies available for each book.
                numCopiesAvailable[ISBN] = numCopiesAvailable.get(ISBN, 0) + numCopies
                
                # Store the price per copy for each book in a queue to calculate the gain later.
                if ISBN not in prices_queue:
                    prices_queue[ISBN] = []
                prices_queue[ISBN].append(pricePerCopy)
            elif operation == "S":
                # Update the number of copies sold for each book.
                numCopiesAvailable[ISBN] = numCopiesAvailable.get(ISBN, 0) - numCopies

                # Extract the month and year from the date 
                month = hMonthNames[int(date.split("/")[1])]
                year = date.split("/")[2]
                month_year = month + ", " + year
                
                # Update the number of copies sold per month
                numCopiesSoldPerMonth[month_year] = numCopiesSoldPerMonth.get(month_year, 0) + numCopies

                # Update the gain for each book
                if prices_queue[ISBN]:
                    buy_price = prices_queue[ISBN].pop(0)
                else:
                    buy_price = 0.0
                total_profit = (pricePerCopy - buy_price) * numCopies
                
                if ISBN not in gain:
                    gain[ISBN] = [0, 0.0]
                gain[ISBN][0] += numCopies
                gain[ISBN][1] += total_profit

        # Print the number of copies available for each book
        print("Number of copies available for each book:")
        for ISBN in numCopiesAvailable:
            print(f" {ISBN}: {numCopiesAvailable[ISBN]}")
        print("\n")

        # Print the number of copies sold per month
        print("Number of copies sold per month:")
        for month_year in numCopiesSoldPerMonth:
            print(f" {month_year}: {numCopiesSoldPerMonth[month_year]}")
        print("\n")

        # Print the gain for each book
        print("Gain for each book:")
        for ISBN in gain:
            print(f" {ISBN}: {gain[ISBN][1]:.2f} (avg {gain[ISBN][1]/gain[ISBN][0]:.2f}, sold {gain[ISBN][0]})")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)

