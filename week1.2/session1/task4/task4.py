# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here? the value that connects the two lists together

both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items? all the values in both lists joined by tomato

food = fruit.union(vegetables)
print(food)

# Add an item to fruit

fruit.add("banana")

# Remove an item from vegetables

vegetables.discard("potato")

# Find and display symmetric difference of the two sets

sym_diff = fruit.symmetric_difference(vegetables)
print(sym_diff)
