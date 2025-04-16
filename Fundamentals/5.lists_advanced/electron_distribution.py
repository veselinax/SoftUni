num = int(input())
result = []
counter = 1
while num > 0:  # Keep looping as long as num is greater than 0
    add_num = 2 * counter ** 2  # Calculate the number to add to the result: 2 times the square of the counter
    if add_num > num:  # If the calculated number is greater than the remaining num
        add_num = num  # Set add_num to be equal to num (if we can't add more than what's left)

    result.append(add_num)  # Append the calculated number to the result list
    num -= add_num  # Subtract the added number from num, reducing it
    counter += 1  # Increment the counter for the next iteration

print(result)  # Print the final list of numbers