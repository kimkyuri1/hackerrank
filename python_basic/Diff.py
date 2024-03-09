# Read the size of set a and the elements of set a
_ = input()  # Not needed
set_a = set(map(int, input().split()))

# Read the size of set b and the elements of set b
_ = input()  # Not needed
set_b = set(map(int, input().split()))

# Compute the symmetric difference
symmetric_difference = sorted(set_a ^ set_b)

# Print the symmetric difference
for num in symmetric_difference:
    print(num)
