# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here

    def __init__ (newobj, x_coordinate, y_coordinate):

        newobj.x = x_coordinate
        newobj.y = y_coordinate

    # Add distance() method here

    def distance(newobj):

        x_part = ((newobj.x) ** 2)
        y_part = ((newobj.y) ** 2)
        objdistance = math.sqrt(x_part + y_part)

        return objdistance

    # Add distance_to() method here
    # (This will need a parameter representing another point)

    def distance_to(newobj, second_obj):

        x_part = ((newobj.x - second_obj.x) ** 2)
        y_part = ((newobj.y - second_obj.y) ** 2)
        objdistanceto = math.sqrt(x_part + y_part)

        return objdistanceto

# Add a definition for a Circle class here, giving it

class Circle:

    def __init__ (newobj, new_radius, new_centre):

        newobj.centre = new_centre
        newobj.radius = new_radius

    def area(newobj):

        obj_area = (newobj.radius ** 2) * math.pi

        return obj_area

    def perimeter(newobj):

        obj_perimeter = (newobj.radius * 2) * math.pi

        return obj_perimeter

#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!
