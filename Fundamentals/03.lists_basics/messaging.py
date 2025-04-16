# Step 1: Read the input
numbers = input().split()  # First line: sequence of numbers as strings
text = input()  # Second line: string from which we'll form the message

# Step 2: Initialize an empty message
message = []

# Step 3: Process each number
for number in numbers:
    # Calculate the sum of digits of the number
    digit_sum = sum(int(digit) for digit in number)

    # Get the index for the character in the text
    index = digit_sum % len(text)  # Wrap around if the index is out of bounds

    # Find the character and add it to the message
    char = text[index]
    message.append(char)

    # Remove the character from the text
    text = text[:index] + text[index + 1:]

# Step 4: Join the message list and print the final message
print("".join(message))
