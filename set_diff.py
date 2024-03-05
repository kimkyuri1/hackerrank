# Read inputs
_ = input()  # Number of students subscribed to English newspaper, not needed
english_subscribers = set(map(int, input().split()))
_ = input()  # Number of students subscribed to French newspaper, not needed
french_subscribers = set(map(int, input().split()))

# Calculate the number of students subscribed to English newspaper only
english_only_subscribers = len(english_subscribers - french_subscribers)

# Output the result
print(english_only_subscribers)
