# Week 1.3, Session 1: For loop equivalent to a list comprehension

animals = ['dog','cat','hamster','goldfish']
not_fish2 = []

not_fish = [item for item in animals if item != 'goldfish']

print(not_fish)

item_no = 0

for item_no in range (0, len(animals) - 1):
    if animals[item_no] != "goldfish":
        not_fish2.append(animals[item_no])

print(not_fish2)

# write the equivalent for loop to create the not_fish list from animals
# print your result to verify it is the same