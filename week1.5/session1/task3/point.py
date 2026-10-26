# Week 1.5, Session 1: Task 3

import math

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

# Finally, add code here to demonstrate use of Point

object1 = Point(3,5)
object2 = Point(6,8)

print(object1.distance())
print(object2.distance())

print(object1.distance_to(object2))


