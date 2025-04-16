# Input: List of elements and the number k
elements = input().split()  # A string of space-separated elements
k = int(input())  # The number k

result = []  # List to store the order of elimination
index = 0  # Starting index

# While the list is not empty
while elements:
    # Calculate the index of the element to eliminate
    index = (index + k - 1) % len(elements)  # Modulo to handle circular indexing
    result.append(elements.pop(index))  # Remove the element and add to result

# Convert all elements to integers before printing
result = [int(i) for i in result]

# Output the result list as a string without spaces
print(f"[{','.join(map(str, result))}]")
#This takes the result list and converts each element to a string,\
# then joins them together with commas, effectively removing spaces.
