# Rewrite your pay computation with time-and-a-half for overtime and create a function
# called computepay which takes two parameters (hours and rate).

def computepay(hours, rate):
    if hours > 40 :
        bonus = rate * 1.5 * (hours - 40)
        pay = 40 * rate + bonus
        return pay
    else :
        pay = hours * rate
        return pay

try :
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except :
    print('Enter numbers only.')
    exit()

print('Pay:', computepay(hours, rate))
