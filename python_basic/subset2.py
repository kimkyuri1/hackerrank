# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the elements of the first set
    n = int(input())
    set1 = set(map(int, input().split()))

    # Read the elements of the second set
    m = int(input())
    set2 = set(map(int, input().split()))

    # Check if set1 is a subset of set2
    if set1.issubset(set2):
        print("True")
    else:
        print("False")
