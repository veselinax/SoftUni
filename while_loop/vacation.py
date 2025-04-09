needed_money = float(input())
money = float(input())

spending = 0
days = 0


while money < needed_money and spending < 5:
    command = input()
    amount = float(input())
    days +=1
    if command == "save":
        money += amount
        spending = 0      # we have to put spending =0 when we have save so the program can count only 5 spendings in a row
    if command == "spend":
        spending +=1
        money -= amount
        if money < 0:
            money = 0
if spending == 5:
    print(f"You can't save the money.")
    print(f"{days}")
if money >= needed_money:
    print(f"You saved the money for {days} days.")