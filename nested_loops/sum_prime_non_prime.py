command = input()

#sum_prime and sum_non_prime are initialized before the loop because these variables are used to accumulate sums \
# across multiple iterations. You want to add to them every time a new prime or non-prime number is encountered. \
# Thus, initializing them before the loop ensures that the sums start from 0 and are updated during each iteration.

sum_prime = 0      # sums are increasing after each iteration thats why initializing before the loop (we want total)
sum_non_prime = 0

while command != "stop":

    number = int(command)

    # is_prime and is_non_prime are initialized inside the loop because for each new number,\
    # you need to reset these flags to ensure you're correctly classifying the current number as prime or non-prime.
    is_prime = False
    is_non_prime = False

    if number < 0:
        print("Number is negative.")
    elif number == 1 or number == 0:  #  0 and 1 are not prime numbers
        is_non_prime = True
    elif number > 1:
        for i in range(2, number):
            if number % i == 0:  #  If divisible by any number other than 1 and itself, it's not prime
                is_non_prime = True
                break        # The break ensures you stop checking once you've found a divisor. (one divisor is enough to stop being prime)
        if not is_non_prime: # If no divisors are found (i.e., is_non_prime is still False after the loop),\
                             # the number is classified as prime (is_prime = True).
            is_prime = True
    if is_prime:
        sum_prime += number
    if is_non_prime:
        sum_non_prime += number
    command = input()       # After processing one number, the program asks for another number. \
                            # This continues until the user enters "stop".
if command == "stop":
    print(f"Sum of all prime numbers is: {sum_prime}")

    print(f"Sum of all non prime numbers is: {sum_non_prime}")