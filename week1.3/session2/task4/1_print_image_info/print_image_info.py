# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

with open ("../images/feep.pgm", "r") as infile:

# Read the file content

    lines = infile.readlines()

    sizes = lines[1].strip().split(" ")

    max_grey = lines[2].strip()

    print(f"Dimensions: {sizes[0]} X {sizes[1]} pixels")

    print(f"Max grey value: {max_grey}")

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)