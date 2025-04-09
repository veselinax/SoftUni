change = float(input())

# Преобразуваме сумата в стотинки (умножаваме по 100)
change = round(change * 100)

# Налични монети в стотинки
coins = [200, 100, 50, 20, 10, 5, 2, 1]

# Инициализиране на броя на монетите
coin_count = 0
i = 0

# Докато има остатък за връщане
while change > 0:
    # Използваме колкото можем от текущата монета
    coin_count += change // coins[i]

    # Намаляваме сумата с използваните монети (остатък)
    change = change % coins[i]

    # Преминаваме към следващата монета
    i += 1

# Печатаме минималния брой монети
print(f"{coin_count}")
