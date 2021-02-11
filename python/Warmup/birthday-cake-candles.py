#!/bin/python3
from random import randrange

"""
print count of highest occuring item in list

input
candles = [4,4,1,3]
output
2

hackerrank.com/challenges/birthday-cake-candles/
"""


def birthdayCakeCandles(candles):
    candles.sort()
    print(candles)

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

    # arr = [4, 4, 1, 3]
    print(birthdayCakeCandles(arr))
