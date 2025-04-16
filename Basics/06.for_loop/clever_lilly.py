age = int(input())
washing_machine_price = float(input())
toy_price = float(input())
money = 0

for year in range(1, age+1):
    if year % 2 == 0:
        money += 5 * year  # 2year -> 10, 4year -> 20, 6year -> 30...
        money -= 1.00  # stolen money
    else:
        money += toy_price
if money >= washing_machine_price:
    print(f"Yes! {(money - washing_machine_price):.2f}")
else:
    print(f"No! {(washing_machine_price - money):.2f}")
