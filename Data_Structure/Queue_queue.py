from queue import Queue

# Create a queue with optional max size
q = Queue(maxsize=5)

# Enqueue (put) items
q.put("A")
q.put("B")
q.put("C")

print("Queue size:", q.qsize())  # Number of items

# Peek is not directly available in Queue, but you can get without removing (by removing and adding back)
# However, in interviews, you can say Queue doesn't have a direct peek method for thread safety.

# Dequeue (get) items
print("Dequeued:", q.get())
print("Dequeued:", q.get())

# Check if queue is empty
print("Is queue empty?", q.empty())

# Enqueue more
q.put("D")
q.put("E")
q.put("F")

# Remove remaining items
while not q.empty():
    print("Dequeued:", q.get())

print("Is queue empty now?", q.empty())
