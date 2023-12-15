#Write a program to count the frequency of elements in a list using a dictionary
print ("\nWilson - Day 28 of #100DaysOfCode\n") 
print("\ncount the frequency of elements in a list using a dictionary\n")

def CountFrequency(list):
  freq = {}
  for item in list:
    if(item in freq):
      freq[item] += 1
    else:
      freq[item] = 1

  for key, value in freq.items():
    print("% d : % d" % (key, value))

if __name__ == "__main__":
  list = ['a','a','b','c','d','c','e','a','f']
  CountFrequency(list)

