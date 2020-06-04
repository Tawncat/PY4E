# Write a function called chop that takes a list and modifies it, removing the
# first and last elements and returns none. Then write a function called middle
# that takes a list and returns a nw list that contains all but the first and
# last elements.

def chop(t):
    del t[0]
    last = len(t) - 1
    del t[last]

def middle(t):
    last = len(t) - 1
    return t[1:last]

mylist = [0, 1, 2, 3, 4, 10]
print(mylist)
chop(mylist)
print(mylist)

secondlist = [56, 1, 2, 3, 4, 130]
modlist = middle(secondlist)
print(secondlist)
print(modlist)
