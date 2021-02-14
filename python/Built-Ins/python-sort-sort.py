"""
www.hackerrank.com/challenges/python-sort-sort/
github.com/ander758/HackerRank

"""


def sort_by_attribute(arr, attribute_index):
    arr_sorted = []
    while arr:
        minimum = arr[0]
        for i in range(0, len(arr)):
            if arr[i][attribute_index] < minimum[attribute_index]:
                minimum = arr[i]
        arr_sorted.append(minimum)
        arr.remove(minimum)
    return arr_sorted


if __name__ == '__main__':
    n = 5  # num of arrays
    m = 3  # num of attributes
    arr = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
    k = 1  # attribute-index to sort by -> arr[i][k]

    for element in sort_by_attribute(arr, k):
        print(' '.join(list(map(str, element))))
