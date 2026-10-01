# Fill out the code to make a very simple calculator

# ask the user to enter number1:
try:
    num1 = int(input("enter the first number: "))

# ask the user to enter number 2:
    num2 = int(input("enter the second number: "))

# calculate the result of adding those numbers together
    answer = num1 + num2

# print out the answer
    print(f"the sum of {num1} and {num2} is {answer}!")
except:
    print("thats not a number")
