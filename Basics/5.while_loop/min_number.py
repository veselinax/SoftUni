import sys

numbers_count = int(input())
min_size = sys.maxsize   # the first we have is always the smallest until we see what are the rest numbers so for it to be smallest we take it to be smaller than the system max (which is always true)
counter = 0

while counter < numbers_count:
    numbers = int(input())
    counter += 1

    if numbers < min_size:
        min_size = numbers
print(min_size)
