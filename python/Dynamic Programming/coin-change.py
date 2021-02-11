#!/bin/python3
"""
TODO: Complete this
https://www.hackerrank.com/challenges/coin-change
"""


def getWays(n, coins):
    count = 0

    for coin in coins:
        # 1. Check if given coin == n
        if coin == n:
            count += 1
            continue
        else:
            # 2. Check if given coin*x == n
            for i in range(2, n + 1):
                now = coin * i
                if now == n:
                    count += 1
                    continue
                elif now > n:
                    continue



    # for i in range(0, len(coins)):
    #     # 1. Check if i is same as n
    #     if coins[i] == n:
    #         count += 1
    #     else:
    #         # 2. Check if i*n times =n TODO Delete when 3. finished
    #         for k in range(2, n+1):
    #             if coins[i] * k == n:
    #                 count += 1
    #     # 3. Check possible sums with different coins
    #     for k in range(2, len(coins) + 1):
    #         arr = [0]*k
    #         print(arr)

    print(count)


    """
    1. Check for addition of same
    2. Check for addition of other
    3. Check for individual
    """


if __name__ == '__main__':
    n = 3
    c = [8, 3, 1, 2]
    getWays(n, c)

    ways = [0]*(n+1)
    print(ways)