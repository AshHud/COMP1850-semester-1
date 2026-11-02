# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

import shapes
from point import Point

my_circle = shapes.Circle(2.5)

print(my_circle)
print(my_circle.area())
print(my_circle.perimeter())
print("Moving the circle...")
my_circle.set_position(Point(1.6, 3.2))
print(my_circle)
my_circle.set_colour("green")
print("Changing the circle's colour...")
print(my_circle)



