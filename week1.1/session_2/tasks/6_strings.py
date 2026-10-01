# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") #prints the original string
print(f"Modified String 1: {user_string.lower()}") #prints the string in lower case
print(f"Modified String 2: {user_string.upper()}") #prints the string in upper case
print(f"Modified String 3: {user_string.strip()}") #prints the string without any outside white space
print(f"Modified String 4: {user_string.replace('a', '@')}") #replaces all the "a" characters with the "@" symbol
print(f"Modified String 5: {user_string.capitalize()}") #changes the first letter of the string to a capitol
print(f"Modified String 6: {user_string[::-1]}") #reverses the order of the string
print(f"Modified String 7: {user_string.title()}") #capitalises every word in the string
print(f"Modified String 8: {len(user_string)}") #returns the length of the string
print(f"Modified String 9: {user_string.find('a')}") #returns the index in the string where the "a" character first appears
print(f"Modified String 10: {user_string.count('a')}") #returns the amount of "a" characters in the string
print(f"Modified String 11: {user_string.startswith('Hello')}") #returns true if the string starts with "Hello"
print(f"Modified String 12: {user_string.endswith('!')}") #returns true if the string ends with the "!" character
print(f"Modified String 13: {user_string.isalnum()}") #returns true if all the characters in the string are either letters or numbers
print(f"Modified String 14: {user_string.isalpha()}") #returns true if all the characters in the string are letters
print(f"Modified String 15: {user_string.isdigit()}") #returns true if all the characters in the string are numbers



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!