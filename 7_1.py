# Write a program to read through a file and print the contents of the file(line by line)
# all in uppercase.

fileinput = input('Enter a file name: ')
file = open(fileinput)

for line in file :
    line = line.upper()
    line = line.rstrip()
    print(line)
