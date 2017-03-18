"""
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def evenly_divsable_by(digit, n_range):
    for i in n_range:
        if digit % i != 0:
            return False
    return True

n = 1
while not evenly_divsable_by(n, range(1, 21)):
    n = n+1
print n
