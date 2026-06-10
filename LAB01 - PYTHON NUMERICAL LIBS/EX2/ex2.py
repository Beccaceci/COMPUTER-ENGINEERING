import numpy
import sys

# The program should be run with the following command line arguments:
# python ex2.py <filename> -b <busID>
# python ex2.py <filename> -l <lineID>
if (len(sys.argv) < 2):
    print("Usage: python ex2.py <filename>")
    sys.exit(1)

if (len(sys.argv) < 4):
    print("Flag -b or -l must be provided")
    sys.exit(1)
filename = sys.argv[1]

# Function to compute the distance between two points (x1, y1) and (x2, y2)
def distance(x1, y1, x2, y2):
    # Compute the distance between two points (x1, y1) and (x2, y2) using the Euclidean distance formula
    x_difference = float(x2) - float(x1)
    y_difference = float(y2) - float(y1)
    return float(numpy.sqrt(numpy.power(x_difference, 2) + numpy.power(y_difference, 2)))


# Compute the total distance traveled by a bus given its tracks
def computeBusDistance (bus_tracks, busID):
    # Sort the tracks based on the expired seconds
    bus_tracks[busID].sort(key=lambda x: int(x[2]))

    # Compute the total distance traveled by the bus by summing the distances between consecutive tracks
    d = 0
    for i in range(len(bus_tracks[busID])-1):
        d += distance(bus_tracks[busID][i][0], bus_tracks[busID][i][1], bus_tracks[busID][i+1][0], bus_tracks[busID][i+1][1])
    return d


# Compute the average speed of the buses traveling on the line by summing the distances traveled by each bus and dividing by the total time taken by each bus
def computeLineAverageSpeed (bus_tracks):
    speed = []
    for busId in bus_tracks:
        # Compute the distance traveled by the bus and the time taken to travel that distance
        bus_distance = computeBusDistance(bus_tracks, busId)
        last_element = len(bus_tracks[busId]) - 1
        bus_time = float(bus_tracks[busId][last_element][2]) - float(bus_tracks[busId][0][2])
        
        # Compute the average speed of the bus and add it to the list of speeds
        speed.append(bus_distance / bus_time if bus_time > 0 else 0)

    return (numpy.mean(speed) if len(speed) > 0 else 0)


try:
    with open (filename, "r") as file:
        if sys.argv[2] == "-b": # The program should print the total distance traveled by the given bus
            bus_tracks = {}
            targetBusId = sys.argv[3]   # The bus ID for which we want to compute the total distance traveled
            for line in file:
                fields = line.strip().split()
                busId = fields[0]   # The bus ID associated with the track in the line

                # Select only the tracks associated with the required bus
                if targetBusId == busId:
                    # Extract the abcissa, ordinate, and expired seconds from the line and create a track for the bus
                    abcissa = fields[2]
                    ordinate = fields[3]
                    seconds = fields[4]
                    track = [abcissa, ordinate, seconds]

                    # Add the track to the list of tracks associated with the bus
                    if busId in bus_tracks: 
                        bus_tracks[busId].append(track)
                    else:
                        bus_tracks[busId] = [track]

            # Compute the total distance traveled by the bus and print it 
            print(f"{targetBusId} - Total Distance: {computeBusDistance(bus_tracks, targetBusId)}")

        elif sys.argv[2] == "-l": # The program should print the average speed of buses traveling on the line
            bus_tracks = {}
            targetLineId = sys.argv[3]  # The line ID for which we want to compute the average speed of the buses traveling on that line
            for line in file:
                fields = line.strip().split()
                lineId = fields[1]

                # Select only the buses associated with the required line
                if targetLineId == lineId:
                    # Extract the bus ID, abcissa, ordinate, and expired seconds from the line and create a track for the bus
                    busId = fields[0]
                    abcissa = fields[2]
                    ordinate = fields[3]
                    seconds = fields[4]
                    track = [abcissa, ordinate, seconds]

                    # Add the track to the list of tracks associated with the bus
                    if busId in bus_tracks:
                        bus_tracks[busId].append(track)
                    else:
                        bus_tracks[busId] = [track]

            # Compute the average speed of the buses traveling on the line and print it
            print(f"{targetLineId} - Average Speed: {computeLineAverageSpeed(bus_tracks)}")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)