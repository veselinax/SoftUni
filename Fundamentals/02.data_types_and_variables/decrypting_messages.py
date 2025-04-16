key = int(input())
n = int(input())
res = ""
for i in range(n):
    letter = input()
    message = (ord(letter) + key)   # ascii code number + added key  (int)
    res += chr(message)   # the symbol of that ascii code number and concatenating the result (we can concatenate strings)

print(res)
