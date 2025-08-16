from collections import deque

class SimpleQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        """Add item to the rear of the queue (O(1))."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return item from the front of the queue (O(1))."""
        if self.is_empty():
            return "Queue is empty!"
        return self.queue.popleft()

    def peek(self):
        """View front item without removing it."""
        if self.is_empty():
            return "Queue is empty!"
        return self.queue[0]

    def is_empty(self):
        """Check if queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return number of items in the queue."""
        return len(self.queue)

    def display(self):
        """Print the queue from front to rear."""
        print("Queue:", list(self.queue))


# Example usage:
q = SimpleQueue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.display()

print("Dequeued:", q.dequeue())
q.display()

print("Front item:", q.peek())
