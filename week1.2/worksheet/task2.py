# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

try:
    numbers = read_numbers()
    numbers.sort()
    total = 0

    minimum_value = numbers[0]
    maximum_value = numbers[len(numbers) - 1]
    for item in numbers:
        total = total + item
    mean_value = total / len(numbers)
    median_value = numbers[(len(numbers) - 1) // 2]

    print(f"Minimum = {minimum_value}")
    print(f"Maximum = {maximum_value}")
    print(f"Mean = {mean_value:.1f}")
    print(f"Median = {median_value}")

except:
    sys.exit("Error: no numbers provided")



