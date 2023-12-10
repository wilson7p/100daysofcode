#Implement a function to find the LCM (Least Common Multiple) of two numbers.
print ("\nWilson - Day 23 of #100DaysOfCode\n") 
print("\nfunction to find the LCM of two numbers\n")

def gcd(a, b):
  while b:
    a, b=b, a%b 
    return a
def lcm(a,b):
  return abs(a * b) // gcd(a, b)

num1 = int(input("enter valu1:"))
num2 = int(input("enter value2:"))
result = lcm(num1, num2)
print(f"LCM of {num1} and {num2} is {result}")

#Create a function to generate a list of prime numbers up to a given limit.
print("\ngenerate a list of prime numbers up to a given limit\n")

def isPrime(n):
  if(n==1 or n==0):
    return False
  for i in range(2,n):
    if(n%i==0):
      return False
  return True

N = int(input("enter range: "))
for i in range(1,N+1):
  if(isPrime(i)):
    print(i,end=" ")
