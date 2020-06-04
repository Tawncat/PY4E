# Wrewrite the guardian code without two if statements. Use a compound logical
# expression using the or operator with a single if statement.


fhand = open('8_2.txt')

for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words) == 0 or words[0] != 'From' or len(words) < 3:
        continue

    print(words[2])
