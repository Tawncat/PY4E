# Write a program that reads a file and prints the letters in decreasing order of
# frequency. Your program should convert all the input to lower case and only count
# the letters a-z. Your program should not count spaces, digits, punctuation, or
# anything other than the letters a-z.
import string

name = input("Enter file:")
if len(name) < 1 :
    name = "romeo.txt"
fhand = open(name)
chars = dict()

for line in fhand :
    line = line.translate(str.maketrans('','', string.punctuation)) # strip punctuation
    line = line.lower()
    words = line.split()

    if len(words) == 0 :
        continue

    # print(words)
    for word in words :
        letters = list(word)
        # print(letters)

        for letter in letters :
            check = letter.isdigit() #filters out digits
            if check == True :
                continue
            chars[letter] = chars.get(letter, 0) + 1

tmp = list()

for key, value in chars.items() :
    tmp.append((value, key))

tmp.sort(reverse=True)

for k, v in tmp :
    print(v, k)
