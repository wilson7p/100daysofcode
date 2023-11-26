#Scope and lifetime of variables
print("\nWilson - Day 10 of 100DaysOfCode")
print("\nScope and lifetime of variables")

total_sum = 0
def totalfun(value):
    global total_sum
    total_sum += value
    print(f"Inside the function - Added {value} to total_sum. New total_sum: {total_sum}")
totalfun(5)
totalfun(10)
totalfun(8)
print(f"Outside the function - Final total_sum: {total_sum}")
