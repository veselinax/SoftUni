destination = input()

while destination != "End":
    min_budget = float(input())
    money = 0
    while money < min_budget:
        savings = float(input())
        money += savings
    print(f"Going to {destination}!")
    destination = input()


