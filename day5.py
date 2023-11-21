#Area of a triangle  
print ("\nWilson - Day 5 of #100DaysOfCode\n")
print("\narea of a triangle \n")

a = int(input("Length 1 :"))
b = int(input("Length 2 :"))
c = int(input("Length 3 :"))
P = (a+b+c)
s = P/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("area :",area)
print("perimeter :",P)
print("semi perimeter :",s)
