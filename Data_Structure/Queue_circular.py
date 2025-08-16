class CicularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def isEmpty(self):
        return self.front == -1

    def enqueue(self, data):
        if self.isFull():
            print("Queue is full!")
            return
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data #enqueue always happen at rear

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        data = self.queue[self.front] #dequeue always happen from front
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return data

    def display(self):
        if self.isEmpty():
            print("Queue is empty, nothing to display")
            return
        i = self.front
        while True:
            print(self.queue[i], " ")
            if i == self.rear:
                break
            i = (i+1) % self.size


cq = CicularQueue(5)
cq.enqueue("a")
cq.enqueue("b")
cq.enqueue("c")
cq.display()
print(f"Removed value is {cq.dequeue()}")
cq.display()

