# Figure out which line of the program is still not properly guarded.
# Contruct a text file which causes the program to fail and modify the program so
# the line is properly guarded.

fhand = open('8_2.txt')

for line in fhand:
    words = line.split()
    print('Debug:', words)
    if len(words) == 0 :
        continue
    if words[0] != 'From' :
        continue
    if len(words) >= 3 :
        print(words[2])
