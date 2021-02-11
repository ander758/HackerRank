#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the fairRations function below.
def fairRations(n, arr):
    sum = 0
    for i in arr:
        sum += i
    if sum/n % 2 == 0:
        return int(sum/n)
    else:
        return 'NO'

if __name__ == '__main__':
    n = 4
    arr = [2, 3, 4, 5, 6]

    print(fairRations(n, arr))
