# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

wordcount = 0
user_input = input("Enter file name (name.txt): ")

# open and read the file
    
with open(user_input, 'r') as file:

# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

    values = file.read()
    split_values = values.split()
    word_count = len(split_values)

# display the wordcount

print(f"{user_input} - {word_count}")

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210
