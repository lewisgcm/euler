"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...')
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18.
It is not possible to try every route to solve this problem, as there are 2^99 altogether!
"""

TRIANGLE = list([])

#Load triangle into memory
with open('euler_67.txt', 'r') as triangleFile:
    for line in triangleFile:
        TRIANGLE.append([int(i) for i in line.replace("\n", "").split(" ")])

#Start with bottom +1 of triangle and apply sub solution a + max(b,c)
for y in range(len(TRIANGLE)-1, -1, -1):
    for x in range(0, len(TRIANGLE[y])-1):
        TRIANGLE[y-1][x] = TRIANGLE[y-1][x] + max(TRIANGLE[y][x], TRIANGLE[y][x+1])

print TRIANGLE[0][0]
