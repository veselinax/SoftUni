whiskey_price = float(input())
beer = float(input())
wine = float(input())
rakija = float(input())
whiskey = float(input())

rakija_price = whiskey_price / 2
wine_price = rakija_price - (rakija_price * 0.40)  # 40% less means New Price=Original Price−(Original Price×0.40)
beer_price = rakija_price - (rakija_price * 0.80)

total_price = rakija_price * rakija + whiskey_price * whiskey + wine_price * wine + beer_price * beer
print(f"{total_price:.2f}")
