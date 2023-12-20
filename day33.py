#Create a class hierarchy for different shapes (circle, rectangle, triangle) and calculate their areas.
print ("\nWilson - Day 33 of #100DaysOfCode\n")
print("\nCreate a class hierarchy for different shapes and calculate their areas\n")

import math

class Shape:
  def area(self):
    pass

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
  def area(self):
    return math.pi * self.radius ** 2

class Rectangle(Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = width
  def area(self):
    return self.length * self.width

class Triangle(Shape):
  def __init__(self, base, height):
    self.base = base
    self.height = height
  def area(self):
    return 0.5 * self.base * self.height

def get_input(prompt): 
  value = int(input(prompt))
  if value<= 0:
    print("enter positive value")
  else:
    return value

def get_user_choice():
  print("select a shape: \n1.circle \n2.rectangle \n3.triangle")
  choice = int(input("enter one operation(1-3)"))

shape_choice = get_user_choice()

if shape_choice == 1:
  radius = get_input("radius: ")
  shape = Circle(radius)

elif shape_choice == 2:
  length = get_input("length: ")
  width = get_input("width: ")
  shape = Rectangle(length, width)

elif shape_choice == 3:
  base = get_input("base: ")
  height = get_input("height: ")
  shape = Triangle(base, height)

print(f"area of the chosen shape: {shape.area()}")
