"""
A palindromic number reads the same both ways.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrom(x):
    return str(x) == str(x)[::-1]

max = 0
for i in range(100, 999):
    for j in range(100, 999):
        if is_palindrom(i*j) and i*j > max:
            max = i*j

print max
