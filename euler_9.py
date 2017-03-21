"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math

def hypotenuse(x, y):
    return math.sqrt((x*x) + (y*y))

def is_pythagorean_triplet(x, y):
    hyp = hypotenuse(x, y)
    if x < y and y < hyp and hyp.is_integer():
        return True
    return False

for i in range(1, 400):
    for j in range(1, 400):
        if is_pythagorean_triplet(i, j):
            hyp = hypotenuse(i, j)
            if hyp + i + j == 1000:
                print str(i) + "^2 + " + str(j) + "^2 = " + str(int(hyp)) + "^2"
