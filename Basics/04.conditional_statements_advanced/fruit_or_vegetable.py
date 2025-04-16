product = input()

if product == "banana" or product == "apple" or product == "kiwi" \
        or product == "cherry" or product == "lemon" or product == "grapes":  # we can continue on the down line the same long line with \
    print("fruit")
elif product == "tomato" or product == "cucumber" \
        or product == "pepper" or product ==  "carrot":
    print("vegetable")
else:
    print("unknown")