products = {}
command = input()

while command != "statistics":
    tokens = command.split(": ")
    product = tokens[0]
    quantity = int(tokens[1])
    if product not in products:
        products[product] = 0  # a check if the product is not already in the dictionary and set its value to 0\
        # That way we make sure that the product will exist before we add the quantity
    products[product] += quantity # Then we add up the quantity
    command = input()
print("Products in stock: ")
for (product, quantity) in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")

