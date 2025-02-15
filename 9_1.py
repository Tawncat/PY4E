# Write a program that reads the words in words.txt and stores them as keys in a
# dictionary. It doesn’t matter what the values are. Then you can use the in operator
# as a fast way to check whether a string is in the dictionary.

fhand = open('words.txt')

words = dict()

for line in fhand :
    word = line.split()
    for eachword in word :
        if eachword not in words :
            words[eachword] = 1
        else :
            words[eachword] += 1

print(words)
