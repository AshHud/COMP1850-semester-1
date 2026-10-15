# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except

invalid_height = False
invalid_width = False
invalid_pixels = False

with open ("../images/feep.pgm", "r") as infile:

# Read the file content

    lines = infile.readlines()

    # Store the width, the height, and the maximum gray value

    sizes = lines[1].strip().split(" ")

    max_grey = lines[2].strip()

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive

    for i in range(3, 3 + int(sizes[1])):
        for j in range(0, int(sizes[0])):

            pixel_row = lines[i].strip().split(" ")

            pixel_row_cleaned = [item for item in pixel_row if item != ""]

            current_pixel = pixel_row_cleaned[j]

            if int(sizes[0]) != len(pixel_row_cleaned):
                invalid_width = True

            if int(sizes[1]) != len(lines) - 3:
                invalid_height = True
 
            if int(current_pixel) < 0 or int(current_pixel) > int(max_grey):
                invalid_pixels = True

if invalid_height == True or invalid_pixels == True or invalid_width == True:
    if invalid_height == True:
        print("Invalid Height")
    elif invalid_width == True:
        print("Invalid Width")
    elif invalid_pixels == True:
        print("Invalid Pixels")
else:
    print("Valid image")

# Check if the widths and heights are the same as specified

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value