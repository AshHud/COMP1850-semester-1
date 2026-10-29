# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class

import geometry

point = geometry.Point(100.0, 1.5)
circle = geometry.Circle(2.5)
if point in circle:
    print("point is inside circle!")
else:
    print("point is not inside circle angry face")