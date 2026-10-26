# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

import geometry

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

x_coord = float(input("Please enter co-ordinate x: "))
y_coord = float(input("Please enter co-ordinate y: "))

circle_radius = float(input("Please enter the radius of the circle: "))

point1 = geometry.Point(x_coord, y_coord)

circle1 = geometry.Circle(circle_radius, point1)

print(f"Area: {circle1.area():.4f}")
print(f"Perimeter: {circle1.perimeter():.4f}")