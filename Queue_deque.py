from collections import deque

queue=deque()
queue.append('a')
queue.append('b')
queue.append('c')
print(f'Queue is {queue}')
for i in range(len(queue)):
    print(f'Queue elements are {queue.popleft()}')

print(f'After removing all elements:{queue}')