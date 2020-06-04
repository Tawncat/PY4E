# Add code to the previous program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created, look through
# the dictionary using a maximum loop to find who has the most messages and print
# how many messages the person has.

fhand = open('mbox-short.txt')
emails = dict()

for line in fhand :
    words = line.split()
    if len(words) == 0 or words[0] != 'From' or len(words) < 1 :
        continue

    emails[words[1]] = emails.get(words[1], 0) + 1

highest = 0
email = ''
for key in emails :
    if emails[key] > highest :
        highest = emails[key]
        email = key
print(emails)
print(highest, email)
