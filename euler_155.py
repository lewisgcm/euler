"""
An electric circuit uses exclusively identical capacitors of the same value C.
The capacitors can be connected in series or in parallel to form sub-units,
which can then be connected in series or in parallel with other capacitors or other sub-units to
form larger sub-units, and so on up to a final circuit.

Using this simple procedure and up to n identical capacitors,
we can make circuits having a range of different total capacitances.
For example, using up to n=3 capacitors of 60 F each, we can obtain the following
7 distinct total capacitance values:
"""
import itertools

def posibilities(cap, number):
    return [cap for n in range(1, number+1)] + [1.0/cap for n in range(1, number+1)]

def calculate_capacity(caps):
    return sum(caps)

for i in range(1, 3):
    for caps in itertools.combinations(posibilities(10, i), i):
        print calculate_capacity(caps)
