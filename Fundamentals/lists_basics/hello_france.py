# wrong in judge
items = input().split("|")
budget = float(input())
prices = []
value_sum = 0

for item in items:
    name, value = item.split("->")
    value = float(value)
    if name == "Clothes" and value < 50.00:
        if budget >= value:
            budget -= value
            value_sum += value
            new_price =round(value + value * 0.40,2)
            prices.append(new_price)
    if name == "Shoes" and value < 35.00:
        if budget >= value:
            budget -= value
            value_sum += value
            new_price = round(value + value * 0.40, 2)
            prices.append(new_price)
    if name == "Accessories" and value < 20.50:
        if budget >= value:
            budget -= value
            value_sum += value
            new_price = round(value + value * 0.40, 2)
            prices.append(new_price)
profit = sum(prices) - value_sum
budget += sum(prices)
prices = [str(x) for x in prices]
print(" ".join(prices))
print(f"Profit: {profit:.2f}")
if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")





