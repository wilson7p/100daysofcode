#Write a function to find the median of a list of numbers
print ("\nWilson - Day 25 of #100DaysOfCode\n")
print("\nmedian of a list of numbers\n")

def median(numbers):
  sort = sorted(numbers)
  n = len(sort)

  if n % 2 == 0:
    left = sort[(n//2) - 1]
    right = sort[(n//2)]
    medianvalue = (left + right) / 2
  else:
    medianvalue = sort[n//2]
  return medianvalue

numbers = [1,2,3,4,5,6,7,8,9,10]
result = median(numbers)
print("Median:", result)
