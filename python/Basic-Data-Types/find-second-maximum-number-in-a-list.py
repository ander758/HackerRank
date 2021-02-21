"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
github.com/ander758/HackerRank

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
"""

def runner_up(arr):
    arr.sort()
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != arr[-1]:
            print(arr[i])
            break


if __name__ == '__main__':
    n = 5
    arr = [2, 3, 6, 6, 5]
    runner_up(arr)
