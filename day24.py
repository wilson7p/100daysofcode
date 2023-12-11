#Implement a function to check if a string is a palindrome.
print ("\nWilson - Day 24 of #100DaysOfCode\n") 
print("\ncheck if a string is a palindrome\n")

def is_palindrome(s):
  clean = ''.join(s.split()).lower()
  return clean == clean[::-1]
input = input("enter sting: ")
result = is_palindrome(input)
print(f'Is "{input}" a palindrome? {result}')


