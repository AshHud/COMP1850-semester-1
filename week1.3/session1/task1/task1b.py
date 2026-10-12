# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())

# 1st iteration: ['apple','pear','banana','orange']
# 4th iteration: ['orange']
# right after the loop finishes []

# doesnt run forever because it loops until fruit is empty