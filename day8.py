#Control flow (if statements, loops)
print ("\nWilson - Day 8 of #100DaysOfCode\n")
print("\nControl flow (if statements, loops)\n")

#if statements
a=10
if a>5:
  print("a is greater than 5")
elif a>10:
  print("a is greater than 10")
else:
  print("a is not greater than 5 or 10")

#for loop
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)

#while loop
num = 0
while num < 10:
    if num == 5:
        break
    print(num)
    num += 1
