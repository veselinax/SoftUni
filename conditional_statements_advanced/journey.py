budget = float(input())
season = input()
journey = ""
destination = ""
price = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.30  # 30% of the budget
    else:
        price = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.40
    else:
        price = budget * 0.80
else:
    destination = "Europe"
    price = budget * 0.90
if season == "summer" and not destination == "Europe":
    journey = "Camp"
else:
    journey = "Hotel"

print(f"Somewhere in {destination}")
print(f"{journey} - {price:.2f}")

