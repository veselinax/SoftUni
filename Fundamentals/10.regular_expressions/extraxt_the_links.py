import re

pattern = r"www\.[a-zA-Z0-9\-]+(\.[a-z]+)+"

while True:
    line = input()
    if line == "":  # Stop when you enter an empty line
        break
    matches = re.findall(pattern, line)
    for match in re.finditer(pattern, line):
        print(match[0])


