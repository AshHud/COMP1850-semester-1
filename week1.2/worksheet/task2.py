# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

try:
    numbers = read_numbers()
    numbers.sort()
    total = 0
    corrected_length = len(numbers) - 1

    minimum_value = numbers[0]

    maximum_value = numbers[corrected_length]

    for item in numbers:
        total = total + item
    mean_value = total / len(numbers)

    if corrected_length % 2 != 0:
        lower_median_value = numbers[corrected_length // 2]
        upper_median_value = numbers[(corrected_length // 2) + 1]
        median_value = (lower_median_value + upper_median_value) / 2
    else:
        median_value = numbers[corrected_length // 2]

    print(f"Minimum = {minimum_value}")
    print(f"Maximum = {maximum_value}")
    print(f"Mean = {mean_value:.1f}")
    print(f"Median = {median_value}")

except:
    sys.exit("Error: no numbers provided")


