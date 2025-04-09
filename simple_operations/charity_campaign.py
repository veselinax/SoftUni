campaign_days_count = int(input())
chefs_count = int(input())
cakes_count = int(input())
waffles_count = int(input())
pancakes_count = int(input())

cake_price = cakes_count * 45
waffle_price = waffles_count * 5.80
pancake_price = pancakes_count * 3.20
price = (cake_price + waffle_price + pancake_price) * chefs_count #daily price
total_price = price * campaign_days_count #price for whole campaign
final_price = total_price - (total_price / 8) # price - expenses ( 1/8 from the price is the price/8)
print(f"{final_price:.2f}")