import heapq


class MaximumPriorityQueue:
    def __init__(self):
        self.maxheap = []

    def push(self, item, priority):
        heapq.heappush(self.maxheap, (-priority, item))

    def pop(self):
        if self.maxheap:
            priority, item = heapq.heappop(self.maxheap)
            return item

    def not_empty(self):
        return len(self.maxheap)


if __name__ == "__main__":
    maxpq = MaximumPriorityQueue()
    maxpq.push("A", 3)
    maxpq.push("B", 1)
    maxpq.push("C", 5)

    while maxpq.not_empty():
        print(maxpq.pop())
