# Receive input
input_str = input().split(", ")  # For example: "1, 0, 2, 0, 3, 0, 4"
numbers = [int(x) for x in input_str]  # Convert to list of integers

# Create a list with non-zero elements
non_zero_numbers = [num for num in numbers if num != 0]

# Count the zeros
zero_count = numbers.count(0)

# Add the zeros to the end of the list
result = non_zero_numbers + [0] * zero_count

# Print the result
print(result)


