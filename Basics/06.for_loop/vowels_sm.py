text = input().lower()
sum = 0

for i in range(len(text)):
    if text[i] == "a":
        sum += 1
    elif text[i] == "e":
        sum += 2
    elif text[i] == "i":
        sum += 3
    elif text[i] == "o":
        sum += 4
    elif text[i] == "u":
        sum += 5
print(sum)