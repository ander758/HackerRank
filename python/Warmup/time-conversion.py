#!/bin/python3


from random import randrange

"""
Convert AM/PM to 24hr format

input= '12:01:00PM' -> output= 12:01:00
input= '12:01:00AM' -> output= 00:01:00

hackerrank.com/challenges/time-conversion/
"""


def timeConversion(s):
    hh = s[:-8]

    if 'AM' in s:
        if hh == '12':
            hh = 0
    elif 'PM' in s:
        if hh != '12':
            hh = str(int(hh) + 12)

    return f'{hh if len(str(hh)) > 1 else str(0) + str(hh)}:{s[3:-2]}'


if __name__ == '__main__':
    arr = ['12:01:00PM', '12:01:00AM']
    print(f'output={timeConversion(arr[randrange(0, len(arr), 1)])}')
