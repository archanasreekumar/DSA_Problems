queue=[]
queue.append('a')
queue.append('b')
queue.append('c')
print(f'Queue is:{queue}')
print('Removing elements from queue:')
for i in range(len(queue)):
    print(f'First element: {queue.pop(0)}')
print(f'After removing all elements:{queue}')