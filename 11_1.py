# Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number of lines that
# matched the regular expression:

import re

regex = input("Enter a regular expression:")

fhand = open('mbox.txt')
linecount = 0

for line in fhand:
    line = line.rstrip()
    if re.search(regex, line):
        linecount += 1

print(fhand, 'had', linecount, 'lines that matched', regex)
