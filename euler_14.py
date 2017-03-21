"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers
finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def step(nat):
    while nat > 1:
        yield nat
        if nat % 2 == 0:
            nat = nat/2
        else:
            nat = (3*nat)+1

def create_chain(start):
    return list(step(start)) + [1]

max_l = 0
max_n = 0
for i in range(1, 1000001):
    l = len(create_chain(i))
    if l > max_l:
        max_l = l
        max_n = i

print max_l
print max_n
