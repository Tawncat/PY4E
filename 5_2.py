# Write a program that prompts for a list of numbers and at the end prints out both
# the maximum and minimum of the numbers.

userNum = None
minimum = None
maximum = None

while userNum != "done" :
    try :
        userNum = input("Enter a number:")

        if minimum is None:
            minimum = int(userNum)
        if maximum is None:
            maximum = int(userNum)

        if userNum == "done" :
            pass
        elif int(userNum) > maximum :
            maximum = int(userNum)
        elif int(userNum) < minimum :
            minimum = int(userNum)

    except :
        print("Invalid input")
        continue

print("Maximum is",maximum)
print("Minimum is",minimum)
