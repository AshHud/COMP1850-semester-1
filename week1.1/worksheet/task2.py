"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
try:
    amount = int(input("How much to save every month?: "))
# Validate that they have entered an integer.
except:
    print("Invalid amount")
    


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
amount = amount * 12
# print this out for the user with a suitable message.
print(f"You have saved: {amount}")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
interest = amount * 0.008
# print this out in the format £X.XX (to two decimal places).
print(f"You have saved {interest:.2f} in interest")
