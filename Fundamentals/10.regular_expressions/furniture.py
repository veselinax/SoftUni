import re

pattern = r">>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)"
furniture = []
total_cost = 0.0

while True:
    line = input()
    if line == "Purchase":
        break

    match = re.match(pattern, line)
    if match:
        name = match[1]              # Furniture name  (match[0] is the whole match)
        price = float(match[2])      # Full price (match[3] is just the decimal part (like .00))
        quantity = int(match[4])     # Quantity
        furniture.append(name)
        total_cost += price * quantity

print("Bought furniture:")
for item in furniture:
    print(item)
print(f"Total money spend: {total_cost:.2f}")



