
import numpy as np

# Read the input line containing space-separated integers
input_line = input()

# Split the input line into individual integers and convert them to integers
numbers = list(map(int, input_line.split()))

# Convert the list of numbers into a 3x3 NumPy array
array_3x3 = np.array(numbers).reshape(3, 3)

# Print the 3x3 NumPy array
print(array_3x3)
