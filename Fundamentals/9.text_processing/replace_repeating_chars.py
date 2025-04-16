string = input()
new_string = string[0]  # Start with the first character

for i in range(1, len(string)):
    if string[i] != string[i - 1]:  # Only add if different from the previous character
        new_string += string[i]

print(new_string)
