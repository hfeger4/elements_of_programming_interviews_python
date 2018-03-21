# Given n, return all primes up to and including n.
import math

def generate_primes(n):
    arr = []
    i = 2
    while i <= n:
        if is_prime(i):
            arr.append(i)
        i += 1
    return arr

def is_prime(num):
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        i += 1
    return True


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main("prime_sieve.tsv",
                                              generate_primes)
