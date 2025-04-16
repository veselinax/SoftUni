text = input()
result = []
strength = 0

for i in range(len(text)):
    if text[i] == '>':
        result.append(text[i])  # Always keep '>'
        strength += int(text[i + 1])  # Add strength from next character
    elif strength > 0:
        strength -= 1  # Skip this character (it's exploded)
    else:
        result.append(text[i])  # Keep normal characters

print(''.join(result))
