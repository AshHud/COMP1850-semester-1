import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

times_to_run = int(input("Enter amount of names to generate: "))

# Display the chosen names, one per line

for i in range(0, times_to_run):
    print(names[random.randint(0,999)])