n = int(input())
is_prime = True

if n == 1 or n == 0:
     is_prime = False  # Numbers less than or equal to 1 are not prime
elif n > 1:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False # If n is divisible by any number other than 1 and itself
            break
if is_prime:  # If no divisors were found, it's prime
    print(is_prime)  # True
else:
    print(is_prime)  # False

