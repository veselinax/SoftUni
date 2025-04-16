import re

text = input()
word = input()
pattern = rf"\b{word}\b"
words = re.findall(pattern, text, re.IGNORECASE)  # the search is not case-sensitive
print(words)
print(len(words))



