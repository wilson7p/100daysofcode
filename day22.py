#Create a function to calculate the area of a rectangle.
print("\nWilson - Day 21 of 100DaysOfCode")
print("\nCalculate the area of a rectangle")

def rarea():
    length = float(input("enter length: "))
    width = float(input("enter width: "))
    area = length * width
    return area

result = rarea()
print(f"The area of the rectangle is: {result}")

#Write a function to check if a number is a perfect square.
print("\n check perfect square")
def is_square(number):
  if number < 0:
    return False
  sqrt = int(number ** 0.5)
  return sqrt ** 2 == number

input = float(input("enter a number:"))
sqresult = is_square(input)

if result:
  print(f"{input} is a perfect square")
else:
  print(f"{input} is not a perfect square")
