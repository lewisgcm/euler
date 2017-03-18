"""
There are several ways to write the number 1/2 as a sum of inverse squares using distinct integers.
For instance, the numbers {2,3,4,5,7,12,15,20,28,35} can be used:
In fact, only using integers between 2 and 45 inclusive, there are exactly three ways to do it,
the remaining two being: {2,3,4,6,7,9,10,20,28,35,36,45} and {2,3,4,6,7,9,12,15,28,30,35,36,45}.
How many ways are there to write the number 1/2 as a sum of inverse squares using
distinct integers between 2 and 80 inclusive?
"""
import itertools
from multiprocessing.dummy import Pool as ThreadPool
from mpmath import mp

def is_inverse_sum(numbers):
    """This function checks if the array of integers are an inverse sum of 0.5"""
    return mp.fsum([mp.fdiv(1, (n*n)) for n in numbers]) == 0.5

def generate_possible(max_number):
    """This function will generate a list of unique integer"""
    for num in range(1, max_number+1):
        yield itertools.combinations(range(1, max_number+1), num)

def test_generator_list(d):
    if is_inverse_sum(d):
        print d

for i in generate_possible(45):
    pool = ThreadPool(45)
    pool.map(test_generator_list, i)
