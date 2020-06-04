# Rewrite your pay program using try and except so that your program handles non-numeric
# input gracefully by printing a message and exiting the program.

try :
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except :
    print('Enter numbers only.')
    exit()

bonus = 0

if hours > 40 :
    bonus = rate * 1.5 * (hours - 40)
    pay = 40 * rate + bonus
else :
    pay = hours * rate

print('Pay:', pay)
