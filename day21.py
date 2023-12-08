print("\nWilson - Day 21 of 100DaysOfCode")
#Implement a program to check if a year is a leap year using if-else statements.
print("\nleap year using if-else statements.")

def leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
check = int(input("Enter a year: "))

if leap(check):
    print(f"{check} is a leap year.")
else:
    print(f"{check} is not a leap year.")
