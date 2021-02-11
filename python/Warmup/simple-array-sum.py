#!/bin/python3
from random import randrange, randint

"""
www.hackerrank.com/challenges/simple-array-sum
"""


def simpleArraySum(arr):
    sum = 0
    for n in arr:
        sum += n
    return sum

if __name__ == '__main__':
    arr = []
    for i in range(1, randint(1, 1000)):
        arr.append(i)
    print(simpleArraySum(arr))
