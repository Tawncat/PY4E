# Rewrite your pay computation to give the employee 1.5 times the hourly rate for
# hours worked above 40 hours.

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
bonus = 0

if hours > 40 :
    bonus = rate * 1.5 * (hours - 40)
    pay = 40 * rate + bonus
else :
    pay = hours * rate

print('Pay:', pay)
