order = input()
amount = int(input())

def orders(item, quantity):
    if item == "coffee":
        price = 1.50 * quantity
    elif item == "water":
        price = 1.00 * quantity
    elif item == "coke":
        price = 1.40 * quantity
    elif item == "snacks":
        price = 2.00 * quantity
    return price

print(f"{orders(order,amount):.2f}")


