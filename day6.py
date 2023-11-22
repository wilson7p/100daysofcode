#working with tuples and sets
print ("\nWilson - Day 6 of #100DaysOfCode\n")
print("\nWorking with tuples and sets\n")

#tuples
fruits = ('apple','banana','cherry')
count_apple = fruits.count('apple')
index_banana = fruits.index('banana')
print("total number of apple in the tuple fruits is :",count_apple)
print("index of banana is: ",index_banana)

#sets
colours = {'red','green','purple'}
colours.add('white')
print("added white!",colours)
colours.remove('white')
print("removed white!",colours)

# Set operations (union, intersection, difference)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
print("union set: ",union_set)
print("intersection set: ",intersection_set)
print("difference set: ",difference_set)
