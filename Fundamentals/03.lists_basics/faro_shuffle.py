cards = input().split(" ")
shuffle_count = int(input())

mid = len(cards) // 2
for shuffle in range(shuffle_count):
    result = []
    for i in range(mid):
        result.append(cards[i])  #  first_half = cards[:mid] everything until mid
        result.append(cards[i+mid])  # second_half = cards[mid:] everything after mid
    cards = result
print(result)