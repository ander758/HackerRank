"""
www.hackerrank.com/challenges/diagonal-difference

print absolute diagonal difference in matrix-array
"""


def calculate_diagonal_diff(arr):
    tl_rb = 0
    tr_bl = 0
    for i in range(0, len(arr)):
        tl_rb += arr[i][i]
        tr_bl += arr[i][len(arr[i]) - 1 - i]
    return abs(tl_rb - tr_bl)

c
if __name__ == '__main__':
    arr = [[1, 2, 3],
           [4, 5, 6],
           [9, 8, 9]]

    print(calculate_diagonal_diff(arr))
