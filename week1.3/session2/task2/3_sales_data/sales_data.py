# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data

Widget_A_total = 0
Widget_B_total = 0
Widget_C_total = 0
Widget_D_total = 0
number_of_rows = 0
highest_sale_amount = 0
sale_values = []
with open("sales.csv", "r") as infile:

# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format

    for line in infile:
        
        current_line_values = line.strip().split(",")

        if current_line_values[2] == "Sales_Amount":
            continue

        number_of_rows = number_of_rows + 1
        current_sale_amount = int(current_line_values[2])
        current_amount_sold = int(current_line_values[3])
        sale_values.append(current_sale_amount)

        if current_sale_amount > highest_sale_amount:
            highest_sale_amount = current_sale_amount

        if current_line_values[1] == "Widget A":
            Widget_A_total = Widget_A_total + current_amount_sold
        elif current_line_values[1] == "Widget B":
            Widget_B_total = Widget_B_total + current_amount_sold
        elif current_line_values[1] == "Widget C":
            Widget_C_total = Widget_C_total + current_amount_sold
        elif current_line_values[1] == "Widget D":
            Widget_D_total = Widget_D_total + current_amount_sold

average_sale_amount = sum(sale_values) / number_of_rows

sold_widgets = [Widget_A_total, Widget_B_total, Widget_C_total, Widget_D_total]
sorted_sold_widgets = [Widget_A_total, Widget_B_total, Widget_C_total, Widget_D_total]

sorted_sold_widgets.sort(reverse = True)

print(sold_widgets)
print(sorted_sold_widgets)

largest_widget_number = sorted_sold_widgets[0]

if largest_widget_number == sold_widgets[0]:
    largest_widget = "Widget A"
elif largest_widget_number == sold_widgets[1]:
    largest_widget = "Widget B"
elif largest_widget_number == sold_widgets[2]:
    largest_widget = "Widget C"
elif largest_widget_number == sold_widgets[3]:
    largest_widget = "Widget D"

print("")
print(f"Largest Sale: {highest_sale_amount}")
print(f"Average Sale per Day: {average_sale_amount}")
print(f"Most Sold Widget: {largest_widget}")


# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows