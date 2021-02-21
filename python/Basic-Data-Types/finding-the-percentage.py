from random import randrange, choice
"""
https://www.hackerrank.com/challenges/finding-the-percentage/problem
github.com/ander758/HackerRank

"""

if __name__ == '__main__':
    n = 3
    student_marks = {
        'Krishna': [67.0, 68.0, 69.0],
        'Arjun': [70.0, 98.0, 63.0],
        'Malika': [52.0, 56.0, 60.0]
    }
    query_name = choice(list(student_marks))
    avg = sum(student_marks.get(query_name)) / len(student_marks.get(query_name))
    print(format(avg, '.2f'))
