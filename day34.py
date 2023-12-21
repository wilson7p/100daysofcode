#Write a program to demonstrate encapsulation in a class.
print ("\nWilson - Day 34 of #100DaysOfCode\n")
print("\nencapsulation in a class.\n")

class Person:
  def __init__(self,name,age):
    self.__name = name
    self.__age = age

  def get_name(self):
    return self.__name

  def get_age(self):
    return self.__age

  def set_name(self, new_name):
    if isinstance(new_name, str):
      self.__name = new_name
    else:
      print("enter string")

  def set_age(self, new_age):
    if isinstance(new_age, int) and new_age > 0:
      self.__age = new_age
    else:
      print("enter positive number")

person1 = Person(name="wilson", age=21)
print(f"name: {person1.get_name()}")
print(f"age: {person1.get_age()}")
