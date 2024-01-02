#Write a program to find the intersection of two sets.
print ("\nWilson - Day 45 of #100DaysOfCode\n") 
print("\nprogram to find the intersection of two sets\n")

def fn_intersection(set1, set2):
    intersection = set1 & set2
    return intersection

set1 = input("enter value for set 1 separated by comma: ")
set2 = input("enter value for set 2 separated by comma: ")

result = fn_intersection(set1, set2)
print("Intersection of the sets:", result)
