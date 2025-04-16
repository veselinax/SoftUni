products = {}

while True:
    command = input().split()
    if command[0] == "buy":
        break

    name = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if name not in products:
        products[name] = [price, quantity]  # store price and quantity
    else:
        products[name][1] += quantity       # update quantity [1]
        products[name][0] = price           # replace price [0] if different

# Print total cost for each product
for name, (price, quantity) in products.items():
    total = price * quantity
    print(f"{name} -> {total:.2f}")
