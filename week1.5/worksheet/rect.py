# Worksheet 1.5: Rectangle Class

import math

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)

        if not isinstance(width, (int)) or not isinstance(height, (int)):
            raise TypeError("width or height is not an integer")
        elif width <= 0 or height <= 0:
            raise ValueError("width or height should be above 0")
        else:
            self.width = width
            self.height = height

    def is_square(self):
        """
        checks if the square is a square
        """
        if self.width == self.height:
            return True
        else:
            return False

    def area(self):
        """
        calculates the area of the square
        """
        square_area = self.width * self.height
        return square_area

    def perimeter(self):
        """
        calculates the perimeter of the square
        """
        square_perimeter = ((self.width * 2) + (self.height * 2))
        return square_perimeter

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)

myrectangle = Rectangle(3, 5)

print(myrectangle.is_square())
print(myrectangle.area())
print(myrectangle.perimeter())