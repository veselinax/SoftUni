budget = float(input())
price_1kg_floor = float(input())
cozonac_count = 0
colored_eggs = 0

price_eggs_1pack = price_1kg_floor * 0.75
price_milk_1l = price_1kg_floor + price_1kg_floor * 0.25
price_milk_250ml = (price_milk_1l * 250) / 1000 #Multiply the price by 250 (because you're looking for the price for 250 mL).
#Then, divide by 1000 (since 1 liter = 1000 mL) to scale it down to the 250 mL portion.

total_price = price_1kg_floor + price_milk_250ml + price_eggs_1pack
while budget > total_price:
    budget -= total_price
    cozonac_count +=1
    colored_eggs += 3
    if cozonac_count % 3 == 0:
        lost_eggs = cozonac_count - 2
        colored_eggs -= lost_eggs
print(f"You made {cozonac_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")