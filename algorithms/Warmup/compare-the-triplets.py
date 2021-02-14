"""
https://www.hackerrank.com/challenges/compare-the-triplets
github.com/ander758/HackerRank
"""


def compareTriplets(a, b):
    points = [0, 0]
    for i_a, i_b in zip(a, b):
        if i_a > i_b:
            points[0] += 1
        elif i_b > i_a:
            points[1] += 1
    return points


if __name__ == '__main__':
    a = [5, 6, 7]
    b = [3, 6, 10]
    print(compareTriplets(a, b))
