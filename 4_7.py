# Rewrite the grade program using a function called computegrade that takes a
# score as its parameter and returns a grade as a string.

def computegrade(score):
    if score < 0 or score > 1 :
        return 'Bad score'
    elif score >= 0.9 :
        return 'A'
    elif score >= 0.8 :
        return 'B'
    elif score >= 0.7 :
        return 'C'
    elif score >= 0.6 :
        return 'D'
    else :
        return 'F'

try :
    score = float(input('Enter score: '))

except:
    score = -1

print(computegrade(score))
