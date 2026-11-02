# Week 1.6, Session 1: Task 5

# Write a program here that uses the QuakeFeed and QuakeDataset
# classes to download earthquake data from a USGS data feed,
# analyze it and display the results

from datetime import datetime
from feed import QuakeFeed
from dataset import QuakeDataset

sig_level = input("Enter Significance Level: ")
user_period = input("Enter Time Period: ")

myQuakeFeed = QuakeFeed(sig_level, user_period)
myDataset = QuakeDataset(myQuakeFeed)
myDataset.read_feed()

# See README.md for full details of what is required and what
# program output should look like

print(myDataset)
