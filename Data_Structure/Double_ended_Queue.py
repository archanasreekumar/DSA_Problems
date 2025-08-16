from collections import deque

# Create deque
dq = deque()

# Add elements
dq.append(10)        # Add to right
dq.appendleft(5)     # Add to left
dq.append(15)

print("Deque:", dq)  # Deque: deque([5, 10, 15])

# Remove elements
dq.pop()             # Remove from right → 15
dq.popleft()         # Remove from left → 5

print("After pops:", dq)  # deque([10])

# Rotate (right shift by 1)
dq.extend([20, 30, 40])
dq.rotate(1)
print("After rotate:", dq)  # deque([40, 10, 20, 30])
