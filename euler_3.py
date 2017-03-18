"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def is_factor(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

HAYSTACK = 13195
for i in range(2, HAYSTACK):
    if HAYSTACK % i == 0 and is_factor(i):
        print i
