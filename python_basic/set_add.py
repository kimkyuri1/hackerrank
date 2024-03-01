# Read the number of country stamps
n = int(input())

# Create an empty set to store the country names
country_stamps = set()

# Read each country name and add it to the set
for _ in range(n):
    country = input().strip()
    country_stamps.add(country)

# Output the total number of distinct country stamps
print(len(country_stamps))
