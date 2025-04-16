# import math
#
# num1 = float(input())
# num2 = float(input())
# num3 = float(input())
#
# def multiplication_sign(a,b,c):
#     product = a * b * c
#     if product == 0:
#         return "zero"
#     elif product > 0:
#         return "positive"
#     elif product < 0:
#         return "negative"
#
# print(multiplication_sign(num1,num2,num3))


def check_product_sign(num1, num2, num3):
    # Check if any number is zero
    if num1 == 0 or num2 == 0 or num3 == 0:
        print("zero")
        return

    # Count how many numbers are negative
    negative_count = sum(1 for num in [num1, num2, num3] if num < 0)

    if negative_count % 2 == 0:
        print("positive")
    else:
        print("negative")


# Input: Read the numbers
num1 = int(input())
num2 = int(input())
num3 = int(input())

# Check and print the result
check_product_sign(num1, num2, num3)
