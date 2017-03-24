"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import itertools

def is_prime(nat):
    for i in range(2, nat):
        if nat % i == 0:
            return False
    return True

def primes():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n = n+1

print sum(itertools.takewhile(lambda x: x < 200000, primes()))
