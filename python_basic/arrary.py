import numpy as np

# Read the input numbers and split them into a list
numbers = input().split()

# Convert the numbers into a NumPy array of type float
numbers_array = np.array(numbers, dtype=float)

# Reverse the array
reversed_array = np.flip(numbers_array)

# Print the reversed array
print(reversed_array)
