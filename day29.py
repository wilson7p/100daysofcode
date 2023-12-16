#Create a set and perform various set operations (union, intersection, etc.)
print ("\nWilson - Day 29 of #100DaysOfCode\n")
print("\nperform various set operations\n")

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

union = set1.union(set2)
print("union: ", union)

intersection = set1.intersection(set2)
print("intersection: ",intersection)

difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)
print("difference of set1 and set2: ", difference_set1)
print("difference of set2 and set1: ", difference_set2)

symmetric_difference = set1.symmetric_difference(set2)
print("symmetric_difference: ",symmetric_difference)

subset = set1.issubset(set2)
print("check wether set1 subset of set2:",subset)

disjoint = set1.isdisjoint(set2)
print("check wether set1 and set2 are disjoint:", disjoint)
