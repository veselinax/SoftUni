wagons = int(input())
my_list = [0] * wagons

while True:
    command = input()
    if command == "End":
        break
    operation = command.split()
    if operation[0] == "add":
        people = int(operation[1])
        my_list[-1] += people
    elif operation[0] == "insert":
        index = int(operation[1])
        people = int(operation[2])
        my_list[index] += people
    elif operation[0] == "leave":
        index = int(operation[1])
        people = int(operation[2])
        my_list[index] -= people
print(my_list)

