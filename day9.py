#Functions and function arguments
print ("\nWilson - Day 9 of #100DaysOfCode\n")
print("Functions and function arguments\n")
#functions
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet("Alice"))
print(greet(name="Bob", greeting="Hi"))  
print(greet("Charlie"))
#function arguments
def print_args(*args, **kwargs):
    print("\nPositional arguments:", args)
    print("Keyword arguments:", kwargs)
print_args(1, 2, 3, a="apple", b="banana")
