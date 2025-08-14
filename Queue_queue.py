from queue import Queue

q=Queue(maxsize=3)
print(f'Size of queue is: {q.qsize()}')
q.put('a')
q.put('b')
q.put('c')
print(q.full())
print(q.get())
print(q.get())
print(q.get())
print(q.empty())