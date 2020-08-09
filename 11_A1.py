# Read through and parse a file with text and numbers. Extract all the numbers
# in the file and compute then sum of those numbers.

import re

filename = input('Enter file:')
fhand = open(filename)
numlist = list()

for line in fhand:
    line = line.rstrip()
    matches = re.findall('[0-9]+', line)

    if len(matches) > 0:
        for line in matches:
            numlist.append(int(line))

print(sum(numlist))
