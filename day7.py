#Dictionaries and dictionaries manipulation
print ("\nWilson - Day 7 of #100DaysOfCode\n")
print("\nDictionaries and dictionaries manipulation\n")

#creating a dictionary
student = {'name': 'wilson','age':21,'marks':{'maths':90,'computer':97,'english':89},'courses':['maths','computer','english']}
# Accessing dictionary values
print("Student Name:", student['name'])
print("Student Age:", student['age'])
print("Maths mark:", student['marks']['maths'])
print("courses:", ', '.join(student['courses']))

keys = student.keys()
values = student.values()

print("\nKeys:", keys)
print("Values:", values)
