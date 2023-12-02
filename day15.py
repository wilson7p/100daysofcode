#loops
print("\nWilson - Day 15 of 100DaysOfCode")
print("\nloops")

#while loop
input = 1
while input <= 10:
     print(input)
     input +=1

#for loop
pets = ['dog', 'cat', 'monkey', 'fish', 'snake']
for pet in pets:
    print(pet)
for index, value in enumerate(pets):
    print(f'{index}:{value}')
print(max(pets))
print(min(pets))
print(sum(range(1, 4)))

