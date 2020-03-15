## DNA
## Identify to whom a sequence of DNA belongs from a given database

# Import modules
from sys import argv, exit
import csv

if len(argv) != 3:
    print("Implementation: python data.py database.csv sequences.txt")
    exit(1)

# Open database csv file
with open(argv[1]) as csvFile:
    reader = csv.reader(csvFile)
    # Write STRs into memory, write database into memory
    strs = next(reader)[1:]
    db = list(reader)

# Open sequence text file (one long string)
with open(argv[2]) as textFile:
    # Write the one line sequence into memory
    sequence = textFile.read()

print(db)
print(strs)
print(sequence)

# Our list of STR matches for the sequence of DNA
match = []

for pattern in strs:

    length = len(pattern)   # Length of current STR
    maxRun = 0              # Tracks maximum number of runs of current STR in sequence
    runCount = 0            # Current runcount, compared later with maxRun to see if we should update
    index = 0               # Variable to set the starting point of the find() method

    # Look for first instance of current STR in sequence, and start looping
    while (sequence.find(pattern, index, len(sequence)) != -1):
        # Returns the starting index
        tmp = sequence.find(pattern, index, len(sequence))

        # First instance default runCount to 1
        if index == 0:
            runCount = 1
        # Check if consecutive
        elif sequence.find(pattern, tmp - length, tmp) != -1:
            runCount += 1
        # Not consecutive
        else:
            runCount = 1

        # if the runcount is greater than the maxRun, update it
        if runCount > maxRun:
            maxRun = runCount

        # Look for next instance of STR
        index = tmp + 1

    # Append the maximum runs of STR to the matches list
    match.append(maxRun)

# Convert our match STR numbers to be strings (Since our db contains strings)
for i in range(0, len(match)):
    match[i] = str(match[i])

# Compare the match list to the database
for person in db:
    if person[1:] == match:
        # Match found
        print(person[0])
        exit(0)

# No match found
print("No match found")
exit(2)