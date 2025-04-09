month = input()
nights = int(input())
price_studio = 0
price_apartment = 0
discount = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
    if 7 < nights < 14:
        price_studio -= price_studio * 0.05  #За студио, при повече от 7 нощувки през май и октомври : 5% намаление
    if nights > 14:
        price_studio -= price_studio *0.30
elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if nights > 14:
        price_studio -= price_studio *0.20
else:
    price_studio = 76
    price_apartment = 77
if nights > 14:
    price_apartment -= price_apartment * 0.10

print(f"Apartment: {(price_apartment * nights):.2f} lv.")
print(f"Studio: {(price_studio * nights):.2f} lv.")