# Write a program that categorizes each mail message by which day of the week the
# commit was done. To do this look for lines that start with “From”, then look for
# the third word and keep a running count of each of the days of the week.
# At the end of the program print out the contents of your dictionary (order does not matter).

fhand = open('mbox-short.txt')
days = dict()

for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From' or len(words) < 2 :
        continue

    days[words[2]] = days.get(words[2], 0) + 1

print(days)
