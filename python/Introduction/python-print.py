from random import randrange

"""
hackerrank.com/challenges/python-print
"""


def get_faculty(n):
    str_out = ''
    for i in range(1, n + 1):
        str_out += str(i)
    return str_out


n = randrange(1, 150, 1)
print(n)
print(get_faculty(n))
