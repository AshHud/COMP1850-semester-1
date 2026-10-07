# Worksheet 1.2: Task 1 Solution
import sys

try:
    grade_number = int(input("Enter grade (0-100): "))

    if grade_number >= 0 and grade_number <= 39:
        grade_type = "Fail"
    elif grade_number >= 40 and grade_number <= 69:
        grade_type = "Pass"
    elif grade_number >= 70 and grade_number <= 100:
        grade_type = "Distinction"
    else:
        sys.exit("Error: Grade must be an integer between 0 and 100")

    print(f"{grade_number} is a {grade_type}")
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")




