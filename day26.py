#Implement a recursive function to calculate the Fibonacci sequence
print ("\nWilson - Day 26 of #100DaysOfCode\n")
print("\nImplement a recursive function to calculate the Fibonacci sequence\n")

def fibonacci(n):
  if n <= 0:
    return "enter positive value"
  elif n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

values = int(input())
for i in range(1, values + 1):
  print(f"{i}: {fibonacci(i)}")

#Create a dictionary to store the names and ages of people
print("dictionary to store the names and ages of people")

people = {'wilson':21,'someone':21}
print(people)

#Write a program to find the common elements between two lists
print("common elements between two lists")

str1 = input("list 1 value separated by comma")
list1 = [int(x) for x in str1.split(',')]
str2 = input("list 2 value separated by comma")
list2 = [int(x) for x in str2.split(',')]

common = set(list1) & set(list2)

if common:
  print(f"common values: {list(common)}")
else:
  print("no common values found")
