first_num = int(input())
second_num = int(input())

for number in range(first_num, second_num +1):
    num_to_str = str(number)
    even_sum = 0  # we want to reset these sums for each number in the range thats why initializing inside the loop
    odd_sum = 0
    for index, digit in enumerate(num_to_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(number, end=" ")

# Initializing variable before or inside of a loop:
# Before the loop: If you want to accumulate(increase/change) or retain(keep) the value across iterations
# Inside the loop: If you want the variable to reset or be independent for each iteration (to start fresh on each iteration)