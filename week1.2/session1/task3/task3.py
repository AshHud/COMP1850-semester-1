# Week 1.2, Session 1: Task 3

fruit = ("apple", "banana", "cherry")
print(fruit)

# Find and display position of "banana"

banana_position = fruit.index("banana")
print(banana_position)

# Display how many times "cherry" occurs

cherry_count = fruit.count("cherry")
print(cherry_count)

# Display how many times "strawberry" occurs

strawberry_count = fruit.count("strawberry")
print(strawberry_count)

# Unpack tuple into variables

(first, second, third) = fruit
print(first)
print(second)
print(third)