import math

party_size = int(input())
days = int(input())
coins = 0

for i in range(1, days+ 1):
    if i % 10 == 0:
        party_size -= 2
    if i % 15 == 0:
        party_size += 5
    coins += 50
    coins -= 2 * party_size
    if i % 3 == 0:   # every third day
        coins -= 3 * party_size
    if i % 5 == 0:
        coins += 20 * party_size
        if i % 3 == 0:
            coins -= 2 * party_size
print(f"{party_size} companions received {math.floor(coins/party_size)} coins each.")
# we want coins for each party member so we divide them
# if we have 14.666 coins we use math floor so we get 14 not round to get 15