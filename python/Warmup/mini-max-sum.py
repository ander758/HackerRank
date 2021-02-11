#!/bin/python3

from random import randrange

"""
Example
arr=[1,3,5,7,9]
--> minSum = 1+3+5+7=16
--> maxSum = 3+5+7+9=24
Output:
16 24
"""

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()

    lower = 0
    for i in range(0, len(arr)-1):
        lower += arr[i]

    higher = 0
    for i in range(1, len(arr)):
        higher += arr[i]

    print(f'{lower} {higher}')



if __name__ == '__main__':
    arr = []
    for i in range(0, randrange(5, 10, 1)):
        arr.append(randrange(1, 10, 1))

    miniMaxSum(arr)
