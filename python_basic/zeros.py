import numpy as np

# Read input
shape = tuple(map(int, input().split()))

# Create arrays using numpy.zeros and numpy.ones
zeros_array = np.zeros(shape, dtype=int)
ones_array = np.ones(shape, dtype=int)

# Print the arrays
print(zeros_array)
print(ones_array)

