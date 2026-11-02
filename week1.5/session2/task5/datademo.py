# Week 1.5, Session 2: Task 5

# Write a program here to create a Dataset containing data
# from a file named by the user

# Your program should display dataset size, mean and median,
# followed by the individual values (using a for loop)

from data import Dataset

user_file = input("Enter filename + extension: ")

myDataset = Dataset(user_file)

print(myDataset)
print(len(myDataset))
print(myDataset[3])
print(myDataset.mean())
print(myDataset.median())