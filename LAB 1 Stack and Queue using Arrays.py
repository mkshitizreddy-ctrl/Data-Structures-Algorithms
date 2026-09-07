"""
Name: Kshitiz Reddy
Reg No: A26MTAI0008
Subject: Data Structure and Algorithms Lab
"""

# Stack using array (list)

class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = []

    def push(self, val):
        if len(self.arr) >= self.size:
            print("Stack Overflow")
            return
        self.arr.append(val)

    def pop(self):
        if len(self.arr) == 0:
            print("Stack Underflow")
            return
        return self.arr.pop()

    def peek(self):
        if len(self.arr) == 0:
            print("Stack is empty")
            return
        return self.arr[-1]

    def is_empty(self):
        return len(self.arr) == 0

    def display(self):
        print("Stack:", self.arr)


# Queue using array (list)

class Queue:
    def __init__(self, size):
        self.size = size
        self.arr = []

    def enqueue(self, val):
        if len(self.arr) >= self.size:
            print("Queue is full")
            return
        self.arr.append(val)

    def dequeue(self):
        if len(self.arr) == 0:
            print("Queue is empty")
            return
        return self.arr.pop(0)

    def front(self):
        if len(self.arr) == 0:
            print("Queue is empty")
            return
        return self.arr[0]

    def is_empty(self):
        return len(self.arr) == 0

    def display(self):
        print("Queue:", self.arr)


# ---- Main ----
if __name__ == "__main__":
    s = Stack(5)
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    print("Popped:", s.pop())
    s.display()

    q = Queue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.display()
    print("Dequeued:", q.dequeue())
    q.display()