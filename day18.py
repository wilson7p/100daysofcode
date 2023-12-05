#Decorators and closures
print("\nWilson - Day 18 of 100DaysOfCode")
print("\nDecorators and closures")

def my_decorator(func):
    def wrapper():
        print("BEFORE")
        func()
        print("AFTER")
    return wrapper

@my_decorator
def say_hello():
    print("WILSON")
say_hello()

