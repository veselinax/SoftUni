n = int(input())


def perfect_number(num):
    my_sum = 0
    for i in range(1, num):
        if num % i == 0:
            my_sum += i
    if my_sum == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

print(perfect_number(n))