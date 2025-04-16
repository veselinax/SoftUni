import re

numbers = input()
pattern = "(\\+359-2-[0-9]{3}-[0-9]{4}|\\+359 2 [0-9]{3} [0-9]{4})"
valid_numbers = re.findall(pattern,numbers)
print(", ".join(valid_numbers))


