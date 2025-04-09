visit_days = int(input())
room_type = input()
review = input()
nights = visit_days - 1
price = 0
discount = 0
if room_type == "room for one person":
    price = 18.00
elif room_type == "apartment":
    price = 25.00
    if nights < 10:
        price -= price * 0.30    # 30% discount
    elif 10<= nights <= 15:
        price -= price *0.35
    else:
        price -= price *0.50
elif room_type == "president apartment":
    price = 35.00
    if nights < 10:
        price -= price * 0.10
    elif 10<= nights <= 15:
        price -= price *0.15
    else:
        price -= price *0.20
cost = price * nights
if review == "positive":
    cost += cost * 0.25    # adding 25% of the price
else:
    cost -= cost * 0.10    # drop 10% of the price
print(f"{cost:.2f}")
