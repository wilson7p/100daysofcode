#Create a custom exception class and raise it in your code.
print ("\nWilson - Day 37 of #100DaysOfCode\n")
print("\ncustom exception class and raise it in your code.\n")

class CustomError(Exception):
  def __init__(self, message):
    super().__init__(message)

def example_function(number):
  if number<0:
    raise CustomError("negative numbers not allowed")

try:
  input = int(input("enter any number"))
  example_function(input)
except CustomError as ce:
  print(f"Custom error caught: {ce}")
