# Write a program to prompt for a file name, and then read through the file and
# look for lines of the form: X-DSPAM-Confidence: 0.8475. When you encounter that line
# pull it apart to extract the floating-point number on the line. Count these lines
# and then compute the total of spam confidence values from these lines. Print out the
# average spam confidence.

fileinput = input('Enter a file name: ')
file = open(fileinput)

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
