chars = input().split(", ")
ascii_dict = {}

for char in chars:
    ascii_dict[char] = ord(char)    # ascii_dict = {char: ord(char) for char in chars}

print(ascii_dict)