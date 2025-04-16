n = int(input())
numbers = []
filtered = []

for i in range(n):
    integer = int(input())
    numbers.append(integer)   # we add the integers in the list of numbers
command = input()    # at the end of the loop we type command (outside of it)
for number in numbers:  # iterating through the list of numbers
    if command == "even":
        if number % 2 == 0:
            filtered.append(number)   # we add to the filtered list
    elif command == "odd":
        if number % 2 != 0:
            filtered.append(number)
    elif command == "positive":
        if number >=0:
            filtered.append(number)
    elif command == "negative":
        if number < 0:
            filtered.append(number)
print(filtered)
