# This program records the domain name (instead of the address) where the message
# was sent from instead of who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.

fhand = open('mbox-short.txt')
emails = dict()

for line in fhand :
    words = line.split()
    if len(words) == 0 or words[0] != 'From' or len(words) < 1 :
        continue

    for word in words :
        search = '@' in word
        if search == True :
            at = word.find('@')
            domain = word[at+1:]
            emails[domain] = emails.get(domain, 0) + 1


print(emails)
