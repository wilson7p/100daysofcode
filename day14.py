#Deep dive into dictionaries
print("\nWilson - Day 14 of 100DaysOfCode")
print("\nDeep dive into dictionaries")

person = {
    'name': 'Wilson',
    'age': 20,
    'address': {
        'street': '123 street',
        'city': 'nowhere',
        'zipcode': '12345'
    },
    'hobbies': ['Music', 'Youtube', 'Coding']
}

print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"Street: {person['address']['street']}")
print(f"City: {person['address']['city']}")
print(f"Zipcode: {person['address']['zipcode']}")
print(f"Hobbies: {', '.join(person['hobbies'])}")

person['age'] = 21
print(f"Modified Age: {person['age']}")
person['occupation'] = 'Software Developer'
print(f"Occupation: {person['occupation']}")

print(f"Keys: {person.keys()}")
print(f"Values: {person.values()}")
print(f"Items: {person.items()}")

print("Iterating: ")
for key, value in person.items():
    print(f"{key}: {value}")

squared_numbers = {x: x*x for x in range(1, 6)}
print(f"Squared Numbers: {squared_numbers}")


