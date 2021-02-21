"""
https://www.hackerrank.com/challenges/nested-list/problem
github.com/ander758/HackerRank

Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
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


def second_lowest(arr):
    arr = sort_by_attribute(arr, 1)
    lowest, second, names = arr[0][1], None, []
    for i in arr:
        if second is None:
            if i[1] != lowest:
                second = i[1]
                names.append(i[0])
        elif i[1] == second:
            names.append(i[0])
        else:
            break
    [print(name) for name in sorted(names)]


if __name__ == '__main__':
    arr = []
    names = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']
    scores = [37.21, 37.21, 37.2, 41.0, 39.0]

    for name, score in zip(names, scores):
        arr.append([name, score])
    second_lowest(arr)
