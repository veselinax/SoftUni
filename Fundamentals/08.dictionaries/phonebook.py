dictionary = {}

while True:
    command = input().split("-")
    if command[0].isdigit():
        n = int(command[0])
        break
    name = command[0]
    number = command[1]
    dictionary[name] = number
for i in range(n):
    name = input()
    if name not in dictionary:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {dictionary[name]}")
