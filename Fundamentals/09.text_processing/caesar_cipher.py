string = input()
encrypted = ""
for word in string:
    for letter in word:
        encrypted += chr(ord(letter) + 3)
print(encrypted)