budget = int(input())
season = input()
fisherman_count = int(input())
price = 0


if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
else:
    price = 2600
if fisherman_count <= 6:
    price -= price * 0.10    # 10% discount
elif 7 <= fisherman_count <= 11:
    price -= price * 0.15  # 15% discount
else:
    price -= price * 0.25 # 25% discount

if (fisherman_count % 2 == 0) and not season == "Autumn":
    price -= price * 0.05  # 5% discount if fishermen are even number except when season is autumn

if price <= budget:
    print(f"Yes! You have {(budget-price):.2f} leva left.")
else:
    print(f"Not enough money! You need {(price-budget):.2f} leva.")