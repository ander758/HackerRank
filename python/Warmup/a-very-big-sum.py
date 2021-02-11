"""
www.hackerrank.com/challenges/a-very-big-sum
input=
5
1000000001 1000000002 1000000003 1000000004 1000000005
output=
5000000015
"""


def calculate_sum(arr):
    return sum(arr)


if __name__ == '__main__':
    arr = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    print(calculate_sum(arr))
