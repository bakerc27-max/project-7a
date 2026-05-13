# Author: Chloe Baker
# GitHub username: bakerc27_max
# Date: 05/13/2026
# Description: Creates and returns a list of prime numbers up to a provided limit

def list_of_primes_up_to(limit=100):
    """Return a list of prime numbers up to and including limit."""
    
    prime_list = [True] * (limit + 1)
    
    prime_list[0] = False
    prime_list[1] = False

    for index in range(4, limit + 1):
        if index % 2 == 0:
            prime_list[index] = False

    divisor = 3

    while divisor <= limit ** 0.5:
        if prime_list[divisor] == True:
            for index in range(divisor + 1, limit + 1):
                if index % divisor == 0:
                    prime_list[index] = False

        divisor = divisor + 1

    prime_numbers = [index for index in range(limit + 1) if prime_list[index] == True]

    return prime_numbers
