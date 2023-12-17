#Write a program to find the intersection of two sets.
print ("\nWilson - Day 30 of #100DaysOfCode\n")
print("\nfind the intersection of two sets.\n")

def intersection(set1, set2):
  result = set1.intersection(set2)
  return result

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

result = intersection(set1,set2)
print(result)

#Read a text file and print its content to the console.
print("\nRead a text file and print its content to the console.")
file_path = 'sample.txt'
file = open(file_path,'r')
content = file.read()
print(content)
