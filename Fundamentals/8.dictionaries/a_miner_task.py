dictionary = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource in dictionary:
        dictionary[resource] += quantity # if it exists increase the quantity
    else:
        dictionary[resource] = quantity # if it doesn't exist - create it
for key,value in dictionary.items():
    print(f"{key} -> {value}")

