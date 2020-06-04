# Encapsulate this code in a function named count, and generalise it so that it
# accepts the string and the letter as arguments.

def count(word, search):
    count = 0
    for letter in word:
        if letter == search:
            count += 1

    return count


word = 'banana'
letter = 'n'

print(count(word, letter))
