#Write a program to implement a simple queue.
print ("\nWilson - Day 48 of #100DaysOfCode\n") 
print("\nProgram to implement a simple queue\n")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return dequeued_item
        else:
            raise IndexError("cannot dequeue from an empty queue")

    def size(self):
        current = self.front
        count = 0
        while current:
            count += 1
            current = current.next
        return count

my_queue = Queue()

my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

print("size of the queue:", my_queue.size())
dequeued_item = my_queue.dequeue()
print("dequeued item:", dequeued_item)
print("size of the queue after dequeue:", my_queue.size())
