# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

music = {
    "Arctic Monkeys": [
        ["Whatever People Say I Am, That’s What I’m Not", 2006], 
        ["Favourite Worst Nightmare", 2007], 
        ["Humbug", 2009], 
        ["Suck it and See", 2011], 
        ["AM", 2013], 
        ["Tranquility Base Hotel + Casino", 2018], 
        ["The Car", 2022]],
    "Tame Impala": [
        ["Innerpseaker", 2010], 
        ["Lonerism", 2012], 
        ["Currents", 2015], 
        ["The Slow Rush", 2020], 
        ["Deadbeat", 2025]],
    "The Strokes": [["Is This It", 2001], ["Room On Fire", 2003], ["First Impressions of Earth", 2006], ["Angles", 2011], ["Comedown Machine", 2013], ["The New Abnormal", 2020], ["Reality Awaits", 2026]],
}

# Pretty-print the data structure

pprint(music, width=80, sort_dicts=False)

# Display details of one album recorded by a specific artist

albums = music.get("Arctic Monkeys")
print(albums[1])
