strings = input().split()
res = ""
for string in strings:
    res += string * len(string)
print(res)