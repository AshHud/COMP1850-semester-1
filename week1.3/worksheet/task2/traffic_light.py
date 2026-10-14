"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
times_looped = 0
maxtime = int(input("enter maximum time: "))  # read an integer number of steps (>0)
state = ""

for i in range(0, maxtime + 1):
    if systime >= 15:
        systime = 0
        times_looped = times_looped + 1

    if systime >= 0 and systime <= 3:
        state = "red"
    elif systime >= 4 and systime <= 6:
        state = "red_amber"
    elif systime >= 7 and systime <= 11:
        state = "green"
    elif systime >= 12 and systime <= 14:
        state = "amber"

    total_time = systime + (times_looped * 15)

    print(f"Time {total_time:03} State {state}")

    systime = systime + 1

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14