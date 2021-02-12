#!/bin/python3
"""
www.hackerrank.com/challenges/capitalize
"""


def solve(s):
    for word in s.split():
        s = s.replace(word, word.capitalize())
    return s


if __name__ == '__main__':
    s = 'chris alan'
    result = solve(s)
    print(result)
