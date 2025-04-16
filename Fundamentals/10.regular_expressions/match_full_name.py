import re
names = input()
valid_names = re.findall("\\b[A-Z][a-z]+ [A-Z][a-z]+\\b",names)
print(" ".join(valid_names))

