"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

def is_prime(prime):
    for i in range(2, prime):
        if prime % i == 0:
            return False
    return True

NTH_PRIME = 10001

x = 2
n = 0
last_prime = 0
while n < NTH_PRIME:
    if is_prime(x):
        last_prime = x
        n = n+1
    x=x+1

print last_prime