"""
https://www.hackerrank.com/challenges/python-tuples/problem
github.com/ander758/HackerRank

Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).
"""

if __name__ == '__main__':
    n = int('2')
    integer_list = list(map(int, '1 2'.split()))
    _tuple = tuple(integer_list)
    print(hash(_tuple))
