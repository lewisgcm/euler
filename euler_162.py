"""
In the hexadecimal number system numbers are represented using 16 different digits:

0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
The hexadecimal number AF when written in the decimal number system equals 10x16+15=175.

In the 3-digit hexadecimal numbers 10A, 1A0, A10, and A01 the digits 0,1 and A are all present.
Like numbers written in base ten we write hexadecimal numbers without leading zeroes.

How many hexadecimal numbers containing at most sixteen hexadecimal digits exist with
 all of the digits 0,1, and A present at least once?
Give your answer as a hexadecimal number.

(A,B,C,D,E and F in upper case, without any leading or trailing code that marks the
number as hexadecimal and without leading zeroes , e.g.
1A3F and not: 1a3f and not 0x1a3f and not $1A3F and not #1A3F and not 0000001A3F)
"""
import itertools

#Number will start at 0000000000000000 and end at FFFFFFFFFFFFFFFF
#Must contain 0,1 and A atleast once
#Only interested in combinations that DO contain 0, 1 and A
#So first find only numbers that contain 0, 1 and A once
#then for each such that A10FFFFFFFFFFFFF could be 1 * (all possible comibinations of FFFFFFFFFFFFF)
#A10, A01, 1A0, 10A, 0A1, 01A
#sum = 0
#for i in itertools.permutations('A10FFFFFFFFFFFFF', 16):
#    sum = sum + (16**13)
#print sum
#print (16**16) - ((6) * 16**13)
#All possible combinations = 16*16
print 16**16
print 4420408745587516162
