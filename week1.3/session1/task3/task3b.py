# Week 1.3, Session 1: Task 3b

fruit = ['apple','pear','banana','orange']

while fruit:
	print(fruit.pop())

if len(fruit) != 0:
	print("There are things in the list")
else:
	print("The list is now empty")


# Add an else clause with a message that the list is now empty