# Week 4, Session 1: Task 3

# You are given function add_two_numbers. Your task is to inspect the code,
# and the run the program and observe the output.


def add_two_numbers(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return num1 + num2       # What happen if you remove the parenthesis ()? nothing changes


# Check if the following lines produce the correct output
print(add_two_numbers(3, 4))                #yes
print(add_two_numbers(num1=3, num2=4))      #yes
print(add_two_numbers(3, num2=4))           #yes

# Why does the next line work?
print(add_two_numbers("3", "4"))            #because the function changes the strings to floats

# What happens if you try this? Uncomment the code to find out.
#print(add_two_numbers("three", "four"))     #error because is not a numerical value
