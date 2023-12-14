#Implement a stack data structure using a list
print ("\nWilson - Day 27 of #100DaysOfCode\n") 
print("\nImplement a stack data structure using a list\n")

class Stack:
  def __init__(self):
    self.items =[]
  def is_empty(self):
    return len(self.items) == 0
  def push(self,item):
    self.items.append(item)
  def pop(self):
    if not self.is_empty():
      return self.items.pop()
    else:
      raise IndexError("pop from empty stack")
  def peek(self):
    if not self.is_empty():
      return self.items[-1]
    else:
      raise IndexError("peek from empty stack")
  def size(self):
    return len(self.items)

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("stack: ", my_stack.items)
print("pop: ",my_stack.pop())
print("after pop:",my_stack.items)
print("peek: ",my_stack.peek())
print("is the stack empty?", my_stack.is_empty())
print("size of the stack: ",my_stack.size())
