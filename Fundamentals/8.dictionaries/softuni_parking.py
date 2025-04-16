n = int(input())
dictionary = {}

for i in range(n):
    command = input().split()
    if command[0] == "register":
        username = command[1]
        license_plate_number = command[2]
        if username in dictionary:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            dictionary[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif command[0] == "unregister":
        username = command[1]
        if username not in dictionary:
            print(f"ERROR: user {username} not found")
        else:
            dictionary.pop(username)   # removes the specific item from the dictionary
            print(f"{username} unregistered successfully")
for key,value in dictionary.items():
    print(f"{key} => {value}")