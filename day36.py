#Write a program that handles exceptions for division by zero.
print ("\nWilson - Day 36 of #100DaysOfCode\n")
print("\nhandles exceptions for division by zero.\n")

def divide(a, b):
  try:
    result = a / b
    print(f"{a} / {b} = {result}")
  except ZeroDivisionError:
    print("diving by zero not allowed")
  
numerator = int(input("numerator: "))
dinominator = int(input("dinominator: ")) 

divide(numerator, dinominator)

