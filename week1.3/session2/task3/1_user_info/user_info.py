# Week 1.3, Session 2: Write User Information to a File
# Prompt the user for their name, age, and favorite colour.

user_name = input("Enter name: ")
user_age = input("Enter age: ")
user_colour = input("Enter favourite colour: ")

# Open a file called 'user_info.txt' for reading

with open ("user_info.txt", "w") as outfile:

# Write each piece of information to the file, each on a new line.

    outfile.write(user_name + "\n")
    outfile.write(user_age + "\n")
    outfile.write(user_colour + "\n")

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
