#!/bin/python3
from random import randrange

"""
hackerrank.com/challenges/birthday-cake-candles/
github.com/ander758/HackerRank
"""


def birthdayCakeCandles(candles):
    candles.sort()

    dct = {}
    for n in candles:
        if str(n) in dct:
            dct[str(n)] += 1
        else:
            dct[str(n)] = 1

    max_value = -1
    for key in dct:
        if dct.get(key) > max_value:
            max_value = dct.get(key)
    return max_value


if __name__ == '__main__':
    arr = []
    for i in range(0, randrange(5, 10, 1)):
        arr.append(randrange(1, 10, 1))

    print(birthdayCakeCandles(arr))
