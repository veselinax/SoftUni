import sys

numbers_count = int(input())
counter = 0
max_number = -sys.maxsize   #max_number, на която задаваме като стойност много малко число, например отрицателната стойност на sys.maxsize

while counter < numbers_count:
    numbers = int(input())
    counter += 1
    if numbers > max_number:  # if the new number is bigger than the max_number till now then our number becomes max
        max_number = numbers
print(max_number)