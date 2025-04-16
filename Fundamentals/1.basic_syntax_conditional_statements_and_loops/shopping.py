budget = int(input())
spending = 0

command = input()
while command != "End":
    price = int(command)
    spending += price
    if spending > budget:
        print("You went in overdraft!")
        break
    command = input()
if command == "End":       # else:
    print("You bought everything needed.")

