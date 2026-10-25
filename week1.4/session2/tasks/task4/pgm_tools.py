
# PGM functions that we write

def readPGM( filename ):
    ''' 
    Read a named PGM file and store the data in a tuple.
    Input: filename string
    Output: tuple of PGM image data
    '''
    try:
        with open(filename,"r") as f:    # read in the file
            data = f.readlines()
        
        data = [line.strip().split() for line in data[1:]] # clean the space-separated data, skip the first line
          
        width = int(data[0][0]) # store the data - compare to the text in the file
        height = int(data[0][1])
        max_gray = int(data[1][0])
        pixels = [[int(data[2+i][j]) for j in range(width)] for i in range(height)] # nested list comprehension for pixel array
    
        return width,height,max_gray,pixels   # tuple of PGM data
    except:
        return 0,0,0,0
    
def writePGM( filename, image ):
    '''
    Write a PGM file to disk
    Input: filename string, image tuple data
    Output: None
    '''
    width,height,max_gray,pixels = image  # unpack the tuple

    with open(filename,"w") as f:           # open a file for writing
    
        f.write("P2\n")        # write the data in PGM format
        f.write(str(width) + " " + str(height) + "\n")        # don't forget the PGM code "P2"
        f.write(str(max_gray) + "\n")
        for i in range(height):
            for j in range(width):
                f.write(str(pixels[i][j]) + " ")
            f.write("\n")

    return None

def invertPGM( image ):
    '''
    Invert an image, ie. pixel value = 255 - pixel value
    Input: image data
    Output: inverted image data
    '''
    width,height,max_gray,pixels = image  # unpack the tuple

    # your code
    # create a new pixel array of inverted data 
    
    max_gray = 255 - max_gray

    inverted = [[255 - int(pixels[i][j]) for j in range(width)] for i in range(height)]  # you can use a similar nested comprehension to the readPGM() function
    
    return width,height,max_gray,inverted

# code to test the PGM functions

image = readPGM("images/feep.pgm")

print(f"Image with width {image[0]} and height {image[1]}")
print(f"{image[3]}")

# write further code to test your own functions

writePGM("images/test,pgm", (3,5,15,[[0,5,10],[0,3,7],[1,6,8],[1,7,9],[1,10,15]]))

new_image = invertPGM((3,5,15,[[0,5,10],[0,3,7],[1,6,8],[1,7,9],[1,10,15]]))

print("---------------------------------------------------------------------------------------------------------------------------")

print(f"Image with width {new_image[0]} and height {new_image[1]} and max gray value {new_image[2]}")
print(f"{new_image[3]}")