#Write a program to find the factorial of a number using a for loop.
print ("\nWilson - Day 54 of #100DaysOfCode\n") 
print("\nprogram to find the factorial of a number using a for loop\n")

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = int(input("Enter a number: "))
if num < 0:
    print("enter positive number")
elif num == 0:
    print("factorial of 0 is 1")
else:
    print(f"factorial of {num} is {factorial(num)}")

#Write a program to implement a priority queue.

class PriorityQueue:
    def __init__(self):
        self.queue = []
    def push(self, item, priority):
        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])
    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)[0]
        else:
            raise IndexError("pop from an empty priority queue")
    def is_empty(self):
        return len(self.queue) == 0

priority_queue = PriorityQueue()
priority_queue.push("Task 1", 3)
priority_queue.push("Task 2", 1)
priority_queue.push("Task 3", 2)
while not priority_queue.is_empty():
    print(priority_queue.pop())
