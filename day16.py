#Sets and set operations
print("\nWilson - Day 16 of 100DaysOfCode")
print("\nSets and set operations")

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
union = set1.union(set2)
print("union:",union)
intersection = set1.intersection(set2)
print("intersection:",intersection)
difference = set1.difference(set2)
print("difference:",difference)
symmetric_difference = set1.symmetric_difference(set2)
print("symmetric difference:",symmetric_difference)

