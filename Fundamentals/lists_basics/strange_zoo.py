tail = input()
body = input()
head = input()

meerkaat = [tail, body, head]
meerkaat[0], meerkaat[2] = meerkaat[2], meerkaat[0]  # replacing first and third element
print(meerkaat)
