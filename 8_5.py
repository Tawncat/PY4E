# Write a program to read through the mail box data and when you find line that
# starts with "From", you will split the line into words using the split function.
# We are interested in who sent the message, which is the second word on the From line.

fname = input("Enter a file name: ")
fhand = open(fname)
#fhand = open('mbox-short.txt')
count = 0
for line in fhand :
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue

    if len(words) >= 3 :
        print(words[1])

    count = count + 1

print("There were", count, "lines in the file with From as the first word.")
