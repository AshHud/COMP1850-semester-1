import random

myNumbers = []

# Get user to input how many random numbers they want

times_to_run = int(input("Enter amount of numbers to generate: "))

# Generate this many random numbers

for i in range(0, times_to_run):
    myNumbers.append(random.random())

# Write the random numbers to a file named random.txt, one number per line

with open("random.txt", "w") as infile:
    for i in range(0, len(myNumbers)):
        infile.write(str(myNumbers[i]) + "\n")
