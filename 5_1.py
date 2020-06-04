# Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is enetred, print out the total, count and average of the numbers.
# If the user enters anything other than a number, detect their mistake usinf try and except
# and print an error message and skip to the next number.

userNum = None
total = 0
count = 0
average = 0

while userNum != "done" :
    try :
        userNum = input("Enter a number:")

        if userNum == "done" :
            average = total/count
        else :
            userNum = int(userNum)
            count += 1
            total += userNum
    except :
        print("Invalid input")
        continue

print(total, count, average)
