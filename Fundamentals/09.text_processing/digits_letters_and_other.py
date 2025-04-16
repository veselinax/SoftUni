string = input()
digits = ""
letters = ""
symbols = ""
for letter in string:
    if letter.isdigit():
        digits += letter
    elif letter.isalpha():
        letters += letter
    else:
        symbols += letter

print(digits)
print(letters)
print(symbols)