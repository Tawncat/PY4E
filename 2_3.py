# Write a program to prompt the user for hours and rate per hour to compute gross pay.
# Round to 2 decimal places

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = round(float(hours) * float(rate), 2)
print("Pay: ",pay)
