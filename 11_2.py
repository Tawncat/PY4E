# Write a program to look for lines of the form: New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() method.
# Compute the average of the numbers and print out the average as an integer.

import re

filename = input('Enter file:')
fhand = open(filename)
numlist = list()

for line in fhand:
    line = line.rstrip()
    matches = re.findall('^New Revision: ([0-9.]+)', line)

    if len(matches) > 0:
        for line in matches:
            numlist.append(int(line))


print(int(sum(numlist)/len(numlist)))
