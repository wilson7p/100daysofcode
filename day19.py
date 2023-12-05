#Basic Calculator
print("\nWilson - Day 19 of 100DaysOfCode")
print("\n#Implement a basic calculator program using a menu-driven approach ")

def add(x, y):
  return x + y
def sub(x, y):
  return x - y
def mul(x, y):
  return x * y
def div(x, y):
  if y != 0:
    return x / y
  else:
    return "cannot divide by zero"

while True:
  print("Calculatr menu: ")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")

  choice = input("Enter you type of calculation (1,2,3,4,5)")
  if choice == '5':
    print("Exiting calculator")
    break

  num1 = float(input("value 1:"))
  num2 = float(input("value 2:"))
  
  if choice == '1':
    result = add(num1,num2)
  elif choice == '2':
    result = sub(num1,num2)
  elif choice == '3':
    result = mul(num1,num2)
  elif choice == '4':
    result = div(num1,num2)  
  else:
    print("enter value from the menu")
    continue
  print("Result: ",result)
