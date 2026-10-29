# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum

from money import Money

print(Money(3,50))
print(Money(3,50).__add__(Money(4,99)))
print(Money(3,50) + Money(4,99))

