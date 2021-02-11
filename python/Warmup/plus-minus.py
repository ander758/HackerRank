#!/bin/python3
"""
www.hackerrank.com/challenges
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
"""


# Complete the plusMinus function below.
def plusMinus(arr):
    print(f'{sum(n>0 for n in arr)/len(arr):.6f}')
    print(f'{sum(n<0 for n in arr)/len(arr):.6f}')
    print(f'{sum(n==0 for n in arr)/len(arr):.6f}')

if __name__ == '__main__':
    arr = [1, 1, 0, -1, -1]

    plusMinus(arr)
