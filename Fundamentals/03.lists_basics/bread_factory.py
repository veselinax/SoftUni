# problem in judge
events = input().split("|")
energy = 100
coins = 100

for event in events:
    name, number = event.split("-")
    if name == "rest":
        if energy + int(number) <= 100:
            energy += int(number)
            gain = int(number)
        else:
            gain = 0
        print(f"You gained {gain} energy.")
        print(f"Current energy: {energy}.")
    elif name == "order":
        energy -= 30
        if energy >= 0:
            coins += int(number)
            print(f"You earned {int(number)} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        ingredient = name
        price = int(number)
        if coins >= price:
            coins -= price
        if coins <= 0:
            print(f"Closed! Cannot afford {ingredient}.")
            break
        else:
            print(f"You bought {ingredient}.")
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")


