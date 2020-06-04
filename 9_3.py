# Write a program to read through a mail log, build a histogram using a dictionary
# to count how many messages have come from each email address, and print the dictionary.

fhand = open('mbox-short.txt')
emails = dict()

for line in fhand :
    words = line.split()
    if len(words) == 0 or words[0] != 'From' or len(words) < 1 :
        continue

    emails[words[1]] = emails.get(words[1], 0) + 1

print(emails)
