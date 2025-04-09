# Input the list of numbers as a string, then convert it to a list of integers
some_lst = [int(x) for x in input().split()]

# Input the number of elements to remove
count = int(input())

# Remove the smallest 'count' elements from the list
for _ in range(count):
    min_value = min(some_lst)  # Find the smallest number in the list
    some_lst.remove(min_value)  # Remove that smallest number from the list

# Convert the remaining numbers to strings for output
some_lst = [str(x) for x in some_lst]  # so we can use join

# Print the remaining numbers as a space-separated string
print(", ".join(some_lst))
