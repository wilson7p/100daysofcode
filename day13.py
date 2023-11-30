#Advanced list operations
print("\nWilson - Day 13 of 100DaysOfCode")
print("\nAdvanced list operations")

list = [1, 2, 3, 4, 5]
sq_list = [x**2 for x in list]
print("sqared list values = ",sq_list)
even = [x for x in sq_list if x % 2 == 0]
print("even numbers in squared list = ",even)
slice_list = sq_list[1:4]  
print("elements from given index", slice_list)
