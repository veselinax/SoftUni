numbers = input().split(", ")
indices = []

for num in range(len(numbers)):
    if int(numbers[num]) % 2 == 0:  # its a string so we transform to int
        indices.append(num)
print(indices)