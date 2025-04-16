trip_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = 2.60 * puzzles_count
doll_price = 3 * dolls_count
teddy_bear_price = 4.10 * teddy_bears_count
minion_price = 8.20 * minions_count
truck_price = 2 * trucks_count

toy_price = puzzle_price + doll_price + minion_price + truck_price +teddy_bear_price
toys_count = puzzles_count + dolls_count + minions_count + trucks_count +teddy_bears_count
if toys_count >= 50:
    toy_price = toy_price - (toy_price * 0.25)  # 25% discount  (toy_price -= toy_price * 0.25)

final_price = toy_price - (toy_price * 0.10)  # 10% expenses    (toy_price -= toy_price * 0.10)

if final_price >= trip_price:
    left_money = final_price - trip_price
    print(f"Yes! {left_money:.2f} lv left.")
else:
    needed_money = trip_price - final_price
    print(f"Not enough money! {needed_money:.2f} lv needed.")
