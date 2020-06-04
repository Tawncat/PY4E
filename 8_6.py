# Rewrite the program that prompts the user for a list of numbers and prints out
# the maximum and minimum of the numbers at the end when the user enters "done".
# Write the program to store the numbers the user enters in a list and use the
# max() and min() functions to compute the maximum and minimum numbers after the loop co'mpletes.'

userNum = None
numbers = list()

while userNum != "done" :
    try :
        userNum = input("Enter a number: ")
        if userNum == "done" :
            pass
        else :
            numbers.append(int(userNum))

    except :
        print("Invalid Input")
        continue

print("Maximum is: ",max(numbers))
print("Minimum is: ",min(numbers))
