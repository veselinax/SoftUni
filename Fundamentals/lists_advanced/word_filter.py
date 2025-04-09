text = input().split()
filtered = [word for word in text if len(word) % 2 == 0]

for f in filtered:
    print(f)