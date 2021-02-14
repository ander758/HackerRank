from random import randrange

"""
hackerrank.com/challenges/python-arithmetic-operators
github.com/ander758/HackerRank

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
"""


def is_in_range(n, n_min, n_max):
    return n_min <= n <= n_max


n = randrange(1, 100, 1)
if n % 2 == 0:
    if is_in_range(n, 6, 20):
        print('Weird')
    else:
        print('Not Weird')
else:
    print('Weird')
