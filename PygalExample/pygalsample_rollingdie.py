""" The program imports the required library and classes and renders the output in the bar chart """
from PygalExample.pygalsample_die import Die
import sys
import os
sys.path.append(os.path.abspath('Users/rahul/Library/Python/3.6/lib.python/site-packages/pygal'))
import pygal

d = Die()

# Generate 100 random dice throws and store the results in a list
results = []
for roll in range(1, 100):
    result = d.roll()
    results.append(result)
print(results)

# Calculate the frequency of dice throw results in a list
frequency = []
for value in range(1,7):
    freq = results.count(value)
    frequency.append(freq)
print(frequency)

# Print frequency of results in bar chart
# Leverage the pygal library

hist = pygal.Bar()
hist.x_labels = range(1,7)
hist.add("D6",frequency)
hist.render_in_browser()





