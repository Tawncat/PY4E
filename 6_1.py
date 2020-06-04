# Write a while loop that starts at the last character in the string and works its way
# backwards to the first character in the string, printing each letter on a separate
# line, except backwards.

fruit = 'watermelon'
length = len(fruit)

while length > 0:
    letter = fruit[length-1]
    print(letter)
    length -= 1
