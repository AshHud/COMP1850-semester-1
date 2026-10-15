# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]

name = []
maths_grade = []
science_grade = []
history_grade = []
average_grade = []

with open("student_data.csv", "r") as infile:

# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3

    for line in infile:
        
        current_line_values = line.strip().split(",")

        if current_line_values[0] == "ID":
            continue

        name.append(current_line_values[1])
        maths_grade.append(int(current_line_values[2]))
        science_grade.append(int(current_line_values[3]))
        history_grade.append(int(current_line_values[4]))

        current_average_grade = (int(current_line_values[2]) + int(current_line_values[3]) + int(current_line_values[4])) / 3

        average_grade.append(f"{current_average_grade:.2f}")

# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f

with open("report.txt", "w") as outfile:

    for i in range (0, len(name)):

        outfile.write(name[i] + ", " + str(average_grade[i]) + "\n")

