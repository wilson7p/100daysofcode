#Handle file-related exceptions while reading or writing files.
print ("\nWilson - Day 38 of #100DaysOfCode\n") 
print("\nHandle file-related exceptions while reading or writing files\n")

import os

def read_file(filename):
  try:
    with open(filename, "r") as file:
      content = file.read()
    print(content)
  except FileNotFoundError:
    print("file not found")
  except PermissionError:
    print("permission denied")
  except Exception as e:
    print(f"error : {e}")

def write_file(filename, contents):
  try:
    with open(filename, "w") as file:
      file.write(contents)
    print("write successfull")
  except PermissionError:
    print("permission denied")
  except Exception as e:
    print(f"error : {e}")

read_file("day38.txt")
write_file("day38op.txt", "im wilson")
