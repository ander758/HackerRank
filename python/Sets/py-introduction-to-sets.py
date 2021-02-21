"""
https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
github.com/ander758/HackerRank

Print average using set
"""


# your code goes here
def average(array):
    return sum(set(array)) / len(set(array))


if __name__ == '__main__':
    n = 10
    arr = list(map(int, '161 182 161 154 176 170 167 171 170 174'.split(' ')))
    result = average(arr)
    print(result)
