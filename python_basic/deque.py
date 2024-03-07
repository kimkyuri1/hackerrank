from collections import deque

# Read the number of operations
n = int(input())

# Create an empty deque
my_deque = deque()

# Iterate through each operation
for _ in range(n):
    operation, *values = input().split()
    
    # Perform the specified operation
    if operation == 'append':
        my_deque.append(*values)
    elif operation == 'appendleft':
        my_deque.appendleft(*values)
    elif operation == 'pop':
        my_deque.pop()
    elif operation == 'popleft':
        my_deque.popleft()

# Print the elements of deque
print(*my_deque)
