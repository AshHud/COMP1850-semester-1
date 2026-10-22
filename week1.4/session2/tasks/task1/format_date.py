# Week 4, Session 2: Task 1

# Write a function format_date that takes 4 arguments: day, month,
# year, separator. The separator is an optional argument with a default
# value to be "-". The function returns the formatted date as a string
# in the format day-month-year with the default separator.


def format_data(day, month, year, separator="-"):
    
    formatted_date = (day + separator + month + separator + year)    # complete your code here

    return formatted_date


# Write code to test the function with separators such as "/", ":", "."

print(format_data("30", "12", "2007"))
print(format_data("23", "8", "2011", "/"))
print(format_data("15", "1", "2023", ":"))
print(format_data("13", "5", "1994", "."))
