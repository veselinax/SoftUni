import re

pattern = r"[0-9]+"  # raw string

while True:
    text = input()
    if not text:
        break
    matches = re.findall(pattern, text)
    for num in matches:
        print(num, end=" ")



