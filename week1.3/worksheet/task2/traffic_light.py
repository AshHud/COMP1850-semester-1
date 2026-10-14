"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
times_looped = 0
loop_time = 0
previous = 0
maxtime = int(input("enter maximum time: "))  # read an integer number of steps (>0)
state = ""
value_list = list(states.values())
key_list = list(states.keys())

next = value_list[0] - 1

for i in range(0, len(value_list)):
    loop_time = loop_time + value_list[i]

for i in range(0, maxtime + 1):

    previous = 0
    next = value_list[0] - 1
    
    if systime >= loop_time:
        systime = 0
        times_looped = times_looped + 1

    if systime >= previous and systime <= next:
        state = key_list[0]
    previous = next
    next = next + value_list[1]

    if systime >= previous and systime <= next :
        state = key_list[1]
    previous = next
    next = next + value_list[2]

    if systime >= previous and systime <= next:
        state = key_list[2]
    previous = next
    next = next + value_list[3]

    if systime >= previous and systime <= next:
        state = key_list[3]

    total_time = systime + (times_looped * loop_time)

    print(f"Time {total_time:03} State {state}")

    systime = systime + 1

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14