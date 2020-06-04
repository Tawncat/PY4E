# Read and parse the “From” lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating
# a list of (count, email) tuples from the dictionary. Then sort the list in reverse
# order and print out the person who has the most commits.

fhand = open('mbox-short.txt')
emails = dict()

for line in fhand :
    words = line.split()

    if len(words) == 0 or words[0] != 'From' or len(words) < 1 :
        continue

    emails[words[1]] = emails.get(words[1], 0) + 1


lst = list()
for k, v in list(emails.items()) :
    lst.append((v, k))

lst.sort(reverse=True)

for k, v in lst[:1] :
    print(v, k)
