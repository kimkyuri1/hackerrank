import cmath

# Read the complex number
z = complex(input())

# Calculate the polar coordinates
r = abs(z)
phi = cmath.phase(z)

# Print the polar coordinates
print(round(r, 3))
print(round(phi, 3))
