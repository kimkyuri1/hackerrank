def print_formatted(number):
    # Calculate the width of the binary representation of 'number'
    width = len(bin(number)) - 2

    # Print formatted values for each integer from 1 to 'number'
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]

        # Print formatted values with appropriate padding
        print(f"{decimal.rjust(width)} {octal.rjust(width)} {hexadecimal.rjust(width)} {binary.rjust(width)}")

# Read input
n = int(input("Enter the maximum value to print: "))

# Call the function with the input value
print_formatted(n)
