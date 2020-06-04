# Modify the program that prompts the user for the file name so that it prints a
# funny message when the user types in the exact file name "na na boo boo". The
# program should behave normally for all other files which exist and don't extist.

fileinput = input('Enter a file name: ')

try :
    file = open(fileinput)

except :
    if fileinput == "na na boo boo" :
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else :
        print("File cannot be opened:", fileinput)
    exit()

count = 0
total = 0

for line in file :
    str = line.startswith('X-DSPAM-Confidence:')
    if str == True :
        colon = line.find(':')
        numberstr = line[colon+1:]
        total += float(numberstr)
        count += 1

print("Average spam confidence: ", total/count)
