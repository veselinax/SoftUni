import math  # Import the math module for mathematical operations

# Read the input, which is a comma-separated string of numbers, and convert it into a list of integers
nums = list(map(int, input().split(', ')))

# Find the maximum number from the input list
max_num = max(nums)

# Calculate the number of groups we will need, where each group corresponds to numbers in a range of 10 (e.g., 1-10, 11-20, etc.)
groups_count = math.ceil(max_num / 10)

# Loop through each group, starting from 1 to the calculated number of groups
for group in range(1, groups_count + 1):
    group_nums = []  # Initialize an empty list to store numbers for the current group
    minimum = group * 10 - 10  # Calculate the minimum value for the current group (e.g., 0, 10, 20, ...)
    maximum = group * 10  # Calculate the maximum value for the current group (e.g., 10, 20, 30, ...)

    # Iterate through the list of numbers and check if they belong to the current group
    for num in nums:
        if minimum < num <= maximum:  # If the number is in the range (minimum, maximum]
            group_nums.append(num)  # Add it to the current group list

    # Print the current group with its numbers thats why the print is inside the loop so for next it resets with empty list and start again
    print(f"Group of {group * 10}'s: {group_nums}")
