# Week 4, Session 1

# You are given the function mystery_func. 
# Inspect the code in the function
# Your task is to write a corresponding docstring
# - what the function does 
# - what is the input data and type
# - what is the return value and type

"""
The function returns firstly, the number of uppercase characters, then secondly the amount of lowercase characters
The input data is the parameter being entered into the function of type string
The return value is two variables specified earlier
"""

# function implementation

def mystery_func(string):
    upper = 0
    lower = 0

    for ch in string:
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1
    return (upper, lower)


# testing

print(mystery_func("abc"))
print(mystery_func("The quick Brown Fox!"))
print(mystery_func("012345"))
print(mystery_func("ABC"))


# Can you predict the output of the following lines of code?
# Uncomment the lines of code one by one and run the program
# to see if you are right?

"""
mystery func X will output 1,0? 1,0 
mystery func X will output an error? 0,0
"""

print(mystery_func("X"))
print(mystery_func("[2, 3]"))
