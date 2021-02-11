#!/bin/python3
"""
www.hackerrank.com/challenges/grading
"""


def gradingStudents(arr):
    # Write your code here
    for i in range(0, len(arr)):
        n = arr[i]
        if n > 40 - 3:
            if n % 5 == 4:
                arr[i] += 1
            elif n % 5 == 3:
                arr[i] += 2
    return arr


if __name__ == '__main__':
    grades = [73, 67, 38, 33]

    for grade in gradingStudents(grades):
        print(grade)
