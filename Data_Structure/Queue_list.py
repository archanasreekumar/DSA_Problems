class SimpleQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Add an item to the end of the queue (O(1) in average case)."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue (O(n) in list)."""
        if self.is_empty():
            return "Queue is empty!"
        return self.queue.pop(0)

    def peek(self):
        """View the front item without removing it."""
        if self.is_empty():
            return "Queue is empty!"
        return self.queue[0]

    def is_empty(self):
        """Check if queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)

    def display(self):
        """Print the queue from front to rear."""
        print("Queue:", self.queue)


# Example usage:
q = SimpleQueue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.display()

print("Dequeued:", q.dequeue())
q.display()

print("Front item:", q.peek())
