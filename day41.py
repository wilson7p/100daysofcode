#Use regular expressions to validate email addresses.
print("\nWilson - Day 41 of #100DaysOfCode\n")
print("\nregular expressions to validate email addresses.")

import re

def isvalid(email):
  pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  match = re.match(pattern, email)
  return bool(match)

inputemail = input("enter your email")
if isvalid(inputemail):
  print(f"{inputemail} is a valid email address")
else:
  print(f"{inputemail} is a not valid email address")
